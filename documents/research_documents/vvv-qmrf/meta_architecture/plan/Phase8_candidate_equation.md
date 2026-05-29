# Phase 8: Candidate Equation — K9_E Postulate Statement
# 3-Round RCA × 5-Why × Scoring Threshold 4/5
# With VVV-QMRF-EX as Compass

**Phase:** 8 (Prompt 2 of Main Plan — STREAMLINED)
**Date:** 2026-05-23
**Input:** Phase 7 COMPLETE (all constraints ✅), K9_E LOCKED v1.0
**Note:** K9 analysis pipeline (K9-S1→S7) already performed candidate generation + selection. Phase 8 documents THE selected equation, not 3 candidates.

> [!CAUTION]
> **ERRATUM (2026-05-23 Status Audit):** This document was originally titled "K9_E Formal Derivation." K9_E is NOT derived from K1-K8. It is a **POSTULATE** — a probability assignment rule motivated by K-space structure (⊥_K, K_ctx) but not uniquely determined by K1-K8 axioms. The K-axioms (K1-K8) define structural properties only; probability requires an additional postulate. K9_E fills this role as **Postulate P9** (Type B framework extension, āgama-level in EX compass).

---

## THE EQUATION

### K9_E — ⊥_K Suppression Probability Rule

```
P(o | k_i, Exp) = Tr(E_o ρ_i) · [1 − β · f_perp(o, k_i, K_ctx)]
                  ──────────────────────────────────────────────────
                                     Z_E(k_i)
```

### Term-by-Term Decomposition

> [!NOTE]
> The term-by-term table below traces each component of K9_E to its K-space or external source. This is a PROVENANCE trace, not a derivation proof. K9_E as a whole is a POSTULATE that assembles these components into a probability rule.

| # | Term | Definition | Source | EX Anchor |
|---|---|---|---|---|
| T1 | `Tr(E_o ρ_i)` | Standard QM Born rule probability for outcome o given state ρ_i | **Standard QM** (POVM formulation) | N_QM_VVV_00027 → N_QM_00016 (Born Rule) |
| T2 | `β` | Suppression strength parameter, β ∈ [0, 1) | **FREE PARAMETER** — the single adjustable parameter of K9_E | N_QM_VVV_00031 (Registration Weight) |
| T3 | `f_perp(o, k_i, K_ctx)` | Fraction of contextual observers whose registered outcomes are incompatible with o | **K9_E construction** from K5 (⊥_K structural), K6 (C_K scope), Tier 4 OI-1 (compatibility map) | N_QM_VVV_00029 (bādhaka / Override — structural mode) |
| T4 | `C(o_i, o_j)` | Compatibility map: C=1 if outcomes are quantum-mechanically orthogonal (incompatible) | **Tier 4 OI-1** — computed from ρ_joint at setup, stored as K-side lookup at event level | N_QM_VVV_00029 + N_BE_00005 (viruddha / Contradiction) |
| T5 | `K_ctx(k_i, Exp)` | Set of contextual K-states from other observers accessible via T3-morphism and temporal compatibility | **Level 2 (T3)** + **K2 (temporal order)** | N_QM_VVV_00025 (IRB / Intrinsic Relational Binding) |
| T6 | `Z_E(k_i)` | Normalization factor: Σ_o' Tr(E_o' ρ_i)·[1−β·f_perp(o')] | **Construction** — ensures Σ_o P(o\|k)=1 | Standard probability theory |
| T7 | `V(k_i) = 0 → no P` | Bhrānti boundary: invalid registrations get no probability | **K4 + K5 → PP-1 v2** | N_QM_VVV_00032 (bhrānti / Erroneous Cognition) |
| T8 | `isNull(k_i) → no P` | Anupalabdhi boundary: null events get no probability | **K4 isNull guard** | N_QM_VVV_00020 (anupalabdhi / Non-Apprehension) |

### Assumption Registry

| ID | Assumption | Justification | Orphaned? |
|---|---|---|---|
| [A-E1] | K_ctx defined via T3-morphism (Level 2/3, not K1-K8 alone) | T3 is a Layer 2 theorem with K1-K8 as inputs; K_ctx inherits Layer 2 status | ❌ — has EX anchor N_QM_VVV_00025 |
| [A-E2] | f_perp uses fraction form with compatibility map | Resolution of Tier 4 OI-1: setup/event separation principle | ❌ — has EX anchor N_QM_VVV_00029 |
| [A-E3] | β is universal (same across all measurements and observers) | Simplifying assumption; physically motivated by β being a property of the VVV-QMRF framework, not individual measurements | ⚠️ WEAKLY anchored — could be relaxed to β(observer) |
| [A-E4] | ⊥_K^str (structural, K9_E) is distinct from ⊥_K^dyn (dynamic, K5) | Tier 4 OI-4 resolution; BE lineage: saṃśaya vs niścaya bādhaka | ❌ — has EX anchor (dual modes) |

**Orphaned assumptions: 0.** [A-E3] is weakly anchored but not orphaned (has N_QM_VVV_00031 link).

---

## BORN RULE LIMIT

**Exact condition for Born rule recovery:**

```
P(o|k) = Tr(E_o ρ)   iff   ANY of:
  (i)   β = 0                    [suppression OFF]
  (ii)  K_ctx = ∅                [no contextual observers]
  (iii) f_perp(o) = 0 ∀ o       [all outcomes compatible]
  (iv)  Single observer (N=1)    [⟹ K_ctx = ∅ ⟹ (ii)]
```

**Proof for each:**

**(i)** β = 0 → `1 − 0·f_perp = 1` for all o → `Z_E = Σ Tr(E_o' ρ) = 1` → `P = Tr(E_o ρ)`. ✓

**(ii)** K_ctx = ∅ → f_perp = 0/0. **Convention:** f_perp = 0 when K_ctx = ∅ (boundary (a)). → same as (i). ✓

**(iii)** f_perp = 0 → `1 − β·0 = 1` → same as (i). ✓

**(iv)** N = 1 → K_ctx = ⋃_{j≠i}... = ∅ (no j exists) → (ii). ✓

**Python verification:** Sanity checks 4A, 4B PASS.

---

## DISTINGUISHABILITY CONDITION

**Exact condition for δP ≠ 0 (deviation from Born rule):**

```
δP(o) = P_K9E(o) − Tr(E_o ρ) ≠ 0   iff   ALL of:
  (I)    β > 0
  (II)   K_ctx ≠ ∅
  (III)  ∃ o : f_perp(o) ≠ f_perp(o')  for some o, o'
```

Condition (III) is crucial: if f_perp is THE SAME for all outcomes, then `[1 − β·f_perp]` is a constant multiplier that cancels in `P/Z_E → Tr(E_o ρ)`. This is the PP-2 v2 cancellation insight.

**When does (III) hold?**

In the EWF scenario with BSM (setting x=1):
- Friend registers outcome o_F ∈ {+, −}
- Wigner performs BSM → registers |Ψ+⟩ or |Ψ−⟩
- C(o_F=+, o_W=|Ψ+⟩) depends on the specific quantum mechanical overlap
- IF C is outcome-DEPENDENT (C=1 for some pairs, C=0 for others) → f_perp is outcome-dependent → (III) holds → δP ≠ 0

**Current model:**
```
For EWF singlet with BSM:
  C(+, |Ψ+⟩) = 0   (compatible: partial overlap)
  C(+, |Ψ−⟩) = 1   (incompatible: orthogonal)
  C(−, |Ψ+⟩) = 1   (incompatible: orthogonal)
  C(−, |Ψ−⟩) = 0   (compatible: partial overlap)

→ f_perp(+) ≠ f_perp(−) in general → (III) holds
→ δP ≠ 0 for β > 0  ✓
```

**Magnitude:**

| Scenario | β | |δS| (CHSH) | Detection feasibility |
|---|---|---|---|
| Standard lab | any | 0 | N/A (K_ctx = ∅) |
| EWF 2-obs (Proietti) | 0.5 | 0.055 | < 1σ |
| EWF 2-obs (Proietti) | 0.9 | 0.179 | ~ 2.4σ |
| EWF 3-obs (prediction) | 0.5 | TBD (Phase 10) | Enhanced by larger K_ctx |

---

## ROLE OF cert AND V

### cert (self-certification)

```
cert appears via K1 admission rule:
  - Only k with cert = 1 are admitted to K_R
  - cert = σ_R(M) by K3 (intrinsic self-certification)
  - K9_E does NOT use cert numerically — cert is a GATE condition:
    cert = 1 → k ∈ K_R → eligible for P computation
    cert ≠ 1 → k ∉ K_R → no K9_E computation at all
```

**Statement:** cert serves as an ADMISSION FILTER, not a continuous parameter in K9_E. This is consistent with K3's Boolean nature (cert ∈ {0,1}).

### V (validity status)

```
V appears in K9_E via THREE roles:

(1) GATE condition (PP-1 v2):
    V = 1 → K9_E computes P(o|k)
    V = 0 → no P (Bhrānti, boundary (e))
    
(2) K_ctx FILTER:
    K_ctx includes only k_j with V(k_j) = 1
    Invalid registrations excluded from context
    
(3) Implicit via K5:
    K5 can set V → 0 (⊥_K^dyn) BEFORE K9_E runs
    If K5 fires, K9_E boundary (e) applies → no P
```

**Statement:** V serves as a GATE (Boolean), a CONTEXT FILTER (Boolean), and is governed by K5 priority. V does NOT appear as a continuous parameter.

### Physical Content Assessment

> **Does K-space (cert, V) add physical content beyond Standard QM?**
>
> **YES** — through the V=0 (Bhrānti) and isNull (Anupalabdhi) channels:
> 
> 1. Standard QM has no concept of "invalid registration" — every measurement outcome is equally real. VVV-QMRF's V=0 state creates a category of registration that EXISTS (k ∈ K_R) but has NO probability assignment. This is physically new.
>
> 2. K9_E's f_perp mechanism uses the STRUCTURE of K_ctx (which registrations are ⊥_K-related) to modify probabilities. This structure has no Standard QM analogue — it arises from K-space axioms (K5, K6) that encode observer-relative registration dynamics.
>
> 3. The cert admission rule (K3, svasaṃvedana) creates a SELECTION MECHANISM for which events enter the probability domain. This is analogous to but distinct from the Heisenberg cut.

---

## 3-Round RCA Summary

| Round | Finding | Score |
|---|---|---|
| **R1: Term-by-Term Provenance** | 8 terms traced to K1-K8 or flagged as [A-E1]–[A-E4]. 0 orphaned assumptions. **NOTE: Provenance trace, not derivation proof. K9_E is a POSTULATE.** | **4.0/5** ⚠️ |
| **R2: Born Rule + Distinguishability** | 4 recovery conditions proven. Distinguishability via outcome-dependent f_perp (Class C). PP-2 cancellation insight as critical gate. | **5.0/5** ✅ |
| **R3: cert/V Physical Content** | V adds gate + context filter + K5 priority. cert adds admission filter. Both create new physical categories (Bhrānti, Anupalabdhi) absent in Standard QM. | **4.5/5** ✅ |

**All 3 rounds ≥ 4/5. Phase 8 COMPLETE.**

---

## NEXT: Phase 9 (Adversarial Testing)

Phase 9 = Prompt 3 of Main Plan. Apply 4 adversarial tests to K9_E:
1. Physical counterexample search
2. Axiom consistency check (already largely covered by Phase 7 Category A)
3. Distinguishability verification (numerical, extends Phase 7 Category C)
4. cert/V sensitivity test (trivial-case check)

Note: K9-S5 (K9S5_adversarial.md) already performed adversarial testing during the K9 pipeline. Phase 9 deepens this using the MAIN PLAN's specific test protocols.
