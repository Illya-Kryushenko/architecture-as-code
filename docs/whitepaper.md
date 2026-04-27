# Architecture as Code for Cloud Adoption Framework and Zero Trust

## Document Status

**Status:** Conceptual proposal / Reference architecture  
**Audience:** Enterprise Architects, CTO, CISO, Architecture Governance Boards, System Integrators  
**Scope:** Architecture modeling, traceability, and validation of intent against implementation  

---

## Executive Summary

Modern cloud environments rely heavily on Infrastructure as Code (IaC) to define and deploy systems with precision. At the same time, architectural intent, risk considerations, and compliance obligations are documented separately through architectural frameworks such as the Microsoft Cloud Adoption Framework (CAF) and Zero Trust. Over time, these two worlds drift apart.

This paper proposes **Architecture as Code (AaC)** as a canonical, machine-readable architecture model that connects architectural intent—requirements, risks, and controls—to implementation and observable evidence. The goal is not to replace existing tooling, but to introduce a missing architectural intelligence layer that enables verification, traceability, and portability of architecture.

The initial implementation scope focuses deliberately on:
- CAF and Zero Trust as anchor frameworks
- Security architecture as the first domain
- Consistency and drift detection between architecture models and Terraform-managed infrastructure

---

## Motivation and Problem Definition

Modern cloud architectures are increasingly defined using Infrastructure as Code (IaC) technologies such as Terraform and Bicep. IaC provides a precise, reproducible description of deployed systems. However, it does not explain **architectural intent**—why the system is built in a certain way.

Conversely, architectural frameworks such as Microsoft Cloud Adoption Framework (CAF) and Zero Trust provide structured guidance but remain largely descriptive. They exist as documents, recommendations, and reference architectures rather than executable or verifiable models.

This results in a structural gap between:
- architectural intent
- architectural guidance
- implementation in IaC
- deployed reality

Over time, organizations experience architectural drift, weak traceability, audit friction, and manual validation processes that rely heavily on expert interpretation rather than observable evidence.

A second, strategic gap also exists: **architecture is not portable**. Architectural knowledge is trapped in documents, slide decks, and templates that cannot be reused, rendered, or transferred across organizations and methodologies without reinterpretation.

---

## Scope and Non‑Goals

### In Scope

- Canonical architecture modeling of intent
- Traceability from requirements and risks to implementation
- Validation and drift detection against observable implementation
- Architecture portability across representation formats

### Non‑Goals

- Not a replacement for Azure Policy, Microsoft Defender, or GRC platforms
- Not a full compliance automation platform
- Not a full Infrastructure as Code generator (initially)
- Not an enforcement engine

### Relationship to Policy-as-Code

Policy engines (OPA, Sentinel, Azure Policy) evaluate and enforce rules.  
Architecture as Code defines **why those rules exist**, how they map to architectural controls, and how enforcement relates back to architectural risk and intent.

---

## Core Concept: Canonical Architecture Model

Architecture is represented as a **structured canonical model**, not static documentation. This model captures intent, constraints, decisions, and mappings to implementation.

The core executable chain of the model is:

> **Risk → Control → Constraint → Implementation → Validation**

Requirements provide an alternative entry point, enabling both:
- risk‑first (security-driven) architectures
- requirement‑first (compliance-driven) architectures

From the canonical model, multiple artifacts can be derived:
- human‑readable documents
- validation logic
- coverage and completeness reports
- implementation scaffolding (future)

Validation aggregates observable evidence upward from implementation to control and risk levels, enabling architecture‑level insight rather than isolated configuration checks.

---

## Minimum Semantic Contract

To ensure that the model remains canonical and not just “structured YAML,” the following semantic contract applies.

### Core Element Types

- **Requirement**
- **Risk**
- **Control**
- **Constraint**
- **ImplementationMapping**
- **ValidationRule**
- **Evidence**

### Mandatory Relationships

- A **Requirement** must map to one or more Controls
- A **Risk** must map to one or more Controls
- A **Control** may define one or more Constraints
- A **Control or Constraint** must map to at least one ImplementationMapping within executable scope
- A **ValidationRule** must reference observable Evidence

### Invariants

- Representation profiles must not change canonical meaning
- Every model element must be either represented or explicitly excluded in a given view
- Validation must reference observable signals (state, logs, policy results)

---

## Requirements as First‑Class Citizens

In regulated environments, architecture is often driven by external requirements originating from contracts, regulatory frameworks, or non‑functional constraints. Traditional documents capture these requirements, but their link to implementation is fragile.

In AaC, requirements are first‑class model elements with explicit verification semantics.

### Requirement Model

| Field | Description |
|------|-------------|
| `id` | Unique identifier |
| `description` | Human-readable statement |
| `source` | Contract, regulation, decision |
| `type` | Security, compliance, functional |
| `verification_criteria` | Condition proving satisfaction |
| `failure_condition` | Condition indicating violation |
| `control_mapping` | Controls implementing the requirement |
| `implementation_mapping` | Optional direct linkage |

---

## Evidence and Validation Semantics

Validation in AaC is evidence‑driven, not configuration‑driven.

### Evidence Model

| Field | Description |
|------|-------------|
| `id` | Evidence identifier |
| `source_type` | Terraform state, logs, policy results |
| `query` | Query or selector for evidence |
| `evaluation_window` | Time scope for evaluation |
| `confidence` | Confidence level of evidence |
| `last_observed` | Timestamp of last observation |
| `raw_reference` | Pointer to source data |

### Aggregation Semantics

- **Implementation level:** PASS / FAIL / MISSING
- **Control level:** PASSED / INCOMPLETE / FAILED
- **Risk level:** MITIGATED / EXPOSED

Evidence gaps are explicitly represented as:
- `external_control`
- `manual_implementation_required`
- `not_yet_automated`

---

## Human vs Machine Representation

The canonical architecture model is the single source of truth.

Human‑readable documents are **derived views**, composed of:
- structured, generated architectural content
- human-authored commentary

Structured content defines architecture.  
Commentary explains architecture.

---

## Representation Profiles and Coverage Control

To support portability, the model separates **semantics from representation**.

### Layers

- **Canonical Layer:** Structured model
- **Representation Layer:** Profiles defining terminology and structure
- **Output Layer:** Concrete artifacts (HLD, LLD, audit packages)

Profiles may:
- reorder sections
- rename terminology
- filter elements

Profiles must not change meaning.

Coverage control ensures that:
- omissions are explicit
- nothing disappears silently between views

---

## Drift Detection and Two‑Way Consistency

Architecture defines intent. Implementation evolves.

The system supports:
1. **Model → IaC consistency checks**
2. **IaC → Model completeness checks**
3. **Selective overrides with expiration**

Terraform state is used as the primary observable source in the initial implementation.

---

## End‑to‑End Example: Privileged Access Architecture

**Scenario:** Zero Trust privileged access using PAW, Conditional Access, and PIM.

- Risk: Privilege escalation via compromised admin endpoint
- Control: Privileged Access Workstation
- Constraints: Compliant devices, PIM enforcement
- Evidence: Sign‑in logs, Conditional Access logs

Output:
- control status
- risk exposure status
- coverage report

---

## Initial Implementation and MVP Scope

### Model Scope

- Azure resources
- Azure Policy
- Management groups
- RBAC
- Core security controls

### Executable Validation Scope

- Terraform‑managed Azure resources

### Excluded (modeled, not automated)

- Conditional Access
- PIM
- Graph API configurations
- Microsoft 365 Security

Initial focus is **model ↔ Terraform consistency**, not generation.

---

## Relationship with Existing Microsoft Capabilities

Azure Policy, Defender for Cloud, and security benchmarks provide enforcement and evaluation.  
AaC provides **architectural intent, traceability, and aggregation** above them.

---

## Strategic Value

- Portable architecture as an asset
- Cross‑organizational handover
- Subcontractor integration
- Methodology independence (CAF, TOGAF, internal standards)

---

## Conclusion

Architecture as Code introduces a shift from static documentation to a living, structured, and verifiable architectural model.

By deliberately constraining scope and building on existing tooling, the approach delivers immediate value while remaining extensible. The long‑term ambition is a portable, vendor‑neutral, methodology‑agnostic format for architectural knowledge that preserves intent, enables validation, and prevents silent drift.
