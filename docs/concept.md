# Architecture as Code (AaC) for CAF and Zero Trust
*A proposal for an Open Standard*

> **For the full whitepaper with representation profiles, drift detection, validation semantics, and detailed examples, see [Whitepaper](whitepaper.md).**

---

## Core hypothesis

It should be possible to transform architecture from descriptive guidance into a structured, machine-readable, and partially enforceable model.

## Initial motivation

Infrastructure as Code solved deployment reproducibility, but did not solve the architectural gap between:

- architectural intent
- decisions
- implementation
- validation

AaC attempts to create a bridge between these layers.

## Initial focus

The first focus area is **Security Architecture**, because it provides:

- stronger structure
- clearer constraints
- better-defined control boundaries
- higher validation value

This makes it a practical and realistic starting point for Architecture as Code.

## Core conceptual chain

A central chain in the model is:

> **Risk → Control → Constraint → Implementation → Signal → Validation**

This chain connects architectural intent with deployed reality and observable verification.

Signals represent observable evidence (state, logs, policy results) that is used as input for validation.

---

### Example

- **Risk:** Privilege escalation via compromised admin endpoint  
- **Control:** Privileged Access Workstation (PAW)  
- **Constraint:** Admin roles require compliant devices  
- **Implementation:** Azure VM with tag `role: PAW`  
- **Signal:** Entra ID sign-in logs, Conditional Access logs  
- **Validation:** Verify that the VM exists, is tagged correctly, and participates in enforced access policies  

The model allows validation results to be interpreted in an architectural context rather than at a single-resource level.

---

## Requirements as first-class citizens

In regulated industries, architecture is driven by **requirements** originating from contracts, compliance frameworks, and stakeholder obligations.

AaC treats requirements as explicit model elements with:

- verification criteria
- failure conditions
- traceable links to controls and implementation

This transforms compliance from a manual, document-based activity into a structured and machine-checkable process.

See the whitepaper for detailed schema and examples.

---

## Human and machine representation

Architecture exists in two complementary forms:

1. **Structured architecture model**  
   Canonical, machine-readable representation (YAML/JSON) used for validation and analysis.

2. **Human-readable documentation**  
   Generated views of the same model, augmented with explanatory commentary.

The model is canonical.  
Documents are derived projections.  
Commentary explains architecture, but must not replace canonical facts.

---

## Template direction

A practical starting point for adoption is to define reusable architecture templates based on established Microsoft guidance, such as:

- CAF landing zones
- Zero Trust identity patterns
- Privileged Access Workstation (PAW) controls
- Key Vault boundary patterns
- Conditional Access and PIM requirements

These templates provide a concrete entry point while preserving architectural intent and traceability.

## Possible future directions

Potential evolution paths include:

- architecture-to-IaC traceability
- baseline IaC generation from structured architecture
- drift detection between model and implementation
- reusable compliance templates
- an open template ecosystem
- extension beyond security architecture to broader infrastructure domains

These are future possibilities, not current assumptions.

---

## Relationship to existing Microsoft capabilities

The AaC approach does **not** replace existing Microsoft capabilities such as:

- Azure Policy
- Microsoft Defender for Cloud
- Microsoft Cloud Security Benchmark

Instead, it:

- references them as implementation evidence
- structures them within an architectural model
- connects them to risks, controls, and constraints
- aggregates their outputs into architectural understanding

---

## Open Standard ambition

This proposal is not tied to a specific vendor, tool, or methodology.

The intent is to define a **vendor-neutral, methodology-agnostic canonical model** that specifies semantics and structure, not a mandatory implementation or governing body.

An Architecture as Code standard should be:

- implementable by any organization
- renderable into any documentation format
- verifiable against any IaC system (initially Terraform, later others)

All contributions—to the model, schema, examples, or validation logic—are welcome under the MIT license.

---

## Representation layer

The architecture model is independent of its textual representation.

Different representation profiles may render the same model using:

- different terminology
- different document structures
- organization-specific formats

The initial implementation includes a single, neutral representation profile.

---

## Coverage and completeness control

The system tracks which elements of the architecture model are represented in each document view.

Elements not included in a representation must be:

- explicitly excluded, or
- marked as not yet represented

This ensures that no architectural decisions, risks, or controls are silently omitted.
