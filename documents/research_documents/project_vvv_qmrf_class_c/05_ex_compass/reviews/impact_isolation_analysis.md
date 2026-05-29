# VVV-QMRF-EX → VVV-QMRF Impact & Isolation Analysis

> **Date:** 2026-05-20
> **Purpose:** Kiểm tra plan VVV-QMRF-EX ảnh hưởng trực tiếp đến file nào, và đánh giá kế hoạch cách ly
>
> **Status (2026-05-20):** ✅ **CLOSED** — Fix 1, Fix 2, Fix 3 đã applied vào plan **v1.0**. Xem [`rca_checkpoint.md`](./rca_checkpoint.md) §2 để xem chi tiết applied-at-version và verification. Plan hiện tại là v1.1 (đã thêm F1-F6 từ RCA review tiếp theo).

---

## 1. File Impact Classification

### 🟢 READ-ONLY — Plan chỉ đọc, không sửa

| # | File | Plan reference | Mục đích |
|---|---|---|---|
| 1 | [system_be_full.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/SYSTEM_Buddhist_Epistemology/system_be_full.md) | Step 1.1 | Parse 263 BE nodes → NetworkX |
| 2 | [system_buddhist_epistemology.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/SYSTEM_Buddhist_Epistemology/system_buddhist_epistemology.md) | — | Quick reference |
| 3 | [system_qm_full.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/SYSTEM_Quantum_Measurement/system_qm_full.md) | Step 1.3 | Parse 105 QM nodes → NetworkX |
| 4 | [node_QM_VVV.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/vvv-qmrf/node_QM_VVV.md) | Step 1.2 | Parse 55 VVV nodes → NetworkX |
| 5 | [edge_QM_VVV.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/vvv-qmrf/edge_QM_VVV.md) | Step 1.4 | Parse 115 edges → NetworkX |
| 6 | [schema_guide.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/vvv-qmrf/schema_guide.md) | Schema ref | Schema compliance check |
| 7 | [dictionary.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/vvv-qmrf/dictionary.md) | Term ref | Terminology reference |
| 8 | 15 category files (`category/`) | Semantic ref | Node definition enrichment |
| 9 | 17 framework postulates (`framework/`) | Semantic ref | E01-E17 postulate definitions |
| 10 | `be_263_node_expansion/` (21 files) | Step 1.4 | Draft bridge data source |

**Kết luận:** ✅ Các files này an toàn — plan chỉ đọc dữ liệu từ đây.

---

### 🟡 RISK ZONE — Plan có ý định gián tiếp ảnh hưởng

> [!WARNING]
> **Hai điểm rủi ro trong plan hiện tại:**

#### Rủi ro 1: Bridge Registry Migration (Plan Section 4.4, line 453)

| File bị ảnh hưởng | Rủi ro |
|---|---|
| [bridge_QM_standard_to_VVV_QMRF.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/vvv-qmrf/bridge_QM_standard_to_VVV_QMRF.md) | Plan nói "15 migrated BR_XXXXX edges (from v0.1 bridge registry)" → **ngụ ý sẽ di chuyển/sao chép 15 BR_XXXXX edges vào BR_EX_QM registry** |

**Vấn đề:** Plan không rõ ràng liệu:
- (A) **Copy** 15 BR_XXXXX vào BR_EX_QM (giữ nguyên file gốc) — ✅ An toàn
- (B) **Migrate** = xóa khỏi file gốc, chuyển sang BR_EX_QM — ❌ Phá vỡ VVV-QMRF core

**Plan hiện tại dùng từ "migrated" (line 453, Section 4.4) → có thể hiểu là option B.**

#### Rủi ro 2: Phase 2 Edge Promotion (Plan Section 4.1–4.2)

| File bị ảnh hưởng | Rủi ro |
|---|---|
| [edge_QM_VVV.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/vvv-qmrf/edge_QM_VVV.md) | Plan nói "~20-30 promoted Phase 2 edges (meeting bridge-level boundary/verification standards)" → **ngụ ý một số Phase 2 edges sẽ được "promote" thành bridge edges** |

**Vấn đề:** "Promote" có nghĩa gì?
- (A) **Copy + re-classify** trong BR_EX_QM registry, giữ nguyên Phase 2 edges trong `edge_QM_VVV.md` — ✅ An toàn
- (B) **Remove from Phase 2** + add to BR_EX_QM — ❌ Phá vỡ `edge_QM_VVV.md` integrity (115 → 85-95 edges)

**Plan không explicit — cần clarify.**

---

### 🟢 NEW FILES — Plan chỉ tạo mới trong `vvv-qmrf-ex/`

| # | New file | Location | Content |
|---|---|---|---|
| 1 | `br_ex_be_registry.md` | `vvv-qmrf-ex/` | Bridge 1 registry (K-side) |
| 2 | `br_ex_qm_registry.md` | `vvv-qmrf-ex/` | Bridge 2 registry (ρ-side) |
| 3 | `vvv_qmrf_ex_intersection.md` | `vvv-qmrf-ex/` | Intersection analysis |
| 4 | `vvv_qmrf_ex_gaps.md` | `vvv-qmrf-ex/` | Gap analysis |
| 5 | `vvv_qmrf_ex_boundary_audit.md` | `vvv-qmrf-ex/` | Boundary audit |
| 6 | `vvv_qmrf_ex_graph.json` | `vvv-qmrf-ex/data/` | Serialized graph |
| 7 | `vvv_qmrf_ex_similarity_be_vvv.csv` | `vvv-qmrf-ex/data/` | Similarity matrix |
| 8 | `vvv_qmrf_ex_similarity_vvv_qm.csv` | `vvv-qmrf-ex/data/` | Similarity matrix |
| 9 | `vvv_qmrf_ex_centrality.csv` | `vvv-qmrf-ex/data/` | Centrality scores |
| 10 | `vvv_qmrf_ex_context.json` | `vvv-qmrf-ex/data/` | Context snapshot |

**Kết luận:** ✅ Tất cả outputs mới nằm trong `vvv-qmrf-ex/` — cách ly đúng.

---

## 2. Đánh Giá Kế Hoạch Cách Ly Hiện Tại

### Điểm mạnh ✅

| # | Aspect | Status |
|---|---|---|
| 1 | Tất cả output mới → `vvv-qmrf-ex/` | ✅ Isolated |
| 2 | Dùng code prefix riêng: `BR_EX_BE_XXXXX`, `BR_EX_QM_XXXXX` | ✅ No collision với `BR_XXXXX`, `ED_QM_VVV_XXXXX` |
| 3 | Boundary controls (Section 8) | ✅ 7 controls defined |
| 4 | "No automatic E17+" rule | ✅ Không tự tạo postulate mới |
| 5 | "QM Standard nodes are read-only anchors" | ✅ Không sửa QM system |

### Điểm yếu ⚠️

| # | Aspect | Issue | Severity |
|---|---|---|---|
| 1 | **"Migrated" BR_XXXXX** | Plan dùng từ "migrated" cho 15 BR v0.1 edges — không rõ copy hay move | 🔴 High |
| 2 | **"Promoted" Phase 2 edges** | Plan nói "promoted" cho 20-30 edges — không rõ copy hay remove | 🔴 High |
| 3 | **Không có Isolation Protocol** | Plan không có section riêng về cách ly VVV-QMRF-EX khỏi VVV-QMRF | 🟡 Medium |
| 4 | **Không có rollback plan** | Nếu VVV-QMRF-EX thất bại, không có cách undo | 🟡 Medium |
| 5 | **Graph JSON chứa VVV-QMRF data** | `vvv_qmrf_ex_graph.json` sẽ chứa copy của toàn bộ VVV-QMRF graph — nhưng đây là snapshot, không phải SOT | 🟢 Low |

---

## 3. Proposed Isolation Protocol — Cần Bổ Sung Vào Plan

> [!IMPORTANT]
> **Đề xuất thêm Section mới vào plan: "Isolation Protocol"**

### Rule I-1: READ-ONLY Contract

```
VVV-QMRF-EX MUST NOT modify any file outside of:
  documents/research_documents/vvv-qmrf-ex/
```

**Files được bảo vệ (frozen):**

| Protected file | Protection level |
|---|---|
| `vvv-qmrf/node_QM_VVV.md` | 🔒 FROZEN — không thêm/xóa/sửa node |
| `vvv-qmrf/edge_QM_VVV.md` | 🔒 FROZEN — không thêm/xóa/sửa edge |
| `vvv-qmrf/bridge_QM_standard_to_VVV_QMRF.md` | 🔒 FROZEN — không migrate, chỉ copy-reference |
| `vvv-qmrf/schema_guide.md` | 🔒 FROZEN |
| `vvv-qmrf/dictionary.md` | 🔒 FROZEN |
| `SYSTEM_Buddhist_Epistemology/*` | 🔒 FROZEN |
| `SYSTEM_Quantum_Measurement/*` | 🔒 FROZEN |
| `category/*` | 🔒 FROZEN |
| `framework/*` | 🔒 FROZEN |

### Rule I-2: Copy-Not-Move

```
"Migrate" → RENAME to "Reference"
"Promote" → RENAME to "Derived-copy"

BR_EX_QM registry will REFERENCE BR_XXXXX edges by ID,
NOT move them from bridge_QM_standard_to_VVV_QMRF.md.

BR_EX_QM registry will DERIVE-COPY Phase 2 edges,
NOT remove them from edge_QM_VVV.md.
```

### Rule I-3: Namespace Isolation

```
VVV-QMRF-EX uses exclusively:
  - BR_EX_BE_XXXXX  (Bridge 1 edges)
  - BR_EX_QM_XXXXX  (Bridge 2 edges)

VVV-QMRF-EX MUST NOT create:
  - N_QM_VVV_XXXXX  (VVV nodes — only VVV-QMRF can)
  - ED_QM_VVV_XXXXX (VVV edges — only VVV-QMRF can)
  - BR_XXXXX        (v0.1 bridges — only VVV-QMRF can)
  - N_BE_XXXXX      (BE nodes — only BE System can)
  - N_QM_XXXXX      (QM nodes — only QM System can)
```

### Rule I-4: Rollback = Delete Directory

```
If VVV-QMRF-EX is abandoned or fails:
  DELETE documents/research_documents/vvv-qmrf-ex/
  No other file is affected.
  VVV-QMRF remains intact.
```

### Rule I-5: Promotion Gate (EX → Core)

```
If VVV-QMRF-EX results prove valuable and user approves:
  1. New BR_EX edges may be SELECTIVELY copied into
     bridge_QM_standard_to_VVV_QMRF.md as new BR_XXXXX entries
  2. This requires SEPARATE RCA approval — not automatic
  3. VVV-QMRF-EX does NOT auto-merge into VVV-QMRF
```

---

## 4. Plan Update Needed

> [!CAUTION]
> **2 chỉnh sửa cần thực hiện trong [vvv-qmrf-ex-plan.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/vvv-qmrf-ex/vvv-qmrf-ex-plan.md) trước khi execute:**

### Fix 1: Section 4, line ~210 — Change "migrated" to "referenced" — ✅ **APPLIED at plan v1.0** (see [`rca_checkpoint.md`](./rca_checkpoint.md) §2)

```diff
- **Tier 1:** 15 migrated BR_XXXXX edges (from v0.1 bridge registry)
+ **Tier 1:** 15 referenced BR_XXXXX edges (copy-reference from v0.1 bridge registry; originals remain frozen in bridge_QM_standard_to_VVV_QMRF.md)
```

### Fix 2: Section 4, line ~211 — Change "promoted" to "derived-copy" — ✅ **APPLIED at plan v1.0** (see [`rca_checkpoint.md`](./rca_checkpoint.md) §2)

```diff
- **Tier 2:** ~20-30 promoted Phase 2 edges (meeting bridge-level boundary/verification standards)
+ **Tier 2:** ~20-30 derived-copy Phase 2 edges (meeting bridge-level boundary/verification standards; originals remain frozen in edge_QM_VVV.md)
```

### Fix 3: Add new Section 8.5 — Isolation Protocol — ✅ **APPLIED at plan v1.0** (now Section 8 with Rules I-1 to I-5; see [`rca_checkpoint.md`](./rca_checkpoint.md) §2)

Add the full Isolation Protocol (Rules I-1 through I-5) as a new section in the plan.

---

## 5. Summary — Impact Map

```
┌─────────────────────────────────────────────────────┐
│             VVV-QMRF-EX Impact Boundary             │
│                                                     │
│  🔒 FROZEN (read-only)         📝 NEW (write)       │
│  ┌──────────────────┐         ┌──────────────────┐  │
│  │ SYSTEM_BE (263)   │──READ──▶│ vvv-qmrf-ex/     │  │
│  │ SYSTEM_QM (105)   │──READ──▶│  br_ex_be_*.md   │  │
│  │ node_QM_VVV (55)  │──READ──▶│  br_ex_qm_*.md   │  │
│  │ edge_QM_VVV (115) │──READ──▶│  intersection.md │  │
│  │ bridge_v0.1 (15)  │──READ──▶│  gaps.md         │  │
│  │ draft bridges (19)│──READ──▶│  data/*.json/csv │  │
│  │ categories (15)   │──READ──▶│                  │  │
│  │ framework (17)    │         │                  │  │
│  └──────────────────┘         └──────────────────┘  │
│       ❌ NO WRITE                 ✅ ALL WRITE       │
└─────────────────────────────────────────────────────┘
```

**Rollback:** Xóa `vvv-qmrf-ex/` → VVV-QMRF không bị ảnh hưởng gì.
