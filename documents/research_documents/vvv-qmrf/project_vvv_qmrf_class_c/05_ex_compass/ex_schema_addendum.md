Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# EX Schema Addendum — VVV-QMRF-EX Local Namespace Declaration

**Version:** 1.1
**Date:** 2026-05-20
**Status:** Active
**RCA Fix:** F1 (v1.0→v1.1) — declares EX-local namespace to prevent ID collision with VVV-QMRF core; Phase 7 adds stretch relation vocabulary

---

## 1. Purpose

This addendum declares the namespace and ID conventions used exclusively within VVV-QMRF-EX.
It is an extension of the VVV-QMRF schema (`vvv-qmrf/schema_guide.md`) and does NOT modify that file.

---

## 2. EX-Local ID Namespaces

| Namespace Prefix | Range | Owner | Description |
|-----------------|-------|-------|-------------|
| `BR_EX_BE_XXXXX` | 00001–99999 | VVV-QMRF-EX | K-side bridge: BE node ↔ VVV-QMRF node |
| `BR_EX_QM_XXXXX` | 00001–99999 | VVV-QMRF-EX | ρ-side bridge: VVV-QMRF node ↔ QM node |

**Isolation constraint (Rule I-3):** VVV-QMRF-EX MUST NOT create IDs of the following types:
`N_QM_VVV_XXXXX`, `ED_QM_VVV_XXXXX`, `BR_XXXXX`, `N_BE_XXXXX`, `N_QM_XXXXX`

---

## 3. Edge Type Classification

### K-side (BE ↔ VVV) edge types
| Edge Type | Origin | Description |
|-----------|--------|-------------|
| `VVV_TO_BE` | Phase 1 | VVV concept draws K-side semantics from BE source-analogue |
| `DRAFT_BRIDGE_BE_VVV` | Phase 1 | BE concept provides K-side support (263-node audit cycle, draft) |
| `BR_EX_BE` | Phase 4 | New BE↔VVV bridge from Phase 3 similarity (Tier2 candidate) |
| `BR_EX_BE_NEW` | Phase 6 | Expert-manual BE↔VVV bridge resolving a KE-PM K-gap node |
| `BR_EX_BE_STRETCH` | Phase 7 / v1.7 | Batch-approved BE↔VVV stretch bridge. **KE-OF threshold (unchanged):** 4.5/5. **KE-SC threshold:** v1.6 = 3.5/5 (pragmatic floor); **v1.7 = 4.0/5 + 1 carve-out at 3.8** (requires structurally sharp boundary guard + raw cosine ≥4.3). 3 v1.6 KE-SC entries reclassified back to exception in v1.7 (see plan §15 and `archives/phase7_logs/phase7_ke_sc_rca_log.md` v1.7 annotations). phase2 `K_SIDE_TYPES` must include this type to count it in K-side anchoring (F-RCA-14). |

### K-side relation vocabulary
| Relation Type | Origin | Description |
|---------------|--------|-------------|
| `operator_decomposition` | Phase 7 KE-OF | Maps a VVV operator-formalism node to a BE concept by decomposing the operator's registration-side semantic function; NOT a claim that BE contains an equivalent mathematical operator |
| `sub_concept_direct_anchor` | Phase 7 KE-SC | Maps a VVV sub-concept to a direct BE anchor after parent-inherited K-side coverage is replaced by cautious direct anchoring; NOT a BE-QM identity claim |

### ρ-side (VVV ↔ QM) edge types
| Edge Type | Origin | Description |
|-----------|--------|-------------|
| `VVV_TO_QM` | Phase 1 | QM concept provides physical substrate for VVV registration concept |
| `BR_QM_VVV` | Phase 1 | VVV extends registration semantics of QM concept (v0.1 bridge) |
| `BR_EX_QM` | Phase 4 | New VVV↔QM bridge from Phase 3 similarity (Tier2 candidate) |

---

## 4. Claim Classes

| Claim Class | Meaning |
|-------------|---------|
| `source_analogue` | VVV draws K-side semantics from BE; NOT conceptual identity |
| `evidence_support` | BE concept supports VVV via audit cycle evidence; draft status |
| `interpretive_mapping` | Cross-domain interpretive link; NOT physical law or formal proof |

---

## 5. Direction Convention (F2 Non-Reversal Rule)

- Derived-copy entries in `br_ex_be_registry.md` and `br_ex_qm_registry.md` MUST NOT silently reverse direction.
- If direction is reversed from the source edge, the rationale MUST record it in the `direction` and `rationale` fields.
- Source: Isolation Rule I-2.

---

## 6. Promotion Gate

Entries with `type = new_similarity_candidate` are NOT promoted to VVV-QMRF core unless:
1. Domain expert review confirms conceptual equivalence or interpretive validity.
2. Confidence score assigned (0.0–1.0).
3. Entry updated to `type = promoted_candidate` and mirrored to appropriate VVV-QMRF core file.

Similarity-only entries (Phase 3 Tier2) remain EX-local until gate conditions are met.

---

*This addendum is part of VVV-QMRF-EX. See `vvv-qmrf-ex-plan.md` for full scope.*
