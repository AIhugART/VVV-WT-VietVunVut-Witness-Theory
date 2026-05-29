# Experimental Test of Local Observer Independence — Unified LLM-Friendly Document

## Source Documents

This document consolidates the following works into a single structured reference:

1. "Experimental test of local observer independence"
   Authors: Massimiliano Proietti et al.
   Published in Science Advances, 2019
   DOI: 10.1126/sciadv.aaw9832

2. Supplementary Materials for:
   "Experimental test of local observer independence"

The goal of this merged document is:
- Pure documentation
- English only
- LLM-friendly structure
- Reduced redundancy
- Clear separation between theory, experiment, assumptions, loopholes, and implications

---

# 1. Core Thesis

The paper experimentally tests whether "facts" observed by different observers can always be reconciled into a single observer-independent reality.

The experiment implements an extended version of the Wigner’s Friend thought experiment and demonstrates a violation of a Bell-type inequality.

Main conclusion:

If the assumptions of:
- locality,
- free choice,
- observer-independent facts

are all accepted simultaneously, then the observed experimental results are impossible.

Therefore, at least one of these assumptions must fail.

---

# 2. Conceptual Background

## 2.1 The Measurement Problem

Quantum mechanics contains two apparently incompatible descriptions:

1. Unitary evolution
   - Continuous
   - Deterministic
   - Governed by the Schrödinger equation

2. Measurement collapse
   - Discrete
   - Probabilistic
   - Produces definite outcomes

The theory does not clearly specify:
- when a physical interaction becomes a "measurement"
- where the boundary between quantum and classical reality exists

This is known as the quantum measurement problem.

---

## 2.2 Wigner’s Friend Scenario

### Setup

A photon is prepared in a superposition:

- horizontal polarization |h>
- vertical polarization |v>

Inside an isolated laboratory:
- Wigner’s friend measures the photon
- The friend records a definite outcome

Outside the laboratory:
- Wigner treats the entire laboratory quantum mechanically
- Wigner assigns a superposition state to:
  - photon
  - friend’s memory

Thus:

Friend perspective:
- definite outcome exists

Wigner perspective:
- friend + photon remain in superposition

This creates a tension between:
- subjective observation
- objective universal description

---

# 3. Observer-Independent Facts

The paper defines the assumption:

## O — Observer-Independent Facts

Any measurement result should correspond to a fact of the world that:
- exists objectively
- can be agreed upon by all observers
- remains well-defined even when not jointly measured

Additional assumptions:

## L — Locality

One observer’s measurement choice cannot instantaneously affect another distant observer’s outcome.

## F — Free Choice

Observers freely choose which measurements to perform.

---

# 4. Bell-Wigner Framework

The experiment extends Wigner’s Friend into a Bell-style scenario.

## Participants

There are four effective observers:

- Alice
- Bob
- Alice’s friend
- Bob’s friend

### Friends
The friends:
- measure photons locally
- record outcomes in memory systems

### Alice and Bob
Alice and Bob can choose between:

1. Reading their friend’s memory
2. Performing interference measurements on:
   - friend memory
   - measured photon jointly

This creates potentially incompatible "facts".

---

# 5. Bell-Wigner Inequality

The experiment tests the CHSH-style inequality:

S = <A1B1> + <A1B0> + <A0B1> - <A0B0>

Classical bound:

S <= 2

Quantum mechanics predicts violation.

Experimental result:

S_exp = 2.416 ± 0.075

Violation:
- more than 5 standard deviations

Interpretation:
- the assumptions O + L + F cannot all simultaneously hold.

---

# 6. Important Distinction From Standard Bell Tests

The paper emphasizes:

This is NOT merely a standard Bell inequality experiment.

Difference:

## Standard Bell Tests
Test:
- Locality
- Free choice
- Predetermined hidden variables

## Bell-Wigner Tests
Test:
- Locality
- Free choice
- Observer-independent facts

The critical difference:
- objectivity of observed facts is directly tested

---

# 7. Definition of Observer

The paper adopts a minimal physical definition.

An observer is any system that can:
1. Extract information from another system
2. Store that information in physical memory

This definition includes:
- humans
- computers
- detectors
- simple quantum systems

The experiment therefore treats photonic memory systems as observers.

---

# 8. Experimental Architecture

## 8.1 Photon Sources

The setup uses three entangled photon-pair sources:

- S0
- SA
- SB

Photon wavelength:
- 1550 nm

Technology:
- Sagnac interferometers
- ppKTP crystals
- Type-II parametric down-conversion

---

## 8.2 State Preparation

Initial entangled state:

|Ψ> = (|hv> - |vh>) / sqrt(2)

A unitary rotation is applied to optimize Bell-Wigner violation.

---

## 8.3 Friend Measurements

Alice’s friend and Bob’s friend use:

- Type-I fusion gates
- Ancillary entangled photons

Purpose:
- nondestructive measurement
- memory encoding

The memory state stores:

- "photon is h"
- "photon is v"

The memory itself is encoded into photon polarization states.

---

## 8.4 Alice and Bob Measurements

Alice and Bob measure either:

### A0 / B0
Directly read friend memory.

### A1 / B1
Perform Bell-state interference measurements on:
- photon
- friend memory jointly

These correspond to Wigner-style measurements.

---

# 9. Observables

Main observables:

## Friend Facts
A0, B0

Measure:
- stored records in friend memories

## Wigner Facts
A1, B1

Measure:
- interference-compatible entangled states

These are incompatible descriptions of reality.

---

# 10. Experimental Data

## Statistics

- 64 measurement settings
- 1794 six-photon coincidence events
- total runtime: 360 hours

## Main Result

Measured Bell-Wigner parameter:

S_exp = 2.416 ± 0.075

This exceeds the classical limit of 2.

---

# 11. Technical Performance

## Entangled State Quality

Typical values:

### Fidelity
~99.6%

### Purity
~99.3%

### Concurrence
~99.4%

These indicate near-ideal entangled states.

---

# 12. Error Sources

Primary limitations:

## Higher-Order Photon Emissions

Probabilistic photon sources can emit:
- unwanted extra photon pairs

These contribute noise.

---

## Detection Efficiency

Detector inefficiency limits:
- coincidence counts
- loophole closure

---

## Optical Loss

Losses reduce:
- observed violation strength
- measurement reliability

---

# 13. Error Analysis

Photon counts follow Poisson statistics.

Two uncertainty estimation methods were used:

1. Error propagation
2. Monte Carlo simulation

The two methods agreed closely.

---

# 14. Supplementary Material — Key Additions

The supplementary document expands several important points.

---

# 15. Loopholes

The experiment inherits loopholes similar to standard Bell tests.

## 15.1 Detection Loophole

Not all photons are detected.

Potential issue:
- sampled events may not represent all events.

Assumption used:
- fair sampling

---

## 15.2 Locality Loophole

Measurement choices and outcomes are not fully space-like separated.

Future experiments would require:
- stricter spacetime arrangement
- event-ready configuration

---

## 15.3 Freedom-of-Choice Loophole

Measurement settings must be chosen independently from hidden variables.

Not fully closed experimentally.

---

## 15.4 Bell-Wigner Specific Loophole

A unique loophole exists:

Do A0 and B0 truly measure only:
- friend memory
and not:
- joint photon-memory systems?

The authors acknowledge this as a future challenge.

---

# 16. Detection Efficiency Threshold

The supplementary analysis derives a required detector efficiency.

For loophole-free violation:

η > 0.875

Comparison:

Standard CHSH Bell tests require only:

η > 0.828

Thus Bell-Wigner tests are experimentally harder.

---

# 17. Alternative Observables

The supplement explores an alternative definition of:

- A0
- B0

This version:
- measures both photon and memory consistency

Experimental result:

S_exp = 2.407 ± 0.073

Still violates the inequality by:
- more than 5 standard deviations

---

# 18. Alternative Measurement Protocol

Another protocol was implemented using:
- linear polarizers
instead of:
- removing beam splitters

Result:

S_exp = 2.346 ± 0.110

Violation remained:
- more than 3 standard deviations

---

# 19. Philosophical Consequences

The paper discusses several interpretational responses.

---

## 19.1 Many-Worlds Interpretation

Possible resolution:
- a privileged global wavefunction exists
- all branches coexist

---

## 19.2 Bohmian Mechanics

Possible resolution:
- hidden-variable framework
- observer-independent global reality retained

---

## 19.3 Relational Quantum Mechanics

Possible resolution:
- facts exist only relative to observers

Different observers may legitimately disagree.

---

## 19.4 QBism

Possible resolution:
- quantum states are subjective beliefs
- measurement outcomes are personal experiences

---

# 20. Central Implication

The experiment suggests:

Observer-independent reality may not be universally maintainable within quantum mechanics.

Different observers may possess:
- incompatible
- irreconcilable
yet internally consistent descriptions of reality.

---

# 21. What The Experiment Does NOT Prove

The paper does NOT prove:
- consciousness creates reality
- humans are special observers
- quantum mysticism
- simulation theory

The experiment only shows:
- specific assumptions about observer-independent facts conflict with quantum predictions.

---

# 22. Why This Result Matters

This experiment is historically important because it transforms:

"Wigner’s Friend"
from:
- philosophical thought experiment

into:
- experimentally testable physics

It directly connects:
- quantum foundations
- measurement theory
- objectivity
- observer relations
- Bell inequalities

into one operational framework.

---

# 23. Practical Experimental Stack

## Hardware

- Ti:sapphire laser
- ppKTP crystals
- SNSPD detectors
- Beam splitters
- Polarizing beam splitters
- Wave plates
- Fiber optics
- Temporal multiplexing

---

## Quantum Operations

- entangled photon generation
- Bell-state measurement
- fusion gates
- nondestructive measurement
- quantum memory encoding

---

# 24. Experimental Assumptions

The interpretation relies on:

1. Quantum mechanics is universally valid
2. Photonic memories qualify as observers
3. Measurement observables correctly represent friend memories
4. Fair sampling assumption
5. Locality assumption
6. Free choice assumption

---

# 25. Final Logical Structure

The experiment establishes:

If:
- quantum predictions are correct

and if:
- locality holds
- free choice holds

then:
- observer-independent facts cannot universally exist.

Equivalent statement:

At least one of:
- locality
- free choice
- observer-independent reality

must fail.

---

# 26. Most Important Conceptual Insight

The deepest implication is not merely:

"quantum systems are probabilistic"

but rather:

Different observers may fundamentally disagree about what physically happened, and quantum mechanics may allow all such descriptions to remain internally valid simultaneously.

---

# 27. Condensed Executive Summary

## Problem
Can all observers agree on objective facts?

## Method
Implement a Bell-style Wigner’s Friend experiment using entangled photons and photonic memories.

## Result
Bell-Wigner inequality violated:
S_exp = 2.416 ± 0.075

## Implication
Observer-independent facts are incompatible with:
- locality
- free choice
- quantum predictions

## Consequence
Quantum reality may fundamentally depend on the observer framework.

---

# 28. Keywords

- Wigner’s Friend
- Bell-Wigner test
- Observer independence
- Quantum foundations
- Measurement problem
- Bell inequality
- CHSH inequality
- Relational quantum mechanics
- QBism
- Many Worlds
- Bohmian mechanics
- Quantum measurement
- Observer-relative facts
- Quantum objectivity
- Entanglement
- Fusion gates
- Bell-state measurement
- Quantum memory

---

# 29. Citation

Massimiliano Proietti et al.
"Experimental test of local observer independence"
Science Advances 5, eaaw9832 (2019)
DOI: 10.1126/sciadv.aaw9832
