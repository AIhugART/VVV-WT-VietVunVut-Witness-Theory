# 76 — Time Evolution (Unitarity): Root Cause Analysis

## Document Metadata
- **Concept ID:** 76
- **Concept Name:** Time Evolution (Unitarity)
- **Category:** Dynamics & Time Evolution
- **Source:** Susskind (2014)
- **Mapping:** T5.15 (Causal production relation)
- **Correspondence Type:** Partial
- **Axiom Cluster:** A1 (Deterministic Causal Law) — inter-measurement domain only
- **Verdict:** Mapping confirmed as "Partial." Unitarity is a complete deterministic law — but only between measurements. At every measurement event, unitarity is suspended and replaced by the projection postulate. This suspension is the critical asymmetry: QM has two incompatible dynamical laws, and the boundary between them is undefined.
- **Method:** Line-by-line Root Cause Analysis (RCA)
- **Scope:** Pure epistemology. No religious or metaphysical content.
- **References:**
  - [QM_Measurement_Unified_Concept_Table.md](../../published_documents/QM_Measurement_Unified_Concept_Table.md) — Concept #76
  - [system_axioms_mapping.md](../../mapping/Buddhist_Epistemology_and_Quantum_Measurement_system_axioms_mapping.md) — T5.15
  - [81_Wavefunction_Collapse_ver_01.md](./81_Wavefunction_Collapse_ver_01.md) — Collapse as unitarity violation
  - [93_Copenhagen_Interpretation_ver_01.md](./93_Copenhagen_Interpretation_ver_01.md) — Copenhagen's two-dynamics problem

---

## 1. Source Definition (from QM Concept Table #76)

> "Quantum states evolve via a unitary operator: |Ψ(t)⟩ = U(t)|Ψ(0)⟩ = e^{−iHt/ħ}|Ψ(0)⟩. Unitarity (U†U = I) ensures conservation of probability and distinguishability of states. Information is never lost — the quantum analogue of the classical 'minus-first law.'"

**Source flag:** S (Susskind 2014)

---

## 2. Line-by-Line Decomposition

### Line 1: "Quantum states evolve via a unitary operator: |Ψ(t)⟩ = U(t)|Ψ(0)⟩ = e^{−iHt/ħ}|Ψ(0)⟩"

- **Content:** The Schrödinger equation in operator form. Given initial state |Ψ(0)⟩ and Hamiltonian H, the state at time t is uniquely determined. The evolution is deterministic, linear, and reversible.
- **Epistemic status:** Mathematically exact. One of the most precisely verified laws in physics.
- **Epistemic analysis:** This is a *complete causal law* — given the cause (initial state + Hamiltonian), the effect (final state) is fully determined. No ambiguity, no probability, no hidden parameters. Between measurements, QM is as deterministic as classical mechanics.
- **No gap in this line.** Unitary evolution is internally consistent and empirically verified.

### Line 2: "Unitarity (U†U = I) ensures conservation of probability"

- **Content:** The unitarity condition. The norm of the state vector is preserved under time evolution: ⟨Ψ(t)|Ψ(t)⟩ = ⟨Ψ(0)|Ψ(0)⟩ = 1. Probabilities sum to 1 at all times.
- **Epistemic status:** Necessary mathematical constraint. Without unitarity, probabilities could grow above 1 or fall below 0.
- **Epistemic analysis:** Probability conservation is the formal guarantee that the theory remains internally consistent over time. It is the dynamical analogue of a logical consistency condition: the theory cannot generate contradictions during evolution.
- **Critical observation:** Wavefunction collapse (projection postulate) *violates* unitarity. The projection |ψ⟩ → P̂_k|ψ⟩/√P_k is not a unitary operation: it is nonlinear, stochastic, and irreversible. Therefore, *measurement breaks the conservation law that governs all non-measurement evolution*.

### Line 3: "and distinguishability of states"

- **Content:** Unitarity preserves inner products: ⟨Φ|Ψ⟩ is constant under unitary evolution. Two states that are orthogonal (perfectly distinguishable) at t=0 remain orthogonal at all t. Two states that are non-orthogonal (partially indistinguishable) remain equally indistinguishable.
- **Epistemic analysis:** This is an *information-preservation* law. Unitary evolution cannot create or destroy distinguishability. If you cannot distinguish two states at t=0, you cannot distinguish them at t=1 by dynamics alone.
- **Consequence:** The only way to increase distinguishability is *measurement* — which breaks unitarity. Information gain requires leaving the unitary regime. This connects directly to the information-disturbance trade-off (#27): gaining information costs unitarity.

### Line 4: "Information is never lost"

- **Content:** The no-information-loss principle. Under unitary evolution, the evolution operator is invertible: U⁻¹ = U†. Any state can be uniquely recovered from any later state. The past is fully recoverable from the present.
- **Epistemic status:** Well-defined between measurements. Contested at measurement boundaries (the information paradox in black holes extends this question to gravitational contexts).
- **Epistemic gap identified:** "Information is never lost" is true *between* measurements. *During* measurement, information about the pre-measurement superposition is irreversibly destroyed (the off-diagonal elements of the density matrix in the measurement basis are erased). Measurement is the only process in QM that destroys information.
- **RCA:** The theory contains a law that says information is never lost, and a postulate that describes a process (measurement) that destroys information. These two are formally incompatible. This is the *two-dynamics problem* — the same contradiction identified in #81 (Line 4) and #93 (Line 2).

### Line 5: "the quantum analogue of the classical 'minus-first law'"

- **Content:** Reference to the "minus-first law" (Brown & Uffink, 2001): the time-reversal invariance of fundamental dynamics. In classical mechanics, the equations of motion are reversible. In QM, unitarity serves the same role.
- **Epistemic status:** Correct analogy. Both classical reversibility and quantum unitarity express the same structural property: fundamental dynamics do not have a preferred time direction.
- **Epistemic analysis:** The minus-first law is about *dynamics*, not *thermodynamics*. Thermodynamic irreversibility (entropy increase) is emergent, not fundamental. Similarly, measurement irreversibility (collapse) may be emergent from unitary dynamics — this is the decoherence program's hypothesis (#95). But decoherence does not derive the Born rule or the projection postulate from unitarity; it only derives the appearance of collapse.

---

## 3. The Two-Dynamics Problem

The core epistemic issue with unitarity is not internal to unitarity itself — unitarity is mathematically perfect. The issue is the *coexistence* of unitarity with the projection postulate.

### 3a. The Two Laws

| Property | Unitary Evolution | Projection Postulate |
|---|---|---|
| Deterministic? | Yes | No (stochastic) |
| Linear? | Yes | No (nonlinear) |
| Reversible? | Yes (U⁻¹ = U†) | No (irreversible) |
| Information-preserving? | Yes | No (destroys off-diagonals) |
| Continuous? | Yes | No (instantaneous jump) |
| Domain | Between measurements | During measurement |
| Status in formalism | Axiom (Schrödinger equation) | Axiom (Born rule + projection) |

### 3b. The Boundary Problem

The two laws are formally incompatible. They cannot both be true simultaneously for the same system. Therefore, there must be a boundary — a moment at which the system transitions from one law to the other. This boundary is the **Heisenberg cut** (#94).

The critical question: **What determines the boundary?**

- **Copenhagen:** The boundary is set by the observer's choice of what counts as "apparatus" (classical) vs. "system" (quantum). The cut is subjective and arbitrary.
- **Many-Worlds:** There is no boundary. Unitarity holds universally. Collapse is an illusion (branching).
- **Decoherence:** The boundary is determined by environmental coupling. It is physical but approximate.
- **QM formalism itself:** No answer. The boundary is not specified.

### 3c. Connection to BIAN Gaps

The two-dynamics problem is the *dynamical expression* of the BIAN gaps:

| BIAN | Dynamical Expression |
|---|---|
| BIAN-16 (no completion) | When does unitary evolution stop and projection begin? |
| BIAN-17 (no regress stop) | If the apparatus is quantum, it should evolve unitarily — when does it "collapse"? |
| BIAN-2 (no self-reference) | The system cannot determine which law applies to itself |

---

## 4. The "Partial" Mapping Explained

T5.15 maps unitarity to a *causal production relation* — a deterministic law in which cause fully determines effect. The mapping is rated "Partial" because:

| Feature | Causal Production (T5.15) | Unitary Evolution |
|---|---|---|
| Deterministic | Yes — universally | Yes — between measurements only |
| Suspension | Never suspended | Suspended at every measurement |
| Domain | All epistemic acts | Only inter-measurement dynamics |
| Exceptions | None | Projection postulate |

The critical asymmetry: a universal causal law admits no exceptions. Unitarity admits exceptions at every measurement event. A deterministic law that is suspended at every observation point is not universal determinism — it is conditional determinism, conditioned on the absence of measurement.

---

## 5. Causal Chain (RCA Diagram)

```
OBSERVATION: Unitary evolution is a perfect deterministic law — between measurements.

WHY is it only "between" measurements?
  → Because measurement is described by a different law (projection postulate).
    WHY are there two incompatible laws?
      → Because the formalism has no unified dynamics covering both evolution and measurement.
        WHY is there no unified dynamics?
          → Because measurement requires modeling the observer/apparatus.
            WHY is the observer/apparatus not modeled?
              → Because the formalism has no epistemic architecture for the measuring system.
                → BIAN-2 (no self-referential layer)
                → BIAN-16 (no completion criterion)
                → BIAN-17 (no regress stopper)

ROOT CAUSE: Unitarity is complete within its domain but its domain is artificially
            restricted. The restriction arises because the formalism cannot incorporate
            the measurement act into the same dynamical framework as evolution.
            The two-dynamics problem is a consequence of the absent epistemic architecture.
```

---

## 6. Cross-Reference: Related QM Concepts

| QM # | Name | Relationship to Unitarity |
|---|---|---|
| 2 | Quantum State | The object that evolves unitarily |
| 8 | Four Postulates | Unitarity is Postulate 2; projection is Postulate 4 |
| 14 | Projective Measurement | The non-unitary operation |
| 22 | Post-Measurement State Update | The rule that violates unitarity |
| 23 | Measurement Backaction | The physical consequence of unitarity violation |
| 27 | Info-Disturbance Trade-off | Information gain requires leaving the unitary regime |
| 43 | Measurement Strength κ | Controls the rate of unitarity violation |
| 81 | Wavefunction Collapse | The defining unitarity violation |
| 93 | Copenhagen | Accepts the two-dynamics split as primitive |
| 94 | Heisenberg Cut | The undefined boundary between the two dynamics |
| 95 | Decoherence | Attempts to derive projection from unitarity |
| 102 | Measurement Reversal | Restoring unitarity by erasing information |

---

## 7. Severity Assessment

| Criterion | Rating |
|---|---|
| Internal consistency | Perfect — within its domain |
| Domain completeness | Incomplete — suspended at measurement boundaries |
| Empirical verification | Strongest possible — verified to 12+ significant figures |
| Structural role | Foundational — one of two incompatible axioms |
| Connection to measurement problem | Central — the two-dynamics split IS the measurement problem |

---

## 8. Conclusion

Unitarity is QM's most rigorous law and its most revealing structural constraint. Its perfection *between* measurements and its suspension *during* measurement together constitute the measurement problem in its purest form.

The mapping to a causal production relation (T5.15) is correctly rated "Partial" because a causal production relation is universal — it admits no exceptions. Unitarity is conditional — it admits exceptions at every measurement event. This conditionality is not a flaw of unitarity; it is a flaw of the formalism's inability to incorporate measurement into the same dynamical framework.

**Single-sentence RCA:** Unitarity is restricted to inter-measurement evolution because the formalism that defines it has no endogenous model of the measurement act — the very event that suspends it.

---

*Document version: 01 | Created: 2026-05-10 | Scope: Pure epistemology*
