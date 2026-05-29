# PP-5: Gate Relocation Patch — P7-G1/G2/G3 → Phase 9

**PrePlan Task:** PP-5
**Date:** 2026-05-23
**Status:** PROPOSED
**Source:** VVV_QMRF_PrePlan_Prompt_Sequence.md §PP-5 (lines 585-664)
**Affects:** K_Space_Axiomatization_plan_v3.md Phase 7 and Phase 9

---

## (A) Logic Error Documentation

Plan v3.0 places three operationalizability gates (P7-G1, P7-G2, P7-G3) in
**Phase 7 (Constraint Identification)**. These gates test whether a proposed
K9 equation satisfies specific operational conditions:

- **P7-G1:** Does the equation operationalize `Phys(o|H_physics)=1` beyond "detector click"?
- **P7-G2:** Does the equation admit `Phys=1 ∧ Lock_K=0` (nontrivial registration gap)?
- **P7-G3:** Does the equation define `t_lock` operationally?

**The error:** Phase 7 is Constraint Identification — it determines what any
valid K9 must satisfy. **No K9 equation has been proposed yet at Phase 7.**
The equations are generated in **Phase 8** (Candidate Generation).

> **Principle:** A gate that tests property X of object Y can only fire
> after object Y exists. G1/G2/G3 test equation-level properties.
> No equation exists until Phase 8. Therefore G1/G2/G3 cannot fire in Phase 7.

Placing these gates in Phase 7 creates a logical deadlock: Phase 7 blocks
on gates that require Phase 8 output to evaluate.

---

## (B) Relocation Specification

### FROM: Phase 7 — REMOVE

```diff
 Phase 7: Constraint Identification
   P7-C1: Category A — Internal consistency K1-K8          [HIGH]
   P7-C2: Category B — Physical validity (Born rule limit) [HIGH]
   P7-C3: Category C — Distinguishability of K9            [BLOCKING]
-  P7-G1: Operationalization of Phys(o|H_physics)          [BLOCKING] ← REMOVE
-  P7-G2: Nontrivial registration gap                      [BLOCKING] ← REMOVE
-  P7-G3: Operational t_lock definition                    [BLOCKING] ← REMOVE
```

### TO: Phase 9 — ADD

```diff
 Phase 9: Adversarial Falsification
   P9-C1: Physical counterexample test
   P9-C2: Axiom consistency check
   P9-C3: Distinguishability verification
   P9-C4: cert + V sensitivity
+  P9-G1: [relocated] Operationalization of Phys(o|H_physics)  [BLOCKING]
+  P9-G2: [relocated] Nontrivial registration gap               [BLOCKING]
+  P9-G3: [relocated] Operational t_lock definition             [BLOCKING]
   P9-C5: Ranking (after all above)
   P9-C6: Class C eligibility Stage 2
```

**New Phase 9 check order:**

| Order | Check | Type | Severity |
|---|---|---|---|
| 1 | P9-C1 | Physical counterexample | HIGH |
| 2 | P9-C2 | Axiom consistency | HIGH |
| 3 | P9-C3 | Distinguishability | BLOCKING |
| 4 | P9-C4 | cert + V sensitivity | HIGH |
| 5 | **P9-G1** | Operationalize Phys (relocated) | **BLOCKING** |
| 6 | **P9-G2** | Nontrivial registration gap (relocated) | **BLOCKING** |
| 7 | **P9-G3** | Operational t_lock (relocated) | **BLOCKING** |
| 8 | P9-C5 | Ranking | — |
| 9 | P9-C6 | Class C eligibility Stage 2 | HIGH |

---

## (C) Revised Phase 7 Scope

After removing G1/G2/G3, Phase 7 contains only:

| Check | Description | Severity |
|---|---|---|
| P7-C1 | Category A — Internal consistency with K1-K8 | HIGH |
| P7-C2 | Category B — Physical validity (Born rule limit) | HIGH |
| P7-C3 | Category C — Distinguishability of K9 vs Standard QM | BLOCKING |

**Revised scope statement:**

> Phase 7 evaluates **constraints** on what any valid K9 equation must satisfy.
> It does not evaluate specific equations. Phase 7 produces a constraint
> checklist (C-BORN, C-NORM, C-NONDIV, C-PARAM, C-TRACE, C-FALSI) that
> Phase 8 candidates must satisfy. Gates that test equation-level properties
> (operationalizability, registration gap, t_lock definition) are deferred
> to Phase 9, where specific equations exist to be tested.

---

## (D) Dependency Impact Verification

| Dependency | Affected? | Details |
|---|---|---|
| Phase 7 → Phase 8 | ❌ UNCHANGED | P7-C1/C2/C3 feed derivation constraints to Phase 8. Removing G1/G2/G3 does not change these constraints. |
| Phase 8 → Phase 9 | ❌ UNCHANGED | P8-C1..C5 feed adversarial tests to Phase 9. Adding P9-G1/G2/G3 extends Phase 9's test set. |
| Phase 9 → Phase 10 | ❌ UNCHANGED | P9-C5 ranking selects K9_candidate for Phase 10 fit. P9-G1/G2/G3 are evaluated before P9-C5 ranking. |
| Phase 10 → Phase 11 | ❌ UNCHANGED | No dependency on G1/G2/G3 placement. |

**Confirmed:** Relocation affects Phase 7 and Phase 9 only. No cascade changes
to other phases.

---

## (E) Issue Registry Update

### Phase 7 Issue Registry (AFTER relocation)

| ID | Description | Severity | Status |
|---|---|---|---|
| P7-C1 | Internal consistency K1-K8 | HIGH | PENDING |
| P7-C2 | Physical validity (Born rule limit) | HIGH | PENDING |
| P7-C3 | Distinguishability vs Standard QM | **BLOCKING** | PENDING |

### Phase 9 Issue Registry (AFTER relocation)

| ID | Description | Severity | Status | Source |
|---|---|---|---|---|
| P9-C1 | Physical counterexample test | HIGH | PENDING | Original |
| P9-C2 | Axiom consistency check | HIGH | PENDING | Original |
| P9-C3 | Distinguishability verification | BLOCKING | PENDING | Original |
| P9-C4 | cert + V sensitivity | HIGH | PENDING | Original |
| **P9-G1** | Operationalize Phys(o\|H_physics) | **BLOCKING** | PENDING | **Relocated from P7-G1** |
| **P9-G2** | Nontrivial registration gap | **BLOCKING** | PENDING | **Relocated from P7-G2** |
| **P9-G3** | Operational t_lock definition | **BLOCKING** | PENDING | **Relocated from P7-G3** |
| P9-C5 | Ranking | — | PENDING | Original |
| P9-C6 | Class C eligibility Stage 2 | HIGH | PENDING | Original |

---

## Implementation Checklist

- [ ] Update plan_v3 §Phase 7: remove G1/G2/G3 lines; add note "relocated to Phase 9 per PP-5"
- [ ] Update plan_v3 §Phase 9: add P9-G1/G2/G3 with BLOCKING severity
- [ ] Update plan_v3 §Issue Registry table: reflect new assignments
- [ ] Cross-reference this patch in CHANGELOG.md
- [ ] Verify K9 Analysis Plan (K9-S5 adversarial) includes G1/G2/G3 checks
      (K9-S5 already includes operationalizability tests — confirm alignment)

---

## Alignment with K9 Analysis Plan

The K9 Analysis Plan (K9-S5, lines 558-683) already includes adversarial tests
that overlap with G1/G2/G3:

| PP-5 relocated gate | K9-S5 equivalent | Overlap |
|---|---|---|
| P9-G1 (Operationalize Phys) | Attack 2: Circular Definition Hunt | Partial — P9-G1 broader |
| P9-G2 (Registration gap) | Attack 5: EWF Scenario Stress Test | Partial — checks cert/V asymmetry |
| P9-G3 (Operational t_lock) | Attack 2: Circular Definition Hunt | Partial — checks temporal definitions |

**Recommendation:** When executing Phase 9, run K9-S5 adversarial tests FIRST,
then apply P9-G1/G2/G3 as additional blocking gates on survivors. This avoids
redundant work while ensuring operationalizability is checked.
