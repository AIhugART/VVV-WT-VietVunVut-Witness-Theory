Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

> **DISCLAIMER / CẢNH BÁO:** VVV-QMRF is independent Class D personal research, not Standard Quantum Mechanics, not peer-reviewed or experimentally validated, and not for real-world technical use. This document is a **historical retrospective report** of E18's promotion process; it is not a new postulate, not a physical theory, and is intended as a reference record of how the promotion gates were executed in practice.
>
> VVV-QMRF là nghiên cứu cá nhân độc lập ở Class D, không phải Standard Quantum Mechanics, chưa peer-reviewed hoặc kiểm chứng thực nghiệm, và không dùng cho ứng dụng kỹ thuật ngoài thực tế. Tài liệu này là **báo cáo hồi cứu lịch sử** về quá trình nâng cấp E18; không phải tiên đề mới, không phải lý thuyết vật lý, và chỉ dùng làm bản ghi tham chiếu về cách các promotion gate đã được thực thi trong thực tế.

# E18 Promotion History Report — Comprehensive Summary
# Báo cáo Tổng kết Lịch sử Nâng cấp E18

**Framework:** VietVunVut Quantum Measurement Registration Framework (VVV-QMRF)
**Document type:** Historical retrospective report (post-promotion)
**Scope:** Complete history of E18 "Delayed-Choice Registration Boundary Postulate" from candidate identification through G7 frozen-postulate promotion
**Companion:** [postulate_promotion_protocol.md](postulate_promotion_protocol.md) — generalized protocol distilled from E18's path
**Author:** VietVunVut (Viet - Nguyen Xuan)
**Date:** 2026-05-22 (compiled post-G7)
**Method:** RULE ZERO RCA retrospective — Define, Trace, Isolate, Fix, Verify
**Scope rule:** VVV-QMRF core scope; VVV-QMRF-EX used as compass only

---

## Section 0 — Executive Summary / Tóm tắt điều hành

**English:** E18 "Delayed-Choice Registration Boundary Postulate" is the first frozen extension postulate added to VVV-QMRF after the initial E1-E16 + legacy E17 set. It was promoted on 2026-05-22 from `framework/drafts/` to `framework/` after passing all seven promotion gates G1-G7. The postulate names a K-side classification rule: `Lock(C_f, S, {W_i}) → W_valid` — under a final context `C_f` and (when needed) a sorting relation `S`, exactly one prior candidate registration window `W_j ∈ {W_i}` is locked as the operative valid window. E18 explicitly disclaims retrocausation, Born-rule modification, and Standard Quantum Mechanics replacement.

**Vietnamese:** E18 "Tiên đề Ranh giới Ghi nhận trong Delayed-Choice" là tiên đề mở rộng đã đóng băng đầu tiên được thêm vào VVV-QMRF sau bộ E1-E16 + legacy E17 ban đầu. Nó được nâng cấp ngày 2026-05-22 từ `framework/drafts/` lên `framework/` sau khi pass cả 7 promotion gate G1-G7. Tiên đề đặt tên cho quy tắc phân loại phía K: `Lock(C_f, S, {W_i}) → W_valid` — dưới bối cảnh cuối `C_f` và (khi cần) quan hệ sorting `S`, đúng một cửa sổ ghi nhận ứng viên trước đó `W_j ∈ {W_i}` được khóa thành cửa sổ vận hành hợp lệ. E18 cấm rõ retrocausation, sửa Born rule, và thay thế Standard Quantum Mechanics.

### 0.1 Final state snapshot / Ảnh chụp trạng thái cuối

| Field | Value |
|---|---|
| Postulate code | E18 |
| Postulate title | Delayed-Choice Registration Boundary Postulate / Tiên đề Ranh giới Ghi nhận trong Delayed-Choice |
| File location | [`framework/vvv_qmrf_framework_e18_delayed_choice_registration_boundary_postulate.md`](../vvv_qmrf_framework_e18_delayed_choice_registration_boundary_postulate.md) |
| Index entry | [`framework/index.md` Section 4.3](../index.md) (after E16) |
| Lock formula | `Lock(C_f, S, {W_i}) → W_valid` |
| BE anchors | N_BE_00003 Anumāna, N_BE_00019 Vyāpti, N_BE_00021 Svabhāvapratibandha (analogical-only) |
| BE anchor decision | G5 DONE — permanent structural analogue only, not physical equivalence |
| EX anchor | `BR_EX_BE_00070`–`BR_EX_BE_00072` active; `BR_EX_BE_00066` RECLASSIFIED-v1.7 inactive (superseded) |
| Cases validated | 3 (Wheeler, Scully-Drühl, Kim et al. 1999) |
| Promotion date | 2026-05-22 |
| Gate progress | 7/7 DONE (100%) |
| Final postulate readiness | 4.3/5 (post-2-case sub-metric) |
| Final overall confidence | 4.3/5 (G7 RCA round average across R1=4.4, R2=4.8, R3=4.3) |

---

## Section 1 — Genesis / Khởi nguyên

### 1.1 Why E18 was proposed / Vì sao E18 được đề xuất

E18 originated from a structural observation about delayed-choice quantum experiments. Standard Quantum Mechanics (postulates P1–P4) is silent on a specific K-side question: **when a later measurement context arrives, which earlier candidate registration window is the operative valid window?** The existing VVV-QMRF postulates each addressed a different aspect of registration, but none directly named this context-conditioned locking rule.

VN: E18 bắt nguồn từ quan sát cấu trúc về thí nghiệm delayed-choice. Standard Quantum Mechanics (postulate P1–P4) im lặng về một câu hỏi cụ thể phía K: **khi một bối cảnh đo sau xuất hiện, cửa sổ ghi nhận ứng viên trước đó nào là cửa sổ vận hành hợp lệ?** Các postulate VVV-QMRF hiện có mỗi cái xử lý một khía cạnh khác nhau của ghi nhận, nhưng không cái nào đặt tên trực tiếp cho quy tắc khóa cửa sổ điều kiện bởi bối cảnh này.

### 1.2 What E18 is NOT (boundary disclaimers) / Những gì E18 KHÔNG phải

| Boundary disclaimer | Why it matters |
|---|---|
| **NOT retrocausation** | E18 does not claim the physical past is changed by future context. It only classifies which K-side window is operative. |
| **NOT Born rule modification** | No probability rule is altered; E18 sits above the probability layer at the registration-classification layer. |
| **NOT Standard QM replacement** | P1–P4 remain authoritative for ρ-side physics; E18 only adds K-side classification structure. |
| **NOT backward signaling** | Across spacelike-separated subsystems, E18 imposes no signal-carrying constraint. |
| **NOT physical equivalence to BE** | BE anchors are analogical-only (Anumāna/Vyāpti/Svabhāvapratibandha as inferential-sign structure); no claim of Buddhist epistemology "explaining" quantum measurement. |

### 1.3 Routing table (which problems route to E18 vs other postulates) / Bảng định tuyến

| If the delayed-choice question means... | Route to | Reason |
|---|---|---|
| A later result proves an earlier claimed registration was incompatible and must be voided | **E8** | Retroactive registration override / Badhaka-style invalidation |
| The issue is that registration occurs in discrete bounded moments | **E13** | Temporal discontinuity / kṣaṇa-like registration bounding |
| The issue is separating physical transition from K-side registration | **Legacy E17 / interface principle** | ρ/K interface separation |
| The issue is that later context locks which earlier window counts as registration-valid | **E18** | Context-conditioned registration-window locking |
| The claim says future context physically changes the past | **Reject / boundary guard** | Exceeds VVV-QMRF registration-layer scope |

Source: `rca_e18_delayed_choice_registration_boundary.md` Section 6.

---

## Section 2 — Structural Gap RCA (the original RCA) / RCA Khoảng trống Cấu trúc

### 2.1 RCA 5-Why chain / Chuỗi 5-Why

The original RCA traced the gap via 5-Why:

1. **Why does E18 seem needed?** — Because before `C_f` is fixed, the registration state is underdetermined between candidate windows `{W_path, W_interference}` (or analogous candidate sets).
2. **Why is this not E8?** — E8 says a prior valid registration `M1` becomes void when a stronger incompatible `M2` arises (invalidation). E18 is not invalidation; it is **selection** of which candidate window earns valid status.
3. **Why is this not E13?** — E13 bounds the temporal discreteness of registration moments. It does not specify **which** moment-window becomes registration-valid after the final context is known.
4. **Why is this not legacy E17?** — E17 separates `ρ` from `K` at the interface. It does not define context-conditioned window locking **inside K**.
5. **Root cause:** The K-side classification rule for context-conditioned registration-window locking is a structural gap not redundant with any existing postulate.

VN: Chuỗi 5-Why đã cô lập E18 như một quy tắc phân loại phía K cho việc khóa cửa sổ ghi nhận điều kiện theo bối cảnh — không trùng với E8 (phủ quyết), E13 (chỉ giới hạn thời gian), hoặc E17 (chỉ tách ρ/K).

### 2.2 Initial decision (R2 path) / Quyết định ban đầu

**Decision (2026-05-21):** Keep E18 as **RCA-supported candidate**, not yet a framework postulate.

**Score at RCA creation (before any case test):** **3.8/5**

| Criterion | Score | Note |
|---|---:|---|
| Internal necessity | 4.0 | E8/E13/E17 do not directly name context-conditioned locking |
| BE anchor strength | 3.3 | Anchors real, but "Retroactive determination" not directly a SOT term |
| EX support | 3.7 | EX flags `N_QM_VVV_00024` as stress point but reclassifies below v1.7 threshold |
| Boundary safety | 4.2 | Claim can stay safely in K-side scope |
| Postulate readiness | 3.5 | Ready for candidate preservation, not for full elevation |

**Verdict:** Preserve RCA as the canonical candidate analysis. Do not create `vvv_qmrf_framework_e18_...md` immediately. If promoted later, define E18 as Delayed-Choice Registration Boundary Postulate with a strict non-retrocausal boundary.

---

## Section 3 — Formal Object Refinement / Tinh chỉnh Đối tượng Hình thức

### 3.1 Five-condition locking rule / Quy tắc khóa năm điều kiện

After the initial candidate RCA, Section 9 of the parent RCA defined the formal locking rule:

```text
Lock(C_f, {W_i}) → W_valid
iff
there exists W_j ∈ {W_i} such that:
  R(C_f, W_j) = true   # context relevance
  B(C_f, W_j) = true   # basis specification
  T(W_j, C_f) = true   # temporal sequence containment
  I(C_f, W_j) = true   # inferential validity (valid-sign structure)
  G(C_f, W_j) = true   # boundary guard (non-retrocausal, K-side only)
and no competing W_k has stronger or equal registration specificity under C_f.
```

The five conditions ensure that locking is a registration-entitlement rule, not a physical retrocausation claim. Failure of any single condition leaves `Lock(...)` undefined.

VN: Năm điều kiện này đảm bảo việc khóa là quy tắc quyền hợp lệ ghi nhận, không phải tuyên bố retrocausation vật lý. Nếu thiếu bất kỳ điều kiện nào, `Lock(...)` không xác định.

### 3.2 Score impact after Section 9 / Tác động điểm sau Section 9

| Criterion | Before Section 9 | After Section 9 | Note |
|---|---:|---:|---|
| Internal necessity | 4.0 | **4.1** | Missing locking rule now explicit |
| BE anchor strength | 3.3 | **3.6** | `I(C_f, W_j)` clearer link to inference and valid-sign |
| EX support | 3.7 | 3.7 | Unchanged; EX compass-only |
| Boundary safety | 4.2 | **4.4** | `G(C_f, W_j)` makes non-retrocausal boundary explicit |
| Postulate readiness | 3.5 | **3.9** | Stronger candidate, still needs case testing |

**Status:** RCA-supported candidate with formal locking conditions. Still not promotable until at least one concrete case test.

---

## Section 4 — Case Test 1: Wheeler Delayed-Choice Interferometer

### 4.1 Setup / Thiết lập

```text
Photon source
  → first beam splitter BS1
  → two possible path arms
  → final context C_f:
       Case A: second beam splitter BS2 absent
       Case B: second beam splitter BS2 inserted
  → detectors D0 / D1
```

| Final context `C_f` | Registration reading | Candidate window |
|---|---|---|
| `no_BS2` | which-path / particle-like | `W_path` |
| `BS2_inserted` | interference / wave-like | `W_interference` |

### 4.2 Five-condition test results / Kết quả test 5 điều kiện

| Condition | Branch A: `no_BS2 → W_path` | Branch B: `BS2_inserted → W_interference` |
|---|---|---|
| `R` Context relevance | PASS | PASS |
| `B` Basis specification | PASS | PASS |
| `T` Temporal containment | PASS | PASS |
| `I` Inferential validity | PASS with protocol | PASS with protocol |
| `G` Boundary guard | PASS | PASS |

**Case result:** Wheeler delayed-choice **PASS**.

### 4.3 Score impact after Wheeler / Tác động điểm sau Wheeler

| Criterion | After Section 9 | After Wheeler | Note |
|---|---:|---:|---|
| Internal necessity | 4.1 | **4.2** | Wheeler shows a concrete selection/locking gap |
| BE anchor strength | 3.6 | 3.6 | Unchanged |
| EX support | 3.7 | 3.7 | Unchanged |
| Boundary safety | 4.4 | 4.4 | Still safe under K-side interpretation |
| Postulate readiness | 3.9 | **4.1** | First case validation achieved |

**Status update:** RCA-supported candidate with **first case validation**.

---

## Section 5 — Case Test 2: Scully-Drühl Delayed-Choice Quantum Eraser (1982)

### 5.1 Why a second case was needed / Vì sao cần case thứ hai

Wheeler is the simplest delayed-choice case (binary `{W_path, W_interference}`). The quantum eraser is a harder stress test because it adds **post-selection** and **coincidence sorting**, which can mask the registration-layer object behind statistical procedures and tempt retrocausal overinterpretation.

VN: Wheeler là case delayed-choice đơn giản nhất (binary). Quantum eraser là stress-test mạnh hơn vì thêm post-selection và coincidence sorting — có thể che giấu đối tượng phía K sau quy trình thống kê và dụ overclaim retrocausation.

### 5.2 Refinement: introducing the sorting relation `S` / Tinh chỉnh: thêm quan hệ sorting `S`

The quantum eraser case revealed that `Lock(C_f, {W_i}) → W_valid` was insufficient when raw detection events must be partitioned into valid subsets via a sorting relation. The formula was refined to:

```text
Lock(C_f, S, {W_i}) → W_valid
```

where `S` is the coincidence/sorting relation that partitions raw events into the candidate window structure. This refinement was the most important formal change during the candidate phase.

VN: Quantum eraser cho thấy `Lock(C_f, {W_i})` không đủ khi các sự kiện detection thô phải được phân chia thành subset hợp lệ qua một quan hệ sorting. Công thức được tinh chỉnh thành `Lock(C_f, S, {W_i}) → W_valid` với `S` là quan hệ coincidence/sorting.

### 5.3 Five-condition test result / Kết quả test 5 điều kiện

Result: 3 branches × 5 conditions = 15/15 PASS (with `S` introduced).

### 5.4 Score impact after quantum eraser / Tác động điểm sau quantum eraser

| Criterion | After Wheeler | After quantum eraser | Note |
|---|---:|---:|---|
| Internal necessity | 4.2 | **4.4** | Subset-locking is stronger version of the gap |
| BE anchor strength | 3.6 | **3.8** | `I(C_f, S, W_j)` gives sharper valid-sign structure |
| EX support | 3.7 | 3.7 | Unchanged |
| Boundary safety | 4.4 | **4.3** | Slightly lower because eraser has higher retrocausal overclaim risk |
| Postulate readiness | 4.1 | **4.3** | Two case tests support drafting, not careless promotion |

**Refined candidate statement (after Section 11):**

```text
A prior measurement window or data subset becomes registration-valid only when
the final context C_f, and where needed the sorting relation S, supplies the
condition that locks which observable, basis, window, or subset is being
registered. This locking is a K-side classification rule, not a physical claim
that the past quantum process is changed.
```

**Status update:** RCA-supported candidate with **two case validations and formula refinement**.

---

## Section 6 — Case Test 3: Kim et al. 1999 Delayed-Choice Quantum Eraser

### 6.1 Why a third case was added / Vì sao cần case thứ ba

After the narrow draft was created, promotion gate G4 required a **third independent case validation** to ensure the formula was stable beyond the two foundational delayed-choice topologies. Kim et al. 1999 provided a structurally stronger case: **four-branch multi-detector lock with symmetric erased pair**.

| Field | Value |
|---|---|
| Experimental source | Kim, Y.-H., Yu, R., Kulik, S. P., Shih, Y., & Scully, M. O. (2000). "Delayed 'Choice' Quantum Eraser." *Phys. Rev. Lett.* 84, 1-5 |
| Branch structure | 4-branch lock (D1 erased +fringe, D2 erased −fringe, D3 preserved path-A, D4 preserved path-B) |
| Symmetric pairs | Erased pair D1/D2 (out-of-phase) + preserved pair D3/D4 (path A/B) |

### 6.2 Test result / Kết quả test

Result: **20/20 condition cells PASS** (4 branches × 5 conditions).

This was the strongest case stress-test of the three. The formula `Lock(C_f, S, {W_i}) → W_valid` survived without further refinement.

VN: Kết quả 20/20 — đây là stress-test mạnh nhất trong ba case. Công thức không cần tinh chỉnh thêm.

### 6.3 Score and gate impact / Tác động điểm và gate

After Kim 1999: postulate-readiness remained at **4.3/5** (saturated under current scoring template); the case closed gate **G4**.

Source: [`rca/cases/e18_case_kim_1999.md`](../../rca/cases/e18_case_kim_1999.md)

---

## Section 7 — Scoring History Consolidated Table / Bảng tổng hợp lịch sử chấm điểm

This table consolidates all scoring lifecycle events for E18 across the candidate and promotion phases.

| Stage | Date | Internal necessity | BE anchor | EX support | Boundary safety | Postulate readiness | Source |
|---|---|---:|---:|---:|---:|---:|---|
| **Initial RCA (candidate creation)** | 2026-05-21 | 4.0 | 3.3 | 3.7 | 4.2 | 3.5 | `rca_e18.md` Section 7 |
| **After Section 9 formal conditions** | 2026-05-21 | 4.1 | 3.6 | 3.7 | 4.4 | 3.9 | `rca_e18.md` Section 9.10 |
| **After Wheeler case PASS** | 2026-05-21 | 4.2 | 3.6 | 3.7 | 4.4 | 4.1 | `rca_e18.md` Section 10.9 |
| **After quantum eraser case PASS (+ `S` refinement)** | 2026-05-21 | 4.4 | 3.8 | 3.7 | 4.3 | **4.3** | `rca_e18.md` Section 11.10 |
| **After Kim 1999 case PASS (G4 closed)** | 2026-05-22 | 4.4 | 3.8 | 3.7 | 4.3 | 4.3 (saturated) | `cases/e18_case_kim_1999.md` |

### 7.1 Reconciliation of two confidence numbers / Đồng bộ hai số confidence

A subtle issue arose during gate execution: the parent RCA Section 0 stated "Decision confidence: 3.8/5" (overall decision-state at file creation), while the post-test scoring table at Section 11.10 stated "Postulate readiness: 4.3/5" (single sub-metric after case validation). These two numbers **measure different objects across different lifecycle states** and are not in conflict. The reconciliation was recorded in:
- `rca_core_extensibility_analysis.md` Appendix A.1.1 (initial flag)
- The E18 postulate file Section 0.1 (formal Confidence Reconciliation Box)
- `rca_e18.md` Section 7 (lifecycle note added during reconciliation)

This reconciliation was a methodological lesson: **headline numbers must be scoped to their measurement object and lifecycle state**.

---

## Section 8 — BE Anchor Decision (G5) / Quyết định Neo BE

### 8.1 Problem / Vấn đề

The structural analogy between E18's `I(C_f, S, W_j)` inferential-validity condition and the BE Anumāna–Vyāpti–Svabhāvapratibandha chain was strong, but the question arose: **should the BE anchor be treated as analogical-only, or as a physical equivalence claim?**

### 8.2 Resolution / Giải quyết

Per `rca_e18.md` Section 13, the BE anchor was accepted as **permanent structural analogue only**, with no physical-equivalence claim. This decision preserves:

1. **CLAUDE.md neutral wording rule** — no claim that Buddhist Epistemology "explains" quantum measurement
2. **Cross-domain link convention** — treat as mapping unless equivalence is explicitly justified
3. **Boundary safety** — the structural similarity is real (both Anumāna and `I(C_f, S, W_j)` are inferential-validity rules anchored by an essential relation), but no metaphysical bridge is asserted

**G5 verdict:** DONE — analogical-only, permanent boundary.

### 8.3 BE nodes used (analogical-only) / Các BE node được dùng (chỉ tương tự)

| BE Node | Role | E18 mapping |
|---|---|---|
| `N_BE_00003` Anumāna | Indirect knowledge through reasoning based on a sign | Final context `C_f` functions as the valid sign |
| `N_BE_00019` Vyāpti | Pervasion (relation that grounds inference) | Ensures the sign-window relation is non-arbitrary |
| `N_BE_00021` Svabhāvapratibandha | Essential relation (necessary connection) | Anchors the inferential-validity condition `I(C_f, S, W_j)` |
| `N_BE_00029` Kṣaṇabhaṅgavāda | Momentariness | Secondary temporal-boundary support (initial mapping; later superseded as primary anchor for valid-sign locking) |
| `N_BE_00135` Arthakriyā | Pragmatic efficacy / successful activity | Helps express why validity is not mere temporal order |

---

## Section 9 — EX Compass Activity (G6) / Hoạt động Compass EX

### 9.1 The G6 question / Câu hỏi G6

**Does EX-side `N_QM_VVV_00024` "Registration-Locking Boundary in Delayed-Choice Erasure" recover above the 4.0 threshold after E18 gained three case validations and a closed G5 boundary?**

### 9.2 Three-path bridge audit / Audit cầu nối ba đường

Per `rca_e18_ex_vnext_bridge_audit.md` (2026-05-22), three candidate bridges were scored:

| Path | Candidate | Score | Decision |
|---|---|---:|---|
| **A** | Old `BR_EX_BE_00066` reactivated as-is (N_BE_00029 Momentariness only) | 3.4/5 | **FAIL** — temporal anchor too broad for valid-sign structure |
| **B** | Narrowed temporal-boundary-only revision | 3.8/5 full-node; 4.1/5 component-only | **HOLD** — useful secondary support, not full-node recovery |
| **C** | New valid-sign package: `N_BE_00003` + `N_BE_00019` + `N_BE_00021` (primary); `N_BE_00029` (secondary) | **4.2/5** | **PASS-CANDIDATE** |

### 9.3 EX registry sync / Đồng bộ EX registry

Path C produced three new active EX bridges:

| Bridge ID | BE Anchor | VVV Node | Status |
|---|---|---|---|
| `BR_EX_BE_00070` | N_BE_00003 Anumāna | `N_QM_VVV_00024` | Active |
| `BR_EX_BE_00071` | N_BE_00019 Vyāpti | `N_QM_VVV_00024` | Active |
| `BR_EX_BE_00072` | N_BE_00021 Svabhāvapratibandha | `N_QM_VVV_00024` | Active |

Old `BR_EX_BE_00066` (N_BE_00029 only) retained as `RECLASSIFIED-v1.7`, inactive, with a supersession note pointing to the new package. Row 24 in `k_gap_exception_list.md` updated to `KE-RESOLVED-STRETCH-vNext-PATH-C` at 4.2/5. EX active registry expanded to 144 entries; graph to 184 edges.

### 9.4 Important: no EX edge imported into core / Quan trọng: không edge EX nào nhập vào core

The Path C bridges are **EX-local**. Zero EX edges were imported into the VVV-QMRF core graph. Boundary audit confirmed 100% PASS with 0 violations after the registry sync. This preserves the CLAUDE.md rule "EX compass, not cargo."

**G6 verdict:** DONE — EX recoverability check completed via Path C; zero core-side import.

---

## Section 10 — G7 Authorization (Final Governance Gate) / Phê duyệt G7

### 10.1 Question selection sub-RCA / Sub-RCA chọn câu hỏi

Before asking the user for authorization, a sub-RCA scored five candidate questions against a 4.0/5 gate:

| Candidate question | Score | Decision |
|---|---:|---|
| Q1: G7 Authorization (yes/no/wait) | **5.0/5** | MUST ask — Q1 itself satisfies G7 |
| Q2: G7 Scope (Full vs Narrow) | **4.0/5** | Should ask — convention choice |
| Q3: Write Appendix C even if G7 not authorized | 3.0/5 | FAIL — default to always write |
| Q4: Update downstream files separately | 2.5/5 | FAIL — subsumed by Q2 |
| Q5: Re-verify G1–G6 before writing | 2.0/5 | FAIL — automatic |

Only Q1 and Q2 cleared the gate.

### 10.2 Three RCA rounds × 5-Why × scoring / Ba vòng RCA

| Round | Object | Score | Status |
|---|---|---:|---|
| R1 | Structural gap justification | **4.4/5** | PASS |
| R2 | Framework invariant check | **4.8/5** | PASS |
| R3 | Concrete change specification | **4.3/5** | PASS |

All three rounds cleared the 4.0/5 gate. Full details in `rca_core_extensibility_analysis.md` Appendix C.

### 10.3 User authorization recorded / Phê duyệt user được ghi nhận

| Question | Answer |
|---|---|
| Q1 G7 Authorization | **"Có — authorize G7"** |
| Q2 G7 Scope | **"Full G7 (Recommended)"** |

### 10.4 Full G7 execution / Thực thi Full G7

Seven concrete actions were executed on 2026-05-22:

1. ✅ Append Appendix C to `rca_core_extensibility_analysis.md`
2. ✅ Update Appendix B.1 G7 status: PENDING → DONE
3. ✅ `git mv` file: `framework/drafts/...narrow_draft.md` → `framework/...postulate.md`
4. ✅ Update file header: Holding state, Document type, Status, Lineage
5. ✅ Update G7 row in Section 8 of renamed file: PENDING → DONE
6. ✅ Add E18 row to `framework/index.md` Section 4.3 (after E16)
7. ✅ Update external references to old path in 3 active files (archives preserved)

**G7 verdict:** DONE — E18 promoted to frozen extension postulate.

---

## Section 11 — Gate Summary Table / Bảng tổng hợp Gate

| Gate | Condition | Evidence | Result |
|---|---|---|---|
| **G1** | Two case validations PASS | Wheeler + Scully-Drühl | ✅ DONE |
| **G2** | Formal locking rule with explicit `S` | `Lock(C_f, S, {W_i}) → W_valid` defined in narrow draft Section 11.8 | ✅ DONE |
| **G3** | Boundary safety ≥ 4.0/5 | 4.3/5 per Section 11.10 | ✅ DONE |
| **G4** | Third independent case validation | Kim et al. 1999 — 20/20 condition cells PASS | ✅ DONE |
| **G5** | BE anchor decision | Analogical-only permanent boundary accepted | ✅ DONE |
| **G6** | EX recoverability check | Path C selected (4.2/5); EX registry sync complete | ✅ DONE |
| **G7** | User-authorized index insertion | User authorized Full G7 on 2026-05-22; 3-round RCA PASS (R1=4.4, R2=4.8, R3=4.3) | ✅ DONE |

**Final state: 7/7 DONE (100%).**

---

## Section 12 — Impact on 6-Dimension Extensibility Verdict / Tác động lên Verdict 6 chiều

E18's promotion did **not** change the 6-dimension verdict shape recorded in `rca_core_extensibility_analysis.md` Appendix A.3, but it realized one candidate under Dimension 2:

| Dimension | Before G7 | After G7 | Confidence | Note |
|---|---|---|---:|---|
| 1 — BE source exhaustion | Gần đóng | **Unchanged** | 4.6/5 | E18 reuses existing BE nodes; no new BE source opened |
| **2 — Structural gap (nội tại)** | Có điều kiện mở | **One candidate frozen, dimension still conditionally open** | 4.1/5 | E18 is the first realized extension; future candidates (E17 R2, multi-RS) remain open |
| 3 — Nodes/edges trong postulate hiện có | Mở | **Unchanged** | 4.5/5 | G7 is a postulate promotion, not sub-node addition |
| 4 — Import EX vào core | Đóng by design | **Unchanged** | 4.9/5 | G7 imported zero EX edges; Path C bridges remain EX-local |
| 5 — Algebraic-layer theorems | Có điều kiện mở | **Unchanged** | 4.1/5 | Outside G7 scope |
| 6 — Inter-RS coordination | Open frontier | **Unchanged** | 4.1/5 | Outside G7 scope |

---

## Section 13 — Lessons Learned / Bài học rút ra

### 13.1 Methodological lessons / Bài học phương pháp

1. **A candidate is not a postulate until tested.** The original RCA correctly preserved E18 at 3.8/5 as a candidate, not as a postulate. Three case validations were needed before promotion was considered.
2. **Formula refinement during case testing is expected.** The introduction of the sorting relation `S` happened during the second case test (quantum eraser), not at the candidate phase. Case tests are formula-refinement opportunities, not just validation.
3. **Headline numbers must be scoped.** Different "confidence" numbers can measure different objects (overall decision vs sub-metric postulate readiness). Reconciliation boxes are essential.
4. **BE anchors stay analogical unless equivalence is justified.** G5's analogical-only decision is reusable convention; it should be the default unless RCA establishes physical equivalence.
5. **EX compass-only, never cargo.** G6 demonstrated that EX-side recovery (Path C) can advance promotion without importing any core edge. The compass-cargo distinction is operationally clean.
6. **Governance gate ≠ technical gate.** G7 is qualitatively different from G1–G6. Even when all technical gates pass, governance authorization is a separate decision belonging to the project author.
7. **Question selection deserves its own RCA.** The sub-RCA filtering five candidate questions down to two (Q1, Q2) prevented over-asking the user. Questions are not free.

### 13.2 Documentation lessons / Bài học tài liệu

1. **"Extend, not overwrite" applies to historical RCA documents.** Appendices A, B, C preserve their narrative state at time of writing. The live state is in the latest appendix.
2. **`git mv` preserves history.** File rename + move must use `git mv` to retain blame/log continuity.
3. **Archive files are frozen historical records.** Updating archive file:/// links is unnecessary and would falsify historical state.
4. **Author metadata rule respects folder boundaries.** Files inside `public_documents`/`published_documents` carry no VVV-QMRF author metadata; files elsewhere preserve it.
5. **Schema consistency matters.** All E1–E16 postulate files follow `vvv_qmrf_framework_e##_..._postulate.md`. E18 must match. Renaming `_narrow_draft → _postulate` is part of promotion, not a separate decision.

### 13.3 Boundary lessons / Bài học ranh giới

1. **Non-retrocausal boundary must be repeated explicitly.** Public delayed-choice language naturally invites retrocausal overinterpretation; every layer of the document must restate the K-side scope.
2. **Standard QM language stays neutral.** No "error/wrong/fallacy" framing of P1–P4; only "scope boundary" / "registration-layer distinction."
3. **A postulate is a K-side classification rule, not a physical theory.** This boundary recurred across every gate. It must be the first line of every E18-related document.

---

## Section 14 — Document Provenance / Nguồn gốc Tài liệu

- **E18 Postulate (frozen, 2026-05-22):** [vvv_qmrf_framework_e18_delayed_choice_registration_boundary_postulate.md](../vvv_qmrf_framework_e18_delayed_choice_registration_boundary_postulate.md)
- **Parent E18 RCA:** [rca_e18_delayed_choice_registration_boundary.md](../../rca/rca_e18_delayed_choice_registration_boundary.md) (commit `cd0e6e2`, 2026-05-21)
- **Kim 1999 case file:** [rca/cases/e18_case_kim_1999.md](../../rca/cases/e18_case_kim_1999.md)
- **G6 EX recoverability check:** [rca_e18_g6_ex_recoverability_check.md](../../rca/rca_e18_g6_ex_recoverability_check.md)
- **G6 EX vNext bridge audit:** [rca_e18_ex_vnext_bridge_audit.md](../../rca/rca_e18_ex_vnext_bridge_audit.md)
- **G7 authorization analysis:** [rca_core_extensibility_analysis.md Appendix C](../../rca/rca_core_extensibility_analysis.md)
- **Framework index:** [framework/index.md](../index.md)
- **BE SOT:** [SYSTEM_Buddhist_Epistemology/system_be_full.md](../../../../SYSTEM_Buddhist_Epistemology/system_be_full.md)
- **Companion (this directory):** [postulate_promotion_protocol.md](postulate_promotion_protocol.md) — generalized protocol distilled from this history

---

## Section 15 — Verify / Kiểm chứng

| Check | Result | Evidence |
|---|---|---|
| All gates G1–G7 closed | PASS | Section 11 gate summary |
| Scoring history complete | PASS | Section 7 consolidated table |
| All three cases documented | PASS | Sections 4, 5, 6 |
| BE anchor decision recorded | PASS | Section 8 |
| EX activity recorded | PASS | Section 9 |
| G7 authorization recorded | PASS | Section 10 |
| Impact on 6-dim verdict recorded | PASS | Section 12 |
| Lessons documented | PASS | Section 13 |
| All sources cited and resolvable | PASS | Section 14 |
| Neutral wording on Standard QM preserved | PASS | "K-side classification rule" / "scope boundary" language used throughout |
| Author metadata correct | PASS | File outside `public_documents`/`published_documents` folders; VVV-QMRF metadata at top |
| Bilingual (En/Vi) discipline preserved | PASS | Each major section has VN summary |

---

© 2026 VietVunVut (Viet - Nguyen Xuan). Licensed under CC BY 4.0.
To view a copy of this license, visit https://creativecommons.org/licenses/by/4.0/
