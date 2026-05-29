Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# VVV-QMRF Testable Prediction Campaign — Internal Evidence Ledger

**Framework:** VietVunVut Quantum Measurement Registration Framework (VVV-QMRF)  
**Campaign:** Testable Prediction Section  
**Document type:** Internal digital evidence ledger  
**Date:** 2026-05-17  
**Status:** Internal campaign-control document  

> **DISCLAIMER:** VVV-QMRF is independent Class D personal research, not Standard Quantum Mechanics, not peer-reviewed or experimentally validated, and not for real-world technical use. Full boundary protocol: `DISCLAIMER.md`.

---

## 1. Purpose

This ledger records internal digital evidence for the Testable Prediction Campaign. Internal evidence means project-local traceability: file paths, source documents, claim IDs, git commit references, review notes, and proof-gap status.

Internal evidence is not experimental validation. It documents how a claim was developed, sourced, revised, and bounded inside the project.

---

## 2. Evidence Entry Schema

Use this schema for every evidence entry:

```yaml
evidence_id: "EVD-TP-000"
paper_id: "INT-TP-00"
external_pair_id: "EXT-TP-00 or N/A"
claim_ids:
  - "C-TP-00-000"
evidence_type: "source_trace | formal_derivation | rca_trace | review_note | proof_gap | dependency | git_snapshot"
source_files:
  - path: "relative/path/to/source.md"
    role: "SOT | framework | meta_architecture | synthesis | mapping | external_target | paper_draft"
    anchor: "section, heading, line range, or quote target"
git_evidence:
  commit_hash: "pending"
  branch: "backup/buddhist-epistemology-quantum-measurement"
  file_path: "relative/path"
  date: "YYYY-MM-DD"
claim_status: "Class A | Class B | Class C | Class D | M | BE-source | excluded"
verification_status: "pending | internally_verified | needs_source_check | blocked | superseded"
public_use: "allowed | allowed_simplified | internal_only | blocked"
boundary: "what this evidence does not support"
notes: "short audit note"
```

---

## 3. Core Source Evidence

### EVD-TP-001 — Schema contract

```yaml
evidence_id: "EVD-TP-001"
paper_id: "CAMPAIGN"
external_pair_id: "ALL"
claim_ids:
  - "C-TP-000"
  - "C-TP-004"
evidence_type: "source_trace"
source_files:
  - path: "documents/research_documents/vvv-qmrf/schema_guide.md"
    role: "SOT"
    anchor: "source hierarchy, claim class, boundary, verification rules"
git_evidence:
  commit_hash: "pending"
  branch: "backup/buddhist-epistemology-quantum-measurement"
  file_path: "documents/research_documents/vvv-qmrf/schema_guide.md"
  date: "2026-05-17"
claim_status: "Class D"
verification_status: "internally_verified"
public_use: "allowed_simplified"
boundary: "The schema guide controls document creation; it is not a physical validation source."
notes: "Use this source to enforce source trace, claim class, and boundary rules."
```

### EVD-TP-002 — Buddhist Epistemology SOT

```yaml
evidence_id: "EVD-TP-002"
paper_id: "CAMPAIGN"
external_pair_id: "ALL"
claim_ids:
  - "C-TP-000"
evidence_type: "source_trace"
source_files:
  - path: "SYSTEM_Buddhist_Epistemology/system_be_full.md"
    role: "SOT"
    anchor: "source of truth policy and node/edge definitions"
git_evidence:
  commit_hash: "pending"
  branch: "backup/buddhist-epistemology-quantum-measurement"
  file_path: "SYSTEM_Buddhist_Epistemology/system_be_full.md"
  date: "2026-05-17"
claim_status: "BE-source"
verification_status: "internally_verified"
public_use: "allowed_simplified"
boundary: "BE source lineage supports structural mapping, not physical proof of Quantum Mechanics."
notes: "Any BE node/edge claim must trace here during RCA."
```

### EVD-TP-003 — E6 registering-system process

```yaml
evidence_id: "EVD-TP-003"
paper_id: "INT-TP-01"
external_pair_id: "EXT-TP-01"
claim_ids:
  - "C-TP-01-003"
  - "C-TP-03-002"
evidence_type: "source_trace"
source_files:
  - path: "documents/research_documents/framework/vvv_qmrf_framework_e06_registering_system_as_process_postulate.md"
    role: "framework"
    anchor: "postulate statement and formal prerequisite for E1"
git_evidence:
  commit_hash: "pending"
  branch: "backup/buddhist-epistemology-quantum-measurement"
  file_path: "documents/research_documents/framework/vvv_qmrf_framework_e06_registering_system_as_process_postulate.md"
  date: "2026-05-17"
claim_status: "Class D"
verification_status: "internally_verified"
public_use: "allowed_simplified"
boundary: "E6 defines K-side registering process; it does not define a Hilbert-space object or physical dynamics."
notes: "Supports `R` and `M_i ∈ R` in ValidReg."
```

### EVD-TP-004 — E1 self-certifying registration

```yaml
evidence_id: "EVD-TP-004"
paper_id: "INT-TP-01"
external_pair_id: "EXT-TP-01"
claim_ids:
  - "C-TP-01-004"
evidence_type: "source_trace"
source_files:
  - path: "documents/research_documents/framework/vvv_qmrf_framework_e01_self_certifying_registration_postulate.md"
    role: "framework"
    anchor: "postulate statement and sigma formal sketch"
git_evidence:
  commit_hash: "pending"
  branch: "backup/buddhist-epistemology-quantum-measurement"
  file_path: "documents/research_documents/framework/vvv_qmrf_framework_e01_self_certifying_registration_postulate.md"
  date: "2026-05-17"
claim_status: "Class D"
verification_status: "internally_verified"
public_use: "allowed_simplified"
boundary: "E1 is not a consciousness claim and not a second detector."
notes: "Supports `σ(M_X)=1` in ValidReg."
```

### EVD-TP-005 — E7 validity location

```yaml
evidence_id: "EVD-TP-005"
paper_id: "INT-TP-01"
external_pair_id: "EXT-TP-01"
claim_ids:
  - "C-TP-01-005"
  - "C-TP-01-006"
  - "C-TP-02-003"
evidence_type: "source_trace"
source_files:
  - path: "documents/research_documents/framework/vvv_qmrf_framework_e07_registration_validity_location_postulate.md"
    role: "framework"
    anchor: "postulate statement and asymmetric validity formal sketch"
git_evidence:
  commit_hash: "pending"
  branch: "backup/buddhist-epistemology-quantum-measurement"
  file_path: "documents/research_documents/framework/vvv_qmrf_framework_e07_registration_validity_location_postulate.md"
  date: "2026-05-17"
claim_status: "Class D"
verification_status: "internally_verified"
public_use: "allowed_simplified"
boundary: "E7 validity is K-side registration validity, not absolute truth and not a physical observable."
notes: "Supports `V(M_X)=1` and later invalidation in ValidReg."
```

### EVD-TP-006 — Registration-layer formalization

```yaml
evidence_id: "EVD-TP-006"
paper_id: "INT-TP-03"
external_pair_id: "EXT-TP-03"
claim_ids:
  - "C-TP-03-001"
  - "C-TP-03-003"
  - "C-TP-03-004"
evidence_type: "formal_derivation"
source_files:
  - path: "documents/research_documents/meta_architecture/vvv_qmrf_meta_architecture_registration_layer_formalization.md"
    role: "meta_architecture"
    anchor: "K-side registration structure, typed state, boundary verification"
git_evidence:
  commit_hash: "pending"
  branch: "backup/buddhist-epistemology-quantum-measurement"
  file_path: "documents/research_documents/meta_architecture/vvv_qmrf_meta_architecture_registration_layer_formalization.md"
  date: "2026-05-17"
claim_status: "Class C/D"
verification_status: "internally_verified"
public_use: "allowed_simplified"
boundary: "K-side structures are not Hilbert spaces, density matrices, or collapse states."
notes: "Supports K-side formal objects while preserving ρ-side boundary."
```

### EVD-TP-007 — Wigner's Friend registration mapping

```yaml
evidence_id: "EVD-TP-007"
paper_id: "INT-TP-04"
external_pair_id: "EXT-TP-04"
claim_ids:
  - "C-TP-04-001"
  - "C-TP-04-002"
  - "C-TP-04-003"
evidence_type: "dependency"
source_files:
  - path: "documents/research_documents/meta_architecture/vvv_qmrf_meta_architecture_wigners_friend_registration_layer_mapping.md"
    role: "meta_architecture"
    anchor: "Wigner's Friend registration-layer application boundary"
  - path: "papers/Testable_Prediction_Section/extended_wigners_friend_k_side_incommensurability/VVV-QMRF_Testable_Prediction_Plan.md"
    role: "paper_draft"
    anchor: "K-side incommensurability scaffold"
git_evidence:
  commit_hash: "pending"
  branch: "backup/buddhist-epistemology-quantum-measurement"
  file_path: "papers/Testable_Prediction_Section/extended_wigners_friend_k_side_incommensurability/VVV-QMRF_Testable_Prediction_Plan.md"
  date: "2026-05-17"
claim_status: "Class C"
verification_status: "needs_source_check"
public_use: "allowed_simplified"
boundary: "EWF application is a stress test and conjecture, not a completed physical solution."
notes: "Requires TP-03 definitions of `K_joint`, `⊥_K`, and contradiction relation before external strengthening."
```

---

## 4. Open Evidence Slots

| Evidence ID | Intended use | Status |
|---|---|---|
| EVD-TP-008 | TP-02 control cases: E8/E9/E14/E16 source trace | pending |
| EVD-TP-009 | TP-05 Proietti source verification | pending |
| EVD-TP-010 | TP-05 Bong source verification | pending |
| EVD-TP-011 | TP-05 Brukner/Frauchiger-Renner source verification | pending |
| EVD-TP-012 | TP-06 Rovelli/Relational QM comparison | pending |
| EVD-TP-013 | Git commit snapshot after campaign master creation | pending |

---

## 5. Evidence Update Rule

Before any external paper is prepared, every claim in that external paper must point to at least one internal evidence entry with `public_use: allowed` or `public_use: allowed_simplified`.
