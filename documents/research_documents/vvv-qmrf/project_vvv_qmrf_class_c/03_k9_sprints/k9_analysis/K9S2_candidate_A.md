# K9-S2: Individual Candidate Analysis — K9_A (V-Filter)
# 3-Round RCA × 5-Why × Scoring Threshold 4/5
# With VVV-QMRF-EX as Compass

**Candidate:** K9_A — V-Filter (Born rule with registration filter)
**Date:** 2026-05-23
**Input:** K9-S1 verified constraint set
**Source:** VVV_QMRF_K9_Analysis_Plan.md §K9-S2 (lines 167-308)
**Prior work:** PP-1 v2 (EX-enriched three-case definition)

---

## Candidate Definition (from PP-1 v2)

```
K9_A — V-Filter (Three-Case, EX-Enriched):

Case 1: V(k)=1 ∧ ¬isNull
  P(o|k) = Tr(E_o ρ)          — Born Rule via arthakriyā (EX N_QM_VVV_00027)

Case 2: V(k)=0 ∧ ¬isNull  (Bhrānti / EX N_QM_VVV_00032)
  No P assignment. Event contributes to N_bhranti counter.
  K-side: registration exists but is erroneous (bādhaka-voided).

Case 3: isNull  (Anupalabdhi / EX N_QM_VVV_00020)
  No P assignment. Event contributes to N_null counter.
  K-side: registration itself is absent (no arthakriyā).

Free parameter: v_rate ∈ [0,1] = fraction of runs with V=1.
(Population parameter, not per-event.)
```

---

## STEP 1: CONSTRAINT CHECK

| Constraint | Status | Condition or Fix |
|---|---|---|
| **C-BORN** | ✅ PASS | V=1 ∧ ¬isNull → P=Tr(E_o ρ). Direct. |
| **C-NORM** | ✅ PASS | V=1 case: Σ_o Tr(E_o ρ) = 1 (POVM completeness). V=0 and isNull: no P assigned → normalization vacuously satisfied. |
| **C-NONDIV** | ✅ PASS | No denominators in K9_A (three-case, no Z). PP-1 v2 eliminated the original V-weighted division. |
| **C-PARAM** | ✅ PASS | 1 free parameter (v_rate). Satisfies ≤1 (for S_exp) and ≤2 (for ⟨A_xB_y⟩). |
| **C-TRACE** | ⚠️ CONDITIONAL | V, cert, ⊥_K traceable to K1/K4/K5. **v_rate is ASSUMPTION [A1]:** not derivable from K1-K8. It is a population parameter requiring external input (experimental setup or K-side population model). EX anchor: N_QM_VVV_00032 (Bhrānti rate depends on decoherence rate, which is experimentally determined). |
| **C-FALSI** | ⚠️ CONDITIONAL | Probability-level: δP=0 when V=1 (Case 1 = Born rule exactly). Registration-level: N_bhranti>0 and N_null>0 are testable predictions. Statistical-level: selection bias in correlations (PP-1 v2 Channel 3). **Falsifiable at registration/statistical level, not probability level.** |
| **C-NONNEG** | ✅ PASS | P = Tr(E_o ρ) ≥ 0 always (positive semi-definiteness). |

---

## STEP 2: BORN RULE DERIVATION

```
K9_A, Case 1 (V=1 ∧ cert=1 ∧ ⊥_K silent):
  By definition: P(o|k) = Tr(E_o ρ)
  
  This IS the Born rule. Reduction is exact.
  No approximation, no limit. Direct identity.
  
  cert=1: holds by K1 admission rule (all k ∈ K_R have cert=1).
  V=1: Case 1 condition.
  ⊥_K silent: no bādhaka → V remains 1.
  
  Algebraically: P(o|k) = Tr(E_o ρ). ∎
```

**Deviation: ZERO** in Case 1. Born rule is exactly recovered.

---

## STEP 3: DIVISION BY ZERO AUDIT

| Denominator | Location | Can it be zero? | Resolution |
|---|---|---|---|
| **None** | K9_A v2 is case-based, no fractions | N/A | ✅ No division at all |

**PP-1 v2 design rationale:** The original K9_A (v1) had Z = Σ V(k)·Tr(E_o ρ) in the denominator, which was zero when all V=0. The three-case redesign eliminates all denominators by not assigning P to V=0 events.

---

## STEP 4: DERIVATION TRACE

| Term | Source | Axiom or ASSUMPTION |
|---|---|---|
| P(o\|k) | Probability assignment | K9 definition (this is what we're building) |
| V(k) | Validity flag | **K4** (arthakriyā axiom, L215-258) |
| cert(k) | Self-certification | **K1** (admission rule, L96-100) |
| ⊥_K | Contradiction operator | **K5** (bādhaka axiom, L260-349) |
| isNull | Null registration | **K8** (absence axiom, L480-540) + EX N_QM_VVV_00020 |
| Tr(E_o ρ) | Born rule | Standard QM (ρ-side) + EX N_QM_00016 |
| E_o | POVM element | Standard QM (ρ-side) |
| ρ | Density matrix | Standard QM (ρ-side) |
| **v_rate** | Population V=1 fraction | **ASSUMPTION [A1]** — EX anchor: Bhrānti rate (N_QM_VVV_00032) depends on decoherence (N_QM_00095). v_rate = 1 − bhrānti_rate − null_rate. |
| **N_bhranti** | Bhrānti event counter | **ASSUMPTION [A2]** — observable defined by K9_A, not by K1-K8 directly. EX anchor: N_QM_VVV_00032 grounds the concept. |
| **N_null** | Null event counter | **ASSUMPTION [A3]** — observable defined by K9_A. EX anchor: N_QM_VVV_00020 (Anupalabdhi). |

**Assumption count: 3** (A1: v_rate, A2: N_bhranti, A3: N_null). All have EX anchors.

---

## STEP 5: DISTINGUISHABILITY ANALYSIS

### When does K9_A predict P(o|k) ≠ Tr(E_o ρ)?

**NEVER at the probability level for individual valid events.** Case 1 (V=1) gives exactly Born rule. Cases 2-3 assign no P.

### δP computation

```
δP = P_K9A(o) − P_QM(o)

For V=1 events:   δP = Tr(E_o ρ) − Tr(E_o ρ) = 0
For V=0 events:   δP is UNDEFINED (K9_A assigns no P, QM assigns Tr(E_o ρ))
For isNull events: δP is UNDEFINED (K9_A assigns no P, QM has no event)
```

### Is δP zero in all realistic EWF scenarios?

**At the probability level: YES.** δP = 0 for all events that have a K9_A probability.

**However:** K9_A predicts **different statistics** from standard QM at the ENSEMBLE level:

```
K9_A ensemble prediction:
  Out of N runs:
  - v_rate · N runs have V=1 → contribute to probability estimation
  - (1 − v_rate) · N runs have V=0 or isNull → excluded from probability estimation

  IF V=0/isNull events are CORRELATED with measurement setting (PP-1 v2 Channel 3):
    Then the effective ensemble (V=1 only) is a BIASED SAMPLE.
    The estimated ⟨A_xB_y⟩ from V=1 events may differ from the
    full-ensemble ⟨A_xB_y⟩ even though each individual P(o|k) = Tr(E_o ρ).

  This is SELECTION BIAS, not probability modification.
  
  Testable via: comparing coincidence rates across measurement settings.
  If N_bhranti varies with setting → selection bias → δS_apparent ≠ 0.
```

### Order of magnitude for EWF

```
K9_A δP (probability level): 0
K9_A δS (statistical level, via selection bias):
  IF v_rate varies by Δv between settings:
    δS ~ Δv · O(1)
  IF v_rate is setting-independent:
    δS = 0 (no distinguishability)
    
  For Proietti (1794 events, σ_S = 0.075):
    To be detectable: δS > 0.075 → Δv > 0.075 (crude estimate)
    With 1794 events: Poissonian σ_N ~ √1794 ~ 42
    Detectable setting-dependent rate variation: > 42/1794 ~ 2.3%
```

---

## STEP 6: EWF RELEVANCE CHECK

### K-state values in EWF

| Observer | cert | V | ⊥_K | K9_A Case |
|---|---|---|---|---|
| **Friend F** (inside lab) | 1 | 1 (initially) | silent (before W measures) | **Case 1** → P = Tr(E_o ρ) |
| **Friend F** (after W measures) | 1 | **0** (K5 ⊥_K fires: W's measurement contradicts F's state) | **fires** | **Case 2** (Bhrānti) → no P |
| **Wigner W** (outside lab) | 1 | 1 | silent | **Case 1** → P = Tr(E_o ρ) |

### Different predictions for F vs W?

**At the probability level: NO.** Both F (V=1) and W (V=1) get Tr(E_o ρ) — but for DIFFERENT ρ (F's state vs W's state). This is standard QM plus K-space perspective structure.

**At the registration level: YES.** F's registration gets K5-voided (V→0) when W measures, producing a Bhrānti event. W's registration remains V=1. This asymmetry IS the K-side formalization of the Wigner's friend paradox.

### Joint probability P(o_F, o_W)?

K9_A alone does NOT define joint probability. K9_A is a SINGLE-K-SPACE probability rule. Joint probability requires either:
- K9_F (colimit, T4-dependent) — separate candidate
- OR: post-hoc composition of F's and W's K-spaces (not axiomatized)

**K9_A's role in joint scenario:** K9_A determines WHICH of F's events survive as V=1 (and thus enter into any joint probability estimation). This is a pre-processing filter, not a joint probability rule.

---

## STEP 7: SPECIAL PROBLEM CHECK (K9_A-specific)

### If v_rate = 1 in all experimental runs (all registrations succeed), does K9_A reduce to Standard QM exactly?

**YES.** If v_rate = 1:
- All events are Case 1 (V=1)
- P(o|k) = Tr(E_o ρ) for all events
- N_bhranti = 0, N_null = 0
- No selection bias (all events included)
- K9_A = Standard QM exactly

**This means:** v_rate = 1 is the DEGENERATE case where K9_A has zero falsifiability at any level. K9_A is only falsifiable IF v_rate < 1 in some experimental scenario.

**EX perspective:** The question "Is v_rate always 1?" translates to "Does Bhrānti ever occur in real experiments?" EX N_QM_VVV_00032 (Bhrānti) is grounded in N_QM_00095 (Decoherence) and N_QM_00102 (Measurement Reversal). In standard lab experiments without EWF structure, Bhrānti does not occur (v_rate = 1). In EWF scenarios where W "undoes" F's measurement, v_rate < 1 is the prediction.

**Critical implication:** K9_A's falsifiability is CONDITIONAL on the EWF scenario being genuinely realized. In Proietti's experiment (photonic observers), the question is whether the type-I fusion gate reversal constitutes genuine K5 ⊥_K firing. If yes → v_rate < 1 and K9_A is testable. If no → v_rate = 1 and K9_A = Standard QM.

---

## STEP 8: VERDICT

```
VERDICT: CONDITIONAL PASS

Satisfies: C-BORN, C-NORM, C-NONDIV, C-PARAM, C-NONNEG (all PASS)
Conditional on: C-TRACE (3 assumptions with EX anchors), C-FALSI (falsifiable
at registration/statistical level only, not probability level)

Modifications required: None — three-case definition is production-ready (PP-1 v2).

Preliminary class: CLASS D — "No probability-level deviation from Standard QM.
Registration-layer and statistical-level observables exist but require
v_rate < 1 in a genuine EWF scenario."

What would make Class C: v_rate < 1 demonstrated or bounded in Proietti data,
with setting-dependent N_bhranti variation producing detectable δS > σ_S.
```

---

## 3-Round RCA Summary

| Round | Finding | Score |
|---|---|---|
| **R1: Constraint Check** | 5/7 PASS, 2/7 CONDITIONAL (C-TRACE, C-FALSI). No FAIL. | **5.0/5** ✅ |
| **R2: Derivation & Distinguishability** | Born rule exact in Case 1. δP=0 always. Selection bias via Channel 3 is the only distinguishability mechanism. | **4.5/5** ✅ |
| **R3: EWF & Special Check** | v_rate=1 → K9_A=QM exactly. Falsifiable only in genuine EWF with K5 ⊥_K firing. F's registration voided by W's measurement is the K-side EWF formalization. | **5.0/5** ✅ |

**All 3 rounds ≥ 4/5. K9-S2 (K9_A) COMPLETE.**
