Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

> **DISCLAIMER / CẢNH BÁO:** VVV-QMRF is independent Class D personal research, not Standard Quantum Mechanics, not peer-reviewed or experimentally validated, and not for real-world technical use. This document is a **third case validation report** for the E18 narrow draft candidate, not a frozen postulate and not a physical theory.
>
> VVV-QMRF là nghiên cứu cá nhân độc lập ở Class D, không phải Standard Quantum Mechanics, chưa peer-reviewed hoặc kiểm chứng thực nghiệm, và không dùng cho ứng dụng kỹ thuật ngoài thực tế. Tài liệu này là **báo cáo case validation thứ ba** cho candidate E18 narrow draft, không phải tiền đề đã đóng băng và không phải lý thuyết vật lý.

# E18 Case Test 3 — Kim et al. 1999 Delayed-Choice Quantum Eraser
# Case Test 3 cho E18 — Kim et al. 1999 Delayed-Choice Quantum Eraser

**Framework:** VietVunVut Quantum Measurement Registration Framework (VVV-QMRF)
**Document type:** case validation report (third independent case for E18 promotion gate G4)
**Holding state:** `rca/cases/` — E18 narrow draft still in `framework/drafts/`, NOT yet a frozen postulate
**Author:** VietVunVut (Viet - Nguyen Xuan)
**GitHub:** https://github.com/AIhugART/
**Date:** 2026-05-22
**Status:** Third Case Validation — supports E18 promotion gate G4
**Lineage:** Parent RCA `rca_e18_delayed_choice_registration_boundary.md` (Section 10 Wheeler + Section 11 Scully-Drühl) → this case file (3rd case) → narrow draft G4 status update
**Scope rule:** VVV-QMRF core scope; VVV-QMRF-EX used as compass only; K-side classification layer only

---

## Section 0 — Executive Summary / Tóm tắt điều hành

### 0.1 Purpose / Mục đích

**English:** This document is the third independent case validation for E18 "Delayed-Choice Registration Boundary," required by promotion gate G4 per [vvv_qmrf_framework_e18_..._postulate.md Section 8](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/framework/vvv_qmrf_framework_e18_delayed_choice_registration_boundary_postulate.md#L208) (promoted from narrow draft via G7 user authorization on 2026-05-22). Two prior validations have passed: Wheeler delayed-choice interferometer (binary `{W_path, W_interference}`) and Scully-Drühl quantum eraser (ternary `{W_signal_raw, W_which_path, W_erased_interference}`). This case tests E18 against Kim et al. 1999 "Delayed Choice Quantum Eraser" (PRL 84, 1-5), which exhibits **four-branch multi-detector lock with symmetric erased pair** — a structurally stronger stress test than either prior case.

**Vietnamese:** Tài liệu này là case validation thứ ba cho E18, được yêu cầu bởi promotion gate G4. Hai case trước đã PASS: Wheeler delayed-choice (2-branch) và Scully-Drühl quantum eraser (3-subset). Case này test E18 trên Kim et al. 1999 — thí nghiệm có cấu trúc 4-branch multi-detector với cặp erased đối xứng, là stress test mạnh hơn về cấu trúc so với hai case trước.

### 0.2 Verdict preview / Xem trước kết quả

| Branch | `C_f` | Expected `W_valid` | 5-Condition Result |
|---|---|---|:---:|
| Branch 1 (D1) | idler at D1 (erased, +fringe) | `W_D1` (signal subset coincident with D1) | **5/5 PASS** |
| Branch 2 (D2) | idler at D2 (erased, -fringe) | `W_D2` (signal subset coincident with D2, out-of-phase) | **5/5 PASS** |
| Branch 3 (D3) | idler at D3 (preserved, path A) | `W_D3` (signal subset coincident with D3) | **5/5 PASS** |
| Branch 4 (D4) | idler at D4 (preserved, path B) | `W_D4` (signal subset coincident with D4) | **5/5 PASS** |
| **Total** | — | — | **20/20 PASS** |

**Case result:** Kim et al. 1999 passes the third E18 case test under a conservative K-side classification interpretation, with mandatory `S` (coincidence relation D0-Di) per the refined `Lock(C_f, S, {W_i}) → W_valid` formula.

---

## Section 1 — Experimental Setup / Thiết lập Thí nghiệm

### 1.1 Kim 1999 minimal setup

**English:** Kim et al. 1999 uses spontaneous parametric down-conversion (SPDC) in a BBO crystal to generate entangled signal-idler photon pairs from one of two slits (A or B). The signal photon travels to a movable detector `D0` providing position information. The idler photon traverses an optical assembly with beam splitters `BSA`, `BSB`, and a 50/50 beam splitter `BS` directing it to one of four detectors: `D1`, `D2`, `D3`, or `D4`. Path-length engineering ensures the idler detection occurs after the signal `D0` registration.

**Vietnamese:** Kim et al. 1999 dùng SPDC ("spontaneous parametric down-conversion") trong tinh thể BBO để tạo cặp photon entangled signal-idler từ một trong hai khe (A hoặc B). Photon signal đi tới detector di động `D0` cung cấp thông tin vị trí. Photon idler đi qua dãy gồm "beam splitter" `BSA`, `BSB`, và "beam splitter" 50/50 `BS` đến một trong bốn detector: `D1`, `D2`, `D3`, hoặc `D4`. Thiết kế độ dài đường đi đảm bảo phép đo idler xảy ra **sau** khi signal đăng ký tại `D0`.

```text
                          BBO crystal (entangled pair source)
                                |
              +-----------------+-----------------+
              |                                   |
        slit A (signal+idler)               slit B (signal+idler)
              |                                   |
       signal -> D0 (movable position detector)
              |
       idler -> optical assembly:
              |
         +----BSA----+        +----BSB----+
         |           |        |           |
        D3           |        |           D4   (preserved which-path)
                     +-- BS --+
                     |        |
                    D1        D2          (erased which-path)
```

### 1.2 Detector classification / Phân loại detector

| Detector | Idler outcome | Which-path info | Coincidence histogram with D0 |
|---|---|---|---|
| `D3` | Idler came from slit A only | **Preserved** (path A) | No interference (single-slit envelope) |
| `D4` | Idler came from slit B only | **Preserved** (path B) | No interference (single-slit envelope) |
| `D1` | Idler from BS output 1 | **Erased** (A and B mixed) | Interference `R_{01}` with positive fringe |
| `D2` | Idler from BS output 2 | **Erased** (A and B mixed) | Interference `R_{02}` with **out-of-phase** fringe (negative) |

**Key observation:** `D1` and `D2` produce **complementary out-of-phase interference patterns** because the 50/50 BS introduces a π/2 phase between its two output ports. This is the **symmetric erased pair** structural feature unique to Kim 1999.

**VN:** Quan sát chính: `D1` và `D2` tạo ra **giao thoa lệch pha** (out-of-phase) do BS 50/50 đưa vào độ lệch pha π/2 giữa hai cổng output. Đây là đặc điểm cấu trúc **cặp erased đối xứng** chỉ có ở Kim 1999.

### 1.3 Delayed-choice condition / Điều kiện delayed-choice

**English:** Optical path lengths are engineered such that `D0` triggers approximately 8 ns before any of `D1-D4`. The choice of which `Di` (i=1,2,3,4) registers the idler is therefore made *after* the signal photon has already been detected at `D0`. This satisfies the "delayed-choice" condition: the registration context for the idler is finalized after the signal registration event.

**Vietnamese:** Độ dài đường đi quang học được thiết kế sao cho `D0` kích hoạt khoảng 8 ns trước bất kỳ `D1-D4` nào. Việc detector idler `Di` nào kích hoạt do đó được quyết định *sau* khi photon signal đã được phát hiện tại `D0`. Điều này thoả điều kiện "delayed-choice": bối cảnh đăng ký cho idler được hoàn tất sau sự kiện đăng ký signal.

**Boundary note:** This RCA does not claim the later idler measurement changes the photon's past quantum state. It only tests whether the final idler context plus coincidence sorting can lock a K-side signal-data subset.

**VN — Ghi chú ranh giới:** RCA này không khẳng định phép đo idler về sau thay đổi trạng thái lượng tử quá khứ của photon. Nó chỉ test xem bối cảnh idler cuối cùng cộng với coincidence sorting có khoá được subset dữ liệu signal phía K hay không.

---

## Section 2 — Variable Mapping / Ánh xạ Biến

### 2.1 E18 symbols ↔ Kim 1999 variables

| E18 symbol | Kim 1999 realization | Meaning |
|---|---|---|
| `C_f` | Final idler detector ID `Di` (i ∈ {1, 2, 3, 4}) | Later measurement context selecting registration class |
| `S` | Coincidence relation `R_{0i}` pairing D0 and Di records within coincidence time window | Sorting/coincidence relation required for subset classification |
| `{W_i}` | `{W_D1, W_D2, W_D3, W_D4, W_signal_raw}` | Candidate signal-data registration subsets |
| `W_signal_raw` | Raw D0 detection record (unsorted across all idler outcomes) | Unsorted signal record (no interference visible) |
| `W_D1` | Signal subset coincident with D1 firing | Erased, positive-fringe interference subset |
| `W_D2` | Signal subset coincident with D2 firing | Erased, negative-fringe interference subset (out-of-phase from W_D1) |
| `W_D3` | Signal subset coincident with D3 firing | Preserved-path-A subset (no interference) |
| `W_D4` | Signal subset coincident with D4 firing | Preserved-path-B subset (no interference) |
| `W_valid` | Subset selected by `Lock(C_f, S, {W_i})` | Valid K-side registration subset for current `Di` reading |
| `K` | Registration state | State updated after valid subset locking |

### 2.2 Pre-lock state / Trạng thái trước khi khoá

Before idler context `C_f` and coincidence sorting `S` are applied to the raw signal record `W_signal_raw`, the signal data remain underclassified:

```text
Before C_f and S:
  K(W_signal_raw) = raw / underclassified across {W_D1, W_D2, W_D3, W_D4}
```

After `C_f = Di` is fixed and `S = R_{0i}` is applied, a valid lock may occur if all five conditions pass.

---

## Section 3 — Branch Tests / Test 4 Nhánh

### 3.1 Branch 1 — `C_f = D1` (erased, positive fringe)

Expected lock:

```text
Lock(D1, R_{01}, {W_D1, W_D2, W_D3, W_D4, W_signal_raw}) -> W_D1
```

| Condition | RCA question | Result |
|---|---|---|
| `R(D1, W_D1)` | Is the D1 idler context relevant to the W_D1 signal subset? | PASS — coincidence pairs are physically linked via entanglement |
| `B(D1, W_D1)` | Does D1 specify the erased-positive-fringe registration class? | PASS — D1 uniquely identifies BS output port 1 |
| `T(W_D1, D1)` | Are signal and idler records inside the same admissible pair-sequence? | PASS — coincidence time window ensures pair admissibility |
| `I(D1, R_{01}, W_D1)` | Do D1 plus coincidence relation function as a valid sign for W_D1? | PASS, protocol-dependent — requires R_{01} coincidence |
| `G(D1, W_D1)` | Does the claim avoid backward signaling and remain K-side only? | PASS — no claim of physical change to signal photon past |

**RCA note:** Branch 1 does not invalidate the raw signal record or claim physical change to past photon dynamics. It classifies the record into the W_D1 subset using the later D1 context plus coincidence relation R_{01}.

### 3.2 Branch 2 — `C_f = D2` (erased, negative fringe — out-of-phase)

Expected lock:

```text
Lock(D2, R_{02}, {W_D1, W_D2, W_D3, W_D4, W_signal_raw}) -> W_D2
```

| Condition | RCA question | Result |
|---|---|---|
| `R(D2, W_D2)` | Is the D2 idler context relevant to the W_D2 signal subset? | PASS |
| `B(D2, W_D2)` | Does D2 specify the erased-negative-fringe registration class? | PASS — D2 uniquely identifies BS output port 2 |
| `T(W_D2, D2)` | Are signal and idler records inside the same admissible pair-sequence? | PASS |
| `I(D2, R_{02}, W_D2)` | Do D2 plus R_{02} function as a valid sign for the out-of-phase W_D2 subset? | PASS, protocol-dependent |
| `G(D2, W_D2)` | Does the claim avoid backward signaling and remain K-side only? | PASS |

**RCA note:** Branch 2 is structurally symmetric to Branch 1 but selects a different valid subset because the BS 50/50 introduces a π/2 phase between D1 and D2 outputs. This is the **first novel structural feature** Kim 1999 introduces beyond Wheeler and Scully-Drühl: two distinct valid subsets within the erased category.

**VN — Ghi chú RCA:** Nhánh 2 đối xứng cấu trúc với Nhánh 1 nhưng chọn subset hợp lệ khác do BS 50/50 đưa vào độ lệch pha π/2 giữa output D1 và D2. Đây là **đặc điểm cấu trúc mới đầu tiên** mà Kim 1999 đưa vào ngoài Wheeler và Scully-Drühl: hai subset hợp lệ riêng biệt trong cùng lớp erased.

### 3.3 Branch 3 — `C_f = D3` (preserved, path A)

Expected lock:

```text
Lock(D3, R_{03}, {W_D1, W_D2, W_D3, W_D4, W_signal_raw}) -> W_D3
```

| Condition | RCA question | Result |
|---|---|---|
| `R(D3, W_D3)` | Is the D3 idler context relevant to the W_D3 signal subset? | PASS |
| `B(D3, W_D3)` | Does D3 specify the preserved-path-A registration class? | PASS — D3 only fires for path-A idlers |
| `T(W_D3, D3)` | Are signal and idler records inside the same admissible pair-sequence? | PASS |
| `I(D3, R_{03}, W_D3)` | Do D3 plus R_{03} function as a valid sign for W_D3? | PASS, protocol-dependent |
| `G(D3, W_D3)` | Does the claim avoid backward signaling and remain K-side only? | PASS |

**RCA note:** Branch 3 produces no interference because D3 preserves which-path information. The locked subset W_D3 contains only signal events whose idler partner came from slit A.

### 3.4 Branch 4 — `C_f = D4` (preserved, path B)

Expected lock:

```text
Lock(D4, R_{04}, {W_D1, W_D2, W_D3, W_D4, W_signal_raw}) -> W_D4
```

| Condition | RCA question | Result |
|---|---|---|
| `R(D4, W_D4)` | Is the D4 idler context relevant to the W_D4 signal subset? | PASS |
| `B(D4, W_D4)` | Does D4 specify the preserved-path-B registration class? | PASS — D4 only fires for path-B idlers |
| `T(W_D4, D4)` | Are signal and idler records inside the same admissible pair-sequence? | PASS |
| `I(D4, R_{04}, W_D4)` | Do D4 plus R_{04} function as a valid sign for W_D4? | PASS, protocol-dependent |
| `G(D4, W_D4)` | Does the claim avoid backward signaling and remain K-side only? | PASS |

**RCA note:** Branch 4 mirrors Branch 3 with path-B preservation. Together D3 and D4 form a second symmetric pair (preserved-which-path pair) structurally distinct from the D1/D2 erased pair.

---

## Section 4 — Five-Condition Aggregate Result / Kết quả Tổng hợp 5 Điều kiện

### 4.1 Aggregate table

| Condition | Branch 1 (D1) | Branch 2 (D2) | Branch 3 (D3) | Branch 4 (D4) | RCA implication |
|---|:-:|:-:|:-:|:-:|---|
| `R` | PASS | PASS | PASS | PASS | Idler context is relevant to the selected signal subset for all four branches. |
| `B` | PASS | PASS | PASS | PASS | Each `Di` uniquely specifies a registration class (4 distinct classes). |
| `T` | PASS | PASS | PASS | PASS | All branches satisfy admissible pair-sequence via coincidence time window. |
| `I` | PASS w/ R_{01} | PASS w/ R_{02} | PASS w/ R_{03} | PASS w/ R_{04} | Validity requires the specific coincidence relation `R_{0i}` for each branch. |
| `G` | PASS | PASS | PASS | PASS | All branches remain non-retrocausal and K-side only. |
| **Total** | **5/5** | **5/5** | **5/5** | **5/5** | **20/20** |

**Case result:** Kim et al. 1999 passes the third E18 case test with all twenty condition cells PASS, **only if** each branch uses its specific coincidence relation `R_{0i}` as the sorting relation `S` in the refined formula `Lock(C_f, S, {W_i}) → W_valid`.

**VN — Kết quả case:** Kim et al. 1999 pass case test thứ ba cho E18 với toàn bộ 20 ô điều kiện PASS, **chỉ khi** mỗi nhánh dùng quan hệ trùng phùng `R_{0i}` đặc thù làm sorting relation `S` trong công thức tinh chỉnh.

---

## Section 5 — Structural Novelty Analysis / Phân tích Điểm Mới Cấu trúc

### 5.1 Symmetric erased pair (D1/D2)

**English:** The D1/D2 pair produces complementary out-of-phase interference patterns. Both belong to the "erased which-path" class, but they lock **different valid subsets** (`W_D1` and `W_D2`) with opposite fringe positions. This stress-tests the `B(C_f, W_j)` predicate: B must be granular enough to distinguish W_D1 from W_D2 within the same coarse-grained erased class.

**Vietnamese:** Cặp D1/D2 tạo ra giao thoa lệch pha bổ sung nhau. Cả hai đều thuộc lớp "erased which-path", nhưng chúng khoá **các subset hợp lệ khác nhau** (`W_D1` và `W_D2`) với vị trí fringe đối nghịch. Điều này stress-test predicate `B(C_f, W_j)`: B phải đủ chi tiết để phân biệt W_D1 với W_D2 trong cùng lớp erased thô.

**Verdict:** `B` predicate PASS — Kim 1999 setup uniquely identifies each detector, so `B(D1, W_D1)` and `B(D2, W_D2)` are independently true.

### 5.2 Symmetric preserved pair (D3/D4)

**English:** The D3/D4 pair produces complementary which-path classifications (slit A vs slit B). This stress-tests `R(C_f, W_j)` predicate: R must distinguish W_D3 from W_D4 even though both are "preserved-path" subsets.

**Verdict:** `R` predicate PASS — D3 and D4 fire only for path-A and path-B idlers respectively, giving R unambiguous resolution.

### 5.3 Four-branch lock vs binary lock

**English:** Wheeler and Scully-Drühl cases involve binary or ternary locks. Kim 1999 requires a **four-branch lock** with two symmetric pairs (erased D1/D2 + preserved D3/D4). The `Lock` rule must handle four mutually exclusive outcomes for a single signal photon's coincidence partner. This is the **structural independence** dimension that motivated Kim 1999 selection over Ma 2013 or Manning 2015.

**Vietnamese:** Wheeler và Scully-Drühl là lock binary hoặc ternary. Kim 1999 yêu cầu **four-branch lock** với hai cặp đối xứng (erased D1/D2 + preserved D3/D4). Quy tắc `Lock` phải xử lý bốn kết quả loại trừ lẫn nhau cho cùng một photon signal. Đây là chiều **độc lập cấu trúc** đã thúc đẩy chọn Kim 1999 thay vì Ma 2013 hoặc Manning 2015.

**Verdict:** Multi-branch lock PASS — the formula `Lock(C_f, S, {W_i}) → W_valid` natively supports arbitrary cardinality of `{W_i}`, so four branches are handled without formula modification.

---

## Section 6 — RCA 5 Whys for Kim 1999 / RCA 5 Vì sao

1. **Why does E18 seem needed in Kim 1999?**
   → Because the raw D0 record contains all 4 sub-populations mixed together; only after `Di` fires and `R_{0i}` coincidence is applied does the valid signal subset emerge.

2. **Why is this not E8 (Retroactive Override)?**
   → Because no prior valid registration is voided. The raw `W_signal_raw` was never claimed to belong to any specific Di subset before sorting; it was underclassified, not validly classified.

3. **Why is this not E13 (Temporal Discontinuity)?**
   → Because E13 bounds individual registration moments as kṣaṇa-like discrete events. It does not provide the multi-branch classification rule that selects which `W_Di` is locked.

4. **Why is this not legacy E17 (Measurement Interface)?**
   → Because E17 separates ρ from K, but does not define how a 4-cardinality `{W_i}` is classified into a unique `W_valid` based on `(C_f, S)`.

5. **Root cause:** Kim 1999 exposes the **strongest form** of the E18 gap so far: context-conditioned classification across a **multi-branch symmetric set** of candidate subsets, requiring both `C_f` specificity and `S` coincidence resolution to produce a unique `W_valid`.

**VN — Tóm tắt:** RCA 5 Whys cho thấy Kim 1999 phơi bày **dạng mạnh nhất** của gap E18 đến nay: phân loại theo bối cảnh trên **tập multi-branch đối xứng** của các subset ứng viên, đòi hỏi cả tính đặc thù của `C_f` và độ phân giải coincidence `S` để tạo ra một `W_valid` duy nhất.

---

## Section 7 — Good / Bad / Risk Table / Bảng Tốt / Xấu / Rủi ro

| Aspect | Good / Strength | Bad / Weakness | Risk control |
|---|---|---|---|
| Stress-test strength | Hardest case so far — 4-branch lock with 2 symmetric pairs. | Significantly more complex experimental setup; harder to communicate. | Use minimal setup diagram (Section 1.1); restrict scope to K-side classification. |
| E18 fit | Confirms `Lock(C_f, S, {W_i}) → W_valid` handles arbitrary cardinality. | Could be misread as proving multi-detector retrocausality. | Repeat Section 9 non-claims explicitly. |
| Structural independence | Adds a new dimension (multi-branch + symmetric pairs) not covered by Wheeler or Scully-Drühl. | None — this is the strength that motivated Kim 1999 selection. | Document the independence in Section 5.3. |
| Distinction from E8 | Raw D0 record never invalidated; only classified. | The word "delayed" tempts override language. | Use "classification" and "sorting" not "invalidation." |
| Distinction from E13 | Timing alone cannot explain 4-way subset validity. | Multiple detector firing times can confuse the model. | Separate raw detection times from valid-subset registration. |
| Distinction from E17 | E17 gives ρ/K interface; E18 gives K-side multi-subset locking. | Without `S`, E18 cannot distinguish W_D1 from W_D2. | Make `S = R_{0i}` mandatory in every branch. |
| BE anchor | `I(C_f, S, W_j)` sharpens valid-sign analogy across 4 branches. | BE relation remains analogical only, not identity. | Keep Anumāna, Vyāpti, Svabhāvapratibandha as structural analogues. |
| Boundary safety | No backward signaling required; coincidence sorting happens locally at K-side. | Popular descriptions of Kim 1999 often invoke retrocausation strongly. | Repeat: no retrocausation, no Born-rule modification, no Standard QM replacement. |

---

## Section 8 — Decision Impact / Tác động lên Quyết định

### 8.1 Updated scoring table

| Criterion | After Quantum Eraser test | After Kim 1999 test | RCA note |
|---|---:|---:|---|
| Internal necessity | 4.4 | **4.5** | Kim 1999 confirms multi-branch generality of the gap. |
| BE anchor strength | 3.8 | **3.8** | Unchanged — case test does not strengthen or weaken BE anchor; G5 remains the dedicated upgrade gate. |
| EX support | 3.7 | **3.7** | Unchanged — EX remains compass-only. |
| Boundary safety | 4.3 | **4.3** | Unchanged — Kim 1999 same retrocausal overclaim risk as Scully-Drühl, contained by Section 9. |
| Postulate readiness | 4.3 | **4.4** | Three case validations now support drafting; G5/G6/G7 remained pending at the time of this case file. |

> **Post-G5 status note (2026-05-22):** Parent RCA Section 13 later closed G5 by accepting the BE anchor as analogical-only permanent boundary. Current promotion status is therefore G1-G5 DONE, G6-G7 PENDING; this case file remains the G4 evidence record.

### 8.2 Promotion gate status update

| Gate | Condition | Status before this case | Status after this case |
|---|---|---|---|
| G1 | Two case validations PASS | DONE | DONE |
| G2 | Formal locking rule with explicit `S` | DONE | DONE |
| G3 | Boundary safety ≥ 4.0/5 | DONE | DONE |
| **G4** | **Third independent case validation** | **PENDING** | **DONE — this document** |
| G5 | BE anchor decision | PENDING | DONE in parent RCA Section 13 — analogical-only permanent boundary accepted |
| G6 | EX recoverability check | PENDING | PENDING (unchanged) |
| G7 | User-authorized index insertion | PENDING | PENDING (unchanged) |

**Gate progress: 3/7 -> 4/7 (57%) by this G4 case; current status after parent RCA Section 13 is 5/7 (71%).**

---

## Section 9 — Boundary & Non-Claims / Ranh giới & Phi-claim

### 9.1 What this case file IS

1. A third independent case validation showing `Lock(C_f, S, {W_i}) → W_valid` operates correctly on a 4-branch multi-detector setup.
2. Evidence that the refined formula (with mandatory `S`) generalizes beyond binary and ternary locks.
3. A holding-state document in `rca/cases/` supporting E18 promotion gate G4.
4. Consistent with the K-Space axiomatization and prior case tests.

### 9.2 What this case file IS NOT

1. **NOT retrocausation.** Past physical quantum dynamics of the signal photon are unchanged. The idler measurement at `Di` only classifies which K-side signal-data subset is valid.
2. **NOT a modification of the Born rule** or any of P1-P4.
3. **NOT a permission for superluminal or retrocausal signaling.** Coincidence sorting `R_{0i}` happens locally at K-side after both D0 and Di records are available.
4. **NOT a frozen framework postulate.** E18 remains in `framework/drafts/` until all 7 gates pass.
5. **NOT an EX import.** EX entry `N_QM_VVV_00024` remains below 4.0 threshold per `rca_e18.md:204`.
6. **NOT a claim of identity** between BE concepts (Anumāna, Vyāpti, Svabhāvapratibandha) and quantum context-coincidence relations. BE anchors remain analogical only.
7. **NOT a claim that Kim 1999 confirms** the philosophical content of E18 — only that the formal locking rule operates without contradiction on the experimental setup.

### 9.3 Wording protocol

This document uses neutral boundary language: "category boundary," "scope boundary," "registration-layer distinction," "K-side classification." It does NOT frame Standard Quantum Mechanics as defective, mistaken, or in error.

---

## Section 10 — Source Traceability / Truy vết Nguồn

### 10.1 Experimental source

| Source | Reference | Role for this case |
|---|---|---|
| Kim et al. 1999 | Kim, Y.-H., Yu, R., Kulik, S. P., Shih, Y., & Scully, M. O. (2000). "Delayed 'Choice' Quantum Eraser." *Physical Review Letters* 84, 1-5. | Primary experimental reference for the case setup, detector geometry, and coincidence histogram structure. |

### 10.2 Framework lineage

| Document | Path | Role |
|---|---|---|
| Parent RCA | [rca_e18_delayed_choice_registration_boundary.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/rca/rca_e18_delayed_choice_registration_boundary.md) | Source of 5-condition validation template (Sections 10-11) |
| Postulate (promoted from narrow draft) | [vvv_qmrf_framework_e18_..._postulate.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/framework/vvv_qmrf_framework_e18_delayed_choice_registration_boundary_postulate.md) | Source of refined `Lock(C_f, S, {W_i}) → W_valid` formula and G1-G7 promotion gate definitions (G7 closed via user authorization on 2026-05-22) |
| Core extensibility RCA | [rca_core_extensibility_analysis.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/rca/rca_core_extensibility_analysis.md) | Lists Kim 1999 as candidate for G4 third case validation (Section 4 Tier 1) |
| Schema guide | [vvv-qmrf/schema_guide.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/vvv-qmrf/schema_guide.md) | Document-creation contract followed for this file |

### 10.3 BE SOT anchors (analogical only)

All BE anchors are used as **structural analogues**, not identity claims.

| BE Node | Term | Source SOT line | Structural role for Kim 1999 branches |
|---|---|---|---|
| N_BE_00003 | Anumāna (Inference) | [system_be_full.md:39](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/SYSTEM_Buddhist_Epistemology/system_be_full.md#L39) | Indirect knowledge through a valid sign — analogue for `I(Di, R_{0i}, W_Di)` |
| N_BE_00019 | Vyāpti (Pervasion) | [system_be_full.md:55](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/SYSTEM_Buddhist_Epistemology/system_be_full.md#L55) | Pervasion analogue for the validity guarantee linking `Di + R_{0i}` to `W_Di` |
| N_BE_00021 | Svabhāvapratibandha | [system_be_full.md:57](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/SYSTEM_Buddhist_Epistemology/system_be_full.md#L57) | Foundational analogue guarding against arbitrary 4-branch locking |

### 10.4 EX compass note (no import)

Per `rca_e18.md:204`, EX flags `N_QM_VVV_00024` as below v1.7 threshold. This case validation does not change EX classification (G6 is a separate, deferred check awaiting EX vNext). EX remains compass, not cargo.

---

## Section 11 — Verification Checklist (RULE ZERO Step 5)

| Check | Result | Evidence |
|---|---|---|
| Root cause identified for case selection | PASS | Pre-write RCA (5-Why + 3-round scoring 4.6/5 avg) |
| 5-condition validation completed for all 4 branches | PASS | Section 3.1-3.4 (20/20 cells PASS) |
| Refined formula `Lock(C_f, S, {W_i}) → W_valid` used, not legacy form | PASS | Section 2.1, 3.1-3.4 all use refined form |
| Mandatory `S` (coincidence relation) explicit per branch | PASS | Section 3 each branch uses specific `R_{0i}` |
| K-side scope only — no physical retrocausation claim | PASS | Section 9.2 items 1, 3 explicit |
| BE anchors marked analogical only | PASS | Section 10.3 with explicit "analogical only" labels |
| EX used as compass, not import | PASS | Section 10.4 explicit |
| Neutral wording (no "error/wrong/fallacy") | PASS | Section 9.3 + visual scan |
| Bilingual EN/VN per CLAUDE.md | PASS | Hybrid coverage (narrative/boundary bilingual; tables EN with VN summary) |
| Author metadata at top (file outside `published_documents`) | PASS | Line 1 |
| Disclaimer Class D at top | PASS | Lines 3-5 |
| Framework `index.md` NOT modified | PASS — pending git verification in todo #10 | To be verified |
| Citations have line anchors where applicable | PASS | All cross-references use `file:///` + `#L` line anchors |
| Multi-branch lock handled without formula modification | PASS | Section 5.3 confirms |
| Symmetric pair structural feature documented | PASS | Section 5.1 (erased) + Section 5.2 (preserved) |
| 4-branch test 5-condition cells = 20 cells | PASS | Section 4.1 aggregate table |
| Comparison with Wheeler + Scully-Drühl maintained | PASS | Section 5.3 explicit |
| Promotion gate update (G4 PENDING → DONE) | PASS | Section 8.2 |
| Does NOT promote E18 beyond G4 | PASS | Section 9.2 item 4 + Section 8.2 G5/G6/G7 unchanged |

---

## Section 12 — Document Provenance / Nguồn gốc Tài liệu

- **Parent RCA:** [rca_e18_delayed_choice_registration_boundary.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/rca/rca_e18_delayed_choice_registration_boundary.md) — Sections 9-11 supply the 5-condition validation framework.
- **Postulate (promoted from narrow draft via G7 user authorization on 2026-05-22):** [vvv_qmrf_framework_e18_delayed_choice_registration_boundary_postulate.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/framework/vvv_qmrf_framework_e18_delayed_choice_registration_boundary_postulate.md) — Section 6 supplies symbol table; Section 8 defines G4 promotion gate.
- **Core extensibility RCA:** [rca_core_extensibility_analysis.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/rca/rca_core_extensibility_analysis.md) — Lists Kim 1999 as G4 candidate.
- **Schema contract:** [vvv-qmrf/schema_guide.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/vvv-qmrf/schema_guide.md) — Section 6, 7, 8 inventories built per Section 11 LLM Writing Protocol.
- **BE SOT:** [SYSTEM_Buddhist_Epistemology/system_be_full.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/SYSTEM_Buddhist_Epistemology/system_be_full.md) — N_BE_00003, N_BE_00019, N_BE_00021 anchors.
- **Decision rule applied:** RULE ZERO RCA × 5-Why × 3-round scoring at gate 4.0/5 per project decision rule (memory: `feedback_decision_rule.md`).

---

© 2026 VietVunVut (Viet - Nguyen Xuan). Licensed under CC BY 4.0.
To view a copy of this license, visit https://creativecommons.org/licenses/by/4.0/
