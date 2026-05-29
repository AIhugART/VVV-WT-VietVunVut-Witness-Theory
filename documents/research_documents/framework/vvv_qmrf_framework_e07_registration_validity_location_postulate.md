Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# E7 — Registration Validity Location Postulate / Tiên đề Định vị Tính hợp lệ Ghi nhận
# Legacy Name: Epistemic Validity Location Postulate / Tiên đề Định vị Tính hợp lệ Nhận thức / VVV-EQM

**Framework:** VietVunVut Quantum Measurement Registration Framework (VVV-QMRF)  
**Document type:** framework
**Author:** VietVunVut (Viet - Nguyen Xuan)  
**GitHub:** https://github.com/AIhugART/  
**Date:** 2026-05-11  
**Status:** Proposal — Registration class D  
**Lineage:** gap/ (BIAN-18) → category/ (Category 04) → framework/ (E7)

---

## 1. Postulate Statement / Phát biểu Tiên đề

**English:**
> The validity of a measurement is intrinsic to the measurement act itself. A measurement does not require subsequent verification to count as valid. Invalidity, when it occurs, is detected extrinsically by a subsequent measurement.

**Vietnamese:**
> Tính hợp lệ của phép đo là nội tại đối với chính hành động đo. Phép đo không cần kiểm chứng sau đó để được coi là hợp lệ. Tính không hợp lệ, khi xảy ra, được phát hiện ngoại tại bởi phép đo tiếp theo.

---

## 2. Prose Statement / Phát biểu Dạng Văn bản

### English

QM has no formal account of measurement validity. In experimental practice, physicists always use extrinsic verification: calibration runs, repetition, cross-checks, statistical analysis. But none of this is integrated into the formalism. Whether a single unrepeated measurement is "valid" is undefined in QM.

E7 introduces an asymmetric validity principle:
- **Validity is default (intrinsic):** A measurement is valid by virtue of having occurred — its causal efficacy (arthakriyasakti) on the detector establishes provisional validity.
- **Invalidity is diagnosed (extrinsic):** Only a subsequent contradicting measurement (badhaka pramana) can retroactively invalidate a prior result.

This derives from the Svatah/Paratah pramanya debate in Buddhist meta-epistemology, specifically Dharmakirti's synthetic position: initial validity is intrinsic (via svasaṃvedana and arthakriyasakti); invalidity is detected extrinsically (via badhaka pramana).

The key insight is the **asymmetry**: validity and invalidity have different registration structures. Validity does not require an external certifier. Invalidity does. This matches experimental practice and provides the formal ground for why single-shot measurements are meaningful (e.g., BB84 in quantum cryptography).

E7 pairs with the Retroactive Registration Override mechanism (bādhaka) to form a complete validity-invalidation architecture: E7 establishes where validity lives; the override mechanism provides the mechanism for when validity fails.

### Vietnamese

QM không có mô tả hình thức về tính hợp lệ của phép đo. Trong thực nghiệm, nhà vật lý luôn dùng kiểm chứng ngoại tại: hiệu chuẩn, lặp lại, kiểm tra chéo, phân tích thống kê. Nhưng không gì trong số này được tích hợp vào hệ hình thức. Phép đo đơn không lặp có "hợp lệ" không? QM không định nghĩa.

E7 đưa ra nguyên lý hợp lệ bất đối xứng:
- **Hợp lệ là mặc định (nội tại):** Phép đo hợp lệ vì đã xảy ra — tác dụng nhân quả (arthakriyasakti) lên detector thiết lập tính hợp lệ tạm thời.
- **Không hợp lệ là chẩn đoán (ngoại tại):** Chỉ phép đo tiếp theo mâu thuẫn (badhaka pramana) mới có thể hồi tố phủ nhận kết quả trước.

Bắt nguồn từ tranh luận Svatah/Paratah pramanya, đặc biệt vị trí tổng hợp của Dharmakirti: hợp lệ ban đầu là nội tại; không hợp lệ được phát hiện ngoại tại.

Ý tưởng then chốt: **bất đối xứng** — hợp lệ và không hợp lệ có cấu trúc nhận thức khác nhau. Hợp lệ không cần chứng nhận ngoại tại. Không hợp lệ thì cần.

---

## 3. Formal Sketch / Phác thảo Hình thức

### 3a. Framework formalism — Asymmetric validity

```
For measurement M yielding result r:
  Default: M is valid (svataḥ)
  
  Invalidity detection:
    ∃ subsequent measurement M′ such that M′ contradicts M
    → M is retroactively marked invalid (bādhaka)
    
  Asymmetry: validity does not require M′.
             Invalidity requires M′.
```

### 3b. Framework formalism — Registered contradiction relation

The phrase "M′ contradicts M" is a K-side validity relation, not physical orthogonality and not ordinary disagreement. It requires a later registration act with enough registration authority to challenge the prior act inside a shared comparison context.

```
M′ ⊥ M
  iff  M′ is a later K-side registration act relative to M
  AND  M′ and M are brought into the same admissible K-side comparison context
  AND  M′ and M concern the same registration target, history, or validity claim
  AND  their registered contents cannot both satisfy the relevant validity
       conditions in that comparison context
  AND  M′ itself satisfies the applicable registration-validity conditions.

Invalidation rule:
  V(M)=1 by default.
  If M′ ⊥ M and M′ has valid registration authority in the comparison context,
  then V(M) may be revised to 0.
```

Boundary: `M′ ⊥ M` does not mean that M did not physically occur, does not make M false inside its original K-side before comparison, and does not apply to merely different perspectives that are not forced into a shared K-side comparison context.

### 3c. Category 04 formalism — DPEC (Dual-Phase Registration Certification)

```
Phase 1 — Intrinsic Validity (Svataḥ):
  Physical interaction → Conditionally Updated State ρ̃
  Provisional validity via arthakriyāśakti (causal efficacy)

Phase 2 — Extrinsic Certification (Parataḥ):
  Ĉ_ext acts on ρ̃:
    If consensus: ρ̃ → ρ_certified (registration-valid)
    If contradiction: invoke REO (Retroactive Registration Override)
```

### 3d. Equivalence status

| Formalism | Source | Status |
|-----------|--------|--------|
| Asymmetric validity rule | Framework E7 | Class D |
| DPEC (ρ̃ → ρ_certified) | Category 04 | Class D |
| Equivalence? | Unproven | Class C |

### 3e. Relationship to Category 01 (REO)

```
E7 (Validity Location)
 │
 ├─ Default valid → single-shot meaningful
 │
 └─ If bādhaka detected:
      → Category 01 (Retroactive Override) executes invalidation
```

### 3f. K1-K8 Source-Chain Anchor (RCA 2026-05-29)

> Closes the BE-SOT → E7 → K-axiom chain bidirectionally. `K_Space_Axiomatization.md` viện dẫn "E7 Axiom 1 / Axioms 2-3 / E7 Axiom 2 / E7 (V_prov/V_final)" cho K4/K5/K6/K7; mục này xác nhận chiều ngược lại từ phía E7.

**Formal axiom labels** (three implicit rules in §3a–§3b, now named for K-Space traceability):

| Label | E7 content | K-Space "Source" reference |
|---|---|---|
| **E7-Ax1** | §3a "Default: M is valid (svataḥ)" — intrinsic default validity | K4 Source: "E7 Axiom 1 (Default validity)" |
| **E7-Ax2** | §3a "Invalidity detection: ∃M' contradicts M → bādhaka" + §3b M'⊥M conditions + authority | K5 Source: "E7 Axioms 2-3 (Invalidation + Asymmetry)"; K6 Source: "E7 Axiom 2 + §4.4" |
| **E7-Ax3** | §3a "Asymmetry: validity ≠ M', invalidity = M'" — irreversibility / V_prov vs V_final | K5 Source: "E7 Axioms 2-3"; K7 Source: "E7 (V_prov vs V_final)" |

*Note: "E7 Axiom 3" is also referenced internally in K5 formal block ("Asymmetry (E7 Axiom 3, post-closure)") — this label is now anchored to E7-Ax3 above.*

**K1-K8 anchor table:**

| E7 axiom | K-axiom target | Mapping note |
|---|---|---|
| E7-Ax1 (svataḥ prāmāṇya — default validity) | **K4** Default Validity | K4 operationalizes E7-Ax1: cert=1 ∧ ¬isNull(k) → V(k)=1 upon instantiation. BE lineage: svataḥ prāmāṇya (intrinsic validity via arthakriyā — causal efficacy). |
| E7-Ax2 (parataḥ + bādhaka — invalidation) | **K5** Invalidation (conditions i-iii) | K5 conditions (i) temporal order, (ii) ⊥ contradiction, (iii) authority = structural form of E7-Ax2 "∃M' contradicts M with valid authority → V(M)→0". |
| E7-Ax2 (bādhaka authority sub-condition) | **K6** Cross-Registration Authority | K6 formalizes E7-Ax2 authority sub-condition: Auth(k2→k1, C_K)=1 iff same C_K-sphere + V(k2)=1 + k1 ∈ scope(D_joint). BE lineage: bādhaka must itself be a valid pramāṇa. |
| E7-Ax3 (asymmetry / irreversibility) | **K5** post-closure irreversibility | K5 "V_final(k)→0 is absolute" (post-closure clause) = E7-Ax3 irreversibility. Also cross-referenced as "E7 Axiom 3" in K5 formal block. |
| E7-Ax3 (V_prov vs V_final) | **K7** Registration Process Closure | K7 V_prov→V_final transition formalizes E7-Ax3 asymmetry. BE lineage: Niścaya — ascertainment/determination at closure. |

*K5_prospective (Layer 2 bridge) inherits E7-Ax2 structural conditions (i)-(iii) via K5 — not a separate E7 anchor target; mediated through K5.*

**AHP trace (SOT links):**

| SOT | Anchor | Status |
|---|---|---|
| SOT-1 (BE Full) | svataḥ/parataḥ prāmāṇya — T6.03 (no dedicated node, L792); bādhaka — N_BE_00006; niścaya — K7 BE lineage | E7 §5b + K_Space K7 property |
| SOT-2 (K-Space canonical) | K4/K5/K6/K7 Source rows + §3f reverse-anchor note (2026-05-29) | `meta_architecture/K_Space_Axiomatization.md` |
| SOT-3 (K-Space Class C) | PEER-SYNC mirror of SOT-2 | `project_vvv_qmrf_class_c/01_axiomatization/K_Space_Axiomatization.md` |
| SOT-4 (CLAUDE.md) | E7 listed as Level 2 E-postulate source for K4-K7 | CLAUDE.md identity §Layer 1 |

Trace score: 4/4 K-side SOTs verified. Anchor strength: **STRONG**.

**RCA verdict (3-round × 5-Why × ≥4/5):**

| Round | Score | Finding |
|---|---|---|
| R1 (Define/Trace) | 4.5/5 | Root cause: E7 prose lacked explicit Axiom 1/2/3 labels → K_Space reference floating |
| R2 (Isolate) | 4.2/5 | Stress points: K6 ← E7-Ax2 authority sub-condition (isolated); K7 ← E7-Ax3 V_prov/V_final (isolated) |
| R3 (Fix+Verify) | 4.8/5 | 5 criteria: SOT-correct ✓, K-text-correct ✓, no loop ✓, no overclaim ✓, boundary clear ✓ |
| **Aggregate** | **4.5/5 PASS** | ≥4/5 threshold met. Anchor confirmed. |

---

## 4. Mathematical Notation / Ký hiệu Toán học

| Symbol | Meaning EN | Ý nghĩa VN | Domain |
|--------|-----------|-------------|--------|
| M | Measurement-registration act | Hành động đo-ghi nhận | Registration event |
| M′ | Subsequent measurement | Phép đo tiếp theo | Verification |
| ρ̃ | Conditionally updated state | Trạng thái cập nhật có điều kiện | Density matrix |
| ρ_certified | Registration-valid state | Trạng thái hợp lệ ghi nhận | Density matrix |
| Ĉ_ext | Extrinsic certification operator | Toán tử xác thực ngoại tại | Category 04 |
| svataḥ | Intrinsic validity | Tính hợp lệ nội tại | Buddhist term |
| parataḥ | Extrinsic validity | Tính hợp lệ ngoại tại | Buddhist term |
| bādhaka | Invalidating cognition | Nhận thức phủ quyết | Buddhist term; source analogue for registration override |
| arthakriyāśakti | Causal efficacy | Tác dụng nhân quả | Buddhist term |

---

## 5. Source Traceability / Truy vết Nguồn gốc

### 5a. BIAN gaps resolved

| BIAN | Gap name | SOT section | SOT line |
|------|----------|-------------|----------|
| BIAN-18 | Intrinsic vs. Extrinsic Measurement Validity Location | T6.03 | L790 |

### 5b. Buddhist Epistemology source

| Property | Value |
|----------|-------|
| SOT section | T6.03 |
| Name | Svataḥ prāmāṇya / Parataḥ prāmāṇya |
| Node status | **No separate node in SOT** (L792) |
| Note | Structural meta-epistemological principle, not a single concept |
| SOT BIAN table | L856: "(No separate node — svataḥ/parataḥ prāmāṇya)" |

### 5c. Key quotations

**SOT T6.03 (L794):**
> "Dharmakīrti's complex position: initial validity is intrinsic (via svasaṃvedana and arthakriyāśakti); invalidity is detected extrinsically (via bādhaka pramāṇa)."

**SOT T6.03 (L795):**
> "QM does not formalize whether a measurement's validity is established by the measurement itself or by subsequent verification. In experimental practice, extrinsic verification is standard: cross-checks, calibration runs, repetition, statistical analysis."

**SOT T6.03 (L796):**
> "QM has no formal account of where measurement validity is located."

**Category 04 (L84), legacy wording requiring registration-layer reading:**
> "The detector triggers the phenomenon intrinsically (Svataḥ), but the Universe, through extrinsic correlations (Parataḥ), is the ultimate entity that stamps the validated registration status onto that measurement."

---

## 6. QM Deficit / Khiếm khuyết QM

**English:**
QM equations "blindly trust every click from every detector" (Category 04, L64). The formalism treats ρ → ρₘ as instant and unconditional. But experimentalists never do this: they calibrate, repeat, and cross-check. E7 writes this verification practice directly into the mathematical structure.

**Vietnamese:**
Phương trình QM "tin mù quáng vào mọi tiếng click" (Category 04, L64). Hệ hình thức coi ρ → ρₘ là tức thời và vô điều kiện. Nhưng nhà thực nghiệm không bao giờ làm vậy. E7 viết thực hành kiểm chứng trực tiếp vào cấu trúc toán học.

---

## 7. Architectural Position / Vị trí Kiến trúc

```
E1 (Self-Certification)
 └→ E7 (Validity Location)  ← THIS POSTULATE
      └→ Category 01 (Retroactive Override / Bādhaka)
```

E7 depends on E1: self-certification (E1) establishes that a measurement CAN be intrinsically valid. E7 specifies WHERE validity lives and its asymmetric relationship with invalidity.

| Layer | Document | Role |
|-------|----------|------|
| Gap | BIAN-18 (in BIAN_index_SOT.md L47, no node) | Diagnosis |
| Category | vvv_qmrf_category_04_e07_dual_phase_registration_certification.md (Category 04) | Prescription |
| Framework | **This document (E7)** | Architecture |

---

## 8. Assertion Level / Mức Khẳng định

| Component | Class | Evidence |
|---|---|---|
| "QM has no validity location" | **M** | SOT T6.03 L796 |
| "Dharmakirti's asymmetric position" | **M** | SOT T6.03 L794 |
| "Extrinsic verification standard in practice" | **M** | SOT T6.03 L795 |
| "Validity intrinsic, invalidity extrinsic" | **M** | SOT T6.03 L794 |
| "Single-shot meaningful" | **D** | Applied consequence |
| "DPEC formalism" | **D** | Proposed |
| "ρ̃ → ρ_certified" | **D** | Proposed |
| "Pairs with Category 01 (REO)" | **M** | Category 04 L78 |

---

## 9. RCA Findings / Phát hiện RCA

### ✅ Finding 1: BIAN-18 now present in BIAN_index_SOT

BIAN-18 was absent from BIAN_index_v2 (which stopped at BIAN-17), but has been **added to BIAN_index_SOT.md L47** with no node (svataḥ/parataḥ prāmāṇya has no dedicated BE node), lens A4 gap, RCA no-mapping. Status: resolved by SOT consolidation 2026-05-12.

### ⚠️ Finding 2: No dedicated BE node

SOT T6.03 explicitly states: "No separate node in the BE SOT." Svataḥ/parataḥ prāmāṇya is a meta-epistemological debate, not a single concept with a node. This is architecturally correct — it reflects that E7 derives from a structural principle, not a single entity.

### ✅ Finding 3: Category 04 is well-developed

Unlike E4 (missing category), E7 has a complete Category 04 document (`vvv_qmrf_category_04_e07_dual_phase_registration_certification.md`) with bilingual prose, formal structure, and implications.

---

## 10. What E7 Does NOT Claim

1. Not claiming verification unnecessary — E7 says validity is default, not that verification is forbidden.
2. Not claiming single measurements infallible — E7 says valid until contradicted, not infallible.
3. Not claiming QM wrong — E7 supplements QM with what experimentalists already do.

---

*Source: system_mapping_SOT.md, vvv_qmrf_category_04_e07_dual_phase_registration_certification.md, QM_measurement_epistemic_postulates_framework.md*

---

## Schema Validation Checklist / Checklist Kiểm chứng Schema

| Check | Status | RCA note |
|---|---|---|
| Document type declared | Pass | Declared as `framework` for schema alignment. |
| Source traceability | Pass | Existing source/cross-reference sections provide the trace base. |
| Claim traceability | Pass | Existing assertion/claim sections classify the major claims. |
| Boundary / non-claim guardrail | Pass | Existing boundary/non-claim text limits overclaiming. |
| Validation rule | Pass | Reuse only with source, claim type, and boundary preserved; unresolved items must be marked `TODO(HOTFIX)` before publication use. |
