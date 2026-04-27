## Architecture as Code — Common Questions and Objections

### Is this just Policy-as-Code?

No.

Policy engines (e.g., OPA, Azure Policy, Sentinel) evaluate whether specific configurations comply with defined rules.

Architecture as Code operates at a different level. It:

- defines architectural intent (risk, control, constraint)
- links that intent to implementation
- interprets validation results in an architectural context

Policy-as-Code answers:

> "Is this configuration compliant?"

Architecture as Code answers:

> "What does this mean for architectural risk and control effectiveness?"

---

### Isn’t this overengineering?

The model is intentionally **complete**, but not intended to be **fully applied everywhere**.

Architecture as Code does not require:

- modeling every component
- replacing existing processes
- introducing a new framework across the entire organization

Instead, it allows **selective application**, starting from areas where:

- architectural risk is high
- validation is difficult
- drift is common

> The model is complete by design, but intentionally applied selectively.

---

### Who creates and maintains the model?

The model does not introduce new architectural knowledge.  
It formalizes knowledge that already exists in:

- architecture documents
- design decisions
- security requirements
- compliance controls

The key shift is not **who writes architecture**, but:

> how architecture becomes verifiable and traceable

Model creation and maintenance should be aligned with existing architecture governance processes, not replace them.

---

### How is this different from compliance tooling?

Compliance frameworks (ISO, NIST, benchmarks) define:

- controls
- requirements
- checklists

They are typically:

- static
- periodic
- audit-driven

Architecture as Code introduces:

- continuous validation against implementation
- explicit traceability from requirement → control → implementation
- aggregation of validation results to architectural outcomes

> It moves from checklist compliance to continuous architectural verification.

---

### Does this work outside of security architecture?

The initial scope is intentionally focused on **security architecture**, because:

- the structure is well-defined
- relationships between risk, control, and implementation are clearer
- validation signals are more readily available

Generalization to other domains (e.g., business logic, distributed systems) is possible, but not assumed.

> Expansion is a future step, not a design assumption.

---

### Is validation reliable if evidence is incomplete?

Validation in AaC is **evidence-driven**, not absolute.

The model explicitly represents uncertainty through:

- evidence sources
- confidence levels
- external or non-automated controls

This means:

- incomplete visibility is modeled, not ignored
- validation results are interpreted with context

> The goal is not perfect certainty, but transparent and explainable evaluation.

---

### Why not rely on Terraform or IaC alone?

Terraform describes the **current state of infrastructure**, but it does not:

- express architectural intent
- explain why resources are configured in a certain way
- link implementation to risk or control objectives

Architecture as Code introduces a layer that connects:

- intent (risk, requirement, control)
- implementation (IaC)
- validation (observed state)

> IaC shows what exists. AaC explains what it means.

---

### How does this scale in large environments?

Scaling is primarily a **tooling and implementation concern**, not a modeling limitation.

The model defines:

- semantics
- relationships
- validation logic

Practical scaling strategies may include:

- partial model coverage
- domain-specific views
- incremental validation
- selective control modeling

> The model defines meaning; tooling defines scale.

---

### How are conflicts or changes handled?

Architecture and implementation naturally diverge over time.

AaC supports this through:

- drift detection (model → implementation)
- completeness checks (implementation → model)
- explicit overrides with expiration (temporary exceptions)

> Divergence is expected, but must be visible and controlled.

---

### How is this different from architecture documentation?

Traditional architecture documentation:

- is descriptive
- becomes outdated
- is difficult to verify

Architecture as Code:

- is structured and machine-readable
- supports validation against real systems
- separates canonical data from human-readable representation

> Documentation becomes a view of the model, not the source of truth.

---

### Is this meant to replace existing tools?

No.

Architecture as Code is designed to **sit above existing tools**, not replace them.

It integrates with:

- IaC (Terraform)
- policy engines (Azure Policy, OPA)
- security tools (Defender)
- compliance frameworks

> It provides the missing architectural layer that connects them.

---

### What is the end goal?

The long-term goal is to establish:

- a canonical, portable architecture model
- consistent traceability from intent to implementation
- continuous validation of architectural correctness
- methodology-independent representation (CAF, TOGAF, internal models)

> Architecture becomes a transferable, verifiable asset rather than static documentation.
