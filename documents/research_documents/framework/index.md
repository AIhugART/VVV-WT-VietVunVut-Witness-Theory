Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Framework Index / Mục lục Framework

## Document status

- **Document type:** Folder index / navigation layer
- **Folder:** `documents/research_documents/framework/`
- **Framework:** VietVunVut Quantum Measurement Registration Framework (VVV-QMRF)
- **Legacy name in older files:** VietVunVut Epistemic Quantum Measurement (VVV-EQM)
- **Purpose:** Provide a reading map for the framework files without changing the claims inside those files.

---

## 1. RCA Summary

| RCA layer | English | Vietnamese |
|---|---|---|
| Symptom | The framework folder contains many postulate files, but no central reading map. | Thư mục framework có nhiều file tiên đề, nhưng chưa có bản đồ đọc trung tâm. |
| Why 1 | E1-E16, the formal model, and the non-postulate interface principle are stored as separate documents. | E1-E16, mô hình hình thức, và nguyên lý giao diện không phải tiên đề được lưu thành các tài liệu riêng. |
| Why 2 | The relation between core postulates, extension postulates, and the two-level `ρ / K` model is not visible at folder level. | Quan hệ giữa các tiên đề lõi, tiên đề mở rộng, và mô hình hai tầng `ρ / K` chưa hiện rõ ở cấp thư mục. |
| Why 3 | The folder lacks an explicit navigation layer. | Thư mục thiếu một tầng điều hướng rõ ràng. |
| Root cause | The framework has conceptual structure, but the file system does not yet expose that structure. | Framework có cấu trúc khái niệm, nhưng hệ thống file chưa biểu lộ cấu trúc đó. |
| Fix | Add this index as a non-claim-making guide to reading order, file roles, and framework boundaries. | Thêm file index này như một hướng dẫn không tạo tuyên bố mới về thứ tự đọc, vai trò file, và ranh giới framework. |
| Verification | The index links all framework Markdown files and excludes non-research system files such as `desktop.ini`. | Index liên kết toàn bộ file Markdown trong framework và loại file hệ thống không phải nghiên cứu như `desktop.ini`. |

---

## 2. Recommended reading order / Thứ tự đọc đề xuất

1. **Start with the formal model:** [vvv_qmrf_framework_formal_registration_state_measurement_model.md](vvv_qmrf_framework_formal_registration_state_measurement_model.md)  
   This defines the two-level boundary between physical state transition `ρ` and registration-state update `K`.

2. **Read the non-postulate interface principle:** [vvv_qmrf_framework_e17_measurement_interface_postulate.md](vvv_qmrf_framework_e17_measurement_interface_postulate.md)
   This states measurement as an interface between `ρ-transition` and `registration-state update` without adding a seventeenth postulate.

3. **Read the core registration postulates:** E1-E7  
   These define the basic registration operations and the role of the registering process.

4. **Read the extension postulates:** E8-E16, then E18  
   These extend the framework to special or boundary cases such as override, null event, validity, absence, relation, structured doubt, and context-conditioned locking of prior candidate registration windows in delayed-choice scenarios.

5. **Consult supporting documents as needed:** [plan/](plan/) and [promote_postulate/](promote_postulate/)  
   See §4.4 for the list. These provide governance records (E3 completion RCA), progress audits, promotion history (E18), and the standardized 7-gate promotion protocol for future postulate candidates.

---

## 3. Framework boundary / Ranh giới framework

This index does not add a new physical theory. It only organizes the existing framework documents.

The framework does **not** claim that Buddhist Epistemology:

1. modifies the Born rule,
2. replaces standard quantum mechanics,
3. provides a physical mechanism for wavefunction collapse,
4. proves a new unified field theory,
5. produces new empirical predictions without additional formal development.

The framework contribution is on the `K` side: the structure of registration-state update / cập nhật trạng thái ghi nhận. The `ρ` side remains the standard physical quantum state layer unless a source file explicitly states a separately justified formal development.

---

## 4. File index / Bảng file

### 4.1 Formal model and interface layer

| Code | File | Title | Role |
|---|---|---|---|
| Model | [vvv_qmrf_framework_formal_registration_state_measurement_model.md](vvv_qmrf_framework_formal_registration_state_measurement_model.md) | RCA Formal Registration-State Measurement Model | Defines the two-level `ρ / K` structure and the safe claim boundary. |
| Interface principle (legacy E17) | [vvv_qmrf_framework_e17_measurement_interface_postulate.md](vvv_qmrf_framework_e17_measurement_interface_postulate.md) | Measurement Interface Principle / Nguyên lý Giao diện Phép đo | Defines measurement as a non-postulate interface between physical transition and registration-state update. |

### 4.2 Core registration postulates

| Code | File | Title | Role |
|---|---|---|---|
| E1 | [vvv_qmrf_framework_e01_self_certifying_registration_postulate.md](vvv_qmrf_framework_e01_self_certifying_registration_postulate.md) | Self-Certifying Registration Postulate / Tiên đề Tự chứng Ghi nhận | Establishes self-certification as a core registration property. |
| E2 | [vvv_qmrf_framework_e02_registration_self_completion_postulate.md](vvv_qmrf_framework_e02_registration_self_completion_postulate.md) | Registration Self-Completion Postulate / Tiên đề Tự hoàn tất Ghi nhận | Establishes completion of the measurement act at the registration layer. |
| E3 | [vvv_qmrf_framework_e03_registration_lock_postulate.md](vvv_qmrf_framework_e03_registration_lock_postulate.md) | Registration Lock Postulate / Tiên đề Khóa Ghi nhận | Defines `V-hat : I_boundary × D → K_R ∪ {k_null}` as the K-side registration-lock function, with P3 distinctness, T6 boundary, and Class D consequence candidates. |
| E4 | [vvv_qmrf_framework_e04_pre_symbolic_registration_stratum_postulate.md](vvv_qmrf_framework_e04_pre_symbolic_registration_stratum_postulate.md) | Pre-Symbolic Registration Stratum Postulate / Tiên đề Tầng Ghi nhận Tiền Biểu tượng | Locates a pre-symbolic registration layer before conceptual classification. |
| E5 | [vvv_qmrf_framework_e05_internal_representation_encoding_postulate.md](vvv_qmrf_framework_e05_internal_representation_encoding_postulate.md) | Internal Representation Encoding Postulate / Tiên đề Mã hóa Biểu diễn Nội tại | Describes internal representation encoding within the registration process. |
| E6 | [vvv_qmrf_framework_e06_registering_system_as_process_postulate.md](vvv_qmrf_framework_e06_registering_system_as_process_postulate.md) | Registering-System-as-Process Postulate / Tiên đề Hệ ghi nhận là Quá trình | Treats the registering system as process rather than substance. |
| E7 | [vvv_qmrf_framework_e07_registration_validity_location_postulate.md](vvv_qmrf_framework_e07_registration_validity_location_postulate.md) | Registration Validity Location Postulate / Tiên đề Định vị Tính hợp lệ Ghi nhận | Locates validity in the registration framework rather than only in physical interaction. |

### 4.3 Extension postulates

| Code | File | Title | Role |
|---|---|---|---|
| E8 | [vvv_qmrf_framework_e08_retroactive_registration_override_postulate.md](vvv_qmrf_framework_e08_retroactive_registration_override_postulate.md) | Retroactive Registration Override Postulate / Tiên đề Phủ quyết Ghi nhận Hồi tố | Covers later correction or invalidation of a prior registration. |
| E9 | [vvv_qmrf_framework_e09_null_registering_system_event_postulate.md](vvv_qmrf_framework_e09_null_registering_system_event_postulate.md) | Null Registering-System Event Postulate / Tiên đề Sự kiện Hệ ghi nhận Rỗng | Covers physical interaction without valid K-side registration encoding. |
| E10 | [vvv_qmrf_framework_e10_tripartite_registration_validity_matrix_postulate.md](vvv_qmrf_framework_e10_tripartite_registration_validity_matrix_postulate.md) | Tripartite Registration Validity Matrix Postulate / Tiên đề Ma trận Hợp lệ Ghi nhận Tam phân | Organizes validity through a three-part registration-validity structure. |
| E11 | [vvv_qmrf_framework_e11_contrapositive_quantum_evidence_registration_postulate.md](vvv_qmrf_framework_e11_contrapositive_quantum_evidence_registration_postulate.md) | Contrapositive Quantum Evidence Registration Postulate / Tiên đề Ghi nhận Bằng chứng Lượng tử Thuần Loại trừ | Covers evidence registration structured through exclusion or contrast. |
| E12 | [vvv_qmrf_framework_e12_limit_faculty_registration_postulate.md](vvv_qmrf_framework_e12_limit_faculty_registration_postulate.md) | Limit-Faculty Registration Postulate / Tiên đề Ghi nhận Giới hạn Năng lực | Covers registration constrained by the capacity of the registering faculty or system. |
| E13 | [vvv_qmrf_framework_e13_temporal_discontinuity_registration_postulate.md](vvv_qmrf_framework_e13_temporal_discontinuity_registration_postulate.md) | Temporal Discontinuity Registration Postulate / Tiên đề Ghi nhận Gián đoạn Thời gian | Covers discontinuity in temporal registration structure. |
| E14 | [vvv_qmrf_framework_e14_validated_absence_registration_postulate.md](vvv_qmrf_framework_e14_validated_absence_registration_postulate.md) | Validated Absence Registration Postulate / Tiên đề Ghi nhận Vắng mặt Hợp lệ | Covers absence as a registration-relevant condition. |
| E15 | [vvv_qmrf_framework_e15_intrinsic_relational_binding_postulate.md](vvv_qmrf_framework_e15_intrinsic_relational_binding_postulate.md) | Intrinsic Relational Binding Postulate / Tiên đề Liên kết Quan hệ Nội tại | Covers intrinsic relation or binding within the registration framework. |
| E16 | [vvv_qmrf_framework_e16_pre_measurement_registration_indeterminacy_postulate.md](vvv_qmrf_framework_e16_pre_measurement_registration_indeterminacy_postulate.md) | Pre-Measurement Registration Indeterminacy Postulate / Tiên đề Bất định Ghi nhận Tiền đo | Covers structured doubt as a registration-state condition. |
| E18 | [vvv_qmrf_framework_e18_delayed_choice_registration_boundary_postulate.md](vvv_qmrf_framework_e18_delayed_choice_registration_boundary_postulate.md) | Delayed-Choice Registration Boundary Postulate / Tiên đề Ranh giới Ghi nhận trong Delayed-Choice | Covers K-side context-conditioned locking of a prior candidate registration window as the operative valid window, with an optional sorting relation when post-selection or coincidence partitioning is needed. |

### 4.4 Supporting documents / Tài liệu hỗ trợ

Các file trong `plan/` và `promote_postulate/` không phải là postulates — chúng là tài liệu quản trị, kế hoạch, và lịch sử hỗ trợ cho việc phát triển và bảo trì framework.

| File | Title / Tiêu đề | Role / Vai trò |
|------|-----------------|----------------|
| [plan/E3_Completion_RCA_Report_2026-05-29.md](plan/E3_Completion_RCA_Report_2026-05-29.md) | E3 Registration Lock — Completion RCA Report | Báo cáo hoàn tất RCA cho E3 ở cấp framework (4.80/5). Ghi nhận canonical E3 update, EX-snapshot sync, và 5 future work items không blocking. |
| [plan/E3_Progress_RCA_2026-05-29.md](plan/E3_Progress_RCA_2026-05-29.md) | E3 Registration Lock — Progress RCA | Kiểm tra tiến độ Plan E3 v2.0: đối chiếu canonical vs plan vs paper vs EX-snapshot. Ghi nhận 6.5/8 steps integrated trước khi completion. |
| [promote_postulate/e18_promotion_history_report.md](promote_postulate/e18_promotion_history_report.md) | E18 Promotion History Report | Lịch sử toàn diện quá trình nâng cấp E18: từ candidate (2026-05-21) → frozen postulate (2026-05-22) qua 7 gates G1–G7. Bao gồm 3 case validations, BE anchor decision, EX recoverability check, và G7 authorization. |
| [promote_postulate/postulate_promotion_protocol.md](promote_postulate/postulate_promotion_protocol.md) | VVV-QMRF Postulate Promotion Protocol v1.0 | Quy trình chuẩn hóa 7-gate (G1–G7) để nâng cấp postulate mới từ candidate → frozen framework postulate. Được rút ra từ E18 path. Dùng làm template cho các lần promotion sau. |

> **Lưu ý:** Các file trong `archives/` là phiên bản cũ của E1–E17 + formal model + index cũ — đã bị thay thế bởi các file active trong thư mục gốc `framework/`. Không dùng archives/ làm nguồn tham chiếu. Thư mục `drafts/` hiện trống (E18 đã được promote ra ngoài qua G7).

---

## 5. Maintenance notes / Ghi chú bảo trì

- Add new framework Markdown files to this index when they are created.
- Keep the file order numerical for E1-E16 postulates; keep interface-principle documents outside the postulate count.
- Do not list system files such as `desktop.ini`.
- Preserve the distinction between `detector response` and `registration-state update`.
- Treat cross-domain Buddhist Epistemology / Quantum Measurement links as mappings unless a source file explicitly provides stronger justification.

---

## Schema Validation Checklist / Checklist Kiểm chứng Schema

| Check | Status | RCA note |
|---|---|---|
| Document type declared | Pass | Declared as `index` for schema alignment. |
| Source traceability | Review required | Add an explicit source corpus before publication reuse. |
| Claim traceability | Review required | Add claim IDs, claim types, source anchors, and boundaries for major claims. |
| Boundary / non-claim guardrail | Pass | Existing boundary/non-claim text limits overclaiming. |
| Validation rule | Pass | Reuse only with source, claim type, and boundary preserved; unresolved items must be marked `TODO(HOTFIX)` before publication use. |
