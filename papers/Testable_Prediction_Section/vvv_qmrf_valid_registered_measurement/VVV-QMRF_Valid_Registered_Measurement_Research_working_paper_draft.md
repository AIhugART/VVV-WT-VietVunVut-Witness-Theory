Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

> **DISCLAIMER:** VVV-QMRF is independent Class D personal research, not Standard Quantum Mechanics, not peer-reviewed or experimentally validated, and not for real-world technical use. Full boundary protocol: `DISCLAIMER.md`.

# When Does an Interaction Become a Valid Registered Measurement?
## A VVV-QMRF Working Paper Draft with a Testability Target for Extended Wigner's Friend Scenarios

**Framework:** VietVunVut Quantum Measurement Registration Framework (VVV-QMRF)  
**Document type:** Working paper draft / theoretical framework proposal / testability-target paper  
**Date:** 2026-05-17  
**Status:** Working paper draft; not peer-reviewed; not experimentally validated  
**Primary claim class:** Registration-layer framework proposal with Class C conjectural application  
**Reader level:** Quantum foundations, philosophy of physics, and cross-disciplinary theoretical research  
**Keywords:** quantum measurement, registration validity, Wigner's Friend, Extended Wigner's Friend, observer-relative facts, Buddhist Pramāṇa epistemology, VVV-QMRF, K-side registration

---

## Abstract

Standard Quantum Mechanics successfully describes physical quantum states, observables, outcome probabilities, and dynamical evolution. This working paper asks a narrower registration-layer question: under what conditions does a physical interaction count as a valid registered measurement for a registering process? The VietVunVut Quantum Measurement Registration Framework (VVV-QMRF) proposes that physical interaction, detector response, K-side registration, and valid registered measurement should be kept conceptually distinct. To make this distinction explicit, the paper defines a six-condition registration-validity criterion, `ValidReg(X, R)`, grounded in three VVV-QMRF postulates: E6, which models the registering system as a process; E1, which supplies occurrence self-certification; and E7, which assigns provisional validity and later invalidation by registered contradiction. The proposed criterion is a K-side registration test, not a modification of the physical `ρ`-side. It does not revise the Born rule, unitary evolution, density-matrix dynamics, or physical collapse. Applied to Extended Wigner's Friend scenarios, the criterion motivates a bounded Class C conjecture: observer-specific valid registrations may fail to embed into a single joint K-side registration space while preserving all validity conditions. This conjecture is presented as a formalization and testability target, not as an experimentally confirmed prediction.

---

## 1. Introduction

Quantum measurement theory contains a familiar conceptual compression. The word "measurement" may refer to a physical interaction, an apparatus response, an outcome update, a record, an observer-relative fact, or a validity-status assignment. Standard Quantum Mechanics gives the physical formalism for states, observables, probabilities, and dynamical evolution. It does not need a separate VVV-QMRF registration layer in order to make successful physical predictions. The present paper therefore does not claim that Standard Quantum Mechanics is incomplete as a predictive physical calculus.

The narrower question examined here is different:

```text
Under what conditions does a physical interaction X become a valid registered measurement for a registering process R?
```

VVV-QMRF addresses this as a registration-layer question. It separates the physical `ρ`-side from the K-side registration architecture. The physical `ρ`-side remains governed by Standard Quantum Mechanics. The K-side asks whether a physical event has been admitted into a process-structured registering system and whether that registration satisfies occurrence, membership, validity, and non-invalidation conditions.

The central distinction is:

```text
physical interaction
≠ detector response
≠ K-side registration
≠ valid registered measurement
```

This distinction is the root-cause fix for the ambiguity addressed by the paper. The visible symptom is that a detector click, physical coupling, or observer report can be called a "measurement" without specifying which layer is being discussed. The root cause is that the registration-validity conditions are not separated from the physical interaction itself. VVV-QMRF proposes `ValidReg(X, R)` as a registration-layer test that makes this separation explicit.

The paper makes four contributions:

1. It defines a layer distinction between physical interaction, detector response, K-side registration, and valid registered measurement.
2. It proposes `ValidReg(X, R)` as a six-condition K-side registration-validity criterion.
3. It applies the criterion to Extended Wigner's Friend scenarios as a stress case for observer-specific registrations.
4. It formulates K-side incommensurability, `K_F ⊥_K K_W`, as a Class C conjecture and testability target.

The paper does not claim that VVV-QMRF replaces Standard Quantum Mechanics, revises the Born rule, supplies a physical collapse mechanism, treats Buddhist Epistemology as physical evidence for Quantum Mechanics, or experimentally confirms K-side incommensurability. Buddhist Pramāṇa epistemology functions here as a structural source model for registration, certification, and validity, not as physical evidence for quantum phenomena.

---

## 2. Background and Scope

### 2.1 Physical `ρ`-Side and K-Side Registration Layer

The physical `ρ`-side is the standard quantum-mechanical layer. It concerns quantum states, observables, physical interactions, outcome probabilities, and physical state-update rules. In ordinary notation, the physical state may be represented by a state vector or density matrix, and the outcome probabilities remain governed by the relevant quantum formalism.

The K-side is the VVV-QMRF registration layer. It concerns whether and how an event is admitted as a measurement-registration act, whether that act belongs to a registering process, whether it carries occurrence certification, and whether it retains validity under later registration conditions. The K-side is not a second Hilbert space, not a new physical substance, and not a replacement for the physical quantum state.

| Layer | Question | Handling in this paper |
|---|---|---|
| Physical `ρ`-side | What physical interaction, state, or outcome probability is described? | Preserved as Standard Quantum Mechanics. |
| Detector response | Did an apparatus or physical system respond? | Treated as physical response, not automatically valid measurement. |
| K-side registration | Was the event admitted as a measurement-registration act? | Modeled as `M_X` inside a registering process. |
| Valid registered measurement | Does the registration satisfy defined validity conditions? | Evaluated by `ValidReg(X, R)`. |

The proposed test classifies registration status. It does not alter physical outcome probabilities.

### 2.2 Source Role of Buddhist Pramāṇa Epistemology

VVV-QMRF is derived from structural analysis of Buddhist Pramāṇa epistemology, especially themes of cognition, occurrence-certification, validity, invalidation, and process-based subject structure. In this paper, those materials function as source analogues for registration architecture. They do not function as physical postulates of Standard Quantum Mechanics.

The boundary is non-negotiable: a structural analogy is not an identity claim. A Buddhist epistemological structure may motivate a K-side registration formalism, but it does not by itself establish a physical mechanism for collapse, decoherence, or outcome selection.

---

## 3. Framework and Method

### 3.1 RCA-Guided Problem Statement

The RCA stack for this paper is:

| RCA layer | Paper-specific formulation |
|---|---|
| Phenomenon | A physical interaction or detector response can be called a measurement. |
| Proximate cause | The term "measurement" compresses physical, apparatus, registration, and validity layers. |
| Underlying mechanism | The registration status of an event is not explicitly separated from the event's physical occurrence. |
| Root cause / new principle | Valid measurement should be defined as a registration-layer status, not automatically inferred from physical interaction alone. |
| Generalization | Extended Wigner's Friend scenarios can be used as a stress case for observer-specific registration validity. |

The changed assumption is therefore precise: instead of assuming that physical interaction alone is sufficient for valid measurement, the paper requires a K-side registration-validity criterion.

### 3.2 E6 → E1 → E7 as Logical Spine

The proposed criterion uses three VVV-QMRF postulates as its minimal logical spine:

```text
E6 gives the domain.
E1 certifies occurrence.
E7 assigns and revises validity.
```

| Postulate | Role in this paper | Boundary |
|---|---|---|
| E6 — Registering-System-as-Process | Defines `R` as a process-structured registering system and types `M_X ∈ R`. | `R` is not a substance, fixed self, or Hilbert-space object. |
| E1 — Self-Certifying Registration | Supplies `σ(M_X)=1`, the occurrence self-certification marker. | Not a consciousness claim and not a second physical detector. |
| E7 — Registration Validity Location | Supplies default K-side validity and possible later invalidation by contradiction. | `V(M_X)` is not a physical observable or absolute metaphysical truth-value. |

This paper does not attempt to present the full E1-E16 architecture. It uses the minimal postulate subset required to define the valid registered measurement criterion.

### 3.3 Symbol Registry

No symbol in the central criterion should be read as stronger than its source status.

| Symbol | Meaning | Claim class | Boundary |
|---|---|---:|---|
| `X` | Physical interaction under consideration. | Support notation | Not automatically a measurement. |
| `ρ` | Physical quantum state description. | External / Standard QM | Not a K-side registration state. |
| `R` | Process-structured registering system. | Class D | Not a substance, self, or Hilbert-space object. |
| `M_X` | K-side measurement-registration act admitted from `X`. | Class D derived notation | Not the raw physical interaction. |
| `M_X ∈ R` | Registration act belongs to registering process `R`. | Class D | E6 domain membership, not physical causation. |
| `σ(M_X)` | Occurrence self-certification marker. | Class D | Not consciousness or introspection. |
| `V(M_X)` | K-side validity status. | Class D | Not a physical observable. |
| `M′` | Later registered contradiction candidate. | Class D | Uses the E7 `M′ ⊥ M` relation; not a second certifier for original occurrence. |
| `ValidReg(X, R)` | `X` counts as valid registered measurement for `R`. | Class D proposal | Registration-layer criterion only. |
| `K_F`, `K_W` | Friend and Wigner K-side registration spaces. | Class D application | Not Hilbert spaces. |
| `K_joint` | Hypothetical joint K-side registration space. | Class C | Not fully formalized. |
| `⊥_K` | K-side incommensurability relation. | Class C | Not canonical QM and not experimentally confirmed. |

---

## 4. The Valid Registered Measurement Criterion

### 4.1 Definition

The target object of the paper is:

```text
ValidReg(X, R)
```

where `X` is a physical interaction and `R` is a process-structured registering system.

The proposed criterion is:

```text
Interaction X is a valid registered measurement for registering process R iff:

1. X occurs at the physical ρ-side.
2. X is admitted into the K-side as a measurement-registration act M_X.
3. M_X belongs to a process-structured registering system R: M_X ∈ R. [E6]
4. M_X self-certifies its occurrence: σ(M_X)=1. [E1]
5. M_X has default K-side validity: V(M_X)=1. [E7]
6. No later contradicting registration M′ invalidates M_X. [E7]
```

Compactly:

```text
ValidReg(X, R) ⇔ X → M_X ∈ R and σ(M_X)=1 and V(M_X)=1 and no M′ invalidates M_X.
```

This is a K-side registration-validity test. It does not modify the Born rule, unitary evolution, density-matrix dynamics, or physical collapse.

### 4.2 Condition 1 — Physical Occurrence

The test begins with a physical interaction. `X` must occur at the physical `ρ`-side. This condition prevents a purely conceptual or linguistic act from being treated as a measurement-registration event without a physical input.

The condition preserves correspondence with Standard Quantum Mechanics. The physical side remains governed by the standard formalism appropriate to the experiment.

### 4.3 Condition 2 — Admission into the K-Side

A physical interaction does not automatically become a K-side measurement-registration act. It must be admitted into the registration architecture as `M_X`. This condition blocks the overcompressed equation:

```text
physical interaction = valid measurement
```

Within VVV-QMRF, that equation is too coarse. The physical event supplies the input, but registration status requires K-side admission.

### 4.4 Condition 3 — Membership in a Registering Process

E6 supplies the domain condition:

```text
M_X ∈ R
```

`R` is a process-structured registering system, not an invariant observer-substance. A registration act is not free-floating; it belongs to a process in which measurement-registration acts are typed by causal continuity. This condition is what makes the test observer- or system-indexed without reducing it to human psychology.

### 4.5 Condition 4 — Occurrence Self-Certification

E1 supplies the occurrence marker:

```text
σ(M_X)=1
```

This means that the registration act carries its own K-side occurrence-certification marker. It does not mean that consciousness collapses the wavefunction. It also does not mean that a second apparatus or later observer is needed to confirm that the registration occurred. E1 is a stopping principle for the K-side version of an infinite meta-registration regress.

### 4.6 Condition 5 — Default K-Side Validity

E7 supplies default K-side validity:

```text
V(M_X)=1
```

This validity status is provisional within the registration architecture. It is not a new physical observable and not an absolute metaphysical truth-value. The point is narrower: once `M_X` is admitted, typed in `R`, and self-certified as having occurred, it receives default K-side validity unless later registered contradiction invalidates it.

### 4.7 Condition 6 — Non-Invalidation by Later Contradiction

E7 also allows invalidation by later registered contradiction:

```text
No M′ invalidates M_X.
```

This condition makes validity asymmetric. Validity is default at the K-side, while invalidity requires a later registered contradiction. The contradiction relation is written `M′ ⊥ M_X`: a later valid registration act shares an admissible comparison context with `M_X`, concerns the same registration target, history, or validity claim, and cannot jointly satisfy the relevant validity conditions with `M_X`. Therefore, claims depending on this relation remain bounded by the Class D status of E7 and by the still-incomplete Step 4 proof.

### 4.8 Failure Cases

The criterion also clarifies negative cases:

| Case | Registration status under `ValidReg(X, R)` |
|---|---|
| `X` does not occur physically. | No valid registered measurement. |
| `X` occurs, but no K-side admission as `M_X` is defined. | Physical interaction or detector response only. |
| `M_X` is not typed inside a process-structured `R`. | Registration act lacks E6 domain membership. |
| `σ(M_X) ≠ 1`. | Occurrence certification is absent. |
| `V(M_X) ≠ 1`. | Default validity is absent or suspended. |
| A later `M′` invalidates `M_X`. | The earlier registration is no longer valid under E7. |

This table is not a new physical classification of quantum events. It is a registration-layer classification of when an interaction counts as a valid registered measurement.

---

## 5. Extended Wigner's Friend as a Stress Case

Extended Wigner's Friend scenarios are useful because they place pressure on observer-specific measurement descriptions. In such scenarios, one observer may have a definite local registration while another observer describes a larger system using a different physical model or registration status. VVV-QMRF does not attempt to resolve the full physical Wigner's Friend problem at the `ρ`-side. It applies `ValidReg(X, R)` separately to observer-specific registering processes.

For Friend `F`:

```text
X_F → M_F ∈ R_F
sigma_F(M_F)=1
V_F(M_F)=1
Therefore F has ValidReg(X_F, R_F).
```

For Wigner `W`:

```text
X_W → M_W ∈ R_W
sigma_W(M_W)=1
V_W(M_W)=1
Therefore W has ValidReg(X_W, R_W).
```

The safe conclusion is:

```text
Friend and Wigner may each have a valid registered measurement inside their own K-side registering process.
```

This local conclusion does not settle whether both registrations can be embedded into one joint K-side registration space. It only prepares the joint-embedding question:

```text
When two observers each satisfy the valid-registration test, can their registrations always be embedded into a single joint K-side registration space?
```

This is the bridge from the main criterion to the conjecture.

---

## 6. Conjecture — K-Side Incommensurability

### 6.1 Statement

The Extended Wigner's Friend application motivates the following bounded conjecture:

```text
Conjecture: K-side incommensurability

In Extended Wigner's Friend scenarios, there may be no K_joint such that
K_F ⊆ K_joint and K_W ⊆ K_joint while all six validity conditions hold
simultaneously for both observer-specific registrations.

Symbolically:
K_F ⊥_K K_W
```

The conjecture should be read carefully. It does not say that reality is subjective, that Friend and Wigner merely obtain different numbers, or that Standard Quantum Mechanics is physically incorrect. It says that two observer-specific K-side registration spaces may fail to embed into a single joint K-side registration space while preserving the same validity architecture.

### 6.2 Derivation Scaffold

The conservative derivation scaffold is:

```text
Step 1 — E6:
Friend and Wigner are modeled as distinct process-structured registering systems R_F and R_W.

Step 2 — E1:
sigma_F(M_F)=1 is intrinsic to M_F inside K_F, and sigma_W(M_W)=1 is intrinsic to M_W inside K_W.

Step 3 — E7:
Each registration has default K-side validity within its own registration process unless invalidated by later registered contradiction.

Step 4 — K_joint attempt:
A joint K-side space would need to preserve both registrations as valid under the same validity architecture. If M_F and M_W are mutually contradicting registrations under the E7 contradiction relation, then a joint validity assignment may fail to satisfy E7.
```

Steps 1-3 are registration-layer applications of active VVV-QMRF sources. Step 4 is the main conjectural step. Registry-level definitions of `K_joint`, `⊥_K`, and `M′ ⊥ M` are now specified, but the Step 4 derivation and operational mapping must still be completed before the conjecture can become a completed derivation.

Therefore the status of this section is:

```text
Class C conjecture / testability target.
Not an experimentally confirmed result.
Not a completed physical prediction.
```

### 6.3 What the Conjecture Does and Does Not Claim

| It claims | It does not claim |
|---|---|
| Some observer-specific K-side registrations may resist joint embedding. | Standard QM requires physical rejection or replacement. |
| The resistance concerns registration validity, not physical dynamics. | Buddhist Epistemology functions as physical evidence for Quantum Mechanics. |
| EWF scenarios are a useful stress case. | Wigner's Friend is fully solved at the physical `ρ`-side. |
| A future formal model can challenge or reject the conjecture. | K-side incommensurability is experimentally confirmed. |

---

## 7. Testability and Disconfirmation

The conjecture becomes scientifically useful only if it can be made challengeable. At the current stage, the paper identifies a testability target rather than a completed empirical protocol.

The formal testability question is:

```text
Does interaction X satisfy Conditions 1-6 for ValidReg(X, R)?
```

The structural testability question is:

```text
Can K_F and K_W be embedded into a K_joint while preserving the six validity conditions?
```

The future empirical target is:

```text
Can the K-side incommensurability relation be mapped to observable Extended Wigner's Friend correlation patterns such as P(o_F, o_W)?
```

The disconfirmation target is:

```text
The K-side incommensurability conjecture would be challenged if an explicitly defined Extended Wigner's Friend protocol and formal registration model produced a K_joint that preserves both observer-specific valid registrations under the six-condition test without contradiction.
```

If such a model exists, then one of three revisions would be required:

1. `⊥_K` is not triggered in that scenario.
2. The proposed E7-based contradiction relation is too broad.
3. The joint-space formalism is stronger than the current VVV-QMRF conjecture anticipates.

The mapping from `⊥_K` to observable correlation patterns such as `P(o_F, o_W)` is not complete in this draft and remains future work. Existing Extended Wigner's Friend experiments and no-go results may provide comparison targets, but VVV-QMRF must first define the operational bridge from K-side incommensurability to measurable data.

---

## 8. Relation to Existing Interpretations

VVV-QMRF should be positioned with neutral comparative language. It does not attack existing interpretations and does not treat Standard Quantum Mechanics as defective. It identifies a registration-layer question and proposes one framework-specific validity criterion.

| Interpretation | Typical measurement handling | VVV-QMRF registration-layer difference |
|---|---|---|
| Copenhagen-style approaches | Measurement is boundary-sensitive and often tied to a classical apparatus role. | VVV-QMRF asks when a physical response becomes a valid K-side registration. |
| Many-Worlds | Physical branching or universal-state evolution represents all outcomes. | VVV-QMRF treats valid registration as singular within a K-side registering process, without modifying physical dynamics. |
| QBism | Outcomes are agent-centered experiences or commitments. | VVV-QMRF adds a proposed registration-validity structure that is not limited to human psychology. |
| Relational Quantum Mechanics | States or facts are relative to systems or observers. | VVV-QMRF is closest here; it proposes E6/E1/E7 machinery for registration validity. |
| Objective Collapse | Physical dynamics are modified to produce collapse. | VVV-QMRF does not propose a new physical collapse law. |

Relational Quantum Mechanics is the closest comparison point because it already treats quantum-state descriptions as relative to systems. VVV-QMRF does not replace Relational Quantum Mechanics. It proposes an additional K-side registration architecture that may clarify how observer-specific valid registrations are structured.

This comparison remains bounded. VVV-QMRF is not presented here as a complete interpretation of Quantum Mechanics. It is presented as a registration-layer framework with a defined validity test.

---

## 9. Scope, Limitations, and Open Formal Tasks

This working paper makes a narrow claim. It defines a VVV-QMRF registration-layer criterion for valid registered measurement and applies that criterion to Extended Wigner's Friend scenarios as a bounded testability target.

The paper does not claim:

```text
VVV-QMRF replaces Standard Quantum Mechanics.
VVV-QMRF revises the Born rule, unitary evolution, density-matrix dynamics, or physical collapse.
Buddhist Epistemology functions as physical evidence for Quantum Mechanics.
K-side incommensurability is experimentally confirmed.
Wigner's Friend is fully resolved at the physical ρ-side.
VVV-QMRF is ready for real-world technical use.
```

The main open formal tasks are:

| Open item | Why it matters | Current status |
|---|---|---|
| Formal definition of `K_joint` | Needed to assess joint embedding. | Defined as a Class D admissible joint K-side registration-space entry; necessary-and-sufficient use conditions remain open. |
| Formal definition of `⊥_K` | Needed to define K-side incommensurability. | Defined as a Class D relation-level registry entry; full proof and operational mapping remain open. |
| Formal definition of `M′ ⊥ M` | Needed to specify contradiction under E7. | Defined as a Class D E7 registered contradiction relation; application proof remains open. |
| Proof or rejection of Step 4 | Needed before claiming completed derivation. | Class C unless proven. |
| Operationalization to `P(o_F, o_W)` | Needed for empirical comparison. | Future work. |
| Comparison with published EWF protocols | Needed for concrete experimental relevance. | Future work unless separately completed. |
| Bibliographic verification | Needed before external submission. | Required before submission. |

The derivation is complete through the application of E6, E1, and E7 to observer-specific valid registrations. The joint-space step remains a Class C conjectural step requiring further formalization.

---

## 10. Conclusion

This working paper isolates the transition from physical interaction to valid registered measurement as the central object of VVV-QMRF testability. The proposed criterion, `ValidReg(X, R)`, distinguishes physical interaction, detector response, K-side registration, and valid registered measurement. It uses E6 to type the registering process, E1 to mark occurrence self-certification, and E7 to assign and revise validity.

The paper preserves Standard Quantum Mechanics at the physical `ρ`-side. It does not revise outcome probabilities, physical dynamics, or collapse mechanisms. Its contribution is not a new physical law, but a registration-layer validity criterion.

Applied to Extended Wigner's Friend scenarios, the criterion motivates a bounded conjecture of K-side incommensurability: observer-specific valid registrations may fail to embed into a single joint K-side registration space while preserving the same validity conditions. That conjecture remains Class C until the Step 4 derivation and the operational comparison targets are fully formalized.

The purpose of the paper is precision before persuasion. It defines, constrains, and makes challengeable the VVV-QMRF concept of valid registered measurement.

---

## Appendix A — RCA and Claim Traceability

### A.1 Minimum RCA Check

```text
Symptom:
The word "measurement" compresses physical interaction, detector response, registration, and validity into one label.

Root cause:
The registration-validity conditions are not separated from physical occurrence.

Changed assumption:
A physical interaction is not automatically a valid registered measurement.

Paper claim:
A physical interaction becomes a valid registered measurement only when it satisfies the six-condition VVV-QMRF K-side criterion.

Paper non-claim:
The criterion does not replace Standard Quantum Mechanics or provide a physical collapse mechanism.

Verification:
E6 supplies the registering process R; E1 supplies σ(M_X)=1; E7 supplies V(M_X)=1 and later invalidation; the EWF conjecture remains Class C until joint-space formalization is completed.
```

### A.2 Claim Inventory

| Claim ID | Claim | Type | Source / verification target | Boundary |
|---|---|---|---|---|
| C-001 | Standard QM describes physical states, observables, probabilities, and dynamics at the `ρ`-side. | External / established | Standard QM literature. | Do not frame Standard QM as logically defective. |
| C-002 | VVV-QMRF asks a separate registration-layer validity question. | Project interpretation | `DISCLAIMER.md`; schema guide; VVV-QMRF framework docs. | Scope-gap claim, not physical critique. |
| C-003 | E6 defines `R` as a process-structured registering system. | Class D | `documents/research_documents/framework/vvv_qmrf_framework_e06_registering_system_as_process_postulate.md`. | `R` is not a Hilbert-space object. |
| C-004 | E1 defines occurrence self-certification `σ(M_X)=1`. | Class D | `documents/research_documents/framework/vvv_qmrf_framework_e01_self_certifying_registration_postulate.md`. | Not a consciousness claim. |
| C-005 | E7 defines default validity and later invalidation. | Class D | `documents/research_documents/framework/vvv_qmrf_framework_e07_registration_validity_location_postulate.md`. | K-side validity, not physical observable. |
| C-006 | `ValidReg(X, R)` is a six-condition registration-validity criterion. | Class D derived proposal | E6 + E1 + E7. | Does not modify physical QM. |
| C-007 | Friend and Wigner may each satisfy local valid registration conditions. | Class D application | Wigner's Friend registration-layer mapping. | Does not resolve full physical WF problem. |
| C-008 | `K_F ⊥_K K_W` may hold in EWF scenarios. | Class C conjecture | Testable prediction plans; future formalization. | Not experimentally confirmed. |
| C-009 | The Step 4 proof and operational mapping require further formalization after registry-level definitions of `K_joint`, `⊥_K`, and `M′ ⊥ M`. | Limitation | Meta-architecture formalization; open task list. | Blocks stronger prediction claims. |

### A.3 Source Corpus

| Source | Role |
|---|---|
| `DISCLAIMER.md` | Boundary source: Class D, not Standard QM, not peer-reviewed, not experimentally validated, not for real-world technical use. |
| `documents/research_documents/vvv-qmrf/schema_guide.md` | Document contract for claim class, formula boundary, source trace, and neutral wording. |
| `documents/research_documents/framework/vvv_qmrf_framework_e06_registering_system_as_process_postulate.md` | E6 source for `R` and `M_X ∈ R`. |
| `documents/research_documents/framework/vvv_qmrf_framework_e01_self_certifying_registration_postulate.md` | E1 source for `σ(M_X)=1`. |
| `documents/research_documents/framework/vvv_qmrf_framework_e07_registration_validity_location_postulate.md` | E7 source for validity and invalidation. |
| `documents/research_documents/meta_architecture/vvv_qmrf_meta_architecture_registration_layer_formalization.md` | K-side symbol and formal architecture source. |
| `documents/research_documents/meta_architecture/vvv_qmrf_meta_architecture_wigners_friend_registration_layer_mapping.md` | Wigner's Friend registration-layer mapping and boundary source. |
| `papers/Testable_Prediction_Section/vvv_qmrf_valid_registered_measurement/VVV-QMRF_Testable_Prediction_Plan_v4.md` | RCA-balanced plan and claim hierarchy for this draft. |
| `papers/Testable_Prediction_Section/extended_wigners_friend_k_side_incommensurability/VVV-QMRF_Testable_Prediction_Plan.md` | Original EWF / `K_F ⊥_K K_W` conjecture scaffold. |

---

## References and Bibliographic Targets to Verify Before External Submission

This working paper draft does not invent finalized bibliographic entries. The following are required reference targets; exact editions, page ranges, DOI information, and citation style must be verified before external submission.

### Standard Quantum Measurement and Foundations

- John von Neumann — mathematical foundations of quantum measurement and measurement-chain formalism.
- Eugene Wigner — original Wigner's Friend framing.
- Standard modern quantum measurement reference, to be selected and verified.

### Extended Wigner's Friend and Observer-Relative Facts

- Frauchiger and Renner — Extended Wigner's Friend no-go structure.
- Časlav Brukner — no-go framing for observer-independent facts.
- Proietti et al. — photonic Extended Wigner's Friend experimental work.
- Bong et al. — Bell-type test of Wigner's Friend assumptions.

### Interpretation Comparisons

- Carlo Rovelli — Relational Quantum Mechanics.
- QBism source target, to be selected and verified.
- Many-Worlds source target, to be selected and verified.
- Objective-collapse source target, to be selected and verified.

### Buddhist Pramāṇa and Structural Source Support

- Dignāga-Dharmakīrti Pramāṇa scholarship on self-awareness, validity, invalidation, and process-based cognition, to be selected and verified.
- These sources support structural background only. They must not be cited as physical evidence for Quantum Mechanics.

---

## Closing Boundary Statement

VVV-QMRF is independent Class D personal research, not Standard Quantum Mechanics, not peer-reviewed or experimentally validated, and not for real-world technical use. The present document is a working paper draft for conceptual and formal critique only.
