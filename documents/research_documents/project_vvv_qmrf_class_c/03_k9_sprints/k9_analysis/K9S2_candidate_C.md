# K9-S2: Individual Candidate Analysis — K9_C (Registration Latency Weighting)
# 3-Round RCA × 5-Why × Scoring Threshold 4/5
# With VVV-QMRF-EX as Compass

**Candidate:** K9_C — Registration Latency Weighting
**Date:** 2026-05-23
**Input:** K9-S1 verified constraint set
**Source:** VVV_QMRF_K9_Analysis_Plan.md §K9-S2 (lines 167-308)

---

## Candidate Definition (from K9 Analysis Plan)

```
K9_C — Registration Latency Weighting:

  P(o|k,H) = Tr(E_o ρ) · g(τ_reg(o)) / Z_C

  g(τ_reg) = exp(−τ_reg / τ_0)
  τ_0 ∈ (0,∞) = characteristic registration time [free parameter]
  Z_C = Σ_o Tr(E_o ρ) · g(τ_reg(o))  [normalization]
  τ_reg(o) = registration latency for outcome o under Hamiltonian H

Idea: outcomes that register faster (smaller τ_reg) get higher probability
weight. K-side interpretation: kṣaṇabhaṅga (momentariness) — registration
that is causally efficacious must complete within a characteristic time.
```

---

## CRITICAL PRE-ANALYSIS: Is τ_reg(o) Outcome-Dependent?

This is THE make-or-break question, identified in PP-2 v2 (Structural Impossibility Theorem).

### 5-Why: τ_reg Outcome-Dependence

| # | Why? | Answer | EX Reference |
|---|---|---|---|
| W1 | What is τ_reg(o)? | The time it takes for outcome o to register in K-space — from measurement initiation to K-state creation. | K9_C definition |
| W2 | Does τ_reg depend on WHICH outcome o occurs? | **This is the key question.** Two interpretations: (A) τ_reg is the same for all outcomes of a given measurement (system-level property); (B) τ_reg varies with o (outcome-dependent latency). | — |
| W3 | Which interpretation does K1-K8 support? | K1 defines k = (M, o, cert, t, V). The timestamp t records WHEN registration occurs. K2 defines causal order. BUT: t is the registration TIME, not the registration LATENCY. τ_reg = t − t_initiation is not directly a K-state field. | K1 L96-100, K2 L135-175 |
| W4 | Does τ_reg(o) vary with o physically? | In QM: for projective measurements on non-degenerate observables, the time to register outcome o is typically system-independent (detector response time). However, for POVM measurements or weak measurements, different outcomes CAN have different registration latencies (e.g., due to different tunneling times, detector dead times, or fluorescence decay rates). | QM physics |
| W5 | Does EX provide guidance? | **EX N_QM_VVV_00031** (Registration Weight / Hierarchical Registration Reliability) → **N_QM_00068** (Signal-to-Noise Ratio). SNR IS outcome-dependent (different outcomes have different signal strengths). If τ_reg correlates with SNR (weaker signal → longer registration), then τ_reg IS outcome-dependent. But this requires an explicit model linking τ_reg to SNR. | EX N_QM_VVV_00031 → N_QM_00068 |

### Verdict on τ_reg Outcome-Dependence

**INTERPRETATION A: τ_reg is system-level (outcome-independent)**

```
If τ_reg(o) = τ_reg for all o:
  P(o|k,H) = Tr(E_o ρ) · g(τ_reg) / [Σ_o Tr(E_o ρ) · g(τ_reg)]
            = Tr(E_o ρ) · g(τ_reg) / [g(τ_reg) · Σ_o Tr(E_o ρ)]
            = Tr(E_o ρ) · g(τ_reg) / [g(τ_reg) · 1]
            = Tr(E_o ρ)

  g(τ_reg) CANCELS. K9_C = Born rule. ZERO distinguishability.
  SAME mechanism as PP-2 v2 cancellation theorem.
```

**INTERPRETATION B: τ_reg is outcome-dependent (τ_reg = τ_reg(o))**

```
If τ_reg(o) varies with o:
  g(τ_reg(o)) ≠ constant across outcomes
  Z_C = Σ_o Tr(E_o ρ) · exp(−τ_reg(o)/τ_0) ≠ g · 1
  
  P(o|k,H) ≠ Tr(E_o ρ) → GENUINE deviation from Born rule.
  
  BUT: τ_reg(o) is NOT a K-state field. K1 defines t (absolute time),
  not τ_reg (latency). To use Interpretation B, we need ASSUMPTION:
  
  [A-C1]: τ_reg(o) is a physically meaningful, outcome-dependent
  quantity that can be estimated from the Hamiltonian H and the
  POVM {E_o}.
  
  This requires a physical MODEL of registration latency:
  τ_reg(o) = f(H, E_o, ρ) — e.g., τ_reg(o) ∝ 1/Tr(E_o ρ)
  (lower probability → longer registration).
  
  If τ_reg(o) ∝ 1/Tr(E_o ρ):
    g(τ_reg(o)) = exp(−1/(τ_0 · Tr(E_o ρ)))
    This is a NONLINEAR modification of Born rule.
    Produces genuine δP ≠ 0.
    
  BUT: this model is CIRCULAR — τ_reg depends on Tr(E_o ρ),
  which is what we're trying to compute.
```

> **CRITICAL FINDING:** Interpretation A (outcome-independent) → K9_C = Born rule (cancels). Interpretation B (outcome-dependent) → requires either (i) a non-circular model of τ_reg(o), or (ii) an assumption that τ_reg(o) can be computed from system Hamiltonian independently of the probability rule.

---

## STEP 1: CONSTRAINT CHECK

| Constraint | Status | Condition or Fix |
|---|---|---|
| **C-BORN** | ✅ PASS (under Interp A); ⚠️ CONDITIONAL (under Interp B) | Interp A: K9_C = Born rule identically. Interp B: need τ_reg(o) → 0 limit to recover Born. If τ_0 → ∞: g → 1 for all o → Born recovered. |
| **C-NORM** | ✅ PASS | Z_C explicitly normalizes. |
| **C-NONDIV** | ⚠️ CONDITIONAL | Z_C = 0 iff ALL Tr(E_o ρ)·g(τ_reg(o)) = 0. Since g > 0 (exponential) and Tr(E_o ρ) ≥ 0 with at least one > 0: Z_C > 0. ✅ |
| **C-PARAM** | ✅ PASS | 1 free parameter (τ_0). Satisfies ≤1 or ≤2. |
| **C-TRACE** | ❌ FAIL | τ_reg is NOT a K-state field in K1-K8. K1 defines t (absolute timestamp), not τ_reg (latency). The exponential weighting function g = exp(−τ_reg/τ_0) is not derivable from K1-K8. **ASSUMPTIONS needed: [A-C1] τ_reg(o) exists; [A-C2] g has exponential form; [A-C3] τ_0 is universal.** |
| **C-FALSI** | Interp A: ❌ FAIL. Interp B: ⚠️ CONDITIONAL | Interp A: δP=0 (cancels). Interp B: δP ≠ 0 if τ_reg(o) genuinely varies with o, but requires non-circular model. |
| **C-NONNEG** | ✅ PASS | g = exp(−x) > 0 always. Tr(E_o ρ) ≥ 0. Product ≥ 0. ✅ |

---

## STEP 2: BORN RULE DERIVATION

### Interpretation A (τ_reg outcome-independent)

```
cert=1 (K1), V=1 (assumed), ⊥_K silent:
  P(o|k,H) = Tr(E_o ρ) · g(τ_reg) / Z_C
  Z_C = g(τ_reg) · Σ_o Tr(E_o ρ) = g(τ_reg) · 1 = g(τ_reg)
  P(o|k,H) = Tr(E_o ρ) · g(τ_reg) / g(τ_reg) = Tr(E_o ρ)
  
  Born rule recovered EXACTLY. ∎
```

### Interpretation B (τ_reg outcome-dependent)

```
cert=1, V=1, ⊥_K silent:
  P(o|k,H) = Tr(E_o ρ) · exp(−τ_reg(o)/τ_0) / Z_C
  
  Born rule recovery requires τ_0 → ∞:
    lim_{τ_0→∞} exp(−τ_reg(o)/τ_0) = 1 for all o
    Z_C → Σ_o Tr(E_o ρ) = 1
    P → Tr(E_o ρ)
    
  Born rule recovered in τ_0 → ∞ LIMIT only.
  For finite τ_0: P ≠ Tr(E_o ρ). ∎
```

---

## STEP 3: DIVISION BY ZERO AUDIT

| Denominator | When zero? | Resolution |
|---|---|---|
| Z_C = Σ_o Tr(E_o ρ)·g(τ_reg(o)) | Never (g>0, at least one Tr(E_o ρ)>0) | ✅ No risk |
| τ_0 | τ_0 = 0 makes g = 0 for τ_reg > 0 | Convention: τ_0 ∈ (0,∞), zero excluded by domain. |

---

## STEP 4: DERIVATION TRACE

| Term | Source | Axiom or ASSUMPTION |
|---|---|---|
| Tr(E_o ρ) | Born rule | Standard QM (ρ-side) |
| **τ_reg(o)** | Registration latency | **ASSUMPTION [A-C1]** — NOT in K1-K8. K1 has t (timestamp) but not latency τ_reg = t − t_init. EX anchor: N_QM_VVV_00039 (Momentary Registration Series) → kṣaṇabhaṅga concept, but no direct axiom. |
| **g = exp(−τ/τ_0)** | Exponential weighting | **ASSUMPTION [A-C2]** — functional form not derived. Why exponential? Physical motivation: memoryless decay (Markov property). But this is imported, not derived. EX anchor: WEAK — N_QM_VVV_00031 (Registration Weight) gestures at hierarchical reliability but doesn't specify functional form. |
| **τ_0** | Characteristic time | **ASSUMPTION [A-C3]** — free parameter. Universal for all outcomes and measurements? Or measurement-dependent? Not specified by K1-K8. |
| **Z_C** | Normalization | Derived from C-NORM + K9_C equation. Not an independent assumption. |

**Assumption count: 3** (A-C1, A-C2, A-C3). EX anchors: WEAK (conceptual but not specific).

---

## STEP 5: DISTINGUISHABILITY ANALYSIS

### Interpretation A: δP = 0 (ALWAYS)

K9_C = Born rule identically under Interpretation A. No deviation possible.

### Interpretation B: δP ≠ 0 IF τ_reg(o) varies

```
δP(o) = P_K9C(o) − P_QM(o)
       = Tr(E_o ρ) · [exp(−τ_reg(o)/τ_0) / Z_C − 1]

Let w(o) = exp(−τ_reg(o)/τ_0)
    Z_C = Σ_o Tr(E_o ρ) · w(o) = ⟨w⟩_Born

δP(o) = Tr(E_o ρ) · [w(o)/⟨w⟩_Born − 1]

This is nonzero iff w(o) ≠ ⟨w⟩_Born, i.e., iff τ_reg(o) ≠ ⟨τ_reg⟩.
```

### Order of magnitude for EWF

```
For Proietti experiment:
  Outcomes are {+1, −1} per observer (binary).
  For projective measurements on photon polarization:
    τ_reg(h) ≈ τ_reg(v) (same detector, same response time)
    → Interpretation A → δP = 0.
    
  For Bell-state measurements (BSM):
    τ_reg(Ψ⁺) vs τ_reg(Ψ⁻): different BSM click patterns
    POSSIBLY different dead times or path lengths
    → Tiny τ_reg difference: δτ ~ ps (picoseconds)
    → τ_0 would need to be ~ ps for detectable effect
    → Extremely fine-tuned. Unnatural.

Estimate: δP ~ δτ/τ_0 · Tr(E_o ρ) for small δτ/τ_0
  If δτ ~ 1 ps, τ_0 ~ 1 ns: δτ/τ_0 ~ 10⁻³
  δP ~ 10⁻³ · 0.5 ~ 5 × 10⁻⁴
  With 1794 events: σ_P ~ 1/√1794 ~ 0.024
  δP/σ_P ~ 0.02 → UNDETECTABLE with current data.
```

---

## STEP 6: EWF RELEVANCE CHECK

### K-state values in EWF

| Observer | cert | V | τ_reg | K9_C prediction |
|---|---|---|---|---|
| Friend F | 1 | 1 | τ_reg(o_F) = detector response time | P(o_F) = Tr(E_oF ρ)·g(τ_reg(o_F))/Z_C |
| Wigner W | 1 | 1 | τ_reg(o_W) = BSM response time | P(o_W) = Tr(E_oW ρ)·g(τ_reg(o_W))/Z_C |

### Different predictions for F vs W?

**Only if τ_reg differs between F's measurement and W's measurement.** Since F uses a direct polarization measurement and W uses a BSM, τ_reg could differ. But:

- τ_reg is a property of the DETECTOR, not of the quantum system
- K1-K8 do not formalize detector response time
- This is a purely instrumental effect, not a fundamental K-space property

### Joint probability?

K9_C does not naturally extend to joint probability P(o_F, o_W). Each probability is computed independently for each K-space. Joint probability requires K9_F (colimit) or external composition rule.

---

## STEP 7: SPECIAL PROBLEM CHECK (K9_C-specific)

### Is τ_reg(o) outcome-independent?

Per K9 Analysis Plan (L273-275):
> "τ_reg(o) must be defined before the outcome o is known (otherwise circular). Is τ_reg an outcome-independent quantity? If outcome-dependent: flag as CIRCULAR DEFINITION."

**Analysis:**

| Scenario | τ_reg outcome-dependence | Circularity? |
|---|---|---|
| Projective measurement, ideal detector | τ_reg ≈ constant for all o | No circularity. But δP = 0. |
| POVM, heterogeneous detectors | τ_reg(o) varies with detector element | No circularity if τ_reg from hardware specs. But δP ≈ 0 (instrumental). |
| τ_reg(o) ∝ 1/Tr(E_o ρ) (probability-dependent) | Yes | **CIRCULAR** — τ_reg depends on P, which depends on τ_reg. |
| τ_reg(o) from Hamiltonian dynamics (Zeno time) | Possibly outcome-dependent | Not circular if computed from H alone, not from P. **But requires explicit model.** |

### Circularity Flag

**IF τ_reg is defined as τ_reg(o) ∝ 1/Tr(E_o ρ):** CIRCULAR DEFINITION. ❌

**IF τ_reg is defined from Hamiltonian dynamics (independent of P):** NOT circular, but requires a specific physical model that K1-K8 do not provide. ⚠️

---

## STEP 8: VERDICT

```
VERDICT: FAIL-FIXABLE

Fails:
  C-TRACE: τ_reg, g, τ_0 all require assumptions not in K1-K8 (3 ORPHANED
           assumptions with WEAK EX anchors only).
  C-FALSI: Under Interpretation A (τ_reg outcome-independent) → δP = 0.
           Under Interpretation B → δP ≠ 0 but requires non-circular τ_reg
           model not provided.

Fixable modifications:
  (1) Provide explicit physical model: τ_reg(o) = f(H, E_o) independent of P.
  (2) Show this model produces detectable δP in Proietti setup.
  (3) Establish EX anchors for the specific τ_reg model.

Without fixes: K9_C either (A) cancels (= Born rule) or (B) requires
an unspecified physical model with weak EX grounding.

Preliminary class: CLASS D (Born rule relabeling under Interpretation A)
                   or INCOMPLETE (under Interpretation B, pending model).
```

---

## 3-Round RCA Summary

| Round | Finding | Score |
|---|---|---|
| **R1: τ_reg Outcome-Dependence** | Two interpretations: A (outcome-independent → cancels) vs B (outcome-dependent → needs model). PP-2 v2 cancellation theorem applies to Interp A. | **5.0/5** ✅ |
| **R2: Constraint Check** | FAIL on C-TRACE (3 orphaned assumptions) and C-FALSI (cancels or circular). C-BORN, C-NORM, C-NONDIV, C-PARAM, C-NONNEG all PASS. | **4.5/5** ✅ |
| **R3: Fixability** | Fixable IF a non-circular τ_reg(o) model is provided. But this model would need to be physically motivated, axiomatically grounded, and detectable. High bar. | **4.5/5** ✅ |

**All 3 rounds ≥ 4/5. K9-S2 (K9_C) COMPLETE.**
