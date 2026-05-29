Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

> **DISCLAIMER / CANH BAO:** VVV-QMRF is independent Class D personal research, not Standard Quantum Mechanics, not peer-reviewed or experimentally validated, and not for real-world technical use. This document is an RCA report, not a new postulate and not a physical theory.
>
> VVV-QMRF la nghien cuu ca nhan doc lap o Class D, khong phai "Standard Quantum Mechanics", chua "peer-reviewed" hoac kiem chung thuc nghiem, va khong dung cho ung dung ky thuat ngoai thuc te. Tai lieu nay la bao cao RCA, khong phai tien de moi va khong phai ly thuyet vat ly.

# RCA for E18 Candidate — Delayed-Choice Registration Boundary

**Scope:** VVV-QMRF core  
**Candidate:** E18 "Delayed-choice registration boundary"  
**Focus:** Locking-point when later context changes which prior measurement window counts as registration-valid  
**Method:** RULE ZERO RCA — Define, Trace, Isolate, Fix the cause, Verify  
**EX use:** VVV-QMRF-EX is used as "EX-compass-only, not core-imported"

---

## Section 0 — Executive Summary

**Root cause isolated:** R2 — structural gap / khoang trong cau truc, but only as a **candidate boundary principle**, not yet as a full framework postulate.

The E18 candidate appears because delayed-choice cases expose a registration-layer question that is not identical to E8, E13, or the legacy E17 interface principle. E8 covers retroactive invalidation of a prior registration when a later incompatible registration arises. E13 covers the discreteness of registration moments. The legacy E17 interface principle separates physical state transition `rho` from registration-state update `K`. None of these directly names the rule for when a later measurement context determines which earlier window is the valid registration window.

**Recommendation:** Create this RCA report and mark E18 as **RCA-supported candidate, not yet framework-postulate**. The next step, if requested, should be a narrow framework proposal only after defining the locking object precisely: not "the past changes," but "the registration-valid window is fixed by the final context that supplies a valid registration condition."

**Decision confidence:** 3.8/5. The gap is stronger than a documentation-only issue because EX independently flags `N_QM_VVV_00024` as "Registration-Locking Boundary in Delayed-Choice Erasure." However, EX v1.7 reclassified that entry below the 4.0 threshold with a thin boundary, so the core must not import it directly. The correct status is candidate retention, not immediate postulate creation.

**Tom tat VN:** Nguyen nhan goc khong phai "qua khu bi thay doi". Nguyen nhan goc la khung VVV-QMRF chua co ten rieng cho diem khoa cua cua so ghi nhan hop le trong delayed-choice: boi canh ve sau khong doi vat ly qua khu, ma quy dinh cua so nao duoc tinh la "valid registration" o tang K.

---

## Section 1 — Define: Symptom vs Cause

### Symptom / Trieu chung

A new E18 candidate is proposed as "Delayed-choice registration boundary": a locking-point where later context retroactively changes the valid measurement window. The user also proposes "Retroactive determination" in Dharmakirti as the Buddhist Epistemology anchor.

VN: De xuat E18 xuat hien vi trong delayed-choice, cach bo tri / boi canh do ve sau co ve nhu quyet dinh lai y nghia cua su kien truoc do. Cach noi de hieu nham la "qua khu bi doi". Cach doc trong VVV-QMRF phai la: cua so nao duoc tinh la "registration-valid" o tang K?

### Apparent cause / Nguyen nhan be mat

The apparent cause is that delayed-choice language sounds retroactive. Because VVV-QMRF already has E8 "Retroactive Registration Override," it is tempting to route the whole issue to E8. But that would treat the visible word "retroactive" as the root cause.

VN: Nguyen nhan be mat la chu "retroactive" lam ta nghi ngay den E8. Nhung RCA khong duoc bam vao tu khoa; phai hoi: co phai dang huy bo ket qua cu, hay dang xac dinh cua so nao moi du dieu kien ghi nhan?

### Source-anchor clarification / Lam ro neo nguon

The exact phrase "Retroactive determination" is treated here as a **user-supplied interpretive phrase**, not as a direct BE SOT term. The nearest verified anchors are:

| Anchor | Verified role | Use in this RCA |
|---|---|---|
| `Badhaka pramana` / invalidating cognition | Used by E8 for retroactive override when a stronger incompatible registration arises (`vvv_qmrf_framework_e08_retroactive_registration_override_postulate.md:34`). | Boundary comparator, not direct E18 anchor. |
| `N_BE_00029` / Momentariness | EX links delayed-choice locking to momentariness, but reclassifies the bridge below the v1.7 threshold (`k_gap_exception_list.md:73`). | Compass signal only. |
| `N_BE_00003` / Anumana | Indirect knowledge through reasoning based on a sign (`system_be_full.md:39`). | Supports context-conditioned registration only if the final context functions as a valid sign. |
| `N_BE_00019` / Vyapti and `N_BE_00021` / Svabhavapratibandha | Pervasion and essential relation ground inference (`system_be_full.md:55`, `system_be_full.md:57`). | Guard against treating arbitrary later context as valid. |
| `N_BE_00135` / Arthakriya | Successful activity and pragmatic truth/causal efficacy in Dharmakirti (`system_be_full.md:171`). | Helps express why validity is not mere temporal order. |

---

## Section 2 — Trace: 5 Whys

### Why 1 — Why does E18 seem needed?

Because delayed-choice experiments make the registration meaning of an earlier event depend on a later measurement context. The earlier event is not simply valid or invalid in isolation; its registration class becomes clear only when the later context supplies the operative measurement basis.

VN: E18 co ve can thiet vi su kien truoc chua du tu no de noi "da ghi nhan cai gi". Boi canh sau moi lam ro cua so do nao la cua so hop le.

### Why 2 — Why is this not just E8?

E8 says a prior measurement `M1` is not permanently registration-valid, and a later incompatible `M2` can retroactively void its registration validity (`vvv_qmrf_framework_e08_retroactive_registration_override_postulate.md:19`). E8 is an **invalidation** rule: prior registration authority becomes void (`vvv_qmrf_framework_e08_retroactive_registration_override_postulate.md:56`).

Delayed-choice registration boundary is different. It is not primarily saying "M1 was invalid." It asks: under the final context, which temporal window and measurement basis count as the valid registration object?

VN: E8 la "phu quyet". E18-candidate la "khoa cua so". Mot ben huy tinh hop le da co; mot ben xac dinh cua so nao moi du dieu kien de goi la ghi nhan hop le.

### Why 3 — Why is this not just E13?

E13 treats quantum state transitions as registration-layer discontinuities, bounded `ksana`-like moments, while preserving continuous physical dynamics between registration events (`vvv_qmrf_framework_e13_temporal_discontinuity_registration_postulate.md:19`). E13 explains that registration events can be bounded moments, not zero-duration physics (`vvv_qmrf_framework_e13_temporal_discontinuity_registration_postulate.md:32`).

Delayed-choice needs more than moment-bounding. It needs a rule for **which** moment-window becomes registration-valid after the final context is known.

VN: E13 noi "co bien thoi diem ghi nhan". E18-candidate noi "bien nao duoc khoa thanh cua so hop le khi boi canh sau xuat hien".

### Why 4 — Why is this not just the legacy E17 interface principle?

The legacy E17 interface principle says measurement is an interface between physical state transition `rho` and registration-state update `K` (`vvv_qmrf_framework_e17_measurement_interface_postulate.md:19`). It also identifies the root cause as lack of formal separation between `rho` and `K` (`vvv_qmrf_framework_e17_measurement_interface_postulate.md:33`).

This separation is necessary but not sufficient. Once `rho` and `K` are separated, delayed-choice still asks which context supplies the locking condition for `K`.

VN: E17 cu giup tach tang vat ly va tang ghi nhan. Nhung sau khi tach roi, van can hoi: boi canh nao khoa cua so ghi nhan?

### Why 5 — What caused the gap to appear?

The framework already has mechanisms for invalidation (E8), temporal bounding (E13), and rho/K separation (legacy E17), but it lacks an explicit registration-layer rule for **context-conditioned locking** of a valid measurement window.

VN: Khoang trong bat dau o cho khung da co cac vien gach rieng le, nhung chua co cau noi: "boi canh sau khong doi qua khu vat ly; no khoa cua so ghi nhan hop le o tang K."

---

## Section 3 — Isolate

### Candidate review

| Candidate | Evidence outcome | RCA status |
|---|---|---|
| R1 — Redundancy with E8 | Partly plausible because both use retroactive language. Not sufficient because E8 voids prior validity, while delayed-choice can select a registration basis/window without declaring a prior detector event invalid. | Not selected |
| **R2 — Structural gap / context-conditioned locking** | Best supported. E8, E13, and legacy E17 each cover nearby structure, but no active postulate names the context-conditioned locking of a valid measurement window. EX independently flags `N_QM_VVV_00024`, but only as compass evidence. | **Selected** |
| R3 — Category boundary only | Important guard. The RCA must not claim that future context physically changes the past. But this guard does not remove the K-side boundary question. | Boundary guard, not root cause |
| R4 — Documentation gap only | Plausible if E8/E13/E17 were enough. But EX flags the same region as a stress point, and the selection-vs-invalidation distinction remains structurally real. | Not selected as final |

### Decision Matrix — Good / Bad / Risk

| Option | Good / Strength | Bad / Weakness | Main risk | Decision impact |
|---|---|---|---|---|
| Treat E18 as redundant with E8 | Protects framework from duplicate postulates. | Collapses selection into invalidation. | Losing the delayed-choice window question. | Reject as too coarse. |
| Treat E18 as structural gap | Names the missing rule: context-conditioned registration locking. | Needs careful boundary guard against "changing the past." | Overclaiming if formalized too fast. | Best current RCA conclusion. |
| Treat E18 as only category boundary | Avoids physical overclaim. | Does not explain why E8/E13/E17 still leave a reader question. | Underbuilding the core. | Keep as guard. |
| Treat E18 as documentation gap | Minimal edit path. | EX and internal comparison suggest more than wording. | Hiding a real K-side locking distinction. | Defer as fallback only. |

### Root cause / Nguyen nhan goc

**Root cause:** The active VVV-QMRF core does not yet explicitly define how a later measurement context locks the valid registration window of an earlier ambiguous measurement sequence.

VN: Nguyen nhan goc la core chua co quy tac noi ro: boi canh do ve sau khoa cua so ghi nhan hop le cua chuoi do truoc do nhu the nao.

### One-sentence isolation

E18 is not about changing the past physical event; it is about when the registration-state `K` becomes entitled to classify a prior temporal window as the valid measurement window under a later-specified context.

VN: E18 khong noi qua khu vat ly bi doi; E18 noi luc nao `K` du quyen phan loai cua so truoc do la cua so do hop le khi boi canh sau da duoc xac lap.

---

## Section 4 — Fix the Cause, Not the Symptom

### Proposed fix / De xuat sua nguyen nhan

Do **not** immediately create a framework E18 postulate. First preserve this RCA as the boundary document. If promoted later, E18 should be written narrowly as:

> **Candidate E18 statement:** A prior measurement interval becomes registration-valid only when the final measurement context supplies the condition that locks which observable, basis, or window is being registered. This locking is a K-side classification rule, not a physical claim that the past quantum process is changed.

VN:

> **Phat bieu ung vien E18:** Mot khoang do truoc do chi tro thanh "registration-valid" khi boi canh do cuoi cung cung cap dieu kien khoa xem observable, basis, hoac cua so nao dang duoc ghi nhan. Viec khoa nay la quy tac phan loai phia K, khong phai tuyen bo vat ly rang qua khu bi thay doi.

### Formal sketch / Phac thao hinh thuc

```text
Events:
  t1..t2 = earlier ambiguous measurement interval
  C_f    = final measurement context / later choice
  W_i    = candidate registration windows
  K      = registration state

Context-conditioned locking:
  Before C_f:
    K(W_i) = registration-underdetermined

  After C_f:
    Lock(C_f, {W_i}) -> W_valid
    U_K(K, W_valid) -> registration-state update

Boundary:
  This does not imply physical retrocausation.
  It means the valid K-side registration window is fixed only after the context condition is complete.
```

### Boundary rules / Quy tac ranh gioi

1. **No physical retrocausation claim.** Later context does not physically alter the past event in this RCA.
2. **No replacement of Standard QM.** Born-rule probabilities and physical dynamics remain in the physical layer.
3. **No EX import.** EX only identifies the delayed-choice locking region as a stress point.
4. **No fake Dharmakirti term.** "Retroactive determination" is treated as interpretive wording unless a direct SOT phrase is later found.

---

## Section 5 — Verify

### Verification against E8

E8 covers retroactive invalidation: a later incompatible `M2` voids `M1` (`vvv_qmrf_framework_e08_retroactive_registration_override_postulate.md:19`, `vvv_qmrf_framework_e08_retroactive_registration_override_postulate.md:56`). E18-candidate covers context-conditioned selection/locking of a valid window. Therefore E18 is not reducible to E8 unless the delayed-choice case is specifically framed as invalidating a prior registration.

**Pass.** Root cause not removed by E8 alone.

### Verification against E13

E13 provides bounded registration discontinuities (`vvv_qmrf_framework_e13_temporal_discontinuity_registration_postulate.md:19`, `vvv_qmrf_framework_e13_temporal_discontinuity_registration_postulate.md:32`). E18-candidate requires a rule for choosing which window becomes valid after context completion. Therefore E13 supplies timing ontology but not the locking rule.

**Pass.** Root cause not removed by E13 alone.

### Verification against legacy E17

The legacy E17 interface principle separates `rho` transition from `K` update (`vvv_qmrf_framework_e17_measurement_interface_postulate.md:19`, `vvv_qmrf_framework_e17_measurement_interface_postulate.md:33`). E18-candidate lives inside the `K` side after that separation. Therefore E17 is prerequisite architecture, not the specific delayed-choice rule.

**Pass.** Root cause not removed by E17 alone.

### Verification against BE SOT

The phrase "Retroactive determination" is not treated as a direct SOT term. The RCA instead uses verified anchors: inference (`N_BE_00003`), pervasion (`N_BE_00019`), essential relation (`N_BE_00021`), momentariness (`N_BE_00029` as EX compass), and Arthakriya (`N_BE_00135`).

**Pass with caution.** BE anchor is interpretive and must remain explicitly bounded.

### Verification against EX compass

VVV-QMRF-EX flags `N_QM_VVV_00024` as "Registration-Locking Boundary in Delayed-Choice Erasure" (`vvv_qmrf_ex_gaps.md:34`). But v1.7 reclassifies it as `KE-SC-RECLASSIFIED-v1.7`, score 3.7/5, below the 4.0 threshold, with `BR_EX_BE_00066` inactive (`k_gap_exception_list.md:73`). Therefore EX supports prioritizing RCA but not importing a core edge.

**Pass.** EX is used as compass, not cargo.

---

## Section 6 — Routing Table

| If delayed-choice means... | Route to | Reason |
|---|---|---|
| A later result proves an earlier claimed registration was incompatible and must be voided. | **E8** | This is retroactive registration override / Badhaka-style invalidation. |
| The issue is that registration occurs in discrete bounded moments. | **E13** | This is temporal discontinuity / `ksana`-like registration bounding. |
| The issue is separating physical transition from K-side registration. | **Legacy E17 / interface principle** | This is rho/K interface separation. |
| The issue is that later context locks which earlier window counts as registration-valid. | **E18 candidate** | This is context-conditioned registration-window locking. |
| The claim says future context physically changes the past. | **Reject / boundary guard** | This exceeds VVV-QMRF registration-layer scope. |

---

## Section 7 — Decision

**Decision:** Keep E18 as an RCA-supported candidate, not yet a formal framework postulate.

**Score:** 3.8/5

**Confidence lifecycle note (RCA Step 5):** This 3.8/5 is the original overall decision confidence for candidate retention at RCA creation time. It is not the later Section 11.10 sub-metric "Postulate readiness: 4.3/5" after Wheeler and quantum eraser case validation. The two numbers measure different objects: overall decision-state vs post-test postulate-readiness. This distinction is reconciled in the E18 postulate Confidence Reconciliation Box (`vvv_qmrf_framework_e18_delayed_choice_registration_boundary_postulate.md:28-51`, promoted from narrow draft via G7 user authorization on 2026-05-22).

**VN:** Diem 3.8/5 nay la confidence tong the luc tao RCA va quyet dinh giu E18 o muc candidate. No khong phai sub-metric "Postulate readiness: 4.3/5" o Section 11.10 sau hai case test. Hai so do hai object khac nhau: trang thai quyet dinh tong the va muc san sang cua postulate sau test.

| Criterion | Score | Note |
|---|---:|---|
| Internal necessity | 4.0 | E8/E13/E17 do not directly name context-conditioned locking. |
| BE anchor strength | 3.3 | Anchors are real, but "Retroactive determination" is not directly verified as a SOT term. |
| EX support | 3.7 | EX flags the stress point but reclassifies it below v1.7 threshold. |
| Boundary safety | 4.2 | The RCA can keep the claim safely in K-side scope. |
| Postulate readiness | 3.5 | Ready for candidate preservation, not ready for full framework elevation. |

### Recommendation / Khuyen nghi

1. Preserve this RCA as the canonical E18 candidate analysis.
2. Do not create `vvv_qmrf_framework_e18_...md` yet.
3. If promoted later, define E18 as **Delayed-Choice Registration Boundary Postulate** with a strict non-retrocausal boundary.
4. Add a future boundary note to E8/E13/E17 only if the user wants framework synchronization.

---

## Section 8 — Final RCA Statement

**English:** The E18 candidate is justified as a registration-layer boundary problem because delayed-choice cases require a rule for when a later context locks the valid registration window of an earlier ambiguous interval. This is not E8 invalidation, not E13 temporal discontinuity alone, and not merely the legacy E17 rho/K interface. However, because the BE anchor is interpretive and EX reclassifies the corresponding bridge below the v1.7 threshold, E18 should remain an RCA-supported candidate rather than an active framework postulate.

**Vietnamese:** Ung vien E18 co ly do ton tai vi delayed-choice can mot quy tac o tang ghi nhan: khi nao boi canh sau khoa cua so ghi nhan hop le cua mot khoang truoc do con mo ho. No khong trung voi E8, khong chi la E13, va khong chi la E17 cu. Tuy nhien, vi neo BE con mang tinh dien giai va EX v1.7 ha muc bridge tuong ung xuong duoi nguong 4.0, E18 nen duoc giu o muc RCA-supported candidate, chua nen nang thanh postulate chinh thuc.

---

## Section 9 — Formal Conditions for `Lock(C_f, {W_i}) -> W_valid`

### 9.1 RCA purpose / Muc dich RCA

This section extends the E18 RCA by defining the minimal formal conditions under which a later context `C_f` may lock one candidate prior registration window `W_j` as the valid window `W_valid`.

VN: Section nay bo sung dieu kien hinh thuc toi thieu de mot boi canh sau `C_f` co quyen khoa mot cua so ghi nhan ung vien `W_j` thanh cua so hop le `W_valid`.

The root issue is not physical retrocausation. The root issue is **registration entitlement**: when does `K` have enough valid context to classify an earlier ambiguous interval as the operative measurement window?

VN: Van de goc khong phai tuong lai doi qua khu vat ly. Van de goc la **quyen hop le cua tang ghi nhan**: khi nao `K` co du boi canh hop le de phan loai mot khoang truoc do con mo ho thanh cua so do dang van hanh?

### 9.2 Formal definition / Dinh nghia hinh thuc

```text
Given:
  C_f     = final context / later measurement context
  {W_i}   = set of candidate prior registration windows
  W_valid = selected valid registration window
  K       = registration state

Lock(C_f, {W_i}) -> W_valid
iff
there exists W_j in {W_i} such that:

  R(C_f, W_j) = true
  B(C_f, W_j) = true
  T(W_j, C_f) = true
  I(C_f, W_j) = true
  G(C_f, W_j) = true

and no competing W_k has stronger or equal registration specificity under C_f.
```

If no `W_j` satisfies all five conditions, `Lock(C_f, {W_i})` is undefined. If more than one `W_j` satisfies all five conditions with equal specificity, the registration window remains underdetermined.

VN: Neu khong co `W_j` nao dat du 5 dieu kien, `Lock(C_f, {W_i})` khong xac dinh. Neu nhieu `W_j` cung dat va dac hieu ngang nhau, cua so ghi nhan van o trang thai chua duoc xac dinh.

### 9.3 Five locking conditions / Nam dieu kien khoa

| Condition | Formal role | Plain meaning | If it fails |
|---|---|---|---|
| `R(C_f, W_j)` | Context relevance | `C_f` must be relevant to the candidate window `W_j`. | No lock; the later context is unrelated. |
| `B(C_f, W_j)` | Basis specification | `C_f` must specify the observable, basis, or registration class for `W_j`. | No lock; the context does not say what is being registered. |
| `T(W_j, C_f)` | Temporal admissibility | `W_j` must belong to the same admissible measurement sequence as `C_f`. | No lock; the window is outside the valid sequence. |
| `I(C_f, W_j)` | Inferential validity | `C_f` must function as a valid sign for `W_j`, not as arbitrary later information. | No lock; the context is not a valid registration reason. |
| `G(C_f, W_j)` | Boundary guard | The lock must remain K-side registration classification only. | Reject or downgrade; the claim exceeds VVV-QMRF scope. |

VN: Nam dieu kien nay ngan E18 bi hieu thanh "tuy tien chon cua so" hoac "tuong lai doi qua khu". `C_f` chi duoc khoa `W_j` khi no lien quan dung, chi ra basis/observable, nam trong cung chuoi do, co gia tri suy luan hop le, va khong vuot qua ranh gioi tang K.

### 9.4 Condition R — Context relevance

```text
R(C_f, W_j) = true
iff
C_f can meaningfully classify W_j within the same measurement question.
```

`C_f` must address the same measurement question as `W_j`. A later context from a separate run, separate apparatus chain, or unrelated observable cannot lock `W_j`.

VN: `C_f` phai tra loi cung cau hoi do voi `W_j`. Boi canh sau cua mot lan chay khac, chuoi may do khac, hoac observable khong lien quan thi khong co quyen khoa `W_j`.

### 9.5 Condition B — Basis specification

```text
B(C_f, W_j) = true
iff
C_f determines the observable, basis, or registration class under which W_j is evaluated.
```

This condition prevents any later event from being treated as a valid locking context. The later context must specify how the prior interval is to be read at the registration layer.

VN: Dieu kien nay chan viec xem moi su kien xay ra sau la boi canh hop le. Boi canh sau phai chi ro khoang truoc do duoc doc theo observable, basis, hoac lop ghi nhan nao.

### 9.6 Condition T — Temporal admissibility

```text
T(W_j, C_f) = true
iff
W_j lies inside the causal-registration sequence to which C_f belongs.
```

`W_j` may be earlier than `C_f`, but it must not be external to the same measurement sequence. This preserves the registration-layer boundary without implying physical retrocausation.

VN: `W_j` co the xay ra truoc `C_f`, nhung khong duoc nam ngoai cung chuoi do. Dieu nay giu E18 o tang ghi nhan, khong bien no thanh tuyên bo vat ly ve viec doi qua khu.

### 9.7 Condition I — Inferential validity

```text
I(C_f, W_j) = true
iff
C_f functions as a valid inferential sign for W_j under registration-validity conditions.
```

A conservative VVV-QMRF version may express this through a Trairupya-like test:

```text
Paksha condition:
  C_f applies to the measurement sequence under consideration.

Sapaksha condition:
  C_f supports W_j in comparable valid registration cases.

Vipaksha condition:
  C_f does not support incompatible W_k cases.
```

This uses Buddhist Epistemology as a structural analogue for validity, not as a claim that the Buddhist theory is identical to quantum physics. The relevant SOT anchors are inference (`N_BE_00003`), pervasion (`N_BE_00019`), and essential relation (`N_BE_00021`).

VN: `C_f` phai la dau hieu suy luan hop le, khong phai thong tin ve sau mot cach ngau nhien. Day la cho neo vao BE logic: `Anumana`, `Vyapti`, va `Svabhavapratibandha`, nhung chi la analog cau truc, khong phai dong nhat BE voi vat ly luong tu.

### 9.8 Condition G — Boundary guard

```text
G(C_f, W_j) = true
iff
Lock(C_f, W_j) does not imply:
  - physical retrocausation;
  - modification of the Born rule;
  - replacement of Standard Quantum Mechanics;
  - direct import of VVV-QMRF-EX bridge structures into the core.
```

This condition is mandatory. If a proposed E18 formulation says or implies that the later context physically changes the earlier quantum process, it fails the boundary guard.

VN: Dieu kien nay bat buoc. Neu mot phat bieu E18 noi hoac ngam y rang boi canh sau lam thay doi tien trinh vat ly truoc do, no khong dat boundary guard.

### 9.9 Specificity rule / Quy tac dac hieu

When more than one candidate window satisfies the five conditions, the framework should select the most specific valid window only if specificity is well-defined.

```text
W_valid = argmax_Wi Specificity(C_f, W_i)
subject to:
  R, B, T, I, G all pass.
```

If specificity is not well-defined, the result is not forced:

```text
Lock(C_f, {W_i}) -> underdetermined
```

VN: Neu co nhieu cua so cung dat dieu kien, chi chon cua so dac hieu nhat khi tieu chuan "dac hieu" da ro. Neu chua ro, khong duoc ep chon; phai giu trang thai underdetermined.

### 9.10 RCA decision impact / Tac dong len quyet dinh RCA

This Section 9 raises the postulate-readiness of E18 but does not fully promote it to a framework postulate. The new formal conditions improve the candidate because they define what was previously missing: the rule by which `C_f` earns the right to lock `W_valid`.

VN: Section 9 lam E18 manh hon, nhung chua tu dong bien E18 thanh postulate chinh thuc. No bo sung dung phan thieu: quy tac de `C_f` co quyen khoa `W_valid`.

| Criterion | Before Section 9 | After Section 9 | RCA note |
|---|---:|---:|---|
| Internal necessity | 4.0 | 4.1 | The missing locking rule is now explicit. |
| BE anchor strength | 3.3 | 3.6 | `I(C_f, W_j)` gives a clearer link to inference and valid sign structure. |
| EX support | 3.7 | 3.7 | Unchanged; EX remains compass-only. |
| Boundary safety | 4.2 | 4.4 | `G(C_f, W_j)` makes the non-retrocausal boundary explicit. |
| Postulate readiness | 3.5 | 3.9 | Stronger candidate, still needs case testing before framework elevation. |

**Updated RCA status:** E18 remains **RCA-supported candidate**, now with formal locking conditions. It should still not be promoted to a framework postulate until tested against at least one concrete delayed-choice or delayed-choice-erasure case.

VN: Trang thai cap nhat: E18 van la **RCA-supported candidate**, nay da co dieu kien khoa hinh thuc. Van chua nen nang thanh postulate framework cho den khi test tren it nhat mot case cu the ve delayed-choice hoac delayed-choice erasure.

---

## Section 10 — Case Test 1: Wheeler Delayed-Choice Interferometer

### 10.1 Purpose / Muc dich

This section tests whether the Section 9 locking rule can operate on a concrete delayed-choice case: the Wheeler delayed-choice interferometer. The purpose is not to prove a new physical claim, but to test whether E18 can classify a valid K-side registration window without collapsing into E8, E13, or the legacy E17 interface principle.

VN: Section nay test xem quy tac khoa o Section 9 co chay duoc tren mot case cu the khong: Wheeler delayed-choice interferometer. Muc dich khong phai chung minh vat ly moi, ma la xem E18 co phan loai duoc cua so ghi nhan hop le phia `K` ma khong bi trung voi E8, E13, hoac E17 cu hay khong.

### 10.2 Minimal setup / Thiet lap toi gian

```text
Photon source
  -> first beam splitter BS1
  -> two possible path arms
  -> final context C_f:
       Case A: second beam splitter BS2 absent
       Case B: second beam splitter BS2 inserted
  -> detectors D0 / D1
```

The final context `C_f` determines the registration basis:

| Final context `C_f` | Registration reading | Candidate window |
|---|---|---|
| `no_BS2` | which-path / particle-like registration | `W_path` |
| `BS2_inserted` | interference / wave-like registration | `W_interference` |

Boundary note: this RCA does not claim that the later BS2 choice physically changes the photon's past. It only tests whether the final context can lock the K-side registration window.

VN: Ghi chu ranh gioi: RCA nay khong noi lua chon BS2 ve sau lam thay doi qua khu vat ly cua photon. No chi test xem boi canh cuoi co khoa duoc cua so ghi nhan phia `K` hay khong.

### 10.3 Variable mapping / Anh xa bien

| E18 symbol | Wheeler case | Meaning |
|---|---|---|
| `C_f` | Final BS2 context: `no_BS2` or `BS2_inserted` | Later measurement context |
| `{W_i}` | `{W_path, W_interference}` | Candidate prior registration windows |
| `W_path` | Which-path registration window | Path-basis reading |
| `W_interference` | Interference registration window | Interference-basis reading |
| `W_valid` | Window selected by `C_f` | Valid K-side registration window |
| `K` | Registration state | State updated after valid window locking |

Before `C_f` is fixed, the registration state remains underdetermined between candidate windows:

```text
Before C_f:
  K({W_path, W_interference}) = registration-underdetermined
```

After `C_f` is fixed, a valid lock may occur if all Section 9 conditions pass.

### 10.4 Branch A — `C_f = no_BS2`

Expected lock:

```text
Lock(no_BS2, {W_path, W_interference}) -> W_path
```

Five-condition test:

| Condition | RCA question | Result |
|---|---|---|
| `R(no_BS2, W_path)` | Is `no_BS2` relevant to path registration? | PASS |
| `B(no_BS2, W_path)` | Does `no_BS2` specify the path/which-path registration class? | PASS |
| `T(W_path, no_BS2)` | Is `W_path` inside the same measurement sequence as `no_BS2`? | PASS |
| `I(no_BS2, W_path)` | Does `no_BS2` function as a valid sign for path registration under the protocol? | PASS, protocol-dependent |
| `G(no_BS2, W_path)` | Does the claim stay within K-side registration classification? | PASS |

RCA note: Branch A does not say a later absence of BS2 rewrites the photon history. It says the final apparatus context licenses a path-basis registration reading.

VN: Nhanh A khong noi viec khong co BS2 ve sau viet lai lich su photon. No noi boi canh may do cuoi cho phep doc ghi nhan theo path-basis.

### 10.5 Branch B — `C_f = BS2_inserted`

Expected lock:

```text
Lock(BS2_inserted, {W_path, W_interference}) -> W_interference
```

Five-condition test:

| Condition | RCA question | Result |
|---|---|---|
| `R(BS2_inserted, W_interference)` | Is inserted BS2 relevant to interference registration? | PASS |
| `B(BS2_inserted, W_interference)` | Does inserted BS2 specify the interference registration class? | PASS |
| `T(W_interference, BS2_inserted)` | Is `W_interference` inside the same measurement sequence as inserted BS2? | PASS |
| `I(BS2_inserted, W_interference)` | Does inserted BS2 function as a valid sign for interference registration under the protocol? | PASS, protocol-dependent |
| `G(BS2_inserted, W_interference)` | Does the claim stay within K-side registration classification? | PASS |

RCA note: Branch B does not say the photon physically becomes wave-like in the past. It says the final context licenses an interference-basis registration reading.

VN: Nhanh B khong noi photon ve mat vat ly tro thanh "wave-like" trong qua khu. No noi boi canh cuoi cho phep doc ghi nhan theo interference-basis.

### 10.6 Five-condition result / Ket qua 5 dieu kien

| Condition | Branch A: `no_BS2 -> W_path` | Branch B: `BS2_inserted -> W_interference` | RCA implication |
|---|---|---|---|
| `R` | PASS | PASS | Final context is relevant to the selected window. |
| `B` | PASS | PASS | Final context specifies the registration class. |
| `T` | PASS | PASS | Candidate window belongs to the same measurement sequence. |
| `I` | PASS with protocol | PASS with protocol | Validity depends on the experimental protocol, not arbitrary later information. |
| `G` | PASS | PASS | The reading remains non-retrocausal and K-side only. |

**Case result:** Wheeler delayed-choice passes the first E18 case test under a conservative registration-layer interpretation.

VN: Ket qua case: Wheeler delayed-choice pass test dau tien cho E18 neu dien giai bao thu o tang ghi nhan, khong vuot sang retrocausation vat ly.

### 10.7 RCA 5 Whys for Wheeler case

1. **Why does E18 seem needed here?** Because before `C_f`, the registration state is underdetermined between `W_path` and `W_interference`.
2. **Why is this not E8?** Because no prior valid registration is being voided; the final context selects the registration basis/window.
3. **Why is this not E13?** Because E13 supplies temporal bounding, but not the rule selecting which candidate window becomes valid.
4. **Why is this not legacy E17?** Because E17 separates `rho` from `K`, but does not define context-conditioned window locking inside `K`.
5. **Root cause:** The Wheeler case exposes the missing rule for context-conditioned registration-window locking.

VN: RCA 5 Whys cho thay Wheeler khong buoc ta noi qua khu vat ly bi doi. No chi buoc ta bo sung quy tac: khi boi canh cuoi da ro, cua so ghi nhan nao duoc khoa thanh hop le?

### 10.8 Good / Bad / Risk table

| Aspect | Good / Strength | Bad / Weakness | Risk control |
|---|---|---|---|
| Clarity | Two branches are simple: `no_BS2` and `BS2_inserted`. | Simpler than delayed-choice quantum eraser, so it may not stress-test all E18 cases. | Use as first test only, not final proof. |
| E18 fit | Directly tests basis/window locking. | Could be misread as a physical claim about the photon path. | Keep all claims at K-side registration classification. |
| Distinction from E8 | Shows selection is not the same as invalidation. | Some readers may still focus on the word "delayed." | State explicitly: no prior registration is voided. |
| Distinction from E13 | Shows timing is necessary but insufficient. | E13 remains a supporting layer and may blur with E18. | State E13 bounds moments; E18 locks the valid window. |
| BE anchor | `I(C_f, W_j)` can be read through valid-sign structure. | BE anchor remains analogical, not identity. | Use `Anumana`, `Vyapti`, and `Svabhavapratibandha` only as structural analogues. |
| Boundary safety | No retrocausal claim is required. | Popular delayed-choice language can invite overclaim. | Repeat the non-retrocausal boundary guard. |

### 10.9 Decision impact / Tac dong len quyet dinh

The Wheeler case increases confidence that E18 is more than a wording issue. It gives one concrete case where the formal locking rule can classify `W_valid` without relying on E8 invalidation.

VN: Case Wheeler lam tang do tin cay rang E18 khong chi la van de cau chu. No cho mot case cu the trong do quy tac khoa co the phan loai `W_valid` ma khong can dua vao E8.

| Criterion | After Section 9 | After Wheeler test | RCA note |
|---|---:|---:|---|
| Internal necessity | 4.1 | 4.2 | Wheeler shows a concrete selection/locking gap. |
| BE anchor strength | 3.6 | 3.6 | Unchanged; BE support remains analogical. |
| EX support | 3.7 | 3.7 | Unchanged; EX remains compass-only. |
| Boundary safety | 4.4 | 4.4 | Still safe under K-side interpretation. |
| Postulate readiness | 3.9 | 4.1 | First case validation is achieved, but one case is not enough for full promotion. |

### 10.10 Updated RCA status / Trang thai RCA cap nhat

**Updated status:** E18 is now **RCA-supported candidate with first case validation**.

It should still not be frozen as a full framework postulate until a second, harder case is tested, preferably delayed-choice quantum eraser, because that case stresses post-selection, coincidence sorting, and the risk of retrocausal overclaim more strongly than the basic Wheeler interferometer.

VN: Trang thai cap nhat: E18 hien la **RCA-supported candidate with first case validation**. Van chua nen dong bang thanh postulate framework day du cho den khi test case thu hai kho hon, tot nhat la delayed-choice quantum eraser, vi case do stress-test post-selection, coincidence sorting, va rui ro overclaim retrocausal manh hon Wheeler co ban.

---

## Section 11 — Case Test 2: Delayed-Choice Quantum Eraser

### 11.1 Purpose / Muc dich

This section tests E18 against a harder delayed-choice case: delayed-choice quantum eraser. Wheeler delayed-choice tests whether a later apparatus context can lock a path or interference registration window. Quantum eraser adds a stronger stress test: later idler context plus coincidence sorting classifies already recorded signal data into valid subsets.

VN: Section nay test E18 tren case kho hon: delayed-choice quantum eraser. Wheeler test viec boi canh may do ve sau khoa cua so path hoac interference. Quantum eraser them stress-test manh hon: boi canh idler ve sau cong voi coincidence sorting phan loai du lieu signal da ghi thanh cac subset hop le.

The purpose remains registration-layer only. This section does not claim backward signaling, physical retrocausation, modification of the Born rule, or replacement of Standard Quantum Mechanics.

VN: Muc dich van chi o tang ghi nhan. Section nay khong claim tin hieu di nguoc thoi gian, retrocausation vat ly, sua Born rule, hay thay the Standard Quantum Mechanics.

### 11.2 Minimal setup / Thiet lap toi gian

```text
Entangled photon pair is created
  -> signal photon goes to signal detector
  -> idler photon is measured later in a chosen context C_f
  -> coincidence relation S pairs signal and idler records
  -> signal data are sorted into valid subsets
```

Two simplified idler contexts are sufficient for the RCA test:

| Final idler context `C_f` | Registration reading | Candidate window/subset |
|---|---|---|
| `which_path_preserved` | which-path / no-interference classification | `W_which_path` |
| `which_path_erased` | erased-path interference or anti-interference subset | `W_erased_interference` |

Boundary note: the raw signal record is not treated as physically changed by the later idler measurement. The later context and sorting relation only classify which signal-data subset is registration-valid for the selected reading.

VN: Ghi chu ranh gioi: ban ghi signal tho khong bi thay doi vat ly boi phep do idler ve sau. Boi canh ve sau va quan he sorting chi phan loai subset du lieu signal nao hop le cho cach doc da chon.

### 11.3 Variable mapping / Anh xa bien

| E18 symbol | Quantum eraser case | Meaning |
|---|---|---|
| `C_f` | Later idler measurement context | Final context that preserves or erases which-path information |
| `S` | Coincidence / sorting relation | Relation pairing signal and idler records |
| `{W_i}` | `{W_signal_raw, W_which_path, W_erased_interference}` | Candidate signal-data registration windows/subsets |
| `W_signal_raw` | Raw signal detection window | Unsorted signal record |
| `W_which_path` | Which-path-classified signal subset | Valid subset when path information is preserved |
| `W_erased_interference` | Erased-path interference subset | Valid subset when which-path information is erased |
| `W_valid` | Window/subset selected by `C_f` and `S` | Valid K-side registration subset |
| `K` | Registration state | State updated after valid subset locking |

Before idler context and coincidence sorting are applied, the signal data remain underclassified:

```text
Before C_f and S:
  K(signal data) = raw / underclassified
```

After `C_f` and `S` are available, a valid lock may occur if all Section 9 conditions pass with the sorting relation included.

### 11.4 Branch A — `C_f = which_path_preserved`

Expected lock:

```text
Lock(which_path_preserved, S, {W_signal_raw, W_which_path, W_erased_interference})
  -> W_which_path
```

Five-condition test:

| Condition | RCA question | Result |
|---|---|---|
| `R(C_f, W_which_path)` | Is the which-path-preserving idler context relevant to which-path signal classification? | PASS |
| `B(C_f, W_which_path)` | Does the idler context specify the which-path / no-interference registration class? | PASS |
| `T(W_which_path, C_f)` | Are signal data and idler context inside the same admissible pair-sequence? | PASS |
| `I(C_f, S, W_which_path)` | Do idler context plus coincidence relation function as a valid sign for this subset? | PASS, protocol-dependent |
| `G(C_f, W_which_path)` | Does the claim stay within K-side sorting/classification? | PASS |

RCA note: Branch A does not invalidate the raw signal record. It classifies the record into a which-path-preserved subset using the later idler context plus coincidence relation.

VN: Nhanh A khong phu quyet ban ghi signal tho. No phan loai ban ghi thanh subset giu which-path bang boi canh idler ve sau cong voi quan he coincidence.

### 11.5 Branch B — `C_f = which_path_erased`

Expected lock:

```text
Lock(which_path_erased, S, {W_signal_raw, W_which_path, W_erased_interference})
  -> W_erased_interference
```

Five-condition test:

| Condition | RCA question | Result |
|---|---|---|
| `R(C_f, W_erased_interference)` | Is the which-path-erasing idler context relevant to the interference subset? | PASS |
| `B(C_f, W_erased_interference)` | Does the idler context specify the erased-path interference registration class? | PASS |
| `T(W_erased_interference, C_f)` | Are signal data and idler context inside the same admissible pair-sequence? | PASS |
| `I(C_f, S, W_erased_interference)` | Do idler context plus coincidence relation function as a valid sign for this subset? | PASS, protocol-dependent |
| `G(C_f, W_erased_interference)` | Does the claim avoid backward signaling and remain K-side only? | PASS |

RCA note: Branch B does not say the later idler measurement physically creates an earlier interference history. It says the later idler context plus sorting relation licenses an interference-subset registration reading.

VN: Nhanh B khong noi phep do idler ve sau tao ra lich su giao thoa trong qua khu. No noi boi canh idler ve sau cong voi quan he sorting cho phep doc subset giao thoa o tang ghi nhan.

### 11.6 Five-condition result / Ket qua 5 dieu kien

| Condition | Branch A: `which_path_preserved -> W_which_path` | Branch B: `which_path_erased -> W_erased_interference` | RCA implication |
|---|---|---|---|
| `R` | PASS | PASS | Idler context is relevant to the selected signal-data subset. |
| `B` | PASS | PASS | Idler context specifies the registration class. |
| `T` | PASS | PASS | Signal and idler records belong to the same admissible pair-sequence. |
| `I` | PASS with protocol and `S` | PASS with protocol and `S` | Validity requires coincidence/sorting relation, not `C_f` alone. |
| `G` | PASS | PASS | The reading remains non-retrocausal and K-side only. |

**Case result:** Delayed-choice quantum eraser passes the second E18 case test only if `S`, the coincidence/sorting relation, is included in the locking rule.

VN: Ket qua case: delayed-choice quantum eraser pass test thu hai cho E18 chi khi them `S`, tuc quan he coincidence/sorting, vao quy tac khoa.

### 11.7 RCA 5 Whys for quantum eraser

1. **Why does E18 seem needed here?** Because raw signal data are not enough to determine the final registration subset before idler context and coincidence sorting are applied.
2. **Why is this not E8?** Because the raw signal record is not voided; it is sorted into valid subsets.
3. **Why is this not E13?** Because temporal bounding does not define how signal-idler coincidence produces a valid subset classification.
4. **Why is this not legacy E17?** Because rho/K separation is necessary, but it does not define idler-context-plus-sorting subset locking inside `K`.
5. **Root cause:** The quantum eraser case exposes a stronger form of the E18 gap: context-conditioned subset locking, not only context-conditioned window locking.

VN: RCA 5 Whys cho thay quantum eraser khong can noi tin hieu di nguoc thoi gian. No can quy tac phan loai subset hop le: boi canh idler ve sau cong voi sorting relation khoa du lieu signal vao subset nao.

### 11.8 Formula refinement / Tinh chinh cong thuc

The Wheeler test can be expressed with the simpler formula:

```text
Lock(C_f, {W_i}) -> W_valid
```

The quantum eraser test shows that this is not general enough. For cases involving post-selection or coincidence sorting, the locking rule should be refined as:

```text
Lock(C_f, S, {W_i}) -> W_valid
```

where:

```text
C_f = final context / later idler measurement context
S   = coincidence or sorting relation
W_i = candidate registration windows or data subsets
```

The inferential validity condition should also be refined:

```text
I(C_f, S, W_j) = true
iff
C_f together with S functions as a valid inferential sign for W_j.
```

VN: Test quantum eraser cho thay cong thuc can them `S`. Trong nhung case co post-selection hoac coincidence sorting, `C_f` mot minh chua du. `C_f` phai di cung `S` moi co the lam dau hieu hop le de khoa `W_j`.

### 11.9 Good / Bad / Risk table

| Aspect | Good / Strength | Bad / Weakness | Risk control |
|---|---|---|---|
| Stress-test strength | Harder than Wheeler; tests post-selection and subset classification. | More complex and easier to misread. | Keep the description minimal and registration-layer only. |
| E18 fit | Shows E18 can handle later-context subset locking. | Requires formula refinement with `S`. | Explicitly define `S` as sorting/coincidence relation. |
| Distinction from E8 | Raw data are classified, not voided. | The word "delayed" may invite override language. | Use "classification" and "sorting," not "invalidation." |
| Distinction from E13 | Timing alone cannot explain subset validity. | Multiple detector times can confuse the window model. | Separate raw detection from valid subset registration. |
| Distinction from E17 | E17 gives rho/K interface; E18 gives K-side subset locking. | Without `S`, E18 may look too general. | Make `S` mandatory for eraser-style cases. |
| BE anchor | `I(C_f, S, W_j)` sharpens the valid-sign analogy. | BE relation remains analogical, not identity. | Keep `Anumana`, `Vyapti`, and `Svabhavapratibandha` as structural analogues only. |
| Boundary safety | No backward signaling is required. | Public descriptions of quantum eraser often overstate retrocausation. | Repeat no retrocausation, no Born-rule modification, no Standard QM replacement. |

### 11.10 Decision impact / Tac dong len quyet dinh

The quantum eraser case strengthens E18 more than Wheeler because it reveals that valid locking may require not only a final context `C_f`, but also a sorting relation `S`. This makes the E18 candidate more precise and less vulnerable to arbitrary-context locking.

VN: Case quantum eraser lam E18 manh hon Wheeler vi no cho thay khoa hop le co the can khong chi boi canh cuoi `C_f`, ma con can quan he sorting `S`. Dieu nay lam E18 chinh xac hon va bot bi rui ro khoa tuy tien bang boi canh ve sau.

| Criterion | After Wheeler test | After quantum eraser test | RCA note |
|---|---:|---:|---|
| Internal necessity | 4.2 | 4.4 | Quantum eraser reveals subset-locking, a stronger version of the gap. |
| BE anchor strength | 3.6 | 3.8 | `I(C_f, S, W_j)` gives a sharper valid-sign structure. |
| EX support | 3.7 | 3.7 | Unchanged; EX remains compass-only. |
| Boundary safety | 4.4 | 4.3 | Slightly lower because quantum eraser has higher retrocausal overclaim risk. |
| Postulate readiness | 4.1 | 4.3 | Two case tests now support drafting, but not careless promotion. |

### 11.11 Updated RCA status / Trang thai RCA cap nhat

**Updated status:** E18 is now **RCA-supported candidate with two case validations and formula refinement**.

The refined candidate statement becomes:

```text
A prior measurement window or data subset becomes registration-valid only when the final context C_f, and where needed the sorting relation S, supplies the condition that locks which observable, basis, window, or subset is being registered. This locking is a K-side classification rule, not a physical claim that the past quantum process is changed.
```

VN: Trang thai cap nhat: E18 hien la **RCA-supported candidate with two case validations and formula refinement**.

Phat bieu ung vien da tinh chinh:

```text
Mot cua so do hoac subset du lieu truoc do chi tro thanh registration-valid khi boi canh cuoi C_f, va khi can thiet quan he sorting S, cung cap dieu kien khoa observable, basis, cua so, hoac subset nao dang duoc ghi nhan. Viec khoa nay la quy tac phan loai phia K, khong phai tuyên bo vat ly rang tien trinh luong tu qua khu bi thay doi.
```

**Promotion caution:** Even after two case validations, E18 should be drafted as a narrow candidate postulate first, not immediately inserted into the framework index as a frozen postulate. The draft should preserve the refined formula `Lock(C_f, S, {W_i}) -> W_valid` and the mandatory non-retrocausal boundary guard.

VN: Canh bao nang cap: Du da co hai case validation, E18 nen duoc draft thanh candidate postulate hep truoc, chua chen ngay vao framework index nhu postulate dong bang. Draft phai giu cong thuc tinh chinh `Lock(C_f, S, {W_i}) -> W_valid` va boundary guard khong-retrocausal bat buoc.


---

## Section 12 — Case Test 3: Kim et al. 1999 Delayed-Choice Quantum Eraser (Extension)

### 12.1 Purpose / Muc dich

This section is added as a downstream **extension** to Sections 9-11. It references the third independent case validation required by E18 promotion gate G4, executed in a dedicated case file. Sections 9-11 above remain authoritative for the formal locking rule and the first two case validations (Wheeler + Scully-Drühl); Section 12 only links the third case and records its decision impact.

VN: Section nay duoc them nhu **mo rong** xuoi dong tu Sections 9-11. No tham chieu case validation doc lap thu ba ma promotion gate G4 cua E18 yeu cau, duoc thuc thi trong mot file case rieng. Sections 9-11 o tren van la nguon chinh thuc cho quy tac khoa hinh thuc va hai case validation dau tien (Wheeler + Scully-Drühl); Section 12 chi link case thu ba va ghi nhan tac dong quyet dinh cua no.

### 12.2 Case file reference / Tham chieu file case

| Field | Value |
|---|---|
| Case file path | [rca/cases/e18_case_kim_1999.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/rca/cases/e18_case_kim_1999.md) |
| Experimental source | Kim, Y.-H., Yu, R., Kulik, S. P., Shih, Y., & Scully, M. O. (2000). "Delayed 'Choice' Quantum Eraser." *Phys. Rev. Lett.* 84, 1-5. |
| Branch structure | 4-branch lock (D1 erased +fringe, D2 erased -fringe, D3 preserved path-A, D4 preserved path-B) |
| Symmetric pairs | Erased pair D1/D2 (out-of-phase) + preserved pair D3/D4 (path A/B) |
| Five-condition cells | 20 cells (4 branches × 5 conditions) |

### 12.3 Case result / Ket qua case

**Case result:** Kim et al. 1999 passes the third E18 case test with all twenty condition cells PASS, **only if** each branch uses its specific coincidence relation `R_{0i}` as the sorting relation `S` in the refined formula `Lock(C_f, S, {W_i}) -> W_valid`.

VN: Ket qua case: Kim et al. 1999 pass case test thu ba cho E18 voi toan bo 20 o dieu kien PASS, **chi khi** moi nhanh dung quan he trung phung `R_{0i}` dac thu lam sorting relation `S` trong cong thuc tinh chinh.

| Branch | C_f | Expected W_valid | Result |
|---|---|---|:---:|
| Branch 1 | D1 (erased, +fringe) | W_D1 | 5/5 PASS |
| Branch 2 | D2 (erased, -fringe) | W_D2 | 5/5 PASS |
| Branch 3 | D3 (preserved, path A) | W_D3 | 5/5 PASS |
| Branch 4 | D4 (preserved, path B) | W_D4 | 5/5 PASS |
| Total | — | — | **20/20 PASS** |

### 12.4 Structural novelty / Diem moi cau truc

Kim 1999 contributes a structural dimension not exercised by Wheeler (binary lock) or Scully-Drühl (ternary lock): **multi-branch lock with symmetric pairs**. The 4-branch setup with two symmetric pairs (erased D1/D2 with out-of-phase fringes + preserved D3/D4 with path A/B) confirms the refined formula `Lock(C_f, S, {W_i}) -> W_valid` natively handles arbitrary `{W_i}` cardinality without requiring formula modification.

VN: Kim 1999 dong gop chieu cau truc ma Wheeler (binary lock) va Scully-Drühl (ternary lock) chua test: **multi-branch lock voi cap doi xung**. Cau hinh 4-nhanh voi hai cap doi xung (erased D1/D2 lech pha + preserved D3/D4 path A/B) xac nhan cong thuc tinh chinh xu ly duoc luc luong tuy y cua `{W_i}` ma khong can sua cong thuc.

### 12.5 RCA decision impact / Tac dong RCA

| Criterion | After Scully-Drühl test | After Kim 1999 test | RCA note |
|---|---:|---:|---|
| Internal necessity | 4.4 | **4.5** | Kim 1999 confirms multi-branch generality of the gap. |
| BE anchor strength | 3.8 | **3.8** | Unchanged — case test does not strengthen BE anchor; G5 remains the dedicated upgrade gate. |
| EX support | 3.7 | **3.7** | Unchanged — EX remains compass-only. |
| Boundary safety | 4.3 | **4.3** | Unchanged — Kim 1999 has same retrocausal overclaim risk as Scully-Drühl, contained by non-claims. |
| Postulate readiness | 4.3 | **4.4** | Three case validations now support drafting; only G5/G6/G7 remain pending. |

### 12.6 Promotion gate impact / Tac dong promotion gate

| Gate | Status before Section 12 | Status after Section 12 |
|---|---|---|
| G1 (two case validations PASS) | DONE | DONE |
| G2 (formal locking rule with explicit S) | DONE | DONE |
| G3 (boundary safety ≥ 4.0/5) | DONE | DONE |
| **G4 (third independent case validation)** | **PENDING** | **DONE — via case file** |
| G5 (BE anchor strength ≥ 4.0/5) | PENDING | PENDING (unchanged) |
| G6 (EX recoverability check) | PENDING | PENDING (unchanged) |
| G7 (user-authorized index insertion) | PENDING | PENDING (unchanged) |

**Gate progress: 3/7 -> 4/7 (57%) at Section 12; Section 13 below later advances G5, so current progress is 5/7 (71%).**

### 12.7 Updated RCA status / Trang thai RCA cap nhat

**Updated status:** E18 is now **RCA-supported candidate with THREE case validations and refined formula** (Wheeler + Scully-Drühl + Kim 1999).

The candidate statement remains:

```text
A prior measurement window or data subset becomes registration-valid only when the final context C_f, and where needed the sorting relation S, supplies the condition that locks which observable, basis, window, or subset is being registered. This locking is a K-side classification rule, not a physical claim that the past quantum process is changed.
```

VN: Trang thai cap nhat: E18 hien la **RCA-supported candidate voi BA case validation va cong thuc tinh chinh** (Wheeler + Scully-Drühl + Kim 1999). Phat bieu candidate giu nguyen.

**Promotion caution (unchanged):** Even after three case validations, E18 remains in `framework/drafts/` until all 7 promotion gates pass. The framework `index.md` MUST NOT list E18 as a frozen postulate until G7 (user-authorized index insertion) is also satisfied.

VN: Canh bao nang cap (giu nguyen): Du da co ba case validation, E18 van o `framework/drafts/` cho den khi tat ca 7 promotion gate pass. Framework `index.md` KHONG duoc liet ke E18 nhu postulate dong bang cho den khi G7 cung thoa.

---

## 13. G5 BE anchor decision: analogical-only acceptance / Quyet dinh neo BE G5

### 13.1 Observed issue / Van de quan sat

After G4, E18 has three independent case validations and a refined locking formula, but G5 remains open because the Buddhist Epistemology anchor score is still 3.8/5. The issue is not lack of prose support; the issue is that a stronger score could only be obtained by treating the BE relation as more than a structural analogy.

VN: Sau G4, E18 da co ba case validation va cong thuc `Lock(C_f, S, {W_i}) -> W_valid` ro hon, nhung G5 van mo vi neo BE chi o 3.8/5. Van de goc khong phai thieu cau van, ma la neu co nang diem bang cach ep neo BE thanh tuong duong vat ly thi se vuot scope.

### 13.2 Five-Why trace / Truy vet 5-Why

| Why step | RCA answer |
|---|---|
| 1. Why is G5 still PENDING? | BE anchor strength is below the 4.0/5 gate if scored as a deep BE-QM grounding. |
| 2. Why is the score below 4.0? | `N_BE_00003`, `N_BE_00019`, and `N_BE_00021` support valid-sign structure only analogically. |
| 3. Why not deepen the anchor? | Deepening would risk turning a structural guide into a physical-equivalence claim. |
| 4. Why is that risk material? | E18 is a K-side registration rule, while Buddhist Epistemology is the ontological/epistemic source frame, not a physical measurement theory. |
| 5. Why choose acceptance instead of upgrade? | The root cause is boundary ambiguity, so the correct fix is an explicit analogical-only boundary, not forced strengthening. |

### 13.3 Decision / Quyet dinh

**G5 decision:** Accept the Buddhist Epistemology anchor for E18 as **permanently analogical-only**.

This decision satisfies G5 by resolving the boundary condition directly: E18 may use BE as a structural source for registration-layer interpretation, but it does not claim BE predicts, explains, replaces, or physically grounds Standard Quantum Mechanics.

VN: Quyet dinh G5: chap nhan neo BE cua E18 la **analogical-only** lau dai. Nghia la BE giup minh thay cau truc ghi nhan, nhung khong duoc noi BE du doan, giai thich vat ly, thay the, hay lam nen tang vat ly cho Standard Quantum Mechanics.

### 13.4 BE anchor chain and identity boundary

| BE code | BE anchor | E18 use | Boundary |
|---|---|---|---|
| `N_BE_00003` | Anumana / inference | Structural analogue for valid-sign based registration: `C_f` only matters when it functions as an admissible sign within `S`. | `C_f` is not a Buddhist `hetu`; it is a measurement-context variable. |
| `N_BE_00019` | Vyapti / pervasion | Structural analogue for non-arbitrary linkage between final context and valid registration window. | E18 does not assert universal logical pervasion inside quantum physics. |
| `N_BE_00021` | Svabhavapratibandha / essential relation | Structural analogue for rejecting arbitrary context-window locking. | E18 does not identify delayed-choice sorting with `tadutpatti` or `tadatmya`. |

### 13.5 Scoring impact / Tac dong diem so

| Criterion | Before G5 decision | After G5 decision | RCA note |
|---|---:|---:|---|
| BE anchor strength as equivalence | 3.8 | 3.8 | No forced strengthening is introduced. |
| BE boundary safety | 3.8 | **4.4** | Boundary is now explicit and non-equivalence is locked. |
| G5 gate satisfaction | PENDING | **DONE** | G5 is satisfied by explicit analogical-only acceptance, the second allowed path in the promotion table. |
| Postulate readiness | 4.4 | **4.4** | Case support unchanged; boundary risk reduced. |

### 13.6 Promotion gate impact / Tac dong promotion gate

| Gate | Status before Section 13 | Status after Section 13 |
|---|---|---|
| G1 (two case validations PASS) | DONE | DONE |
| G2 (formal locking rule with explicit S) | DONE | DONE |
| G3 (boundary safety >= 4.0/5) | DONE | DONE |
| G4 (third independent case validation) | DONE | DONE |
| **G5 (BE anchor decision)** | **PENDING** | **DONE — analogical-only accepted as permanent boundary** |
| **G6 (EX recoverability check)** | PENDING | **DONE — EX registry sync completed via Path C; `BR_EX_BE_00070`–`BR_EX_BE_00072` active; `BR_EX_BE_00066` remains `RECLASSIFIED-v1.7` inactive** |
| G7 (user-authorized index insertion) | PENDING | PENDING |

**Gate progress: 6/7 DONE; G7 PENDING.** G6 chain: PENDING → HOLD (`rca_e18_g6_ex_recoverability_check.md`) → Path C PASS-CANDIDATE 4.2/5 (`rca_e18_ex_vnext_bridge_audit.md`) → DONE after EX registry sync (`br_ex_be_registry.md` entries `BR_EX_BE_00070`–`BR_EX_BE_00072`). EX K-side direct coverage: 47/52 = 90.4%. See also `rca_core_extensibility_analysis.md` Appendix B for extensibility verdict impact.

### 13.7 Verification / Kiem chung

- E18 remains in `framework/drafts/`; no insertion into `framework/index.md` is authorized by this section.
- No EX structure is imported into the core; EX remains compass-only.
- BE is used as a structural analogue, not as empirical support for a physics claim.
- The fix removes the root cause: boundary ambiguity around G5.
- G6 is DONE: EX registry sync completed; `BR_EX_BE_00070`–`BR_EX_BE_00072` active as valid-sign package for `N_QM_VVV_00024`; old `BR_EX_BE_00066` preserved as `RECLASSIFIED-v1.7` historical record.

VN: Kiem chung: E18 van o `framework/drafts/`; chua duoc vao `framework/index.md`. EX khong bi import. BE chi la neo cau truc, khong phai bang chung vat ly. Root cause cua G5 da duoc dong lai. G6 DONE sau khi sync registry EX voi Path C valid-sign package (`BR_EX_BE_00070`–`BR_EX_BE_00072` active); bridge cu `BR_EX_BE_00066` giu nguyen la lich su RECLASSIFIED-v1.7.

