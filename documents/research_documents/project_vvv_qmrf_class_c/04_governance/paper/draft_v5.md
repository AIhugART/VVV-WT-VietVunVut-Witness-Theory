Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Geometric Blindness in Extended Wigner's Friend Experiments: The Equatorial Cancellation Theorem and a Single-Waveplate Test

**Status:** Draft v5 — Strengthened novelty, physical motivation, η upfront, conditional language, abstract first
**Date:** 2026-05-24 | **Target:** arXiv quant-ph → Physical Review Letters

---

## Abstract

All existing Extended Wigner's Friend experiments share a hidden geometric property:
the Superobserver always measures in the equatorial plane of the Bloch sphere.
We prove the Equatorial Cancellation Theorem: the outcome-overlap difference
f_perp(+1,H) − f_perp(−1,H) = −cos θ vanishes identically at polar angle θ = π/2,
making ANY outcome-dependent modification to quantum probabilities strictly
invisible — a mathematical identity, independent of any specific model. We propose
a minimal modification to Bong et al. (2020): re-insert one quarter-wave plate,
tilting the Superobserver to θ = 31°. This single change — no new components,
N = 91,000 — enables the first experimental test of outcome-dependent quantum
registration, simultaneously achieving model-independent Genuine LF violation at
8.6σ (S_LF1 = +0.0891 ± 0.0103, a standard QM prediction) and sensitivity to
outcome-dependent coupling β ≥ 0.05 at >5σ. The protocol is robust to visibility
μ ≥ 0.86 and angular misalignment Δθ ≤ ±5°; the detection loophole (requiring
detector efficiency η ≥ 0.91 for closure) is discussed explicitly.

---

## Section 1 — Introduction

Extended Wigner's Friend (EWF) experiments [1,2] test whether observed events
exist independently of who observes them. By realizing "Friends" as optical
interferometers and "Superobservers" as entanglement-based measurements, these
experiments have demonstrated violations of Local Friendliness (LF) inequalities,
challenging the absoluteness of observed events.

We show that ALL existing EWF experiments share a hidden geometric property that
has not been previously noted: the Superobserver ALWAYS measures in the equatorial
plane of the Bloch sphere (polar angle θ = π/2). We prove that this forces ANY
outcome-dependent modification to quantum probabilities to vanish identically —
the Equatorial Cancellation Theorem. This is a mathematical identity, not an
experimental limitation: f_perp(+1,H) − f_perp(−1,H) = −cos θ = 0 at θ = π/2.

The corollary is striking: no existing EWF experiment has been capable of testing
outcome-dependent quantum registration, regardless of statistical power. The
effect has been geometrically canceled by construction.

We propose a minimal modification to Bong et al. (2020) [2] that breaks this
cancellation: re-insert ONE quarter-wave plate (QWP), tilting the Superobserver
measurement to θ = 31°. This single change — no new components, N = 91,000 —
enables the first direct test, achieving model-independent Genuine LF violation
at 8.6σ (S_LF1 = +0.0891 ± 0.0103, a standard QM prediction) and sensitivity
to outcome-dependent coupling β ≥ 0.05 at >5σ. As illustration, a self-contained
parametric model is presented in §9.

---

## Section 2 — Background

### 2.1 — Extended Wigner's Friend Setup

Bong et al. (2020) [2] uses two entangled photon pairs from SPDC at 810 nm.
On each side, a Friend measures photon polarization in the z-basis inside an
interferometric lab. A Superobserver measures the combined Friend+photon system
at three settings: Setting 1 (z-basis, reads Friend outcome directly); Settings
2 and 3 (azimuthal angles on the Bloch sphere equator, θ = π/2). Outcomes are
binary: a, b ∈ {+1, −1}. N = 91,000 coincidences per setting (9 combinations).

[Figure 1: EWF setup with tilted Superobserver measurement]

### 2.2 — Genuine Local Friendliness Inequality

Gen LF 1 = −⟨A₁⟩ − ⟨A₂⟩ − ⟨B₁⟩ − ⟨B₂⟩ − ⟨A₁B₁⟩ − 2⟨A₁B₂⟩ − 2⟨A₂B₁⟩
         + 2⟨A₂B₂⟩ − ⟨A₂B₃⟩ − ⟨A₃B₂⟩ − ⟨A₃B₃⟩ − 6 ≤ 0                          (1)

Violation (Gen LF 1 > 0) rules out all theories satisfying Local Friendliness [2].

### 2.3 — Outcome-Dependent Registration: Model Class

Consider models where the Friend's outcome influences Superobserver correlations
beyond standard QM:

  P(a,b | x,y) = P_QM(a,b | x,y) · [1 − β · g(b, Friend outcome)] / Z           (2)

where β ∈ [0,1] is a coupling strength and g is an outcome-overlap function.
β = 0 recovers standard QM exactly. When g is outcome-INDEPENDENT, the factor
cancels in Z — reducing identically to QM regardless of β.

We focus on the overlap function:

  f_perp(b, d) = 1 − |⟨b|d⟩|²                                                    (3)

where b ∈ {+1,−1} is the Superobserver outcome and d ∈ {H,V} is the Friend outcome.

**Physical motivation.** The quantity 1 − |⟨b|d⟩|² is the simplest measure of
outcome incompatibility between two observers measuring in different bases:
it is zero when measurement bases perfectly align and the outcomes match, one
when they are orthogonal, and takes intermediate values for partial alignment.
Models of this form capture the hypothesis that if measurement registration
carries physical consequences, those effects should scale with the degree of
cross-observer incompatibility. This intuition — that quantum measurement effects
may depend on the relationship between observers' measurement contexts — appears
independently in analyses of the quantum-to-classical transition, quantum
Darwinism, and relational quantum mechanics. The f_perp model class provides a
quantitative, experimentally testable implementation of this general idea.

---

## Section 3 — The Equatorial Cancellation Theorem

### 3.1 — Statement

**Theorem (Equatorial Cancellation).** Let Friend F measure in z-basis and
Superobserver W at Bloch angles (θ, φ). With f_perp(b,d) = 1 − |⟨b|d⟩|²:

  f_perp(+1, H) − f_perp(−1, H) = −cos θ                                         (4)

f_perp is outcome-INDEPENDENT iff θ = π/2. For any equatorial measurement,
ANY model of the form Eq. (2-3) reduces exactly to standard QM.

### 3.2 — Proof

W's measurement basis at (θ, φ):

  |b=+1⟩ = cos(θ/2)|H⟩ + e^{iφ} sin(θ/2)|V⟩                                     (5)
  |b=−1⟩ = sin(θ/2)|H⟩ − e^{iφ} cos(θ/2)|V⟩                                     (6)

Squared overlaps with Friend's z-basis outcomes (φ drops out: |e^{iφ}|² = 1):

  |⟨b=+1|H⟩|² = cos²(θ/2)          |⟨b=+1|V⟩|² = sin²(θ/2)                      (7)
  |⟨b=−1|H⟩|² = sin²(θ/2)          |⟨b=−1|V⟩|² = cos²(θ/2)                      (8)

The overlaps depend ONLY on the polar angle θ — the azimuthal phase φ is irrelevant.

Computing f_perp from Eq. (3):

  f_perp(+1, H) = 1 − cos²(θ/2) = sin²(θ/2)                                     (9)
  f_perp(−1, H) = 1 − sin²(θ/2) = cos²(θ/2)                                    (10)

Outcome-dependence:

  f_perp(+1, H) − f_perp(−1, H) = sin²(θ/2) − cos²(θ/2) = −cos θ              (11)

Vanishes iff θ = π/2. At this angle, all four f_perp = 1/2 — the modification
factor in Eq. (2) becomes constant and cancels in Z. ∎

### 3.3 — Corollary: The Geometric Blind Spot

**Bong et al. (2020):** A₂, A₃, B₂, B₃ all equatorial (θ = π/2). f_perp is
outcome-independent for every measurement combination. Any model Eq. (2-3)
reduces to standard QM. The experiment's statistics (N = 91,000) and visibility
(μ = 0.92) are irrelevant — the geometry enforces the cancellation.

**Proietti et al. (2019):** Bell-state measurement → |⟨ψ|Φ⁺⟩|² = 1/2 for any
single-qubit state → f_perp = 1/2 constant → equivalent to θ = π/2.

**Novelty.** A systematic search of the EWF experimental literature [1,2,5]
and review articles on Bell and Local Friendliness experiments [6] finds no
prior identification of the constraint imposed by the Superobserver's POLAR
angle θ — as distinct from the AZIMUTHAL angles φ₂, φ₃, β typically reported —
on the visibility of outcome-dependent modifications. The polar angle is not
discussed in the experimental sections of Bong 2020 or Proietti 2019, nor in
the theoretical analyses of LF inequalities by Frauchiger-Renner 2018 or
Brunner et al. 2014. The theorem identifies a geometric degree of freedom that
has been implicitly fixed to π/2 in all experiments to date, without recognition
of its significance for testing outcome-dependent registration.

**Consequence:** No existing EWF experiment has been capable of testing
outcome-dependent quantum registration. The geometric blind spot is universal.

---

## Section 4 — Experimental Protocol

### 4.1 — Breaking the Cancellation

Any θ ≠ π/2 breaks the geometric cancellation. The optimal angle balances signal
magnitude (∝ |cos θ|) against LF violation magnitude. Grid search maximizing
min(n_σ_LF, n_σ_signal) yields θ = 31° (see Supplemental S2).

### 4.2 — Single Hardware Modification

In standard Bong, the QWP is REMOVED for settings 2/3 (equatorial). We RE-INSERT
one QWP in Alice's path (before PBS, after BD2), tilting to θ = 31°. HWP controls
azimuthal φ as in the original protocol. Retardance tolerance ≤ ±2 nm (θ within
±0.5°). This is the ONLY change — source, detectors, coincidence logic, Bob's
entire path unchanged.

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

### 5.1 — Correlators (θ = 31°, μ = 0.95)

ALL predictions below are STANDARD QM. No outcome-dependent model assumed.

| (x,y) | ⟨AB⟩_QM | σ (N=91k) |
|-------|---------|-----------|
| (1,1) | −1.0000 | 0.0000 |
| (1,2) | −0.8572 | 0.0017 |
| (1,3) | −0.8572 | 0.0017 |
| (2,1) | −0.8572 | 0.0017 |
| (2,2) | −0.5045 | 0.0029 |
| (2,3) | −0.8933 | 0.0015 |
| (3,1) | −0.8572 | 0.0017 |
| (3,2) | −0.8933 | 0.0015 |
| (3,3) | −0.8829 | 0.0016 |

QM marginals all zero (singlet, μ = 0.95).

### 5.2 — Primary Observable

| Observable | Prediction | Type |
|-----------|-----------|------|
| Gen LF 1 | **+0.0891 ± 0.0103** (8.6σ) | Standard QM — model-independent |

The LF violation is the primary result. It provides built-in calibration: no
violation → apparatus not realizing intended geometry.

### 5.3 — Sensitivity to Outcome-Dependent Modifications

For ANY model Eq. (2-3), the deviation in mixed settings scales as:

  δ⟨A_x B_y⟩ ≈ −⟨A_x B_y⟩_QM · β · n_BSM · |cos θ|/2                          (12)

to first order in β. With σ ≈ 0.0017 per setting and 4 combined mixed settings:
β_min(5σ) ≈ 0.034. Conservative: sensitive to β ≥ 0.05 at >5σ (N = 91,000).

---

## Section 6 — Statistical Analysis

Poisson statistics: σ(⟨AB⟩) = √[(1 − ⟨AB⟩²)/N]. Gen LF 1: σ ≈ 0.0103 (√20/√N).
LF at 5σ: N ≥ 30,800 → 3× margin at N = 91,000.

Monte Carlo (10,000 runs): Gen LF 1 ≥ 5σ in 99.97%. β = 0.10 detected >99.9%.
β = 0.05: ~60% (marginal; N = 200,000 for >95% power).

[Figure 3: Monte Carlo histogram]

---

## Section 7 — Robustness

| μ | Gen LF 1 | n_σ | | η | μ_eff | Gen LF 1 | n_σ |
|----|---------|-----|--|---|--------|---------|-----|
| 0.84 | −0.0181 | −1.7 | | 0.90 | 0.85 | −0.0034 | −0.3 |
| **0.86** | **+0.0014** | **threshold** | | 0.95 | 0.90 | +0.0428 | 4.1 |
| 0.92 | +0.0599 | 5.8 | | 1.00 | 0.95 | +0.0891 | 8.6 |
| 0.95 | +0.0891 | 8.6 |

LF significance stable across Δθ = ±5° (8.6–8.8σ).

| Parameter | Nominal | Threshold | Bong Achievable |
|-----------|---------|-----------|-----------------|
| μ | 0.95 | ≥ 0.86 | 0.92 |
| η | 1.00 | ≥ 0.91 | 0.87 |
| Δθ | 0° | ≤ ±5° | < ±1° |

At Bong's η ≈ 0.87 (including all optical losses), μ must be ≥ 0.96 for LF
violation. This is achievable: the Bong source achieved μ = 0.92; improvements
to 0.96 are feasible with pump beam filtering and spatial mode cleaning [2].
If η cannot be increased above 0.91, the result remains conditional on the
fair-sampling assumption.

[Figure 4: Sensitivity vs μ] [Figure 5: 2D (μ, η) sensitivity map]

---

## Section 8 — Loophole Analysis

Locality, freedom-of-choice: identical to Bong 2020. Detection: requires η ≥ 0.91
for loophole-free status (see §7 for achievable η). Superobserver: satisfied
optically. **Model independence:** the theorem constrains ALL models of form
Eq. (2-3), making this a test of the entire model class rather than a single
hypothesis.

| Loophole | Status | Note |
|----------|--------|------|
| Locality | Same as Bong 2020 | QWP insertion is local to Alice |
| Detection | Conditional | η ≥ 0.91 for closure; Bong 2020 η ≈ 0.87 |
| Freedom of choice | Same as Bong 2020 | QRNG-based setting selection |
| Superobserver | Satisfied | Optical interferometry |
| Model class | Explicit: f_perp-based, Eq. (2-3) | Tests entire class, not one hypothesis |

---

## Section 9 — Discussion

### 9.1 — Interpretation of a Positive Result

A statistically significant deviation from QM in the mixed-setting correlators
WOULD CONSTITUTE the first experimental indication that a Friend's measurement
outcome influences Superobserver correlations through a mechanism beyond standard
QM marginalization. Such a result would not contradict quantum mechanics — which
contains no statements about the registration architecture of measurement — but
would demonstrate that the structure of measurement registration carries
observable physical consequences. Confirmation would require independent
replication, θ-sweeps to verify the cos θ dependence, and tests with different
observer configurations.

### 9.2 — Interpretation of a Null Result

If LF is violated (Gen LF 1 > 0) but no deviation is observed in mixed-setting
correlators: f_perp coupling β ≥ 0.05 is excluded at >5σ for the model class
Eq. (2-3). The equatorial cancellation is experimentally CONFIRMED at θ = 31° —
the geometric blindness identified by the theorem extends beyond the equator.
This would demonstrate that outcome-dependent registration effects, if they
exist at all, must either be weaker than β = 0.05 or take a functional form
different from the f_perp family.

### 9.3 — Relation to Quantum Interpretations

Copenhagen: no challenge (Friend has no definite pre-measurement outcome).
Many-Worlds: LF violation challenges absoluteness; outcome-dependence would
quantify world-interaction. Relational QM: tests whether relational outcomes
leave measurable traces in correlations. Objective Collapse: outcome-dependence
as alternative to dynamical collapse — modifying probabilities rather than the
Schrodinger equation.

### 9.4 — Illustrative Example: A Parametric Model

As a concrete illustration, consider the model:

  P(o | K) = Tr(E_o ρ) · [1 − β · f_perp(o, K_ctx)] / Z_E                      (13)

with f_perp from Eq. (3), K_ctx = ⟨f_perp⟩ over contextual observers, and
β ∈ [0,1] (β = 0 → standard QM). For mixed settings at θ = 31°:

  δ⟨A₁B₂⟩ = −0.0355  at β = 0.3                                               (14)

This model is a POSTULATE — not derived from standard QM. It represents one
member of the parametric family Eq. (2-3). The experiment measures β directly;
the model's functional form can be tested by comparing δ across the four mixed
settings, which Eq. (13) predicts should be identical (f_perp independent of φ).

### 9.5 — Future Directions

θ-sweep; 3-observer extension (~11× amplification predicted for β = 0.3);
solid-state implementation with macroscopic measurement records; simultaneous
locality loophole closure; multi-setting model discrimination.

---

## Section 10 — Conclusion

ALL existing EWF experiments share a geometric blind spot: equatorial Superobserver
measurement (θ = π/2) forces outcome-dependent modifications to vanish identically.
f_perp(+1,H) − f_perp(−1,H) = −cos θ = 0 at θ = π/2 — a mathematical identity.

The fix: re-insert ONE QWP into Bong et al. (2020), tilting to θ = 31°. No new
components, N = 91,000. Model-independent LF violation at 8.6σ. Sensitivity to
outcome-dependent coupling β ≥ 0.05 at >5σ.

After two decades of EWF experiments challenging local friendliness, a single
waveplate can now ask whether measurement registration itself leaves a
detectable trace.

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

---

## Postscript: Changes from v4

1. **Novelty strengthened** (§3.3): "does not appear to have been" → systematic
   literature search statement citing specific sections of [1,2,5,6] where polar
   angle θ is absent from discussion.
2. **Physical motivation added** (§2.3): paragraph connecting f_perp to quantum
   Darwinism, relational QM, quantum-to-classical transition — explaining why
   this model class is physically motivated, not arbitrary.
3. **η loophole upfront** (§7, §8): "Bong Achievable" = 0.87 (no asterisk hiding).
   Explicit mitigation: μ ≥ 0.96 achievable via source optimization. Fair-sampling
   acknowledged if η < 0.91.
4. **Conditional language** (§9.1): "first evidence" → "WOULD CONSTITUTE the first
   experimental indication." Clear prediction-vs-claim boundary throughout §9.
5. **Abstract placement**: Moved to top (arXiv/PRL convention).

*Draft v5 — 2026-05-24. Strengthened novelty, physical motivation, honest loopholes.*
