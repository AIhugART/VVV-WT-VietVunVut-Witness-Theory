# Schema-Control Traceability — VVV-QMRF Working Paper v2.0

**Status:** Internal project document. Not part of the submitted paper.  
**Paper:** `VVV-QMRF_Working_Paper_v2.0.md`  
**Role:** Implements the VVV-QMRF `publication_draft` control layer required by `documents/research_documents/vvv-qmrf/schema_guide.md`. Keeps the working paper's claims, formulas, and boundaries traceable across revisions.

---

## A.1 Source Corpus and Authority

| Source | Role | Authority boundary |
|---|---|---|
| `SYSTEM_Buddhist_Epistemology/system_be_full.md` | Buddhist Epistemology SOT for node/edge RCA | Final authority for BE node/edge definitions if BE codes are used. |
| Active VVV-QMRF framework documents for E1, E6, E7 | VVV-QMRF source layer | Source for registration-layer postulates and proposed K-side conditions. |
| Prasad (2023) | External Buddhist Pramana support | Supports structural extraction only; does not prove QM claims. |
| Standard QM references | External physics context | Source for P1-P4, Born rule, and unitary dynamics; not modified here. |
| Proietti et al. (2019), Bong et al. (2020) | Existing empirical comparison | Compatibility check only; not confirmation of VVV-QMRF. |

## A.2 Claim Traceability Matrix

| Claim ID | Claim | Type | Source / anchor | Boundary | Verification rule |
|---|---|---|---|---|---|
| C-001 | Standard QM specifies outcome probabilities but is scope-silent on VVV-QMRF registration validity conditions. | interpretive_mapping | Section 1; Standard QM postulates | Does not say Standard QM is defective. | Check wording preserves `scope-silent` boundary. |
| C-002 | VVV-QMRF introduces a K-side registration layer separate from physical Hilbert-space dynamics. | derived | Sections 2.1-2.2; active VVV-QMRF sources | Does not alter P1-P4 or the Born rule. | Confirm every K-side claim remains separate from the rho-side. |
| C-003 | The six-condition test defines valid registered measurement inside K-side modeling. | formal_notation | Section 3.1; E1/E6/E7 lineage | Proposed definition, not established QM law. | Confirm all six conditions are stated and claim class remains D. |
| C-004 | K-side stopping terminates registration regress when Conditions 1-6 hold. | conjecture / derived proposition | Section 3.2 | Does not solve the rho-side measurement problem. | Keep formal proof listed as open item. |
| C-005 | Observer-indexed self-certification separates `K_F` and `K_W`. | formal_notation | Section 3.3; E1 lineage | Not a consciousness claim. | Confirm observer index remains K-side only. |
| C-006 | `requires_K_joint` marks configurations where joint registration validity is structurally required. | formal_notation | Section 4.3 | Sufficient conditions only, not necessary-and-sufficient characterization. | Keep open item for full characterization. |
| C-007 | `K_joint` failure follows when both observers cannot preserve simultaneous validity in one joint K-space. | conjecture / derived proposition | Section 4.5; E7 Axiom 2 lineage | Depends on proposed E7 and `perp_K`; not proven theorem. | Keep Step 4 and relation formalism as open items. |
| C-008 | EWF configurations satisfying Condition A are candidates for K-side incommensurability. | conjecture | Sections 4.3-4.6 | Candidate structural condition, not universal claim for all EWF cases. | Check Condition C/D negative controls remain present. |
| C-009 | LF-level violation is expected only when structural and empirical conditions are jointly sufficient. | conjecture | Sections 4.6 and 5.1 | Absence of LF violation under weak/noisy regimes is not automatic falsification. | Verify falsification condition includes empirical-strength clause. |
| C-010 | Proietti and Bong data are compatible with the registration-layer reading. | boundary_application | Sections 5.2-5.4 | Compatibility is not confirmation. | Confirm wording never says existing data prove VVV-QMRF. |

## A.3 Concept Traceability Matrix

| Concept | Canonical name | Source role | Registration role | Boundary |
|---|---|---|---|---|
| `K` | K-side registration space | VVV-QMRF proposal | Holds registration events and validity states. | Not identical to Hilbert space `H`. |
| `k = <M, o, cert, t, V>` | Minimal K-state tuple | Formal notation | Represents a registration event. | Not a new physical state vector. |
| `M` | Measurement act identifier | E6 lineage | Places an interaction inside a registering process. | Not every physical interaction is admitted as `M`. |
| `σ_R(M)` | Observer-indexed self-certification | E1 lineage | Marks intrinsic K-side occurrence-certification for R. | Not consciousness and not external validation. |
| `V(M)` | K-side validity value | E7 lineage | Tracks default validity and later invalidation. | Not detector efficiency or Born probability. |
| `requires_K_joint` | Joint-registration requirement predicate | VVV-QMRF proposed predicate | Marks when one joint validity structure is required. | Sufficient conditions A-D only. |
| `K_joint` | Proposed joint registration structure | VVV-QMRF proposed model | Attempts to contain `K_F` and `K_W` jointly. | Not directly observed as a physical object. |
| `M_W perp_K M_F` | K-side conflict relation | VVV-QMRF proposed relation | Marks incompatible joint-validity commitments. | Not a Hilbert-space orthogonality claim unless separately formalized. |
| `K_F perp_K K_W` | K-side incommensurability | VVV-QMRF conjectural relation | Marks failed joint validity under required K-joint conditions. | Not universal observer disagreement. |

## A.4 Formula and Symbol Registry

| Formula ID | Expression | Formula class | Symbols | Domain of validity | Interpretation boundary |
|---|---|---|---|---|---|
| F-001 | `k = <M, o, cert, t, V>` | definition | `M`: act; `o`: outcome; `cert`: certification; `t`: registration time; `V`: validity | K-side registration modeling | Does not define a physical quantum state. |
| F-002 | `σ_R(M) in {0,1}` | definition / constraint | `R`: registering system; `M`: measurement act | Observer-indexed K-side self-certification | Does not invoke consciousness. |
| F-003 | `requires_K_joint(F,W,M_F,M_W)` | predicate definition | `F,W`: observers; `M_F,M_W`: acts | EWF configurations with possible joint-validity demand | Sufficient-condition predicate only. |
| F-004 | `M_W perp_K M_F` | conjectural relation | `perp_K`: K-side conflict marker | Same K-space joint-validity analysis | Not physical orthogonality by itself. |
| F-005 | `K_F perp_K K_W` | conjectural relation | `K_F,K_W`: observer-indexed K spaces | EWF cases where `requires_K_joint = 1` and K-joint fails | Not all observer-relative descriptions are incommensurable. |
| F-006 | `rho_mu = mu|Phi^-><Phi^-| + (1-mu)/2(... )` | external physics model | `rho_mu`, `mu`, `Phi^-` | Bong et al. state-family discussion | Used as cited experimental context, not VVV-QMRF invention. |

## A.5 Boundary and Non-Claim Checklist

| Check | Status |
|---|---|
| K-side notation remains separate from rho-side physical dynamics. | Pass if Sections 2, 4, and 5 keep layer separation explicit. |
| Existing experiments are described as compatibility checks only. | Pass if Sections 5.2-5.4 do not use confirmation language. |
| `perp_K` is presented as proposed registration-layer relation. | Pass if Sections 4.4-4.6 keep Class C/D status. |
| `requires_K_joint` is not claimed as necessary and sufficient. | Pass if Section 4.3 and Open Items preserve this limitation. |
| Buddhist Epistemology is used as structural source, not proof of QM. | Pass if Section 2.3 and non-claims preserve this boundary. |
| Standard QM is not framed as logically defective. | Pass if the paper uses `scope-silent`, `registration-layer gap`, or neutral boundary language. |
| Formal proof and purpose-designed experiment remain open. | Pass if Section 7.2 and Section 7.3 remain unchanged or strengthened. |

## A.6 RCA Verification

**Define:** The paper's main risk is not a single sentence but a missing schema-control layer for source, claim, concept, formula, and boundary tracking.

**Trace:** Formal-looking notation can make Class C/D proposals look stronger than their evidence level; this happens when formulas are introduced before their class, symbols, domain, and boundary are declared.

**Isolate:** The root cause is missing traceability infrastructure around a publication-facing draft.

**Fix:** This document adds source hierarchy, claim traceability, concept traceability, formula registry, and boundary checklist without rewriting the main argument.

**Verify:** The root cause is removed only if future revisions update this document whenever a major claim, formula, source, or boundary changes.
