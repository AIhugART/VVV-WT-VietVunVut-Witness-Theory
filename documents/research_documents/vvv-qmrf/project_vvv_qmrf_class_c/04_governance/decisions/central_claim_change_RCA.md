Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Central Claim Change — RCA Decision Document
# Quyết định thay đổi Tuyên bố trung tâm — Tài liệu RCA

**Framework:** VietVunVut Quantum Measurement Registration Framework (VVV-QMRF)
**Document type:** `meta_architecture / decision`
**Date:** 2026-05-22
**Version:** 1.0
**Author:** VietVunVut (Viet - Nguyen Xuan)
**Status:** Active — Phase 0 of Two-Track Approach adopted
**Scope:** VVV-QMRF core (Internal-first); VVV-QMRF-EX consulted as compass only
**Linked artifacts:**
- [readiness_assessment_phi_claim.md](../../archives/review/readiness_assessment_phi_claim.md)
- [K_Space_Axiomatization.md](../K_Space_Axiomatization.md) — Layer 1 frozen (K1–K8), Layer 2 (T1–T7)
- [phi_map_track_b_roadmap.md](phi_map_track_b_roadmap.md) — Long-term plan for full φ-form claim

> **DISCLAIMER / CẢNH BÁO:** VVV-QMRF is independent Class D personal research, not Standard Quantum Mechanics, not peer-reviewed or experimentally validated, and not for real-world technical use. Full boundary protocol: `DISCLAIMER.md`.

---

## 0. Summary / Tóm tắt

| | |
|---|---|
| **Decision** | Adopt **Track A** central claim wording immediately; pursue **Track B** (full φ: K → B(H) conjecture) as long-term roadmap. |
| **Quyết định** | Áp dụng tuyên bố trung tâm **Track A** ngay; theo đuổi **Track B** (conjecture đầy đủ φ: K → B(H)) như là lộ trình dài hạn. |
| **Rationale** | Track B has readiness 4.0/10 — adopting it now would create a stronger overclaim than the wording it intends to fix. Track A has readiness 8–9/10 and is fully supported by existing K-Space Axiomatization v2.1. |
| **Rule Zero compliance** | Full 5-step RCA performed (see §2). Root cause isolated: Component 2 (φ definition) is the single failure point gating Track B. |

---

## 1. Define — Symptom vs. Cause

### 1.1 Symptom

The current CLAUDE.md "Identity and scope rules" paragraph uses the wording:

> *"VVV-QMRF fills these gaps by adding 16 registration-layer postulates derived from structural analysis of Buddhist Pramāṇa epistemology..."*

This wording (`fills the gaps`, `adding 16 postulates`) is **declaratively assertive**: it states a completion-style claim that does not match the project's actual Class D research status. Reviewers may interpret it as "VVV-QMRF asserts a fix for Standard QM", which is not the project's intent.

### 1.2 Proposed replacement (initial request)

> *"VVV-QMRF proposes a registration-logic structure K and conjectures the existence of a structure-preserving map φ: K → B(H), where B(H) is the algebra of bounded operators on Hilbert space. We derive necessary conditions for φ and identify where standard QM interpretations fail to satisfy them."*

The replacement is more mathematically rigorous and falsifiable, but it depends on artifacts that **do not yet exist** in the project (see Component 2 below).

### 1.3 Cause

Two needs in tension:

- **(a) Stronger scientific claim:** the project wants a falsifiable mathematical conjecture rather than a philosophical interpretation.
- **(b) Missing artifact:** no document in the project defines φ: K → B(H), what "structure-preserving" means in this context, or which necessary conditions on φ are derived from K1–K8.

Adopting (b)-dependent wording now would re-create the same kind of overclaim the wording change was supposed to fix.

---

## 2. Trace — 5 Whys

1. **Why** change the central claim? → Current wording `fills the gaps` is read as "VVV-QMRF fixes QM", not as Class D research.
2. **Why** not just edit the wording? → A wording edit cannot create the mathematical bridge between K (registration-logic structure) and B(H) (operator algebra) needed for a falsifiable conjecture.
3. **Why** is a falsifiable conjecture needed? → To move VVV-QMRF from "philosophical interpretation" to "research program" with explicit success/failure criteria.
4. **Why** target B(H) specifically, instead of C\*-algebra, von Neumann algebra, or a category C\_obs? → This is itself an open question; B(H) is the narrowest of the natural targets and may be insufficient because K carries predicates (`cert`, `V`) that have no natural analogue in B(H).
5. **Root cause** → The proposed claim is **artifact-dependent**: K1–K8 are frozen (Layer 1) and T1–T7 are defined (Layer 2), but (i) φ is not defined, (ii) "structure-preserving" is not formalized for K → target, and (iii) §6 interpretation-comparison is currently architectural, not "fail necessary conditions for φ". Adopting the φ-form claim now would treat the symptom (wording strength) by re-introducing overclaim (asserting an unproven conjecture as central project identity).

---

## 3. Isolate — Failure Point

Per the readiness assessment ([readiness_assessment_phi_claim.md](../../archives/review/readiness_assessment_phi_claim.md)):

| Component | Score | Status |
|-----------|:----:|--------|
| C1 — "proposes registration-logic structure K" | **8.5/10** | Ready (K1–K8 frozen, T1–T7 in Layer 2) |
| C2 — "conjectures φ: K → B(H)" | **1.5/10** | **Not in project. Single failure point.** |
| C3 — "derive necessary conditions for φ" | **1.0/10** | Depends on C2 |
| C4 — "interpretations fail to satisfy" | **5.0/10** | Comparison exists but framed architecturally, not as φ-conditional failure |
| **Weighted total** | **4.0/10** | Not ready |

**Isolated root cause:** Component 2 is the single gating failure. All downstream components depend on it. Components 1 and 4 already exist in adequate form for a Track A claim.

---

## 4. Fix the Cause — Two-Track Decision

### 4.1 Track A — Adopted Immediately (Phase 0)

**Track A central claim (adopted 2026-05-22):**

> *"VVV-QMRF proposes a registration-logic structure K, axiomatized via K1–K8 (Layer 1 frozen) with bridge theorems T1–T7 (Layer 2), and derives K-side incommensurability (K_F ⊥_K K_W) in Extended Wigner's Friend scenarios. We identify where standard QM interpretations lack the structural machinery to formalize registration-layer conditions that VVV-QMRF provides. The K-space carrier supports 16 registration-layer postulates (E1–E16) derived from structural analysis of Buddhist Pramāṇa epistemology (Dignāga–Dharmakīrti tradition)."*

Track A:
- ✅ Fully supported by K-Space Axiomatization v2.1 (Layer 1 + Layer 2).
- ✅ Concrete model consistency proof (EWF 2-observer model, §7).
- ✅ Existing interpretation comparison (WP v2.0 §6) provides "lack structural machinery" claim.
- ✅ Honest about Class D status; no asserted φ.
- ✅ Preserves E1–E16 content (extend, not overwrite).
- ✅ Preserves "K ≠ H" architectural commitment.

### 4.2 Track B — Long-Term Roadmap (Phase 1–4)

**Track B target claim (aspirational, ~10–15 weeks of work):**

> *"VVV-QMRF proposes a registration-logic structure K and conjectures the existence of a structure-preserving map φ: K → B(H), where B(H) is the algebra of bounded operators on Hilbert space. We derive necessary conditions for φ and identify where standard QM interpretations fail to satisfy them."*

Track B will be pursued **without changing the central claim** until all four components reach readiness ≥ 8/10. The detailed roadmap lives in [phi_map_track_b_roadmap.md](phi_map_track_b_roadmap.md).

### 4.3 What Track A explicitly does NOT do

- ❌ Claim that VVV-QMRF "fills the gaps" of Standard QM (avoid declarative overclaim).
- ❌ Assert φ: K → B(H) exists (this is a future conjecture, not a current claim).
- ❌ Frame interpretations as "wrong" or "fail" — uses neutral boundary language per CLAUDE.md terminology rule.
- ❌ Touch BE node/edge SOT (`system_be_full.md`).

---

## 5. Verify — Verification Anchors

| Item to verify | Anchor |
|----------------|--------|
| K1–K8 frozen | [K_Space_Axiomatization.md §1](../K_Space_Axiomatization.md) |
| T1–T7 defined | [K_Space_Axiomatization.md §2](../K_Space_Axiomatization.md) |
| K ≠ H boundary preserved | [K_Space_Axiomatization.md §0.4](../K_Space_Axiomatization.md) and Track A wording absence of φ |
| φ does not exist yet | `grep "B(H)"` returns only this file, `phi_map_track_b_roadmap.md`, and the readiness assessment |
| §6 comparison still architectural | WP v2.0 §6 unchanged by Phase 0 |
| Author metadata rule compliance | Author block at top; this file is outside `public_documents/` and `published_documents/` |
| Extend-not-overwrite | CLAUDE.md change preserves E1–E16 content; only re-frames the central claim |

---

## 6. Risks Carried Forward

| Risk ID | Status after Phase 0 | Notes |
|---------|---------------------|-------|
| **R-1** Overclaim regression | ✅ Mitigated by adopting Track A | Reverted from "fills gaps" to scoped wording |
| **R-2** K ≠ H violation | ✅ Mitigated by Track A having no φ | Becomes active when Track B starts Phase 1 |
| **R-3** B(H) target too narrow | 🟠 Carried into Track B Phase 1 | Phase 1 §1 explicitly considers target selection |
| **R-4** §6 re-frame weakening | 🟡 Carried into Track B Phase 3 | Mitigation: keep existing §6 in parallel with new §6.X |
| **R-5** public_documents update | 🟡 Deferred until Track B Phase 4 | No public-document changes in Phase 0 |
| **R-6** Zenodo Working Paper v2.0 DOI | 🟠 Carried | Track A wording is consistent with WP v2.0 §1; no erratum needed for WP v2.0 publish |

---

## 7. EX Compass Note

VVV-QMRF-EX (v1.6 + v1.7 complete) maps K ↔ ρ (registration ↔ density operator). EX does **not** provide φ: K → B(H), because B(H) is the *observable algebra*, not the state ρ. EX intelligence informs Component 4 (interpretation failure analysis via KE-SC node review) but cannot be imported as cargo for Component 2. EX continues to serve as compass for Track B prioritization.

---

## 8. Change Log

| Date | Version | Change |
|------|---------|--------|
| 2026-05-22 | 1.0 | Initial decision document. Track A adopted. CLAUDE.md updated. Track B roadmap created. |
| 2026-05-22 | 2.0 | Track B Phase 4 complete. All C1–C4 ≥ 8/10 (C1: 8.5, C2: 8.0, C3: 8.0, C4: 8.0). CLAUDE.md central claim updated to active φ conjecture (Track B target claim). K_to_BH_Structure_Preserving_Map_v0_1.md v0.2 contains φ definition, N_1–N_T, and EWF consistency check. WP v2.0 §6.1 contains φ-conditional interpretation analysis. Track A wording preserved within the paragraph; E1–E16 list unchanged. |

---

*Track B Phases 1–4 complete as of 2026-05-22. Central claim promoted to Track B target. See [phi_map_track_b_roadmap.md](phi_map_track_b_roadmap.md) for residual open items (φ-O2, φ-O5, φ-O6).*
