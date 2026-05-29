# Decision: T4 Bypass for K9 Candidate Evaluation

**Decision ID:** D-T4-BYPASS-01
**Date:** 2026-05-23
**Status:** PROPOSED
**Affects:** K_Space_Axiomatization_plan_v3.md Phase 7-12, VVV_QMRF_K9_Analysis_Plan.md K9-S1→S7

---

## Problem Statement

T4 (N-Observer Generalization Theorem) has **3 unresolved BLOCKING items**:
- **T4-B1:** T4-H Colimit Existence Hypothesis — unproven
- **T4-B2:** F7d Global Commutativity — N>2 path-independence unproven
- **T4-B3:** Open Item #9 — N>2 concrete model missing

Resolving all 3 requires ~18-26h of category-theoretic proof work.

However, **only 1 of 6 K9 candidates** (K9_F, Colimit Probability) depends on T4.

---

## Decision

**K9_A, K9_B, K9_C, K9_D, K9_E proceed to evaluation (PrePlan + K9 Analysis Pipeline) WITHOUT T4 proof.**

**Justification:**
1. K9_A uses K4/K5 only → T1 (N=2, constructive) sufficient
2. K9_B uses K3/K5/K6 → T1 sufficient
3. K9_C uses K2 timestamps → no joint K-space needed
4. K9_D uses K3 cert → no joint K-space needed
5. K9_E uses K5/K6 ⊥_K → T1 sufficient for pairwise context
6. **Only K9_F** requires T4 colimit for joint probability construction

**T4 proof (Tier 5-7, ~18-26h) is DEFERRED** until one of:
- All non-F candidates fail K9-S3 ranking (score < 12/25) AND K9_F is last standing
- K9-S5 adversarial eliminates all non-F survivors
- Researcher explicitly requests T4 proof for independent reasons

---

## Dependency Verification

| Candidate | Uses T1 (N=2)? | Uses T4 (N≥2)? | T4 bypass valid? |
|---|---|---|---|
| K9_A (V-Filter) | No (single K_R) | No | ✅ |
| K9_B (Registration-Conditioned) | Yes (for EWF joint) | No | ✅ |
| K9_C (Latency Weighting) | No (single K_R) | No | ✅ |
| K9_D (Certification Discount) | No (single K_R) | No | ✅ (but pre-FAIL) |
| K9_E (⊥_K Suppression) | Yes (for context) | No | ✅ |
| K9_F (Colimit Probability) | No | **YES** | ❌ BLOCKED |

**Confirmed:** T1 derivation (K_Space_Axiom lines 569-627) uses K1/K2/K3/K6/K8 only, does NOT reference T4-H.

---

## K9_F Handling

K9_F enters K9-S2 evaluation with status:

```
K9-S2 Step 7 (Special Problem Check for K9_F):
  "K9_F is blocked until T4 is proven. Estimated prerequisites:
   1. T4-H colimit existence proof (~5-7h)
   2. F7d global commutativity proof (~4-6h)
   3. N=3 EWF concrete model (~9-11h)
  K9_F preliminary verdict: CONDITIONAL PASS (blocked by T4)."
```

K9_F can receive a **CONDITIONAL PASS** in K9-S2 but cannot be selected as PRIMARY in K9-S3 unless T4 proof is completed.

---

## Trigger to Revisit This Decision

| Trigger | Action |
|---|---|
| All 5 non-F candidates FAIL K9-S2 | Begin T4 proof immediately (Tier 5) |
| K9_F is highest-scoring survivor in K9-S3 | Begin T4 proof, K9_F becomes CONDITIONAL PRIMARY |
| K9-S5 eliminates all non-F candidates | Begin T4 proof or accept FINDING VVV-K9-NULL |
| Researcher requests T4 proof independently | Proceed to Tier 5 regardless of K9 status |

---

## Saved Effort (if bypass holds)

| Skipped | Effort saved |
|---|---|
| T4-H proof (Tier 5) | 5-7h |
| F7d proof (Tier 6) | 4-6h |
| N=3 model (Tier 7) | 9-11h |
| **Total saved** | **18-24h** |
