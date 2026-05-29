Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# BR_EX_BE Registry — K-side Bridge: BE ↔ VVV-QMRF

**Version:** 2.9 (2026-05-23 promote_new_bridge: full-run batch +3 K-side)
**Date:** 2026-05-23
**Total Entries:** 80 / **77 active** (+9 promote_new_bridge total: 2 K9_E K-side + 3 DRAFT→ACTIVE + 1 K_PENDING-RCA + 3 full-run K-side) + 2 RECLASSIFIED + 2 FOLDED + 3 draft (superseded)
**Namespace:** BR_EX_BE_00001–BR_EX_BE_00080 active; BR_EX_BE_DRAFT_00073A–00073C retained provenance

---

## Overview

This registry maps Buddhist Epistemology (BE) nodes to VVV-QMRF nodes on the K-side (knowledge-registration side).

| Entry Type | Count | Source |
|-----------|-------|--------|
| `reference_copy` | 36 | Phase 1 graph edges (VVV_TO_BE + DRAFT_BRIDGE_BE_VVV) |
| `new_similarity_candidate` | 1 | Phase 3 cosine similarity (Tier2, cosine >= 0.50) |
| `expert_manual_mapping` | 9 | Phase 6 domain expert mapping (KE-PM resolution) |
| `stretch_expert_mapping` | 23 | Phase 7 KE-OF/KE-SC stretch mapping (batch-approved) |
| `draft_current_core_C4_C5` | 3 | C4/C5 draft-only K-side rows for current-Core nodes outside frozen 52-node EX baseline |
| **Total numbered active/historical rows** | **72** | Excludes draft-only `BR_EX_BE_DRAFT_*` rows from active count and graph sync |

**Direction convention:** Entries normalize to BE_node → VVV_node (K-side: BE anchors VVV).
See `ex_schema_addendum.md §5` for F2 non-reversal policy.

---

## Entries

### BR_EX_BE_00001 — Entry 1

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00001` |
| **Type** | reference_copy |
| **Source Edge Type** | `DRAFT_BRIDGE_BE_VVV` |
| **BE Node** | `N_BE_00046` |
| **BE Concept** | Representationalism |
| **BE Layer** | RCA |
| **VVV Node** | `N_QM_VVV_00021` |
| **VVV Concept** | Registration Lock / Registration-Lock Operator |
| **Direction** | N_BE_00046 → N_QM_VVV_00021 |
| **Relation Type** | draft_bridge_support |
| **Claim Class** | evidence_support |
| **Confidence** | 0.70 |
| **Boundary Note** | Draft only; gate-passed through 263-node audit cycle but not yet formally verified. |
| **Rationale** | BE concept provides K-side support via 263-node audit cycle (draft — pending formal verification) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00002 — Entry 2

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00002` |
| **Type** | reference_copy |
| **Source Edge Type** | `DRAFT_BRIDGE_BE_VVV` |
| **BE Node** | `N_BE_00055` |
| **BE Concept** | Pramāphala |
| **BE Layer** | RCA |
| **VVV Node** | `N_QM_VVV_00027` |
| **VVV Concept** | Registration Self-Completion Matrix / Act-Result Registration Identity |
| **Direction** | N_BE_00055 → N_QM_VVV_00027 |
| **Relation Type** | draft_bridge_support |
| **Claim Class** | evidence_support |
| **Confidence** | 0.70 |
| **Boundary Note** | Draft only; gate-passed through 263-node audit cycle but not yet formally verified. |
| **Rationale** | BE concept provides K-side support via 263-node audit cycle (draft — pending formal verification) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00003 — Entry 3

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00003` |
| **Type** | reference_copy |
| **Source Edge Type** | `DRAFT_BRIDGE_BE_VVV` |
| **BE Node** | `N_BE_00096` |
| **BE Concept** | Anvaya |
| **BE Layer** | RCA |
| **VVV Node** | `N_QM_VVV_00042` |
| **VVV Concept** | Tripartite Registration Validity Matrix / Strict Apparatus Axiom |
| **Direction** | N_BE_00096 → N_QM_VVV_00042 |
| **Relation Type** | draft_bridge_support |
| **Claim Class** | evidence_support |
| **Confidence** | 0.70 |
| **Boundary Note** | Draft only; gate-passed through 263-node audit cycle but not yet formally verified. |
| **Rationale** | BE concept provides K-side support via 263-node audit cycle (draft — pending formal verification) |
| **Origin** | Phase 1 graph |
| **Status** | FOLDED-structural-review |
| **Fold-parent** | BR_EX_BE_00008 (Tri-rūpa-hetu → N_QM_VVV_00042) |
| **Fold-decision** | BIAN-14 structural review (2026-05-21): Anvaya is 2nd condition of Trairūpya, fully captured by D_001 + ED_BE_00111. See `reviews/bian14_structural_review.md`. |

### BR_EX_BE_00004 — Entry 4

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00004` |
| **Type** | reference_copy |
| **Source Edge Type** | `DRAFT_BRIDGE_BE_VVV` |
| **BE Node** | `N_BE_00097` |
| **BE Concept** | Vyatireka |
| **BE Layer** | RCA |
| **VVV Node** | `N_QM_VVV_00042` |
| **VVV Concept** | Tripartite Registration Validity Matrix / Strict Apparatus Axiom |
| **Direction** | N_BE_00097 → N_QM_VVV_00042 |
| **Relation Type** | draft_bridge_support |
| **Claim Class** | evidence_support |
| **Confidence** | 0.70 |
| **Boundary Note** | Draft only; gate-passed through 263-node audit cycle but not yet formally verified. |
| **Rationale** | BE concept provides K-side support via 263-node audit cycle (draft — pending formal verification) |
| **Origin** | Phase 1 graph |
| **Status** | FOLDED-structural-review |
| **Fold-parent** | BR_EX_BE_00008 (Tri-rūpa-hetu → N_QM_VVV_00042) |
| **Fold-decision** | BIAN-14 structural review (2026-05-21): Vyatireka is 3rd condition of Trairūpya, fully captured by D_001 + ED_BE_00112. BIAN-15 link (BR_EX_BE_00005) remains active. See `reviews/bian14_structural_review.md`. |

### BR_EX_BE_00005 — Entry 5

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00005` |
| **Type** | reference_copy |
| **Source Edge Type** | `DRAFT_BRIDGE_BE_VVV` |
| **BE Node** | `N_BE_00097` |
| **BE Concept** | Vyatireka |
| **BE Layer** | RCA |
| **VVV Node** | `N_QM_VVV_00001` |
| **VVV Concept** | Contrapositive Quantum Evidence / Purely Contrastive Quantum Evidence Structure |
| **Direction** | N_BE_00097 → N_QM_VVV_00001 |
| **Relation Type** | draft_bridge_support |
| **Claim Class** | evidence_support |
| **Confidence** | 0.70 |
| **Boundary Note** | Draft only; gate-passed through 263-node audit cycle but not yet formally verified. |
| **Rationale** | BE concept provides K-side support via 263-node audit cycle (draft — pending formal verification) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00006 — Entry 6

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00006` |
| **Type** | reference_copy |
| **Source Edge Type** | `DRAFT_BRIDGE_BE_VVV` |
| **BE Node** | `N_BE_00118` |
| **BE Concept** | Ālambanaparīkṣā |
| **BE Layer** | RCA |
| **VVV Node** | `N_QM_VVV_00021` |
| **VVV Concept** | Registration Lock / Registration-Lock Operator |
| **Direction** | N_BE_00118 → N_QM_VVV_00021 |
| **Relation Type** | draft_bridge_support |
| **Claim Class** | evidence_support |
| **Confidence** | 0.70 |
| **Boundary Note** | Draft only; gate-passed through 263-node audit cycle but not yet formally verified. |
| **Rationale** | BE concept provides K-side support via 263-node audit cycle (draft — pending formal verification) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00007 — Entry 7

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00007` |
| **Type** | reference_copy |
| **Source Edge Type** | `DRAFT_BRIDGE_BE_VVV` |
| **BE Node** | `N_BE_00127` |
| **BE Concept** | Pramāṇa formula |
| **BE Layer** | RCA |
| **VVV Node** | `N_QM_VVV_00027` |
| **VVV Concept** | Registration Self-Completion Matrix / Act-Result Registration Identity |
| **Direction** | N_BE_00127 → N_QM_VVV_00027 |
| **Relation Type** | draft_bridge_support |
| **Claim Class** | evidence_support |
| **Confidence** | 0.70 |
| **Boundary Note** | Draft only; gate-passed through 263-node audit cycle but not yet formally verified. |
| **Rationale** | BE concept provides K-side support via 263-node audit cycle (draft — pending formal verification) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00008 — Entry 8

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00008` |
| **Type** | reference_copy |
| **Source Edge Type** | `DRAFT_BRIDGE_BE_VVV` |
| **BE Node** | `N_BE_00158` |
| **BE Concept** | Tri-rūpa-hetu |
| **BE Layer** | RCA |
| **VVV Node** | `N_QM_VVV_00042` |
| **VVV Concept** | Tripartite Registration Validity Matrix / Strict Apparatus Axiom |
| **Direction** | N_BE_00158 → N_QM_VVV_00042 |
| **Relation Type** | draft_bridge_support |
| **Claim Class** | evidence_support |
| **Confidence** | 0.70 |
| **Boundary Note** | Draft only; gate-passed through 263-node audit cycle but not yet formally verified. |
| **Rationale** | BE concept provides K-side support via 263-node audit cycle (draft — pending formal verification) |
| **Origin** | Phase 1 graph |
| **Sub-evidence** | BR_EX_BE_00003 (Anvaya / N_BE_00096), BR_EX_BE_00004 (Vyatireka / N_BE_00097) — folded under this bridge per BIAN-14 structural review (2026-05-21). See `reviews/bian14_structural_review.md`. |

### BR_EX_BE_00009 — Entry 9

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00009` |
| **Type** | reference_copy |
| **Source Edge Type** | `DRAFT_BRIDGE_BE_VVV` |
| **BE Node** | `N_BE_00161` |
| **BE Concept** | Nonoccurrence condition |
| **BE Layer** | RCA |
| **VVV Node** | `N_QM_VVV_00001` |
| **VVV Concept** | Contrapositive Quantum Evidence / Purely Contrastive Quantum Evidence Structure |
| **Direction** | N_BE_00161 → N_QM_VVV_00001 |
| **Relation Type** | draft_bridge_support |
| **Claim Class** | evidence_support |
| **Confidence** | 0.70 |
| **Boundary Note** | Draft only; gate-passed through 263-node audit cycle but not yet formally verified. |
| **Rationale** | BE concept provides K-side support via 263-node audit cycle (draft — pending formal verification) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00010 — Entry 10

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00010` |
| **Type** | reference_copy |
| **Source Edge Type** | `DRAFT_BRIDGE_BE_VVV` |
| **BE Node** | `N_BE_00161` |
| **BE Concept** | Nonoccurrence condition |
| **BE Layer** | RCA |
| **VVV Node** | `N_QM_VVV_00020` |
| **VVV Concept** | Validated Absence Registration / Conditioned Null Registration |
| **Direction** | N_BE_00161 → N_QM_VVV_00020 |
| **Relation Type** | draft_bridge_support |
| **Claim Class** | evidence_support |
| **Confidence** | 0.70 |
| **Boundary Note** | Draft only; gate-passed through 263-node audit cycle but not yet formally verified. |
| **Rationale** | BE concept provides K-side support via 263-node audit cycle (draft — pending formal verification) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00011 — Entry 11

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00011` |
| **Type** | reference_copy |
| **Source Edge Type** | `DRAFT_BRIDGE_BE_VVV` |
| **BE Node** | `N_BE_00164` |
| **BE Concept** | Pramāṇādhīna prameyādhigama |
| **BE Layer** | RCA |
| **VVV Node** | `N_QM_VVV_00027` |
| **VVV Concept** | Registration Self-Completion Matrix / Act-Result Registration Identity |
| **Direction** | N_BE_00164 → N_QM_VVV_00027 |
| **Relation Type** | draft_bridge_support |
| **Claim Class** | evidence_support |
| **Confidence** | 0.70 |
| **Boundary Note** | Draft only; gate-passed through 263-node audit cycle but not yet formally verified. |
| **Rationale** | BE concept provides K-side support via 263-node audit cycle (draft — pending formal verification) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00012 — Entry 12

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00012` |
| **Type** | reference_copy |
| **Source Edge Type** | `DRAFT_BRIDGE_BE_VVV` |
| **BE Node** | `N_BE_00165` |
| **BE Concept** | Prameyādhīna pramāṇasiddhi |
| **BE Layer** | RCA |
| **VVV Node** | `N_QM_VVV_00027` |
| **VVV Concept** | Registration Self-Completion Matrix / Act-Result Registration Identity |
| **Direction** | N_BE_00165 → N_QM_VVV_00027 |
| **Relation Type** | draft_bridge_support |
| **Claim Class** | evidence_support |
| **Confidence** | 0.70 |
| **Boundary Note** | Draft only; gate-passed through 263-node audit cycle but not yet formally verified. |
| **Rationale** | BE concept provides K-side support via 263-node audit cycle (draft — pending formal verification) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00013 — Entry 13

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00013` |
| **Type** | reference_copy |
| **Source Edge Type** | `DRAFT_BRIDGE_BE_VVV` |
| **BE Node** | `N_BE_00170` |
| **BE Concept** | Non-distinction of means and result |
| **BE Layer** | RCA |
| **VVV Node** | `N_QM_VVV_00027` |
| **VVV Concept** | Registration Self-Completion Matrix / Act-Result Registration Identity |
| **Direction** | N_BE_00170 → N_QM_VVV_00027 |
| **Relation Type** | draft_bridge_support |
| **Claim Class** | evidence_support |
| **Confidence** | 0.70 |
| **Boundary Note** | Draft only; gate-passed through 263-node audit cycle but not yet formally verified. |
| **Rationale** | BE concept provides K-side support via 263-node audit cycle (draft — pending formal verification) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00014 — Entry 14

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00014` |
| **Type** | reference_copy |
| **Source Edge Type** | `DRAFT_BRIDGE_BE_VVV` |
| **BE Node** | `N_BE_00173` |
| **BE Concept** | Bāhyārtha |
| **BE Layer** | RCA |
| **VVV Node** | `N_QM_VVV_00021` |
| **VVV Concept** | Registration Lock / Registration-Lock Operator |
| **Direction** | N_BE_00173 → N_QM_VVV_00021 |
| **Relation Type** | draft_bridge_support |
| **Claim Class** | evidence_support |
| **Confidence** | 0.70 |
| **Boundary Note** | Draft only; gate-passed through 263-node audit cycle but not yet formally verified. |
| **Rationale** | BE concept provides K-side support via 263-node audit cycle (draft — pending formal verification) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00015 — Entry 15

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00015` |
| **Type** | reference_copy |
| **Source Edge Type** | `DRAFT_BRIDGE_BE_VVV` |
| **BE Node** | `N_BE_00175` |
| **BE Concept** | Sārūpya |
| **BE Layer** | RCA |
| **VVV Node** | `N_QM_VVV_00021` |
| **VVV Concept** | Registration Lock / Registration-Lock Operator |
| **Direction** | N_BE_00175 → N_QM_VVV_00021 |
| **Relation Type** | draft_bridge_support |
| **Claim Class** | evidence_support |
| **Confidence** | 0.70 |
| **Boundary Note** | Draft only; gate-passed through 263-node audit cycle but not yet formally verified. |
| **Rationale** | BE concept provides K-side support via 263-node audit cycle (draft — pending formal verification) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00016 — Entry 16

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00016` |
| **Type** | reference_copy |
| **Source Edge Type** | `DRAFT_BRIDGE_BE_VVV` |
| **BE Node** | `N_BE_00179` |
| **BE Concept** | Representative perception |
| **BE Layer** | RCA |
| **VVV Node** | `N_QM_VVV_00021` |
| **VVV Concept** | Registration Lock / Registration-Lock Operator |
| **Direction** | N_BE_00179 → N_QM_VVV_00021 |
| **Relation Type** | draft_bridge_support |
| **Claim Class** | evidence_support |
| **Confidence** | 0.70 |
| **Boundary Note** | Draft only; gate-passed through 263-node audit cycle but not yet formally verified. |
| **Rationale** | BE concept provides K-side support via 263-node audit cycle (draft — pending formal verification) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00017 — Entry 17

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00017` |
| **Type** | reference_copy |
| **Source Edge Type** | `DRAFT_BRIDGE_BE_VVV` |
| **BE Node** | `N_BE_00185` |
| **BE Concept** | Yojanā |
| **BE Layer** | RCA |
| **VVV Node** | `N_QM_VVV_00021` |
| **VVV Concept** | Registration Lock / Registration-Lock Operator |
| **Direction** | N_BE_00185 → N_QM_VVV_00021 |
| **Relation Type** | draft_bridge_support |
| **Claim Class** | evidence_support |
| **Confidence** | 0.70 |
| **Boundary Note** | Draft only; gate-passed through 263-node audit cycle but not yet formally verified. |
| **Rationale** | BE concept provides K-side support via 263-node audit cycle (draft — pending formal verification) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00018 — Entry 18

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00018` |
| **Type** | reference_copy |
| **Source Edge Type** | `DRAFT_BRIDGE_BE_VVV` |
| **BE Node** | `N_BE_00193` |
| **BE Concept** | Dharmakīrti's anti-realism |
| **BE Layer** | RCA |
| **VVV Node** | `N_QM_VVV_00021` |
| **VVV Concept** | Registration Lock / Registration-Lock Operator |
| **Direction** | N_BE_00193 → N_QM_VVV_00021 |
| **Relation Type** | draft_bridge_support |
| **Claim Class** | evidence_support |
| **Confidence** | 0.70 |
| **Boundary Note** | Draft only; gate-passed through 263-node audit cycle but not yet formally verified. |
| **Rationale** | BE concept provides K-side support via 263-node audit cycle (draft — pending formal verification) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00019 — Entry 19

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00019` |
| **Type** | reference_copy |
| **Source Edge Type** | `DRAFT_BRIDGE_BE_VVV` |
| **BE Node** | `N_BE_00203` |
| **BE Concept** | Four process mechanisms |
| **BE Layer** | RCA |
| **VVV Node** | `N_QM_VVV_00027` |
| **VVV Concept** | Registration Self-Completion Matrix / Act-Result Registration Identity |
| **Direction** | N_BE_00203 → N_QM_VVV_00027 |
| **Relation Type** | draft_bridge_support |
| **Claim Class** | evidence_support |
| **Confidence** | 0.70 |
| **Boundary Note** | Draft only; gate-passed through 263-node audit cycle but not yet formally verified. |
| **Rationale** | BE concept provides K-side support via 263-node audit cycle (draft — pending formal verification) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00020 — Entry 20

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00020` |
| **Type** | reference_copy |
| **Source Edge Type** | `DRAFT_BRIDGE_BE_VVV` |
| **BE Node** | `N_BE_00240` |
| **BE Concept** | Perceptual-conceptual gap |
| **BE Layer** | RCA |
| **VVV Node** | `N_QM_VVV_00021` |
| **VVV Concept** | Registration Lock / Registration-Lock Operator |
| **Direction** | N_BE_00240 → N_QM_VVV_00021 |
| **Relation Type** | draft_bridge_support |
| **Claim Class** | evidence_support |
| **Confidence** | 0.70 |
| **Boundary Note** | Draft only; gate-passed through 263-node audit cycle but not yet formally verified. |
| **Rationale** | BE concept provides K-side support via 263-node audit cycle (draft — pending formal verification) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00021 — Entry 21

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00021` |
| **Type** | reference_copy |
| **Source Edge Type** | `DRAFT_BRIDGE_BE_VVV` |
| **BE Node** | `N_BE_00253` |
| **BE Concept** | Anupalabdhi |
| **BE Layer** | RCA |
| **VVV Node** | `N_QM_VVV_00020` |
| **VVV Concept** | Validated Absence Registration / Conditioned Null Registration |
| **Direction** | N_BE_00253 → N_QM_VVV_00020 |
| **Relation Type** | draft_bridge_support |
| **Claim Class** | evidence_support |
| **Confidence** | 0.70 |
| **Boundary Note** | Draft only; gate-passed through 263-node audit cycle but not yet formally verified. |
| **Rationale** | BE concept provides K-side support via 263-node audit cycle (draft — pending formal verification) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00022 — Entry 22

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00022` |
| **Type** | reference_copy |
| **Source Edge Type** | `VVV_TO_BE` |
| **BE Node** | `N_BE_00015` |
| **BE Concept** | Exclusion |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00001` |
| **VVV Concept** | Contrapositive Quantum Evidence / Purely Contrastive Quantum Evidence Structure |
| **Direction** | N_BE_00015 → N_QM_VVV_00001 |
| **Relation Type** | source_analogue_of |
| **Claim Class** | source_analogue |
| **Confidence** | 0.90 |
| **Boundary Note** | Not conceptual identity; VVV concept draws K-side semantics from BE source-analogue. Direction reversed in derived copy (F2: non-reversal recorded here). |
| **Rationale** | VVV concept draws K-side semantics from BE source-analogue (F2: direction label only; original VVV→BE direction preserved) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00023 — Entry 23

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00023` |
| **Type** | reference_copy |
| **Source Edge Type** | `VVV_TO_BE` |
| **BE Node** | `N_BE_00015` |
| **BE Concept** | Exclusion |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00004` |
| **VVV Concept** | Informative Silence - registration |
| **Direction** | N_BE_00015 → N_QM_VVV_00004 |
| **Relation Type** | source_analogue_of |
| **Claim Class** | source_analogue |
| **Confidence** | 0.90 |
| **Boundary Note** | Not conceptual identity; VVV concept draws K-side semantics from BE source-analogue. Direction reversed in derived copy (F2: non-reversal recorded here). |
| **Rationale** | VVV concept draws K-side semantics from BE source-analogue (F2: direction label only; original VVV→BE direction preserved) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00024 — Entry 24

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00024` |
| **Type** | reference_copy |
| **Source Edge Type** | `VVV_TO_BE` |
| **BE Node** | `N_BE_00015` |
| **BE Concept** | Exclusion |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00006` |
| **VVV Concept** | Exclusion-Based State Selection / Exclusion-Based Registration |
| **Direction** | N_BE_00015 → N_QM_VVV_00006 |
| **Relation Type** | source_analogue_of |
| **Claim Class** | source_analogue |
| **Confidence** | 0.90 |
| **Boundary Note** | Not conceptual identity; VVV concept draws K-side semantics from BE source-analogue. Direction reversed in derived copy (F2: non-reversal recorded here). |
| **Rationale** | VVV concept draws K-side semantics from BE source-analogue (F2: direction label only; original VVV→BE direction preserved) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00025 — Entry 25

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00025` |
| **Type** | reference_copy |
| **Source Edge Type** | `VVV_TO_BE` |
| **BE Node** | `N_BE_00015` |
| **BE Concept** | Exclusion |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00020` |
| **VVV Concept** | Validated Absence Registration / Conditioned Null Registration |
| **Direction** | N_BE_00015 → N_QM_VVV_00020 |
| **Relation Type** | source_analogue_of |
| **Claim Class** | source_analogue |
| **Confidence** | 0.90 |
| **Boundary Note** | Not conceptual identity; VVV concept draws K-side semantics from BE source-analogue. Direction reversed in derived copy (F2: non-reversal recorded here). |
| **Rationale** | VVV concept draws K-side semantics from BE source-analogue (F2: direction label only; original VVV→BE direction preserved) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00026 — Entry 26

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00026` |
| **Type** | reference_copy |
| **Source Edge Type** | `VVV_TO_BE` |
| **BE Node** | `N_BE_00021` |
| **BE Concept** | Essential relation |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00025` |
| **VVV Concept** | Intrinsic Relational Binding / Entanglement - registration Architecture |
| **Direction** | N_BE_00021 → N_QM_VVV_00025 |
| **Relation Type** | source_analogue_of |
| **Claim Class** | source_analogue |
| **Confidence** | 0.90 |
| **Boundary Note** | Not conceptual identity; VVV concept draws K-side semantics from BE source-analogue. Direction reversed in derived copy (F2: non-reversal recorded here). |
| **Rationale** | VVV concept draws K-side semantics from BE source-analogue (F2: direction label only; original VVV→BE direction preserved) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00027 — Entry 27

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00027` |
| **Type** | reference_copy |
| **Source Edge Type** | `VVV_TO_BE` |
| **BE Node** | `N_BE_00022` |
| **BE Concept** | Causal efficacy |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00027` |
| **VVV Concept** | Registration Self-Completion Matrix / Act-Result Registration Identity |
| **Direction** | N_BE_00022 → N_QM_VVV_00027 |
| **Relation Type** | source_analogue_of |
| **Claim Class** | source_analogue |
| **Confidence** | 0.90 |
| **Boundary Note** | Not conceptual identity; VVV concept draws K-side semantics from BE source-analogue. Direction reversed in derived copy (F2: non-reversal recorded here). |
| **Rationale** | VVV concept draws K-side semantics from BE source-analogue (F2: direction label only; original VVV→BE direction preserved) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00028 — Entry 28

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00028` |
| **Type** | reference_copy |
| **Source Edge Type** | `VVV_TO_BE` |
| **BE Node** | `N_BE_00001` |
| **BE Concept** | Valid cognition |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00029` |
| **VVV Concept** | Retroactive Registration Override / Formal Measurement Invalidation |
| **Direction** | N_BE_00001 → N_QM_VVV_00029 |
| **Relation Type** | source_analogue_of |
| **Claim Class** | source_analogue |
| **Confidence** | 0.90 |
| **Boundary Note** | Not conceptual identity; VVV concept draws K-side semantics from BE source-analogue. Direction reversed in derived copy (F2: non-reversal recorded here). |
| **Rationale** | VVV concept draws K-side semantics from BE source-analogue (F2: direction label only; original VVV→BE direction preserved) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00029 — Entry 29

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00029` |
| **Type** | reference_copy |
| **Source Edge Type** | `VVV_TO_BE` |
| **BE Node** | `N_BE_00006` |
| **BE Concept** | Erroneous cognition |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00032` |
| **VVV Concept** | Registration Error / Bhrānti Status |
| **Direction** | N_BE_00006 → N_QM_VVV_00032 |
| **Relation Type** | source_analogue_of |
| **Claim Class** | source_analogue |
| **Confidence** | 0.90 |
| **Boundary Note** | Not conceptual identity; VVV concept draws K-side semantics from BE source-analogue. Direction reversed in derived copy (F2: non-reversal recorded here). |
| **Rationale** | VVV concept draws K-side semantics from BE source-analogue (F2: direction label only; original VVV→BE direction preserved) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00030 — Entry 30

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00030` |
| **Type** | reference_copy |
| **Source Edge Type** | `VVV_TO_BE` |
| **BE Node** | `N_BE_00011` |
| **BE Concept** | Self-awareness |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00033` |
| **VVV Concept** | Self-Certifying Registration Operator / Registration Regress Stopper |
| **Direction** | N_BE_00011 → N_QM_VVV_00033 |
| **Relation Type** | source_analogue_of |
| **Claim Class** | source_analogue |
| **Confidence** | 0.90 |
| **Boundary Note** | Not conceptual identity; VVV concept draws K-side semantics from BE source-analogue. Direction reversed in derived copy (F2: non-reversal recorded here). |
| **Rationale** | VVV concept draws K-side semantics from BE source-analogue (F2: direction label only; original VVV→BE direction preserved) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00031 — Entry 31

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00031` |
| **Type** | reference_copy |
| **Source Edge Type** | `VVV_TO_BE` |
| **BE Node** | `N_BE_00029` |
| **BE Concept** | Momentariness |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00039` |
| **VVV Concept** | Registering-System-as-Process Framework / Momentary Registration Series |
| **Direction** | N_BE_00029 → N_QM_VVV_00039 |
| **Relation Type** | source_analogue_of |
| **Claim Class** | source_analogue |
| **Confidence** | 0.90 |
| **Boundary Note** | Not conceptual identity; VVV concept draws K-side semantics from BE source-analogue. Direction reversed in derived copy (F2: non-reversal recorded here). |
| **Rationale** | VVV concept draws K-side semantics from BE source-analogue (F2: direction label only; original VVV→BE direction preserved) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00032 — Entry 32

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00032` |
| **Type** | reference_copy |
| **Source Edge Type** | `VVV_TO_BE` |
| **BE Node** | `N_BE_00018` |
| **BE Concept** | Triple-condition syllogism |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00042` |
| **VVV Concept** | Tripartite Registration Validity Matrix / Strict Apparatus Axiom |
| **Direction** | N_BE_00018 → N_QM_VVV_00042 |
| **Relation Type** | source_analogue_of |
| **Claim Class** | source_analogue |
| **Confidence** | 0.90 |
| **Boundary Note** | Not conceptual identity; VVV concept draws K-side semantics from BE source-analogue. Direction reversed in derived copy (F2: non-reversal recorded here). |
| **Rationale** | VVV concept draws K-side semantics from BE source-analogue (F2: direction label only; original VVV→BE direction preserved) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00033 — Entry 33

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00033` |
| **Type** | reference_copy |
| **Source Edge Type** | `VVV_TO_BE` |
| **BE Node** | `N_BE_00009` |
| **BE Concept** | Non-conceptual perception |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00044` |
| **VVV Concept** | Pre-Symbolic Stratum / Formalism-External Physical Event |
| **Direction** | N_BE_00009 → N_QM_VVV_00044 |
| **Relation Type** | source_analogue_of |
| **Claim Class** | source_analogue |
| **Confidence** | 0.90 |
| **Boundary Note** | Not conceptual identity; VVV concept draws K-side semantics from BE source-analogue. Direction reversed in derived copy (F2: non-reversal recorded here). |
| **Rationale** | VVV concept draws K-side semantics from BE source-analogue (F2: direction label only; original VVV→BE direction preserved) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00034 — Entry 34

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00034` |
| **Type** | reference_copy |
| **Source Edge Type** | `VVV_TO_BE` |
| **BE Node** | `N_BE_00012` |
| **BE Concept** | Transcendental perception |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00048` |
| **VVV Concept** | Limit-Faculty Registration / Transcendental Registration Mode |
| **Direction** | N_BE_00012 → N_QM_VVV_00048 |
| **Relation Type** | source_analogue_of |
| **Claim Class** | source_analogue |
| **Confidence** | 0.90 |
| **Boundary Note** | Not conceptual identity; VVV concept draws K-side semantics from BE source-analogue. Direction reversed in derived copy (F2: non-reversal recorded here). |
| **Rationale** | VVV concept draws K-side semantics from BE source-analogue (F2: direction label only; original VVV→BE direction preserved) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00035 — Entry 35

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00035` |
| **Type** | reference_copy |
| **Source Edge Type** | `VVV_TO_BE` |
| **BE Node** | `N_BE_00029` |
| **BE Concept** | Momentariness |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00051` |
| **VVV Concept** | Temporal Discontinuity Doctrine / Moment-to-Moment Quantum Transition |
| **Direction** | N_BE_00029 → N_QM_VVV_00051 |
| **Relation Type** | source_analogue_of |
| **Claim Class** | source_analogue |
| **Confidence** | 0.90 |
| **Boundary Note** | Not conceptual identity; VVV concept draws K-side semantics from BE source-analogue. Direction reversed in derived copy (F2: non-reversal recorded here). |
| **Rationale** | VVV concept draws K-side semantics from BE source-analogue (F2: direction label only; original VVV→BE direction preserved) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00036 — Entry 36

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00036` |
| **Type** | reference_copy |
| **Source Edge Type** | `VVV_TO_BE` |
| **BE Node** | `N_BE_00007` |
| **BE Concept** | Doubt |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00054` |
| **VVV Concept** | Pre-Measurement Registration Indeterminacy / Structured Registration-Doubt State |
| **Direction** | N_BE_00007 → N_QM_VVV_00054 |
| **Relation Type** | source_analogue_of |
| **Claim Class** | source_analogue |
| **Confidence** | 0.90 |
| **Boundary Note** | Not conceptual identity; VVV concept draws K-side semantics from BE source-analogue. Direction reversed in derived copy (F2: non-reversal recorded here). |
| **Rationale** | VVV concept draws K-side semantics from BE source-analogue (F2: direction label only; original VVV→BE direction preserved) |
| **Origin** | Phase 1 graph |

### BR_EX_BE_00037 — Entry 37

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00037` |
| **Type** | new_similarity_candidate |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00086` |
| **BE Concept** | Momentariness |
| **BE Layer** | evidence |
| **VVV Node** | `N_QM_VVV_00051` |
| **VVV Concept** | Temporal Discontinuity Doctrine / Moment-to-Moment Quantum Transition |
| **Direction** | N_BE_00086 → N_QM_VVV_00051 |
| **Relation Type** | conceptual_parallel |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.56 (cosine=0.564452) |
| **Boundary Note** | Similarity-based only (cosine ≥ 0.50); requires domain expert review before promotion. N_BE_00086 is evidence-layer duplicate of core N_BE_00029 (already source_analogue via BR_EX_BE_00035). |
| **Rationale** | BE evidence-layer Momentariness node has semantic structural parallel with VVV Temporal Discontinuity concept identified via Phase 3 embedding similarity (all-mpnet-base-v2, dim=768) |
| **Origin** | Phase 3 similarity (Tier2) — F11 RCA fix (was ghost entry with empty fields) |

### BR_EX_BE_00038 — Entry 38

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00038` |
| **Type** | expert_manual_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00013` |
| **BE Concept** | Particular / Unique mark (svalakṣaṇa) |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00011` |
| **VVV Concept** | Dual-Phase Registration Certification |
| **Direction** | N_BE_00013 → N_QM_VVV_00011 |
| **Relation Type** | structural_analogy |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.32 (cosine=0.317, expert-validated) |
| **Boundary Note** | Structural analogy only. Svalakṣaṇa grounds the intrinsic triggering phase of dual-phase registration. Not identity claim. |
| **Rationale** | Dual-phase registration formalizes the two-step epistemic act: (1) causal contact with svalakṣaṇa, (2) conceptual certification via sāmānyalakṣaṇa. Cross-validated via Dignāga PS I.3-4. |
| **Origin** | Phase 6 expert mapping (KE-PM resolution) |

### BR_EX_BE_00039 — Entry 39

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00039` |
| **Type** | expert_manual_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00001` |
| **BE Concept** | Valid cognition (pramāṇa) |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00018` |
| **VVV Concept** | Verification-Integrated Density Matrix Evolution |
| **Direction** | N_BE_00001 → N_QM_VVV_00018 |
| **Relation Type** | functional_analogy |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.30 (cosine=0.298, expert-validated) |
| **Boundary Note** | Functional analogy: pramāṇa as self-verifying cognition (svataḥ-prāmāṇya) parallels verification-integrated evolution. |
| **Rationale** | Verification-integrated density matrix evolution models simultaneous evolution and validation; maps to pramāṇa as non-deceptive cognition (avisamvādi) in Dharmakīrti PV I. |
| **Origin** | Phase 6 expert mapping (KE-PM resolution) |

### BR_EX_BE_00040 — Entry 40

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00040` |
| **Type** | expert_manual_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00052` |
| **BE Concept** | Pramā (veridical cognition) |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00031` |
| **VVV Concept** | Registration Weight / Hierarchical Reliability |
| **Direction** | N_BE_00052 → N_QM_VVV_00031 |
| **Relation Type** | structural_analogy |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.29 (cosine=0.289, expert-validated medium-high) |
| **Boundary Note** | Structural analogy: registration weight formalizes the graded epistemic authority (prāmāṇya) hierarchy: pratyakṣa > anumāna > śabda. |
| **Rationale** | Registration weight quantifies epistemic reliability; directly maps to pramā as the graded outcome of pramāṇa with degrees of epistemic authority. |
| **Origin** | Phase 6 expert mapping (KE-PM resolution) |

### BR_EX_BE_00041 — Entry 41

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00041` |
| **Type** | expert_manual_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00006` |
| **BE Concept** | Erroneous cognition (viparyaya) |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00036` |
| **VVV Concept** | Null Registering-System Event |
| **Direction** | N_BE_00006 → N_QM_VVV_00036 |
| **Relation Type** | functional_analogy |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.27 (cosine=0.272, expert-validated) |
| **Boundary Note** | Functional analogy: null registration = system present but no valid output. Maps to viparyaya as cognitive failure mode per Dharmakīrti PV III. |
| **Rationale** | Null registering-system event = apparatus present but producing no valid output; maps to viparyaya as the failure mode of the pramāṇa instrument. |
| **Origin** | Phase 6 expert mapping (KE-PM resolution) |

### BR_EX_BE_00042 — Entry 42

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00042` |
| **Type** | expert_manual_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00009` |
| **BE Concept** | Non-conceptual perception (nirvikalpaka pratyakṣa) |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00038` |
| **VVV Concept** | Measured-but-Unregistered K-State |
| **Direction** | N_BE_00009 → N_QM_VVV_00038 |
| **Relation Type** | structural_analogy |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.31 (cosine=0.308, expert-validated high) |
| **Boundary Note** | Structural analogy: measured-but-unregistered = causal contact without conceptual registration. Maps to nirvikalpaka pratyakṣa (bare perception before kalpanā overlay). |
| **Rationale** | Physical interaction occurred but no epistemic registration resulted; maps to nirvikalpaka pratyakṣa: sensory contact (kalpanā-apoḍha) not yet conceptualized. Phase 3 also found ρ-match (N_QM_00022, 0.530). |
| **Origin** | Phase 6 expert mapping (KE-PM resolution) |

### BR_EX_BE_00043 — Entry 43

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00043` |
| **Type** | expert_manual_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00018` |
| **BE Concept** | Triple-condition syllogism (trairūpya) |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00043` |
| **VVV Concept** | Trairūpya Apparatus Validity Conditions |
| **Direction** | N_BE_00018 → N_QM_VVV_00043 |
| **Relation Type** | terminological_identity |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.35 (cosine=0.348, expert-validated high — terminological match) |
| **Boundary Note** | Direct terminological identity: VVV trairūpya re-interprets Dignāga's Hetucakra triple-condition (pakṣa-dharmatva, anvaya, vyatireka) as apparatus validity conditions. |
| **Rationale** | Trairūpya in VVV formalizes the same triple-condition from Dignāga's PS. VVV re-interprets as apparatus validity for quantum registration. Strongest conceptual link among Phase 6 mappings. |
| **Origin** | Phase 6 expert mapping (KE-PM resolution) |

### BR_EX_BE_00044 — Entry 44

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00044` |
| **Type** | expert_manual_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00086` |
| **BE Concept** | Momentariness (kṣaṇabhaṅga) |
| **BE Layer** | evidence |
| **VVV Node** | `N_QM_VVV_00045` |
| **VVV Concept** | Pre-Symbolic Event ε(M) |
| **Direction** | N_BE_00086 → N_QM_VVV_00045 |
| **Relation Type** | structural_analogy |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.35 (cosine=0.350, expert-validated medium-high) |
| **Boundary Note** | Structural analogy: ε(M) = raw pre-symbolic event before mathematical registration; kṣaṇabhaṅga = momentary particular before conceptualization. Both share pre-conceptual + fleeting structure. |
| **Rationale** | Pre-symbolic event ε(M) maps to kṣaṇabhaṅga: the momentary svalakṣaṇa that exists for exactly one kṣaṇa before conceptual overlay. |
| **Origin** | Phase 6 expert mapping (KE-PM resolution) |

### BR_EX_BE_00045 — Entry 45

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00045` |
| **Type** | expert_manual_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00008` |
| **BE Concept** | Conceptual construction (kalpanā/vikalpa) |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00047` |
| **VVV Concept** | Degree of Symbolization |
| **Direction** | N_BE_00008 → N_QM_VVV_00047 |
| **Relation Type** | functional_analogy |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.32 (cosine=0.320, expert-validated high) |
| **Boundary Note** | Functional analogy: symbolization degree quantifies the nirvikalpaka→savikalpaka spectrum. Dignāga's binary is generalized to continuous [0,1] measure. |
| **Rationale** | Degree of symbolization = amount of conceptual overlay on a registration event. Directly maps to kalpanā/vikalpa as conceptual construction. Degree 0 = nirvikalpaka, degree 1 = full savikalpaka. |
| **Origin** | Phase 6 expert mapping (KE-PM resolution) |

### BR_EX_BE_00046 — Entry 46

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00046` |
| **Type** | expert_manual_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00083` |
| **BE Concept** | Samādhi (meditative concentration) |
| **BE Layer** | evidence |
| **VVV Node** | `N_QM_VVV_00050` |
| **VVV Concept** | Non-Ordinary Valid Registration Output |
| **Direction** | N_BE_00083 → N_QM_VVV_00050 |
| **Relation Type** | functional_analogy |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.29 (cosine=0.285, expert-validated) |
| **Boundary Note** | Functional analogy: samādhi is the epistemic precondition enabling yogipratyakṣa; non-ordinary registration output is the formal result of yogipratyakṣa-class registration. |
| **Rationale** | Non-ordinary valid registration = yogipratyakṣa output. Samādhi is the necessary condition per Dharmakīrti PV III.281-286. Parent N_QM_VVV_00048 already mapped. |
| **Origin** | Phase 6 expert mapping (KE-PM resolution) |
---

## Phase 7 Stretch Mapping Entries (v1.6 batch-approved)

### BR_EX_BE_00047 — Entry 47

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00047` |
| **Type** | stretch_expert_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00015` |
| **BE Concept** | Apoha / Exclusion |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00003` |
| **VVV Concept** | Projection Operator / Null-Projection Op |
| **Direction** | N_BE_00015 → N_QM_VVV_00003 |
| **Relation Type** | operator_decomposition |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.46 (RCA score; Phase 7 batch-approved) |
| **Boundary Note** | Maps projection selection to K-side exclusion by alternatives; not a Hilbert-space identity. |
| **Rationale** | Projection operator semantics are decomposed as selection-by-exclusion. Apoha supplies the K-side exclusion structure. |
| **Origin** | Phase 7 KE-OF stretch mapping; score 4.6/5; see `phase7_ke_of_rca_log.md` |

### BR_EX_BE_00048 — Entry 48

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00048` |
| **Type** | stretch_expert_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00018` |
| **BE Concept** | Triple-condition syllogism (trairupya) |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00010` |
| **VVV Concept** | PVM-equivalent Registration Authority |
| **Direction** | N_BE_00018 → N_QM_VVV_00010 |
| **Relation Type** | operator_decomposition |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.45 (RCA score; Phase 7 batch-approved) |
| **Boundary Note** | Trairupya is a K-side validity analogue, not a projector-valued measure. |
| **Rationale** | PVM authority is decomposed as validity-constraint semantics; trairupya supplies the three-condition validity structure. |
| **Origin** | Phase 7 KE-OF stretch mapping; score 4.5/5; see `phase7_ke_of_rca_log.md` |

### BR_EX_BE_00049 — Entry 49

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00049` |
| **Type** | stretch_expert_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00234` |
| **BE Concept** | Avisamvaditva / Reliability |
| **BE Layer** | evidence |
| **VVV Node** | `N_QM_VVV_00014` |
| **VVV Concept** | Extrinsic Registration-Certification Operator C_ext |
| **Direction** | N_BE_00234 → N_QM_VVV_00014 |
| **Relation Type** | operator_decomposition |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.46 (RCA score; Phase 7 batch-approved) |
| **Boundary Note** | Maps certification reliability, not physical detector response. |
| **Rationale** | Extrinsic certification is decomposed as non-deceptive registration validity; avisamvaditva supplies reliability semantics. |
| **Origin** | Phase 7 KE-OF stretch mapping; score 4.6/5; see `phase7_ke_of_rca_log.md` |

### BR_EX_BE_00050 — Entry 50

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00050` |
| **Type** | stretch_expert_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00029` |
| **BE Concept** | Momentariness |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00023` |
| **VVV Concept** | Registration Lock V_yava / Irreversible Registration Lock |
| **Direction** | N_BE_00029 → N_QM_VVV_00023 |
| **Relation Type** | operator_decomposition |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.45 (RCA score; Phase 7 batch-approved) |
| **Boundary Note** | Maps temporal boundary/non-return structure, not physical irreversibility. |
| **Rationale** | Registration lock is decomposed as a boundary after which the event is no longer the same registration moment. |
| **Origin** | Phase 7 KE-OF stretch mapping; score 4.5/5; see `phase7_ke_of_rca_log.md` |

### BR_EX_BE_00051 — Entry 51

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00051` |
| **Type** | stretch_expert_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00022` |
| **BE Concept** | Arthakriya / Causal efficacy |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00028` |
| **VVV Concept** | Act-Result Tensor T_act-res |
| **Direction** | N_BE_00022 → N_QM_VVV_00028 |
| **Relation Type** | operator_decomposition |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.47 (RCA score; Phase 7 batch-approved) |
| **Boundary Note** | Maps act-result function, not tensor algebra. |
| **Rationale** | Act-result tensor semantics are decomposed as successful function/effect; arthakriya supplies act-result efficacy. |
| **Origin** | Phase 7 KE-OF stretch mapping; score 4.7/5; see `phase7_ke_of_rca_log.md` |

### BR_EX_BE_00052 — Entry 52

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00052` |
| **Type** | stretch_expert_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00006` |
| **BE Concept** | Bhranti / Erroneous cognition |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00030` |
| **VVV Concept** | Invalidation Operator O_bhranti |
| **Direction** | N_BE_00006 → N_QM_VVV_00030 |
| **Relation Type** | operator_decomposition |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.48 (RCA score; Phase 7 batch-approved) |
| **Boundary Note** | Maps epistemic invalidity, not quantum state invalidation. |
| **Rationale** | Invalidation operator semantics are decomposed as recognition of erroneous registration. |
| **Origin** | Phase 7 KE-OF stretch mapping; score 4.8/5; see `phase7_ke_of_rca_log.md` |

### BR_EX_BE_00053 — Entry 53

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00053` |
| **Type** | stretch_expert_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00011` |
| **BE Concept** | Svasaṃvedana / Self-awareness |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00034` |
| **VVV Concept** | Reflexive Registration Operator R_svasa |
| **Direction** | N_BE_00011 → N_QM_VVV_00034 |
| **Relation Type** | operator_decomposition |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.48 (RCA score; Phase 7 batch-approved) |
| **Boundary Note** | Maps reflexive certification, not physical self-awareness. |
| **Rationale** | Reflexive operator semantics are decomposed as self-certifying registration structure. |
| **Origin** | Phase 7 KE-OF stretch mapping; score 4.8/5; see `phase7_ke_of_rca_log.md` |

### BR_EX_BE_00054 — Entry 54

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00054` |
| **Type** | stretch_expert_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00253` |
| **BE Concept** | Anupalabdhi / Non-perception |
| **BE Layer** | evidence |
| **VVV Node** | `N_QM_VVV_00037` |
| **VVV Concept** | Null Registration Operator E_empty |
| **Direction** | N_BE_00253 → N_QM_VVV_00037 |
| **Relation Type** | operator_decomposition |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.46 (RCA score; Phase 7 batch-approved) |
| **Boundary Note** | Maps non-registration as non-apprehension, not a null projection identity. |
| **Rationale** | Null operator semantics are decomposed as K-side non-apprehension/non-registration. |
| **Origin** | Phase 7 KE-OF stretch mapping; score 4.6/5; see `phase7_ke_of_rca_log.md` |

### BR_EX_BE_00055 — Entry 55

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00055` |
| **Type** | stretch_expert_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00250` |
| **BE Concept** | Tadutpatti / Causal production |
| **BE Layer** | evidence |
| **VVV Node** | `N_QM_VVV_00041` |
| **VVV Concept** | Causal Memory Projection Pi_causal |
| **Direction** | N_BE_00250 → N_QM_VVV_00041 |
| **Relation Type** | operator_decomposition |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.45 (RCA score; Phase 7 batch-approved) |
| **Boundary Note** | Maps causal linkage only, not a memory projection operator. |
| **Rationale** | Causal memory projection is decomposed as causal-production linkage in the registration chain. |
| **Origin** | Phase 7 KE-OF stretch mapping; score 4.5/5; see `phase7_ke_of_rca_log.md` |

### BR_EX_BE_00056 — Entry 56

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00056` |
| **Type** | stretch_expert_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00008` |
| **BE Concept** | Kalpana / Conceptual construction |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00046` |
| **VVV Concept** | Symbolization Operator Lambda |
| **Direction** | N_BE_00008 → N_QM_VVV_00046 |
| **Relation Type** | operator_decomposition |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.48 (RCA score; Phase 7 batch-approved) |
| **Boundary Note** | Maps symbolization/conceptualization, not a physical symbol operator. |
| **Rationale** | Symbolization operator semantics are decomposed as conceptual construction. |
| **Origin** | Phase 7 KE-OF stretch mapping; score 4.8/5; see `phase7_ke_of_rca_log.md` |

### BR_EX_BE_00057 — Entry 57

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00057` |
| **Type** | stretch_expert_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00012` |
| **BE Concept** | Alaukika perception |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00049` |
| **VVV Concept** | Limit-Faculty Registration Operator M_trans |
| **Direction** | N_BE_00012 → N_QM_VVV_00049 |
| **Relation Type** | operator_decomposition |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.47 (RCA score; Phase 7 batch-approved) |
| **Boundary Note** | Maps non-ordinary registration-function, not quantum measurement by yogic perception. |
| **Rationale** | Limit-faculty operator is decomposed as non-ordinary perception/registration capacity. |
| **Origin** | Phase 7 KE-OF stretch mapping; score 4.7/5; see `phase7_ke_of_rca_log.md` |

### BR_EX_BE_00058 — Entry 58

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00058` |
| **Type** | stretch_expert_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00029` |
| **BE Concept** | Momentariness |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00052` |
| **VVV Concept** | Discrete Transition Operator T_ksana |
| **Direction** | N_BE_00029 → N_QM_VVV_00052 |
| **Relation Type** | operator_decomposition |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.47 (RCA score; Phase 7 batch-approved) |
| **Boundary Note** | Maps discrete transition structurally, not quantum dynamics. |
| **Rationale** | Discrete transition operator is decomposed as moment-to-moment discontinuity. |
| **Origin** | Phase 7 KE-OF stretch mapping; score 4.7/5; see `phase7_ke_of_rca_log.md` |

### BR_EX_BE_00059 — Entry 59

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00059` |
| **Type** | stretch_expert_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00007` |
| **BE Concept** | Samsaya / Doubt |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00055` |
| **VVV Concept** | Indeterminacy Operator S_samsaya |
| **Direction** | N_BE_00007 → N_QM_VVV_00055 |
| **Relation Type** | operator_decomposition |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.48 (RCA score; Phase 7 batch-approved) |
| **Boundary Note** | Maps epistemic indeterminacy, not quantum indeterminacy as physical law. |
| **Rationale** | Indeterminacy operator semantics are decomposed as undecided K-side status. |
| **Origin** | Phase 7 KE-OF stretch mapping; score 4.8/5; see `phase7_ke_of_rca_log.md` |

### BR_EX_BE_00060 — Entry 60

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00060` |
| **Type** | stretch_expert_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00097` |
| **BE Concept** | Vyatireka / Negative concomitance |
| **BE Layer** | evidence |
| **VVV Node** | `N_QM_VVV_00007` |
| **VVV Concept** | Counterfactual Evidential Branch |
| **Direction** | N_BE_00097 → N_QM_VVV_00007 |
| **Relation Type** | sub_concept_direct_anchor |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.38 (RCA score; Phase 7 batch-approved) |
| **Boundary Note** | Maps absence-side evidence, not quantum counterfactual physics. |
| **Rationale** | Counterfactual evidential branch receives a direct K-side anchor in negative concomitance. |
| **Origin** | Phase 7 KE-SC stretch mapping; score 3.8/5; see `phase7_ke_sc_rca_log.md` |

### BR_EX_BE_00061 — Entry 61 ⚠️ RECLASSIFIED-v1.7

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00061` |
| **Type** | stretch_expert_mapping_RECLASSIFIED_v1_7 |
| **v1.7 Status** | **RECLASSIFIED-v1.7-KE-SC-THRESHOLD-RAISE** (no longer active in v1.7 graph) |
| **v1.7 Reason** | Score 3.7/5 below v1.7 KE-SC threshold 4.0/5; boundary guard "unelaborated registration ≠ IFM" too thin (Nirvikalpaka is broad concept; IFM is QM-specific experiment) |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00009` |
| **BE Concept** | Nirvikalpaka / Non-conceptual perception |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00008` |
| **VVV Concept** | Ideal Information Without Direct Disturbance |
| **Direction** | N_BE_00009 → N_QM_VVV_00008 |
| **Relation Type** | sub_concept_direct_anchor |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.37 (RCA score; Phase 7 batch-approved at 3.5/5 threshold; v1.7 reclassified) |
| **Boundary Note** | Maps unelaborated registration, not interaction-free measurement. |
| **Rationale** | Information without direct disturbance is anchored to a non-conceptual registration mode. |
| **Origin** | Phase 7 KE-SC stretch mapping; score 3.7/5; see `phase7_ke_sc_rca_log.md` and `phase7_ke_sc_rca_log.md` v1.7 annotations |

### BR_EX_BE_00062 — Entry 62

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00062` |
| **Type** | stretch_expert_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00250` |
| **BE Concept** | Tadutpatti / Causal production |
| **BE Layer** | evidence |
| **VVV Node** | `N_QM_VVV_00012` |
| **VVV Concept** | Intrinsic Causal Triggering Phase |
| **Direction** | N_BE_00250 → N_QM_VVV_00012 |
| **Relation Type** | sub_concept_direct_anchor |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.40 (RCA score; Phase 7 batch-approved) |
| **Boundary Note** | Maps causal-production structure only. |
| **Rationale** | Intrinsic triggering phase receives a direct K-side causal-production anchor. |
| **Origin** | Phase 7 KE-SC stretch mapping; score 4.0/5; see `phase7_ke_sc_rca_log.md` |

### BR_EX_BE_00063 — Entry 63

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00063` |
| **Type** | stretch_expert_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00234` |
| **BE Concept** | Avisamvaditva / Reliability |
| **BE Layer** | evidence |
| **VVV Node** | `N_QM_VVV_00013` |
| **VVV Concept** | Extrinsic Registration Certification Phase |
| **Direction** | N_BE_00234 → N_QM_VVV_00013 |
| **Relation Type** | sub_concept_direct_anchor |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.40 (RCA score; Phase 7 batch-approved) |
| **Boundary Note** | Maps registration validity, not apparatus response. |
| **Rationale** | Extrinsic certification phase receives a direct K-side non-deceptiveness anchor. |
| **Origin** | Phase 7 KE-SC stretch mapping; score 4.0/5; see `phase7_ke_sc_rca_log.md` |

### BR_EX_BE_00064 — Entry 64

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00064` |
| **Type** | stretch_expert_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00052` |
| **BE Concept** | Prama / Valid cognition |
| **BE Layer** | evidence |
| **VVV Node** | `N_QM_VVV_00016` |
| **VVV Concept** | Certified Registration State |
| **Direction** | N_BE_00052 → N_QM_VVV_00016 |
| **Relation Type** | sub_concept_direct_anchor |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.41 (RCA score; Phase 7 batch-approved) |
| **Boundary Note** | Maps valid outcome analogue, not Buddhist cognition identity. |
| **Rationale** | Certified registration state receives a direct K-side valid-outcome anchor. |
| **Origin** | Phase 7 KE-SC stretch mapping; score 4.1/5; see `phase7_ke_sc_rca_log.md` |

### BR_EX_BE_00065 — Entry 65 (Phase 12 targeted reactivation)

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00065` |
| **Type** | stretch_expert_mapping |
| **Phase 12 Status** | **REACTIVATED-TARGETED-RCA** (active only as a narrowed source analogue for internal representational form) |
| **Phase 12 Reason** | RCA narrowed the claim from broad internal encoding equivalence to representational-form support. `N_BE_00179` plus `ED_BE_00130` supports mediated representative apprehension, while physical detector storage and apparatus encoding remain outside the BE anchor. |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00179` |
| **BE Concept** | Representative perception |
| **BE Layer** | evidence |
| **VVV Node** | `N_QM_VVV_00022` |
| **VVV Concept** | Internal Representation Encoding |
| **Direction** | N_BE_00179 → N_QM_VVV_00022 |
| **Relation Type** | sub_concept_direct_anchor |
| **Claim Class** | source_analogue_for_internal_representational_form |
| **Confidence** | 0.40 (RCA score; Phase 12 narrowed re-score at v1.7 KE-SC threshold) |
| **Boundary Note** | Maps mediated representational form only; does not map physical detector storage, apparatus memory, or engineering-level encoding equivalence. |
| **Rationale** | Internal representation receives a narrow K-side anchor in representative perception only at the level of mediated representational form, not physical storage or detector-trace engineering. |
| **Origin** | Phase 7 KE-SC stretch mapping; reclassified in v1.7; Phase 12 targeted K-gap RCA reactivated with narrowed boundary; see `reviews/k_gap_rca_phase11_v1_7.md` |

### BR_EX_BE_00066 — Entry 66 ⚠️ RECLASSIFIED-v1.7

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00066` |
| **Type** | stretch_expert_mapping_RECLASSIFIED_v1_7 |
| **v1.7 Status** | **RECLASSIFIED-v1.7-KE-SC-THRESHOLD-RAISE** (no longer active in v1.7 graph) |
| **v1.7 Reason** | Score 3.7/5 below v1.7 KE-SC threshold 4.0/5; boundary guard "temporal boundary ≠ delayed-choice erasure" too thin (Momentariness is generic Buddhist concept; delayed-choice erasure is QM-specific experiment) |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00029` |
| **BE Concept** | Momentariness |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00024` |
| **VVV Concept** | Registration-Locking Boundary in Delayed-Choice Erasure |
| **Direction** | N_BE_00029 → N_QM_VVV_00024 |
| **Relation Type** | sub_concept_direct_anchor |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.37 (RCA score; Phase 7 batch-approved at 3.5/5 threshold; v1.7 reclassified) |
| **Boundary Note** | Maps temporal boundary only, not delayed-choice erasure. |
| **Supersession Note** | Preserved as `RECLASSIFIED-v1.7`; not deleted, overwritten, or reactivated. E18 Path C bridge package (`BR_EX_BE_00070`–`BR_EX_BE_00072`) supersedes this old bridge for full-node recoverability of `N_QM_VVV_00024`; this row remains historical temporal-boundary support only. |
| **Rationale** | Delayed-choice locking boundary receives a direct moment-boundary anchor. |
| **Origin** | Phase 7 KE-SC stretch mapping; score 3.7/5; see `phase7_ke_sc_rca_log.md` and v1.7 annotations |

### BR_EX_BE_00067 — Entry 67

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00067` |
| **Type** | stretch_expert_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00011` |
| **BE Concept** | Svasaṃvedana / Self-awareness |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00035` |
| **VVV Concept** | Primary Registration Closure / Regress-Terminating |
| **Direction** | N_BE_00011 → N_QM_VVV_00035 |
| **Relation Type** | sub_concept_direct_anchor |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.40 (RCA score; Phase 7 batch-approved) |
| **Boundary Note** | Maps reflexive closure, not physical consciousness. |
| **Rationale** | Regress-terminating closure receives a direct reflexive-registration anchor. |
| **Origin** | Phase 7 KE-SC stretch mapping; score 4.0/5; see `phase7_ke_sc_rca_log.md` |

### BR_EX_BE_00068 — Entry 68

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00068` |
| **Type** | stretch_expert_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00086` |
| **BE Concept** | Momentariness |
| **BE Layer** | evidence |
| **VVV Node** | `N_QM_VVV_00040` |
| **VVV Concept** | Momentary Registering Moments {o1,o2,...,on} |
| **Direction** | N_BE_00086 → N_QM_VVV_00040 |
| **Relation Type** | sub_concept_direct_anchor |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.40 (RCA score; Phase 7 batch-approved) |
| **Boundary Note** | Maps moment enumeration, not quantum time evolution. |
| **Rationale** | Momentary registering moments receive a direct fluxional momentariness anchor. |
| **Origin** | Phase 7 KE-SC stretch mapping; score 4.0/5; see `phase7_ke_sc_rca_log.md` |

### BR_EX_BE_00069 — Entry 69

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00069` |
| **Type** | stretch_expert_mapping |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00087` |
| **BE Concept** | Ksanabhangavada |
| **BE Layer** | evidence |
| **VVV Node** | `N_QM_VVV_00053` |
| **VVV Concept** | Ksana Registration Event / Registration Seal |
| **Direction** | N_BE_00087 → N_QM_VVV_00053 |
| **Relation Type** | sub_concept_direct_anchor |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.41 (RCA score; Phase 7 batch-approved) |
| **Boundary Note** | Maps ksana registration boundary, not physical collapse. |
| **Rationale** | Ksana event/seal receives a direct Ksanabhangavada anchor. |
| **Origin** | Phase 7 KE-SC stretch mapping; score 4.1/5; see `phase7_ke_sc_rca_log.md` |

### BR_EX_BE_00070 — Entry 70 (E18 Path C EX vNext sync)

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00070` |
| **Type** | stretch_expert_mapping_E18_Path_C |
| **EX vNext Status** | **RECOVERED-vNext-PATH-C** (active valid-sign bridge package for `N_QM_VVV_00024`) |
| **EX vNext Reason** | RCA `rca_e18_ex_vnext_bridge_audit.md` selected Path C at 4.2/5. `N_BE_00003` supports the sign/inference component of E18 valid registration locking; `BR_EX_BE_00066` remains reclassified and is not reactivated. |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00003` |
| **BE Concept** | Inference / Anumana |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00024` |
| **VVV Concept** | Registration-Locking Boundary in Delayed-Choice Erasure |
| **Direction** | N_BE_00003 -> N_QM_VVV_00024 |
| **Relation Type** | sub_concept_direct_anchor |
| **Claim Class** | interpretive_mapping_valid_sign_support |
| **Confidence** | 0.42 (RCA score; E18 Path C EX vNext bridge audit) |
| **Boundary Note** | Analogical-only support for the sign/inference component of registration locking; no BE-QM identity, no physical retrocausation, no Standard QM modification, and no core import. |
| **Rationale** | E18 locking uses final context plus sorting relation as a sign-like basis for valid branch registration; Anumana anchors the inferential valid-sign aspect only. |
| **Origin** | E18 G6 follow-up; `rca_e18_ex_vnext_bridge_audit.md`; Path C authorized by user on 2026-05-22 |

### BR_EX_BE_00071 — Entry 71 (E18 Path C EX vNext sync)

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00071` |
| **Type** | stretch_expert_mapping_E18_Path_C |
| **EX vNext Status** | **RECOVERED-vNext-PATH-C** (active valid-sign bridge package for `N_QM_VVV_00024`) |
| **EX vNext Reason** | RCA `rca_e18_ex_vnext_bridge_audit.md` selected Path C at 4.2/5. `N_BE_00019` supports the stable relation/pervasion component of E18 valid registration locking. |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00019` |
| **BE Concept** | Pervasion / Vyapti |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00024` |
| **VVV Concept** | Registration-Locking Boundary in Delayed-Choice Erasure |
| **Direction** | N_BE_00019 -> N_QM_VVV_00024 |
| **Relation Type** | sub_concept_direct_anchor |
| **Claim Class** | interpretive_mapping_valid_relation_support |
| **Confidence** | 0.42 (RCA score; E18 Path C EX vNext bridge audit) |
| **Boundary Note** | Analogical-only support for the sorting-relation constraint in E18; no BE-QM identity, no physical retrocausation, no Standard QM modification, and no core import. |
| **Rationale** | E18 requires a sorting relation `S` that links final context to a valid branch window; Vyapti anchors the relation-constraint aspect only. |
| **Origin** | E18 G6 follow-up; `rca_e18_ex_vnext_bridge_audit.md`; Path C authorized by user on 2026-05-22 |

### BR_EX_BE_00072 — Entry 72 (E18 Path C EX vNext sync)

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00072` |
| **Type** | stretch_expert_mapping_E18_Path_C |
| **EX vNext Status** | **RECOVERED-vNext-PATH-C** (active valid-sign bridge package for `N_QM_VVV_00024`) |
| **EX vNext Reason** | RCA `rca_e18_ex_vnext_bridge_audit.md` selected Path C at 4.2/5. `N_BE_00021` supports the essential-connection component of E18 valid registration locking. |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00021` |
| **BE Concept** | Essential relation / Svabhavapratibandha |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00024` |
| **VVV Concept** | Registration-Locking Boundary in Delayed-Choice Erasure |
| **Direction** | N_BE_00021 -> N_QM_VVV_00024 |
| **Relation Type** | sub_concept_direct_anchor |
| **Claim Class** | interpretive_mapping_valid_connection_support |
| **Confidence** | 0.42 (RCA score; E18 Path C EX vNext bridge audit) |
| **Boundary Note** | Analogical-only support for the stable valid-connection component of E18; no BE-QM identity, no physical retrocausation, no Standard QM modification, and no core import. |
| **Rationale** | E18 valid registration depends on a stable connection between final context, sorting rule, and valid window; Svabhavapratibandha anchors the connection aspect only. |
| **Origin** | E18 G6 follow-up; `rca_e18_ex_vnext_bridge_audit.md`; Path C authorized by user on 2026-05-22 |

---

## promote_new_bridge Batch (2026-05-23) — K9_E K-side + DRAFT→ACTIVE

### BR_EX_BE_00073 — Entry 73 (K9_E f_perp K-side)

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00073` |
| **Type** | new_bridge_promotion |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00018` |
| **BE Concept** | Triple-condition syllogism / Trairūpya |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00062` |
| **VVV Concept** | f_perp(K_ctx) — Contextual Suppression Function |
| **Direction** | N_BE_00018 → N_QM_VVV_00062 |
| **Relation Type** | structural_analogy |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.90 (RCA 4.5/5) |
| **Boundary Note** | Trairūpya supplies K-side structural analogy for three-condition validity filtering; f_perp is mathematical implementation on probability side. No BE-QM identity. Not a Hilbert-space derivation. Mediated through parent N_QM_VVV_00042. |
| **Rationale** | f_perp inherits validity-gating from Trairūpya through N_QM_VVV_00042. Three-condition structure parallels f_perp's suppression when K_ctx high. |
| **Origin** | promote_new_bridge RCA gate 2026-05-23; `reviews/rca_promote_new_bridge_batch_2026_05_23.md` |

### BR_EX_BE_00074 — Entry 74 (K9_E K_ctx K-side)

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00074` |
| **Type** | new_bridge_promotion |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00015` |
| **BE Concept** | Exclusion / Apoha |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00063` |
| **VVV Concept** | K_ctx(k_i, Exp) — Contextual Incommensurability Aggregate |
| **Direction** | N_BE_00015 → N_QM_VVV_00063 |
| **Relation Type** | structural_analogy |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.90 (RCA 4.5/5) |
| **Boundary Note** | Apoha provides K-side structural analogy for binary incommensurability (K5 ⊥_K). K_ctx is the aggregate. No BE-QM identity. K5 is a VVV axiom, not a BE derivation. |
| **Rationale** | K_ctx aggregates binary exclusion relations whose primitive (K5 ⊥_K) has structural affinity with Buddhist exclusion logic (Apoha). Analogy only, not conceptual identity. |
| **Origin** | promote_new_bridge RCA gate 2026-05-23; `reviews/rca_promote_new_bridge_batch_2026_05_23.md` |

### BR_EX_BE_00075 — Entry 75 (00056 DRAFT→ACTIVE)

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00075` |
| **Type** | new_bridge_promotion |
| **Promotion** | DRAFT→ACTIVE (supersedes BR_EX_BE_DRAFT_00073A) |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00003` primary; `N_BE_00019`; `N_BE_00021` |
| **BE Concept** | Inference / Anumana + Pervasion / Vyapti + Essential relation / Svabhavapratibandha |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00056` |
| **VVV Concept** | Delayed-Choice Registration Boundary |
| **Direction** | N_BE_00003 / N_BE_00019 / N_BE_00021 → N_QM_VVV_00056 |
| **Relation Type** | sub_concept_direct_anchor |
| **Claim Class** | interpretive_mapping_valid_sign_support |
| **Confidence** | 0.88 (C3 RCA 4.4/5; re-verified 5.0/5) |
| **Boundary Note** | Analogical-only K-side support for generalized E18 valid-window locking; no BE-QM identity, no physical retrocausation. |
| **Rationale** | E18 Lock(C_f, S, {W_i}) → W_valid. BE package supports sign, relation, and stable-connection aspects only. Promoted from BR_EX_BE_DRAFT_00073A. |
| **Origin** | C3 K-side RCA → C4 draft → promote_new_bridge RCA gate 2026-05-23; `reviews/rca_promote_new_bridge_batch_2026_05_23.md` |

### BR_EX_BE_00076 — Entry 76 (00057 DRAFT→ACTIVE)

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00076` |
| **Type** | new_bridge_promotion |
| **Promotion** | DRAFT→ACTIVE (supersedes BR_EX_BE_DRAFT_00073B) |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00019` primary; `N_BE_00021`; `N_BE_00003` |
| **BE Concept** | Pervasion / Vyapti + Essential relation / Svabhavapratibandha + Inference / Anumana |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00057` |
| **VVV Concept** | Sorting-Conditioned Registration Subset |
| **Direction** | N_BE_00019 / N_BE_00021 / N_BE_00003 → N_QM_VVV_00057 |
| **Relation Type** | sub_concept_direct_anchor |
| **Claim Class** | interpretive_mapping_draft_relation_support |
| **Confidence** | 0.84 (C3 RCA 4.2/5; re-verified 5.0/5) |
| **Boundary Note** | Analogical-only K-side support for sorting/coincidence constraint; sorting is not Buddhist inference identity, not a new Standard QM law. |
| **Rationale** | Sorting relation S partitions raw records into valid window. Vyapti + Svabhavapratibandha support relation-constraint; Anumana supports sign-like subset selection. Promoted from BR_EX_BE_DRAFT_00073B. |
| **Origin** | C3 K-side RCA → C4 draft → promote_new_bridge RCA gate 2026-05-23; `reviews/rca_promote_new_bridge_batch_2026_05_23.md` |

### BR_EX_BE_00077 — Entry 77 (00059 DRAFT→ACTIVE)

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00077` |
| **Type** | new_bridge_promotion |
| **Promotion** | DRAFT→ACTIVE (supersedes BR_EX_BE_DRAFT_00073C) |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00006`; `N_BE_00234`; `N_BE_00052` |
| **BE Concept** | Erroneous cognition / Bhranti + Avisamvaditva + Prama |
| **BE Layer** | core + evidence |
| **VVV Node** | `N_QM_VVV_00059` |
| **VVV Concept** | Decoherence-Induced Registration Update |
| **Direction** | N_BE_00006 / N_BE_00234 / N_BE_00052 → N_QM_VVV_00059 |
| **Relation Type** | sub_concept_direct_anchor |
| **Claim Class** | interpretive_mapping_draft_registration_state_update_support |
| **Confidence** | 0.84 (C5 RCA 4.2/5; re-verified 5.0/5) |
| **Boundary Note** | Analogical-only K-side support for registration-state update and validity/error reclassification; not BE analogue of decoherence physics. Bhranti/error, Avisamvaditva/reliability, Prama/valid-knowledge classification only. |
| **Rationale** | K-side routing: decoherence can route defeated response to error or instantiate new K-state. BE concepts supply classification framework. Promoted from BR_EX_BE_DRAFT_00073C. |
| **Origin** | C5 RCA → C4 draft → promote_new_bridge RCA gate 2026-05-23; `reviews/rca_promote_new_bridge_batch_2026_05_23.md` |

---

## C4 Current-Core Draft K-Side Rows (2026-05-22; superseded by active 00075–00077)

These rows formalize C3 K-side RCA results for current-Core nodes outside the frozen 52-node EX baseline. They are **draft-only**: not active `BR_EX_BE`, not graphable, not counted in `47/52`, and not authorized for `data/*.json` mutation.

**C7 automation safety note:** graph-sync automation must ignore every `BR_EX_BE_DRAFT_*` row. `phase4_graph_sync.py` currently parses only numbered headings matching `BR_EX_[A-Z]+_\d+`, so `BR_EX_BE_DRAFT_00073A`-`BR_EX_BE_DRAFT_00073C` are intentionally outside the graphable parser shape. Do not rename these rows into `BR_EX_BE_00073*` without explicit promotion and graph-sync approval.

### BR_EX_BE_DRAFT_00073A — Draft Row A (C4 current-Core K-side)

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_DRAFT_00073A` |
| **Type** | draft_current_core_C4 |
| **C4 Status** | `DRAFT-C4-K-SIDE` (not active; not graphable) |
| **C6 Audit Status** | `AUDIT-PASS-DRAFT` |
| **C8 Promotion Readiness** | `PROMOTION-CANDIDATE-LATER` (requires explicit renumber policy, graph-sync dry review, and active metric policy) |
| **Source Edge Type** | `BR_EX_BE_DRAFT_ONLY` |
| **BE Node** | `N_BE_00003` primary support; `N_BE_00019` relation support; `N_BE_00021` connection support |
| **BE Concept** | Inference / Anumana + Pervasion / Vyapti + Essential relation / Svabhavapratibandha |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00056` |
| **VVV Concept** | Delayed-Choice Registration Boundary / Context-Conditioned Registration Window Locking |
| **Direction** | N_BE_00003 / N_BE_00019 / N_BE_00021 -> N_QM_VVV_00056 |
| **Relation Type** | draft_valid_sign_window_lock_support |
| **Claim Class** | interpretive_mapping_draft_valid_sign_support |
| **Confidence** | draft-only; C3 RCA score 4.4/5 |
| **Boundary Note** | Analogical-only K-side support for generalized E18 valid-window locking; no BE-QM identity, no physical retrocausation, no Standard QM modification, no active EX coverage, and no core import. |
| **Rationale** | C3 RCA isolates `N_QM_VVV_00056` as generalized E18 `Lock(C_f, S, {W_i}) -> W_valid`. The BE package supports the sign, relation, and stable-connection aspects only; it does not turn delayed-choice registration into a Buddhist-physics identity claim. |
| **Origin** | C3 K-side RCA recorded in `k_gap_exception_list.md` §4.1; C4 draft-only registry formalization authorized by user on 2026-05-22 |

### BR_EX_BE_DRAFT_00073B — Draft Row B (C4 current-Core K-side)

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_DRAFT_00073B` |
| **Type** | draft_current_core_C4 |
| **C4 Status** | `DRAFT-C4-K-SIDE` (not active; not graphable) |
| **C6 Audit Status** | `AUDIT-PASS-DRAFT` |
| **C8 Promotion Readiness** | `PROMOTION-CANDIDATE-WITH-GUARD-LATER` (requires sorting/relation wording guard and graph-sync dry review) |
| **Source Edge Type** | `BR_EX_BE_DRAFT_ONLY` |
| **BE Node** | `N_BE_00019` primary relation support; `N_BE_00021` connection support; `N_BE_00003` inference support |
| **BE Concept** | Pervasion / Vyapti + Essential relation / Svabhavapratibandha + Inference / Anumana |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00057` |
| **VVV Concept** | Sorting-Conditioned Registration Subset / Coincidence-Sorted Valid Window |
| **Direction** | N_BE_00019 / N_BE_00021 / N_BE_00003 -> N_QM_VVV_00057 |
| **Relation Type** | draft_sorting_relation_constraint_support |
| **Claim Class** | interpretive_mapping_draft_relation_support |
| **Confidence** | draft-only; C3 RCA score 4.2/5 |
| **Boundary Note** | Analogical-only K-side support for the sorting/coincidence relation constraint; sorting is not identical to Buddhist inference, not an active bridge, not a new Standard QM law, and not a graph edge. |
| **Rationale** | C3 RCA isolates `N_QM_VVV_00057` as the explicit sorting relation `S` that partitions raw records into the valid prior registration window. Vyapti and Svabhavapratibandha support the relation-constraint structure; Anumana remains secondary support for sign-like valid subset selection. |
| **Origin** | C3 K-side RCA recorded in `k_gap_exception_list.md` §4.1; C4 draft-only registry formalization authorized by user on 2026-05-22 |

### BR_EX_BE_DRAFT_00073C — Draft Row C (C5 current-Core K-side)

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_DRAFT_00073C` |
| **Type** | draft_current_core_C5 |
| **C5 Status** | `DRAFT-C5-K-SIDE` (not active; not graphable) |
| **C6 Audit Status** | `AUDIT-PASS-DRAFT-WITH-BOUNDARY-GUARD` |
| **C8 Promotion Readiness** | `HOLD-FOR-GUARDED-PROMOTION-REVIEW` (requires rho/K boundary wording lock before any promotion review) |
| **Source Edge Type** | `BR_EX_BE_DRAFT_ONLY` |
| **BE Node** | `N_BE_00006` error-status support; `N_BE_00234` reliability criterion; `N_BE_00052` valid-knowledge endpoint |
| **BE Concept** | Erroneous cognition / Bhranti + Avisamvaditva + Prama |
| **BE Layer** | core + RCA |
| **VVV Node** | `N_QM_VVV_00059` |
| **VVV Concept** | Decoherence-Induced Registration Update |
| **Direction** | N_BE_00006 / N_BE_00234 / N_BE_00052 -> N_QM_VVV_00059 |
| **Relation Type** | draft_validity_error_status_update_support |
| **Claim Class** | interpretive_mapping_draft_registration_state_update_support |
| **Confidence** | draft-only; C5 RCA score 4.2/5 |
| **Boundary Note** | Analogical-only K-side support for registration-state update and validity/error-status reclassification; not a BE analogue of decoherence physics, not active coverage, not a Standard QM modification, and not a graph edge. |
| **Rationale** | C5 RCA isolates the root of `N_QM_VVV_00059` as a K-side routing problem: decoherence support can participate in a registration-state update path that either instantiates a new K-state or routes a defeated prior response toward registration-error status. Bhranti supports error-status reclassification, Avisamvaditva supports the reliability/non-deceptiveness criterion, and Prama supports the valid-knowledge endpoint; none of these claims identifies BE with physical decoherence. |
| **Origin** | C5 dedicated RCA for `N_QM_VVV_00059`; draft-only registry formalization authorized by user on 2026-05-22 |

> C5 note: `BR_EX_BE_DRAFT_00073C` resolves the C3 caveat only at draft level. It does not promote `N_QM_VVV_00059` to active K-side coverage and does not authorize graph sync, script execution, or frozen denominator changes.

---

## Full-Run Batch (2026-05-23) — 3 K-side entries

### BR_EX_BE_00078 — Entry 78

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00078` |
| **Type** | new_bridge_promotion |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00015` |
| **BE Concept** | Anupalabdhi (Valid Non-Perception / Valid Absence Registration) |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00002` |
| **VVV Concept** | Interaction-Free State Inference (IFSI) |
| **Direction** | N_BE_00015 → N_QM_VVV_00002 |
| **Relation Type** | structural_analogy |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 1.00 (RCA score 5.0/5) |
| **Boundary Note** | IFSI operationalizes Anupalabdhi logic in QM measurement context: no-click → state inference under complete-alternative conditions. Inherits through parent N_QM_VVV_00001 (Contrapositive Evidence). Not a BE-QM identity claim. |
| **Rationale** | IFSI is the procedural inference mechanism of N_QM_VVV_00001's Contrapositive Evidence category. BE anchor is Anupalabdhi — the valid-absence registration standard that IFSI implements procedurally in QM. Inheritance chain: Anupalabdhi → Contrapositive Evidence (00001) → IFSI (00002). |
| **Origin** | promote_new_bridge RCA gate (full-run batch); 2026-05-23 |

### BR_EX_BE_00079 — Entry 79

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00079` |
| **Type** | new_bridge_promotion |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00015` |
| **BE Concept** | Anupalabdhi (Valid Non-Perception / Valid Absence Registration) |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00005` |
| **VVV Concept** | Non-Informative Null Event / Broken-Detector Null |
| **Direction** | N_BE_00015 → N_QM_VVV_00005 |
| **Relation Type** | structural_analogy (contrastive) |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.80 (RCA score 4.0/5) |
| **Boundary Note** | INDIRECT-1-LEVEL (via contrast with N_QM_VVV_00004 Informative Silence). This is the NEGATIVE contrast to Anupalabdhi — what valid absence is NOT. Anupalabdhi provides the positive standard for valid non-perception; 00005 isolates the failure mode where null events are caused by detector failure or invalid setup. Not a direct BE source-analogue. |
| **Rationale** | Without BE contrast bridge, 00005 floats as pure QM diagnostic without K-side grounding. BE Anupalabdhi implicitly requires distinguishing valid absence from detector failure — 00005 makes this distinction explicit at the registration layer. Spot-check upgrade (CONFIRMATORY→EXPLORATORY) detected INDIRECT-1-LEVEL that would have been missed under CONFIRMATORY-only review. |
| **Origin** | promote_new_bridge RCA gate (full-run batch, spot-check upgraded); 2026-05-23 |

### BR_EX_BE_00080 — Entry 80

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00080` |
| **Type** | new_bridge_promotion |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_00013` |
| **BE Concept** | Dual-Phase Registration (DPEC Root) |
| **BE Layer** | core |
| **VVV Node** | `N_QM_VVV_00015` |
| **VVV Concept** | Conditionally Updated State ρ̃ |
| **Direction** | N_BE_00013 → N_QM_VVV_00015 |
| **Relation Type** | structural_analogy |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 1.00 (RCA score 5.0/5) |
| **Boundary Note** | ρ̃ inherits DPEC K-side grounding through N_QM_VVV_00011 chain. It is a registration-status notation (intermediate state between physical update and certified registration), not a new density-matrix law. BE grounding via parent chain: BE_00013 → VVV_00011 (DPEC) → VVV_00012 (Intrinsic Phase) → VVV_00015 (ρ̃). |
| **Rationale** | ρ̃ is the state notation for DPEC's provisional validity — it needs BE grounding but inherits it through the DPEC chain. Parent 00011 already bridged (BR_EX_BE_00041). Bridge provides direct K-side trace for the intermediate registration state. |
| **Origin** | promote_new_bridge RCA gate (full-run batch); 2026-05-23 |