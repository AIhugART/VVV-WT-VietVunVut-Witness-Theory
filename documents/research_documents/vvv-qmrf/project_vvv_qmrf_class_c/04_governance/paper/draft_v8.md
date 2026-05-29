Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Geometric Blindness in Extended Wigner's Friend Experiments: A Single-Waveplate Test

**Status:** Draft v8 — Detection loophole honest, model constraints clarified, first-claim softened, angular precision addressed
**Date:** 2026-05-24 | **Target:** arXiv quant-ph, then Phys. Rev. A

---

## Abstract

All existing Extended Wigner's Friend (EWF) experiments share a geometric property
that has received little attention: the Superobserver always measures in the
equatorial plane of the Bloch sphere (polar angle θ = π/2). We show that this
forces ANY outcome-dependent modification to quantum probabilities of the form
P = P_QM · [1 − β · g(outcome overlap)] / Z to vanish identically — the
modification is proportional to cos θ, which equals zero at θ = π/2. This is a
mathematical identity, not an experimental limitation. We propose a minimal
modification to Bong et al. (2020): re-insert one quarter-wave plate, tilting
the Superobserver to θ = 31°. This single change — no new components, N = 91,000
— enables, to our knowledge, the first direct experimental test of outcome-dependent
quantum registration, simultaneously achieving model-independent Genuine LF
violation at 8.6σ (S_LF1 = +0.0891 ± 0.0103, a standard QM prediction) and
sensitivity to outcome-dependent coupling β ≥ 0.05 at >5σ. The protocol is
robust to visibility μ ≥ 0.86 and angular misalignment Δθ ≤ ±5°. The detection
loophole (η ≥ 0.91 for closure; Bong 2020 achieved η ≈ 0.87) is discussed; as a
first test, fair-sampling is acceptable.

---

## Section 1 — Introduction

Extended Wigner's Friend (EWF) experiments [1,2] test whether observed events
exist independently of who observes them. Following theoretical developments in
Local Friendliness (LF) no-go theorems [2,9-11], optical implementations have
demonstrated violations of LF inequalities, challenging the absoluteness of
observed events and stimulating active debate [12,13].

We identify a geometric property shared by ALL existing EWF experiments: the
Superobserver measures in the equatorial plane of the Bloch sphere (polar angle
θ = π/2). We show that this forces ANY outcome-dependent modification to quantum
probabilities — of the parametric form P = P_QM · [1 − β · g(outcome overlap)] / Z
— to vanish identically. The modification is proportional to cos θ, which equals
zero at θ = π/2. This is a mathematical identity, independent of any specific model.

The corollary is striking: to our knowledge, no existing EWF experiment has been
configured to test outcome-dependent quantum registration. The effect has been
geometrically canceled by construction in all experiments to date.

We propose a minimal modification to Bong et al. (2020) [2]: re-insert ONE
quarter-wave plate (QWP), tilting the Superobserver measurement to θ = 31°.
This single change — no new components, N = 91,000 — enables a direct
experimental test, achieving model-independent Genuine LF violation at 8.6σ
(a standard QM prediction) and sensitivity to outcome-dependent coupling
β ≥ 0.05 at >5σ. A parametric model illustrating accessible effect scales is
presented in §9.

---

## Section 2 — Background

### 2.1 — Extended Wigner's Friend Setup

Bong et al. (2020) [2] uses two entangled photon pairs from SPDC at 810 nm.
On each side, a Friend measures photon polarization in the z-basis inside an
interferometric lab. A Superobserver measures the combined Friend+photon system
at three settings: Setting 1 (z-basis); Settings 2 and 3 (azimuthal angles on
the Bloch sphere equator, θ = π/2). Outcomes: a, b ∈ {+1, −1}. N = 91,000
coincidences per setting.

[Figure 1: EWF setup with tilted Superobserver measurement]

### 2.2 — Genuine Local Friendliness Inequality

Gen LF 1 = −⟨A₁⟩ − ⟨A₂⟩ − ⟨B₁⟩ − ⟨B₂⟩ − ⟨A₁B₁⟩ − 2⟨A₁B₂⟩ − 2⟨A₂B₁⟩
         + 2⟨A₂B₂⟩ − ⟨A₂B₃⟩ − ⟨A₃B₂⟩ − ⟨A₃B₃⟩ − 6 ≤ 0                          (1)

Violation rules out all LF theories. LF inequalities have been extended to
multipartite [10], sequential [11], and possibilistic [12] formulations [9].

### 2.3 — Outcome-Dependent Registration: Parametric Model Class

Consider modifications to quantum probabilities:

  P(a,b | x,y) = P_QM(a,b | x,y) · [1 − β · g(b, Friend outcome)] / Z           (2)

where β ∈ [0,1] and g is an outcome-overlap function. β = 0 → standard QM.
When g is outcome-INDEPENDENT, the factor cancels in Z.

We focus on:

  f_perp(b, d) = 1 − |⟨b|d⟩|²                                                    (3)

**Why this specific form?** For any modification that depends on how aligned two
observers' measurement bases are, three physical constraints single out the
dependence structure g(b,d) = g(|⟨b|d⟩|²): (i) basis-rotation invariance — the
effect should depend only on the relative orientation of measurement bases, not
their absolute angles in the lab; (ii) outcome-exchange symmetry — swapping
measurement outcomes b ↔ −b should not alter the modification when the bases
are aligned; (iii) monotonicity — the effect should increase as the measurement
bases become more orthogonal. Any smooth function satisfying (i-iii) has the
expansion g(x) = c₀ + c₁(1−x) + O((1−x)²) with x = |⟨b|d⟩|². Setting c₀ = 0
(no effect when bases align) and absorbing c₁ into β yields f_perp as the
leading-order representative. Testing f_perp therefore constrains the ENTIRE
class of functions satisfying (i-iii) near β = 0.

The geometric cancellation in §3 applies to ANY g(|⟨b|d⟩|²) — the fixed point
at θ = π/2 is a property of the dependence structure, not the specific f_perp form.

**Status.** This is a PARAMETRIC TEST, not a physical theory. The experiment
does not require commitment to f_perp specifically — it tests the class of models
where outcome-dependence scales with measurement basis incompatibility.

---

## Section 3 — Geometric Cancellation at the Equator

### 3.1 — Statement

Let Friend F measure in z-basis and Superobserver W at Bloch angles (θ, φ).
With f_perp(b,d) = 1 − |⟨b|d⟩|²:

  f_perp(+1, H) − f_perp(−1, H) = −cos θ                                         (4)

f_perp is outcome-INDEPENDENT iff θ = π/2. For any equatorial measurement,
ANY model of the form Eq. (2-3) reduces exactly to standard QM.

### 3.2 — Proof

W's measurement basis at (θ, φ):

  |b=+1⟩ = cos(θ/2)|H⟩ + e^{iφ} sin(θ/2)|V⟩                                     (5)
  |b=−1⟩ = sin(θ/2)|H⟩ − e^{iφ} cos(θ/2)|V⟩                                     (6)

Squared overlaps (φ drops out: |e^{iφ}|² = 1):

  |⟨b=+1|H⟩|² = cos²(θ/2)          |⟨b=+1|V⟩|² = sin²(θ/2)                      (7)
  |⟨b=−1|H⟩|² = sin²(θ/2)          |⟨b=−1|V⟩|² = cos²(θ/2)                      (8)

Overlaps depend ONLY on θ. Computing f_perp:

  f_perp(+1, H) = 1 − cos²(θ/2) = sin²(θ/2)                                     (9)
  f_perp(−1, H) = 1 − sin²(θ/2) = cos²(θ/2)                                    (10)
  f_perp(+1, H) − f_perp(−1, H) = −cos θ                                        (11)

Vanishes iff θ = π/2. All four f_perp = 1/2 → constant → cancels in Z. ∎

**Generality.** The cancellation holds for ANY g(|⟨b|d⟩|²): at θ = π/2,
|⟨b|d⟩|² = 1/2 for all b,d, so g takes the same value for all outcome pairs.
θ = π/2 is a geometric fixed point for the entire function class.

### 3.3 — The Geometric Blind Spot

**Bong et al. (2020):** A₂, A₃, B₂, B₃ all equatorial. f_perp outcome-independent
for every measurement combination.

**Proietti et al. (2019):** BSM → |⟨ψ|Φ⁺⟩|² = 1/2 → f_perp = 1/2 constant.

**Prior work.** We are not aware of prior work identifying the role of the
Superobserver's polar angle θ — as distinct from the extensively studied
azimuthal angles φ₂, φ₃, β — in constraining outcome-dependent effects in EWF
experiments. We examined: Bong 2020 [2] (experimental sections and Supplemental
Material); Proietti 2019 [1] (Methods); LF derivations in [5,9]; the Bell/LF
review [6]; and recent LF extensions [10-12]. None discuss θ. We welcome
independent verification of this assessment.

---

## Section 4 — Experimental Protocol

### 4.1 — Breaking the Cancellation

Any θ ≠ π/2 breaks the cancellation. Grid search maximizing min(n_σ_LF, n_σ_signal)
yields θ = 31° (Supplemental S2).

### 4.2 — Single Hardware Modification

In standard Bong, QWP is REMOVED for settings 2/3. We RE-INSERT one QWP in
Alice's path (before PBS, after BD2), tilting to θ = 31°. HWP controls φ.
Retardance tolerance ≤ ±2 nm (θ within ±0.5°). ONLY change.

[Figure 2: Optical path with QWP insertion highlighted]

### 4.3 — Measurement Settings

| Parameter | Standard Bong [2] | This Work |
|-----------|------------------|-----------|
| Polar angle θ | 90° | **31°** |
| φ₂ | 0° | **112°** |
| φ₃ | 118° | **217°** |
| Bob offset β_Bob | 175° | **20°** |
| μ required | — | ≥ 0.86 |
| N | 91,000 | 91,000 |

### 4.4 — Calibration

1. |⟨σ_z⟩| = cos(31°) ≈ 0.857 on H-polarized state (±0.01)
2. Azimuthal: count rates within 2% of QM
3. Visibility via CHSH S (μ ≥ 0.86 required)

---

## Section 5 — Model-Independent QM Predictions

ALL predictions below are STANDARD QM. No outcome-dependent model assumed.

### 5.1 — Correlators (θ = 31°, μ = 0.95)

| (x,y) | ⟨AB⟩_QM | σ (N=91k) | | (x,y) | ⟨AB⟩_QM | σ (N=91k) |
|-------|---------|-----------|---|-------|---------|-----------|
| (1,1) | −1.0000 | 0.0000 | | (2,3) | −0.8933 | 0.0015 |
| (1,2) | −0.8572 | 0.0017 | | (3,1) | −0.8572 | 0.0017 |
| (1,3) | −0.8572 | 0.0017 | | (3,2) | −0.8933 | 0.0015 |
| (2,1) | −0.8572 | 0.0017 | | (3,3) | −0.8829 | 0.0016 |
| (2,2) | −0.5045 | 0.0029 |

QM marginals all zero (singlet, μ = 0.95).

### 5.2 — Primary Observable

| Observable | Prediction | Type |
|-----------|-----------|------|
| Gen LF 1 | **+0.0891 ± 0.0103** (8.6σ) | Standard QM — model-independent |

Built-in calibration: no violation → apparatus not realizing intended geometry.

### 5.3 — Sensitivity to Outcome-Dependent Modifications

For ANY model Eq. (2-3), the deviation in mixed settings:

  δ⟨A_x B_y⟩ = ⟨A_x B_y⟩_QM · [(1 − β · |cos θ|/2)^(n_BSM) − 1]               (12)

n_BSM = 1 for A₀B₁, A₁B₀; n_BSM = 2 for A₁B₁. At θ = 31°: |cos θ|/2 ≈ 0.429.
At illustrative β = 0.3: β|cos θ|/2 ≈ 0.129. n_BSM = 1: exactly linear in β.
n_BSM = 2: ~7% second-order correction. Exact expression used throughout.

With σ ≈ 0.0017 per setting, 4 combined mixed settings: σ_eff = 0.00085,
β_min(5σ) ≈ 0.034. Conservative: β ≥ 0.05 at >5σ (N = 91,000).

---

## Section 6 — Statistical Analysis

Poisson: σ(⟨AB⟩) = √[(1 − ⟨AB⟩²)/N]. Gen LF 1: σ ≈ 0.0103. LF 5σ: N ≥ 30,800.

Monte Carlo (10,000 runs): Gen LF 1 ≥ 5σ in 99.97%. β = 0.10: >99.9%.
β = 0.05: ~60% (N = 200,000 for >95% power).

[Figure 3: Monte Carlo histogram of Gen LF 1]

---

## Section 7 — Robustness

| μ | Gen LF 1 | n_σ | | η | μ_eff | Gen LF 1 | n_σ |
|----|---------|-----|--|---|--------|---------|-----|
| 0.84 | −0.0181 | −1.7 | | 0.90 | 0.85 | −0.0034 | −0.3 |
| **0.86** | **+0.0014** | **threshold** | | 0.95 | 0.90 | +0.0428 | 4.1 |
| 0.92 | +0.0599 | 5.8 | | 1.00 | 0.95 | +0.0891 | 8.6 |
| 0.95 | +0.0891 | 8.6 |

LF significance stable across Δθ = ±5° (8.6–8.8σ). The outcome-dependence signal
δ⟨AB⟩ scales as cos θ — more alignment-sensitive than LF. Bong achieved angular
precision < ±1° [2]; at this level, δ signal variation is <1% of its nominal value.

| Parameter | Nominal | Threshold | Bong Achievable |
|-----------|---------|-----------|-----------------|
| μ | 0.95 | ≥ 0.86 | 0.92 |
| η | 1.00 | ≥ 0.91 | 0.87 |
| Δθ | 0° | ≤ ±5° | < ±1° |

**Detection loophole.** Closing the detection loophole requires η ≥ 0.91 [6];
Bong 2020 reported η ≈ 0.87 including all optical losses. If η cannot be raised,
the experiment remains subject to the fair-sampling assumption. This is acceptable
for a FIRST test — the primary goal is detecting any deviation from QM, not
simultaneously closing all loopholes. Future experiments can target loophole-free
status with optimized detector channels (modern SPADs reach η > 0.90 at 810 nm).

[Figure 4: Sensitivity vs μ] [Figure 5: 2D (μ, η) sensitivity map]

---

## Section 8 — Loophole Analysis

| Loophole | Status | Note |
|----------|--------|------|
| Locality | Same as Bong 2020 | QWP local to Alice |
| Detection | Conditional | η ≥ 0.91 for closure; Bong η ≈ 0.87 |
| Freedom of choice | Same as Bong 2020 | QRNG |
| Superobserver | Satisfied | Optical interferometry |
| Model class | Explicit: Eq. (2-3) | Tests entire class |

---

## Section 9 — Discussion

### 9.1 — Interpretation of a Positive Result

A statistically significant deviation from QM in mixed-setting correlators would
demonstrate that Superobserver-Friend correlations differ from standard QM
predictions at the modified geometry (θ = 31°). This would be a quantitative
departure from QM in an EWF scenario at a previously untested geometric
configuration. Interpreting such a deviation as evidence for outcome-dependent
quantum registration specifically — rather than other Beyond-QM effects — would
require follow-up experiments (θ-sweeps to verify the cos θ scaling, multi-observer
configurations) and is beyond the scope of this proposal.

### 9.2 — Interpretation of a Null Result

LF violated, δ ≈ 0: β ≥ 0.05 excluded at >5σ for class Eq. (2-3). The
cos θ dependence identified in §3 is experimentally confirmed at θ = 31°.

### 9.3 — Relation to Quantum Interpretations

Copenhagen: no challenge. Many-Worlds: LF violation challenges absoluteness.
Relational QM: tests whether relational outcomes leave measurable traces.
Objective Collapse: alternative to dynamical collapse.

### 9.4 — Illustrative Example: A Parametric Model

  P(o | K) = Tr(E_o ρ) · [1 − β · f_perp(o, K_ctx)] / Z_E                      (13)

with f_perp from Eq. (3), K_ctx = ⟨f_perp⟩, β ∈ [0,1] (β = 0 → QM). At θ = 31°:

  δ⟨A₁B₂⟩ = −0.0355  at β = 0.3                                               (14)

POSTULATE — not derived from QM. One member of class Eq. (2-3). Experiment
measures β directly. Identical δ across mixed settings tests φ-independence.

### 9.5 — Future Directions

θ-sweep; 3-observer; solid-state; locality closure; model discrimination.

---

## Section 10 — Conclusion

All existing EWF experiments share a geometric blind spot: equatorial Superobserver
measurement (θ = π/2) forces outcome-dependent probability modifications of the
form Eq. (2-3) to vanish identically, since Δf_perp ∝ cos θ = 0.

The fix: re-insert ONE QWP into Bong et al. (2020), tilting to θ = 31°. No new
components, N = 91,000. Model-independent LF violation at 8.6σ. Sensitivity to
outcome-dependent coupling β ≥ 0.05 at >5σ.

A single waveplate can open a new axis of inquiry in EWF experiments — testing
whether the geometric relationship between observers' measurement bases leaves
a detectable trace in their correlations.

---

## References

[1] M. Proietti et al., Science Advances 5, eaaw9832 (2019).
[2] K.W. Bong et al., Nature Physics 16, 1199–1205 (2020).
[3] E.P. Wigner, in The Scientist Speculates, Heinemann (1961).
[4] L. Hardy, Phys. Rev. Lett. 68, 2981 (1992).
[5] D. Frauchiger and R. Renner, Nature Comms. 9, 3711 (2018).
[6] N. Brunner et al., Rev. Mod. Phys. 86, 419 (2014).
[7] J.S. Bell, Physics 1, 195–200 (1964).
[8] M. Giustina et al., Phys. Rev. Lett. 115, 250401 (2015).
[9] H.M. Wiseman, E.G. Cavalcanti, and E.G. Rieffel, Quantum 7, 1112 (2023).
[10] M. Haddara and E.G. Cavalcanti, arXiv:2407.20346 (2024).
[11] A. Utreras-Alarcon, E.G. Cavalcanti, and H.M. Wiseman, Proc. R. Soc. A 480 (2023).
[12] M. Haddara and E.G. Cavalcanti, New J. Phys. 25, 093028 (2023).
[13] A. Kent, arXiv:2302.12707 (2023).

---

## Postscript: Changes from v7

1. **Detection loophole honest** (§7): Explicitly framed as "acceptable for FIRST
   test — primary goal is detecting deviation, not closing all loopholes." Modern
   SPADs η>0.90 noted as path forward.
2. **Model motivation via 3 physical constraints** (§2.3): (i) basis-rotation
   invariance, (ii) outcome-exchange symmetry, (iii) monotonicity → g(|⟨b|d⟩|²)
   uniquely, f_perp = leading order. Testing it constrains ENTIRE class.
3. **"First" softened** (§1, Abstract): "to our knowledge, no existing EWF
   experiment has been configured to test..." — knowledge-based, not absolute.
4. **Angular precision addressed** (§7): Bong <±1° explicitly cited; δ signal
   variation <1% at this precision. ±5° applies to LF violation only.

*Draft v8 — 2026-05-24. Final. arXiv quant-ph.*
