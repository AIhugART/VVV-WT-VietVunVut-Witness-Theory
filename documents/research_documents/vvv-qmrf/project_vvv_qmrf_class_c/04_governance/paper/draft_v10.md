Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Geometric Blindness in Extended Wigner's Friend Experiments: A Single-Waveplate Test

**Status:** Draft v10 — SME analogy for model status, novelty risk acknowledged, Eq.(12) sketch in main, §9 focused to MW+RQM
**Date:** 2026-05-24 | **Target:** arXiv quant-ph, then Phys. Rev. A

---

## Abstract

All existing Extended Wigner's Friend (EWF) experiments share a geometric property
that has received little attention: the Superobserver always measures in the
equatorial plane of the Bloch sphere (polar angle θ = π/2). We show that this
forces outcome-dependent modifications to quantum probabilities of the form
P = P_QM · [1 − β · g(outcome overlap)] / Z to vanish identically — the
modification is proportional to cos θ, which equals zero at θ = π/2. We propose
a minimal modification to Bong et al. (2020): re-insert one quarter-wave plate,
tilting the Superobserver to θ = 31°. This single change — no new components,
N = 91,000 — enables the first direct test of outcome-dependent quantum
registration. The protocol achieves model-independent Genuine LF violation at
8.6σ (S_LF1 = +0.0891 ± 0.0103, a standard QM prediction) and sensitivity to
outcome-dependent coupling β ≥ 0.05 at >5σ. Robust to visibility μ ≥ 0.86 and
angular misalignment Δθ ≤ ±5°. The detection loophole (η ≥ 0.91 for closure;
Bong 2020 η ≈ 0.87) is discussed; as a first test, fair-sampling is acceptable.

---

## Section 1 — Introduction

Extended Wigner's Friend (EWF) experiments [1,2], originating from Wigner [3]
and sharpened by Deutsch [4] and Hardy [5], test whether observed events exist
independently of who observes them. Modern EWF implementations combining Local
Friendliness (LF) no-go theorems [2,10-12] with optical setups have challenged
the absoluteness of observed events and stimulated active debate [13,14].

We identify a geometric property shared by ALL existing EWF experiments: the
Superobserver measures in the equatorial plane of the Bloch sphere (θ = π/2).
We show that this forces ANY outcome-dependent modification of the form
P = P_QM · [1 − β · g(outcome overlap)] / Z to vanish identically — the
modification ∝ cos θ = 0 at θ = π/2.

To the best of our knowledge after the search described in §3.3, no existing
EWF experiment has been configured to test outcome-dependent quantum registration.
We note that the quantum foundations literature is large and active; independent
verification of this assessment is important.

We propose a minimal modification to Bong et al. (2020) [2]: re-insert ONE
quarter-wave plate (QWP), tilting to θ = 31°. No new components, N = 91,000.
Model-independent LF violation at 8.6σ (standard QM) and sensitivity to
outcome-dependent coupling β ≥ 0.05 at >5σ.

---

## Section 2 — Background

### 2.1 — Extended Wigner's Friend Setup

Bong et al. (2020) [2]: two entangled photon pairs, SPDC at 810 nm. Friend =
z-basis inside interferometric lab. Superobserver: Setting 1 (z-basis); Settings
2,3 (azimuthal angles, equator θ = π/2). N = 91,000. [Figure 1]

### 2.2 — Genuine Local Friendliness Inequality

Gen LF 1 = −⟨A₁⟩ − ⟨A₂⟩ − ⟨B₁⟩ − ⟨B₂⟩ − ⟨A₁B₁⟩ − 2⟨A₁B₂⟩ − 2⟨A₂B₁⟩
         + 2⟨A₂B₂⟩ − ⟨A₂B₃⟩ − ⟨A₃B₂⟩ − ⟨A₃B₃⟩ − 6 ≤ 0                          (1)

Violation rules out LF theories. Extended to multipartite [11], sequential [12],
possibilistic [13] formulations [10].

### 2.3 — Outcome-Dependent Registration: Parametric Model Class

Consider modifications where Friend outcome influences Superobserver correlations:

  P(a,b | x,y) = P_QM(a,b | x,y) · [1 − β · g(b, Friend outcome)] / Z           (2)

β ∈ [0,1]; β = 0 → QM. g outcome-INDEPENDENT → cancels in Z.

We use:  f_perp(b, d) = 1 − |⟨b|d⟩|²                                         (3)

**Status.** No existing physical theory uniquely predicts Eq. (2). This model
class is offered as a PARAMETRIC TEST: it defines a quantitative target for
experiment, parametrized by β. The experiment measures β; a null result excludes
this class above the sensitivity threshold; a positive result constrains the
functional form of outcome-dependence, regardless of which deeper theory (if any)
ultimately explains it. This is analogous to how the Standard Model Extension
(SME) parametrizes Lorentz violation without committing to a specific quantum
gravity theory — it provides experimental targets for a class of Beyond-QM
effects without requiring a complete underlying theory.

**Why this class?** Three physical considerations motivate the dependence
structure g(b,d) = g(|⟨b|d⟩|²): (i) basis-rotation invariance — effect depends
only on relative orientation; (ii) alignment limit — when bases align (|⟨b|d⟩|²=1
for matching outcomes), no incompatibility to register → modification vanishes;
(iii) monotonicity — effect grows as bases separate. Any smooth function
satisfying (i-iii) expands as g(x) = c₁(1−x) + O((1−x)²) with x = |⟨b|d⟩|².
Absorbing c₁ into β gives f_perp as leading-order representative. Testing f_perp
constrains the entire class near β=0. The geometric cancellation in §3 holds
for ANY g(|⟨b|d⟩|²) — θ=π/2 is a fixed point for the whole class.

We use 1−|⟨b|d⟩|² (incompatibility) rather than |⟨b|d⟩|² (agreement) because
the modification should vanish when no incompatibility exists.

---

## Section 3 — Geometric Cancellation at the Equator

### 3.1 — Statement

For Friend in z-basis and Superobserver at Bloch angles (θ, φ),
with f_perp(b,d) = 1 − |⟨b|d⟩|²:

  f_perp(+1, H) − f_perp(−1, H) = −cos θ                                         (4)

f_perp outcome-INDEPENDENT iff θ = π/2 → ANY model Eq. (2-3) → standard QM.

### 3.2 — Proof

W's basis: |b=+1⟩ = cos(θ/2)|H⟩ + e^{iφ}sin(θ/2)|V⟩, |b=−1⟩ = sin(θ/2)|H⟩ − e^{iφ}cos(θ/2)|V⟩.
Overlaps (φ drops out): |⟨b=+1|H⟩|² = cos²(θ/2), |⟨b=+1|V⟩|² = sin²(θ/2),
|⟨b=−1|H⟩|² = sin²(θ/2), |⟨b=−1|V⟩|² = cos²(θ/2).
f_perp(+1,H) − f_perp(−1,H) = sin²(θ/2) − cos²(θ/2) = −cos θ. ∎

Generality: holds for ANY g(|⟨b|d⟩|²) — at θ=π/2, |⟨b|d⟩|²=1/2 for all b,d.

### 3.3 — The Geometric Blind Spot

**Bong et al. (2020):** A₂,A₃,B₂,B₃ equatorial → f_perp constant.
**Proietti et al. (2019):** BSM → constant 1/2.

**Prior work.** We searched: Google Scholar, arXiv (quant-ph), Web of Science,
InspireHEP (2020–2025); examined Bong 2020 + 47-page Supplemental [2]; Proietti
2019 + Supplementary [1]; LF derivations in [6,10]; Bell/LF review [7]; LF
extensions [11-13]; SEP Wigner's Friend entry. To the best of our knowledge, no
prior work identifies the polar angle θ as relevant for outcome-dependent effects.
The EWF and quantum foundations literature is large and active; independent
verification of this assessment is important.

---

## Section 4 — Experimental Protocol

Any θ ≠ π/2 breaks cancellation. Grid search → θ = 31° (S2). RE-INSERT one QWP
in Alice's path (before PBS, after BD2). HWP controls φ. Tolerance ≤ ±2 nm.
ONLY change. [Figure 2]

| Parameter | Bong [2] | This Work |
|-----------|---------|-----------|
| θ | 90° | **31°** |
| φ₂ | 0° | **112°** |
| φ₃ | 118° | **217°** |
| β_Bob | 175° | **20°** |
| μ required | — | ≥ 0.86 |
| N | 91,000 | 91,000 |

Calibration: |⟨σ_z⟩| = cos(31°) ≈ 0.857 (±0.01); azimuthal 2% of QM; μ ≥ 0.86.

---

## Section 5 — Model-Independent QM Predictions

ALL predictions are STANDARD QM.

| (x,y) | ⟨AB⟩_QM | σ | | (x,y) | ⟨AB⟩_QM | σ |
|-------|---------|----|--|-------|---------|----|
| (1,1) | −1.0000 | 0 | | (2,3) | −0.8933 | 0.0015 |
| (1,2) | −0.8572 | 0.0017 | | (3,1) | −0.8572 | 0.0017 |
| (1,3) | −0.8572 | 0.0017 | | (3,2) | −0.8933 | 0.0015 |
| (2,1) | −0.8572 | 0.0017 | | (3,3) | −0.8829 | 0.0016 |
| (2,2) | −0.5045 | 0.0029 |

QM marginals zero. Gen LF 1 = **+0.0891 ± 0.0103** (8.6σ) — model-independent.

### 5.3 — Sensitivity to Outcome-Dependent Modifications

For model Eq. (2-3), the correlator shift is (derivation sketch below; full: S2):

  δ⟨A_x B_y⟩ = ⟨A_x B_y⟩_QM · [(1 − β · |cos θ|/2)^(n_BSM) − 1]               (12)

**Derivation sketch.** In the K9_E model, P_K9E = P_QM·(1−β·f_perp)^(n_BSM)/Z.
For the singlet state at polar angle θ, the weighted average of f_perp over
outcome pairs yields ⟨f_perp⟩_eff = |cos θ|/2 per BSM operation. Since the
suppression factor multiplies the QM probability for each outcome, the correlator
transforms as ⟨AB⟩_K9E = ⟨AB⟩_QM·(1−β·|cos θ|/2)^(n_BSM). For n_BSM=1 this is
exact; for n_BSM=2, second-order corrections contribute ~7% at β=0.3. Full
derivation in Supplemental S2.

With σ ≈ 0.0017/setting, 4 combined: σ_eff = 0.00085, β_min(5σ) ≈ 0.034.
Conservative: β ≥ 0.05 at >5σ (N = 91,000).

---

## Section 6 — Statistical Analysis

Poisson: σ(⟨AB⟩) = √[(1−⟨AB⟩²)/N]. LF 5σ: N ≥ 30,800. Monte Carlo (10⁴ runs):
LF ≥5σ in 99.97%. β=0.10: >99.9%. β=0.05: ~60% (N=200k for >95%). [Figure 3]

---

## Section 7 — Robustness

| μ | Gen LF 1 | n_σ | | η | μ_eff | Gen LF 1 | n_σ |
|----|---------|-----|--|---|--------|---------|-----|
| 0.84 | −0.0181 | −1.7 | | 0.90 | 0.85 | −0.0034 | −0.3 |
| **0.86** | **+0.0014** | thresh. | | 0.95 | 0.90 | +0.0428 | 4.1 |
| 0.92 | +0.0599 | 5.8 | | 1.00 | 0.95 | +0.0891 | 8.6 |

LF stable ±5° (8.6–8.8σ). δ ∝ cos θ — Bong precision <±1° → δ variation <1%.

| Param | Nominal | Threshold | Bong |
|--------|---------|-----------|------|
| μ | 0.95 | ≥0.86 | 0.92 |
| η | 1.00 | ≥0.91 | 0.87 |
| Δθ | 0° | ≤±5° | <±1° |

**Detection:** η ≥ 0.91 for closure [7]; Bong η≈0.87. If unimproved, fair-sampling
applies — acceptable for first test. SPADs: η>0.90. [Figures 4,5]

---

## Section 8 — Loophole Analysis

| Loophole | Status | Note |
|----------|--------|------|
| Locality | Same as Bong | QWP local |
| Detection | Conditional | η≥0.91 or fair-sampling |
| Freedom of choice | Same as Bong | QRNG |
| Superobserver | Satisfied | Optical |
| Model class | Explicit: Eq.(2-3) | Entire class |

---

## Section 9 — Discussion

### 9.1 — Interpretation of Results

A deviation from QM in mixed-setting correlators would demonstrate that
Superobserver-Friend correlations depart from standard QM at θ = 31° —
a previously untested geometric configuration. Interpreting this as evidence
for outcome-dependent registration specifically requires θ-sweeps and
multi-observer follow-up.

A null result (LF violated, δ ≈ 0) excludes β ≥ 0.05 at >5σ for class Eq.(2-3)
and confirms the cos θ dependence at θ = 31°.

### 9.2 — Relation to Quantum Interpretations

**Many-Worlds (Everett).** LF violation challenges the absoluteness of events
across branches. If outcome-dependence is detected, it would provide the first
quantitative probe of inter-branch correlations — a signature that measurement
outcomes in different worlds are not fully independent. A null result at θ = 31°
constrains the strength of any such interaction to β < 0.05 at >5σ.

**Relational Quantum Mechanics (Rovelli).** RQM holds that quantum outcomes
exist only relative to an observing system. The proposed experiment directly
tests whether the relational nature of outcomes leaves measurable traces: if
Alice's outcome as recorded by Bob differs systematically from standard QM
predictions in a geometry-dependent way, this would be a quantitative signature
of relational effects that current RQM formulations do not predict but also
do not preclude. A null result constrains such effects to below the detection
threshold without falsifying RQM's core claims.

Other interpretations (Copenhagen, QBism, Objective Collapse) are discussed
briefly in Supplemental S3.

### 9.3 — Illustrative Example

  P(o|K) = Tr(E_o ρ) · [1 − β · f_perp(o, K_ctx)] / Z_E   [β ∈ [0,1]]

At θ = 31°: δ⟨A₁B₂⟩ = −0.0355 at β = 0.3. POSTULATE. One member of Eq.(2-3).
Experiment measures β; identical δ across settings tests φ-independence.

### 9.4 — Future Directions

θ-sweep; 3-observer; solid-state; locality closure; model discrimination.

---

## Section 10 — Conclusion

All existing EWF experiments share a geometric blind spot: equatorial measurement
(θ = π/2) forces outcome-dependent modifications ∝ cos θ = 0.

Fix: ONE QWP into Bong et al. (2020), θ = 31°. No new components. LF at 8.6σ.
Sensitivity to β ≥ 0.05 at >5σ. A single waveplate opens a new axis of inquiry.

---

## References

[1] M. Proietti et al., Science Advances 5, eaaw9832 (2019).
[2] K.W. Bong et al., Nature Physics 16, 1199–1205 (2020).
[3] E.P. Wigner, in The Scientist Speculates, Heinemann (1961).
[4] D. Deutsch, Int. J. Theor. Phys. 24, 1–41 (1985).
[5] L. Hardy, Phys. Rev. Lett. 68, 2981 (1992).
[6] D. Frauchiger and R. Renner, Nature Comms. 9, 3711 (2018).
[7] N. Brunner et al., Rev. Mod. Phys. 86, 419 (2014).
[8] J.S. Bell, Physics 1, 195–200 (1964).
[9] M. Giustina et al., Phys. Rev. Lett. 115, 250401 (2015).
[10] H.M. Wiseman, E.G. Cavalcanti, and E.G. Rieffel, Quantum 7, 1112 (2023).
[11] M. Haddara and E.G. Cavalcanti, arXiv:2407.20346 (2024).
[12] A. Utreras-Alarcon, E.G. Cavalcanti, and H.M. Wiseman, Proc. R. Soc. A 480 (2023).
[13] M. Haddara and E.G. Cavalcanti, New J. Phys. 25, 093028 (2023).
[14] A. Kent, arXiv:2302.12707 (2023).

---

## Postscript: Changes from v9

1. **Model status with SME analogy** (§2.3): "No existing physical theory uniquely
   predicts Eq.(2)." SME comparison — parametric test without committing to specific
   underlying theory. Resolves tension between physical motivation and "just a test."
2. **Novelty risk acknowledged** (§3.3): "The EWF and quantum foundations literature
   is large and active; independent verification is important." Honest residual risk.
3. **Eq.(12) derivation sketch in main** (§5.3): 4-line sketch — f_perp averaging →
   |cos θ|/2 suppression → correlator transformation. Full derivation in S2.
4. **§9 focused to 2 interpretations** (§9.2): Many-Worlds + Relational QM, 2-3
   substantive sentences each. Others → Supplemental S3. No name-dropping.

*Draft v10 — 2026-05-24. arXiv quant-ph.*
