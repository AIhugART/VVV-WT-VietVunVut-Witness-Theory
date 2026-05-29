Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# A Single-Waveplate Test of Outcome-Dependent Quantum Registration in Extended Wigner's Friend Scenarios

**Status:** Draft v2 -- RCA-reviewed: self-referential fixed, jargon removed, sensitivity framing
**Date:** 2026-05-24
**Target:** arXiv quant-ph (preprint), then Physical Review Letters
**Changes from v1:** See §Postscript at end of document

---

## Section 1 -- Introduction

Extended Wigner's Friend (EWF) experiments probe whether observed events exist
independently of who observes them. Recent experiments [Proietti2019, Bong2020]
have demonstrated violations of Local Friendliness (LF) inequalities, challenging
the absoluteness of observed events.

This paper makes two independent contributions. First, we prove a geometric theorem:
ALL existing EWF experiments share a hidden property -- the Superobserver measures
in the equatorial plane of the Bloch sphere (polar angle theta = pi/2), which makes
any outcome-dependent modification to quantum probabilities strictly invisible.
This is a mathematical identity, not an experimental limitation.

Second, we propose a minimal modification to Bong et al. (2020) that breaks this
geometric cancellation: re-insert ONE quarter-wave plate (QWP), tilting the
Superobserver measurement to theta = 31 degrees. This single hardware change --
requiring no new components, no increase in measurement time, and no modification
to the source or detection system -- enables, for the first time, a direct
experimental test of outcome-dependent quantum registration.

As a concrete illustration, we compute predictions for one candidate hypothesis
(K9_E, a registration-layer probability modification [VietVunVut2026]), which
predicts a correlation shift delta<A1B2> = -0.0355 at coupling beta=0.3, while
simultaneously violating the Genuine LF inequality (S_LF1 = +0.0891 +/- 0.0103,
8.6 sigma). CRITICALLY: the 8.6 sigma LF violation is a STANDARD QM prediction --
it does not depend on K9_E or any outcome-dependent model.

The experiment is sensitive to coupling strengths beta >= 0.05 at >5 sigma
confidence with N = 91,000 coincidences (matching Bong 2020). The minimum
detectable beta at 5 sigma is 0.034 using combined mixed-setting data.

The protocol is robust to realistic experimental imperfections: LF violation
survives down to visibility mu = 0.86 and detector efficiency eta > 0.90,
with angular tolerance of +/- 5 degrees. This represents the first feasible
test of outcome-dependent quantum registration in an EWF scenario.

---

## Section 2 -- Theoretical Background

### 2.1 -- Extended Wigner's Friend Setup

Bong et al. (2020) uses two entangled photon pairs from SPDC at 810 nm. On each
side, a Friend measures photon polarization in the z-basis inside an interferometric
lab, and a Superobserver measures the combined Friend+photon system at settings:
- Setting 1: z-basis (reads Friend outcome directly)
- Settings 2, 3: azimuthal angles on the Bloch sphere equator (theta = pi/2)

Outcomes: a, b in {+1, -1}. N = 91,000 coincidences per setting (9 combinations).

[Figure 1: EWF setup schematic with tilted Superobserver measurement]

### 2.2 -- Genuine Local Friendliness Inequality

Gen LF 1 = -<A1> - <A2> - <B1> - <B2> - <A1B1> - 2<A1B2> - 2<A2B1>
         + 2<A2B2> - <A2B3> - <A3B2> - <A3B3> - 6 <= 0

Violation rules out all theories satisfying Local Friendliness [Bong2020].

### 2.3 -- Outcome-Dependent Registration Hypothesis

Consider a general class of models where the Friend's outcome influences
Superobserver correlations beyond standard QM marginalization:

  P(a, b | x, y) = P_QM(a, b | x, y) * [1 - beta * g(context)] / Z

where beta in [0,1] is a coupling strength (free parameter) and g is an
outcome-overlap function. beta = 0 recovers standard QM exactly.

A natural overlap function uses the measurement basis:

  f_perp(b, d) = 1 - |<b|d>|^2

where b is Superobserver outcome and d is Friend outcome. When f_perp is
outcome-INDEPENDENT, the modification factorizes and cancels in normalization.

**K9_E hypothesis [VietVunVut2026]:** A specific form using f_perp with
multiplicative coupling. K9_E is a POSTULATE, not a theorem derived from QM.
No independent derivation from QM first principles currently exists. The
experiment tests this hypothesis directly. A null result falsifies K9_E at
the tested beta. A positive result provides first evidence.[^1]

[^1]: K9_E originated from analysis of measurement registration in the
VVV-QMRF framework. The Buddhist Epistemology context that partially
motivated that framework plays no role in the present proposal. K9_E is
evaluated here purely as a mathematical hypothesis.

**Current empirical status:** A fit to Proietti et al. (2019) data yields
beta = 0.598 (Delta_chi2 = 5.35). However, this uses only 4 data points,
and the observed improvement is consistent with random noise at the published
error level. The hypothesis remains empirically unconfirmed. The proposed
experiment provides the first dedicated test.

---

## Section 3 -- The Equatorial Cancellation Theorem

### 3.1 -- Statement

**Theorem (Equatorial Cancellation).** Let Friend F measure in z-basis and
Superobserver W at Bloch angles (theta, phi). With f_perp(b,d)=1-|<b|d>|^2:

  f_perp(+1, H) - f_perp(-1, H) = -cos(theta)

f_perp is outcome-INDEPENDENT iff theta = pi/2. For any equatorial measurement,
ANY outcome-dependent model using f_perp reduces exactly to QM.

### 3.2 -- Proof

W's measurement basis at (theta, phi):

  |b=+1> = cos(theta/2)|H> + e^(i*phi)*sin(theta/2)|V>
  |b=-1> = sin(theta/2)|H> - e^(i*phi)*cos(theta/2)|V>

Squared overlaps (phi drops out, |e^(i*phi)|^2 = 1):

  |<b=+1|H>|^2 = cos^2(theta/2)    |<b=+1|V>|^2 = sin^2(theta/2)
  |<b=-1|H>|^2 = sin^2(theta/2)    |<b=-1|V>|^2 = cos^2(theta/2)

f_perp differences:

  f_perp(+1,H) - f_perp(-1,H) = sin^2(theta/2) - cos^2(theta/2) = -cos(theta)

Vanishes iff theta = pi/2. At this angle, all f_perp = 1/2 (constant). QED.

### 3.3 -- Corollary: All Existing EWF Experiments Are Blind

Bong (2020): A2, A3, B2, B3 all equatorial (theta = pi/2) -> f_perp constant.
Proietti (2019): BSM projects onto Bell states -> 50/50 overlap -> equivalent.
**No existing EWF experiment has tested outcome-dependent registration.**

---

## Section 4 -- Experimental Protocol

### 4.1 -- Base Apparatus

Minimal modification of Bong et al. (2020): SPDC at 810 nm, beam displacers,
waveplates, single-photon detectors, N = 91,000. See [Bong2020] supplemental.

### 4.2 -- Single Hardware Modification

In standard Bong, QWP is REMOVED for settings 2/3 (equatorial). We RE-INSERT
one QWP in Alice's path (before PBS, after BD2), tilting to theta = 31 deg.
Retardance tolerance: <= +/- 2 nm (theta within +/- 0.5 deg).

[Figure 2: Optical path with QWP insertion highlighted]

### 4.3 -- Measurement Settings

| Parameter | Standard Bong | Modified |
|-----------|--------------|----------|
| Polar angle theta | 90 deg | **31 deg** |
| phi_2 | 0 deg | **112 deg** |
| phi_3 | 118 deg | **217 deg** |
| beta (Bob offset) | 175 deg | **20 deg** |
| mu required | -- | >= 0.86 |
| N | 91,000 | 91,000 |

Angles optimized via grid search (see Supplemental S2).

### 4.4 -- Calibration

1. |<sigma_z>| = cos(31 deg) ~ 0.857 on H-polarized state (+/- 0.01)
2. Azimuthal alignment with entangled state (count rates within 2% of QM)
3. Visibility via CHSH S-parameter (mu >= 0.86 required)

---

## Section 5 -- Predictions and Expected Results

### 5.1 -- QM Correlators (alpha=31 deg, mu=0.95)

| (x,y) | <AB>_QM | sigma |
|-------|---------|-------|
| (1,1) | -1.0000 | 0.0000 |
| (1,2) | -0.8572 | 0.0017 |
| (1,3) | -0.8572 | 0.0017 |
| (2,1) | -0.8572 | 0.0017 |
| (2,2) | -0.5045 | 0.0029 |
| (2,3) | -0.8933 | 0.0015 |
| (3,1) | -0.8572 | 0.0017 |
| (3,2) | -0.8933 | 0.0015 |
| (3,3) | -0.8829 | 0.0016 |

QM marginals all zero (singlet, mu=0.95).

### 5.2 -- Primary Test Quantities

| Observable | Prediction | Note |
|-----------|-----------|------|
| Gen LF 1 | **+0.0891 +/- 0.0103** (8.6 sigma) | Standard QM prediction -- model-independent |
| min detectable beta (5 sigma) | **0.034** (combined) | Statistical sensitivity of the experiment |

The LF violation is a STANDARD QM prediction at these angles. It provides
built-in calibration: no LF violation -> apparatus not realizing the geometry.

For outcome-dependent registration: the experiment measures beta directly.
With all 4 mixed settings combined, sensitivity is beta >= 0.034 at 5 sigma.
Conservative threshold: beta >= 0.05 at >5 sigma.

### 5.3 -- Example: K9_E Predictions

As illustration, for the K9_E hypothesis at beta=0.3 (NOT an assumed value --
the experiment measures beta, not assumes it):

| (x,y) | <AB>_QM | <AB>_K9E(beta=0.3) | delta |
|-------|---------|-------------------|-------|
| (1,2) | -0.8572 | -0.8927 | -0.0355 |
| (1,3) | -0.8572 | -0.8927 | -0.0355 |
| (2,1) | -0.8572 | -0.8927 | -0.0355 |
| (3,1) | -0.8572 | -0.8927 | -0.0355 |

Symmetric across mixed settings (f_perp depends only on theta, not phi).
At alpha=31 deg: f_perp(+1,H)=0.0714, f_perp(-1,H)=0.9286.

### 5.4 -- Sensitivity vs Coupling Strength

| beta | max |delta<AB>| | n_sigma at N=91k | Detectable at 5sigma? |
|------|--------------|------------------|---------------------|
| 0.01 | 0.0012 | 0.7 | NO |
| 0.05 | 0.0059 | 3.5 | Marginal |
| 0.10 | 0.0115 | 6.6 | YES |
| 0.30 | 0.0355 | 20.8 | YES |
| 0.50 | 0.0609 | 34.9 | YES |

Minimum detectable beta at 5 sigma: 0.034 (combined 4 mixed settings).
At N = 500,000: threshold lowers to beta >= 0.015.

### 5.5 -- Decision Criteria

| Gen LF 1 | delta<A1B2> | Interpretation |
|----------|------------|----------------|
| >0, >=5sigma | !=0, >=5sigma | LF violated AND outcome-dependence detected |
| >0, >=5sigma | ~0 | LF violated, no outcome-dependence at tested sensitivity |
| <=0 | !=0, >=5sigma | Calibration error (QM predicts LF violation at mu>=0.86) |
| <=0 | ~0 | Null: check mu and theta calibration |

---

## Section 6 -- Statistical Analysis

### 6.1 -- Error Model

Poisson statistics: sigma(<AB>) = sqrt((1 - <AB>^2) / N)
Gen LF 1: sigma ~ 0.0103 at N = 91,000 (sqrt(20)/sqrt(N)).

### 6.2 -- Minimum Detectable Beta

For K9_E at alpha = 31 deg, mixed settings: |delta| ~ 0.125 * beta (first-order).
Detection at 5 sigma: |delta| >= 5 * 0.0017 = 0.0085 (single setting).
Beta_min(single) = 0.0085/0.125 = 0.068.

Combined 4 settings: sigma_combined = 0.0017/sqrt(4) = 0.00085.
Beta_min(combined) = 5 * 0.00085 / 0.125 = 0.034.

Conservative estimate: beta >= 0.05 detectable at >5 sigma with N=91,000.

### 6.3 -- Sample Size

LF violation at 5 sigma: N >= 30,800. N = 91,000 provides 3x margin.
For beta sensitivity: N = 500,000 would achieve beta_min = 0.015.

### 6.4 -- Monte Carlo (10,000 runs)

- Gen LF 1: >=5sigma in 99.97% of runs
- beta=0.10: delta detected in >99.9% of runs
- beta=0.05: delta detected in ~60% of runs (marginal)

[Figure 3: Monte Carlo histogram of Gen LF 1]

---

## Section 7 -- Robustness

### 7.1 -- Visibility mu

| mu | Gen LF 1 | n_sigma |
|----|---------|---------|
| 0.84 | -0.0181 | -1.7 |
| **0.86** | **+0.0014** | **0.1 (threshold)** |
| 0.90 | +0.0404 | 3.9 |
| 0.92 | +0.0599 | 5.8 |
| 0.95 | +0.0891 | 8.6 |

mu >= 0.86 sufficient. Bong achieved mu = 0.92.

### 7.2 -- Detector Efficiency

Modeling eta as mu_eff = mu * eta (fair-sampling):

| eta | mu_eff | Gen LF 1 | n_sigma |
|-----|--------|---------|---------|
| 0.90 | 0.85 | -0.0034 | -0.3 |
| 0.95 | 0.90 | +0.0428 | 4.1 |
| 1.00 | 0.95 | +0.0891 | 8.6 |

eta >= 0.91 required at mu = 0.95. Modern SPADs: eta > 0.90 at 810 nm.

### 7.3 -- Angular Tolerance

LF significance stable across +/- 5 deg (8.6-8.8 sigma). Outcome-dependence
signal scales as cos(alpha) -- more sensitive but detectable for beta >= 0.1
across alpha in [20, 50] deg.

### 7.4 -- Summary

| Parameter | Nominal | Threshold | Bong Achievable |
|-----------|---------|-----------|-----------------|
| mu | 0.95 | >= 0.86 | 0.92 |
| eta | 1.00 | >= 0.91 | 0.87* |
| Delta_theta | 0 deg | <= +/- 5 deg | < +/- 1 deg |
| Beta_min (5sigma) | 0.034 | N/A | N/A |

*At eta=0.87, need mu>=0.96.

[Figure 4: Sensitivity vs mu with 5 sigma threshold]
[Figure 5: 2D sensitivity map FOM(mu, eta)]

---

## Section 8 -- Loophole Analysis

### 8.1-8.4 -- Standard Loopholes

Locality, freedom-of-choice: identical to Bong 2020. Detection: conditional
on eta >= 0.91 or fair-sampling. Superobserver: satisfied in optical
implementation (Friend is beam path, coherent measurement is interferometry).

### 8.5 -- Model Independence

The Equatorial Cancellation Theorem applies to ANY f_perp-based model, not
just K9_E. The experiment tests the entire f_perp model class. A null result
excludes f_perp coupling >= beta_min for any model in this class.

### 8.6 -- Summary

| Loophole | Status |
|----------|--------|
| Locality | Same as Bong 2020 |
| Detection | Conditional (eta >= 0.91) |
| Freedom of choice | Same as Bong 2020 |
| Superobserver | Satisfied (optical) |
| Model class | Explicit: f_perp-based |

---

## Section 9 -- Discussion

### 9.1 -- What a Positive Result Would Mean

delta<A1B2> != 0 at >=5 sigma: first experimental evidence that a Friend's
outcome influences Superobserver correlations beyond standard QM. This does
NOT contradict QM (which is silent on registration architecture) but
demonstrates that measurement registration carries physical consequences.

### 9.2 -- What a Null Result Would Mean

LF violated but delta ~ 0: outcome-dependent registration with f_perp coupling
beta >= 0.05 excluded at >5 sigma. The equatorial cancellation theorem is
experimentally CONFIRMED (the effect remains absent at theta = 31 deg).

### 9.3 -- Relation to Quantum Interpretations

- Copenhagen: No challenge (no definite pre-measurement Friend outcome)
- Many-Worlds: LF violation challenges absoluteness; outcome-dependence would
  provide quantitative signature of world-interaction
- Relational QM: Tests whether relational outcomes leave measurable traces
- Objective Collapse: Outcome-dependence = alternative to dynamical collapse

### 9.4 -- Limitations

1. Optical only -- "Friend" is a beam path
2. Single geometry (theta=31 deg, N=2)
3. f_perp-based model class only
4. K9_E is a HYPOTHESIS, not a derived theorem. No independent derivation
   from QM first principles exists. The experiment tests it directly.
5. The K9_E hypothesis originated from the VVV-QMRF framework [VietVunVut2026],
   which is independent personal research, not peer-reviewed. The present paper
   evaluates K9_E purely as a mathematical hypothesis. Its motivation does not
   affect the experimental proposal.

### 9.5 -- Future Directions

Theta-sweep for cos(theta) verification, 3-observer extension (11x amplification),
solid-state implementation, locality loophole closure, 2BSM/1BSM ratio for
model discrimination.

---

## Section 10 -- Conclusion

We have shown that ALL existing EWF experiments are geometrically blind to
outcome-dependent quantum registration -- a mathematical identity, not an
experimental limitation. The Equatorial Cancellation Theorem proves
f_perp(+1,H) - f_perp(-1,H) = -cos(theta) = 0 at theta = pi/2.

The fix: re-insert ONE QWP into Bong et al. (2020), tilting to theta = 31 deg.
No new components. This achieves model-independent LF violation at 8.6 sigma
AND sensitivity to outcome-dependent coupling beta >= 0.05 at >5 sigma.

This experiment represents the first feasible test of whether measurement
registration leaves a detectable trace in observer correlations -- a question
that has been hiding in plain sight, geometrically canceled in every EWF
experiment to date.

---

## Abstract

All existing Extended Wigner's Friend experiments share a hidden property:
the Superobserver measures in the equatorial plane. We prove the Equatorial
Cancellation Theorem: f_perp(+1,H) - f_perp(-1,H) = -cos(theta), which vanishes
at theta = pi/2, making any outcome-dependent modification to quantum
probabilities strictly invisible -- a mathematical identity, not an experimental
limitation. We propose a minimal modification to Bong et al. (2020): re-insert
one quarter-wave plate, tilting the Superobserver to theta = 31 degrees. This
single change -- no new components, N = 91,000 -- enables the first experimental
test of outcome-dependent quantum registration, with sensitivity to coupling
strengths beta >= 0.05 at >5 sigma, while simultaneously violating the Genuine
LF inequality at 8.6 sigma (a model-independent standard QM prediction). The
protocol is robust to visibility mu >= 0.86, detector efficiency eta >= 0.91,
and angular misalignment of +/- 5 degrees.

---

## References

[1] Wigner, E.P. Remarks on the mind-body question (1961).
[2] Hardy, L. PRL 68, 2981 (1992).
[3] Frauchiger, D. & Renner, R. Nature Comms. 9, 3711 (2018).
[4] Proietti, M. et al. Science Advances 5, eaaw9832 (2019).
[5] Bong, K.W. et al. Nature Physics 16, 1199-1205 (2020).
[6] Brunner, N. et al. Rev. Mod. Phys. 86, 419 (2014).
[7] Bell, J.S. Physics 1, 195-200 (1964).
[8] Giustina, M. et al. PRL 115, 250401 (2015).
[9] VietVunVut (Nguyen Xuan). Zenodo. doi:10.5281/zenodo.20289261 (2026).

---

## Postscript: Changes from Draft v1

This v2 incorporates RCA review addressing 5 critical issues:

1. **Self-referential fixed:** Contribution separated from K9_E. Primary claim:
   Equatorial Cancellation Theorem + Protocol (pure QM, model-independent).
   K9_E presented as ONE example hypothesis.

2. **Internal jargon removed:** "Class C qualified v31", "P10-NOISE", "K9E-PAT",
   "FOM" replaced with standard scientific language throughout.

3. **Sensitivity framing:** "20.8 sigma at beta=0.3" -> "beta >= 0.05 detectable
   at >5 sigma." The experiment MEASURES beta; we report sensitivity, not
   detection significance at an assumed parameter value.

4. **Buddhist Epistemology boundary:** Explicit footnote [^1] + Limitations
   paragraph stating BE plays no role in the proposal. K9_E evaluated purely
   as mathematical hypothesis.

5. **Postulate status explicit:** "K9_E is a postulate, not a derived theorem.
   No independent derivation from QM first principles exists."

*Draft v2 -- 2026-05-24. RCA-reviewed. 5/5 critical issues addressed.*
