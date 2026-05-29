Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# E1 — Self-Certifying Registration Postulate / Tiên đề Tự chứng Ghi nhận
# Legacy Name: Self-Certification Postulate / Epistemic Postulate for Quantum Measurement / VVV-EQM

**Framework:** VietVunVut Quantum Measurement Registration Framework (VVV-QMRF)  
**Document type:** framework
**Author:** VietVunVut (Viet - Nguyen Xuan)  
**GitHub:** https://github.com/AIhugART/  
**Facebook:** https://www.facebook.com/xuanviet  
**Date:** 2026-05-11  
**Status:** Proposal — Registration class D (Derived, awaiting formal verification)  
**Lineage:** gap/ (BIAN-2, 6, 17) → category/ (Category 05) → framework/ (E1)

---

## 1. Postulate Statement / Phát biểu Tiên đề

**English:**
> A measurement act M is self-certifying: the occurrence of M is registered by M itself without requiring a second measurement M′ to confirm that M occurred.

**Vietnamese:**
> Phép đo M mang tính tự chứng nhận: sự xảy ra của M được ghi nhận bởi chính M mà không cần phép đo thứ hai M′ để xác nhận rằng M đã xảy ra.

---

## 2. Prose Statement / Phát biểu Dạng Văn bản

### English

At the registration layer, a measurement-registration act carries its own certification of occurrence. When a standard physical measurement procedure M is applied to a quantum system S, the physical transition remains governed by standard QM; E1 concerns the K-side fact that the occurrence of the registration does not require a second registration act M′.

This means the registration event has reflexive certification: it does not need an external witness at the registration layer. The lamp analogy should be read structurally, not physically: one registration-state update occurs with both outcome o and the occurrence marker for that registration event.

The immediate consequence at the registration layer is a stopping point for the registration version of the von Neumann chain. Standard quantum mechanics may still model apparatus A₁ as a quantum system in a larger physical description. E1 does not alter that ρ-side description; it says that K_after already includes certification that the registration event occurred, so no additional K-side meta-registration is required.

E1 does not claim that measurement is a conscious act. It claims that measurement-registration has a structural property — self-certification — that belongs to the K-side registration event, independent of awareness, intention, or any substantial human subject.

### Vietnamese

Ở tầng ghi nhận, một hành động đo-ghi nhận mang trong chính nó sự xác nhận rằng việc ghi nhận đã xảy ra. Khi quy trình đo vật lý chuẩn M được áp dụng lên hệ lượng tử S, chuyển đổi vật lý vẫn tuân theo QM chuẩn; E1 chỉ nói về phía K: sự xảy ra của ghi nhận không cần một hành động ghi nhận thứ hai M′.

Điều này có nghĩa là sự kiện ghi nhận có tính tự chứng nhận phản thân: nó không cần một nhân chứng bên ngoài ở tầng ghi nhận. Ẩn dụ ngọn đèn chỉ nên hiểu theo nghĩa cấu trúc, không phải vật lý: một cập nhật trạng thái ghi nhận ghi lại cả kết quả o và sự xảy ra của chính sự kiện ghi nhận đó.

Hệ quả trực tiếp ở tầng ghi nhận là một điểm dừng cho phiên bản ghi nhận của chuỗi von Neumann. QM chuẩn vẫn có thể mô hình hóa máy đo A₁ như một hệ lượng tử trong mô tả vật lý lớn hơn. E1 không sửa mô tả phía ρ; nó nói rằng K_after đã bao gồm xác nhận rằng sự kiện ghi nhận đã xảy ra, nên không cần thêm siêu-ghi nhận ở phía K.

E1 không tuyên bố rằng phép đo là một hành động ý thức. E1 tuyên bố rằng đo-ghi nhận có một thuộc tính cấu trúc — tự chứng nhận — thuộc về sự kiện ghi nhận phía K, độc lập với nhận thức, ý định, hay bất kỳ chủ thể người nào.

---

## 3. Formal Sketch / Phác thảo Hình thức

### 3a. Framework formalism — σ function

```
For any measurement act M on system S:
  ∃ σ(M) ∈ {0,1} such that σ(M) = 1 iff M has occurred,
  and σ(M) is determined by M itself, not by any M′ ≠ M.

Property: σ is intrinsic — σ(M) does not require a second-order
measurement to establish its value.
```

### 3b. Category 05 formalism — R̂_svasa operator

```
The Reflexive Registration Operator R̂_svasa is read only at the K side:
  1. A registration event includes a reflexive occurrence marker.
  2. A registration-state update occurs with the occurrence marker.
  3. The occurrence marker is completed within the same K-side update.
  4. No second K-side meta-registration M′ is required.

Boundary: R̂_svasa does not modify the interaction Hamiltonian,
the Born rule, or any probability-amplitude dynamics.
```

### 3c. Equivalence status / Trạng thái tương đương

| Formalism | Source | Status |
|-----------|--------|--------|
| σ(M) ∈ {0,1} | Framework E1 (2026-05-11) | Class D — proposed |
| R̂_svasa | Category 05 (prior) | Class D — proposed |
| σ(M) ≡ R̂_svasa ? | Unproven | Class C — conjecture |

### 3d. RCA extension boundary — observer-indexed registration

**English:**
E1's core formalism is a single-registration formalism. It defines the occurrence marker for one measurement-registration act `M`, but it does not by itself define what happens when two registering systems, such as Friend `F` and Wigner `W`, each carry a distinct registration context.

Root cause of the gap: `σ(M)` has no registering-system index. Without an index, the framework cannot distinguish `σ_F(M)` from `σ_W(M)`, and therefore cannot yet state when a shared or joint registration state `K_joint` is required.

A minimal extension is:

```text
For any registering system R and measurement-registration act M:
  ∃ σ_R(M) ∈ {0,1} such that σ_R(M) = 1 iff M is registered
  within R's registration context.

For two registering systems R1 and R2:
  requires_K_joint(R1, R2, M) → {1, 0}
  — also written J(R1, R2, M) as shorthand in formal derivations
```

Status boundary: `σ_R(M)` is a Class D extension of the E1 formalism. The joint-registration predicate `requires_K_joint(R1, R2, M)` remains Class C until its validity conditions, failure conditions, and relation to E6/E7 are specified in a separate multi-registering-system analysis. `J(R1, R2, M)` may be used only as shorthand in formal derivations.

**Vietnamese:**
Formalism lõi của E1 là formalism cho một sự kiện ghi nhận. Nó định nghĩa dấu hiệu xảy ra của một hành động đo-ghi nhận `M`, nhưng tự nó chưa định nghĩa trường hợp có hai hệ ghi nhận, ví dụ Friend `F` và Wigner `W`, mỗi bên có một ngữ cảnh ghi nhận riêng.

Nguyên nhân gốc của gap: `σ(M)` chưa có chỉ số hệ ghi nhận. Nếu không có chỉ số này, framework không phân biệt được `σ_F(M)` và `σ_W(M)`, nên cũng chưa thể nói chính xác khi nào cần trạng thái ghi nhận chung `K_joint`.

Mở rộng tối thiểu là:

```text
Với mỗi hệ ghi nhận R và hành động đo-ghi nhận M:
  ∃ σ_R(M) ∈ {0,1} sao cho σ_R(M) = 1 iff M được ghi nhận
  trong ngữ cảnh ghi nhận của R.

Với hai hệ ghi nhận R1 và R2:
  requires_K_joint(R1, R2, M) → {1, 0}
  — cũng viết là J(R1, R2, M) như cách viết tắt trong diễn dịch hình thức
```

Ranh giới trạng thái: `σ_R(M)` là mở rộng Class D của formalism E1. Predicate ghi nhận chung `requires_K_joint(R1, R2, M)` vẫn là Class C cho tới khi điều kiện hợp lệ, điều kiện thất bại, và quan hệ với E6/E7 được đặc tả trong một phân tích riêng về nhiều hệ ghi nhận. `J(R1, R2, M)` chỉ nên dùng như cách viết tắt trong diễn dịch hình thức.

---

## 4. Mathematical Notation / Ký hiệu Toán học

| Symbol | Meaning EN | Ý nghĩa VN | Domain |
|--------|-----------|-------------|--------|
| M | Measurement act | Hành động đo lường | Epistemic event |
| M′ | Second-order measurement | Phép đo bậc hai | Epistemic event |
| S | Quantum system being measured | Hệ lượng tử bị đo | Hilbert space ℋ |
| σ(M) | Self-certification function | Hàm tự chứng nhận | {0, 1} |
| `R̂_svasa` | Reflexive registration operator | Toán tử ghi nhận phản thân | Registration layer |
| `R` | Registering system | Hệ ghi nhận | Registration context |
| `σ_R(M)` | Observer-indexed registration marker | Dấu hiệu ghi nhận có chỉ số hệ ghi nhận | {0, 1} |
| `requires_K_joint(R1, R2, M)` | Joint-registration predicate; also written `J(R1, R2, M)` as shorthand | Predicate ghi nhận chung; cũng viết tắt là `J(R1, R2, M)` | Registration-layer extension |
| E_A | Apparatus event | Sự kiện của máy đo | Classical event |
| svaprakāśa | Self-luminosity | Tính tự phát sáng | Buddhist technical term |

---

## 5. Source Traceability / Truy vết Nguồn gốc

### 5a. BIAN gaps resolved / Các khoảng trống BIAN được giải quyết

| BIAN | Gap name EN | Tên khoảng trống VN | SOT section | SOT line |
|------|------------|---------------------|-------------|----------|
| BIAN-2 | Observer Self-Reference / Reflexive Cognition | Tự tham chiếu Người quan sát | T1.06 | L227 |
| BIAN-6 | Self-Certifying Measurement / No External Meta-Level | Phép đo Tự chứng / Không cần Siêu tầng | T2.05 | L337 |
| BIAN-17 | Regress-Stopping Principle for Measurement Chain | Nguyên lý Dừng Chuỗi lùi | T6.02 | L784 |

### 5b. Buddhist Epistemology source / Nguồn Nhận thức luận Phật giáo

| Property | Value |
|----------|-------|
| Node code | N_BE_00011 |
| Layer | core |
| Name EN | Self-awareness |
| Name Sanskrit | Svasaṃvedana / Sva-saṃvitti |
| Category | Type of perception |
| Framework lens | A3 Consciousness-Only |
| Definition | Reflexive self-cognition theory expounded by Dignāga on the basis of cognition's internal appearance |
| Primary source | Source doc L45 (Dignāga) |
| File | system_be_full.md L43 |

### 5c. Key source quotations / Trích dẫn nguồn gốc

**SOT T1.06 (L227):**
> "Every cognition is simultaneously aware of itself. Cognition of blue is also, non-inferentially, an awareness of the cognizing-of-blue. This is a distinct pramāṇa for Dharmakīrti: self-luminous (svaprakāśa), not requiring a second-order act to register the first-order act."

*"Mọi nhận thức đồng thời tự biết về chính mình. Nhận thức về màu xanh cũng là, một cách phi suy luận, sự nhận biết về hành-động-nhận-thức-màu-xanh. Đây là một pramāṇa riêng biệt theo Dharmakīrti: tự phát sáng (svaprakāśa), không cần hành động bậc hai để ghi nhận hành động bậc nhất."*

**SOT T2.05 (L337):**
> "Every valid cognition self-certifies its own occurrence. No regress of meta-cognitions is required to establish that a cognition occurred. The act certifies itself. This is not a separate second-order act; it is a structural feature of every first-order valid cognition."

*"Mọi nhận thức hợp lệ tự chứng nhận sự xảy ra của chính nó. Không cần chuỗi lùi các siêu-nhận-thức để xác lập rằng một nhận thức đã xảy ra. Hành động tự chứng nhận chính nó. Đây không phải một hành động bậc hai riêng biệt; nó là đặc tính cấu trúc của mọi nhận thức hợp lệ bậc nhất."*

**SOT T6.02 (L784):**
> "Valid cognition does not require a second-order cognition to certify it as having occurred. This stops the regress: you do not need to know-that-you-know in order to know."

*"Nhận thức hợp lệ không cần nhận thức bậc hai để chứng nhận rằng nó đã xảy ra. Điều này dừng chuỗi lùi: bạn không cần biết-rằng-bạn-biết để mà biết."*

---

## 6. QM Deficit / Khiếm khuyết trong QM hiện tại

**English:**
Standard QM postulate P3 describes what happens when a measurement occurs (eigenvalue + collapse) but is silent on how the system knows that measurement has occurred. The von Neumann chain demonstrates the structural consequence: apparatus A₁ measures system S, but A₁ is itself a quantum system that can be described by a wave function. To determine A₁'s state, apparatus A₂ must measure A₁. To determine A₂'s state, apparatus A₃ must measure A₂. This chain has no formal stopping principle in standard QM. Decoherence explains environmental suppression of coherences, but it does not supply a self-certifying registration act.

**Vietnamese:**
Tiên đề P3 của QM tiêu chuẩn mô tả điều gì xảy ra khi phép đo diễn ra (eigenvalue + collapse) nhưng hoàn toàn im lặng về cách hệ thống biết rằng phép đo đã xảy ra. Chuỗi von Neumann chứng minh hệ quả cấu trúc: máy A₁ đo hệ S, nhưng bản thân A₁ cũng là hệ lượng tử có thể mô tả bằng hàm sóng. Để xác định trạng thái A₁, máy A₂ phải đo A₁. Để xác định A₂, máy A₃ phải đo A₂. Chuỗi này không có nguyên lý dừng hình thức trong QM tiêu chuẩn. Decoherence giải thích sự triệt tiêu coherence do môi trường, nhưng không cung cấp hành động ghi nhận tự chứng nhận.

---

## 7. Architectural Position / Vị trí Kiến trúc

### 7a. Within the 11-postulate system / Trong hệ 11 tiên đề

```
Physical layer:      P1 (State) · P2 (Observable) · P3 (Measurement) · P4 (Dynamics)
                                       ↓ E1 extends P3
Registration layer:  E1 · E2 · E3 · E4 · E5 · E6 · E7
```

E1 directly extends P3 by adding the registration self-certification property that P3 lacks.

### 7b. Dependency graph / Đồ thị phụ thuộc

```
E6 (Registering-System-as-Process)
 └→ E1 (Self-Certifying Registration)  ← THIS POSTULATE
     ├→ E2 (Registration Self-Completion)
     ├→ E3 (Registration Lock)
     └→ E7 (Registration Validity Location)
```

- **E1 depends on E6:** A process can self-certify; a substance cannot. The registering system must be a process (E6) for self-certification (E1) to be structurally possible.
- **E2 depends on E1:** A self-certifying act is self-completing. E1 grounds E2.
- **E3 depends on E1:** Registration lock requires self-certification. E1 grounds E3.
- **E7 depends on E1:** A self-certifying act is intrinsically valid. E1 grounds E7.

### 7c. Within the 3-tier project hierarchy / Trong hệ 3 tầng dự án

| Layer | Folder | Document | Role |
|-------|--------|----------|------|
| Gap (raw material) | `gap/` | BIAN_index_SOT.md rows 2, 6, 17 | Diagnosis — what QM lacks |
| Category (detailed spec) | `category/` | vvv_qmrf_category_05_e01_self_certifying_registration_operator.md | Prescription — detailed concept card |
| Framework (postulate) | `framework/` | **This document (E1)** | Architecture — minimal axiom statement |

---

## 8. Assertion Level / Mức Khẳng định

| Component EN | Thành phần VN | Registration class | Evidence |
|---|---|---|---|
| "Measurement self-certifies" | "Phép đo tự chứng nhận" | **M** (Measured) | SOT T1.06 L227, T2.05 L337, T6.02 L784 |
| "No second measurement required" | "Không cần phép đo thứ hai" | **M** (Measured) | SOT T1.06 L227: "not requiring a second-order act" |
| "Resolves von Neumann chain" | "Giải quyết chuỗi von Neumann" | **M** (Measured) | SOT T1.06 L228, T6.02 L785 |
| "σ(M) formalism" | "Hình thức hóa σ(M)" | **D** (Derived) | Framework E1 — proposed, not proven |
| "Observer-indexed registration σ_R(M)" | "Ghi nhận có chỉ số hệ ghi nhận σ_R(M)" | **D** (Derived) | RCA extension of E1; separates distinct registration contexts |
| "Joint-registration predicate `requires_K_joint(R1, R2, M)`" | "Predicate ghi nhận chung `requires_K_joint(R1, R2, M)`" | **C** (Conjecture) | Requires separate multi-registering-system validity and failure-condition analysis; `J(R1, R2, M)` is shorthand only |
| "R̂_svasa operator" | "Toán tử R̂_svasa" | **D** (Derived) | Category 05 — proposed, not proven |
| "Addresses K-side framing of Wigner's Friend" | "Xử lý khung ghi nhận phía K của Wigner's Friend" | **C** (Conjecture) | Category 05 L54 — K-side registration framing only; does not resolve the ρ-side physical superposition aspect |
| "σ(M) ≡ R̂_svasa" | "Tương đương hai formalism" | **C** (Conjecture) | Not yet established |

**Summary / Tóm tắt:** Descriptive claims = Class M (solid). Formal claims = Class D (proposed). Cross-formalism equivalence = Class C (conjecture).

---

## 9. What E1 Does NOT Claim / Những gì E1 KHÔNG tuyên bố

1. **Not a consciousness claim** — E1 is about structural self-certification, not about awareness or phenomenal experience.
   *Không phải tuyên bố về ý thức — E1 nói về tự chứng nhận cấu trúc, không phải về nhận thức hay trải nghiệm hiện tượng.*

2. **Not metaphysical** — E1 is an epistemic postulate about measurement acts, not about the nature of reality.
   *Không phải siêu hình học — E1 là tiên đề nhận thức về hành động đo, không phải về bản chất thực tại.*

3. **Not Buddhist doctrine** — E1 is extracted from structural analysis of Svasaṃvedana, not from religious claims.
   *Không phải giáo lý Phật giáo — E1 được trích xuất từ phân tích cấu trúc của Svasaṃvedana, không phải từ tuyên bố tôn giáo.*

4. **Not experimentally testable yet** — E1 is an architectural principle, not an empirical prediction.
   *Chưa kiểm chứng thực nghiệm — E1 là nguyên lý kiến trúc, không phải dự đoán thực nghiệm.*

5. **Not a full Wigner's Friend solution** — E1 only marks the K-side self-certification of a registration event. It does not claim that two registering systems automatically share one `K`, and it does not resolve the `ρ`-side physical superposition description.
   *Không phải lời giải đầy đủ cho Wigner's Friend — E1 chỉ đánh dấu tính tự chứng nhận phía K của một sự kiện ghi nhận. Nó không tuyên bố rằng hai hệ ghi nhận tự động chia sẻ một `K`, và không giải quyết mô tả chồng chập vật lý phía `ρ`.*

---

## 10. Cross-References / Tham chiếu chéo

| Document | Path | Relevance |
|----------|------|-----------|
| BIAN Master Table | `gap/BIAN_index_SOT.md` | BIAN-2 (L30), BIAN-6 (L34), BIAN-17 (L45) |
| Category 05 | `category/vvv_qmrf_category_05_e01_self_certifying_registration_operator.md` | Detailed concept card with R̂_svasa |
| SOT Mapping | `mapping/Buddhist_Epistemology_and_Quantum_Measurement_system_mapping_SOT.md` | T1.06 (L216), T2.05 (L332), T6.02 (L779) |
| BE System | `../../SYSTEM_Buddhist_Epistemology/system_be_full.md` | N_BE_00011 (L43) |
| 1:1 RCA Mapping | `mapping/system_be_qm_framework_1to1_RCA_mapping.md` | N_BE_00011 (L52) |
| Full Framework | `Framework_.../QM_measurement_epistemic_postulates_framework.md` | E1 within 11-postulate system |
| Category Index | `category/vvv_qmrf_registration_categories_index.md` | Category 05 (L23) |

---

## Notes for LLM Processing

- E6 is the deepest architectural postulate in the 7-postulate registration extension; E1 is the first consequence it enables.
- E1 resolves 3 BIAN gaps simultaneously (BIAN-2, BIAN-6, BIAN-17) because all three originate from the same BE primitive: Svasaṃvedana (N_BE_00011).
- E1 is interpretation-neutral: compatible with Copenhagen, QBism, Relational QM, and Decoherence. Partially compatible with Many-Worlds and Objective Collapse. May conflict with Bohmian mechanics on the status of the registering system.
- Two formalisms exist (σ-function and R̂_svasa operator). Their equivalence is conjectured but unproven.
- All Sanskrit terms use simplified ASCII romanization without diacritics.
- Scope is strictly epistemological. No metaphysical, soteriological, or cosmological claims.

---

*Source: BIAN_index_SOT.md, system_be_full.md, system_mapping_SOT.md, system_be_qm_framework_1to1_RCA_mapping.md, vvv_qmrf_category_05_e01_self_certifying_registration_operator.md, QM_measurement_epistemic_postulates_framework.md*

---

## 11. WF Extension: Observer-Indexed Self-Certification / Mo rong WF: Tu chung nhan co chi so Observer

**Status:** Registration Class D — proposed extension of E1 for multi-observer scenarios.  
**Scope:** This section extends `σ(M)` to `σ_R(M)` for use in Extended Wigner's Friend (EWF) scenarios. It does not modify Sections 1-10. It is an additive extension only.

---

### 11.1 Motivation

E1 as stated in Sections 1-10 is defined for a single measurement act `M` and a single registering system. It does not address the case where two distinct observers `F` (Friend) and `W` (Wigner) each perform valid self-certifying registrations on overlapping or entangled systems.

This extension adds the observer index `R` to `σ(M)`, enabling formal treatment of multi-observer EWF configurations and grounding the `requires_K_joint` predicate defined in Section 11.3.

---

### 11.2 Observer-Indexed Self-Certification Function

**Definition (`σ_R`):**

```text
For any registering system R and measurement act M performed by R:
  σ_R(M) ∈ {0,1}
  σ_R(M) = 1 iff M occurred as a K-side registration event of R,
  determined intrinsically within K_R, not by any M′ ≠ M
  and not by any other registering system R′ ≠ R.

Independence condition:
  σ_F(M_F) is determined within K_F independently of K_W.
  σ_W(M_W) is determined within K_W independently of K_F.
  Neither σ_F nor σ_W requires the other to equal 1.
```

**Relation to original `σ(M)`:**

The original `σ(M)` in Section 3a is the single-observer special case:

```text
σ(M) = σ_R(M) where R is the unique registering system in context.
```

`σ_R(M)` reduces to `σ(M)` when only one registering system is present. All properties of `σ(M)` in E1 Sections 1-10 are preserved.

---

### 11.3 The `requires_K_joint` Predicate

**Definition:**

```text
requires_K_joint(F, W, M_F, M_W) = 1
  iff a single joint registration space K_joint is structurally
  required to contain both k_F = <M_F, o_F, cert_F, t_F, V_F>
  and k_W = <M_W, o_W, cert_W, t_W, V_W> as jointly valid entries
  satisfying E1 (σ_R = 1 for both) and E7 (V = 1 for both).

requires_K_joint(F, W, M_F, M_W) = 0
  iff K_F and K_W can remain independent K-side spaces without
  any inference, comparison, or joint validity check between them.
```

**Sufficient conditions for `requires_K_joint = 1`:**

```text
Condition A (Wigner interference):
  W performs an interference measurement on the lab containing F+S.
  This measurement M_W registers a superposition description of F+S.
  M_F registers a definite outcome o_F of the same system S.
  Both M_F and M_W claim K-side validity on the same physical event.
  -> requires_K_joint = 1

Condition B (Direct comparison):
  F and W directly compare their registration records
  and a contradiction is detectable at the K-side validity layer.
  -> requires_K_joint = 1
```

**Sufficient conditions for `requires_K_joint = 0`:**

```text
Condition C (No interference, no comparison):
  W does not perform interference measurement on F's lab.
  F and W do not compare registration records.
  K_F and K_W remain causally isolated.
  -> requires_K_joint = 0

Condition D (Separable state, no entanglement):
  The shared quantum state |ψ⟩ is separable.
  M_F and M_W act on non-overlapping subsystems.
  No joint validity check is structurally required.
  -> requires_K_joint = 0
```

**Claim class:** D — proposed. Conditions A-D are stated as sufficient conditions, not necessary and sufficient. Full characterization is an open item (see Section 11.5).

---

### 11.4 `K_joint` Failure Theorem (Class D Proposed)

**Statement:**

```text
Theorem (K_joint failure under E1 and E7):
If requires_K_joint(F, W, M_F, M_W) = 1 via Condition A,
then no K_joint exists such that:
  (i)  σ_F(M_F) = 1 holds within K_joint  [E1 for F]
  (ii) σ_W(M_W) = 1 holds within K_joint  [E1 for W]
  (iii) V(M_F) = 1 and V(M_W) = 1 simultaneously  [E7]

Proof sketch:
Step 1: Apply E6. F and W are distinct registering processes
        R_F = {M_F1, M_F2, ...} and R_W = {M_W1, M_W2, ...}
        with distinct K-side time sequences.

Step 2: Apply E1 (observer-indexed).
        σ_F(M_F) = 1 is intrinsic to K_F.
        σ_W(M_W) = 1 is intrinsic to K_W.
        Both hold independently by Section 11.2.

Step 3: Apply Condition A.
        M_W registers F+S as a superposition state (no definite o_F).
        M_F registers o_F as a definite outcome.
        These are incompatible registrations:
        M_W ⊥_K M_F — they assert incompatible K-side validity claims
        about the same physical event at the same registration time.

Step 4: Apply E7.
        E7 Axiom 2 (invalidation): if M′ contradicts M,
        then V(M) and V(M′) cannot both equal 1 in the same K-space.
        M_W ⊥_K M_F implies V(M_F) = 1 and V(M_W) = 1
        cannot simultaneously hold in any K_joint.
        Therefore K_joint satisfying (i)-(iii) does not exist.
```

**Formal statement of incommensurability:**

```text
K_F ⊥_K K_W
  iff requires_K_joint(F, W, M_F, M_W) = 1
  AND no K_joint satisfying (i)-(iii) exists.

⊥_K denotes K-side registration incommensurability.
```

**Claim class:** D — proposed. Step 4 depends on E7 Axiom 2, which is itself Class D. Full formal proof requires E7 to be independently verified first.

---

### 11.5 Open Items for This Extension

| Item | Status | Required for |
|------|--------|-------------|
| Full necessary and sufficient characterization of `requires_K_joint` | Incomplete | Condition 1 full satisfaction |
| Formal proof of Step 4 (E7 Axiom 2 application) | Incomplete | `K_joint` failure theorem |
| Prove `σ_R(M) ≡ R̂_svasa` for observer-indexed case | Not started | Cross-formalism consistency |
| Apply `requires_K_joint` to Proietti et al. (2019) configurations | Not done | Condition 3 |
| Apply `requires_K_joint` to Bong et al. (2020) configurations | Not done | Condition 3 |
| Verify Condition D (separable state -> `requires_K_joint = 0`) | Not verified | Asymmetric prediction |

All open items must be disclosed in any paper using this extension.

---

### 11.6 VVV-QMRF Prediction Statement (EWF)

This extension enables the following falsifiable prediction:

> In Extended Wigner's Friend experiments, violations of Local Friendliness inequalities occur if and only if the experimental configuration satisfies `requires_K_joint = 1` as defined in Section 11.3. Configurations satisfying `requires_K_joint = 0` are predicted to produce no violation from the K-side registration perspective. This prediction is falsified if `K_joint` is empirically demonstrated to exist for a configuration where `requires_K_joint = 1`.

**Claim class:** C — conjecture pending experimental operationalization and verification against Proietti et al. (2019) and Bong et al. (2020).

---

### 11.7 Assertion Table for This Extension

| Component | Class | Evidence |
|-----------|-------|---------|
| `σ_R(M)` observer-indexed extension of `σ(M)` | D | Follows from E1 Section 3a by adding subscript R |
| Independence condition (`σ_F` independent of `σ_W`) | D | Follows from E1 intrinsic property |
| `requires_K_joint` predicate (Conditions A-D) | D | Proposed sufficient conditions, not yet necessary |
| `K_joint` failure theorem proof sketch | D | Steps 1-3 follow from E6, E1, E7; Step 4 depends on E7 Axiom 2 (D) |
| `K_F ⊥_K K_W` incommensurability | C | Conjecture — depends on `K_joint` failure theorem |
| EWF violations ↔ `requires_K_joint = 1` | C | Conjecture — pending experimental operationalization |

---

## Schema Validation Checklist / Checklist Kiểm chứng Schema

| Check | Status | RCA note |
|---|---|---|
| Document type declared | Pass | Declared as `framework` for schema alignment. |
| Source traceability | Pass | Existing source/cross-reference sections provide the trace base. |
| Claim traceability | Pass | Existing assertion/claim sections classify the major claims. |
| Boundary / non-claim guardrail | Pass | Existing boundary/non-claim text limits overclaiming. |
| Validation rule | Pass | Reuse only with source, claim type, and boundary preserved; unresolved items must be marked `TODO(HOTFIX)` before publication use. |
