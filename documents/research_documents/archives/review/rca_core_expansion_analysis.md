# RCA: VVV-QMRF Core Expansion — Khả năng, Hướng đi, và Trade-off EX Promotion

**Date:** 2026-05-21
**Scope:** Phân tích 3 câu hỏi:
1. Core còn mở rộng thêm được không?
2. Thêm cụ thể hướng nào?
3. Nếu apply EX → Core thì trade-off gì?

---

## 1. Hiện trạng Core (Snapshot)

| Thành phần | Số lượng | File |
|-----------|----------|------|
| **VVV nodes** | 55 (N_QM_VVV_00001–00055, gap ở 00017/00019) | `node_QM_VVV.md` |
| **VVV edges** (nội bộ) | 40 (Phase 1: VVV↔VVV) | `edge_QM_VVV.md` |
| **VVV→QM edges** | 60 (Phase 2: grounded_by) | `edge_QM_VVV.md` |
| **VVV→BE edges** | 15 (Phase 3: source_analogue) | `edge_QM_VVV.md` |
| **Bridge edges** | 15 (BR_00001–BR_00015) | `bridge_QM_standard_to_VVV_QMRF.md` |
| **Categories** | 15 (Cat 01–15) | `category/` |
| **BIAN gaps** | 19 resolved + 1 reserved (BIAN-20) | `BIAN_index_SOT.md` |
| **EX bridge entries** | 69 total / 64 active / 2 folded / 3 reclassified | `br_ex_be_registry.md` |

### Câu trả lời ngắn: **Có, Core còn mở rộng được — nhưng theo 5 hướng khác nhau, mỗi hướng có trade-off riêng.**

---

## 2. Năm Hướng Mở Rộng Core

### Hướng A — Thêm VVV Nodes mới (Mở rộng chiều dọc)

| Yếu tố | Chi tiết |
|---------|---------|
| **Nguồn** | Mở BIAN-21+, hoặc phát hiện gap mới từ QM literature |
| **Ví dụ** | Quantum error correction registration, Deferred measurement principle, Quantum contextuality registration |
| **Khả thi?** | ✅ Có — nhưng cần BIAN gap analysis mới |
| **Rủi ro** | Lạm phát nodes → graph phức tạp, khó maintain |
| **Điều kiện** | Phải qua Decision Gate ≥ 3.5/5 (rule trong `node_QM_VVV.md`) |

**Cụ thể:**
- BIAN-20 đang 🔒 Reserved (Entanglement correlation type) — có thể mở
- QM modern topics chưa cover: **Quantum Contextuality** (Kochen-Specker), **Quantum Darwinism** (Zurek), **Quantum Reference Frames** — mỗi cái có thể sinh 2-5 VVV nodes mới

### Hướng B — Thêm Edges nội bộ (Mở rộng chiều ngang)

| Yếu tố | Chi tiết |
|---------|---------|
| **Nguồn** | Phát hiện quan hệ giữa các VVV nodes hiện có mà chưa được encode |
| **Ví dụ** | Self-Completion (00027) ↔ Self-Certifying (00033): cùng address "closure" nhưng chưa có edge |
| **Khả thi?** | ✅ Có — graph hiện tại còn sparse |
| **Rủi ro** | Thấp — không thêm concepts mới, chỉ make explicit quan hệ đã implicit |
| **Điều kiện** | Phải tuân theo controlled relation types |

**Graph density hiện tại:**
- 55 nodes, 40 internal edges → ratio 0.73 edges/node (thấp)
- Lý thuyết: 55 nodes có thể có tới ~1485 directed edges (55×54/2)
- Thực tế hợp lý: 80-120 internal edges (ratio 1.5-2.2)
- **Còn chỗ cho ~40-80 internal edges nữa**

### Hướng C — Thêm Bridge Edges QM↔VVV (Mở rộng liên kết)

| Yếu tố | Chi tiết |
|---------|---------|
| **Nguồn** | `bridge_QM_standard_to_VVV_QMRF.md` §8 đã có expansion rule sẵn |
| **Ví dụ** | 60 Phase 2 edges nhưng chỉ 15 bridges — còn ~45 Phase 2 edges chưa có bridge form |
| **Khả thi?** | ✅ Có — rule đã written: expand in batches of 10-15 |
| **Rủi ro** | Trung bình — mỗi bridge cần schema đầy đủ (claim type, boundary guard, verification) |
| **Điều kiện** | Must map existing Phase 2 edges or document boundary guards |

### Hướng D — Thêm BE Source-Analogue Edges (Mở rộng K-side depth)

| Yếu tố | Chi tiết |
|---------|---------|
| **Nguồn** | BE SOT có 263 nodes, hiện core chỉ dùng 15 source-analogue edges → 15/263 = 5.7% |
| **Ví dụ** | EX registry đã map 64 active BE nodes → VVV nodes. Đây là nguồn chính cho Hướng D |
| **Khả thi?** | ✅ Có — **đây chính là EX → Core promotion** |
| **Rủi ro** | **CAO** — xem §3 Trade-off Analysis |
| **Điều kiện** | Phải qua EX → Core promotion gate (Rule I-5) |

### Hướng E — Thêm Categories mới (Mở rộng framework)

| Yếu tố | Chi tiết |
|---------|---------|
| **Nguồn** | Categories mới từ BIAN gaps mới, hoặc synthesis cross-category |
| **Ví dụ** | "Registration Coherence Maintenance" (giữ coherence qua nhiều registrations liên tiếp), "Multi-Observer Registration Reconciliation" |
| **Khả thi?** | ✅ Có — nhưng cần RCA + BIAN gap analysis |
| **Rủi ro** | Lớn nhất trong 5 hướng — mỗi category sinh 2-5 nodes + edges + postulate |
| **Điều kiện** | Phải có BIAN gap chưa resolved + đủ QM substrate |

---

## 3. Trade-off Analysis: EX → Core Promotion

### 3.1 Cái EX sẽ mang vào Core (nếu promote)

| Từ EX | Số lượng | Vào Core thành |
|-------|----------|----------------|
| reference_copy entries | 34 active | → Nâng cấp thành chính thức Phase 3 source-analogue edges (`ED_QM_VVV_001xx`) |
| similarity candidate | 1 | → Validate hoặc reject |
| expert_manual_mapping | 9 | → Nâng cấp thành chính thức nếu pass RCA |
| stretch_expert_mapping | 20 active | → Mỗi cái cần individual RCA review |
| **Total candidates** | **64** | **Tối đa ~50 new Phase 3 edges** (sau reject/fold) |

### 3.2 Trade-off Matrix

| Dimension | Benefit (Pro) | Cost (Con) | Severity |
|-----------|--------------|------------|----------|
| **Coverage** | Phase 3 tăng từ 15 → ~50-65 source-analogue edges; BE coverage tăng từ 5.7% → ~20% | Nhiều weak/low-confidence edges (0.32-0.70) vào core → giảm average confidence | 🟡 Medium |
| **Traceability** | Mỗi VVV node có nhiều BE anchors hơn → truy vết dày đặc hơn | Graph density tăng → harder to visualize, harder to audit | 🟡 Medium |
| **Integrity** | EX entries đã qua 11 Phases of audit → not random | Nhưng EX threshold thay đổi (3.5→4.0 trong v1.7) → 3 entries đã bị reclassify. Nếu core freeze, phải pick 1 threshold forever | 🔴 High |
| **Maintenance** | Centralized: 1 file thay vì 2 registries | Core files hiện frozen (Rule I-1) → promotion = unfreeze → cần re-freeze → version bump toàn bộ | 🔴 High |
| **Publication** | Paper có nhiều BE support evidence hơn → richer bibliography | Paper phải defend mỗi mapping → thêm nhiều qualification paragraphs | 🟡 Medium |
| **Backward compatibility** | Không break gì — additive only | Nhưng: edge count tăng ~4x cho Phase 3 → any downstream tool phải update | 🟢 Low |
| **Schema** | EX schema (`ex_schema_addendum.md`) đã handle confidence tiers, claim types | Core schema (`schema_guide.md`) chưa có confidence tiers cho source-analogue edges → cần schema update | 🟡 Medium |

### 3.3 Rủi ro cụ thể

> [!CAUTION]
> **R1 — Overclaim risk:** EX entries ở confidence 0.32-0.70. Nếu promote vào core Phase 3 (hiện toàn 0.90 source_analogue), reader có thể hiểu nhầm tất cả đều có cùng authority level.

> [!WARNING]
> **R2 — Threshold instability:** v1.7 đã nâng threshold từ 3.5→4.0, khiến 3 entries bị reclassify. Nếu tương lai nâng tiếp → phải reclassify lại trong core.

> [!WARNING]
> **R3 — Direction ambiguity:** EX dùng BE→VVV direction. Core Phase 3 dùng VVV→BE direction (source_analogue). Promotion cần direction normalization.

### 3.4 Decision Framework

```
                     ┌─────────────────────┐
                     │  EX → Core          │
                     │  Promotion Gate     │
                     └─────────┬───────────┘
                               │
               ┌───────────────┴───────────────┐
               │                               │
        ┌──────┴──────┐                 ┌──────┴──────┐
        │  Option 1   │                 │  Option 2   │
        │  FULL MERGE │                 │  SELECTIVE  │
        │  64 entries │                 │  PROMOTION  │
        └──────┬──────┘                 └──────┬──────┘
               │                               │
   ┌───────────┴───────────┐       ┌───────────┴───────────┐
   │ Pro: Complete          │       │ Pro: Quality control   │
   │ Con: Threshold risk    │       │ Con: Partial coverage  │
   │ Con: Schema change     │       │ Pro: Only high-conf    │
   │ Score: 2.5/5           │       │ Score: 4.0/5           │
   └───────────────────────┘       └───────────────────────┘

                               │
                        ┌──────┴──────┐
                        │  Option 3   │
                        │  KEEP EX    │
                        │  AS-IS      │
                        └──────┬──────┘
                               │
                   ┌───────────┴───────────┐
                   │ Pro: No risk           │
                   │ Pro: Core stays clean  │
                   │ Con: 2 registries      │
                   │ Score: 3.5/5           │
                   └───────────────────────┘
```

---

## 4. Recommended Expansion Strategy

### Phase-by-phase (không phải all-at-once)

| Priority | Hướng | Action | Risk | Gating |
|:--------:|-------|--------|:----:|--------|
| 1️⃣ | **B** (Edges nội bộ) | Phát hiện + encode implicit relations giữa 55 nodes hiện có | 🟢 Low | Self-contained; no frozen file touched |
| 2️⃣ | **C** (Bridge expansion) | Convert ~15-20 Phase 2 edges thành bridge form | 🟢 Low | `bridge_QM_standard_to_VVV_QMRF.md` §8 rule |
| 3️⃣ | **D** (EX selective) | Promote chỉ entries confidence ≥ 0.70 + type `source_analogue` | 🟡 Med | Needs core unfreeze + schema update |
| 4️⃣ | **A** (New nodes) | Mở BIAN-20 + scan 2-3 QM topics mới | 🟡 Med | Needs BIAN gap analysis |
| 5️⃣ | **E** (New categories) | Chỉ khi có strong BIAN gap + đủ QM substrate | 🔴 High | Full RCA cycle per category |

### EX Promotion: Option 2 (Selective) là tốt nhất

Selective promotion = chỉ promote entries thỏa **tất cả** điều kiện:

| Criterion | Threshold |
|-----------|-----------|
| Confidence | ≥ 0.70 |
| Type | `reference_copy` (source_analogue) hoặc `expert_manual_mapping` |
| Status | Active (not FOLDED, not RECLASSIFIED) |
| Direction | Phải normalize sang VVV→BE |

Estimate: **~36 reference_copy (hiện 34 active) + ~5-6 expert entries = ~40 entries** pass filter.

---

## 5. Tóm tắt 1 bảng

| Câu hỏi | Trả lời |
|---------|---------|
| Core còn mở rộng được? | ✅ **Có** — theo 5 hướng |
| Hướng nào an toàn nhất? | **B** (thêm edges nội bộ) → **C** (bridge expansion) |
| Hướng nào impactful nhất? | **D** (EX promotion selective) — tăng BE coverage 5.7%→~15% |
| Hướng nào rủi ro nhất? | **E** (new categories) — full RCA cycle mỗi category |
| EX → Core: Full merge? | ❌ Không khuyến nghị — threshold instability + overclaim risk |
| EX → Core: Selective? | ✅ Khuyến nghị — chỉ conf ≥ 0.70, type validated |
| EX → Core: Keep as-is? | 🆗 Acceptable — nếu chưa sẵn sàng cho core unfreeze |
