Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# BE Node Expansion RCA Audit — Batch D

## Document Status

| Field | Value |
|---|---|
| Document type | RCA audit table |
| Parent policy | `BE_Node_Expansion_Policy_RCA.md` |
| Prior audits | `BE_Node_Expansion_RCA_Audit_Batch_AB.md`; `BE_Node_Expansion_RCA_Audit_Batch_C.md`; `BE_QM_Bridge_Registry_Consolidated_Draft_Batch_BC.md` |
| Scope | Batch D `N_BE_00131`-`N_BE_00180` |
| Execution mode | Evidence Layer First |
| Boundary | Structural analogy only; no BE-QM identity; no new QM law; no automatic E17+ |

---

## 1. Fact-Forcing Gate Record

Before this file was created, the following facts were checked:

1. Files and lines that call this new file: none yet. This Batch D audit is standalone and should not be treated as active mapping SOT until reviewed.
2. Existing-file check: `documents/research_documents/vvv-qmrf/*Batch_D*` returned no files; search for `BE_Node_Expansion_RCA_Audit_Batch_D` returned no matches.
3. Data read/write structure: this file does not read or write runtime data. It defines audit fields only: `node_id`, `current_type`, `proposed_status`, `related_core_node`, `mapping_relevance`, `BIAN_relation`, `postulate_relation`, `bridge_candidate`, and `RCA_note`. No date format is required.
4. User instruction quoted verbatim: "làm theo RCA"

---

## 2. RCA Purpose

This audit applies the Evidence Layer First policy to Batch D nodes from `N_BE_00131` through `N_BE_00180`.

The goal is triage, not promotion. Nodes may be marked `canonical-extension-candidate` only when they have clear, bounded BE-QM / VVV-QMRF relevance and are not already fully covered by the 30 core nodes.

---

## 3. Batch D RCA Audit Table

| Node | Current type | Proposed status | Related core node | Mapping relevance | BIAN relation | Postulate relation | Bridge candidate | RCA note |
|---|---|---|---|---|---|---|---|---|
| N_BE_00131 | RCA | evidence-only | N_BE_00002 / N_BE_00010 | medium | perception-scope context | existing E support only | possible | Laukika perception may support ordinary perception boundaries, but it is mostly covered by Pratyaksa and mental perception nodes. |
| N_BE_00132 | RCA | evidence-only | N_BE_00002 / N_BE_00010 | medium | BIAN-3 context | existing E support only | possible | Alaukika perception may contextualize non-ordinary perception, but it carries scope risk and should remain evidence-only. |
| N_BE_00133 | RCA | evidence-only | N_BE_00001 / N_BE_00010 | medium | cognition context | existing E support only | possible | Jnana is too broad as cognition/knowledge; use only as support for pramana and perception analysis. |
| N_BE_00134 | RCA | evidence-only | N_BE_00001 / N_BE_00018 | medium | validity-theory context | existing E support only | possible | Pramanyavada supports validity theory, but it is broad and overlaps with Pramana and Svatah-pramanya. |
| N_BE_00135 | RCA | evidence-only | N_BE_00022 | high | pragmatic validity support | existing E support only | possible | Arthakriya duplicates the core pragmatic validity node; retain as source evidence rather than split. |
| N_BE_00136 | RCA | evidence-only | N_BE_00022 / N_BE_00001 | medium | method support | no automatic E impact | possible | Gold-testing method supports verification discipline, but it is methodological rather than a direct registration-layer structure. |
| N_BE_00137 | RCA | evidence-only | N_BE_00028 | medium | uncertainty context | existing E support only | possible | Samsaya may support doubt/uncertainty discussion, but it does not by itself create a distinct measurement bridge. |
| N_BE_00138 | RCA | evidence-only | N_BE_00028 / N_BE_00001 | low | inquiry context | no automatic E impact | no | Jijnasa is inquiry motivation; it belongs to epistemic method context, not direct BE-QM mapping. |
| N_BE_00139 | RCA | evidence-only | N_BE_00025 / N_BE_00026 | medium | ontology boundary support | no automatic E impact | possible | Paramarthasat or dravyasat is metaphysics-sensitive; keep as boundary evidence only. |
| N_BE_00140 | RCA | evidence-only | N_BE_00026 | medium | conventionality support | no automatic E impact | possible | Samvrtisat or prajnaptisat supports conventional-level language but should not become QM ontology. |
| N_BE_00141 | RCA | evidence-only | N_BE_00026 | medium | conventionality support | no automatic E impact | possible | Conventionally real supports boundary vocabulary for mapping claims, not a new bridge. |
| N_BE_00142 | RCA | evidence-only | N_BE_00025 | medium | ontology boundary support | no automatic E impact | possible | Rigorously real is too metaphysical for direct mapping; use only as scope boundary evidence. |
| N_BE_00143 | RCA | evidence-only | N_BE_00018 / N_BE_00019 | medium | inference context | existing E support only | possible | Inference in Indian logic is broad and covered by Anumana and Vyapti; retain as source evidence. |
| N_BE_00144 | RCA | no-map | none | low | none | none | no | Nyaya-Vaisesika categories are comparative-system context, not a direct Buddhist Epistemology bridge. |
| N_BE_00145 | RCA | evidence-only | N_BE_00005 / N_BE_00025 | low | ontology contrast | no automatic E impact | no | Dravya is category ontology context; avoid treating substance as a QM entity. |
| N_BE_00146 | RCA | evidence-only | N_BE_00005 | low | ontology contrast | no automatic E impact | no | Guna is property-category context, not direct registration architecture. |
| N_BE_00147 | RCA | evidence-only | N_BE_00022 / N_BE_00029 | low | action/process context | no automatic E impact | no | Karma as category/action context is too broad and should not be mapped to physical dynamics. |
| N_BE_00148 | RCA | evidence-only | N_BE_00014 / N_BE_00015 | medium | universals/exclusion context | existing E support only | possible | Samanya supports universal/general concept discussion, but core Samanyalaksana and Apoha already cover the mapping use. |
| N_BE_00149 | RCA | evidence-only | N_BE_00013 / N_BE_00005 | medium | particularity context | existing E support only | possible | Visesa may support particularity contrast, but core Svalaksana already carries the mapping role. |
| N_BE_00150 | RCA | evidence-only | N_BE_00019 / N_BE_00021 | low | relation context | no automatic E impact | no | Samavaya is inherence-category context; it should not be imported as a BE-QM relation. |
| N_BE_00151 | RCA | canonical-extension-candidate | N_BE_00024 | high | BIAN-18 support | existing E support only | possible | Abhava is distinct enough to refine absence/non-occurrence cognition and null-event analysis while remaining support-only. |
| N_BE_00152 | RCA | evidence-only | N_BE_00018 / N_BE_00019 | medium | analogy-method context | no automatic E impact | possible | Argument from analogy is method context; useful for bridge governance, not a direct BE-QM concept node. |
| N_BE_00153 | RCA | evidence-only | N_BE_00018 | medium | inference-structure support | existing E support only | possible | Pratijna supports inference format, but it is a component of broader inferential structure. |
| N_BE_00154 | RCA | evidence-only | N_BE_00018 | medium | inference-structure support | existing E support only | possible | Paksa supports subject-of-inference structure, but it remains a component-level support node. |
| N_BE_00155 | RCA | evidence-only | N_BE_00018 | medium | inference-structure support | existing E support only | possible | Sadhya or sadhyadharma supports probandum structure, but it is not a separate measurement bridge. |
| N_BE_00156 | RCA | evidence-only | N_BE_00018 / N_BE_00021 | high | BIAN-14 support | existing E support only | possible | Hetu or linga is important evidence-marker support but largely overlaps with inference and svabhavapratibandha logic. |
| N_BE_00157 | RCA | evidence-only | N_BE_00018 / N_BE_00019 | medium | inference-structure support | existing E support only | possible | Drstanta supports example-based inference but remains a component of the inference system. |
| N_BE_00158 | RCA | canonical-extension-candidate | N_BE_00018 / N_BE_00019 | high | BIAN-14 support | existing E support only | possible | Tri-rupa-hetu is a distinct three-condition inferential validity structure relevant to tripartite measurement validity analysis. |
| N_BE_00159 | RCA | evidence-only | N_BE_00018 | high | inference context | existing E support only | possible | Anumana-epistemology is broad and duplicates core Anumana; use as source evidence. |
| N_BE_00160 | RCA | evidence-only | N_BE_00020 / N_BE_00019 | high | bridge-rule support | existing E support only | possible | Avinabhava definition refines necessary relation evidence but duplicates the core necessary-relation node. |
| N_BE_00161 | RCA | canonical-extension-candidate | N_BE_00024 / N_BE_00019 | high | BIAN-15 / BIAN-18 support | existing E support only | possible | Nonoccurrence condition is distinct for negative evidence and null-event analysis; candidate status is bounded to support logic only. |
| N_BE_00162 | RCA | no-map | none | low | source provenance | no automatic E impact | no | Pramanasamuccaya is a text/source node; use for provenance, not direct mapping. |
| N_BE_00163 | RCA | evidence-only | N_BE_00001 | medium | pramana context | existing E support only | possible | Pramana and samuccaya clarifies source framing but does not split from core Pramana. |
| N_BE_00164 | RCA | canonical-extension-candidate | N_BE_00001 / N_BE_00005 | high | BIAN-16 support | existing E support only | possible | Pramanadhina prameyadhigama directly refines dependence of object-known on means of knowing, relevant to registration completion analysis. |
| N_BE_00165 | RCA | canonical-extension-candidate | N_BE_00001 / N_BE_00005 | high | BIAN-16 support | existing E support only | possible | Prameyadhina pramanasiddhi directly refines dependence of means-validity on object-domain, relevant to reciprocal registration analysis. |
| N_BE_00166 | RCA | evidence-only | N_BE_00001 | high | pramana-system context | existing E support only | possible | Pramanavyavastha is system-level arrangement of pramana; important context but too broad for direct bridge status. |
| N_BE_00167 | RCA | evidence-only | N_BE_00002 / N_BE_00008 | high | non-conceptual perception support | existing E support only | possible | Kalpanapodha duplicates core non-conceptual perception and exclusion of construction; retain as source evidence. |
| N_BE_00168 | RCA | evidence-only | N_BE_00013 | high | particularity support | existing E support only | possible | Svalaksana duplicates core particular; use as source evidence only unless later bridge needs finer wording. |
| N_BE_00169 | RCA | evidence-only | N_BE_00014 | high | conceptual-general support | existing E support only | possible | Samanyalaksana duplicates core generality/conceptual-object node; keep evidence-only. |
| N_BE_00170 | RCA | canonical-extension-candidate | N_BE_00001 / N_BE_00055 | high | BIAN-16 support | existing E support only | possible | Non-distinction of means and result is distinct and directly relevant to measurement self-completion and pramana-phala analysis. |
| N_BE_00171 | RCA | canonical-extension-candidate | N_BE_00010 / N_BE_00029 | high | BIAN-4 / BIAN-8 support | existing E support only | possible | Sautrantika cognitive process gives a bounded process model for cognition and representation, useful for registration-sequence review. |
| N_BE_00172 | RCA | evidence-only | N_BE_00029 | high | BIAN-8 support | existing E support only | possible | Utpatti and vinasa simultaneity refines momentariness, but core Ksanikavada already carries temporal discontinuity support. |
| N_BE_00173 | RCA | canonical-extension-candidate | N_BE_00005 / N_BE_00010 | high | BIAN-4 support | existing E support only | possible | Bahyartha is distinct for external-object status in representational analysis; candidate status must remain anti-identity and support-only. |
| N_BE_00174 | RCA | evidence-only | N_BE_00010 / N_BE_00011 | high | cognition/self-awareness support | existing E support only | possible | Samvedana is important cognition evidence but overlaps with mental perception and self-awareness nodes. |
| N_BE_00175 | RCA | canonical-extension-candidate | N_BE_00010 / N_BE_00005 | high | BIAN-4 support | existing E support only | possible | Sarupya directly refines cognitive resemblance/form-bearing, relevant to internal representation and encoding analysis. |
| N_BE_00176 | RCA | evidence-only | N_BE_00008 | high | conceptual construction support | existing E support only | possible | Kalpana duplicates the core conceptual construction node; retain as source evidence. |
| N_BE_00177 | RCA | evidence-only | N_BE_00026 | medium | convention boundary support | no automatic E impact | possible | Tathya-samvrti supports accurate conventionality but should remain boundary vocabulary, not QM ontology. |
| N_BE_00178 | RCA | evidence-only | N_BE_00026 | medium | convention boundary support | no automatic E impact | possible | Mithya-samvrti supports inaccurate conventionality; use as interpretive boundary evidence only. |
| N_BE_00179 | RCA | canonical-extension-candidate | N_BE_00010 / N_BE_00046 | high | BIAN-4 support | existing E support only | possible | Representative perception is a distinct representation-side candidate for BIAN-4, but must not be treated as a QM formalism. |
| N_BE_00180 | RCA | evidence-only | N_BE_00010 / N_BE_00025 | medium | mind-only boundary context | no automatic E impact | possible | Vijnaptimatra is metaphysics-sensitive; useful for representation-boundary context only, not direct QM ontology. |

---

## 4. Batch D RCA Result

Batch D contains many inference-structure, ontology-category, and representation-process nodes. The RCA result keeps the Evidence Layer First rule: most nodes remain `evidence-only` or `no-map`, while only narrowly bounded nodes become candidates for later gate review.

Candidate nodes for later RCA gate review:

```text
N_BE_00151  Abhava
N_BE_00158  Tri-rupa-hetu
N_BE_00161  Nonoccurrence condition
N_BE_00164  Pramanadhina prameyadhigama
N_BE_00165  Prameyadhina pramanasiddhi
N_BE_00170  Non-distinction of means and result
N_BE_00171  Sautrantika cognitive process
N_BE_00173  Bahyartha
N_BE_00175  Sarupya
N_BE_00179  Representative perception
```

These are candidates only. None is promoted by this audit.

---

## 5. RCA 5 Whys Summary

### Why are only 10 of 50 Batch D nodes marked as candidates?

1. Why not promote all Batch D nodes? Because full promotion would violate Evidence Layer First and collapse source context into canonical mapping structure.
2. Why would that be a problem? Because many Batch D nodes are broad, duplicate, textual, comparative, or metaphysics-sensitive.
3. Why does duplication matter? Because the 30 core nodes already cover major roles such as Pramana, Pratyaksa, Anumana, Svalaksana, Samanyalaksana, Kalpana, Arthakriya, Ksanikavada, and Samvrti-satya.
4. Why keep any candidates at all? Because some nodes isolate distinct registration-relevant substructures: absence/nonoccurrence, three-condition validity, reciprocal pramana-prameya dependency, representation process, external-object status, resemblance, and representative perception.
5. Root cause: Batch D has high source richness but mixed structural specificity; only nodes with bounded, non-duplicate, BIAN-relevant function should proceed to gate review.

RCA decision: keep 40 nodes outside promotion and send 10 nodes to a later promotion-gate mini-audit.

---

## 6. Verification

| Check | Result | RCA note |
|---|---|---|
| Evidence Layer First preserved | Pass | Most Batch D nodes remain evidence-only or no-map. |
| No full canonical replacement | Pass | No Batch D node becomes final canonical-extension. |
| No automatic E17+ | Pass | No new registration-layer postulate is proposed. |
| BIAN impact controlled | Pass | BIAN mentions are support/refinement only. |
| Boundary preserved | Pass | Ontology and comparative-system nodes remain evidence-only/no-map. |
| Bridge draft deferred | Pass | Candidate nodes require promotion-gate mini-audit first. |
| B/C bridge registry unchanged | Pass | Consolidated B/C bridge rows remain draft and are not finalized here. |

---

## 7. Recommended Next RCA Step

Run a promotion-gate mini-audit for the ten Batch D candidates:

```text
N_BE_00151
N_BE_00158
N_BE_00161
N_BE_00164
N_BE_00165
N_BE_00170
N_BE_00171
N_BE_00173
N_BE_00175
N_BE_00179
```

Do not update the main mapping SOT until candidate gate review and bridge draft review are complete.
