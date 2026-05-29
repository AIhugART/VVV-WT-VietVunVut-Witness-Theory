Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

> **Ghi chú phiên bản cũ / Legacy note:** File này thuộc đường dẫn cũ `VVV-EQM` và chỉ giữ để tham chiếu lịch sử. Khi làm việc hiện tại phiên bản VVV-QMRF (after 2026-05-14), bắt buộc phải dùng phiên bản mới tại [documents\research_documents\vvv-qmrf\dictionary.md](../../vvv-qmrf/dictionary.md); nếu phát hiện đang dùng file cũ này, phải tự cập nhật hướng làm việc sang phiên bản mới.

# VVV-QMRF Registration Dictionary
# Từ điển Thuật ngữ Registration của VVV-QMRF

**Date:** 2026-05-14  
**Scope:** Dictionary for VVV-QMRF terms that resemble existing Standard Quantum Measurement terms; `VVV-EQM` is retained as a legacy name.  
**Primary frame:** Buddhist Epistemology  
**Mapped domain:** Quantum Measurement  
**RCA rule:** If a VVV-QMRF term looks like an existing QM term, append `- registration` unless the text is explicitly discussing the canonical physical QM concept.

---

## 0. Project Name RCA

### English

**Legacy name:** `VietVunVut Epistemic Quantum Measurement (VVV-EQM)`.

**Preferred public name:** `VietVunVut Quantum Measurement Registration Framework (VVV-QMRF)`.

**Symptom:** The word `Epistemic` can make the framework sound as if matter, detectors, or physical interactions possess human-like cognition.

**Root cause:** The project name compressed the Buddhist Epistemology source lineage and the neutral `K`-side registration layer into one word. The framework's novelty is not human cognition and not a new physical quantum state law; it is the `registration-state update` from `K_before` to `K_after`.

**Fix:** Use `VVV-QMRF` as the public-facing name. Keep `VVV-EQM` only as a legacy name for older documents or historical continuity.

**Verification:** Standard Quantum Measurement still supplies `p_QM(o) = Tr(E_o ρ)`, detector response, and `ρ_after`. VVV-QMRF adds the registration layer `K_before → K_after`, formalized as `K_after = U_K(K_before, o)`. The name now points to `registration`, not human-like cognition.

### Tiếng Việt

**Tên cũ:** `VietVunVut Epistemic Quantum Measurement (VVV-EQM)`.

**Tên chính đề xuất:** `VietVunVut Quantum Measurement Registration Framework (VVV-QMRF)`.

**Triệu chứng:** Chữ `Epistemic` có thể làm người đọc tưởng vật chất, detector, hoặc tương tác vật lý có nhận thức kiểu con người.

**Nguyên nhân gốc:** Tên dự án cũ nén nguồn gốc Buddhist Epistemology và tầng ghi nhận trung tính `K` vào cùng một chữ. Điểm mới của framework không phải là nhận thức người, cũng không phải luật trạng thái lượng tử vật lý mới; điểm mới là `registration-state update` từ `K_before` sang `K_after`.

**Cách sửa:** Dùng `VVV-QMRF` làm tên public-facing. Giữ `VVV-EQM` chỉ như tên legacy cho tài liệu cũ hoặc mạch lịch sử.

**Kiểm chứng:** Standard Quantum Measurement vẫn giữ `p_QM(o) = Tr(E_o ρ)`, `detector response`, và `ρ_after`. VVV-QMRF thêm tầng registration `K_before → K_after`, hình thức hóa bằng `K_after = U_K(K_before, o)`. Tên mới chỉ về `registration`, không chỉ về nhận thức giống con người.

| Role | Name | Use |
|---|---|---|
| Preferred public name | `VietVunVut Quantum Measurement Registration Framework (VVV-QMRF)` | Use in new public-facing documents. |
| Legacy name | `VietVunVut Epistemic Quantum Measurement (VVV-EQM)` | Use only when discussing older documents or naming history. |
| Core mechanism | `registration-state update` | Use for the `K_before → K_after` operation. |
| Avoided framing | `Epistemic` as the main project-name keyword | Avoid anthropomorphizing matter or detector response. |

---

## 1. RCA Finding

### English

**Symptom:** Several VVV-QMRF concepts look similar to established Standard Quantum Measurement concepts such as `No-Result Measurement`, `Projection Operator`, `Post-Measurement State Update`, `Entanglement`, and `Decoherence`.

**Root cause:** The physical quantum state `ρ` and the registration state `K` are not always separated in the term name. This can make a VVV-QMRF registration-layer concept appear to be a redefinition of a canonical QM physical concept.

**Fix:** Keep canonical QM node names unchanged in `SYSTEM_Quantum_Measurement/system_qm_full.md`. For VVV-QMRF concepts, use `- registration` to mark that the novelty belongs to the `K`-side registration layer, not to the physical `ρ`-side formalism.

**Verification:** Standard QM still supplies `p_QM(o) = Tr(E_o ρ)`, physical detector response, and `ρ_after`. VVV-QMRF adds `K_before → K_after`, formalized as `K_after = U_K(K_before, o)`. The novelty is in `U_K`, not in the Born rule or a new physical collapse law.

### Tiếng Việt

**Triệu chứng:** Một số khái niệm VVV-QMRF nhìn giống khái niệm QM chuẩn như `No-Result Measurement`, `Projection Operator`, `Post-Measurement State Update`, `Entanglement`, và `Decoherence`.

**Nguyên nhân gốc:** Tên gọi chưa luôn tách rõ trạng thái lượng tử vật lý `ρ` và trạng thái ghi nhận `K`. Vì vậy người đọc có thể hiểu nhầm rằng VVV-QMRF đang định nghĩa lại khái niệm vật lý QM cũ.

**Cách sửa:** Giữ nguyên tên node QM chuẩn trong `SYSTEM_Quantum_Measurement/system_qm_full.md`. Với khái niệm VVV-QMRF, thêm hậu tố `- registration` để đánh dấu rằng điểm mới nằm ở tầng ghi nhận `K`, không phải tầng vật lý `ρ`.

**Kiểm chứng:** QM chuẩn vẫn giữ `p_QM(o) = Tr(E_o ρ)`, `detector response`, và `ρ_after`. VVV-QMRF chỉ thêm `K_before → K_after`, hình thức hóa bằng `K_after = U_K(K_before, o)`. Điểm mới nằm ở `U_K`, không nằm ở `Born rule` hay luật `collapse` vật lý mới.

---

## 2. Naming Rule

| Rule | Use |
|---|---|
| Canonical QM term | Use only for the existing physical QM concept. |
| VVV-QMRF term resembling QM | Append `- registration`. |
| General K-side update | Prefer `registration-state update` / cập nhật trạng thái ghi nhận. |
| Apparatus physical signal | Use `detector response`, not `registration`. |
| Human-only language | Avoid unless the context is explicitly human cognition; use `registering system` for the general case. |

---

## 3. Dictionary Table

| No. | VVV-QMRF registration term | Avoid ambiguous term in VVV context | Nearest Standard QM term | Difference from old QM | RCA root cause | Source traceability |
|---:|---|---|---|---|---|---|
| 1 | `No-Result Measurement - registration` | `No-Result Measurement` when used as VVV novelty | `N_QM_00033` No-Result Measurement / Null Measurement | Standard QM says detector silence can be an outcome that updates the quantum state. VVV-QMRF adds the registration meaning: a valid null event can become positive registration status under the right conditions. | Null-result physics already exists; the new part is the registration of absence or exclusion. | `SYSTEM_Quantum_Measurement/system_qm_full.md` L70; `category/vvv_qmrf_category_01_e11_purely_contrastive_evidence.md` L42-L47, L84-L85; `category/vvv_qmrf_category_13_e14_validated_absence_registration.md` L31-L35, L50-L61; `node_QM_VVV.md` L33-L37, L50. |
| 2 | `Projection Operator - registration` | `Projection Operator` for VVV `P_null` or `Π̂_absent^(ℋ_M)` | `N_QM_00018` Projection Operator; `N_QM_00014` PVM | Standard QM projection operators represent physical projective measurement. VVV-QMRF uses proposed null/absence projection as a registration-side formal symbol for exclusion or subspace-bounded absence registration. | The operator shape resembles PVM, but the function is registration by exclusion/absence inside the measurement-accessible subspace, not a new canonical PVM operator. | `SYSTEM_Quantum_Measurement/system_qm_full.md` L51, L55; `category/vvv_qmrf_category_01_e11_purely_contrastive_evidence.md` L22-L25, L41-L47; `category/vvv_qmrf_category_13_e14_validated_absence_registration.md` L41-L58; `node_QM_VVV.md` L35, L92-L93, L145-L147. |
| 3 | `Post-Measurement State Update - registration` | `Post-Measurement State Update` when referring to `K_after` | `N_QM_00022` Post-Measurement State Update | Standard QM updates `ρ` after outcome `k`. VVV-QMRF updates `K`, the registration state, after the outcome becomes registrable and valid. | The word `update` is shared, but the updated object differs: QM updates `ρ`; VVV-QMRF updates `K`. | `SYSTEM_Quantum_Measurement/system_qm_full.md` L59; `VVV_EQM_vs_Standard_QM_system_diagram.md` L23-L32, L94-L110, L156-L158; `node_QM_VVV.md` L47-L48, L98. |
| 4 | `Entanglement - registration` | `Entanglement` when used as VVV relational category | `N_QM_00047` Entanglement; `N_QM_00090` Bell's Inequality & Bell Correlations | Standard QM defines non-factorizable physical correlation. VVV-QMRF classifies entanglement as an extension relation: intrinsic registration non-separability beyond causal models and beyond Tādātmya-style logical genus-species identity, not a third classical Dharmakīrti subtype. | The physical phenomenon already exists; the new part is the registration-side extension classification of the relation. | `SYSTEM_Quantum_Measurement/system_qm_full.md` L84, L127; `category/vvv_qmrf_category_14_e15_intrinsic_relational_binding.md` L11, L27-L31, L40-L50, L57-L63; `node_QM_VVV.md` L55, L158-L163. |
| 5 | `Decoherence - registration` | `Decoherence` when used as certification/validation layer | `N_QM_00095` Decoherence & Environment as Measurement | Standard QM describes environmental decoherence and suppression of coherences. VVV-QMRF may use environmental correlations as part of extrinsic registration certification, not as a replacement for decoherence theory. | Decoherence is physical support; certification is registration-layer interpretation. | `SYSTEM_Quantum_Measurement/system_qm_full.md` L132; `category/vvv_qmrf_category_04_e07_dual_phase_registration_certification.md` L47-L53, L67-L77, L131; `node_QM_VVV.md` L43-L49, L103. |
| 6 | `Measurement - registration` | `Measurement` when finality/validity is VVV-specific | `N_QM_00019` Measurement (Physical Act) | Standard QM measurement determines an observable value through apparatus and may disturb the system. VVV-QMRF asks when that physical event becomes registered or certified. | Physical measurement and registered measurement were compressed into one term. | `SYSTEM_Quantum_Measurement/system_qm_full.md` L56; `category/vvv_qmrf_category_04_e07_dual_phase_registration_certification.md` L31-L35, L47-L53; `category/vvv_qmrf_category_08_e03_registration_lock_operation.md` L39-L49; `VVV_EQM_vs_Standard_QM_system_diagram.md` L49-L72. |
| 7 | `Detector Response - registration input` | Treating detector response as already registration status | `N_QM_00019` Measurement; `N_QM_00021` System-Meter Coupling | Standard QM has apparatus response or physical trace. VVV-QMRF treats detector response as input into the registration pipeline, not final registration status by itself. | A detector click is physical signal; registered status requires `K`-side processing. | `SYSTEM_Quantum_Measurement/system_qm_full.md` L56, L58; `VVV_EQM_vs_Standard_QM_system_diagram.md` L58-L65, L83-L110, L116; `category/vvv_qmrf_category_08_e03_registration_lock_operation.md` L39-L49. |
| 8 | `Certified Registration State` | `Certified Measurement State` if it suggests a new physical density matrix | Nearest support: `N_QM_00022` Post-Measurement State Update; `N_QM_00025` Density Matrix | Standard QM has post-measurement state and density matrix formalism. VVV-QMRF adds the status that a conditionally updated state has passed registration certification. | `ρ_certified` can look like a new physical state; RCA bounds it as a registration-status label unless a full physical equation is supplied. | `SYSTEM_Quantum_Measurement/system_qm_full.md` L59, L62; `category/vvv_qmrf_category_04_e07_dual_phase_registration_certification.md` L47-L61, L126-L134; `node_QM_VVV.md` L47-L49, L136-L140. |
| 9 | `PVM-equivalent Registration Authority` | `PVM-equivalent epistemic authority` if physical equivalence is implied | `N_QM_00014` Projective Measurement (PVM) | Standard PVM is a physical/projective measurement formalism. VVV-QMRF only claims that a valid registration structure can have registration authority comparable to direct measurement, not that it is physically identical to PVM. | The word `equivalent` can overclaim physical identity. The safe claim is registration authority, not physical equivalence. | `SYSTEM_Quantum_Measurement/system_qm_full.md` L51; `category/vvv_qmrf_category_01_e11_purely_contrastive_evidence.md` L57-L64, L81-L87; `node_QM_VVV.md` L42, L133. |
| 10 | `Registering System - registration process` | `Observer` as a human-only or static subject | `N_QM_00094` Heisenberg Cut; `N_QM_00020` von Neumann Measurement Model | Standard QM often treats the observer/registering side as a boundary or chain element. VVV-QMRF models the registering side as a registration process that converts physical trace into internal encoding and registration lock. | Human observer language hides the general `K`-side registering system. | `SYSTEM_Quantum_Measurement/system_qm_full.md` L57, L131; `category/vvv_qmrf_category_08_e03_registration_lock_operation.md` L27-L33, L39-L49, L70-L71; `VVV_EQM_vs_Standard_QM_system_diagram.md` L61-L65, L94-L110. |
| 11 | `Interaction-Free State Inference - registration` | Treating IFSI as only null measurement | Nearest support: `N_QM_00033` No-Result Measurement; `N_QM_00005` Superposition | Standard QM supplies the physical null event and superposition structure. VVV-QMRF names the registration inference pattern: no click excludes one branch and registers the alternative. | The physical no-click is old; the contrapositive registration inference is new. | `SYSTEM_Quantum_Measurement/system_qm_full.md` L42, L70; `category/vvv_qmrf_category_01_e11_purely_contrastive_evidence.md` L31-L35, L41-L47, L70-L72; `node_QM_VVV.md` L34, L124-L130. |
| 12 | `Informative Silence - registration` | `Informative Silence` without detector-validity boundary | Nearest support: `N_QM_00033` No-Result Measurement | Standard QM can treat no-click as information. VVV-QMRF adds a validity distinction between informative silence and broken-detector null events. | Without the registration label, all silence may be falsely treated as valid evidence. | `SYSTEM_Quantum_Measurement/system_qm_full.md` L70; `category/vvv_qmrf_category_01_e11_purely_contrastive_evidence.md` L84-L85; `category/vvv_qmrf_category_13_e14_validated_absence_registration.md` L59-L61, L64-L70; `node_QM_VVV.md` L36-L37, L132. |

---

## 4. Human-Loaded and Buddhist-Source Term Rule

### English

When a term sounds human-only, religious, mystical, Pali, or Sanskrit, do not use it as the primary VVV-QMRF technical name unless the text explicitly discusses Buddhist Epistemology. Use a neutral `registration` or `K`-layer term in the main concept name, and keep the Buddhist term as `BE source` or lineage.

### Tiếng Việt

Khi một thuật ngữ nghe như chỉ dành cho con người, tôn giáo, thần bí, Pali, hoặc Sanskrit, không dùng nó làm tên kỹ thuật chính của VVV-QMRF trừ khi đoạn đó đang nói trực tiếp về Buddhist Epistemology. Tên chính nên dùng ngôn ngữ trung tính thuộc tầng `registration` hoặc `K`; thuật ngữ Buddhist giữ ở vai trò `BE source` / nguồn gốc đối chiếu.

| Old / risky term | RCA risk | Preferred VVV-QMRF term | Keep as BE source? |
|---|---|---|---|
| `cognition` | Can sound like matter is doing human cognition. | `registration` / `valid registration` | Only when discussing Buddhist cognition directly. |
| `knowledge` | Can sound subjective or human-only. | `registration status` / `registered status` | No, unless quoting source wording. |
| `truth` / `truth-stamped` | Can sound metaphysical or mystical. | `validity` / `validated registration` | No, use only in source quotation or critique. |
| `observer` | Can imply a human subject. | `registering system` | Only when discussing canonical observer language. |
| `mental` / `subjective` | Can anthropomorphize the measurement chain. | `internal representation` / `semantic registration status` | No, unless the context is explicitly human cognition. |
| `commitment` / `epistemic commitment` | Can sound like a human decision. | `registration lock` / `registration-lock operation` | Only as source lineage from `vvv_qmrf_category_08_e03_registration_lock_operation.md`. |
| `Anupalabdhi` | Pali/Sanskrit/Buddhist term can look religious if used as QM name. | `Validated Absence Registration` / `Conditioned Null Registration` | Yes: `BE source: Anupalabdhi`. |
| `Pramāṇa` | Religious/philosophical source term can overclaim authority. | `valid registration status` | Yes: `BE source: Pramāṇa`. |
| `Ākāra` / `Â_kāra` | Sanskrit/Buddhist source term can look mystical. | `Internal Representation Encoding` | Yes: source notation only. |
| `V_yava` / `V̂_yava` | Sanskrit/Buddhist source term can look mystical. | `Registration Lock` / `Irreversible Registration Locking` | Yes: source notation only. |
| `Apoha` | Buddhist exclusion theory can look like a physical QM operator. | `Exclusion-Based Registration` | Yes: `BE source: Apoha`. |
| `Svabhāvapratibandha` | Sanskrit source term can look like a new physical force. | `Intrinsic Relational Binding` | Yes: `BE source: Svabhāvapratibandha`. |

**RCA verification:** The old terms are not deleted from the project because they preserve Buddhist Epistemology lineage. The fix is to move them out of primary VVV-QMRF technical names and keep them as source traceability.

---

## 5. Canonical QM Terms Not Renamed

These existing Standard Quantum Measurement concepts keep their original names when cited as physical QM concepts:

| Canonical QM node | Keep name | Reason |
|---|---|---|
| `N_QM_00014` | `Projective Measurement (PVM)` | Existing physical/textbook measurement formalism. |
| `N_QM_00018` | `Projection Operator` | Existing standard projection operator. |
| `N_QM_00019` | `Measurement (Physical Act)` | Existing apparatus-based physical act. |
| `N_QM_00021` | `System-Meter Coupling` | Existing physical coupling between system and meter. |
| `N_QM_00022` | `Post-Measurement State Update` | Existing `ρ`-side quantum state update. |
| `N_QM_00033` | `No-Result Measurement (Null Measurement)` | Existing physical/operational no-click measurement. |
| `N_QM_00047` | `Entanglement` | Existing non-factorizable quantum correlation. |
| `N_QM_00095` | `Decoherence & Environment as Measurement` | Existing environmental decoherence concept. |

---

## 6. Boundary Statements for Publication Use

Use these sentences when a document risks confusing VVV-QMRF with Standard QM:

1. **VVV-QMRF does not rename or replace the canonical QM physical concept. It adds a `registration` layer describing how the outcome becomes registered, classified, and validated.**
2. **In this document, `- registration` marks a `K`-side operation, not a new `ρ`-side physical law.**
3. **Standard QM explains the probability and physical update of `ρ`; VVV-QMRF explains the registration-state update `K_before → K_after`.**
4. **`detector response` means the apparatus' physical response; `registration` means the later K-side status of that response as classified or valid.**
5. **Any claim of equivalence to PVM, collapse, decoherence, or entanglement must be read as registration-layer equivalence unless a separate physical equation and experimental prediction are supplied.**

---

## 7. RCA Verification Checklist

Before publishing or extending a VVV-QMRF term, verify:

- [ ] Does the term look identical to an existing QM node?
- [ ] If yes, has `- registration` been added for VVV-QMRF usage?
- [ ] Does the text clearly say whether it refers to `ρ` or `K`?
- [ ] Does the text preserve `p_QM(o) = Tr(E_o ρ)` unchanged?
- [ ] Does the text distinguish `detector response` from `registration-state update`?
- [ ] Does the text avoid claiming that VVV-QMRF replaces Standard QM?
- [ ] Are source traces given for both the old QM concept and the VVV-QMRF registration concept?

---

## 8. Minimal Glossary

| Term | Short Vietnamese explanation |
|---|---|
| `ρ` | Trạng thái lượng tử vật lý của hệ. |
| `K` | Trạng thái ghi nhận: cái hệ đã ghi nhận, phân loại, hoặc xác thực. |
| `detector response` | Phản ứng vật lý của máy đo, ví dụ click hoặc tín hiệu. |
| `registration-state update` | Cập nhật trạng thái ghi nhận `K`; đây là vùng mới của VVV-QMRF. |
| `- registration` | Hậu tố báo rằng thuật ngữ đang nói về tầng ghi nhận, không phải khái niệm vật lý QM cũ. |
