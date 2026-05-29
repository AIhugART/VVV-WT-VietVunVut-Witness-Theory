Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# VVV-QMRF Research Terminology and Symbol Registry / Bảng Thuật ngữ và Ký hiệu Nghiên cứu VVV-QMRF

**Framework:** VietVunVut Quantum Measurement Registration Framework (VVV-QMRF)  
**Document ID:** VVV-QMRF-REGISTRY-TERMINOLOGY-001  
**Document type:** index  
**Date:** 2026-05-16  
**Status:** derived research registry  
**Purpose:** Provide the technical registry for VVV-QMRF terminology, symbols, claim classes, source traces, and boundary rules.  
**Scope:** Registration-layer terminology and notation used in active VVV-QMRF research documents.  
**Out of scope:** This registry does not define new Standard Quantum Mechanics laws, does not replace canonical QM notation, and does not upgrade VVV-QMRF proposals into peer-reviewed physics.  
**Schema contract:** `documents/research_documents/vvv-qmrf/schema_guide.md`

> **DISCLAIMER / CẢNH BÁO:** VVV-QMRF is independent Class D personal research, not Standard Quantum Mechanics, not peer-reviewed or experimentally validated, and not for real-world technical use. Full boundary protocol: `DISCLAIMER.md`.
>
> VVV-QMRF là nghiên cứu cá nhân độc lập ở Class D, không phải "Standard Quantum Mechanics", chưa "peer-reviewed" hoặc kiểm chứng thực nghiệm, và không dùng cho ứng dụng kỹ thuật ngoài thực tế. Giao thức giới hạn đầy đủ: `DISCLAIMER.md`.

---

## 1. Source Corpus / Tập nguồn

| Source | Role | Required trace |
|---|---|---|
| `documents/research_documents/vvv-qmrf/schema_guide.md` | Schema contract | Document type, symbol registry rule, formula boundary rule, index-document requirements. |
| `documents/research_documents/meta_architecture/vvv_qmrf_meta_architecture_registration_layer_formalization.md` | Primary VVV-QMRF symbol registry source | Symbol class, layer, owner, status, and boundary for the research-level registry. |
| `documents/research_documents/vvv-qmrf/VVV_QMRF_vs_Standard_QM_system_diagram.md` | Layer-boundary support | Separation between physical state `ρ` and registration state `K`; `U_K` does not modify Born-rule probability. |
| `documents/research_documents/framework/vvv_qmrf_framework_e01_self_certifying_registration_postulate.md` | E1 source | `σ(M)`, `R̂_svasa`, `M′`, and K-side self-certification boundary. |
| `documents/research_documents/synthesis/vvv_qmrf_synthesis_s1_lambda_registration_natural_interface_lemma.md` | S1-Λ source | `Λ`, `ε(M)`, and symbolization-interface status as lemma/interface. |
| `documents/research_documents/category/vvv_qmrf_category_13_e14_validated_absence_registration.md` | E14 / VAR source | `Π̂_absent^(ℋ_M)`, null result boundary, and validity-gated absence registration. |
| `SYSTEM_Buddhist_Epistemology/system_be_full.md` | BE SOT when BE node or edge definitions are used | Use only for BE node/edge meanings; BE source terms remain structural lineage, not QM operators. |

---

## 2. RCA Summary / Tóm tắt RCA

### 2.1 Define

**Symptom:** The old file presented VVV-QMRF symbols as a high-school lesson, while the file name and location now require a research-facing technical registry.

**Triệu chứng:** File cũ trình bày ký hiệu như bài học phổ thông, nhưng tên và vị trí mới yêu cầu nó là bảng kỹ thuật nghiên cứu.

### 2.2 Trace — 5 Whys

1. **Why can the registry drift?** Because educational prose can simplify notation without preserving claim class and source trace.  
   **Vì sao bảng có thể lệch?** Vì văn phong giáo dục có thể làm dễ ký hiệu nhưng không giữ đầy đủ loại claim và nguồn.
2. **Why is that risky?** Because VVV-QMRF notation can look like canonical QM notation if the layer is not stated.  
   **Vì sao rủi ro?** Vì ký hiệu VVV-QMRF có thể trông giống ký hiệu QM chuẩn nếu không ghi tầng.
3. **Why does the layer matter?** Because `ρ` belongs to the physical QM side, while `K` belongs to the registration layer.  
   **Vì sao tầng quan trọng?** Vì `ρ` thuộc tầng vật lý QM, còn `K` thuộc tầng ghi nhận.
4. **Why must formula status be declared?** Because symbolic notation can look stronger than the evidence supporting it.  
   **Vì sao phải khai báo trạng thái công thức?** Vì ký hiệu toán học có thể làm claim trông mạnh hơn bằng chứng.
5. **Why is the registry needed?** Because every formula-using document needs a single place to check symbol meaning, claim class, domain, and boundary.  
   **Vì sao cần registry?** Vì mọi tài liệu dùng công thức cần một nơi kiểm tra nghĩa ký hiệu, loại claim, domain, và ranh giới.

### 2.3 Isolate

**Root cause:** The document was classified as `highschool_lesson`, but the actual research need is an `index`-style symbol registry that enforces source trace, claim class, formula boundary, and update rules before symbols are reused.

**Nguyên nhân gốc:** Doc bị đặt ở lớp `highschool_lesson`, trong khi nhu cầu thật là registry dạng `index`, bắt buộc có nguồn, loại claim, ranh giới công thức, và rule cập nhật trước khi dùng lại ký hiệu.

### 2.4 Fix

This file is now normalized as the research-facing VVV-QMRF terminology and symbol registry. Educational documents may simplify the language, but they must not override the status, source trace, layer, or boundary in this registry.

### 2.5 Verify

The root cause is removed only if every retained symbol answers these fields: meaning, domain, claim class, source trace, and boundary.

---

## 3. Registry Admission Rule / Quy tắc đưa ký hiệu vào bảng

Each symbol must score at least **3.5/5** before it is kept in the canonical registry.

| Criterion | Pass condition |
|---|---|
| Meaning EN | The English technical meaning is explicit. |
| Nghĩa VN | The Vietnamese explanation is clear enough for reuse. |
| Domain | The symbol is assigned to `standard QM`, `registration-layer`, `bridge`, `BE-source lineage`, or `proposal`. |
| Claim class | The symbol has a status such as Class A, B, C, D, M, or BE-source. |
| Boundary | The registry states what the symbol must not imply. |

Symbols below 3.5/5 must be moved to a provisional list, sourced more strongly, or removed from formula use.

---

## 4. Claim Class System / Hệ phân loại claim

| Class | Meaning | Usage rule |
|---|---|---|
| Class A | Canonical Standard QM notation | Use as standard QM notation; do not rename as VVV-QMRF notation. |
| Class B | Standard mathematical or conventional label | Safe when context defines it. |
| Class C | Conjectural VVV-QMRF formal definition | Formal inside VVV-QMRF only; not canonical QM. |
| Class D | Proposed VVV-QMRF operator, map, category, or notation | Registration-layer proposal; not source-system physics by itself. |
| Class M | External model, experiment, or exemplar | Evidence/example only; not a VVV-QMRF axiom. |
| BE-source | Buddhist Epistemology source term | Structural lineage or analogy; not a physical operator. |

---

## 5. Claim Traceability / Truy vết claim

| Claim ID | Claim | Type | Source | Boundary |
|---|---|---|---|---|
| C-001 | VVV-QMRF is a registration-layer research framework. | derived | `schema_guide.md`; `registration_layer_formalization.md` | Not Standard Quantum Mechanics and not an empirically validated physical theory. |
| C-002 | `ρ`, `ψ`, `ℋ`, `E_o`, and `p_QM(o)=Tr(E_oρ)` remain physical-side QM notation. | source / external standard | `VVV_QMRF_vs_Standard_QM_system_diagram.md`; standard QM convention | Not replaced by `K`, `𝒦`, or `U_K`. |
| C-003 | `K`, `K_before`, `K_after`, `𝒦`, and `U_K` are VVV-QMRF registration-layer notation. | formal_notation | `registration_layer_formalization.md` | Not physical quantum states or Schrödinger evolution. |
| C-004 | `σ(M)` and `R̂_svasa` are K-side self-certification formalisms. | formal_notation | `vvv_qmrf_framework_e01_self_certifying_registration_postulate.md` | Not consciousness-collapse claims and not Hamiltonian modification. |
| C-005 | `Λ` is a symbolization interface between pre-symbolic and symbolic registration stages. | formal_notation | `vvv_qmrf_synthesis_s1_lambda_registration_natural_interface_lemma.md` | Lemma/interface status; not a separate postulate unless future RCA upgrades it. |
| C-006 | `Π̂_absent^(ℋ_M)` is bounded absence-projection notation for validated absence registration. | formal_notation | `vvv_qmrf_category_13_e14_validated_absence_registration.md` | Valid only inside measurement-accessible subspace `ℋ_M`; not proof of absence outside the tested domain. |
| C-007 | `⊥_K` is a K-side incommensurability relation between registration structures. | formal_notation / conjectural relation | `papers/Testable_Prediction_Section/extended_wigners_friend_k_side_incommensurability/VVV-QMRF_Working_Paper_v2.0.md`; EWF testable-prediction lineage | Not physical orthogonality, not an event-level null value, and not a Standard QM postulate. |
| C-008 | `K_joint` is an admissible joint K-side registration space for testing whether two registration structures can be jointly preserved as valid. | formal_notation / conjectural structure | `papers/Testable_Prediction_Section/extended_wigners_friend_k_side_incommensurability/VVV-QMRF_Working_Paper_v2.0.md`; EWF testable-prediction lineage | Not a physical Hilbert space, not a private observer K-space, and not a new Standard QM state space. |
| C-009 | `M′ ⊥ M` is a registered contradiction relation for later K-side invalidation of a prior registration act. | formal_notation / validity relation | `framework/vvv_qmrf_framework_e07_registration_validity_location_postulate.md`; E7/E8 validity-invalidation lineage | Not physical orthogonality, not ordinary disagreement, and not denial that M physically occurred. |
| C-010 | `requires_K_joint` is a predicate requiring a shared validity demand `D_joint` across two K-side registration structures, determining whether a joint K-side validity check is structurally needed. | formal_notation / predicate | `papers/Testable_Prediction_Section/extended_wigners_friend_k_side_incommensurability/VVV-QMRF_Working_Paper_v2.0.md`; EWF testable-prediction lineage | Not a physical constraint on ρ-side dynamics; `requires_K_joint=0` does not guarantee K_joint exists. |
| C-011 | `Bridge_EWF` is a bridge lemma linking `D_joint` to E7 registered contradiction `M_W ⊥ M_F` in EWF/LF configurations. | formal_notation / bridge lemma | `papers/Testable_Prediction_Section/extended_wigners_friend_k_side_incommensurability/VVV-QMRF_Working_Paper_v2.0.md`; Step 4 proof audit lineage | Class D proposed lemma; application to concrete experiments remains Class C. |
| C-012 | `ODC_K` is an operational data criterion connecting observed EWF/LF probabilities to the existence or failure of an admissible joint K-side registration model. | formal_notation / operational criterion | `papers/Testable_Prediction_Section/extended_wigners_friend_k_side_incommensurability/VVV-QMRF_Working_Paper_v2.0.md`; ODC_K Section 4.6 lineage | Class C proposed criterion; requires predeclared tolerance τ; not a direct detector readout. |

---

## 6. Canonical Symbol Registry / Bảng ký hiệu chuẩn

**RCA admission gate:** Each retained symbol must declare `Domain`, `Notation type`, `Claim class`, `Status`, `Source trace`, `Usage rule`, and `Boundary`. A symbol below **3.5/5** on meaning, Vietnamese clarity, domain, claim class, and boundary must be marked `provisional`, folded into an existing symbol, or removed before publication-facing reuse.

### 6.1 Standard QM reference symbols / Ký hiệu tham chiếu QM chuẩn

| Symbol | Meaning EN | Nghĩa VN | Domain | Notation type | Claim class | Status | Source trace | Usage rule | Boundary |
|---|---|---|---|---|---|---|---|---|---|
| `ρ` | Physical quantum state description, often a density operator. | Mô tả trạng thái lượng tử vật lý. | standard QM | mathematical state symbol | Class A | active | `registration_layer_formalization.md`; `VVV_QMRF_vs_Standard_QM_system_diagram.md` | Use only for the physical quantum layer. | Not a K-side registration state. |
| `ρ_before` / `ρ_o` | Pre-measurement and outcome-conditioned physical-state labels. | Nhãn trạng thái vật lý trước đo và trạng thái vật lý có điều kiện theo outcome. | standard QM | mathematical state label | Class A/B | active | system diagram; `registration_layer_formalization.md` | Use only for physical-side before/after labels in diagrams. | Not `K_before`, `K_after`, or a K-side registration state. |
| `D(ℋ)` | Density-operator state space over `ℋ`. | Không gian/tập các toán tử mật độ trên `ℋ`. | standard QM | mathematical set notation | Class A/B | active | `registration_layer_formalization.md` | Use when writing `ρ ∈ D(ℋ)`. | Not the registration-state space `𝒦`. |
| `ψ` | Wave function or state vector notation where context allows. | Ký hiệu hàm sóng hoặc vector trạng thái khi ngữ cảnh cho phép. | standard QM | mathematical state symbol | Class A | active | Standard QM convention; registry support docs | Use where a wave-function/state-vector context is explicit. | Not VVV-QMRF registration state. |
| `ℋ` | Hilbert space for physical quantum states. | Không gian Hilbert của trạng thái vật lý. | standard QM | mathematical space symbol | Class A | active | `registration_layer_formalization.md` | Use for physical quantum-state space. | Not the registration-state space `𝒦`. |
| `ℋ_S ⊗ ℋ_A` | Composite physical Hilbert space for system plus apparatus. | Không gian Hilbert tích tensor cho hệ và apparatus. | standard QM | composite-space notation | Class A/B | active | `registration_layer_formalization.md` | Use only for the physical interaction substrate. | Not `𝒦` and not a registration-state space. |
| `Ĥ` | Hamiltonian operator for physical dynamics. | Toán tử Hamiltonian cho động lực học vật lý. | standard QM | mathematical operator | Class A | active | Standard QM convention; E1 boundary | Use only for physical dynamics. | Not modified by `σ(M)` or `R̂_svasa`. |
| `𝒮` / `S` | Quantum system being measured. | Hệ lượng tử đang được đo. | standard QM | system label | Class A/B | active | `registration_layer_formalization.md` | Use only as the physical-side measured-system label. | Not the registering system `R`. |
| `𝒜` / `A` | Apparatus or measuring device. | Thiết bị đo hoặc apparatus. | standard QM | apparatus label | Class A/B | active | `registration_layer_formalization.md` | Use only as the physical-side apparatus label. | A detector response is not automatically valid K-side registration. |
| `E_o` | Measurement effect associated with outcome `o`. | Hiệu ứng đo gắn với outcome `o`. | standard QM | mathematical effect symbol | Class A | active | `registration_layer_formalization.md`; system diagram | Use for QM measurement effects. | Not a VVV-QMRF operator. |
| `M = {E_o}` | QM measurement represented as effects/outcomes. | Phép đo QM dưới dạng tập hiệu ứng/outcome. | standard QM | mathematical measurement notation | Class A | active | `registration_layer_formalization.md`; system diagram | Use for physical-side measurement setting. | Distinguish from K-side `M` as measurement-registration act. |
| `p_QM(o)=Tr(E_oρ)` | Born-rule probability for outcome `o`. | Xác suất Born-rule cho outcome `o`. | standard QM | probability formula | Class A | active | `registration_layer_formalization.md`; system diagram | Use as the preserved Standard QM probability rule. | Not replaced by `U_K`. |
| `ρ_after` | Post-measurement physical state. | Trạng thái vật lý sau phép đo. | standard QM | mathematical state symbol | Class A | active | `registration_layer_formalization.md`; system diagram | Use for physical post-measurement state. | Not the same as `K_after`. |

### 6.2 Registration-state symbols / Ký hiệu trạng thái ghi nhận

| Symbol | Meaning EN | Nghĩa VN | Domain | Notation type | Claim class | Status | Source trace | Usage rule | Boundary |
|---|---|---|---|---|---|---|---|---|---|
| `K` | Registration state. | Trạng thái ghi nhận. | registration-layer | mathematical state symbol | Class D | active | `registration_layer_formalization.md` | Use for the K-side registration layer only. | Not the physical state `ρ`. |
| `k` | One element of `𝒦`. | Một phần tử của không gian trạng thái ghi nhận `𝒦`. | registration-layer | mathematical element symbol | Class C | active | `registration_layer_formalization.md` | Use for a formal registration-state element. | Not a vector in `ℋ`. |
| `𝒦` | K-side registration-state space. | Không gian trạng thái ghi nhận phía K. | registration-layer | mathematical space symbol | Class C | active | `registration_layer_formalization.md` | Use for the formal space of K-side states. | Not `ℋ` and not canonical QM state space. |
| `𝒦_pre` | Pre-symbolic registration stratum. | Tầng ghi nhận tiền biểu tượng. | registration-layer | stratum symbol | Class C/D | active / boundary-sensitive | `registration_layer_formalization.md`; S1-Λ source | Use for pre-symbolic K-side registration only. | Not raw consciousness. |
| `𝒦_sym` | Symbolic registration stratum. | Tầng ghi nhận đã có biểu tượng/ký hiệu. | registration-layer | stratum symbol | Class C/D | active / boundary-sensitive | `registration_layer_formalization.md`; S1-Λ source | Use for symbolically encoded K-side registration. | Not Born-rule probability space. |
| `K_before` | Prior registration state before registered outcome update. | Trạng thái ghi nhận trước khi outcome được ghi nhận. | registration-layer | mathematical state symbol | Class D | active | `registration_layer_formalization.md`; system diagram | Use for the starting K-side state in `U_K`. | Not a pre-measurement wavefunction. |
| `K_after` | Posterior registration state after registered outcome update. | Trạng thái ghi nhận sau khi outcome được ghi nhận. | registration-layer | mathematical state symbol | Class D | active | `registration_layer_formalization.md`; system diagram | Use for the result of K-side registration-state update. | Not a new density matrix. |
| `cert` | Self-certification marker. | Dấu chứng nhận rằng sự kiện ghi nhận đã xảy ra. | registration-layer | status marker | Class C | active | `registration_layer_formalization.md`; E1 source | Use as a formal occurrence-certification marker. | Formal marker only; not consciousness. |
| `t(M)` | Registration time of `M`. | Thời điểm ghi nhận của `M`. | registration-layer | time parameter | Class B/D | active / boundary-sensitive | `registration_layer_formalization.md` | Use for timing of a K-side registration event. | Not a claim that physical time itself is discrete. |
| `t` | Registration-time component inside a K-state tuple. | Thành phần thời điểm ghi nhận trong tuple trạng thái K. | registration-layer | tuple component | Class B/D | active / boundary-sensitive | `registration_layer_formalization.md` | Use only inside K-state tuples. | Not proof that physical time is discrete. |
| `V` | Validity status component inside a K-state tuple. | Thành phần trạng thái hợp lệ trong tuple trạng thái K. | registration-layer | tuple component / status label | Class D | active | `registration_layer_formalization.md` | Use for K-side validity status. | Not absolute metaphysical truth and not a physical observable. |

### 6.3 Registration update and event symbols / Ký hiệu cập nhật và sự kiện ghi nhận

| Symbol | Meaning EN | Nghĩa VN | Domain | Notation type | Claim class | Status | Source trace | Usage rule | Boundary |
|---|---|---|---|---|---|---|---|---|---|
| `U_K` | Registration update rule. | Quy tắc cập nhật trạng thái ghi nhận. | registration-layer | update function | Class D | active / boundary-sensitive | `registration_layer_formalization.md`; system diagram | Use only for `K_before → K_after`. | Not Schrödinger evolution, unitary physical dynamics, Born-rule probability, or physical collapse. |
| `o` | Outcome supplied by the physical measurement side to the K-side update. | Outcome được phía vật lý cung cấp cho cập nhật tầng K. | bridge / interface | outcome label | Class B/D | active | `registration_layer_formalization.md`; system diagram | Use as the bridge input from physical outcome to registration update. | Outcome probabilities remain governed by QM. |
| `D_o` | Detector response associated with outcome `o`. | Phản hồi detector gắn với outcome `o`. | bridge / interface | physical trace label | Class B | active | system diagram; S1 registration pipeline | Use only for apparatus physical response before validated K-side registration. | Not identical to `K_after` or `registration-state update`. |
| `I` | Physical interaction entering possible registration. | Tương tác vật lý có thể đi vào ghi nhận. | bridge / interface | event label | Class B | active | `registration_layer_formalization.md` | Use for a physical interaction that may feed registration. | Not every `I` becomes a valid `M`. |
| `M` | Measurement-registration act. | Hành vi đo-ghi nhận ở tầng K. | registration-layer | event / act symbol | Class D | active / overloaded | `registration_layer_formalization.md`; E1 source | Use for K-side measurement-registration act; specify when contrasting with `M={E_o}`. | Not identical to a bare physical interaction `I` or to `M={E_o}`. |
| `M′` | Later registration act that may challenge a prior registration. | Hành vi ghi nhận sau có thể thách thức ghi nhận trước. | registration-layer | meta-event symbol | Class D | active | E1/E7 source | Use only for secondary, later, or comparison-stage registration acts. | Not required for primary self-certification under E1. |
| `M′ ⊥ M` | Registered contradiction relation between a later act and a prior act. | Quan hệ mâu thuẫn ghi nhận giữa hành vi sau và hành vi trước. | registration-layer | validity relation | Class D | active / boundary-sensitive | E7 source; `registration_layer_formalization.md` | Use only when M′ and M share an admissible K-side comparison context, concern the same target/history/validity claim, cannot jointly satisfy validity conditions, and M′ itself has valid registration authority. | Not physical orthogonality, not ordinary disagreement, and not proof that M did not physically occur. |
| `σ(M)` | Self-certification function. | Hàm tự chứng nhận sự kiện `M`. | registration-layer | certification function | Class D | active / boundary-sensitive | E1 source; `registration_layer_formalization.md` | Use for K-side occurrence certification. | Certifies occurrence of `M` without `M′`; not a detector Hamiltonian. |
| `R̂_svasa` | Reflexive registration operator. | Toán tử ghi nhận phản thân. | registration-layer / BE-source lineage | proposed operator | Class D | active / boundary-sensitive | E1 source; Category 05 source pointer inside E1 | Use only as proposed K-side self-certification notation. | Not a consciousness-collapse operator. |
| `≡^K` | K-side act-result inseparability. | Tính không tách rời giữa hành vi và kết quả ở tầng K. | registration-layer | relation symbol | Class D | active | `registration_layer_formalization.md` | Use for K-side act-result closure. | Not physical identity in `ℋ`. |

### 6.4 Core registration operators, maps, and relations / Toán tử, ánh xạ, và quan hệ ghi nhận lõi

| Symbol | Meaning EN | Nghĩa VN | Domain | Notation type | Claim class | Status | Source trace | Usage rule | Boundary |
|---|---|---|---|---|---|---|---|---|---|
| `C` / `C_R` | Registration lock. | Khóa interaction thành trạng thái đã được ghi nhận. | bridge / interface | mapping / lock symbol | Class D | active | `registration_layer_formalization.md`; E3 source | Use for locking available interaction into registered status. | Does not by itself collapse `ρ`. |
| `ε(M)` | Pre-symbolic registration event. | Sự kiện ghi nhận tiền biểu tượng. | bridge / interface | pre-symbolic event symbol | Class D | active | `registration_layer_formalization.md`; E4 source; S1-Λ source | Use for the first K-side intake of a physical trace. | Not a mystical perception event. |
| `Λ` | Symbolization operator. | Toán tử biểu tượng hóa. | bridge / interface | symbolization map | Class D | active / boundary-sensitive | `registration_layer_formalization.md`; S1-Λ source | Use for mapping pre-symbolic registration into symbolic result. | Not the Born rule and not a new physical interaction Hamiltonian. |
| `r` | Symbolic registered result. | Kết quả ghi nhận đã được biểu tượng hóa. | registration-layer | result symbol | Class D | active | `registration_layer_formalization.md`; S1-Λ source | Use for K-side symbolic result. | Not the physical outcome probability itself. |
| `f_enc` | Internal encoding map. | Ánh xạ mã hóa nội tại. | registration-layer | encoding map | Class D | active | `registration_layer_formalization.md`; E5 source | Use for internal K-side encoding of a registered result. | Not a second apparatus. |
| `\|R_k⟩_A` | Apparatus record state carrying outcome-indexed content. | Trạng thái bản ghi của apparatus mang nội dung theo chỉ số outcome. | bridge / interface | record-state notation | Class B/D | active / boundary-sensitive | `registration_layer_formalization.md`; E5 source | Use only inside the internal encoding expression. | Not `K_after` and not a second apparatus measurement. |
| `a_k` | Internally encoded outcome/eigenvalue content. | Nội dung outcome/eigenvalue được mã hóa nội tại. | bridge / interface | outcome-content label | Class B/D | active | `registration_layer_formalization.md`; E5 source | Use as the content encoded by `f_enc`. | Not a new probability law or external validation. |
| `Ā` / `Â_kara` | Internal representation encoding operator. | Toán tử mã hóa biểu tượng nội tại. | registration-layer / BE-source lineage | encoding operator | Class D | active / normalized alias | `registration_layer_formalization.md`; Category 08; system diagram | Prefer `Ā` in compact diagrams and trace `Â_kara` as source notation. | Source lineage only; not mystical cognition. |
| `V_yava` / `V̂_yava` | Irreversible registration lock. | Khóa ghi nhận không đảo ngược ở tầng K. | registration-layer / BE-source lineage | registration-lock operator | Class D | active / normalized alias | `registration_layer_formalization.md`; Category 08; system diagram | Prefer `V_yava` in compact diagrams and trace `V̂_yava` as source notation. | Registration lock, not proof of physical irreversibility. |
| `V(M,t)` / `V(M)` | Validity status function. | Hàm trạng thái hợp lệ của ghi nhận. | registration-layer | validity function | Class D | active | `registration_layer_formalization.md`; E7 source | Use for K-side validity status. | K-side validity, not absolute metaphysical truth. |
| `⊥` | Registration contradiction relation. | Quan hệ mâu thuẫn ở tầng ghi nhận. | registration-layer | relation symbol | Class B/D | active | `registration_layer_formalization.md` | Use for K-side contradiction unless explicitly specified otherwise. | Not physical orthogonality unless separately specified. |
| `K_joint` | Admissible joint K-side registration space for joint validity preservation. | Không gian ghi nhận chung phía K dùng để kiểm tra hai cấu trúc ghi nhận có thể cùng hợp lệ hay không. | registration-layer | joint-space symbol | Class D | active / conjectural | `VVV-QMRF_Working_Paper_v2.0.md`; EWF testable-prediction lineage | Use only when testing whether two K-side registration structures can embed into one candidate space while preserving self-certification, order, validity, and non-invalidation constraints. | Not a Hilbert space, not an observer's private K-space, not a mere record list, and not a Standard QM state space. |
| `⊥_K` | K-side incommensurability relation between registration structures. | Quan hệ không thể gom chung hợp lệ giữa các cấu trúc ghi nhận phía K. | registration-layer | relation symbol | Class D | active / conjectural | `VVV-QMRF_Working_Paper_v2.0.md`; EWF testable-prediction lineage | Use for `A ⊥_K B` only when `requires_K_joint(A,B)=1` and no admissible `K_joint` preserves both sides as jointly valid under self-certification, registration-order, validity, and non-invalidation constraints. | Not physical orthogonality, not an event-level null value such as `Null_K(e)`, and not a Standard QM postulate. |
| `R=<M_1,M_2,...,M_n>` | Registering system as process. | Hệ ghi nhận như một chuỗi sự kiện. | registration-layer | process notation | Class D | active | `registration_layer_formalization.md`; E6 source | Use for ordered registration-event series. | Not a fixed substantial observer. |
| `𝐈_R` / `I_R` | Hypothetical independent identity marker for `R`. | Dấu giả định về một bản sắc độc lập của `R`. | registration-layer | negated identity marker | Class D | active only under negation | `registration_layer_formalization.md`; E6 source | Use only in `¬∃𝐈_R` style process-identity constraints. | Not a physical identity matrix for the apparatus. |
| `M_i` | Indexed registration event inside process `R`. | Sự kiện ghi nhận có chỉ số trong tiến trình `R`. | registration-layer | indexed event symbol | Class D | active | `registration_layer_formalization.md`; E6/S2 support | Use for ordered K-side registration events. | Not a sequence of physical collapses. |
| `Δ(M_i,M_{i+1})` | Temporal registration gap. | Khoảng gián đoạn giữa hai lần ghi nhận. | registration-layer | temporal relation symbol | Class D | active / boundary-sensitive | `registration_layer_formalization.md`; E13/S2 support | Use for K-side discontinuity between registration events. | Not proof that physical time is discrete. |
| `RegistrationState(t)` | Active K-side registration-state identity at time `t`. | Bản sắc trạng thái ghi nhận đang hoạt động tại thời điểm `t`. | registration-layer | temporal status function | Class D | active / boundary-sensitive | `registration_layer_formalization.md`; S2-Δ support | Use only for K-side registration continuity/gap statements. | Not the physical quantum state as a function of time. |
| `Sym(ε(M))=∅` | No symbolic value at the pre-symbolic stage. | Chưa có giá trị biểu tượng ở tầng tiền biểu tượng. | registration-layer | constraint formula | Class D | active | `registration_layer_formalization.md`; E4 source | Use to mark pre-symbolic status before `Λ`. | Not absence of physical interaction. |

### 6.5 Extended proposed category symbols / Ký hiệu đề xuất mở rộng theo category

| Symbol | Meaning EN | Nghĩa VN | Domain | Notation type | Claim class | Status | Source trace | Usage rule | Boundary |
|---|---|---|---|---|---|---|---|---|---|
| `P_null` / `P̂_null` | Null-projection registration operator. | Toán tử ghi nhận chiếu-rỗng. | proposal / bridge | proposed operator | Class D | active / boundary-sensitive | `registration_layer_formalization.md`; Category 01 | Use for null-projection registration support. | Built on projection support; not canonical PVM by itself. |
| `Π̂_absent^(ℋ_M)` | Bounded absence projection. | Phép chiếu vắng mặt có giới hạn bởi không gian đo được `ℋ_M`. | proposal / bridge | proposed operator | Class D support | active / boundary-sensitive | E14 / VAR source | Use only for validated absence inside the declared accessible subspace. | Valid only inside measurement-accessible subspace `ℋ_M`. |
| `ℋ_M` | Measurement-accessible subspace used by VAR. | Không gian con mà thiết lập đo có thể kiểm tra. | bridge / interface | subspace symbol | Class B/D | active | E14 / VAR source | Use to bound validated-absence claims. | Does not cover what the setup cannot validly test. |
| `I_(ℋ_M)` | Identity operator on `ℋ_M`. | Toán tử đơn vị trên không gian con `ℋ_M`. | bridge / interface | mathematical operator | Class B | active | E14 / VAR source | Use only inside the VAR absence-projection expression. | Only scoped to the declared measurement-accessible subspace. |
| `λ_i` | Tested property/eigenvalue label inside `ℋ_M`. | Nhãn thuộc tính/eigenvalue được kiểm tra trong `ℋ_M`. | bridge / interface | eigenvalue/property label | Class B | active | E14 / VAR source | Use for tested alternatives in `ℋ_M`. | Absence claim applies only to the tested set. |
| `Ĉ_ext` | Extrinsic registration-certification operator. | Toán tử chứng nhận ghi nhận từ ngoài. | proposal / registration-layer | proposed operator | Class D | active / boundary-sensitive | `registration_layer_formalization.md`; Category 04 | Use for proposed certification of registration status. | Certification layer, not environmental decoherence itself. |
| `ρ̃` | Conditionally updated physical state. | Trạng thái vật lý được cập nhật có điều kiện. | proposal / bridge | provisional state notation | Class D | provisional | `registration_layer_formalization.md`; Category 04 | Use only when provisional certification status is explicit. | Provisional notation; not a new density-matrix law. |
| `ρ_certified` | Certified registration-status label. | Nhãn trạng thái ghi nhận đã được chứng nhận. | proposal / bridge | status label | Class D | provisional | `registration_layer_formalization.md`; Category 04 | Use as a status label, not as a canonical physical state. | Status label, not a canonical physical state. |
| `𝒯_act-res` | Act-result tensor. | Tensor nối hành vi-kết quả ở tầng ghi nhận. | proposal / registration-layer | proposed tensor | Class D | active / boundary-sensitive | `registration_layer_formalization.md`; Category 02 | Use for K-side act-result inseparability. | Not a Born-rule tensor. |
| `Ô_bhranti` | Invalidation / registration override operator. | Toán tử phủ quyết hoặc ghi đè ghi nhận. | proposal / registration-layer | proposed operator | Class D | active / boundary-sensitive | `registration_layer_formalization.md`; Category 03 | Use for K-side registration-status override. | Reclassifies registration status; does not alter physical history. |
| `Ê_empty` | Null registration operator. | Toán tử ghi nhận rỗng. | proposal / registration-layer | proposed operator | Class D | active / boundary-sensitive | `registration_layer_formalization.md`; Category 06 | Use for K-side non-engagement after interaction. | Marks non-engagement after interaction; not every no-result measurement. |
| `Π̂_causal` | Causal memory projection. | Phép chiếu ký ức nhân quả ở tầng ghi nhận. | proposal / registration-layer | proposed operator | Class D | active / boundary-sensitive | `registration_layer_formalization.md`; Category 07 | Use for continuity across registering moments. | Continuity without identity; not hidden-variable memory. |
| `𝕍_tri` | Tripartite apparatus validity tensor / criteria set. | Bộ tiêu chí/tensor hợp lệ ba phần. | proposal / registration-layer | criteria-set symbol | Class D | active | `registration_layer_formalization.md`; Category 09 / E10 | Use as a validity gate for registration authority. | Validity gate, not detector physics itself. |
| `M̂_trans` | Limit-faculty registration operator. | Toán tử ghi nhận của năng lực giới hạn. | proposal / registration-layer | proposed operator | Class D | active / boundary-sensitive | `registration_layer_formalization.md`; Category 11 / E12 | Use for validity-gated non-ordinary registration. | Not new eigenvalue physics. |
| `T̂_kṣaṇa` | Discrete transition operator. | Toán tử chuyển đoạn rời rạc của ghi nhận. | proposal / registration-layer | proposed operator | Class D | active / boundary-sensitive | `registration_layer_formalization.md`; Category 12 / E13 | Use for K-side registration transition. | Not replacement for quantum jump operators. |
| `Ŝ_saṃśaya` | Structured registration-doubt operator. | Toán tử nghi vấn ghi nhận có cấu trúc. | proposal / registration-layer | proposed operator | Class D | active / boundary-sensitive | `registration_layer_formalization.md`; Category 15 / E16 | Use for pre-measurement K-side suspension over alternatives. | K-side suspension, not hidden-variable ignorance. |
| `ℰ_svabh` | Intrinsic relational binding symbol. | Ký hiệu liên kết quan hệ nội tại. | proposal / registration-layer relation | folded relation symbol | Class D folded symbol | folded | `registration_layer_formalization.md`; Category 14 / E15 | Keep folded into the intrinsic relational binding category. | Not a new physical force. |
| `δ(o)` | Possible empirical difference marker for outcome statistics. | Dấu hiệu khác biệt thực nghiệm có thể có cho thống kê outcome. | proposal / empirical status | difference marker | Class D / empirical_status | provisional | system diagram claim ladder; formal model boundary | Use only when discussing whether VVV-QMRF has a nonzero testable difference. | No experimental validation claim without a defined nonzero model and tests. |

### 6.6 BE-source lineage labels / Nhãn dòng nguồn Phật học

| Label | Meaning EN | Nghĩa VN | Domain | Notation type | Claim class | Status | Source trace | Usage rule | Boundary |
|---|---|---|---|---|---|---|---|---|---|
| `Svasaṃvedana` | Self-awareness as BE source lineage for self-certification. | Tự tri như dòng nguồn BE cho tự chứng nhận. | BE-source lineage | source label | BE-source | active | `SYSTEM_Buddhist_Epistemology/system_be_full.md`; E1 source | Use only as BE source lineage. | Not a consciousness-collapse mechanism. |
| `Pramāṇa-phala` | Act-result relation as BE source lineage. | Quan hệ phương tiện-kết quả nhận thức. | BE-source lineage | source label | BE-source | active | `SYSTEM_Buddhist_Epistemology/system_be_full.md`; E2/Category 02 sources | Use only as source-side lineage for act-result structure. | Structural lineage only, not QM identity. |
| `Apoha` | Exclusion as BE source lineage. | Loại trừ như dòng nguồn BE. | BE-source lineage | source label | BE-source | active | `SYSTEM_Buddhist_Epistemology/system_be_full.md`; mapping sources | Use only as source-side exclusion lineage. | Not identical to quantum complementarity. |
| `Anupalabdhi` | Non-perception / absence cognition as BE source lineage. | Vắng mặt được nhận biết hợp lệ. | BE-source lineage | source label | BE-source | active | `SYSTEM_Buddhist_Epistemology/system_be_full.md`; E14 / VAR source | Use only as source-side absence-cognition lineage. | Not a physical substance or a canonical QM operator. |
| `Trairūpya` | Three-condition validity criterion as source lineage. | Tiêu chuẩn ba điều kiện cho tính hợp lệ. | BE-source lineage | source label | BE-source | active | `SYSTEM_Buddhist_Epistemology/system_be_full.md`; E10/E14 sources | Use only as source-side validity lineage. | Validity gate analogue, not native QM formalism. |

### 6.7 Code and diagram relation registry / Bảng mã và quan hệ sơ đồ

| Symbol / code | Meaning EN | Nghĩa VN | Domain | Notation type | Claim class | Status | Source trace | Usage rule | Boundary |
|---|---|---|---|---|---|---|---|---|---|
| `P1–P4` | Standard QM physical postulate codes. | Mã bốn postulate vật lý của QM chuẩn. | standard QM | postulate code | Class A | active | `system_qm_full.md`; schema guide | Use only for Standard QM state space, observables, measurement, and dynamics. | Not VVV-QMRF registration postulates. |
| `E1–E16` | VVV-QMRF registration-layer postulate codes. | Mã postulate tầng ghi nhận của VVV-QMRF. | registration-layer | postulate code | Class D | active | active VVV-QMRF framework/category documents | Use only for VVV-QMRF registration-layer structure. | Not Standard QM physical postulates. |
| `N_BE_00001` etc. | Buddhist Epistemology node codes. | Mã node Buddhist Epistemology. | BE-source lineage | node code | BE-source | active | `SYSTEM_Buddhist_Epistemology/system_be_full.md` | Use for BE source trace and RCA only. | Not QM/VVV-QMRF physical operators. |
| `ED_BE_00001` etc. | Buddhist Epistemology edge codes. | Mã edge Buddhist Epistemology. | BE-source lineage | edge code | BE-source | active | `SYSTEM_Buddhist_Epistemology/system_be_full.md` | Use for BE source relation trace and RCA only. | Source relation is not physical causation. |
| `N_QM_VVV_00001` etc. | VVV-QMRF quantum-measurement concept node codes. | Mã node concept VVV-QMRF trong domain đo lượng tử. | registration-layer | node code | Class D | active | `node_QM_VVV.md`; `dictionary.md` | Use for VVV-QMRF concept indexing. | Not canonical QM node codes. |
| `→` | Directed relation or process progression declared by context. | Quan hệ có hướng hoặc tiến trình theo ngữ cảnh. | diagram relation | diagram arrow | metadata | active | schema guide; system diagram | Use only with an explicit relation label or nearby context. | Does not automatically imply physical causation. |
| `-. label .->` | Dashed labeled relation in Mermaid diagrams. | Mũi tên đứt có nhãn trong Mermaid. | diagram relation | diagram arrow | metadata | active | schema guide; system diagram | Use for boundary, support, or interpretive relation labels. | Not automatic derivation or physical interaction. |
| `<=>` | Structural equivalence marker when explicitly justified. | Dấu tương ứng cấu trúc khi đã nêu lý do. | diagram relation | mapping relation | metadata | reserved / boundary-sensitive | schema guide; mapping rules | Use only for declared structural mapping output. | Not identity unless separately proven. |

### 6.8 EWF/LF testable-prediction symbols / Ký hiệu dự đoán kiểm chứng EWF/LF

| Symbol | Meaning EN | Nghĩa VN | Domain | Notation type | Claim class | Status | Source trace | Usage rule | Boundary |
|---|---|---|---|---|---|---|---|---|---|
| `D_joint` | Shared validity demand requiring two K-side registration structures to be assessed under one comparison architecture. | Yêu cầu hợp lệ chung — đòi hỏi hai cấu trúc ghi nhận phía K được đánh giá trong cùng một kiến trúc so sánh. | registration-layer / EWF | validity-demand symbol | Class D | active / conjectural | `VVV-QMRF_Working_Paper_v2.0.md` §4.3; EWF testable-prediction lineage | Use only when a shared cross-observer validity constraint is structurally required. | Not a physical postulate; not imposed by mere database co-location. |
| `requires_K_joint` | Predicate: `requires_K_joint(A,B)=1` iff a `D_joint` is structurally imposed and cannot be evaluated without a candidate `K_joint`. | Vị từ "yêu cầu K_joint" — bằng 1 khi `D_joint` được áp đặt và không thể đánh giá nếu không có `K_joint`. | registration-layer / EWF | predicate | Class D | active / conjectural | `VVV-QMRF_Working_Paper_v2.0.md` §4.3; EWF testable-prediction lineage | Operational sufficient conditions A-E are provided; necessary-and-sufficient core is via `D_joint`. | `requires_K_joint=0` does not guarantee `K_joint` exists; it only means the joint check is not structurally demanded. |
| `AdmJoint` | Admissible joint K-side registration space predicate: `AdmJoint(K_joint; A,B)=1` iff a candidate `K_joint` preserves both A and B under Conditions 1-6. | Vị từ "K_joint khả chấp" — bằng 1 khi một `K_joint` ứng viên bảo toàn cả A và B dưới Conditions 1-6. | registration-layer / EWF | predicate | Class D | active / conjectural | `VVV-QMRF_Working_Paper_v2.0.md` §4.3; F-EWF-000 | Test whether two K-side structures embed into one joint space under all preservation constraints. | Not a physical Hilbert space test. |
| `Bridge_EWF` | Bridge lemma: `Bridge_EWF(D_joint; M_F, M_W)=1` iff `D_joint` necessarily instantiates `M_W ⊥ M_F` in an EWF/LF configuration. | Bổ đề cầu nối — bằng 1 khi `D_joint` tất yếu tạo ra `M_W ⊥ M_F` trong cấu hình EWF/LF. | registration-layer / EWF | bridge lemma | Class D/C | active / boundary-sensitive | `VVV-QMRF_Working_Paper_v2.0.md` §4.5; Step 4 proof audit lineage | Apply only when the LF comparison requires both claims as one cross-observer validity constraint. | Class D proposed lemma; application to concrete experiments remains Class C. |
| `ODC_K` | Operational data criterion: `ODC_K(Data, Cfg)` returns `K_joint_exists` or `K_joint_fails` based on whether a joint registration model J_K fits observed data under predeclared tolerance τ. | Tiêu chí dữ liệu vận hành — trả về `K_joint_exists` hoặc `K_joint_fails` dựa trên việc mô hình J_K có khớp dữ liệu quan sát dưới dung sai τ đã khai báo trước. | bridge / operational | operational criterion | Class C | active / boundary-sensitive | `VVV-QMRF_Working_Paper_v2.0.md` §4.6; ODC_K lineage | τ must be fixed before data evaluation; otherwise criterion becomes post hoc. | Not a direct detector readout; not a claim that Standard QM is falsified if `K_joint_fails`. |
| `Null_K(e)` | Event-level registration null: event `e` fails to enter any valid K-side registration domain. | Sự kiện không vào được miền ghi nhận hợp lệ phía K. | registration-layer | null marker | Class D | active / boundary-sensitive | `VVV-QMRF_Working_Paper_v2.0.md` §4.4; `⊥_K` boundary clauses | Use `Null_K(e)` or `R_K(e) = ⊥` for single-event failure to register. | Do not use `⊥_K` for this purpose; `⊥_K` is a relation, not a value. |

---

## 7. Formula Inventory / Danh sách công thức

| Formula ID | Formal expression | Formula class | Domain of validity | Source trace | Interpretation boundary |
|---|---|---|---|---|---|
| F-K-001 | `k ∈ 𝒦; k=<M,o,cert,t,V>` | definition | Minimal K-side registration-state tuple. | `registration_layer_formalization.md` | Defines registration state only; not a physical state vector or density matrix. |
| F-K-002 | `K_after = U_K(K_before,o)` | heuristic_formalization | K-side registration-state update after a physical outcome is available. | `registration_layer_formalization.md`; system diagram | Not Schrödinger evolution, Born-rule probability, or physical collapse. |
| F-E1-001 | `σ(M)=1 iff M occurred as K-side registration` | definition | K-side self-certification marker for E1. | E1 framework source | Does not require `M′`; not consciousness-caused collapse. |
| F-E2-001 | `M ≡^K r` | heuristic_formalization | K-side registration self-completion. | `registration_layer_formalization.md`; E2 source | Act-result inseparability inside `𝒦`; not physical identity in `ℋ`. |
| F-E7-001 | `V(M)=1; if M′ ⊥ M and M′ has valid registration authority in the comparison context, then V(M)->0` | constraint | K-side validity and invalidation by registered contradiction. | `registration_layer_formalization.md`; E7/E8 sources | K-side validity rule; not universal metaphysical truth and not denial that M physically occurred. |
| F-S1-001 | `I -> ε(M) -> Λ(ε(M))=r` | lemma_expression | Registration flow from interaction to symbolic result. | `registration_layer_formalization.md`; S1-Λ source | Not a replacement for detector physics. |
| F-E3-001 | `C: ℋ -> 𝒦; C(I)=k_locked` | mapping_function | Bridge from available interaction to locked registration status. | `registration_layer_formalization.md`; E3 source | Does not by itself collapse `ρ`. |
| F-E4-001 | `ε(M) ∈ 𝒦_pre; Sym(ε(M))=∅` | definition | Pre-symbolic registration stage. | `registration_layer_formalization.md`; E4 source | No symbolic value yet; not absence of physical interaction. |
| F-S1-002 | `Λ: 𝒦_pre -> 𝒦_sym; r=Λ(ε(M))` | lemma_expression | Symbolization interface between E4 and E5. | S1-Λ source | Interface/lemma status; not a separate postulate by default. |
| F-E5-001 | `∃ f_enc: \|R_k⟩_A ↦ a_k internally within 𝒦` | heuristic_formalization | Internal encoding of registered content after symbolization. | `registration_layer_formalization.md`; E5 source | Not a second apparatus measurement, hidden variable, or physical observable. |
| F-E6-001 | `R=<M_1,M_2,...,M_n>; t(M_1)<...<t(M_n); ¬∃𝐈_R independent of {M_i}` | constraint | Registering system modeled as ordered K-side process. | `registration_layer_formalization.md`; E6 source | Not a fixed observer, soul, or single physical apparatus identity. |
| F-S2-001 | `∀t∈(t(M_i),t(M_{i+1})), RegistrationState(t)=∅` | lemma_expression | K-side temporal registration gap between registration events. | `registration_layer_formalization.md`; S2-Δ support | Not a claim that physical time is discontinuous. |
| F-E14-001 | `Π̂_absent^(ℋ_M)=I_(ℋ_M)-Σ_i \|λ_i><λ_i\|` | heuristic_formalization | Validated absence registration inside accessible subspace `ℋ_M`. | E14 / VAR source | Does not assert absence outside the tested subspace. |
| F-EWF-000 | `AdmJoint(K_joint; A,B)=1 iff embeddings i_A:A->K_joint and i_B:B->K_joint preserve act, outcome, certification, order, validity, Conditions 1-6, and non-invalidation constraints` | definition / conjectural structure | Admissible joint K-side registration space for joint validity preservation. | `VVV-QMRF_Working_Paper_v2.0.md`; EWF testable-prediction lineage | Registration-layer joint-preservation test only; not a physical state space. |
| F-EWF-001 | `A ⊥_K B iff requires_K_joint(A,B)=1 AND no admissible K_joint preserves both A and B as jointly valid` | definition / conjectural relation | K-side incommensurability between registration structures. | `VVV-QMRF_Working_Paper_v2.0.md`; EWF testable-prediction lineage | Registration-layer relation only; not physical orthogonality and not event-level registration-null. |
| F-EWF-002 | `requires_K_joint(A,B)=1 iff A,B are valid in own K-side AND brought under D_joint AND D_joint requires joint assessment AND cannot be evaluated while A,B remain independent AND preserving D_joint requires a candidate K_joint` | definition / predicate | Shared-validity-demand predicate for EWF/LF configurations. | `VVV-QMRF_Working_Paper_v2.0.md` §4.3; EWF testable-prediction lineage | `requires_K_joint=0` does not guarantee K_joint exists. |
| F-EWF-003 | `Bridge_EWF(D_joint; M_F, M_W)=1 iff D_joint requires cross-observer validity AND M_F registers definite o_F AND M_W registers superposition of the same lab AND no admissible reinterpretation preserves both claims` | definition / bridge lemma | Bridge from `D_joint` to `M_W ⊥ M_F` in EWF/LF. | `VVV-QMRF_Working_Paper_v2.0.md` §4.5; Step 4 proof audit lineage | Class D proposed; application remains Class C. |
| F-EWF-004 | `ODC_K(Data, Cfg) = K_joint_exists iff ∃ J_K satisfying Conditions 1-6, AdmJoint(iv), reproducing observed probabilities within τ, and not reclassifying a Bridge_EWF config; = K_joint_fails iff Cfg satisfies requires_K_joint=1 AND Bridge_EWF=1 AND no such J_K fits` | definition / operational criterion | Operational data criterion for K_joint existence/failure. | `VVV-QMRF_Working_Paper_v2.0.md` §4.6; ODC_K lineage | Class C; τ must be predeclared; not a direct detector readout. |
| F-EWF-005 | `Null_K(e) or R_K(e)=⊥` | definition / event-level null | Event-level failure to enter valid K-side registration domain. | `VVV-QMRF_Working_Paper_v2.0.md` §4.4; `⊥_K` boundary clauses | Do not conflate with `⊥_K`; `⊥_K` is a relation, `Null_K(e)` is a single-event status. |

---

## 8. Concept Traceability / Truy vết concept

| Concept | Canonical name | Source | Role | Boundary |
|---|---|---|---|---|
| E1 | Self-certifying registration | `framework/vvv_qmrf_framework_e01_self_certifying_registration_postulate.md` | Blocks K-side regress by making primary registration self-certifying. | Not a consciousness claim and not `ρ`-side collapse. |
| E2 | Registration self-completion | `framework/vvv_qmrf_framework_e02_registration_self_completion_postulate.md` | Treats act/result completion as K-side registration structure. | Not physical identity in `ℋ`. |
| E3 | Registration lock | `framework/vvv_qmrf_framework_e03_registration_lock_postulate.md` | Defines `V-hat : I_boundary × D → K_R ∪ {k_null}` as the K-side lock from interaction boundary to registered/null tuple. | Not physical collapse, not P3, and not beta/K9_E. |
| E4 | Pre-symbolic registration stratum | `framework/vvv_qmrf_framework_e04_pre_symbolic_registration_stratum_postulate.md` | Defines raw registration before symbolic value. | Not mystical perception and not absence of physical interaction. |
| E5 | Internal representation encoding | `framework/vvv_qmrf_framework_e05_internal_representation_encoding_postulate.md` | Encodes registered outcome internally. | Not a second apparatus measurement. |
| E6 | Registering system as process | `framework/vvv_qmrf_framework_e06_registering_system_as_process_postulate.md` | Treats registering system as ordered events. | Not a fixed substantial observer. |
| E7 | Registration validity location | `framework/vvv_qmrf_framework_e07_registration_validity_location_postulate.md` | Places validity at K-side registration status. | Not absolute metaphysical truth. |
| E8 | Retroactive registration override | `framework/vvv_qmrf_framework_e08_retroactive_registration_override_postulate.md` | Reclassifies prior registration status when contradicted. | Does not alter physical history. |
| E14 | Validated absence registration | `category/vvv_qmrf_category_13_e14_validated_absence_registration.md`; E14 framework source | Makes controlled absence a positive registration category when validity conditions hold. | Not ordinary detector silence or failed measurement. |
| S1-Λ | Registration natural interface lemma | `synthesis/vvv_qmrf_synthesis_s1_lambda_registration_natural_interface_lemma.md` | Connects pre-symbolic event to symbolic registration. | Lemma/interface, not postulate unless future RCA upgrades it. |
| `⊥_K` | K-side incommensurability relation | `VVV-QMRF_Working_Paper_v2.0.md` §4.4 | Registration-layer relation between structures that cannot be jointly preserved as valid. | Not physical orthogonality; not event-level null. |
| `K_joint` | Admissible joint K-side registration space | `VVV-QMRF_Working_Paper_v2.0.md` §4.3 | Candidate joint space testing whether two K-side structures can be jointly valid. | Not a physical Hilbert space; not a private observer K-space. |
| `M′ ⊥ M` | E7 registered contradiction relation | `framework/vvv_qmrf_framework_e07_registration_validity_location_postulate.md` §3b | Later act contradiction triggering possible invalidation of prior act. | Not physical orthogonality; not denial that M occurred. |
| `D_joint` | Shared validity demand | `VVV-QMRF_Working_Paper_v2.0.md` §4.3 | Structurally required cross-observer validity assessment. | Not a physical postulate. |
| `requires_K_joint` | Joint K-side check predicate | `VVV-QMRF_Working_Paper_v2.0.md` §4.3 | Whether a joint K-side check is structurally demanded. | `=0` does not guarantee K_joint exists. |
| `Bridge_EWF` | Bridge lemma for EWF/LF | `VVV-QMRF_Working_Paper_v2.0.md` §4.5 | Links `D_joint` to `M_W ⊥ M_F`. | Class D proposed; Class C application. |
| `ODC_K` | Operational data criterion | `VVV-QMRF_Working_Paper_v2.0.md` §4.6 | Connects observed data to `K_joint_exists`/`K_joint_fails`. | Class C; requires predeclared τ. |

---

## 9. Relationship Rules / Quy tắc quan hệ

| Relation | Meaning | Required boundary |
|---|---|---|
| `ρ-side -> K-side input` | Physical outcome can enter registration update. | Physical probability remains governed by Standard QM. |
| `source_of` | A BE concept provides source lineage for a VVV-QMRF registration concept. | Source lineage is not identity. |
| `structural_analogy` | A BE relation and a QM/VVV-QMRF relation share a useful structure. | Analogy is not proof. |
| `derives_from` | A VVV-QMRF symbol follows from an active framework/category/synthesis document. | Show source trace and claim class. |
| `depends_on` | A formula requires previously defined symbols. | No formula may use an undefined symbol. |
| `contrast_with` | A valid category is separated from similar-looking non-cases. | Define the negative control, especially for null/absence registration. |

---

## 10. Failure Modes / Các cách hiểu lệch cần chặn

| Failure mode | Prevention |
|---|---|
| Reading `K` as `ρ`. | Always state `K` is registration state and `ρ` is physical quantum state. |
| Reading `𝒦` as `ℋ`. | Mark `𝒦` as Class C VVV-QMRF registration-state space, not Hilbert space. |
| Reading `U_K` as a new physical evolution law. | State that `U_K` updates registration status only. |
| Reading `σ(M)` or `R̂_svasa` as consciousness-caused collapse. | State that E1 is structural self-certification at K-side. |
| Reading `Π̂_absent^(ℋ_M)` as proof of absence everywhere. | Restrict it to measurement-accessible subspace `ℋ_M`. |
| Reading `detector response` as identical to `registration-state update`. | Use `detector response` only for apparatus physical response; use `registration-state update` for K-side update. |
| Reading BE-source terms as QM operators. | Keep them in BE-source lineage unless a VVV-QMRF source explicitly defines a derived operator. |

---

## 11. Update Rule / Quy tắc cập nhật

1. Add a new symbol only after it has meaning, domain, claim class, source trace, and boundary.
2. Add or update formulas only after every symbol in the formula appears in this registry.
3. If an active framework, category, synthesis, or meta-architecture document changes a symbol status, update this registry in the same change set.
4. If a source uses legacy terminology, preserve it only as trace and use the current normalized label.
5. If a formula looks stronger than its source evidence, downgrade the claim class before publication-facing reuse.
6. Course-level documents may simplify wording, but they must not weaken the claim boundary in this registry.

---

## 12. What This Registry Does NOT Claim / Những gì registry này KHÔNG tuyên bố

- It does not claim that VVV-QMRF replaces Standard Quantum Mechanics.
- It does not modify the Born rule, Schrödinger equation, Hamiltonian dynamics, or canonical QM state-update rules.
- It does not claim that Buddhist Epistemology proves Quantum Mechanics.
- It does not identify `detector response` with `registration-state update`.
- It does not treat derived VVV-QMRF notation as canonical QM notation.
- It does not treat BE-source terms as physical operators.
- It does not make Class C or Class D symbols peer-reviewed or experimentally validated.

---

## 13. Validation Checklist / Checklist kiểm chứng

| Check | Pass condition |
|---|---|
| Metadata | Author metadata exists and `document_type` is `index`. |
| Source corpus | Schema guide and active research sources are listed. |
| Claim types | Major claims are classified by type or class. |
| Symbol registry | Every retained symbol has meaning, domain, claim class, source trace, and boundary. |
| Formula registry | Every formula has formula class, domain of validity, source trace, and interpretation boundary. |
| K-side vs ρ-side | Registration-layer claims do not modify physical QM. |
| Terminology | `registration-state update` is used for K-side update; `detector response` is reserved for apparatus response. |
| BE boundary | BE-source labels are structural lineage, not QM identity claims. |
| Overclaim check | No claim says BE proves, solves, or replaces QM. |
| Update rule | New symbols and formulas must be added here before reuse. |
