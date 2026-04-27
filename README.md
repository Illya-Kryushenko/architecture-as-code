# Architecture as Code (AaC)

**Structured architecture models linked to CAF, Zero Trust, and Infrastructure as Code**

---

## Overview

This repository captures the initial concept of transforming architecture from static documentation into a structured, traceable, and partially executable model.

The current starting point is **Microsoft Cloud Adoption Framework (CAF)** and **Zero Trust** guidance. The core idea is to transform architectural guidance into **machine-readable architecture models** that can be linked to:

- architectural intent and decisions  
- Infrastructure as Code  
- validation and drift detection  

The initial focus is **Security Architecture**, where the structure is stronger and the relationships between **risk, control, constraints, and implementation** are clearer.

---

## Repository Positioning and Status

**This repository is not a product, framework, or turn-key tool.**

It represents a **reference architecture and canonical architecture model** for Architecture as Code — an approach to treating architecture as a **structured, first-class, and transferable asset**, rather than static documentation.

The repository serves as:

- a **canonical architecture model proposal**
- a **reference architecture for CAF and Zero Trust**
- a **conceptual and technical foundation** for architecture governance, validation, and traceability
- a **design authority baseline** from which organizations, system integrators, or vendors may build their own tooling, standards, or internal platforms

Tooling, automation, and enforcement are considered **derived concerns**, intentionally secondary to the architectural semantic model.

---

## Problem

Modern cloud environments have a structural gap between:

- architectural intent  
- architectural guidance  
- implementation in IaC  
- deployed reality  

Architecture documents explain *intent*, but become outdated.  
IaC accurately describes *implementation*, but does not express **architectural intent**.

As a result, organizations struggle with:

- architectural drift  
- weak traceability  
- poor alignment between decisions and implementation  
- manual and inconsistent validation of architecture  

---

## Core Idea

The model introduces an **explicit architecture layer above IaC** that links:

- guidance  
- constraints  
- requirements  
- architectural decisions  
- implementation mappings  
- validation rules  

The long-term direction is to move from **architecture as static text** to **architecture as a living, structured, and verifiable model**.

The architecture model becomes the **single semantic source of truth**, from which documentation, validation logic, and derived artifacts are generated.

---

## Initial Direction

The first practical scope focuses on:

- CAF and Zero Trust as **executable architectural templates**
- Security Architecture as the first implementation domain
- human-readable architecture documents generated from a structured model
- support for both **canonical architecture data** and **human commentary**
- early validation against **Terraform state** through a working prototype

Terraform is used as an **observable representation of implemented reality**, not as the authority on architectural intent.

---

## Guiding Principles

- The architecture model is the **primary source of truth**
- Human-readable documents are **generated views** of the model  
- Structured content **defines** architecture  
- Commentary **explains** architecture  
- Commentary must **not replace canonical architectural facts**

---

## Specification

The **Architecture as Code (AaC) model specification** is defined in:

- [`docs/architecture-model.md`](docs/architecture-model.md)
- [Example model](examples/basic-model.yaml) – illustrates risks, controls, and implementation mappings
- [Terraform state example](examples/example.tfstate) – used for validation

The specification includes:

- canonical architectural elements (risks, controls, constraints, implementations)
- required relationships and traceability semantics
- rules for validation and aggregation of results

The specification is versioned and intentionally open to evolution based on feedback and real-world use.

---

## Repository Scope

This repository currently contains:

- concept documents and whitepaper material  
- an evolving Architecture as Code canonical model  
- initial architectural decision records (ADRs)  
- example model representations  
- a working prototype validator  
- early implementation code used to test the concept  

---

## Current Status

### Conceptually defined

- the Architecture as Code concept and rationale  
- a canonical architecture model focused on traceability from:
  - risk → control → constraint → implementation → validation (derived from observable state)
- clear separation between:
  - canonical architecture model  
  - human-readable architectural views  
- early concepts for:
  - representation profiles  
  - coverage and completeness tracking  

### Implemented in the current prototype

- parsing an AaC model from YAML  
- parsing Terraform state from JSON  
- validating:
  - resource types  
  - tags  
  - selected parameters  
  against the architecture model  
- producing validation results via a simple CLI  

### Not yet implemented

- signal-informed risk coverage analysis  
- signal-based validation  
- profile-based document rendering  
- validation beyond the Terraform state scope  
- broader multi-domain support beyond the current example focus  

---

## What You Can Do Today

With the current prototype, you can:

- define a simple architecture model linking risks, controls, and implementation mappings  
- validate Terraform state against that model  
- identify:
  - missing implementations  
  - misconfigured resources  
  - partially implemented controls  
- observe how implementation issues propagate through the architecture model to higher-level outcomes:
  - control status  
  - risk status (e.g. FAILED, INCOMPLETE, EXPOSED)  

A ready-to-use example is provided. Run:
```bash
PYTHONPATH=. python -m aac.cli --model examples/basic-model.yaml --state examples/example.tfstate
```
The output shows validation results at mapping, control, and risk levels.

## Scope (Initial Version)

The initial scope focuses on **architecture modeling and Terraform-based validation**.

### Out of scope for the current prototype

- Identity governance automation (including PIM and Conditional Access)  
- Microsoft Graph-based configuration validation  
- Full Microsoft 365 security integration  

These areas are **explicitly modeled**, but not yet automated.

---

## Contributing

This project follows an **open standard model**, not a single-vendor roadmap.

To contribute:

- open an issue to discuss the change  
- fork the repository  
- submit a pull request  

Contributions may include:

- model evolution  
- validation logic  
- parsers and generators  
- use cases and examples  

---

## Documentation

- **Concept** — brief introduction to Architecture as Code  
- **Whitepaper** — full concept, validation semantics, requirement-first approach  
- **Architecture Model** — detailed element definitions
