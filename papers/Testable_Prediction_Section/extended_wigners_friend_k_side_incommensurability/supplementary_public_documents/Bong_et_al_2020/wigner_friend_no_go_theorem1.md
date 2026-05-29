# A Strong No-Go Theorem on the Wigner's Friend Paradox

**Authors:** Kok-Wei Bong, Aníbal Utreras-Alarcón, Farzad Ghafari, Yeong-Cherng Liang, Nora Tischler, Eric G. Cavalcanti, Geoff J. Pryde, Howard M. Wiseman

**Affiliation:** Griffith University (Brisbane & Gold Coast), National Cheng Kung University (Taiwan)

**arXiv:** 1907.05607v4 [quant-ph], 15 Mar 2023

---

## Abstract

This paper addresses whether quantum theory applies at all scales, including to observers themselves. Building on the Extended Wigner's Friend Scenario (EWFS) introduced by Brukner, the authors prove:

> If quantum evolution is controllable on the scale of an observer, then at least one of the following must be false:
> 1. No-Superdeterminism
> 2. Locality
> 3. Absoluteness of Observed Events (AOE)

New theory-independent inequalities (LF inequalities) are derived that are violated by quantum correlations. These are demonstrated in a proof-of-principle photonic experiment.

---

## 1. Background: The Measurement Problem

### Wigner's Friend Thought Experiment

- A "friend" performs a measurement on a quantum system inside an isolated lab.
- The friend observes a definite outcome and updates the state accordingly.
- "Wigner" (a superobserver) describes the entire lab — including the friend — as a unitarily evolving quantum state.
- When the system is in superposition, Wigner's description and the friend's description appear contradictory.

This contradiction is the **measurement problem**: reconciling unitary (deterministic) evolution of isolated systems with the nonunitary (probabilistic) state update after measurement.

### Why Decoherence Is Not Enough

Decoherence suppresses quantum effects at macroscopic scales but does not resolve the measurement problem: it still leaves a multitude of quasiclassical wave function components without explaining why single outcomes are perceived.

### Proposed Resolutions (and Their Radical Implications)

- Reject observer-independent measurement outcomes: many-worlds, relational QM, QBism
- Postulate faster-than-light or retrocausal hidden-variable effects: Bohmian mechanics, retrocausality
- Modify quantum dynamics: objective collapse models, gravity-induced collapse

---

## 2. Prior Work: Brukner's Scenario

Brukner introduced an Extended Wigner's Friend Scenario (EWFS) with:
- Two spatially separated labs, each with a friend (Charlie, Debbie)
- Two superobservers (Alice, Bob)
- Each friend measures half of an entangled pair

Brukner's three assumptions:
1. Freedom of choice
2. Locality (parameter independence)
3. Observer-Independent Facts (OIF) — equivalent to Kochen-Specker Noncontextuality (KSNC)

From these, Brukner derived a Bell inequality violable by quantum mechanics.

**Limitation of Brukner's approach:** OIF/KSNC involves counterfactual reasoning about unperformed measurements. The Kochen-Specker theorem already contradicts KSNC + freedom of choice without needing the friends' observations at all. This weakens the implications about observer objectivity.

---

## 3. This Paper's Contribution: Local Friendliness (LF)

### Three Assumptions

**Assumption 1 — Absoluteness of Observed Events (AOE):**
An observed event is a real single event, not relative to anything or anyone.

- In EWFS: there exists a joint probability distribution P(abcd|xy) such that:
  - (i) Marginalizing over c,d recovers the empirical probabilities: `℘(ab|xy) = Σ_{c,d} P(abcd|xy)`
  - (ii) When x=1, Alice's outcome equals Charlie's: `P(a|cd, x=1, y) = δ_{a,c}`
  - (iii) When y=1, Bob's outcome equals Debbie's: `P(b|cd, x, y=1) = δ_{b,d}`
- AOE does NOT assume truth values for unperformed measurements (respects Peres: "unperformed experiments have no results").

**Assumption 2 — No-Superdeterminism (NSD):**
Any set of events on a space-like hypersurface is uncorrelated with freely chosen actions subsequent to that hypersurface.

- In EWFS: `P(cd|xy) = P(cd)` — friends' outcomes are independent of superobservers' settings.

**Assumption 3 — Locality (L):**
The probability of an observable event is unchanged by conditioning on a space-like-separated free choice, even when conditioned on other events outside the future light-cone.

- In EWFS:
  - `P(a|cdxy) = P(a|cdx)` — Alice's outcome is independent of Bob's setting y
  - `P(b|cdxy) = P(b|cdy)` — Bob's outcome is independent of Alice's setting x

The conjunction of AOE + NSD + L is called **Local Friendliness (LF)**.

### Theorem 1

> If a superobserver can perform arbitrary quantum operations on an observer and its environment, then no physical theory can satisfy Local Friendliness.

- Theory-independent: conclusions hold for any theory that correctly predicts correlations between superobservers' outcomes.
- All three LF assumptions are essential (unlike Brukner's theorem).

---

## 4. LF vs LHV Correlations

### Key Properties of LF Correlations

| Property | Description |
|---|---|
| LF ⊇ LHV | LF correlations are a superset of Local Hidden Variable (LHV) correlations |
| Finite characterization | LF correlations can always be bounded by a finite set of inequalities |
| N=2: LF = LHV | For 2 measurement settings per party, LF and LHV give identical constraints |
| N=3, O=2: LF ⊋ LHV | For 3 binary-outcome settings, LF is strictly larger than LHV |

### Why LF Is Strictly Weaker Than Bell Assumptions

Bell's theorem requires AOE + NSD + L + **Outcome Independence**:
- Outcome independence: `P(a|bxyλ) = P(a|xyλ)` and `P(b|axyλ) = P(b|xyλ)`

LF does not require outcome independence. Therefore:
- Violation of LF inequalities → stronger conclusions than violation of Bell inequalities
- A quantum state can violate a Bell inequality while satisfying all LF inequalities (demonstrated experimentally at μ = 0.80, 0.81)

### The General LF Model Structure

From AOE + NSD + Locality, the empirical probabilities satisfy:

```
℘(ab|xy) =
  Σ_{c,d} δ_{a,c} P(b|cdy) P(cd)          if x = 1
  Σ_{c,d} δ_{b,d} P(a|cdx) P(cd)          if y = 1
  Σ_{c,d} P_NS(ab|cdxy) P(cd)             if x≠1, y≠1
```

where `P_NS(ab|cdxy)` is a no-signalling distribution. The variables c, d play the role of hidden variables λ in Bell's theorem, but they correspond to actually observed events.

---

## 5. LF Inequalities for N=3, O=2

The LF polytope for 3 binary-outcome settings per party has **932 facets** grouped into **9 inequivalent classes**:

### Inequality Categories

| Label | Measurement Settings | LF Inequality? | Bell Facet? |
|---|---|---|---|
| Brukner | (1i, 1j) | Yes | Yes |
| Semi-Brukner | (1i, 23) | Yes | Yes |
| Bell non-LF | (23, 23) | No | Yes |
| I3322 | (123, 123) | Yes | Yes |
| Genuine LF | (123, 123) | Yes | No |

Note: i, j ∈ {2,3}. "Bell non-LF" facets are Bell facets but NOT LF facets.

### Selected Explicit Inequalities

Using correlators `⟨AiBj⟩` where Ai (Bj) is Alice's (Bob's) outcome ∈ {−1,+1} for setting i (j):

**Genuine LF Facet 1** (256 instances):
```
-⟨A1⟩ - ⟨A2⟩ - ⟨B1⟩ - ⟨B2⟩
- ⟨A1B1⟩ - 2⟨A1B2⟩ - 2⟨A2B1⟩ + 2⟨A2B2⟩
- ⟨A2B3⟩ - ⟨A3B2⟩ - ⟨A3B3⟩ - 6  ≤  0
```
Maximum quantum violation: **1.345** (provably optimal).
White-noise tolerance: **18.3%**.

**Genuine LF Facet 2** (256 instances):
```
-⟨A1⟩ - ⟨A2⟩ - ⟨A3⟩ - ⟨B1⟩
- ⟨A1B1⟩ - ⟨A2B1⟩ - ⟨A3B1⟩ - 2⟨A1B2⟩
+ ⟨A2B2⟩ + ⟨A3B2⟩ - ⟨A2B3⟩ + ⟨A3B3⟩ - 5  ≤  0
```
Best quantum violation: **0.880** (two-qutrit state required). White-noise tolerance: ~18.0%.

**Brukner inequality** (32 instances):
```
⟨A1B1⟩ - ⟨A1B3⟩ - ⟨A2B1⟩ - ⟨A2B3⟩ - 2  ≤  0
```

**Semi-Brukner inequality** (32 instances):
```
-⟨A1B2⟩ + ⟨A1B3⟩ - ⟨A3B2⟩ - ⟨A3B3⟩ - 2  ≤  0
```

**Bell non-LF (CHSH, not an LF facet)**:
```
⟨A2B2⟩ - ⟨A2B3⟩ - ⟨A3B2⟩ - ⟨A3B3⟩ - 2  ≤  0
```

---

## 6. Experiment

### Setup

- Systems: polarization-encoded photons
- Friends (Charlie, Debbie): photon paths within beam-displacer interferometers
- Superobservers (Alice, Bob): photon-detection measurements
- Source: type-I spontaneous parametric down-conversion (BiBO crystals, 404 nm CW laser)
- Quantum state family tested:

```
ρ_μ = μ|Φ⁻⟩⟨Φ⁻| + (1−μ)/2 (|HV⟩⟨HV| + |VH⟩⟨VH|)
```

where `|Φ⁻⟩ = (|HV⟩ − |VH⟩)/√2`, and μ ∈ [0,1] is the pure-state fraction.

### Measurement Implementation

- **Setting x=1 (ask friend):** motorized mirror inserted → reveals photon path → Alice reads Charlie's outcome directly
- **Settings x=2,3 (superobserver measurement):** mirror removed → interferometer closed → Charlie's measurement reversed → Alice measures polarization after interferometer with different HWP settings

### Measurement Angles

```
φ1 = 168°,  φ2 = 0°,  φ3 = 118°,  β = 175°
```

### Key Experimental Results

| μ value | Observation |
|---|---|
| Low μ | No inequalities violated |
| μ = 0.80, 0.81 | Bell non-LF violated; no LF inequalities violated |
| μ = 0.87 | First LF inequality violated (Semi-Brukner) |
| High μ | All inequality categories violated, including Genuine LF |

- Verified: none of the 932 LF inequalities are violated at μ = 0.80, 0.81 — confirming LF correlations strictly contain LHV correlations.
- Most data points ≥ 2 standard deviations from 0.
- ~91,000 coincidences per measurement set; ~550 coincidences/second overall.

---

## 7. Implications

### Comparison with Bell's Theorem

| Feature | Bell's Theorem | LF Theorem |
|---|---|---|
| Assumptions | AOE + NSD + L + Outcome Independence | AOE + NSD + L |
| LF is strictly weaker | — | Yes |
| Violations → conclusions | Reject outcome independence (standard QM does this) | Must reject AOE (if L and NSD kept) |

### Resolving the LF No-Go Theorem

Rejecting each assumption leads to different interpretations:

**Reject AOE:**
- QBism: measurement outcomes are personal to the agent
- Relational interpretation (Rovelli): facts are relative to observers
- Many-worlds (Everett): all outcomes occur in different branches

**Reject Locality:**
- Bohmian mechanics: nonlocal hidden variables

**Reject No-Superdeterminism:**
- Retrocausality (Price)
- Superdeterminism ('t Hooft)

**Maintain LF (restrict observers):**
- Objective collapse theories (e.g., GRW, Penrose): collapse occurs before macroscopic superpositions form → LF inequalities would not be violated with real observers

### Path Forward: AI Observers in Quantum Computers

If universal quantum computation and strong AI are both physically possible, quantum coherent simulations of an observer could be realized. Experiments with AI agents of increasing complexity can test the LF no-go theorem more stringently. Violation with a given class of "friends" implies either LF assumptions are false, or that class is not a genuine observer.

---

## 8. Mathematical Derivation Summary

### LHV ⊆ LF (Proof Sketch)

An LHV model has the form:
```
℘(ab|xy) = Σ_λ P(a|x,λ) P(b|y,λ) P(λ)
```

Writing λ = (λ^A_1, λ^B_1, λ^A_2, ..., λ^B_N) with local deterministic strategies `P(a|x,λ) = δ_{a,λ^A_x}`, and setting `λ^A_1 = c`, `λ^B_1 = d`, one recovers exactly the LF structure of Eq. (6). The converse is not generally true, proving LHV ⊊ LF.

### LF Polytope Computation

- Extreme points of LF for N=3, O=2: 96 points (4 combinations of (c,d) × 24 extreme points of N=2 no-signalling polytope)
- Facet enumeration: performed using PANDA software (parallel adjacency decomposition algorithm)
- Result: 932 LF facets in 9 inequivalent classes

---

## 9. Connection to Device-Independent Randomness

The LF polytopes (also called "partially deterministic polytopes") are connected to device-independent randomness certification in the presence of no-signalling adversaries — an information-theoretic application independent of the foundational motivation.

---

## Glossary

| Term | Definition |
|---|---|
| AOE | Absoluteness of Observed Events: observed outcomes are real, absolute, not relative |
| NSD | No-Superdeterminism: measurement settings are uncorrelated with prior hidden variables |
| L | Locality: a local setting cannot influence a distant outcome |
| LF | Local Friendliness: the conjunction of AOE + NSD + L |
| LHV | Local Hidden Variable: the standard assumption behind Bell inequalities |
| EWFS | Extended Wigner's Friend Scenario: two labs, two friends, two superobservers |
| OIF | Observer-Independent Facts: Brukner's assumption, equivalent to KSNC |
| KSNC | Kochen-Specker Noncontextuality: all observables have definite values regardless of measurement context |
| NS | No-Signalling: correlations that cannot be used for faster-than-light communication |
| POVM | Positive Operator Valued Measure: generalized quantum measurement |
| BiBO | Bismuth triborate crystal used in spontaneous parametric down-conversion |
| SPDC | Spontaneous Parametric Down-Conversion: photon pair generation process |

---

## Citation

Bong, K.-W., Utreras-Alarcón, A., Ghafari, F., Liang, Y.-C., Tischler, N., Cavalcanti, E. G., Pryde, G. J., & Wiseman, H. M. (2023). A strong no-go theorem on the Wigner's friend paradox. *arXiv:1907.05607v4*.
