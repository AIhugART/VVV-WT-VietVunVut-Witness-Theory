# Decision: K9 Candidate Name Reconciliation

**Decision ID:** D-NAME-01
**Date:** 2026-05-23
**Status:** PROPOSED
**Affects:** K_Space_Axiomatization_plan_v3.md, VVV_QMRF_K9_Analysis_Plan.md

---

## Problem Statement

Two planning documents define K9 candidates with **overlapping but inconsistent naming**:

- **plan_v3** (K_Space_Axiomatization_plan_v3.md §1.4): defines 3 candidates — K9_A, K9_B, K9_C
- **K9 Analysis Plan** (VVV_QMRF_K9_Analysis_Plan.md): defines 5 candidates — K9_A, K9_C, K9_D, K9_E, K9_F

The name "K9_C" appears in **both** documents but refers to **different equations**.

---

## Mapping Table

| plan_v3 Name | K9 Analysis Plan Name | Equation | Match Status |
|---|---|---|---|
| K9_A (V-Weighted Born Rule) | K9_A (V-Filter) | `V(k)·Tr(E_o ρ)/Z` → corrected to case-based (PP-1) | ✅ SAME concept |
| K9_B (Registration-Conditioned) | *(not present)* | `Tr(E_o ρ)·f(cert,V,⊥_K,C_K)` | ⚠️ plan_v3 ONLY |
| K9_C (Colimit Probability via T4) | K9_F (Colimit Probability) | `P(o_F,o_W\|K_joint)` via T4 colimit | ❌ NAME COLLISION |
| *(not present)* | K9_C (Registration Latency Weighting) | `Tr(E_o ρ)·g(τ_reg)/Z_C` | ⚠️ Analysis Plan ONLY |
| *(not present)* | K9_D (Certification Discount) | `[cert+(1-cert)·α]·Tr(E_o ρ)/Z_D` | ⚠️ Analysis Plan ONLY; pre-identified FAIL |
| *(not present)* | K9_E (⊥_K Suppression) | `Tr(E_o ρ)·[1-β·f_perp]/Z_E` | ⚠️ Analysis Plan ONLY |

---

## Collision Detail

| | plan_v3 "K9_C" | K9 Analysis Plan "K9_C" |
|---|---|---|
| **Full name** | Colimit Probability via T4 | Registration Latency Weighting |
| **Equation** | `lim_{colimit} Σᵢ wᵢ·P(o\|Kᵢ)` | `Tr(E_o ρ)·g(τ_reg(o))/Z_C` |
| **T4 dependency** | YES — requires T4 colimit | NO |
| **Free parameters** | 2-3 (weighting scheme) | 1 (τ₀ characteristic time) |

These are **completely different equations** sharing the same label.

---

## Decision: Adopt K9 Analysis Plan Naming as Authoritative

**Rationale:**
1. K9 Analysis Plan has the **larger, more complete** candidate set (5 vs 3)
2. K9 Analysis Plan has **structured evaluation protocol** (K9-S1→S7) already referencing these names
3. plan_v3 candidates map cleanly into the Analysis Plan naming with one rename

**Authoritative naming (post-reconciliation):**

| Canonical Name | Source | Equation | T4 Needed? |
|---|---|---|---|
| **K9_A** | Both | V-Filter (case-based, corrected by PP-1) | NO |
| **K9_B** | plan_v3 only | Registration-Conditioned: `Tr(E_o ρ)·f(cert,V,⊥_K,C_K)` | NO |
| **K9_C** | K9 Analysis Plan | Registration Latency Weighting: `Tr(E_o ρ)·g(τ_reg)/Z_C` | NO |
| **K9_D** | K9 Analysis Plan | Certification Discount (pre-identified FAIL: α cancels) | NO |
| **K9_E** | K9 Analysis Plan | ⊥_K Suppression: `Tr(E_o ρ)·[1-β·f_perp]/Z_E` | NO |
| **K9_F** | Both (was plan_v3 "K9_C") | Colimit Probability via T4 | YES |

**Actions required:**
1. In plan_v3: rename "K9_C (Colimit Probability)" → "K9_F" with cross-reference note
2. In K9 Analysis Plan: add K9_B (Registration-Conditioned) to candidate list, or note it as plan_v3-only candidate evaluated separately in PP-2
3. All future documents use canonical naming above

---

## Impact Assessment

| Document | Change Required |
|---|---|
| K_Space_Axiomatization_plan_v3.md | Rename K9_C → K9_F in §1.4 and all references (~5 occurrences) |
| VVV_QMRF_K9_Analysis_Plan.md | Add note: "K9_B from plan_v3 evaluated in PP-2; included as 6th candidate if PP-2 produces viable specification" |
| K_Space_Axiomatization.md | No change (does not reference K9 candidates by name) |
| All future K9 documents | Use canonical naming above |

---

## Verification Checklist

- [ ] plan_v3 K9_C references updated to K9_F
- [ ] K9 Analysis Plan acknowledges K9_B existence
- [ ] No document uses "K9_C" to mean "Colimit Probability" after this decision
- [ ] K9-S2 pipeline runs 6 candidates (A/B/C/D/E/F) or explicitly excludes K9_B with justification
