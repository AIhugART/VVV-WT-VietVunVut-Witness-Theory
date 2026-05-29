Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Experimental Test of Local Observer Independence: Supplementary Scientific Synthesis

## Bibliographic Information

**Paper:** "Experimental test of local observer independence"

**Authors:** Massimiliano Proietti, Alexander Pickston, Francesco Graffitti, Peter Barrow, Dmytro Kundys, Cyril Branciard, Martin Ringbauer, Alessandro Fedrizzi

**Journal:** Science Advances 5, eaaw9832 (2019)

**Published:** 20 September 2019

**DOI:** 10.1126/sciadv.aaw9832

**License noted in source summaries:** CC BY 4.0

---

## Purpose of This Supplementary Document

This document is a faithful supplementary synthesis of the scientific content represented in the available notes on Proietti et al. (2019) and its supplementary materials. Its purpose is to preserve the original scientific content, reduce redundancy, and organize the material into a publication-oriented reference.

This document does not add an external philosophical framework, does not reinterpret the experiment beyond the source summaries, and does not replace the original paper or supplementary materials.

---

## Abstract

The scientific method relies on facts established through repeated measurements and agreed upon universally, independently of who observed them. In quantum mechanics, the objectivity of observations is not clear, as illustrated by Wigner's friend thought experiment, where two observers can assign seemingly different descriptions to the same physical process.

Proietti et al. report an experimental test of an extended Wigner's friend scenario using four observers in a six-photon optical experiment. The associated Bell-type inequality is violated by more than five standard deviations. Under the assumptions of locality and free choice, the result implies that quantum theory must be interpreted in an observer-dependent way, or that at least one of the assumptions of locality, free choice, and observer-independent facts must fail.

---

## 1. Background and Motivation

### 1.1 The Measurement Problem

Quantum theory describes physical processes as continuous and deterministic under unitary evolution, except for observations, which are associated with instantaneous and probabilistic outcomes. This tension is known as the measurement problem. The theory does not specify a precise boundary between a unitary physical interaction and a measurement that produces a definite outcome.

### 1.2 Wigner's Friend Thought Experiment

In the original Wigner's friend scenario, a photon is prepared in an equal superposition of horizontal and vertical polarization. Wigner's friend, located inside an isolated laboratory, measures the photon and records one definite result in a physical memory:

- "photon is h"
- "photon is v"

From the friend's perspective, a definite fact has been established. From Wigner's external perspective, if the laboratory is treated quantum mechanically, the photon and the friend's record evolve into an entangled superposition:

```text
(1/sqrt(2))(|h> +/- |v>)
  -> (1/sqrt(2))(|h>|"photon is h"> +/- |v>|"photon is v">)
  = |F+/-_photon/record>
```

Wigner can in principle perform an interference measurement on the combined photon-record system. This creates a tension between the friend's definite recorded outcome and Wigner's coherent quantum description of the closed laboratory.

### 1.3 Observer-Independent Facts

The paper analyzes the assumption that facts established by measurements are observer-independent. In the Bell-Wigner setting, this is formulated as one of three assumptions:

- **O -- Observer-independent facts:** information obtained from a measurement is a fact of the world that all observers can agree on; such facts take definite values even if not all are co-measured.
- **L -- Locality:** one observer's measurement choice does not influence the outcome of a distant observer.
- **F -- Free choice:** Alice and Bob can freely and independently choose which measurements to perform.

Under these assumptions, the observed marginal probability distributions must be compatible with a single joint probability distribution for all relevant observables.

---

## 2. Theoretical Framework

### 2.1 Extended Wigner's Friend Scenario

The tested scenario extends Wigner's friend to four observers:

- Alice's friend
- Bob's friend
- Alice
- Bob

Alice's friend and Bob's friend each measure one photon from an entangled pair inside their respective laboratories and store the outcome in a physical memory. Alice and Bob, outside those laboratories, can each choose one of two measurements in each run.

### 2.2 Measurement Choices

Alice and Bob estimate the joint probability distributions P(Ax, By) for all combinations x, y in {0, 1}.

- **A0 / B0:** Alice or Bob measures the state of the friend's memory record. This corresponds to reading or attesting the friend's fact.
- **A1 / B1:** Alice or Bob jointly measures the friend's photon and the friend's record. This corresponds to a Wigner-type measurement on the combined system.

### 2.3 Joint Probability Requirement

If O, L, and F are all accepted, then there must exist a single joint probability distribution:

```text
P(A0, A1, B0, B1)
```

whose marginals reproduce the experimentally accessible distributions P(Ax, By).

### 2.4 Bell-Wigner Inequality

Any joint distribution satisfying O, L, and F must obey the CHSH-type Bell-Wigner inequality:

```text
S = <A1 B1> + <A1 B0> + <A0 B1> - <A0 B0> <= 2
```

where Ax and By take values in {-1, +1}, and:

```text
<Ax By> = sum_{a,b} ab * P(Ax = a, By = b)
```

A violation of this inequality means that the measured probability distributions are not compatible with O, L, and F all holding simultaneously. If locality and free choice are retained, then observer-independent facts must be abandoned in this experimental framework.

### 2.5 Difference from Standard Bell Tests

Although the experiment uses Bell-type mathematical machinery, the conceptual target differs from a standard Bell test.

| Feature | Standard Bell Test | Bell-Wigner Test |
|---|---|---|
| Shared assumptions | Locality, free choice | Locality, free choice |
| Additional assumption | Predetermination or local hidden variables | Observer-independent facts |
| What a violation constrains | Local hidden-variable accounts | Joint compatibility of observer-independent facts with locality and free choice |
| Required observables | Correlations between measurement outcomes | Observables representing facts associated with different observers |

A Bell-Wigner violation also implies a Bell violation, but not every Bell violation qualifies as a Bell-Wigner violation. The Bell-Wigner test requires specific observables that represent facts established by the inner and outer observers.

### 2.6 Definition of Observer

The paper uses a minimal physical definition of observer. An observer is any physical system that can extract information from another system through an interaction and store that information in a physical memory.

This definition does not require consciousness or macroscopic size. It includes human observers, computers, measurement devices, and simple quantum systems. Under the universality of quantum mechanics, the theory does not distinguish between microscopic and macroscopic systems as information storage devices.

---

## 3. Experimental Implementation

### 3.1 Overview

The experiment realizes the extended Wigner's friend scenario using a six-photon optical setup. Three entangled photon-pair sources provide the photons needed for the initial entangled pair and the two friend-memory systems.

The effective observers are implemented as follows:

- Alice's friend and Bob's friend are realized by nondestructive optical measurements using type-I fusion gates and ancilla photons.
- Alice and Bob perform either direct memory measurements or joint Bell-state-type measurements on the photon-memory systems.

### 3.2 Photon Sources

The setup uses three Sagnac-type interferometer photon-pair sources:

- S0
- SA
- SB

Each source generates pairs of 1550-nm photons entangled in polarization:

```text
|Psi-> = (|h>|v> - |v>|h>) / sqrt(2)
```

The sources are based on a 775-nm, 1.6-ps pulsed Ti:sapphire laser focused into a 22-mm periodically poled potassium titanyl phosphate (ppKTP) crystal. The down-conversion process is collinear type-II parametric down-conversion.

The laser repetition rate is 80 MHz and is temporally multiplexed to effectively quadruple the pulse rate while suppressing higher-order emissions.

Reported source and apparatus characteristics include:

- photon wavelength: 1550 nm
- signal-to-noise ratio: 140 +/- 10
- pair generation rate: approximately 8000 photon pairs per mW per second
- heralding efficiency: approximately 50%
- spectral filtering: 3-nm band-pass filters
- detectors: superconducting nanowire single-photon detectors (SNSPDs), approximately 80% efficiency
- coincidence window: 1 ns

### 3.3 Source Quality

Quantum state tomography gives the following source-quality figures:

| Quantity | Value |
|---|---|
| Fidelity | 99.62 +0.01 / -0.04 % |
| Purity | 99.34 +0.01 / -0.09 % |
| Concurrence | 99.38 +0.02 / -0.10 % |

After propagation through the optical circuit, the fidelities are:

| Source | Fidelity after transmission |
|---|---|
| S0 | 98.79 +/- 0.03 % |
| SA | 98.70 +/- 0.03 % |
| SB | 98.59 +/- 0.03 % |

### 3.4 Initial State Preparation

The photon pair from S0 is rotated by a half-wave plate at angle 7pi/16:

```text
|Psi_tilde> = (1 tensor U_{7pi/16}) |Psi->
U_{7pi/16} = cos(7pi/8) * sigma_z + sin(7pi/8) * sigma_x
```

This state is chosen to maximize the violation of the Bell-Wigner inequality for the selected measurement settings.

In the polarization basis, the state is represented as:

```text
|Psi_tilde>_ab =
  (1/sqrt(2)) cos(pi/8)(|h>_a |v>_b + |v>_a |h>_b)
+ (1/sqrt(2)) sin(pi/8)(|h>_a |h>_b - |v>_a |v>_b)
```

### 3.5 Friend Measurements Using Type-I Fusion Gates

Alice's friend and Bob's friend implement nondestructive polarization measurements using type-I fusion gates. Each gate uses:

- a polarizing beam splitter (PBS)
- a quarter-wave plate at pi/4
- a half-wave plate at pi/8
- an ancilla entangled photon pair from SA or SB

The operation is post-selected on coincident outputs and uses heralding photons to signal successful friend measurements.

For the nondestructive measurement of photon a, Alice's friend uses an ancilla pair from SA. The measurement copies the incoming photon's polarization information, with an h/v flip, into the memory photon:

```text
|h>_a |Psi->_a'a -> (1/2) |h>_a |v>_alpha
|v>_a |Psi->_a'a -> (1/2) |v>_a |h>_alpha
```

The memory encoding is:

```text
|"photon is h"> = |v>_alpha
|"photon is v"> = |h>_alpha
```

The total success probability per friend measurement is 1/4. The global success probability for both fusion gates is 1/16.

### 3.6 Four-Photon State After Friend Measurements

After both friend measurements succeed, Alice and Bob share a four-photon state involving the original photons and the memory photons:

```text
|Psi_tilde'>_{a,alpha,b,beta} =
  (1/sqrt(2)) cos(pi/8)
    (|hv>_{a,alpha} |vh>_{b,beta} + |vh>_{a,alpha} |hv>_{b,beta})
+ (1/sqrt(2)) sin(pi/8)
    (|hv>_{a,alpha} |hv>_{b,beta} - |vh>_{a,alpha} |vh>_{b,beta})
```

Here, photons a and b are the original photons from S0, while alpha and beta carry the friends' memory records.

### 3.7 Alice and Bob's Observables

Alice and Bob measure the following observables on their local photon-memory systems:

```text
A0 = B0 = 1 tensor (|v><v| - |h><h|)
A1 = B1 = |Psi+><Psi+| - |Psi-><Psi-|
```

where:

```text
|Psi+/- > = (|hv> +/- |vh>) / sqrt(2)
```

The A0 / B0 observables read the friend's record. They are implemented by direct polarization measurement on the memory photon, without a beam splitter.

The A1 / B1 observables are Wigner-type joint measurements on the photon and memory. They are implemented using a 50/50 beam splitter followed by polarization projection. Nonclassical interference enables a partial Bell-state measurement.

The Bell-state measurement fidelity reported from quantum measurement tomography is:

```text
F_BSM = 96.84 +0.05 / -0.05 %
```

### 3.8 Data Collection

The main experiment used:

- 64 total measurement settings
- 4 x 4 eigenstates for each observable pair
- 1794 six-photon coincidence events
- 360 hours of total measurement time
- 100 mW pump power

The low pump power was used to suppress higher-order photon emissions from probabilistic photon-pair sources.

---

## 4. Main Results

### 4.1 Measured Expectation Values

The measured expectation values are:

| Observable pair | Measured value |
|---|---|
| <A0 B0> | -0.678 +/- 0.033 |
| <A0 B1> | 0.570 +/- 0.040 |
| <A1 B0> | 0.595 +/- 0.041 |
| <A1 B1> | 0.571 +/- 0.034 |

### 4.2 Bell-Wigner Parameter

The Bell-Wigner parameter is:

```text
S_exp = <A1 B1> + <A1 B0> + <A0 B1> - <A0 B0>
      = 2.416 +/- 0.075
```

This violates the observer-independent bound:

```text
S <= 2
```

by more than five standard deviations.

### 4.3 Error Analysis

Each expectation value is calculated from 16 measured six-photon coincidence counts. The counts are modeled using Poisson statistics:

```text
sigma^2_{n_i} = n_i
```

The propagated uncertainty is:

```text
sigma^2_f(n1,...,n16) = sum_{i=1}^{16} (df/dn_i)^2 * sigma^2_{n_i}
```

The four expectation values are statistically independent, so their uncertainties are combined independently. A Monte Carlo routine with 100,000 samples was also used to account for low-count and potentially asymmetric error behavior. The two methods agreed to within 0.0032.

### 4.4 Primary Experimental Limitation

The main experimental limitation is higher-order photon emissions from probabilistic photon-pair sources. Higher-order contributions scale with a higher exponent of pump power and are reduced by operating at relatively low pump power.

The cross-polarization design also helps prevent three-pair emissions from S0 from producing false coincidences.

---

## 5. Supplementary Results

### 5.1 Alternative Observables A0 and B0

The supplementary analysis includes an alternative definition of A0 and B0 from Brukner (2018):

```text
A0 = B0 = |h><h| tensor |"photon is h"><"photon is h"|
        - |v><v| tensor |"photon is v"><"photon is v"|
```

This observable measures both the friend's record and the original photon as a consistency check. If the photon state is inconsistent with the recorded memory, the measurement result is assigned 0.

On the four-photon state, the assignment is:

- |hv> -> +1
- |vh> -> -1
- |hh> and |vv> -> 0

The results with this alternative definition are:

| Observable pair | Measured value |
|---|---|
| <A0 B0> | -0.662 +/- 0.033 |
| <A0 B1> | 0.573 +/- 0.039 |
| <A1 B0> | 0.600 +/- 0.040 |
| <A1 B1> | 0.571 +/- 0.034 |
| S_exp | 2.407 +/- 0.073 |

This again violates the Bell-Wigner inequality by more than five standard deviations.

### 5.2 Alternative Measurement Protocol for A0 and B0

A second supplementary protocol uses linear polarizers in the relevant modes before the beam splitter, rather than removing the beam splitter. This prevents interference while avoiding changes to optical alignment.

The protocol reduces the success probability of A0 / B0 measurements by a factor of 1/4 and increases statistical uncertainty. It was implemented for the alternative A0 / B0 definition.

The results are:

| Observable pair | Measured value |
|---|---|
| <A0 B0> | -0.609 +/- 0.048 |
| <A0 B1> | 0.577 +/- 0.049 |
| <A1 B0> | 0.588 +/- 0.049 |
| <A1 B1> | 0.571 +/- 0.034 |
| S_exp | 2.346 +/- 0.110 |

This violates the Bell-Wigner inequality by more than three standard deviations. The reduced violation relative to the main protocol is attributed to approximately 4.83 +/- 0.97% photon loss introduced by the polarizers.

### 5.3 Supplementary Figures Represented in the Source Notes

The supplementary material is described as including:

- **Fig. S1:** detailed experimental setup, including laser, temporal multiplexing, photon sources, fusion gates, measurement modules, and SNSPDs.
- **Fig. S2:** full experimental data for the alternative observable analysis.
- **Fig. S3:** full data for the alternative measurement protocol.

---

## 6. Loopholes and Limitations

### 6.1 General Loopholes

Bell-Wigner tests inherit the main loopholes of conventional Bell tests:

- detection loophole
- locality loophole
- freedom-of-choice loophole

Due to the increased complexity of the Bell-Wigner configuration, closing these loopholes is more demanding than in standard Bell tests.

In the present experiment, the detection and space-time loopholes are addressed by assumptions such as fair sampling and by empirical checks such as absence of signaling consistent with Poissonian statistics.

### 6.2 Locality and Freedom-of-Choice Loopholes

The experiment is analogous to an event-ready Bell test. The successful fusion-gate events herald which experimental runs contribute to the Bell-Wigner test.

A fully loophole-free configuration would require:

- heralding events to be space-like separated from Alice's and Bob's setting choices
- each party's setting choice to be space-like separated from the other party's measurement outcome

### 6.3 Detection Loophole

The limited fusion-gate success probability does not by itself create a detection loophole in an event-ready configuration, because only heralded events contribute. However, for the fusion gates to be genuinely event-ready, the ancilla detectors should be photon-number resolving.

Closing the detection loophole also requires measurement protocols capable of projecting onto the relevant eigenstates in a single run.

The source summaries report a minimum symmetric combined detection efficiency threshold:

```text
eta > 0.875
```

This is more demanding than the standard CHSH threshold for maximally entangled states:

```text
eta > 0.828
```

### 6.4 Bell-Wigner-Specific Loophole

A loophole specific to Bell-Wigner tests concerns whether A0 and B0 genuinely measure only the friend's memory records. If these observables also effectively measure the original photon in a way that compromises the interpretation as reading the friend's fact, the Bell-Wigner interpretation is weakened.

Closing this loophole requires measurement devices that clearly separate the original system from the memory system and measure only the memory photons for A0 and B0.

### 6.5 Status of Photonic Observers

The experiment treats photonic memory systems as observers under the paper's minimal physical definition: systems that extract information and store it in physical memory.

Denying photonic memories the status of observers would require modifying or restricting this definition, potentially invoking new physics beyond standard quantum mechanics. The paper emphasizes that the conflict arises between recorded facts, not from consciousness itself.

---

## 7. Interpretive Consequences Discussed in the Source Material

### 7.1 Main Logical Consequence

Accepting the status of the photonic memories as observers and modulo remaining loopholes, the violation of the Bell-Wigner inequality implies that at least one of the following assumptions must fail:

1. **Free choice (F):** Alice and Bob can freely choose their measurements.
2. **Locality (L):** Alice's and Bob's choices do not influence each other's outcomes.
3. **Observer-independent facts (O):** measurement outcomes are facts of the world that all observers can agree on.

If locality and free choice are retained, then observer-independent facts cannot be maintained in the tested framework.

### 7.2 Interpretations Mentioned

The source material discusses several possible interpretive responses:

- **Many-worlds / Everett:** facts may be established from a privileged global wavefunction perspective.
- **Bohmian mechanics:** a global hidden-variable framework may provide a privileged description.
- **Relational quantum mechanics:** facts are defined relative to observers.
- **QBism:** quantum mechanics is treated as a tool for an agent's subjective expectations about future measurement outcomes.

Observer-relative interpretations allow different observers to assign incompatible accounts of what happened in an experiment, while remaining internally consistent within their respective descriptions.

### 7.3 Relationship to Frauchiger-Renner

The source summaries note a relationship to the Frauchiger-Renner theorem, which is another no-go theorem concerning quantum theory's ability to describe its own use. That theorem rests on different assumptions and does not explicitly include locality. Its interpretation within nonlocal theories remains debated.

### 7.4 Open Relativistic Question

The source summaries also mention an open question: whether the conclusions drawn from Bell or Bell-Wigner tests change under relativistic conditions, including scenarios with non-inertial observers or horizons.

---

## 8. What the Experiment Does Not Establish

The source material explicitly separates the scientific conclusion from unsupported extrapolations. The experiment does not establish that:

- consciousness creates reality
- human observers are special
- quantum mysticism follows from the result
- simulation theory follows from the result

The experiment tests the compatibility of observer-independent facts with locality, free choice, and quantum predictions in a specific extended Wigner's friend configuration.

---

## 9. Key Numerical Summary

| Quantity | Value |
|---|---|
| Main Bell-Wigner parameter | S_exp = 2.416 +/- 0.075 |
| Main violation significance | More than 5 standard deviations |
| Alternative observable result | S_exp = 2.407 +/- 0.073 |
| Alternative measurement protocol result | S_exp = 2.346 +/- 0.110 |
| Classical / observer-independent bound | S <= 2 |
| Six-photon coincidences | 1794 |
| Total measurement time | 360 hours |
| Pump power | 100 mW |
| Photon wavelength | 1550 nm |
| Source fidelity at source | 99.62 +0.01 / -0.04 % |
| Bell-state measurement fidelity | 96.84 +/- 0.05 % |
| Minimum detection efficiency for loophole-free Bell-Wigner test | eta > 0.875 |
| Standard CHSH comparison threshold | eta > 0.828 |

---

## 10. Key Equation Reference

| Equation | Description |
|---|---|
| `|F+/-_photon/record> = (1/sqrt(2))(|h>|"h"> +/- |v>|"v">)` | Wigner's description of photon and friend record |
| `S = <A1 B1> + <A1 B0> + <A0 B1> - <A0 B0> <= 2` | Bell-Wigner inequality |
| `|Psi-> = (|h>|v> - |v>|h>) / sqrt(2)` | Entangled source state |
| `|Psi_tilde> = (1 tensor U_{7pi/16}) |Psi->` | Rotated input state from S0 |
| `A0 = B0 = 1 tensor (|v><v| - |h><h|)` | Friend-record observable |
| `A1 = B1 = |Psi+><Psi+| - |Psi-><Psi-|` | Wigner-type joint observable |
| `S_exp = 2.416 +/- 0.075` | Main measured Bell-Wigner parameter |

---

## 11. References Listed in the Source Summaries

1. K. Popper, *Realism and the Aim of Science*, Routledge (1992).
2. E. Wigner, "Remarks on the mind-body problem," in *The Scientist Speculates* (1961), pp. 284-302.
3. C. Brukner, "On the quantum measurement problem," arXiv:1507.05255 (2015).
4. C. Brukner, "A no-go theorem for observer-independent facts," *Entropy* 20, 350 (2018).
5. D. Frauchiger and R. Renner, "Quantum theory cannot consistently describe the use of itself," *Nature Communications* 9, 3711 (2018).
6. D. Deutsch, "Quantum theory as a universal physical theory," *International Journal of Theoretical Physics* 24, 1-41 (1985).
7. R. Healey, "Quantum theory and the limits of objectivity," *Foundations of Physics* 48, 1568-1589 (2019).
8. V. Baumann, F. Del Santo, and C. Brukner, "Comment on Healey's 'Quantum theory and the limits of objectivity'," *Foundations of Physics* 49, 741-749 (2019).
9. A. Fine, "Hidden variables, joint probability, and the Bell inequalities," *Physical Review Letters* 48, 291-295 (1982).
10. J. Clauser, M. Horne, A. Shimony, and R. Holt, "Proposed experiment to test local hidden-variable theories," *Physical Review Letters* 23, 880-884 (1969).
11. J. S. Bell and A. Aspect, *Speakable and Unspeakable in Quantum Mechanics*, Cambridge University Press (2004).
12. J. S. Bell, "On the Einstein Podolsky Rosen paradox," *Physics* 1, 195-200 (1964).
13. V. Baumann and C. Brukner, "Wigner's friend as a rational agent," arXiv:1901.11274 (2019).
14. F. Graffitti et al., "Independent high-purity photons created in domain-engineered crystals," *Optica* 5, 514 (2018).
15. F. Graffitti et al., "Design considerations for high-purity heralded single-photon sources," *Physical Review A* 98, 053811 (2018).
16. R.-B. Jin et al., "Pulsed Sagnac polarization-entangled photon source with a PPKTP crystal at telecom wavelength," *Optics Express* 22, 11498 (2014).
17. D. E. Browne and T. Rudolph, "Resource-efficient linear optical quantum computation," *Physical Review Letters* 95, 010501 (2005).
18. J.-W. Pan et al., "Experimental demonstration of four-photon entanglement and high-fidelity teleportation," *Physical Review Letters* 86, 4435-4438 (2001).
19. J.-A. Larsson, "Loopholes in Bell inequality tests of local realism," *Journal of Physics A* 47, 424003 (2014).
20. G. C. Ghirardi, A. Rimini, and T. Weber, "Unified dynamics for microscopic and macroscopic systems," *Physical Review D* 34, 470-491 (1986).
21. D. Lazarovici and M. Hubert, "How quantum mechanics can consistently describe the use of itself," *Scientific Reports* 9, 470 (2019).
22. H. I. Everett III, "Relative state formulation of quantum mechanics," *Reviews of Modern Physics* 29, 454-462 (1957).
23. D. Bohm, "A suggested interpretation of the quantum theory in terms of hidden variables," *Physical Review* 85, 166-179 (1952).
24. C. Rovelli, "Relational quantum mechanics," *International Journal of Theoretical Physics* 35, 1637 (1996).
25. C. A. Fuchs, "Notwithstanding Bohr, the reasons for QBism," *Mind and Matter* 15, 245-300 (2017).
26. I. Durham, "Observer-independence in the presence of a horizon," arXiv:1902.09028 (2019).
27. A. Fedrizzi et al., "A wavelength-tunable fiber-coupled source of narrowband entangled photons," *Optics Express* 15, 15377-15386 (2007).
28. M. A. Broome et al., "Reducing multi-photon rates in pulsed down-conversion by temporal multiplexing," *Optics Express* 19, 22698-22708 (2011).
29. J. Calsamiglia and N. Lutkenhaus, "Maximum efficiency of a linear-optical Bell-state analyzer," *Applied Physics B* 72, 67-71 (2001).
30. S. L. Braunstein and A. Mann, "Measurement of the Bell operator and quantum teleportation," *Physical Review A* 51, R1727-R1730 (1995).
31. P. H. Eberhard, "Background level and counter efficiencies required for a loophole-free EPR experiment," *Physical Review A* 47, R747-R750 (1993).

---

## Consolidation Note

This synthesis consolidates the five available source notes in the Proietti et al. 2019 supplementary folder. It preserves the scientific content represented there, removes repetition, and keeps the conclusion conditional on the assumptions used in the original Bell-Wigner framework.
