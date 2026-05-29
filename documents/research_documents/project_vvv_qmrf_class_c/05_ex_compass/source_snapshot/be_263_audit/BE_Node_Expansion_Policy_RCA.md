Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# BE Node Expansion Policy RCA

## Document Status

| Field | Value |
|---|---|
| Document type | RCA policy / governance plan |
| Scope | Buddhist Epistemology node expansion for BE-QM / VVV-QMRF mapping |
| Decision mode | Hybrid Canonical Extension |
| Default execution | Evidence Layer First |
| Boundary | Structural analogy only; not BE-QM identity and not a new QM law |

---

## 1. RCA Decision

VVV-QMRF should not replace the current 30-node Buddhist Epistemology backbone with all 263 nodes in one step.

The approved RCA decision is:

```text
Do not perform full canonical replacement.
Use Hybrid Canonical Extension.
Start with Evidence Layer First.
Promote individual RCA nodes only through an RCA gate.
Do not add VVV-QMRF postulates beyond E1-E16 unless a new registration-layer function is demonstrated.
```

---

## 2. Fact-Forcing Gate Record

Before this file was created, the following facts were checked:

1. Files and lines that call this new file: none yet. This is a standalone policy document and no existing document currently references or calls it.
2. Existing-file check: `documents/research_documents/**/*Node*Expansion*Policy*RCA*.md` returned no files; `documents/research_documents/**/*policy*.md` returned no files.
3. Data read/write structure: this file does not read or write data files. It defines governance fields only: `Node status`, `Mapping role`, `Bridge ID`, `BE node`, `BE status`, `QM/VVV-QMRF target`, `Relation type`, `Confidence`, `Claim class`, `Boundary`, and `Source`. No date format is required.
4. User instruction quoted verbatim: "thực hiện theo RCA"

---

## 3. Root Cause Analysis

### Symptom

`SYSTEM_Buddhist_Epistemology/system_be_full.md` contains 263 unique BE node codes, while the current BE-QM system mapping primarily uses the 30 core nodes `N_BE_00001` through `N_BE_00030`.

### Cause Chain

1. The mapping layer uses a compact canonical backbone for stability and publication clarity.
2. The full BE SOT also contains line-by-line RCA nodes from `N_BE_00031` through `N_BE_00263`.
3. These RCA nodes provide fine-grained source traceability, but not all of them are stable ontology nodes.
4. Treating every RCA node as canonical would mix source evidence, textual detail, methodological context, and ontology claims.
5. The root cause is the absence of a formal node-expansion policy that separates core backbone nodes from RCA evidence-layer nodes.

### Root Cause

The project has two valid BE node layers, but their roles must remain distinct:

```text
N_BE_00001-N_BE_00030  = core canonical backbone
N_BE_00031-N_BE_00263  = RCA evidence layer by default
```

---

## 4. Node Layer Model

| Layer | Node range | Default status | Role |
|---|---|---|---|
| Layer A | `N_BE_00001`-`N_BE_00030` | core | Stable canonical BE backbone for published mapping and high-level traceability |
| Layer B | `N_BE_00031`-`N_BE_00263` | evidence-only | Fine-grained RCA support, source grounding, audit evidence |
| Layer C | Selected RCA nodes | canonical-extension-candidate | Nodes that may deserve promotion after RCA review |
| Layer D | Promoted RCA nodes | canonical-extension | Official extensions after passing all RCA gates |

---

## 5. Node Status Schema

Each expanded node should receive one status before it is used in bridge, BIAN, or postulate work.

| Status | Meaning | Allowed use |
|---|---|---|
| `core` | Existing canonical node from the 30-node backbone | Published mapping, BIAN, bridge, VVV-QMRF traceability |
| `evidence-only` | RCA detail that supports a claim but is not a canonical ontology node | Citation support, audit trail, source grounding |
| `canonical-extension-candidate` | RCA node that may deserve promotion | Temporary bridge review, RCA audit |
| `canonical-extension` | Promoted node after passing RCA gate | Canonical extension mapping and bridge registry |
| `no-map` | Node has no direct BE-QM / VVV-QMRF relevance | Do not map; may remain source context |
| `deprecated` | Node should not be used for current mapping | Exclude from active bridge and BIAN work |

---

## 6. RCA Promotion Gate

A node from `N_BE_00031` through `N_BE_00263` may be promoted only if all six checks pass.

| Gate | Question | Pass condition |
|---|---|---|
| 1 | Is this a stable BE concept rather than only textual/source detail? | The node has a distinct conceptual role. |
| 2 | Is it non-duplicate with the 30 core nodes? | It is not already fully covered by a core node. |
| 3 | Is it relevant to QM or VVV-QMRF? | It supports a mapping, bridge, BIAN, or registration-layer analysis. |
| 4 | Does it have a clear relation to an existing structure? | It connects to a BIAN, bridge, postulate, or core node. |
| 5 | Is source traceability clear? | It has a source line, source note, or RCA provenance. |
| 6 | Is the boundary explicit? | It remains analogy/support, not BE-QM identity or QM law. |

If any gate fails, the node remains `evidence-only` or `no-map`.

---

## 7. Bridge Registry Schema

Expanded nodes should not be inserted into prose-only mapping without a bridge registry. Use bridge rows to preserve traceability and boundary control.

```markdown
| Bridge ID | BE node | BE status | QM/VVV-QMRF target | Relation type | Confidence | Claim class | Boundary | Source |
|---|---|---|---|---|---|---|---|---|
```

### Relation Types

```text
structural-analogy
functional-parallel
support-evidence
contrast
gap-source
reverse-gap
no-direct-analogue
```

### Confidence Values

```text
strong
medium
weak
evidence-only
no-map
```

### Claim Classes

```text
textual
structural
interpretive
VVV-QMRF-derived
speculative
```

---

## 8. BIAN Impact Rules

Expanded BE nodes may support or refine BIAN analysis, but they do not automatically create new BIAN categories.

For each BIAN, classify RCA node impact as:

| Impact | Meaning | Action |
|---|---|---|
| support-existing | Node supports an existing BIAN | Add as evidence only |
| refine-existing | Node clarifies a BIAN subtype | Add subtype note, not a new BIAN by default |
| new-candidate | Node reveals a distinct structural gap | Mark as BIAN candidate for separate RCA |
| reverse-gap | Node helps identify QM-to-BE asymmetry | Review under reverse-gap rules |
| no-impact | Node does not affect BIAN structure | Do not map |

A new BIAN candidate requires:

```text
clear BE source
+ clear QM absence or reverse asymmetry
+ registration-layer relevance
+ explicit analogy boundary
```

### BIAN SOT Update Blocker

Fact-forcing gate record for this edit:

1. Files that reference this policy: `BE_Node_Expansion_RCA_Audit_Batch_AB.md`, `BE_Node_Expansion_RCA_Audit_Batch_C.md`, `BE_Node_Expansion_RCA_Audit_Batch_D.md`, `BE_Node_Expansion_RCA_Promotion_Gate_Batch_B_Candidates.md`, `BE_Node_Expansion_RCA_Promotion_Gate_Batch_C_Candidates.md`, `BE_QM_Bridge_Registry_Draft_Batch_B_Candidates.md`, and `BE_QM_Bridge_Registry_Consolidated_Draft_Batch_BC.md`.
2. Public functions/classes affected: none. This is a Markdown governance document, not executable code.
3. Data read/write structure: this file does not read or write runtime data. The affected governance fields are `BIAN impact`, `bridge status`, `source-node status`, `no-analogue verification`, `postulate non-impact`, and `main SOT insertion point`. No date format is used.
4. User instruction quoted verbatim: "RCA thêm rule chặn việc này Bridge draft → main BIAN SOT update , thêm ở đâu ?"

A bridge draft must not be promoted directly into the main BIAN SOT.

```text
Bridge draft -> main BIAN SOT update = blocked by default
```

Root cause: a bridge draft records provisional support, analogy, gap-source evidence, or registry routing. It does not by itself prove that a BIAN category is new, changed, or ready for canonical SOT insertion.

Before any bridge-draft evidence can affect the main BIAN SOT, all checks below must pass:

| Gate | Required result |
|---|---|
| Final bridge status | Draft bridge has a final `BR_XXXXX` ID or an approved final bridge decision. |
| Source-node status | BE node status is confirmed as `core`, `canonical-extension`, or explicitly allowed `evidence-only` support. |
| BIAN impact audit | Separate RCA audit classifies the impact as `support-existing`, `refine-existing`, or `new-candidate`. |
| No-analogue verification | The target BIAN still satisfies no-direct-analogue or approved reverse-gap criteria. |
| Postulate non-impact check | The change does not imply automatic E17+ or hidden postulate expansion. |
| Main SOT insertion point | The exact BIAN SOT location and wording are identified before insertion. |

If any gate fails, the bridge evidence remains in the Bridge Registry or as an RCA support note. Do not update the main BIAN SOT.

---

## 9. Postulate Impact Rules

Expanded BE nodes do not automatically increase the VVV-QMRF postulate count beyond E1-E16.

Default rule:

```text
No E17+ by default.
```

A candidate postulate beyond E1-E16 may be proposed only if all five conditions pass:

| Condition | Requirement |
|---|---|
| New function | The node or node cluster identifies a new registration-layer function. |
| Non-duplicate | The function is not already covered by E1-E16. |
| Necessary | Without it, VVV-QMRF cannot describe a required registration event or condition. |
| Bridgeable | The function can be traced through BE source, QM/VVV-QMRF target, and bridge logic. |
| Bounded | It does not claim Buddhist Epistemology proves, solves, or replaces Quantum Measurement. |

If any condition fails, add evidence to an existing postulate or bridge instead of creating a new postulate.

---

## 10. Recommended Audit Batches

Do not audit all 263 nodes as one undifferentiated set. Use batches.

| Batch | Node range | Purpose |
|---|---|---|
| A | `N_BE_00001`-`N_BE_00030` | Confirm current core backbone |
| B | `N_BE_00031`-`N_BE_00080` | First RCA expansion audit |
| C | `N_BE_00081`-`N_BE_00130` | Second RCA expansion audit |
| D | `N_BE_00131`-`N_BE_00180` | Third RCA expansion audit |
| E | `N_BE_00181`-`N_BE_00230` | Fourth RCA expansion audit |
| F | `N_BE_00231`-`N_BE_00263` | Final RCA expansion audit |

Each audit row should include:

```text
node_id
current_type
proposed_status
related_core_node
mapping_relevance
BIAN_relation
postulate_relation
bridge_candidate
RCA_note
```

---

## 11. Verification Checklist

Before any expanded node becomes canonical-extension, verify:

| Check | Required result |
|---|---|
| 30 core nodes remain stable | Pass |
| 39 core BE edges remain stable unless separately audited | Pass |
| Expanded nodes are evidence-only by default | Pass |
| No automatic E17+ is introduced | Pass |
| No new BIAN is introduced without separate RCA | Pass |
| Every promoted node passes the six RCA gates | Pass |
| Every bridge row includes confidence and boundary | Pass |
| Publication-facing documents distinguish core from expanded nodes | Pass |

---

## 12. Non-Claims

This policy does not claim:

1. That all 263 BE nodes are equally canonical.
2. That every BE node has a QM analogue.
3. That Buddhist Epistemology proves or solves Quantum Measurement.
4. That expanded BE nodes create new QM laws, operators, or physical postulates.
5. That VVV-QMRF must add postulates beyond E1-E16.
6. That line-by-line RCA nodes should replace the 30-node backbone without audit.

---

## 13. Recommended Next Step

Use this policy as the contract for a first audit table:

```text
Batch A: N_BE_00001-N_BE_00030
Batch B: N_BE_00031-N_BE_00080
```

The first audit should test the policy rather than promote nodes immediately.
