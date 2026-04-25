# Architecture as Code (AaC) for CAF and Zero Trust
*A proposal for an Open Standard*

> **For the full whitepaper with representation profiles, drift detection, validation semantics, and detailed examples, see [Whitepaper](whitepaper.md).**

## Core hypothesis

It should be possible to transform architecture from descriptive guidance into a structured, machine‑readable, and partially enforceable model.

## Initial motivation

Infrastructure as Code solved deployment reproducibility, but did not solve the architectural gap between:

- intent
- decisions
- implementation
- validation

AaC attempts to create a bridge between these layers.

## Initial focus

The first focus area is Security Architecture because it provides:

- stronger structure
- clearer constraints
- better traceability
- higher validation value

## Core conceptual chain

A central chain in the model is:

> Risk → Control → Constraint → Implementation → Signal → Validation

This allows the model to connect architecture with deployed reality and verification.

**Example:**
- Risk: Privilege escalation via compromised admin endpoint
- Control: Privileged Access Workstation (PAW)
- Constraint: Admin roles require compliant devices
- Implementation: Azure VM with tag `role: PAW`
- Signal: Entra ID sign‑in logs, Conditional Access logs
- Validation: Check that the VM exists and has the required tag

## Requirements as first‑class citizens

In regulated industries, architecture is driven by **requirements** from contracts, compliance frameworks, and stakeholders. AaC treats requirements as explicit model elements with **verification criteria** and **failure conditions**, linking them directly to controls and implementation. This turns compliance from a manual audit exercise into an automated, machine‑checked process. See the whitepaper for details.

## Human and machine representation

Architecture exists in two complementary forms:

1. **Structured model** – for processing, validation, and automation (YAML/JSON)
2. **Human‑readable documentation** – generated views of the same model, augmented with explanatory commentary

The model is canonical. Documents are derived projections. Commentary explains, but must not replace canonical facts.

## Template direction

A practical starting point is to define architecture templates based on Microsoft guidance such as:

- CAF landing zones
- Zero Trust identity patterns
- PAW / privileged access controls
- Key Vault boundary patterns
- Conditional Access and PIM requirements

## Possible future directions

- architecture‑to‑IaC traceability
- baseline IaC generation from structured architecture
- drift detection
- compliance templates
- open template ecosystem
- extension from security architecture to broader infrastructure architecture

## Relationship to existing Microsoft capabilities

The solution does **not** replace:
- Azure Policy
- Microsoft Defender for Cloud
- Microsoft Cloud Security Benchmark

Instead, it:
- references them
- structures them
- connects them to architecture decisions and IaC

## Open Standard ambition

This proposal is not tied to a specific vendor, tool, or methodology.

The goal is to create an **Open Standard** for Architecture as Code that can be:
- implemented by any organisation
- rendered into any documentation format
- validated against any IaC tool (initially Terraform, later others)

All contributions — to the model, the schema, or the validator — are welcome under the MIT license.

## Representation layer

The architecture model is independent from its textual representation.

Different representation profiles can render the same model using:
- different terminology
- different document structures
- organisation‑specific formats

The initial implementation includes a single neutral representation.

## Coverage and completeness control

The system tracks which elements of the architecture model are represented in each document view.

Elements not included in a representation must be:
- explicitly excluded
- or marked as not yet represented

This ensures no architectural decisions or controls are silently omitted.
