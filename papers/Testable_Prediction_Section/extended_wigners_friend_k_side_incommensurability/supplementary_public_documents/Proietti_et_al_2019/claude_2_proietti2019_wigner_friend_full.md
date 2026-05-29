# Experimental Test of Local Observer Independence

**Authors:** Massimiliano Proietti, Alexander Pickston, Francesco Graffitti, Peter Barrow, Dmytro Kundys, Cyril Branciard, Martin Ringbauer, Alessandro Fedrizzi

**Published:** Science Advances, Vol. 5, eaaw9832, 20 September 2019
**DOI:** 10.1126/sciadv.aaw9832
**License:** CC BY 4.0

---

## Abstract

The scientific method relies on facts established through repeated measurements and agreed upon universally, independently of who observed them. In quantum mechanics, the objectivity of observations is not clear — most markedly exposed in Wigner's eponymous thought experiment, where two observers can experience seemingly different realities. This paper reports an experimental test of an extended Wigner's friend scenario using four observers in a six-photon optical experiment. The associated Bell-type inequality is violated by five standard deviations. Under the assumptions of locality and free choice, this result implies that quantum theory must be interpreted in an observer-dependent way.

---

## 1. Background and Motivation

### 1.1 The Measurement Problem

Quantum theory describes all physical processes as continuous and deterministic — except for observations, which are instantaneous and probabilistic. This creates a fundamental conflict known as the **measurement problem**: the theory does not specify a precise boundary between a unitary physical interaction and a measurement.

### 1.2 The Original Wigner's Friend Scenario

Consider a photon in equal superposition of horizontal |h⟩ and vertical |v⟩ polarization, measured by Wigner's Friend in an isolated laboratory.

**From the Friend's perspective:** She randomly observes one definite outcome (h or v) in every run. This constitutes a fact recorded in her physical memory.

**From Wigner's perspective (outside):** He must describe the joint photon-friend system as evolving unitarily into the entangled state:

```
(1/√2)(|h⟩ ± |v⟩) → (1/√2)(|h⟩|"photon is h"⟩ ± |v⟩|"photon is v"⟩) =: |F±_photon/record⟩
```

Wigner can perform an interference experiment to verify this entangled superposition — concluding that his friend cannot have recorded a definite outcome. Yet the friend always does record a definite outcome. The friend can even communicate that she recorded *a* definite outcome (without revealing which), and both descriptions remain unchanged. This raises the question: can their two accounts be reconciled?

---

## 2. Theoretical Framework

### 2.1 The Extended Wigner's Friend Scenario

The paper tests a no-go theorem (Brukner 2018) built on an extended scenario with **four observers**:

- **Alice's Friend** and **Bob's Friend** each measure one photon from an entangled pair inside their respective isolated laboratories.
- **Alice** and **Bob** each operate from outside those laboratories and can choose one of two measurement types per run.

**Measurement choices:**
- `x=0` (or `y=0`): Alice (Bob) measures the state of their friend's memory record, defining random variables A0 (B0).
- `x=1` (or `y=1`): Alice (Bob) jointly measures the friend's photon and record together, defining variables A1 (B1).

After many runs, Alice and Bob estimate the joint probability distributions P(Ax, By) for all four combinations x, y ∈ {0, 1}.

### 2.2 Key Assumptions

The no-go theorem rests on three jointly incompatible assumptions:

**O — Observer-Independent Facts:** Information obtained from a measurement is a fact of the world that all observers agree on. Such facts take definite values even when not all are co-measured.

**L — Locality:** Alice's and Bob's measurement choices do not influence each other's outcomes.

**F — Free Choice:** Alice and Bob can freely and independently choose their measurements.

Under O, L, and F, it must be possible to construct a single joint probability distribution P(A0, A1, B0, B1) whose marginals match the observed P(Ax, By).

### 2.3 The Bell-Wigner Inequality

Any joint distribution satisfying O, L, and F must satisfy the Clauser-Horne-Shimony-Holt (CHSH) inequality:

```
S = ⟨A1B1⟩ + ⟨A1B0⟩ + ⟨A0B1⟩ − ⟨A0B0⟩ ≤ 2
```

where Ax, By ∈ {−1, +1} and ⟨AxBy⟩ = Σ_{a,b} ab · P(Ax=a, By=b).

Quantum theory predicts this inequality can be violated. A violation implies the observed probabilities are incompatible with O, L, and F together. Accepting L and F, it follows that the facts established by the four observers cannot coexist within a single observer-independent framework.

### 2.4 Distinction from Standard Bell Tests

Although Bell's mathematical machinery is reused, this is a conceptually different test:

| Feature | Standard Bell Test | Bell-Wigner Test |
|---|---|---|
| Shared assumptions | L, F | L, F |
| Third assumption | Predetermination (PD): outcomes are deterministic or not | Observer-Independence (O): outcomes are objective facts |
| What a violation rules out | L ∧ F ∧ PD | L ∧ F ∧ O |
| Observables required | Any | Must represent observations/facts by specific observers |
| Implication direction | Violation ⟹ ¬(L ∧ F ∧ PD) | Violation ⟹ ¬(L ∧ F ∧ O); any Bell-Wigner violation also implies a Bell violation, but not vice versa |

### 2.5 Definition of Observer

An **observer** is any physical system that can extract information from another system via some interaction and store that information in a physical memory. This definition:
- Does not require consciousness or large size
- Covers humans, computers, measurement devices, and simple quantum systems
- Is consistent with quantum theory's universality (no distinction between microscopic and macroscopic systems)

---

## 3. Experimental Implementation

### 3.1 Overview

The experiment uses **six photons** produced by three entangled photon-pair sources. Alice's Friend and Bob's Friend are physically realized by quantum optical measurement devices (fusion gates + ancilla photons). Alice and Bob perform joint measurements on the combined photon-and-memory systems.

### 3.2 Photon Sources

Three Sagnac-type interferometer sources (S0, SA, SB) produce pairs of 1550-nm photons entangled in polarization:

```
|Ψ⁻⟩ = (|h⟩|v⟩ − |v⟩|h⟩) / √2
```

**Source quality (measured via quantum state tomography):**
- Fidelity: F = 99.62 +0.01/−0.04 %
- Purity: P = 99.34 +0.01/−0.09 %
- Concurrence: C = 99.38 +0.02/−0.10 %

After propagation through the optical circuit, fidelities settle at:
- F0 = 98.79 ± 0.03% (S0)
- FA = 98.70 ± 0.03% (SA)
- FB = 98.59 ± 0.03% (SB)

**Laser system:**
- 775-nm, 1.6-ps pulsed Ti:sapphire laser, 80 MHz repetition rate
- Rate quadrupled via temporal multiplexing to suppress higher-order emissions
- Signal-to-noise ratio: 140 ± 10 (photon pairs vs. higher-order contributions)
- Generation rate: ~8000 photon pairs mW⁻¹s⁻¹
- Heralding efficiency: ~50%
- Detection: Superconducting nanowire single-photon detectors (SNSPDs), ~80% efficiency
- Coincidence window: 1 ns

### 3.3 State Preparation

The photon pair from S0 is rotated by a half-wave plate (HWP) at angle 7π/16:

```
|Ψ̃⟩ = (1 ⊗ U_{7π/16}) |Ψ⁻⟩
```

where U_{7π/16} = cos(7π/8)σz + sin(7π/8)σx. This state maximizes the violation of the Bell-Wigner inequality for the chosen measurement settings.

Expanded in the polarization basis:

```
|Ψ̃⟩_ab = (1/√2) cos(π/8)(|h⟩_a|v⟩_b + |v⟩_a|h⟩_b)
         + (1/√2) sin(π/8)(|h⟩_a|h⟩_b − |v⟩_a|v⟩_b)
```

### 3.4 Implementing the Friends as Physical Observers

Alice's Friend and Bob's Friend are implemented via **type-I fusion gates** using ancilla entangled pairs from SA and SB.

**Fusion gate mechanics:**

A polarizing beam splitter (PBS) with a quarter-wave plate (QWP) at π/4 and an HWP at π/8 implements:

```
|h⟩|h⟩ →^{PBS} |h⟩|h⟩ →^{Q/HWP} |h⟩ ⊗ (|h⟩ + i|v⟩)/√2
|v⟩|v⟩ →^{PBS} |v⟩|v⟩ →^{Q/HWP} |v⟩ ⊗ (|h⟩ − i|v⟩)/√2
```

The heralding photon is projected onto |h⟩ by another PBS. The net operation is:

```
FG_I = (1/√2)( −i|h⟩⟨h|⊗⟨h| − |v⟩⟨v|⊗⟨h| )
```

with success probability 1/2.

**Nondestructive polarization measurement of photon a:**

Using ancilla pair |Ψ⁻⟩_{a'a} from SA:

```
|h⟩_a |Ψ⁻⟩_{a'a} →^{FG_I} (1/2)|h⟩_a |v⟩_ᾱ
|v⟩_a |Ψ⁻⟩_{a'a} →^{FG_I} (1/2)|v⟩_a |h⟩_ᾱ
```

The state of the incoming photon is copied (with a h↔v flip) into the memory photon ᾱ. The encoding is:

```
|"photon is h"⟩_ᾱ = |v⟩_ᾱ
|"photon is v"⟩_ᾱ = |h⟩_ᾱ
```

Total success probability per friend: 1/4. Combined success probability for both friends: 1/16.

### 3.5 The Four-Photon Entangled State

After both fusion gates succeed, Alice and Bob share the four-photon state:

```
|Ψ̃'⟩_{aᾱbβ} = (1/√2) cos(π/8)(|hv⟩_{aᾱ}|vh⟩_{bβ} + |vh⟩_{aᾱ}|hv⟩_{bβ})
              + (1/√2) sin(π/8)(|hv⟩_{aᾱ}|hv⟩_{bβ} − |vh⟩_{aᾱ}|vh⟩_{bβ})
```

where photon a (b) carries the original S0 photon, and ᾱ (β) carries the friend's memory.

### 3.6 Measurement Settings

**Observables A0, B0 (reading friend's record):**

```
A0 = B0 = 1 ⊗ (|v⟩⟨v| − |h⟩⟨h|)
```

Implemented by direct polarization measurement on the memory photon (no beam splitter). Projects onto:
- |hv⟩_{aᾱ} and |vv⟩_{aᾱ} → eigenvalue +1
- |hh⟩_{aᾱ} and |vh⟩_{aᾱ} → eigenvalue −1

**Observables A1, B1 (Wigner-type joint measurement):**

```
A1 = B1 = |Ψ+⟩⟨Ψ+| − |Ψ−⟩⟨Ψ−|
```

where |Ψ±⟩ = (|hv⟩ ± |vh⟩)/√2.

Implemented via nonclassical interference on a 50/50 beam splitter (BS) followed by polarization projection. |Ψ+⟩ → eigenvalue +1; |Ψ−⟩ → eigenvalue −1; |Φ±⟩ → eigenvalue 0.

Bell-state measurement fidelity: F_BSM = 96.84 +0.05/−0.05 %.

### 3.7 Data Collection

- 64 total measurement settings (4 × 4 eigenstates for each of 4 observable pairs)
- 1794 six-photon coincidence events collected
- Total measurement time: 360 hours
- Pump power: 100 mW (kept low to suppress higher-order photon emissions)

---

## 4. Results

### 4.1 Measured Expectation Values

| Observable pair | Measured value |
|---|---|
| ⟨A0B0⟩ | −0.678 +0.033/−0.033 |
| ⟨A0B1⟩ | +0.570 +0.040/−0.040 |
| ⟨A1B0⟩ | +0.595 +0.041/−0.041 |
| ⟨A1B1⟩ | +0.571 +0.034/−0.034 |

### 4.2 Bell-Wigner Parameter

```
S_exp = ⟨A1B1⟩ + ⟨A1B0⟩ + ⟨A0B1⟩ − ⟨A0B0⟩
      = 2.416 +0.075/−0.075
```

Classical (observer-independent) bound: S ≤ 2

**Violation: 5+ standard deviations above the bound.**

### 4.3 Error Analysis

Each expectation value ⟨AxBy⟩ = f(n1, …, n16) is computed from 16 six-photon coincidence counts ni following Poisson statistics (σ²_ni = ni). Uncertainty propagation:

```
σ²_f = Σ_{i=1}^{16} (∂f/∂ni)² · σ²_ni
```

The four expectation values are statistically independent, so uncertainties combine independently. A Monte Carlo method (100,000 samples) was also used to account for asymmetric errors; both methods agree to within 0.0032.

**Primary limitation:** Higher-order photon pair emissions from probabilistic sources. These are suppressed by:
1. Six-fold coincidence detection (filters out three-pair emissions where three pairs come from any single source)
2. Cross-polarization design (excludes three-pair contributions from S0)
3. Low pump power (100 mW) to suppress four-or-more pair emissions

---

## 5. Discussion

### 5.1 Loopholes

Bell-Wigner tests share the loopholes of conventional Bell tests:

**Detection loophole:** Only a fraction of photons are detected. Addressed by assuming fair sampling. In the event-ready configuration, the limited fusion gate success probability does not introduce a detection loophole for heralded events — but ancilla detectors would need to be photon-number-resolving in a fully loophole-free test.

**Locality loophole:** Alice and Bob's settings could in principle influence each other. Addressed empirically by verifying no signaling between measurement devices (consistent with Poissonian statistics).

**Space-time loophole:** In a fully loophole-free version, heralding events must be space-like separated from Alice and Bob's setting choices, and each party's choice must be space-like separated from the other's outcome.

**Observer definition loophole:** One might deny photonic memories the status of "observers." This would require new physics beyond standard quantum mechanics (e.g., consciousness-based collapse as Wigner originally suggested). The paper argues: quantum theory makes no distinction between microscopic and macroscopic information storage, so the conflict between records persists regardless of the observer's size or complexity.

**Bell-Wigner-specific loophole:** The observables A0, B0 must genuinely measure the friends' memory records. A fully rigorous test requires measurement devices that cleanly separate the system photon from the memory photon and measure only the latter.

### 5.2 Required Detection Efficiency for Loophole-Free Test

Assuming symmetric detection efficiency η per photon and a fixed-outcome strategy when a detector fails:

- Expected values under inefficiency:
  - ⟨A0B0⟩ = η²(−1/√2) + (1−η)²
  - ⟨A0B1⟩ = ⟨A1B0⟩ = η³(1/√2) + (1−η)(1−η²)
  - ⟨A1B1⟩ = η⁴(1/√2) + (1−η²)²

- Minimum required efficiency to violate inequality (2):

```
η > √(2/(3(1 − 1/√2))) − 1 ≈ 0.875
```

This is stricter than the standard CHSH requirement of η > 2√2 − 2 ≈ 0.828.

### 5.3 Interpretive Implications

The violation of S ≤ 2 (given L and F) implies assumption O must be abandoned. At least one of the following must hold:

1. **Reject Locality (L):** Facts are non-local. Some nonlocal theories (e.g., Bohmian mechanics) may accommodate the result, though the Frauchiger-Renner theorem suggests abandoning locality alone may not suffice.

2. **Reject Free Choice (F):** Measurement settings are not independent. This is a radical position typically associated with superdeterminism.

3. **Reject Observer Independence (O):** Facts of the world depend on the observer. This is the most natural reading. Compatible interpretations include:
   - **Many-Worlds / Everett:** A privileged observer with access to the global wavefunction can define objective facts; local observers cannot.
   - **Bohmian Mechanics:** Hidden variables are globally defined; local facts are contextual.
   - **Relational Quantum Mechanics (Rovelli):** Physical quantities are only defined relative to observers; no observer-independent facts exist.
   - **QBism:** Quantum mechanics is a tool for an agent's subjective predictions of future measurement outcomes; different agents may irreconcilably disagree about outcomes.

All observer-relative interpretations require accepting that different observers can irreconcilably disagree about what happened in an experiment.

---

## 6. Supplementary Material

### 6.1 Alternative Observables A0, B0

The original no-go theorem (Brukner 2018) used a slightly different definition:

```
A0 = B0 = |h⟩⟨h| ⊗ |"photon is h"⟩⟨"photon is h"|
         − |v⟩⟨v| ⊗ |"photon is v"⟩⟨"photon is v"|   [Eq. S1]
```

This definition also measures the original photon as a consistency check. If the photon state is inconsistent with the friend's record, the result is assigned 0.

**Results with alternative observables (from Fig. S2 data):**

| Observable pair | Value |
|---|---|
| ⟨A0B0⟩ | 0.662 +0.033/−0.033 |
| ⟨A0B1⟩ | 0.573 +0.039/−0.039 |
| ⟨A1B0⟩ | 0.600 +0.040/−0.040 |
| ⟨A1B1⟩ | 0.571 +0.034/−0.034 (unchanged) |
| **S_exp** | **2.407 +0.073/−0.073** |

Violation: more than 5 standard deviations.

### 6.2 Alternative Measurement Protocol for A0, B0

Instead of removing the beam splitter (which risks disturbing optical alignment), linear polarizers can be inserted in modes a(b) and ᾱ(β) before the BS. This prevents interference and effectively measures photons before the BS.

**Trade-off:** Reduces success probability of A0/B0 measurement by factor 1/4, increasing statistical uncertainty.

**Results:**

| Observable pair | Value |
|---|---|
| ⟨A0B0⟩ | −0.609 +0.048/−0.048 |
| ⟨A0B1⟩ | 0.577 +0.049/−0.049 |
| ⟨A1B0⟩ | 0.588 +0.049/−0.049 |
| ⟨A1B1⟩ | 0.571 +0.034/−0.034 (unchanged) |
| **S_exp** | **2.346 +0.110/−0.110** |

Violation: more than 3 standard deviations. (Reduced due to ~4.83 ± 0.97% photon loss from polarizers, which lowers counts in A0/B0 settings relative to normalization.)

### 6.3 Experimental Setup Summary

**Laser and pump:**
- Ti:sapphire laser, 775 nm, 1.6-ps pulses, 80 MHz rep. rate
- Temporal multiplexing ×4 to quadruple effective pulse rate
- Protected by Faraday isolator; spatially filtered by single-mode fiber

**Photon pair generation:**
- Three Sagnac interferometers, each with a 22-mm ppKTP crystal
- Type-II collinear parametric down-conversion → 1550-nm polarization-entangled pairs
- Outputs coupled to single-mode fibers; polarization controllers maintain state during transport

**Fusion gates:**
- Temporal mode matching via physical delays
- One photon per gate acts as herald (success signal); other continues to measurement stage

**Detection:**
- SNSPDs, ~80% detection efficiency
- 3-nm bandpass filters for spectral purity
- Time-tagging via FPGA; 6-photon coincidences within 1-ns window

---

## 7. Key Equations Reference

| Equation | Description |
|---|---|
| `\|F±_{ph/rec}⟩ = (1/√2)(\|h⟩\|"h"⟩ ± \|v⟩\|"v"⟩)` | Friend's entangled state (Wigner's description) |
| `S = ⟨A1B1⟩ + ⟨A1B0⟩ + ⟨A0B1⟩ − ⟨A0B0⟩ ≤ 2` | Bell-Wigner (CHSH) inequality |
| `\|Ψ̃⟩ = (1⊗U_{7π/16})\|Ψ⁻⟩` | Input state from S0 |
| `FG_I = (1/√2)(−i\|h⟩⟨h\|⊗⟨h\| − \|v⟩⟨v\|⊗⟨h\|)` | Type-I fusion gate operation |
| `\|Ψ̃'⟩_{aᾱbβ}` | Four-photon state shared by Alice and Bob (Eq. 11) |
| `A0 = B0 = 1 ⊗ (\|v⟩⟨v\| − \|h⟩⟨h\|)` | Friend's record observable |
| `A1 = B1 = \|Ψ+⟩⟨Ψ+\| − \|Ψ−⟩⟨Ψ−\|` | Wigner-type joint observable |
| `S_exp = 2.416 ± 0.075` | Measured Bell-Wigner parameter |

---

## 8. References

1. K. Popper, *Realism and the Aim of Science* (Routledge, 1992).
2. E. Wigner, "Remarks on the mind-body problem," in *The Scientist Speculates*, I. G. Good, Ed. (Heinemann, 1961), pp. 284–302.
3. Č. Brukner, "On the quantum measurement problem," arXiv:1507.05255 [quant-ph] (2015).
4. Č. Brukner, "A no-go theorem for observer-independent facts," *Entropy* 20, 350 (2018).
5. D. Frauchiger, R. Renner, "Quantum theory cannot consistently describe the use of itself," *Nat. Commun.* 9, 3711 (2018).
6. D. Deutsch, "Quantum theory as a universal physical theory," *Int. J. Theor. Phys.* 24, 1–41 (1985).
7. R. Healey, "Quantum theory and the limits of objectivity," *Found. Phys.* 48, 1568–1589 (2019).
8. V. Baumann, F. Del Santo, Č. Brukner, "Comment on Healey's 'Quantum theory and the limits of objectivity'," *Found. Phys.* 49, 741–749 (2019).
9. A. Fine, "Hidden variables, joint probability, and the Bell inequalities," *Phys. Rev. Lett.* 48, 291–295 (1982).
10. J. Clauser, M. Horne, A. Shimony, R. Holt, "Proposed experiment to test local hidden-variable theories," *Phys. Rev. Lett.* 23, 880–884 (1969).
11. J. S. Bell, A. Aspect, *Speakable and Unspeakable in Quantum Mechanics*, 2nd ed. (Cambridge Univ. Press, 2004).
12. J. S. Bell, "On the Einstein Podolsky Rosen paradox," *Phys. Ther.* 1, 195–200 (1964).
13. V. Baumann, Č. Brukner, "Wigner's friend as a rational agent," arXiv:1901.11274 (2019).
14. F. Graffitti et al., "Independent high-purity photons created in domain-engineered crystals," *Optica* 5, 514 (2018).
15. F. Graffitti et al., "Design considerations for high-purity heralded single-photon sources," *Phys. Rev. A* 98, 053811 (2018).
16. R.-B. Jin et al., "Pulsed Sagnac polarization-entangled photon source with a PPKTP crystal at telecom wavelength," *Opt. Express* 22, 11498 (2014).
17. D. E. Browne, T. Rudolph, "Resource-efficient linear optical quantum computation," *Phys. Rev. Lett.* 95, 010501 (2005).
18. J.-W. Pan et al., "Experimental demonstration of four-photon entanglement and high-fidelity teleportation," *Phys. Rev. Lett.* 86, 4435–4438 (2001).
19. J.-Å. Larsson, "Loopholes in Bell inequality tests of local realism," *J. Phys. A Math. Theor.* 47, 424003 (2014).
20. G. C. Ghirardi, A. Rimini, T. Weber, "Unified dynamics for microscopic and macroscopic systems," *Phys. Rev. D* 34, 470–491 (1986).
21. D. Lazarovici, M. Hubert, "How quantum mechanics can consistently describe the use of itself," *Sci. Rep.* 9, 470 (2019).
22. H. I. Everett III, "'Relative state' formulation of quantum mechanics," *Rev. Mod. Phys.* 29, 454–462 (1957).
23. D. Bohm, "A suggested interpretation of the quantum theory in terms of 'hidden' variables. I," *Phys. Rev.* 85, 166–179 (1952).
24. C. Rovelli, "Relational quantum mechanics," *Int. J. Theor. Phys.* 35, 1637 (1996).
25. C. A. Fuchs, "Notwithstanding Bohr, the reasons for QBism," *Mind Matter* 15, 245–300 (2017).
26. I. Durham, "Observer-independence in the presence of a horizon," arXiv:1902.09028 (2019).
27. A. Fedrizzi et al., "A wavelength-tunable fiber-coupled source of narrowband entangled photons," *Opt. Express* 15, 15377–15386 (2007).
28. M. A. Broome et al., "Reducing multi-photon rates in pulsed down-conversion by temporal multiplexing," *Opt. Express* 19, 22698–22708 (2011).
29. J. Calsamiglia, N. Lütkenhaus, "Maximum efficiency of a linear-optical Bell-state analyzer," *Appl. Phys. B* 72, 67–71 (2001).
30. S. L. Braunstein, A. Mann, "Measurement of the Bell operator and quantum teleportation," *Phys. Rev. A* 51, R1727–R1730 (1995).
31. P. H. Eberhard, "Background level and counter efficiencies required for a loophole-free Einstein-Podolsky-Rosen experiment," *Phys. Rev. A* 47, R747–R750 (1993).
