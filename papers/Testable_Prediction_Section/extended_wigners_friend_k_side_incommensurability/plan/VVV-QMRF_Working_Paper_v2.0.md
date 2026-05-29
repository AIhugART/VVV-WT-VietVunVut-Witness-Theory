Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# When Does a Physical Interaction Become a Valid Registered Measurement?
## A VVV-QMRF Registration-Layer Extension of Quantum Mechanics with a Testable Prediction for Extended Wigner's Friend Scenarios

**Working Paper v2.0**
**Author:** Viet Nguyen Xuan (VietVunVut)
**Repository:** https://github.com/AIhugART/VVV-QMRF-VietVunVut-Quantum-Measurement-Registration-Framework
**Status:** Working paper submitted for community feedback. All formal claims are Class D (proposed) or Class C (conjecture) unless stated otherwise. Critique is explicitly invited.
**Document type:** Publication-facing draft / `publication_draft`
**Date:** 2026-05-17
**Scope:** Registration-layer modeling of Extended Wigner's Friend scenarios within VVV-QMRF.
**Out of scope:** Replacement of Standard Quantum Mechanics, revision of the Born rule, consciousness-based collapse, or direct physical detection of K-side structures.
**Claim boundary:** Formal notation in this paper defines proposed K-side registration models unless separately identified as Standard Quantum Mechanics or externally validated experimental result.
**Formula boundary:** Symbols such as `K`, `σ_R(M)`, `requires_K_joint`, and `⊥_K` are registration-layer notation, not new physical observables.
**Reader level:** Technical working-paper reader; community feedback is invited before publication-level claims are strengthened.
**Neutral wording boundary:** Standard Quantum Mechanics is treated as scope-silent about registration architecture, not as logically defective.

---

## Abstract

The quantum measurement problem has remained unresolved for nearly a century. Standard quantum mechanics specifies, via postulate P3, that a measurement of observable A on state |ψ⟩ yields eigenvalue aₖ with probability |⟨aₖ|ψ⟩|². What P3 does not specify is when a physical interaction constitutes a valid registered measurement event. This silence generates the von Neumann chain problem and leaves the Heisenberg cut formally undefined.

This paper proposes VVV-QMRF (VietVunVut Quantum Measurement Registration Framework): a registration-layer extension of quantum mechanics grounded in Buddhist Pramāṇa epistemology (Dignāga–Dharmakīrti tradition). The framework adds a K-side registration space K, separate from the physical Hilbert space H, and proposes a six-condition test for valid registered measurement. Applied to Extended Wigner's Friend (EWF) scenarios, this yields a specific conjecture: K-side registration spaces of two observers are incommensurable (K_F ⊥_K K_W) when a joint registration space K_joint is structurally required but cannot satisfy all six conditions simultaneously.

This conjecture is not trivially true for all frameworks. It separates ordinary Bell-type nonclassicality from LF-level Wigner-friend inconsistency, as illustrated by data from Bong et al. (2020) at μ = 0.80, 0.81 where Bell non-LF violation is reported while Local Friendliness inequalities remain unviolated. Existing data from Proietti et al. (2019) and Bong et al. (2020) are compatible with the prediction under the registration-layer reading developed here. The framework does not replace Standard Quantum Mechanics, revise the Born rule, invoke consciousness, or claim that a K-side structure is directly observed as a physical object. All formal claims are classified by evidence level. A purpose-designed experiment is required for confirmation.

---

## 1. The Registration Layer Gap

### 1.1 What Quantum Mechanics Specifies

Standard quantum mechanics is built on four postulates:

- **P1 (State):** A physical system is represented by a density operator ρ ∈ D(H).
- **P2 (Observables):** Physical quantities are represented by self-adjoint operators A on H.
- **P3 (Measurement):** Measurement of A on state |ψ⟩ yields eigenvalue aₖ with probability |⟨aₖ|ψ⟩|², after which the state updates to the corresponding eigenstate.
- **P4 (Dynamics):** Between measurements, the state evolves unitarily via the Schrödinger equation.

P3 specifies what outcome appears and with what probability. P3 does not specify when a physical interaction counts as a measurement, what structural conditions distinguish a measurement from a non-measurement interaction, or what stops the measurement chain.

This is the registration layer gap.

### 1.2 The Von Neumann Chain Problem

Von Neumann (1932) observed that if apparatus A1 measures system S, A1 becomes entangled with S. If apparatus A2 then measures A1, A2 becomes entangled with A1+S. No postulate of standard QM specifies where this chain terminates. Every proposed stopping point — macroscopic size, decoherence, consciousness — is external to the formalism.

Decoherence (Zurek 2003) explains why superpositions become effectively classical at the macroscopic scale. It does not explain when a physical interaction constitutes a registration event in the sense of a definite recorded outcome. The von Neumann chain problem is a registration-layer problem, not a decoherence problem.

### 1.3 The Heisenberg Cut

Copenhagen quantum mechanics (Bohr 1935; Heisenberg 1958) assigns measurement authority to "the classical apparatus" without formally defining what makes an apparatus classical, why it has registration authority, or what structural conditions produce a definite outcome. The Heisenberg cut is a boundary without a formal location.

VVV-QMRF addresses both problems by introducing a registration layer K, separate from the physical layer ρ, and proposing formal conditions for valid registration events within K.

---

## 2. The K-side Registration Space

### 2.1 Layer Separation

VVV-QMRF introduces a strict separation between two layers:

- **Physical layer (ρ-side):** Physical states, observables, and dynamics as described by Standard QM. This layer is not modified. ρ ∈ D(H), H is the standard Hilbert space.
- **Registration layer (K-side):** The space of registration events, recording conditions, and validity states. K ≠ H. K-side structure does not alter ρ-side dynamics.

This separation is the core architectural commitment of VVV-QMRF.

### 2.2 Minimal K-state

A registration event is represented by a minimal K-state tuple:

```
k = ⟨M, o, cert, t, V⟩

where:
  M    = measurement act identifier
  o    = registered outcome
  cert = certification status (self-certified or not)
  t    = registration time
  V    = validity status ∈ {0, 1}
```

The K-side registration space K is the collection of such tuples produced by a registering system R over time.

### 2.3 Source: Buddhist Pramāṇa Epistemology

The registration-layer architecture is derived structurally from Buddhist Pramāṇa epistemology (Dignāga–Dharmakīrti tradition), as systematized by Prasad (2023). Pramāṇa theory addresses the formal conditions under which a cognition constitutes a valid knowledge event. The structural extraction used here concerns:

- **Svasaṃvedana:** Self-certifying cognition — a cognition that certifies its own occurrence without requiring a second-order cognition to validate it. Source for E1.
- **Arthakriyā:** Validity as functional success — a cognition is valid if it enables successful engagement with its object. Source for validity conditions in E7.
- **Svataḥ/Parataḥ prāmāṇya:** Initial validity is intrinsic, while invalidity is detected extrinsically. This is used as a structural meta-epistemological principle for E7, not as a standalone Buddhist Epistemology node.
- **Anumāna/Pratyakṣa:** Inference and perception as distinct registration modes. Source for E11, E14.

This is a structural extraction, not a claim that Buddhist epistemology proves quantum mechanics or that quantum mechanics validates Buddhist doctrine.

---

## 3. The Valid Registered Measurement Test

This section states the central contribution of the paper: a six-condition test for when a physical interaction constitutes a valid registered measurement.

### 3.1 The Six Conditions

**Interaction X is a valid registered measurement for registering system R if and only if:**

```
Condition 1 (Physical):
  X occurs at the physical ρ-side.
  [Standard QM governs this layer. VVV-QMRF does not modify it.]

Condition 2 (Admission):
  X is admitted into K-side as measurement act M_X for system R.
  [The interaction crosses the layer boundary into K.]

Condition 3 (Process membership):
  M_X ∈ R, where R = {M_R1, M_R2, ...} is the registering
  process of system R ordered by registration time.    [E6]

Condition 4 (Self-certification):
  σ_R(M_X) = 1: M_X self-certifies its occurrence within K_R,
  determined intrinsically, not by any external M′ ≠ M_X.  [E1]

Condition 5 (Default validity):
  V(M_X) = 1 by default upon admission.              [E7]

Condition 6 (Non-invalidation):
  No later registration act M′ in K_R contradicts M_X
  such that V(M_X) is revised to 0.                  [E7]
```

All six conditions must hold for X to count as a valid registered measurement.

### 3.2 The K-side Stopping Proposition

**Proposition (K-side stopping, Class D proposed):**

If Conditions 1–6 hold for measurement act M_X of registering system R, then no further K-side registration act is required to certify M_X. The von Neumann registration regress terminates at M_X on the K-side without modifying ρ-side dynamics.

**Why this addresses the Heisenberg cut:** Condition 4 (self-certification) provides the formal property that Copenhagen assigns to "classical apparatus" without definition. An apparatus has registration authority because σ_R(M) = 1 is determined intrinsically within K_R, requiring no external certifier. This is the registration-layer account of why the chain stops.

**Claim class:** D (proposed). Formal proof that Conditions 1–6 are jointly sufficient for chain termination is an open item.

### 3.3 Observer-Indexed Self-Certification

For multi-observer scenarios, the self-certification function carries an observer index:

```
σ_R(M) ∈ {0, 1}

σ_R(M) = 1  iff  M occurred as a K-side registration event
  of registering system R, determined intrinsically within K_R,
  not by any M′ ≠ M and not by any R′ ≠ R.

Independence: σ_F(M_F) is determined within K_F
  independently of K_W, and vice versa.
```

The original σ(M) is the single-observer special case: σ(M) = σ_R(M) where R is unique. All properties of the single-observer case are preserved. **[E01 Section 11.2, Class D]**

---

## 4. Extended Wigner's Friend and K-side Incommensurability

### 4.1 The Extended Wigner's Friend Setup

In the Extended Wigner's Friend scenario (Frauchiger and Renner 2018; Brukner 2018), two observer pairs interact with a shared quantum system:

- **Friend F** measures quantum system S inside a sealed laboratory. From F's perspective, a definite outcome o_F is recorded: σ_F(M_F) = 1.
- **Wigner W** models the entire laboratory (F + S) as a unitarily evolving quantum state. From W's perspective, F+S is in superposition before W's measurement. W then performs an interference measurement M_W on F's laboratory.

Standard QM supplies formal descriptions for both perspectives without providing a registration-layer account of their structural incompatibility. This is where the registration layer offers new structure.

### 4.2 Applying the Six Conditions to Each Observer

**Friend F:**
```
X_F → M_F ∈ R_F         [Condition 3, E6]
σ_F(M_F) = 1             [Condition 4, E1]
V_F(M_F) = 1             [Condition 5, E7]
No M′ contradicts M_F    [Condition 6, E7]
→ M_F is a valid registered measurement within K_F.
```

**Wigner W:**
```
X_W → M_W ∈ R_W         [Condition 3, E6]
σ_W(M_W) = 1             [Condition 4, E1]
V_W(M_W) = 1             [Condition 5, E7]
No M′ contradicts M_W    [Condition 6, E7]
→ M_W is a valid registered measurement within K_W.
```

Both observers satisfy the six conditions independently within their own K-sides.

### 4.3 The requires_K_joint Predicate

The question is whether a joint registration space K_joint can contain both K_F and K_W as jointly valid entries.

```
requires_K_joint(F, W, M_F, M_W) = 1
  iff a single K_joint is structurally required to contain both
  k_F = ⟨M_F, o_F, cert_F, t_F, V_F⟩ and
  k_W = ⟨M_W, o_W, cert_W, t_W, V_W⟩
  as jointly valid entries satisfying Conditions 1–6 for both.

requires_K_joint(F, W, M_F, M_W) = 0
  iff K_F and K_W can remain independent K-side spaces without
  any joint validity check between them.
```

**Sufficient conditions for requires_K_joint = 1:**

- **Condition A (Wigner interference):** W performs an interference measurement on the laboratory containing F+S. M_W registers a superposition description of F+S; M_F registers a definite outcome o_F of the same system S. Both claim K-side validity on the same physical event. → requires_K_joint = 1.
- **Condition B (Direct comparison):** F and W directly compare registration records and a logical contradiction is detectable. → requires_K_joint = 1.

**Sufficient conditions for requires_K_joint = 0:**

- **Condition C (No interference, no comparison):** W does not perform interference measurement on F's laboratory. K_F and K_W remain causally isolated. → requires_K_joint = 0.
- **Condition D (Separable state):** The shared quantum state |ψ⟩ is separable and M_F, M_W act on non-overlapping subsystems. → requires_K_joint = 0.

**Claim class:** D (proposed). Conditions A–D are sufficient conditions only. Necessary and sufficient characterization of requires_K_joint is an open item.

### 4.4 Definition Boundary for K_joint and K-side Conflict

Before stating the K_joint failure proposition, the paper uses the following bounded definitions:

```
K_joint
  A proposed registration-layer model that would contain entries from
  K_F and K_W in one joint validity structure.

M_W ⊥_K M_F
  A proposed K-side conflict relation: M_W and M_F cannot both retain
  validity value 1 inside the same K_joint because their registered
  contents impose incompatible joint-validity commitments on the same
  physical event domain.

joint-validity failure
  The failure of any proposed K_joint to satisfy Conditions 1-6 for
  both M_F and M_W while preserving V(M_F)=1 and V(M_W)=1.
```

These definitions are registration-layer definitions only. They do not introduce a new physical observable, alter Hilbert-space dynamics, or claim that K_joint is directly detected as a physical object. The relation `⊥_K` is a Class D proposed formal relation; its use in the empirical prediction remains Class C until a full mathematical characterization and purpose-designed test are supplied.

### 4.5 K_joint Failure and K-side Incommensurability

**Proposition (K_joint failure, Class D proposed):**

If requires_K_joint = 1 via Condition A, then no K_joint exists such that:
- (i) σ_F(M_F) = 1 holds within K_joint [Condition 4 for F]
- (ii) σ_W(M_W) = 1 holds within K_joint [Condition 4 for W]
- (iii) V(M_F) = 1 and V(M_W) = 1 simultaneously [Condition 5+6 for both]

**Proof sketch:**

```
Step 1 [E6]: F and W are distinct registering processes R_F and R_W
  with distinct K-side time sequences.

Step 2 [E1, observer-indexed]: σ_F(M_F) = 1 is intrinsic to K_F.
  σ_W(M_W) = 1 is intrinsic to K_W. Both hold independently.

Step 3 [Condition A]: M_W registers F+S as superposition (no definite o_F).
  M_F registers o_F as definite outcome. These are contradicting
  registrations: M_W ⊥_K M_F — they assert incompatible K-side
  validity claims on the same physical event.

Step 4 [E7 Axiom 2]: If M′ contradicts M, V(M) and V(M′) cannot both
  equal 1 in the same K-space. M_W ⊥_K M_F implies V(M_F) = 1 and
  V(M_W) = 1 cannot simultaneously hold in any K_joint.
  Therefore K_joint satisfying (i)–(iii) does not exist.
```

**K-side incommensurability:**

```
K_F ⊥_K K_W
  iff  requires_K_joint = 1  AND  no K_joint satisfying (i)–(iii) exists.
```

**Claim class of Step 4:** D (proposed). Depends on E7 Axiom 2, which is itself Class D. Full formal proof is an open item listed in Section 7.

### 4.6 The Falsifiable Prediction

VVV-QMRF predicts a two-part structure:

> In Extended Wigner's Friend experiments, configurations satisfying requires_K_joint = 1 are the configurations in which K-side joint-validity failure is structurally relevant. A violation of Local Friendliness inequalities is expected only when this structural condition is combined with sufficient empirical strength, such as adequate entanglement, visibility, and noise control. Configurations satisfying requires_K_joint = 0 are predicted to produce no LF violation from the K-side registration perspective.

**This prediction is falsified if:** An EWF experiment produces results better modeled by a single joint-registration structure than by K-side incommensurability in a configuration where requires_K_joint = 1 — i.e., if the experimental data are consistent with one K_joint satisfying Conditions 1-6 for both observers simultaneously, under Condition A and under empirical conditions strong enough for LF-level failure to be observable. The empirical absence of LF violation in a weak-entanglement or high-noise regime does not by itself falsify the framework, because Section 5.1 treats requires_K_joint = 1 as structurally necessary but not empirically sufficient for visible LF violation. If a single joint-registration model is empirically favored under the relevant structural and empirical conditions, E7 Axiom 2 or the proposed `⊥_K` relation requires revision.

**Claim class:** C (conjecture). Pending experimental operationalization and verification.

---

## 5. Experimental Contact

### 5.1 What Distinguishes VVV-QMRF from Existing Frameworks

The key asymmetry is this: requires_K_joint = 1 is a structurally necessary but not empirically sufficient condition for LF violation. The quantum state must also be sufficiently entangled, and the experiment must have sufficient visibility and noise control, for K_joint failure to produce an observable inequality violation. This generates a two-regime structure:

- **Regime 1:** requires_K_joint = 1 AND state weakly entangled → Condition A structurally active, K_joint structurally required, but empirical LF violation may be absent.
- **Regime 2:** requires_K_joint = 1 AND state strongly entangled → K_joint failure is predicted to become visible as LF violation.

A decoherence-only framework does not distinguish these two regimes at the registration-layer level, because it contains no predicate equivalent to requires_K_joint for separating Bell non-LF violation from LF-level joint-validity failure.

This is not trivially true for all frameworks. It generates an observable conjecture: Bell non-LF violation can appear in Regime 1 while LF inequalities remain unviolated, and LF violation appears in Regime 2 when entanglement, visibility, and noise conditions are sufficient.

### 5.2 Proietti et al. (2019)

**Reference:** Proietti, M. et al. Experimental test of local observer independence. Science Advances 5(9), eaaw9832 (2019). DOI: 10.1126/sciadv.aaw9832.

**Setup:** Six-photon optical experiment with four observers (Alice's Friend, Bob's Friend, Alice, Bob). Two measurement choices per external observer:

- A0 / B0: read Friend's memory record (no interference).
- A1 / B1: Wigner-type joint measurement via nonclassical interference on a 50/50 beam splitter.

**Applying requires_K_joint:**

| Term | Configuration | W interference? | Condition | requires_K_joint | Role in S |
|------|--------------|----------------|-----------|-----------------|-----------|
| ⟨A1B1⟩ | Both Wigner-type | Both sides | A | 1 | Added |
| ⟨A1B0⟩ | Alice Wigner, Bob record | Alice side | A | 1 | Added |
| ⟨A0B1⟩ | Alice record, Bob Wigner | Bob side | A | 1 | Added |
| ⟨A0B0⟩ | Both record readout | None | C | 0 | Subtracted |

**Experimental values (alternative observable protocol):**

```
S = ⟨A1B1⟩ + ⟨A1B0⟩ + ⟨A0B1⟩ − ⟨A0B0⟩
S = 0.571 + 0.577 + 0.573 − 0.662
S = 2.407  (reported: 2.407 ± 0.073, violation > 5σ)
```

**VVV-QMRF reading:** The three terms with requires_K_joint = 1 contribute positively to the violated aggregate expression. The one term with requires_K_joint = 0 is subtracted. This aggregate sign pattern is consistent with the K_F ⊥_K K_W prediction, but it is not a per-configuration confirmation because S is evaluated as a combined inequality expression.

**Result:** Consistent at Bell-Wigner term-contribution level. Not a per-configuration confirmation; S is an aggregate expression.

### 5.3 Bong et al. (2020)

**Reference:** Bong, K.W. et al. A strong no-go theorem on the Wigner's friend paradox. Nature Physics 16, 1199–1205 (2020). DOI: 10.1038/s41567-020-0990-x. arXiv: 1907.05607.

**Setup:** Extended Wigner's Friend scenario with four observers (Charlie, Debbie, Alice, Bob). Three measurement settings per external observer. Friends implemented as photon paths within beam-displacer interferometers. State family:

```
ρ_μ = μ|Φ⁻⟩⟨Φ⁻| + (1−μ)/2 (|HV⟩⟨HV| + |VH⟩⟨VH|)
```

where μ ∈ [0,1] controls singlet fraction.

**Applying requires_K_joint to settings:**

| Setting pair | Alice side | Bob side | W interference? | Condition | requires_K_joint |
|-------------|-----------|---------|----------------|-----------|-----------------|
| x=1, y=1 | Ask Charlie | Ask Debbie | None | C | 0 |
| x=1, y=2/3 | Ask Charlie | Superobserver | Bob side | A | 1 |
| x=2/3, y=1 | Superobserver | Ask Debbie | Alice side | A | 1 |
| x=2/3, y=2/3 | Superobserver | Superobserver | Both sides | A | 1 |

**μ-threshold behavior and VVV-QMRF reading:**

| μ regime | Reported result | VVV-QMRF reading |
|----------|----------------|-----------------|
| Low μ | No inequalities violated | requires_K_joint = 1 structurally active in x=2/3 settings; LF violation absent because state too weakly entangled |
| μ = 0.80, 0.81 | Bell non-LF violated; LF inequalities NOT violated | Regime 1: Condition A active, K_joint required, but entanglement insufficient for LF-level failure |
| μ ≈ 0.87 | First LF violation (Semi-Brukner) | Transition to Regime 2: K_joint failure is interpreted as becoming empirically visible |
| High μ | All categories violated including Genuine LF | Regime 2: x=2/3, y=2/3 Condition A strongly active, K_joint failure fully exposed |

**The asymmetric prediction:** At μ = 0.80, 0.81, Bell non-LF violation appears while LF inequalities remain unviolated. VVV-QMRF offers a registration-layer account of this asymmetry via the two-regime structure: requires_K_joint = 1 in superobserver settings (Condition A), but the quantum state at this μ value is not sufficiently entangled for K_joint failure to produce LF-level violation. A framework without a requires_K_joint predicate has no structural account, at the registration-layer level, of why Bell-type violation and LF-type violation may appear at different μ thresholds.

**Result:** Consistent at structural setting-level and μ-threshold level.

### 5.4 Overall Condition 3 Status

Both Proietti et al. (2019) and Bong et al. (2020) are compatible with the VVV-QMRF prediction under the registration-layer reading developed here. This is an existing-data compatibility check, not confirmation. A purpose-designed experiment varying requires_K_joint directly as an independent variable is required for confirmation-level evidence.

### 5.5 Claim-Control Summary

| Claim | Current status | Boundary condition |
|-------|----------------|--------------------|
| Six-condition registered measurement test | Class D proposed definition | Defines K-side registration validity; does not revise P1-P4 or the Born rule |
| K-side stopping proposition | Class D proposed proposition | Requires formal proof of joint sufficiency of Conditions 1-6 |
| K_joint failure proposition | Class D proposed proposition | Depends on E7 Axiom 2 and the proposed definition boundary for ⊥_K; full mathematical characterization remains open |
| requires_K_joint predicate | Class D proposed predicate | Sufficient conditions A-D only; necessary and sufficient characterization remains open |
| LF-violation prediction | Class C conjecture | requires_K_joint = 1 is structurally necessary but not empirically sufficient; entanglement, visibility, and noise control also matter |
| Proietti/Bong comparison | Existing-data compatibility check | Aggregate-level and setting-level consistency only; not confirmation |

This table functions as the claim-control layer for the working paper: formal language is limited by the stated evidence class, and empirical language is limited to compatibility unless a purpose-designed experiment directly tests requires_K_joint.

---

## 6. Positioning Against Existing Interpretations

| Interpretation | Response to EWF paradox | VVV-QMRF difference |
|---------------|------------------------|---------------------|
| Copenhagen | WF is ill-posed; classical apparatus required | E1/E7 formalize why apparatus has registration authority: σ_R(M) = 1 intrinsically |
| Many-Worlds | All outcomes occur; no paradox | Registration events are singular per K-side, not globally branching |
| QBism | Facts are agent-relative; no paradox | Agrees on agent-relativity; adds formal K-side structure via six conditions |
| Relational QM | Facts are relation-relative; no paradox | Closest existing framework; VVV-QMRF adds formal registration machinery that Relational QM does not provide |
| Objective Collapse | Physical collapse restores absolute facts | VVV-QMRF does not require physical collapse mechanism on ρ-side |

**Relation to Relational Quantum Mechanics:** Rovelli (1996) argues that quantum states are relative to observers. VVV-QMRF adds the formal registration-layer structure that explains why they are relative: σ_R(M) operates intrinsically within K_R, independently of K_{R′}. K_F ⊥_K K_W is the registration-layer account of Rovelli's observer-relativity. This is a genuine extension, not a restatement: VVV-QMRF supplies the formal conditions (E1, E6, E7) and the requires_K_joint predicate that Relational QM does not.

---

## 7. Scope, Limitations, and Open Items

### 7.1 What This Paper Does Not Claim

- Does not replace Standard Quantum Mechanics or revise P1–P4.
- Does not revise the Born rule or unitary evolution.
- Does not claim Buddhist epistemology proves quantum mechanics.
- Does not claim K-side incommensurability is experimentally confirmed.
- Does not claim that consciousness plays any role in registration.
- Does not claim the EWF paradox is fully resolved on the ρ-side.
- Does not claim requires_K_joint is a necessary and sufficient condition (sufficient only).

### 7.2 Open Items

| Open item | Location | Status |
|-----------|---------|--------|
| Formal proof of Step 4 (E7 Axiom 2 in K_joint failure proposition) | Section 4.5 | Incomplete |
| Formal definition of ⊥_K as a mathematical relation | Section 4.4 | Proposed definition boundary only; full formalism incomplete |
| Necessary and sufficient characterization of requires_K_joint | Section 4.3 | Sufficient conditions only |
| Prove equivalence of σ(M) and R̂_svasa formalisms | E01 Section 11.5 | Not started |
| Axiomatize K as a full mathematical structure (topology, order) | Section 2.2 | Partial |
| Apply requires_K_joint to Proietti raw count-level data | Section 5.2 | Aggregate level only |
| Apply requires_K_joint to individual LF facet terms in Bong | Section 5.3 | Setting-level only |
| Explicit separability verification for Bong ρ_μ regimes | Section 5.3 | Not done |
| Purpose-designed VVV-QMRF experiment | Section 5.4 | Not done |

### 7.3 Falsification Condition (Restated)

This paper's central prediction is falsified if:

> An Extended Wigner's Friend experiment produces results better modeled by a single joint-registration structure than by K-side incommensurability, for a configuration where requires_K_joint = 1 via Condition A and the empirical regime has sufficient entanglement, visibility, and noise control for LF-level failure to be observable.

In operational terms, this would mean that the data support one registration-layer model in which Conditions 1-6 are jointly satisfiable for both observers with V(M_F)=1 and V(M_W)=1, rather than a model requiring K_F ⊥_K K_W. If that occurs under the stated structural and empirical conditions, E7 Axiom 2 or the proposed `⊥_K` relation requires revision and the K_joint failure proposition does not hold.

---

## References

1. von Neumann, J. (1932). Mathematical Foundations of Quantum Mechanics. Princeton University Press.
2. Bohr, N. (1935). Can Quantum-Mechanical Description of Physical Reality Be Considered Complete? Physical Review 48, 696–702.
3. Heisenberg, W. (1958). Physics and Philosophy. Harper & Row.
4. Wigner, E.P. (1961). Remarks on the mind-body question. In: The Scientist Speculates, Good (ed.), pp. 284–302.
5. Rovelli, C. (1996). Relational quantum mechanics. International Journal of Theoretical Physics 35, 1637–1678.
6. Prasad, H.S. (2023). Buddhist Pramāṇa-Epistemology. Studia Humana 12(1-2), 21–52. DOI: 10.2478/sh-2023-0004.
7. Zurek, W.H. (2003). Decoherence, einselection, and the quantum origins of the classical. Reviews of Modern Physics 75, 715–775.
8. Frauchiger, D. and Renner, R. (2018). Quantum theory cannot consistently describe the use of itself. Nature Communications 9, 3711.
9. Brukner, C. (2018). A no-go theorem for observer-independent facts. Entropy 20(5), 350.
10. Proietti, M. et al. (2019). Experimental test of local observer independence. Science Advances 5(9), eaaw9832. DOI: 10.1126/sciadv.aaw9832.
11. Bong, K.W. et al. (2020). A strong no-go theorem on the Wigner's friend paradox. Nature Physics 16, 1199–1205. DOI: 10.1038/s41567-020-0990-x.
12. Jordan, A.N. and Siddiqi, I.A. (2024). Quantum Measurement Theory and Practice. Cambridge University Press. DOI: 10.1017/9781009103909.

---

*Working Paper v2.0 — VVV-QMRF*
*Submitted to PhilSci Archive for community feedback*
*All formal claims are Class D (proposed) or Class C (conjecture)*
*Falsification condition stated in Section 4.6 and Section 7.3*
*Purpose-designed experiment required for confirmation*
