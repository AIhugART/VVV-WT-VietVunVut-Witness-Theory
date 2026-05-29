Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# VVV-QMRF Testable Prediction Campaign — Publication Gates

**Framework:** VietVunVut Quantum Measurement Registration Framework (VVV-QMRF)  
**Campaign:** Testable Prediction Section  
**Document type:** Publication gate checklist / internal-to-external promotion protocol  
**Date:** 2026-05-17  
**Status:** Internal campaign-control document  

> **DISCLAIMER:** VVV-QMRF is independent Class D personal research, not Standard Quantum Mechanics, not peer-reviewed or experimentally validated, and not for real-world technical use. Full boundary protocol: `DISCLAIMER.md`.

---

## 1. Purpose

This document defines the gates required before a Testable Prediction Campaign paper moves from internal technical development to external public release.

The goal is to preserve two qualities at the same time:

1. Internal technical rigor.
2. External public safety and readability.

---

## 2. Gate Overview

```text
Gate 0 — Paper identity defined
Gate 1 — RCA complete
Gate 2 — Claim registry complete
Gate 3 — Source trace complete
Gate 4 — Symbol and formula boundaries complete
Gate 5 — Internal evidence ledger updated
Gate 6 — External simplification complete
Gate 7 — External disclaimer and non-claims present
Gate 8 — Citation and public evidence check complete
Gate 9 — User approval for public action
```

---

## 3. Internal Gate Checklist

### Gate 0 — Paper identity defined

Required:

```text
Paper ID assigned: INT-TP-XX
External pair assigned: EXT-TP-XX
One-sentence purpose written
Main research question written
Claim class target written
Dependencies listed
```

Pass condition:

```text
A reader can tell what bottleneck this paper solves and which later papers depend on it.
```

### Gate 1 — RCA complete

Required:

```text
Phenomenon
Proximate cause
Underlying mechanism
Root cause / new principle
Generalization
Three-Why trace for major claims
```

Pass condition:

```text
The paper fixes the root cause, not only a wording symptom.
```

### Gate 2 — Claim registry complete

Required:

```text
Every major claim has a Claim ID.
Every major claim has a class: A, B, C, D, M, BE-source, or Excluded.
Every Class C claim has an open proof or operationalization note.
Every excluded claim is removed or rewritten.
```

Pass condition:

```text
No major claim appears in the internal paper without a registry row.
```

### Gate 3 — Source trace complete

Required:

```text
BE claims trace to SYSTEM_Buddhist_Epistemology/system_be_full.md.
E6 claims trace to the E6 framework document.
E1 claims trace to the E1 framework document.
E7 claims trace to the E7 framework document.
K-side notation traces to the registration-layer formalization.
Wigner's Friend application traces to the Wigner mapping and external literature targets.
```

Pass condition:

```text
Each source-sensitive claim has a source file and anchor.
```

### Gate 4 — Symbol and formula boundaries complete

Required:

```text
All symbols are defined.
All symbols have a layer: ρ-side, K-side, external math, BE-source, or conjectural.
All formulas have status: definition, constraint, mapping function, scoring function, lemma expression, or heuristic formalization.
No K-side symbol is presented as canonical QM.
```

Pass condition:

```text
A reader cannot confuse K-side notation with Hilbert-space physics.
```

### Gate 5 — Internal evidence ledger updated

Required:

```text
Each major claim has at least one internal evidence entry.
Each evidence entry has public_use status.
Proof gaps are recorded.
Git evidence fields are updated when commits exist.
```

Pass condition:

```text
The internal paper can be audited through the evidence ledger.
```

---

## 4. External Gate Checklist

### Gate 6 — External simplification complete

Required:

```text
No long RCA sections.
No internal claim-scoring bureaucracy.
No LLM workflow notes.
No self-validation tone.
Minimal notation only.
Research question appears early.
Argument is readable without project-internal context.
```

Pass condition:

```text
The paper reads as a public research note, not an internal lab notebook.
```

### Gate 7 — External disclaimer and non-claims present

Required:

```text
Status and Scope disclaimer present.
Non-claims present where appropriate.
No claim that VVV-QMRF replaces Standard QM.
No claim that VVV-QMRF revises Born rule, unitary evolution, density-matrix dynamics, or physical collapse.
No claim that Buddhist Epistemology proves Quantum Mechanics.
No claim of experimental validation unless independently documented.
```

Pass condition:

```text
The external paper states what it claims and what it does not claim.
```

### Gate 8 — Citation and public evidence check complete

Required:

```text
External citations verified or labeled as source targets.
Public evidence ledger slot assigned.
Public version ID assigned.
Venue-specific wording checked.
Public critique invitation included if the release is informal.
```

Pass condition:

```text
The paper does not invent citations or overstate public evidence.
```

### Gate 9 — User approval for public action

Required:

```text
User explicitly approves the specific action.
User explicitly approves the specific venue.
User explicitly approves the version to release.
```

Pass condition:

```text
No post, upload, submission, or public comment occurs without explicit current approval.
```

---

## 5. Decision Score Rules

Use scores internally only. Do not put these scores in external papers.

| Score | Meaning | Action |
|---:|---|---|
| 5.0 | Strong enough for external draft preparation | Prepare external draft. |
| 4.0–4.9 | Good, but check boundaries and citations | Prepare with caution. |
| 3.5–3.9 | Internal plan only unless user approves limited public note | Do not release as paper yet. |
| 3.0–3.4 | Needs more source trace or formal work | Keep internal. |
| < 3.0 | Root cause not solved | Redo RCA. |

Minimum scores:

```text
Internal paper readiness: ≥ 3.5/5
External paper readiness: ≥ 4.0/5
Public submission readiness: ≥ 4.5/5
```

---

## 6. Pair-Specific Gates

| Paper pair | Internal gate emphasis | External gate emphasis |
|---|---|---|
| TP-01 ValidReg | E6/E1/E7 source trace and six-condition clarity | Simple criterion and strong disclaimer |
| TP-02 Control cases | Failure taxonomy and source trace to E7/E8/E9/E14/E16 | Clear examples without overextending |
| TP-03 K-side spaces | `K_joint`, embedding, contradiction relation definitions | Avoid treating K-side as physical space |
| TP-04 EWF | Step 4 proof-gap discipline | State conjecture, not completed solution |
| TP-05 Disconfirmation | Operational mapping to public comparison targets | Avoid claiming existing validation |
| TP-06 Interpretation | Neutral comparison and source verification | Avoid dismissive language toward other interpretations |

---

## 7. External Red-Flag Rewrite Rules

| If external draft says | Rewrite as |
|---|---|
| "VVV-QMRF predicts" | "VVV-QMRF proposes a testability target" unless operational mapping is complete. |
| "This proves" | "This suggests" or "This paper proposes". |
| "Standard QM cannot" | "Standard QM does not separately formalize this VVV-QMRF registration-layer criterion". |
| "Wigner's Friend is solved" | "The scenario is used as a stress test for the registration-layer criterion". |
| "Buddhist Epistemology explains collapse" | "Buddhist Epistemology provides source lineage for a registration-layer framework". |
| "Reddit response validates the framework" | "Public critique was received and logged". |

---

## 8. Final Promotion Checklist

Before any external paper is released:

```text
[ ] Internal paper exists.
[ ] External paper exists.
[ ] Claim IDs are present in claim registry.
[ ] Internal evidence entries exist.
[ ] Public evidence slot exists.
[ ] Disclaimer is present.
[ ] Non-claims are present.
[ ] No unverified citation is presented as verified.
[ ] No Class C claim is presented as established.
[ ] No public action occurs without explicit user approval.
```
