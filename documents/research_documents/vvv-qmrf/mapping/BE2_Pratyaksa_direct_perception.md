Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# RCA: BE2 / N_BE_00002 — Pratyakṣa as Direct Perception

## 1. Canonical Identification

| Field | Value |
|---|---|
| Short label | BE2 |
| Canonical node code | N_BE_00002 |
| Concept | Pratyakṣa |
| English rendering | Direct perception / non-inferential cognition |
| Vietnamese rendering | Nhận thức trực tiếp / nhận thức không qua suy luận |
| Category | Source of knowledge |
| Framework | Buddhist Epistemology / Pramāṇavāda |
| Ground tradition | Dignāga–Dharmakīrti epistemology |
| Parent node | N_BE_00001 — Pramāṇa |
| Primary object | N_BE_00013 — Svalakṣaṇa |
| Primary exclusion | N_BE_00008 — Vikalpa / Kalpanā |

**Canonical statement:** N_BE_00002 denotes Pratyakṣa, the Buddhist epistemological category of direct perception within the Pramāṇavāda framework. It is classified as a source of knowledge and functions as one of the two primary forms of Pramāṇa, alongside N_BE_00003 — Anumāna.

**Document type:** mapping
---

## 2. RCA Definition

### 2.1 Define — observed issue

**Symptom:** The short diagram label `BE2` can be misunderstood as a framework, a category family, or ordinary perception in general.

**Cause:** The abbreviated label hides the canonical node code, Sanskrit term, category, and internal graph relations.

### 2.2 Trace — 5 Whys

1. **Why does `BE2` look ambiguous?** Because it is a shortened diagram label rather than the canonical node code `N_BE_00002`.
2. **Why does this matter?** Because the project distinguishes node, category, framework, and cross-domain mapping status.
3. **Why can `Pratyakṣa` be misread as ordinary perception?** Because English "perception" often includes interpreted, conceptual, and linguistic recognition.
4. **Why is that wrong in this framework?** Because Dignāga defines Pratyakṣa as cognition free from conceptual construction, not as ordinary interpreted perception.
5. **Why must the definition be constrained?** Because mapping Pratyakṣa directly to a symbolic quantum readout would collapse a non-conceptual epistemic act into a mathematical output.

### 2.3 Isolate — root cause

**Root cause:** `BE2` was used as a shorthand label without explicitly preserving its canonical status as `N_BE_00002 — Pratyakṣa`, a source-of-knowledge node in Buddhist Epistemology whose defining condition is direct, non-inferential, non-conceptual cognition.

### 2.4 Fix — corrected formulation

Use the canonical form when precision is required:

```text
N_BE_00002 — Pratyakṣa / Direct perception
Category: Source of knowledge
Framework: Buddhist Epistemology / Pramāṇavāda
Role: direct, non-inferential cognition free from conceptual construction
```

### 2.5 Verify — root cause removed

The ambiguity is removed if every usage distinguishes:

```text
BE2 = diagram shorthand
N_BE_00002 = canonical node code
Pratyakṣa = concept
Source of knowledge = category
Pramāṇavāda = framework
Eigenvalue readout = QM structural analogue only
```

---

## 3. Formal Epistemic Schema

### 3.1 Minimal schema

```text
BE2 = N_BE_00002 = Pratyakṣa
Pratyakṣa = direct cognition free from kalpanā
```

### 3.2 Expanded condition schema

```text
Pratyakṣa(C, O) is valid if and only if:

1. direct_apprehension(C, O) = true
2. inferential_mediation(C, O) = false
3. conceptual_construction(C, O) = false
4. error_or_deception(C, O) = false
5. object_type(O) = svalakṣaṇa
```

Where:

```text
C = cognitive event
O = object as directly apprehended
svalakṣaṇa = unique, concrete, causally efficacious particular
kalpanā = conceptual construction / linguistic-categorical overlay
```

### 3.3 Compressed formula

```text
N_BE_00002 := Pratyakṣa(C, O)
             ⇔ Direct(C, O) ∧ ¬Inferential(C, O) ∧ ¬Kalpanā(C, O) ∧ ¬Bhrānti(C, O)
```

### 3.4 Object relation formula

```text
N_BE_00002 → N_BE_00013
Pratyakṣa apprehends Svalakṣaṇa
```

### 3.5 Exclusion relation formula

```text
N_BE_00002 → N_BE_00008
Pratyakṣa is free from Kalpanā
```

---

## 4. Graph Relations

| Edge | Relation | Meaning |
|---|---|---|
| ED_BE_00001 | N_BE_00001 → N_BE_00002 | Pramāṇa includes Pratyakṣa |
| ED_BE_00005 | N_BE_00002 → N_BE_00013 | Pratyakṣa apprehends Svalakṣaṇa |
| ED_BE_00038 | N_BE_00002 → N_BE_00008 | Pratyakṣa is free from Vikalpa / Kalpanā |

### Graph expression

```text
N_BE_00001 —includes→ N_BE_00002
N_BE_00002 —apprehends→ N_BE_00013
N_BE_00002 —is free from→ N_BE_00008
```

---

## 5. Relation to the Four Quantum-Mechanics Postulates

Within the four-postulate structure, `N_BE_00002 — Pratyakṣa` is most closely related to the second postulate:

```text
P2: possible measurement results are the eigenvalues of the measured operator.
```

The structural relation is:

```text
P2 → N_BE_00002
Measurement eigenvalue readout structurally parallels Pratyakṣa.
```

### RCA boundary

This relation is not an identity claim.

```text
Pratyakṣa = non-conceptual direct cognition.
Eigenvalue readout = symbolic, mathematically encoded measurement result.
```

Therefore:

```text
P2 functions as a formal measurement-output analogue of BE2, but P2 is not BE2.
```

---

## 6. Scientific English Statement

`N_BE_00002` denotes `Pratyakṣa`, the category of direct perception in Buddhist epistemology. Within the Pramāṇavāda framework, Pratyakṣa is a primary source of valid cognition and is defined as immediate, non-inferential cognition free from conceptual construction (`kalpanā`). Its proper object is the `svalakṣaṇa`, the unique and causally efficacious particular.

In the quantum-measurement mapping, Pratyakṣa can be structurally compared to an eigenvalue readout, because both function as terminal, non-inferential outcome-events within their respective systems. However, the comparison is only structural and functional, not ontological or doctrinal. A quantum eigenvalue is already a symbolic and mathematically encoded result, whereas Pratyakṣa is defined precisely by its freedom from conceptual and linguistic construction. Thus, `P2 → N_BE_00002` should be read as a constrained analogy: the eigenvalue readout plays a Pratyakṣa-like role as the terminal measurement event, but it does not instantiate Pratyakṣa in the strict Buddhist epistemological sense.

---

## 7. Vietnamese Explanation

`BE2` là nhãn ngắn trong diagram. Tên chuẩn là `N_BE_00002 — Pratyakṣa`.

Nói đơn giản:

```text
Pratyakṣa = biết trực tiếp
không qua suy luận
không qua đặt tên
không qua phân loại
không qua diễn giải khái niệm
```

Ví dụ gần đúng:

```text
Thấy một màu đỏ ngay khi nó xuất hiện.
```

Nhưng khi nói:

```text
"Đây là hoa hồng đỏ"
```

thì đã có thêm `kalpanā`, tức "conceptual construction". Vì vậy nó không còn là Pratyakṣa thuần túy theo nghĩa nghiêm ngặt.

Trong mapping với Quantum Measurement, kết quả đo như:

```text
spin = up
energy = 1.2 eV
detector = click
```

có thể được so với `Pratyakṣa` vì nó là kết quả trực tiếp của phép đo. Nhưng nó không đồng nhất với `Pratyakṣa`, vì kết quả lượng tử đã được viết thành số, ký hiệu, hoặc giá trị toán học.

---

## 8. Mermaid Diagram Map

### 8.1 Local Arrow Semantics / Quy ước mũi tên local

This table explains only the arrows used in this diagram. It follows the broader Arrow Semantics rule in `documents/research_documents/vvv-qmrf/schema_guide.md`.

Bảng này chỉ giải thích các mũi tên dùng trong sơ đồ này. Nó tuân theo quy tắc Arrow Semantics rộng hơn trong `documents/research_documents/vvv-qmrf/schema_guide.md`.

| Diagram arrow label | Local meaning | Must not imply |
|---|---|---|
| `includes / ED_BE_00001`, `includes / ED_BE_00002` | Canonical Buddhist Epistemology inclusion edges from the BE SOT. | A Quantum Mechanics relation or a cross-system identity claim. |
| `apprehends / ED_BE_00005`, `is free from / ED_BE_00038`, `operates through / ED_BE_00007`, `requires / ED_BE_00010`, `grounds valid inference` | Internal Buddhist Epistemology node relations or SOT-supported dependency relations. | Physical causation inside Standard Quantum Mechanics. |
| `P2 --> QREAD`, `P4 --> QPRED` | Internal Standard Quantum Mechanics diagram flow from postulate to measurement-output or probability component. | A VVV-QMRF novelty or Buddhist Epistemology equivalence. |
| Dashed QM-to-BE arrows with labels such as `Pratyakṣa-like terminal output` | Structural analogy or bounded mapping between systems. | Identity, proof, or doctrinal equivalence. |
| Dashed arrows to `RCA Boundary` | Boundary guard showing where the analogy must be constrained. | That the boundary is optional. |
| `BOUND --> WARN` | RCA boundary explanation leading to the warning that BE2 and eigenvalue readout differ in kind. | A rejection of the useful structural comparison. |

```mermaid
flowchart TD
    subgraph QM["Quantum Mechanics — Four Postulates"]
        P1["P1<br/>Observable = Hermitian operator"]
        P2["P2<br/>Measurement result = eigenvalue"]
        P3["P3<br/>Distinguishable states = orthogonal vectors"]
        P4["P4<br/>Born rule<br/>P(λᵢ)=|⟨λᵢ|ψ⟩|²"]
    end

    subgraph BE["Buddhist Epistemology — Pramāṇavāda Nodes"]
        BE1["N_BE_00001<br/>Pramāṇa<br/>valid cognition"]
        BE2["N_BE_00002<br/>Pratyakṣa<br/>direct perception"]
        BE3["N_BE_00003<br/>Anumāna<br/>inference"]
        BE5["N_BE_00005<br/>Prameya<br/>object of cognition"]
        BE8["N_BE_00008<br/>Kalpanā / Vikalpa<br/>conceptual construction"]
        BE13["N_BE_00013<br/>Svalakṣaṇa<br/>unique particular"]
        BE15["N_BE_00015<br/>Apoha<br/>exclusion"]
        BE16["N_BE_00016<br/>Liṅga / Hetu<br/>inferential sign"]
        BE19["N_BE_00019<br/>Vyāpti<br/>invariant relation"]
    end

    subgraph RCA["RCA Boundary"]
        BOUND["Structural analogy only<br/>not identity"]
        WARN["BE2 is non-conceptual;<br/>eigenvalue readout is symbolic"]
    end

    QREAD["Eigenvalue readout<br/>symbolic terminal result"]
    QPRED["Predicted outcome probabilities<br/>probabilistic expectation before measurement"]

    BE1 -->|"includes / ED_BE_00001"| BE2
    BE1 -->|"includes / ED_BE_00002"| BE3
    BE2 -->|"apprehends / ED_BE_00005"| BE13
    BE2 -->|"is free from / ED_BE_00038"| BE8
    BE3 -->|"operates through / ED_BE_00007"| BE16
    BE16 -->|"requires / ED_BE_00010"| BE19
    BE19 -->|"grounds valid inference"| BE3

    P1 -. "defines valid measurement instrument" .-> BE1
    P1 -. "selects measurable object" .-> BE5
    P2 --> QREAD
    QREAD -. "Pratyakṣa-like terminal output" .-> BE2
    P3 -. "distinction by exclusion" .-> BE15
    P4 --> QPRED
    P4 -. "probabilistic Vyāpti analogue" .-> BE19
    QPRED -. "enables Anumāna-like prediction" .-> BE3

    QREAD -.-> BOUND
    BOUND --> WARN
```

---

## 9. Final RCA Conclusion

```text
BE2 is not a framework and not a general category label.
BE2 is the diagram shorthand for the canonical node N_BE_00002.
N_BE_00002 denotes Pratyakṣa, direct non-inferential cognition, classified as a Source of Knowledge within the Buddhist Epistemology / Pramāṇavāda framework.
```

The correct cross-domain statement is:

```text
P2 → N_BE_00002
```

meaning:

```text
The eigenvalue readout of quantum measurement plays a Pratyakṣa-like terminal-output role, but only as a structural analogy, because Pratyakṣa is non-conceptual whereas an eigenvalue is already symbolic.
```

---

## What This Mapping Does NOT Claim / Những gì Mapping này KHÔNG tuyên bố

1. This mapping does not claim identity between Buddhist Epistemology and Quantum Measurement.
2. This mapping does not introduce new canonical QM laws, operators, or postulates unless a separate VVV-QMRF framework document explicitly proposes them.
3. This mapping does not claim that Buddhist Epistemology proves or solves Quantum Measurement; it only identifies structural analogies, contrasts, supports, and gaps.
4. `registration-state update` names the VVV-QMRF K-side update; `detector response` remains only the apparatus physical response.

---

## Schema Validation Checklist / Checklist Kiểm chứng Schema

| Check | Status | RCA note |
|---|---|---|
| Document type declared | Pass | Declared as `mapping` for schema alignment. |
| Source traceability | Review required | Add an explicit source corpus before publication reuse. |
| Claim traceability | Review required | Add claim IDs, claim types, source anchors, and boundaries for major claims. |
| Boundary / non-claim guardrail | Pass | Existing boundary/non-claim text limits overclaiming. |
| Validation rule | Pass | Reuse only with source, claim type, and boundary preserved; unresolved items must be marked `TODO(HOTFIX)` before publication use. |
