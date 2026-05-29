Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# E14 — Validated Absence Registration Postulate / Tiên đề Ghi nhận Vắng mặt Hợp lệ
# Legacy Name: Epistemic Absence Cognition Postulate / Tiên đề Nhận thức Vắng mặt / VVV-EQM

**Framework:** VietVunVut Quantum Measurement Registration Framework (VVV-QMRF)  
**Document type:** framework
**Author:** VietVunVut (Viet - Nguyen Xuan)  
**GitHub:** https://github.com/AIhugART/  
**Facebook:** https://www.facebook.com/xuanviet  
**Date:** 2026-05-12  
**Status:** Proposal — Registration class D  
**Lineage:** gap/ (BIAN-9) → category/ (Category 13) → framework/ (E14)

---

## 1. Postulate Statement

**English:**
> The null result of a quantum measurement — when the measurement setup satisfies E10's Trairūpya conditions — constitutes a distinct, formally valid registration act: the positive registration of the *absence* of the measured property. This act (Validated Absence Registration, VAR) is registration-equivalent in authority to a positive detection event within the valid measurement context. It is categorically distinct from measurement failure (E8 domain) and from Null Registering-System Event / Registration Non-Engagement (E9 domain).

**Vietnamese:**
> Kết quả rỗng của phép đo lượng tử — khi thiết lập đo thỏa điều kiện Trairūpya của E10 — tạo thành một hành vi ghi nhận riêng biệt, chính thức hợp lệ: ghi nhận dương tính về *sự vắng mặt* của thuộc tính đo. Hành vi này (VAR) có thẩm quyền ghi nhận tương đương với sự kiện phát hiện dương tính trong bối cảnh đo hợp lệ. Khác biệt hoàn toàn với lỗi đo (E8) và Sự kiện Hệ ghi nhận Rỗng / Trạng thái Bất tạo Ghi nhận (E9).

---

## 2. Prose Statement

QM handles null results implicitly: they appear as residual probability (1 − Σ P(λᵢ)). There is no formal category treating "no detection" as a first-class registration act. *Anupalabdhi* (Non-perception) in Buddhist Epistemology establishes this: under the right conditions, NOT perceiving an object that WOULD be perceived if present is a valid means of registration, using pramāṇa as its source analogue, for establishing absence.

E14 maps this directly. When E10's three conditions hold (the detector is properly coupled, calibrated, and dark-count-free), a null result is not a failure — it is a positive registration of the property's absence within the measurement-accessible subspace. The Absence Projector $\hat{\Pi}_{absent}^{(\mathcal{H}_M)}$ yields a definite post-measurement state that encodes positive absence registration only inside that valid test domain.

Key distinction from E9 and E11:
- **E9**: Physical interaction occurred, no valid K-side registration encoding (non-informative registration non-engagement)
- **E11**: No physical interaction, positive registration via contrapositive (IFSI — interaction-free)
- **E14**: Physical interaction offered, valid null result = positive registration of *absence* (Anupalabdhi)

---

## 3. Formal Sketch

```
Absence Projector (within measurement-accessible subspace ℋ_M):
  Π̂_absent^(ℋ_M) = I_ℋ_M − Σᵢ |λᵢ⟩⟨λᵢ|, with |λᵢ⟩ ∈ ℋ_M

Subspace condition:
  Π̂_absent^(ℋ_M) registers absence only inside ℋ_M, not outside the valid test domain.

Null measurement event (under E10 conditions):
  Pre-state:   |ψ⟩ (arbitrary superposition)
  Null click:  Π̂_absent^(ℋ_M) triggers
  Post-state:  ρ → Π̂_absent^(ℋ_M) ρ Π̂_absent^(ℋ_M) / Tr(Π̂_absent^(ℋ_M) ρ)

Registration content:
  "System does NOT have any tested property in {λ₁, λ₂, ...λₙ} within ℋ_M"
  This IS positive absence registration — not "we don't know"

Boundary:
  Π̂_absent^(ℋ_M) is used here as registration-authority notation inside the tested subspace, not as a new physical postulate replacing Standard QM projection rules.

Anupalabdhi conditions check:
  1. Object perceivable IF present:  E10 C2 (Sapakṣasattva) ✅
  2. Object not perceived:           null click ✅
  3. Therefore absent:               valid registration ✅
```

---

## 4. Three-way Distinction (E8 / E9 / E14)

| Scenario | Physical interaction | Registration output | Domain |
|----------|:-------------------:|:-------------------:|--------|
| Bhrānti (false positive) | NO | YES (error) | E8 override |
| NRE | YES | NONE (no valid K-side output) | E9 |
| IFSI | NO | YES (contrapositive) | E11 |
| **EAC (null = absence)** | **YES** | **YES (absence)** | **E14** |
| Standard PVM | YES | YES (presence) | PVM |

---

## 5. Architectural Position

```
E10 (Validity gate) — conditions for valid registration
 ├→ E14 (EAC) ← THIS POSTULATE: valid null output as positive absence registration
 ├→ E9  (NRE) — contrast case: interaction without valid K-side output
 └→ E11 (IFSI) — contrast case: no target interaction, positive registration via contrapositive
```

| Layer | Document | Role |
|-------|----------|------|
| Gap | BIAN-9 (SOT L38, N_BE_00253) | Diagnosis |
| Category | vvv_qmrf_category_13_e14_validated_absence_registration.md (Category 13) | Prescription |
| Framework | **This document (E14)** | Architecture |

---

## 6. Assertion Level

| Component | Class |
|---|---|
| "Anupalabdhi is valid pramāṇa" | **M** (Buddhist logic) |
| "Null result under E10 = positive absence registration" | **D** |
| "Π̂_absent^(ℋ_M) operator definition" | **D** |
| "EAC ≠ NRE ≠ IFSI" | **M** (structural analysis) |

---

*Source: category/vvv_qmrf_category_13_e14_validated_absence_registration.md, framework/vvv_qmrf_framework_e10_tripartite_registration_validity_matrix_postulate.md, framework/vvv_qmrf_framework_e09_null_registering_system_event_postulate.md, BIAN_index_SOT.md*

---

## Schema Validation Checklist / Checklist Kiểm chứng Schema

| Check | Status | RCA note |
|---|---|---|
| Document type declared | Pass | Declared as `framework` for schema alignment. |
| Source traceability | Pass | Existing source/cross-reference sections provide the trace base. |
| Claim traceability | Pass | Existing assertion/claim sections classify the major claims. |
| Boundary / non-claim guardrail | Review required | Add explicit non-identity and non-physical-law boundaries before reuse. |
| Validation rule | Pass | Reuse only with source, claim type, and boundary preserved; unresolved items must be marked `TODO(HOTFIX)` before publication use. |
