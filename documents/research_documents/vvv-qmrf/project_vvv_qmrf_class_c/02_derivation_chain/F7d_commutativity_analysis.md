# F7d Global Commutativity Analysis

**Date:** 2026-05-23
**Source:** K_Space_Axiomatization.md v2.1, lines 833-842
**Status:** DEFERRED (see Decision D-T4-BYPASS-01)
**Dependency:** Requires T4-H proof (T4_H_proof_gap_analysis.md) + Level 4 ⊥_K boundary clauses

---

## Problem Statement

F7d states that for T4 (N-observer K_joint construction):

> **Pairwise AdmJoint is NECESSARY but NOT SUFFICIENT for N>2.**
> Global overlap compatibility requires: all embedding paths bringing the same
> K-state into K_joint must produce identical images (M, o, cert, t, V agree).

The concern is that **V dynamics may differ along different embedding paths**
because K5 firing depends on C_K (cross-registration sphere) membership,
which may differ depending on the path taken.

---

## The Commutativity Problem

For N=3 observers F, W, SW:

```
Path 1: k ∈ K_F ──i_FW──→ K_joint(F,W) ──i_{FW,SW}──→ K_joint(F,W,SW)
Path 2: k ∈ K_F ──i_FSW──→ K_joint(F,SW) ──i_{FSW,W}──→ K_joint(F,W,SW)

Commutativity requires:
  i_{FW,SW}(i_FW(k)) = i_{FSW,W}(i_FSW(k))

For M, o, cert, t fields: K8 preserves these → agreement likely.
For V field: K5 may fire differently along different paths!
```

---

## Candidate Counterexample Scenarios

### Scenario CE-1: Asymmetric C_K membership

**Setup:**
- F measures qubit at t₁, registers k_F = ⟨M_F, o_F, 1, t₁, 1⟩
- W measures F's lab at t₂ > t₁, registers k_W = ⟨M_W, o_W, 1, t₂, 1⟩
- SW observes W's lab at t₃ > t₂, registers k_SW = ⟨M_SW, o_SW, 1, t₃, 1⟩

**Path 1:** K_F → K_joint(F,W) → K_joint(F,W,SW)
- At K_joint(F,W): C_K = {k_F, k_W}. If k_W ⊥_K k_F → V(k_F) → 0 via K5.
- k_F enters K_joint(F,W,SW) with V=0.

**Path 2:** K_F → K_joint(F,SW) → K_joint(F,W,SW)
- At K_joint(F,SW): C_K = {k_F, k_SW}. If k_SW does NOT ⊥_K k_F (different measurement basis) → V(k_F) remains 1.
- k_F enters K_joint(F,W,SW) with V=1.

**Result:** V(k_F) = 0 via Path 1, V(k_F) = 1 via Path 2. **COMMUTATIVITY VIOLATED.**

**Analysis:** This counterexample **depends on** whether k_W ⊥_K k_F fires
in isolation (before k_SW is considered). The question is: does the
cross-registration context (C_K) in K_joint(F,W) differ from the context
in K_joint(F,W,SW)?

**Resolution possibility:** If K5 ⊥ test uses ONLY the content of o(k₁), o(k₂)
(not the C_K membership) → same outcome regardless of path. But K5 as written
requires "within shared C_K sphere" (K5 text, K_Space_Axiom L260-265).
C_K membership IS path-dependent → counterexample may be real.

### Scenario CE-2: Temporal ordering ambiguity

**Setup:** Same as CE-1, but with t₂ = t₃ (W and SW measure simultaneously).

- Path 1: K_joint(F,W) processes k_W first → K5 fires on k_F → V(k_F) = 0
- Path 2: K_joint(F,SW) processes k_SW first → K5 silent on k_F → V(k_F) = 1

**Analysis:** K2 requires strict total order within each K_R, but K_joint may
have **partial order** when timestamps from different K_R are incomparable.
If t₂ = t₃ and they're from different K_R, the order in K_joint is undefined.
K5 firing depends on "∃k₂ **later** in order" — undefined for incomparable elements.

**Resolution possibility:** Define K_joint order to resolve ties deterministically
(e.g., by observer index). But this introduces arbitrary ordering that may
affect V outcomes.

### Scenario CE-3: C_K sphere growth

**Setup:**
- K_joint(F,W): C_K contains only {k_F, k_W}
- K_joint(F,W,SW): C_K contains {k_F, k_W, k_SW}

When k_F is embedded from K_joint(F,W) → K_joint(F,W,SW), the C_K sphere
GROWS to include k_SW. If k_SW ⊥_K k_F → V(k_F) may change during
the second embedding, even though it was already "settled" in K_joint(F,W).

**Analysis:** This is not a commutativity problem per se, but a **stability**
problem: does V(k_F) in K_joint(F,W) remain stable when K_joint(F,W) is
embedded into a larger K_joint?

**Resolution possibility:** K8 says embedding preserves V "at time of embedding."
If V(k_F) = 0 in K_joint(F,W), it stays 0 in K_joint(F,W,SW). But if
V(k_F) = 1 in K_joint(F,W) and then k_SW ⊥_K k_F fires in K_joint(F,W,SW),
V(k_F) → 0 post-embedding. This is consistent with K5 (new ⊥ events can
always invalidate) but means the final V depends on what other observers
are included → order of inclusion matters → commutativity threatened.

---

## Proof Scope: What Needs to Be Shown

### IF proving commutativity (F7d holds):

**Sufficient conditions candidate:** K5 firing is **content-determined** —
the ⊥_K test between k₁ and k₂ depends ONLY on:
- o(k₁), o(k₂) (outcomes)
- M(k₁), M(k₂) (measurement acts)
- temporal relation k₁ <_R k₂ or k₂ <_R k₁

And NOT on:
- Which K_joint they meet in
- Which other k₃ are present in C_K
- The path by which k₁ reached K_joint

**Proof structure:**
1. Lemma: K8 preserves o and M → same content regardless of path
2. Lemma: If ⊥_K depends only on content → K5 fires identically on both paths
3. Theorem: V(k) in K_joint is path-independent

**Level 4 dependency:** The ⊥_K boundary clauses (§4.4) define WHAT ⊥_K tests.
If ⊥_K is purely content-based → proof succeeds. If ⊥_K depends on C_K structure
(which observers are present) → proof fails.

### IF finding counterexample (F7d fails for general diagrams):

**Action:** Restrict T4 to **commutative diagrams only**:

> T4 (restricted): K_joint = colimit of diagram D, provided D is a
> **commutative** diagram in C_{K-space} (all parallel paths give same result).

This means T4 applies to diagrams where the observer inclusion order
doesn't matter — e.g., when all pairwise ⊥_K relationships are already
determined before constructing the joint space.

---

## Key Question for Level 4

> Does ⊥_K(k₁, k₂) depend on **which C_K sphere** they share,
> or only on **the content** of k₁ and k₂?

If content-only → F7d provable.
If C_K-dependent → F7d may fail → T4 restricted.

---

## Files to Reference

| File | Relevance |
|---|---|
| K_Space_Axiomatization.md L260-349 | K5 definition and ⊥_K mechanism |
| K_Space_Axiomatization.md L479-540 | K8 cross-space embedding preservation |
| K_Space_Axiomatization.md L833-842 | F7d guard statement |
| vvv_qmrf_meta_architecture_level_4_unfreeze_gate.md | Level 4 ⊥_K boundary clauses |
| T4_H_proof_gap_analysis.md | T4-H proof steps (prerequisite) |
