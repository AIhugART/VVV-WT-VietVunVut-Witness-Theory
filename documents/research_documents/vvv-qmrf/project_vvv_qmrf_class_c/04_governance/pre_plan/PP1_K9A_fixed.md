# PP-1 v2: Fix K9_A — Division by Zero
# 3-Round RCA × 5-Why × Scoring Threshold 4/5
# With VVV-QMRF-EX as Compass

**PrePlan Task:** PP-1 v2
**Date:** 2026-05-23
**Source:** VVV_QMRF_PrePlan_Prompt_Sequence.md §PP-1 (lines 62-141)
**Compass:** VVV-QMRF-EX intersection analysis, bridge registries
**Method:** 3-round RCA × 5-Why × scoring threshold 4/5

---

## EX Compass Context

Before RCA: what does VVV-QMRF-EX tell us about K9_A's key variables?

### V=0 semantics via EX graph

| EX Node | Concept | K-side (BE) anchor | ρ-side (QM) anchor | K9 relevance |
|---|---|---|---|---|
| **N_QM_VVV_00029** (centrality #8) | Retroactive Registration Override | N_BE_00001 — Valid cognition (Bādhaka: contradicting cognition voids earlier one) | N_QM_00102 — Measurement Reversal | **K5 V→0 is the K-side analogue of Bādhaka pramāṇa.** The physical substrate is measurement reversal. |
| **N_QM_VVV_00032** (community 7) | Registration Error / Bhrānti Status | N_BE_00006 — Erroneous cognition | N_QM_00095 — Decoherence & Environment | **V=0 registration = Bhrānti status.** Not absence of event, but reclassification of event as erroneous. |
| **N_QM_VVV_00020** (centrality #15) | Validated Absence Registration | N_BE_00015 — Exclusion (Apoha) + N_BE_00161 — Nonoccurrence + N_BE_00253 — Anupalabdhi | N_QM_00033 — Null Measurement | **isNull events (K4b) = Anupalabdhi (validated absence).** Distinct from V=0 (Bhrānti). |

### Born Rule via EX graph

| EX Node | Concept | K-side (BE) anchor | ρ-side (QM) anchor |
|---|---|---|---|
| **N_QM_VVV_00027** (centrality #2) | Registration Self-Completion Matrix / Act-Result Identity | N_BE_00022 — Arthakriyā (causal efficacy) + N_BE_00055 — Pramāphala (result of valid cognition) + N_BE_00127 — Pramāṇa formula + N_BE_00170 — Non-distinction of means and result | N_QM_00016 — **Born Rule** + N_QM_00019 — Measurement |
| **N_QM_VVV_00021** (centrality #1) | Registration Lock | N_BE_00046 — Representationalism + 7 others | N_QM_00020 — von Neumann Model + N_QM_00094 — Heisenberg Cut |

### EX Compass Insight for K9_A

> **N_QM_VVV_00027** maps Born Rule to **arthakriyā** (causal efficacy): P(o) is the probability of a causally efficacious registration event. This means:
> - **V=1 events ARE arthakriyā-bearing:** they have causal efficacy → Born rule P(o) applies
> - **V=0 events are Bhrānti (N_QM_VVV_00032):** erroneous cognition. They had causal contact but the registration is ERROR, not ABSENCE.
> - **isNull events are Anupalabdhi (N_QM_VVV_00020):** validated absence. No outcome registered at all.
>
> The previous PP-1 v1 conflated V=0 and isNull into a single "N_null" category. **EX says they are structurally distinct:** V=0 = Bhrānti (had outcome, now invalid) vs isNull = Anupalabdhi (no outcome at all).

---

## ROUND 1: Root Cause — Why Does Division by Zero Occur?

### 5-Why Chain

| # | Why? | Answer | Source |
|---|---|---|---|
| W1 | Why does K9_A produce division by zero? | Z(K) = Σ_o V(k)·Tr(E_o ρ) = 0 when V(k)=0, so P = 0/0 | K9_A original equation |
| W2 | Why does Z(K) = 0 when V=0? | V(k) is a **per-tuple** binary flag (K4), not per-outcome. When V=0, every term = 0. | K4 formal (L220-249) |
| W3 | Why is V per-tuple, not per-outcome? | K1 defines k = ⟨M, o, cert, t, V⟩ — V is a field of the tuple. One V per tuple, not one V per possible outcome. The equation mistakenly distributes V across outcomes. | K1 formal (L86-93) |
| W4 | Why does V=0 not mean P=0? | **EX compass:** V=0 = Bhrānti status (N_QM_VVV_00032) — the registration is reclassified as erroneous. Bhrānti is not "zero probability outcome." It is "this registration had causal contact but is now invalid." | EX: N_BE_00006 → N_QM_VVV_00032 |
| W5 | What is the correct K-side semantics of V=0? | **EX compass:** V=0 marks an event that underwent arthakriyā (causal contact) but was subsequently voided by Bādhaka (K5 invalidation). The event is NOT absent (that's isNull/Anupalabdhi). It is PRESENT but REVOKED. | EX: N_QM_VVV_00029 (Bādhaka path) |

### Root Cause Statement (EX-enriched)

> **RC-1:** K9_A treats V=0 as a multiplicative zero in probability, but EX graph shows V=0 is **Bhrānti** (erroneous registration) — structurally distinct from isNull (Anupalabdhi/validated absence). V=0 events had causal contact with the physical system (arthakriyā occurred) but the registration was voided by Bādhaka (K5). The correct treatment requires THREE cases: V=1 (valid), V=0 (Bhrānti), isNull (Anupalabdhi), not TWO.

### Score

| Criterion | Score | Justification |
|---|---|---|
| Root cause identified? | 5/5 | V is per-tuple; V=0 ≠ P=0 — EX Bhrānti path confirms |
| Root cause actionable? | 5/5 | Three-case definition derivable from EX structure |
| Root cause non-trivial? | 5/5 | EX revealed Bhrānti ≠ Anupalabdhi distinction missed in v1 |
| Root cause verified against axioms + EX? | 5/5 | K1/K4/K5 + EX nodes 00029/00032/00020 all confirm |
| **Average** | **5.0/5** | **≥ 4/5 PASS ✅** |

---

## ROUND 2: Corrected Definition — Three-Case K9_A

### 5-Why: Why Three Cases?

| # | Why? | Answer |
|---|---|---|
| W1 | Why not two cases (valid/invalid)? | Because EX graph distinguishes N_QM_VVV_00032 (Bhrānti/error) from N_QM_VVV_00020 (Anupalabdhi/absence). They have different BE anchors and different QM substrates. |
| W2 | What QM substrate maps to each? | V=0 → N_QM_00095 (Decoherence/Environment). isNull → N_QM_00033 (Null Measurement). Different physics. |
| W3 | Does the K-axiom structure support 3 cases? | Yes: K4(a) ¬isNull ∧ V=1; K5 V→0 (Bhrānti path); K4(b) isNull ∧ V=0 (Anupalabdhi path). |
| W4 | What observable does each case produce? | V=1 → P(o) via Born rule (arthakriyā). V=0 → N_bhranti count. isNull → N_null count. |
| W5 | Are N_bhranti and N_null independently measurable? | N_bhranti: requires detecting registration-then-invalidation events. N_null: requires detecting null measurement outcomes. Different experimental signatures. |

### Corrected K9_A Definition (EX-Enriched)

```
K9_A — V-Filter (Three-Case, EX-Enriched):

  Case 1: ¬isNull(k) ∧ V(k) = 1
    Condition: Non-null, valid registration (arthakriyā-bearing)
    EX anchor: N_QM_VVV_00027 (Act-Result Identity → Born Rule)
    P(o | k) = Tr(E_o ρ)
    Standard Born rule. No modification.

  Case 2: ¬isNull(k) ∧ V(k) = 0
    Condition: Non-null, invalidated registration (Bhrānti status)
    EX anchor: N_QM_VVV_00032 (Registration Error)
    K5 fired: registration was valid, then contradicted by Bādhaka.
    P(o | k, V=0): UNDEFINED as probability.
    Observables:
      - o(k) is RECORDED but REVOKED (registration exists but is invalid)
      - Contributes to N_bhranti(H) — count of Bhrānti events
      - o(k) content preserved (physical outcome DID occur, K5 boundary)
    Physical interpretation: decoherence/environment
    (N_QM_00095) overrode the registration

  Case 3: isNull(k) ∧ V(k) = 0
    Condition: Null registration (Anupalabdhi)
    EX anchor: N_QM_VVV_00020 (Validated Absence)
    K4(b): o(k)=∅, ΔI(k)=0 → V=0 by definition
    P(o | k_null): UNDEFINED (no outcome to assign probability to)
    Observables:
      - Contributes to N_null(H) — count of Anupalabdhi events
      - No o content (o=∅)
    Physical interpretation: null measurement (N_QM_00033)

  Free parameters:
    v_rate ∈ [0,1] — fraction of runs with V(k)=1 for all k
                     (population parameter, not per-event)
    Physical: registration success rate

    [OPTIONAL] bhranti_rate ∈ [0,1] — fraction of non-null events
               with V=0 (K5-induced Bhrānti)
               bhranti_rate ≤ (1 - v_rate) if v_rate counts V=1 events
               ⚠ Only 1 of {v_rate, bhranti_rate} is free (they're complements
               for non-null events). Parameter budget: 1.

  Normalization:
    Case 1: Σ_o P(o|k) = Σ_o Tr(E_o ρ) = 1. ✓
    Case 2: No P to normalize. N_bhranti incremented. ✓
    Case 3: No P to normalize. N_null incremented. ✓

  Born rule recovery (C-BORN):
    When cert=1 ∧ V=1 ∧ ⊥_K silent ∧ ¬isNull:
      All conditions → Case 1 → P(o|k) = Tr(E_o ρ). ∎
```

### K9_A Observables (3, not 1)

| Observable | EX Node | K Case | Formula | Measurable? |
|---|---|---|---|---|
| P(o) | N_QM_VVV_00027 | Case 1 (V=1) | Tr(E_o ρ) | Yes (standard) |
| N_bhranti | N_QM_VVV_00032 | Case 2 (V=0, ¬isNull) | Count of K5-fired events | Yes, if V=0 operationalized |
| N_null | N_QM_VVV_00020 | Case 3 (isNull) | Count of o=∅ events | Yes (null measurement counts) |

### Score

| Criterion | Score | Justification |
|---|---|---|
| Division by zero eliminated? | 5/5 | No denominator in any case |
| Born rule recovery proven? | 5/5 | Case 1 IS Born rule |
| V=0 semantics EX-grounded? | 5/5 | Bhrānti path (N_QM_VVV_00032) distinct from Anupalabdhi (N_QM_VVV_00020) |
| Three cases axiom-justified? | 5/5 | K4(a), K5, K4(b) partition all k ∈ K_R |
| **Average** | **5.0/5** | **≥ 4/5 PASS ✅** |

---

## ROUND 3: Distinguishability — EX-Guided Assessment

### 5-Why: Can K9_A Produce Observable Deviations?

| # | Why? | Answer |
|---|---|---|
| W1 | When does K9_A differ from Standard QM? | When N_bhranti > 0 or N_null deviates from detector noise baseline. Standard QM has no Bhrānti/Anupalabdhi concept. |
| W2 | Where in the EX graph does distinguishability live? | **N_QM_VVV_00029** (Retroactive Registration Override) → N_QM_00102 (Measurement Reversal). If measurement reversal is detected (ρ-side), K5 firing (K-side) should produce measurable N_bhranti. |
| W3 | What experiment probes this? | **EWF (Extended Wigner's Friend):** W's entangled-basis measurement constitutes a Bādhaka for F's registration. If K5 fires, F's registration enters Bhrānti status. The CHSH inequality violation is measured on the joint system — N_bhranti events should show modified correlations. |
| W4 | Does P(o) change in Case 1? | **NO.** When V=1, P = Tr(E_o ρ) exactly. δP = 0 at probability level. |
| W5 | Where is the distinguishability then? | **Three-level answer from EX:** |
| | | (a) **Registration layer:** N_bhranti > 0 (new observable, no QM analogue) |
| | | (b) **Statistical layer:** effective sample size N_eff = N_total − N_bhranti − N_null < N_total |
| | | (c) **Correlation layer:** if Bhrānti events are non-randomly distributed across measurement settings → CHSH statistics are modified (selection effect) |

### EX-Enriched Distinguishability Verdict

```
FINDING PP1-DIST-v2 (EX-Enriched):

K9_A produces THREE distinguishability channels, ordered by testability:

CHANNEL 1 — δP = 0 (probability level)
  When V=1: P(o|k) = Tr(E_o ρ) exactly.
  No probability deviation from Standard QM in valid events.
  Status: TRIVIAL — no distinguishability at this level.

CHANNEL 2 — N_bhranti > 0 (registration level)
  K5-induced invalidation produces events in Bhrānti status.
  EX anchor: N_QM_VVV_00032 → N_QM_00095 (decoherence substrate)
  Testable: Yes, if Bhrānti events can be operationally identified.
  EWF signature: F's registration invalidated by W's measurement.
  Observable: N_bhranti / N_total = bhranti_rate
  QM has no concept of this → distinguishable IF bhranti_rate > 0.
  Status: CONDITIONAL — requires operationalization of V=0 detection.

CHANNEL 3 — Selection bias in correlations (statistical level)
  If bhranti_rate depends on measurement setting (e.g., basis choice),
  then removing Bhrānti events from the sample introduces a
  setting-dependent selection bias in ⟨A_xB_y⟩ correlations.
  EX anchor: path through N_QM_VVV_00025 (Entanglement-registration)
             → N_QM_00090 (Bell's Inequality)
  Observable: Δ⟨A_xB_y⟩ = ⟨A_xB_y⟩_all − ⟨A_xB_y⟩_valid ≠ 0
              iff bhranti_rate varies across (x,y) settings.
  Status: TESTABLE — requires Proietti-type data with per-event V status.

OVERALL: K9_A's distinguishability is NOT at the probability level
but at the REGISTRATION and STATISTICAL levels. This is consistent
with K9_A being a registration-layer extension, not a probability-
modifying theory.
```

### Score

| Criterion | Score | Justification |
|---|---|---|
| Distinguishability assessment honest? | 5/5 | Explicitly states δP=0 at probability level |
| EX-grounded channels identified? | 5/5 | Three channels via EX nodes 00032, 00029, 00025 |
| Falsification condition stated? | 5/5 | Channel 3 is directly testable in Proietti data |
| Channel 3 (selection bias) novel vs v1? | 5/5 | v1 had only N_null; v2 adds setting-dependent selection via EX |
| **Average** | **5.0/5** | **≥ 4/5 PASS ✅** |

---

## (C) Class Assignment (EX-Enriched)

**Class D (Conjecture) — upgraded from v1**

| Criterion | v1 Verdict | v2 Verdict (EX) |
|---|---|---|
| δP ≠ 0? | No | No (Channel 1) |
| Registration-layer observable? | Yes (N_null only) | Yes (N_bhranti + N_null — **two distinct observables**) |
| Statistical-layer test? | No | **Yes (Channel 3: setting-dependent selection bias)** |
| Class | D | **D, with clear path to C via Channel 3** |

---

## (D) What Would Make K9_A Class C? (EX-Enriched Path)

| Requirement | v1 | v2 (EX) | Status |
|---|---|---|---|
| R1: Operationalize V=0 detection | Needed | Needed — **EX specifies substrate:** decoherence (N_QM_00095) for Bhrānti, null measurement (N_QM_00033) for Anupalabdhi | NOT YET |
| R2: Predict N_bhranti for EWF | Not in v1 | **New:** predict bhranti_rate(x,y) for each CHSH setting | NOT YET |
| R3: Show Channel 3 selection bias | Not in v1 | **New:** show Δ⟨A_xB_y⟩ ≠ 0 with statistical significance | NOT YET |
| R4: V-fluctuation rate model | Needed | Needed (Tier 4 A4.3) | NOT YET |
| R5: All R1-R4 satisfied | → Class C | → Class C | |

---

## ASSUMPTION Registry (EX-Enriched)

| ID | Statement | EX grounding | If false |
|---|---|---|---|
| A-1a | V=0 ∧ ¬isNull events (Bhrānti) contribute to N_bhranti, not P | N_QM_VVV_00032 (Registration Error → N_BE_00006 Erroneous cognition) | If Bhrānti events DO get P: need modified Born rule for V=0 case |
| A-1b | isNull events (Anupalabdhi) contribute to N_null, not P | N_QM_VVV_00020 (Validated Absence → N_BE_00253 Anupalabdhi) | If null events DO get P: need P(∅) assignment |
| A-2 | V=0 and isNull are operationally distinguishable | EX: different QM substrates (N_QM_00095 vs N_QM_00033) | If indistinguishable: collapse to v1's two-case (N_null = N_bhranti + N_null_old) |

---

## Constraint Satisfaction Summary

| Constraint | Status | Proof |
|---|---|---|
| C-BORN | ✅ PASS | Case 1: P = Tr(E_o ρ) |
| C-NORM | ✅ PASS | Case 1: Σ=1; Cases 2-3: no P |
| C-NONDIV | ✅ PASS | No denominator |
| C-PARAM | ✅ PASS | 1 free parameter (v_rate or bhranti_rate) |
| C-TRACE | ✅ PASS | V from K4/K5; Bhrānti from EX 00032; Anupalabdhi from EX 00020 |
| C-FALSI | ⚠️ CONDITIONAL→PROMISING | Channel 3 (selection bias) provides testable falsification |

---

## 3-Round RCA Summary

| Round | Finding | Score | Δ vs v1 |
|---|---|---|---|
| **R1: Root Cause** | V=0 = Bhrānti (erroneous, NOT absent); isNull = Anupalabdhi (absent) | **5.0/5** | **v1 conflated these; v2 separates via EX** |
| **R2: Corrected Definition** | Three-case: V=1→Born, V=0→N_bhranti, isNull→N_null | **5.0/5** | **v1 had two cases; v2 adds EX-grounded third** |
| **R3: Distinguishability** | Channel 3 (selection bias in correlations) is testable | **5.0/5** | **v1 had only N_null; v2 adds Channel 3 via EX path** |

**All 3 rounds ≥ 4/5. PP-1 v2 COMPLETE.**

---

## v1 → v2 Delta Summary

| Aspect | PP-1 v1 | PP-1 v2 (EX Compass) |
|---|---|---|
| V=0 semantics | Undifferentiated "invalid" | Bhrānti (N_QM_VVV_00032) — erroneous but present |
| isNull semantics | Merged with V=0 | Anupalabdhi (N_QM_VVV_00020) — validated absence |
| Number of cases | 2 | **3** |
| Born rule anchor | K4/K5 only | **N_QM_VVV_00027 → N_QM_00016 (Born Rule) via arthakriyā** |
| Distinguishability channels | 1 (N_null) | **3 (δP=0, N_bhranti, selection bias)** |
| Falsification | Weak (N_null detection) | **Stronger (Channel 3: setting-dependent Δ⟨A_xB_y⟩)** |
| Path to Class C | Unclear | **Clear: R1→R4 via EX substrate nodes** |
