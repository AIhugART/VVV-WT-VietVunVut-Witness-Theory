Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# RCA — Tại sao [A-E3] đang là TOP 1? (Full AHP Pipeline Analysis)

**Date:** 2026-05-24
**Method:** Full Anti-Hallucination Pipeline (9-file) + 5-Whys RCA x scoring threshold 4/5
**Scope:** VVV-QMRF, VVV-QMRF-EX as compass
**Reference verdict:** `RCA_A_E3_beta_universal_final_verdict.md` (commit `897028b`, 3-Round RCA 3.75/5)

---

## Executive Summary

> **[A-E3] đang là #1 vì STALE DATA — Top 10 v1.1 được xây dựng TRƯỚC KHI RCA A-E3 Final Verdict được áp dụng.**
>
> Verdict đó (commit `897028b`) đã RECLASSIFY [A-E3] từ "assumption" → "FREE PARAMETER (MEASUREMENT TARGET)". Khi reclassify, H score giảm từ 5→2, Risk Score giảm từ 22.5→6.0 — [A-E3] KHÔNG CÒN trong Top 10.
>
> **Root cause:** Documentation cascade (Appendix A của verdict) chưa được thực thi đầy đủ — `anti_hallucinations/00_top_10_hallucinations_record.md` chưa được cập nhật.

---

## 1. Full AHP Pipeline — Truy vết [A-E3]

### Step 1 — 01_early_warning.md: Signal Scan

| Signal ID | Signal | Match? | Explanation |
|-----------|--------|--------|-------------|
| R1 | Category error | **NO** | β là free parameter, không claim là physical explanation |
| R3 | Contradiction with known fact | **NO** | β không mâu thuẫn với QM — nó là extension parameter |
| O3 | Assumption not flagged | **YES (historical)** | Trước reclassification: [A-E3] bị coi là assumption. Sau verdict: đã reclassify. |
| O4 | Weak anchor | **YES (historical)** | Trước: 1 SOT (WEAK). Sau: FREE PARAMETER không cần anchor kiểu assumption. |
| Y1 | Ambiguous boundary language | **YES** | "β universal" claim cần caveat: "modeling choice, cross-experiment pending" |
| Y5 | BE lineage not documented | **YES** | β không có BE lineage — nhưng không cần vì là measurement parameter |

**Kết luận:** [A-E3] trigger O3 + O4 (historical) + Y1 (documentation). Không trigger RED signals nào.

### Step 2 — 02_detection.md: Component Classification

**Phân loại gốc (trước verdict):** Nhóm C — New, flagged assumption, có EX anchor.
**Phân loại đúng (sau verdict):** **FREE PARAMETER** — không thuộc 4 nhóm nào. Cần thêm "Nhóm P: Measurement Parameters."

| Thuộc tính | Trước verdict | Sau verdict |
|------------|---------------|-------------|
| Nhóm | C (New — flagged assumption) | **P (Free Parameter — measurement target)** |
| Sinh ra từ đâu? | Class C | Class C |
| Cần anchor không? | Có (WEAK: N_QM_VVV_00031) | Không (parameter được ĐO, không derive) |
| Cần flag assumption không? | Có ([A-E3]) | Không (reclassified: FREE PARAMETER) |

### Step 3 — 03_sot_traceability.md: Trace Score

**Trước verdict:** Trace score = 1/6 (chỉ SOT-4: CLAUDE.md).
**Sau verdict:** Trace score không áp dụng cho free parameter. β được xác minh qua MEASUREMENT (Proietti D1: β=0.598), không qua SOT trace.

### Step 4 — 04_analysis.md: 5-Whys RCA

```
W1: Tại sao [A-E3] đang là #1 trong Top 10?
  → Vì Risk Score = 22.5 — cao nhất toàn VVV-QMRF.

W2: Tại sao Risk Score = 22.5?
  → Vì H=5 (Vàng — speculative), W=3 (beta ảnh hưởng toàn K9_E), A=0.5 (WEAK anchor).
    Công thức: 5 × 3 × 1.5 = 22.5.

W3: Tại sao H=5, A=0.5?
  → Vì Top 10 v1.1 vẫn phân loại [A-E3] là "assumption" với anchor WEAK.
    Điều này đến từ origin investigation — nơi [A-E3] được chấm hallucination 5/10.

W4: Tại sao Top 10 chưa cập nhật sau RCA A-E3 Final Verdict?
  → Vì Top 10 v1.0 được tạo TRƯỚC KHI verdict được áp dụng.
    Top 10 v1.1 chỉ cập nhật T5 K_ctx (do T9) — không audit [A-E3].
    Documentation cascade (Appendix A của verdict) chưa đến file này.

W5: ROOT CAUSE — Tại sao [A-E3] vẫn #1?
  → STALE DATA + INCOMPLETE DOCUMENTATION CASCADE.
    RCA A-E3 Final Verdict (commit 897028b) đã RECLASSIFY [A-E3] từ
    "assumption" → "FREE PARAMETER (MEASUREMENT TARGET)", nhưng:
    (a) anti_hallucinations/ files được tạo SAU verdict — không reflect verdict
    (b) Top 10 ranking formula giả định mọi component là "assumption" — không
        có cơ chế phân biệt FREE PARAMETER
    (c) Không ai re-audit Top 10 sau khi verdict được commit

ROOT CAUSE (1 câu):
  Top 10 ranking không reflect RCA A-E3 Final Verdict vì AHP được tạo
  sau verdict và documentation cascade chưa đến các file AHP.
```

### Step 5 — 05_scoring.md: Re-score [A-E3]

**Trước verdict (as "assumption"):**

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| H (hallucination) | 5/10 | Speculative, flagged, WEAK anchor |
| W (structural weight) | 3 | Beta ảnh hưởng toàn K9_E |
| A (anchor penalty) | 0.5 | 1 SOT, conceptual only |
| **Risk** | **22.5** | CRITICAL |

**Sau verdict (as "FREE PARAMETER"):**

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| H (hallucination) | **2/10** | β là genuine free parameter — giống coupling constants trong vật lý. Được ĐO (β=0.598 từ Proietti D1). "Universal" là modeling choice (Occam), không phải hallucination. |
| W (structural weight) | 3 | Không đổi — β vẫn là core parameter của K9_E |
| A (anchor penalty) | **0** | FREE PARAMETER không cần anchor kiểu assumption. "Anchor" của β là MEASUREMENT (Proietti D1), mạnh hơn mọi SOT trace. |
| **Risk** | **6.0** | LOW — không vào Top 10 |

**Reclassification impact:**

```
Trước: [A-E3] = assumption → H=5, A=0.5 → Risk = 22.5 → #1 CRITICAL
Sau:  [A-E3] = FREE PARAMETER → H=2, A=0 → Risk = 6.0 → ngoài Top 10
```

### Step 6 — label_system.md: Re-label

| Label | Trước | Sau | Lý do |
|-------|-------|-----|-------|
| Primary | `[AH-WARN]` | `[AH-OK]` | H=5→2, từ Vàng xuống Xanh lá |
| Risk Score | `[RS-CRIT]` | `[RS-LOW]` | Risk 22.5→6.0 |
| Secondary | `[AH-EX] [AH-WEAK]` | `[AH-EX]` | A=0.5→0 (free parameter), giữ EX flag |
| **Full** | `[AH-WARN] [RS-CRIT] [AH-EX] [AH-WEAK]` | `[AH-OK] [RS-LOW] [AH-EX]` | |

### Step 7 — 06_solution.md: Solution

| Thuộc tính | Trước | Sau |
|------------|-------|-----|
| Solution type | ANCHOR (tìm experimental motivation) | **DOCUMENT** (caveat về modeling choice) |
| Priority | P2 (MEDIUM) | **P4 (ONGOING)** |
| Status | OPEN | **RECLASSIFIED** |

---

## 2. Top 10 Impact — [A-E3] Removal

### Current Top 10 (v1.1) → New Top 10 (v1.2)

| v1.1 Rank | Component | v1.1 Risk | Action | v1.2 Rank |
|-----------|-----------|-----------|--------|-----------|
| #1 | [A-E3] beta universal | 22.5 | **REMOVED** (reclassified: FREE PARAMETER) | — |
| #2 | phi-map K→B(H) | 18.0 | → new #1 | **#1** |
| #3 | P10-NOISE | 18.0 | → new #2 | **#2** |
| #4 | T5 K_ctx | 18.0 | → new #3 | **#3** |
| #5 | T4-H Steps 3-4 | 18.0 | → new #4 | **#4** |
| #6 | K9E-PAT | 12.0 | → new #5 | **#5** |
| #7 | K9_E 2 implementations | 12.0 | → new #6 | **#6** |
| #8 | K5_prospective | 12.0 | → new #7 | **#7** |
| #9 | E1-E16 postulates | 9.6 | → new #8 | **#8** |
| #10 | P10-TIM N0 omitted | 9.0 | → new #9 | **#9** |
| — | (new entry) | — | **Thêm** | **#10** |

### New #10 Candidate — cần 3-Round RCA

Pool ứng viên thay thế:

| Candidate | H | W | A | Risk | Rationale |
|-----------|---|---|---|--------|-----------|
| D2 — Phase9 stale assumptions | 3 | 1 | 0.2 | 3.6 | Đã fix trong tech debt |
| D14 — D-T4-BYPASS status | 3 | 1 | 0.2 | 3.6 | Đã update "PROPOSED"→"APPLIED" |
| BE↔QM cross-domain mapping | 4 | 2 | 0.2 | 9.6 | Risk category error trong mapping files |
| K9_E numerical stability | 3 | 2 | 0.2 | 7.2 | Numerical prediction tại beta cao |
| Peer-sync mechanism failure risk | 3 | 2 | 0.2 | 7.2 | Nếu peer-sync fails, K-Space copies drift |

**Chọn: BE↔QM cross-domain mapping (H=4, W=2, A=0.2, Risk=9.6)**

Đây là rủi ro tiềm ẩn: các mapping file (`refine_mapping.md`, `system_mapping.md`) chứa cross-domain links giữa BE concepts và QM concepts. Nếu không có boundary statement rõ ràng, đây là Type 1 Category Error.

---

## 3. 3-Round RCA Verification

| Round | Focus | Score | Findings |
|-------|-------|-------|----------|
| R1 | [A-E3] reclassification — is the RCA A-E3 Final Verdict binding? | 5/5 | Verdict đã được commit (`897028b`), 3-round RCA, quyết định dứt khoát. AHP phải reflect verdict. |
| R2 | H score re-evaluation — is H=2 correct for FREE PARAMETER? | 4.5/5 | β như coupling constant: H=2 (Xanh lá — genuine parameter, measured). "Universal" modeling choice cần caveat documentation — không ảnh hưởng H score. |
| R3 | Top 10 removal impact — does removing [A-E3] break ranking? | 5/5 | Không. [A-E3] removal khiến mọi component khác tăng 1 hạng. Phi-map (#2→#1) xứng đáng: H=6 cao nhất. Thêm BE↔QM mapping (#10) hợp lý: category error risk. |
| **Aggregate** | | **4.83/5** PASS (>= 4/5) | |

---

## 4. Documentation Cascade Status

Từ Appendix A của RCA A-E3 Final Verdict:

| # | File | Status |
|---|------|--------|
| 1 | `project_vvv_qmrf_class_c/index.md` | ✅ Đã cập nhật (commit `897028b`) |
| 2 | `Phase8_candidate_equation.md` | ✅ Đã cập nhật |
| 3 | `Phase9_adversarial_testing.md` | ✅ Đã cập nhật |
| 4 | `Phase13_honest_assessment.md` | ✅ Đã cập nhật |
| 5 | `Phase11_3observer_prediction.md` | ✅ Đã cập nhật |
| 6 | `K_Space_Axiomatization.md` (Class C) | ⚠️ Cần verify |
| 7 | `meta_architecture/K_Space_Axiomatization.md` | ⚠️ Cần PEER-SYNC |
| 8 | `rca_technical_debt_inventory_2026_05_24.md` | ⚠️ D3 cần đánh dấu RESOLVED |
| **9** | **`anti_hallucinations/00_top_10_hallucinations_record.md`** | **❌ CHƯA CẬP NHẬT — ĐÂY LÀ BUG NÀY** |
| **10** | **`anti_hallucinations/label_system.md`** | **❌ CHƯA CẬP NHẬT** |
| **11** | **`anti_hallucinations/RCA_FINAL_VERDICT_*.md`** | **❌ CHƯA CẬP NHẬT** |

---

## 5. Final Verdict

> **[A-E3] đang là #1 vì STALE DATA — AHP được tạo SAU RCA verdict nhưng không reflect verdict đó.**
>
> RCA A-E3 Final Verdict (commit `897028b`) đã quyết định: [A-E3] = FREE PARAMETER (MEASUREMENT TARGET), không còn là assumption. H score thực tế = 2/10 (Xanh lá), Risk = 6.0 (LOW), ngoài Top 10.
>
> **Hành động:** (1) Remove [A-E3] khỏi Top 10. (2) Thêm β vào "Free Parameter Registry" mới. (3) Re-rank Top 10 — phi-map thành #1. (4) Thêm BE↔QM cross-domain mapping làm #10 mới. (5) Cập nhật label_system.md.

---

*RCA: Why [A-E3] is #1 — 2026-05-24. Full AHP pipeline. Root cause: STALE DATA + incomplete documentation cascade. 3-Round RCA: 4.83/5.*
