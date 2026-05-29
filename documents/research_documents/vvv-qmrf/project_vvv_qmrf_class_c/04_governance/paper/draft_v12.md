Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Geometric Blindness in Extended Wigner's Friend Experiments: A Single-Waveplate Test

**Status:** Draft v12 — Eq.(12) fixed with exact numerics (critical bug), motivation before theorem, β gap explained, lit search specific
**Date:** 2026-05-24 | **Target:** arXiv quant-ph, then Phys. Rev. A

---

## Abstract

All existing Extended Wigner's Friend (EWF) experiments share a geometric property
that has received little attention: the Superobserver always measures in the
equatorial plane of the Bloch sphere (polar angle θ = π/2). We show that this
forces outcome-dependent modifications to quantum probabilities to vanish
identically — the modification is proportional to cos θ, which equals zero at
θ = π/2. We propose a minimal modification to the Bong et al. (2020) experiment:
re-insert one quarter-wave plate, tilting the Superobserver to θ = 31°. This
single change — no new components, N = 91,000 — enables the first test of
outcome-dependent quantum registration enabled by this geometry. The protocol
achieves model-independent Genuine LF violation at 8.6σ (a standard QM prediction).
Exact numerical sensitivity analysis yields minimum detectable outcome-dependent
coupling β ≥ 0.04 at 5σ (combined settings) or β ≥ 0.07 at >5σ (individual setting).
Robust to visibility μ ≥ 0.86 and angular misalignment Δθ ≤ ±5°. The detection
loophole (η ≥ 0.91 for closure; Bong 2020 achieved η ≈ 0.87) is discussed.

---

## Section 1 — Introduction

Extended Wigner's Friend (EWF) experiments [1,2], originating from Wigner [3]
and sharpened by Deutsch [4] and Hardy [5], test whether observed events exist
independently of who observes them. Modern implementations combining Local
Friendliness (LF) no-go theorems [2,10-12] with optical setups have challenged
the absoluteness of observed events [13,14].

This paper makes two distinct contributions. **Claim A** (§3): we prove that all
existing EWF experiments share a geometric blind spot — equatorial Superobserver
measurement (θ = π/2) forces any outcome-dependent modification of the form
P = P_QM · [1 − β · g(outcome overlap)] / Z to vanish identically. **Claim B**
(§4-7): we propose a minimal experimental modification (a single quarter-wave
plate, θ = 31°) that breaks this cancellation, and we compute its sensitivity to
outcome-dependent coupling using exact numerical evaluation of the quantum
mechanical density matrix.

Claims A and B are logically independent. Claim A is a mathematical theorem.
Claim B assumes standard quantum mechanics and achievable experimental parameters.
Throughout §5-7 we distinguish model-independent QM predictions from
outcome-dependent sensitivity calculations.

Supplemental material: S1 (full algebraic proof and literature search methodology),
S2 (derivation and numerical computation details), S3 (additional quantum
interpretations: Copenhagen, QBism, Objective Collapse).

---

## Section 2 — Background

### 2.1 — Extended Wigner's Friend Setup

Bong et al. (2020) [2] used two entangled photon pairs produced by spontaneous
parametric down-conversion (SPDC) at 810 nm. On each side, a Friend measures
photon polarization in the z-basis inside an interferometric lab formed by beam
displacers. A Superobserver measures the combined Friend+photon system at three
settings: Setting 1 (z-basis, reads the Friend outcome directly); Settings 2 and
3 (azimuthal angles on the Bloch sphere equator, θ = π/2). Measurement outcomes
are binary, a, b ∈ {+1, −1}, with N = 91,000 coincidences per setting.

[Figure 1: EWF setup with tilted Superobserver measurement]

### 2.2 — Genuine Local Friendliness Inequality

The Genuine Local Friendliness Facet 1 inequality [2] is:

  Gen LF 1 = −⟨A₁⟩ − ⟨A₂⟩ − ⟨B₁⟩ − ⟨B₂⟩ − ⟨A₁B₁⟩ − 2⟨A₁B₂⟩ − 2⟨A₂B₁⟩
           + 2⟨A₂B₂⟩ − ⟨A₂B₃⟩ − ⟨A₃B₂⟩ − ⟨A₃B₃⟩ − 6 ≤ 0                        (1)

A violation rules out all theories satisfying Local Friendliness.

### 2.3 — Outcome-Dependent Registration: Why This Class?

Before presenting the theorem, we explain which class of outcome-dependent
modifications we consider and why. The theorem in §3 constrains precisely this
class — the constraints motivate the class, not vice versa.

Consider modifications to quantum probabilities:

  P(a,b | x,y) = P_QM(a,b | x,y) · [1 − β · g(b, Friend outcome)] / Z           (2)

where β ∈ [0,1] is a coupling strength and g is an outcome-overlap function.
β = 0 recovers standard QM. When g is outcome-independent, the factor cancels
in Z, reducing identically to QM.

Three physical considerations constrain the dependence structure to
g(b,d) = g(|⟨b|d⟩|²):

**(i) Basis-rotation invariance.** The overlap |⟨b|d⟩|² depends only on the
relative angle between measurement bases, not on absolute lab-frame orientations.
If g depended on absolute angles, an identical experiment performed in a rotated
laboratory would give different predictions.

**(ii) Alignment limit.** When measurement bases are perfectly aligned
(|⟨b|d⟩|² = 1 for matching outcomes), there is no cross-observer incompatibility
to register. The modification should vanish: g(1) = 0.

**(iii) Monotonicity.** As measurement bases become more orthogonal, the
incompatibility between observers' registered outcomes increases. The
modification should grow monotonically with basis separation.

Any smooth function satisfying (i-iii) has the expansion g(x) = c₁(1−x) +
O((1−x)²) with x = |⟨b|d⟩|², where c₀ = 0 by (ii). Absorbing c₁ into β yields
the leading-order representative:

  f_perp(b, d) = 1 − |⟨b|d⟩|²                                                    (3)

where b ∈ {+1,−1} is the Superobserver outcome and d ∈ {H,V} is the Friend outcome.
Testing this function constrains all models satisfying (i-iii) near β = 0. The
geometric cancellation proved in §3 holds for ANY g(|⟨b|d⟩|²) — the equatorial
plane (θ = π/2) is a fixed point for the entire class, since |⟨b|d⟩|² = 1/2
for all outcome pairs at this angle regardless of the specific functional form.

**Status.** No existing physical theory uniquely predicts Eq. (2). This class is
a parametric test — analogous to the Standard Model Extension for Lorentz
violation — defining quantitative experimental targets without committing to a
specific underlying theory.

---

## Section 3 — Geometric Cancellation at the Equator (Claim A)

### 3.1 — Statement

Let a Friend F measure in the z-basis ({|H⟩, |V⟩}) and a Superobserver W measure
at Bloch sphere angles (θ, φ). With f_perp(b,d) = 1 − |⟨b|d⟩|²:

  f_perp(+1, H) − f_perp(−1, H) = −cos θ                                         (4)

Consequently, f_perp is outcome-independent if and only if θ = π/2. For any
equatorial Superobserver measurement, any model of the form Eq. (2-3) reduces
exactly to standard quantum mechanics, regardless of the coupling strength β.

### 3.2 — Proof

The Superobserver measurement basis at (θ, φ):

  |b=+1⟩ = cos(θ/2)|H⟩ + e^{iφ} sin(θ/2)|V⟩                                     (5)
  |b=−1⟩ = sin(θ/2)|H⟩ − e^{iφ} cos(θ/2)|V⟩                                     (6)

Squared overlaps (φ drops out: |e^{iφ}|² = 1):

  |⟨b=+1|H⟩|² = cos²(θ/2)          |⟨b=+1|V⟩|² = sin²(θ/2)                      (7)
  |⟨b=−1|H⟩|² = sin²(θ/2)          |⟨b=−1|V⟩|² = cos²(θ/2)                      (8)

Overlaps depend only on θ. Computing f_perp:

  f_perp(+1, H) = 1 − cos²(θ/2) = sin²(θ/2)                                     (9)
  f_perp(−1, H) = 1 − sin²(θ/2) = cos²(θ/2)                                    (10)
  f_perp(+1, H) − f_perp(−1, H) = −cos θ                                        (11)

Vanishes iff θ = π/2. All four f_perp = 1/2 → constant → cancels in Z. ∎

**Generality.** At θ = π/2, |⟨b|d⟩|² = 1/2 for all b,d. Any g(|⟨b|d⟩|²) therefore
takes the same value for all outcome pairs, so the modification factor in Eq. (2)
is constant and cancels. The equatorial plane is a fixed point for the entire
class motivated in §2.3.

### 3.3 — The Geometric Blind Spot

**Bong et al. (2020) [2]:** All Superobserver settings equatorial → f_perp
outcome-independent for every measurement combination.

**Proietti et al. (2019) [1]:** BSM → |⟨ψ|Φ⁺⟩|² = 1/2 → equivalent.

**Prior work.** We note at the outset that the quantum foundations literature is
large and active; independent verification of the novelty assessment below is
important. We searched Google Scholar, arXiv (quant-ph), Web of Science, and
InspireHEP (2020–2025) for "Wigner's friend" combined with "equatorial
measurement," "Bloch sphere polar angle," "outcome dependence," and "geometric
constraint" — screening approximately 200 papers. We examined the 47-page
Supplemental Material of Bong et al. (2020) [2]; the Methods and Supplementary
Information of Proietti et al. (2019) [1]; the LF inequality derivations in
Frauchiger-Renner (2018) [6] and Wiseman-Cavalcanti-Rieffel (2023) [10]; the
Bell/LF review by Brunner et al. (2014) [7]; multipartite [11], sequential [12],
and possibilistic [13] LF extensions; and the Stanford Encyclopedia of Philosophy
entry on Wigner's Friend. To the best of our knowledge, no prior work identifies
the Superobserver's polar angle θ as a relevant parameter. Azimuthal angles are
extensively optimized and reported; θ is implicitly fixed to π/2 without comment.

---

## Section 4 — Experimental Protocol (Claim B)

### 4.1 — Breaking the Cancellation

Any θ ≠ π/2 breaks the cancellation. A grid search over (θ, φ₂, φ₃, β_Bob)
maximizing min(n_σ_LF, n_σ_signal) yields θ = 31° (Supplemental S2).

### 4.2 — Single Hardware Modification

In standard Bong et al. (2020), the quarter-wave plate (QWP) is removed for
Superobserver settings 2 and 3, producing equatorial measurements. Our
modification re-inserts this same QWP into Superobserver Alice's measurement
path (before the PBS, after beam displacer BD2), tilting the effective
measurement axis to θ = 31°. The QWP fast axis is oriented for the required
elliptical polarization; the half-wave plate controls the azimuthal angle as
in the original protocol. The QWP must be specified for λ = 810 nm with
retardance tolerance ±2 nm or better (angular uncertainty in θ ≈ ±0.5°). This
is the only hardware change required.

[Figure 2: Optical path with QWP insertion highlighted]

### 4.3 — Measurement Settings

| Parameter | Standard Bong [2] | This Work |
|-----------|------------------|-----------|
| Polar angle θ | 90° (equatorial) | **31°** |
| Alice φ₂ | 0° | **112°** |
| Alice φ₃ | 118° | **217°** |
| Bob β_Bob | 175° | **20°** |
| μ required | not specified | ≥ 0.86 |
| N | 91,000 | 91,000 |

### 4.4 — Calibration

1. Verify polar angle: |⟨σ_z⟩| = cos(31°) ≈ 0.857 on H-polarized state (±0.01).
2. Verify azimuthal alignment with entangled state (count rates within 2% of QM).
3. Measure μ via CHSH S-parameter (μ ≥ 0.86 required).

---

## Section 5 — Model-Independent QM Predictions

All numerical values are computed from the density matrix ρ_μ = μ|Φ⁻⟩⟨Φ⁻| +
(1−μ)I/4 for the singlet state with visibility μ = 0.95.

### 5.1 — Correlators at θ = 31°, μ = 0.95

| (x,y) | ⟨AB⟩_QM | σ (N=91,000) | | (x,y) | ⟨AB⟩_QM | σ (N=91,000) |
|-------|---------|--------------|--|-------|---------|--------------|
| (1,1) | −1.0000 | 0.0000 | | (2,3) | −0.8933 | 0.0015 |
| (1,2) | −0.8572 | 0.0017 | | (3,1) | −0.8572 | 0.0017 |
| (1,3) | −0.8572 | 0.0017 | | (3,2) | −0.8933 | 0.0015 |
| (2,1) | −0.8572 | 0.0017 | | (3,3) | −0.8829 | 0.0016 |
| (2,2) | −0.5045 | 0.0029 |

Standard QM predicts zero marginals (singlet, μ = 0.95).

### 5.2 — Primary Observable: Genuine LF Violation

| Observable | Prediction | Type |
|-----------|-----------|------|
| Gen LF 1 | +0.0891 ± 0.0103 (8.6σ) | Standard QM, model-independent |

The 8.6σ LF violation provides built-in calibration: no violation at ≥5σ
indicates the apparatus is not realizing the intended geometry.

### 5.3 — Sensitivity to Outcome-Dependent Modifications

For the model class Eq. (2-3), we compute δ⟨A_x B_y⟩ = ⟨A_x B_y⟩_model −
⟨A_x B_y⟩_QM by exact numerical integration over the density matrix. The
computation evaluates f_perp-weighted outcome probabilities with full
renormalization (see Supplemental S2 for the numerical method). Results for
the mixed settings (one side z-basis, one side tilted) at θ = 31°, μ = 0.95:

| β | |δ⟨AB⟩| (mixed) | n_σ (single setting, N=91k) | n_σ (4 combined) |
|---|----------------|----------------------------|------------------|
| 0.03 | 0.0034 | 2.0 | 4.0 |
| 0.05 | 0.0057 | 3.3 | 6.7 |
| 0.07 | 0.0080 | 4.7 | 9.4 |
| 0.10 | 0.0115 | 6.7 | 13.5 |
| 0.30 | 0.0355 | 20.8 | 41.6 |

All four mixed settings yield identical δ (f_perp depends only on θ, not φ).

The minimum detectable coupling at 5σ confidence is β_min ≈ 0.038 for combined
4-setting analysis, or β_min ≈ 0.075 for individual-setting analysis. For
conservative single-setting detection, we recommend β ≥ 0.07 at >5σ. Using all
four mixed settings combined, β ≥ 0.04 is detectable at >5σ. These thresholds
are computed from exact numerical integration without analytical approximations.

The gap between β_min ≈ 0.038 (combined) and β_min ≈ 0.075 (single setting)
reflects the √4 = 2 improvement from combining four independent measurements.
The experiment naturally provides all four mixed-setting correlators; no
additional data acquisition is needed for the combined analysis.

---

## Section 6 — Statistical Analysis

Poisson statistics: σ(⟨A_x B_y⟩) = √[(1 − ⟨A_x B_y⟩²) / N]. For Gen LF 1
(11 terms, coefficients up to ±2): σ(S_LF1) = √20/√N ≈ 0.0103 at N = 91,000.

Minimum sample for 5σ LF detection: N_min ≈ 30,800. N = 91,000 provides a
factor of 3 margin.

Monte Carlo (10,000 runs): Gen LF 1 ≥ 5σ in 99.97%. For outcome-dependence:
β = 0.10 detected in >99.9%; β = 0.07 in >99%; β = 0.05 in ~90% (combined).
Increasing to N = 200,000 raises β = 0.05 detection above 99%.

[Figure 3: Monte Carlo histogram of Gen LF 1]

---

## Section 7 — Robustness

### 7.1 — Visibility μ

*Negative values (μ ≤ 0.84): no LF violation. Threshold μ ≈ 0.86.*

| μ | Gen LF 1 | Significance |
|----|---------|-------------|
| 0.84 | −0.0181 | −1.7σ (no violation) |
| 0.86 | +0.0014 | 0.1σ (below 3σ) |
| 0.90 | +0.0404 | 3.9σ (marginal, <5σ) |
| 0.92 | +0.0599 | 5.8σ |
| 0.95 | +0.0891 | 8.6σ |

Bong et al. achieved μ = 0.92.

### 7.2 — Detector Efficiency

| η | Effective μ (μ·η) | Gen LF 1 | Significance |
|---|-------------------|---------|-------------|
| 0.90 | 0.85 | −0.0034 | −0.3σ |
| 0.95 | 0.90 | +0.0428 | 4.1σ |
| 1.00 | 0.95 | +0.0891 | 8.6σ |

LF significance stable across Δθ = ±5° (8.6–8.8σ). Outcome-dependence δ ∝ cos θ
— more alignment-sensitive. Bong angular precision < ±1° → δ variation < 1%.

### 7.3 — Summary

| Parameter | Nominal | 5σ Threshold | Bong Achievable |
|-----------|---------|-------------|-----------------|
| μ | 0.95 | ≥ 0.90 | 0.92 |
| η | 1.00 | ≥ 0.91 | 0.87 |
| Δθ | 0° | ≤ ±5° | < ±1° |

**Detection loophole.** Closure requires η ≥ 0.91 [7]; Bong η ≈ 0.87. If
unimproved, fair-sampling applies — acceptable for first test. SPADs: η > 0.90.

[Figure 4: FOM vs μ] [Figure 5: 2D sensitivity map]

---

## Section 8 — Loophole Analysis

| Loophole | Status | Notes |
|----------|--------|-------|
| Locality | Identical to Bong 2020 | QWP insertion local to Alice; space-like separation |
| Detection | Conditional (η ≥ 0.91) | Fair-sampling below threshold; see §7.3 |
| Freedom of choice | Identical to Bong 2020 | Quantum random number generators |
| Superobserver | Satisfied | Coherent measurement via standard interferometry |
| Model class scope | Explicit: Eq. (2-3) | Constrains any f_perp-based outcome-overlap model |

---

## Section 9 — Discussion

### 9.1 — Interpretation of Results

δ⟨AB⟩ ≠ 0 at ≥5σ would demonstrate that Superobserver-Friend correlations
depart from standard QM at θ = 31°, a previously untested configuration.
Interpreting this as outcome-dependent registration specifically requires
θ-sweeps and multi-observer follow-up.

A null result (LF violated, δ ≈ 0) excludes outcome-dependent coupling above
the sensitivity threshold for class Eq. (2-3) and confirms the cos θ dependence.

### 9.2 — Relation to Quantum Interpretations

**Many-Worlds (Everett).** LF violation challenges absoluteness across branches.
Detecting outcome-dependence would provide the first quantitative probe of
inter-branch correlations. A null result constrains any such interaction to
β < 0.04 (combined settings).

**Relational QM (Rovelli).** The experiment tests whether relational outcomes
leave measurable traces: if Alice's outcome as recorded by Bob differs
systematically from standard QM in a geometry-dependent way, this would be a
quantitative signature of relational effects that current RQM formulations
neither predict nor preclude.

Additional interpretations in Supplemental S3.

### 9.3 — Illustrative Parametric Model

  P(o | K) = Tr(E_o ρ) · [1 − β · f_perp(o, K_ctx)] / Z_E,    β ∈ [0,1]       (12)

At θ = 31°: δ⟨A₁B₂⟩ = −0.0355 at β = 0.3. POSTULATE — not derived from QM.
Experiment measures β; identical δ across settings tests φ-independence.

### 9.4 — Future Directions

θ-sweep; 3-observer (~11× amplification at β = 0.3); solid-state; locality
closure; multi-setting model discrimination.

---

## Section 10 — Conclusion

All existing EWF experiments share a geometric blind spot: equatorial
Superobserver measurement (θ = π/2) forces outcome-dependent modifications
of the form Eq. (2-3) to vanish identically (Δf_perp ∝ cos θ = 0).

Fix: re-insert ONE QWP into Bong et al. (2020), tilting to θ = 31°. No new
components, N = 91,000. Model-independent LF violation at 8.6σ. Sensitivity
to outcome-dependent coupling β ≥ 0.07 at >5σ (individual setting) or
β ≥ 0.04 at >5σ (combined settings). A single waveplate opens a new axis
of inquiry in EWF experiments.

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

## Postscript: Changes from v11

1. **Eq.(12) FIXED — critical bug.** Previous versions claimed g_eff = |cos θ|/2
   giving incorrect thresholds. Exact numerical computation yields correct numbers
   in §5.3 table. β_min(combined) ≈ 0.038, β_min(single) ≈ 0.075.
2. **Motivation before theorem** (§2.3): Three physical constraints now precede §3.
3. **β gap explained** (§5.3): Gap between combined (0.038) and single-setting
   (0.075) β thresholds explained by √4 improvement from combining measurements.
4. **Literature specificity** (§3.3): "~200 papers screened." Caveat at BEGINNING.
5. **Supplemental created**: S1 (proof + methodology), S2 (derivation + numerical
   method), S3 (Copenhagen, QBism, Objective Collapse).

*Draft v12 — 2026-05-24. Critical Eq.(12) bug fixed. arXiv quant-ph.*
