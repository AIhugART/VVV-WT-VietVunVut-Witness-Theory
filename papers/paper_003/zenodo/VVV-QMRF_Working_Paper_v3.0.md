Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# When Does a Physical Interaction Become a Valid Registered Measurement?
## A VVV-QMRF Registration-Layer Framework with the K9_E Class C Testable Hypothesis and an Experimental Specification for Extended Wigner's Friend

**Working Paper v3.0** *(promoted from draft 2026-05-28 — all phases P1-P7 complete)*
**Author:** Viet Nguyen Xuan (VietVunVut)
**Affiliation:** Independent Researcher, Vietnam
**Contact:** viet@vvvqmrf.com | https://vvvqmrf.com
**Repository:** https://github.com/AIhugART/VVV-QMRF-VietVunVut-Quantum-Measurement-Registration-Framework
**Date:** 2026-05-28
**Status:** Working paper. All formal claims are Class D (proposed) or Class C (conjecture/qualified) unless stated otherwise. Critique is explicitly invited.
**Plan reference:** `papers/paper_003/VVV-QMRF_Working_Paper_v3.0_plan.md`
**Base version:** v2.0 (`papers/Testable_Prediction_Section/.../VVV-QMRF_Working_Paper_v2.0.md`)

> **DISCLAIMER:** VVV-QMRF is independent personal research, not Standard Quantum Mechanics, not peer-reviewed, and not experimentally confirmed. K9_E (P9) is classified **Class C (qualified)**: structurally testable but empirically unconfirmed. Evidence is real but ambiguous; noise as an alternative explanation cannot be ruled out (v30 noise sensitivity analysis FAIL). Confirmation or rejection requires a purpose-designed K9-S12 photonic Extended Wigner's Friend experiment. VVV-QMRF does not replace Standard QM, revise the Born rule, or invoke consciousness. Full boundary protocol: `DISCLAIMER.md`. Formal definitions: `documents/research_documents/project_vvv_qmrf_class_c/06_references/VVV_QMRF_Definitions.md`.

---

## Abstract

Standard quantum mechanics specifies, via postulate P3, that a measurement of observable A on state |ψ⟩ yields eigenvalue aₖ with probability |⟨aₖ|ψ⟩|². What P3 does not specify is *when* a physical interaction constitutes a valid registered measurement event. This silence generates the von Neumann chain problem — every measuring apparatus becomes entangled with the system it measures, with no postulate indicating where this chain terminates — and leaves the Heisenberg cut formally undefined.

This paper proposes VVV-QMRF (VietVunVut Quantum Measurement Registration Framework): a registration-layer extension of quantum mechanics grounded in Buddhist Pramāṇa epistemology (Dignāga–Dharmakīrti tradition). The framework introduces a K-side registration space K, structurally separate from the physical Hilbert space H (K ≠ H), and proposes a six-condition test for valid registered measurement. These six conditions formalize when a physical interaction crosses from the ρ-side into the K-side as a self-certified, validity-bearing registration event. Applied to Extended Wigner's Friend (EWF) scenarios, this yields the K-side incommensurability conjecture: K_F ⊥_K K_W holds when a joint registration space K_joint is structurally required but cannot satisfy all six conditions simultaneously for both observers.

The K-side registration space is axiomatized via eight frozen registration-logic axioms (K1–K8, Layer 1) and nine updatable bridge theorems (T1–T9, Layer 2). K1 defines the K-state carrier set (five-tuple: M, o, cert, t, V); K2 imposes a strict total temporal order; K3 formalizes self-certification; K4 assigns default validity; K5 governs invalidation and cross-registration contradiction; K6 defines cross-registration authority; K7 formalizes registration process closure (provisional → final validity); K8 guarantees validity preservation under cross-space embeddings. Layer 2 extends this structure with bridge theorems T1–T9, including K5_prospective (a conservative pre-instantiation evaluation mode required for probability assignment), K7_trace (a closure transition record), and D_enc (a transition-encoding semantic definition). T4-H — the N-observer colimit existence hypothesis — has been verified as a full theorem across all four steps (RCA 4.74/5, 2026-05-28), upgrading the three-observer prediction to Class C.

K9_E is the probability postulate (Postulate P9) motivated by the K-space architecture. It is not a theorem derivable from K1–K8 alone — the core axioms define structural properties (registration, validity, incommensurability) but do not uniquely determine a probability rule. K9_E fills this gap as P9: P(o|K) = Tr(E_o ρ) · (1 − β·K_ctx), where β ∈ [0,1] is a single free parameter and K_ctx is the fraction of contextual observer registrations in prospective incommensurability with the current registration. At β = 0, K9_E reduces exactly to the Born rule. Six of the eight terms in K9_E are entirely new concepts not present in Standard QM. The proposed experimental specification (K9-S12 Modified Bong Protocol — single waveplate at angle α = 31°) predicts Genuine LF 1 = +0.0891 (8.6σ), δ⟨A₁B₂⟩ = −0.0355 (20.8σ), and figure of merit FOM = 8.6; this proposal was submitted to arXiv as a separate experimental child paper (paper_002, 2026-05-27).

**Empirical status (Class C qualified):** A genuine non-circular fit to raw Proietti et al. (2019) data yields β = 0.598, visibility V = 0.939, Δχ² = 5.35 (2.31σ) in favor of K9_E over quantum mechanics with uniform visibility. However, a v30 noise sensitivity analysis returned FAIL: the noise threshold for evidence robustness is 0.10 σ RMS (well below the 3.0 σ threshold for PASS). Random noise at any magnitude produces Δχ² ≥ 5.35 in approximately 50% of realizations due to K9_E's directional sensitivity and the small sample of four data points. The A0B0 setting alone drives 80% of the Δχ² improvement. The 2.31σ signal reflects model flexibility, not confirmed physical suppression. Adversarial tests (4/4 PASS) and operationalizability gates (3/3 PASS) confirm K9_E's structural robustness, but empirical confirmation remains open and requires the K9-S12 photonic EWF experiment with dedicated noise characterization.

This paper presents three logically independent projects under a one-way motivation chain. **Project A** (BE↔QM Comparative Mapping) provides a 30-node, 39-edge comparative framework between Buddhist Pramāṇa epistemology and quantum measurement — an interpretive framework that motivated the registration-layer architecture but does not itself constitute evidence for that architecture. **Project B** (VVV-QMRF Conceptual Framework) develops the formal K-space axiomatization (K1–K8, Layer 1 frozen) and bridge theorem suite (T1–T9, Layer 2 updatable), including the conjectured structure-preserving map φ: K → B(H) with necessary conditions N₁–N_T (Class D supporting conjecture). **Project C** (K9_E Testable Hypothesis) is the scientifically falsifiable claim: the K9_E probability postulate (P9) produces predictions structurally different from Standard QM (δ_S ≠ 0 when β > 0), avoids the Frauchiger–Renner paradox via K5 V_prov mechanism, and is falsifiable via the K9-S12 Modified Bong Protocol. A→B→C is a one-way motivation chain, not a logical derivation. A null K9_E result falsifies Project C but does not invalidate Projects A or B.

VVV-QMRF does not replace Standard Quantum Mechanics. It does not revise postulates P1–P4 or the Born rule (K9_E recovers Born exactly at β = 0). It does not invoke consciousness. It does not claim Buddhist epistemology proves quantum mechanics. All formal claims are classified by evidence level; classification criteria are stated in the project's formal definitions document. Falsification requires a photonic EWF experiment with the K9-S12 single-waveplate protocol or equivalent. Critique is explicitly invited.

---

## 1. The Registration Layer Gap

### 1.1 What Quantum Mechanics Specifies

Standard quantum mechanics is built on four postulates:

- **P1 (State):** A physical system is represented by a density operator ρ ∈ D(H).
- **P2 (Observables):** Physical quantities are represented by self-adjoint operators A on H.
- **P3 (Measurement):** Measurement of A on state |ψ⟩ yields eigenvalue aₖ with probability |⟨aₖ|ψ⟩|², after which the state updates to the corresponding eigenstate.
- **P4 (Dynamics):** Between measurements, the state evolves unitarily via the Schrödinger equation.

P3 specifies what outcome appears and with what probability. P3 does not specify when a physical interaction counts as a measurement, what structural conditions distinguish a measurement from a non-measurement interaction, or what stops the measurement chain. This is the registration layer gap.

### 1.2 The Von Neumann Chain Problem

Von Neumann (1932) observed that if apparatus A1 measures system S, A1 becomes entangled with S. If apparatus A2 then measures A1, A2 becomes entangled with A1+S. No postulate of standard QM specifies where this chain terminates. Decoherence (Zurek 2003) explains why superpositions become effectively classical at the macroscopic scale, but it does not explain when a physical interaction constitutes a registration event in the sense of a definite recorded outcome. The von Neumann chain problem is a registration-layer problem, not a decoherence problem.

### 1.3 The Heisenberg Cut

Copenhagen quantum mechanics (Bohr 1935; Heisenberg 1958) assigns measurement authority to "the classical apparatus" without formally defining what makes an apparatus classical, why it has registration authority, or what structural conditions produce a definite outcome. VVV-QMRF addresses both problems by introducing a registration layer K, separate from the physical layer ρ, and proposing formal conditions for valid registration events within K. The K1–K8 axioms (§4) formalize this registration layer structurally.

---

## 2. The K-side Registration Space

### 2.1 Layer Separation

VVV-QMRF introduces a strict separation between two layers:

- **Physical layer (ρ-side):** Physical states, observables, and dynamics as described by Standard QM. This layer is not modified.
- **Registration layer (K-side):** The space of registration events, recording conditions, and validity states. K ≠ H. K-side structure does not alter ρ-side dynamics.

### 2.2 Minimal K-state

A registration event is represented by a minimal K-state tuple:

```
k = ⟨M, o, cert, t, V⟩
```

The K-side registration space K is the collection of such tuples produced by a registering system R over time. Section §4 formalizes this minimal K-state as the K1–K8 axiom set.

### 2.3 Source: Buddhist Pramāṇa Epistemology (Project A)

The registration-layer architecture is structurally derived from Buddhist Pramāṇa epistemology (Dignāga, 5th century; Dharmakīrti, 7th century). The structural extraction concerns: **Svasaṃvedana** (self-certifying cognition, source for K3), **Arthakriyā** (validity as functional success, source for K4/K7), and **Anumāna/Pratyakṣa** (inference and perception as distinct registration modes). This is Project A: a comparative interpretive framework. Project A motivates Project B via one-way structural inspiration; it does not constitute empirical evidence for the K-space architecture or K9_E.

---

## 3. The Valid Registered Measurement Test

### 3.1 The Six Conditions

**Interaction X is a valid registered measurement for registering system R if and only if:**

```
Condition 1 (Physical):    X occurs at the physical ρ-side.
Condition 2 (Admission):   X is admitted into K-side as M_X for system R.
Condition 3 (Process):     M_X ∈ R ordered by registration time.          [K2, E6]
Condition 4 (Self-cert):   σ_R(M_X) = 1 intrinsically within K_R.         [K3, E1]
Condition 5 (Validity):    V(M_X) = 1 by default upon admission.           [K4, E7]
Condition 6 (Non-invalid): No later M′ revises V(M_X) to 0.               [K5, K7, E7]
```

The cert and V fields are formalized as K3 (self-certification) and K4/K5/K7 (default validity and invalidation) in §4.

### 3.2 The K-side Stopping Proposition

**Proposition (Class D proposed):** If Conditions 1–6 hold for M_X, no further K-side registration act is required to certify M_X. The von Neumann registration regress terminates at M_X on the K-side without modifying ρ-side dynamics. Condition 4 (self-certification) provides the formal property that Copenhagen assigns to "classical apparatus" without definition.

### 3.3 Observer-Indexed Self-Certification

For multi-observer scenarios: σ_R(M) = 1 iff M occurred as a K-side registration event of R, determined intrinsically within K_R, not by any M′ ≠ M and not by any R′ ≠ R. The independence σ_F(M_F) ⊥ σ_W(M_W) is formalized in K3 (§4.1).

---

## 4. K-Space Architecture: Axioms K1–K8 and Layer 2

This section presents the formal axiomatization of the K-side registration space. The axioms and bridge theorems are the structural backbone of VVV-QMRF and the foundation on which K9_E (§5) and the EWF incommensurability result (§6) rest.

> **Scope boundary (v2.4 §0.6 audit):** The K-space axiomatization in this section is **purely structural**. It contains zero probability equations, zero numerical values, and zero experimental data. K9_E (§5) is a separate probability postulate (P9) that is **not derivable from K1–K8 alone** — the axioms define structural properties (registration, validity, incommensurability) but do not uniquely determine a probability rule. Data fitting (§7) is a separate empirical analysis. This three-layer separation is architectural: K1–K8 (structure) → K9_E (postulate) → data fitting (empirical).

The authoritative peer-synced source is `documents/research_documents/meta_architecture/K_Space_Axiomatization.md` (canonical) and `documents/research_documents/project_vvv_qmrf_class_c/01_axiomatization/K_Space_Axiomatization.md` (working copy), both v2.4.

### 4.1 Layer 1 (Frozen): Axioms K1–K8

Layer 1 contains eight registration-logic axioms whose text is frozen unconditionally. K1–K4 and K8 carry no Level 4 semantic dependencies. K5, K6, and K7 have conditional semantic dependencies on Level 4 scope (when they fire / when closure occurs) but their text is frozen regardless of Level 4 changes.

| Axiom | Name | Core function | BE lineage | Class |
|---|---|---|---|---|
| **K1** | Carrier Set | K_R = set of 5-tuples k = ⟨M, o, cert, t, V⟩; cert = 1 for all k ∈ K_R (admission invariant); t-injectivity: distinct events have distinct timestamps | Pramāṇa — cognition as structured event: act, object, self-awareness, result, validity | C |
| **K2** | Temporal Order | (K_R, <_R) is strict total order (chain): k₁ <_R k₂ iff t(k₁) < t(k₂); discrete: no K-side registration identity between consecutive events | Kṣaṇabhaṅgavāda — momentariness; registration time is discrete within K_R | D |
| **K3** | Self-Certification | cert(k) = σ_R(M) ∈ {0,1} determined intrinsically within K_R; independent of any R′ ≠ R; observer-indexed independence | Svasaṃvedana — self-certifying cognition: a cognition certifies its own occurrence without a second-order cognition | D |
| **K4** | Default Validity | V(k) = 1 upon instantiation for ¬isNull(k); V(k) = 0 for null events (isNull: o = ∅ ∧ ΔI = 0); V is provisional until K7 closure | Svataḥ prāmāṇya — intrinsic validity by default; arthakriyā (causal efficacy) | D |
| **K5** | Invalidation | V(k₁) → 0 iff ∃k₂ later in K2 order, k₂ ⊥ k₁ in shared C_K, k₂ has Auth(K6); fires only when requires_K_joint = 1; pre-closure reversible, post-closure absolute | Parataḥ prāmāṇya — invalidity detected extrinsically; bādhaka pramāṇa | D |
| **K6** | Cross-Reg. Authority | Auth(k₂ → k₁, C_K) = 1 iff: both in same C_K; V(k₂) = 1; k₁ ∈ scope(D_joint); non-transitive across distinct C_K | Bādhaka pramāṇa — a contradicting cognition must itself be a valid pramāṇa | D |
| **K7** | Closure | R closes at t_close when no pending requires_K_joint demands remain; V_prov → V_final; post-closure: no new k, K5 irreversibility absolute, no new D_joint | Niścaya (ascertainment) — a cognition becomes determinate at cognitive closure | D |
| **K8** | Embedding Preservation | For embedding i: K_R → K_X: V_X(i(k)) = V_R(k) at t_embed; all five fields preserved; post-embedding V evolves under K_X's K4–K7 | Anugama — continuity: validity accompanies a cognition into a broader context | D |

**Note on K1 claim class:** K1 is classified C because the K-state tuple definition is shared with the K9_E postulate (which is Class C); K1 provides K9_E's domain. K2–K8 remain Class D as structural axioms without empirical content.

### 4.2 K5_prospective: Conservative Pre-Instantiation Evaluation Extension

K9_E requires assessing incommensurability *before* an outcome is registered — to compute the suppression factor f_perp(o) = P(K5 fires prospectively on hypothetical outcome o). K5's standard post-hoc mode (modifying V of an actual tuple) is not designed for this. K5_prospective is a **conservative extension** that adds a new evaluation target while preserving K5's identical conditions (i)–(iii):

```
K5 (post-hoc):     V(k₁) → 0 iff ∃k₂: k₁ <_R k₂ ∧ k₂ ⊥ k₁ ∧ Auth(k₂→k₁)
                   Target: actual k₁ ∈ K_R.    Effect: V_prov modified.

K5_prospective:    K5 fires on k_o* iff ∃k_prev: k_prev <_joint k_o*
                     ∧ k_o* ⊥ k_prev ∧ Auth(k_o*→k_prev)
                   Target: hypothetical k_o* = ⟨M*, o, cert=1, t*, V=1⟩.
                   Effect: contributes to f_perp(o) in K9_E only.
```

**Same conditions (i)–(iii). Same structural logic. Different target and effect.** K5_prospective does NOT modify V of any actual tuple in K_R. It has no operational role outside K9_E. This conservative extension was upgraded from "semantic extension" to an explicit axiom-level clause in v29 (2026-05-23, 3-Round RCA Round 2 score 4.90/5), resolving assumption [A-E1] through the T9 construction theorem.

**Claim class:** C (conservative extension of K5; same conditions; new evaluation mode only).

### 4.3 Layer 2 (Updatable): Bridge Theorems T1–T9

Layer 2 bridge theorems connect K1–K8 to the framework's operational definitions (Level 4 predicates: D_joint, requires_K_joint, Bridge_EWF, ODC_K). Layer 2 is updatable independently of K1–K8.

| Theorem | Name | Core function | Class | Status |
|---|---|---|---|---|
| **T1** | K_joint Construction | K_joint exists as categorical colimit of embedding diagram when requires_K_joint = 1; order = transitive closure of embedded orders + cross-temporal relations | D | Pending L4 freeze |
| **T2** | ⊥_K Derivation | K_A ⊥_K K_B iff requires_K_joint = 1 ∧ no admissible K_joint; traced to K5 conflict (V_prov forced to 0 in candidate K_joint) or K7 lock | D | Pending L4 freeze |
| **T3** | Bridge_EWF | Bridge_EWF = 1 derivable from K5 in EWF: M_F registers definite o_F; M_W registers same lab as superposition; no reinterpretation preserves both without changing validity claim; conditional on AJVS | D/C | Pending L4 freeze |
| **T4** | N-Observer Colimit | K_joint(R₁,...,R_N) exists as colimit for N ≥ 2 when pairwise AdmJoint + global commutativity hold; ⊥_K non-transitive in general | D | **T4-H THEOREM 4/4 (2026-05-28)** |
| **T5** | K_joint Associativity | K_joint(K_joint(A,B),C) ≅ K_joint(A,B,C) as K1–K8-preserving isomorphism; conditional on T4-H | D | T4-H resolved; L4 freeze pending |
| **T6** | Decoherence Update | Decoherence-induced ρ-side change produces K-side registration-state update when Conditions 1–6 hold | D | Updatable |
| **T7** | IRB Scope Propagation | Intrinsic Relational Binding (entanglement) between R_i and R_j induces requires_K_joint = 1 under specific conditions | D | Updatable |
| **T8** | K5_prospective Frequency Bridge | f_perp = E[I(K5_prospective fires)] = fraction of K_ctx with prospective ⊥; derives K9_E suppression term structurally; eliminates assumption [A-E2] | C | Structural derivation from K5p |
| **T9** | K_ctx Construction | K_ctx = {φ_ij(k_j) ∈ K_joint : k_j ∈ K_{R_j}, requires_K_joint = 1, temporally compatible}; φ_ij = canonical K8-constrained T1 embedding; eliminates [A-E1] via 5 lemmas (L1-L5) | C | L1–L5 proven |

**T4-H THEOREM (4/4, 2026-05-28, RCA 4.74/5):** All four steps verified:
- Step 1: C_{K-space} satisfies category axioms (identity, composition, associativity).
- Step 2: K_colim = (∐_i K_i)/~ constructed; all five fields well-defined via lexicographic t-assignment and embedding-time V snapshot; 5/5 verification gates PASS.
- Step 3: K1–K8 preserved through quotient construction via T-PRES Lemma + T-REP Corollary (K2 acyclicity resolved) + V monotone dynamics.
- Step 4: Universal property verified: u([k,i]) := f_i(k) is well-defined (diagram compatibility + T-REP), K8-preserving, and unique.

T4-H is no longer a hypothesis. T4 conclusions hold for all N ≥ 2. The three-observer prediction (§10) is upgraded from Class C-conditional to Class C. T1 (N=2 constructive) remains independently valid without invoking the colimit universal property.

### 4.4 K7_trace and D_enc: Canonical Layer 2 (v2.4, 2026-05-27)

**K7_trace — Closure Transition Record:** A conservative extension of K7. Defines Δ_closure(k) := V_prov(k) − V_final(k) at t_close. Records the transition magnitude (0 or 1) without modifying V or creating new tuples. Claim class: C-canonical. Promoted from BB-VVV local origin to canonical Layer 2 by RCA 4.77/5.

**D_enc — Transition-Encoding Registration Act:** A semantic definition (parent: K7_trace). Enc(M_aware, k_F) = 1 iff o(M_aware) depends counterfactually on Δ_closure(k_F). Pattern: same as K5_prospective (binary classification of hypothetical act). Claim class: C-canonical.

**Four canonical consumers of K7_trace (cross-validation of architectural status):**

| Consumer | Usage | Status |
|---|---|---|
| T_BB V3 Step 1 (BB-VVV) | Δ_closure as V_prov substitute post-closure (Baumann-Brukner 2024) | §9.1 — T_BB Class C conditional |
| D_enc | Parent for Enc predicate | Canonical Layer 2 |
| 3-OBS hierarchical registration transition | T4-H THEOREM unlocks Class C upgrade for 3-observer prediction | §10 — Class C (2026-05-28) |
| FR-VVV avoidance chain Step 2 | Frauchiger-Renner K5→K6→V=0 path; K7_trace scenario-agnostic across B&B and FR | §9.2 — V_FR2 PASS (2026-05-28) |

The four-consumer canonical status confirms K7_trace is an architectural element, not a single-use construct.

### 4.5 K-Space and Buddhist Pramāṇa: One-Way Motivation, Not Empirical Evidence

The BE lineage entries in §4.1 record the structural inspiration for each axiom. This is Project A's role in VVV-QMRF: a one-way motivation from Pramāṇa theory's analysis of valid cognition to K-space's analysis of valid registration.

**What this does NOT mean:**
- Buddhist epistemology does not prove K1–K8.
- K1–K8 are not derived from Buddhist texts; they are derived from the registration-layer problem posed by Standard QM.
- Project A's 30-node, 39-edge BE↔QM comparative mapping is a separate independent project (see §12.3 for the A→B→C independence statement).
- A result that falsifies K9_E does not falsify Buddhist epistemology, the BE↔QM mapping, or the K-space architecture.

---

## 5. K9_E: Probability Postulate (P9)

> **ERRATUM note (from Phase 8 source document, 2026-05-23):** This section was formerly titled "K9_E Formal Derivation." K9_E is **NOT derived from K1–K8**. It is a **POSTULATE** — a probability assignment rule motivated by K-space structure (⊥_K, K_ctx) but not uniquely determined by K1–K8 axioms. This distinction is load-bearing: the entire §5 must be read as proposing P9, not proving it.

### 5.1 Why K1–K8 Alone Do Not Determine a Probability Rule

The eight axioms of Layer 1 define the structural properties of the K-side registration space: what tuples are admitted (K1), how they are ordered (K2), how self-certification works (K3), how default validity is assigned (K4), how cross-registration contradiction fires (K5), what counts as authority for invalidation (K6), when the registration process closes (K7), and how validity is preserved under embedding (K8).

Nowhere in K1–K8 is there a formula that maps K-state tuples to real-valued probabilities. The axioms determine:

- *Which* registration events are valid (cert = 1, V = 1)
- *When* one event invalidates another (K5 conditions)
- *How* events embed across K-spaces (K8)

They do not determine *how much probability* to assign to each outcome. Multiple distinct probability functions are consistent with the K1–K8 structure. In particular, the Born rule P(o) = Tr(E_o ρ) is consistent with K1–K8 (with β = 0, the K-space constraints are satisfied trivially). But so is any function that respects the V-gate (V = 0 → no probability), the isNull-gate (isNull(k) → no probability), and normalizes over the outcome space.

K9_E fills this gap by adding a specific probability assignment rule as **Postulate P9**, motivated by the K-space incommensurability structure (K5_prospective, T8, T9) but not derivable from it. This is analogous to how the Born rule P3 in Standard QM is an irreducible postulate of the theory — it is not derivable from P1 (state), P2 (observables), or P4 (dynamics).

### 5.2 The K9_E Equation

**Postulate P9 (K9_E Probability Postulate):**

```
P(o | k_i, Exp) = Tr(E_o ρ_i) · [1 − β · f_perp(o, k_i, K_ctx)]
                  ─────────────────────────────────────────────────
                                    Z_E(k_i)

where:
  f_perp(o, k_i, K_ctx) = |{k_j ∈ K_ctx : K5_prospective fires on k_o* vs k_j}|
                           ────────────────────────────────────────────────────────
                                              |K_ctx|

  K_ctx(k_i, Exp) = {φ_ij(k_j) ∈ K_joint : k_j ∈ K_{R_j},
                     requires_K_joint(R_i, R_j) = 1,
                     temporally compatible with k_i}        [T9]

  Z_E(k_i) = Σ_{o'} Tr(E_{o'} ρ_i) · [1 − β · f_perp(o')]  [normalization]

  β ∈ [0, 1)  — single free parameter (suppression strength)
```

**Born rule limit (exact, not approximate):**

K9_E reduces to the Born rule exactly under any of the following equivalent conditions:

```
P(o|k) = Tr(E_o ρ)   iff any of:

  (i)   β = 0                  [suppression OFF — K-space has no effect on P]
  (ii)  K_ctx = ∅              [no contextual observers — f_perp undefined → 0 by convention]
  (iii) f_perp(o) = 0 ∀ o     [all outcomes compatible — no prospective K5 firing]
  (iv)  Single observer N=1   [implies K_ctx = ∅ → (ii)]
```

For condition (i): β = 0 → [1 − 0·f_perp] = 1 for all o → Z_E = Σ Tr(E_o ρ) = 1 → P = Tr(E_o ρ). Standard single-observer laboratory experiments have N = 1 (condition iv) and therefore K9_E is observationally equivalent to Standard QM in all non-EWF contexts.

### 5.3 Eight-Term Provenance: What Is New in K9_E

K9_E assembles eight structural components. Six of these eight terms are entirely new concepts not present in Standard QM. This table records the provenance of each term — it is a traceability record, not a derivation proof.

| # | Term | Definition | Source | In Standard QM? |
|---|---|---|---|---|
| T1 | `Tr(E_o ρ_i)` | Born rule probability (POVM formulation) | **Standard QM** | ✅ |
| T2 | `β` | Suppression strength, β ∈ [0,1) | **Free parameter** — the single adjustable parameter of K9_E; analogous to coupling constants (α, G, g) in physics | ❌ **NEW** |
| T3 | `f_perp(o, k_i, K_ctx)` | Fraction of contextual registrations prospectively incommensurable with outcome o | **K5_prospective + T8** — structural derivation from binary K5/K6 primitives (T8-H1: fraction form is uniquely forced) | ❌ **NEW** |
| T4 | `C(o_i, o_j)` | Compatibility map: 1 if outcomes are QM-orthogonal (incompatible), 0 otherwise | **K-space construction** from ρ_joint at setup, stored as K-side lookup | ❌ **NEW** |
| T5 | `K_ctx(k_i, Exp)` | Set of contextual K-states from other observers via T9 morphism + temporal compatibility | **T9 + K2** — K_ctx is a theorem, not an assumption (L1–L5 in T9) | ❌ **NEW** |
| T6 | `Z_E(k_i)` | Normalization: Σ_{o'} Tr(E_{o'} ρ_i)·[1−β·f_perp(o')] | Modified from QM (Standard QM auto-normalizes; K9_E suppression breaks auto-normalization, requiring explicit Z) | ⚠️ **MODIFIED** |
| T7 | `V(k) = 0 → no P` | Bhrānti gate: invalid registrations receive no probability | **K4 + K5 → PP-1 v2** — grounded in BE concept bhrānti (erroneous cognition) | ❌ **NEW** |
| T8 | `isNull(k) → no P` | Anupalabdhi gate: null events (o = ∅, ΔI = 0) receive no probability | **K4 isNull guard** — grounded in BE concept anupalabdhi (non-apprehension) | ❌ **NEW** |

**Summary:** Of eight terms in K9_E: 1 from Standard QM (T1: Born rule), 1 modified from QM (T6: normalization), **6 entirely new** (T2–T5, T7, T8). The four original K9_E construction assumptions ([A-E1]–[A-E4]) are fully resolved: [A-E1] ELIMINATED (T9, 5 lemmas), [A-E2] ELIMINATED (T8/T8-H1), [A-E3] RECLASSIFIED as free parameter β, [A-E4] BE-anchored. **Net: 0 orphaned assumptions, 1 free parameter (β).**

### 5.4 K9_E Is a Postulate, Not a Theorem

**This is the most important boundary statement in this section.**

K9_E is **Postulate P9** — a proposed probability assignment rule added to the VVV-QMRF framework alongside K1–K8. It is not derivable from K1–K8 alone. The axioms define structural properties (registration, validity, incommensurability) but do not uniquely determine a probability rule.

The relationship between K1–K8 and K9_E is the same as the relationship between P1, P2, P4 (state, observables, dynamics) and P3 (Born rule) in Standard QM: the structural postulates define the mathematical space, but the probability rule is an additional postulate with its own empirical motivation.

**What K1–K8 do:** Define the K-space structural constraints (carrier, order, certification, validity, invalidation, authority, closure, embedding). Supply the structural vocabulary used in K9_E (K5_prospective, T8, T9). Constrain the form of a probability rule (V-gate via T7, isNull-gate via T8), but do not determine β or the specific suppression formula.

**What K9_E adds:** A specific probability assignment rule P(o|K) with a single free parameter β. The suppression term f_perp is structurally motivated by K5_prospective incommensurability and formally derived (via T8, T9) to have the fraction form — but the *presence* of the suppression term (i.e., that β ≠ 0 in nature) is a postulate, not a derivation.

**Consequence:** K9_E is falsifiable (β = 0 recovers Born exactly; any measured β ≠ 0 confirms K9_E; K9-S12 protocol provides the definitive test). K1–K8 are not individually falsifiable — they are structural definitions of the registration layer.

### 5.5 Distinguishability from Standard QM

When β > 0, K9_ctx ≠ ∅, and f_perp is outcome-dependent, K9_E produces predictions structurally different from Standard QM.

**Distinguishability condition:** δP(o) = P_{K9E}(o) − Tr(E_o ρ) ≠ 0 iff ALL of:

```
  (I)   β > 0
  (II)  K_ctx ≠ ∅   (requires_K_joint = 1 for at least one observer pair)
  (III) ∃ o, o' : f_perp(o) ≠ f_perp(o')
```

Condition (III) is critical: if f_perp is constant across outcomes, the suppression factor [1 − β·f_perp] is a uniform multiplier that cancels in the normalized ratio P/Z_E → Tr(E_o ρ). This is the PP-2 v2 cancellation insight: K9_E must suppress *differentially* across outcomes to produce an observable signal.

In EWF scenarios with Bell-State Measurement (BSM), the compatibility map C(o_F, o_W) is outcome-dependent (some (o_F, o_W) pairs are compatible, others are incommensurable), producing outcome-dependent f_perp and therefore a genuine δP ≠ 0.

**Theoretical magnitude (CHSH, β = 0.5):** δ_S = −0.055. This is a *theoretical* value — the predicted deviation in the CHSH parameter for Proietti-type 2-observer EWF. At β = 0.9, δ_S = −0.179 (≈ 2.4σ detection horizon). No empirical detection of δ_S has been achieved to date. See §7 for empirical status.

**3-observer amplification (Class C, T4-H THEOREM):** The 3-observer K_ctx is larger, producing an amplification factor of approximately 11× relative to 2-observer. Predicted δ_M3 = −0.223 at β = 0.3 (illustrative, conditional only on K9_E postulate P9 — T4-H is now THEOREM, §10).

### 5.6 Projects B and C Are Independent Claims

The φ-map conjecture (§11, Project B) and K9_E (Project C) are logically independent:

**Project B (φ-map):** Conjectures the existence of a structure-preserving map φ: K → B(H). Derives necessary conditions N₁–N_T. Provides φ-conditional scope boundaries for existing QM interpretations. This conjecture is Class D and concerns the *formal relationship* between K-space and the algebra of bounded operators. It does not make testable predictions about measurement statistics.

**Project C (K9_E):** Proposes a probability postulate P9 with a single free parameter β. Makes testable predictions (K9-S12). Can be confirmed or falsified by experiment. K9_E's empirical status is entirely independent of whether φ exists.

**Independence in both directions:**
- A proof that φ: K → B(H) exists (or does not exist) would not confirm or falsify K9_E.
- A K9-S12 experimental confirmation of K9_E (β ≠ 0 measured) would not prove φ exists.
- A K9-S12 null result (β = 0 measured) would falsify K9_E but would not falsify the φ-map conjecture or the K-space architecture.

This independence is architectural: Project B concerns the structural embedding of K into H; Project C concerns the probability assignment within K. They share the K-space vocabulary (K1–K8, T1–T9) but their claims are logically disjoint.

---

## 6. Extended Wigner's Friend and K-side Incommensurability

### 6.1 The Extended Wigner's Friend Setup

In the Extended Wigner's Friend scenario (Frauchiger and Renner 2018; Brukner 2018), two observer pairs interact with a shared quantum system:

- **Friend F** measures quantum system S inside a sealed laboratory. From F's perspective, a definite outcome o_F is recorded: σ_F(M_F) = 1.
- **Wigner W** models the entire laboratory (F + S) as a unitarily evolving quantum state, then performs an interference measurement M_W on F's laboratory.

Standard QM describes both perspectives as valid without providing a formal account of their structural incompatibility. This is where the registration layer offers new structure.

### 6.2 Applying the Six Conditions to Each Observer

**Friend F:**
```
X_F → M_F ∈ R_F         [Condition 3, K2]
σ_F(M_F) = 1             [Condition 4, K3]
V_F(M_F) = 1             [Condition 5, K4]
No M′ contradicts M_F    [Condition 6, K5/K7]
→ M_F is a valid registered measurement within K_F.
```

**Wigner W:**
```
X_W → M_W ∈ R_W         [Condition 3, K2]
σ_W(M_W) = 1             [Condition 4, K3]
V_W(M_W) = 1             [Condition 5, K4]
No M′ contradicts M_W    [Condition 6, K5/K7]
→ M_W is a valid registered measurement within K_W.
```

Both observers satisfy the six conditions independently within their own K-sides. The question is whether a joint registration space K_joint can contain both K_F and K_W as jointly valid entries.

### 6.3 The requires_K_joint Predicate

**Definition (admissible joint K-side registration space, Class D proposed):**

```
AdmJoint(K_joint; A, B) = 1
  iff  there exist embeddings i_A: A → K_joint and i_B: B → K_joint such that:
    (i)   embeddings preserve act, outcome, cert, registration time/order, validity;
    (ii)  self-certification remains intrinsic to each embedded act;
    (iii) Conditions 1-6 remain satisfied for each embedded structure;
    (iv)  no required registration-state update in K_joint invalidates either embedded
          structure while both are still claimed as jointly valid;
    (v)   K_joint does not import an external certifier as source of self-certification.
```

**Definition (requires_K_joint predicate, Class D proposed):**

```
requires_K_joint(A, B) = 1
  iff  A and B are each valid or provisionally valid within their own K-side
  AND  A and B are brought under a shared validity demand D_joint
  AND  D_joint requires both to be assessed as parts of the same registration target,
       history, counterfactual claim, or validity claim
  AND  truth of D_joint cannot be evaluated while leaving A and B in fully independent K-sides
  AND  preserving D_joint requires a K_joint in which A and B are jointly valid.

requires_K_joint(A, B) = 0
  iff  no shared D_joint is imposed, or D_joint can be evaluated without embedding A and B
       into one candidate K_joint.
```

**Operational sufficient conditions for requires_K_joint = 1:**

- **Condition A (Wigner interference):** W performs an interference measurement on F's lab; M_W registers a superposition description while M_F registers a definite outcome for the same lab. → requires_K_joint = 1.
- **Condition B (Direct comparison):** F and W directly compare records and a logical contradiction is detectable. → requires_K_joint = 1.
- **Condition B2 (LF constraint):** An LF inequality requires F-side and W-side claims to have simultaneous cross-observer validity. → requires_K_joint = 1.

**Operational sufficient conditions for requires_K_joint = 0:**

- **Condition C (No interference, no comparison):** W does not perform interference on F's lab. → requires_K_joint = 0.
- **Condition D (Separable state):** Shared state is separable; M_F and M_W act on non-overlapping subsystems. → requires_K_joint = 0.
- **Condition E (Independent bookkeeping):** Records stored together but no joint validity demand imposed. → requires_K_joint = 0.

### 6.4 Formal Definition of K-side Incommensurability

**Definition (K-side incommensurability relation ⊥_K, Class D proposed):**

```
A ⊥_K B
  iff  requires_K_joint(A, B) = 1
  AND  there exists no admissible K_joint such that:
       (i)   A and B both embed into K_joint,
       (ii)  their respective self-certifications are preserved,
       (iii) their respective validity conditions remain satisfied, and
       (iv)  no required registration-state update in K_joint invalidates
             either A or B while both are still claimed as jointly valid.
```

**Definition (K-side comparison context C_K):** A minimal shared frame in which two registration acts are evaluated for compatibility. C_K requires: (a) both acts admitted into the same comparison domain; (b) both indexed to the same registration target; (c) comparison does not presuppose joint validity. C_K is strictly weaker than AdmJoint.

**Definition (cross-registration authority):** In C_K, M_later has valid cross-registration authority w.r.t. M_earlier iff: (a) both belong to same C_K; (b) V(M_later) = 1; (c) M_later's content directly concerns the same registration target as M_earlier; (d) the comparison architecture does not arbitrarily privilege one observer.

**Boundary clauses:**
- ⊥_K does not assert that either physical event fails to occur on the ρ-side.
- ⊥_K does not mean either observer's outcome is false within its own K-side.
- ⊥_K is not equivalent to a registration-null event Null_K(e).
- ⊥_K applies only when both sides are valid/provisionally valid within their own K-sides.

### 6.5 K_joint Failure and K-side Incommensurability

**Bridge lemma (Class D proposed; application status: Class C):**

```
Bridge_EWF(D_joint; M_F, M_W) = 1
  iff  D_joint requires F-side and W-side registrations to be evaluated as jointly valid
       parts of one laboratory registration history
  AND  M_F registers a definite friend-side outcome o_F
  AND  M_W registers the same laboratory as coherent superposition (no definite o_F as W-side claim)
  AND  LF/no-go comparison requires both claims to support one cross-observer validity constraint
  AND  no reinterpretation inside K_joint preserves both without changing the validity claim
       of at least one side.

Bridge_EWF(D_joint; M_F, M_W) = 1 → M_W ⊥ M_F.
```

**Relativization defense (rejected):** A relativized K_joint hosting only meta-descriptions ("within K_F, M_F registered |h⟩") does not satisfy D_joint. D_joint requires joint validity of the *original* registration claims, not meta-descriptions of them. Relativizing the contents abandons D_joint rather than satisfying it.

**Conditional lemma (K_joint failure, Class D proposed):** Under requires_K_joint = 1, Bridge_EWF = 1, and valid cross-registration authority, no admissible K_joint exists such that σ_F(M_F) = 1, σ_W(M_W) = 1, V(M_F) = 1, and V(M_W) = 1 simultaneously hold. K_F ⊥_K K_W follows. **Claim class of Step 4:** C/D boundary — conditional on full Bridge_EWF semantic proof.

### 6.6 The Falsifiable Prediction and ODC_K

VVV-QMRF conjectures that configurations satisfying requires_K_joint = 1 are the natural candidates for LF-level violation when the quantum state is sufficiently entangled.

**Operational data criterion (ODC_K, Class C proposed):**

```
ODC_K(Data, Cfg) = K_joint_fails
  iff  Cfg satisfies requires_K_joint = 1 via D_joint and Bridge_EWF,
  AND  no joint registration model J_K satisfying:
       (i)   jointly valid F-side and W-side registrations,
       (ii)  Conditions 1-3, 5, 6 preserved (Condition 4 by construction),
       (iii) AdmJoint condition (iv): no required invalidation while both are jointly claimed,
       (iv)  observed probability distribution reproduced within predeclared tolerance τ,
       (v)   not reclassifying a Bridge_EWF config as mere independent bookkeeping.
```

τ must be fixed before data collection; ODC_K is sensitive to the choice of τ.

**Compatibility checks with existing data:**

*Proietti et al. (2019):* The three correlators with requires_K_joint = 1 (⟨A₁B₁⟩, ⟨A₁B₀⟩, ⟨A₀B₁⟩) contribute positively to the violated expression S = 2.407; the one term with requires_K_joint = 0 (⟨A₀B₀⟩) is subtracted. This allocation is structurally compatible. The VVV-QMRF reading is a term-role interpretation of an aggregate inequality, not a per-configuration experimental confirmation.

*Bong et al. (2020):* Two-regime structure:

| μ regime | Reported result | VVV-QMRF reading |
|---|---|---|
| μ = 0.80-0.81 | Bell non-LF violated; LF inequalities NOT violated | Regime 1: requires_K_joint = 1 active, entanglement insufficient for LF failure |
| μ ≈ 0.87 | First LF violation (Semi-Brukner) | Transition Regime 1 → 2 |
| High μ | All categories violated including Genuine LF | Regime 2: K_joint failure exposed |

**Per-facet μ-threshold ODC_K prediction:**

| Facet class | μ=0.80-0.81 | High-μ |
|---|---|---|
| Bell non-LF | K_joint_fails (violated) | K_joint_fails (violated) |
| Brukner | K_joint_exists (not violated) | K_joint_fails (violated) |
| Semi-Brukner | K_joint_exists (not violated) | K_joint_fails (violated) |
| Genuine LF | K_joint_exists (not violated) | K_joint_fails (violated) |

The prediction hierarchy (Bell non-LF first, then Semi-Brukner, then Genuine LF) matches the observed μ-threshold ordering. **Not yet a facet-level confirmation** — full ODC_K stage 3 model-fit test has not been performed. These are compatibility checks.

### 6.7 Connection to K1–K8 and K5_prospective

The Level 4 formalism of §6.1–6.6 can now be traced directly to Layer 1 axioms via the K-space architecture (§4):

**requires_K_joint = K5 precondition:**

```
requires_K_joint(A, B) = 1
  ⟺  K5 firing precondition met: comparison context C_K exists
  ⟺  D_joint imposes a shared validity demand on K_F and K_W
     (K5 formal block: "fires only when requires_K_joint = 1")
```

K5 does not fire in isolation — it fires only when there is a joint validity demand. The requires_K_joint = 0/1 distinction in §6 is precisely the K5 precondition distinction in Layer 1. Every operational sufficient condition A–E for requires_K_joint maps to whether K5's precondition is met.

**Bridge_EWF = K5_prospective evaluation:**

```
Bridge_EWF(D_joint; M_F, M_W) = 1
  ⟺  K5_prospective fires on hypothetical k_o* vs k_prev = k_F:
     — k_F <_joint k_o*         [K2 temporal order in K_joint from T1]
     — k_o* ⊥ k_F within C_K   [K5 registered contradiction, minimal ⊥ definition]
     — Auth(k_o* → k_F, C_K) = 1  [K6 authority]
```

Bridge_EWF = 1 means exactly that K5_prospective would fire if W's hypothetical registration k_o* were realized — the structural bridge between Level 4 formalism and Layer 1 axioms. This is the connection exploited by T8 to derive f_perp (§5.3).

**K7_trace and K_joint failure:** When K_F ⊥_K K_W is established, K7_trace records Δ_closure(k_F) := V_prov(k_F) − V_final(k_F). The four canonical consumers of K7_trace (§4.4, §9.3) all derive from this same closure event in structurally distinct EWF scenarios.

---

## 7. Empirical Status (Class C Qualified)

**Classification:** K9_E = **Class C (qualified)** — structurally testable, empirically **UNCONFIRMED**. Evidence is real (a genuine non-circular fit shows 2.31σ improvement over QM-uniform-visibility) but ambiguous (noise at any magnitude produces an equivalent improvement in ~50% of realizations). Confirmation or rejection requires the K9-S12 purpose-designed photonic EWF experiment.

### 7.1 D1 Proietti: Genuine Non-Circular Fit

**Version history (critical):** The Phase 10 data fitting document (2026-05-23) identified a *circular fit* error in the earlier Phase 10 analysis: the "data" used were reconstructed as E_exp = V_exp · E_QM, mathematically guaranteeing β = 0 as the best-fit result (a tautology, not an empirical finding). The v29 analysis (2026-05-23) replaced this with a **genuine non-circular fit** using raw correlator values extracted directly from Proietti et al. (2019) Figure 3 (`Wigner_figure_3.md` SOT document).

**Genuine fit results (raw Proietti Figure 3 data):**

| Quantity | Value | Meaning |
|---|---|---|
| β (best-fit) | **0.598** | K9_E suppression parameter at genuine fit |
| V (visibility, fitted) | **0.939** | Higher than circular-fit V = 0.854; non-uniform visibility detected |
| χ²/DOF | 0.670 (DOF = 2) | Good fit quality, p = 0.51 |
| Δχ² (K9_E vs QM-uniform-V) | **5.35** | K9_E improves fit over QM with uniform visibility |
| σ-significance | **2.31σ** | Marginal detection level |

**Why the raw data differs from reconstructed data:** The raw Proietti Figure 3 correlator values (e.g., A0B0 = −0.678) differ substantially from reconstructed values (−0.604 in the circular-fit analysis). The non-uniform pattern across the four correlators is what drives the genuine-fit improvement — when K9_E's directional suppression is applied, it preferentially reduces some correlators (those with high requires_K_joint = 1 contribution) over others (requires_K_joint = 0), producing a better fit than a uniform-visibility model.

**Two K9_E model variants co-exist** with different calibration paths:
- **Additive model** (`utils/k9e_predictor.py`): E = E_QM · [1 − β·n_BSM·g_ctx], g_ctx ≈ 0.039 (from theoretical δ_S = −0.055 at β = 0.5).
- **Multiplicative model** (`proietti_raw_fit.py`): E = E_QM · [1 − β·g_eff]^n_BSM, g_eff = 0.146 (from PP-4 sanity check). Produces larger suppression; used for genuine fit.

The two models agree at first order in β·g but diverge for β > 0.3.

### 7.2 v30 Noise Sensitivity Analysis: FAIL

The v30 noise sensitivity analysis (P10-NOISE, 2026-05-24) asked: *How large must non-uniform noise be to produce Δχ² ≥ 5.35 by chance?*

**Result:** **FAIL.** The noise threshold is 0.10 σ RMS — far below the 3.0 σ threshold required for PASS.

| Metric | Value | Interpretation |
|---|---|---|
| Noise threshold (2σ, B4 Monte Carlo) | **0.10 σ RMS** | Noise at ANY magnitude produces Δχ² ≥ 5.35 in ~50% of realizations |
| PASS threshold | 3.0 σ RMS | Threshold for "noise ruled out" |
| Verdict | **FAIL** (0.10 << 3.0) | Non-uniform noise cannot be ruled out as explanation |
| Single-setting fragility (B2) | **1.85 σ at A0B0** | Only a 1.85σ shift at A0B0 eliminates K9_E advantage |
| A0B0 contribution to Δχ² | **80%** | Nearly the entire K9_E "signal" is driven by one data point |

**What this means:** The 2.31σ signal reflects **model flexibility** (K9_E has one more degree of freedom than QM-uniform-visibility), not confirmed physical K9_E suppression. With only 4 correlator values and K9_E's directional sensitivity, random noise at any magnitude produces a Δχ² ≥ 5.35 improvement approximately half the time. The genuine fit improvement is real but not distinguishable from a noise artifact with current data.

**Why this downgraded K9_E from "genuine" to "qualified":** The v29 upgrade to Class C (genuine) was based on three conditions: (1) genuine non-circular fit, (2) K5_prospective axiom upgrade, (3) T4-H Step 1. Conditions (2) and (3) remain valid. Condition (1) still holds as a genuine fit, but the noise analysis reveals that the fit evidence is insufficient to rule out noise. The v30 P10-NOISE FAIL downgraded the empirical sub-condition from "real evidence" to "real but ambiguous evidence." Class C structural qualification is unchanged; the (genuine) → (qualified) downgrade concerns the empirical confidence level only.

**Methodology rationale (conservative):** The noise analysis was designed to ERR ON THE SIDE OF CAUTION — a Type I error (falsely claiming noise is ruled out) is fatal to project credibility; a Type II error (correctly noting that noise cannot be ruled out) is recoverable via the K9-S12 experiment.

### 7.3 K9E-PAT: CLOSED as UNRESOLVABLE

**Open item K9E-PAT** asked whether the K9_E multiplicative suppression pattern (predicted 2BSM/1BSM ratio ≈ 2) is confirmed by Proietti data.

**Result:** **CLOSED as UNRESOLVABLE (v31 RCA 4.92/5).**

The empirical 2BSM/1BSM ratio of −0.78 is not a meaningful test of the K9_E pattern:

1. The ratio −0.78 is computed from A0B1 + A1B0 avg = −0.0235 divided by A1B1 = +0.0179 — both are sub-σ residuals (consistent with zero).
2. The ratio of two near-zero numbers carries no physical information about suppression structure.
3. Both K9_E model variants predict suppression ratio ≈ 2: additive (2.000 exactly), multiplicative (1.913). The predicted value ≈ 2 is not discriminating for current data quality.
4. P10-NOISE already established that 4 data points are insufficient to test any pattern — A0B0 alone drives 80% of Δχ².

The path to pattern confirmation is K9-S12: an alpha-sweep protocol (QWP angle 0°–90°) with N = 91,000 events and dedicated noise characterization, providing direct 2BSM/1BSM comparison with sufficient statistics.

### 7.4 Adversarial Tests (4/4 PASS) and Operationalizability Gates (3/3 PASS)

Despite the empirically qualified status, K9_E passes all structural validity tests:

**Adversarial tests (4/4 PASS — Phase 9):**
1. Born limit recovery: β = 0 → P = Tr(E_o ρ) exactly (verified analytically and numerically).
2. Single-observer reduction: N = 1 → K_ctx = ∅ → K9_E = Born (verified).
3. V-gate (Bhrānti): V = 0 events receive no probability (verified).
4. isNull-gate (Anupalabdhi): null events (o = ∅) receive no probability (verified).

**Operationalizability gates (3/3 PASS — G1/G2/G3, all 5.0/5):**
- G1: K9_E is operationally distinguishable from Standard QM (δ_S ≠ 0 when β > 0 and K_ctx ≠ ∅): PASS.
- G2: K9_E has a predeclared falsification condition (K9-S12 protocol, §8): PASS.
- G3: K9_E's free parameter β is measurable in principle (Proietti-type EWF experiment): PASS.

**Important boundary:** Adversarial tests and operationalizability gates confirm that K9_E is *structurally consistent and testable*. They do not confirm it is empirically correct. The 4/4 PASS result establishes that K9_E is a well-formed scientific hypothesis; the P10-NOISE FAIL establishes that current empirical evidence is insufficient to confirm it.

---

## 8. K9-S12 Modified Bong Protocol

This section summarizes the experimental specification for the first dedicated test of the K9_E probability postulate. The full protocol is presented in the experimental child paper (paper_002, arXiv submitted 2026-05-27). Section §8 provides the VVV-QMRF-level framing; the photonic implementation details are in paper_002.

### 8.1 The Equatorial Gap: Why No Prior Test Exists

**Proposition 1 (Equatorial Cancellation Theorem, paper_002 §3):** Every published optical EWF experiment — Proietti et al. (2019) and Bong et al. (2020) — used Superobserver measurement settings at the Bloch sphere equatorial plane (θ = π/2). At θ = π/2, the squared basis overlaps |⟨b|d⟩|² = 1/2 for all outcome pairs (b, d). This makes the overlap-dependent suppression factor f_perp constant across all outcomes — the suppression cancels in the normalization Z_E and P_K9E reduces exactly to the Born rule. This is not a special property of K9_E; it holds for **any** overlap-only deformation of the form P′ = P_QM · g(|⟨b|d⟩|²) / Z.

**Consequence:** Both published optical EWF experiments are geometrically blind to the entire overlap-only class of deformations, including K9_E. No published experiment has varied the polar angle θ. The K9-S12 protocol is the first proposal to break this fixed point.

**Signal structure:** The K9_E signal δ⟨AB⟩(θ) vanishes identically at θ = π/2 and is generically non-zero otherwise:

```
f_perp(+1, H) − f_perp(−1, H) = −cos θ                           [Eq. 11, paper_002]

At θ = π/2:  cos(π/2) = 0  →  f_perp constant  →  δ⟨AB⟩ = 0     [equatorial null]
At θ = 31°:  cos(31°) ≈ 0.857  →  f_perp outcome-dependent  →    [non-zero signal]
             δ⟨AB⟩ ≠ 0 for β > 0
```

This vanishing-at-equator structure is a **genuine observable** (Lemma 1, paper_002 §3.2): it cannot be eliminated by any unitary relabeling of the Superobserver's measurement basis.

### 8.2 Single-QWP Design and Predictions

**Experimental modification:** A single quarter-wave plate (QWP) is re-inserted into the Bong et al. (2020) apparatus, tilting the Superobserver measurement from θ = π/2 to θ = 31°. No other hardware change is required. N = 91,000 coincidences per setting (same as Bong 2020).

**Why θ = 31° (near-optimal):** Grid search over θ ∈ [0°, 90°] shows θ = 35° yields FOM = 8.8 vs. 8.6 at θ = 31°. The broad plateau means the exact optimum is non-critical: θ = 31° is near-optimal, not uniquely optimal (paper_002 v94 update). The key criterion is that θ ≠ π/2 — any angle away from the equator probes the signal.

**Quantitative predictions at θ = 31° (exact numerical computation):**

| Observable | Prediction | Significance | Role |
|---|---|---|---|
| Gen LF 1 (Genuine LF Facet 1) | **+0.0891** | **8.6σ** | Confirms LF violation is preserved at θ = 31° |
| δ⟨A₁B₂⟩ = ⟨A₁B₂⟩_{θ=31°} − ⟨A₁B₂⟩_{θ=π/2} | **−0.0355** | **20.8σ** | Core K9_E signal — non-zero iff K9_E with β > 0 |
| Minimum detectable β at 5σ | **0.07** | — | Search sensitivity |
| Figure of Merit (FOM) | **8.6** | — | Combined LF + K9_E signal |

**Scope boundary (paper_002 §2.3):** These predictions assume the overlap-only class (Level 0). The experiment tests whether nature exhibits overlap-dependent deformation; it does not test the full K9_E framework. Broader deformation classes (Level 1: density-matrix-dependent; Level 2: multi-partite; Level 3: non-geometric) lie outside Proposition 1's scope and require independent experimental designs.

**Loophole status:** Under fair-sampling (η ≈ 0.87), K9-S12 is a **loophole-open screening test**. A positive result (δ⟨A₁B₂⟩ ≠ 0 at θ = 31°) requires independent verification including θ-sweeps (paper_002 §8.2). A null δ⟨AB⟩ across a full θ-sweep would falsify the overlap-only class.

**Falsification conditions:** K9_E (overlap-only class) is falsified if δ⟨AB⟩ = 0 at θ = 31° within predeclared statistical tolerance, confirmed by θ-sweep.

### 8.3 Why IBM Quantum Was Rejected

The IBM Quantum approach to K9_E testing was evaluated and rejected (v31 RCA 4.92/5) on the basis of a **double category error**:

**Error 1 (registration structure):** K9_E requires a K-space registration structure — tuples k = ⟨M, o, cert, t, V⟩ with K3 self-certification (cert = 1 intrinsic), K4 default validity (V = 1 upon admission), K5 invalidation (V → 0 via cross-registration contradiction), and K7 closure (V_prov → V_final). Gate-model QPUs implement unitary circuits with binary qubit states. There is no concept of a K-side registration tuple, K_R carrier set, or validity field V ∈ {0,1} on a QPU. K-space does not exist as a computational object on IBM Quantum hardware.

**Error 2 (EWF scenario):** K9_E specifically requires an Extended Wigner's Friend configuration — a Friend observer registering a definite outcome within a sealed laboratory, and a Superobserver performing an interference measurement on the entire Friend+system composite. Gate-model circuits simulate quantum evolution but do not implement the structural architecture of multiple registering systems with K_joint construction and cross-registration authority. The "Friend" and "Superobserver" roles in K9_E are K-space structural roles, not qubit register labels.

**Conclusion:** K9_E's testable predictions are predictions about photonic EWF statistics. Only an optical EWF apparatus implementing the K9-S12 protocol (or equivalent) constitutes a valid test platform.

### 8.4 Relationship to paper_002

paper_002 ("Have Optical Wigner's Friend Experiments Been Blind to a Geometric Degree of Freedom?") was submitted to arXiv 2026-05-27 as an independent experimental child paper. The VVV-QMRF framing in §8.1–8.3 provides the K-space motivation for the experimental protocol; the photonic implementation details, statistical analysis, and Supplemental materials are in paper_002.

paper_002 is self-contained as a physics paper: it presents the Equatorial Cancellation Theorem (Proposition 1) and single-waveplate protocol without requiring the VVV-QMRF K-space framework. The K9_E postulate (§5) provides one theoretical motivation for the overlap-dependent deformation parameter β; paper_002 frames β as a phenomenological search parameter analogous to Standard Model Extension (SME) coefficients.

---

## 9. Connections to Baumann-Brukner and Frauchiger-Renner

This section documents how two specific papers in the EWF literature connect to VVV-QMRF's K-space structure. These are **Layer 4 (Class D) structural compatibility assessments** — they show that VVV-QMRF's machinery can be applied to the scenarios in these papers, not that the papers empirically confirm K9_E.

### 9.1 Baumann & Brukner (2024): T_BB Class C Conditional

**Paper reference:** Baumann, V. and Brukner, Č. (2024). "Wigner's friend as a rational agent." [arXiv reference; fit plan source: `09_Fitting_Baumann_Brukner/BB_VVV_fit_plan.md` v1.4]

**Scenario:** A Friend F measures a quantum system inside a sealed lab; a Wigner W performs either a coherent (interference) measurement or a projective (read-out) measurement on the lab. B&B show that a rational agent (W) cannot consistently assign memory to F after a coherent measurement — the "no-awareness" result.

**VVV-QMRF compatibility analysis (BB_VVV_compatibility_section.md v2.1):**

| Verification | Status | Finding |
|---|---|---|
| V1: K5 ↔ B&B q₀₀ < 0 condition | ⚠️ **PARTIAL (F4 triggered)** | R_BB (near-readout, x ≈ 0) ≠ R_K5 (interference, x ≈ π/4). B&B's no-valid-joint-model fires near readout; K5 fires at interference. Structurally **different failure modes** — not mathematically equivalent. F4 finding: at x = π/4 (maximum interference), q₀₀ = 0.5 > 0 always, while requires_K_joint = 1 and K5 fires. |
| V2: K7 closure ↔ B&B memory change Δp | ✅ **PASS** | K7 closure magnitude Δp = \|1 − 2α²\| · sin²(2x) / 2 matches B&B memory change with identical functional form. Verified at 5 test points including readout (x≈0), maximal interference (x=π/4), and transition region. |
| T_BB (Option A) | ✅ **Class C (conditional)** | No-awareness result derived via K5 → K6 → V=0 chain using K7_trace + D_enc. G1 CLOSED by K7_trace §18 + D_enc §19. Computational verification PASS (`bb_vvv_t_bb_verification.py`). |
| T_BB' (Option C) | ✅ **CLOSED (superseded)** | V1 F4 finding falsifies T_BB' Step 1 premise (R_BB = R_K5 was required). T_BB (Option A) computationally verified; T_BB' superseded. |

**P2-C (π/8 first-principles):** The compatibility check at angle x = π/8 yields Δp = \|1 − 2α²\| / 4 exactly — a first-principles derivation from K7 closure (no free parameters). This is **exact** for all α² ≠ 0.5 (symmetric state degeneracy at α² = 0.5 confirmed as expected: Δp = 0).

**T_BB derivation chain:**

```
K5_prospective: W's coherent measurement → requires_K_joint(K_F, K_W) = 1
K7 closure:     K_F closes at t_close(K_F)
K7_trace:       Δ_closure(k_F) := V_prov(k_F) − V_final(k_F) ∈ {0,1}
D_enc:          Enc(M_aware, k_F) = 1 iff o(M_aware) counterfactually depends on Δ_closure
K5 fires:       requires_K_joint(M_aware, M_W) = 1 → V(M_aware) → 0
Result:         Friend F cannot retain awareness (V=0) → T_BB no-awareness result
```

**Key boundary:** V1's F4 finding does not invalidate T_BB. T_BB uses K7_trace + D_enc (Layer 2), not the R_BB = R_K5 equivalence. What F4 establishes is that B&B's no-valid-joint-model condition and VVV-QMRF's K5 incommensurability capture **structurally different aspects** of the Wigner's Friend problem — they are compatible frameworks analyzing different failure modes.

### 9.2 Frauchiger & Renner (2018): FR Paradox Avoided via K5 V_prov

**Paper reference:** Frauchiger, D. and Renner, R. (2018). "Quantum theory cannot consistently describe the use of itself." *Nature Communications* 9, 3711.

**Scenario:** Four agents (F1, F2, W1, W2) in nested EWF setups. FR show that under three assumptions (Q: universality, C: consistency, S: single-outcome), agents reach mutually contradictory predictions. The contradiction requires that V(k_F1) = 1 AND V(k_W1) = 1 simultaneously — both the Friend's registration and the Wigner's registration are valid at the same time under the same cross-observer validity demand.

**VVV-QMRF FR avoidance chain:**

```
FR contradiction requires:   V(k_F1) = 1  AND  V(k_W1) = 1  simultaneously
                                              ↓
K5 fires at t₂:              K_F1 ⊥_K K_W1 within comparison context C_K
                              (W1's coherent measurement ≡ requires_K_joint = 1)
                                              ↓
K6 Authority:                 Auth(K_W1 → K_F1) = 1
                              → V(k_F1) → 0  (K5 post-closure irreversible)
                                              ↓
Premise fails:                V(k_F1) = 1 AND V(k_W1) = 1 NEVER simultaneously satisfied
                                              ↓
FR contradiction:             AVOIDED — K5 gates the joint validity condition at source
```

**VVV-QMRF recast of FR assumption (S):** The FR argument requires F1's outcome and W1's outcome to belong to the same validity domain (joint cross-observer fact). K5 ⊥_K prevents this: they are structurally incommensurable registrations. VVV-QMRF does not *reject* (S); it *scopes* (S) to within a single K-context. The FR contradiction never assembles within VVV-QMRF's structural machinery because the joint validity demand is blocked by K5 before it can be evaluated.

**V_FR2 verification (script-verified, 2026-05-28):** K7_trace records Δ_closure(k_F1) := V_prov(k_F1) − V_final(k_F1) at W1's coherent measurement. This is **structurally identical** to T_BB Step 2 in B&B — the same K7_trace definition applies unchanged to a different scenario with different agents and a different contradiction mechanism. `fr_vvv_k7trace_consumer_verification.py` v1.0: OVERALL PASS.

**T_FR status (Class D, blocked by G_FR2):** A full T_FR (No-Joint-Validity Bridge Theorem) for the 4-agent scenario (F1, F2, W1, W2) requires the N=4 K_joint construction, which depends on T4-H for N=4. T4-H is THEOREM for N=2 (T1 constructive) and general N (abstract colimit proof, Steps 1-4). The N=4 concrete instantiation has not been explicitly verified. A simplified 2-agent version (F1+W1) is feasible and structurally established by V_FR2.

### 9.3 K7_trace + D_enc: Canonical Layer 2 with Four Consumers

The V_FR2 result confirms K7_trace as a **scenario-agnostic** Layer 2 primitive — it applies with identical definition across structurally distinct scenarios:

| Consumer | Scenario | Role | Status |
|---|---|---|---|
| **T_BB** (BB-VVV) | Baumann-Brukner (2024): F + W angle sweep | V_prov substitute after K7 closure for T_BB no-awareness derivation | Class C conditional |
| **D_enc** | All scenarios with K7 closure | Parent: Enc(M_aware, k_F) = 1 iff counterfactual dependence on Δ_closure | Class C-canonical |
| **3-OBS** | Three-observer hierarchical EWF | Δ_closure propagation through F1→F2→W hierarchy (§10) | Class C (T4-H verified) |
| **FR** (FR-VVV) | Frauchiger-Renner (2018): 4-agent nested EWF | V_FR2: Δ_closure(k_F1) after W1's coherent measurement — blocks FR joint validity | Class D (T_FR blocked by G_FR2) |

**Architectural significance:** K7_trace being consumed by four structurally distinct analyses (B&B angle-sweep, D_enc semantic, 3-OBS hierarchical, FR nested) confirms it is a legitimate Layer 2 primitive — not a single-use BB-VVV construct. This cross-validation was the primary criterion for canonical promotion (RCA 4.77/5, 2026-05-27).

---

## 10. T4-H THEOREM and 3-Observer Prediction

### 10.1 T4-H: From Hypothesis to Theorem (4/4 Steps, 2026-05-28)

T4-H is the N-observer Colimit Existence Theorem for the category C_{K-space}. It states: *for any finite diagram D of K-spaces with K1–K8-preserving morphisms, the colimit K_colim exists and satisfies K1–K8.*

T4-H was originally framed as a hypothesis ("T4-H") because its proof required four sequential steps. As of 2026-05-28 all four are verified (RCA 4.74/5):

| Step | Claim | Key technique | Status |
|---|---|---|---|
| Step 1 | C_{K-space} is a valid category | Identity morphisms + composition + associativity via K8-preserving maps | **VERIFIED** |
| Step 2 | K_colim = (∐_i K_i)/~ is constructible | Lexicographic t-assignment (SP1), V-snapshot at embedding (SP2), transitive closure for <_colim (SP3); 5/5 gates PASS | **VERIFIED** (RCA 4.73/5) |
| Step 3 | K_colim satisfies K1–K8 | **T-PRES Lemma** (all morphisms preserve t exactly, resolving K2 acyclicity); K3–K8 verified via quotient structure | **VERIFIED** (RCA 4.74/5, 2026-05-28) |
| Step 4 | K_colim satisfies universal property | u([k,i]) := f_i(k) well-defined (T-REP corollary), K8-preserving, unique | **VERIFIED** (2026-05-28) |

**T-PRES Lemma (key to Step 3):** Any morphism f: K_i → K_j in C_{K-space} satisfies t_j(f(k)) = t_i(k) for all k ∈ K_i. This is because K8-preservation requires all five tuple fields (M, o, cert, t, V) to be preserved exactly. Consequence: all representatives of any equivalence class [k, i] share the same t value (T-REP Corollary), ensuring K2's acyclicity condition holds in K_colim without cycles.

**Claim class:** T4-H is now a **full THEOREM**, not a hypothesis or conditional claim. T1 (N=2 constructive) remains independently valid without invoking T4-H's universal property. T4, T5 (K_joint Associativity) are upgraded accordingly.

### 10.2 Upgrade: 3-Observer Prediction from Class C-Conditional to Class C

The 3-observer registration transition mechanism (`3observer_registration_transition.md`, v1.1, 2026-05-28) was previously classified **Class C-conditional** pending T4-H Steps 3-4. With T4-H THEOREM confirmed, the conditional gate is resolved.

**3-observer hierarchical configuration:**

```
Hierarchy: t_F1 < t_F2 < t_W

  F1 measures system S → registers k_F1 in K_{F1}
  F2 measures F1's lab → registers k_F2 in K_{F2}
  W (Superobserver) measures joint F1+F2 lab
     (requires_K_joint = 1; interference measurement)
```

The registration transition mechanism traces via four steps:

- **H1:** K7_trace records Δ_closure(k_F1) = V_prov(k_F1) − V_final(k_F1) at t_close(K_{F1}).
- **H2:** K7_trace records Δ_closure(k_F2) similarly at t_close(K_{F2}).
- **H3:** D_enc evaluates: Enc(M_aware, k_F1) = 1 iff the post-closure act M_aware's outcome depends counterfactually on Δ_closure(k_F1). In the 3-OBS case, this propagation requires K_joint for N=3, provided by T4-H.
- **H4:** If Enc = 1 → requires_K_joint(M_aware, M_W) = 1 → K5 fires → V(M_aware) → 0 → no-awareness result propagates hierarchically.

**Upgraded classification:**

| Component | Prior class | Current class | Condition |
|---|---|---|---|
| K7_trace + D_enc application | C-conditional | **Class C** | T4-H THEOREM 2026-05-28 |
| No-awareness propagation (H1-H4) | C-conditional | **Class C** | T4-H THEOREM 2026-05-28 |
| Numerical prediction δ_M3 | Illustrative | Illustrative | Conditional on K9_E P9 only (see §10.3) |

### 10.3 3-Observer Numerical Prediction (Illustrative)

**Important scope boundary:** The 3-observer *structural mechanism* (§10.2) is Class C — it follows from K-space axioms K1–K8 + Layer 2 (K7_trace, D_enc) + T4-H THEOREM. The 3-observer *numerical prediction* (δ_M3) requires the additional K9_E postulate (P9) — it is illustrative and conditional on K9_E.

**Prediction (conditional on K9_E P9):**

```
δ_M3 = −0.223  at β = 0.3  (illustrative, not a measurement)
```

- 3-observer K_ctx is larger than 2-observer K_ctx → amplification factor ≈ 11× relative to 2-observer δ_S.
- At β = 0.3, the 2-observer prediction gives δ_S ≈ −0.020; the 3-observer setup predicts δ_M3 ≈ −0.223.
- The amplification arises because K_ctx(k_i, Exp) includes two contextual observer registrations instead of one, increasing f_perp.

**Dependency chain for numerical prediction:**

```
K7_trace + D_enc (Layer 2, canonical)
    ↓ mechanism (Class C)
T4-H THEOREM (N=3 K_joint — resolved)
    ↓ structural substrate
K9_E postulate P9 (Class C qualified — not yet confirmed)
    ↓ probability assignment
δ_M3 = −0.223 at β=0.3 (illustrative)
```

**Caveat:** β = 0.3 is chosen for illustration (not from a fit to 3-observer data, which does not yet exist). The true β value, if K9_E is correct, would be determined by a future 3-observer experiment. The 11× amplification factor itself is structural (from K_ctx size) and holds for any non-zero β, not just β = 0.3.

---

## 11. φ Conjecture: Structure-Preserving Map K → B(H) (Class D Supporting)

> **This section is Class D supporting material — NOT the central claim of v3.0.** The central claims of this paper are the K-space architecture (§4), the K9_E postulate (§5), and the K9-S12 experimental specification (§8). The φ conjecture (Project B) is logically independent of K9_E (Project C) — see §5.6 for the independence statement.

### 11.1 The Conjecture and Its Motivation

**Conjecture (Class D):** There exists a structure-preserving map φ: K → B(H), where B(H) is the algebra of bounded operators on Hilbert space H, such that φ encodes the registration-logic properties of K-space (K1–K8) in the operator-algebraic language of Standard QM.

**Motivation:** VVV-QMRF's K-space axiomatizes *what gets registered* (registration-logic structure). Standard QM's B(H) axiomatizes *what can be measured* (operator-algebraic structure). If φ exists, it would formalize the correspondence between registration events in K and observable operators in B(H) — not by identifying K with H, but by showing that K's registration-logic has a faithful structural image in operator-algebraic language.

**Phase 1–4 completion (Project B Track B):** The φ-map research program has completed four phases:
- **Phase 1:** Target selection — B(H) chosen as codomain with image Im(φ) ⊆ {P_o} ∪ {0} (projection sub-lattice). Three counter-arguments against B(H) resolved.
- **Phase 2:** Necessary conditions N₁–N_T derived from K1–K8 and T1–T9 (§11.2).
- **Phase 3:** φ-conditional interpretation scope analysis (§12.2).
- **Phase 4:** Open items documented (φ-O2: N₆ sufficiency boundary confirmed as fundamental; C2 readiness 8.0/10).

**Why B(H) as codomain (not C\*-algebra, von Neumann algebra, or projection lattice):**

| Alternative | Problem |
|---|---|
| P(H) projection lattice | Not an algebra — K6 authority-composition (φ-6) has no natural image |
| Von Neumann algebra M | Requires specifying which subalgebra — adds unwarranted structural choice |
| Functor to category C_obs | Loses concrete B(H) operator intuition; abstract for current phase |
| **B(H) (chosen)** | Contains all projections P_o; admits φ-1 through φ-7' conditions; standard QM home |

**EWF connection:** In the EWF scenario, K_F ⊥_K K_W on the K-side maps to [ι(P_{o_F}), P_{o_W}] ≠ 0 in B(H) — the familiar non-commutativity of quantum observables. The φ-conditional analysis (§12.2) re-frames each interpretation's structural gap as the specific necessary condition N_i it lacks machinery to satisfy.

### 11.2 Necessary Conditions N₁–N_T (Derived from K1–K8)

The following necessary conditions must hold for any map φ: K → B(H) to qualify as structure-preserving. These are necessary conditions — not sufficient for φ's existence.

| Condition | Source axiom | Statement | B(H) encoding |
|---|---|---|---|
| **φ-1** (Well-Definedness) | K1 | φ: K_R → B(H) is a total function; ∀k ∈ K_R, φ(k) ∈ B(H) defined | cert(k) = 1 for all k ∈ K_R → no undefined images |
| **φ-2** (Lüders Order) | K2 | k₁ <_R k₂ maps to Lüders update: ρ ↦ P_{o₂} · P_{o₁} · ρ · P_{o₁} · P_{o₂} (application order from temporal order) | Non-commutativity of P_{o₁}, P_{o₂} mirrors non-symmetry of <_R |
| **φ-3** (Cert-Reflection) | K3 | φ(k) is determined by k's own tuple fields alone; for all R' ≠ R: φ_R(k) ∉ φ_{R'}(k') | P_o = \|o⟩⟨o\| determined entirely by the registered outcome o — intrinsic |
| **φ-4** (Validity-Positivity) | K4 | V(k) = 1 → φ(k) = P_o ≥ 0, φ(k) ≠ 0; V(k) = 0 → φ(k) = 0 | Connects to AOE (Bong 2020): V(k) = 1 (default validity) → non-zero positive operator |
| **φ-5** (Invalidation-Absorption) | K5 | V_final(k) = 0 (post-closure irreversible) → φ(k) = 0; P_o → 0 is irreversible in B(H) | Zero operator is an absorbing element: 0·A = A·0 = 0; no recovery without additional info |
| **φ-6** (Authority-Composition) | K6 | Auth(k₂ → k₁, C_K) = 1 maps to P_{o₂} · P_{o₁} ≠ 0 (non-annihilating composition) | k₂ has authority over k₁ only if their projectors are not onto orthogonal subspaces |
| **φ-7** (Embedding Naturality) | K8 | Diagram commutes: φ_X(i(k)) = ι(φ_R(k)) where ι: B(H_R) → B(H_X) is tensor extension | ι(P_o) = P_o ⊗ 1_{H_extra} — standard tensor product inclusion of subsystem projector |
| **φ-7′** (Closure Finalization) | K7 | φ_final(k) = φ_prov(k) at t_close; post-closure φ is fixed; provisional φ_prov can change pre-closure | Fixes the operator image at t_close — after that, φ(k) = 0 or P_o cannot change |
| **N_T** (Theorem bridge) | T2, T3 | K_F ⊥_K K_W (K-side) → [ι(P_{o_F}), P_{o_W}] ≠ 0 (B(H)-side): non-commutativity as image of incommensurability | This is the φ-conditional EWF connection: operator non-commutativity is the B(H) image of K-side ⊥_K |

**Derivation status:** N₁–N_T are derived under the assumption that φ exists. They state what φ *must* satisfy; they do not prove φ *does* exist. The relationship is: φ exists → N₁–N_T hold. The converse (N₁–N_T hold → φ exists) remains unproven. Open item φ-O2 (N₆ sufficiency for K6 authority-composition) is documented as a fundamental boundary.

### 11.3 K ≠ H Boundary Reaffirmed

A critical architectural boundary: **φ is a map from K to B(H), not an identification K = H.**

Three distinct layers remain separate throughout the φ analysis:
- **K (registration layer):** Tuples ⟨M, o, cert, t, V⟩ with registration-logic operations (K1–K8). Not a Hilbert space, not a probability space.
- **ρ (physical state layer):** Density operators ρ ∈ D(H), evolving under Standard QM (P1–P4). Not modified by VVV-QMRF.
- **B(H) (observable algebra):** Bounded operators, containing projection operators P_o. The codomain of φ.

φ: K → B(H) maps registration events to operators, but it does not collapse K into H. The image Im(φ) ⊆ {P_o} ∪ {0} is a small subset of B(H) — φ selects the operators relevant to registration from within the full operator algebra. This is the formal expression of K ≠ H: K-side validity events map *into* B(H) without being *identified with* H.

**Why this matters:** If K = H were asserted, VVV-QMRF would be claiming that every registration event has a direct physical correspondent in the Hilbert space — this would constitute a modification of Standard QM. K ≠ H (preserved by φ) ensures VVV-QMRF remains a registration-layer analysis rather than a modification of quantum dynamics.

### 11.4 Class D Supporting Status

The φ conjecture is Class D:
- The **existence** of φ is not proven. No constructive proof has been given that a map satisfying all of φ-1 through φ-7', N_T is well-defined for all K-spaces.
- The necessary conditions are **not sufficient**. Satisfying N₁–N_T would be required for φ to exist, but whether it is sufficient is an open mathematical question.
- **No empirical prediction** derives solely from φ. K9_E (§5) provides all testable predictions independently of φ.
- φ is **not falsified** by a K9_E null result. The φ conjecture concerns the formal relationship K → B(H), not the probability assignment P(o|K).

The value of the φ analysis is interpretive: it provides the formal language for §12.2 (φ-conditional scope boundaries for existing QM interpretations) and maps the VVV-QMRF framework into a notation familiar to operator-algebraic quantum mechanics. It is supporting infrastructure for the project's long-term formalization goal, not its current testable claim.

---

## 12. Positioning Against Existing Interpretations

### 12.1 Architectural Comparison

| Interpretation | Response to EWF paradox | VVV-QMRF difference |
|---|---|---|
| Copenhagen | WF is ill-posed; classical apparatus required | K3/K4 formalize why apparatus has registration authority: σ_R(M) = 1 intrinsically (no Heisenberg cut needed) |
| Many-Worlds | All outcomes occur; no paradox | Registration events are singular per K-side (K1 cert = 1 invariant); not globally branching |
| QBism | Facts are agent-relative; no paradox | Agrees on agent-relativity; adds formal K-side structure (K1–K8, six conditions) that QBism does not supply |
| Relational QM | Facts are relation-relative; no paradox | Closest existing framework; VVV-QMRF adds formal machinery (K3 self-cert, K7 closure, requires_K_joint) that RQM does not |
| Objective Collapse (GRW) | Physical collapse restores absolute facts | VVV-QMRF does not require physical collapse on ρ-side; K5 operates on K-side validity, independent of ρ dynamics |

**Relation to Relational Quantum Mechanics:** Rovelli (1996) argues quantum states are relative to observers. VVV-QMRF adds the formal registration-layer structure explaining *why* they are relative: σ_R(M) operates intrinsically within K_R, independently of K_{R′}. K_F ⊥_K K_W is the registration-layer account of Rovelli's observer-relativity. This is a genuine extension: VVV-QMRF supplies the formal conditions (K3 self-cert, K2 temporal order, K5 invalidation, K7 closure, requires_K_joint predicate) that Relational QM does not.

### 12.2 φ-Conditional Scope Boundaries (Class D)

Section §11 derives necessary conditions N₁–N_T for any structure-preserving map φ: K → B(H). These conditions re-frame each architectural gap in §12.1 as a **φ-conditional scope boundary**: the specific condition N_i that the interpretation lacks the structural machinery to satisfy.

**Scope boundary convention:** "Lacks the structural machinery for N_i" means the interpretation does not supply the formal element required by N_i — not that the interpretation is incorrect within its own domain.

| Interpretation | Architectural gap (§12.1) | φ-conditional scope boundary | N_i lacking |
|---|---|---|---|
| Copenhagen | No formal definition of classical apparatus | Cannot construct φ-domain element k = ⟨M, o, cert, t, V⟩ with cert field → φ has no defined domain | **N₃** (cert-reflection, §11.2): cert = σ_R(M) = 1 required to admit k into K_R |
| Many-Worlds | No physical observable distinguishes branches | No singular admission act per branch → K_R carrier set underspecified → φ total function (N₁) has no well-defined domain | **N₁** (well-definedness, §11.2): φ total requires K_R well-defined; branching leaves carrier set underspecified |
| QBism | Subjective probability is not a physical quantity | No structural V(k) ∈ {0,1} field: agent-relative belief is not a binary validity predicate → φ cannot satisfy validity-positivity | **N₄** (validity-positivity, §11.2): V(k) = 1 → φ(k) = P_o ≥ 0 requires V as structural field, not degree of belief |
| Relational QM | No temporal closure event | RQM has relational facts but no t_close → φ_final cannot be fixed | **N₇** (closure-finalization, §11.2): φ = φ_final fixed at t_close requires temporal closure boundary absent from RQM |
| Objective Collapse (GRW) | Collapse on ρ-side only | GRW collapse operates on ρ-side state; K-side V: 1→0 irreversible transition not formally supplied | **N₅** (invalidation-absorption, §11.2): K-side V-update and post-closure irreversibility not entailed by ρ-side collapse |

**Status — Class D:** N₁–N_T are derived under the assumption that φ: K → B(H) exists (§11). This §12.2 analysis means: *if φ were to exist, these are the structural elements existing interpretations would need to supply.* Neither φ's existence nor the empirical correctness of these scope boundaries is asserted. See §13.4 for the relationship between this φ-conditional analysis and the broader architectural constraint framing.

### 12.3 Three Logically Independent Projects

VVV-QMRF comprises three projects related by a one-way motivation chain. This section makes that independence explicit to prevent the critique that Buddhist epistemology is post-hoc justification for a physics claim.

**Project A — BE↔QM Comparative Mapping (interpretive framework):**
- 30 nodes (N_BE_00001–N_BE_00030), 39 edges (ED_BE_00001–ED_BE_00039)
- Comparative framework between Buddhist Pramāṇa epistemology and quantum measurement concepts
- Independently testable as a comparative-philosophy framework (internal consistency, historical accuracy of BE nodes, adequacy of QM node definitions)
- **Does NOT constitute evidence for K-space axioms or K9_E**

**Project B — VVV-QMRF Conceptual Framework (formal axiomatization):**
- K1–K8 frozen Layer 1 axioms; T1–T9 updatable Layer 2 bridge theorems; φ-map Class D conjecture
- Independently testable as a formal axiom system (consistency, non-redundancy, expressive power)
- Motivated by Project A's structural analysis of valid registration, but not logically derived from it
- **Does NOT make testable physical predictions by itself**

**Project C — K9_E Testable Hypothesis (falsifiable claim):**
- K9_E postulate P9 with one free parameter β; Class C (qualified)
- Falsifiable via K9-S12 Modified Bong Protocol (§8); predicts δ⟨A₁B₂⟩ ≠ 0 at θ = 31°
- Motivated by Project B's K-space structure (K5_prospective → T8 → f_perp), but K9_E is a *postulate* not *derivable* from K1–K8
- **This is the only project with a current falsification path**

**A→B→C: one-way motivation, not logical derivation:**

```
Project A (BE↔QM)  →(motivates)→  Project B (K-space)  →(motivates)→  Project C (K9_E)
    ↑                                    ↑                                    ↑
interpretive                          formal                             testable
framework                          axiomatization                       hypothesis
```

Each project is independently falsifiable:
- Project A is falsified if the BE node definitions are historically inaccurate or the QM node definitions mischaracterize Standard QM.
- Project B is falsified if K1–K8 are internally inconsistent, or if the K-space formalism cannot be applied consistently to any EWF scenario.
- Project C is falsified if δ⟨AB⟩ = 0 at θ = 31° across a full θ-sweep (K9-S12 null result).

**A null K9_E result (β = 0 measured by K9-S12) falsifies Project C but does not invalidate Project B (the K-space architecture remains valid as a formal structure) or Project A (the BE↔QM comparative framework stands independently).**

---

## 13. Scope, Limitations, and Open Items

### 13.1 What This Paper Does Not Claim

- Does not replace Standard Quantum Mechanics or revise P1–P4.
- Does not revise the Born rule or unitary evolution (K9_E recovers Born exactly at β = 0).
- Does not claim Buddhist epistemology proves quantum mechanics (Project A is interpretive framework, not evidence).
- Does not claim K-side incommensurability is experimentally confirmed.
- Does not claim that consciousness plays any role in registration.
- Does not claim the EWF paradox is fully resolved on the ρ-side.
- Does not claim requires_K_joint is a necessary-and-sufficient condition for all LF violations; it is proposed only as a necessary registration-layer condition.
- **Does not claim K9_E is experimentally confirmed** — K9_E is Class C (qualified): structurally testable, empirically unconfirmed. The 2.31σ Proietti fit is real but ambiguous; noise cannot be ruled out as an alternative explanation (§7).
- **Does not claim the φ-map φ: K → B(H) is proven to exist** — the map is conjectured (Class D). The necessary conditions N₁–N_T are derived but not sufficient for φ's existence (§11).
- **Does not claim K9_E is the unique probability rule consistent with K1–K8** — K1–K8 are structural axioms that do not uniquely determine a probability rule; K9_E is one motivated postulate, not the only possibility.
- **Does not claim the 3-observer prediction δ_M3 = -0.223 is independent of β** — this value is illustrative at β = 0.3; the true β is unknown until experimental measurement.

### 13.2 Formal Phase Summary and Open Items

The ⊥_K formal definition chain is complete at the proposed Class D/C level:

| Formal layer | Symbol | Class | Defined in |
|---|---|---|---|
| K-side incommensurability | ⊥_K | D | §6.4 |
| Admissible joint K-space | K_joint / AdmJoint | D | §6.3 |
| Joint-validity demand | D_joint / requires_K_joint | D | §6.3 |
| K-side comparison context | C_K | D | §6.4 |
| Bridge lemma | Bridge_EWF | D/C | §6.5 |
| Operational data criterion | ODC_K | C | §6.6 |
| K-Space axioms (Layer 1) | K1–K8 | D (K1=C) | §4.1–4.2 |
| Bridge theorems (Layer 2) | T1–T9, K7_trace, D_enc | D/C | §4.3–4.4 |
| Probability postulate | K9_E (P9) | C (qualified) | §5 |
| Experimental protocol | K9-S12 | C | §8 |
| φ conjecture | φ: K → B(H) | D (supporting) | §11 |

**Resolved items (updated from v2.0):**

| Item | v2.0 status | v3.0 status |
|---|---|---|
| Axiomatize K as full mathematical structure | Deferred long-term task | **RESOLVED** — K1–K8 v2.4, T1–T9, K7_trace, D_enc (§4) |
| K5_prospective (A1 assumption) | Class D semantic extension | **RESOLVED** — upgraded to K5_prospective clause (§4.2) |
| T4-H colimit existence | Conditional hypothesis | **THEOREM** (4/4 steps, RCA 4.74/5, 2026-05-28, §10.1) |
| 3-OBS Class C-conditional | Conditional on T4-H | **Class C** (T4-H resolved, §10.2) |
| K7_trace canonical status | BB-VVV local construct | **Canonical Layer 2** (4 consumers, RCA 4.77/5, §4.4) |

**Deferred proof items (not required for current claim class):**

| Deferred item | Reason deferred |
|---|---|
| Full semantic proof for Bridge_EWF | Requires formal semantics of "no admissible reinterpretation"; paper uses operational sufficient conditions |
| Full formal proof for ⊥_K as mathematical relation | K1–K8 structural definition complete; full topological/order-theoretic treatment deferred |
| AdmJoint necessary-and-sufficient conditions | Currently sufficient conditions A–E; full characterization is an open item |
| Equivalence of σ(M) and R̂_svasa formalisms | Separate research track |

### 13.3 Falsification Condition (Restated)

**K9_E (Project C) is falsified** by: a K9-S12 experimental result with δ⟨A₁B₂⟩ = 0 at θ = 31° within predeclared statistical tolerance across a full θ-sweep. This would falsify the overlap-only class of deformations (the class that K9_E belongs to), not just a specific β value.

**The K-side incommensurability conjecture is falsified** by: an EWF experiment producing results consistent with a single K_joint registration model satisfying Conditions 1–6 for both observers simultaneously, for a configuration independently classified as requires_K_joint = 1 via D_joint and Bridge_EWF. If K_joint exists empirically, the Bridge_EWF conditional bridge requires revision.

**K9_E falsification (K9-S12 null result) does not falsify:**
- The K-space architectural framework (K1–K8 + Layer 2) — Project B
- The K-side incommensurability conjecture (K_F ⊥_K K_W) — a different structural claim
- The BE↔QM comparative mapping — Project A

Operationally, all three falsification tests require a predefined data criterion (tolerance τ fixed before data collection); otherwise the criterion becomes post-hoc.

### 13.4 Architectural Constraints of the K-side/ρ-side Separation

The core architectural commitment of VVV-QMRF is K ≠ H: the registration layer is structurally distinct from the physical layer (§2.1). This separation enables the framework to address the registration layer gap. It also imposes two architectural constraints that are inherent consequences of the layer separation, not oversights.

**Constraint 1 — Self-certification is not a ρ-side observable.** Condition 4 requires σ_R(M) = 1 to be determined intrinsically within K_R. Any physical measurement of σ would itself require a second-order registration act, re-entering the von Neumann regress that K3 is designed to terminate. The operational compromise is stated in ODC_K condition (ii): self-certification is treated as a structural postulate satisfied by construction when the registering system meets the architectural definition of a K-side observer.

**Constraint 2 — D_joint is a framework-level classification, not a physical observable.** The predicate D_joint(A, B, Arch) classifies whether a comparison architecture demands joint validity. Operational sufficient conditions A–E (§6.3) connect observable features of the setup (interference vs. readout, comparison vs. no comparison) to D_joint values in a reproducible way. But the mapping is a VVV-QMRF classification of the experimental architecture, not a measurement of a physical quantity.

**These constraints are typical of the measurement problem, not unique to VVV-QMRF.** Every interpretation or extension of quantum mechanics that addresses measurement introduces an unobservable primitive:

| Framework | Central concept | Why not directly observable |
|---|---|---|
| Copenhagen | Classical apparatus / Heisenberg cut | No formal definition of what makes an apparatus classical |
| Many-Worlds (Everett) | Branching of worlds | No physical observable distinguishes one branch |
| QBism | Agent's degree of belief | Subjective probability is not a physical quantity |
| Relational QM (Rovelli) | Facts relative to observer | Relata are only defined within the relation |
| Objective Collapse (GRW) | Collapse mechanism | Collapse events are postulated, not yet detected |
| **VVV-QMRF** | **Self-certification / D_joint** | **K-side properties are not ρ-side observables (K ≠ H)** |

What distinguishes VVV-QMRF is that the constraints are explicitly named, traced to a single architectural commitment (K ≠ H), and given operational bridges (ODC_K, conditions A–E) that define what can and cannot be tested under the current formalism.

---

## References

1. von Neumann, J. (1932). *Mathematical Foundations of Quantum Mechanics.* Princeton University Press.
2. Bohr, N. (1935). Can Quantum-Mechanical Description of Physical Reality Be Considered Complete? *Physical Review* 48, 696–702.
3. Heisenberg, W. (1958). *Physics and Philosophy.* Harper & Row.
4. Wigner, E.P. (1961). Remarks on the mind-body question. In: *The Scientist Speculates,* Good (ed.), pp. 284–302.
5. Rovelli, C. (1996). Relational quantum mechanics. *International Journal of Theoretical Physics* 35, 1637–1678.
6. Prasad, H.S. (2023). Buddhist Pramāṇa-Epistemology. *Studia Humana* 12(1-2), 21–52. DOI: 10.2478/sh-2023-0004.
7. Zurek, W.H. (2003). Decoherence, einselection, and the quantum origins of the classical. *Reviews of Modern Physics* 75, 715–775.
8. Frauchiger, D. and Renner, R. (2018). Quantum theory cannot consistently describe the use of itself. *Nature Communications* 9, 3711.
9. Brukner, C. (2018). A no-go theorem for observer-independent facts. *Entropy* 20(5), 350.
10. Proietti, M. et al. (2019). Experimental test of local observer independence. *Science Advances* 5(9), eaaw9832. DOI: 10.1126/sciadv.aaw9832.
11. Bong, K.W. et al. (2020). A strong no-go theorem on the Wigner's friend paradox. *Nature Physics* 16, 1199–1205. DOI: 10.1038/s41567-020-0990-x.
12. Jordan, A.N. and Siddiqi, I.A. (2024). *Quantum Measurement Theory and Practice.* Cambridge University Press. DOI: 10.1017/9781009103909.
13. Baumann, V. and Brukner, Č. (2024). Wigner's friend's memory and the no-signaling principle. *Quantum* 8, 1481. arXiv:2305.15497.
14. VietVunVut (Viet - Nguyen Xuan) (2026). Has Every Wigner's Friend Experiment Been Blind to a Geometric Degree of Freedom? Submitted to arXiv 2026-05-27 (arXiv ID pending confirmation). Internal ref: `papers/paper_002/manuscript.md`.
15. VietVunVut (Viet - Nguyen Xuan) (2026). VVV-QMRF Class C. Working Paper v3.0. DOI: 10.5281/zenodo.20431310. Zenodo.

---

## Appendices

**Appendix A** — K9_E reproduction scripts: `documents/research_documents/project_vvv_qmrf_class_c/07_fits/`
**Appendix B** — K_Space_Axiomatization v2.4: `documents/research_documents/meta_architecture/K_Space_Axiomatization.md`
**Appendix C** — AHP audit footprint: `documents/research_documents/anti_hallucinations/`

---

## Draft phase status

| Phase | Sections | Status |
|---|---|---|
| **P1** | Skeleton + Abstract (8 paras) + §4 K-Space Architecture | **COMPLETE 2026-05-28** |
| **P2** | §5 K9_E Postulate + §7 Empirical Status | **COMPLETE 2026-05-28** |
| **P3** | §8 K9-S12 + §10 T4-H + 3-OBS | **COMPLETE 2026-05-28** |
| **P4** | §9 BB+FR + §11 φ-map Class D | **COMPLETE 2026-05-28** |
| **P5** | Carry-over §1, §2, §3 (headers) + §6 + §12 + §13 | **COMPLETE 2026-05-28** |
| **P6** | Abstract finalization + header update | **COMPLETE 2026-05-28** |
| **P7** | CHANGELOG + README + AHP footprint verified | **COMPLETE 2026-05-28** |

---

*VVV-QMRF Working Paper v3.0 — All phases P1-P7 complete (2026-05-28). All mini-RCA PASS (4.57–4.6/5). Average 4.58/5.*
*Promoted from draft to final 2026-05-28. Abstract (8 para) + §1–§13 (~14,500w). Supporting files: CHANGELOG.md, README.md, plan.*
*References [13] and [14] finalized; [14] arXiv ID pending confirmation post-submission.*
*All formal claims classified by evidence level. Class C = structurally testable, empirically UNCONFIRMED. Class D = proposed.*
