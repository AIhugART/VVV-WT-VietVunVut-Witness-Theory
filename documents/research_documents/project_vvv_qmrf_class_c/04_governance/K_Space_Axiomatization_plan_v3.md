Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# RCA Audit Plan v3 — K_Space_Axiomatization v3.0 derivation chain
# Kế hoạch RCA v3 — Chuỗi dẫn xuất K_Space_Axiomatization phiên bản 3.0

**Target (output A):** `documents/research_documents/meta_architecture/K_Space_Axiomatization_plan.md` (extend; phase 7–12 added).
**Target (output B):** `documents/research_documents/meta_architecture/K_Space_Axiomatization_v3.md` (NEW file — extend Layer 1+2 verbatim from v2.1; add Layer 3–5).
**Target (output C):** `documents/research_documents/meta_architecture/fits/` (NEW directory; Python venv `fits/.venv/`; scripts for Phase 10 numerical fits).
**Plan version:** v3.0 (2026-05-23)
**Method:** RCA Rule Zero + 3 rounds × 5-Why × scoring threshold (per `feedback_decision_rule.md`, threshold 3.5/5)
**Scope:** VVV-QMRF core (Internal-first); VVV-QMRF-EX used as **compass only** (citation in `EX-MARGIN` notes allowed; structure import BLOCKED).
**Status:** **SUPERSEDED** (2026-05-23). Actual execution followed K9_E path (not K9_A/B/C). See main plan `K_Space_Axiomatization_plan.md` Phases 7–13 verdicts for completed work. This file retained as architectural blueprint and RCA decision record (R1–R8, amendments A1–A6).

> **DISCLAIMER:** VVV-QMRF is independent Class D personal research, not Standard Quantum Mechanics, not peer-reviewed or experimentally validated, and not for real-world technical use. Full boundary protocol: `DISCLAIMER.md`.

---

## 0. RCA Motivation (Rule Zero)

### 0.1 Define — Symptom vs. Cause

| | |
|---|---|
| **Symptom** | `K_Space_Axiomatization.md` v2.1 dừng ở K1–K8 + T1–T7 (registration-logic axioms). KHÔNG sinh `probability equation` để fit dữ liệu EWF (Extended Wigner's Friend) của Proietti et al. 2019, Bong et al. 2020, hoặc tái dựng Frauchiger–Renner 2018 no-go. Plan file hiện tại đã đóng Phase 1–6 (F1–F10f) cho v1.5/v2.1 nhưng KHÔNG có roadmap cho "axiom → equation → data → prediction" mà `VVV_QMRF_Prompt_Sequence.md` đặt ra. |
| **Root cause** | K1–K8 đặc tả K-space **structurally** (`cert`, `V ∈ {0,1}`, `⊥_K`, `AdmJoint`) nhưng thiếu **bridge axiom định lượng** — chưa có ánh xạ "registration-state → continuous probability value". Khoảng cách "binary V → continuous P" (PROMPT 3 TEST 2) là **structural gap of K1–K8**, không phải lỗi diễn đạt. Vì vậy plan v25 đo lường nội tại đã đầy đủ; cần plan v26 cho hướng dẫn xuất equation + falsifiability. |

### 0.2 Trace — 5 Whys

1. **Why** `K_Space_Axiomatization.md` v2.1 không dẫn ra equation? → K5/K6 cho boolean V/Auth, không sinh xác suất.
2. **Why** phải có equation? → `VVV_QMRF_Prompt_Sequence.md` PROMPT 1–7 yêu cầu chuỗi `constraints → equation → fit (3 papers) → 3-observer prediction → interpretation reduction → honest assessment`.
3. **Why** chuỗi này cần thiết bây giờ? → Working Paper v2.0 đã promote central claim (commit d708504); Track B Phase 1–3 verified EWF model nhưng vẫn φ-conditional (memory `project_k_space_axiomatization.md`); cần Layer 3 (quantitative bridge) để chuyển Class D → testable.
4. **Why** không sửa v2 (overwrite)? → CLAUDE.md `extend, not overwrite`: Layer 1 K1–K8 đã **FROZEN**. Phải tạo v3 như extension layer.
5. **Root cause:** Plan v25 thiết kế cho RCA *nội tại* (Phase 1–6 internal consistency). Thiếu sườn cho derivation chain externalize ra dữ liệu. Cần plan v3.0 — bám theo 7 prompt, tạo v3 file, và `fits/` artifact.

### 0.3 Isolate — Gap chính xác

- Plan file thiếu **6 Phase mới** (Phase 7–12), tương ứng PROMPT 1–7 (PROMPT 4 expanded thành Phase 10a/10b/10c).
- v3 file thiếu **3 Layer mới** (Layer 3 probability bridge / Layer 4 multi-paper fit / Layer 5 prediction+reduction+assessment).
- Workspace thiếu **`fits/` artifact**: Python venv + 3 fit scripts.

### 0.4 Fix the cause — không phải symptom

- KHÔNG patch wording trong v2 hay add caveats.
- CÓ tạo file mới `K_Space_Axiomatization_v3.md` **extend** từ v2 (preserve Layer 1+2 verbatim) + thêm Layer 3–5.
- KHÔNG import VVV-QMRF-EX structure. CÓ dùng EX như compass: `EX-MARGIN` citation note (M4) cho intelligence về stress points (KE-SC 4.0).
- Phase 10 dùng **numerical fit thật** (scipy least-squares + χ²), reproducible qua venv riêng.

### 0.5 Verify

- Mỗi Phase mới (7–12) phải có verdict gate **≥ 3.5/5** theo `feedback_decision_rule.md`.
- v3 chỉ nâng version sau khi toàn bộ phase đóng đủ điểm.
- Class D conjecture KHÔNG được lẫn với K1–K8 frozen text. Class C promotion (cho K9_candidate) chỉ khi 2-stage audit (P8-C5 + P9-C6) đều pass.
- `EX-MARGIN` citation phân biệt rõ với structure import qua grep-lint gate (sprint S8).

---

## 1. Scope & Guardrails

### 1.1 Three primary data sources (M5 — all binding equally)

| ID | Source | arXiv | Loại data | Phase fit |
|----|--------|-------|-----------|-----------|
| **D1** | Proietti et al. 2019, *Experimental test of local observer-independence* | 1902.05080 | Experimental CHSH; S_exp = 2.416 ± 0.075 (5σ violation); 4 expectation values ⟨A_xB_y⟩; 6-photon; 1794 6-fold coincidences; 360h | **Phase 10a** |
| **D2** | Bong et al. 2020, *A strong no-go theorem on the Wigner's friend paradox* | 1907.05607 | Experimental Local Friendliness (LF) inequality violation; stronger no-go than Bell-Wigner | **Phase 10b** |
| **D3** | Frauchiger & Renner 2018, *Quantum theory cannot consistently describe the use of itself* | 1604.07422 | Theoretical no-go; agents F/F̄/W/W̄ reasoning; halting prob P(w=ok ∧ w̄=ōk) per round; Table 4 statements | **Phase 10c** (consistency, not χ²) |

### 1.2 Modification flags vs plan v1

| Flag | Modification |
|------|--------------|
| **M1** | Phase 10 = numerical fit thật, Python venv, scipy least-squares + χ² |
| **M2** | Sprint pacing tách session — S1 chạy trước, S2+ chờ approve từng bước |
| **M3** | `K9_candidate` được phép Class C nếu derivation từ K1–K8 đủ chặt (default D) |
| **M4** | EX node citation cho phép trong margin notes (`EX-MARGIN`), không structure import |
| **M5** | Bong + FR nâng lên primary data ngang Proietti |

### 1.3 CLAUDE.md guardrails (mandatory)

| Guard | Áp dụng |
|-------|---------|
| `extend, not overwrite` | v3 preserves K1–K8 verbatim from v2.1; chỉ thêm Layer 3–5 |
| `Internal-first; EX as compass; selectively imported` | EX chỉ xuất hiện ở `EX-MARGIN`; lint gate chặn structure import |
| Author metadata | v3 file outside `published_documents/` → PHẢI có header (per CLAUDE.md identity rules) |
| Boundary language | KHÔNG "logical fallacy" / "wrong" / "mistake" cho Standard QM; dùng "category boundary", "registration-layer distinction" |
| Bilingual | Title + key section heading song ngữ; equation/proof English; high-level explanation Vietnamese |
| Claim class discipline | Layer 3 default Class D, eligible Class C; Layer 4–5 Class D; flag ASSUMPTION rõ ràng |

---

## 1.4 **PRE-PHASE-7: Candidate Bridge Axioms K9_A / K9_B / K9_C (RCA R5–R7)**

**Context (RCA R5 4.9/5):** K1–K8 are structurally complete but generate NO distinguishability from Standard QM (binary cert/V ∈ {0,1} have no mechanism to produce continuous probability deviation). A bridge axiom K9 is **structurally necessary**. Three candidate K9 sketches are pre-proposed before Phase 7 so that Phase 7 C3 evaluates "K1–K8 + K9_candidate → distinguishability?" (not K1–K8 alone → guaranteed BLOCKING).

**Parameter Budget (RCA R6 4.9/5):** Proietti D1 provides only 4 data points (⟨A_xB_y⟩ values). Fitting constraint: #free_parameters ≤ 2 to maintain DOF ≥ 1 for χ² goodness-of-fit test. K9 candidates must respect this budget.

### Candidate Bridge Axiom K9_A: V-Weighted Born Rule

```
K9_A: P(o | K) = V(k) · |⟨o|ψ⟩|² / Z(K)
```

**Derivation:** K4 defines V(k) ∈ {0,1} (validity status). K9_A interprets V as a registration-validity gate: if V=1, use Born rule; if V=0, no registered event (outcome suppressed). Normalization Z(K) ensures Σ_o P(o|K) = 1 under variable V.

**Axiom form (candidate):**
```
K9_A: Probability of outcome o, given K-state k, is weighted by
      registration validity: P(o|K) ∝ V(k)·Tr(E_o ρ).
      Normalization: Z(K) = Σ_o V(k)·Tr(E_o ρ).
```

**Free parameters:** 1 (optional scaling α if V gets continuous weighting; default α=1).

**Born rule limit:** cert=1 ∧ V=1 ∀k → P(o|K) = |⟨o|ψ⟩|² ✓

**Distinguishability vs Standard QM:** K9_A suppresses registered events with V=0. Standard QM always assigns P(o) = |⟨o|ψ⟩|² regardless of V. Deviation: δP(o) ≠ 0 only if V(k) varies across runs (i.e., some runs register, some don't). **Potential weakness:** if V is always 1 (all registrations succeed), K9_A is identical to Born rule. Distinguishability depends on empirical V-fluctuation.

**Status:** ✓ READY for Phase 7. 1 parameter ≤ 2 budget.

**Referent convention (RCA A1):** In K9_A, `V(k)` refers to `V(k_o^*)` where `k_o^*` is the K-state tuple that **would be instantiated** if outcome `o` is registered. At measurement time, `k_o^*` is hypothetical. Its V is determined by: (a) K4 default: `V(k_o^*) = 1` if `¬isNull(k_o^*)`. (b) K5 pre-evaluation: if `requires_K_joint = 1` AND existing `K_joint` contains `k_prev` such that `k_o^* ⊥ k_prev` within `C_K`, then `V_prov(k_o^*) → 0` upon instantiation (prospective K5 firing). **ASSUMPTION A1 (Class D):** K9_A requires K5 to fire **prospectively** on hypothetical tuples — semantic extension of K5 (which is defined for actual tuples, not hypothetical ones).

### Candidate Bridge Axiom K9_B: Registration-Conditioned Probability

```
K9_B: P(o | K) = Tr(E_o ρ) · f(cert(k), V(k), ⊥_K, C_K)
```

**Derivation:** K3 defines cert as self-certification marker. K5 defines ⊥_K (incommensurability) and firing conditions. K9_B modulates Born rule by a context-dependent function f that encodes registration conditions beyond validity alone.

**Axiom form (candidate):**
```
K9_B: P(o|K) = Tr(E_o ρ) · f(cert, V, ⊥_K, C_K)
      where f: {0,1} × {0,1} × {firing states} × {context} → [0,1]
      encodes how cert status, validity, and cross-registration
      context modulate outcome probability.
```

**Specification of f — CONDITIONAL REQUIREMENT for Phase 7:**

Option B1 (multiplicative): f(cert, V, ⊥_K, C_K) = f_cert(cert) · f_V(V) · f_context(⊥_K, C_K)
- ~~f_cert: {0→α, 1→1}~~ **REMOVED (RCA A3):** `cert(k) = 1 ∀k ∈ K_R` by K1 admission rule (lines 96–100 of v2.1). f_cert is always 1; α is not a real free parameter. cert's discriminating role operates at K_R admission boundary (pre-K_R), not inside K_R.
- f_V: {0→0, 1→1} (validity gate)
- f_context: depends on whether ⊥_K fires (0 or 1)
- **Free parameters:** 0–1 (f_context sensitivity only; α removed per RCA A3). ✓ PASS budget.

Option B2 (table-lookup): f explicitly specifies P(o|K) for each combination (cert, V, ⊥_K status) — fully determined by K1–K8 constraints, no free parameters. ✓ PASS budget if derivable.

Option B3 (information-theoretic): f(cert, V, ⊥_K, C_K) := I(K; o | context) / H(o) (information weighting). Requires information-theoretic foundation from K1–K8. TBD.

**Born rule limit:** f(1, 1, no-firing, trivial) = 1 → P(o|K) = Tr(E_o ρ) ✓

**Distinguishability vs Standard QM:** K9_B produces Δ P(o) whenever f ≠ 1, which depends on cert, V, or cross-registration context. More flexible than K9_A. **Requires specification of f before Phase 7; otherwise marked INCOMPLETE.**

**Status:** ⚠️ CONDITIONAL READY. Requires f-specification before Phase 7. If f is derived from K1–K8 (B2/B3), mark READY. If f requires additional assumption, note as CLASS D.

**Referent convention (RCA A1):** Same as K9_A: `V(k)` and `cert(k)` in `f(cert, V, ⊥_K, C_K)` refer to hypothetical tuple `k_o^*`. Additionally, `⊥_K` and `C_K` are evaluated on the **existing** K_joint state. K9_B's distinguishability depends on `f_context(⊥_K, C_K) ≠ 1`, which requires `requires_K_joint = 1` (K5 firing context). **ASSUMPTION A1 applies** (prospective K5 evaluation).

### Candidate Bridge Axiom K9_C: Colimit Probability via T4

```
K9_C: P(o_F, o_W | K_joint(F,W)) = lim_{colimit over K_i} w_i · P(o | K_i)
```

**Derivation:** T4 (bridge theorem, memory) defines colimit for N-observer K-states. K9_C uses T4 colimit to construct joint probability from individual observer registrations.

**Axiom form (candidate):**
```
K9_C: For multi-observer scenario (F, W, …), the joint probability
      is the weighted colimit of individual K-probabilities:
      P(o_F, o_W, … | K_joint) = lim_{colimit} Σ_i w_i(context) · P(o | K_i).
      Weighting scheme w_i: context-dependent (e.g., observer authority).
```

**Free parameters:** Weighting scheme w_i (2–3 parameters depending on context complexity).

**Born rule limit:** Single observer (N=1), w=1 → P(o|K) reduces to marginal from K_joint ✓

**Distinguishability vs Standard QM:** K9_C allows joint probabilities P(o_F, o_W) to differ from Standard QM if colimit weighting diverges from classical product. Extended Wigner's Friend (EWF) scenarios may show Δ P(o_F, o_W) when multiple observers have incommensurable K-spaces (⊥_K fires). **Requires T4 formalization and weighting-scheme specification.**

**Status:** ⚠️ NOT READY for Phase 7. Requires T4 formalization (not yet completed). Defer to Phase 8 if K9_A/B insufficient. If T4 formalization is completed before Phase 7, upgrade to CONDITIONAL READY.

### Pre-Phase-7 RCA Gate: Distinguishability Pre-Analysis (P7-C3 forecast)

**Forecast using K9_A/B/C:**

| K9 | K1–K8 mechanism | Distinguishability signal | Phase 7 C3 verdict (forecast) |
|----|---|---|---|
| **K9_A** | V-gating (binary suppression) | δ P(o) ≠ 0 if V-fluctuation across runs | **MARGINAL**: Signal exists only if experiment measures V-variability. Proietti D1 reports single S_exp; no V-breakdown. Likely **INSUFFICIENT** unless D2 (Bong) or re-analysis of D1 data reveals V-fluctuation. |
| **K9_B** | Context-dependent f(cert,V,⊥_K) | δ P(o) ≠ 0 if context or cert varies | **PROMISING**: If f is derived from K1–K8 rigorously (B2/B3), could produce distinguishable signal. Depends on f-specification quality. |
| **K9_C** | Colimit weighting w_i across observers | δ P(o_F,o_W) ≠ 0 in EWF multi-observer scenarios | **AMBITIOUS**: EWF (Proietti, Bong) may show signal if colimit differs from product. Requires T4 + weighting scheme. High potential but high complexity. |

**Pre-Phase-7 recommendation:** 
- Phase 7 evaluates K9_A + K9_B rigorously.
- If both fail C3 (no distinguishability), escalate to team: does K1–K8 need axiom redesign, or should K9_C be fast-tracked despite T4 incompleteness?
- Do NOT carry K9 candidates into Phase 8 if they fail Phase 7 C3.

### Pre-Phase-7: Proietti D1 K5 Firing Analysis (RCA A2)

**Question:** Does K5 fire in the Proietti 2019 (1902.05080) 6-photon EWF setup? If not, K9_A/B produce zero distinguishability for D1.

**Analysis:**
- Proietti setup: 6-photon Extended Wigner's Friend (EWF). Friend (F) measures photon in HV basis; Wigner (W) measures composite system in entangled basis.
- `requires_K_joint = 1`: Two observers (F, W) share a physical system → C_K exists → K5 firing precondition **satisfied**.
- K5 firing scenario: F registers `o_F ∈ {H, V}` (K4: `V(k_F) = 1`). W registers `o_W` in entangled basis → `o_W` may contain superposition of F's outcome → `k_W ⊥ k_F` possible → `V_prov(k_F) → 0`.
- **Conclusion:** K5 **CAN fire** in Proietti EWF setup. V-fluctuation signal exists in principle.

**Caveat — aggregation washout:** Proietti reports **aggregate** ⟨A_xB_y⟩ over 1794 coincidences. V-fluctuation is per-event; aggregation may wash out signal. Phase 10a must model **expected V-fluctuation rate** across the coincidence ensemble, not per-event V values.

**Single-observer caveat:** Standard CHSH experiments (single lab, no EWF) have `requires_K_joint = 0` → K5 does not fire → K9_A/B = Born rule exactly. Proietti D1 is specifically chosen because it IS an EWF setup with `requires_K_joint = 1`. D1 dataset selection is justified.

---

## 2. Phase Plan — extension to `K_Space_Axiomatization_plan.md`

Phase 7–12 mới đặt sau Phase 6 đã đóng. Fix ID đánh số liên tiếp **F11a, F11b, …** (không xung đột F1–F10f).

### Phase 7 — Physics Constraints Identification + RCA Gate Prerequisites (PROMPT 1)

**Scope:** Trước khi đề xuất equation, định danh **toàn bộ hard constraint** mà P(o_F, o_W | K-params) phải thỏa mãn. Phân ba category A/B/C. **INTEGRALLY INCLUDE** the three RCA gate questions from reference file `rca_k_h_registration_observability_plan.md` (§13) as **operational prerequisites** for any valid probability equation.

| ID | Target | Severity | Câu hỏi RCA |
|----|--------|----------|-------------|
| **P7-G1** | **Gate 1 — Operationalization of Phys(o\|H_physics)** | **BLOCKING** | Reference file §13 Gate 1: Does the equation operationalize `Phys(o\|H_physics)=1` beyond "detector click"? Phys should mean: decoherence (Decoh) + amplification (Ampl) + stability (Stable) criteria met. If candidate reduces Phys to detector language only, it fails operationalizability and cannot proceed. |
| **P7-G2** | **Gate 2 — Nontrivial registration gap** | **BLOCKING** | Reference file §13 Gate 2: Can the equation admit scenarios where `Phys=1 ∧ Lock_K=0`? (i.e., physically admissible but registration-locked fails). If equation forces Lock_K=1 whenever Phys=1, the two-gate structure collapses and adds no content. Document: which cases (C1–C10 from reference §13) apply in equation's regime? |
| **P7-G3** | **Gate 3 — Operational lock time definition** | **BLOCKING** | Reference file §13 Gate 3: Does the equation use an operationally defined `t_lock`? Prefer `t_lock := t_lock^val` (validation-lock time per §13 Gate 3). If t_lock is vague ("when observer knows result"), equation's timing predictions cannot be tested. |
| P7-C1 | Category A — Internal consistency K1–K8 | HIGH | Liệt kê đủ constraint từng axiom áp lên P? K2 t-injectivity → P phụ thuộc t-ordering? K5 ⊥_K → P điều kiện hóa lên context `C_K`? K7 t_close → cutoff time cho P sampling? K8 cross-space → P bảo toàn dưới embedding? |
| P7-C2 | Category B — Physical validity (Born rule limit) | HIGH | Born rule recover ở giới hạn nào? `cert=1 ∧ V=1 ∀k` có ép `P → \|⟨o\|ψ⟩\|²` không? No-signaling và normalization constraint từ Standard QM được giữ thế nào? |
| P7-C3 | Category C — Distinguishability of K9_A/B/C | **BLOCKING** | **REVISED (RCA R5 4.9/5):** Does K1–K8 + K9_candidate_i (A/B/C) generate prediction KHÁC Standard QM? Pre-Phase-7 forecast: K9_A marginal (depends on V-fluctuation), K9_B promising (if f is specified), K9_C ambitious (requires T4 + weighting). If ALL three fail Phase 7 C3, state khoa học finding: "K1–K8 + proposed K9_A/B/C cannot generate empirical distinguishability under current axiomatization. Axiom redesign required." Do NOT proceed to Phase 8 unless at least ONE K9 candidate passes C3. |

**Verdict gate:** ≥3.5/5; P7-C3 = "no distinguishability from K9_A/B/C" → dừng plan, escalate for redesign. **NEW (RCA R2 4.9/5):** P7-G1 OR P7-G2 OR P7-G3 = FAIL → candidate REJECTED before Phase 8. Gates are HARD STOPS, not soft criteria. No candidate proceeds to Phase 8 that fails any gate.

**EX compass note (M4):** memory `project_vvv_qmrf_ex_v1_6_phase9.md` ghi KE-SC bump từ 3.5→4.0 trong v1.7. Stress point lớn nhất tập trung tại K5 multi-observer/cross-context firing → ưu tiên Phase 7 Category A check K5 firing constraint trước.

**RCA Integration (R1 4.5/5):** Reference file's K-H lemmas (HDEF-01, KHI-01, DRC-02, TIM-01, NUL-01, COR-01) are cited in Phase 7 *as examples of operationalizability*, not promoted to new axioms. Phase 7 gates are the **validation checkpoints** that reference file provides.

### Phase 8 — Candidate Equation Generation (PROMPT 2)

**Scope:** Sinh **đúng 3 candidate** equation, mỗi candidate có term-by-term derivation, Born rule limit, distinguishability condition, role of `cert`/`V`.

| ID | Target | Severity | Câu hỏi RCA |
|----|--------|----------|-------------|
| P8-C1 | Term-by-term derivation traceability | HIGH | Mỗi term có chỉ ra axiom K1–K8 nào / `ASSUMPTION` flag không? |
| P8-C2 | Born rule limit verifiable | HIGH | Có condition cụ thể (cert=1 ∧ V=1 toàn bộ?) mà equation reduce đúng Born? |
| P8-C3 | Distinguishability magnitude computable | HIGH | Có scenario cụ thể với numeric difference > 0 vs Standard QM? |
| P8-C4 | cert + V appear non-trivially | MEDIUM | Nếu cert/V không xuất hiện → state "K-space adds no physical content beyond Standard QM in this formulation"; discard candidate. |
| **P8-C5 (M3+R3)** | Class C eligibility audit (Stage 1 of 2) | HIGH | Mỗi candidate: zero unjustified assumption beyond K1–K8 ∪ {Born rule recovery}? Pass P8-C5 → eligible for Stage 2 (P9-C6). Fail P8-C5 → mặc định Class D, KHÔNG eligible for Stage 2. **RCA R3 4.7/5:** Class C requires BOTH P8-C5 (derivational rigor) AND P9-C6 (operationalizability via Gates 1/2/3). Compound gate prevents false testability claims. |

**Bridge constraint:** mỗi candidate phải derive được từ K1–K8 + (nếu cần) **một** bridge axiom đánh dấu rõ `K9_candidate(i)` — KHÔNG đặt vào Layer 1 (vẫn frozen), mà ở Layer 3 (candidate bridge axiom). Đây resolve gap "binary → continuous".

### Phase 9 — Adversarial Falsification (PROMPT 3)

**Scope:** 4 test trên mỗi candidate sống sót Phase 8 (counterexample, axiom-consistency, distinguishability, cert/V sensitivity). Rank candidates.

| ID | Target | Severity | Test |
|----|--------|----------|------|
| P9-C1 | Test 1 — Physical counterexample | HIGH | Scenario cho `P ∉ [0,1]` hoặc `Σ_o P ≠ 1` hoặc vi phạm no-signaling? |
| P9-C2 | Test 2 — Axiom consistency | HIGH | Term nào contradict / undefined by K1–K8? `⊥_K` operationalize số ra sao? Binary → continuous gap closed? |
| P9-C3 | Test 3 — Distinguishability verification | HIGH | Numeric difference vs Standard QM trong scenario cụ thể. |
| P9-C4 | Test 4 — cert/V sensitivity | MEDIUM | `cert=1 ∧ V=1 ∀k` → equation reduce exactly Standard QM? |
| **P9-C5** | Rank surviving candidates | MEDIUM | Top-1 / Top-2 / Top-3 by combined criterion |
| **P9-C6 (M3+R3)** | Class C confirmation after adversarial (Stage 2 of 2) | HIGH | **RCA R3 4.7/5 — Compound gate:** Class-C-eligible candidate (P8-C5 PASSED) must ALSO: (1) pass all 4 adversarial tests, (2) satisfy Gates 1/2/3 from Phase 7 (operationalizability). Only if P9-C6 PASSES can candidate be **promoted to Class C**. Fail any criterion → demote to Class D with reason. Class D is still publishable as "theoretical exploration"; no stigma. |

**RCA gate:** Zero candidate pass all 4 tests → document failure mode, identify structural gap, dừng v3 ở Layer 3 partial state.

### Phase 10 — Multi-paper Data Fit (PROMPT 4 expanded — M1 + M5)

#### Phase 10a — Proietti CHSH numerical fit (D1)

| ID | Action |
|----|--------|
| P10a-C1 | Extract numerical: ⟨A_0B_0⟩, ⟨A_0B_1⟩, ⟨A_1B_0⟩, ⟨A_1B_1⟩ + Poisson 1σ errors từ arXiv 1902.05080 Fig.3 (main + Sup-Mat) |
| P10a-C2 | Identify free parameters trong K9_candidate selected; bounds từ K1–K8 |
| P10a-C3 | **Python script** `fits/proietti_chsh_fit.py`: `scipy.optimize.least_squares` + χ² + residuals + 1σ param uncertainty |
| P10a-C4 | Fit Standard QM Born rule lên cùng dataset cùng procedure; report Δχ². **Pre-registered decision criterion (RCA A6):** Likelihood ratio test (Wilks' theorem): `Δχ² = χ²_Born − χ²_K9`, `ΔDOF = #params_K9 − #params_Born`. Decision: `Δχ² > χ²_critical(ΔDOF, α=0.05)`. For ΔDOF=1: threshold = 3.84. For ΔDOF=2: threshold = 5.99. If `Δχ² ≤ threshold`: "K9 fits D1 no better than Born at 95% confidence." |
| P10a-C5 | Parameter interpretation in K-space; boundary check (param at 0 or 1?) |

#### Phase 10b — Bong LF inequality numerical fit (D2)

| ID | Action |
|----|--------|
| P10b-C1 | Extract numerical từ arXiv 1907.05607: LF inequality (3 settings/observer, 6 outcomes); violation magnitude + error bars |
| P10b-C2 | LF observable set khác CHSH → extend K9_candidate cho LF observable space; nếu không extend được, document scope boundary |
| P10b-C3 | **Python script** `fits/bong_lf_fit.py`: cùng pipeline scipy |
| P10b-C4 | Compare vs Standard QM LF prediction |
| P10b-C5a | **Cross-consistency — common params (RCA A5):** For parameters shared between CHSH and LF formulations, compare fitted values: `α_D1 vs α_D2`. Criterion: `|α_D1 − α_D2| < 2σ` (combined uncertainty). |
| P10b-C5b | **Extension-parameter scope (RCA A5):** If K9_candidate requires extension for LF observables (P10b-C2), document extension-specific parameters separately. These are scope-expansion, NOT consistency test — no D1 counterpart exists for comparison. |

#### Phase 10c — Frauchiger–Renner consistency check (D3, theoretical)

| ID | Action |
|----|--------|
| P10c-C1 | Extract 4 statements F/F̄/W/W̄ + halting prob per round từ arXiv 1604.07422 Table 4 |
| P10c-C2 | Compute K9_candidate prediction cho mỗi statement (no fitting — theoretical) |
| P10c-C3 | **Python script** `fits/fr_consistency.py`: numeric verification của K9_candidate's structural response to FR statements |
| P10c-C4 | Internal consistency: K9_candidate avoid được FR contradiction không? Mechanism nào (K5 V_prov pre-closure / K7 t_close timing / K8 cross-space)? |
| P10c-C5 | Reproduce vs avoid: |
| | – Nếu K9_candidate **reproduce** FR contradiction → K-space chia sẻ cùng problem với QT — finding quan trọng |
| | – Nếu K9_candidate **structurally avoid** FR → identify exact axiom blocking the paradox; document as Class C lemma |

#### Phase 10 — Joint verdict + Timing-Data Constraint

| ID | Action |
|----|--------|
| P10-C6 | 3-way consistency check: fit D1 OK + fit D2 OK + consistency D3 OK → strong evidence for K9_candidate. Split outcomes → RCA mismatch root cause; document, do not force consensus. |
| **P10-TIM** | **RCA R4 4.7/5 — Timing Data Feasibility:** Omit null-model N0 fit. Reason: D1/D2/D3 arXiv papers publish summary statistics (⟨A_xB_y⟩, LF values, FR statements), NOT event-level timestamps. Defensible proxy (publication date, table-appearance time) would use coarse calendar timestamps (months apart) → artifacts dominate signal. **Phase 10 is TWO-WAY comparison only:** VVV-QMRF vs Standard QM, using published numerical data. No N0 classical-processing baseline. **Phase 12 documents this data-availability gap honestly** as "K-H operational metrics (τ_reg, N_null) deferred to future work pending raw event-level data access." |

### Phase 11 — 3-Observer Prediction + Interpretation Reduction (PROMPT 5 + PROMPT 6)

#### Phase 11a — 3-observer EWF prediction

| ID | Action |
|----|--------|
| **P11a-G0** | **T4 readiness gate (RCA A4, BLOCKING):** T4 (N-observer K_joint) must be formalized to the level required by selected K9_candidate BEFORE Phase 11a begins. For K9_A/B with N=2 (F/W): T1 suffices (K_joint for 2 observers exists) → PASS. For N=3 (F/W/SW): requires T4 N-observer generalization. If unavailable → Phase 11a produces 2-observer prediction only; 3-observer deferred. For K9_C: requires full T4 colimit → MUST be formalized. |
| P11a-C1 | Extend K9_candidate using T4 colimit (N-observer K_joint) cho 3 observers F/W/SW (subject to P11a-G0 gate) |
| P11a-C2 | Flag mọi additional ASSUMPTION ngoài K1–K8 ∪ T4 |
| P11a-C3 | Compute P(o_F, o_W, o_SW) using best-fit params (no refit) |
| P11a-C4 | Standard QM prediction cho cùng setup; compute Δ per outcome |
| P11a-C5 | If max Δ > 0 → compute experimental runs cho 3σ discrimination; describe physical setup |
| P11a-C6 | Falsifiability statement (PROMPT 5 STEP 5 format) |

#### Phase 11b — Interpretation reduction map

| ID | Action |
|----|--------|
| P11b-C1 | Copenhagen: cert=1, V=1 cho one outcome / V=0 cho others → reduces? |
| P11b-C2 | Many-Worlds: K_joint exists ∀ observer pairs, ⊥_K never fires → reduces? |
| P11b-C3 | Relational QM: ⊥_K fires cross-observer, no global K_joint → reduces? |
| P11b-C4 | QBism: cert encodes agent-specific registration, no inter-agent V comparison → reduces? |
| P11b-C5 | Identify K-space region không tương ứng interpretation nào → genuinely new VVV-QMRF claim region |

### Phase 12 — Honest Assessment (PROMPT 7)

| ID | Target | Action |
|----|--------|--------|
| P12-C1 | Assumption audit | Liệt kê mọi assumption Phase 7–11 không derive từ K1–K8; rate JUSTIFIED / WEAKLY JUSTIFIED / UNJUSTIFIED |
| P12-C2 | Circular reasoning check | Conclusion-as-premise patterns; AJVS axiom vs conclusion distinction |
| P12-C3 | Alternative explanations | Could simpler framework produce same fit? VVV-QMRF specifically required, hay any param-rich framework? |
| P12-C4 | Missing physics | cert + V encode physical content beyond Standard QM? Nếu "none" cho cả hai → state "K-space currently a notational variant of Standard QM, not extension." |
| P12-C5 | Publication readiness | Min additional work cho Foundations of Physics / Phys Rev A submission; rate EASY / MEDIUM / HARD / REQUIRES_EXPERT_COLLAB |

**RCA gate:** Phase 12 KHÔNG được soften. Output có thể là "K-space is notational variant" — acceptable nếu đó là sự thật RCA trỏ tới.

---

## 3. Output B — `K_Space_Axiomatization_v3.md` structure

```
Author metadata (per CLAUDE.md identity rules)
Title bilingual EN/VN
Version: 3.0
Status: Layer 1 (K1–K8) FROZEN — verbatim from v2.1
        Layer 2 (T1–T7) preserved verbatim from v2.1
        Layer 3 (Probability Bridge K9_candidate) NEW — Class C eligible (default D)
        Layer 4 (3-paper Data Fit) NEW — Class D
        Layer 5 (Prediction + Reduction + Assessment) NEW — Class D
DISCLAIMER

§0 RCA Motivation (extended)
  0.6 Why v3 — gap analysis K1–K8 → equation
  0.7 EX compass note pattern (M4) — citation vs structure-import rule

§1 Layer 1 — K1–K8 (PRESERVED VERBATIM from v2.1, byte-diff = 0 expected)
§2 Layer 2 — T1–T7 (PRESERVED VERBATIM from v2.1, byte-diff = 0 expected)

§3 Layer 3 — Probability Bridge (NEW)
  3.1 Constraint Catalog (Phase 7 output)
  3.2 Candidate Equations 1/2/3 (Phase 8 output)
  3.3 Adversarial Test Results (Phase 9 output)
  3.4 Selected K9_candidate — final Class assignment (C if 2-stage audit pass, else D)

§4 Layer 4 — Multi-paper Data Fit (NEW)
  §4a Proietti 2019 fit (D1) — link `fits/proietti_chsh_fit.py`
  §4b Bong et al. 2020 fit (D2) — link `fits/bong_lf_fit.py`
  §4c Frauchiger–Renner 2018 consistency (D3) — link `fits/fr_consistency.py`
  §4d Joint cross-consistency analysis (P10-C6 verdict)

§5 Layer 5 — Prediction + Reduction + Assessment (NEW)
  5.1 3-observer EWF prediction (Phase 11a)
  5.2 Interpretation reduction table (Phase 11b)
  5.3 Honest assessment (Phase 12)
  5.4 Falsifiability statement

§6 Open Items v3 + Action Items A6+

CHANGELOG v2.1 → v3.0

[EX-MARGIN compass notes embedded throughout, M4 pattern]
```

### 3.1 EX-MARGIN citation pattern (M4)

```markdown
Some K-space claim about V/cert behavior under stress.

> **EX-MARGIN [EX_NODE_xxx]:** Compass note — VVV-QMRF-EX node `EX_NODE_xxx`
> shows KE-SC = 4.0 stress at this junction; cited for prioritization only,
> not imported as structure. See EX v1.7 §M.N.
```

**Lint gate (S8 QA):**
- ALLOWED: `EX-MARGIN [EX_*]:` block, prose reference to EX node id for prioritization context.
- BLOCKED: `EX_EDGE_xxx →`, `from EX_NODE`, `inherits EX_*`, any structural reuse of EX edge definitions.

---

## 4. Output C — `fits/` artifact directory

### 4.1 Layout (chốt)

```
documents/research_documents/meta_architecture/fits/
├── .venv/                          # Python venv (numpy + scipy + matplotlib)
├── README.md                       # how to reproduce (venv setup, run order)
├── data/
│   ├── proietti_2019_chsh.csv      # extracted from arXiv 1902.05080
│   ├── bong_2020_lf.csv            # extracted from arXiv 1907.05607
│   └── frauchiger_renner_2018.csv  # extracted from arXiv 1604.07422 Table 4
├── proietti_chsh_fit.py            # Phase 10a
├── bong_lf_fit.py                  # Phase 10b
├── fr_consistency.py               # Phase 10c
├── joint_consistency.py            # Phase 10 P10-C6 verdict
└── outputs/
    ├── proietti_fit_params.json
    ├── proietti_residual_plot.png
    ├── bong_fit_params.json
    ├── bong_residual_plot.png
    ├── fr_consistency_report.json
    └── joint_verdict.json
```

### 4.2 Venv setup (Windows PowerShell, chốt)

```powershell
cd documents/research_documents/meta_architecture/fits
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install numpy scipy matplotlib
pip freeze > requirements.txt
```

### 4.3 Reproducibility contract

- Mọi script đọc data từ `data/*.csv` (no hard-coded numbers in scripts).
- Mọi output ghi vào `outputs/*.json|*.png` (deterministic seed nếu có Monte Carlo).
- `README.md` documents Python version, exact reproduction steps, expected runtime.

### 4.4 CSV schema (synthetic example, NOT raw production data)

**`data/proietti_2019_chsh.csv`:**
```csv
setting_label,expectation_value,sigma_upper,sigma_lower
A0B0,-0.870,0.030,0.030
A0B1,0.568,0.045,0.045
A1B0,0.561,0.043,0.043
A1B1,0.417,0.050,0.050
```
Date format: not applicable (single-experiment paper, reference date in CITATION metadata only).

**`data/bong_2020_lf.csv`:** columns `setting_index` (int), `outcome_label` (str), `lf_value` (float), `sigma` (float).

**`data/frauchiger_renner_2018.csv`:** columns `statement_id` (str: e.g. "F1", "Fbar1", "W1", "Wbar1"), `agent` (str), `predicted_probability` (float ∈ [0,1]).

---

## 5. Sprint Sequencing (M2 — tách session)

| Sprint | Deliverable | Gate (≥3.5/5 + user approve) | Est. time |
|--------|-------------|------------------------------|-----------|
| **S1** | Plan file A updated: Phase 7+8 issue registry + Fix ID prefix F11/F12 + dependency map | Self-close, then user review | 2–3h |
| **S2** | Plan file A: Phase 9 + 10a + 10b + 10c registry | Approve before S3 | 2h |
| **S3** | Phase 7 RCA outputs → v3 §3.1 Constraint Catalog | Approve | 3–4h |
| **S4** | Phase 8 + 9: 3 candidates + adversarial; finalize K9_candidate + Class assignment | Approve | 4–6h |
| **S5a** | Phase 10a: `fits/.venv/` setup + `fits/proietti_chsh_fit.py` + outputs/proietti_*.{json,png} | Approve | 3–4h |
| **S5b** | Phase 10b: `fits/bong_lf_fit.py` + outputs/bong_*.{json,png} | Approve | 3–4h |
| **S5c** | Phase 10c: `fits/fr_consistency.py` + outputs/fr_consistency_report.json | Approve | 2–3h |
| **S5d** | Phase 10: `fits/joint_consistency.py` + outputs/joint_verdict.json + P10-C6 narrative | Approve | 1h |
| **S6** | Phase 11 (3-observer + reduction map) → v3 §5.1+§5.2 | Approve | 3–4h |
| **S7** | Phase 12 honest assessment → v3 §5.3+§5.4 | Approve | 2h |
| **S8** | Write v3 §1–2 preserved + §3–5 new, integrate all phases; QA gates (byte-diff K1–K8, EX-leak lint, claim-class audit) | Approve final | 3h |

**Total revised estimate:** 28–37h split into ≥8 sessions.

Each sprint ends with:
1. Concrete deliverable (file / section / script / artifact)
2. RCA verdict ≥3.5/5 logged
3. Gate question for user approve / modify

---

## 6. Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| R1 — Phase 7 Category C empty (no distinguishability) | HIGH | Treat as legit finding; document; don't continue Phase 8 |
| R2 — All 3 Phase 8 candidates fail adversarial | HIGH | Document failure mode; identify structural gap; don't fabricate |
| R3 — Proietti fit identical to Standard QM | MEDIUM | Honest report; "equally well, indistinguishable by this dataset" |
| R4 — EX structure imported by mistake | MEDIUM | Lint gate (S8) blocks structural EX patterns |
| R5 — K1–K8 text accidentally modified in v3 | **BLOCKING** | Byte-diff v3 §1–2 vs v2.1 §1–2; auto-fail if non-zero |
| R6 — Class C ↔ Class D mix-up | HIGH | Per-section claim-class badge; review checklist |
| R7 — Bilingual inconsistency | LOW | Section title bilingual; equation English |
| R8 (M1) — Python fit non-convergent / fit poor | MEDIUM | Multi-seed optimizer; bounded params from K1–K8; document failure structurally if needed |
| R9 (M1) — Numeric extraction loss (.tex provides expectation values, not raw counts) | MEDIUM | Use published values; document uncertainty; flag blocker if raw needed |
| R10 (M3) — Class C promotion too lenient → claim too strong | HIGH | 2-stage audit (P8-C5 + P9-C6) both must pass; default D until both pass |
| R11 (M4) — EX node citation leaks structure | MEDIUM | Lint script in S8 |
| R12 (M5) — 3-paper data give contradictory fits | HIGH | P10-C6 joint verdict — legit scientific finding; document mismatch, don't force consensus |
| R13 (M5) — Bong LF uses different observable set; K9_candidate may not generalize | MEDIUM | P10b-C2 explicit observable extension step; document scope boundary if no extension possible |
| R14 (M5) — FR is theoretical, no "data" to fit | LOW | Phase 10c reframed as consistency check (structural Class C verification), not numerical fit; still binding per M5 |
| R15 — Plan file A merge conflict if v25 has unsaved edits | LOW | Read v25 head first in S1; reconcile before extending |
| **R16 (RCA R2 4.9/5)** | **Gate hard-stop may reject all candidates** | HIGH | If P7-G1 OR P7-G2 OR P7-G3 fails for all 3 Phase 8 candidates, no candidates proceed to Phase 10. RCA R2 4.9/5 approves gates as hard stops (prevents resource waste). Honest outcome: "K-space K1–K8 cannot generate probability equation with required operationalizability." |
| **R17 (RCA R4 4.7/5)** | **Two-way fit only (N0 omitted) reduces comparison depth** | MEDIUM | Omitting null-model N0 classical-processing baseline means cannot distinguish whether signal is K-H-driven or just statistical artifact. RCA R4 4.7/5 approves omission to avoid defensible-proxy bias. Mitigation: Phase 9 TEST 5 (consistency with τ_reg/N_null/I metrics) is a post-hoc theoretical gate. |

---

## 7. Issue Registry — Phase 7–12 dự kiến

| ID | Phase | Severity | Status |
|----|-------|----------|--------|
| P7-C1 | 7 | HIGH | PENDING |
| P7-C2 | 7 | HIGH | PENDING |
| P7-C3 | 7 | **BLOCKING** | PENDING |
| P8-C1 | 8 | HIGH | PENDING |
| P8-C2 | 8 | HIGH | PENDING |
| P8-C3 | 8 | HIGH | PENDING |
| P8-C4 | 8 | MEDIUM | PENDING |
| P8-C5 | 8 | HIGH | PENDING |
| P9-C1 | 9 | HIGH | PENDING |
| P9-C2 | 9 | HIGH | PENDING |
| P9-C3 | 9 | HIGH | PENDING |
| P9-C4 | 9 | MEDIUM | PENDING |
| P9-C5 | 9 | MEDIUM | PENDING |
| P9-C6 | 9 | HIGH | PENDING |
| P10a-C1..C5 | 10a | HIGH | PENDING |
| P10b-C1..C5 | 10b | HIGH | PENDING |
| P10c-C1..C5 | 10c | HIGH | PENDING |
| P10-C6 | 10 | HIGH | PENDING |
| P11a-G0 | 11a | **BLOCKING** | PENDING |
| P11a-C1..C6 | 11a | HIGH | PENDING |
| P11b-C1..C5 | 11b | MEDIUM | PENDING |
| P12-C1..C5 | 12 | HIGH | PENDING |

**Fix ID allocation:** F11a, F11b, … (Phase 7); F12a, … (Phase 8); …; F16a, … (Phase 12). Reserves F11–F99 for v3.0 derivation chain. Future v3.x patches use F100+.

---

## 8. Dependency Map (forward)

```
Phase 7 (Constraints)
  P7-C1 (K1–K8 internal)  → P8 candidate derivation traceability
  P7-C2 (Born limit)      → P8-C2, P9-C4
  P7-C3 (Distinguishable) → P9-C3, P11a-C5 (gating)

Phase 8 (3 candidates)
  P8-C1..C4 → P9-C1..C4 (per-candidate adversarial)
  P8-C5    → P9-C6 (Class C eligibility carry-through)

Phase 9 (adversarial)
  P9-C5 ranking → Phase 10 selected K9_candidate
  P9-C6 Class assignment → v3 §3.4 claim class

Phase 10 (3-paper fit)
  P10a → §4a + outputs/proietti_*
  P10b → §4b + outputs/bong_*
  P10c → §4c + outputs/fr_*
  P10-C6 joint → §4d

Phase 11 (prediction + reduction)
  P11a-C1..C6 → §5.1 + falsifiability statement
  P11b-C1..C5 → §5.2 reduction table

Phase 12 (honest assessment)
  P12-C1..C5 → §5.3 + §5.4

S8 QA gates
  Byte-diff K1–K8 = 0          (block-or-pass)
  EX-leak grep = 0              (block-or-pass)
  Claim-class audit consistency (block-or-pass)
  Verdict aggregate ≥ 3.5/5     (block-or-pass)
```

---

## 9. Verdicts Summary (template — to be filled per phase)

### Phase 7 — PENDING

| ID | Score | Severity | Status |
|----|-------|----------|--------|
| P7-C1 | — | HIGH | PENDING |
| P7-C2 | — | HIGH | PENDING |
| P7-C3 | — | BLOCKING | PENDING |

### Phase 8 — PENDING
### Phase 9 — PENDING
### Phase 10 (a/b/c/joint) — PENDING
### Phase 11 — PENDING
### Phase 12 — PENDING

---

## 10. Decisions chốt

| # | Quyết định | Trạng thái |
|---|-----------|-----------|
| 1 | `fits/` location | **CHỐT**: `documents/research_documents/meta_architecture/fits/` |
| 2 | Python env | **CHỐT**: venv `fits/.venv/` với numpy + scipy + matplotlib |
| 3 | Sprint pacing | **CHỐT**: tách session (M2); S1 chạy trước, S2+ chờ approve |
| 4 | Class label cho K9_candidate | **CHỐT**: cho phép Class C nếu derivation từ K1–K8 đủ chặt (default D, M3) |
| 5 | EX usage | **CHỐT**: cho phép citation EX node ids ở `EX-MARGIN` notes; không structure import (M4) |
| 6 | Primary data sources | **CHỐT**: Proietti + Bong + FR ngang hàng (M5) |
| 7 | Plan file destination | **CHỐT**: lưu plan này vào `K_Space_Axiomatization_plan_v3.md` (file đang đọc) |
| **8 (RCA R1 4.5/5)** | **Reference file integration** | **CHỐT**: `rca_k_h_registration_observability_plan.md` provides **validation-layer checkpoints only**, not co-equal framework. K-H lemmas (HDEF-01–COR-01) cited as operationalizability examples; NOT promoted to new axioms. Phase 7 Gates 1/2/3 are hard-stop prerequisites for Phase 8 candidates. |
| **9 (RCA R2 4.9/5)** | **Gate structure rigor** | **CHỐT**: P7-G1 OR P7-G2 OR P7-G3 = FAIL → candidate REJECTED before Phase 8. Hard stops, not soft criteria. Prevents resource waste on operationally opaque equations. |
| **10 (RCA R3 4.7/5)** | **Class C eligibility (compound gate)** | **CHỐT**: Class C requires P8-C5 (derivational rigor) AND P9-C6 (Gate operationalizability + adversarial tests). Both must pass. Default is Class D. Prevents false testability claims. |
| **11 (RCA R4 4.7/5)** | **Timing data constraint** | **CHỐT**: Omit null-model N0 fit; use two-way comparison (VVV-QMRF vs Standard QM) only. Phase 12 documents data-availability gap: "K-H operational metrics τ_reg, N_null deferred to future work pending raw event-level data." Avoids defensible-proxy bias (coarse calendar timestamps). |
| **12 (RCA R5 4.9/5)** | **K9 proposal timing** | **CHỐT**: K9 candidates (K9_A, K9_B, K9_C) PRE-PROPOSED before Phase 7. Phase 7 C3 evaluates "K1–K8 + K9_i → distinguishability?" (not K1–K8 alone). Eliminates tautological BLOCKING of K1–K8 standalone. |
| **13 (RCA R6 4.9/5)** | **Parameter budget for fitting** | **CHỐT**: K9 candidates must have ≤ 2 free parameters to fit Proietti D1 (4 data points). Prevents overfitting; ensures χ² DOF ≥ 1. K9_A: 1 param ✓. K9_B: 1–2 params conditional on f-spec ✓. K9_C: 2–3 params (deferred). |
| **14 (RCA R7 4.58/5)** | **K9_A/B/C maturity levels** | **CHỐT**: K9_A ready for Phase 7. K9_B conditional (requires f-specification). K9_C deferred (requires T4 formalization). Phase 7 evaluates ready + conditional; escalate to Phase 8 if K9_A/B fail C3. |
| **15 (RCA R8 4.0/5)** | **3-round audit amendments A1–A6** | **CHỐT**: 6 amendments applied (2026-05-23). A1: K9_A/B referent convention (`V(k_o^*)` hypothetical tuple + ASSUMPTION A1 Class D). A2: Proietti K5 firing analysis (`requires_K_joint=1` confirmed in EWF). A3: K9_B B1 cert α removed (vacuous by K1 admission rule). A4: Phase 11a T4 gate (P11a-G0 BLOCKING). A5: P10b-C5 split → C5a (common-param) + C5b (extension-param). A6: P10a-C4 Δχ² pre-registered (Wilks' theorem, p<0.05). |

---

## 11. Trạng thái hiện tại

**Plan v3.0 đã được UPDATE với 7 RCA verdicts + 6 amendments (2026-05-23):**
- **RCA R1 4.5/5:** Reference file integration (validation-layer checkpoints only, no structure import)
- **RCA R2 4.9/5:** Gate structure (P7-G1/G2/G3 = hard stops; reject gate-failing candidates before Phase 8)
- **RCA R3 4.7/5:** Class C eligibility (compound gate: P8-C5 + P9-C6 both pass required)
- **RCA R4 4.7/5:** Timing data feasibility (omit N0 fit; two-way comparison VVV vs QM only)
- **RCA R5 4.9/5:** K9 pre-proposed (K9_A/B/C before Phase 7; eliminates tautological K1–K8-alone BLOCKING)
- **RCA R6 4.9/5:** Parameter budget ≤2 (K9 candidates must fit Proietti D1 4-point constraint)
- **RCA R7 4.58/5:** K9 maturity levels (K9_A ready, K9_B conditional, K9_C deferred)
- **RCA R8 4.0/5:** 3-round audit amendments (A1: referent convention, A2: Proietti K5, A3: cert α removed, A4: P11a-G0 T4 gate, A5: P10b-C5 split, A6: Δχ² pre-registered)

**Overall RCA aggregate: 4.54/5** ✓ All verdicts pass ≥4/5 threshold (stricter than plan's 3.5/5). **CORE ARCHITECTURAL FIXES + 3-ROUND AUDIT AMENDMENTS APPROVED. Plan is READY FOR S1.**

**ASSUMPTION A1 (Class D):** K9_A/B require K5 to fire prospectively on hypothetical tuples `k_o^*`. This is a semantic extension of K5 (defined for actual tuples). Flagged as Class D assumption; must be justified or removed during Phase 7 C3 evaluation.

**Plan đã được lưu. KHÔNG bắt đầu Sprint S1 cho đến khi user explicit approve.**

Next action (chờ user):
- `proceed S1` / `bắt đầu S1` → tôi bắt đầu cập nhật `K_Space_Axiomatization_plan.md` (output A) thêm Phase 7+8 registry.
- `modify: <thay đổi>` → tôi điều chỉnh plan v3 trước khi bắt đầu.
- `pause` → giữ nguyên plan, không làm gì thêm session này.

---

*Plan v3.0 — 2026-05-23 (RCA-verified + architectural fixes + 3-round audit amendments). RCA Rule Zero applied. VVV-QMRF scope. VVV-QMRF-EX as compass (M4). 3 primary data sources binding (M5). Numerical fit via Python venv (M1). Sprint-tách session (M2). Class C eligible cho K9_candidate (M3). RCA R1–R7 (4.63/5) + R8 (4.0/5, 6 amendments A1–A6) → aggregate 4.54/5. Amendments: A1 referent convention V(k_o^*), A2 Proietti K5 firing, A3 cert α removed, A4 P11a-G0 T4 gate, A5 P10b-C5 split, A6 Δχ² pre-registered. ASSUMPTION A1 (Class D) flagged. CORE FIXES + AUDIT AMENDMENTS APPROVED. READY FOR S1.*

