Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# BIAN-14 Structural Review — Fold/Keep Decision

**Document type:** RCA structural review
**Date:** 2026-05-21
**Scope:** Decide whether BR_DRAFT_C_001 (Anvaya) and BR_DRAFT_C_002 (Vyatireka) should fold as sub-evidence under BR_DRAFT_D_001 (Tri-rūpa-hetu), or remain standalone bridge IDs
**Decision authority:** VVV-QMRF-EX RCA gate (§14.10 open item #1)
**Boundary:** EX-only; no core file modification

---

## 1. Evidence Inventory

### 1.1 The Three Draft Bridges Under Review

| Bridge | Batch | BE Node | BE Concept | Definition | Edge Identity |
|--------|-------|---------|------------|------------|---------------|
| BR_DRAFT_C_001 | C | N_BE_00096 | Anvaya | "Association, agreement in presence, or positive concomitance in inductive reasoning." (system_be_full.md row 96) | ED_BE_00111: Anvaya (N_BE_00096) "is identical with" Positive concomitance (N_BE_00214); the 2nd criterion of trairūpya |
| BR_DRAFT_C_002 | C | N_BE_00097 | Vyatireka | "Dissociation, agreement in absence, or negative concomitance in inductive reasoning." (system_be_full.md row 97) | ED_BE_00112: Vyatireka (N_BE_00097) "is identical with" Negative concomitance (N_BE_00215); the 3rd criterion of trairūpya |
| BR_DRAFT_D_001 | D | N_BE_00158 | Tri-rūpa-hetu | "Three characteristics, criteria, or conditions of a valid logical reason." (system_be_full.md row 158) | No direct edge to N_BE_00018; structurally synonymous with Trairūpya (N_BE_00018) |

### 1.2 The Core Node (Already Mapped)

| Node | BE Concept | Definition | BIAN SOT Status | EX Registry |
|------|------------|------------|-----------------|-------------|
| N_BE_00018 | Trairūpya (Triple-condition syllogism) | "The three conditions for a valid reason: (i) pakṣadharmatva, (ii) anvaya / sapakṣe sattvam, (iii) vyatireka / vipakṣe 'sattvam." | ✅ Resolved — Cat 09 + E10 | BR_EX_BE_00032 (source_analogue, confidence 0.90) |

### 1.3 EX Registry Current State (BIAN-14 cluster)

| BR_EX_ID | BE Node | BE Concept | VVV Node | Type | Confidence |
|----------|---------|------------|----------|------|------------|
| BR_EX_BE_00003 | N_BE_00096 | Anvaya | N_QM_VVV_00042 | reference_copy (draft_bridge) | 0.70 |
| BR_EX_BE_00004 | N_BE_00097 | Vyatireka | N_QM_VVV_00042 | reference_copy (draft_bridge) | 0.70 |
| BR_EX_BE_00008 | N_BE_00158 | Tri-rūpa-hetu | N_QM_VVV_00042 | reference_copy (draft_bridge) | 0.70 |
| BR_EX_BE_00032 | N_BE_00018 | Triple-condition syllogism | N_QM_VVV_00042 | reference_copy (source_analogue) | 0.90 |

All four already map to the same VVV target: **N_QM_VVV_00042** (Tripartite Registration Validity Matrix).

---

## 2. RCA Round 1 — Structural Independence Test

**Question:** Does Anvaya (C_001) carry independent bridge-level structural significance apart from Tri-rūpa-hetu (D_001)?

### 5-Why Analysis

1. **Why does C_001 exist as a separate bridge?**
   → Because N_BE_00096 is a distinct node (row 96) in the 263-node BE system.

2. **Why is it distinct from D_001?**
   → Because Anvaya names one specific logical operation (positive concomitance = co-presence of probans and probandum), while Tri-rūpa-hetu names the structural whole containing all three conditions.

3. **Why does that distinction matter for VVV-QMRF bridge purposes?**
   → Because in Category 09, Condition 2 (Sapakṣasattva / positive calibration) is the QM translation of Anvaya. If Anvaya folds, Condition 2's source traceability becomes indirect (via D_001 → Tri-rūpa-hetu → implicitly contains Anvaya).

4. **Why would indirect traceability be a problem?**
   → Because the RCA framework requires each claim anchor to have a traceable source path. If C_001 folds, the trace for Condition 2 goes: `Cat 09 §3 Condition 2 → D_001 → N_BE_00158 (Tri-rūpa-hetu) → implicitly includes Anvaya`. This is still valid but one hop longer.

5. **Why does an extra hop matter?**
   → **It doesn't fundamentally.** The additional hop is a convenience loss, not an integrity loss. The BE SOT edge ED_BE_00111 already formally records that "Anvaya is identical with Sapakṣe sattvam, the 2nd criterion of trairūpya." This edge exists regardless of bridge-level status.

**Round 1 verdict:** Anvaya's structural significance is **fully captured** by Trairūpya (N_BE_00018) + edge ED_BE_00111. The bridge adds traceability convenience but not independent structural content.

---

## 3. RCA Round 2 — Paired-Evidence Test

**Question:** Do Anvaya (C_001) and Vyatireka (C_002) carry paired significance that would be lost by folding?

### 5-Why Analysis

1. **Why are C_001 and C_002 paired?**
   → Because Anvaya (positive concomitance) and Vyatireka (negative concomitance) are complementary halves of the validity test: "present where the target is present" AND "absent where the target is absent."

2. **Why does pairing matter for VVV-QMRF?**
   → Category 09 Condition 2 (positive calibration) and Condition 3 (false-positive exclusion) directly mirror this pair. The pairing is structurally significant in both BE and QM contexts.

3. **If they fold, is the pairing preserved?**
   → **Yes.** D_001 (Tri-rūpa-hetu) explicitly contains all three conditions. The pairing is encoded in:
   - N_BE_00018 definition: "(ii) anvaya / sapakṣe sattvam, (iii) vyatireka / vipakṣe 'sattvam"
   - Edges ED_BE_00109 + ED_BE_00110 (conditions 2 and 3 of Trairūpya)
   - Edges ED_BE_00111 + ED_BE_00112 (Anvaya/Vyatireka identity with conditions)

4. **What would be lost by folding?**
   → Only the **direct bridge-level pointer** from C_001/C_002 to N_QM_VVV_00042. The semantic content is fully preserved through D_001 + edge network.

5. **Is there any case where C_001 or C_002 would serve a different BIAN target than D_001?**
   → **C_002 yes:** BR_DRAFT_C_002 (Vyatireka) also serves **BIAN-15** (Purely Contrastive Quantum Evidence Structure). This is already recorded in the uniqueness audit §3.3 and in BR_EX_BE_00005 (N_BE_00097 → N_QM_VVV_00001).

**Round 2 verdict:** The pairing is preserved through D_001's definition and the edge network. However, **C_002 has a dual-BIAN function** (BIAN-14 + BIAN-15) that must be preserved.

---

## 4. RCA Round 3 — EX Registry Impact Test

**Question:** What happens to the EX registry entries if we fold?

### Current State

```
BR_EX_BE_00003  N_BE_00096 (Anvaya)      → N_QM_VVV_00042  [draft_bridge, 0.70]
BR_EX_BE_00004  N_BE_00097 (Vyatireka)   → N_QM_VVV_00042  [draft_bridge, 0.70]
BR_EX_BE_00005  N_BE_00097 (Vyatireka)   → N_QM_VVV_00001  [draft_bridge, 0.70]  ← BIAN-15 link
BR_EX_BE_00008  N_BE_00158 (Tri-rūpa)    → N_QM_VVV_00042  [draft_bridge, 0.70]
BR_EX_BE_00032  N_BE_00018 (Trairūpya)   → N_QM_VVV_00042  [source_analogue, 0.90]
```

### If Fold (C_001 + C_002 become sub-evidence of D_001):

| Action | Entry | Change |
|--------|-------|--------|
| Reclassify | BR_EX_BE_00003 | Type → `sub_evidence_of_BR_EX_BE_00008`; Status → `FOLDED-structural-review` |
| Reclassify | BR_EX_BE_00004 (BIAN-14 link) | Type → `sub_evidence_of_BR_EX_BE_00008`; Status → `FOLDED-structural-review` |
| **KEEP** | BR_EX_BE_00005 (BIAN-15 link) | **No change** — Vyatireka → N_QM_VVV_00001 serves BIAN-15 independently |
| No change | BR_EX_BE_00008 | Becomes the **primary bridge** for BIAN-14 sub-condition support |
| No change | BR_EX_BE_00032 | Remains the **source analogue** bridge for BIAN-14 core |

### Impact Assessment

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Active BIAN-14 support bridges | 4 | 2 active + 2 folded | −2 active (metadata only) |
| BIAN-15 support bridges | 2 | 2 | 0 |
| Total EX entries | 69 | 69 | 0 (no deletion) |
| Active EX entries | 66 | 64 active + 2 folded | −2 active |
| Graph edges | No change | No change | 0 |

---

## 5. Scoring — Fold vs Keep (threshold 4.0/5)

| Criterion | Fold | Keep | Weight |
|-----------|:----:|:----:|:------:|
| **C1: Structural independence** — Does C_001/C_002 add unique structural content not captured by D_001? | No — D_001 + edges fully capture | Yes — direct pointer | 1.5 |
| **C2: Traceability** — Is the source trace adequate after fold? | Yes — edge chain is 1 hop longer but complete | Yes — direct | 1.0 |
| **C3: Paired-evidence preservation** — Is the Anvaya-Vyatireka pairing preserved? | Yes — via D_001 definition + edges | Yes — directly | 1.0 |
| **C4: Dual-BIAN safety** — Is BR_EX_BE_00005 (BIAN-15) unaffected? | Yes — BIAN-15 link untouched | Yes | 1.0 |
| **C5: Registry hygiene** — Does the action reduce ambiguity? | Yes — fewer standalone bridges for a single structural concept | No — 3 bridges for 1 BIAN creates mild density | 0.5 |

### Scores

| Option | C1 (×1.5) | C2 (×1.0) | C3 (×1.0) | C4 (×1.0) | C5 (×0.5) | **Total** |
|--------|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|
| **FOLD** | 1.5 | 1.0 | 1.0 | 1.0 | 0.5 | **5.0/5** |
| **KEEP** | 0 | 1.0 | 1.0 | 1.0 | 0 | **3.0/5** |

**FOLD scores 5.0/5 ≥ threshold 4.0/5. KEEP scores 3.0/5 < threshold.**

---

## 6. DECISION

```
╔═══════════════════════════════════════════════════════════════════╗
║                     BIAN-14 STRUCTURAL REVIEW                    ║
║                                                                   ║
║  VERDICT: FOLD                                                    ║
║                                                                   ║
║  BR_DRAFT_C_001 (Anvaya)  → sub-evidence of BR_DRAFT_D_001      ║
║  BR_DRAFT_C_002 (Vyatireka) → sub-evidence of BR_DRAFT_D_001    ║
║     (BIAN-14 link only; BIAN-15 link BR_EX_BE_00005 KEPT)       ║
║                                                                   ║
║  Score: FOLD 5.0/5 vs KEEP 3.0/5 (threshold 4.0/5)              ║
║                                                                   ║
║  Root cause: C_001 and C_002 are constituent conditions of the   ║
║  Trairūpya structure. Their structural content is fully captured  ║
║  by D_001 (Tri-rūpa-hetu) + BE SOT edges ED_BE_00111 and        ║
║  ED_BE_00112. They do not add independent bridge-level content.  ║
║                                                                   ║
║  Safety: BR_EX_BE_00005 (Vyatireka → BIAN-15) is UNAFFECTED.    ║
╚═══════════════════════════════════════════════════════════════════╝
```

---

## 7. Implementation Actions

### 7.1 EX Registry (br_ex_be_registry.md)

| Entry | Action | New Status Field |
|-------|--------|-----------------|
| BR_EX_BE_00003 | Add `Status: FOLDED-structural-review` and `Fold-parent: BR_EX_BE_00008` | FOLDED |
| BR_EX_BE_00004 | Add `Status: FOLDED-structural-review` and `Fold-parent: BR_EX_BE_00008` | FOLDED |
| BR_EX_BE_00005 | No change | active |
| BR_EX_BE_00008 | Add `Sub-evidence: BR_EX_BE_00003 (Anvaya), BR_EX_BE_00004 (Vyatireka)` | active |

### 7.2 Plan (vvv-qmrf-ex-plan.md)

Mark §14.10 open item #1 (BIAN-14 structural review) as:
```
✅ Resolved — FOLD decision (2026-05-21)
   See reviews/bian14_structural_review.md
```

### 7.3 Checkpoint (reviews/rca_checkpoint.md)

Update BIAN-14 structural review line from `⏳ Pending` to `✅ Resolved — FOLD`.

### 7.4 Files NOT Modified

| File | Reason |
|------|--------|
| `BIAN_index_SOT.md` | Source snapshot — frozen |
| `node_QM_VVV.md` | Core — Rule I-1 |
| `vvv_qmrf_ex_graph.json` | Graph edges unchanged — only metadata classification changes |
| `phase1_graph_construction.py` | Loader unchanged — BIAN-14 mapping stays |
| Any file outside `vvv-qmrf-ex/` | Rule I-4 isolation |

---

## 8. Post-Decision Dependency Update

| Open Item | Previous Status | New Status |
|-----------|----------------|------------|
| #1 BIAN-14 structural review | ⏳ Pending | ✅ Resolved — FOLD |
| #2 Final BR_XXXXX ID assignment | ⏳ Deferred | ⏳ Deferred — but now simplified: BIAN-14 needs 1 structural bridge ID (D_001) + 1 source-analogue ID (core) instead of 3+1 |
| #3 EX → Core promotion | Out-of-scope | Out-of-scope — no change |

---

## Schema Validation Checklist

| Check | Status | RCA note |
|---|---|---|
| Document type declared | Pass | Declared as `RCA structural review` for schema alignment. |
| Source traceability | Pass | All claims trace to BIAN_index_SOT.md, system_be_full.md, br_ex_be_registry.md, and BE_QM_Bridge_Finalization_Review_Uniqueness_Audit.md. |
| Claim traceability | Pass | Decision scored with 5-criterion weighted rubric at threshold 4.0/5. |
| Boundary / non-claim guardrail | Pass | EX-only scope; no core file modification; BIAN-15 safety explicitly verified. |
| Validation rule | Pass | Reuse only with source, claim type, and boundary preserved. |
