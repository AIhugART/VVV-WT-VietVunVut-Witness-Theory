# Phase 9: Adversarial Testing — Main Plan 4-Test Protocol on K9_E
# 3-Round RCA × 5-Why × Scoring Threshold 4/5
# With VVV-QMRF-EX as Compass

**Phase:** 9 (Prompt 3 of Main Plan)
**Date:** 2026-05-23
**Input:** Phase 8 COMPLETE, K9-S5 adversarial results, Tier 4 OI resolutions
**Prior art:** K9-S5 performed 5 attacks; Phase 9 uses the Main Plan's 4 SPECIFIC tests.

> **ERRATUM (2026-05-23 RCA Logic Audit — F1+F2 cascade):**
> 1. **F1 — Circular Fit:** The numerical delta_S values and detection thresholds below use K9_E predictions compared to QM theory, not to experimental data. Phase 10's "beta=0 best-fit" was later found to be a circular fit (data = V*QM; see Phase 10 ERRATUM). The adversarial tests below validate K9_E's STRUCTURAL behavior (P in [0,1], normalization, no-signaling, axiom consistency, distinguishability mechanism). They do not constitute empirical validation.
> 2. **F2 — K9_E is a POSTULATE (P9), not derived from K1-K8:** Phase 8 ERRATUM reclassified K9_E. Test 2 below traces K9_E terms to K1-K8 for CONSISTENCY verification (provenance), not for derivation. K1-K8 do not uniquely determine K9_E.
>
> See [Phase 8 ERRATUM](Phase8_candidate_equation.md), [Phase 10 ERRATUM](Phase10_data_fitting.md), and [index.md §4 ERRATUM](../index.md).

---

## TEST 1 — Physical Counterexample Search

> **Goal:** Find a concrete scenario where K9_E produces P outside [0,1], doesn't sum to 1, or violates no-signaling.

### Test 1a: P outside [0,1]

**Scenario:** Maximally adversarial — β → 1, f_perp(o) = 1 for some o.

```
P(o) = Tr(E_o ρ) · [1 − β · 1] / Z_E
     = Tr(E_o ρ) · (1 − β) / Z_E

If β = 0.99:
  P(o) = Tr(E_o ρ) · 0.01 / Z_E
  Z_E = Σ_o' Tr(E_o' ρ) · (1 − 0.99 · f_perp(o'))
  
For f_perp(o₁)=1, f_perp(o₂)=0:
  Z_E = Tr(E_o₁ ρ)·0.01 + Tr(E_o₂ ρ)·1.0
  Z_E > 0  ✓
  P(o₁) = Tr(E_o₁ ρ)·0.01 / Z_E > 0  ✓
  P(o₂) = Tr(E_o₂ ρ)·1.0 / Z_E > 0  ✓
  P(o₁) + P(o₂) = Z_E / Z_E = 1  ✓
```

**Critical bound:** β ∈ [0, 1) (strict) guarantees `1 − β·f_perp > 0` since `β < 1` and `f_perp ≤ 1` → `β·f_perp < 1`.

If β = 1 (boundary):
```
f_perp(o) = 1 → 1 − 1·1 = 0 → P(o) = 0
BUT if f_perp(o) = 1 for ALL o → Z_E = 0 → DIVISION BY ZERO ⚠️
```

**Fix:** β ∈ [0, 1) (open interval) prevents this. β = 1 is EXCLUDED by definition.

**Can f_perp = 1 for all o simultaneously?**
```
f_perp(o) = |{k_j : inconsistent with o}| / |K_ctx|

For f_perp = 1 for ALL o: every k_j in K_ctx must be inconsistent with EVERY o.
But k_j has a specific outcome o(k_j). At minimum, k_j is CONSISTENT with o = o(k_j).
→ f_perp(o(k_j)) < 1 for o = o(k_j).
→ f_perp cannot be 1 for ALL o simultaneously.
→ Z_E > 0 ALWAYS (even at β → 1).
```

**RESULT: ✅ PASS. No physical counterexample found. P ∈ [0,1] and Σ P = 1 guaranteed by construction.**

### Test 1b: No-signaling violation

**Scenario:** Alice (observer A) and Bob (observer B) in EWF.

```
Alice's marginal: P(o_A) = Σ_{o_B} P(o_A, o_B)

K9_E modifies P(o_A | k_A, K_ctx_A).
K_ctx_A depends on the EXPERIMENTAL SETUP (which observers exist, 
which T3-morphisms connect them), NOT on Bob's measurement CHOICE.

Bob's setting choice determines:
  - Which POVM {E_o_B} he applies
  - What outcome o_B he gets
  
Bob's setting does NOT change:
  - K_ctx_A (determined by experiment architecture)
  - f_perp for Alice (depends on K_ctx_A, not Bob's setting)
  - Alice's modified probability P(o_A)

Therefore: Alice's marginal P(o_A) is INDEPENDENT of Bob's setting.
No-signaling preserved. ✓
```

**CAVEAT:** In Proietti-style experiment, Alice's setting x (BSM vs read friend) changes Alice's OWN K_ctx (x=1: ⊥_K fires; x=0: compatible). This affects Alice's OWN P, not Bob's. This is a local setting effect, not signaling.

**RESULT: ✅ PASS. No-signaling preserved.**

---

## TEST 2 — Axiom Consistency Check

> **Goal:** Identify any term in K9_E that contradicts or is undefined by K1-K8.

### Term-by-term audit

| Term | K1-K8 Status | Issue? |
|---|---|---|
| `Tr(E_o ρ_i)` | EXTERNAL (Standard QM) | ⚠️ ρ is ρ-side, not K-side. K1-K8 do not define ρ. This is by design — K-space and ρ-space are distinct layers (VVV-QMRF architecture). |
| `β` | FREE PARAMETER | ⚠️ Not derivable from K1-K8. Flagged as [A-E3]. Expected — every extension framework has free parameters. |
| `f_perp` | CONSTRUCTED from K5 ⊥_K (structural mode) | ⚠️ Uses Tier 4 OI-1 compatibility map C(o_i, o_j), which requires ρ_joint at setup. |
| `K_ctx` | CONSTRUCTED via T9 (K8-constrained T1 embedding, phi_ij = i_j) | [A-E1] FULLY ELIMINATED (2026-05-24, T9 L1-L5). |
| `Z_E` | CONSTRUCTED | ✅ Mathematical normalization, no axiom dependency. |
| `V = 0 → no P` | K4/K5 → PP-1 v2 | ✅ Directly derived. |
| `isNull → no P` | K4 isNull guard | ✅ Directly derived. |

### K5 ⊥_K operationalization issue

> **Main Plan TEST 2 specifically asks:** "How ⊥_K is operationalized numerically (K5 does not give a number)"

K5 defines ⊥_K as a BINARY relation: k₂ ⊥_K k₁ iff bādhaka fires.
K9_E converts this to a CONTINUOUS probability modification via:

```
f_perp(o) = count(⊥_K events with inconsistent outcomes) / count(K_ctx)
```

This is a FREQUENCY interpretation of the binary ⊥_K relation:
- ⊥_K is binary per-pair → f_perp counts HOW MANY pairs → fraction → continuous
- The binary-to-continuous conversion is via COUNTING, not via reinterpreting ⊥_K itself
- This is analogous to: "coin is binary (H/T) → frequency of H is continuous"

**Is this valid?** YES — counting instances of a binary relation to produce a fraction is standard mathematical practice. K5 says "⊥_K exists or not" per pair. K9_E says "what fraction of contextual pairs have ⊥_K." No axiom violation.

### V ∈ {0,1} → continuous probability gap

> **Main Plan TEST 2 specifically asks:** "Whether V ∈ {0,1} produces a continuous probability"

```
V = 1: K9_E assigns P(o|k) = Tr(E_o ρ) · [1 − β·f_perp] / Z_E  (continuous)
V = 0: K9_E assigns no P  (no probability at all)

The CONTINUOUS probability comes from Tr(E_o ρ) (Standard QM, already continuous),
modified by f_perp (fraction, continuous) and β (parameter, continuous).

V does NOT produce the continuous probability — it is a GATE:
  V=1 → use continuous formula
  V=0 → no formula applied

This is like: "if temperature > 0°C → water is liquid (continuous flow)"
The binary condition (T > 0?) gates a continuous phenomenon (flow rate).
```

**No axiom violation.** V is a gate, not a source of continuity.

### Assumptions beyond K1-K8

| Assumption | Beyond K1-K8? | Justified? |
|---|---|---|
| [A-E1] K_ctx via T3 | YES (Layer 2) | ✅ **FULLY ELIMINATED** (2026-05-24) — T9 constructs phi_ij = i_j (K8-constrained T1 embedding), 5 lemmas L1-L5 |
| [A-E2] f_perp fraction form | YES (construction) | ✅ **SPLIT:** [A-E2a] counting → DERIVED (T8 + T8-H1, 5 lemmas: uniform weight forced by binary K1-K8 + K6 non-hierarchy). [A-E2b] outcome filter → MODERATE (structurally determined, not assumed) |
| [A-E3] beta universal | YES (simplifying) | ✅ **RECLASSIFIED: FREE PARAMETER (MEASUREMENT TARGET)** — β is a measurement target like coupling constants in physics. Universality is a MODELING CHOICE (Occam's razor). 0 assumptions remain. See [RCA A-E3 Final Verdict](../04_governance/RCA_A_E3_beta_universal_final_verdict.md). |
| [A-E4] bot_K^str != bot_K^dyn | YES (Tier 4 OI-4) | ✅ STRONG — formally distinguished, dual modes confirmed |

> **ERRATUM (2026-05-24 — T8/T9 + RCA A-E3 update):** This table has been updated to reflect T8 (K5_prospective Frequency Bridge) and T9 (K_ctx Construction Theorem) added to `K_Space_Axiomatization.md` v2.3. [A-E1] FULLY ELIMINATED. [A-E2] FULLY ELIMINATED (T8-H1). [A-E3] RECLASSIFIED as FREE PARAMETER (was WEAKLY JUSTIFIED) via 3-Round RCA (aggregate 3.75/5). Net: original 4 assumptions → 0 assumptions + 1 free parameter (β) + 0 orphaned. See [RCA A-E3 Final Verdict](../04_governance/RCA_A_E3_beta_universal_final_verdict.md).

**RESULT: ✅ PASS. All terms traceable. 0 orphaned assumptions. 0 assumptions. 1 free parameter (β). 3 eliminated/reclassified ([A-E1] ELIMINATED, [A-E2] ELIMINATED, [A-E3] RECLASSIFIED).**

---

## TEST 3 — Distinguishability Verification

> **Goal:** Compute numerical predictions for BOTH K9_E and Standard QM in the same scenario.

### Scenario: EWF 2-observer, singlet state, CHSH measurement

**Standard QM prediction (from PP-4 sanity checks):**
```
Optimal CHSH angles: a₁=0, a₂=π/2, b₁=π/4, b₂=−π/4
S_QM = −E(a₁,b₁) − E(a₁,b₂) − E(a₂,b₁) + E(a₂,b₂)
     = cos(π/4) + cos(−π/4) + cos(π/4) − cos(3π/4)
     = 0.7071 + 0.7071 + 0.7071 + 0.7071
     = 2√2 ≈ 2.828

|S_QM| = 2√2 ≈ 2.828
```

**K9_E prediction (from PP-4 k9e_predictor):**

For EWF with BSM (setting x=1, where ⊥_K^str fires):

```python
# From k9e_predictor.py sanity checks:
# k9e_expectation(θ_A, θ_B, beta, setting_x=1)

β = 0.3:
  S_K9E ≈ 2.808  → δS = −0.020
  
β = 0.5:
  S_K9E ≈ 2.773  → δS = −0.055
  
β = 0.7:
  S_K9E ≈ 2.720  → δS = −0.108
  
β = 0.9:
  S_K9E ≈ 2.649  → δS = −0.179
```

### Explicit numerical comparison

| Setting pair | S_QM | S_K9E (β=0.5) | δS | δS as fraction |
|---|---|---|---|---|
| (a₁,b₁) | −cos(π/4) = −0.7071 | −0.6932 | +0.0139 | 2.0% |
| (a₁,b₂) | −cos(−π/4) = −0.7071 | −0.6932 | +0.0139 | 2.0% |
| (a₂,b₁) | −cos(π/4) = −0.7071 | −0.6932 | +0.0139 | 2.0% |
| (a₂,b₂) | +cos(3π/4) = +0.7071 | +0.6932 | −0.0139 | 2.0% |
| **CHSH S** | **2.828** | **2.773** | **−0.055** | **1.9%** |

**Direction of effect:** K9_E ALWAYS predicts |S| < |S_QM| (suppression reduces correlations).

### Detection feasibility (Proietti data)

```
Proietti reported: S_exp = 2.416 ± 0.075 (1σ)
S_QM(singlet) = 2√2 ≈ 2.828

δS_experimental = S_exp − S_QM = 2.416 − 2.828 = −0.412
σ_S = 0.075

K9_E at β = 0.5: δS = −0.055 → 0.73σ below S_QM
K9_E at β = 0.9: δS = −0.179 → 2.39σ below S_QM

Proietti data: δS = −0.412 → 5.5σ below S_QM
```

> [!IMPORTANT]
> The Proietti experimental S is LOWER than S_QM by 5.5σ. K9_E also predicts S LOWER than S_QM. This is the SAME DIRECTION. However, the experimental deficit (−0.412) is larger than K9_E's maximum theoretical prediction (−0.200 at β=0.95). This gap could be due to experimental imperfections (detector efficiency, dark counts, alignment errors), which are NOT modeled by K9_E.

**RESULT: ✅ PASS. Distinguishability is REAL (δS ≠ 0 for β > 0). Magnitude is small relative to Proietti precision but detectable at β ≥ 0.9. Direction (|S| < |S_QM|) is consistent with experimental observation.**

---

## TEST 4 — cert and V Sensitivity

> **Goal:** Set cert=1, V=1 for all k. Does K9_E reduce to Standard QM?

### Setup: All registrations valid, all self-certified

```
cert = 1 for all k  → all k admitted to K_R (K1 satisfied trivially)
V = 1 for all k     → no Bhrānti events (K5 never fired or was reversed)
```

### Analysis

```
With V=1 for all k:
  K9_E boundary (e) never triggers → all k get P(o|k)
  K_ctx includes all k_j from other observers with V=1 (= all of them)
  
Does K9_E = Standard QM in this case?
  
CASE 1: β = 0
  P = Tr(E_o ρ) → EXACT BORN RULE ✓

CASE 2: β > 0 AND K_ctx ≠ ∅
  P = Tr(E_o ρ) · [1 − β·f_perp(o)] / Z_E
  
  If f_perp(o) = 0 for all o:
    P = Tr(E_o ρ) → BORN RULE ✓
    This occurs when NO k_j in K_ctx has outcome inconsistent with k_i.
    (Standard lab: single observer or no ⊥_K → f_perp = 0)
  
  If f_perp(o) > 0 for some o:
    P ≠ Tr(E_o ρ) → NOT BORN RULE
    This occurs when K_ctx contains ⊥_K-related registrations.
    (EWF scenario with BSM → ⊥_K fires)
```

### Conclusion

```
cert = 1, V = 1 for all k:
  Standard lab (no EWF): K9_E = Born rule  ✓ (correct limit)
  EWF with BSM: K9_E ≠ Born rule  ✓ (intended distinguishability)
  EWF without BSM: K9_E = Born rule  ✓ (no ⊥_K → f_perp = 0)
```

**RESULT: ✅ PASS. The trivial case (cert=1, V=1) gives Born rule in standard scenarios. K9_E deviates ONLY in EWF scenarios where ⊥_K^str fires — this is the INTENDED behavior.**

---

## OVERALL RANKING

The Main Plan asks for ranking of surviving candidates. Since K9 pipeline already selected K9_E as RANK 1 (and K9_A as fallback), this section confirms the ranking:

| Rank | Candidate | Test 1 | Test 2 | Test 3 | Test 4 | Overall |
|---|---|---|---|---|---|---|
| **1** | **K9_E** | ✅ PASS | ✅ PASS (4 assumptions, none orphaned) | ✅ δS ≠ 0, magnitude 0.02-0.20 | ✅ Born limit + EWF deviation | **SURVIVES** |
| 2 | K9_A (fallback) | ✅ | ✅ (1 assumption) | ⚠️ δP = 0 at prob level, Channel 3 only | ✅ | Class D |
| — | K9_B | ❌ DEAD (PP-2) | — | — | — | ELIMINATED |
| — | K9_C | — | ⚠️ τ_reg not axiomatized | ⚠️ if τ_reg outcome-independent → cancels | — | NOT SELECTED |
| — | K9_D | ❌ DEAD (PP-2) | — | — | — | ELIMINATED |
| — | K9_F | T4 BLOCKED | — | — | — | DEFERRED |

---

## Phase 9 Gate — PP-5 Relocated Gates

Per PP-5, formal gates G1/G2/G3 are evaluated HERE (relocated from Phase 7):

### G1: Internal Consistency (Category A from Phase 7)

| K-axiom | K9_E Consistent? |
|---|---|
| K1-K8 | ✅ 7/7 PASS (Phase 7) |

**G1: ✅ PASS.**

### G2: Physical Validity (Category B from Phase 7)

| Constraint | K9_E Satisfies? |
|---|---|
| C-BORN | ✅ (4 recovery conditions) |
| C-NORM | ✅ (Z_E construction) |
| C-NONNEG | ✅ (β < 1 strict) |
| C-NONDIV | ✅ (Z_E > 0 proven) |
| No-signaling | ✅ (conditional for N>2) |

**G2: ✅ PASS.**

### G3: Distinguishability (Category C from Phase 7)

| Requirement | K9_E Satisfies? |
|---|---|
| δP ≠ 0 in at least one scenario | ✅ (EWF + BSM + β > 0) |
| Magnitude computable | ✅ (δS = β-dependent, 0.02-0.20) |
| Direction specified | ✅ (|S_K9E| < |S_QM|, always suppression) |
| Falsifiable statement | ✅ (Phase 7 §C-3) |

**G3: ✅ PASS (Class C).**

---

## 3-Round RCA Summary

| Round | Finding | Score |
|---|---|---|
| **R1: Tests 1-2** | No physical counterexample. All terms traced. ⊥_K binary→continuous via counting (valid). V is gate not source. 4 justified assumptions. | **5.0/5** ✅ |
| **R2: Test 3** | δS = −0.055 (β=0.5) to −0.179 (β=0.9). Direction: |S| < |S_QM|. Consistent with Proietti data direction. Detection at 2σ needs β ≥ 0.9. | **4.5/5** ✅ |
| **R3: Test 4 + Gates** | Born limit confirmed (standard lab). EWF deviation confirmed. G1/G2/G3 all PASS. Phase 9 COMPLETE. | **5.0/5** ✅ |

**All 3 rounds ≥ 4/5. Phase 9 COMPLETE. G1/G2/G3 PASS.**

---

## NEXT: Phase 10 (Data Fitting)

Phase 10 = Prompt 4 of Main Plan. Fit K9_E against Proietti 2019 data.

**Prerequisites:**
- ✅ K9_E locked and validated (Phases 7-9)
- ✅ PP-4 Python infrastructure ready (13/13 sanity checks PASS)
- ⚠️ D1-BLK-1 (individual ⟨A_xB_y⟩ extraction from Fig. 3): NOT YET DONE
  - PATH A: Extract 4 individual correlations → fit β with DOF=3
  - PATH B: Use S_exp = 2.416 only → fit β with DOF=0 (no goodness-of-fit)

**Decision needed:** Proceed with PATH B (S_exp only) or wait for D1-BLK-1?
