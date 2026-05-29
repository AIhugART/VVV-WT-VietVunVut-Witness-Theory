# Experimental Test of Local Observer Independence

**Authors:** Massimiliano Proietti, Alexander Pickston, Francesco Graffitti, Peter Barrow, Dmytro Kundys, Cyril Branciard, Martin Ringbauer, Alessandro Fedrizzi
**Published:** Science Advances, Vol. 5, eaaw9832, 20 September 2019
**DOI:** 10.1126/sciadv.aaw9832
**License:** CC BY 4.0

---

## Abstract

The scientific method relies on facts established through repeated measurements and agreed upon universally, independently of who observed them. In quantum mechanics, the objectivity of observations is not clear, most markedly exposed in Wigner's eponymous thought experiment where two observers can experience seemingly different realities. Using a state-of-the-art six-photon experiment, the authors realize an extended Wigner's friend scenario and experimentally violate the associated Bell-type inequality by five standard deviations. If locality and free choice are assumed, this result implies that quantum theory must be interpreted in an observer-dependent way.

---

## 1. Background and Motivation

### 1.1 The Measurement Problem

The observer's role as arbiter of universal facts was challenged by 20th century physics. In quantum theory, all physical processes are continuous and deterministic except for observations, which are instantaneous and probabilistic. This conflict — the measurement problem — arises because quantum theory provides no precise cut between a unitary physical interaction and a measurement.

### 1.2 Wigner's Friend Thought Experiment

Consider a single photon in a superposition of horizontal |h> and vertical |v> polarization, measured by an observer (Wigner's friend) inside an isolated laboratory.

- The friend randomly observes one of two outcomes per run: h or v.
- Her record is stored in a physical memory state: |"photon is h"> or |"photon is v">.
- This constitutes a fact from her point of view.

From outside the closed laboratory, Wigner must describe the measurement as a unitary interaction, leaving photon and friend's record in the entangled state:

```
(1/sqrt(2))(|h> +/- |v>) --> (1/sqrt(2))(|h>|"photon is h"> +/- |v>|"photon is v">) =: |F±_photon/record>
```

Wigner can perform an interference experiment to verify this superposition — a fact from his point of view. But this contradicts the friend's definite outcome. The friend can even inform Wigner that she recorded a definite outcome (without revealing it), yet their descriptions remain unchanged. This raises the question: can their records be reconciled, or are they fundamentally incompatible as observer-independent facts of the world?

---

## 2. Theoretical Framework

### 2.1 Extended Wigner's Friend Scenario

The scenario is extended to four observers: Alice, Bob, Alice's friend, and Bob's friend. An entangled state is shared between two separate laboratories.

- Alice's friend and Bob's friend each measure their respective subsystem nondestructively and record the outcome.
- Alice and Bob, outside the labs, can each choose one of two measurements per run:
  - **A0 / B0**: Measure the state of their friend's record (attest the friend's fact).
  - **A1 / B1**: Jointly measure the friend's record and the friend's system (establish their own fact).

After many runs, Alice and Bob estimate the joint probability distributions P(Ax, By) for all four combinations x, y in {0, 1}.

### 2.2 Three Core Assumptions

The no-go theorem (Brukner 2018) considers three assumptions:

- **O (Observer-independent facts):** A record obtained from a measurement is a fact of the world that all observers can agree on. Such facts take definite values even if not all are co-measured.
- **L (Locality):** Alice's and Bob's choices do not influence each other's outcomes.
- **F (Free choice):** Alice and Bob can freely and independently choose their measurements.

Under O, L, and F, it must be possible to construct a single joint probability distribution P(A0, A1, B0, B1) whose marginals match all observed P(Ax, By).

### 2.3 The Bell-Wigner Inequality

Any joint probability distribution satisfying O, L, and F must obey the Clauser-Horne-Shimony-Holt (CHSH) inequality:

```
S = <A1 B1> + <A1 B0> + <A0 B1> - <A0 B0> <= 2
```

where <Ax By> = sum_{a,b} ab * P(Ax=a, By=b), and outcomes a, b in {-1, +1}.

A violation of this inequality, given assumptions L and F, implies that the observed probability distributions are incompatible with observer-independent facts (assumption O).

### 2.4 Distinction from Standard Bell Tests

Although Bell's mathematical machinery is used, the Bell-Wigner test differs from standard Bell tests:

- Standard Bell tests rule out Local Hidden Variable theories via the assumption of **predetermination (PD)**: outcomes are deterministic or stochastic but pre-exist measurement.
- Bell-Wigner tests rule out **observer-independent facts (O)**: outcomes exist as objective facts accessible to all observers.
- Bell-Wigner tests use specific observables that represent facts relative to different observers.
- Any Bell-Wigner violation implies a Bell violation, but not vice versa.

### 2.5 Definition of Observer

Formally, an observation is the act of extracting and storing information about an observed system. An observer is any physical system that can extract information from another system via some interaction and store that information in a physical memory. This definition covers human observers, classical computers, quantum computers, and simple measurement devices. Quantum mechanics does not distinguish between large (even conscious) and small physical systems (universality principle).

---

## 3. Experimental Setup

### 3.1 Overview

The experiment uses three photon-pair sources based on a Sagnac-type interferometer design: S0, SA, and SB. Each generates pairs of 1550-nm single photons entangled in the polarization degree of freedom in the state:

```
|Psi-> = (|h>|v> - |v>|h>) / sqrt(2)
```

State quality (measured via quantum state tomography):
- Fidelity: F = 99.62 (+0.01 / -0.04) %
- Purity: P = 99.34 (+0.01 / -0.09) %
- Concurrence: C = 99.38 (+0.02 / -0.10) %

After further transmission to the fusion gates, fidelities degrade slightly:
- F0 = 98.79 (+0.03 / -0.03) % (source S0)
- FA = 98.70 (+0.03 / -0.03) % (source SA)
- FB = 98.59 (+0.03 / -0.03) % (source SB)

### 3.2 Laser and Source Details

- Pump laser: 775-nm, 1.6 ps pulsed Ti:sapphire laser
- Crystal: 22-mm periodically poled potassium titanyl phosphate (ppKTP) in Sagnac interferometer
- Process: collinear type-II parametric down-conversion
- Repetition rate: 80 MHz, quadrupled via temporal multiplexing to suppress higher-order emissions
- Signal-to-noise ratio: 140 +/- 10 (photon pairs vs. higher-order contributions)
- Pair generation rate: ~8000 photon pairs per mW per second
- Heralding efficiency: ~50%
- Spectral filtering: 3-nm band-pass filters
- Detectors: superconducting nanowire single-photon detectors (SNSPDs), ~80% detection efficiency
- Coincidence window: 1 ns (field-programmable gate array time-tagger)

### 3.3 Initial State Preparation

The photon pair from source S0 is rotated using a half-wave plate (HWP) at angle 7pi/16:

```
|Psi~> = (1 ⊗ U_{7pi/16}) |Psi->
U_{7pi/16} = cos(7pi/8) * sigma_z + sin(7pi/8) * sigma_x
```

This state maximizes the violation of the Bell-Wigner inequality for the chosen measurement settings.

### 3.4 Friend Measurements via Type-I Fusion Gates

Alice's friend and Bob's friend each implement a nondestructive polarization measurement using a type-I fusion gate (FGI). Each fusion gate uses:
- A polarizing beam splitter (PBS): transmits horizontal, reflects vertical photons
- A quarter-wave plate (QWP) at pi/4 and a half-wave plate at pi/8 behind the PBS
- An ancilla entangled photon pair from SA (or SB)

The gate realizes the transformation (for post-selected coincident outputs):

```
|h>|h> --PBS--> |h>|h> --Q/HWP--> |h> (|h> + i|v>) / sqrt(2)
|v>|v> --PBS--> |v>|v> --Q/HWP--> |v> (|h> - i|v>) / sqrt(2)
```

The heralding (second) photon is projected onto |h> via another PBS.

The fusion gate operation is:

```
FGI = (1/sqrt(2)) (i |h><h| ⊗ |h><h| - |v><v| ⊗ |v><v|)
```

Success probability: 1/2.

For nondestructive measurement of photon a, Alice's friend uses ancilla |Psi->_{a'a} from SA:

```
|h>_a |Psi->_{a'a} --FGI--> (1/2) |h>_a |v>_alpha
|v>_a |Psi->_{a'a} --FGI--> (1/2) |v>_a |h>_alpha
```

The state of the incoming photon is copied (with h <-> v flip) onto photon alpha (the memory). The encoding is:

```
|"photon is h"> = |v>_alpha
|"photon is v"> = |h>_alpha
```

Total success probability per friend measurement: 1/4.

### 3.5 Four-Photon Entangled State

After both friends successfully measure, the joint state of photons a, alpha, b, beta shared by Alice and Bob is:

```
|Psi~'>_{a,alpha,b,beta} =
  (1/sqrt(2)) cos(pi/8) (|hv>_{a,alpha} |vh>_{b,beta} + |vh>_{a,alpha} |hv>_{b,beta})
+ (1/sqrt(2)) sin(pi/8) (|hv>_{a,alpha} |hv>_{b,beta} - |vh>_{a,alpha} |vh>_{b,beta})
```

Global success probability for both fusion gates: 1/16.

### 3.6 Alice and Bob's Measurements

Alice and Bob measure the following observables on their joint photon/friend's-record systems:

```
A0 = B0 = 1 ⊗ (|v><v| - |h><h|)
A1 = B1 = |Psi+><Psi+| - |Psi-><Psi-|
```

where |Psi+/-> = (|hv> +/- |vh>) / sqrt(2).

Equivalently on the four-photon state |Psi~'>:
- A0 / B0: project onto |hv> and |vv> (eigenvalue +1), |hh> and |vh> (eigenvalue -1), using QWP and HWP before PBS, without beam splitter.
- A1 / B1: use a 50/50 beam splitter (BS) followed by projection onto |vh>, implementing a Bell-state measurement. Due to nonclassical interference, this projects onto the singlet |Psi-> with success probability 1/2. |Psi+> takes eigenvalue +1, |Psi-> takes eigenvalue -1, |Phi+/-> take eigenvalue 0.

Bell-state measurement fidelity (quantum measurement tomography): F_bsm = 96.84 (+0.05 / -0.05) %.

Note: A0 cannot be measured by ignoring photon a due to the probabilistic photon source. Photon a must be measured in a polarization-insensitive way by summing projections onto both orthogonal polarizations.

---

## 4. Results

### 4.1 Measured Expectation Values

From 1794 six-photon coincidence events collected over 360 hours (64 measurement settings, 4x4 eigenstates per observable pair):

```
<A0 B0> = -0.678 (+0.033 / -0.033)
<A0 B1> =  0.570 (+0.040 / -0.040)
<A1 B0> =  0.595 (+0.041 / -0.041)
<A1 B1> =  0.571 (+0.034 / -0.034)
```

### 4.2 Bell-Wigner Parameter

```
S_exp = <A1 B1> + <A1 B0> + <A0 B1> - <A0 B0>
      = 2.416 (+0.075 / -0.075)
```

This violates the classical bound of S <= 2 by more than five standard deviations.

Theoretical prediction for ideal states: probabilities of approximately 1/4 * (1 + 1/sqrt(2)) ~= 0.427 and 1/4 * (1 - 1/sqrt(2)) ~= 0.073.

### 4.3 Primary Limitation

The main experimental limitation is higher-order photon emissions from the probabilistic photon-pair sources. Higher-order contributions (four or more photon pairs) scale with a higher exponent of pump power and are suppressed by operating at a relatively low pump power of 100 mW. The cross-polarization design prevents three-pair emissions from S0 from producing false coincidences.

### 4.4 Error Analysis

Each <Ax By> is calculated from 16 measured six-fold coincidence counts ni following Poisson statistics with variance sigma^2_{ni} = ni. Uncertainty propagation:

```
sigma^2_f(n1,...,n16) = sum_{i=1}^{16} (df/dni)^2 * sigma^2_{ni}
```

The four expectation values are statistically independent, so uncertainties are combined independently. A Monte Carlo routine with 100,000 samples was also used to handle potentially asymmetric errors at low count rates. Both methods agree to within 0.0032.

---

## 5. Alternative Observables and Protocols

### 5.1 Alternative Definition of A0, B0 (from Brukner 2018)

An alternative observable definition:

```
A0 = B0 = |h><h| ⊗ |"photon is h"><"photon is h"| - |v><v| ⊗ |"photon is v"><"photon is v"|
```

This measures both the friend's record and the original photon as a consistency check. If the photon state is inconsistent with the record, the measurement result is assigned 0.

On the four-photon state, this assigns: |hv> -> +1, |vh> -> -1, |hh> and |vv> -> 0.

Results with this definition:

```
<A0 B0> = -0.662 (+0.033 / -0.033)
<A0 B1> =  0.573 (+0.039 / -0.039)
<A1 B0> =  0.600 (+0.040 / -0.040)
<A1 B1> =  0.571 (+0.034 / -0.034)   [unchanged]

S_exp = 2.407 (+0.073 / -0.073)
```

Again violates the Bell-Wigner inequality by more than 5 standard deviations.

### 5.2 Alternative Measurement Protocol for A0, B0

A less invasive method: introduce linear polarizers in modes a (b) and alpha (beta) before the beam splitter, preventing interference. This measures photons before the BS without disturbing optical alignment.

This protocol was implemented for the alternative A0, B0 definition. It reduces the success probability of measuring A0 (B0) by a factor of 1/4. To compensate, the 16 eigenvectors were fully measured only for <A1 B1>; other observables used only non-zero eigenvalue projections, normalized against total <A1 B1> counts.

Results:

```
<A0 B0> = -0.609 (+0.048 / -0.048)
<A0 B1> =  0.577 (+0.049 / -0.049)
<A1 B0> =  0.588 (+0.049 / -0.049)
<A1 B1> =  0.571 (+0.034 / -0.034)   [unchanged]

S_exp = 2.346 (+0.110 / -0.110)
```

Violates the Bell-Wigner inequality by more than 3 standard deviations. The reduced violation (compared to the main protocol) is due to approximately 4.83 +/- 0.97% loss introduced by the polarizers, which reduces counts in A0/B0 settings relative to normalization, thereby reducing <A0 B1>, <A1 B0>, and <A0 B0>.

---

## 6. Loopholes and Path to Loophole-Free Test

### 6.1 General Loopholes

Bell-Wigner tests are subject to the same loopholes as conventional Bell tests: locality loophole, freedom-of-choice loophole, and detection loophole. Due to increased experimental complexity, practical requirements for closing these loopholes are significantly more challenging than for standard Bell tests.

In the present experiment:
- **Detection and space-time loopholes**: addressed by the assumption of fair sampling and empirically verified absence of signaling (consistent with Poissonian statistics).
- **Observable interpretation**: it is assumed (with negligible experimental deviations) that the measured A0, B0 factorize as in the main definition, with identity on the photon system, so that A0 and B0 genuinely measure the friends' records.

### 6.2 Locality and Freedom-of-Choice Loopholes

The experiment is analogous to an event-ready Bell test: detection of ancilla photons in the fusion gates heralds which events contribute to the Bell-Wigner test. Closing these loopholes requires:
- Heralding events space-like separated from Alice's and Bob's setting choices.
- Each party's setting choice space-like separated from the other party's measurement outcome.

### 6.3 Detection Loophole

Limited fusion gate success probability is not an issue in the event-ready configuration: only heralded events contribute. However, to ensure the fusion gates are genuinely event-ready, the ancilla detectors should be photon-number-resolving.

For closing the detection loophole, the measurement protocol must project onto any eigenstate in any single run (not projecting onto each eigenstate separately across different runs).

Practical implementations:
- For A0/B0: pass the friend's photon through a PBS with detectors at both outputs.
- For A1/B1: a full Bell-state measurement with linear optics is impossible, but it suffices to distinguish |Psi+>, |Psi->, and a third outcome for |Phi+/->. This can be done with detectors added to the second PBS outputs.

### 6.4 Minimum Required Detection Efficiency

Assuming symmetric combined detection efficiency eta per photon, with fixed output (+1) assigned when a detector fails:

```
<A0 B0> = eta^2 * (-1/sqrt(2)) + (1-eta)^2
<A0 B1> = <A1 B0> = eta^3 * (1/sqrt(2)) + (1-eta)(1-eta^2)
<A1 B1> = eta^4 * (1/sqrt(2)) + (1-eta^2)^2
```

Minimum detection efficiency required (for perfect quantum states):

```
eta > sqrt(3(1 - 1/sqrt(2))) - 1 ~= 0.875
```

This is more stringent than for a standard CHSH test with maximally entangled states, which requires eta > 2*sqrt(2) - 2 ~= 0.828. Non-maximally entangled states could potentially relax this requirement, at the cost of reduced violation.

### 6.5 Bell-Wigner-Specific Loophole

A loophole specific to Bell-Wigner tests: if A0 and B0 do not strictly measure only the friend's memory (but also the system photon), the interpretation as unveiling the friend's fact is compromised. Closing this loophole requires measurement devices for A0 and B0 that clearly separate the initial system from the friend's memory, measuring only the memory photon.

---

## 7. Discussion and Interpretations

### 7.1 Main Conclusion

Accepting the photons' status as observers and modulo remaining loopholes, the violation of S <= 2 implies that at least one of the following assumptions must fail:

1. **Free choice (F):** Alice and Bob can freely choose their measurements.
2. **Locality (L):** Alice's and Bob's choices do not influence each other's outcomes.
3. **Observer-independent facts (O):** Measurement outcomes are facts of the world that all observers agree on.

### 7.2 Relationship to Frauchiger-Renner Theorem

The related no-go theorem by Frauchiger and Renner (2018) rests on different assumptions that do not explicitly include locality. The precise interpretation of that result within nonlocal theories is under debate. It appears that abandoning free choice and locality might not fully resolve the contradiction in that framework either.

### 7.3 Possible Interpretations

If L and F are retained, then observer-independent facts must be abandoned. Compatible interpretations include:

- **Many-worlds interpretation (Everett):** Facts of the world can only be established by a privileged observer with access to the global wavefunction.
- **Bohmian mechanics:** Similar privileged global observer perspective.
- **Relational quantum mechanics (Rovelli):** Facts are only defined relative to observers; no absolute observer-independent facts exist.
- **QBism (Fuchs):** Quantum mechanics is a tool capturing an agent's subjective predictions of future measurement outcomes. Different observers may irreconcilably disagree about what happened in an experiment.

### 7.4 On the Status of Photonic Observers

Denying photonic memories the status of observer would require revising the minimal definition of observer, typically requiring new physics outside standard quantum theory. Wigner originally argued that consciousness prevents superposition, but the conflict revealed by a Bell-Wigner test does not arise in consciousness — it arises between recorded facts. Since quantum theory does not distinguish microscopic from macroscopic systems, the conclusions hold regardless of observer size or complexity.

Implementing the experiment with more complex (macroscopic) observers would not add new insight into observer independence, but would test whether quantum mechanics holds at larger scales, ruling out collapse models (e.g., GRW).

### 7.5 Open Question: Relativistic Extension

A further open question is whether the conclusions drawn from Bell or Bell-Wigner tests change under relativistic conditions with non-inertial observers.

---

## 8. Summary of Key Numerical Results

| Quantity | Value |
|---|---|
| S_exp (main protocol) | 2.416 +/- 0.075 |
| Violation significance | > 5 standard deviations |
| S_exp (alternative observables) | 2.407 +/- 0.073 |
| S_exp (alternative protocol) | 2.346 +/- 0.110 |
| Classical bound | S <= 2 |
| Total six-photon coincidences | 1794 |
| Total measurement time | 360 hours |
| Pump power | 100 mW |
| Photon wavelength | 1550 nm |
| Source fidelity (at source) | 99.62% |
| Bell-state measurement fidelity | 96.84% |
| Min. detection efficiency needed | eta > 0.875 |

---

## 9. References

1. K. Popper, Realism and the Aim of Science, Routledge (1992).
2. E. Wigner, Remarks on the mind-body problem, in The Scientist Speculates (1961), pp. 284-302.
3. C. Brukner, On the quantum measurement problem, arXiv:1507.05255 (2015).
4. C. Brukner, A no-go theorem for observer-independent facts, Entropy 20, 350 (2018).
5. D. Frauchiger, R. Renner, Quantum theory cannot consistently describe the use of itself, Nat. Commun. 9, 3711 (2018).
6. D. Deutsch, Quantum theory as a universal physical theory, Int. J. Theor. Phys. 24, 1-41 (1985).
7. R. Healey, Quantum theory and the limits of objectivity, Found. Phys. 48, 1568-1589 (2019).
8. V. Baumann, F. Del Santo, C. Brukner, Comment on Healey's "Quantum theory and the limits of objectivity", Found. Phys. 49, 741-749 (2019).
9. A. Fine, Hidden variables, joint probability, and the Bell inequalities, Phys. Rev. Lett. 48, 291-295 (1982).
10. J. Clauser, M. Horne, A. Shimony, R. Holt, Proposed experiment to test local hidden-variable theories, Phys. Rev. Lett. 23, 880-884 (1969).
11. J. S. Bell, A. Aspect, Speakable and Unspeakable in Quantum Mechanics, Cambridge Univ. Press (2004).
12. J. S. Bell, On the Einstein Podolsky Rosen paradox, Physics 1, 195-200 (1964).
13. V. Baumann, C. Brukner, Wigner's friend as a rational agent, arXiv:1901.11274 (2019).
14. F. Graffitti et al., Independent high-purity photons created in domain-engineered crystals, Optica 5, 514 (2018).
15. F. Graffitti et al., Design considerations for high-purity heralded single-photon sources, Phys. Rev. A 98, 053811 (2018).
16. R.-B. Jin et al., Pulsed Sagnac polarization-entangled photon source with a PPKTP crystal at telecom wavelength, Opt. Express 22, 11498 (2014).
17. D. E. Browne, T. Rudolph, Resource-efficient linear optical quantum computation, Phys. Rev. Lett. 95, 010501 (2005).
18. J.-W. Pan et al., Experimental demonstration of four-photon entanglement and high-fidelity teleportation, Phys. Rev. Lett. 86, 4435-4438 (2001).
19. J.-A. Larsson, Loopholes in Bell inequality tests of local realism, J. Phys. A 47, 424003 (2014).
20. G. C. Ghirardi, A. Rimini, T. Weber, Unified dynamics for microscopic and macroscopic systems, Phys. Rev. D 34, 470-491 (1986).
21. D. Lazarovici, M. Hubert, How quantum mechanics can consistently describe the use of itself, Sci. Rep. 9, 470 (2019).
22. H. I. Everett III, Relative state formulation of quantum mechanics, Rev. Mod. Phys. 29, 454-462 (1957).
23. D. Bohm, A suggested interpretation of the quantum theory in terms of hidden variables, Phys. Rev. 85, 166-179 (1952).
24. C. Rovelli, Relational quantum mechanics, Int. J. Theor. Phys. 35, 1637 (1996).
25. C. A. Fuchs, Notwithstanding Bohr, the reasons for QBism, Mind Matter 15, 245-300 (2017).
26. I. Durham, Observer-independence in the presence of a horizon, arXiv:1902.09028 (2019).
27. A. Fedrizzi et al., A wavelength-tunable fiber-coupled source of narrowband entangled photons, Opt. Express 15, 15377-15386 (2007).
28. M. A. Broome et al., Reducing multi-photon rates in pulsed down-conversion by temporal multiplexing, Opt. Express 19, 22698-22708 (2011).
29. J. Calsamiglia, N. Lutkenhaus, Maximum efficiency of a linear-optical Bell-state analyzer, Appl. Phys. B 72, 67-71 (2001).
30. S. L. Braunstein, A. Mann, Measurement of the Bell operator and quantum teleportation, Phys. Rev. A 51, R1727-R1730 (1995).
31. P. H. Eberhard, Background level and counter efficiencies required for a loophole-free EPR experiment, Phys. Rev. A 47, R747-R750 (1993).

---

*End of document. Synthesized from: aaw9832.pdf (main paper) and aaw9832_sm.pdf (supplementary materials), Science Advances 2019.*
