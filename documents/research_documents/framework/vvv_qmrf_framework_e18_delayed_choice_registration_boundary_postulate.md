Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

> **DISCLAIMER / CẢNH BÁO:** VVV-QMRF is independent Class D personal research, not Standard Quantum Mechanics, not peer-reviewed or experimentally validated, and not for real-world technical use. This document is a **frozen extension postulate** in the VVV-QMRF framework; it is not a physical theory and adds no Standard QM claim.
>
> VVV-QMRF là nghiên cứu cá nhân độc lập ở Class D, không phải Standard Quantum Mechanics, chưa peer-reviewed hoặc kiểm chứng thực nghiệm, và không dùng cho ứng dụng kỹ thuật ngoài thực tế. Tài liệu này là **tiên đề mở rộng đã đóng băng** trong khung VVV-QMRF; không phải lý thuyết vật lý và không thêm bất kỳ tuyên bố Standard QM nào.

# E18 — Delayed-Choice Registration Boundary Postulate
# Tiên đề E18 — Ranh giới Ghi nhận trong Delayed-Choice

**Framework:** VietVunVut Quantum Measurement Registration Framework (VVV-QMRF)
**Document type:** framework postulate (frozen extension postulate, promoted from narrow draft)
**Holding state:** `framework/` — promoted to frozen extension postulate via G7 user authorization on 2026-05-22; listed in `framework/index.md` Section 4.3 alongside E8–E16
**Author:** VietVunVut (Viet - Nguyen Xuan)
**GitHub:** https://github.com/AIhugART/
**Date:** 2026-05-22 (promoted)
**Status:** Frozen extension postulate — Registration class D — Promoted from Tier 1 narrow draft per `rca_core_extensibility_analysis.md` Appendix C
**Lineage:** RCA-supported candidate → narrow draft → **framework postulate (this document, G7 DONE 2026-05-22)**
**Scope rule:** VVV-QMRF core scope; VVV-QMRF-EX used as compass only, no edge import

---

## Section 0 — Executive Summary / Tóm tắt điều hành

**English:** This document is the Tier 1 narrow framework proposal for E18 "Delayed-Choice Registration Boundary," recommended by [rca_core_extensibility_analysis.md:424](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/rca/rca_core_extensibility_analysis.md#L424) after `rca_e18_delayed_choice_registration_boundary.md` passed two case validations (Wheeler delayed-choice + quantum eraser). E18 names the K-side classification rule by which a later context `C_f` (with sorting relation `S` when needed) locks one prior candidate registration window `W_j` as the operative valid window `W_valid`. E18 is **not** retrocausation, **not** Born-rule modification, and **not** a Standard Quantum Mechanics replacement.

**Vietnamese:** Tài liệu này là đề xuất khung hẹp ưu tiên Tier 1 cho E18 "Ranh giới Ghi nhận trong Delayed-Choice," được khuyến nghị bởi `rca_core_extensibility_analysis.md:424` sau khi RCA E18 pass hai case test (Wheeler + quantum eraser). E18 đặt tên cho quy tắc phân loại phía K — quy tắc nói rằng một bối cảnh sau `C_f` (kèm quan hệ sorting `S` khi cần) có thể khoá một cửa sổ ghi nhận ứng viên `W_j` thành cửa sổ hợp lệ vận hành `W_valid`. E18 **không** phải retrocausation, **không** sửa Born rule, và **không** thay thế Standard Quantum Mechanics.

### 0.1 Confidence Reconciliation Box / Hộp Đồng bộ Confidence

**Background:** [rca_core_extensibility_analysis.md:348](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/rca/rca_core_extensibility_analysis.md#L348) (Section A.1.1) flagged a confidence ambiguity between two numbers used in the parent RCA file:

- **Headline in `rca_e18.md` Section 0** ([line 25](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/rca/rca_e18_delayed_choice_registration_boundary.md#L25)): "Decision confidence: **3.8/5**" — overall decision-state at file creation, before case testing.
- **Sub-metric in Section 11.10** ([line 757](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/rca/rca_e18_delayed_choice_registration_boundary.md#L757)): "Postulate readiness: **4.3/5**" — single criterion in the 5-criteria scoring matrix, after two case validations.

**Root-cause resolution (RCA Step 5 — verify root cause removed, not just patched):** The two numbers are NOT in conflict. They measure two different objects across two different lifecycle states. The narrow draft headline below is **scoped explicitly** to the post-2-case readiness state, with the lifecycle table making the trajectory explicit.

| Lifecycle state | Source line | "Postulate readiness" sub-metric | Note |
|---|---|---:|---|
| At RCA file creation (pre-test) | [rca_e18:238](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/rca/rca_e18_delayed_choice_registration_boundary.md#L238) | 3.5 | Decision: candidate, not framework |
| After Section 9 formal conditions added | [rca_e18:414](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/rca/rca_e18_delayed_choice_registration_boundary.md#L414) | 3.9 | Stronger candidate, no case yet |
| After Wheeler case PASS | [rca_e18:564](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/rca/rca_e18_delayed_choice_registration_boundary.md#L564) | 4.1 | First case validation |
| After quantum eraser case PASS | [rca_e18:757](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/rca/rca_e18_delayed_choice_registration_boundary.md#L757) | **4.3** | Two case validations, formula refined with `S` |

**Narrow Draft Readiness (scoped headline):** **4.3/5** (post-2-case postulate readiness).

**This is NOT a promotion of the overall decision confidence to 4.3/5.** It is a scoped readiness metric for the narrow-draft artifact only. Promotion to a frozen framework postulate requires further steps listed in Section 8 below.

**VN — Hộp đồng bộ confidence:**
- `rca_e18.md:25` headline "Decision confidence 3.8/5" = trạng thái pre-test, đo overall decision state tại thời điểm tạo file RCA.
- `rca_e18.md:757` sub-metric "Postulate readiness 4.3/5" = một trong 5 tiêu chí scoring, đo sau hai case test PASS.
- Hai số KHÔNG mâu thuẫn — đo hai object khác nhau ở hai trạng thái lifecycle khác nhau. Narrow draft này dùng headline scoped 4.3/5 (chỉ readiness của bản nháp), KHÔNG promote thành "overall confidence" mới.

---

## Section 1 — Postulate Statement / Phát biểu đề xuất

**English:**
> A prior measurement window or data subset `W_j` from the candidate set `{W_i}` becomes registration-valid (`W_valid`) only when a final context `C_f`, together with a sorting/coincidence relation `S` when needed, supplies a valid inferential sign for `W_j`. This locking operation is a K-side classification rule: it determines which earlier window the registration state `K` is entitled to call the operative measurement window. E18 does NOT assert that the past quantum process is physically changed.

**Vietnamese:**
> Một cửa sổ đo hoặc subset dữ liệu `W_j` thuộc tập ứng viên `{W_i}` chỉ trở thành registration-valid (`W_valid`) khi bối cảnh cuối `C_f`, cùng với quan hệ sorting/coincidence `S` khi cần, cung cấp một dấu hiệu suy luận hợp lệ cho `W_j`. Thao tác khoá này là quy tắc phân loại phía K: nó xác định cửa sổ trước đó nào mà trạng thái ghi nhận `K` có quyền hợp lệ gọi là cửa sổ đo vận hành. E18 KHÔNG khẳng định tiến trình lượng tử quá khứ bị thay đổi vật lý.

### 1.1 One-Sentence Object (per `schema_guide.md`)

"E18 is the K-side classification rule that determines which prior candidate registration window earns the right to be called valid, given a final context and (when applicable) a sorting relation."

---

## Section 2 — Prose Statement / Diễn giải

**English:** Standard Quantum Mechanics (P1–P4) is silent on the K-side question raised by delayed-choice experiments: when a later measurement context arrives, which earlier candidate window is the operative valid registration window? E8 (Retroactive Registration Override) handles invalidation of a prior valid registration when a stronger incompatible registration arises ([vvv_qmrf_framework_e08_retroactive_registration_override_postulate.md:19](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/framework/vvv_qmrf_framework_e08_retroactive_registration_override_postulate.md#L19)). E13 (Temporal Discontinuity Registration) handles the bounded `ksana`-like nature of registration moments. The legacy E17 interface principle handles the separation between physical state transition `rho` and registration-state update `K`. None of these directly names the locking rule by which a context-conditioned final state classifies an earlier ambiguous window as the operative valid window.

The delayed-choice family (Wheeler 1978, Scully–Drühl 1982 quantum eraser) provides two case validations of this structural gap. The Wheeler case shows that a context-only locking rule `Lock(C_f, {W_i}) → W_valid` is sufficient for choosing between interference vs which-path windows. The quantum eraser case shows that a sorting relation `S` must be added when post-selection or coincidence sorting partitions raw detection events into valid subsets — yielding the refined `Lock(C_f, S, {W_i}) → W_valid`.

**Vietnamese:** Standard Quantum Mechanics (P1–P4) không nói gì về câu hỏi phía K mà delayed-choice đặt ra: khi bối cảnh đo sau xuất hiện, cửa sổ ứng viên trước đó nào là cửa sổ ghi nhận vận hành hợp lệ? E8, E13, và legacy E17 đều không đặt tên trực tiếp cho quy tắc khoá này. Hai case Wheeler và quantum eraser xác nhận gap. Quantum eraser cho thấy cần thêm quan hệ sorting `S` khi có post-selection hoặc coincidence sorting phân chia dữ liệu thô thành subset hợp lệ.

---

## Section 3 — Formal Sketch / Phác thảo Hình thức

```
Given:
  C_f     = final context / later measurement context
  {W_i}   = set of candidate prior registration windows or data subsets
  S       = sorting / coincidence / post-selection relation (when applicable)
  W_valid = selected valid registration window
  K       = registration state

E18 locking rule (refined):
  Lock(C_f, S, {W_i}) -> W_valid
  iff
  there exists W_j in {W_i} such that:
    I(C_f, S, W_j) = true                                    (valid inferential sign)
    R(C_f, W_j)    = true                                    (registration relevance)
    B(C_f, W_j)    = true                                    (K-side bounded)

Valid inferential sign condition:
  I(C_f, S, W_j) = true
  iff
  C_f together with S functions as a valid inferential sign for W_j
  in the Anumana-Vyapti analogical sense (structural analogue only).

Reduction to context-only case:
  When S is trivial (single-detection, no sorting):
    Lock(C_f, {W_i}) -> W_valid                              (Wheeler-type cases)

Non-claims (explicit):
  - E18 does NOT assert any physical change to past quantum dynamics rho(t<t_f).
  - E18 does NOT modify the Born rule or any P1-P4 postulate.
  - E18 does NOT permit superluminal or retrocausal signaling.
  - E18 operates only on the K-side classification layer.
```

---

## Section 4 — Architectural Position / Vị trí Kiến trúc

```
E8  (Retroactive Override)  -- invalidates prior registration when later incompatible arises
E13 (Temporal Discontinuity) -- bounds registration moments as ksana-like
E17 (Measurement Interface)  -- separates rho transition from K-side update
        |
        +--> E18 (Delayed-Choice Boundary) <-- THIS DRAFT
              E18: K-side rule for WHICH prior window earns registration-valid status
              when a final context C_f (with S if needed) supplies the locking condition
```

| Distinction | E8 | E13 | E17 | **E18 (this draft)** |
|---|---|---|---|---|
| Object | Invalidate prior valid registration | Bound registration moment | Separate rho ↔ K | **Classify which prior window is valid** |
| Trigger | Later incompatible stronger registration | Discrete ksana-like event | Any measurement step | **Later context C_f + sorting S** |
| Direction | Voids existing | Bounds duration | Layer interface | **Selects from candidate set** |
| Output | "Prior is voided" | "Moment is discrete" | "K is separate from rho" | **"`W_j` becomes `W_valid`"** |

---

## Section 5 — Source Traceability / Truy vết Nguồn

### 5.1 Buddhist Epistemology anchors (analogical only, not identity)

All BE anchors are used as **structural analogues**, not identity claims. Per `mapping/be15` schema model and CLAUDE.md "treat cross-domain links as analogies unless equivalence is explicitly justified."

| BE Node | Term | Source SOT line | Structural role for E18 | Identity boundary |
|---|---|---|---|---|
| N_BE_00003 | Anumāna (Inference) | [system_be_full.md:39](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/SYSTEM_Buddhist_Epistemology/system_be_full.md#L39) | Indirect knowledge through a sign (`liṅga`) — analogue for `I(C_f, S, W_j)` valid-sign structure | Analogical only — `C_f` is a measurement context, not a logical hetu in Dignāga's sense |
| N_BE_00019 | Vyāpti (Pervasion) | [system_be_full.md:55](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/SYSTEM_Buddhist_Epistemology/system_be_full.md#L55) | Pervasion relation between probans and probandum — analogue for the validity guarantee linking `C_f` and `W_j` | Analogical only — quantum context-window relation is not a logical universal pervasion |
| N_BE_00021 | Svabhāvapratibandha (Essential relation) | [system_be_full.md:57](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/SYSTEM_Buddhist_Epistemology/system_be_full.md#L57) | Dharmakīrti's universal foundation (tadutpatti / tādātmya) for inference — analogue for guarding against arbitrary context locking | Analogical only — no claim that delayed-choice locking is `tadutpatti` or `tādātmya` |
| N_BE_00135 | Arthakriyā (Successful activity) | [system_be_full.md:171](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/SYSTEM_Buddhist_Epistemology/system_be_full.md#L171) | Dharmakīrti's pragmatic truth criterion — analogue for "validity is not mere temporal order" | Analogical only — no ontological claim about causal efficacy in QM |

**User-supplied phrase note:** "Retroactive determination" is treated as a user-supplied interpretive phrase, NOT a direct BE SOT term. It is not used as an E18 anchor.

### 5.2 Standard Quantum Mechanics case references

| Case | Reference | Role for E18 |
|---|---|---|
| Wheeler delayed-choice (1978) | Used as case validation in [rca_e18 Section 10](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/rca/rca_e18_delayed_choice_registration_boundary.md#L422) | First case PASS — context-only locking sufficient |
| Scully–Drühl quantum eraser (1982) | Used as case validation in [rca_e18 Section 11](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/rca/rca_e18_delayed_choice_registration_boundary.md#L576) | Second case PASS — requires sorting `S` |

### 5.3 VVV-QMRF-EX compass note (no import)

Per `rca_e18.md:204`, EX flags `N_QM_VVV_00024` as "Registration-Locking Boundary in Delayed-Choice Erasure" but v1.7 reclassifies it as `KE-SC-RECLASSIFIED-v1.7` at score 3.7/5, below the 4.0 threshold, with `BR_EX_BE_00066` inactive (`k_gap_exception_list.md:73`). **EX therefore supports prioritizing this RCA but does NOT support importing a core edge.** EX is used as compass, not cargo.

---

## Section 6 — Symbol Table / Bảng Ký hiệu

| Symbol | Definition | Type | Domain |
|---|---|---|---|
| `C_f` | Final context — the later measurement context that arrives after the candidate windows | Context object | Set of measurement contexts on the same registering system |
| `S` | Sorting / coincidence / post-selection relation; applicable when raw detection is partitioned into valid subsets | Relation | Relations over raw-detection record sets |
| `W_i` | Candidate prior registration window or data subset | Window / subset | Set of windows in the registering system's pre-`C_f` history |
| `{W_i}` | The full candidate set under consideration | Set | Power set of registration windows |
| `W_j` | A specific candidate index in `{W_i}` selected by the locking rule | Window | `W_j ∈ {W_i}` |
| `W_valid` | The valid registration window resulting from successful locking | Window | The unique `W_j` selected by `Lock(C_f, S, {W_i})` |
| `K` | Registration state of the registering system | State | K-Space (see `K_Space_Axiomatization.md`) |
| `I(C_f, S, W_j)` | Valid-inferential-sign predicate | Boolean | True iff `C_f` + `S` functions as a valid inferential sign for `W_j` |
| `R(C_f, W_j)` | Registration-relevance predicate | Boolean | True iff `W_j` is relevant to the registration object pointed to by `C_f` |
| `B(C_f, W_j)` | K-side-bounded predicate | Boolean | True iff the proposed locking stays within K-side classification scope |

---

## Section 7 — Boundary & Non-Claims / Ranh giới & Phi-claim

### 7.1 What E18 narrow draft IS

1. A K-side classification rule for selecting `W_valid` from `{W_i}` given `C_f` and (when needed) `S`.
2. A registration-layer postulate proposal in the holding state `framework/drafts/`, awaiting promotion.
3. A structural addition that names a gap not covered by E8, E13, or legacy E17.
4. A draft consistent with the K-Space axiomatization (K1–K8) and recent T5/T6/T7 algebraic theorems.

### 7.2 What E18 narrow draft IS NOT

1. **NOT retrocausation.** Past physical quantum dynamics `rho(t < t_f)` are unchanged. Only K-side classification is updated when `C_f` arrives.
2. **NOT a modification of the Born rule** or any of the four physical postulates (P1–P4) of Standard Quantum Mechanics.
3. **NOT a permission for superluminal or retrocausal signaling.** Locking happens at the K-side classification layer, after `C_f` is locally available.
4. **NOT a frozen framework postulate.** This document is a holding-state draft. The framework index in `documents/research_documents/framework/index.md` is intentionally untouched.
5. **NOT an EX import.** EX entry `N_QM_VVV_00024` is below the v1.7 threshold and is used only as a compass signal.
6. **NOT a claim of identity between BE concepts and quantum context-window relations.** All BE anchors are structural analogues only.

### 7.3 Wording protocol (per `schema_guide.md` Section 0.0)

This draft uses neutral boundary language: "category boundary," "scope boundary," "registration-layer distinction." It does NOT frame Standard Quantum Mechanics as defective, mistaken, or in error.

---

## Section 8 — Promotion Path / Lộ trình Nâng cấp

E18 narrow draft → frozen framework postulate requires ALL of the following conditions, none of which are satisfied yet:

| Gate | Condition | Status | Evidence required |
|---|---|---|---|
| G1 | Two case validations PASS | **DONE** | `rca_e18.md:544-564` (Wheeler) + `rca_e18.md:744-759` (quantum eraser) |
| G2 | Formal locking rule with explicit `S` | **DONE** | Section 3 above + `rca_e18.md:709-731` |
| G3 | Boundary safety ≥ 4.0/5 | **DONE** | Boundary safety 4.3/5 per `rca_e18.md:756` |
| G4 | Third independent case validation | **DONE** | [rca/cases/e18_case_kim_1999.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/rca/cases/e18_case_kim_1999.md) — Kim et al. 1999 4-branch lock, 20/20 condition cells PASS |
| G5 | BE anchor decision | **DONE** | Parent RCA Section 13 accepts BE anchor as analogical-only permanent boundary; no physical-equivalence claim |
| G6 | EX recoverability check (does EX `N_QM_VVV_00024` cross 4.0 threshold after evidence?) | **DONE** | EX registry sync completed via [br_ex_be_registry.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/vvv-qmrf-ex/br_ex_be_registry.md) entries `BR_EX_BE_00070`-`BR_EX_BE_00072`. Path C valid-sign package scored 4.2/5; old `BR_EX_BE_00066` remains `RECLASSIFIED-v1.7` and inactive with supersession note. |
| G7 | User-authorized index insertion | **DONE** | User authorized G7 with Full scope on 2026-05-22; see [rca_core_extensibility_analysis.md Appendix C](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/rca/rca_core_extensibility_analysis.md) — 3-round RCA decision (R1=4.4, R2=4.8, R3=4.3, all PASS); file renamed from `..._narrow_draft.md` to `..._postulate.md` and moved into `framework/` root |

**All gates G1–G7 are PASS as of 2026-05-22. E18 is now a frozen extension postulate in `framework/` listed in `framework/index.md` Section 4.3 alongside E8–E16.** (G4 was advanced to DONE via `rca/cases/e18_case_kim_1999.md`; G5 was advanced to DONE by parent RCA Section 13 analogical-only BE anchor decision; G6 was advanced to DONE after EX registry sync via Path C; G7 was advanced to DONE via user authorization recorded in `rca_core_extensibility_analysis.md` Appendix C.)

---

## Section 9 — Verification Checklist (Rule Zero Step 5) / Danh mục Kiểm chứng

Per RULE ZERO Step 5 — verify root cause is removed, not just patched:

| Check | Result | Evidence |
|---|---|---|
| Confidence ambiguity root cause removed via lifecycle table | **PASS** | Section 0.1 lifecycle table makes 3.5 → 3.9 → 4.1 → 4.3 trajectory explicit |
| Headline scoped, not promoted to overall confidence | **PASS** | Section 0.1 explicitly labels 4.3/5 as "Narrow Draft Readiness," not "overall decision confidence" |
| File NOT in `framework/` root (per `rca_e18.md:243`) | **PASS** | Path = `framework/drafts/` |
| File NOT in framework index | **PASS** | `framework/index.md` untouched |
| Formula uses refined `Lock(C_f, S, {W_i})` not legacy `Lock(C_f, {W_i})` | **PASS** | Section 3 uses refined form; legacy noted only as reduction case |
| K-side scope only, no physical claim | **PASS** | Section 7.2 items 1–3 explicit |
| BE anchors marked analogical only | **PASS** | Section 5.1 every row has "Identity boundary" column |
| EX used as compass, not import | **PASS** | Section 5.3 explicit |
| Neutral wording (no "error/wrong/fallacy") | **PASS** | Section 7.3 + visual scan |
| Bilingual EN/VN per CLAUDE.md | **PASS** | Hybrid coverage per Q3 verdict (narrative/boundary bilingual; formal/citation EN-only) |
| Author metadata at top (file outside `published_documents`) | **PASS** | Line 1 |
| Disclaimer Class D at top | **PASS** | Lines 3-5 |
| Citations have line anchors | **PASS** | Parent-RCA line anchors refreshed after Section 7 lifecycle-note insertion |

---

## Section 10 — RCA Trace Summary / Tóm tắt RCA

### 10.1 Three-round decision gate applied during drafting

| Round | Decision | Score | Result |
|---|---|---:|---|
| R1 | Narrow draft scope = K-side classification only, NO physical/ontological claim | **4.5/5** | PASS (boundary safety) |
| R2 | Formula = refined `Lock(C_f, S, {W_i}) → W_valid`, NOT legacy `Lock(C_f, {W_i})` | **4.4/5** | PASS (internal necessity) |
| R3 | Headline confidence "Narrow Draft Readiness 4.3/5" consistent with lifecycle table | **4.5/5** | PASS (traceability) |

All three rounds cleared the 4.0/5 gate per the project decision rule.

### 10.2 Q1-Q2-Q3 verdict trace

| Question | Verdict | 3-round score | Recorded |
|---|---|---:|---|
| Q1 file location | `framework/drafts/` subfolder | 4.4/5 | Above (file path) |
| Q2 headline confidence | 4.3/5 scoped + Reconciliation Box | 4.5/5 | Section 0.1 |
| Q3 bilingual depth | Hybrid per RCA E18 precedent | 4.3/5 | Throughout |

---

## Section 11 — Open Questions for Future Sessions / Câu hỏi mở

1. **G4 closed by Kim 1999:** The third independent case validation is no longer open. Kim et al. (1999) delayed-choice quantum eraser closed G4 with a 4-branch lock and 20/20 condition cells PASS via `rca/cases/e18_case_kim_1999.md`.
2. **G5 closed by analogical-only BE anchor:** The BE anchor decision is no longer open. Parent RCA Section 13 accepts the Anumāna–Vyāpti–Svabhāvapratibandha chain as a permanent structural analogue only, not as physical equivalence.
3. **G6 EX recoverability check is DONE:** RCA `rca_e18_ex_vnext_bridge_audit.md` selected Path C at 4.2/5, and EX registry sync has now added active valid-sign package entries `BR_EX_BE_00070`-`BR_EX_BE_00072`. Old `BR_EX_BE_00066` remains `RECLASSIFIED-v1.7`, inactive, and preserved with a supersession note.
4. **G7 closed by user authorization on 2026-05-22:** User authorized G7 with Full scope via the 3-round RCA decision recorded in `rca_core_extensibility_analysis.md` Appendix C (R1=4.4, R2=4.8, R3=4.3, all PASS). E18 file renamed from `..._narrow_draft.md` to `..._postulate.md` and moved from `framework/drafts/` to `framework/`; `framework/index.md` Section 4.3 updated with the E18 row.

---

## Section 12 — Document Provenance / Nguồn gốc Tài liệu

- **Parent RCA:** [rca_e18_delayed_choice_registration_boundary.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/rca/rca_e18_delayed_choice_registration_boundary.md) (commit `cd0e6e2`, 2026-05-21).
- **Companion RCA:** [rca_core_extensibility_analysis.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/rca/rca_core_extensibility_analysis.md) Section A.1.1 (commit `b779117`, 2026-05-22) — flagged the confidence ambiguity resolved in Section 0.1 above.
- **Schema contract:** [vvv-qmrf/schema_guide.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/vvv-qmrf/schema_guide.md) — document creation contract followed for all sections.
- **BE SOT:** [SYSTEM_Buddhist_Epistemology/system_be_full.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/SYSTEM_Buddhist_Epistemology/system_be_full.md) — single source of truth for N_BE_00003, N_BE_00019, N_BE_00021, N_BE_00135.
- **Framework precedent:** [vvv_qmrf_framework_e16_pre_measurement_registration_indeterminacy_postulate.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/framework/vvv_qmrf_framework_e16_pre_measurement_registration_indeterminacy_postulate.md) — structural template followed for sections 1–7.

---

© 2026 VietVunVut (Viet - Nguyen Xuan). Licensed under CC BY 4.0.
To view a copy of this license, visit https://creativecommons.org/licenses/by/4.0/
