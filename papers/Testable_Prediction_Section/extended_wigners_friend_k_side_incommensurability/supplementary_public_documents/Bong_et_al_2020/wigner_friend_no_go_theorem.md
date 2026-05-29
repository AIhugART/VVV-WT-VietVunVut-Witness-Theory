# A Strong No-Go Theorem on the Wigner's Friend Paradox

**Authors:** Kok-Wei Bong, Aníbal Utreras-Alarcón, Farzad Ghafari, Yeong-Cherng Liang, Nora Tischler, Eric G. Cavalcanti, Geoff J. Pryde, Howard M. Wiseman

**Affiliations:** Griffith University (Brisbane & Gold Coast, Australia); National Cheng Kung University (Taiwan)

**arXiv:** 1907.05607v4 [quant-ph] — 15 Mar 2023

---

## Abstract

This paper proves that if quantum evolution is controllable at the scale of an observer, then at least one of the following three assumptions must be false:

1. **No-Superdeterminism (NSD)** — measurement settings are freely chosen
2. **Locality (L)** — no faster-than-light influence of settings on distant outcomes
3. **Absoluteness of Observed Events (AOE)** — every observed event exists absolutely, not relative to any observer

New theory-independent inequalities (Local Friendliness inequalities) are derived and experimentally violated using photonic systems. This theorem places strictly stronger constraints on physical reality than Bell's theorem.

---

## 1. Background: The Wigner's Friend Thought Experiment

### Setup
- A **friend** (observer) measures a quantum system inside an isolated laboratory.
- **Wigner** (superobserver) treats the entire lab — friend included — as a unitarily evolving quantum state.
- If the friend's system is in superposition, the friend observes a definite outcome, but Wigner's unitary description yields an entangled state with no definite value for the friend's outcome.

### The Measurement Problem
This apparent contradiction between:
- The friend's **state-update rule** (non-unitary, probabilistic collapse), and
- Wigner's **unitary evolution rule** (deterministic, reversible)

...is the quantum **measurement problem**.

### Why Decoherence Does Not Solve It
Decoherence suppresses interference at the macroscopic level but still leaves a superposition of many quasi-classical branches. It does not explain why a single outcome is perceived.

---

## 2. Extended Wigner's Friend Scenario (EWFS)

### Scenario (Brukner's Setup, Extended Here)

```
Entangled particle pair
       |
   ----+----
   |       |
Charlie   Debbie     <- Friends (observers inside labs)
   |       |
 Alice    Bob        <- Superobservers (outside, space-like separated)
```

- **Charlie** and **Debbie** each measure one particle from an entangled pair, recording outcomes `c` and `d`.
- **Alice** and **Bob** each independently choose one of N measurement settings (`x`, `y`) and record outcomes (`a`, `b`).
- Crucially, Alice's setting `x=1` means she opens Charlie's lab and asks him his result (so `a = c`). For `x ∈ {2,...,N}`, she performs a different quantum operation on the whole lab, potentially erasing Charlie's memory.
- All measurements by Alice and Bob are **space-like separated**.

### What Is Measured
The experiment yields empirical probabilities `℘(a,b|x,y)` — correlations between superobserver outcomes only. The friends' outcomes `c`, `d` are generally not accessible after the superobserver acts (except when `x=1` or `y=1`).

---

## 3. The Three Assumptions: Local Friendliness (LF)

### Assumption 1 — Absoluteness of Observed Events (AOE)
> An observed event is a real single event, not relative to anything or anyone.

**In the EWFS**, AOE requires the existence of a joint probability distribution `P(a,b,c,d|x,y)` such that:

- `℘(a,b|x,y) = Σ_{c,d} P(a,b,c,d|x,y)`  — marginalizing over friend outcomes recovers observed stats
- `P(a|c,d,x=1,y) = δ_{a,c}`              — when Alice asks Charlie, she reports his answer
- `P(b|c,d,x,y=1) = δ_{b,d}`              — when Bob asks Debbie, he reports her answer

**Key distinction from OIF/KSNC:** AOE only assigns truth values to *actually performed* measurements. It does not assume counterfactual definiteness. It is compatible with Peres' dictum: "Unperformed experiments have no results."

### Assumption 2 — No-Superdeterminism (NSD)
> Any set of events on a space-like hypersurface is uncorrelated with freely chosen actions subsequent to that hypersurface.

**In the EWFS:** The friends' outcomes are independent of the superobservers' settings:
```
P(c,d|x,y) = P(c,d)   for all c, d, x, y
```

### Assumption 3 — Locality (L)
> The probability of an observable event is unchanged by conditioning on a space-like-separated free choice, even conditioned on other events outside the future light cone of that choice.

**In the EWFS:**
```
P(a|c,d,x,y) = P(a|c,d,x)   — Alice's outcome independent of Bob's setting
P(b|c,d,x,y) = P(b|c,d,y)   — Bob's outcome independent of Alice's setting
```

### The Conjunction
The conjunction of AOE + NSD + L is called **Local Friendliness (LF)**.

---

## 4. Main Theorem

> **Theorem 1 (Local Friendliness No-Go):** If a superobserver can perform arbitrary quantum operations on an observer and its environment, then no physical theory can satisfy Local Friendliness.

**Proof strategy:** LF implies a set of inequality constraints on `℘(a,b|x,y)` (the LF inequalities). Quantum mechanics predicts violations of these inequalities in EWFS scenarios. The theorem is *theory-independent*: if the quantum predictions are observed experimentally, the metaphysical conclusions hold for any theory.

---

## 5. LF Correlations vs. Bell (LHV) Correlations

### LHV Model (Bell)
A set of correlations has a **local hidden variable (LHV)** model if:
```
℘(a,b|x,y) = Σ_λ P(a|x,λ) P(b|y,λ) P(λ)
```

### LF Model (This Paper)
Under AOE + NSD + L, the general form is:

```
℘(a,b|x,y) =
  Σ_{c,d} δ_{a,c} P(b|c,d,y) P(c,d)         if x=1
  Σ_{c,d} δ_{b,d} P(a|c,d,x) P(c,d)         if y=1
  Σ_{c,d} P_NS(a,b|c,d,x,y) P(c,d)          if x≠1 and y≠1
```

where `P_NS` satisfies the no-signalling condition (locality only, not full local causality).

### Key Structural Differences

| Property | LHV | LF |
|---|---|---|
| Requires hidden variables | Yes | No |
| Assumes outcome independence | Yes | No |
| Assumes counterfactual definiteness | Yes (via KSNC) | No |
| For N=2 settings | Same as LF | Same as LHV |
| For N≥3 settings | Strict subset of LF | Strict superset of LHV |
| Violations imply | Nonlocality or non-realism | Must reject AOE (if L and NSD kept) |

**LHV ⊂ LF ⊂ NS (no-signalling)**

---

## 6. LF Inequalities for N=3, O=2

For 3 binary-outcome measurement settings per party, the LF polytope has **932 facets** grouped into **9 inequivalent classes**:

### Inequality Classes

| Label | Settings Involved | Is LF Inequality? | Is Bell Facet? |
|---|---|---|---|
| Brukner | (1i, 1j) | Yes | Yes |
| Semi-Brukner | (1i, 23) | Yes | Yes |
| Bell non-LF | (23, 23) | No | Yes |
| I3322 | (123, 123) | Yes | Yes |
| Genuine LF | (123, 123) | Yes | No |

**Note:** "Bell non-LF" inequalities are Bell facets but *not* LF facets — they do not constrain LF correlations. This means quantum correlations can violate Bell inequalities while still satisfying all LF inequalities (demonstrated experimentally at μ = 0.80, 0.81).

### Representative Inequalities (correlator form, where A_i, B_j ∈ {+1,−1})

**Genuine LF Facet 1** (256 occurrences):
```
−⟨A₁⟩ − ⟨A₂⟩ − ⟨B₁⟩ − ⟨B₂⟩
− ⟨A₁B₁⟩ − 2⟨A₁B₂⟩ − 2⟨A₂B₁⟩ + 2⟨A₂B₂⟩
− ⟨A₂B₃⟩ − ⟨A₃B₂⟩ − ⟨A₃B₃⟩ − 6  ≤  0  (LF bound)
```

**Genuine LF Facet 2** (256 occurrences):
```
−⟨A₁⟩ − ⟨A₂⟩ − ⟨A₃⟩ − ⟨B₁⟩
− ⟨A₁B₁⟩ − ⟨A₂B₁⟩ − ⟨A₃B₁⟩ − 2⟨A₁B₂⟩
+ ⟨A₂B₂⟩ + ⟨A₃B₂⟩ − ⟨A₂B₃⟩ + ⟨A₃B₃⟩ − 5  ≤  0
```

**Bell I3322 (inputs 1,2)**:
```
−⟨A₁⟩ + ⟨A₂⟩ + ⟨B₁⟩ − ⟨B₂⟩
+ ⟨A₁B₁⟩ − ⟨A₁B₂⟩ − ⟨A₁B₃⟩ − ⟨A₂B₁⟩
+ ⟨A₂B₂⟩ − ⟨A₂B₃⟩ − ⟨A₃B₁⟩ − ⟨A₃B₂⟩ − 4  ≤  0
```

**Brukner inequality** (CHSH-type, settings 1,2 × 1,3):
```
⟨A₁B₁⟩ − ⟨A₁B₃⟩ − ⟨A₂B₁⟩ − ⟨A₂B₃⟩ − 2  ≤  0
```

**Semi-Brukner inequality** (settings 2,3 × 1,2):
```
−⟨A₁B₂⟩ + ⟨A₁B₃⟩ − ⟨A₃B₂⟩ − ⟨A₃B₃⟩ − 2  ≤  0
```

**Bell non-LF** (not an LF constraint):
```
⟨A₂B₂⟩ − ⟨A₂B₃⟩ − ⟨A₃B₂⟩ − ⟨A₃B₃⟩ − 2  ≤  0  (LHV bound only)
```

---

## 7. Quantum Violations

### Target Quantum State
Two-qubit polarization states:
```
ρ_μ = μ |Φ⁻⟩⟨Φ⁻| + (1−μ)/2 (|HV⟩⟨HV| + |VH⟩⟨VH|)
```
where `|Φ⁻⟩ = (|HV⟩ − |VH⟩)/√2`, and μ ∈ [0,1] controls the singlet fraction.

### Measurement Directions
Projective measurements in the XY plane of the Bloch sphere:
```
Alice: |φ_x⟩ = (|H⟩ + e^{iφ_x}|V⟩)/√2
Bob:   |β_y⟩ = (|H⟩ + e^{i(β−φ_y)}|V⟩)/√2

Chosen angles: φ₁=168°, φ₂=0°, φ₃=118°, β=175°
```

### Maximal Quantum Violations of Genuine LF Inequalities
- **Genuine LF 1:** Max quantum violation = **1.345** (LF bound = 0), achieved with a partially entangled two-qubit state (Schmidt coefficients ≈ 0.776, 0.631). White-noise tolerance: **18.3%**.
- **Genuine LF 2:** Max quantum violation = **0.880** (LF bound = 0), achieved with a partially entangled two-qutrit state. White-noise tolerance: **18.0%**.

---

## 8. Experiment

### System
- **Entangled pair:** Polarization-encoded photons
- **Friends (Charlie, Debbie):** Photon paths within beam-displacer (BD) interferometers
- **Superobservers (Alice, Bob):** Photon-detection measurements

### Source
Type-I spontaneous parametric down-conversion (SPDC) using two orthogonally oriented BiBO crystals, pumped by a 404 nm CW laser diode. An imbalanced pump-beam interferometer controls the μ parameter by mixing a decoherent (long arm) state with a singlet-producing (short arm) state.

### Measurement Implementation

| Setting | Implementation |
|---|---|
| x=1 (ask friend) | Motorized mirror inserted → reveals photon path = friend's outcome |
| x=2 or 3 (superobserver measurement) | Mirror removed → closes interferometer → reverses friend's measurement → measures polarization |

### Experimental Results Summary

| μ value | Observation |
|---|---|
| Low μ | No inequalities violated |
| μ ≈ 0.80–0.81 | **Bell inequalities violated, but NO LF inequalities violated** (confirms LF ⊋ LHV) |
| μ ≈ 0.87 | First LF inequality violation (Semi-Brukner) |
| High μ | All inequality types violated, including Genuine LF |

All data points (except μ=0.81) are ≥2 standard deviations from zero. The experiment verified all 932 LF facets.

---

## 9. Comparison with Bell's Theorem

| Feature | Bell's Theorem | LF No-Go Theorem |
|---|---|---|
| Assumptions | NSD + L + AOE + Outcome Independence | NSD + L + AOE |
| AOE explicit? | Implicit (as "macroreality") | Explicit |
| Outcome independence required? | Yes | No |
| Counterfactual definiteness? | Yes (via KSNC/OIF) | No |
| Strength of conclusions | Weaker | **Strictly stronger** |
| Friends' observations essential? | No | Yes |

**Key implication:** Violations of Bell inequalities can be accommodated by rejecting outcome independence while keeping L, NSD, and AOE. The LF theorem closes this escape route: if LF inequalities are violated, one *must* reject AOE (given L and NSD).

---

## 10. Implications and Interpretations

### What Violating LF Inequalities Forces

Given NSD and L, a violation of LF inequalities requires rejecting **AOE** — the idea that measurement outcomes are real, absolute, observer-independent facts.

### Interpretations That Reject AOE
- **QBism** (Fuchs & Schack): measurement outcomes are personal beliefs, not objective facts
- **Relational Quantum Mechanics** (Rovelli): facts are always relative to a reference system
- **Many-Worlds** (Everett): no single absolute outcome; all branches real

### Interpretations That Reject L (Keep AOE)
- **Bohmian Mechanics**: nonlocal but deterministic hidden variables

### Interpretations That Reject NSD
- Retrocausality (Price), superdeterminism ('t Hooft) — no complete quantum-compatible theory exists yet

### Objective Collapse Theories
Theories like GRW or Penrose gravity-collapse restore absolute outcomes by preventing macroscopic superpositions. In this case, LF inequalities would not be violable with genuine observers — an open empirical question.

### Path Toward Stronger Tests
- AI agents running in large quantum computers as "friends" could probe LF assumptions more rigorously
- Each new class of "friend" systems tested either demonstrates LF violation (ruling out those assumptions) or shows that such systems are not genuine observers

---

## 11. Connection to Randomness Certification

The LF polytopes have been independently studied as "partially deterministic polytopes" in the context of device-independent randomness certification against no-signalling adversaries (Woodhead 2014; Colbeck 2006; Pironio et al. 2010; Acín & Masanes 2016).

---

## Key Definitions Reference

| Term | Definition |
|---|---|
| AOE | Absoluteness of Observed Events: observed outcomes are real, absolute, not relative |
| NSD | No-Superdeterminism: settings are uncorrelated with pre-existing variables |
| L | Locality: local settings do not influence distant outcomes (parameter independence) |
| LF | Local Friendliness = AOE ∧ NSD ∧ L |
| LHV | Local Hidden Variable model (Bell correlations) |
| EWFS | Extended Wigner's Friend Scenario |
| OIF | Observer-Independent Facts (Brukner's stronger assumption, implies KSNC) |
| KSNC | Kochen-Specker Noncontextuality |
| NS | No-Signalling |
| SPDC | Spontaneous Parametric Down-Conversion |

---

## Citation

Bong, K.-W., Utreras-Alarcón, A., Ghafari, F., Liang, Y.-C., Tischler, N., Cavalcanti, E. G., Pryde, G. J., & Wiseman, H. M. (2023). *A strong no-go theorem on the Wigner's friend paradox*. arXiv:1907.05607v4 [quant-ph].
