Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Geometric Blindness in Extended Wigner's Friend Experiments: A Single-Waveplate Test

**Status:** Draft v7 — Final pre-arXiv. Cautious novelty, theorem generality, claim calibrated, refs expanded, self-naming softened.
**Date:** 2026-05-24 | **Target:** arXiv quant-ph → Phys. Rev. A / PRL

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
— enables the first experimental test of outcome-dependent quantum registration,
simultaneously achieving model-independent Genuine LF violation at 8.6σ
(S_LF1 = +0.0891 ± 0.0103, a standard QM prediction) and sensitivity to
outcome-dependent coupling β ≥ 0.05 at >5σ. The protocol is robust to visibility
μ ≥ 0.86 and angular misalignment Δθ ≤ ±5°; the detection loophole (η ≥ 0.91
for closure) is discussed explicitly.

---

## Section 1 — Introduction

Extended Wigner's Friend (EWF) experiments [1,2] test whether observed events
exist independently of who observes them. Following theoretical developments in
Local Friendliness (LF) no-go theorems [2,9-11], optical implementations have
demonstrated violations of LF inequalities, challenging the absoluteness of
observed events and stimulating active debate about the nature of measurement
in quantum mechanics [12,13].

We identify a geometric property shared by ALL existing EWF experiments: the
Superobserver measures in the equatorial plane of the Bloch sphere (polar angle
θ = π/2). We show that this forces ANY outcome-dependent modification to quantum
probabilities — of the parametric form P = P_QM · [1 − β · g(outcome overlap)] / Z
— to vanish identically. The modification is proportional to cos θ, which equals
zero at θ = π/2. This is a mathematical identity, independent of any specific model.

The corollary is striking: no existing EWF experiment has been capable of testing
outcome-dependent quantum registration, regardless of statistical power. The
effect has been geometrically canceled by construction.

We propose a minimal modification to Bong et al. (2020) [2]: re-insert ONE
quarter-wave plate (QWP), tilting the Superobserver measurement to θ = 31°.
This single change — no new components, N = 91,000 — enables the first direct
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
at three settings: Setting 1 (z-basis, reads Friend outcome directly); Settings
2 and 3 (azimuthal angles on the Bloch sphere equator, θ = π/2). Outcomes are
binary: a, b ∈ {+1, −1}. N = 91,000 coincidences per setting.

[Figure 1: EWF setup with tilted Superobserver measurement]

### 2.2 — Genuine Local Friendliness Inequality

Gen LF 1 = −⟨A₁⟩ − ⟨A₂⟩ − ⟨B₁⟩ − ⟨B₂⟩ − ⟨A₁B₁⟩ − 2⟨A₁B₂⟩ − 2⟨A₂B₁⟩
         + 2⟨A₂B₂⟩ − ⟨A₂B₃⟩ − ⟨A₃B₂⟩ − ⟨A₃B₃⟩ − 6 ≤ 0                          (1)

Violation rules out all LF theories. LF inequalities have been extended to
multipartite scenarios [10], sequential measurements [11], and possibilistic
formulations [12], establishing a rich theoretical framework [9].

### 2.3 — Outcome-Dependent Registration: Parametric Model Class

Consider modifications to quantum probabilities where the Friend's outcome
influences Superobserver correlations:

  P(a,b | x,y) = P_QM(a,b | x,y) · [1 − β · g(b, Friend outcome)] / Z           (2)

where β ∈ [0,1] and g is an outcome-overlap function. β = 0 → standard QM.
When g is outcome-INDEPENDENT, the factor cancels in Z.

We focus on the overlap function:

  f_perp(b, d) = 1 − |⟨b|d⟩|²                                                    (3)

where b ∈ {+1,−1} is Superobserver outcome and d ∈ {H,V} is Friend outcome.

**Why this function?** For any model where the modification depends on measurement
bases, the natural scalar quantity capturing basis alignment is the Born-rule
transition probability |⟨b|d⟩|². The complement 1 − |⟨b|d⟩|² is the simplest
symmetric function vanishing for aligned bases and saturating for orthogonal
ones. This makes f_perp the canonical first-order representative of the class:
any smooth g(b,d) reduces to a linear function of f_perp near β = 0, so testing
f_perp constrains the entire class at leading order. Importantly, the geometric
cancellation identified in §3 applies to ANY g that depends on outcomes only
through |⟨b|d⟩|² — a broad class including sigmoid, exponential, and
information-theoretic variants.

**Status.** This is a PARAMETRIC TEST, not a physical theory. Physical motivations
for outcome-dependence have been discussed in quantum Darwinism, relational
quantum mechanics, and the quantum-to-classical transition. The f_perp class
provides a falsifiable implementation of the hypothesis that cross-observer
incompatibility modulates outcome probabilities.

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

**Generality.** The cancellation at θ = π/2 holds for ANY outcome-overlap
function g(b,d) that depends on outcomes only through the squared inner product
|⟨b|d⟩|². This includes g = −log(|⟨b|d⟩|²) (information-theoretic), g = σ(|⟨b|d⟩|²)
with sigmoid σ, and any smooth function whose Taylor expansion begins with the
f_perp term. The result identifies a geometric fixed point at θ = π/2 where this
entire function class becomes outcome-independent. Functions with different
dependence structures (e.g., involving azimuthal phase φ) are not constrained
by this specific cancellation.

### 3.3 — The Geometric Blind Spot

**Bong et al. (2020):** A₂, A₃, B₂, B₃ all equatorial. f_perp outcome-independent
for every measurement combination.

**Proietti et al. (2019):** BSM → |⟨ψ|Φ⁺⟩|² = 1/2 → f_perp = 1/2 constant.

**Prior work.** We are not aware of prior work identifying the role of the
Superobserver's polar angle θ — as distinct from the extensively studied
azimuthal angles φ₂, φ₃, β — in constraining outcome-dependent effects in EWF
experiments. We examined: Bong 2020 experimental sections and Supplemental
Material [2]; Proietti 2019 Methods [1]; LF inequality derivations in [5,9];
the Bell/LF review by Brunner et al. 2014 [6]; and recent LF extensions
[10-12]. None discuss θ as a relevant parameter. The azimuthal angles are
optimized and reported; θ is implicitly fixed to π/2 without comment. We
welcome independent verification of this assessment.

**Consequence:** No existing EWF experiment has tested outcome-dependent
quantum registration. The geometric blind spot is universal.

---

## Section 4 — Experimental Protocol

### 4.1 — Breaking the Cancellation

Any θ ≠ π/2 breaks the cancellation. Grid search maximizing min(n_σ_LF, n_σ_signal)
yields θ = 31° (Supplemental S2).

### 4.2 — Single Hardware Modification

In standard Bong, QWP is REMOVED for settings 2/3. We RE-INSERT one QWP in
Alice's path (before PBS, after BD2), tilting to θ = 31°. HWP controls φ as
in the original. Retardance tolerance ≤ ±2 nm (θ within ±0.5°). ONLY change.

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

For ANY model Eq. (2-3), the deviation in mixed settings is:

  δ⟨A_x B_y⟩ = ⟨A_x B_y⟩_QM · [(1 − β · |cos θ|/2)^(n_BSM) − 1]               (12)

where n_BSM = 1 for A₀B₁, A₁B₀; n_BSM = 2 for A₁B₁.

At θ = 31°: |cos θ|/2 ≈ 0.429. At illustrative β = 0.3: β|cos θ|/2 ≈ 0.129.
n_BSM = 1: Eq. (12) exactly linear in β. n_BSM = 2: ~7% second-order correction.

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

LF significance stable across Δθ = ±5° (8.6–8.8σ).

| Parameter | Nominal | Threshold | Bong Achievable |
|-----------|---------|-----------|-----------------|
| μ | 0.95 | ≥ 0.86 | 0.92 |
| η | 1.00 | ≥ 0.91 | 0.87 |
| Δθ | 0° | ≤ ±5° | < ±1° |

At Bong's η ≈ 0.87, μ ≥ 0.96 required. Achievable via source optimization [2].
If η < 0.91, fair-sampling applies.

[Figure 4: Sensitivity vs μ] [Figure 5: 2D (μ, η) sensitivity map]

---

## Section 8 — Loophole Analysis

Locality, freedom-of-choice: identical to Bong 2020. Detection: η ≥ 0.91 for
loophole-free (§7). Superobserver: satisfied optically. Model independence:
result constrains ALL models Eq. (2-3).

| Loophole | Status | Note |
|----------|--------|------|
| Locality | Same as Bong 2020 | QWP local to Alice |
| Detection | Conditional | η ≥ 0.91; Bong η ≈ 0.87 |
| Freedom of choice | Same as Bong 2020 | QRNG |
| Superobserver | Satisfied | Optical interferometry |
| Model class | Explicit: Eq. (2-3) | Tests entire class |

---

## Section 9 — Discussion

### 9.1 — Interpretation of a Positive Result

A statistically significant deviation from QM in the mixed-setting correlators
would demonstrate that the correlations between Superobserver and Friend outcomes
differ from standard quantum mechanical predictions at the modified geometry
(θ = 31°). While the parametric model class Eq. (2-3) provides one interpretation
of such a deviation, the primary experimental finding would be the deviation
itself — a quantitative departure from QM in an EWF scenario at a previously
untested geometric configuration. Establishing whether such a deviation
constitutes evidence for "outcome-dependent quantum registration" specifically,
rather than other possible Beyond-QM effects, would require follow-up experiments
(θ-sweeps, multi-observer configurations) and theoretical analysis beyond the
scope of this proposal.

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

This model is a POSTULATE — not derived from QM. One member of class Eq. (2-3).
Experiment measures β directly. Identical δ across mixed settings tests
φ-independence.

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
not just whether events are absolute, but whether the geometric relationship
between observers' measurement bases leaves a detectable trace in their
correlations.

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

## Postscript: Changes from v6

1. **Novelty cautious** (§3.3): "We are not aware of prior work..." + "We welcome
   independent verification." More diplomatic than absolute claim.
2. **Why f_perp + theorem generality** (§2.3, §3.2): Canonical first-order
   representative justification. New paragraph: cancellation at θ=π/2 holds for
   ANY g depending on outcomes via |⟨b|d⟩|² — sigmoid, exponential,
   information-theoretic variants all share this fixed point.
3. **§9.1 calibrated** (§9.1): No longer "first evidence for outcome-dependent
   registration." Framed as "deviation from QM at previously untested geometry"
   — interpretation follows from follow-up work, not claimed here.
4. **References 8→13** (§Refs): LF extensions [9-12] + Kent critique [13]
   from 2021-2024. Wiseman-Cavalcanti-Rieffel (Quantum 2023), Haddara-Cavalcanti
   (2024), Utreras-Alarcon et al. (2023), Haddara-Cavalcanti (NJP 2023).
5. **Self-naming softened**: Title subtitle removed. "Equatorial Cancellation
   Theorem" → "Geometric Cancellation at the Equator."

*Draft v7 — 2026-05-24. Final pre-arXiv. Target: arXiv quant-ph, then PRL/Phys. Rev. A.*
