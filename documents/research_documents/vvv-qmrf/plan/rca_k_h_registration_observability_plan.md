Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# RCA Plan: K-H Registration Observability Program

> **Fact-Forcing Gate facts before file creation**
>
> 1. File(s) and line(s) that will call this new file: none at creation time. This is a standalone planning note under `documents/research_documents/vvv-qmrf/plan/` and no existing repository file currently imports, links, or calls it.
> 2. Existing-file check: `Glob` on `documents/research_documents/vvv-qmrf/plan/*.md` returned no Markdown files. No existing file in that folder serves this exact planning purpose.
> 3. Data file behavior: this file does not read or write data files. It is a Markdown planning document only. No data fields, data schema, or date format are introduced.
> 4. User instruction quoted verbatim: "RCA lưu nội dung chat thành C:\Stable_Diffusion\Buddhist_Epistemology_Quantum_Measurement\documents\research_documents\vvv-qmrf\plan tự đặt tên file"
>
> **Status:** Planning note derived from the current RCA discussion.
>
> **Boundary:** This document defines a research path for VVV-QMRF registration-layer observability. It does not claim that VVV-QMRF is a physical law, does not modify the Born rule, and does not replace Standard Quantum Mechanics.

---

## 1. Central RCA Question

**Question:** Can VVV-QMRF use RCA to define a measurable K-H relation and eventually test whether the registration layer has physically observable consequences?

**Short answer:** Not yet as a physical law. VVV-QMRF is ready for a K-H registration-observability research program, but it still lacks a complete physical deviation model, experimental protocol, and falsification pathway.

---

## 2. Root Cause

### Symptom

The current VVV-QMRF model can state:

```text
K_after = U_K(K_before, o)
```

RCA extension note (fix B3):

```text
The signature U_K(K_before, o) is the existing VVV-QMRF core form
(node N_QM_VVV_00023). This plan proposes extending it to
U_K(K_before, o | H) by adding the registration horizon H as a
conditioning parameter. The extension does not replace the core
signature; it adds H as a structured context. The core node table
should be updated to record this extension when (and only when)
HDEF-01 is promoted from candidate lemma to accepted framework
definition.
```

but this does not yet define:

1. what contextual domain constrains the update,
2. when an outcome becomes a registered event,
3. which measurable quantities can test the K-H relation,
4. whether any measurable deviation exists beyond Standard QM or a control model.

### Root Cause

The framework has a strong registration architecture, but it does not yet have a measurement-prediction architecture.

### RCA Fix

Define a staged K-H observability program:

```text
H definition -> K-H interface -> registration completion condition -> operational metrics -> deviation criterion -> falsification protocol
```

---

## 3. Current Readiness Assessment

| Area | Status | RCA verdict |
|---|---:|---|
| Separation of `rho` and `K` | Present | Ready |
| `K_after = U_K(K_before, o)` | Present | Ready |
| S1 pipeline `epsilon(M) -> Lambda -> A -> V_yava` | Present | Ready |
| `V_yava` as registration lock | Present | Ready |
| `H` defined as a formal domain | Missing | Required |
| `phi_H` K-H interface | Missing | Required |
| `Reg(o,H)` registration condition | Candidate only | Needs lemma |
| Measurable metrics | Missing | Required |
| Nonzero deviation `delta_KH` | Missing | Required for physical-law candidate |
| Experimental protocol | Missing | Required |
| Falsification rule | Missing | Required |

**Overall RCA verdict:** VVV-QMRF is not ready to claim physical-law status. It is ready to develop a K-H measurable-registration program.

---

## 4. Definition HDEF-01: Registration Horizon

```text
H := Registration Horizon
```

`H` is the structured registration-layer domain that specifies the contextual, historical, question-framing, and validity conditions under which an outcome `o` is eligible to update `K_before` into `K_after`.

Formal structure:

```text
H = (C, R, Q, V)
```

| Component | Meaning | Role |
|---|---|---|
| `C` | Context conditions | The setup or context in which `o` is read |
| `R` | Record-history constraints | The relevant prior registration history |
| `Q` | Question or hypothesis frame | The question that `o` is answering |
| `V` | Validity constraints | The conditions for registration lock |

Explicit decomposition mapping (fix B1):

When used with the two-gate registration condition (§6.2), the full horizon `H` decomposes as:

```text
H = (H_physics, H_register)
```

where:

```text
H_register = (C, R, Q, V)    ← defined here in HDEF-01
H_physics  = (rho_SA, M, Pi_o, H_A, epsilon_dec, theta_amp,
              N_threshold, tau_stab, epsilon_stab)    ← defined in §13 Gate 1
```

HDEF-01 therefore defines `H_register`. `H_physics` is defined separately in §13 Gate 1 because physical admissibility conditions belong to Standard QM and operational detector criteria, not to VVV-QMRF novelty.

Boundary:

```text
H is not Hilbert space, not Hamiltonian, and not a hidden physical variable.
H belongs to the registration layer unless a separate physical model is supplied.
H_register is VVV-QMRF registration-layer content.
H_physics is Standard QM + operational detector content.
```

---

## 5. KHI-01: K-H Interface Lemma

The simplest safe K-H interface is:

```text
phi_H(o, K_before) = U_K(K_before, o | H) = K_after
```

Meaning:

`phi_H` maps an outcome `o` and a prior registration state `K_before` into `K_after`, under the registration horizon `H`.

Safer type signature:

```text
phi_H: O x K_space -> K_space
```

or, if `H` is explicit:

```text
phi: H_space x O x K_space -> K_space
```

Boundary:

`phi_H` is a registration-layer mapping. It is not a physical collapse equation.

---

## 6. DRC-02: Contextual Registration Completion Lemma

### 6.1 Earlier compact form

Given:

```text
K_after = U_K(K_before, o | H)
```

A compact contextual registration condition can be written as:

```text
Reg(o,H) = 1 iff V_yava(K_after, H) = 1
```

Equivalently:

```text
Reg(o,H) = 1 iff V_yava(U_K(K_before, o | H), H) = 1
```

Meaning:

An outcome `o` becomes a registered event under `H` if and only if the updated K-state is locked as valid by `V_yava` under `H`.

Status:

```text
Candidate lemma, not postulate, not physical law.
```

### 6.2 RCA rewrite: two-gate registration condition

RCA refinement: the compact form above still packs two different kinds of condition into the single symbol `H`. To preserve the boundary between physical admissibility and registration validity, decompose `H` as:

```text
H = (H_physics, H_register)
```

where:

| Component | Role | Boundary |
|---|---|---|
| `H_physics` | Physical admissibility horizon: setup, detector, time window, threshold, and noise/control model | Standard QM and operational detector conditions; not VVV-QMRF novelty |
| `H_register` | Registration horizon: context, record history, question frame, and validity constraints | VVV-QMRF K-side registration layer |

The rewritten condition is:

```text
Reg(o,H) = 1 iff
    Phys(o | H_physics) = 1
    and
    V_yava(U_K(K_before, o | H_register), H_register) = 1
```

Compact form:

```text
Reg(o,H) = Phys(o | H_physics) and Lock_K(o | K_before, H_register)
```

with:

```text
Lock_K(o | K_before, H_register)
:= V_yava(U_K(K_before, o | H_register), H_register) = 1
```

Truth table:

| `Phys(o|H_physics)` | `Lock_K(...)` | `Reg(o,H)` | Meaning |
|---:|---:|---:|---|
| 0 | 0 | 0 | No admissible physical candidate and no valid registration |
| 0 | 1 | 0 | Registration without admissible physical basis; flag as invalid or false registration |
| 1 | 0 | 0 | Admissible physical candidate, but not a registered event |
| 1 | 1 | 1 | Admissible physical candidate becomes a valid registered event |

RCA verdict:

```text
The two-gate rewrite is preferred for future K-H work because it separates
physical admissibility from registration lock. VVV-QMRF adds the registration
gate; it does not replace the physical gate.
```

Boundary statement:

```text
Phys(o|H_physics) determines whether o is an admissible physical candidate
under the measurement setup. Lock_K determines whether that admissible candidate
becomes a valid K-side registered event. VVV-QMRF adds Lock_K; it does not
modify Standard QM probabilities.
```

---

## 7. TIM-01: Registration Latency `tau_reg(H)`

Definition (preferred two-gate form):

```text
tau_reg(H) = t[Lock_K(o | K_before,H_register)=1] - t[Phys(o|H_physics)=1]
```

where:

```text
t_phys     := t[Phys(o | H_physics) = 1]
t_lock_val := t[V_yava(K_after, H_register) = 1]
```

Deprecated compact form (fix B2):

```text
[DEPRECATED — retained for traceability only]
tau_reg(H) = t_lock(H) - t_detect
t_detect := t[D_o = 1]
t_lock(H) := t[V_yava(K_after,H) = 1]
```

Deprecation reason: `D_o=1` (detector click) is not equivalent to `Phys(o|H_physics)=1` (physical admissibility). See §13 Gate 1. The compact form is retained for historical traceability but should not be used in new derivations.

Deprecated earlier compact form:

```text
[DEPRECATED — retained for traceability only]
tau_reg(H) = t[V_yava(U_K(K_before,o|H),H)=1] - t[D_o=1]
```

Meaning:

`tau_reg(H)` measures the time between the detector response and the registration-lock event under `H`.

Null case:

```text
tau_reg(H) = t_lock - t_detect, if D_o=1 and Reg(o,H)=1
tau_reg(H) = infinity or censored, if D_o=1 and Reg(o,H)=0
tau_reg(H) = undefined, if D_o=0
```

Prediction candidate:

```text
delta_tau_KH = E[tau_reg | H_1] - E[tau_reg | H_0]
```

If:

```text
delta_tau_KH != 0
```

then `H` has a measurable effect on registration latency.

Boundary:

`tau_reg(H)` does not modify `p_QM(o) = Tr(E_o rho)`.

---

## 8. NUL-01: Null Registration Rate `N_null(H)`

Definition:

```text
N_null(H) = P(Reg(o,H)=0 | Phys(o|H_physics)=1, H)
```

Earlier detector-response form:

```text
N_null(H) = P(Reg(o,H)=0 | D_o=1, H)
```

Using the two-gate registration condition:

```text
N_null(H) = P(Lock_K(o | K_before,H_register) != 1 | Phys(o|H_physics)=1, H)
```

Earlier compact form:

```text
N_null(H) = P(V_yava(U_K(K_before,o|H),H) != 1 | D_o=1, H)
```

or:

```text
N_null(H) = 1 - P(V_yava(U_K(K_before,o|H),H) = 1 | D_o=1, H)
```

Meaning:

`N_null(H)` measures the rate at which a detector response occurs but no valid registered event is produced under `H`.

Useful subtypes:

```text
N_null(H) = N_no-update(H) + N_no-lock(H) + N_invalidated(H)
```

| Subtype | Meaning |
|---|---|
| `N_no-update` | `Phys(o|H_physics)=1` but no `U_K` update occurs |
| `N_no-lock` | update occurs but `V_yava=0` at initial evaluation |
| `N_invalidated` | registration initially locked (`V_yava=1`) but later invalidated or overridden by E8-style retroactive registration override (`N_QM_VVV_00029`) |

Temporal scope clarification (fix D2):

```text
N_null(H) measures the final registration status after all E8-style
overrides have been applied. N_invalidated counts events that initially
passed Lock_K but were later demoted to Reg(o,H)=0 by retroactive
registration override. The three subtypes are mutually exclusive at
final-status evaluation time and sum to N_null(H).
```

Prediction candidate:

```text
delta_N_KH = N_null(H_1) - N_null(H_0)
```

If:

```text
delta_N_KH != 0
```

then `H` has a measurable effect on null registration rate.

Boundary:

`N_null(H)` is a registration-layer metric, not a claim that Standard QM predicts the wrong outcome probabilities.

---

## 9. COR-01: Conditional K-H Information Criterion

Definition, after the two-gate rewrite:

```text
I(K_after; H_register | o, K_before, H_physics)
```

Meaning:

This measures how much information `H_register` contributes to predicting `K_after` after `o`, `K_before`, and the physical admissibility horizon `H_physics` are already known.

Earlier compact form:

```text
I(K_after; H | o, K_before)
```

Entropy form:

```text
I(K_after; H_register | o, K_before, H_physics)
= H_info(K_after | o, K_before, H_physics)
- H_info(K_after | o, K_before, H_physics, H_register)
```

Criterion:

```text
I(K_after; H_register | o, K_before, H_physics) > 0
```

means `H_register` contributes independent information to `K_after` after physical admissibility has already been controlled.

Equivalent condition:

```text
p(K_after | o,K_before,H_physics,H_register) != p(K_after | o,K_before,H_physics)
```

Falsifying condition:

```text
I(K_after; H_register | o, K_before, H_physics) = 0
```

within statistical uncertainty means `H_register` does not provide independent information about `K_after` in that regime.

Boundary:

This is an information-theoretic registration metric. It does not modify the Born rule and does not create a new physical probability law for `o`.

---

## 10. Deviation Criteria

A registration-layer deviation can be defined as:

```text
delta_X_KH = X_reg(H_1) - X_reg(H_0)
```

where:

```text
X_reg in {tau_reg, N_null, epsilon_reg, I(K_after;H|o,K_before)}
```

Examples:

```text
delta_tau_KH = E[tau_reg | H_1] - E[tau_reg | H_0]
```

```text
delta_N_KH = N_null(H_1) - N_null(H_0)
```

```text
delta_I_KH = I(K_after;H | o,K_before) - I_control(K_after;H | o,K_before)
```

A physical-law candidate would require a much stronger condition:

```text
p_VVV(o | K,H) = p_QM(o) + delta_KH(o)
```

with:

```text
delta_KH(o) != 0
```

and with a clear experimental protocol, numerical prediction, and falsification rule.

---

## 11. Proposed Missing Lemmas and Postulate Candidates

| Code | Name | Type | Purpose | Node traceability (fix F1) |
|---|---|---|---|---|
| `HDEF-01` | Registration Horizon Definition | Definition | Defines `H = (C,R,Q,V)` i.e. `H_register` | Candidate placeholder: extends `N_QM_VVV_00021` (Registration Lock) scope |
| `KHI-01` | K-H Interface Lemma | Lemma | Defines `phi_H(o,K_before)=K_after` | Candidate placeholder: extends `N_QM_VVV_00023` (`V̂_yava`) signature |
| `DRC-02` | Contextual Registration Completion Lemma | Lemma | Defines `Reg(o,H)` | Candidate placeholder: new two-gate condition combining `Phys` + `Lock_K` |
| `TIM-01` | Registration Latency Definition | Operational metric | Defines `tau_reg(H)` | Candidate placeholder: operational metric, no existing VVV node |
| `NUL-01` | Null Registration Rate Definition | Operational metric | Defines `N_null(H)` | Candidate placeholder: operational metric, links to `N_QM_VVV_00036`–`00038` (null registering events) |
| `COR-01` | Conditional K-H Information Criterion | Statistical metric | Defines `I(K_after;H|o,K_before)` | Candidate placeholder: statistical metric, no existing VVV node |
| `DEV-01` | K-H Deviation Criterion | Physical-candidate gate | Defines `delta_X_KH` | Candidate placeholder: physical-candidate gate, no existing VVV node |
| `FAL-01` | Falsification Rule | Scientific boundary | Defines what would make each claim unsupported | Candidate placeholder: scientific boundary, no existing VVV node |

Recommendation:

Do not immediately promote these to E17+ postulates. First define them as derived conditions, lemmas, and operational metrics. Promote only if RCA shows structural necessity inside the core framework.

Node-table integration note (fix F1):

```text
When any of the above items is promoted from candidate lemma to
accepted framework definition, a corresponding placeholder entry
should be created in node_QM_VVV.md with:
  - Node type: "Candidate lemma" or "Operational metric"
  - RCA strength: "Class D planning / not yet structural"
  - Source: this document (rca_k_h_registration_observability_plan.md)
This follows VVV-QMRF-EX boundary control C3: no automatic E17+
postulate creation. Promotion requires explicit RCA gate.
```

---

## 12. Falsification Rules

### TIM-F1

```text
If E[tau_reg | H_1] - E[tau_reg | H_0] = 0 within measurement uncertainty,
after controlling detector latency, software latency, human response delay,
post-selection, noise, and learning effect (observer familiarity bias
between sequential trials), then the K-H latency hypothesis is not
supported.
```

### NUL-F1

```text
If N_null(H_1) - N_null(H_0) = 0 within statistical uncertainty,
after controlling detector threshold, noise, software filtering, post-selection,
and H pre-registration, then the K-H null-registration hypothesis is not supported.
```

### COR-F1

```text
If I(K_after;H | o,K_before) = 0 within statistical uncertainty,
after controlling confounders, sampling bias, and finite-sample mutual
information estimation bias (which scales as O(1/N) and can produce
spurious positive I values at small sample sizes), then H does not
provide independent information about K_after in that regime.
```

---

## 13. RCA Gate Questions Before Next Phase

Before advancing the K-H observability program toward prediction or physical-law-candidate language, three gate questions must be answered. If these questions remain unresolved, the document should not advance beyond planning status.

### Gate 1 — Physical admissibility

`Phys(o | H_physics)=1` must not mean detector click. If it is reduced to:

```text
Phys(o | H_physics)=1 iff D_o=1
```

then the physical gate is only detector response or detector efficiency, which is already handled by Standard QM plus detector modeling. In that case, the two-gate structure collapses into:

```text
Reg = detector worked AND registration locked
```

and it adds no new physical content.

RCA refinement:

```text
Phys(o | H_physics)=1
```

should mean that `o` is an admissible physical macro-record candidate, not merely a detector click. It should be operationalized by physical criteria such as decoherence, amplification, and stability.

Preferred compact definition:

```text
Phys(o | H_physics)=1 iff
    Decoh(o | rho_SA, Pi_o, epsilon_dec)=1
    and
    Ampl(o | H_A, theta_amp, N_threshold)=1
    and
    Stable(o | tau_stab, epsilon_stab)=1
```

where:

```text
H_physics = (rho_SA, M, Pi_o, H_A, epsilon_dec, theta_amp, N_threshold, tau_stab, epsilon_stab)
```

| Component | Meaning |
|---|---|
| `rho_SA` | Joint system-apparatus state |
| `M` | Measurement setting |
| `Pi_o` | Pointer/effect channel associated with outcome `o` |
| `H_A` | Apparatus Hilbert space or effective apparatus state space |
| `epsilon_dec` | Decoherence threshold |
| `theta_amp` | Amplification/distinguishability threshold |
| `N_threshold` | Minimum effective apparatus degrees of freedom or scale threshold |
| `tau_stab` | Minimum persistence time for a macro-record candidate |
| `epsilon_stab` | Maximum allowed instability/error rate |

Decoherence criterion:

```text
Decoh(o)=1 iff max_{i != j} |rho_A^{ij}| < epsilon_dec
```

or, using the joint system-apparatus state:

```text
Decoh(o)=1 iff
|| rho_SA - sum_o Pi_o rho_SA Pi_o ||_off < epsilon_dec
```

Amplification criterion:

```text
Ampl(o)=1 iff
    dim(H_A^eff) > N_threshold
    and
    D(rho_A^o, rho_A^{not-o}) > theta_amp
```

where `D` may be a distinguishability metric such as trace distance.

Stability criterion:

```text
Stable(o)=1 iff
P(record_o(t + tau_stab) = record_o(t)) > 1 - epsilon_stab
```

RCA boundary:

```text
Phys=1 is not detector click. It is the emergence of an admissible physical
macro-record candidate under decoherence, amplification, and stability criteria.
```

Relation to Standard QM:

```text
Phys is still a physical-side admissibility gate. It does not by itself modify
p_QM(o)=Tr(E_o rho). It refines what counts as a physical macro-record candidate
before K-side registration lock.
```

RCA verdict:

```text
The document may not advance if Phys remains equal to D_o=1. Phys must be given
content beyond detector language, otherwise the two-gate structure has no new
physical meaning.
```

### Gate 2 — Nontrivial registration gap

The two-gate model has content only if there are possible cases where:

```text
Phys(o | H_physics)=1
and
Lock_K(o | K_before,H_register)=0
```

Meaning:

A candidate can be physically admissible but still fail to become a registered event.

Practical cases where `Lock_K=0` while `Phys=1`:

| Case | Condition | Meaning |
|---|---|---|
| C1 | Signal below registration threshold | Event is physically admissible, but not strong enough for registration lock |
| C2 | Ambiguous classification | Outcome exists as a candidate, but cannot be classified into a definite `K_after` |
| C3 | Time-window mismatch | Event is physically admissible but outside the accepted registration window |
| C4 | Competing record conflict | Event conflicts with prior record history `R` |
| C5 | Validation failure | Event fails validity constraints `V` |
| C6 | Data corruption or data loss | Physical candidate exists, but registration pipeline loses or corrupts the record |
| C7 | Later invalidation | A provisional record is overridden by E8-style invalidation |
| C8 | Null registration event | Physical candidate exists, but the registering system does not engage |
| C9 | Context mismatch | Event is admissible physically but does not answer the `Q` frame of `H_register` |
| C10 | Multiple-candidate ambiguity | Multiple physical candidates prevent a single definite `K_after` lock |

Operational test:

```text
N_null(H) = P(Lock_K=0 | Phys=1)
```

If:

```text
P(Lock_K=0 | Phys=1) = 0
```

in every relevant regime, then the two-gate model adds no measurable content beyond the physical gate.

RCA verdict:

```text
The document must define a non-empty or at least testable Phys=1, Lock_K=0 region.
Otherwise, K-H observability remains formal but not operationally meaningful.
```

### Gate 3 — Operational lock time

`t_lock` must be operationally defined. It should not be left as a vague moment when an observer knows the result.

VVV-QMRF should distinguish four lock-time candidates:

| Code | Lock time | Meaning | Default status |
|---|---|---|---|
| `t_lock^hw` | Hardware lock | Time when apparatus creates the first stable hardware record | Useful proxy in instrumentation |
| `t_lock^sw` | Software/data lock | Time when the event is written to log, disk, database, or event stream with an ID | Useful proxy in computerized experiments |
| `t_lock^val` | Validation lock | Time when the event passes threshold, filter, coincidence, or validity rule and is committed as valid | Preferred VVV-QMRF default |
| `t_lock^obs` | Observer-access lock | Time when a human observer reads or becomes aware of the result | Not default; use only for human-observer studies |

Preferred VVV-QMRF definition:

```text
t_lock := t_lock^val
```

because `V_yava` corresponds to validated registration lock, not merely detector impact, data storage, or human reading.

Thus:

```text
tau_reg^val(H) = t_lock^val(H_register) - t_phys(H_physics)
```

or:

```text
tau_reg^val(H) = t[V_yava(K_after,H_register)=1] - t[Phys(o|H_physics)=1]
```

RCA boundary:

```text
Photon hit or detector interaction belongs to the physical gate.
Validation or commit belongs to the registration gate.
Observer reading is a later access event unless the experiment explicitly studies human registration.
```

### Gate Summary

| Gate | Must answer | If unresolved |
|---|---|---|
| Gate 1 | What does `Phys(o|H_physics)=1` mean in physical language, not detector language? | `Phys` remains an empty label |
| Gate 2 | When can `Lock_K=0` while `Phys=1`? | Two-gate model has no extra content |
| Gate 3 | Which operational `t_lock` is used? | `tau_reg` is not measurable |

RCA conclusion:

```text
The next phase may begin only after Gate 1, Gate 2, and Gate 3 are answered
with operational definitions. Until then, K-H observability remains a planning
program, not a prediction-ready model.
```

---

## 14. Next Step: Minimal Delayed-Choice Testbed

### 14.1 Verdict

This document is moving in the right direction and is a solid foundation. The next step is not to add more definitions. The next step is to answer the three RCA gate questions in concrete physical language, choose the simplest possible experiment, and test whether the `Lock_K` gate has any observable consequence.

RCA warning:

```text
Do not keep expanding notation unless the expansion increases testability.
```

The immediate next task is:

```text
Choose one minimal experiment, define H_physics, define two H_register contexts,
and measure whether tau_reg differs between those contexts after controls.
```

### 14.2 Proposed simplest experiment

The simplest proposed testbed is a delayed-choice experiment with two different `H_register` contexts.

Goal:

```text
Test whether different H_register contexts produce different tau_reg while
H_physics is held fixed as much as possible.
```

Core prediction:

```text
delta_tau_KH =
E[tau_reg^val | H_register_1]
-
E[tau_reg^val | H_register_0]
```

If:

```text
delta_tau_KH != 0
```

after controlling detector latency, software latency, post-selection, timestamp synchronization, and noise, then this is the first candidate signal that `Lock_K` has an observable registration-layer consequence.

Boundary:

```text
This does not claim retrocausation, Born-rule modification, or physical collapse
modification. Delayed-choice is used only as a minimal testbed for different
registration contexts.
```

### 14.3 Why delayed-choice is a useful first testbed

| Reason | RCA value |
|---|---|
| It naturally separates physical event and later registration context | Fits the two-gate model |
| `H_physics` can be held nearly fixed | Helps isolate `H_register` |
| Two registration contexts can be defined | Allows comparison between context-dependent locks |
| Timestamped records can be used | Makes `tau_reg^val` operational |
| It does not require immediate Born-rule modification | Keeps the first test at registration-observability level |

### 14.4 Two candidate H_register contexts

Example contexts:

```text
H_register_0 = which-path registration context
H_register_1 = erasure/interference registration context
```

| Context | Question frame `Q` | Validity condition `V` | Expected lock type |
|---|---|---|---|
| `H_register_0` | Which path? | Valid path information is available | path-lock |
| `H_register_1` | Interference or erasure relation? | Valid coincidence/sorting relation is available | relation-lock |

RCA boundary:

```text
H_register does not change the photon. It changes the condition under which an
admissible physical candidate is locked into a particular K_after type.
```

### 14.5 Observable

Use validation-lock latency:

```text
tau_reg^val(H_register)
=
t_lock^val(H_register) - t_phys(H_physics)
```

where:

```text
t_lock^val = time when the event passes the registration validity rule and is committed as valid
```

and:

```text
t_phys = time when Phys(o|H_physics)=1 is operationally marked
```

If the experiment cannot directly mark `t_phys`, use the earliest defensible physical-event timestamp and explicitly label it as a proxy.

### 14.6 Gate Resolution Prerequisites (fix D1)

The following prediction (§14.7) is valid only after the three §13 gate questions are resolved for this specific testbed. The required resolutions are:

```text
Gate 1 resolution for this testbed:
  Phys(o | H_physics)=1  :=  a photon pair is detected in coincidence
  within the timing window, with decoherence, amplification, and
  stability criteria met by the BBO source + detector hardware.
  This is NOT merely D_o=1; it includes the physical admissibility
  criteria from §13 Gate 1.

Gate 2 resolution for this testbed:
  Phys=1, Lock_K=0 cases include:
  - C2 (ambiguous classification): photon detected but sorting
    relation unavailable or ambiguous.
  - C3 (time-window mismatch): photon detected outside the
    coincidence window for the chosen H_register.
  - C9 (context mismatch): photon is physically admissible but
    does not match the Q frame of the chosen H_register.
  These cases demonstrate a nontrivial registration gap.

Gate 3 resolution for this testbed:
  t_lock := t_lock^val (validation lock time)
  = time when the event is committed as valid by the coincidence-
    counting electronics and sorting algorithm for the chosen
    H_register context.
  t_phys := earliest defensible physical-event timestamp
  = time of the first detector click in the coincidence pair.
```

RCA status:

```text
The gate resolutions above are preliminary and testbed-specific.
They must be refined when a concrete experimental setup is chosen.
Prediction §14.7 is conditional on these gate resolutions being
operationally instantiated.
```

### 14.7 Prediction

Primary prediction:

```text
Prediction DC-P1:
E[tau_reg^val | H_register_1]
!=
E[tau_reg^val | H_register_0]
```

Directional version, if the erasure/interference context requires more sorting or validation:

```text
E[tau_reg^val | H_register_1]
>
E[tau_reg^val | H_register_0]
```

RCA status:

```text
This is a registration-latency prediction, not a quantum-probability prediction.
```

### 14.8 Required controls

| Control | Purpose |
|---|---|
| Detector latency | Prevents confusing hardware delay with `Lock_K` |
| Software latency | Prevents confusing processing delay with registration theory |
| Timestamp synchronization | Required because `tau_reg` is a timing metric |
| Post-selection bias | Critical in delayed-choice and erasure-style experiments |
| Coincidence window | Required if `H_register_1` depends on sorting or relation-lock |
| Noise threshold | Prevents detector artifacts from entering `Phys=1` |
| Pre-registration of `H_register` | Prevents choosing the registration context after seeing data |

### 14.9 Null Model Definition (fix E1)

To make `delta_tau_KH != 0` meaningful, a null model N0 must be defined against which the VVV-QMRF registration-layer prediction is compared.

```text
Null Model N0 (classical registration-latency model):

tau_reg^N0(H_register) = tau_hardware + tau_software(H_register) + tau_noise

where:
  tau_hardware = fixed detector + electronics latency (same for both contexts)
  tau_software(H_register) = processing latency specific to the sorting
    algorithm used for H_register_0 vs H_register_1
  tau_noise = random noise floor from timestamp jitter
```

N0 predicts:

```text
E[tau_reg^N0 | H_register_1] - E[tau_reg^N0 | H_register_0]
= tau_software(H_register_1) - tau_software(H_register_0)
```

This difference is purely classical: it reflects only the computational cost difference between which-path sorting and erasure/interference sorting.

VVV-QMRF deviation criterion:

```text
delta_tau_KH is meaningful only if:
  |delta_tau_KH_measured - delta_tau_KH_N0| > threshold
where threshold accounts for measurement uncertainty, timestamp
jitter, and finite-sample effects.
```

Falsification integration:

```text
If delta_tau_KH_measured = delta_tau_KH_N0 within uncertainty,
then the registration-layer Lock_K hypothesis adds no observable
consequence beyond classical processing differences in this testbed.
```

Boundary (VVV-QMRF-EX compass C5):

```text
N0 does not modify p_QM(o) = Tr(E_o rho). N0 is a classical
registration-processing model. The comparison tests whether
Lock_K has consequences beyond what classical processing explains,
not whether Born-rule probabilities are changed.
```

### 14.10 Falsification

```text
If
E[tau_reg^val | H_register_1]
-
E[tau_reg^val | H_register_0]
= 0
within uncertainty after controls,
then the Lock_K latency hypothesis is not supported in this experiment.
```

If a nonzero difference remains after controls, the correct claim is only:

```text
Lock_K has a candidate observable registration-layer consequence in this testbed.
```

Not allowed:

```text
Lock_K proves retrocausation.
Lock_K modifies the Born rule.
VVV-QMRF is now a validated physical law.
```

### 14.11 RCA next action

The next document should not add more general definitions. It should instantiate the testbed:

```text
1. Choose one delayed-choice setup.
2. Define H_physics in physical language.
3. Define H_register_0 and H_register_1.
4. Define t_phys and t_lock^val.
5. Define the data table needed for tau_reg.
6. Define controls and falsification.
7. Only then evaluate whether delta_tau_KH is meaningful.
```

---

## 15. Final RCA Verdict

VVV-QMRF currently has enough internal structure to define a K-H measurable-registration program, but it is not ready to claim physical-law status.

Ready now:

```text
HDEF-01
KHI-01
DRC-02
TIM-01
NUL-01
COR-01
```

Not ready yet:

```text
validated physical law
Born-rule modification
Standard QM replacement
```

Next research step:

```text
Write a formal K-H Registration Observability document and trace every definition to E1-E16, S1, and the existing VVV-QMRF framework files.
```
