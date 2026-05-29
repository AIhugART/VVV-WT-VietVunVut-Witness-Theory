# When Does a Physical Interaction Become a Valid Registered Measurement?
## A VVV-QMRF Registration-Layer Extension of Quantum Mechanics with a Testable Prediction for Extended Wigner's Friend Scenarios

**Working Paper v2.0**
**Author:** Viet Nguyen Xuan (VietVunVut)
**Repository:** https://github.com/AIhugART/VVV-QMRF-VietVunVut-Quantum-Measurement-Registration-Framework
**Status:** Working paper submitted for community feedback. All formal claims are Class D (proposed) or Class C (conjecture) unless stated otherwise. Critique is explicitly invited.

---

## Abstract

The quantum measurement problem has remained unresolved for nearly a century. Standard quantum mechanics specifies, via postulate P3, that a measurement of observable A on state |ψ⟩ yields eigenvalue aₖ with probability |⟨aₖ|ψ⟩|². What P3 does not specify is when a physical interaction constitutes a valid registered measurement event. This silence generates the von Neumann chain problem and leaves the Heisenberg cut formally undefined.

This paper proposes VVV-QMRF (VietVunVut Quantum Measurement Registration Framework): a registration-layer extension of quantum mechanics grounded in Buddhist Pramāṇa epistemology (Dignāga–Dharmakīrti tradition). The framework adds a K-side registration space K, separate from the physical Hilbert space H, and proposes a six-condition test for valid registered measurement. Applied to Extended Wigner's Friend (EWF) scenarios, this yields a specific conjecture: K-side registration spaces of two observers are incommensurable (K_F ⊥_K K_W) when a joint registration space K_joint is structurally required but cannot satisfy all six conditions simultaneously.

This conjecture is not trivially true for all frameworks. It separates ordinary Bell-type nonclassicality from LF-level Wigner-friend inconsistency, as illustrated by data from Bong et al. (2020) at μ = 0.80, 0.81 where Bell non-LF violation is reported while Local Friendliness inequalities remain unviolated. Existing data from Proietti et al. (2019) and Bong et al. (2020) are compatible with the proposed structural reading. The framework does not replace Standard Quantum Mechanics, revise the Born rule, or invoke consciousness. All formal claims are classified by evidence level. A purpose-designed experiment with a predefined operational criterion is required for confirmation.

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

**Provisional and final validity (Class D proposed):**

Because E7 permits a later registration act to revise the validity of an earlier act, every validity assignment in K-side is provisional until the registration process closes. Formally:

```
V_prov(M) = 1  iff  M satisfies Conditions 1-5 and no known later act
  has contradicted M within its K-side up to the current registration time.

V_prov(M) may be revised to 0 if a later act M' with valid cross-registration
  authority contradicts M per E7.

V_final(M) = 1  iff  V_prov(M) = 1 and no future registration act within K_R
  will contradict M (a limit property).

For the purposes of requires_K_joint and ⊥_K, provisional validity is the
  operative notion unless stated otherwise.
```

### 2.3 Source: Buddhist Pramāṇa Epistemology

The registration-layer architecture is derived structurally from Buddhist Pramāṇa epistemology (Dignāga, 5th century; Dharmakīrti, 7th century), as systematized by Prasad (2023). Pramāṇa theory addresses the formal conditions under which a cognition constitutes a valid knowledge event. The Buddhist source relation is not used as empirical evidence for quantum mechanics. It functions as a structural source for the registration-layer postulates E1, E6, and E7; the move from Pramāṇa theory to K-side registration is a project-level formal extraction, not an established claim in Buddhist studies. The structural extraction used here concerns:

- **Svasaṃvedana:** Self-certifying cognition — a cognition that certifies its own occurrence without requiring a second-order cognition to validate it. Source for E1.
- **Arthakriyā:** Validity as functional success — a cognition is valid if it enables successful engagement with its object. Source for validity conditions in E7.
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

Standard QM describes both perspectives as valid without providing a formal account of their structural incompatibility. This is where the registration layer offers new structure.

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

**Definition (admissible joint K-side registration space, Class D proposed):**

For two K-side registration structures `A` and `B`, an admissible `K_joint(A,B)` is a proposed K-side registration space that can host both structures under a single validity architecture without changing the validity rules that made either structure valid in its own K-side. Formally:

```
AdmJoint(K_joint; A, B) = 1
  iff  there exist embeddings i_A: A -> K_joint and i_B: B -> K_joint
  such that:
       (i)   i_A and i_B preserve the registered act, outcome, certification,
             registration time/order, and validity status of A and B;
             the embedding respects the internal time-order of each structure
             (if e1 <_A e2 then i_A(e1) <_joint i_A(e2)), and the combined
             order in K_joint is the transitive closure of the two embedded
             orders plus any cross-structure temporal relations implied by
             the shared laboratory history;
       (ii)  self-certification remains intrinsic to each embedded act;
       (iii) the Conditions 1-6 validity test remains satisfied for each
             embedded registration structure;
       (iv)  no later registration-state update required by K_joint invalidates
             either embedded structure while both are still claimed as jointly valid;
       (v)   K_joint does not import an external certifier M' as the source of
             the original self-certification for either side.
```

`K_joint` is therefore not a physical Hilbert space, not an observer's private K-space, and not a mere collection of records. It is a registration-layer candidate for joint validity preservation.

**Definition (requires_K_joint predicate, Class D proposed):**

For two K-side registration structures `A` and `B`, `requires_K_joint(A,B)=1` means that the framework is not merely comparing two private records; it is asking whether both records can support one shared registration-validity claim. Formally:

```
requires_K_joint(A, B) = 1
  iff  A and B are each valid or provisionally valid within their own K-side
  AND  A and B are brought under a shared validity demand D_joint
  AND  D_joint requires both A and B to be assessed as parts of the same
       registration target, history, counterfactual claim, or validity claim
  AND  the truth or validity of D_joint cannot be evaluated while leaving
       A and B in fully independent K-side spaces
  AND  preserving D_joint requires a candidate K_joint in which A and B
       are embedded as jointly valid entries satisfying Conditions 1-6.

requires_K_joint(A, B) = 0
  iff no shared validity demand D_joint is imposed, or D_joint can be
      evaluated without embedding A and B into one candidate K_joint.
```

Formally, `D_joint` is a predicate over pairs of K-side registration structures and a comparison architecture:

```
D_joint(A, B, Arch) ∈ {0, 1}
```

It evaluates to 1 when `Arch` demands that A and B support one shared registration-validity claim. The comparison architecture `Arch` is specified by the experimental design (EWF setup, LF inequality, direct comparison protocol, etc.). `D_joint` is not imposed by any single observer; it is a structural feature of the comparison architecture.

For the EWF case:

```
requires_K_joint(F, W, M_F, M_W) = 1
  iff  k_F = <M_F, o_F, cert_F, t_F, V_F> and
       k_W = <M_W, o_W, cert_W, t_W, V_W>
       are both claimed as valid entries for one laboratory registration
       history, one cross-observer comparison, or one LF-style
       observer-independent fact constraint.
```

Here `D_joint` is the demand that the two K-side structures be jointly valid under one comparison architecture. It is not a demand that both physical interactions be globally identical, and it is not a new physical postulate.

**Operational sufficient conditions for `requires_K_joint = 1`:**

- **Condition A (Wigner interference):** W performs an interference measurement on the laboratory containing F+S. `M_W` registers a superposition description of F+S; `M_F` registers a definite outcome `o_F` for S within the same laboratory registration history. Both claims concern the same registration history but place incompatible K-side validity requirements on that history. -> `requires_K_joint = 1`.
- **Condition B (Direct comparison):** F and W directly compare registration records and a logical contradiction is detectable. -> `requires_K_joint = 1`.
- **Condition B2 (LF observer-independent fact constraint):** an LF inequality or no-go argument requires F-side and W-side outcome claims to be assigned simultaneous cross-observer validity. -> `requires_K_joint = 1`.

**Operational sufficient conditions for `requires_K_joint = 0`:**

- **Condition C (No interference, no comparison):** W does not perform interference measurement on F's laboratory. `K_F` and `K_W` remain causally and inferentially isolated. -> `requires_K_joint = 0`.
- **Condition D (Separable state):** the shared quantum state `|ψ⟩` is separable and `M_F`, `M_W` act on non-overlapping subsystems. -> `requires_K_joint = 0`.
- **Condition E (Independent bookkeeping only):** A and B are stored in the same database, report, or external archive, but no shared validity demand is imposed on their contents. -> `requires_K_joint = 0`.

**Claim class:** D (proposed). The `D_joint` definition gives the necessary-and-sufficient structural core for when a joint K-side check is required. Conditions A-E remain operational sufficient cases and require experiment-specific instantiation.

### 4.4 Formal Definition of K-side Incommensurability

The symbol `⊥_K` denotes a registration-layer incommensurability relation, not a physical contradiction and not an event-level null value. It is defined relative to a proposed joint K-side space.

**Definition (K-side incommensurability relation, Class D proposed):**

Let `A` and `B` be K-side registration structures, where each may be an individual registration act (`M_A`, `M_B`) or an observer-indexed registration space (`K_A`, `K_B`). Let `V_A`, `V_B` be their respective validity conditions, including self-certification, registration order, and non-invalidation constraints. Then:

```
A ⊥_K B
  iff  requires_K_joint(A, B) = 1
  AND  there exists no admissible K_joint such that
       (i) A and B both embed into K_joint,
       (ii) their respective self-certifications are preserved,
       (iii) their respective validity conditions remain satisfied, and
       (iv) no required registration-state update in K_joint invalidates
            either A or B while both are still claimed as jointly valid.
```

For observer-indexed registration spaces, this yields:

```
K_A ⊥_K K_B
  iff  requires_K_joint(K_A, K_B) = 1
  AND  no admissible K_joint preserves both K_A and K_B
       as jointly valid registration spaces under Conditions 1-6.
```

For individual registration acts inside a required joint comparison, use the E7 registered contradiction relation, not the space-level incommensurability symbol. The contradiction relation depends on a comparison context defined as follows:

**Definition (K-side comparison context, Class D proposed):**

A K-side comparison context `C_K` is a minimal shared frame in which two registration acts can be evaluated for compatibility. `C_K` requires:

```
(a) both acts are admitted into the same comparison domain;
(b) both acts are indexed to the same registration target or history;
(c) the comparison does not presuppose that both acts are already jointly valid.
```

`C_K` is strictly weaker than `AdmJoint`: it enables the comparison without requiring that joint validity be preserved. `AdmJoint` requires `C_K` but adds preservation of Conditions 1-6 and validity for both sides.

**Definition (cross-registration authority, Class D proposed):**

In a comparison context `C_K` containing acts `M_earlier` and `M_later`:

```
M_later has valid cross-registration authority w.r.t. M_earlier iff:
  (a) M_later is a valid registered measurement within its own K-side
      (σ(M_later) = 1, V(M_later) = 1 per Conditions 1-6);
  (b) M_later's registration content directly concerns the same
      registration target or history as M_earlier;
  (c) M_later was produced by a measurement act that, within the
      comparison architecture, is structurally required to register the
      state of the same laboratory or composite system that M_earlier
      registered as a subsystem;
  (d) the comparison architecture does not arbitrarily privilege one
      observer's K-side over the other — it only identifies which act
      is later in registration time and whether its content is
      structurally incompatible with the earlier act's content.
```

**Definition (act-level registered contradiction, Class D proposed; grounded in E7):**

```
M_A ⊥ M_B
  iff  M_A and M_B share a K-side comparison context C_K,
       concern the same registration target, history, or validity claim,
       cannot both satisfy the relevant validity conditions there,
       and the later act has valid cross-registration authority
       with respect to the earlier act.
```

Act-level contradiction can support a conclusion that no admissible `K_joint` preserves the relevant K-side spaces, but it is not identical to the space-level relation `K_A ⊥_K K_B`.

**Boundary clauses:**

- `⊥_K` does not assert that either physical event fails to occur on the ρ-side.
- `⊥_K` does not mean that either observer's registered outcome is false within its own K-side.
- `⊥_K` is not equivalent to an event-level registration-null value. If an event fails to enter a valid K-registration domain, that should be written separately as `Null_K(e)` or `R_K(e) = ⊥`, not conflated with `A ⊥_K B`.
- `⊥_K` is a registration-layer relation proposed by VVV-QMRF; it is not a new postulate of Standard Quantum Mechanics.
- `⊥_K` is defined only for K-side structures that are each valid or provisionally valid within their own K-side. If either structure fails admission or is already invalidated within its own K-side, `⊥_K` does not apply; the situation should be described using the relevant single-K-side invalidation language of E7.

### 4.5 K_joint Failure and K-side Incommensurability

**Bridge lemma (D_joint to E7 contradiction, Class D proposed; application status: Class C):**

In an EWF/LF configuration, `D_joint` necessarily instantiates the E7 registered contradiction `M_W ⊥ M_F` when all of the following hold:

```
Bridge_EWF(D_joint; M_F, M_W) = 1
  iff  D_joint requires F-side and W-side registrations to be evaluated
       as jointly valid parts of one laboratory registration history
  AND  M_F registers a definite friend-side outcome o_F
  AND  M_W registers the same laboratory as a coherent superposition
       in which no definite o_F is preserved as a W-side valid claim
  AND  the LF/no-go comparison requires both claims to support one
       cross-observer validity constraint
  AND  no reinterpretation inside the same K_joint can preserve both
       registered contents without changing the validity claim of at
       least one side.

Bridge_EWF(D_joint; M_F, M_W) = 1 -> M_W ⊥ M_F.
```

This bridge is not triggered by mere difference of perspective. It is triggered only when the comparison architecture requires both registrations to support the same cross-observer validity claim.

**Relativization defense and response (Class D proposed):**

A possible objection: could `K_joint` host meta-level facts such as "within `K_F`, `M_F` registered `|h⟩`" and "within `K_W`, `M_W` registered `|Ψ+⟩`" without contradiction? Under this reading, both meta-descriptions are jointly true, and the original registration contents are never directly compared.

This relativization defense is rejected here because `D_joint` demands joint validity of the original registration claims, not meta-descriptions of them. If `K_joint` only hosts relativized meta-descriptions indexed to different K-spaces, it does not satisfy `D_joint`: the LF/no-go constraint requires F's outcome and W's outcome to be assigned simultaneous cross-observer validity as facts about the same laboratory history, not as facts-about-facts whose validity is relativized to different K-side perspectives. Relativizing the contents abandons `D_joint` rather than satisfying it. The bridge is therefore not defeated by second-order redescription.

**Conditional lemma (K_joint failure, Class D proposed; proof audit status: conditional):**

If `requires_K_joint = 1` via `D_joint`, `Bridge_EWF(D_joint; M_F, M_W)=1`, and the later act has valid cross-registration authority with respect to the earlier act, then no admissible `K_joint` exists such that:
- (i) `σ_F(M_F) = 1` holds within `K_joint` [Condition 4 for F]
- (ii) `σ_W(M_W) = 1` holds within `K_joint` [Condition 4 for W]
- (iii) `V(M_F) = 1` and `V(M_W) = 1` simultaneously remain preserved [Condition 5+6 for both]
- (iv) no required registration-state update invalidates either embedded structure while both are still claimed as jointly valid [AdmJoint condition (iv)]

**Proof audit:**

```
Step 1 [E6]: F and W are distinct registering processes R_F and R_W
  with distinct K-side time sequences.

Step 2 [E1, observer-indexed]: σ_F(M_F) = 1 is intrinsic to K_F.
  σ_W(M_W) = 1 is intrinsic to K_W. Both hold independently.

Step 3 [D_joint + Bridge_EWF]: D_joint requires both M_F and M_W to support
  one cross-observer validity constraint. M_F registers o_F as definite.
  M_W registers F+S as coherent superposition with no definite o_F preserved
  as a W-side valid claim. Under Bridge_EWF, the two contents instantiate
  M_W ⊥ M_F inside the required comparison context.

Step 4 [E7 + AdmJoint condition (iv)]: E7 says that if M′ ⊥ M and M′ has
  valid cross-registration authority in the comparison context, then V(M) may be
  revised to 0. Therefore, if Bridge_EWF makes M_W ⊥ M_F a necessary
  registration-state update inside K_joint, then K_joint cannot also satisfy
  AdmJoint condition (iv), which requires that no embedded side be invalidated
  while both are still claimed as jointly valid.

Step 5 [Conditional conclusion]: Under those assumptions, no admissible
  K_joint preserving both K_F and K_W as jointly valid exists.
```

**K-side incommensurability:**

```
K_F ⊥_K K_W
  iff  requires_K_joint = 1
  AND  Bridge_EWF(D_joint; M_F, M_W) = 1
  AND  no admissible K_joint preserves both K_F and K_W as jointly valid
       under Conditions 1-6 and AdmJoint condition (iv).
```

**Claim class of Step 4:** C/D boundary. `Bridge_EWF` is a proposed Class D bridge lemma, but its application to concrete EWF/LF experiments remains Class C until the paper supplies a full semantic proof that no admissible reinterpretation can preserve both claims inside the same `K_joint`, and until operational data criteria are supplied.

### 4.6 The Falsifiable Prediction

VVV-QMRF conjectures:

> In Extended Wigner's Friend experiments, configurations satisfying requires_K_joint = 1 are the natural candidates for LF-level violation, provided the quantum state and measurement settings are strong enough to expose the failure of a single joint registration space. Configurations satisfying requires_K_joint = 0 are predicted not to generate LF-level violation by the K-side registration mechanism alone.

requires_K_joint = 1 is therefore proposed as a necessary registration-layer condition for LF-level contradiction to be exposed, but it is not by itself sufficient for an observed LF inequality violation. Empirical violation also depends on entanglement strength, measurement settings, and experimental noise.

This is not a theorem of Standard Quantum Mechanics and is not yet a necessary-and-sufficient characterization of all LF violations.

**Operational data criterion (ODC_K, Class C proposed):**

`K_joint` is not directly observed by a detector. It is operationally tested through the existence or failure of a joint registration model for the observed EWF/LF probability data.

```
ODC_K(Data, Cfg) = K_joint_exists
  iff  there exists a joint registration model J_K such that:
       (i)   J_K assigns jointly valid entries to the relevant F-side and
             W-side registrations selected by Cfg;
       (ii)  J_K preserves Conditions 1-3, 5, and 6 for each embedded
             registration; Condition 4 (self-certification) is treated as
             a structural postulate satisfied by construction when the
             registering system satisfies the architectural definition
             of a K-side observer (Section 3.3);
       (iii) J_K preserves AdmJoint condition (iv): no required
             registration-state update invalidates either embedded side
             while both are still claimed as jointly valid;
       (iv)  J_K reproduces the observed probability distribution within
             the predeclared statistical tolerance τ;
       (v)   J_K does not reclassify a Bridge_EWF configuration as a merely
             independent bookkeeping case.

ODC_K(Data, Cfg) = K_joint_fails
  iff  Cfg satisfies requires_K_joint = 1 via D_joint and Bridge_EWF,
  AND  no J_K satisfying (i)-(v) fits the observed data within τ.
```

Here `Cfg` is the experimental configuration, including measurement settings, observer roles, and the prior classification of `requires_K_joint`. The tolerance `τ` must be fixed before evaluating the data; otherwise the criterion becomes post hoc.

**Interpretation:** `ODC_K = K_joint_fails` does not mean that Standard QM fails. It means the data do not support one registration-layer joint-validity model preserving both K-side claims under the VVV-QMRF constraints.

**τ sensitivity:** The choice of statistical tolerance `τ` affects the sensitivity of `ODC_K`. A `τ` that is too large risks false-negative `K_joint_fails` conclusions (accepting poor models); a `τ` that is too small risks false-positive `K_joint_fails` conclusions (rejecting models due to experimental noise). Calibration of `τ` requires specification before data collection and should be guided by the experiment's statistical power and expected effect size. This paper does not fix `τ`; it is a parameter to be set by the experimental design.

**Claim class:** C (conjecture). Pending experimental operationalization and verification.

---

## 5. Experimental Contact

### 5.1 What Distinguishes VVV-QMRF from Existing Frameworks

The key asymmetry is this: requires_K_joint = 1 is a necessary but not sufficient condition for LF violation. The quantum state must also be sufficiently entangled for K_joint failure to produce an observable inequality violation. This generates a two-regime structure:

- **Regime 1:** requires_K_joint = 1 AND state weakly entangled → Condition A structurally active, K_joint structurally required, but empirical LF violation may be absent.
- **Regime 2:** requires_K_joint = 1 AND state strongly entangled → K_joint failure is empirically visible as LF violation.

A decoherence-only framework does not distinguish these two regimes at the registration-layer level, because it contains no predicate equivalent to requires_K_joint for separating Bell non-LF violation from LF-level joint-validity failure.

This is not trivially true for all frameworks. It generates an observable expectation: Bell non-LF violation can appear in Regime 1 while LF inequalities remain unviolated, and LF violation appears in Regime 2 when entanglement is sufficient.

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

**VVV-QMRF reading:** The three terms with requires_K_joint = 1 contribute positively to the violated expression. The one term with requires_K_joint = 0 is subtracted. The allocation of Wigner-type and record-readout settings within the aggregate Bell-Wigner expression is compatible with the VVV-QMRF reading. However, the violation belongs to the aggregate S value, not to any single correlator term. This is a term-role interpretation of an aggregate inequality, not a per-configuration experimental confirmation.

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
| μ ≈ 0.87 | First LF violation (Semi-Brukner) | Transition to Regime 2: K_joint failure becomes empirically visible |
| High μ | All categories violated including Genuine LF | Regime 2: x=2/3, y=2/3 Condition A strongly active, K_joint failure fully exposed |

**The asymmetric prediction:** At μ = 0.80, 0.81, Bell non-LF violation appears while LF inequalities remain unviolated. VVV-QMRF accounts for this via the two-regime structure: requires_K_joint = 1 in superobserver settings (Condition A), but the quantum state at this μ value is not sufficiently entangled for K_joint failure to produce LF-level violation. A framework without an explicit analogue of requires_K_joint does not provide this particular registration-layer distinction between Bell-type violation and LF-type joint-validity failure at different μ thresholds.

**Applying requires_K_joint and Bridge_EWF to individual LF facet terms:**

Bong et al. report the LF polytope for N=3, O=2 has 932 facets grouped into 9 inequivalent classes. Five classes are relevant to the VVV-QMRF mapping:

| Facet class | Settings | LF facet? | Bell facet? | `requires_K_joint` per term | `Bridge_EWF` per term | VVV-QMRF reading |
|---|---|---|---|---|---|---|
| Brukner | (1i, 1j) | Yes | Yes | Mixed: (1,1)→0; (1,j),(i,1),(i,j)→1 | (1,1)→0; others→1 | Violation driven by superobserver terms with `requires_K_joint=1` |
| Semi-Brukner | (1i, 23) | Yes | Yes | All terms →1 (no (1,1) term) | All terms →1 (≥1 superobserver per term) | Violation → `K_joint` fails for all contributing terms |
| Bell non-LF | (23, 23) | **No** | Yes | All terms →1 | All terms →1 | Violation is Bell-level; does NOT constitute LF joint-validity failure |
| I3322 | (123, 123) | Yes | Yes | Mixed: (1,1)→0; others→1 | (1,1)→0; others→1 | Mixed; LF violation requires superobserver-contributed terms |
| Genuine LF | (123, 123) | Yes | **No** | Mixed: (1,1)→0; others→1 | (1,1)→0; others→1 | Strongest test: violation → pure LF failure without Bell-analogue support |

**Per-setting-pair Bridge_EWF classification:**

```
Bridge_EWF = 1 for (x∈{2,3}, y=1): Bob reads Debbie → definite outcome.
  Alice superobserver → registers superposition of Debbie's lab → M_Alice ⊥ M_Debbie.
Bridge_EWF = 1 for (x=1, y∈{2,3}): symmetric.
Bridge_EWF = 1 for (x∈{2,3}, y∈{2,3}): both register superpositions of both labs.
Bridge_EWF = 0 for (x=1, y=1): both ask friends; no cross-observer validity conflict.
```

**ODC_K prediction per facet class:**

| Facet class | μ=0.80-0.81 prediction | High-μ prediction | Mechanism |
|---|---|---|---|
| Bell non-LF | `K_joint_fails` (violated) | `K_joint_fails` (violated) | Bell-level; superobserver correlators alone suffice |
| Brukner | `K_joint_exists` (NOT violated) | `K_joint_fails` (violated) | Friend-read terms at low μ preserve at least one J_K |
| Semi-Brukner | `K_joint_exists` (NOT violated) | `K_joint_fails` (violated) | Single-superobserver-side insufficient at low μ |
| Genuine LF | `K_joint_exists` (NOT violated) | `K_joint_fails` (violated) | All-setting joint model preservable at low μ; fails at high μ |

This is the per-facet operationalization of the two-regime structure: at μ=0.80-0.81, Bell non-LF alone is violated because only superobserver-superobserver correlators are strong enough. The mixed-setting LF facets (Brukner, Semi-Brukner, Genuine LF) are not yet violated because the friend-read correlators dilute the joint K-side failure when entanglement is insufficient. As μ increases, the superobserver-contributed terms dominate and the full LF facets become violated.

**Result:** Setting-level, μ-threshold-level, and now per-facet-term-level classification is structurally compatible with the published Bong et al. data. The prediction hierarchy (Bell non-LF violates first, then Semi-Brukner, then Genuine LF) matches the observed μ-threshold ordering. Not yet a facet-level confirmation because the full ODC_K model-fit test (stage 3) has not been performed against the published correlator data.

### 5.4 Operational Use of ODC_K

For existing EWF/LF datasets, `ODC_K` should be applied in three stages:

1. **Configuration classification:** classify each measurement setting or LF facet term as `requires_K_joint = 1` or `0` using `D_joint` and the operational conditions in Section 4.3.
2. **Bridge classification:** for settings with `requires_K_joint = 1`, test whether `Bridge_EWF(D_joint; M_F, M_W)=1` is satisfied by the registration contents required by that setting.
3. **Model-fit test:** attempt to construct a joint registration model `J_K` satisfying Conditions 1-6 and AdmJoint condition (iv), then compare its predicted probabilities with the observed data under a predeclared tolerance `τ`.

A dataset supports the VVV-QMRF conjecture only if the settings classified as `requires_K_joint = 1` and `Bridge_EWF = 1` are precisely the settings where `ODC_K` returns `K_joint_fails`, while settings classified as `requires_K_joint = 0` remain compatible with `K_joint_exists` or require no joint K-side test.

This criterion is stronger than the current aggregate compatibility checks in Sections 5.2-5.3. Those checks show structural compatibility, not confirmation.

### 5.5 Purpose-Designed Experiment Specification (Class C proposed)

The existing-data checks in Sections 5.2–5.3 are compatibility checks, not confirmation. A purpose-designed experiment must vary `requires_K_joint` directly as an independent variable.

**Core design principle:** The same physical platform (photonic EWF) can switch between `requires_K_joint = 0` and `requires_K_joint = 1` by changing only the external observers' measurement settings, while keeping the source, friends, and state identical.

**Platform:** Four-party photonic EWF setup with two friends (Charlie, Debbie, encoded as photon paths) and two superobservers (Alice, Bob), following the Bong et al. (2020) architecture:

- Friend-read setting (x=1 or y=1): external observer reads friend's memory record directly. No interference on friend's laboratory. → `requires_K_joint = 0` (Condition C or E).
- Superobserver setting (x∈{2,3} or y∈{2,3}): external observer performs interference measurement on friend's laboratory. → `requires_K_joint = 1` (Condition A) + `Bridge_EWF = 1`.

**Independent variables:**

| Variable | How varied | Values |
|---|---|---|
| `requires_K_joint` | Measurement setting pairs (x,y) | 0: (x=1, y=1); 1: (x∈{2,3}, y=1), (x=1, y∈{2,3}), (x∈{2,3}, y∈{2,3}) |
| Entanglement strength | State parameter μ ∈ [0,1] | Scan from μ ≈ 0.5 to μ ≈ 1.0 in fine steps (Δμ ≤ 0.05) |

**Dependent variable:** `ODC_K(Data, Cfg)` as defined in Section 4.6. For each (μ, setting-pair) combination:

1. Collect coincident photon counts.
2. Attempt to fit a joint registration model `J_K` satisfying Conditions 1-6 and AdmJoint condition (iv).
3. Compare model fit to data under predeclared tolerance `τ`.
4. Return `K_joint_exists` or `K_joint_fails`.

**Predeclared tolerance τ:** Must be fixed before data collection. Recommended: χ² goodness-of-fit test at α = 0.05, or Bayesian model comparison with predeclared prior and Bayes factor threshold.

**Predicted outcome (two-regime structure):**

| μ range | (x=1,y=1) `requires_K_joint=0` | (x∈{2,3}, y∈{2,3}) `requires_K_joint=1` | (mixed) `requires_K_joint=1` |
|---|---|---|---|
| Low μ (< 0.80) | `K_joint_exists` | `K_joint_exists` | `K_joint_exists` |
| Mid μ (0.80–0.87) | `K_joint_exists` | `K_joint_fails` (Bell non-LF) | `K_joint_exists` (LF not yet violated) |
| High μ (> 0.87) | `K_joint_exists` | `K_joint_fails` | `K_joint_fails` (LF violated) |

The critical test is the mid-μ regime: Bell non-LF violation appears while LF inequalities remain unviolated. This is the Regime 1 → Regime 2 transition that a decoherence-only framework does not predict as a registration-layer distinction.

**Falsification (any one suffices):**

1. A setting with `requires_K_joint = 1` and `Bridge_EWF = 1` yields `ODC_K = K_joint_exists` at any μ where the corresponding LF inequality is independently violated.
2. A setting with `requires_K_joint = 0` yields `ODC_K = K_joint_fails`.
3. The predicted μ-hierarchy (Bell non-LF first, then Semi-Brukner, then Genuine LF) is inverted or absent.

**Claim class:** C (conjectural experiment specification). The specification is derived from the Class D formal chain but has not been peer-reviewed as an experimental protocol. Implementation requires an experimental collaboration with access to a photonic EWF platform.

### 5.6 Overall Condition 3 Status

Both Proietti et al. (2019) and Bong et al. (2020) are compatible with the VVV-QMRF conjecture. This is an existing-data compatibility check, not confirmation. The experiment specification in Section 5.5 defines what a confirmation-level test requires.

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
- Does not claim requires_K_joint is a necessary-and-sufficient condition for all LF violations; it is proposed only as a necessary registration-layer condition for the K-side mechanism described here.

### 7.2 Formal Phase Summary and Open Items

The `⊥_K` formal definition chain is now complete at the proposed level (Class D/C). Each dependent layer has a registry-level definition and a working paper location:

| Formal layer | Symbol | Class | Defined in |
|---|---|---|---|
| K-side incommensurability | `⊥_K` | D | Section 4.4 |
| Admissible joint K-space | `K_joint` / `AdmJoint` | D | Section 4.3 |
| Joint-validity demand | `D_joint` / `requires_K_joint` | D | Section 4.3 |
| E7 registered contradiction | `M′ ⊥ M` | D | E7 framework §3b; Section 4.4 |
| Bridge lemma | `Bridge_EWF` | D/C | Section 4.5 |
| Operational data criterion | `ODC_K` | C | Section 4.6 |
| LF facet-term classification | — | C | Section 5.3 |

**Deferred proof items (not required for current claim class):**

| Deferred item | Reason deferred |
|---|---|
| Full semantic proof for `Bridge_EWF` | Requires formal semantics of "no admissible reinterpretation"; paper currently uses operational sufficient conditions |
| Full formal proof for `⊥_K` as a mathematical relation | Requires axiomatized K-space (topology, order); paper currently uses registration-layer structural definition |
| `AdmJoint` necessary-and-sufficient conditions | Currently sufficient conditions A-E; full characterization requires completed K-space axiomatization |
| Equivalence of `σ(M)` and `R̂_svasa` formalisms | Separate research track (E01 §11.5) |
| Axiomatize K as a full mathematical structure | ~~Long-term architectural task; not needed for current Class C/D claims~~ → Addressed 2026-05-19: K1-K7 core axioms + T1-T4 bridge theorems formalized in `documents/research_documents/meta_architecture/K_Space_Axiomatization.md` (VVV-QMRF §K-AXIOM v1.3). Layer 1 (K1-K7) frozen; Layer 2 (T1-T4) pending Level 4 freeze. Concrete model (minimal EWF, 2 observers) completed: K1-K7 consistency verified, Level 4 derivation chain verified, T2 proof attempt done with 3 gaps (EP, relativization, Level 4 ⊥ freeze). |

**Next-step operational items (required for confirmation):**

| Next item | Current status | Priority |
|---|---|---|
| Purpose-designed VVV-QMRF experiment | Section 5.5 | Class C experiment specification completed; requires experimental collaboration for implementation |
| `ODC_K` stage 3 model-fit test on published correlator data | Section 5.3 — classification done; fit not performed | High — would upgrade from structural compatibility to quantitative test |
| Apply `requires_K_joint` to Proietti raw count-level data | Section 5.2 — aggregate level only | Medium |
| Explicit separability verification for Bong `ρ_μ` regimes | Section 5.3 — not done | Medium |

### 7.3 Falsification Condition (Restated)

This paper's central conjecture is falsified if:

> An Extended Wigner's Friend experiment produces results consistent with a single K_joint registration model satisfying Conditions 1–6 for both observers simultaneously, for a configuration independently classified as requires_K_joint = 1 via D_joint and Bridge_EWF.

Operationally, this requires a predefined data criterion connecting observed probabilities to the existence of such a joint registration model. If `K_joint` exists empirically, E7 Axiom 2 or the Step 4 conditional bridge requires revision, and the `K_joint` failure proposition does not hold.

### 7.4 Architectural Constraints of the K-side/ρ-side Separation

The core architectural commitment of VVV-QMRF is `K ≠ H`: the registration layer is structurally distinct from the physical layer (Section 2.1). This separation is what enables the framework to address the registration layer gap. It also imposes two architectural constraints that are not fixable by refinement — they are inherent consequences of the layer separation, not oversights.

**Constraint 1 — Self-certification is not a ρ-side observable.** Condition 4 requires `σ_R(M) = 1` to be determined intrinsically within `K_R`. This cannot be a ρ-side observable because any physical measurement of `σ` would itself require a second-order registration act, re-entering the von Neumann regress that E1 is designed to terminate. Making `σ` directly testable from ρ-side data would collapse the K-side back into the ρ-side and remove the framework's reason for existing. The operational compromise is stated in `ODC_K` condition (ii): self-certification is treated as a structural postulate satisfied by construction when the registering system meets the architectural definition of a K-side observer. What is tested is not whether `σ = 1`, but whether — given that assumption — the full joint registration model can reproduce the observed data.

**Constraint 2 — `D_joint` is a framework-level classification, not a physical observable.** The predicate `D_joint(A, B, Arch)` classifies whether a comparison architecture demands joint validity. Experimental architectures are designed and described in the language of Standard QM plus assumptions (O, L, F, AOE, NSD); they do not carry intrinsic VVV-QMRF labels. The bridge from physical setup to K-side predicate is therefore interpretive. This does not make `D_joint` arbitrary: operational sufficient conditions A–E (Section 4.3) connect observable features of the setup (interference vs. readout, comparison vs. no comparison, separable vs. entangled state) to `D_joint` values in a reproducible way. But the mapping is a VVV-QMRF classification of the experimental architecture, not a measurement of a physical quantity.

**These constraints are typical of the measurement problem, not unique to VVV-QMRF.** Every interpretation or extension of quantum mechanics that addresses measurement must introduce a primitive concept that is not directly observable within the formalism:

| Framework | Central concept | Why not directly observable |
|---|---|---|
| Copenhagen | Classical apparatus / Heisenberg cut | No formal definition of what makes an apparatus classical |
| Many-Worlds (Everett) | Branching of worlds | No physical observable distinguishes one branch from another |
| QBism | Agent's degree of belief | Subjective probability is not a physical quantity |
| Relational QM (Rovelli) | Facts relative to observer | Relata are only defined within the relation |
| Objective Collapse (GRW) | Collapse mechanism | Collapse events are postulated, not yet detected |
| **VVV-QMRF** | **Self-certification / `D_joint`** | **K-side properties are not ρ-side observables (`K ≠ H`)** |

This is not a methodological coincidence. If the measurement problem could be resolved using only concepts that are directly observable within the standard physical formalism, it would not have remained open for nearly a century. The presence of an unobservable primitive in every listed framework reflects the depth of the problem, not a defect unique to any one proposal.

The presence of architectural constraints does not distinguish VVV-QMRF from existing frameworks. What distinguishes it is that the constraints are explicitly named, traced to a single architectural commitment, and given operational bridges (`ODC_K`, conditions A–E) that define what can and cannot be tested under the current formalism.

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
*Experiment specification in Section 5.5; requires experimental collaboration for implementation*
