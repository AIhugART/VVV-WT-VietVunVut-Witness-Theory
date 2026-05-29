Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# VVV-QMRF Working Paper v3.0 — Implementation Plan
# Kế hoạch thực hiện Working Paper v3.0

**Framework:** VietVunVut Quantum Measurement Registration Framework (VVV-QMRF)
**Document type:** `plan / RCA decision record + section map`
**Date:** 2026-05-28
**Plan version:** 1.0
**Author:** VietVunVut (Viet - Nguyen Xuan)
**Status:** Plan only — full draft not yet started; awaiting plan review before drafting.
**Scope:** VVV-QMRF core (Class C qualified). VVV-QMRF-EX used as compass only (no structure import).
**Target file:** `papers/paper_003/VVV-QMRF_Working_Paper_v3.0_draft.md` → promoted to `papers/paper_003/VVV-QMRF_Working_Paper_v3.0.md` after review.

**Source artifacts:**
- v2.0 base: `papers/Testable_Prediction_Section/extended_wigners_friend_k_side_incommensurability/VVV-QMRF_Working_Paper_v2.0.md` (812 lines)
- v3.0 LEGACY structure plan (SUPERSEDED): `papers/Testable_Prediction_Section/extended_wigners_friend_k_side_incommensurability/plan/VVV-QMRF_Working_Paper_v3.0_structure.md` (2026-05-23, φ-centric — outdated relative to v35 index)
- Project Class C index: `documents/research_documents/project_vvv_qmrf_class_c/index.md` (v35, 2026-05-28)
- K-Space SOT (peer-synced): `documents/research_documents/meta_architecture/K_Space_Axiomatization.md` and `documents/research_documents/project_vvv_qmrf_class_c/01_axiomatization/K_Space_Axiomatization.md`
- φ-map (Class D supporting): `documents/research_documents/meta_architecture/K_to_BH_Structure_Preserving_Map_v0_1.md` v0.2
- K9-S12 child paper (arXiv submitted 2026-05-27): `papers/paper_002/manuscript.md`

> **DISCLAIMER:** VVV-QMRF is independent personal research, Class C (qualified) for K9_E hypothesis. Not Standard Quantum Mechanics, not peer-reviewed, not experimentally confirmed. Full boundary protocol carried over to v3.0 §13.

---

## 0. Why a new plan (not the legacy structure plan)

The legacy structure plan dated 2026-05-23 placed the **φ-map (K → B(H)) conjecture** as the central claim from the abstract. Project Class C index v35 (2026-05-28) has since reorganized the framework into three logically independent projects with a one-way motivation chain:

| Project | Type | Status as of v35 |
|---|---|---|
| A | BE↔QM Comparative Mapping | 30 nodes, 39 edges |
| B | VVV-QMRF Conceptual Framework (K1-K8, T1-T9, φ-map) | Layer 1 frozen; φ-map Class D |
| C | K9_E Testable Hypothesis | Class C (qualified); arXiv preprint submitted (paper_002) |

The central claim of v3.0 must reflect the new center of gravity: **K-Space architecture (Project B) plus K9_E testable hypothesis (Project C) plus K9-S12 Modified Bong experimental specification**. The φ-map remains Class D supporting material, not the central claim.

This plan therefore supersedes the legacy structure plan for content decisions but retains its file-organization conventions.

---

## 1. 3-Round RCA × 5-Why × Scoring (Decision Method)

The user's binding rule (`feedback_decision_rule.md`): apply 3-round RCA × 5-Why × scoring threshold 4/5 before meaningful decisions. The decision is whether to draft v3.0 as outlined, and what central claim, section structure, and risk-mitigation protocol to adopt.

### Round 1 — Scope and central question

**5-Why chain:**
1. Why is v3.0 needed? — v2.0 (2026-05-23) does not contain K9_E Class C, K5_prospective axiom upgrade, T4-H THEOREM (4/4), K9-S12 arXiv preprint, BB-VVV/FR-VVV fit plans, or the explicit Project A/B/C separation.
2. Why do these new pieces matter? — They convert VVV-QMRF from "registration-layer interpretive framework" to "testable framework with a submitted preprint and a falsifiable photonic-EWF experimental specification".
3. Why keep the v2.0 title? — The title is a research **question**, not a claim. K9_E, T4-H, K9-S12 are sharper answers to the same question.
4. Why update the central claim but not the title? — Title (question) is durable; claim (answer) progresses with research.
5. Why an explicit 3-project separation? — To preempt the critique "BE-QM mapping is post-hoc justification". Project A→B→C is one-way motivation, not logical derivation. Each project stands or falls on its own.

**Decision:** Keep v2.0 title verbatim. Expand abstract to cover 3-project architecture, K9_E, K9-S12, Class C qualified.
**Score:** 4.5/5 (PASS, threshold ≥4/5).

### Round 2 — New content structure

**5-Why chain:**
1. Why a dedicated K9_E section in v3.0? — K9_E is Project C's central testable claim; a subsection placement would understate it.
2. Why detail K5_prospective + T4-H THEOREM + K7_trace + D_enc? — All are Layer 2 updates since v2.0. K9_E depends on K5_prospective; T4-H THEOREM unlocks the 3-OBS Class C upgrade; K7_trace + D_enc is the canonical Layer 2 element with four consumers.
3. Why include K9-S12 (paper_002)? — It was arXiv-submitted 2026-05-27 and provides a concrete falsification path with Gen LF 1 = +0.0891 at 8.6σ. v3.0 references paper_002 as the experimental child paper.
4. Why dedicated sections for BB and FR fits? — Layer 4 (Class D) empirical-context evidence; FR paradox avoidance via K5 V_prov is a structural achievement independent of K9_E fit data.
5. Why is φ-map no longer the central claim? — Index v35 lists K9_E (Project C) as the central testable claim and φ-map as Class D supporting conjecture (Project B Track B Phase 1-4 complete but not central). The legacy structure plan (φ-centric) is outdated.

**Decision:** v3.0 structure differs from the legacy plan. Central claim = K-Space architecture + K9_E postulate + EWF/K9-S12 testable prediction. φ-map kept as §11 Class D supporting section.
**Score:** 4.7/5 (PASS).

### Round 3 — Risks and boundary protocols

**5-Why chain:**
1. Why stronger Class C disclaimer? — v30 noise sensitivity analysis returned FAIL (noise_threshold = 0.10 σ RMS); K9_E was downgraded from (genuine) to (qualified). v3.0 must be explicit that the empirical evidence is real but ambiguous.
2. Why explicit Project A/B/C separation? — To dispel any "BE-QM mapping as post-hoc justification" critique. Each project is independently falsifiable; a null K9_E result does not invalidate the conceptual framework.
3. Why label K9_E as POSTULATE (P9), not THEOREM? — K1-K8 define structural properties only and do not uniquely determine a probability rule. K9_E is an added postulate, not a derivation.
4. Why close K9E-PAT (multiplicative-pattern open item) as UNRESOLVABLE? — The empirical 2BSM/1BSM ratio of -0.78 is the ratio of two sub-σ residuals (red herring). Both additive (ratio=2.000) and multiplicative (ratio=1.913) models predict roughly 2. Four data points are insufficient to discriminate.
5. Why reject the IBM Quantum approach? — Double category error: K9_E requires K-space registration structure, which is absent on gate-model QPUs. v3.0 must explain why photonic EWF is the only viable confirmation path.

**Decision:** v3.0 must include explicit boundary protocols: (a) Class C qualified disclaimer; (b) 3-project independence statement; (c) K9_E POSTULATE label; (d) IBM-Q rejection rationale; (e) K9-S12 paper reference; (f) Anti-Hallucination Pipeline (AHP) audit footprint.
**Score:** 4.6/5 (PASS).

### Aggregate

| Round | Score | Threshold | Verdict |
|---|---|---|---|
| Round 1 (scope) | 4.5/5 | ≥4/5 | PASS |
| Round 2 (structure) | 4.7/5 | ≥4/5 | PASS |
| Round 3 (risks) | 4.6/5 | ≥4/5 | PASS |
| **Aggregate** | **4.6/5** | **≥4/5** | **PASS** |

Plan approved by RCA. Proceed to delta map and section structure.

---

## 2. Delta v2.0 → v3.0

| # | Delta | Source | Priority |
|---|---|---|---|
| D1 | Project A/B/C separation (one-way motivation chain, not derivational) | Index v35 §1 | HIGH — blocks reviewer critique |
| D2 | Abstract update: K9_E (P9), Class C qualified, 3 projects, K9-S12 arXiv | Index v35 §1, §2 | HIGH |
| D3 | New §4 K-Space Architecture: K1-K8 frozen + K5_prospective + Layer 2 (T1-T9, K7_trace, D_enc) | K_Space_Axiomatization.md v2.4 | HIGH |
| D4 | New §5 K9_E Postulate (P9): equation, 8-term provenance (6/8 NEW), Born limit, distinguishability | Index §3, Phase8_candidate_equation.md | HIGH — heart of v3.0 |
| D5 | New §7 Empirical Status: D1 Proietti genuine fit (β=0.598, 2.31σ), v30 noise sensitivity FAIL, qualified status | Phase10, P10-NOISE | HIGH |
| D6 | New §8 K9-S12 Modified Bong protocol: single QWP α=31°, Gen LF 1 = +0.0891 (8.6σ), reference paper_002 | paper_002 manuscript, K9S12 | HIGH |
| D7 | Update §6 EWF K-side incommensurability — expressed via K-Space axioms (K5_prospective, K7_trace) | v2.0 §4 + K_Space_Axiomatization | MEDIUM |
| D8 | New §9 BB and FR fits: T_BB Class C conditional, V_FR2 PASS, K7_trace as 4-consumer canonical Layer 2 | BB_VVV_fit_plan v1.4, FR_VVV_fit_plan v0.1 | MEDIUM |
| D9 | New §10 T4-H THEOREM (4/4) + 3-Observer prediction Class C: δ_M3 = -0.223 at β=0.3 | T4_H_steps3_4 doc, 3observer_registration_transition.md | MEDIUM |
| D10 | §11 φ Conjecture (Class D supporting, NOT central) | K_to_BH_Structure_Preserving_Map_v0_1.md v0.2 | MEDIUM |
| D11 | Update §12 Positioning + §13 Limitations: φ-conditional analysis (carry from v2.0 §6.1), add IBM-Q rejection | v2.0 §6.1 + v31 RCA | MEDIUM |
| D12 | §7.4 Adversarial Tests + Operationalizability Gates (4/4 + 3/3 PASS) | Phase 9, RCA reports | LOW |
| D13 | Anti-Hallucination Pipeline (AHP) audit footprint (appendix link) | `documents/research_documents/anti_hallucinations/` | LOW |

---

## 3. What v3.0 MUST NOT do (preservation rules)

| Rule | Source |
|---|---|
| Keep the v2.0 title verbatim: "When Does a Physical Interaction Become a Valid Registered Measurement?" | User explicit instruction + CLAUDE.md "extend, not overwrite" |
| Do not claim VVV-QMRF "solves" or "resolves" the quantum measurement problem | CLAUDE.md RULE ZERO (category boundary RCA) |
| Do not invoke consciousness | v2.0 §7.1 |
| Do not revise the Born rule (K9_E reduces to Born exactly at β=0) | Index §3 |
| Do not claim K9_E is experimentally confirmed (Class C qualified, not C genuine) | Index §2 v30 downgrade |
| Do not frame Standard QM as "wrong" or "incomplete" — use "silent on registration architecture" | CLAUDE.md Terminology |
| Do not import VVV-QMRF-EX structure — use only as compass | CLAUDE.md "VVV-QMRF core / EX integration rule" |
| Keep Project A→B→C as one-way motivation chain, not logical derivation | Index v35 §1 |
| Keep `papers/paper_003/` outside `public_documents/` — therefore include author metadata at top of every new file | CLAUDE.md "Document contract rules" |

---

## 4. File plan — `papers/paper_003/`

| File | Path (relative to repo root) | Status | Purpose |
|---|---|---|---|
| Plan (this file) | `papers/paper_003/VVV-QMRF_Working_Paper_v3.0_plan.md` | 2026-05-28 (CURRENT) | RCA decision record + section map |
| Main draft | `papers/paper_003/VVV-QMRF_Working_Paper_v3.0_draft.md` | Not yet started | Working draft |
| Final (after review) | `papers/paper_003/VVV-QMRF_Working_Paper_v3.0.md` | Not yet started | Promoted final |
| CHANGELOG | `papers/paper_003/CHANGELOG.md` | Not yet started | Tracks v2.0 → v3.0 delta |
| README | `papers/paper_003/README.md` | Not yet started | Scope + relationship to v2.0 and paper_002 |

---

## 5. Section structure (proposed)

> Total estimated length: ~14,000-16,000 words (v2.0 was ~12,000). Net new writing ~4,000 words; ~10,000 carry-over with light forward-reference updates.

### Title and subtitle

```
Title (verbatim from v2.0, user-locked):
  When Does a Physical Interaction Become a Valid Registered Measurement?

Subtitle (proposed for v3.0):
  A VVV-QMRF Registration-Layer Framework with the K9_E Class C Testable
  Hypothesis and an Experimental Specification for Extended Wigner's Friend
```

### Abstract (8 paragraphs, ~650 words)

| Para | Content |
|---|---|
| 1 | The registration-layer gap: P3 silent on what counts as a measurement; von Neumann chain; Heisenberg cut. |
| 2 | VVV-QMRF response: K-side registration space K ≠ H; six-condition test for valid registered measurement (carry from v2.0). |
| 3 | K-Space architecture: Layer 1 frozen (K1-K8, including K5_prospective conservative extension), Layer 2 updatable (T1-T9, K7_trace, D_enc canonical). |
| 4 | K9_E Postulate (P9): P(o\|K) = Tr(E_o ρ) · (1 − β·K_ctx). One free parameter β ∈ [0,1]. Born limit at β=0. Six of eight terms are entirely new concepts not present in Standard QM. |
| 5 | EWF application: K_F ⊥_K K_W formal definition chain (carry from v2.0). K9-S12 Modified Bong Protocol predicts Gen LF 1 = +0.0891 (8.6σ), δ⟨A₁B₂⟩ = -0.0355 (20.8σ), FOM=8.6 — submitted to arXiv as paper_002 (2026-05-27). |
| 6 | Empirical status (Class C qualified): D1 Proietti genuine non-circular fit yields β=0.598, V=0.939, Δχ²=5.35 (2.31σ); v30 noise sensitivity analysis returned FAIL (noise_threshold = 0.10 σ RMS); evidence real but ambiguous; confirmation requires dedicated K9-S12 experiment. |
| 7 | **Three logically independent projects (one-way motivation, not logical derivation):** Project A — BE↔QM comparative mapping (30 nodes, 39 edges, interpretive framework). Project B — VVV-QMRF conceptual framework (K1-K8 frozen, T1-T9 bridge theorems, φ-map Class D). Project C — K9_E testable hypothesis (Class C qualified, K9-S12 falsification path). A→B→C is one-way motivation; each project is independently falsifiable. A null K9_E result does not invalidate the framework. |
| 8 | Disclaimer: not SQM; not peer-reviewed; not experimentally confirmed; falsification path via K9-S12 photonic-EWF experiment. Critique invited. |

### Body sections

```
§1. The Registration Layer Gap                            [carry v2.0 §1, ~700w]
    1.1 What Quantum Mechanics specifies (P1-P4)
    1.2 The von Neumann chain problem
    1.3 The Heisenberg cut

§2. The K-side Registration Space                         [carry v2.0 §2 + forward-ref, ~900w]
    2.1 Layer separation (K ≠ H)
    2.2 Minimal K-state
    2.3 Buddhist Pramāṇa source (Project A motivation)
    + forward-ref sentence: "§4 formalizes this minimal K-state as the K1-K8 axiom set."

§3. The Valid Registered Measurement Test                 [carry v2.0 §3 + forward-ref, ~600w]
    3.1 The six conditions
    3.2 The K-side stopping proposition
    3.3 Observer-indexed self-certification
    + forward-ref sentence: "The cert and V fields are formalized as K1 and K4 in §4."

§4. K-Space Architecture: Axioms K1-K8 and Layer 2 ← NEW  [~1,400w]
    4.1 Layer 1 (frozen): K1-K8 (table with name and core function)
    4.2 K5_prospective (v29 conservative extension): same conditions, new evaluation target
    4.3 Layer 2 (updatable): T1-T9 bridge theorems
    4.4 K7_trace + D_enc canonical Layer 2 (v2.4, RCA 4.77/5; four consumers: T_BB + D_enc + 3-OBS + FR)
    4.5 Where does this come from? — Project A (Buddhist Pramāṇa) as one-way motivation, NOT empirical evidence

§5. K9_E: Probability Postulate (P9) ← NEW                [~1,800w — HEART of v3.0]
    5.1 Why K1-K8 alone do not determine a probability rule
    5.2 The K9_E equation: P(o|K) = Tr(E_o ρ) · f_perp(K_ctx); f_perp = 1 − β·K_ctx; β ∈ [0,1]; Born limit at β=0
    5.3 Eight-term provenance (T1-T8): 6/8 entirely NEW, 1 modified (T6), 1 from QM (T1 Born rule)
    5.4 K9_E is a POSTULATE (P9), not a theorem (explicit boundary statement)
    5.5 Distinguishability: δ_S(β=0.5) = −0.055 (theoretical); β=0 ⇒ Born exact
    5.6 Why Project B (φ-map) and Project C (K9_E) are independent claims

§6. Extended Wigner's Friend and K-side Incommensurability [carry v2.0 §4 + update, ~1,800w]
    6.1 The EWF setup (carry v2.0 §4.1)
    6.2 Applying the six conditions per observer (carry v2.0 §4.2)
    6.3 The requires_K_joint predicate (carry v2.0 §4.3)
    6.4 K-side incommensurability formal definition (carry v2.0 §4.4)
    6.5 K_joint failure and Bridge_EWF (carry v2.0 §4.5)
    6.6 ODC_K operational data criterion (carry v2.0 §4.6)
    6.7 NEW: Connection to K1-K8 + K5_prospective (~300w)
        — Show requires_K_joint as K5 firing condition
        — Show Bridge_EWF as K5_prospective evaluation target
        — Cross-reference §4 axiom labels

§7. Empirical Status (Class C Qualified) ← NEW            [~1,200w]
    7.1 D1 Proietti genuine non-circular fit: β=0.598, V=0.939, Δχ²=5.35 (2.31σ)
    7.2 v30 noise sensitivity analysis FAIL: noise_threshold = 0.10 σ RMS (threshold for PASS: >3.0 σ);
        single-setting fragility 1.85σ at A0B0; A0B0 drives 80% of Δχ²
    7.3 K9E-PAT CLOSED as UNRESOLVABLE (v31 RCA 4.92/5): empirical ratio -0.78 is ratio of two sub-σ
        residuals; both additive (ratio=2.000) and multiplicative (ratio=1.913) models predict ~2; four
        data points insufficient
    7.4 Adversarial tests 4/4 PASS + Operationalizability gates 3/3 PASS

§8. K9-S12 Modified Bong Protocol ← NEW                   [~1,000w]
    8.1 Single-QWP design at α=31°
    8.2 Predictions: Gen LF 1 = +0.0891 (8.6σ); δ⟨A₁B₂⟩ = -0.0355 (20.8σ); FOM=8.6
    8.3 Why IBM Quantum was rejected (double category error: K9_E requires K-space registration
        structure, absent on gate-model QPUs)
    8.4 Reference to paper_002 (arXiv submitted 2026-05-27)

§9. Connections to Baumann-Brukner and Frauchiger-Renner ← NEW [~700w]
    9.1 BB (2024) fit plan v1.4: T_BB Class C conditional, P2-C π/8 exact first-principles,
        T_BB' CLOSED (superseded), BB_VVV_compatibility v2.1
    9.2 FR (2018) fit plan v0.1: V_FR2 PASS (2026-05-28); FR paradox AVOIDED via K5 V_prov mechanism;
        K7_trace fourth canonical consumer confirmed
    9.3 K7_trace + D_enc as the canonical Layer 2 element with four consumers

§10. T4-H THEOREM and 3-Observer Prediction ← NEW         [~700w]
    10.1 T4-H Steps 1-4 proven (RCA 4.74/5): Step 1 category proof, Step 2 colimit construction,
         Steps 3-4 T-PRES Lemma + K1-K8 verification + universal property
    10.2 3-OBS upgraded from Class C-conditional to Class C (2026-05-28)
    10.3 Prediction: δ_M3 = -0.223 at β=0.3 (11× amplification, illustrative; conditional only on
         K9_E postulate P9 — T4-H is now THEOREM, no longer conditional dependency)

§11. φ Conjecture: Structure-Preserving Map K → B(H) (Class D Supporting) ← MOVED FROM CENTRAL  [~800w]
    11.1 K → B(H) conjecture (Project B Track B Phase 1-4 complete)
    11.2 Necessary conditions N_1 through N_T derived from K1-K8 and T1-T9
    11.3 K ≠ H boundary reaffirmed: φ maps structure, not ontological identification
    11.4 Open status: existence not proven, sufficiency not shown — Class D supporting only

§12. Positioning Against Existing Interpretations         [carry v2.0 §6 + §6.1, ~1,200w]
    12.1 Architectural comparison table (carry v2.0 §6)
    12.2 φ-conditional scope boundaries (carry v2.0 §6.1, with §11 forward-reference)
    12.3 NEW: Three logically independent projects (~300w):
         Project A independently testable as a comparative-philosophy framework;
         Project B independently testable as a formal axiomatization;
         Project C independently testable via K9-S12 photonic EWF.
         A→B→C is one-way motivation; B→C is conceptual dependency only,
         not logical entailment.

§13. Scope, Limitations, and Open Items                   [carry v2.0 §7 + update, ~1,000w]
    13.1 What this paper does NOT claim (carry + 4 new bullets):
         — Does not claim K9_E experimentally confirmed (Class C qualified)
         — Does not claim φ-map proven to exist (Class D supporting)
         — Does not claim K9_E is the unique probability rule consistent with K1-K8
         — Does not claim 3-observer δ_M3 prediction independent of β value
    13.2 Formal phase summary (carry v2.0 §7.2 + Track B Phase 1-4 + K9_E Phase 7-13)
    13.3 Falsification condition (carry v2.0 §7.3 + K9-S12 explicit reference)
    13.4 Architectural constraints (carry v2.0 §7.4 verbatim — K ≠ H is structural)

References                                                [v2.0 + ~6 new refs]
  Existing v2.0 refs 1-12 (carry)
  + Baumann & Brukner (2024)
  + Reference to paper_002 arXiv preprint (K9-S12)
  + K_Space_Axiomatization.md as internal reference
  + K_to_BH_Structure_Preserving_Map_v0_1.md as internal reference
  + Project Class C index as internal reference
  + Anti-Hallucination Pipeline as internal reference

Appendices (optional):
  A. K9_E reproduction scripts (link to 07_fits/)
  B. K_Space_Axiomatization v2.4 full text (link to peer-sync file)
  C. AHP audit footprint (link to anti_hallucinations/)
```

---

## 6. Writing order (7 phases)

| Phase | Sections | Dependencies | Est. effort |
|---|---|---|---|
| P1 | Skeleton (all section headings) + Abstract draft + §4 (K-Space Architecture) | Read K_Space_Axiomatization v2.4 in full | ~1.5h |
| P2 | §5 (K9_E Postulate — HEART) + §7 (Empirical Status) | Read Phase8_candidate_equation.md, Phase10, P10-NOISE methodology | ~2h |
| P3 | §8 (K9-S12 paper_002) + §10 (T4-H + 3-OBS) | Read papers/paper_002/manuscript.md + T4_H_steps3_4 + 3observer_registration_transition.md | ~1.5h |
| P4 | §9 (BB + FR fits) + §11 (φ-map Class D supporting) | Read BB v2.1 + FR v0.1 + K_to_BH v0.2 | ~1h |
| P5 | Carry-over: §1, §2, §3, §6, §12, §13 with forward-reference updates | Re-read v2.0 sections to be carried | ~1.5h |
| P6 | Abstract finalization + §12.3 (3-project independence) + Disclaimer block | All above done | ~1h |
| P7 | CHANGELOG + README + final formatting + AHP audit footprint | All draft done | ~1h |

Total estimated effort: ~9.5 hours of focused drafting.

Checkpoint protocol: at the end of each phase, save draft and ask user for go/no-go on the next phase. This matches the "Yes, plan file only first" approval (user wants to review before drafting).

---

## 7. Risks and mitigations

| # | Risk | Severity | Mitigation in v3.0 |
|---|---|---|---|
| R1 | Reviewer treats K9_E as confirmed | HIGH | "Class C qualified" badge in abstract; explicit "evidence ambiguous, noise not ruled out" in §7.2 |
| R2 | Reader confuses Project A/B/C dependency | HIGH | §12.3 dedicated subsection + Abstract para 7 + Disclaimer: "K9_E falsifiable independently; null does not invalidate framework" |
| R3 | K9_E mistaken as theorem from K1-K8 | HIGH | §5.4 dedicated boundary: "K9_E is added postulate P9; K1-K8 do not uniquely determine probability rule" |
| R4 | φ-map mistaken as central claim (legacy structure plan bleed-through) | MEDIUM | §11 explicit "Class D supporting, NOT central"; abstract para 4 leads with K9_E, not φ |
| R5 | Title interpretation as "VVV-QMRF answers the question definitively" | MEDIUM | §13.1 bullet: "Does not claim K9_E is the unique answer to the registration-layer question" |
| R6 | Carry-over from v2.0 introduces stale references | MEDIUM | Phase 5 does explicit forward-reference audit on every carried section |
| R7 | AHP non-compliance for new content | MEDIUM | Phase 7 includes AHP audit footprint; every new claim traced to SOT in cross-reference table |
| R8 | K9-S12 paper_002 already submitted — v3.0 must not contradict | LOW | §8.4 references paper_002 manuscript verbatim; cross-check `papers/paper_002/manuscript.md` before P3 |
| R9 | BB-VVV/FR-VVV fit plans not yet frozen | LOW | §9 frames as "current status as of v35 (2026-05-28)"; cites fit-plan version numbers |
| R10 | Plan drift between this file and draft | LOW | Both files maintained in `papers/paper_003/`; CHANGELOG records plan→draft delta |

---

## 8. Constraint compliance check

| Constraint | How v3.0 satisfies |
|---|---|
| CLAUDE.md RULE ZERO (RCA) | 3-Round RCA in §1 of this plan; every new claim in §2 traces to SOT file |
| Extend-not-overwrite | v2.0 file untouched; v3.0 carries forward §1, §2, §3 (six conditions) with forward-reference deltas only |
| Author metadata | `papers/paper_003/` ∉ `public_documents/` and ∉ `published_documents/` → author block at top of every new file |
| K_Space_Axiomatization peer-sync | §4 references both peer files; no structural edits to axiomatization in v3.0 |
| Anti-Hallucination Pipeline | Appendix C audit footprint; every new claim cross-referenced to SOT in trace table |
| Neutral boundary language | "lacks structural machinery for", "registration-layer distinction" — never "wrong/false/error" for SQM |
| Bilingual where appropriate | Body in technically precise English; CHANGELOG bilingual labels; communication with user in Vietnamese (this plan section labels include Vietnamese translations) |
| VVV-QMRF-EX as compass only | §13.2 references EX intelligence; no EX structure import |
| Use `/rca-scientific-paper` skill | If user requests deep RCA on a specific claim during drafting, invoke that skill |
| BIAN naming for new QM concept nodes | No new BIAN-XX nodes introduced in v3.0 (existing only) |
| Five-digit BE node/edge codes | No BE node/edge revisions in v3.0; carry-over only |

---

## 9. Estimated complexity: **MEDIUM-HIGH**

- New writing: ~4,000 words across 5 new sections (§4, §5, §7, §8, §9, §10)
- Carry-over: ~10,000 words from v2.0 with light edits
- Cross-references: ~40 file links to `documents/research_documents/`
- Total effort: ~9.5 hours focused drafting (P1-P7)
- Risk profile: mostly framing/disclaimer risks (all mitigated by explicit boundary statements per §7 above)

---

## 10. Next step (gated)

Per user instruction "Yes, but plan file only first", this plan file is the deliverable. The draft itself is NOT yet started. Awaiting user review of this plan.

Once user approves drafting, the writing order is P1 → P7 with a checkpoint at the end of each phase.

---

## 11. Change log

| Date | Plan version | Change |
|---|---|---|
| 2026-05-28 | 1.0 | Initial plan. 3-Round RCA passed (aggregate 4.6/5). 13 deltas mapped. 13-section structure with line budgets. 7-phase writing order. 10 risks identified and mitigated. Project A/B/C explicit in abstract per user direction. φ-map kept as §11 Class D supporting per user direction. |

---

© 2026 VietVunVut (Viet - Nguyen Xuan). Licensed under CC BY 4.0.
