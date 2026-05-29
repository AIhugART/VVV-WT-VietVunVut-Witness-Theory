Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

> **DISCLAIMER / CANH BAO:** VVV-QMRF is independent personal research (Layer 1-2: Class D; Layer 3 K9_E: Class C genuine), not Standard Quantum Mechanics, not peer-reviewed or experimentally validated, and not for real-world technical use. Full boundary protocol: `DISCLAIMER.md`.

# VVV-QMRF-EX Bridge Promotion Pipeline

**Document type:** index (bridge promotion pipeline)
**Date:** 2026-05-23
**Status:** active
**Scope:** Quy trinh chuan hoa nhan node moi tu `source_snapshot/vvv_qmrf_core/node_QM_VVV.md` va promote thanh BR_EX_BE va BR_EX_QM bridge entries.
**Out of scope:** Khong mutate frozen EX baseline metrics; khong tu dong sua registry files; khong thay the domain expert review.

**Source corpus:**

| Source | Role |
|---|---|
| `source_snapshot/vvv_qmrf_core/node_QM_VVV.md` | Single source of truth for VVV node codes |
| `source_snapshot/system_be/system_be_full.md` | BE SOT for K-side bridge trace |
| `source_snapshot/system_qm/system_qm_full.md` | QM SOT for rho-side bridge trace |
| `br_ex_be_registry.md` | Target registry -- K-side bridge entries |
| `br_ex_qm_registry.md` | Target registry -- rho-side bridge entries |
| `ex_schema_addendum.md` | Namespace rules + promotion gate + direction convention |
| `source_snapshot/vvv_qmrf_core/schema_guide.md` | Document creation contract |

---

## RCA Purpose

### Define

**Symptom:** [node_QM_VVV.md](source_snapshot/vvv_qmrf_core/node_QM_VVV.md) duoc update lien tuc -- v29 K9_E extraction them 7 nodes moi (N_QM_VVV_00060-00066) -- nhung cac bridge registry khong duoc sync dong bo.

**Current gap:**
- 3 nodes chi co DRAFT entries: N_QM_VVV_00056, 00057, 00059
- 7 K9_E Class C nodes hoan toan MISSING o ca hai registry: N_QM_VVV_00060-00066

### Trace -- 5 Whys

1. Vi sao node moi khong duoc promote? Vi khong co quy trinh chuan.
2. Vi sao khong co quy trinh? Vi promotion duoc lam ad-hoc theo tung batch (Phase 1, Phase 7, Phase 12).
3. Vi sao ad-hoc? Vi moi batch co source edge khac nhau (VVV_TO_BE, DRAFT_BRIDGE_BE_VVV, BR_EX_BE_NEW) va gate criteria khac nhau.
4. Vi sao khac nhau? Vi khong co mot RCA-based promotion gate thong nhat cho tat ca bridge types.
5. **Root cause:** VVV-QMRF-EX thieu mot **standardized, repeatable bridge promotion pipeline** bao gom: (a) phat hien node moi, (b) phan loai K-side/rho-side potential, (c) ap dung RCA gate thong nhat, (d) output bridge entry dung format.

### Isolate

Khong co quy trinh phat hien + phan loai + promote duoc viet thanh document doc lap. Moi lan promote deu la tac vu thao tung rieng le.

### Fix

Pipeline nay chuan hoa 4 giai doan: **Detect -> Classify -> RCA Gate -> Promote**.

### Verify

Root cause bi loai bo khi: (1) moi node moi duoc phat hien qua gap detection, (2) duoc phan loai, (3) qua RCA gate >= 4.0/5, (4) ghi theo template chuan, (5) pass verification checklist.

---

## 1. Node Gap Detection

### 1.1 Parse source

**Input:** `source_snapshot/vvv_qmrf_core/node_QM_VVV.md`

Extract tat ca `N_QM_VVV_XXXXX` codes tu bang "New VVV-QMRF Nodes" (Section 2). Chi lay ACTIVE codes -- loai tru cac codes da bi folded/downgraded (ghi chu trong RCA note duoi bang).

Output: `ACTIVE_VVV_NODES` = set of all active N_QM_VVV_XXXXX codes.

### 1.2 Parse registries

**Input:** `br_ex_be_registry.md`, `br_ex_qm_registry.md`

Extract tat ca VVV node codes da co ACTIVE bridge entry. Loai tru:
- `RECLASSIFIED-v1.7` entries
- `FOLDED-structural-review` entries
- `DRAFT_ONLY` entries (BR_EX_BE_DRAFT_*, BR_EX_QM_DRAFT_*)

Output:
- `BRIDGED_BE_VVV` = set of VVV nodes with active BR_EX_BE entry
- `BRIDGED_QM_VVV` = set of VVV nodes with active BR_EX_QM entry

### 1.3 Diff

```
K_GAP    = ACTIVE_VVV_NODES minus BRIDGED_BE_VVV   (thieu K-side BE bridge)
RHO_GAP  = ACTIVE_VVV_NODES minus BRIDGED_QM_VVV   (thieu rho-side QM bridge)
DUAL_GAP = K_GAP giao voi RHO_GAP                    (thieu ca hai)
```

**Gap report format:**

| Gap Type | Node Code | Node Concept | Claim Class | Priority |
|---|---|---|---|---|
| DUAL_GAP | N_QM_VVV_00060 | K9_E Probability Postulate (P9) | Class C | HIGH |
| K_GAP | N_QM_VVV_00062 | f_perp(K_ctx) | Class C | MEDIUM |

**Priority rule:**
- `HIGH`: DUAL_GAP + Class C node
- `MEDIUM`: DUAL_GAP + Class D, hoac single-side gap + Class C
- `LOW`: Single-side gap + Class D

---

## 2. Node Classification Matrix

### 2.1 Classification axes

| Axis | Source in `node_QM_VVV.md` | Output |
|---|---|---|
| **K-side potential** | "Difference from old QM system" column + "RCA root cause" -- co reference BE concept (BIAN, Anupalabdhi, Trairupya, Apoha, Svasamvedana)? | `K_CANDIDATE` hoac `K_NOT_APPLICABLE` |
| **rho-side potential** | "Existing QM nearest node(s)" column -- co canonical QM node (N_QM_XXXXX)? | `RHO_CANDIDATE` hoac `RHO_NOT_APPLICABLE` |
| **Claim class** | "RCA strength / status" column | `CLASS_C` hoac `CLASS_D` |

**Rule for K-side:** Neu RCA root cause mention BIAN-X hoac BE concept name -> `K_CANDIDATE`.

**Rule for rho-side:** Neu co it nhat 1 canonical QM node in "Existing QM nearest node(s)" -> `RHO_CANDIDATE`.

### 2.2 Special classification rules

**K9_E internal nodes** (beta 00061, f_perp 00062, K_ctx 00063, delta_S 00066): Purely VVV internal -- khong co BE source-analogue truc tiep.
- K-side: `K_PENDING-RCA` -- defer, khong block rho-side promote
- rho-side: `RHO_CANDIDATE` -- promote neu co QM substrate hoac recognized as independent VVV formalism

**Evidence/prediction nodes** (00064, 00065): Measurement result hoac prediction -- khong phai concept.
- K-side: `K_NOT_APPLICABLE` -- evidence khong can BE bridge
- rho-side: `RHO_CANDIDATE` -- bridge den QM experimental foundation
- Boundary guard bat buoc: "This is an empirical measurement result, not a conceptual bridge"

**Root vs sub-nodes:** Root category node duoc uu tien promote truoc sub-nodes. Sub-nodes co the inherit bridge neu relation type la `contains`.

### 2.3 Classification output format

| Node | K-side | rho-side | Claim Class | Priority |
|---|---|---|---|---|
| N_QM_VVV_00060 | K_PENDING-RCA | RHO_CANDIDATE (N_QM_00016) | CLASS_C | HIGH |
| N_QM_VVV_00061 | K_NOT_APPLICABLE | RHO_CANDIDATE (internal) | CLASS_C | HIGH |
| N_QM_VVV_00062 | K_CANDIDATE (Trairupya) | RHO_CANDIDATE (N_QM_00016) | CLASS_C | MEDIUM |
| N_QM_VVV_00063 | K_CANDIDATE (K5 bot_K) | RHO_CANDIDATE (independent) | CLASS_C | MEDIUM |
| N_QM_VVV_00064 | K_NOT_APPLICABLE | RHO_CANDIDATE (N_QM_00090) | CLASS_C | MEDIUM |
| N_QM_VVV_00065 | K_NOT_APPLICABLE | RHO_CANDIDATE (internal) | CLASS_C | LOW |
| N_QM_VVV_00066 | K_NOT_APPLICABLE | RHO_CANDIDATE (internal) | CLASS_C | LOW |

---

## 2.5 RCA Freshness Gate

**Purpose:** Phan loai do "tuoi" cua RCA truoc khi vao 5-Step RCA Gate. Tranh confirmatory RCA bi treat nhu exploratory — dam bao assumptions duoc cross-check doc lap.

**Pipeline position:**

```
Detect (Section 1) → Classify (Section 2) → [RCA Freshness Gate (Section 2.5)] → RCA Gate (Section 3) → Promote (Section 4)
```

### 2.5.1 Freshness classification

Moi bridge proposal duoc gan mot trong ba freshness levels:

| Freshness | Trigger | Meaning |
|-----------|---------|---------|
| `EXPLORATORY` | Node hoan toan moi, chua co pre-classification, chua co RCA truoc do | Map la **kham pha** — can independent SOT verification |
| `CONFIRMATORY` | Node da duoc pre-classify (e.g., Section 7 Immediate Application) | Map la **xac nhan** — assumptions can cross-check doc lap |
| `RE-VERIFY` | Node co DRAFT RCA tu batch truoc (C3/C4/C5) | Map la **xac minh lai** — SOT khong thay doi ke tu RCA goc |

### 2.5.2 Cross-check requirements per freshness level

| Freshness | Required cross-check | Minimum SOT sources |
|-----------|---------------------|---------------------|
| `EXPLORATORY` | Full 5-step RCA + independent SOT verification | >= 2 source files doc lap |
| `CONFIRMATORY` | Cross-check pre-classification assumptions: (a) QM substrate co thuc su la nearest node? (b) BE analogue co direct hay indirect? (c) Co alternative map nao bi bo qua? | >= 1 SOT file ngoai pre-classification source |
| `RE-VERIFY` | (a) SOT khong thay doi ke tu RCA goc; (b) DRAFT fields day du; (c) Neu SOT thay doi → escalate len `EXPLORATORY` | SOT goc + current SOT (diff) |

### 2.5.3 Indirect map detection

**Rule:** Neu BE bridge di qua >= 2 lop trung gian, gan co `INDIRECT-N-LEVEL` va ghi ro mediation path trong boundary note.

**Detection test:**
1. BE node → VVV node: co direct source-analogue trong RCA root cause?
2. Neu khong: VVV node co `contains` / `inherits from` relation den mot VVV node khac?
3. Neu co: quan he do la `structural_analogy` (1 level), `functional_analogy` (1 level), hay `transitive` (>= 2 levels)?

**Example (from 2026-05-23 batch):**
```
f_perp (00062) → N_QM_VVV_00042 → N_BE_00018 (Trairupya)
→ 2 levels indirect → flag: INDIRECT-2-LEVEL
```

### 2.5.4 Internal map audit

**Rule:** Khi QM node = "Internal", map khong tao graph edge nhung van can RCA gate. Phai kiem tra:

1. That su khong co canonical QM node nao tuong duong?
2. Co QM node nao gan dung (partial match) bi bo qua?
3. Neu co QM experimental foundation gan nhat → ghi ro trong rationale (e.g., "No direct QM analogue; nearest experimental foundation is N_QM_XXXXX")

**Internal Audit Schedule:** Moi 6 thang, re-check danh sach "Internal" maps xem co canonical QM node moi nao xuat hien khong.

### 2.5.5 Extended classification output format

Mo rong Section 2.3 output format voi cot freshness:

| Node | K-side | rho-side | Claim Class | RCA Freshness | Priority |
|---|---|---|---|---|---|
| N_QM_VVV_00060 | K_PENDING-RCA | RHO_CANDIDATE (N_QM_00016) | CLASS_C | CONFIRMATORY | HIGH |
| N_QM_VVV_00061 | K_NOT_APPLICABLE | RHO_CANDIDATE (internal) | CLASS_C | CONFIRMATORY | HIGH |
| N_QM_VVV_00062 | K_CANDIDATE (Trairupya) | RHO_CANDIDATE (N_QM_00016) | CLASS_C | CONFIRMATORY | HIGH |
| N_QM_VVV_00063 | K_CANDIDATE (K5 bot_K) | RHO_CANDIDATE (independent) | CLASS_C | CONFIRMATORY | HIGH |
| N_QM_VVV_00064 | K_NOT_APPLICABLE | RHO_CANDIDATE (N_QM_00090) | CLASS_C | CONFIRMATORY | MEDIUM |
| N_QM_VVV_00065 | K_NOT_APPLICABLE | RHO_CANDIDATE (internal) | CLASS_C | CONFIRMATORY | MEDIUM |
| N_QM_VVV_00066 | K_NOT_APPLICABLE | RHO_CANDIDATE (internal) | CLASS_C | CONFIRMATORY | MEDIUM |

### 2.5.6 Freshness Gate decision tree

```
Freshness = EXPLORATORY?
  YES → Full 5-step RCA (Section 3) + >= 2 SOT sources
  NO  → Freshness = CONFIRMATORY?
          YES → Cross-check assumptions + >= 1 independent SOT
                 → Assumptions PASS? → RCA Gate (Section 3)
                 → Assumptions FAIL? → Escalate to EXPLORATORY
          NO  → Freshness = RE-VERIFY?
                  YES → Diff SOT (current vs original RCA)
                         → SOT unchanged + DRAFT complete? → RCA Gate (Section 3)
                         → SOT changed? → Escalate to EXPLORATORY
                  NO  → ERROR: unclassified freshness — escalate
```

### 2.5.7 Edge case: mixed freshness trong cung 1 batch

Neu batch chua ca EXPLORATORY + CONFIRMATORY nodes:
- EXPLORATORY nodes duoc uu tien xu ly truoc (kham pha map moi)
- CONFIRMATORY nodes xu ly sau (xac nhan pre-classification)
- RE-VERIFY nodes xu ly cuoi cung (xac minh lai)

### 2.5.8 RCA gate log: them freshness field

Mo rong Section 3.4 RCA gate log format voi freshness:

```markdown
### RCA Gate Log -- BR_EX_BE_00XXX

| Field | Value |
|---|---|
| **Freshness** | CONFIRMATORY |
| **Pre-classification source** | promote_new_bridge.md Section 7.2 |
| **Cross-check SOT** | system_be_full.md (verified N_BE_XXXXX) |
| **Cross-check result** | PASS / PASS-WITH-FLAGS / FAIL-ESCALATED |

| Step | Score | Finding |
|---|---|---|...
```

### 2.5.9 CONFIRMATORY Spot-Check Anti-Drift Mechanism

**RCA root cause (2026-05-23 batch review):** Khi tat ca node trong batch deu duoc pre-classify la CONFIRMATORY, pipeline co xu huong xac nhan (verify) thay vi thach thuc (falsify) — goi la **confirmatory drift**. Cross-check requirements (§2.5.2) giup giam nhung khong loai bo hoan toan structural bias nay. Root cause: pipeline design chua co co che ngau nhien nang cap freshness de chong confirmatory drift.

**Fix:** Moi batch, chon ngau nhien (random) **it nhat 1 CONFIRMATORY node** upgrade len `EXPLORATORY`. Node duoc chon phai qua full 5-step RCA + independent SOT verification (>= 2 SOT sources doc lap), pha vo structural bias ma khong can thay doi toan bo pipeline.

#### 2.5.9.1 Selection rule

| Batch size (CONFIRMATORY nodes) | Minimum spot-check count |
|---|---|
| 1–3 | 1 |
| 4–7 | 2 |
| 8+ | ceil(N/4) |

**Selection criteria:**
- Uu tien node co **BE bridge INDIRECT** (>= 2 cap) — day la noi confirmatory drift de xuat hien nhat
- Uu tien node co **QM bridge "Internal"** — de independent re-evaluate xem co QM analogue nao bi bo qua khong
- Khong chon node da qua EXPLORATORY trong batch truoc do (tranh lap)

#### 2.5.9.2 Spot-check execution

```
1. Chon ngau nhien N node tu CONFIRMATORY pool
2. Upgrade freshness: CONFIRMATORY → EXPLORATORY
3. Chay full 5-step RCA + >= 2 SOT sources doc lap (theo §2.5.2 dong EXPLORATORY)
4. So sanh ket qua EXPLORATORY vs CONFIRMATORY goc:
   a. Cung PASS → confirmatory bias LOW — tiep tuc
   b. Cung PASS nhung score giam >= 0.5 → confirmatory drift detected — ghi log, escalate review
   c. FAIL → confirmatory drift CONFIRMED — escalate toan bo batch len EXPLORATORY
```

#### 2.5.9.3 Decision tree update

Chen buoc spot-check vao truoc CONFIRMATORY path:

```
Freshness = EXPLORATORY?
  YES → Full 5-step RCA (Section 3) + >= 2 SOT sources
  NO  → Freshness = CONFIRMATORY?
          YES → [SPOT-CHECK] Random selected for EXPLORATORY upgrade?
                  YES → Upgrade to EXPLORATORY → Full 5-step RCA + >= 2 SOT sources
                  NO  → Cross-check assumptions + >= 1 independent SOT
                         → Assumptions PASS? → RCA Gate (Section 3)
                         → Assumptions FAIL? → Escalate to EXPLORATORY
          NO  → Freshness = RE-VERIFY?
                  YES → Diff SOT (current vs original RCA)
                         → SOT unchanged + DRAFT complete? → RCA Gate (Section 3)
                         → SOT changed? → Escalate to EXPLORATORY
                  NO  → ERROR: unclassified freshness — escalate
```

#### 2.5.9.4 Spot-check log format

Mo rong Section 3.4 RCA gate log format voi spot-check field:

```markdown
### RCA Gate Log -- BR_EX_BE_00XXX

| Field | Value |
|---|---|
| **Freshness (original)** | CONFIRMATORY |
| **Spot-Check Upgraded?** | YES → EXPLORATORY |
| **Spot-Check Reason** | Random selection (batch YYYY-MM-DD, N of M) |
| **Pre-classification source** | promote_new_bridge.md Section 7.2 |
| **Cross-check SOT** | system_be_full.md + system_qm_full.md (2 sources, EXPLORATORY) |
| **Cross-check result** | PASS / PASS-WITH-FLAGS / FAIL-ESCALATED |
| **Delta vs CONFIRMATORY** | Score change: X.X → Y.Y (delta = Z.Z) |

| Step | Score | Finding |
|---|---|---|...
```

---

## 3. 5-Step RCA Gate

Moi bridge proposal phai qua 5 buoc. Moi buoc 1.0 diem, tong 5.0.
**Pass threshold: >= 4.0/5.**

### 3.1 Scoring rubric

| Step | Score 1.0 | Score 0.5 | Score 0.0 |
|---|---|---|---|
| **Define** | Node identity + bridge need ro rang | Node ro nhung bridge direction mo ho | Khong xac dinh duoc |
| **Trace** | Source trace day du, SOT anchor chinh xac | Source trace co nhung thieu SOT anchor | Khong trace duoc ve SOT |
| **Isolate** | Root cause lap luan ro rang | Root cause dung nhung lap luan yeu | Khong tim ra root cause |
| **Fix** | Proposal du fields, claim class phu hop, boundary note ro | Thieu 1-2 fields hoac boundary note yeu | Thieu nhieu hoac overclaim |
| **Verify** | Tat ca checks pass | 1-2 minor issues | Major issue (SOT conflict, ID collision, overclaim) |

### 3.2 Decision thresholds

- **>= 4.0/5 -> PASS** -> promote thanh active bridge entry
- **3.5-3.9/5 -> DRAFT** -> ghi DRAFT entry (khong active, khong graphable)
- **< 3.5/5 -> REJECT** -> ghi log ly do, node quay lai `PENDING-RCA`

### 3.3 Edge case rules

- **DUAL_GAP node:** RCA gate chay 2 lan doc lap (K-side + rho-side). Mot side fail khong block side kia.
- **K_PENDING-RCA node:** Chi chay rho-side RCA. K-side ghi chu `K-PENDING-RCA` trong Origin.
- **Evidence node:** Define step ghi ro "empirical measurement result, not a conceptual bridge."

### 3.4 RCA gate log format

```markdown
### RCA Gate Log -- BR_EX_BE_00XXX

| Step | Score | Finding |
|---|---|---|
| Define | 1.0 | [...] |
| Trace | 0.5 | [...] |
| Isolate | 1.0 | [...] |
| Fix | 1.0 | [...] |
| Verify | 1.0 | [...] |
| **Total** | **4.5/5** | **PASS** |

**Decision:** Promote to active entry.
**Date:** YYYY-MM-DD
```

---

## 4. Bridge Entry Templates

### 4.1 BR_EX_BE template (K-side: BE -> VVV)

```markdown
### BR_EX_BE_00XXX -- Entry XXX

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_BE_00XXX` |
| **Type** | new_bridge_promotion |
| **Source Edge Type** | `BR_EX_BE_NEW` |
| **BE Node** | `N_BE_XXXXX` |
| **BE Concept** | [...] |
| **BE Layer** | [core / evidence / RCA] |
| **VVV Node** | `N_QM_VVV_00XXX` |
| **VVV Concept** | [...] |
| **Direction** | N_BE_XXXXX -> N_QM_VVV_00XXX |
| **Relation Type** | [source_analogue_of / structural_analogy / functional_analogy / operator_decomposition / sub_concept_direct_anchor] |
| **Claim Class** | [source_analogue / interpretive_mapping / evidence_support] |
| **Confidence** | 0.XX (RCA score X.X/5) |
| **Boundary Note** | [...] |
| **Rationale** | [...] |
| **Origin** | promote_new_bridge RCA gate; YYYY-MM-DD |
```

**Field rules:**
- `Type`: Luon la `new_bridge_promotion`
- `Relation Type`: Tu vocabulary `ex_schema_addendum.md` Section 3 (K-side)
- `Direction`: BE -> VVV (K-side convention)
- `Confidence`: RCA score / 5.0
- `Boundary Note`: Bat buoc -- it nhat 1 cau gioi han claim

### 4.2 BR_EX_QM template (rho-side: VVV -> QM)

```markdown
### BR_EX_QM_00XXX -- Entry XXX

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_QM_00XXX` |
| **Type** | new_bridge_promotion |
| **Source Edge Type** | `BR_EX_QM_NEW` |
| **VVV Node** | `N_QM_VVV_00XXX` |
| **VVV Concept** | [...] |
| **QM Node** | `N_QM_XXXXX` |
| **QM Concept** | [...] |
| **QM Layer** | RCA |
| **Direction** | N_QM_VVV_00XXX -> N_QM_XXXXX |
| **Relation Type** | [physical_substrate_for / registration_layer_extension_of] |
| **Claim Class** | interpretive_mapping |
| **Confidence** | 0.XX (RCA score X.X/5) |
| **Boundary Note** | Not physical explanation; not new QM law. [...] |
| **Rationale** | [...] |
| **Origin** | promote_new_bridge RCA gate; YYYY-MM-DD |
```

**Field rules:**
- `Relation Type`: `physical_substrate_for` (standard) hoac `registration_layer_extension_of`
- `Direction`: VVV -> QM (rho-side convention)
- `Boundary Note`: Bat buoc include "Not physical explanation; not new QM law"

### 4.3 Draft entry template (RCA score 3.5-3.9)

```markdown
### BR_EX_XX_DRAFT_00XXX -- Draft Entry XXX

| Field | Value |
|-------|-------|
| **BR_EX_ID** | `BR_EX_XX_DRAFT_00XXX` |
| **Type** | draft_promotion_pending |
| **Status** | `DRAFT-PENDING-REVIEW` |
| **RCA Score** | X.X/5 |
| **Deferral Reason** | [Step(s) scoring below 1.0] |
| **Promotion Readiness** | [What needs to improve] |
| ... (remaining fields same as active template) ... |
```

---

## 5. Promotion Execution Rules

### 5.1 Atomicity

Moi node promote doc lap. Mot node fail RCA gate KHONG block cac node khac.

### 5.2 Immutability

- KHONG mutate frozen EX baseline (`/52` denominator)
- Node moi ghi vao registry voi **next available ID**, khong renumber
- DRAFT IDs nam ngoai active namespace

### 5.3 ID assignment

```
BR_EX_BE next ID = max({existing active BR_EX_BE numbers}) + 1
BR_EX_QM next ID = max({existing active BR_EX_QM numbers}) + 1
```

DRAFT IDs (BR_EX_BE_DRAFT_*, BR_EX_QM_DRAFT_*) khong anh huong den next ID.

### 5.4 Registry sync

Sau khi promote, cap nhat header:

```markdown
**Version:** X.Y (YYYY-MM-DD promote_new_bridge batch)
**Date:** YYYY-MM-DD
**Total Entries:** N active (+M new)
```

### 5.5 Batch promote workflow

```
1. Trigger: node_QM_VVV.md duoc update
2. Detect: Gap detection (Section 1) -> gap list
3. Classify: Classification matrix (Section 2) -> phan loai
4. RCA Freshness Gate (Section 2.5): Phan loai freshness
   a. EXPLORATORY: full RCA + >= 2 SOT sources
   b. CONFIRMATORY: cross-check assumptions + >= 1 independent SOT
   c. RE-VERIFY: diff SOT, DRAFT field check
5. RCA Gate: Moi node qua 5-step RCA (Section 3)
   a. DUAL_GAP: 2 RCA gates doc lap
   b. K_GAP only: chi K-side RCA
   c. RHO_GAP only: chi rho-side RCA
6. Promote: Ghi vao registry (Section 4)
   a. >= 4.0: ACTIVE
   b. 3.5-3.9: DRAFT
   c. < 3.5: REJECTED + log
7. Sync: Cap nhat registry header
8. Verify: Verification checklist (Section 6)
```

---

## 6. Verification Checklist

### 6.1 Per-entry checklist

- [ ] Node code ton tai va ACTIVE trong `node_QM_VVV.md`
- [ ] BR_EX_BE: BE node trace ve `system_be_full.md`
- [ ] BR_EX_QM: QM node trace ve `system_qm_full.md`
- [ ] Claim class khong overclaim (boundary note bat buoc)
- [ ] RCA score >= 4.0/5 (hoac 3.5-3.9 cho DRAFT)
- [ ] BR_EX_ID khong trung existing active entry
- [ ] Direction tuan theo F2 non-reversal rule
- [ ] Boundary note ton tai va ro rang
- [ ] Relation type nam trong vocabulary da khai bao
- [ ] Khong mutate frozen EX baseline metrics
- [ ] Registry header metadata duoc update

### 6.2 Per-batch checklist

- [ ] Tat ca gap nodes da duoc xu ly
- [ ] Gap list duoc cap nhat
- [ ] Khong con DUAL_GAP HIGH-priority nodes chua xu ly
- [ ] Registry files khong bi corrupt
- [ ] Khong ID collision

### 6.3 Cross-registry consistency

- [ ] Neu node co ca BR_EX_BE va BR_EX_QM: claim class nhat quan
- [ ] Neu node chi co mot side: ghi ro reason cho side con lai
- [ ] K9_E internal nodes khong bi ep thanh BE bridge khi khong co source-analogue

---

## 7. Immediate Application: K9_E Nodes (N_QM_VVV_00060-00066)

### 7.1 Gap detection

```
K_GAP   = {00060, 00061, 00062, 00063, 00064, 00065, 00066} (7 nodes)
RHO_GAP = {00060, 00061, 00062, 00063, 00064, 00065, 00066} (7 nodes)
DUAL_GAP = {00060, 00061, 00062, 00063, 00064, 00065, 00066} (7 nodes)
```

### 7.2 Classification (preliminary)

| Node | K-side | rho-side | Priority |
|---|---|---|---|
| 00060 K9_E Postulate | K_PENDING-RCA | RHO_CANDIDATE (N_QM_00016) | HIGH |
| 00061 beta | K_NOT_APPLICABLE | RHO_CANDIDATE (internal) | HIGH |
| 00062 f_perp | K_CANDIDATE (Trairupya) | RHO_CANDIDATE (N_QM_00016) | HIGH |
| 00063 K_ctx | K_CANDIDATE (K5 bot_K) | RHO_CANDIDATE (independent) | HIGH |
| 00064 Genuine Fit | K_NOT_APPLICABLE | RHO_CANDIDATE (N_QM_00090) | MEDIUM |
| 00065 2BSM/1BSM | K_NOT_APPLICABLE | RHO_CANDIDATE (internal) | MEDIUM |
| 00066 delta_S | K_NOT_APPLICABLE | RHO_CANDIDATE (internal) | MEDIUM |

### 7.3 Execution order

1. N_QM_VVV_00060: BR_EX_QM truoc, BR_EX_BE defer
2. N_QM_VVV_00061: BR_EX_QM only
3. N_QM_VVV_00062: BR_EX_QM + BR_EX_BE
4. N_QM_VVV_00063: BR_EX_QM + BR_EX_BE
5. N_QM_VVV_00064: BR_EX_QM only (evidence node, boundary guard)
6. N_QM_VVV_00065: BR_EX_QM only (prediction node, boundary guard)
7. N_QM_VVV_00066: BR_EX_QM only (theoretical metric)

### 7.4 Target IDs

```
BR_EX_QM: max active = BR_EX_QM_00074 -> next: BR_EX_QM_00075 through 00081 (7 entries)
BR_EX_BE: max active = BR_EX_BE_00072 -> next: BR_EX_BE_00073, 00074 (2 entries for 00062, 00063)
```
(DRAFT namespace IDs khong anh huong.)

### 7.5 K9_E boundary guards (mandatory for all Class C nodes)

- "K9_E is a POSTULATE (P9), not a theorem derivable from K1-K8. beta is a phenomenological parameter. Evidence is real but ambiguous (2.31sigma). Confirmation or rejection requires a 3-observer experiment."
- Evidence nodes: "This is an empirical measurement result / falsifiable prediction, not a conceptual bridge."
- Internal nodes: "This is a VVV-QMRF internal construct -- no direct BE or QM analogue."

---

## What This Document Does NOT Claim

* Khong tu dong hoa promotion -- moi entry van can RCA review
* Khong thay the domain expert review cho cross-domain mappings
* Khong mutate frozen EX baseline metrics
* Khong claim moi node CAN hoac NEN co ca K-side va rho-side bridge
* Khong dinh nghia lai VVV node codes
* Khong sua doi namespace rules trong `ex_schema_addendum.md`

---

## Validation Checklist

- [x] Document type declared: index (bridge promotion pipeline)
- [x] RCA purpose: Define, Trace, Isolate, Fix, Verify
- [x] Source corpus listed
- [x] All 7 sections present
- [x] RCA threshold >= 4.0/5 applied consistently
- [x] BR_EX_BE and BR_EX_QM templates match existing registry format
- [x] Namespace rules consistent with `ex_schema_addendum.md`
- [x] Direction conventions follow F2 non-reversal rule
- [x] Boundary notes mandatory for all entry types
- [x] K9_E immediate application section complete

---

## References

| Reference | Path |
|---|---|
| VVV Node SOT | `source_snapshot/vvv_qmrf_core/node_QM_VVV.md` |
| BE SOT | `source_snapshot/system_be/system_be_full.md` |
| QM SOT | `source_snapshot/system_qm/system_qm_full.md` |
| K-side Registry | `br_ex_be_registry.md` |
| rho-side Registry | `br_ex_qm_registry.md` |
| EX Schema Addendum | `ex_schema_addendum.md` |
| EX Expansion Plan | `vvv-qmrf-ex-plan.md` |
| Core Schema Guide | `source_snapshot/vvv_qmrf_core/schema_guide.md` |
