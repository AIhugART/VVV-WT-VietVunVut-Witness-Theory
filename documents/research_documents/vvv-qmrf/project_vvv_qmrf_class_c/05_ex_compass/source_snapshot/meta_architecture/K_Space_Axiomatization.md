Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# K-Space Axiomatization — Registration-Logic Foundation for VVV-QMRF
# Tiên đề hóa Không gian K — Nền tảng Registration-Logic cho VVV-QMRF

**Framework:** VietVunVut Quantum Measurement Registration Framework (VVV-QMRF)
**Document type:** `meta_architecture`
**Date:** 2026-05-19
**Author:** VietVunVut (Viet - Nguyen Xuan)
**Status:** Mixed — K1: Class C (formal definition); K2–K8, T1–T4: Class D (proposed registration-layer) *(K1 elevated to Class C as carrier-set formal definition; see §1 K1 Property table and §5 C-KAXIOM-001)*
**Source:** Derived from VVV-QMRF Working Paper v2.0 Section 7.2 deferred item #5
**Cite:** VVV-QMRF §K-AXIOM
**Plan reference:** `papers/Testable_Prediction_Section/extended_wigners_friend_k_side_incommensurability/plan/VVV-QMRF_K_Space_Axiomatization_Plan.md`

**Scope:** Axiomatize the K-side registration space as a formal registration-logic structure. This document provides the mathematical/logical foundation that the working paper v2.0 structural definitions rest upon.
**Out of scope:** This document does not modify Standard Quantum Mechanics, does not change any VVV-QMRF postulate (E1-E16), does not upgrade claim classes of paper v2.0, and does not claim K-space is a canonical QM object.

> **DISCLAIMER / CẢNH BÁO:** VVV-QMRF is independent Class D personal research, not Standard Quantum Mechanics, not peer-reviewed or experimentally validated, and not for real-world technical use. Full boundary protocol: `DISCLAIMER.md`.

---

## 0. RCA Motivation / Động lực RCA

### 0.1 Define — Symptom vs. Cause

| | |
|---|---|
| **Symptom** | Working paper v2.0 Section 7.2 lists "Axiomatize K as a full mathematical structure" as a deferred item. Three other deferred proof items (`Bridge_EWF` semantic proof, `⊥_K` mathematical proof, `AdmJoint` necessary-and-sufficient conditions) are all blocked by the absence of axiomatized K-space. |
| **Root cause** | K is defined **extensionally** (as a collection of tuples `k = ⟨M, o, cert, t, V⟩`) rather than **intensionally** (via axioms that determine the properties of the space). All operations on K (embedding, union for `K_joint`, `⊥_K`, validity propagation) are defined ad-hoc per use case rather than derived from an axiomatic structure. |

### 0.2 Trace — 5 Whys

*(Note: The questions below trace the RCA Motivation — why axiomatization is needed now. This is a "Why is this the right fix?" trace, not a backward causal trace from symptom to deeper cause. The backward causal trace is: K extensional → no admission rule → axioms undefined → proofs blocked. The motivation trace and causal trace are complementary; both are valid RCA phases.)*

1. **Why needed?** VVV-QMRF uses K as a "space" in formal claims without mathematical foundation.
2. **Why now?** Three deferred proof items in paper v2.0 are blocked by this absence.
3. **Why not before?** Paper achieved Class C/D claims with structural definitions; operational bridges sufficed.
4. **Why is this right timing?** Paper formal chain is complete (Section 7.2). Axiomatization now serves dual purpose: foundation for proof upgrades AND quality audit of the paper's formal chain before community feedback arrives.
5. **Root cause:** K was introduced architecturally (`K ≠ H`) but never given formal axiomatic definition. This was intentional architectural debt to prioritize operational contact. Debt is now due.

### 0.3 Isolate — The Gap

K is currently a **collection** without structure. To be a **space**, it requires at minimum:
- **Axiomatized membership rule** — an admission criterion determining which tuples belong to K_R (K already has an extensional collection of tuples per §0.1; what it lacks is a formal membership axiom with cert-based admission rule and structural guarantees)
- **Order structure** — temporal ordering of registration events
- **Validity structure** — how validity propagates through order
- **Operations** — embedding (morphism between K-spaces), joint construction (for `K_joint`)

### 0.4 Fundamental Design Decision

K-space is NOT a pure mathematical space. It is a **registration-logic structure**: a mathematical carrier (chain within each K_R, partial order across K_R via embeddings, with morphisms preserving structure) whose primitive predicates are epistemological (`cert`, `V`, `⊥`). This is not Hilbert space, not phase space, not probability space — these are all (math + math). K-space is (math + registration-logic). The mathematical structure is the **carrier**, not the **content**.

### 0.5 2-Layer Architecture

```
Layer 1 — CORE AXIOMS (K1-K8): Frozen (syntactic)
  Based on dependency stack Level 0-3 (BE SOT, K≠H, E1-E7, K-state tuple).
  K1-K8 axiom TEXT does not depend on Level 4 — text is unconditionally frozen.
  K5/K6/K7 have CONDITIONAL SEMANTIC DEPENDENCIES on Level 4:
    - K5 firing narrows by Level 4 ⊥_K boundary clauses
    - K6 Auth depends on D_joint extensional scope
    - K7 t_close timing depends on requires_K_joint extensional scope
  K1-K4 and K8 carry NO Level 4 semantic dependencies.
  See §5 C-KAXIOM-010 for full 2-part syntactic/semantic isolation breakdown.

Layer 2 — BRIDGE THEOREMS (T1-T3 pending Level 4 freeze + T4 new Class D): Updatable
  T1-T3: Connect core axioms to Level 4 structural definitions; updatable when Level 4 changes.
  T4: New Class D theorem (N-observer generalization); independently updatable; requires
      separate verification not tied to Level 4 freeze.
  All bridge theorems updatable without changing K1-K8 text.
```

---

## 1. Core Axioms — Layer 1 (Frozen) / Tiên đề Lõi — Tầng 1

### AXIOM K1 — Carrier Set / Tập nền

**Statement:**
> The K-side registration space of a registering system R is a set K_R whose elements are K-state tuples. Each tuple contains five fields: measurement-registration act identifier (M), registered outcome (o), self-certification marker (cert), registration time (t), and validity status (V).

**Formal:**
```
K_R = { k | k = ⟨M, o, cert, t, V⟩ }

where:
  M    ∈ M_K          — measurement-registration act identifier
  o    ∈ O ∪ {∅}      — registered outcome (∅ reserved for null/absence cases, E9/E14)
  cert ∈ {0,1}        — self-certification marker (admission filter at K_R boundary)
  t    ∈ T_R          — registration time (discrete index or real-valued timestamp)
  V    ∈ {0,1}        — validity status

Cert admission rule:
  k ∈ K_R ⇒ cert(k) = 1.
  Reason: K_R is "produced by R over time" — every element of K_R is a registration
  event that has occurred. By K3, occurrence implies σ_R(M) = 1, hence cert(k) = 1.
  The cert ∈ {0,1} range is retained for the admission-filtering boundary:
  events with cert = 0 are NOT admitted into K_R (admission failure outside K_R scope).

  ⚠ Structural-constant clarification (PG-01):
  Within K_R, cert is effectively a structural constant: cert(k) = 1 for ALL k ∈ K_R
  by the admission rule above. The declaration cert ∈ {0,1} does NOT imply cert can
  take value 0 inside K_R — it records the type of the field at the boundary. The
  discriminating role of cert (filtering cert=0 events) is exercised at the K_R
  admission boundary, not inside K_R. Once k is inside K_R, cert(k)=1 is invariant.

Injection constraint (t-injectivity):
  t restricted to K_R is injective:
    ∀k1, k2 ∈ K_R: t(k1) = t(k2) → k1 = k2.
  Reason: registration events within K_R are identified by their timestamp;
  two distinct k cannot share t within the same K_R. This is a definitional
  property of the registration process: if two acts share a timestamp in K_R,
  they are the same registration act. The constraint is required for K2
  totality and RegistrationState well-definedness (see K2).

K_R is produced by registering system R over time.
K_R is finite or countably infinite (a consequence of K2 discreteness — see K2 S2-Δ lemma).
```

| Property | Value |
|---|---|
| **Source** | Level 3: K-state tuple from `meta_architecture/vvv_qmrf_meta_architecture_registration_layer_formalization.md` §1 |
| **BE lineage** | Pramāṇa — cognition as structured event: act (pramāṇa), object (prameya), self-awareness (svasaṃvedana), result (phala), validity |
| **Claim class** | C (conjectural VVV-QMRF formal definition) |
| **Dependency** | Level 3 (K-state tuple). No Level 4 dependency. |
| **Boundary** | `K_R` is not a Hilbert space, not a set of physical density matrices, not a probability space. Elements `k` are registration states — they record what was registered, not what physically exists. The `o = ∅` slot is reserved for E9 (null event) and E14 (validated absence). K4 operationalizes E9 via the `isNull(k) := o(k) = ∅ ∧ ΔI(k) = 0` guard (cert=1 ∧ isNull(k) → V=0 by definition); E14 (validated absence) accommodation is structural only (see Open Item #3). |
| **Consistency** | K1 is consistent with K ≠ H (Level 1). The carrier set contains registration tuples, not physical states. |

### AXIOM K2 — Temporal Order / Thứ tự Thời gian

**Statement:**
> (K_R, <_R) is a strict total order (chain) where k1 <_R k2 iff t(k1) < t(k2) for k1, k2 ∈ K_R produced by the same registering process R. Within a single K_R, all registration events are comparable via their timestamps. The order is discrete: between any two consecutive registration events k_i and k_{i+1}, there is no K-side registration-state identity.
>
> **Clarification on order type:** Within a single K_R, the order is **total** (every pair of elements is comparable) because all elements share the same timestamp space T_R. The term "partial order" applies only when considering the **cross-K-space** setting: elements from different K_R, K_{R'} with independent timestamp spaces are NOT comparable. K2 axiomatizes the intra-K_R case, which is a strict total order. The inter-K-space partial order emerges in T1 (K_joint construction) where independent timestamp spaces are combined.

**Formal:**
```
For all k1, k2 ∈ K_R:
  k1 <_R k2  iff  t(k1) < t(k2)

(K_R, <_R) is a strict total order (chain):
  (i)    Irreflexive:   ¬(k <_R k)
  (ii)   Transitive:    k1 <_R k2  ∧  k2 <_R k3  →  k1 <_R k3
  (iii)  Asymmetry:     k1 <_R k2  →  ¬(k2 <_R k1)     [follows from (i)+(ii)]
  (iv)   Totality:      ∀k1, k2 ∈ K_R, k1 ≠ k2  →  k1 <_R k2  ∨  k2 <_R k1
                        [all elements comparable — follows from K1 t-injectivity]

  Totality proof (from K1 injection constraint):
    Take k1, k2 ∈ K_R with k1 ≠ k2.
    By K1 t-injectivity: t(k1) ≠ t(k2).
    By T_R strict total order: t(k1) < t(k2)  ∨  t(k2) < t(k1).
    By <_R definition: k1 <_R k2  ∨  k2 <_R k1.  ∎

Discreteness (S2-Δ lemma):
  Define: RegistrationState: T_R → (K_R ∪ {∅})
          RegistrationState(t) = k    if ∃k ∈ K_R with t(k) = t
          RegistrationState(t) = ∅    otherwise
  (Well-defined: K1 t-injectivity guarantees at most one k per distinct t in K_R;
   K2 strict total order then ensures the map is well-defined.)
  For any consecutive pair k_i, k_{i+1} ∈ K_R with no k' such that k_i <_R k' <_R k_{i+1}:
    ∀t ∈ (t(k_i), t(k_{i+1})),  RegistrationState(t) = ∅
```

| Property | Value |
|---|---|
| **Source** | Level 2: E6 (Registering-System-as-Process) + S2-Δ lemma |
| **BE lineage** | Kṣaṇabhaṅgavāda — momentariness: registration time is discrete; no continuous registration identity between events |
| **Claim class** | D (proposed) |
| **Dependency** | Level 2 (E6, S2-Δ). No Level 4 dependency. |
| **Boundary** | Does NOT claim physical time is discrete. Only registration-time is discrete within K_R. Physical time in H remains continuous as per Standard QM. The "no registration-state identity between events" is a K-side property, not a claim about physical continuity. |
| **Order type note** | Within a single K_R, the order is **strict total** (chain), not merely partial. The partial-order structure emerges only in the cross-K-space setting (K_joint, T1). Previous versions mislabeled this as "strict partial order" — corrected in v1.2. |
| **Consistency** | K2 is consistent with E6's definition of R as an ordered sequence {M_1, ..., M_n} with t(M_1) < ... < t(M_n). E6's total ordering of the sequence confirms strict totality. The discreteness clause directly instantiates the Δ lemma. |

### AXIOM K3 — Self-Certification / Tự chứng nhận

**Statement:**
> For each k ∈ K_R, the certification marker cert(k) = σ_R(M) ∈ {0,1} is determined intrinsically within K_R, not by any external registration act M' ≠ M and not by any registering system R' ≠ R. σ_R(M) = 1 iff M has occurred as a K-side registration event of R.

**Formal:**
```
Act-token convention:
  M_K is a set of measurement-registration act TOKENS (unique event identifiers).
  Two registration events of the same act-type but different timestamps are
  distinct M_K members: token(M_1) ≠ token(M_2) even if type(M_1) = type(M_2).
  K5 and T1 apply token-level reasoning; act-type reasoning requires separate notation.

σ_R: M_K → {0,1}

σ_R(M) = 1  iff  M has occurred as a K-side registration event of R,
                 and this occurrence is determined intrinsically within K_R.

For all k ∈ K_R:
  cert(k) = σ_R(M)                                    [cert tracks self-certification]

Observer-indexed independence:
  σ_R(M) is independent of σ_{R′}(M′) for any R′ ≠ R.
  σ_R(M) does not require ∃M′ ≠ M such that σ_{M′}(M) = 1.

Reflexivity (E1 core property):
  The certification of M's occurrence is part of M's own K-side instantiation.
  No second-order meta-registration chain is required on the K-side.
```

| Property | Value |
|---|---|
| **Source** | Level 2: E1 (Self-Certifying Registration) |
| **BE lineage** | Svasaṃvedana — self-awareness/self-certifying cognition: a cognition certifies its own occurrence without requiring a second-order cognition |
| **Claim class** | D (proposed) |
| **Dependency** | Level 2 (E1). No Level 4 dependency. |
| **Boundary** | σ_R(M) certifies the OCCURRENCE of M as a K-side registration event. It does NOT certify that the physical outcome is true/correct. It is NOT consciousness, NOT a physical detector response, NOT a second-order measurement act. It is a structural property of K-side registration events — the K-side analogue of "the detector clicked" being registered as "the detector clicked" without needing another detector to detect the first detector. |
| **Consistency** | K3 is consistent with E1's definition of σ(M) as intrinsic to M. The observer-indexed extension matches paper v2.0 §3.3. K3 does not require the equivalence of σ(M) and R̂_svasa formalisms (paper v2.0 §7.2 deferred item #4). |

### AXIOM K4 — Default Validity / Tính hợp lệ Mặc định

**Statement:**
> For any k ∈ K_R with ¬isNull(k), the validity status V(k) = 1 upon instantiation of k in K_R. [cert(k) = 1 for all k ∈ K_R by K1 admission rule — not restated here.] Validity is the default state of a non-null registration event; it does not require external confirmation. For isNull(k), V(k) = 0 by K4(b). All k ∈ K_R are covered by one of the two clauses.

**Formal:**
```
isNull(k) :=  o(k) = ∅  ∧  ΔI(k) = 0
              (E9 null event: interaction occurred but zero information transfer)

For all k ∈ K_R:
  (a) ¬isNull(k)  →  V(k) = 1   (upon instantiation: non-null self-certified events
                                  are valid by default)
  (b)  isNull(k)  →  V(k) = 0   (E9 null events: o=∅ ∧ ΔI=0 → zero information
                                  transfer → V=0 by K4 formal convention)

Joint exhaustiveness:
  K1 admission rule (cert=1) + isNull dichotomy partition all k ∈ K_R.
  K4 defines V for both branches: no k has V undetermined by K4.

  [cert(k) = 1 for all k ∈ K_R is guaranteed by K1 admission rule — clause (a) need
   not restate it; it is shown here for clarity and omitted from K5/K7 downstream proofs.]

E9 null registration event — K4(b) explanatory note:
  For k_null ∈ K_R with isNull(k_null):
    cert(k_null) = 1  (self-certified: interaction occurred, K1 admission rule)
    V(k_null) = 0     (K4(b) formal clause — not external commentary)
  The isNull guard excludes k_null from clause (a) — no conflict, no override.

Default rule:
  For non-null k: V(k) starts at 1. No external act is required to establish V(k) = 1.

Provision: V(k) = 1 is provisional until the registration process closes
  (per E7: V_prov vs V_final distinction; see K7 Closure Axiom).
```

| Property | Value |
|---|---|
| **Source** | Level 2: E7 Axiom 1 (Default validity) |
| **BE lineage** | Svataḥ prāmāṇya — intrinsic validity: a cognition is valid by default in virtue of its occurrence (arthakriyā — causal efficacy) |
| **Claim class** | D (proposed) |
| **Dependency** | Level 2 (E7 Axiom 1). No Level 4 dependency. |
| **Boundary** | V(k) = 1 is default K-side registration validity for non-null events. It does NOT mean the physical outcome is correct, does NOT mean the Born-rule probability was calculated correctly, and is NOT absolute metaphysical truth. It only means: within K_R, this registration event is treated as valid until contradicted. The isNull guard (o=∅ ∧ ΔI=0) excludes E9 null events from the `cert=1 → V=1` rule — no override is needed. A null event certifies "interaction occurred" but its outcome is ∅ (zero information) → V=0 by definition, not by K5 contradiction. The provisional/final distinction is formalized in K7 (Closure Axiom). |
| **Consistency** | K4 is consistent with E7 Axiom 1. K4 works with K3: only self-certified events (cert=1) get default validity. Events that fail admission (cert=0) have no validity status defined by this axiom. K4 + isNull guard is compatible with E9: null events are self-certified (interaction occurred) but carry V=0 because outcome information is ∅/zero — the isNull guard excludes them from the `cert=1 → V=1` rule without contradiction. K4 + K3 together: cert=1 (K3 intrinsic) ∧ ¬isNull(k) → V=1 (K4 default). |

### AXIOM K5 — Invalidation / Vô hiệu hóa

**Statement:**
> V(k1) → 0 iff there exists k2 ∈ K_R with k1 <_R k2 such that k2 stands in registered contradiction (⊥) to k1 within a shared K-side comparison context C_K, and k2 has valid cross-registration authority with respect to k1. Validity cannot be externally confirmed (only contradicted). Pre-closure: V_prov(k1) → 0 is reversible in principle if the contradicting act is itself invalidated before process closure (K7). Post-closure: V_final(k1) → 0 is irreversible and absolute. *(Note: "k2 ∈ K_R" has two readings — native intra-K_R and cross-space via K_joint. See K_R disambiguation in formal block below.)*

**Primitive predicate definitions:**

1. **Registered Contradiction (⊥) — minimal operational definition:**
   > For k1, k2 ∈ K_R within a shared comparison context C_K: `k2 ⊥ k1` holds iff the registration contents o(k1) and o(k2) cannot both be treated as valid K-side claims within the same C_K. This is a registration-layer contradiction, NOT a physical contradiction (ρ-side), NOT logical inconsistency in Standard QM, and NOT a claim that either physical event failed to occur.
   >
   > Minimal condition: `k2 ⊥ k1` when:
   > - k1 registers a definite outcome `o(k1) = φ` (e.g., `|h⟩⟨h|` or `|0⟩`)
   > - k2 registers a content in which `φ` is not preserved as a valid claim (e.g., superposition `|ψ⟩ ≠ |h⟩` or complementary outcome `|1⟩`)
   > - The validity of both claims cannot be simultaneously maintained without contradiction.
   >
   > Full formalization of ⊥ conditions (including boundary clauses: not physical erasure, not null event, not invalid when both sides are independently valid) is in Level 4 (paper v2.0 §4.4). The above minimal definition is sufficient for K5 operational closure.

2. **Comparison Context (C_K):**
   > A comparison context C_K is a K-side structure in which registration contents from multiple K-state tuples are evaluated for mutual consistency. C_K is defined by the D_joint demand (Level 4, §4.3): a C_K exists iff `requires_K_joint` = 1 for the relevant K-spaces.

3. **Cross-Registration Authority — deferred to K6:**
   > The "valid cross-registration authority" condition is formalized in Axiom K6 below.

**Formal:**
```
Firing precondition:
  C_K must exist — i.e., requires_K_joint = 1 for the relevant K-spaces (Level 4, §4.3).
  K5 is a cross-observer invalidation rule: it fires only in joint-registration
  (K_joint) contexts. When requires_K_joint = 0, no C_K exists, condition (ii)
  is undefined, and K5 does not fire.

V(k1) → 0  iff  ∃k2 ∈ K_R such that:

  (i)   k1 <_R k2                                    [K2: k2 is later in registration order]
  (ii)  k2 ⊥ k1  within shared C_K                    [registered contradiction in comparison context]
  (iii) k2 has valid cross-registration authority      [authority conditions from paper v2.0 §4.4]
        with respect to k1 in C_K

Asymmetry (E7 Axiom 3, post-closure):
  Post-closure: ¬∃F such that F(k′) → V_final(k) = 1.
  (No external function can restore V_final once K7 closes.)
  Pre-closure: V_prov(k) can return to 1 if the K5 trigger k2 is itself invalidated
  before closure — this is reversibility, not a violation of asymmetry.
  The asymmetry guarantee is absolute only for V_final (post-closure K7).

Validity stages (K7):
  V_prov(k)  — provisional validity, during open registration process (pre-closure)
  V_final(k) — final validity, after registration process closes (post-closure)
  K5 conditions (i)-(iii) govern V_prov transitions during the open process.
  V(k) in K5 refers to V_prov(k) pre-closure and V_final(k) post-closure.

Irreversibility (post-closure only):
  V_final(k) → 0  ⇒  V_final(k) remains 0 permanently.
  (After registration process closes (K7), invalidation is absolute and cannot be revised.)

Pre-closure (K7):
  V_prov(k) → 0 is in principle reversible: if the contradicting act k2 is itself
  invalidated (V(k2) → 0) before process closure (K7), the K5 trigger for k1 is
  removed and V_prov(k1) is no longer forced to 0. Governed by K7 — pre-closure
  K5 transitions are not final.

Reversibility corollary (explicit revert path — corollary of biconditional iff):
  Step 1: If ∃k2 satisfying (i)+(ii)+(iii) → V_prov(k1) = 0.   [K5 fires]
  Step 2: If k2 itself later invalidated: V(k2) → 0 before K7 closure
          → condition (iii) "k2 has valid cross-registration authority" fails for k2.
  Step 3: If no other k2′ satisfies all of (i)+(ii)+(iii) for k1
          → ¬∃k2 satisfying (i)+(ii)+(iii)
          → K5 biconditional LHS: V_prov(k1) = 0 no longer holds
          → V_prov(k1) reverts to K4 default: V_prov(k1) = 1.
  Mechanism: V_prov(k1) is re-evaluated via biconditional, not "stuck at 0".
  The notation "→ 0" describes a state assignment governed by iff, not a
  one-way imperative transition. Sticky-at-0 reading is incorrect for V_prov.

K_R disambiguation (cross-space context):
  When C_K exists (requires_K_joint = 1), the quantifier ∃k2 ∈ K_R operates over
  the relevant subspace of K_joint: k2 may originate from a different K-space K_X
  and appears as i_X(k2) ∈ K_joint. The concrete model (§7) uses i_W(k_W) ∈ K_joint
  — the operative reading of K_R is K_joint when C_K exists. In isolated scenarios
  (requires_K_joint = 0, no C_K), K5 does not fire because condition (ii) is
  undefined (no C_K to evaluate ⊥ within).
```

| Property | Value |
|---|---|
| **Source** | Level 2: E7 Axioms 2-3 (Invalidation + Asymmetry) |
| **BE lineage** | Parataḥ prāmāṇya — invalidity is detected extrinsically. Bādhaka pramāṇa — a contradicting cognition (bādhaka) retroactively voids the earlier cognition. |
| **Claim class** | D (proposed) |
| **Dependency** | Level 2 (E7 Axioms 2-3). Uses `⊥` and "cross-registration authority" as **primitive predicates** whose full formalization is in Level 4 (paper v2.0 §4.4). K5 asserts the structural rule; the precise conditions for `k2 ⊥ k1` and "valid cross-registration authority" are defined in the bridge theorems (T1-T3). **2nd-order Layer 2 dependencies — Dep-A:** C_K existence precondition requires Level 4 predicate `requires_K_joint = 1` (Level 4 §4.3); K5 does not fire when C_K is absent (also reflected in Layer 1 Summary K5 row Role 1, via F4). **Dep-B (F7a non-circularity guard):** K5 condition (i) is defined natively by K2's `<_R` ordering. In cross-space application, K5 can only be evaluated after a candidate `K_joint` has already been constructed. T1 constructs `<_joint>` from K2 native orders + Level 4 cross-structure temporal relations + K8 field preservation; K5 does not define or prove `<_joint>`. Therefore Dep-B is an application-order dependency only: K5 uses `<_joint>` inside `K_joint` after T1 supplies the candidate joint order, so no circular dependency is introduced. |
| **Boundary** | K5 is a registration-layer invalidation rule. It does NOT claim that the physical outcome of M_1 is retroactively erased from ρ-side history. The physical interaction I_1 still occurred; only its K-side registration validity is revised. The `⊥` relation is NOT physical orthogonality in H. The irreversibility of V→0 is a K-side property, not a claim about physical time asymmetry. |
| **Consistency** | K5 is consistent with E7 Axioms 2-3 and with the act-level contradiction definition in paper v2.0 §4.4. The primitive predicates (⊥, C_K, cross-registration authority) now have minimal operational definitions: ⊥ is defined above in K5, C_K is tied to requires_K_joint, and authority is formalized in K6 below. This removes the prior dependency inversion where frozen K5 relied on undefined Level 4 primitives. |

### AXIOM K6 — Cross-Registration Authority / Thẩm quyền Chéo

**Statement:**
> For k1, k2 ∈ K_R with k1 <_R k2, k2 has valid cross-registration authority with respect to k1 in comparison context C_K iff: (a) both k1 and k2 belong to the same C_K, (b) V(k2) = 1 at the time of the authority check (k2 has not itself been invalidated), and (c) the validity demand D_joint that defines C_K includes the claim-content of k1 within its scope. Cross-registration authority is NOT a hierarchy of observers; it is a structural relation within a shared comparison context.

**Formal:**
```
Auth(k2 → k1, C_K) = 1  iff  all of:

  (a)  C_K-sphere(k1) = C_K-sphere(k2)      [both belong to same C_K]
  (b)  V(k2) = 1                             [k2 not invalidated at check time]
  (c)  k1 ∈ scope(D_joint)                   [k1's claim falls within D_joint scope]

  where:
    C_K-sphere(k) is the comparison context that k belongs to.
    scope(D_joint) is the set of registration acts whose claims D_joint demands
    joint validity evaluation for.

Notation note:
  Auth(k2 → k1, C_K) is an INSTANCE-LEVEL relation, not a global direction.
  Auth(k1 → k2, C_K) may hold simultaneously when both k1, k2 are valid within
  the same C_K — mutual authority is permitted. The arrow "k2 → k1" reads
  "k2 has authority with respect to k1 in this instance", not "k2 always ranks
  above k1". K5 applies Auth with temporal direction (k1 <_R k2) — directionality
  is imposed by K5, not by K6 itself.

Auth is NOT:
  - Observer hierarchy (no "Wigner over Friend" privilege)
  - Physical measurement authority (not a ρ-side property)
  - Absolute epistemic authority (bound to C_K, not universal)
  - Transitive across distinct C_K contexts:
      Auth(k2→k1, C_K) ∧ Auth(k3→k2, C_K') ⇏ Auth(k3→k1, ·)  [when C_K ≠ C_K']
      Note: within a single shared C_K the formal block does not exclude transitivity.

Non-transitivity proof sketch (counterexample):
  Consider three registration events k1, k2, k3 ∈ K_R with k1 <_R k2 <_R k3,
  and TWO distinct comparison contexts C_K and C_K':

  Setup:
    - Auth(k2→k1, C_K) = 1:  k1, k2 ∈ C_K, V(k2)=1, k1 ∈ scope(D_joint of C_K).
    - Auth(k3→k2, C_K') = 1: k2, k3 ∈ C_K', V(k3)=1, k2 ∈ scope(D_joint of C_K').
    - But k1 ∉ C_K' (k1 is not in the second comparison context).

  Claim: Auth(k3→k1, ·) = 0 in BOTH contexts:
    - In C_K:  k3 ∉ C_K  → condition (a) fails → Auth(k3→k1, C_K) = 0.
    - In C_K': k1 ∉ C_K' → condition (a) fails → Auth(k3→k1, C_K') = 0.

  Therefore: Auth(k2→k1, C_K) ∧ Auth(k3→k2, C_K') holds (C_K ≠ C_K'), but
  Auth(k3→k1, ·) = 0 in every available comparison context. ∎

  Scope: this counterexample proves non-transitivity across distinct C_K contexts
  (C_K ≠ C_K'). It does not claim non-transitivity within a single shared C_K.

  ⚠ Intra-C_K transitivity and K5 invalidation chains (PG-07):
  Even if Auth is transitive within a single shared C_K — i.e., Auth(k2→k1, C_K)=1
  and Auth(k3→k2, C_K)=1 could in principle yield Auth(k3→k1, C_K)=1 — this does
  NOT enable transitive K5 invalidation chains. K5 requires an INDEPENDENT ⊥_K
  relation for each pair: V(k1)→0 requires Auth(k2→k1, C_K)=1 checked atomically
  at the moment of invalidation. The transitivity of Auth within C_K provides no
  shortcut: k3 cannot void k1 merely because k3 has authority over k2 and k2 has
  authority over k1. Each K5 invalidation step is an independent check; no chain
  propagation is implied by Auth transitivity alone.

  Physical intuition: Authority is context-bound. Two different D_joint demands
  create two different comparison scopes. Transitivity would require a single
  C_K containing all three events with overlapping scope — which is not
  guaranteed by the pairwise authority relations.
```

| Property | Value |
|---|---|
| **Source** | Level 2: E7 Axiom 2 + paper v2.0 §4.4 cross-registration authority section |
| **BE lineage** | Bādhaka pramāṇa — a contradicting cognition must be a valid cognition (pramāṇa) itself to serve as bādhaka. An invalid cognition cannot void another. |
| **Claim class** | D (proposed) |
| **Dependency** | Level 2 (E7 Axiom 2). Uses `C_K` and `D_joint` from Level 4 with three Auth roles: (1) existential precondition — K6 operates only when C_K exists (requires_K_joint = 1); (2) C_K-sphere membership parameter (condition a); (3) D_joint scope parameter (condition c). **Dep-A (2nd-order Layer 2 dependency):** Auth(k2→k1, C_K) requires C_K to exist (requires_K_joint = 1, Level 4 §4.3); K6 does not operate when C_K is absent — analog K5 Dep-A. **Conditional semantic dependency (I-03 pattern):** condition (c) `k1 ∈ scope(D_joint)` means Level 4 changes to D_joint scope alter which k1 have Auth = 1, without altering K6 text (syntactic freeze holds); analogous to K5 ⊥_K boundary clauses (I-03/F3). |
| **Boundary** | Auth is a K-side structural relation within C_K. It does NOT create observer hierarchy, does NOT grant absolute epistemic privilege, and is NOT a claim about physical measurement authority. Two observers in the same C_K may have mutual authority (symmetric) when both are valid. Authority is lost the moment V(k2) → 0 (K5). |
| **Consistency** | K6 operationalizes K5's condition (iii) — "valid cross-registration authority" is no longer an undefined primitive. K6 is consistent with E7 Axiom 2's extrinsic invalidation: a contradicting act must itself be valid. K6's non-transitivity preserves the pair-wise nature of authority checks. |

### AXIOM K7 — Registration Process Closure / Đóng Quá trình Ghi nhận

**Statement:**
> The registration process R of K_R closes at registration time t_close when no pending `requires_K_joint` demands remain for any pair of K-spaces involving K_R. At closure, for all k ∈ K_R: V(k) transitions from provisional status V_prov(k) to final status V_final(k). After closure: (a) no new k can be instantiated in K_R, (b) K5 irreversibility becomes absolute (V(k)→0 cannot be revised by any future event), (c) no new D_joint involving K_R can be raised, and (d) K_joint involving K_R becomes final (no reconfiguration of the joint space is permitted). Before closure, all V(k) are provisional and subject to K5 invalidation.

**Formal:**
```
R closes at t_close(K_R) iff:
  ∀ pairs (K_R, K_X) where X is any registering system:
    pending(K_R, K_X) = ∅

  where pending(K_R, K_X) is the set of unresolved requires_K_joint demands
  whose D_joint involves both K_R and K_X.

At closure:
  For all k ∈ K_R:
    V_prov(k) → V_final(k)     [provisional → final]

Post-closure properties:
  (a)  K_R is closed under new k:  ∄k_new ∈ K_R with t(k_new) > t_close
  (b)  K5 irreversibility is absolute: V_final(k) = 0 → V_final(k) stays 0 permanently
  (c)  No new D_joint(K_R, ·) can be raised
  (d)  K_joint involving K_R becomes final (no reconfiguration)

Pre-closure:
  All V(k) are V_prov(k). K5 invalidation transitions modify V_prov.
  The V_final value for each k is the limit of V_prov(k) as t → t_close.

  Stabilization condition (V_final well-definedness):
    Within any compact time interval [t_start, t_close], the number of K5
    validity transitions for any k ∈ K_R is finite (finiteness of K_R and
    of the set of K5 triggers ensures this). Therefore V_prov(k) stabilizes
    before t_close, and V_final(k) = lim_{t → t_close^-} V_prov(k) is
    well-defined.

  Equivalent formulation:
    V_final(k) := V_prov(k) at t = t_close (value at exact closure time).
    This is consistent with the limit: the final value equals the stabilized
    pre-closure value.
```

| Property | Value |
|---|---|
| **Source** | Level 2: E7 (V_prov vs V_final distinction, paper v2.0 §2.2) |
| **BE lineage** | Niścaya (ascertainment/determination) — a cognition becomes determinate when the cognitive process reaches closure; before that, it is provisional (saṃśaya — doubt is possible) |
| **Claim class** | D (proposed) |
| **Dependency** | Level 2 (E7 V_prov/V_final distinction). Uses `requires_K_joint` and `D_joint` from Level 4 as closure condition inputs. **Dep-B (2nd-order Layer 2 dependency):** K7 closure condition `pending(K_R, K_X) = ∅` uses the concept of "resolved demand" — a requires_K_joint demand is resolved when a K_joint registration event satisfying T2 AdmJoint conditions has occurred; without T2, "resolved" is an undefined primitive in K7; T2 is a silent Layer 2 dependency for closure semantics — analog K5 Dep-B (T1 `<_joint` for K5 condition (i)). **Conditional semantic dependency (I-03 pattern):** Level 4 extensional scope of `requires_K_joint` (which event types require joint registration) directly determines t_close timing — expanding the scope delays closure, narrowing it advances closure; K7 text is frozen but t_close (and therefore when V_prov → V_final and when K5 irreversibility becomes absolute) depends on Level 4 content; analogous to K5 ⊥_K boundary clauses (I-03/F3) and K6 D_joint scope (I-03/F6a). |
| **Boundary** | K7 defines when the K-side registration process closes. It does NOT claim the physical interaction has ended, does NOT claim the H-space state has reached a final value, and does NOT claim that all possible measurements have been completed. Closure is a K-side property: no more joint validity demands are pending. In practice, t_close may be identified with the end of an experimental protocol, the publication of results, or any agreed-upon endpoint of the registration process. |
| **Consistency** | K7 resolves the "provisional" gap in K4 and K5. K4's default validity is provisional until closure; K5's irreversibility is provisional until closure, then absolute. K7 is consistent with E7's distinction between V_prov and V_final. K7 does not conflict with K5: pre-closure K5 transitions are reversible in principle (if the contradicting act is itself invalidated before closure), but post-closure K5 transitions are absolute. |

### AXIOM K8 — Cross-Space Embedding Preservation / Bảo toàn qua Phép nhúng

**Statement:**
> For any embedding i_{R→X}: K_R → K_X that maps a K-state tuple k ∈ K_R into a joint or cross K-space K_X, the embedding preserves the validity value V(k) at the moment of embedding: V_X(i_{R→X}(k)) = V_R(k) at embedding time t_embed. Furthermore, the embedding preserves the remaining tuple fields (M, o, cert, t) unchanged. After embedding, V_X(k) evolves independently within K_X according to K4-K7 — the embedding preserves the initial validity snapshot, not immunity from future invalidation.

**Formal:**
```
For any embedding i: K_R → K_X (where K_X may be a joint K-space K_joint
or any cross-space structure):

  (i)   V-preservation (Embedding Postulate):
        V_X(i(k)) = V_R(k)  at t_embed  for all k ∈ K_R
        (V-value carries over into K_X at the moment of embedding.)

  (ii)  Field preservation:
        M_X(i(k)) = M_R(k)      [act identifier preserved]
        o_X(i(k)) = o_R(k)      [registered outcome preserved]
        cert_X(i(k)) = cert_R(k) [self-certification marker preserved]
        t_X(i(k)) = t_R(k)      [registration timestamp preserved]

        ΔI auxiliary (E9 derivability):
        ΔI(k) is determined by M(k) and o(k) per E9 definition — it is an
        auxiliary quantity, not an additional tuple field. Because (ii) preserves
        M and o exactly, ΔI is automatically preserved: ΔI(i(k)) = ΔI(k).
        Consequence: isNull(k) = [o(k)=∅ ∧ ΔI(k)=0] is preservation-invariant
        across embedding — null status cannot flip from K_R to K_X via K8.

  (iii) Post-embedding evolution:
        After t_embed, V_X(i(k)) evolves according to K4-K7 rules
        within K_X. K8 does NOT immunize against future K5 invalidation
        in K_X. It only guarantees that the embedding itself does not
        alter V — the embedded element enters K_X with its native validity
        intact, then stands or falls by K_X's own validity dynamics.

  (iv)  Non-redundancy:
        K8 is NOT derivable from K4. K4 governs V upon instantiation
        within a native K_R — it is silent on cross-space embedding
        behavior. K8 is an independent postulate about the behavior
        of V under the embedding operation. A framework without K8
        (or an equivalent postulate) cannot guarantee that embedded
        registration acts retain their validity status.

        Counter-model (K4 holds, K8 fails):
          Let K_F = { k_F } with V_F(k_F) = 1 (K4 satisfied at
          native instantiation in K_F).
          Define embedding i: K_F → K_joint where the embedding
          operation assigns V_joint(i(k_F)) = 0 (validity dropped
          on transfer).
          K4 is satisfied in K_F: cert(k_F) = 1 ∧ ¬isNull(k_F)
          → V_F(k_F) = 1.  ✓
          K8 fails: V_joint(i(k_F)) ≠ V_F(k_F).  ✗
          Therefore K4 ⊬ K8. K8 is an independent postulate. □
```

| Property | Value |
|---|---|
| **Source** | Architectural necessity identified during T1 construction: K1-K7 alone cannot guarantee V-preservation through cross-space embeddings because K4 only governs V upon instantiation within a native K_R. Formerly tracked as "Embedding Postulate (EP)" — an external postulate required by T1. Promoted to K8 (v1.4) to make the axiom set self-contained. |
| **BE lineage** | Anugama (continuity/attendant relation) — the validity of a cognition accompanies it when the cognition is taken up in a broader cognitive context; the cognition does not lose its epistemic status merely by being embedded in a larger framework |
| **Claim class** | D (proposed) |
| **Dependency** | Level 0-3 (K1 tuple structure, K4 default validity). No Level 4 dependency. |
| **Boundary** | K8 is a structural postulate about the embedding operation itself, not about the native K-spaces being embedded. It guarantees snapshot preservation, not permanent immunity. After embedding, K5 can still fire in K_X and invalidate i(k). K8 does NOT claim that V-values are absolutely invariant under all operations — only that the embedding map i itself does not alter them. |
| **Consistency** | K8 is consistent with K4: K4 defines validity at native instantiation, K8 defines validity-preservation at cross-space transfer. They govern different moments. K8 is consistent with K5: K8 guarantees the initial V snapshot in K_X, but K5 can still transition V_X(i(k)) → 0 afterwards — the embedded element inherits both rights (default validity) and liabilities (future invalidation) of its new home. K8 + K1 together guarantee that the embedded tuple maintains its identity (5-field structure) across spaces. |

### Layer 1 Summary / Tổng kết Tầng 1

| Axiom | Content | Fields covered | Source level | Freeze status | Level 4 dependency | Layer 2 theorem dep. (semantic) |
|---|---|---|---|---|---|---|
| K1 | Carrier set — K_R is a set of 5-field tuples | M, o, cert, t, V | Level 3 | Frozen | None | None |
| K2 | Temporal order — strict total order (chain) within K_R, discrete; RegistrationState defined | t (ordering) | Level 2 | Frozen | None | None |
| K3 | Self-certification — σ_R(M) intrinsic to R | cert | Level 2 | Frozen | None | None |
| K4 | Default validity — V=1 on instantiation for ¬isNull(k); E9 covered by isNull guard (no override) | V (default) | Level 2 | Frozen | None | None |
| K5 | Invalidation — V→0 by later ⊥ with authority; minimal ⊥ definition included | V (transition) | Level 2 | Frozen (syntactic) | C_K roles: (1) existential precondition — K5 fires only when C_K exists (requires_K_joint = 1); (2) ⊥ evaluation parameter (condition ii); (3) Auth evaluation parameter (condition iii) | **T1** (Dep-B): `<_joint` ordering used by K5 inside K_joint is constructed by T1; K5 applied only after T1 candidate K_joint exists |
| K6 | Cross-registration authority — structural relation within C_K, non-hierarchical | V (authority condition) | Level 2 | Frozen (syntactic) | C_K roles: (1) existential precondition for all Auth checks; (2) C_K-sphere membership parameter (condition a); (3) D_joint scope parameter (condition c) | None direct |
| K7 | Registration process closure — V_prov → V_final, absolute irreversibility | V (closure) | Level 2 | Frozen (syntactic) | Uses requires_K_joint for pending check only | **T2** (Dep-B): "resolved demand" semantics (when pending = ∅) requires T2 AdmJoint resolution definition; K7 closure timing depends on T2 |
| K8 | Cross-space embedding preservation — V preserved at embedding time; fields preserved | V (embedding) + M, o, cert, t | Level 3 | Frozen | None | None |

**Dependency isolation:** K1-K8 depend ONLY on Level 0-3 (BE SOT, K≠H, E1-E7, K-state tuple). Where K5-K7 reference Level 4 concepts (C_K, D_joint, requires_K_joint), they reference them for **scope identification only** (e.g., "is k1 in the same C_K as k2?"), not for their internal structure or definition.

**Syntactic freeze (unconditional):** K1-K8 text is frozen. If paper v2.0 community feedback changes the internal structure of AdmJoint, K1-K8 do not change — AdmJoint appears only in bridge theorems T1-T4, not in any K1-K8 axiom text.

**Layer 2 semantic dependencies (K5, K7):** "Frozen (syntactic)" means the axiom TEXT is frozen. The SEMANTIC BEHAVIOR of K5 (when it fires via `<_joint`) and K7 (when closure occurs via "resolved demand") depends on Layer 2 theorems T1 and T2 respectively. If T1 or T2 are updated (pending Level 4 freeze), K5/K7 semantics may shift even though K5/K7 text does not change. This is an application-order dependency (T1/T2 supply inputs K5/K7 consume), not a logical circularity. K1-K4 and K8 carry no Layer 2 semantic dependencies.

**Semantic dependency for ⊥_K (conditional):** K5 minimal ⊥ definition provides K5-local operational closure. However, Level 4 §4.4 boundary clauses ("not null event", "not invalid when both sides independently valid") narrow K5 minimal ⊥ and constitute a real semantic dependency: if these boundary clauses change, K5 fires in a different set of cases even though K5 text is unchanged. The syntactic freeze guarantee holds unconditionally; the semantic behavior guarantee for K5 is conditional on Level 4 ⊥ boundary clauses remaining a conservative extension of K5 minimal ⊥ (adding scope, not contradicting it). Only bridge theorems T1-T3 need updating for structural Level 4 changes.

---

## 2. Bridge Theorems — Layer 2 (Updatable) / Định lý Cầu nối — Tầng 2

**Status note:** Theorems T1-T3 are **pending Level 4 freeze** (paper v2.0 in community review). They connect K1-K8 to the paper's structural definitions. If Level 4 definitions change, T1-T3 are updated independently of K1-K8. T4 is new (Class D).

### T1 — K_joint Construction Theorem

**Statement:**
> Given K-side spaces K_A and K_B of registering systems A, B: if requires_K_joint(A, B) = 1 via a shared validity demand D_joint, then a candidate joint K-space K_joint(A, B) exists as the categorical colimit of the embedding diagram (K_A, K_B with structure-preserving morphisms). Equivalently: K_joint is the smallest K-space (up to isomorphism) containing order-preserving embeddings i_A: K_A → K_joint and i_B: K_B → K_joint that preserve cert and V values — "smallest" meaning minimal w.r.t. inclusion of K1-K8 structure, not minimal in cardinality. The embedding respects the internal time-order of each structure, and the combined order in K_joint is the transitive closure of the two embedded orders plus cross-structure temporal relations from the shared laboratory history. See T4 for the N-observer colimit generalization.

**Derivation — Layer 1 inputs + Level 4 inputs (composition, not pure derivation):**

> **Architectural note (F-RCA-P4-02):** T1 is a *composition theorem*, not a pure Layer 1 derivation. It combines Layer 1 axioms (K1-K8) with Level 4 inputs (D_joint context, cross-structure temporal relations). The cross-structure temporal relations encode physical laboratory history — a fact external to K-space axioms. T1 constructs `<_joint` from these two input streams; it does NOT derive cross-rel from K1-K8 alone.

```
Layer 1 inputs (K1-K8):
  - K1: K_A, K_B are sets of tuples → K_joint carrier = i_A(K_A) ∪ i_B(K_B)
  - K2: each K-space has native temporal order <_A, <_B (chains)
  - K3: embeddings i_A, i_B preserve cert values
  - K6: cross-registration authority evaluated within C_K defined by D_joint
  - K8: embeddings preserve V values at embedding time
        (V_X(i(k)) = V_R(k) at t_embed — K8 replaces former external EP; axiom
        set now self-contained for V-preservation)

Level 4 inputs (D_joint context — external to K1-K8):
  - requires_K_joint(A, B) = 1 via shared validity demand D_joint (§4.3)
  - cross-structure temporal relations (cross-rel) from shared laboratory history:
    e.g., t_F < t_W established by experimental protocol, not derivable from K1-K8
  - C_K specification for authority context

Composition:
  <_joint = (i_A(<_A) ∪ i_B(<_B) ∪ cross-rel)^+   [transitive closure]

Order type of <_joint:
  (K_joint, <_joint) is a PARTIAL ORDER (not necessarily total).
  Restricted to each image i_X(K_X): <_joint is a CHAIN (preserved from <_X by K2).
  Across distinct images i_A(K_A) and i_B(K_B): <_joint is PARTIAL — elements are
  comparable only through explicit cross-rel from Level 4 D_joint or transitive chain.
  (See K2 dòng Order type note: partial-order structure emerges at cross-K-space level.)
  T4 extends this to N-observer colimit: the colimit order is also partial in general.

  K_joint(A,B) exists as a candidate K-space with this combined order,
  preserving K1 carrier structure + K2 intra-order + K3 cert + K8 V.

Note: existence of a candidate K_joint does NOT guarantee admissibility.
Admissibility requires AdmJoint conditions (i)-(v) to hold (Level 4, §4.3).

F7a non-circularity guard:
  T1 does not depend on K5 Dep-B. K5 is evaluated only AFTER a candidate
  K_joint with <_joint exists. Dependency direction:
    [K1/K2/K3/K6/K8] + [Level 4 cross-rel + D_joint]
      → T1 candidate K_joint / <_joint
        → K5 application inside K_joint.
  No circularity: T1 supplies inputs K5 consumes; K5 does not supply inputs T1 needs.
```

| Property | Value |
|---|---|
| **Level 4 dependency** | `requires_K_joint` predicate, `D_joint` definition (paper v2.0 §4.3). K6 authority structure. |
| **Layer 1 dependency** | K8 (cross-space embedding preservation) — V-preservation is now derived from a core axiom, not an external postulate. **Former EP gap (G1) resolved by promoting EP → K8 (v1.4).** |
| **Claim class** | D (proposed) |
| **Freeze status** | Pending Level 4 freeze |
| **Update trigger** | If `requires_K_joint` definition changes or AdmJoint embedding conditions change |

### T2 — ⊥_K Derivation Theorem

**Statement:**
> For K-side spaces K_A and K_B: K_A ⊥_K K_B holds iff requires_K_joint(A, B) = 1 AND no admissible K_joint exists satisfying AdmJoint conditions (i)-(v) while preserving K4 (default validity) and K5 (no invalidation) for both embedded sides simultaneously. The incommensurability is traced to a K5 conflict: any candidate K_joint forces V(k_A) → 0 or V(k_B) → 0 while both are claimed as jointly valid.

**Derivation from axioms:**
```
K_A ⊥_K K_B
  ↔ requires_K_joint(A,B) = 1                              [Level 4, §4.3]
  ∧ ¬∃ K_joint: AdmJoint(K_joint; K_A, K_B) = 1             [Level 4, §4.3]

T2 focuses on the case where AdmJoint fails via K5 conflict:
  Under candidate K_joint, ∃k_A ∈ i_A(K_A), k_B ∈ i_B(K_B) such that
  k_B ⊥ k_A within C_K (registered contradiction)            [K5 primitive, Level 4 §4.4]
  AND Auth(k_B → k_A, C_K) = 1 (cross-registration authority) [K6]
  → K5 forces V_prov(k_A) → 0  OR  V_prov(k_B) → 0     [K5 pre-closure]
  → AdmJoint condition (iv) violated                         [Level 4, §4.3]
    (no V_prov invalidation while both are claimed jointly valid
     during the candidate K_joint admissibility check)

F7b timing guard:
  T2's AdmJoint(iv) check is pre-closure. It operates on V_prov because
  K7 assigns V_final only after pending requires_K_joint demands have
  been resolved. Therefore T2 cannot use V_final as the admissibility
  input without creating a timing inversion between T2 and K7.

Note: K5 conflict is a SUFFICIENT condition for AdmJoint failure,
NOT a necessary condition. AdmJoint may fail for other reasons.

Non-K5 failure example (K7 lock path):
  Suppose K_A has already closed at t_close(K_A) before D_joint is raised.
  A new D_joint(K_A, K_B) demands joint registration involving K_A.
  K7 post-closure property (a): no new k can be instantiated in K_A after t_close.
  → Embedding i_A: K_A → K_joint cannot satisfy AdmJoint condition (i) for the
    new acts demanded by D_joint (they cannot exist in closed K_A).
  → AdmJoint = 0 via K7 lock, with NO K5 contradiction required.
  → ⊥_K(K_A, K_B) holds via T2 (⊥_K iff requires_K_joint=1 ∧ ¬∃admissible K_joint),
    but the failure path is K7 closure, not K5 registered contradiction.
In such cases, ⊥_K may still hold, but the derivation trace
differs from the T2 K5-conflict path shown above.

⚠ TEMPORAL DEPENDENCY ACKNOWLEDGMENT:
  T2 derives ⊥_K (incommensurability) from K5 conflict.
  K5 uses ⊥ (registered contradiction) as a primitive predicate.
  The MINIMAL operational definition of ⊥ is given in K5 (Layer 1).
  The FULL formalization of ⊥ conditions is in Level 4 (paper v2.0 §4.4),
  whose precise boundary clauses are NOT yet frozen.

  This is a TEMPORAL DEPENDENCY, not a logical circularity:
    - K5's minimal ⊥ definition (Layer 1) is self-contained and NOT circular.
    - T2 needs Level 4 full ⊥ boundary clauses to complete its derivation in
      the general case. Level 4 is not yet frozen — this is an incompleteness,
      not a self-referential loop.
    - v1.3 CONCRETE MODEL FINDING: The dependency does NOT arise in the
      concrete model (§7.5 Step 4) — K5 minimal ⊥ is directly verifiable
      by content inspection (|h⟩ vs |Ψ+⟩) without invoking Level 4 full ⊥.
    - In the general case: T2 derivation is CONDITIONAL on Level 4 ⊥
      boundary clauses being a conservative extension of K5 minimal ⊥
      (adding scope, not contradicting it). This is a temporal dependency
      that resolves when Level 4 freezes — it is not a logical circle.
    - Resolution path: freeze Level 4 ⊥ boundary clauses independently
      of T2. T2's derivation is then complete without any circularity.
```

Boundary clauses (from paper v2.0 §4.4):
```
  ⊥_K does NOT assert that either physical event fails to occur on the ρ-side.
  ⊥_K does NOT mean either observer's outcome is false within its own K-side.
  ⊥_K is NOT equivalent to Null_K(e) — null registration is separate (E9).
  ⊥_K applies only when both sides are valid/provisionally valid within their own K-side.
```

F7b K7 resolution semantics:
```
  For K7 closure, a requires_K_joint demand is resolved when T2 yields
  one of two admissibility outcomes:

    (1) Success path:
        ∃K_joint such that AdmJoint(K_joint; K_A, K_B) = 1.
        The demand is resolved by successful joint registration.

    (2) Failure path:
        ¬∃K_joint such that AdmJoint(K_joint; K_A, K_B) = 1.
        The demand is resolved as K_A ⊥_K K_B.

  In both cases, the pending demand is no longer open. K7 may then
  evaluate whether pending(K_R, K_X) = ∅. T2 supplies the resolution
  semantics; K7 performs the closure transition from V_prov to V_final.
```

| Property | Value |
|---|---|
| **Level 4 dependency** | `AdmJoint` conditions (i)-(v), `⊥_K` boundary clauses, `D_joint` (paper v2.0 §4.3-4.4) |
| **Layer 1 dependency** | K5 (invalidation rule) + K6 (authority condition) + K8 (V-preservation at embedding) — T2 derivation uses all three. **K8 resolves former EP gap (G1): V-preservation is now derived from a core axiom.** |
| **Claim class** | D (proposed). Derivation trace is Class D; the ⊥_K conclusion matches paper v2.0 Class D definition. |
| **Important** | K5 conflict is a SUFFICIENT condition for AdmJoint failure, not necessary. AdmJoint may fail for other reasons. F7b: AdmJoint(iv) is checked against `V_prov` during pre-closure admissibility testing; `V_final` is assigned only after K7 closure. T2 also supplies K7's "resolved demand" semantics: a demand is resolved either by successful `AdmJoint = 1` or by failure `AdmJoint = 0` producing `⊥_K`. |
| **Freeze status** | Pending Level 4 freeze |
| **Update trigger** | If AdmJoint conditions (i)-(v) change, or ⊥_K boundary clauses are revised |

### T3 — Bridge_EWF Formalization Theorem

**Statement:**
> In an Extended Wigner's Friend configuration where D_joint requires F-side and W-side registrations to support one cross-observer validity constraint, Bridge_EWF(D_joint; M_F, M_W) = 1 is derivable from K5 when: (a) M_F registers a definite friend-side outcome o_F, (b) M_W registers the same laboratory as a coherent superposition in which no definite o_F is preserved as a W-side valid claim, and (c) no reinterpretation inside the same K_joint can preserve both registered contents without changing the validity claim of at least one side.

**Derivation from axioms:**
```
Bridge_EWF(D_joint; M_F, M_W) = 1
  ↔ D_joint requires F-side and W-side registrations to be evaluated
    as jointly valid parts of one laboratory registration history     [Level 4, §4.3]

Temporal precondition (EWF setup — explicit):
  t_F < t_W in laboratory history:
    F measures the particle/friend system first (inside lab, at t_F).
    W performs the interference measurement afterward (on the lab, at t_W).
  This satisfies K5 condition (i): k_F <_R k_W in K_joint via cross-rel
  (K2 native orders + Level 4 cross-rel supply t_F < t_W → i_F(k_F) <_joint i_W(k_W)).
  T3 derivation presupposes EWF temporal ordering; it is not valid for t_W < t_F.

  ∧ M_F: k_F = ⟨M_F, o_F, 1, t_F, 1⟩  (definite outcome, self-certified, valid)
  ∧ M_W: k_W = ⟨M_W, o_W, 1, t_W, 1⟩  (superposition registered, no definite o_F)
  ∧ Under candidate K_joint:
      k_W ⊥ k_F within C_K (registration contents incompatible)       [Level 4, §4.4]
      ∧ k_W has valid cross-registration authority                   [Level 4, §4.4]
      → K5: V(k_F) → 0  OR  V(k_W) → 0                              [K5]
      → AdmJoint condition (iv) violated                             [Level 4, §4.3]
  → M_W ⊥ M_F (act-level registered contradiction)                   [Level 4, §4.4]

Semantic Postulate dependency — AJVS:
  T3 depends on AJVS (Axiom of Joint Validity Semantics — see AJVS section below T3):
  "A K_joint satisfies D_joint iff it hosts original first-order K-side validity
   claims of both K_A and K_B as jointly evaluable. Hosting only meta-descriptions
   ('within K_F, M_F registered |h⟩') does NOT satisfy D_joint — relativizing
   registration contents abandons D_joint rather than satisfying it."

  AJVS is a named Semantic Layer postulate (Layer 0.5), separate from K1-K8.
  It defines what counts as "satisfying D_joint" in VVV-QMRF.
  If AJVS is rejected → T3's conclusion (Bridge_EWF = 1) does not follow from
  K1-K8 alone. K1-K8 remain structurally valid; only D_joint semantic scope changes.
```

| Property | Value |
|---|---|
| **Level 4 dependency** | `Bridge_EWF` lemma, `D_joint`, cross-registration authority (paper v2.0 §4.5) |
| **Layer 1 dependency** | K5 (invalidation) + K6 (authority) + K8 (V-preservation at embedding) — T3 derivation uses all three. |
| **Semantic postulate** | Relativization defense — formalized as **AJVS** (see below). T3 is conditional on AJVS. This is not an internal contradiction; AJVS is a declared Semantic Layer postulate defining what counts as satisfying `D_joint`. |
| **Claim class** | D/C boundary (matches paper v2.0 §4.5 classification) |
| **Freeze status** | Pending Level 4 freeze |
| **Update trigger** | If `Bridge_EWF` sufficient conditions change, or cross-registration authority criteria are revised, or AJVS is challenged |

---

### AJVS — Axiom of Joint Validity Semantics / Tiên đề Ngữ nghĩa Hiệu lực Chung

> **Architectural note:** AJVS is a **Semantic Layer postulate** — it sits above Level 4 structural definitions but is separate from K1-K8 registration-logic axioms. K1-K8 govern K-space structure and operations; AJVS governs what "satisfying D_joint" means at the level of claim content. This is the formalization of F-RCA-P7-04 (Action Item A1).

**Statement:**
> A candidate K_joint satisfies D_joint(A, B) iff it hosts the **original** K-side validity claims of both K_A and K_B as **jointly evaluable first-order claims** in a shared comparison context C_K. Hosting only meta-descriptions of the form "within K_A, M_A registered o_A" does NOT satisfy D_joint. Relativizing registration contents to sub-context descriptions abandons D_joint rather than satisfying it.

**Formal:**
```
Let D_joint(A, B) be raised: requires_K_joint(A, B) = 1.
Let K_joint be a candidate with embeddings i_A: K_A → K_joint, i_B: K_B → K_joint.

K_joint satisfies D_joint iff:
  ∀k ∈ K_A ∪ K_B claimed as jointly valid:
    i_X(k) carries o(k) as a FIRST-ORDER validity claim in K_joint
    — directly evaluable, not wrapped in a meta-description predicate.

Relativization escape (violates AJVS):
  A K_joint that hosts only:
    "within K_F, M_F registered |h⟩"   [meta-description of K_F-internal fact]
  does NOT constitute joint evaluation of M_F's claim.
  D_joint requires: i_F(k_F) evaluated directly as "o(k_F) = |h⟩ is valid in K_joint".

AJVS boundary:
  First-order:  o(k) directly evaluable in K_joint     → D_joint satisfied.
  Second-order: "K_X says o(k) is valid within K_X"   → D_joint NOT satisfied.
```

| Property | Value |
|---|---|
| **Nature** | Semantic Postulate — Layer 0.5 (above Level 4 structural defs; separate from K1-K8 registration-logic) |
| **BE lineage** | Dignāga–Dharmakīrti distinction: pratyakṣa (direct first-order perception/registration) vs anumāna (inferential / meta-cognition). Joint validity in VVV-QMRF requires pratyakṣa-level first-order registration, not anumāna-level meta-description |
| **Claim class** | D (proposed semantic postulate) |
| **Source** | VVV-QMRF architectural stance (paper v2.0 §4.5, now elevated to named postulate) |
| **If AJVS holds** | T3 conclusion Bridge_EWF = 1 follows from K1-K8 + AJVS. Relativization escape route closed. |
| **If AJVS rejected** | T3 conclusion does NOT follow from K1-K8 alone. Relativization escape open. K1-K8 remain structurally valid — only D_joint semantic scope changes. |
| **Cascade** | T3 (cites AJVS instead of unnamed external assumption); §10.5 Final Verdict; §10.6 A1 (resolved); Layer 2 Summary T3 row |

---

### T4 — N-Observer Generalization Theorem

**Statement:**
> For N ≥ 2 registering systems R_1, ..., R_N with K-side spaces K_1, ..., K_N: the joint K-space K_joint(R_1, ..., R_N) exists as the colimit of the embedding diagram only when (1) every pair (i, j) with requires_K_joint(K_i, K_j) = 1 satisfies pairwise AdmJoint, and (2) the N-observer embedding diagram satisfies global overlap compatibility: shared K-state images and all embedding paths commute in the candidate K_joint. K-side incommensurability ⊥_K is NOT necessarily transitive: K_A ⊥_K K_B ∧ K_B ⊥_K K_C does NOT entail K_A ⊥_K K_C. Each pair requires an independent D_joint and AdmJoint check, but pairwise admissibility alone does not prove N-way colimit commutativity.

**Derivation from axioms:**
```
K_joint(R_1,...,R_N) = colimit of embedding diagram D where:
  objects:  K_1, K_2, ..., K_N
  morphisms: for each pair (i,j) with requires_K_joint(K_i,K_j) = 1
             and AdmJoint satisfied: embedding i_{ij}: K_i → K_j (or K_i → K_joint)
  colimit universal property: K_joint is the minimal K-space receiving
    embeddings from all K_i that commute with the diagram morphisms.

F7d global commutativity guard:
  Pairwise AdmJoint is necessary but not sufficient for N-observer colimit
  existence. K8 preserves tuple fields and V values along each embedding,
  but K8 does not by itself guarantee path-independence across multiple
  embeddings. For N > 2, T4 requires an additional global compatibility
  condition: whenever two embedding paths carry the same source K-state or
  shared overlap into K_joint, their images must agree on M, o, cert, t,
  and initial V at embedding time, and their post-embedding validity dynamics
  must not force inconsistent identifications. Thus the diagram must commute
  globally, not merely pairwise.

T4-H — Colimit Existence Hypothesis (explicit conditional — F-RCA-P4-06 Option A):
  The category C_{K-space} — whose objects are K-spaces (K1-K8-structured
  sets) and whose morphisms are K1-K8-preserving embeddings — is assumed
  to have colimits for all finite embedding diagrams.

  Formal statement of T4-H:
    For any finite diagram D of K-spaces with K1-K8-preserving morphisms,
    the colimit colim(D) exists in C_{K-space}.

  Status: HYPOTHESIS, not a theorem derivable from K1-K8 alone.
    K1-K8 define the structure of individual K-spaces; they do NOT by
    themselves prove that C_{K-space} is cocomplete (has all colimits).
    T4 conclusions hold CONDITIONAL on T4-H.

  Plausibility argument (not a proof — see Open Item A5):
    Each K_R is a finite totally-ordered set (K2 chain) of K1-structured
    tuples with binary V (K4-K5) and intrinsic cert (K3). The category
    of finite totally-ordered sets with order-preserving maps has finite
    colimits (disjoint union + quotient by morphism-imposed equivalences).
    K1-K8 morphisms preserve the five-field tuple structure; shared cross-rel
    and global commutativity (F7d) impose the identification conditions.
    A finite colimit of such sets is therefore structurally plausible, but
    the rigorous category-theoretic proof is deferred to Open Item A5.

  Conditional scope:
    If T4-H holds  → T4 conclusions valid for all N ≥ 2.
    If T4-H fails  → N-observer colimit may not exist in general; T1
                     (N = 2, constructive) remains valid independently
                     because T1 builds K_joint explicitly without invoking
                     the colimit universal property.

Non-transitivity of ⊥_K:
  Counter-example possibility:
    K_A ⊥_K K_B  ∧  K_B ⊥_K K_C  ∧  ¬(K_A ⊥_K K_C)
    when: requires_K_joint(A,C) = 0 (no shared validity demand)
    OR: requires_K_joint(A,C) = 1 AND AdmJoint(K_joint; K_A, K_C) = 1

  Each pair (i,j) must pass independent:
    (a) requires_K_joint check (is joint validity demanded?)
    (b) AdmJoint check (can joint validity be preserved?)

Number of pairwise checks for N observers:
  At most N(N-1)/2 pairs with requires_K_joint = 1 (when all pairs require joint check).
  Not all pairs necessarily require K_joint (some may be causally/comparison-isolated).
```

| Property | Value |
|---|---|
| **Level 4 dependency** | All Level 4 definitions, generalized to N observers; global overlap/path-commutativity condition for N-observer diagrams |
| **Claim class** | D (proposed) — NEW. Not in paper v2.0 (which handles N=2 only). |
| **Important** | Pairwise `AdmJoint` checks are necessary local conditions, not sufficient global conditions. N-observer `K_joint` requires pairwise admissibility plus global overlap/path-commutativity. K8 supplies field/V preservation along each embedding but does not by itself prove global commutativity. |
| **Freeze status** | New theorem. Requires independent verification for N>2. |
| **Update trigger** | When N>2 EWF scenarios are modeled; when paper v3.0 extends to multi-observer cases |

### Layer 2 Summary / Tổng kết Tầng 2

| Theorem | Bridges axioms to | Level 4 dependency | Freeze status | Risk if Level 4 changes |
|---|---|---|---|---|
| T1 | K_joint construction | `requires_K_joint`, `D_joint`, embeddings | Pending | Theorem statement updates; K1-K8 unchanged |
| T2 | ⊥_K derivation | `AdmJoint` (i)-(v), `⊥_K` boundary clauses | Pending | Derivation chain updates; K1-K8 unchanged |
| T3 | Bridge_EWF formalization | `Bridge_EWF` lemma, **AJVS** (Semantic Postulate Layer 0.5 — relativization defense, formalized) | Pending | Derivation chain may need revision if AJVS challenged; K1-K8 unchanged |
| T4 | N-observer generalization | All Level 4, generalized to N; **T4-H** Colimit Existence Hypothesis (conditional) | New — Class D | Conditional on T4-H; independently updatable |

---

## 3. Audit Matrices / Ma trận Kiểm toán

### 3.1 E1-E7 Core Postulate Audit

**Question for each postulate:** Are K1-K8 sufficient to capture its K-side structural content, or do the axioms contradict it?

| Postulate | Content | K-space coverage | Verdict |
|---|---|---|---|
| **E1** | Self-Certifying Registration: σ(M)=1 intrinsic to M; no M' required | K3 directly instantiates σ_R(M) with intrinsic determination and observer-indexed independence | **COVERED — K3** |
| **E2** | Registration Self-Completion: M ≡^K r (act-result inseparability) | Not directly axiomatized as a separate equivalence relation. K1 encodes E2 structurally: each admitted K-state tuple `k = ⟨M,o,cert,t,V⟩` co-instantiates the registration act `M` with its registered result `o` (`r` on the E2 side) in one K-side event, so no separate result-producing act is required. K4/K7 govern the tuple's validity lifecycle (`V_prov` → `V_final`) after instantiation; they support completion status but do not define the act-result inseparability itself. | **ENCODED — K1 tuple structure; K4/K7 validity lifecycle noted** |
| **E3** | Registration Lock: C: H→K, C(I)=k_locked | Not directly axiomatized. C is a bridge map (H→K), not an intra-K-space property. K1-K8 describe K-space structure; C belongs to the bridge layer (interface between ρ-side and K-side). | **OUT-OF-SCOPE — Bridge layer. No conflict.** |
| **E4** | Pre-Symbolic Registration Stratum: ε(M) ∈ K_pre, Sym(ε)=∅ | Not directly axiomatized. K1 defines K-state tuples at the symbolic level (o is a symbolic outcome). The pre-symbolic stratum K_pre is a substructure not formalized in K1-K8. | **OUT-OF-SCOPE — Reserved for K-space stratification extension** |
| **E5** | Internal Representation Encoding: f_enc maps apparatus state to outcome within K | Not directly axiomatized. f_enc is an encoding map that operates within K but is not a structural property of K-space itself. | **OUT-OF-SCOPE — Encoding operation. No conflict.** |
| **E6** | Registering-System-as-Process: R = {M_1,...,M_n}, no identity beyond acts | K2 directly instantiates the temporal order as a strict partial order. K1+K2 together encode: R IS the ordered set of K-state tuples — there is no "R" separate from its K_R. | **COVERED — K1+K2** |
| **E7** | Registration Validity Location: V=1 default (Axiom 1), V→0 by ⊥ (Axiom 2), asymmetry (Axiom 3) | K4 = Axiom 1 (default, with E9 exception). K5 = Axiom 2+3 (invalidation + asymmetry + irreversibility). K6 = authority condition. K7 = closure (V_prov → V_final). All three E7 axioms + provisional/final distinction are directly instantiated. | **COVERED — K4+K5+K6+K7** |

**E1-E7 Audit verdict: 3/7 COVERED directly (E1, E6, E7). 1/7 ENCODED implicitly (E2). 3/7 OUT-OF-SCOPE (E3, E4, E5). Zero contradictions. Coverage gaps are intentional (bridge layer items, pre-symbolic stratification, encoding operations — these belong to other architectural layers, not K-space axiomatization).**

### 3.2 E8-E16 Extension Postulate Audit

**Question for each postulate:** Does the postulate require K-space structure beyond K1-K8? If yes, is the gap documented?

| Postulate | Content | K-space requirement | Verdict |
|---|---|---|---|
| **E8** | Retroactive Registration Override: M_2 retroactively voids M_1 | K5 covers single-step invalidation: a later contradictory registration `k2` can force `V_prov(k1) → 0` before closure. K7 makes this pre-closure transition revisable: if the contradicting act `k2` is itself invalidated before `t_close`, the K5 trigger for `k1` is removed and `V_prov(k1)` is no longer forced to 0. In cross-space cases where E8 is evaluated inside a `requires_K_joint` / `C_K` context, T2 supplies the resolved-demand semantics needed before K7 closure: the demand resolves either by successful `AdmJoint = 1` or by `AdmJoint = 0` producing `⊥_K`. This E8 invalidation path is distinct from E9 null status: E8 is `V_prov→0` by K5 contradiction/authority, not definitional `V=0` from `o=∅`. E8's orthogonality trigger condition (`⟨λ_2|λ_1⟩=0`) remains a ρ-side condition, not a K-space axiom. Multi-step retroactive chains (`k3` voids `k2`, which re-opens `k1`) are still not fully formalized. | **PARTIAL — K5 single-step `V_prov→0` + K7 pre-closure re-assessment covered; T2 supplies resolved-demand semantics when E8 occurs in `C_K`; multi-step retroactive chain formalization deferred.** |
| **E9** | Null Registering-System Event: interaction occurred but ΔI=0 | K1 reserves `o=∅` slot. K4 includes explicit E9 exception clause: null events have `cert=1` (interaction occurred) and `V=0` by definition because zero outcome information is transferred. This `V=0` is definitional null status, not K5/K6 invalidation: it requires no `⊥`, no `Auth`, and no shared `C_K`. Therefore F2's K6 non-transitivity refinement across distinct `C_K` contexts does not affect E9. | **COVERED — K1 `o=∅` + K4 E9 exception; independent of K6/Auth/C_K.** |
| **E10** | Tripartite Registration Validity Matrix: three validity criteria | Validity criteria operate on K-side predicates; K4-K5-K6-K7 provide the underlying validity structure. The tripartite matrix is a taxonomy layer on top of K4-K7. | **COVERED — K4-K7 as foundation. No new axiom needed.** |
| **E11** | Contrapositive Quantum Evidence: evidence from absence | Evidence structure is outside K-space (bridge/evidence layer). Evidence ABOUT K-side states is not a property OF K-space. | **OUT-OF-SCOPE — Bridge/evidence layer. No conflict.** |
| **E12** | Limit-Faculty Registration: different registering capacities | Different K_R types with different registration capacities are type-level distinctions, not new axioms. K1-K8 apply to all K_R regardless of capacity type. | **COVERED — Taxonomy layer. No new axiom needed.** |
| **E13** | Temporal Discontinuity Registration | K2 already encodes discreteness via the Δ lemma clause (no registration-state identity between events). | **COVERED — K2** |
| **E14** | Validated Absence Registration: registration from absence of detection | Requires k_absence ∈ K_R with cert=1, o=∅ (or o = "absence of X"), V=1 (valid absence). K1 reserves o=∅ slot. K4's default validity applies (non-null → V=1); the absence registration is not null (it carries positive information "X is absent"). The validity conditions for absence (expectation of detection + validated non-occurrence) are beyond K4-K5 scope. | **PARTIAL — K1 o=∅ + K4 default validity structurally accommodate. Specific validity conditions for absence deferred.** |
| **E15** | Intrinsic Relational Binding: entanglement as K-side relation | Relations BETWEEN K-spaces (K_A and K_B correlated via shared quantum state) are not covered by K1-K8, which are primarily intra-K-space axioms. T1 (K_joint) handles embeddings but not the nature of the binding relation itself. | **GAP — Inter-K-space relation structure not axiomatized. Reserved for K-space relation extension.** |
| **E16** | Pre-Measurement Registration Indeterminacy: K-side state before first registration | K1-K7 describe K_R as a set of K-state tuples produced over time. The state BEFORE the first registration event (k_0 or pre-registration K-state) is not defined. | **GAP — Pre-registration K-state not defined. Reserved for K0 (pre-registration axiom).** |

**E8-E16 Audit verdict: 6/9 COVERED or structurally accommodated (E9, E10, E11, E12, E13; E8 partial; E14 partial). 2 gaps (E15, E16). All gaps explicitly documented — no hidden incompatibilities.**

### 3.3 Operational Bridge Preservation Audit

**Question for each bridge:** Do K1-K8 invalidate or alter any operational bridge defined in paper v2.0?

| Bridge | Paper § | What it does | Preservation check | Verdict |
|---|---|---|---|---|
| **Condition A** | §4.3 | Wigner interference → requires_K_joint=1 | K1-K8 do not reference `requires_K_joint` directly. Bridge operates at Level 4 (D_joint). K-space axioms do not force or prevent requires_K_joint=1. | **PASS — Bridge unchanged.** |
| **Condition B** | §4.3 | Direct comparison → requires_K_joint=1 | Same as above. K1-K5 are silent on comparison architecture. | **PASS — Bridge unchanged.** |
| **Condition B2** | §4.3 | LF constraint → requires_K_joint=1 | Same as above. | **PASS — Bridge unchanged.** |
| **Condition C** | §4.3 | No interference → requires_K_joint=0 | K1-K8 do not force K_joint construction. K_R remains isolated unless D_joint demands otherwise. | **PASS — Bridge unchanged.** |
| **Condition D** | §4.3 | Separable state → requires_K_joint=0 | K1-K8 do not reference entanglement or separability (ρ-side properties). | **PASS — Bridge unchanged.** |
| **Condition E** | §4.3 | Independent bookkeeping → requires_K_joint=0 | K1-K8 do not conflate K_R set membership with joint validity demands. | **PASS — Bridge unchanged.** |
| **ODC_K** | §4.6 | Model-fit test for K_joint existence | K1-K8 define K-space structure but do not pre-determine ODC_K outcome. τ remains a free parameter. K4-K7 define validity propagation — ODC_K tests whether a joint model preserving K4-K7 fits data. | **PASS — ODC_K unchanged. K4-K7 provide the validity constraints ODC_K checks.** |

**Operational bridge audit verdict: 7/7 bridges preserved (no bridge broken by K1-K7). However: bridges B, B2, and ODC_K have an indirect semantic dependency on K4-K7 validity structure. K4-K7 define the validity propagation rules that these bridges operationalize. If K4-K7 were to change significantly, the semantic content of these bridges would shift even though their formal predicates (requires_K_joint, D_joint, AdmJoint) remain syntactically unchanged. This is a semantic dependency, not a syntactic break.**

### 3.4 BE Source Lineage Audit

**Question for each axiom:** Is the axiom consistent with its BE structural source?

**SOT verification scope:** K1–K3 BE concepts are directly traceable to `system_be_full.md` (N_BE_00001, N_BE_00029/N_BE_00087, N_BE_00011). K4–K8 BE concepts (Svataḥ prāmāṇya, Parataḥ prāmāṇya, Bādhaka pramāṇa, Niścaya, Anugama) are authentic Dharmakīrti-tradition vocabulary but do **not** appear in `system_be_full.md`. Consistency for K4–K8 is assessed as scholarly structural analogy, not SOT-derived verification. Per §6 Non-Overclaim Guardrail #8: "BE sources are structural lineage, NOT proof."

| Axiom | BE source | BE claim | K-space instantiation | Consistency | SOT status |
|---|---|---|---|---|---|
| **K1** | Pramāṇa (cognition as structured event) | A cognition (pramāṇa) has: act, object (prameya), self-awareness (svasaṃvedana), result (phala) | K-state tuple has: M (act), o (object/outcome), cert (self-awareness marker), t (temporal index), V (validity/result status) | **Consistent — 5-field tuple maps onto pramāṇa structure** | ✅ SOT-verifiable: N_BE_00001 |
| **K2** | Kṣaṇabhaṅgavāda (momentariness) | Cognition is momentary; no enduring cognitive substance between moments | Registration time is discrete; no K-side identity between consecutive events (Δ lemma) | **Consistent — discrete order matches momentariness without claiming physical time is discrete** | ✅ SOT-verifiable: N_BE_00029, N_BE_00087 |
| **K3** | Svasaṃvedana (self-awareness) | A cognition is self-aware; it illuminates both object and itself without a second cognition | σ_R(M) determined intrinsically within K_R; no M' required | **Consistent — intrinsic certification matches self-awareness** | ✅ SOT-verifiable: N_BE_00011 (Sva-saṃvitti) |
| **K4** | Svataḥ prāmāṇya (intrinsic validity) | Validity is intrinsic to cognition; it is the default, not something added by verification | V(k)=1 upon instantiation for ¬isNull(k); no external act required | **Structurally consistent — default validity matches intrinsic validity** | ⚠ Not in SOT; Prāmāṇyavāda category (N_BE_00134) is closest; scholarly annotation |
| **K5** | Parataḥ prāmāṇya + Bādhaka pramāṇa | Invalidity is detected extrinsically; a contradicting later cognition (bādhaka) voids the earlier one | V(k)→0 only by later k' with ⊥ and authority; asymmetry: no external function restores V=1 | **Structurally consistent — extrinsic invalidation matches bādhaka structure; asymmetry matches parataḥ** | ⚠ Not in SOT; scholarly annotation from Dharmakīrti tradition |
| **K6** | Bādhaka pramāṇa | A contradicting cognition must itself be valid to serve as a defeater; an invalid cognition cannot void another cognition | Cross-registration authority requires a valid later registration within the relevant shared C_K; invalid or out-of-scope registrations cannot invalidate k1 | **Structurally consistent — authority condition preserves bādhaka validity requirement** | ⚠ Not in SOT; scholarly annotation from Dharmakīrti tradition |
| **K7** | Niścaya (ascertainment/determination) | Cognition becomes determinate when the cognitive process reaches closure; before closure, doubt or revision remains possible | Closure converts V_prov to V_final only after pending requires_K_joint demands are resolved | **Structurally consistent — closure formalizes ascertainment without denying provisional pre-closure status** | ⚠ Not in SOT; scholarly annotation from Dharmakīrti tradition |
| **K8** | Anugama (continuity/attendant relation) | A cognition retains its epistemic status when taken up in a broader cognitive context | Embedding preserves M, o, cert, t, and initial V at embedding time, while still allowing later validity dynamics | **Structurally consistent — embedding preserves epistemic continuity without claiming immunity from later invalidation** | ⚠ Not in SOT; scholarly annotation (broader Sanskrit philosophical vocabulary) |

**BE lineage audit verdict (revised):**
- **K1, K2, K3: SOT-VERIFIED** — BE structural sources directly traceable to `system_be_full.md`. Zero inconsistencies.
- **K4–K8: STRUCTURALLY CONSISTENT (UNVERIFIABLE FROM SOT)** — BE concepts (Svataḥ prāmāṇya, Parataḥ prāmāṇya, Bādhaka pramāṇa, Niścaya, Anugama) are not present in `system_be_full.md`. Structural analogy is well-motivated by Dharmakīrti scholarship, but cannot be confirmed against the declared single source of truth. No inconsistency is found, but SOT-based verification is not possible for K4–K8.
- **Overall:** 3/8 SOT-verifiable; 5/8 scholarly annotation. Zero inconsistencies found. "Structural extraction, not identity" boundary preserved throughout.

---

## 4. Six-Condition Test — Derivation from Axioms / Kiểm tra Sáu Điều kiện

**Question:** Can the six conditions for valid registered measurement (paper v2.0 §3.1) be expressed in terms of K1-K8?

| Condition | Original formulation | K-space expression | Derivable? |
|---|---|---|---|
| **C1 (Physical)** | X occurs at ρ-side | Not a K-space condition. C1 is ρ-side — outside K1-K8 scope. | **N/A — ρ-side condition** |
| **C2 (Admission)** | X admitted into K-side as M_X for R | k ∈ K_R with M = M_X. Admission = instantiation of k in K_R. By K1 cert admission rule: cert(k)=1 for all k ∈ K_R. | **K1: k ∈ K_R, cert(k)=1** |
| **C3 (Process membership)** | M_X ∈ R where R = {M_R1, M_R2, ...} | k ∈ K_R, t(k) in the temporal order of K_R. | **K1 + K2: k ∈ K_R with t(k) ordered** |
| **C4 (Self-certification)** | σ_R(M_X) = 1, determined intrinsically | cert(k) = σ_R(M_X) = 1, determined within K_R. | **K3: cert(k) = σ_R(M)** |
| **C5 (Default validity)** | V(M_X) = 1 by default | V(k) = 1 upon instantiation for ¬isNull(k) (K4 isNull guard excludes E9 null events; no override). | **K4: cert=1 ∧ ¬isNull(k) → V=1** |
| **C6 (Non-invalidation)** | No later M' contradicts M_X with authority | No k' > k with k' ⊥ k and Auth(k'→k, C_K)=1 → V(k) stays 1. Pre-closure: provisional. Post-closure (K7): final. | **K5 + K6 + K7** |

**Six-condition test verdict: 5/5 K-side conditions derivable from K1-K8. C1 is ρ-side — correctly outside K-space scope.**

---

## 5. Claim Traceability / Truy vết Claim

| Claim ID | Claim | Claim type | Source | Confidence | Boundary |
|---|---|---|---|---|---|
| C-KAXIOM-001 | K_R is a set of 5-field K-state tuples (K1) | Class C formal definition | This document §1, K1 | High | Not a Hilbert space; not a physical state space |
| C-KAXIOM-002 | (K_R, <_R) is a strict total order (chain) with discrete registration-time (K2) | Class D proposed | This document §1, K2; E6; S2-Δ | High | Registration-time only; not physical time. Total within K_R; partial only in cross-K-space (K_joint). |
| C-KAXIOM-003 | σ_R(M) is determined intrinsically within K_R (K3) | Class D proposed | This document §1, K3; E1 | High | Certifies occurrence, not truth of outcome |
| C-KAXIOM-004 | V(k)=1 by default for self-certified non-null events; isNull(k) guard covers E9 null events (K4) | Class D proposed | This document §1, K4; E7 Axiom 1 | High | Default K-side validity for ¬isNull(k); not absolute truth |
| C-KAXIOM-005 | V(k)→0 iff later contradicting act with authority (K5) | Class D proposed | This document §1, K5; E7 Axioms 2-3 | High | Registration-layer only; not physical erasure |
| C-KAXIOM-006 | K_joint exists as colimit of embedding diagram (T1) | Class D proposed | This document §2, T1; paper v2.0 §4.3 | Medium — pending Level 4 freeze | Candidate K_joint, not guaranteed admissible |
| C-KAXIOM-007 | ⊥_K derivable from K1-K5 + AdmJoint failure (T2) | Class D proposed | This document §2, T2; paper v2.0 §4.4 | Medium — pending Level 4 freeze | Registration-layer incommensurability only |
| C-KAXIOM-008 | Bridge_EWF derivable from K5 + EWF config (T3) | Class D/C boundary | This document §2, T3; paper v2.0 §4.5 | Medium — pending Level 4 freeze | EWF-specific; not general LF theorem |
| C-KAXIOM-009 | N-observer joint K-space is colimit; ⊥_K non-transitive (T4) | Class D proposed — NEW | This document §2, T4 | Low — new, unverified for N>2 | Generalization; requires independent verification |
| C-KAXIOM-006a | K6: Auth(k2→k1, C_K)=1 iff shared C_K, V(k2)=1, k1∈scope(D_joint); non-hierarchical, non-transitive (K6) | Class D proposed | This document §1, K6; E7 Axiom 2; paper v2.0 §4.4 | Medium | Structural relation within C_K; not observer hierarchy |
| C-KAXIOM-007a | K7: R closes at t_close when no pending requires_K_joint; V_prov→V_final; post-closure irreversibility absolute (K7) | Class D proposed | This document §1, K7; E7 V_prov/V_final; paper v2.0 §2.2 | Medium | K-side closure only; not physical process termination |
| C-KAXIOM-008b | K8: V_X(i(k)) = V_R(k) at t_embed; fields M, o, cert, t preserved unchanged across embedding; non-redundant with K4 (K4 governs native instantiation, K8 governs cross-space transfer — see §1 K8 counter-model) | Class D proposed | This document §1, K8; T1 derivation dependency; Open Item #13 (EP→K8 promotion) closed | High | Snapshot preservation at embedding time, not permanent immunity; K5 can still fire in K_X after embedding |
| C-KAXIOM-010 | 2-layer architecture isolates K1-K8 from Level 4 changes in two senses. **(1) Syntactic isolation (unconditional):** K1-K8 axiom text is frozen — Level 4 changes (AdmJoint criteria, D_joint definitions, requires_K_joint scope) do not alter K1-K8 text. **(2) Conditional semantic dependencies (K5/K6/K7):** K5 ⊥_K evaluation is narrowed by Level 4 boundary clauses (F3); K6 Auth evaluation depends on D_joint extensional scope (F6a); K7 t_close timing depends on requires_K_joint extensional scope (F6b). K1-K4 and K8 reference Level 4 for scope identification only or not at all. See §0.5 for full distinction. | Architectural claim | This document §0.5 | High — structural property | Architectural design, not mathematical theorem. Syntactic isolation is unconditional; semantic dependencies are conditional on Level 4 extensional content. |

---

## 6. Non-Overclaim Guardrails / Ranh giới Chống Khẳng định Quá mức

1. **K-space is NOT a Hilbert space.** K_R is a set of registration tuples, not a vector space with inner product. K ≠ H is the core architectural commitment.

2. **K-space axioms do NOT modify Standard QM.** P1-P4, Born rule, Schrödinger equation, and ρ-side dynamics are unchanged.

3. **K-space axioms are NOT physical laws.** They are proposed registration-layer structural definitions (Class D). They do not make empirically testable predictions independent of the operational bridges in paper v2.0.

4. **K-space is registration-logic, not pure mathematics.** The axioms include primitive epistemological predicates (σ, V, ⊥) that have no analogue in standard mathematical spaces. This is intentional — K-space is a different kind of structure than Hilbert space.

5. **Bridge theorems T1-T3 are pending Level 4 freeze.** They derive current paper v2.0 definitions from axioms. If community feedback changes those definitions, T1-T3 are updated — K1-K8 are not. T3 additionally depends on an external philosophical assumption (relativization defense, paper v2.0 §4.5) not derivable from K1-K8.

6. **K1-K8 coverage across E1-E16 uses four verdict states (per §3.1, §3.2):**
   - **COVERED** (direct axiomatization): E1 (K3), E6 (K2), E7 (K4/K5/K7), E9 (K4 isNull), E10 (K5 scope), E12 (K5/K6), E13 (K2 discrete)
   - **ENCODED** (structural implication without direct axiom): E2 (K1+K3 tuple structure)
   - **PARTIAL** (single-step covered; multi-step deferred): E8 (K5 single-step covered; retroactive chain deferred), E14 (structural accommodation only)
   - **OUT-OF-SCOPE** (other architectural layers — no conflict, no gap): E3, E4, E5, E11
   - **GAP** (extensions deferred to future work): E15, E16
   Full per-postulate verdicts in §3.2.

7. **This document does NOT upgrade any paper v2.0 claim class.** All claims remain Class D/C as in the paper. Axiomatization provides the foundation for future upgrades but does not perform them.

8. **BE sources are structural lineage, NOT proof.** Each axiom annotates its BE source for traceability. The BE source is a structural analogue, not empirical evidence for the axiom's truth.

---

## 7. Concrete Model & Proof Attempt — Level 4 Freeze Check / Mô hình Cụ thể & Nháp Chứng minh

**Methodology:** Following the "smallest model first, consistency before derivability" protocol. This section:
1. Defines the smallest concrete EWF model (2 observers, 1 registration event each)
2. Walks K1-K8 for consistency
3. Walks Level 4 definitions for consistency
4. Presents a proof attempt for T2 with gaps explicitly marked

### 7.1 Concrete Model Definition / Định nghĩa Mô hình Cụ thể

> **Notation convention (§7):** Outcome labels use Hilbert ket notation (`|h⟩`, `|Ψ+⟩`) symbolically. `o ∈ O` is a K-side registration label — it is NOT a Hilbert vector. The K_R ≠ H boundary (K1) is preserved. The ⊥ test in §7.3 L4-5 uses H-side content compatibility as bridge reasoning: "`|Ψ+⟩` does not preserve `|h⟩` as a valid claim" means W's registered superposition content is incompatible with F's registered definite outcome — this is a K-side comparison via H-side content semantics, not a claim that K_R contains H vectors.

**Scenario:** Extended Wigner's Friend (EWF), minimal configuration.

- **Friend F** measures spin of particle S inside sealed laboratory. Outcome: spin-up (|h⟩).
- **Wigner W** performs interference measurement on F's entire laboratory. Registers superposition |Ψ+⟩ = (1/√2)(|h⟩|"saw h"⟩ + |v⟩|"saw v"⟩). No definite o_F preserved as W-side valid claim.

**Concrete K-spaces:**

```
K_F = { k_F }     where k_F = ⟨M_F, |h⟩, 1, t_F, 1⟩

  M_F  = "Friend measures spin of S"
  o_F  = |h⟩  (definite outcome: spin-up)
  cert = 1     (self-certified)
  t_F  = 1     (registration time index)
  V    = 1     (valid by default)

K_W = { k_W }     where k_W = ⟨M_W, |Ψ+⟩, 1, t_W, 1⟩

  M_W  = "Wigner interference measurement on F+S laboratory"
  o_W  = |Ψ+⟩  (superposition: no definite spin-up preserved)
  cert = 1      (self-certified)
  t_W  = 2      (registration time index; after t_F in laboratory history)
  V    = 1      (valid by default)
```

**Model properties:**
- |K_F| = 1, |K_W| = 1 (one event each — smallest non-trivial case)
- F and W are distinct registering systems (R_F ≠ R_W)
- Both are non-null events (o ≠ ∅)

### 7.2 K1-K8 Consistency Walk / Kiểm tra Nhất quán K1-K8

| Axiom | Check on K_F | Check on K_W | Result |
|---|---|---|---|
| **K1** (Carrier) | k_F = ⟨M_F, \|h⟩, 1, 1, 1⟩ is a 5-field tuple. k_F ∈ K_F. cert(k_F) = 1 → admitted. | k_W = ⟨M_W, \|Ψ+⟩, 1, 2, 1⟩ is a 5-field tuple. k_W ∈ K_W. cert(k_W) = 1 → admitted. | ✅ Both satisfy K1 |
| **K2** (Total order) | K_F = {k_F}: singleton. Trivially a strict total order (no pair to compare). Discrete: trivially satisfied. | K_W = {k_W}: singleton. Same reasoning. | ✅ Both satisfy K2 |
| **K3** (Self-cert) | σ_F(M_F) = 1, determined within K_F. No M' ≠ M_F required. No R' ≠ R_F involved. | σ_W(M_W) = 1, determined within K_W. No M' ≠ M_W required. No R' ≠ R_W involved. σ_F and σ_W are independent. | ✅ Both satisfy K3 |
| **K4** (Default V) | cert(k_F) = 1 → V(k_F) = 1 upon instantiation. k_F is non-null (o_F = \|h⟩ ≠ ∅). No E9 exception applies. | cert(k_W) = 1 → V(k_W) = 1 upon instantiation. k_W is non-null (o_W = \|Ψ+⟩ ≠ ∅). No E9 exception applies. | ✅ Both satisfy K4 |
| **K5** (Invalidation) | No k' ∈ K_F with k_F <_F k'. K_F has only one element. No invalidation possible within K_F. V(k_F) remains 1. | No k' ∈ K_W with k_W <_W k'. K_W has only one element. No invalidation possible within K_W. V(k_W) remains 1. | ✅ K5 vacuously satisfied (no later event exists in either K-space) |
| **K6** (Authority) | No pair within K_F to check authority. Vacuously satisfied. | No pair within K_W to check authority. Vacuously satisfied. | ✅ Vacuously satisfied |
| **K7** (Closure) | ⚠ Closure BLOCKED: requires_K_joint(F,W) = 1 is established in §7.3 (Condition A). K7 precondition `pending(K_F, K_W) = ∅` is NOT met until D_joint is resolved. V_prov(k_F) = 1 (provisional only). V_final NOT yet assigned. | ⚠ Same as K_F: closure BLOCKED pending D_joint resolution. V_prov(k_W) = 1 (provisional only). V_final NOT yet assigned. | ⚠ Closure blocked for both K_F and K_W until §7.3 D_joint resolves — K7 working as designed. |
| **K8** (Embedding) | Intra-K-space: k_F has no embedding to check (K_F is native). Vacuously satisfied. | Intra-K-space: k_W has no embedding to check (K_W is native). Vacuously satisfied. **Tested in K_joint context at L4-7 below.** | ✅ Vacuously satisfied intra-K-space; tested cross-space in §7.3 |

**K1-K8 intra-K-space consistency verdict:**
> K_F and K_W each individually satisfy K1-K8 without contradiction. K5, K6, and K8 are vacuously satisfied because each K-space has only one element. K7 is conditionally satisfied: if requires_K_joint = 1 (Level 4), then closure is blocked until D_joint is resolved, making V_final pending. This is not an inconsistency — it is K7 working as designed. K8's embedding preservation is tested in the cross-space K_joint construction at L4-7.

### 7.3 Level 4 Definitions Walk / Kiểm tra Định nghĩa Tầng 4

Walking through each Level 4 definition (paper v2.0 §4.3-4.5) applied to the concrete model.

**Step L4-1: requires_K_joint predicate**

```
requires_K_joint(F, W) = ?

Check conditions (paper v2.0 §4.3):
  (a) K_F and K_W are each valid within their own K-side?       YES (K4, verified §7.2)
  (b) Are they brought under a shared validity demand D_joint?   YES — EWF setup demands both
      be assessed as parts of one laboratory registration history
  (c) Does D_joint require both to be parts of the same          YES — LF/no-go constraint requires
      registration target/history/validity claim?                 F's and W's outcomes to be assigned
                                                                  simultaneous cross-observer validity
  (d) Can D_joint be evaluated while leaving K_F, K_W            NO — the comparison demands
      in fully independent K-spaces?                              embedding into one candidate K_joint
  (e) Does preserving D_joint require a candidate K_joint?       YES

→ requires_K_joint(F, W) = 1    via Condition A (Wigner interference)
```

| Check | Status |
|---|---|
| Condition A (Wigner interference) | ✅ W performs interference on F+S lab. M_W registers superposition. M_F registers definite outcome. Both concern same lab history. |

**Step L4-2: D_joint predicate**

```
D_joint(K_F, K_W, Arch_EWF) = 1

Arch_EWF = "Extended Wigner's Friend: F measures S inside lab;
            W performs interference on F+S; LF comparison demands
            both claims support one cross-observer validity constraint."

D_joint evaluates to 1 because Arch_EWF demands that K_F and K_W
support one shared registration-validity claim about the same laboratory.
```

| Check | Status |
|---|---|
| D_joint = 1 | ✅ Consistent with paper v2.0 §4.3 definition |

**Step L4-3: Comparison context C_K**

```
C_K exists for (k_F, k_W)?

Check conditions (paper v2.0 §4.4):
  (a) Both acts admitted into same comparison domain?     YES — D_joint demands it
  (b) Both indexed to same registration target/history?   YES — same laboratory F+S
  (c) Comparison does not presuppose both already         YES — comparison TESTS whether
      jointly valid?                                       they can be jointly valid

→ C_K(k_F, k_W) exists.
```

| Check | Status |
|---|---|
| C_K exists | ✅ All three conditions met |

**Step L4-4: Cross-registration authority**

```
Auth(k_W → k_F, C_K) = ?

K6 frozen conditions (CORE Auth criteria — Layer 1 syntactically frozen):
  (a) C_K-sphere(k_F) = C_K-sphere(k_W)?                YES — both in same C_K (L4-3)
  (b) V(k_W) = 1?                                        YES — K4 default, not invalidated
  (c) k_F ∈ scope(D_joint)?                               YES — D_joint demands F's claim
                                                                 be part of joint evaluation

→ K6 conditions (a)+(b)+(c) all satisfied: Auth = 1 under K6 alone. [K6 frozen Layer 1]

Paper v2.0 §4.4 additional conditions (Level 4 strengthening — not required by K6):
  Note: K6 frozen text is sufficient for Auth=1. Paper §4.4 conditions extend K6 scope
  for the general case; they do not contradict K6 in this model. Auth=1 holds under
  both K6 alone and K6 + paper extensions.
  (a') k_W is valid registered measurement?               YES — σ_W(M_W)=1, V(k_W)=1
  (b') k_W's content concerns same target as k_F?         YES — same laboratory F+S
  (c') k_W produced by measurement structurally required   YES — W's interference measurement
       to register state of same system k_F registered?         measures the lab containing F+S
  (d') No arbitrary privilege?                             YES — only temporal ordering
                                                                 and content incompatibility used

→ Auth(k_W → k_F, C_K) = 1   [K6 core sufficient; paper §4.4 extensions consistent]
```

| Check | Status |
|---|---|
| Auth = 1 | ✅ All conditions met. k_W has authority over k_F in this C_K. |

**Step L4-5: Registered contradiction ⊥**

```
k_W ⊥ k_F within C_K?

Check K5 minimal definition:
  - k_F registers o_F = |h⟩ (definite outcome)
  - k_W registers o_W = |Ψ+⟩ (superposition; no definite |h⟩ preserved as W-side valid claim)
  - Can both be treated as valid K-side claims within the same C_K?
    NO — |h⟩ is a definite state claim; |Ψ+⟩ is a superposition that does not preserve
    |h⟩ as a valid claim. Within one C_K, claiming both "outcome is definitely |h⟩"
    AND "outcome is superposition with no definite |h⟩" is a registration contradiction.

→ k_W ⊥ k_F within C_K.    [K5 minimal definition satisfied]

Check paper v2.0 §4.4 act-level definition:
  - Same C_K?                                              YES (L4-3)
  - Same registration target?                              YES (same lab F+S)
  - Cannot both satisfy validity conditions?               YES (above)
  - Later act has valid cross-registration authority?       YES (L4-4)

→ M_W ⊥ M_F    [act-level registered contradiction confirmed]
```

| Check | Status |
|---|---|
| k_W ⊥ k_F | ✅ Registration contradiction established |

**Step L4-6: Bridge_EWF**

```
Bridge_EWF(D_joint; M_F, M_W) = ?

Check conditions (paper v2.0 §4.5):
  (a) D_joint requires F-side and W-side registrations to be     YES (L4-2)
      evaluated as jointly valid parts of one lab history?
  (b) M_F registers definite friend-side outcome o_F?            YES — o_F = |h⟩
  (c) M_W registers same lab as coherent superposition with      YES — o_W = |Ψ+⟩,
      no definite o_F preserved as W-side valid claim?                no |h⟩ preserved
  (d) LF/no-go comparison requires both claims to support        YES — by EWF setup
      one cross-observer validity constraint?
  (e) No reinterpretation inside same K_joint can preserve       CHECK — this is the
      both contents without changing validity of at least              relativization
      one side?                                                        defense question

Relativization defense check (paper v2.0 §4.5):
  Could K_joint host meta-descriptions ("within K_F, M_F registered |h⟩")?
  Paper's answer: NO — D_joint demands joint validity of original claims,
  not meta-descriptions. Relativizing abandons D_joint rather than satisfying it.
  This is a FRAMEWORK-LEVEL SEMANTIC COMMITMENT (documented in T3).

→ Bridge_EWF(D_joint; M_F, M_W) = 1    [assuming relativization defense holds]
```

| Check | Status |
|---|---|
| Bridge_EWF = 1 | ✅ All conditions met (conditional on relativization defense — framework-level semantic commitment) |

**Step L4-7: AdmJoint check**

```
Does an admissible K_joint(K_F, K_W) exist?

Candidate K_joint = i_F(K_F) ∪ i_W(K_W) = { i_F(k_F), i_W(k_W) }

Check AdmJoint conditions (paper v2.0 §4.3):
  (i)   Embeddings preserve act, outcome, cert, time/order, V?
        i_F(k_F) = ⟨M_F, |h⟩, 1, t_F, V_joint(k_F)⟩
        i_W(k_W) = ⟨M_W, |Ψ+⟩, 1, t_W, V_joint(k_W)⟩
        Act, outcome, cert preserved? YES.
        Order: t_F < t_W in lab history → i_F(k_F) <_joint i_W(k_W). YES.
        V preservation by K8 [V_X(i(k)) = V_R(k) at t_embed]:
          V_joint(i_F(k_F)) = V_F(k_F) = 1       [k_F native V preserved at embedding]
          V_joint(i_W(k_W)) = V_W(k_W) = 1       [k_W native V preserved at embedding]
        Both V=1 carry into K_joint.                                     ✅ K8

  (ii)  Self-certification intrinsic to each embedded act?
        σ_F(M_F) = 1 in K_joint? Must remain intrinsic → not redefined by K_joint. YES.
        σ_W(M_W) = 1 in K_joint? Same. YES.                              ✅

  (iii) Conditions 1-6 satisfied for each embedded structure?
        For i_F(k_F): C1-C5 carry over. C6 (non-invalidation) → CHECK:
          Is there k' in K_joint with k' ⊥ i_F(k_F) and Auth?

          ⊥-preservation across embedding (corollary of K8 + K5 minimal ⊥):
            K8 preserves o values at embedding: o(i_W(k_W)) = o(k_W) = |Ψ+⟩;
            o(i_F(k_F)) = o(k_F) = |h⟩.
            K5 minimal ⊥ depends on o content compatibility (per K5 dòng definition).
            Since K8 preserves o, the K5 ⊥ test gives the same result in K_joint:
            k_W ⊥ k_F (native C_K, L4-5) → i_W(k_W) ⊥ i_F(k_F) (K_joint C_K). ✓

          → i_W(k_W) ⊥ i_F(k_F) within C_K (established in L4-5; preserved via K8)
          → Auth(i_W(k_W) → i_F(k_F), C_K) = 1 (established in L4-4)
          → K5 FIRES: V(i_F(k_F)) → 0                                    ⚠ CONFLICT
        For i_W(k_W): C1-C6 → no later event contradicts k_W in K_joint. OK.  ✅

  (iv)  No required registration-state update invalidates either embedded
        structure while both claimed as jointly valid?
        → K5 just fired: V(i_F(k_F)) → 0 while both were claimed jointly valid.
        → AdmJoint condition (iv) VIOLATED.                                ❌ FAILS

→ AdmJoint(K_joint; K_F, K_W) = 0    [no admissible K_joint exists for this model]
```

| Check | Status |
|---|---|
| AdmJoint = 0 | ❌ Condition (iv) violated via K5 conflict |

**Step L4-8: ⊥_K conclusion**

```
K_F ⊥_K K_W?

  requires_K_joint(F, W) = 1?                              YES (L4-1)
  ∃ admissible K_joint?                                     NO  (L4-7)

→ K_F ⊥_K K_W    [K-side incommensurability holds in this model]
```

| Check | Status |
|---|---|
| K_F ⊥_K K_W | ✅ Incommensurability established for this concrete model |

### 7.4 Consistency Verdict / Kết luận Nhất quán

> **The concrete model is internally consistent.** Walking K1-K8 on K_F and K_W individually produces no contradiction. Walking Level 4 definitions on the joint scenario produces a well-defined chain:
>
> requires_K_joint = 1 → D_joint = 1 → C_K exists → Auth = 1 → k_W ⊥ k_F → Bridge_EWF = 1 → K5 fires in K_joint → AdmJoint(iv) fails → K_F ⊥_K K_W.
>
> Each step follows from the previous without circular reasoning within THIS model. The concrete model serves as **evidence of consistency** (a satisfying model exists for all axioms simultaneously).

**Identified gaps (not inconsistencies):**

| # | Gap | Severity | Location |
|---|-----|----------|----------|
| G1 | Relativization defense is framework-level semantic commitment required by this formulation of D_joint | Medium | L4-6, step (e). Documented in T3. |
| G2 | K7 closure conditional on D_joint resolution | Low | §7.2 K7 row. Working as designed. |
| G3 | K5 minimal ⊥ definition used here; full Level 4 ⊥ formalization not frozen | Medium | L4-5. Documented in Open Item #14. |

### 7.5 T2 Proof Attempt / Nháp Chứng minh T2

**Goal:** Derive K_F ⊥_K K_W from K1-K8 + Level 4 definitions in the concrete model.

**Statement to prove:**
> In the EWF concrete model (§7.1): if requires_K_joint(F,W) = 1 via D_joint, and Bridge_EWF(D_joint; M_F, M_W) = 1, then K_F ⊥_K K_W.

**Proof attempt:**

```
Step 1 — Setup (SOLID ✅):
  K_F = {k_F} with k_F = ⟨M_F, |h⟩, 1, 1, 1⟩.     [K1: well-formed tuple, cert=1]
  K_W = {k_W} with k_W = ⟨M_W, |Ψ+⟩, 1, 2, 1⟩.    [K1: well-formed tuple, cert=1]
  σ_F(M_F) = 1, σ_W(M_W) = 1, independent.           [K3: intrinsic self-certification]
  V(k_F) = 1, V(k_W) = 1 by default.                  [K4: cert=1 → V=1, non-null]

Step 2 — requires_K_joint (SOLID ✅, modulo Level 4 definition):
  requires_K_joint(F, W) = 1.
  Justification: Condition A — W performs interference on F+S lab.
  D_joint(K_F, K_W, Arch_EWF) = 1.
  Source: paper v2.0 §4.3 definition. Applied correctly in L4-1, L4-2.
  Confidence: HIGH — direct application of sufficient condition A.

Step 3 — C_K and Auth (SOLID ✅):
  C_K(k_F, k_W) exists.                               [L4-3: all three conditions met]
  Auth(k_W → k_F, C_K) = 1.                           [K6 + L4-4: all conditions met]
  Confidence: HIGH — mechanical check of conditions.

Step 4 — Registered contradiction (SOLID ✅ at K5 minimal level):
  k_W ⊥ k_F within C_K.
  Justification: o_F = |h⟩ (definite), o_W = |Ψ+⟩ (superposition, no |h⟩ preserved).
  These cannot both be valid K-side claims within one C_K.
  Source: K5 minimal definition.
  Confidence: HIGH for K5 minimal. MEDIUM for full Level 4 ⊥ (not frozen).
  ⚠ GAP G3: Full Level 4 ⊥ boundary clauses not frozen. K5 minimal used here
  is self-contained but may need revision if Level 4 changes ⊥ semantics.

Step 5 — Bridge_EWF (MEDIUM ⚠ — semantic boundary):
  Bridge_EWF(D_joint; M_F, M_W) = 1.
  Justification: All conditions (a)-(d) mechanically checked in L4-6.
  Condition (e) — "no reinterpretation preserves both" — depends on
  relativization defense (paper v2.0 §4.5).
  ⚠ GAP G1: Relativization defense is a framework-level semantic commitment.
  If rejected, Bridge_EWF = 1 does not follow from K1-K8 alone.
  Confidence: MEDIUM — conditional on this semantic commitment.

Step 6 — K5 fires in candidate K_joint (SOLID ✅):
  By K8: embeddings i_F, i_W preserve V values.         [K8: V_X(i(k)) = V_R(k)]
  In candidate K_joint:
    i_F(k_F) <_joint i_W(k_W)                          [K2: t_F < t_W]
    i_W(k_W) ⊥ i_F(k_F) within C_K                    [Step 4]
    Auth(i_W(k_W) → i_F(k_F), C_K) = 1                 [Step 3]
    → K5: V_prov(i_F(k_F)) → 0                         [K5 pre-closure invalidation]
  At this stage, V_final has not yet been assigned: K7 closure can occur only
  after the pending requires_K_joint demand is resolved.
  This happens while D_joint claims both as jointly valid.
  → AdmJoint condition (iv) violated.
  Confidence: HIGH — direct K5 + K8 application. No gap.

Step 7 — Conclusion (SOLID ✅):
  requires_K_joint(F, W) = 1                            [Step 2]
  ¬∃ K_joint: AdmJoint(K_joint; K_F, K_W) = 1          [Step 6]
  → K_F ⊥_K K_W                                         [T2 ⊥_K Derivation Theorem; consistent with paper v2.0 §4.4 definition]
  ∎ (conditional)
```

### 7.6 Proof Attempt Assessment / Đánh giá Nháp Chứng minh

| Step | Confidence | Depends on | Gap? |
|------|-----------|------------|------|
| 1 (Setup) | HIGH | K1, K3, K4 | None |
| 2 (requires_K_joint) | HIGH | Level 4 §4.3 Condition A definition | Level 4 not frozen |
| 3 (C_K, Auth) | HIGH | K6 + Level 4 §4.4 | Level 4 not frozen |
| 4 (⊥ contradiction) | HIGH/MEDIUM | K5 minimal / Level 4 full ⊥ | **G3**: Level 4 ⊥ not frozen |
| 5 (Bridge_EWF) | MEDIUM | External philosophical assumption | **G1**: Relativization defense |
| 6 (K5 in K_joint) | HIGH | K5 + K8 | None (resolved by K8) |
| 7 (Conclusion) | HIGH | Steps 2+6 + ⊥_K definition | Level 4 definition |

**Overall assessment:**
> The proof attempt is **valid conditional on two remaining identified dependencies** (G1, G3). Neither is an internal contradiction — one is a philosophical boundary, one is a temporal dependency:
>
> - **G1 (Relativization defense)**: Framework-level semantic commitment — not derived within K1-K8. This formulation makes explicit what counts as "satisfying a joint validity demand." Documented as a semantic boundary, not a mathematical gap.
> - **G3 (Level 4 ⊥ freeze)**: Temporal dependency — resolves when paper v2.0 Level 4 boundary clauses are frozen. K5 minimal ⊥ is sufficient for the concrete model.
>
> **Former EP gap (G1 in v1.3): RESOLVED.** EP promoted to K8 (v1.4) — V-preservation through cross-space embedding is now a core axiom. The proof chain no longer depends on an external postulate for Step 6.
>
> The circularity concern from v1.2 Open Item #14 is **not present in this concrete model** because K5's minimal ⊥ definition is sufficient for Step 4 without invoking Level 4's full ⊥ formalization. The circularity only appears in the GENERAL case where T2 needs AdmJoint conditions that reference full ⊥. In the concrete model, ⊥ is directly verified by content inspection (|h⟩ vs |Ψ+⟩).

### 7.7 Next Steps / Bước Tiếp theo

Following the 5-step methodology:

| Step | Status | Timeline estimate |
|------|--------|-------------------|
| ✅ Step 1 — Concrete Model (§7.1-7.4) | **DONE** — consistency established | — |
| ✅ Step 2 — Proof attempt for T2 (§7.5-7.6) | **DONE** — 2 remaining dependencies (G1: relativization; G3: Level 4 ⊥ freeze). Former EP gap resolved by K8. | — |
| ⬜ Step 3 — Submit K-Axiom + Concrete Model to PhilSci | Ready for community review | 1-2 weeks |
| ⬜ Step 4 — Based on feedback, decide: close remaining gaps or find collaborator | Pending feedback | After Step 3 |
| ⬜ Extension — Generalize from N=2 to N>2 | T4 verification (Open Item #9) | After Step 4 |

**Decision point after community feedback:**
- If gaps G1, G3 are accepted as documented → Level 4 freeze proceeds
- If G1 (relativization) is challenged → T3 needs revision, but K1-K8 unchanged (this is a philosophical/semantic challenge, not mathematical)
- If consistency check reveals new issues → return to concrete model, extend

---

## 8. Open Items / Các mục Để Mở

| # | Item | Status | Priority |
|---|------|--------|:--------:|
| 1 | Multi-step retroactive chain (E8 extension) | Deferred — K5 single-step; K5 V_prov pre-closure mechanism allows re-assessment of invalidating acts before K7 closure (F1: V_prov/V_final lifecycle — V_prov→0 reversible pre-closure, V_final→0 irreversible post-closure). Multi-step chain requires additional axiom(s). | Medium |
| 2 | Null K-state full formalization (E9 detailed operationalization) | Partial — K1 o=∅ + K4 E9 exception structurally accommodate null events. Detailed operationalization deferred. | Low-Medium |
| 3 | Validated absence validity conditions (E14 extension) | Partial — K1 o=∅ + K4 default validity structurally accommodate. Specific absence validity conditions deferred. | Medium |
| 4 | Inter-K-space relation structure (E15 extension) | Deferred — new axiom needed | Low-Medium |
| 5 | Pre-registration K-state (E16 extension / K0) | Deferred — new axiom needed | Low-Medium |
| 6 | Pre-symbolic registration stratum (E4 formalization) | Deferred — K-space stratification | Low |
| 7 | Equivalence of σ(M) and R̂_svasa formalisms | Deferred — separate research track (paper v2.0 §7.2 item #4) | Low |
| 8 | Full semantic proof for Bridge_EWF "no admissible reinterpretation" | Pending Level 4 freeze + T3 completion. External assumption (relativization defense) documented. | High |
| 9 | T4 N>2 verification | Requires multi-observer EWF modeling | Medium |
| 10 | Update paper v2.0 Section 7.2 deferred item #5 status | After community feedback on this document | Low |
| 11 | RCA re-audit after community feedback | After Level 4 freeze and T1-T3 finalization | High |
| 12 | K6 Auth non-transitivity edge cases (circular authority chains) | **Resolved v1.2** — counterexample provided in K6 formal block. Remaining: N≥3 exotic topologies. | Low |
| 13 | Embedding Postulate (EP) promotion decision | **Resolved v1.4** — EP promoted to K8 (Cross-Space Embedding Preservation). K8 is now a frozen Layer 1 core axiom. T1-T3 no longer depend on an external postulate for V-preservation. | ~~High~~ → Resolved |
| 14 | T2 temporal dependency — Level 4 ⊥ freeze | T2 derivation is conditional on Level 4 ⊥ formalization being consistent with K5 minimal definition. This is a TEMPORAL DEPENDENCY (incompleteness), not a logical circularity — relabeled in v1.5 RCA. **v1.3 update:** Dependency NOT present in concrete model (§7.5 Step 4) — K5 minimal ⊥ is directly verifiable by content inspection (|h⟩ vs |Ψ+⟩). Dependency remains only in general case (arbitrary |K_R|, N observers). **v1.4/Phase 2 update:** T2 also documented as K7 Dep-B (F6b + F7b): T2's AdmJoint(iv) operates on V_prov during pre-closure admissibility testing; resolved-demand outcomes (AdmJoint=1 or AdmJoint=0 → ⊥_K) supply K7 closure semantics. This is a Layer 2 (updatable) dependency — K1-K8 unchanged. Resolves when Level 4 ⊥ boundary clauses are frozen. | **High** |
| 15 | Concrete model gaps G1-G3 (§7.4) | G1 (Relativization): framework-level semantic commitment required by this formulation of D_joint. G2 (K7 closure): working as designed. G3 (Level 4 ⊥): see #14. All gaps are external dependencies, not internal contradictions. **v1.4:** Former EP gap resolved by K8. Renumbered G1-G4 → G1-G3. **Phase 2 note:** Dep-A (C_K existence precondition, Level 4 §4.3) and Dep-B (T1 `<_joint>` ordering via K2+K8+Level 4 cross-rel) are satisfied dependencies in the concrete model (§7.5 Steps 3, 6 — both SOLID ✅ HIGH confidence; concrete model's cross-rel `t_F < t_W in lab history` supplies the Level 4 input) — not open gaps. Documented in K5/K6/K7 Dependency rows. | Medium |
| 16 | `RegistrationState(t)` undefined primitive in K2 Discreteness | **Resolved v1.5 RCA (RC-02)** — `RegistrationState: T_R → (K_R ∪ {∅})` formally defined inline in K2 formal block. Well-definedness guaranteed by K2 strict total order (at most one k per distinct t). | ~~Medium~~ → Resolved |
| 17 | K8 non-redundancy with K4 — no counter-model or proof sketch | **Resolved v1.5 RCA (PG-02)** — Counter-model added to K8 §(iv): K_F = {k_F, V_F=1}, embedding i assigns V_joint(i(k_F))=0 → K4 satisfied, K8 fails → K4 ⊬ K8. | ~~Medium~~ → Resolved |
| 18 | §3.3 Operational Bridge semantic dependency on K4-K7 untracked | §3.3 lists 7 sufficient-condition bridges (Condition A, B, B2, C, D, E, ODC_K) for raising `requires_K_joint`. The verdict notes B, B2, and ODC_K have indirect semantic dependency on K4-K7 validity propagation, but the table does not annotate which K-axioms each Condition row depends on. Add K-axiom dependency annotations (e.g., K4, K5, K7) to each §3.3 Condition row. Note: the predicate-level mapping (σ, V, ⊥, Auth, D_joint, requires_K_joint, C_K → K-axioms) is a separate task belonging to Layer 4 §4.4, not to §3.3. | Medium |

---

## 9. Cross-References / Tham chiếu Chéo

| Document | Relationship |
|---|---|
| `papers/.../VVV-QMRF_Working_Paper_v2.0.md` | Downstream — K-space axioms are the foundation for §3-4 structural definitions |
| `meta_architecture/vvv_qmrf_meta_architecture_registration_layer_formalization.md` | Upstream — Defines the K-state tuple, σ(M), V(M), and the symbol registry that K1-K5 axiomatize |
| `framework/vvv_qmrf_framework_e01_self_certifying_registration_postulate.md` | Upstream — Source for K3 |
| `framework/vvv_qmrf_framework_e06_registering_system_as_process_postulate.md` | Upstream — Source for K2 |
| `framework/vvv_qmrf_framework_e07_registration_validity_location_postulate.md` | Upstream — Source for K4, K5 |
| `synthesis/vvv_qmrf_synthesis_s3_registering_system_as_process_foundation.md` | Upstream — Source for K2 discreteness (Δ lemma) |
| `SYSTEM_Buddhist_Epistemology/system_be_full.md` | Diagonal — BE SOT for lineage annotations |
| `vvv-qmrf/schema_guide.md` | Process — Document creation contract; this document follows schema |

---

## 10. Level 4 Freeze Check — Internal Consistency Verdict / Phán quyết Nhất quán Nội tại

### 10.1 Question / Câu hỏi

> Can the Level 4 definitions (⊥_K, AdmJoint, D_joint, requires_K_joint, Bridge_EWF, C_K, Auth) be formally proven consistent with K1-K8 without external confirmation?

### 10.2 RCA Trace / Truy vết RCA

| Step | Question | Answer |
|------|----------|--------|
| **Define** | What is the "Level 4 freeze check"? | A formal proof that all Level 4 definitions from paper v2.0 §4.3-4.5 are consistent with Layer 1 axioms K1-K8 — no contradiction arises when combining them. |
| **Trace (Why 1)** | Why is this needed? | Level 4 is currently the least stable layer (in community review). Before freezing it, internal consistency must be established so that community feedback does not hit contradictions that could have been caught internally. |
| **Trace (Why 2)** | Why is it hard? | Because Level 4 definitions were designed bottom-up (from EWF use case) while K1-K8 were designed top-down (from BE structural sources). The two directions may not converge. Plus, Level 4 uses complex primitives (⊥, Authority, C_K) whose full formalization is not yet frozen. |
| **Trace (Why 3)** | Why can't it be purely internal? | Because one Level 4 dependency — the relativization defense (Bridge_EWF condition (e), paper v2.0 §4.5) — is a SEMANTIC choice about what counts as "satisfying D_joint." This document treats that boundary as external to K1-K8: VVV-QMRF makes the stance explicit through the relativization defense, rather than deriving it from the K-space axioms themselves. |
| **Isolate** | What are the blockers? | (1) Relativization defense = framework-level semantic commitment required by this formulation of D_joint (not a mathematical gap). (2) Full Level 4 ⊥ boundary clauses = not yet frozen (temporal dependency). (3) General case proof (arbitrary |K_R| and N observers) = requires stronger mathematical foundations. |
| **Fix cause** | What CAN be done internally? | Promote EP → K8 (DONE v1.4). Concrete model consistency proof (DONE v1.3). Edge case testing. General case proof sketch with explicit boundary documentation. |
| **Verify** | How to verify? | Walk every Level 4 definition against K1-K8 in the concrete model (§7). Check no contradiction arises. Document what IS proven vs. what depends on external assumptions. |

### 10.3 What CAN Be Proven Internally / Có thể Chứng minh Nội tại

| # | Statement | Status | Confidence |
|---|-----------|--------|:----------:|
| P1 | K1-K8 are internally consistent (concrete model: 2 observers, 1 event each) | **PROVEN** (§7.2-7.4) | HIGH |
| P2 | Level 4 definitions can be expressed in terms of K1-K8 primitives | **PROVEN** (§7.3) | HIGH |
| P3 | Derivation graph (no circular reasoning, multiple parallel inputs): `requires_K_joint(F,W)=1` ⇒ `D_joint=1` (Condition A bridge); `D_joint=1` ⇒ `C_K exists`; `C_K + V(k_W)=1 + k_F ∈ scope(D_joint)` ⇒ `Auth(k_W→k_F, C_K)=1` [K6]; `o(k_F), o(k_W) + C_K` ⇒ `k_W ⊥ k_F` [K5 minimal ⊥ test]; `Bridge_EWF conditions (a-d) + relativization defense (e)` ⇒ `Bridge_EWF=1`; `k_F <_joint k_W + ⊥ + Auth` ⇒ `K5 fires → V_prov(k_F)→0`; K5 fires under D_joint joint validity claim ⇒ `AdmJoint(iv) violated` ⇒ `¬∃ admissible K_joint` ⇒ `⊥_K(K_F,K_W)`. Note: Auth and ⊥ are PARALLEL inputs to K5 firing, not sequential — ⊥ test (content-based) does not depend on Auth. | **PROVEN** (§7.3, §7.5) | HIGH |
| P4 | Step 6 (K5 fires in K_joint) does NOT depend on any external postulate | **PROVEN** (v1.4: K8 resolves former EP gap; F1: K5 fires on V_prov pre-closure — V_prov/V_final distinction is K5+K7 internal, no new external dependency) | HIGH |
| P5 | K5 minimal ⊥ can be verified by content inspection without invoking Level 4 full ⊥ (circularity absent in concrete model) | **PROVEN** (§7.5 Step 4) | HIGH |
| P6 | K_joint candidate existence is constructible via T1 composition: K1-K8 (carrier + order + cert + V-preservation) + Level 4 inputs (requires_K_joint, D_joint, cross-structure temporal relations from laboratory history). T1 is a composition theorem, not a pure K1-K8 derivation — cross-rel is an external Level 4 input. | **PROVEN for composition** (T1, updated v1.4; F-RCA-P4-02 architectural note added) | HIGH |

### 10.4 What CANNOT Be Proven Internally / Không thể Chứng minh Nội tại

| # | Statement | Why not | Nature of boundary |
|---|-----------|---------|-------------------|
| E1 | Relativization defense: "meta-descriptions do not satisfy D_joint" | Semantic choice about the nature of joint validity — not derived within K1-K8 | **Framework-level semantic commitment** required by this formulation of D_joint |
| E2 | Full Level 4 ⊥ boundary clauses are correct | Still in community review (paper v2.0). Internal consistency with K5 minimal ⊥ can be checked, but community may disagree with boundary clauses. | **Temporal dependency** (resolves when Level 4 freezes) |
| E3 | General case proof (arbitrary N, arbitrary |K_R|) | Requires stronger mathematical foundations (structural induction proofs, category-theoretic colimit properties for N>2). | **Mathematical capacity boundary** (documented honestly) |

### 10.5 Final Verdict / Phán quyết Cuối cùng

> **Level 4 definitions ARE internally consistent with K1-K8 in the concrete model.**
>
> The proof chain has exactly **one declared semantic postulate dependency**: **AJVS** (Axiom of Joint Validity Semantics — formalized in v1.5.6). AJVS defines what counts as satisfying D_joint in this formulation (first-order claim vs meta-description). This is NOT an internal contradiction — it is a named **Semantic Layer postulate** that VVV-QMRF declares explicitly rather than deriving from K1-K8. Copenhagen, Many-Worlds, QBism, and VVV-QMRF make different semantic choices about joint validity; this document only commits VVV-QMRF to the relativization defense.
>
> **Decision:** Level 4 can freeze with **one documented framework-level semantic commitment** (relativization defense). The former EP gap (G1 in v1.3) is resolved by promoting EP → K8. The ⊥ circularity concern (Open Item #14) is absent in the concrete model. The remaining temporal dependency (Level 4 ⊥ full boundary clauses) resolves when paper v2.0 exits community review.
>
> **Confidence level for Level 4 freeze:** **MEDIUM-HIGH.** Internal consistency is proven for the relevant model class. The remaining blocker is the framework-level semantic commitment about what counts as satisfying D_joint in this formulation.

### 10.6 Remaining Action Items After Freeze / Các Mục Hành động Sau Freeze

| # | Item | Priority | Blocks |
|---|------|:--------:|--------|
| A1 | ~~Document relativization defense as "Axiom of Joint Validity Semantics"~~ | ~~High~~ | **Resolved v1.5.6** — AJVS formalized as named Semantic Postulate (Layer 0.5): first-order vs second-order claim distinction, BE lineage (pratyakṣa vs anumāna), conditional scope documented. T3 updated to cite AJVS. (F-RCA-P7-04) |
| A2 | Freeze Level 4 ⊥ boundary clauses after community feedback resolves Open Item #14 | High | T2 non-circularity in general case |
| A3 | General case proof (structural induction on \|K_R\|, N observers) | Medium | T4, E8, E15 |
| A4 | Edge case: E9 null events, E14 validated absence | Medium | E8-E16 audit phase |
| A5 | Category-theoretic proof of K_joint colimit existence (N>2) | Low-Medium | T4 — **T4-H explicit hypothesis added v1.5.6**: T4 conclusions now formally conditional on T4-H; plausibility argument documented; rigorous proof deferred. (F-RCA-P4-06 Option A resolved) |
| A6 | When Level 4 freezes, verify that conditional semantic dependencies — Dep-A (C_K existence precondition, Level 4 §4.3) and Dep-B (T1 `<_joint>` ordering via K2+K8+Level 4) documented in K5/K6/K7 Dependency rows — remain consistent with frozen Level 4 extensional definitions | Medium | Level 4 freeze (resolves Open Item #14) |

---

*Document v1.5.6 — 2026-05-20 — VVV-QMRF §K-AXIOM*
*Status: Mixed — K1: Class C (formal definition); K2–K8, T1–T4: Class D (proposed registration-layer).*
*Layer 1 (K1-K8): Frozen (syntactic; K5/K6/K7 have conditional semantic deps on Level 4). Layer 2 (T1-T3 pending Level 4 freeze + T4 new Class D): Updatable.*
*RCA cascade-sync (v1.5 → v1.5.1): Sprint 1 P0 fixes from line-by-line audit 2026-05-20. (S1a) Header Status corrected: Mixed K1=Class C, K2–K8/T1–T4=Class D (F-RCA-P1-01). (S1b) §0.4 mathematical carrier: "poset" → "chain within K_R, partial across K_R via embeddings" to match K2 v1.2 correction (F-RCA-P1-04). (S1c) §0.5 Layer 1: absolute "do NOT depend on Level 4" → qualified syntactic/semantic isolation with K5/K6/K7 conditional deps; Layer 2: T4 status distinguished from T1-T3 "pending Level 4" (F-RCA-P1-05, F-RCA-P1-07). (S1d) K1 Boundary: "o=∅ not operationalized" → E9 operationalized via K4 isNull guard; E14 structural only (F-RCA-P2-02). (S1e) §5 Claim Traceability: added C-KAXIOM-008b for K8 V-preservation through cross-space embeddings (F-RCA-P5-03). Zero substantive axiom changes — all fixes are cascade-sync of previous revision outcomes.*
*RCA polish (v1.5.1 → v1.5.2): Sprint 2 fixes 2026-05-20. (S2a) K5 Asymmetry clause: "¬∃F → V=1 (no restore)" → qualified V_final post-closure irreversible; V_prov pre-closure reversible if trigger removed — asymmetry absolute only post-K7 closure (F-RCA-P3-03). (S2b) K8 (ii) field preservation: added ΔI auxiliary derivability note — ΔI determined by M+o per E9, preserved auto via M+o preservation; isNull predicate therefore preservation-invariant across embedding; null status cannot flip in K_joint (F-RCA-P3-10). (S2c) Open Item #18: corrected §3.3 content description from "7 predicates (σ, V, ⊥, Auth, D_joint, requires_K_joint, C_K)" → "7 sufficient-condition bridges (Condition A, B, B2, C, D, E, ODC_K) for requires_K_joint"; predicate-level mapping is Layer 4 §4.4 task, not §3.3 (F-RCA-P5-02). Zero axiom text changes — S2b extends K8 formal block with auxiliary derivability note only.*
*RCA substantive axiom fixes (v1.5.3 → v1.5.4): Sprint 4 fixes 2026-05-20. (S4a) K1 Formal block: added explicit t-injectivity injection constraint "∀k1,k2 ∈ K_R: t(k1)=t(k2)→k1=k2" with rationale; also corrected K1 countability claim to forward-ref K2 S2-Δ (F-RCA-P2-03). (S4b) K2 Totality (iv): replaced prose rationale with formal proof citing K1 t-injectivity; updated RegistrationState well-definedness to cite K1 injection explicitly (F-RCA-P2-03). (S4c) K7 Pre-closure: added Stabilization condition — finite K5 transitions guarantee V_prov stabilizes before t_close → V_final well-defined; added equivalent formulation V_final := V_prov(t_close) (F-RCA-P3-07). (S4d) T1 Derivation: restructured as composition theorem — explicit "Layer 1 inputs (K1/K2/K3/K6/K8)" + "Level 4 inputs (requires_K_joint, D_joint, cross-rel from lab history)" sections; architectural note that cross-rel is external Level 4 input not derivable from K1-K8; F7a guard updated with new dependency diagram (F-RCA-P4-02). (S4e) §10.3 P6: corrected "derivable from K1-K8 + scope identifiers" → "constructible via T1 composition: K1-K8 + Level 4 inputs including cross-rel" (F-RCA-P7-03, coupled with P4-02).*
*RCA notation+sync (v1.5.2 → v1.5.3): Sprint 3 fixes 2026-05-20. (S3a) K5 Statement: added forward-reference note "K_R has two readings — native and cross-space via K_joint; see K_R disambiguation in formal block" (F-RCA-P3-01). (S3b) K6 Formal block: added "Notation note" block clarifying Auth(k2→k1) is instance-level, bidirectional within shared C_K permitted, directionality imposed by K5 not K6 (F-RCA-P3-04). (S3c) K7 Statement: added property (d) "K_joint involving K_R becomes final (no reconfiguration)" to match Formal block (F-RCA-P3-06). (S3d) Guardrail #6: rewrote binary "cover vs deferred" as 4-state verdict (COVERED/ENCODED/PARTIAL/OUT-OF-SCOPE/GAP) per §3.2 — E11 corrected from "covered" to OUT-OF-SCOPE; E8 corrected from "fully deferred" to PARTIAL (F-RCA-P5-05). (S3e) §7.1: added notation convention block — ket symbols are K-side labels not H vectors; K_R ≠ H preserved; ⊥ test uses H-side content compatibility as bridge reasoning (F-RCA-P6-01). (S3f) §8 Item #15: Dep-B wording corrected "K2+K8" → "K2+K8+Level 4 cross-rel" with note concrete model supplies cross-rel via lab history (F-RCA-P7-01). Zero axiom text changes — all notation and sync fixes.*
*RCA doc+logic polish (v1.5.4 → v1.5.5): Sprint 5 fixes 2026-05-20. (S5a) §0.2: added parenthetical note distinguishing RCA Motivation trace vs backward Causal trace — both valid, complementary phases (F-RCA-P1-02). (S5b) §0.3: "Carrier set" → "Axiomatized membership rule" — K already has extensional collection; K1 adds formal admission rule, not a new carrier (F-RCA-P1-03). (S5c) K3 Formal block: added act-token convention — M_K is a set of unique event tokens; two events of same type but different timestamps are distinct members (F-RCA-P2-04). (S5d) K4 Statement: simplified — removed redundant cert=1 condition (guaranteed by K1 admission rule); K4(b) clause now covers isNull case explicitly (F-RCA-P2-05). (S5e) K4 Formal block: restructured as two formal clauses — (a) ¬isNull(k) → V=1 and (b) isNull(k) → V=0 — with Joint exhaustiveness note; V(k_null)=0 promoted from commentary to formal axiom clause (F-RCA-P2-06). (S5f) K5 Formal block: added Reversibility corollary with explicit revert path — iff biconditional means V_prov(k1) returns to K4 default=1 if trigger k2 is invalidated and no other k2′ satisfies all conditions (F-RCA-P3-02). (S5g) T1 Statement: "minimal K-space" → "categorical colimit of the embedding diagram" with formal colimit definition + T4 forward-ref (F-RCA-P4-03). (S5h) T1 Derivation: added Order type block — (K_joint,<_joint) is partial; restricted to each image i_X(K_X) it is a chain; across distinct images it is partial (F-RCA-P4-01). (S5i) T3 Derivation: added Temporal precondition block — t_F < t_W explicit; satisfies K5 condition (i) via cross-rel; derivation presupposes EWF ordering (F-RCA-P4-05). (S5j) §7.3 L4-4: clarified K6 frozen (a)+(b)+(c) are CORE Auth criteria sufficient alone; paper §4.4 (a′)–(d′) are Level 4 strengthening that K6 does not require but does not contradict (F-RCA-P6-03). (S5k) §7.3 L4-7: added ⊥-preservation derivation step — K8 preserves o → K5 ⊥ test same result in K_joint → k_W ⊥ k_F carries across embedding (F-RCA-P6-02). (S5l) §7.5 Step 7: citation changed from "Definition of ⊥_K, paper v2.0 §4.4" → "T2 ⊥_K Derivation Theorem; consistent with paper v2.0 §4.4 definition" — proof chain now self-contained (F-RCA-P6-05). (S5m) §7.6 table Step 1: removed K8 from deps list (Step 1 Setup does not use K8; K8 used in Step 6 only) (F-RCA-P6-04). (S5n) §10.3 P3: rewritten from linear chain notation to DAG description — Auth and ⊥ are parallel K5 inputs; ⊥ test (content-based) does not depend on Auth (F-RCA-P7-02). F-RCA-P4-06 (T4 colimit proof) and F-RCA-P7-04 (relativization defense as AJVS axiom) remain DEFERRED pending community feedback. Zero K1-K8 axiom text changes — all Sprint 5 fixes are doc/logic clarifications and formal-block completions.*
*RCA MAJOR resolution (v1.5.5 → v1.5.6): Sprint 6 fixes 2026-05-20. (S6-1) T4 Derivation: added T4-H — Colimit Existence Hypothesis block after F7d guard — T4 conclusions now formally conditional on T4-H; status HYPOTHESIS (not theorem derivable from K1-K8); plausibility argument documented (finite totally-ordered sets with preserving maps have finite colimits); rigorous proof deferred to Open Item A5; if T4-H fails, T1 (constructive N=2) remains valid independently (F-RCA-P4-06 Option A resolved). (S6-2) Added AJVS — Axiom of Joint Validity Semantics as named Semantic Layer 0.5 postulate (separate from K1-K8), inserted between T3 and T4: formalizes first-order vs second-order claim distinction; K_joint satisfies D_joint iff it hosts ORIGINAL first-order K-side validity claims, not meta-descriptions; BE lineage pratyakṣa (first-order) vs anumāna (inferential meta) documented; conditional scope stated — if AJVS rejected, T3 conclusion does not follow but K1-K8 remain valid (F-RCA-P7-04 resolved). (S6-3) T3 Derivation: "External semantic assumption" block renamed "Semantic Postulate dependency — AJVS"; T3 property table row updated from "External assumption" to "Semantic postulate: AJVS (see below)". (S6-4) Layer 2 Summary T3 row: cites AJVS; T4 row: cites T4-H hypothesis; §10.6 A1 marked RESOLVED (AJVS formalized v1.5.6); §10.6 A5 updated noting T4-H hypothesis added v1.5.6; §10.5 Final Verdict updated from "external dependency" to "AJVS semantic postulate dependency". All 10/10 MAJOR findings now closed. Zero K1-K8 axiom text changes — Sprint 6 adds two named postulates (T4-H, AJVS) at Semantic Layer 0.5 and formally scopes T4 conclusions conditional on T4-H.*
*RCA audit (v1.4 → v1.5): Full Phase 1–5 RCA audit completed (plan v28). Phase 1 (F1–F5c): K5 V_prov/V_final lifecycle split (F1, BLOCKING resolved); K6 non-transitivity scoped to distinct C_K contexts (F2); §0.5 isolation paragraph 2-part split (F3); Layer 1 Summary C_K roles (F4); K5 K_R disambiguation + firing precondition + Dep-A/Dep-B documented (F5a–F5c). Phase 2 (F6a–F6c): K6/K7 Dep-A (C_K precondition) + I-03 pattern documented (F6a–F6b); C-KAXIOM-010 rewritten as 2-part syntactic/semantic isolation (F6c). Phase 3 (F7a–F7d): T1 non-circularity guard (F7a); T2 AdmJoint V_prov timing + K7 resolved-demand semantics (F7b); T3 framework-level semantic boundary wording (F7c); T4 global commutativity guard (F7d). Phase 4 (F8a–F8d): E2 K1 vs K4/K7 boundary; E9 definitional null-status boundary; E8 V_prov/T2/E9 precision; BE lineage expanded to 8/8 PASS (F8a–F8d). Phase 5 (F9a–F9d): §7.5 Step 6 V_prov notation (F9a); §7.5 Step 4 stale GAP G4 → G3 label (F9b); §10.3 P4 citation V_prov internal note + §7.5 Step 6 stale "modulo EP" removed (F9c); §7.3 L4-7 K8 canonical V_F/V_W subscript notation (F9d). Phase 6 (F10a–F10f): Open Item #1 K5 V_prov attribution (F10a); Open Item #14 T2 Dep-B note (F10b); Open Item #15 Dep-A/Dep-B satisfied note (F10c); Action Item A6 added — Dep-A/Dep-B post-freeze verification (F10d); document header and version history updated (F10e–F10f).*
*RCA audit (v1.3 → v1.4): (1) EP promoted to K8 (Cross-Space Embedding Preservation) — Layer 1 now has 8 core axioms. K8 guarantees V-preservation through cross-space embeddings. (2) T1 derivation updated: V-preservation now from K8, not external postulate. Former EP gap (G1) RESOLVED. (3) T2 proof attempt gaps reduced from 3 to 2: only relativization defense (G1, framework-level semantic commitment) and Level 4 ⊥ freeze (G3, temporal) remain. (4) Concrete model §7 updated: K8 consistency walk, AdmJoint check (i) now derives from K8. (5) §10 Level 4 Freeze Check verdict added: internal consistency PROVEN for concrete model; relativization defense documented as framework-level semantic boundary. (6) Open Item #13 closed (EP → K8). Open Items #14, #15 updated.*
*Previous (v1.2 → v1.3): (1) Concrete model §7 added: minimal EWF (2 observers, 1 event each). K1-K7 consistency walk completed — no contradictions. Level 4 definitions walk completed — derivation chain verified. (2) T2 proof attempt with 3 gaps. (3) Circularity shown absent in concrete model. (4) Open Items #14, #15 added.*
*Previous (v1.1 → v1.2): K2 corrected to total order. T1 EP gap acknowledged. K6 non-transitivity counterexample. T2 circularity acknowledgment.*
*Previous (v1.0 → v1.1): Added K6, K7, K4 E9 exception, K5 minimal ⊥ definition, K1 cert admission rule. Fixed T1 V-preservation (EP), T2 sufficient-vs-necessary, T3 external assumption.*
*Next: PhilSci submission → Community feedback → Level 4 ⊥ boundary clauses freeze (resolves #14) → T1-T3 finalization → N>2 generalization (T4, #9) → E8-E16 extension audit phase.*
