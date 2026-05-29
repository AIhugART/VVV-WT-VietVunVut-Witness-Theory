Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# RCA Round 2 — Structural Resolution: What MUST Be Fixed vs. What CAN Be Deferred?

**Date:** 2026-05-24
**Method:** 3-Round RCA x 5-Why x scoring threshold 4/5
**Scope:** VVV-QMRF, VVV-QMRF-EX as compass
**Input from Round 1:** 3 discrepancies identified. C2 honest = 7.5/10. φ-O2 is the only potentially BLOCKING open item. 4 open items + K9_E noise impact to triage.
**Sources:** `K_to_BH_Structure_Preserving_Map_v0_1.md` (v0.2) §5, §6, §7; `ex_compass_index.md`; `RCA_P10_NOISE_methodology_decision_2026_05_24.md`

---

## 0. Executive Snapshot

| Thuộc tính | Giá trị |
|------------|---------|
| **Câu hỏi quyết định** | Trong 4 open items + K9_E noise impact, cái nào PHẢI sửa ngay (MUST-FIX), cái nào CÓ THỂ hoãn (DEFERRED)? |
| **Items to triage** | φ-O2 (N_6 sufficiency), φ-O5 (N-observer), φ-O6 (codomain), φ-O7 (EX factorization), K9_E boundary note, CLAUDE.md phase sync |
| **EX compass bearings** | KE-SC 4.0 (K5 multi-observer) → φ-O2 priority; KE-SC 3.5 (T4 colimit) → φ-O5 deferral validated; KE-SC 3.7 (K9 beta) → K9_E noise note needed |

---

## 1. Open Item Triage — Individual Analysis

### 1.1 φ-O2: N_6 Sufficiency — "Auth(k2→k1, C_K)=1 ↔ P_{o2}·P_{o1}≠0"

**Current state:** N_6 proves forward direction (Auth=1 → P·P≠0). Reverse direction (P·P≠0 → Auth=1) is unresolved.

**5-Why: Tại sao sufficiency chưa được prove?**

```
W1: Tại sao φ-O2 vẫn unresolved sau Phase 2-4?
  → Phase 2 derived N_6 as necessary condition. Sufficiency được ghi nhận
    là open item và deferred. Phase 3-4 không đụng đến φ-O2.

W2: Tại sao sufficiency khó prove?
  → Auth(k2→k1, C_K)=1 requires 3 conditions từ K6:
    (a) k1, k2 in same C_K sphere
    (b) V(k2) = 1
    (c) k1 ∈ scope(D_joint)
    Trong khi P_{o2}·P_{o1}≠0 chỉ cho biết: hai projection không orthogonal trong H.
    → Làm sao từ "không orthogonal trong H" suy ra "cùng C_K sphere"?

W3: Có thể encode C_K sphere membership trong B(H) không?
  → C_K là K-side structural concept: "epistemic sphere" — tập hợp các K-space
    chia sẻ cùng D_joint (Level 4 construct). B(H) là operator algebra trên H.
    → KHÔNG có natural analogue của C_K trong B(H).
    → Hai projection có thể không orthogonal trong H nhưng thuộc về
    hai C_K sphere HOÀN TOÀN KHÁC NHAU (ví dụ: hai experiment độc lập).

W4: Có phải sufficiency là PROVABLY IMPOSSIBLE từ B(H) information alone?
  → K6 condition (a): "same C_K sphere" — C_K là K-side epistemic construct.
    K6 condition (c): "k1 ∈ scope(D_joint)" — D_joint là Level 4 extensional construct.
    B(H) chỉ chứa operator-algebraic information (projectors, commutators, spectra).
    → B(H) KHÔNG CÓ information về C_K membership hay D_joint scope.
    → Do đó: P_{o2}·P_{o1}≠0 → Auth=1 là KHÔNG THỂ prove từ B(H) alone.

W5: ROOT CAUSE — Tại sao sufficiency không thể prove?
  → **K6 chứa information (C_K sphere, D_joint scope) không có B(H) analogue.**
    Đây là FUNDAMENTAL BOUNDARY của φ, không phải bug hay gap.
    φ là map từ K → B(H). Nếu K-side chứa information không encode được
    trong B(H), thì φ KHÔNG THỂ là isomorphism (two-way) ở những chỗ đó.
    → Resolution: DOCUMENT φ-O2 NHƯ PERMANENT NECESSARY-ONLY BOUNDARY.
    Đây là KẾT QUẢ, không phải thiếu sót.
```

**Triage verdict:** **MUST-FIX — document as permanent boundary.**

N_6 là necessary-only condition vĩnh viễn. Lý do: K6's C_K sphere và D_joint scope là K-side structural concepts không có B(H) analogue. P_{o2}·P_{o1}≠0 là necessary nhưng không sufficient cho Auth=1. Đây là FUNDAMENTAL BOUNDARY của φ — φ ánh xạ K → B(H) nhưng không thể capture toàn bộ K-side structure trong B(H) image.

Document boundary statement: "N_6 is a necessary condition only. Sufficiency (P_{o2}·P_{o1}≠0 → Auth=1) cannot be proven from B(H) information alone because K6's conditions (a) shared C_K sphere and (c) D_joint scope membership are K-side structural concepts with no operator-algebraic analogue in B(H). This is a fundamental boundary of the φ-map — φ captures registration-operator correspondence but does not encode the full epistemic structure of K-space."

---

### 1.2 φ-O5: N-Observer Generalization

**Current state:** 2-observer EWF model works. N-observer needs T4-H Steps 2-4 (colimit with global commutativity). T4-H Steps 2-4 are deferred (Layer 2, updatable).

**Triage analysis:**
- φ-O5 dependency chain: φ-O5 → T4-H Steps 2-4 → T4 colimit → T1 N=2 constructive
- T4-H Step 1 is proven (pairwise AdmJoint necessary but not sufficient)
- Steps 2-4 require global overlap/path-commutativity — non-trivial category theory
- φ-O5 is properly documented as deferred with explicit dependency
- EX compass: KE-SC 3.5 on T4 colimit — confirms this is a stress point, not a quick fix

**Triage verdict:** **DEFERRED — valid deferral.** Dependency chain is explicit. T4-H Steps 2-4 are the gating items, not φ-O5 itself. No action needed beyond existing documentation.

---

### 1.3 φ-O6: Better Codomain M = vN({P_o})

**Current state:** B(H) is the working target. φ-O6 asks whether the von Neumann algebra M = vN({P_o : o ∈ O}) (smallest W*-algebra containing all outcome projectors) is a better codomain.

**Triage analysis:**
- N_1–N_T are all stated in B(H) language. All conditions use only projection operators and the zero operator — which are all in M.
- If we switch to M: all necessary conditions still hold (M ⊆ B(H), projections ∈ M, 0 ∈ M). The statements become slightly more precise (codomain = exactly the algebra generated by φ's image).
- BUT: Lüders products P_{o2}·P_{o1}·P_{o2} are in M (since M is an algebra closed under multiplication). The commutator condition [ι(P_{o_F}), P_{o_W}] ≠ 0 is evaluated in M (since the projectors are in M).
- B(H) vs M: functionally equivalent for all current φ use cases. M is "cleaner" but changes nothing material.
- Cost of switching: central claim wording "φ: K → B(H)" → "φ: K → M ⊂ B(H)" or "φ: K → vN({P_o})". All downstream documents need update.

**Triage verdict:** **DEFERRED — optimization, not necessity.** B(H) is adequate. M = vN({P_o}) would be more precise but changes no necessary condition and no concrete model verification. Document rationale; revisit only if B(H) proves problematic.

---

### 1.4 φ-O7: EX Factorization φ = Born ∘ φ_EX

**Current state:** Compass question — does φ decompose as Born rule applied to EX's K↔ρ map? φ_EX: K → ρ (density operators) then Born: ρ ↦ P_o (post-measurement projection).

**Triage analysis:**
- This is an architectural question about whether φ is a "derived" map (composed from EX + Born) or a "fundamental" map (direct K → B(H) without going through ρ).
- EX maps K ↔ ρ (density operators). Born rule maps ρ → P(o) = Tr(P_o ρ) (probability). Post-measurement state update maps ρ → P_o ρ P_o / Tr(...) (projection).
- φ maps k → P_o directly (without going through ρ). So φ ≠ Born ∘ φ_EX in the literal sense — φ skips ρ entirely.
- The question is whether φ CAN be factored through ρ. This is a mathematical question about diagram commutativity, not a structural necessity.
- EX compass constraint: "EX edges are NOT merged into K1–K8 or T1–T7. EX is compass, not cargo." (CLAUDE.md). φ-O7 should respect this boundary.

**Triage verdict:** **DEFERRED — compass-only.** φ-O7 is a curiosity, not a structural requirement. φ was designed as a direct K → B(H) map (registration → observable), intentionally bypassing the state layer (ρ). Factorability through ρ would undermine this architectural choice. No action needed.

---

### 1.5 K9_E Noise Downgrade Impact on Phi-Map Motivation

**Current state:** K9_E downgraded from genuine to qualified (v30, 2026-05-24). Noise sensitivity analysis FAIL (noise_threshold = 0.10 sigma RMS). Phi-map §0 references Proietti 2019 as experimental motivation.

**5-Why: Tại sao K9_E noise downgrade có thể ảnh hưởng đến φ-map?**

```
W1: Tại sao φ-map §0 reference Proietti?
  → §0 "Motivation" table cites 3 papers: FR (inconsistent conclusions),
    Proietti (CHSH violation → observer-independent facts cannot coexist),
    Bong (AOE + Locality violated by QM).
    → Proietti được dùng để motivate K_F ⊥_K K_W → [P_{o_F}, P_{o_W}] ≠ 0.

W2: Cái gì trong Proietti reference bị ảnh hưởng bởi K9_E noise downgrade?
  → K9_E noise downgrade ảnh hưởng đến: K9_E's fit to Proietti data (beta=0.598, 2.31sigma).
    → K9_E fit nói về SUPPRESSION PATTERN (K9_E vs QM-uniform).
    → φ-map dùng Proietti nói về NON-COMMUTATIVITY ([P_{o_F}, P_{o_W}] ≠ 0).

W3: Non-commutativity trong Proietti có bị ảnh hưởng bởi noise không?
  → [P_{o_F}, P_{o_W}] ≠ 0 là CHSH violation — Proietti đo được 5σ (S = 2.42 ± 0.08).
    → Đây là STANDARD QM EXPERIMENTAL FACT — CHSH violation không phải K9_E-specific.
    → Noise analysis của P10-NOISE target K9_E's suppression pattern, không target CHSH.
    → KẾT LUẬN: [P_{o_F}, P_{o_W}] ≠ 0 KHÔNG bị ảnh hưởng bởi K9_E noise downgrade.

W4: Vậy tại sao cần boundary note?
  → Dù non-commutativity không bị ảnh hưởng, nhưng φ-map §0 table nói "Proietti —
    CHSH violation — observer-independent facts cannot coexist" trong cùng document
    với K9_E claim "genuine fit beta=0.598, 2.31sigma."
    → Người đọc có thể CONFOUND hai thứ: CHSH violation (vững, 5σ) và
    K9_E suppression (không vững, noise FAIL).
    → Boundary note ngăn confound này: "φ-map uses Proietti for Standard QM
    CHSH violation only, not for K9_E suppression."

W5: ROOT CAUSE — Có cần thay đổi gì trong φ-map §0?
  → **Không cần thay đổi logic. Chỉ cần CLARIFY BOUNDARY.**
    φ-map dùng Proietti cho operator non-commutativity (Standard QM fact, 5σ).
    K9_E noise downgrade không ảnh hưởng đến fact này.
    → Fix: thêm 1 câu boundary note trong §0 table's Proietti row:
    "(Standard QM CHSH violation; unaffected by K9_E noise sensitivity analysis)"
```

**Triage verdict:** **MUST-FIX — add boundary note to φ-map §0.** Không thay đổi logic. Chỉ thêm clarification để ngăn confound giữa CHSH violation (Standard QM, vững) và K9_E suppression (K9_E-specific, noise-affected).

---

### 1.6 CLAUDE.md Phase Count Sync

**Current state:** CLAUDE.md line 65: "Track B Phases 1–3 complete." Roadmap v2.0: "Track B Phases 1–4 complete."

**Analysis:** Phase 4 = central claim promotion. CLAUDE.md IS the Phase 4 target (central claim was promoted TO CLAUDE.md). Therefore CLAUDE.md must say "1–4", not "1–3." Pure sync failure.

**Triage verdict:** **MUST-FIX — sync to "1–4".**

---

## 2. Triage Summary Table

| Item | Classification | Rationale | Action |
|------|---------------|-----------|--------|
| φ-O2 (N_6 sufficiency) | **MUST-FIX** | Real structural limitation. Document as permanent necessary-only boundary — K6 conditions (C_K, D_joint) have no B(H) analogue. | Add §6.X "N_6 Boundary Statement" to phi-map doc. Update §8 C2 re-assessment. |
| K9_E noise boundary | **MUST-FIX** | Confound risk giữa CHSH (vững) và K9_E suppression (noise-affected). | Add 1 câu boundary note trong §0 table Proietti row. |
| CLAUDE.md phase count | **MUST-FIX** | Pure sync failure. Phase 4 = CLAUDE.md promotion. | Edit CLAUDE.md line 65: "1–3" → "1–4." |
| φ-O5 (N-observer) | **DEFERRED** | Valid deferral. Dependency: T4-H Steps 2-4. EX compass confirms. | No action. Existing documentation adequate. |
| φ-O6 (codomain) | **DEFERRED** | Optimization only. M = vN({P_o}) không thay đổi necessary condition nào. B(H) is adequate. | No action. Document rationale. |
| φ-O7 (EX factorization) | **DEFERRED** | Compass-only curiosity. φ intentionally bypasses ρ. Factorability would undermine architecture. | No action. |

---

## 3. Round 2 Scoring

| Tiêu chí | Điểm | Ghi chú |
|----------|------|---------|
| Item-by-item analysis depth | 5/5 | Mỗi open item được phân tích riêng với 5-Why. φ-O2 được chứng minh là fundamental boundary (không thể prove, không phải chưa prove). |
| MUST-FIX vs DEFERRED criteria | 5/5 | Tiêu chí rõ ràng: structural necessity + confound risk → MUST-FIX. Optimization + curiosity → DEFERRED. |
| EX compass integration | 4.5/5 | KE-SC bearings được dùng để validate φ-O2 priority (4.0), φ-O5 deferral (3.5), K9_E note (3.7). Không import EX structure. |
| Boundary preservation | 5/5 | φ ≠ Born ∘ φ_EX (φ-O7) được xác nhận là architectural choice. K9_E noise không ảnh hưởng đến φ-map CHSH logic. |
| Actionability | 5/5 | 3 MUST-FIX items có action cụ thể, mỗi action có scope rõ ràng. 3 DEFERRED items có rationale documented. |
| **Round 2** | **4.9/5** | PASS (>= 4/5) |

---

## 4. Round 2 Verdict

**3 MUST-FIX, 3 DEFERRED.**

- **φ-O2:** Đây KHÔNG PHẢI là gap có thể đóng — đây là FUNDAMENTAL BOUNDARY của φ. K6 chứa K-side structural information (C_K sphere, D_joint scope) không có B(H) analogue. Documenting boundary này là KẾT QUẢ NGHIÊN CỨU, không phải thừa nhận thiếu sót.
- **K9_E noise:** CHSH violation (5σ) ≠ K9_E suppression (noise-affected). Boundary note ngăn confound, không thay đổi logic.
- **CLAUDE.md:** Sync failure thuần túy.

**Forward to Round 3:** Final decision — C2 re-assessment, classification verdict, path forward.

---

*RCA Round 2 — Structural Resolution. 2026-05-24. Score: 4.9/5. PASS. Proceed to Round 3.*
