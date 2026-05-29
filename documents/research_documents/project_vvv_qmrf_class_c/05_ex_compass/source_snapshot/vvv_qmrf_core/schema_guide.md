Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

> **DISCLAIMER / CẢNH BÁO:** VVV-QMRF is independent Class D personal research, not Standard Quantum Mechanics, not peer-reviewed or experimentally validated, and not for real-world technical use. Full boundary protocol: `DISCLAIMER.md`.
>
> VVV-QMRF là nghiên cứu cá nhân độc lập ở Class D, không phải Standard Quantum Mechanics, chưa peer-reviewed hoặc kiểm chứng thực nghiệm, và không dùng cho ứng dụng kỹ thuật ngoài thực tế. Giao thức giới hạn đầy đủ: `DISCLAIMER.md`.

# VVV-QMRF Schema Guide — LLM-Friendly Document Creation Contract
# Hướng dẫn Schema VVV-QMRF — Khế ước Tạo Tài liệu Thân thiện cho LLM

**Framework:** VietVunVut Quantum Measurement Registration Framework (VVV-QMRF)  
**Document type:** Schema guide / Document creation contract  
**Status:** Derived control guide — not a new postulate, not a new SOT  
**Scope:** `documents/research_documents/`, `publish/course-highschool-vvv-qmrf/`, and future VVV-QMRF research or educational documents  
**Primary purpose:** Create new VVV-QMRF documents and educational lessons that are structurally complete, traceable to SOT, and safe against overclaiming.  
**Mục đích chính:** Tạo tài liệu VVV-QMRF và bài học giáo dục mới sao cho đủ cấu trúc, truy vết được về "SOT", và tránh khẳng định quá mức.

## 0.0 Neutral Wording Protocol / Quy tắc Diễn đạt Trung tính

**EN:** Do not use negatively evaluative wording such as "logical fallacy", "Classical analogy mistake", "mistake", "wrong", "false", or "error" when explaining Standard Quantum Mechanics, educational analogies, or VVV-QMRF boundaries. Use neutral boundary language such as "category boundary", "scope boundary", "interpretive boundary", "not implied by this analogy", or "registration-layer distinction". Standard Quantum Mechanics must not be framed as logically defective; VVV-QMRF may only identify registration-layer scope gaps unless a separate physical equation and external validation are supplied.

**VN:** Không dùng các từ mang nghĩa đánh giá tiêu cực như "logical fallacy", "Classical analogy mistake", "mistake", "wrong", "false", hoặc "error" khi giải thích "Standard Quantum Mechanics", ví dụ giáo dục, hoặc ranh giới VVV-QMRF. Hãy dùng ngôn ngữ ranh giới trung tính như "category boundary", "scope boundary", "interpretive boundary", "not implied by this analogy", hoặc "registration-layer distinction". Không trình bày "Standard Quantum Mechanics" như có lỗi logic; VVV-QMRF chỉ được nêu khoảng trống phạm vi ở tầng ghi nhận, trừ khi có phương trình vật lý riêng và kiểm chứng bên ngoài.

---

## 0. One-Sentence Rule / Quy tắc Một câu

**EN:** A new VVV-QMRF document is valid only if every major claim, concept, relation, and formula declares its source, claim type, boundary, and verification rule.  
**VN:** Một tài liệu VVV-QMRF mới chỉ hợp lệ khi mọi claim, concept, quan hệ, và công thức quan trọng đều khai báo nguồn, loại claim, ranh giới, và cách kiểm chứng.

---

## 1. Source Corpus / Tập nguồn

This guide is derived from the following active documents. It summarizes their structural rules; it does not replace them.

Guide này được rút ra từ các tài liệu sau. Nó tóm tắt quy tắc cấu trúc, nhưng không thay thế nguồn gốc.

| Source | Role in this guide | Extracted schema rule |
|---|---|---|
| `SYSTEM_Buddhist_Epistemology/system_be_full.md` | Buddhist Epistemology SOT | Use as the single source of truth for BE node/edge definitions during RCA. |
| `category/vvv_qmrf_category_13_e14_validated_absence_registration.md` | Category schema model | A category must define valid cases, invalid cases, traceability matrix, assertion level, and failure contrast. |
| `framework/vvv_qmrf_framework_e01_self_certifying_registration_postulate.md` | Framework postulate schema model | A framework document must separate postulate statement, prose explanation, formal sketch, symbol table, source trace, boundary, and non-claims. |
| `mapping/vvv_qmrf_mapping_be15_exclusion_based_registration.md` | Mapping schema model | A mapping document must separate canonical code, source term, normalized label, legacy label, structural analogue, and identity boundary. |
| `meta_architecture/vvv_qmrf_meta_architecture_bian_01_registration_establishment.md` | Meta-architecture schema model | A meta-architecture document must show component registry, derivation chain, layer position, and evidence chain. |
| `synthesis/vvv_qmrf_synthesis_s1_lambda_registration_natural_interface_lemma.md` | Synthesis and formula schema model | A synthesis document must state lemma, formalism, operator disambiguation, verification test, and downstream consequences. |

---

## 2. RCA for This Guide / RCA cho Guide này

### 2.1 Define — observed issue / Xác định vấn đề

**Symptom:** New VVV-QMRF documents can sound correct but may omit traceability, source hierarchy, claim class, mathematical symbol registry, or boundary conditions.  
**Triệu chứng:** Tài liệu mới có thể viết nghe đúng nhưng thiếu truy vết, thứ bậc nguồn, loại claim, bảng ký hiệu toán học, hoặc điều kiện biên.

**Cause:** The project has many strong document patterns, but no single document-creation contract that every new document must follow.  
**Nguyên nhân:** Project có nhiều mẫu tài liệu tốt, nhưng chưa có một "document-creation contract" chung cho mọi tài liệu mới.

### 2.2 Trace — 5 Whys / Truy nguyên 5 lần hỏi "vì sao"

1. **Why can a new document drift?** Because it may copy prose without copying the traceability discipline.  
   **Vì sao doc mới có thể lệch?** Vì nó có thể sao chép văn phong nhưng không sao chép kỷ luật truy vết.
2. **Why is traceability hard?** Because BE, QM, VVV-QMRF categories, formulas, and mappings use different source layers.  
   **Vì sao truy vết khó?** Vì BE, QM, category VVV-QMRF, công thức, và mapping thuộc nhiều tầng nguồn khác nhau.
3. **Why does that create risk?** Because a derived registration-layer proposal can be mistaken for canonical Buddhist doctrine or physical QM law.  
   **Vì sao rủi ro?** Vì đề xuất tầng ghi nhận có thể bị hiểu nhầm thành giáo nghĩa BE chuẩn hoặc quy luật vật lý QM.
4. **Why do formulas need special care?** Because symbolic notation can look stronger than the evidence behind it.  
   **Vì sao công thức cần cẩn thận?** Vì ký hiệu toán học có thể làm claim trông chắc hơn bằng chứng thật sự.
5. **Why is a schema guide needed?** Because LLMs need explicit fields and validation rules, not only examples.  
   **Vì sao cần schema guide?** Vì "LLM" cần trường dữ liệu và rule kiểm tra rõ, không chỉ cần ví dụ.

### 2.3 Isolate — root cause / Cô lập nguyên nhân gốc

**Root cause:** VVV-QMRF lacks a universal schema contract that forces each new document to declare source authority, claim class, concept lineage, formula validity, and boundary rules before writing the final prose.  
**Nguyên nhân gốc:** VVV-QMRF thiếu một schema chung bắt buộc mỗi doc mới khai báo quyền lực nguồn, loại claim, dòng truy vết concept, phạm vi hợp lệ của công thức, và rule ranh giới trước khi viết bản văn hoàn chỉnh.

### 2.4 Fix — corrected document-creation rule / Sửa đúng nguyên nhân

Every new VVV-QMRF document must be built in this order:

```text
SOT hierarchy → document type → claim inventory → concept inventory → formula inventory → relationship rules → RCA checklist → final prose
```

Mọi tài liệu mới phải đi theo thứ tự:

```text
Thứ bậc SOT → loại tài liệu → danh sách claim → danh sách concept → danh sách công thức → quy tắc quan hệ → checklist RCA → bản văn cuối
```

### 2.5 Verify — root cause removed / Kiểm chứng

The root cause is removed only if the new document can answer these questions:

1. Which source authorizes each major claim?
2. Which claims are source-level, derived, interpretive, conjectural, or unsupported?
3. Which BE node/edge definitions come from `system_be_full.md`?
4. Which VVV-QMRF rule is a registration-layer proposal rather than standard QM?
5. Which formulas define, model, score, or only heuristically express the idea?
6. Which boundary prevents analogy from becoming identity?

Nếu doc mới trả lời được 6 câu trên, nó mới đủ chuẩn.

---

## 3. SOT Hierarchy / Thứ bậc SOT

Use this hierarchy whenever two sources conflict.

Dùng thứ bậc này khi hai nguồn mâu thuẫn.

| Rank | Source layer | Authority rule |
|---:|---|---|
| 1 | `SYSTEM_Buddhist_Epistemology/system_be_full.md` | Final authority for BE node/edge definitions during RCA. |
| 2 | Active VVV-QMRF source documents | Authority for current VVV-QMRF terminology, postulates, categories, mappings, and synthesis. |
| 3 | Derived documents created with this schema | Valid only when their claims trace to Rank 1 or Rank 2. |
| 4 | Interpretive layer | Allowed only when explicitly labeled `derived interpretation` or `structural analogy`. |
| 5 | Unsupported prose | Must be removed, sourced, or downgraded to `TODO(HOTFIX)`. |

### Conflict rule / Quy tắc khi mâu thuẫn

```text
If a new document conflicts with system_be_full.md on a BE node or edge, trust system_be_full.md.
If a VVV-QMRF source uses legacy terminology, preserve it only as legacy trace and use the current normalized term.
If a formula looks stronger than the source evidence, downgrade its claim class.
```

```text
Nếu doc mới mâu thuẫn với system_be_full.md về node/edge BE, tin system_be_full.md.
Nếu nguồn VVV-QMRF dùng thuật ngữ cũ, giữ nó như legacy trace và dùng thuật ngữ chuẩn hiện tại.
Nếu công thức trông mạnh hơn bằng chứng nguồn, hạ cấp loại claim của công thức.
```

---

## 4. Universal Document Schema / Schema Chung cho Mọi Tài liệu

Every new VVV-QMRF document should contain these fields or clearly explain why a field is not applicable.

Mọi doc mới nên có các trường này, hoặc nói rõ vì sao trường nào không áp dụng.

```yaml
document_id: "stable identifier for the document"
document_type: "framework | category | mapping | meta_architecture | synthesis | mathematical_formula | index | publication_draft | course_lesson | highschool_lesson | academic_lesson"
date: "YYYY-MM-DD, for example 2026-05-16"
title_en: "English title"
title_vn: "Vietnamese title when useful"
status: "source | derived | proposal | draft | review | archived"
purpose: "what problem this document solves"
scope: "what this document is allowed to discuss"
out_of_scope: "what this document must not claim"
source_corpus:
  - path: "source file path"
    role: "SOT | VVV-QMRF source | derived support | external support"
SOT_references:
  - source: "system_be_full.md or active VVV-QMRF source"
    anchor: "node, edge, section, or quoted line reference"
key_claims:
  - claim_id: "C-001"
    claim_text: "precise claim"
    claim_type: "source | derived | interpretive_mapping | conjecture | unsupported | overclaim"
concept_traceability:
  - concept_id: "E1, E14, N_BE_00015, BIAN-01, S1-Λ, etc."
    source_file: "path"
    boundary: "what this concept does not mean"
formula_inventory:
  - formula_id: "F-001"
    status: "definition | constraint | mapping_function | scoring_function | lemma_expression | heuristic_formalization"
relationship_rules:
  - relation_id: "R-001"
    relation_type: "dependency | analogy | contrast | derivation | support"
    arrow: "optional visual notation, for example A → B or A -. label .-> B"
    arrow_semantics: "what the arrow means and what it must not imply"
validation_checklist:
  - check: "rule to verify before finalizing"
failure_modes:
  - failure: "common misuse"
    prevention: "how to avoid it"
```

---

## 5. Document Type Schema / Schema theo Loại Tài liệu

### 5.1 Framework document / Tài liệu framework

Use for postulates such as E1, E14, or future registration-layer postulates.

Dùng cho tiên đề như E1, E14, hoặc tiên đề tầng ghi nhận mới.

Required blocks:

| Block | Requirement |
|---|---|
| `postulate_statement` | One precise English statement and optional Vietnamese explanation. |
| `registration_role` | What this postulate adds to the registration layer. |
| `formal_sketch` | Minimal notation; no stronger than the evidence. |
| `symbol_registry` | Required if symbols appear. |
| `source_traceability` | BE SOT, BIAN gap, category document, and framework lineage. |
| `assertion_level` | Source-supported, derived, conjectural, boundary-sensitive, or overclaim. |
| `what_it_does_not_claim` | Required to prevent philosophical or physical overclaiming. |
| `LLM_notes` | Short instructions for safe reuse. |

Minimum rule:

```text
A framework document must say what changes at the K-side registration layer and what does NOT change at the ρ-side physical layer.
```

```text
Doc framework phải nói rõ điều gì đổi ở tầng ghi nhận K-side và điều gì KHÔNG đổi ở tầng vật lý ρ-side.
```

### 5.2 Category document / Tài liệu category

Use for registration categories such as Validated Absence Registration.

Required blocks:

| Block | Requirement |
|---|---|
| `category_identity` | English name, Vietnamese name, source lineage, status. |
| `definition` | What counts as an instance. |
| `validity_conditions` | Required conditions for the category to apply. |
| `negative_controls` | Similar-looking cases that do not qualify. |
| `formal_structure` | Optional formula or model, with symbol registry. |
| `traceability_matrix` | Claim/concept/source/boundary table. |
| `assertion_level` | Distinguish source support from VVV-QMRF proposal. |
| `what_it_does_not_claim` | Required for boundary-sensitive categories. |

Category rule from E14 / VAR:

```text
Not every null event is valid absence registration.
A null event becomes positive absence registration only when validity conditions hold.
```

```text
Không phải mọi sự im lặng của máy đo đều là ghi nhận vắng mặt hợp lệ.
Sự kiện rỗng chỉ thành ghi nhận vắng mặt dương tính khi điều kiện hợp lệ được thỏa mãn.
```

### 5.3 Mapping document / Tài liệu mapping

Use when mapping Buddhist Epistemology to Quantum Measurement.

Required blocks:

| Block | Requirement |
|---|---|
| `canonical_identification` | Code, preferred label, source term, legacy label if any. |
| `system_A` | Ground system; usually Buddhist Epistemology. |
| `system_B` | Target system; usually Quantum Measurement. |
| `structural_reasoning` | Why the mapping is structurally useful. |
| `mapping_status` | analogy, support, contrast, dependency, or equivalence. |
| `identity_boundary` | Required: what is not identical. |
| `graph_relation` | Node/edge codes when available. |
| `RCA_boundary` | Prevent category error between BE and QM. |

Mapping rule from BE15:

```text
Exclusion-Based Registration structurally parallels complementarity or mutually exclusive outcomes, but it is not identical to them.
```

```text
"Exclusion-Based Registration" có cấu trúc giống một phần với "complementarity" hoặc outcome loại trừ nhau, nhưng không đồng nhất với chúng.
```

### 5.4 Meta-architecture document / Tài liệu meta-architecture

Use for rules about the framework itself: gap classification, layer design, pipeline completeness, interface principles.

Required blocks:

| Block | Requirement |
|---|---|
| `thesis` | What architectural rule this document establishes. |
| `component_inventory` | Codes, names, layers, types, sources. |
| `derivation_chain` | How each component follows from the source gap or lemma. |
| `layer_position` | Where the component belongs: gap, category, framework, synthesis, meta-architecture. |
| `yield_analysis` | What the architecture adds and what it does not add. |
| `evidence_chain` | Trace from source evidence to derived components. |

Meta-architecture rule from BIAN-01:

```text
A gap resolution may generate a new architectural layer, but every generated component must show its derivation chain.
```

```text
Một cách giải quyết gap có thể sinh ra tầng kiến trúc mới, nhưng mọi thành phần sinh ra phải có chuỗi phát sinh rõ.
```

### 5.5 Synthesis document / Tài liệu synthesis

Use for lemmas, pipelines, and cross-postulate integration.

Required blocks:

| Block | Requirement |
|---|---|
| `lemma_or_synthesis_statement` | Precise statement of what is integrated. |
| `adjacent_stages` | Pipeline stages or postulates being connected. |
| `formalism` | Minimal formula and conditions. |
| `operator_disambiguation` | Required when symbols can be confused with nodes, faculties, or operations. |
| `verification_test` | Criteria such as the ENI 4-point test. |
| `rejection_evidence` | Why stronger alternatives were rejected. |
| `downstream_consequences` | Components generated or affected. |

Synthesis rule from S1-Λ:

```text
A transition lemma is not automatically a new postulate.
If the transition is an interface rather than a separate operation, classify it as lemma or interface, not postulate.
```

```text
Bổ đề chuyển tiếp không tự động là tiên đề mới.
Nếu chuyển tiếp là giao diện chứ không phải thao tác riêng, phân loại nó là lemma/interface, không phải postulate.
```

### 5.6 Mathematical formula document / Tài liệu công thức toán học

Use for any document whose main purpose is to define, derive, compare, or validate formulas.

Required blocks:

| Block | Requirement |
|---|---|
| `formula_id` | Stable formula code, e.g. `F-VAR-001`, `F-S1L-001`. |
| `formula_name` | Human-readable name. |
| `formula_class` | definition, constraint, mapping_function, scoring_function, lemma_expression, or heuristic_formalization. |
| `formal_expression` | The formula itself. |
| `symbol_registry` | Every symbol must be defined before use. |
| `assumptions` | Conditions required before the formula applies. |
| `domain_of_validity` | Where the formula is allowed to be used. |
| `source_trace` | Which source, node, edge, section, or formula supports each part. |
| `derivation_steps` | Step-by-step derivation or justification. |
| `interpretation_boundary` | What the formula must not be taken to prove. |
| `failure_modes` | Common misuses. |
| `LLM_usage_rule` | How an LLM may reuse or extend the formula. |

Formula rule:

```text
A VVV-QMRF formula is valid only if every symbol is defined, every inference step is traced, and the formula's claim class is stated.
```

```text
Một công thức VVV-QMRF chỉ hợp lệ nếu mọi ký hiệu được định nghĩa, mọi bước suy luận được truy vết, và loại claim của công thức được khai báo.
```

### 5.7 Index document / Tài liệu index

Use for registries, lists, or canonical tables.

Required blocks:

| Block | Requirement |
|---|---|
| `canonical_list` | Stable list of documents, nodes, postulates, formulas, or concepts. |
| `status` | Active, draft, derived, deprecated, archived. |
| `source_pointer` | Path to the authoritative source for each row. |
| `cross_reference` | Related docs and dependencies. |
| `update_rule` | When and how the index should be updated. |

### 5.8 Publication-facing draft / Bản nháp hướng xuất bản

Use for papers, abstracts, introductions, and publication-oriented prose.

Required blocks:

| Block | Requirement |
|---|---|
| `claim_discipline` | Every strong claim must have source or citation. |
| `scope_boundary` | Separate interpretation from formal proof and experimental prediction. |
| `citation_discipline` | No invented sources. Mark missing citation explicitly. |
| `non_overclaim_rule` | Never say BE solves QM unless formal proof and tests exist. |
| `reader_level` | State whether the text is technical, general, or bilingual explanatory. |

### 5.9 Educational course document / Tài liệu bài học giáo dục

Use for lessons, course units, high-school explanations, and academic teaching notes derived from VVV-QMRF.

Dùng cho bài học, đơn vị khóa học, giải thích phổ thông, và ghi chú giảng dạy học thuật được rút ra từ VVV-QMRF.

Allowed educational `document_type` values:

| Document type | Use when | Reader level |
|---|---|---|
| `course_lesson` | The lesson belongs to a course but does not need a more specific level. | Declared in the lesson metadata. |
| `highschool_lesson` | The lesson is written for high-school learners or introductory public teaching. | High-school / phổ thông. |
| `academic_lesson` | The lesson is written for university, research, or technically trained readers. | Undergraduate, graduate, or research-facing. |

Required blocks:

| Block | Requirement |
|---|---|
| `learning_objectives` | State what the learner should understand after the lesson. |
| `reader_level` | Declare `highschool`, `undergraduate`, `academic`, or another explicit level. |
| `source_trace` | Point back to this schema and the active VVV-QMRF or BE/QM sources used. |
| `concept_boundary` | State what each simplified concept must not be taken to mean. |
| `formula_boundary` | Required when symbols appear; distinguish teaching notation from formal claim. |
| `misconception_guard` | List likely misunderstandings and block them directly. |
| `main_lesson` | Present the teaching content at the declared reader level. |
| `example_or_analogy` | Mark examples as analogy unless equivalence is explicitly justified. |
| `exercise_or_quiz` | Include questions or exercises when useful for learning validation. |
| `what_this_lesson_does_not_claim` | Required non-claims for QM, BE, and VVV-QMRF boundaries. |
| `mini_validation_checklist` | Short checklist confirming source trace, boundaries, and no overclaim. |

High-school lesson rule:

```text
A highschool_lesson may simplify language, but it must not simplify the claim boundary.
Teaching analogies are allowed only when they are marked as analogies, not proofs.
```

```text
Bài highschool_lesson có thể làm ngôn ngữ dễ hơn, nhưng không được làm ranh giới claim lỏng hơn.
Ví dụ minh họa chỉ được dùng như analogy, không phải proof.
```

Academic lesson rule:

```text
An academic_lesson must preserve source trace, claim type, formula class, and boundary conditions when it teaches a research concept.
```

```text
Bài academic_lesson phải giữ truy vết nguồn, loại claim, loại công thức, và điều kiện biên khi giảng một concept nghiên cứu.
```

Educational RCA rule:

```text
If a learner-friendly sentence sounds stronger than the research source, downgrade the sentence before adding more explanation.
```

```text
Nếu một câu dễ học nghe mạnh hơn nguồn nghiên cứu, hãy hạ cấp câu đó trước khi thêm giải thích.
```

---

## 6. Claim Traceability Schema / Schema Truy vết Claim

Every major claim must be recorded before final prose is written.

Mọi claim quan trọng phải được ghi trước khi viết bản văn hoàn chỉnh.

| Field | Meaning | Vietnamese guide |
|---|---|---|
| `claim_id` | Stable claim code | Mã claim ổn định |
| `claim_text` | Exact claim | Câu claim chính xác |
| `claim_type` | Source, derived, interpretive, conjecture, unsupported, overclaim | Loại claim |
| `source_file` | File supporting the claim | File nguồn |
| `source_anchor` | Node, edge, section, quote, or line reference | Điểm neo truy vết |
| `confidence` | high, medium, low | Mức tin cậy |
| `allowed_usage` | How the claim may be used | Được dùng thế nào |
| `forbidden_usage` | What the claim must not imply | Không được suy ra gì |
| `verification_rule` | How to check the claim | Cách kiểm chứng |

### Claim classes / Các loại claim

| Claim type | Use when | Rule |
|---|---|---|
| `source` | Directly present in SOT or active source | May be stated strongly within source scope. |
| `derived` | Built from source by VVV-QMRF architecture | Must state derivation path and status. |
| `interpretive_mapping` | Cross-system structural comparison | Must include analogy/non-identity boundary. |
| `formal_notation` | Symbolic representation of a concept | Must include symbol registry and claim class. |
| `conjecture` | Plausible but unproven relation | Must not be presented as fact. |
| `boundary_application` | Example such as dark-matter reasoning | Must remain conditional. |
| `unsupported` | No source found | Must be removed, sourced, or marked `TODO(HOTFIX)`. |
| `overclaim` | Stronger than evidence | Must be downgraded or removed. |

---

## 7. Concept Traceability Schema / Schema Truy vết Concept

Use this schema for every major concept: E1, E14, BE15, BIAN-01, S1-Λ, ENI, GCS, MIP, PCC, or future concepts.

Dùng schema này cho mọi concept quan trọng.

| Field | Meaning |
|---|---|
| `concept_id` | Stable code: `E1`, `E14`, `N_BE_00015`, `BIAN-01`, `S1-Λ`, etc. |
| `canonical_name` | Preferred current VVV-QMRF name. |
| `legacy_names` | Old labels kept only for traceability. |
| `source_term` | BE term, QM term, or VVV-QMRF term. |
| `definition` | Short definition. |
| `source_file` | Source document path. |
| `SOT_anchor` | BE node/edge, BIAN row, postulate, section, or formula. |
| `registration_role` | Role inside VVV-QMRF registration architecture. |
| `QM_boundary` | What it does not claim about standard QM. |
| `BE_boundary` | What it does not claim about Buddhist Epistemology. |
| `failure_mode` | Common misuse. |

### Concept traceability seeds / Hạt giống truy vết concept

| Concept | Source anchor | Safe use | Boundary |
|---|---|---|---|
| `N_BE_00011 — Self-awareness` | `system_be_full.md`; E1 source trace | Source lineage for structural self-certification. | Do not turn E1 into a consciousness claim. |
| `N_BE_00015 — Exclusion` | `ED_BE_00016`; BE15 mapping | Source lineage for exclusion-based semantic registration. | Do not treat complementarity as identical to Apoha. |
| `N_BE_00018 — Trairūpya` | `system_be_full.md`; E14 Category 13 | Validity gate model for conditioned absence registration. | Do not treat it as native QM formalism. |
| `N_BE_00253 — Anupalabdhi` | `ED_BE_00115`, `ED_BE_00116`; E14 Category 13 | Source lineage for valid absence cognition. | Do not treat absence as a new physical substance. |
| `S1-Λ` | S1 synthesis document | Interface lemma for E4 to E5 transition. | Do not promote it to a postulate without RCA. |
| `BIAN-01` | BIAN-01 meta-architecture document | Gap that generated S1-Λ and downstream meta-architecture. | Do not treat all gaps as equally productive. |

---

## 8. Mathematical Formula Schema / Schema Công thức Toán học

### 8.1 Formula inventory / Danh sách công thức

Each formula must appear in a table before being used in prose.

Mỗi công thức phải nằm trong bảng trước khi dùng trong văn bản.

| Field | Required | Rule |
|---|---:|---|
| `formula_id` | yes | Stable code. |
| `formula_name` | yes | Plain-language name. |
| `formula_class` | yes | Use the allowed enum below. |
| `formal_expression` | yes | Exact expression. |
| `symbol_registry` | yes | Define every symbol. |
| `assumptions` | yes | Preconditions. |
| `domain_of_validity` | yes | Where it applies. |
| `source_trace` | yes | Source for each structural part. |
| `derivation_steps` | yes | Steps from source to expression. |
| `interpretation_boundary` | yes | What it does not prove. |
| `failure_modes` | yes | Misreadings to block. |

Allowed `formula_class` values:

```text
definition
constraint
mapping_function
scoring_function
lemma_expression
heuristic_formalization
```

### 8.2 Symbol registry rule / Quy tắc bảng ký hiệu

```text
No symbol may appear in a formula unless it appears in the symbol_registry first.
```

```text
Không ký hiệu nào được xuất hiện trong công thức nếu chưa được định nghĩa trước trong symbol_registry.
```

Minimum symbol registry:

| Symbol | Meaning EN | Nghĩa VN | Domain | Source trace |
|---|---|---|---|---|
| `M` | Measurement act | Hành động đo | registration event | source path / section |
| `K` | Registration-state layer | Tầng trạng thái ghi nhận | VVV-QMRF | source path / section |
| `ρ` | Quantum state description | Mô tả trạng thái lượng tử | standard QM | QM source if used |
| `Λ` | Symbolization map | Ánh xạ biểu tượng hóa | S1-Λ / synthesis | source path / section |

### 8.3 Formula boundary rule / Quy tắc ranh giới công thức

```text
A formula in VVV-QMRF may define a registration-layer model.
It does not automatically define a new physical law.
```

```text
Công thức trong VVV-QMRF có thể định nghĩa mô hình tầng ghi nhận.
Nó không tự động là quy luật vật lý mới.
```

### 8.4 Minimal formula document template / Template tối giản cho doc công thức

```yaml
formula_document:
  document_id: "FORMULA-..."
  document_type: "mathematical_formula"
  date: "YYYY-MM-DD"
  title_en: "..."
  purpose: "why this formula is needed"
  source_corpus:
    - "source path"
  formula_inventory:
    - formula_id: "F-001"
      formula_name: "..."
      formula_class: "definition | constraint | mapping_function | scoring_function | lemma_expression | heuristic_formalization"
      formal_expression: "..."
      symbol_registry:
        - symbol: "..."
          meaning_en: "..."
          meaning_vn: "..."
          domain: "..."
          source_trace: "..."
      assumptions:
        - "..."
      domain_of_validity:
        - "..."
      derivation_steps:
        - step: 1
          statement: "..."
          source_trace: "..."
      interpretation_boundary:
        - "..."
      failure_modes:
        - failure: "..."
          prevention: "..."
  validation_checklist:
    - "all symbols defined"
    - "all derivation steps traced"
    - "formula class declared"
    - "not presented as physical law unless externally validated"
```

### 8.5 Formula examples as schema patterns / Ví dụ công thức như mẫu schema

These examples show formatting only. They are not new proofs.

Các ví dụ này chỉ minh họa cấu trúc trình bày. Chúng không phải chứng minh mới.

| Formula pattern | Source model | Required boundary |
|---|---|---|
| `σ(M) = 1 iff M has occurred` | E1 framework | K-side self-certification marker; does not alter Hamiltonian or Born rule. |
| `Π̂_absent^(ℋ_M) = I_ℋ_M - Σᵢ |λᵢ⟩⟨λᵢ|` | E14 category | Conditioned absence projection inside accessible subspace; not proof of physical absence outside valid domain. |
| `M(T) := D \ Other(T)` | BE15 mapping | Semantic exclusion model; not quantum complementarity itself. |
| `Λ: ε(M) → Ā(M)` | S1-Λ synthesis | Interface lemma; not a separate postulate unless future RCA upgrades it. |

---

## 9. Relationship Rules / Quy tắc Quan hệ

### 9.1 Relation types / Các loại quan hệ

| Relation type | Meaning | Required boundary |
|---|---|---|
| `source_of` | A source concept supports a VVV-QMRF concept. | Do not make source concept identical to derived concept. |
| `derives_from` | A component follows by RCA or formal derivation. | Show derivation steps. |
| `structural_analogy` | Similar role across systems. | Must say "not identity". |
| `contrast_with` | Negative control or failure contrast. | Must define both sides. |
| `depends_on` | One component requires another. | Must state dependency direction. |
| `generalizes` | Broader category includes narrower case. | Must avoid erasing the narrower case. |

### 9.2 Arrow Semantics / Quy tắc mũi tên

Use arrows only after the relation type is known. An arrow is visual notation for a declared relation; it is not automatically a physical cause, proof, or identity claim.

Chỉ dùng mũi tên sau khi đã biết loại quan hệ. Mũi tên là ký hiệu nhìn cho một quan hệ đã khai báo; nó không tự động là nguyên nhân vật lý, chứng minh, hoặc claim đồng nhất.

| Arrow form | Allowed meaning | Required boundary |
|---|---|---|
| `A → B` | Directed dependency or sequence inside one declared layer. | Must state whether the layer is physical `ρ-side`, registration `K-side`, or document logic. |
| `A ↔ B` | Structural correspondence between two systems. | Mapping is not identity; do not read as equivalence unless separately proven. |
| `A ⇒ B` | Logical implication inside one formal rule set. | Use only when the source or derivation explicitly supports implication. |
| `A ⇢ B` | Registration-state update on the K-side. | Not a detector response and not a Standard QM state update. |
| `A -. label .-> B` | Boundary note, preservation note, contrast, or RCA fix path. | The label must say what is preserved, limited, contrasted, or fixed. |
| `A ~ B` | Educational analogy or interpretive resemblance. | Analogy is not proof and must not create physical or doctrinal identity. |

Decision rule:

```text
If the relation is a BE SOT edge, cite ED_BE_000xx first.
If the relation maps BE to QM, prefer structural correspondence or analogy notation, not causal notation.
If the relation updates K, use registration-state update language.
If the relation is Standard QM physics, keep it inside the physical ρ-side and do not mix it with K-side novelty.
If the relation type is unclear, do not draw the arrow; run RCA first.
```

Quy tắc chọn:

```text
Nếu quan hệ là edge trong BE SOT, cite ED_BE_000xx trước.
Nếu quan hệ map BE sang QM, ưu tiên tương ứng cấu trúc hoặc analogy, không dùng ký hiệu nhân quả.
Nếu quan hệ cập nhật K, dùng ngôn ngữ "registration-state update".
Nếu quan hệ là vật lý Standard QM, giữ trong tầng vật lý ρ-side và không trộn với điểm mới K-side.
Nếu chưa rõ loại quan hệ, không vẽ mũi tên; RCA trước.
```

### 9.3 Non-negotiable boundaries / Ranh giới bắt buộc

```text
Mapping is not identity.
Analogy is not proof.
Derived notation is not canonical QM.
Registration-layer model is not automatic physical law.
Validated absence is not ordinary silence.
Detector response is not the same as registration-state update.
Self-certifying registration is not a consciousness claim.
S1-Λ is a lemma/interface unless RCA upgrades it.
```

```text
Mapping không phải đồng nhất.
Analogy không phải chứng minh.
Ký hiệu derived không phải QM chuẩn.
Mô hình tầng ghi nhận không tự động là quy luật vật lý.
Vắng mặt hợp lệ không phải im lặng thông thường.
"Detector response" không giống "registration-state update".
Tự chứng ghi nhận không phải claim về ý thức.
S1-Λ là lemma/interface trừ khi RCA nâng cấp nó.
```

---

## 10. Terminology Rules / Quy tắc Thuật ngữ

| Term | Required use |
|---|---|
| `VVV-QMRF` | Current name: VietVunVut Quantum Measurement Registration Framework. |
| `VVV-EQM` | Legacy name only; keep for traceability. |
| `registration-state update` | General K-side update term beyond human cognition. |
| `detector response` | Use only for the apparatus' physical response. |
| `BIAN-XX` | Use two digits for new BIAN concept nodes, `BIAN-01` to `BIAN-99`; BIAN derives from Vietnamese `bí ẩn`, meaning `mystery`. |
| `N_BE_00001` style | Use five-digit BE node codes. Do not use old short forms. |
| `ED_BE_00001` style | Use five-digit BE edge codes. Do not use old short forms. |
| `source term` | Original BE/QM term. |
| `normalized label` | Current VVV-QMRF-facing label. |
| `legacy label` | Old label retained only for comparison and traceability. |

---

## 11. LLM Writing Protocol / Giao thức Viết cho LLM

Use this protocol before writing any new VVV-QMRF document.

Dùng quy trình này trước khi viết bất kỳ doc VVV-QMRF mới nào.

```text
Step 1 — Identify document_type.
Step 2 — List source_corpus.
Step 3 — Read required SOT before making claims.
Step 4 — Create claim inventory.
Step 5 — Create concept inventory.
Step 6 — Create formula inventory if symbols appear.
Step 7 — Assign claim_type and assertion level.
Step 8 — Add mapping boundaries and non-claims.
Step 9 — Run RCA: Define, Trace, Isolate, Fix, Verify.
Step 10 — Write final prose only after traceability is complete.
```

LLM must refuse or pause when:

```text
A source is missing.
A claim cannot be classified.
A formula has undefined symbols.
A mapping lacks an analogy/non-identity boundary.
A new BE node/edge code conflicts with system_be_full.md.
A derived registration-layer proposal is being phrased as standard QM.
```

"LLM" phải dừng hoặc hỏi lại khi:

```text
Thiếu nguồn.
Không phân loại được claim.
Công thức có ký hiệu chưa định nghĩa.
Mapping thiếu ranh giới analogy/non-identity.
Mã node/edge BE mới mâu thuẫn với system_be_full.md.
Đề xuất tầng ghi nhận bị viết như QM chuẩn.
```

---

## 12. Minimal Templates / Template Tối giản

### 12.1 General document template / Template doc chung

```markdown
Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# [Title EN] / [Title VN]

**Framework:** VVV-QMRF  
**Document type:** [framework/category/mapping/meta_architecture/synthesis/mathematical_formula/index/publication_draft]  
**Date:** YYYY-MM-DD  
**Status:** [source/derived/proposal/draft/review]  
**Scope:** [allowed scope]

## 1. Purpose / Mục đích

## 2. Source Corpus / Tập nguồn

| Source | Role | Required trace |
|---|---|---|

## 3. RCA Summary / Tóm tắt RCA

### Define
### Trace
### Isolate
### Fix
### Verify

## 4. Claim Traceability / Truy vết Claim

| Claim ID | Claim | Type | Source | Boundary |
|---|---|---|---|---|

## 5. Concept Traceability / Truy vết Concept

| Concept | Canonical name | Source | Role | Boundary |
|---|---|---|---|---|

## 6. Main Content / Nội dung chính

## 7. What This Document Does NOT Claim / Những gì doc này KHÔNG tuyên bố

## 8. Validation Checklist / Checklist Kiểm chứng
```

### 12.2 Mapping document template / Template mapping

```markdown
## Canonical Identification

| Field | Value |
|---|---|
| Source system | Buddhist Epistemology |
| Target system | Quantum Measurement / VVV-QMRF |
| BE node | N_BE_000XX |
| BE edge | ED_BE_000XX |
| Source term | ... |
| Normalized label | ... |
| Legacy label | ... |
| Mapping status | structural analogy / dependency / contrast / support |

## Mapping Statement

[Node_A] <=> [Node_B] : [brief structural reasoning]

## RCA Boundary

This is a structural mapping, not an identity claim.
```

### 12.3 Mathematical formula template / Template công thức toán học

````markdown
## Formula Identity

| Field | Value |
|---|---|
| Formula ID | F-... |
| Formula name | ... |
| Formula class | definition / constraint / mapping_function / scoring_function / lemma_expression / heuristic_formalization |
| Status | source / derived / conjectural |

## Formal Expression

```text
[formula]
```

## Symbol Registry

| Symbol | Meaning EN | Meaning VN | Domain | Source trace |
|---|---|---|---|---|

## Assumptions

## Domain of Validity

## Derivation Steps

| Step | Statement | Source trace | Claim type |
|---|---|---|---|

## Interpretation Boundary

## Failure Modes

## LLM Usage Rule
````

### 12.4 Educational lesson template / Template bài học giáo dục

```markdown
Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# [Lesson Title EN or VN]

**Document type:** [course_lesson/highschool_lesson/academic_lesson]
**Date:** YYYY-MM-DD
**Status:** educational draft
**Reader level:** [highschool/undergraduate/academic]
**Scope:** [allowed teaching scope]
**Source trace:** `documents/research_documents/vvv-qmrf/schema_guide.md`; [active source path]
**Claim boundary:** This lesson is an educational interpretation of VVV-QMRF terminology; it does not replace Standard Quantum Mechanics.
**Formula boundary:** Symbols, if present, are teaching notation unless explicitly classified as formal VVV-QMRF notation.
**Neutral wording boundary:** Standard Quantum Mechanics, analogies, and VVV-QMRF boundaries are described with neutral boundary language.

## 1. Learning Objectives / Mục tiêu bài học

## 2. RCA Learning Problem / Vấn đề học tập theo RCA

### Define
### Trace
### Isolate
### Fix
### Verify

## 3. Main Lesson / Bài giảng chính

## 4. Example or Analogy / Ví dụ hoặc analogy

## 5. Formula or Symbol Explanation / Giải thích công thức hoặc ký hiệu

## 6. Misconception Guard / Chặn hiểu sai

## 7. Exercise or Quiz / Bài tập hoặc trắc nghiệm

## 8. Source Links / Nguồn liên quan

## What This Lesson Does NOT Claim

* It does not claim that VVV-QMRF replaces Standard Quantum Mechanics.
* It does not claim that Buddhist Epistemology proves Quantum Mechanics.
* It does not use analogy or teaching notation as proof of a physical theory.

## Mini Validation Checklist

* Reader level is declared.
* Source trace is listed.
* Claim boundary, formula boundary, and neutral wording boundary are stated.
* Standard Quantum Mechanics is described with neutral boundary language.
* Analogies are marked as analogies, not proofs.
```

---

## 13. RCA Verification Checklist / Checklist Kiểm chứng RCA

Use this checklist before marking a new document as complete.

Dùng checklist này trước khi coi doc mới là hoàn thành.

| Check | Pass condition |
|---|---|
| Metadata | Author metadata exists unless the file is under `documents/published_documents/`. |
| Document type | `document_type` is declared. |
| Date | Date uses `YYYY-MM-DD`. |
| Source corpus | All required sources are listed. |
| BE SOT | BE node/edge definitions trace to `system_be_full.md`. |
| Claim types | Every major claim has `claim_type`. |
| Derived claims | Every derived claim has a derivation path. |
| Mapping boundary | Every cross-system mapping says whether it is analogy, support, contrast, or equivalence. |
| Formula registry | Every formula has defined symbols and a validity domain. |
| Reader level | Educational documents declare the intended learner level. |
| Lesson boundaries | Educational documents include claim boundary and formula boundary. |
| Teaching analogy | A lesson marks analogies as analogies, not proof. |
| High-school simplification | `highschool_lesson` simplifies language without weakening claim boundaries. |
| Academic lesson trace | `academic_lesson` preserves source trace, claim type, formula class, and boundary conditions. |
| Non-claims | The document states what it does not claim. |
| K-side vs ρ-side | Registration-layer claims do not modify physical QM unless explicitly justified. |
| Terminology | Uses `registration-state update` for K-side update and `detector response` only for apparatus response. |
| BIAN codes | New BIAN codes use `BIAN-XX`. |
| BE codes | BE node/edge codes use five digits. |
| Overclaim check | No claim says BE proves or solves QM without formal proof and empirical validation. |
| Unsupported claim check | Unsupported claims are removed, sourced, downgraded, or marked `TODO(HOTFIX)`. |

---

## 14. Final Operational Rule / Quy tắc Vận hành Cuối

```text
Do not write a beautiful document first and add traceability later.
Build traceability first, then write the document.
```

```text
Đừng viết một doc thật hay rồi mới thêm truy vết sau.
Hãy xây truy vết trước, rồi mới viết doc.
```
