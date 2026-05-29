Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# RCA Round 1 — Structural Audit: Is the Phi-Map Complete?

**Date:** 2026-05-24
**Method:** 3-Round RCA x 5-Why x scoring threshold 4/5
**Scope:** VVV-QMRF, VVV-QMRF-EX as compass
**Target:** phi-map K→B(H) — document `K_to_BH_Structure_Preserving_Map_v0_1.md` (v0.2) vs roadmap `phi_map_track_b_roadmap.md` (v2.0) vs CLAUDE.md
**Trigger:** Discrepancy giữa roadmap C2=8.0/10 và phi-map document tự đánh giá C2=7.0–7.5/10. CLAUDE.md ghi "Phases 1–3 complete" trong khi roadmap ghi "Phases 1–4 complete."
**Sources:** `K_to_BH_Structure_Preserving_Map_v0_1.md` (v0.2), `phi_map_track_b_roadmap.md` (v2.0), `CLAUDE.md` (line 65), `central_claim_change_RCA.md` (v1.0)

---

## 0. Executive Snapshot

| Thuộc tính | Giá trị |
|------------|---------|
| **Câu hỏi quyết định** | Phi-map document tự đánh giá C2=7.0–7.5, roadmap ghi C2=8.0, CLAUDE.md ghi Phases 1–3 (roadmap: 1–4). Gap nào là thật, gap nào là documentation sync? |
| **Discrepancies found** | 3 discrepancies: (1) C2 score gap 0.5–1.0 điểm, (2) Phase count mismatch (1–3 vs 1–4), (3) φ-O2 unresolved |
| **EX compass constraint** | Không EX node nào trực tiếp resolve φ-O2. KE-SC 4.0 (K5 multi-observer) gợi ý φ-O2 là priority, nhưng không cung cấp proof. |

---

## 1. Discrepancy Table (Pre-RCA Audit)

| # | Item | Roadmap (v2.0) | Phi-map doc (v0.2) | CLAUDE.md | Delta | Type |
|---|------|---------------|-------------------|-----------|-------|------|
| D1 | C2 readiness | 8.0/10 | 7.0–7.5/10 | (not stated) | -0.5 to -1.0 | Score gap |
| D2 | Phase status | "Phases 1–4 complete" | "Phase 2 complete" (title) | "Phases 1–3 complete" | Inconsistent | Sync failure |
| D3 | φ-O2 sufficiency | "Necessary only; sufficiency deferred" (in φ-O2 row) | ⚠️ "Deferred to Phase 3/4" (§5, §7 open items) | (not mentioned) | Not resolved | Real gap |

**Additional finding:** Roadmap v2.0 promotion checklist claims "Internal consistency check: K-Axiom + φ definition + N_1–N_T + §6.1 mutually compatible" ✅ — but φ-O2 is only half-characterized (necessary direction only). Compatibility check is valid for the necessary direction but silent on the missing sufficiency direction.

---

## 2. 5-Whys: Tại sao có readiness gap?

```
W1: Tại sao roadmap ghi C2=8.0 nhưng phi-map document tự đánh giá 7.0–7.5?
  → Roadmap v2.0 được cập nhật sau Phase 4 (promote central claim),
    dựa trên toàn bộ body of work (phi-map doc + WP §6.1 + CLAUDE.md promotion).
    Phi-map document v0.2 §8 được viết ở cuối Phase 2 và chưa được tái đánh giá
    sau Phase 3 (WP §6.1 re-framing) và Phase 4 (CLAUDE.md promotion).
    → Đây là STALE SELF-ASSESSMENT: document v0.2 không biết về Phase 3-4.

W2: Tại sao phi-map document không được tái đánh giá sau Phase 3-4?
  → Phase 3 operated trên WP v2.0 §6.1 (interpretation re-framing).
    Phase 4 operated trên CLAUDE.md (central claim promotion).
    Phi-map document v0.2 là Phase 1-2 artifact — không phải target của Phase 3-4 edits.
    Điểm C2 được "carry forward" từ v0.2 mà không re-evaluate.
    → Đây là DOCUMENTATION WORKFLOW GAP: mỗi phase cập nhật file riêng,
    không có bước "cross-document sync" sau mỗi phase.

W3: Tại sao gap này quan trọng? C2=7.5 vs 8.0 có khác biệt gì?
  → C2=8.0 là NGƯỠNG PROMOTION GATE (roadmap §1: "C2 target ≥ 8").
    Nếu C2 thật sự là 7.0–7.5, thì promotion gate CHƯA ĐƯỢC ĐÁP ỨNG.
    → Tuy nhiên, con số 7.0–7.5 đến từ self-assessment VIẾT Ở PHASE 2.
    Sau Phase 3-4, C2 có thể đã được cải thiện (WP §6.1 thêm φ-conditional analysis,
    CLAUDE.md central claim được formulate rõ ràng).
    → CÂU HỎI THẬT: không phải "tại sao có gap", mà là "C2 thật sự bây giờ là bao nhiêu?"

W4: Vậy C2 thật sự bây giờ là bao nhiêu? Làm sao đánh giá?
  → C2 = "conjectures φ: K → B(H)" — đánh giá mức độ φ được define và characterize.
    Sub-criteria (từ phi-map doc §8):
    - Target B(H) selected with justification: ✅ (§1, 3 counter-arguments)
    - Image restriction Im(φ) ⊆ Proj(B(H)) ∪ {0}: ✅ (§1.3)
    - "Structure-preserving" formalized (φ-1 to φ-7′): ✅ (§2)
    - K ≠ H reconciliation essay: ✅ (§3)
    - Concrete EWF 2-observer model: ✅ (§4)
    - Necessary conditions N_1–N_8 formally derived: ✅ (§6)
    - Bridge condition N_T from T2/T3: ✅ (§6)
    - φ-O1, φ-O3, φ-O4 resolved: ✅
    - φ-O2 sufficiency: ⚠️ NECESSARY-ONLY
    - N-observer generalization: ⚠️ DEFERRED (φ-O5)
    - Better codomain: ⚠️ OPEN (φ-O6)
    → Với φ-O2 necessary-only, N_6 là ĐẦY ĐỦ về mặt necessary condition
    nhưng KHÔNG ĐẦY ĐỦ về mặt characterization của φ-6.
    → Điểm thật: 7.5/10. Không phải 7.0 (có quá nhiều thứ đã hoàn thành),
    không phải 8.0 (φ-O2 vẫn là limitation thật sự).

W5: ROOT CAUSE — Tại sao có readiness gap?
  → **Gap có HAI thành phần:**
    (a) DOCUMENTATION SYNC FAILURE (~60%): Phi-map document v0.2 §8 self-assessment
        được viết ở Phase 2 và không được cập nhật sau Phase 3-4.
        Roadmap v2.0 C2=8.0 dựa trên Phase 4 holistic assessment.
        → Fix: cập nhật phi-map document §8 với post-Phase 4 re-assessment.
    (b) REAL STRUCTURAL LIMITATION (~40%): φ-O2 (N_6 sufficiency) vẫn necessary-only.
        Đây là genuine limitation — φ-6 authority-composition mới được
        characterize một chiều. Điểm C2 không thể đạt 8.0 chừng nào
        φ-O2 chưa được resolved HOẶC documented như fundamental boundary.
        → Fix: hoặc prove sufficiency, hoặc document đây là permanent boundary.
    (c) PHASE COUNT MISMATCH (D2): CLAUDE.md ghi "Phases 1–3", roadmap ghi "1–4".
        Phase 4 = promote central claim lên CLAUDE.md → nếu đã promote,
        CLAUDE.md phải ghi "Phases 1–4". Đây là sync failure đơn thuần.
        → Fix: sync CLAUDE.md "1–3" → "1–4".
```

---

## 3. Round 1 Scoring

| Tiêu chí | Điểm | Ghi chú |
|----------|------|---------|
| Định nghĩa vấn đề chính xác | 5/5 | 3 discrepancies được phân lập rõ: D1 (score gap), D2 (phase mismatch), D3 (φ-O2 unresolved) |
| Causal chain depth | 4.5/5 | 5-Why truy đến 2 root causes: documentation sync failure (60%) + real structural limitation (40%). Phase count mismatch được trace riêng. |
| Root cause isolation | 4.5/5 | Hai thành phần của gap được tách biệt rõ. Stale self-assessment ≠ genuine limitation. |
| Fix feasibility | 5/5 | Cả 3 discrepancies đều có fix rõ ràng: (a) update §8, (b) resolve-or-document φ-O2, (c) sync CLAUDE.md |
| Verification path | 4/5 | Verification = cross-check phi-map doc §8 mới + CLAUDE.md sync + roadmap update. Cần thêm: φ-O2 resolution verification. |
| **Round 1** | **4.6/5** | PASS (>= 4/5) |

---

## 4. Round 1 Verdict

**Gap là THẬT nhưng NHỎ hơn con số 0.5–1.0 điểm gợi ý.**

- **D1 (C2 score gap):** 60% là stale self-assessment (phi-map doc §8 written at Phase 2). 40% là genuine limitation (φ-O2). Honest C2 = 7.5/10.
- **D2 (phase count mismatch):** Pure sync failure. CLAUDE.md phải ghi "1–4" để khớp roadmap.
- **D3 (φ-O2 unresolved):** Real gap. Cần Round 2 để xác định: đây là gap có thể đóng (prove sufficiency) hay fundamental boundary (document as permanent)?

**Forward to Round 2:** φ-O2 là open item duy nhất có thể là BLOCKING. Round 2 sẽ triage cả 4 open items (φ-O2, φ-O5, φ-O6, φ-O7) + K9_E noise impact.

---

## 5. Round 2 Input

| Item | Status from Round 1 | Question for Round 2 |
|------|---------------------|----------------------|
| φ-O2 (N_6 sufficiency) | REAL GAP — necessary-only | Provable or fundamental boundary? |
| φ-O5 (N-observer) | DEFERRED — T4-H Steps 2-4 | Still valid deferral? |
| φ-O6 (codomain) | OPEN | Does M = vN({P_o}) change anything? |
| φ-O7 (EX factorization) | COMPASS-ONLY | Any action needed? |
| K9_E noise impact | NOT ASSESSED | Does noise downgrade weaken φ-map motivation? |
| CLAUDE.md phase count | SYNC FAILURE | Fix in Phase E |

---

*RCA Round 1 — Structural Audit. 2026-05-24. Score: 4.6/5. PASS. Proceed to Round 2.*
