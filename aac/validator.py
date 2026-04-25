import json
from .model import ArchitectureModel


def get_nested_attr(obj, path):
    """
    Helper to access nested dictionary keys using dot notation
    (e.g., 'settings.tls_version').
    """
    for key in path.split('.'):
        if isinstance(obj, dict):
            obj = obj.get(key)
        else:
            return None
    return obj


def check_resource_matches_mapping(resource, mapping):
    """
    Checks if a resource from Terraform state matches a single implementation mapping.
    Returns (is_match, error_message).
    """
    # 1. Check resource type
    if resource.get("type") != mapping.resource_type:
        return False, "type mismatch"

    # 2. Check tags
    if mapping.tags:
        tags = resource.get("tags", {})
        for key, expected_value in mapping.tags.items():
            if tags.get(key) != expected_value:
                return (
                    False,
                    f"tag '{key}' mismatch: expected '{expected_value}', got '{tags.get(key)}'"
                )

    # 3. Check parameters
    if mapping.parameters:
        attributes = resource.get("attributes", {})
        for param_path, expected_value in mapping.parameters.items():
            actual_value = get_nested_attr(attributes, param_path)
            if actual_value != expected_value:
                return (
                    False,
                    f"param '{param_path}' mismatch: expected {expected_value}, got {actual_value}"
                )

    return True, "ok"


def check_model_against_terraform_state(model: ArchitectureModel, state_path: str) -> bool:
    """
    Validates an architecture model against a Terraform state file.
    Also provides summaries of control coverage and risk coverage.
    """
    with open(state_path) as f:
        state = json.load(f)

    # Flatten resources from state for easier lookup
    all_resources = []
    for resource in state.get("resources", []):
        for instance in resource.get("instances", []):
            all_resources.append({
                "type": resource["type"],
                "name": resource.get("name", ""),
                "attributes": instance.get("attributes", {}),
                "tags": instance.get("attributes", {}).get("tags", {})
            })

    all_passed = True
    control_mapping_results = {}

    print("--- Mapping Validation ---")
    for mapping in model.implementation_mapping:
        control_mapping_results.setdefault(mapping.control_id, [])

        found = False
        for res in all_resources:
            matches, msg = check_resource_matches_mapping(res, mapping)

            if matches:
                found = True
                control_mapping_results[mapping.control_id].append("PASS")
                print(f"✅ PASS: {mapping.control_id} -> {res['name']} ({mapping.resource_type})")
                break

            # Resource type matched, but one of the checks failed
            if msg != "type mismatch":
                print(f"❌ FAIL: {mapping.control_id} found resource '{res['name']}', but {msg}")
                control_mapping_results[mapping.control_id].append("FAIL")
                all_passed = False
                found = True
                break

        if not found:
            print(f"⚠️  MISSING: {mapping.control_id} (no resource of type {mapping.resource_type} found)")
            control_mapping_results[mapping.control_id].append("MISSING")
            all_passed = False

    covered_control_ids = set()

    print("\n--- Control Coverage Analysis ---")
    for control in model.controls:
        results = control_mapping_results.get(control.id, [])

        if results and all(result == "PASS" for result in results):
            control_status = "COVERED"
            status_icon = "🛡️"
            covered_control_ids.add(control.id)
        elif "FAIL" in results:
            control_status = "FAILED"
            status_icon = "❌"
        elif "MISSING" in results:
            control_status = "MISSING"
            status_icon = "⚠️"
        else:
            control_status = "MISSING"
            status_icon = "⚠️"

        print(f"{status_icon} {control_status} | Control '{control.name}' (ID: {control.id})")

    print("\n--- Risk Coverage Analysis ---")
    for risk in model.risks:
        risk_controls = getattr(risk, "controls", [])

        is_covered = any(
            control_id in covered_control_ids
            for control_id in risk_controls
        )

        status = "🛡️  COVERED" if is_covered else "🚨 EXPOSED"
        print(f"{status} | Risk '{risk.name}' (ID: {risk.id})")

    return all_passed