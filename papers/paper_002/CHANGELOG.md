# CHANGELOG — "Have Optical Wigner's Friend Experiments Been Blind to a Geometric Degree of Freedom?"

**Paper ID:** paper_002 | **Target:** arXiv quant-ph → Phys. Rev. A
**Author:** VietVunVut (Viet — Nguyen Xuan)

---

## v88 (2026-05-26) — 3/7-issue RCA (threshold 4.5/5): Operational observable in "In brief"; §2.3 + §7 compressed; Novelty crystallization

**Scoring summary (7 issues):** 3 implemented (≥4.0/5), 4 rejected.

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | "Blind spot" overclaim → assertive reduction | 2.5/5 | **Rejected** — Oscillation. v87 just softened abstract; body "systematically unexplored" = v79 RCA 4.5/5 |
| 2 | Toy physical mechanism in main text | 1.5/5 | **Rejected** — v81 genre boundary auto-reject; v84+v85 already added physical context + info-theoretic |
| 3 | Cắt 20-25% defensive justification | 3.5/5 | **Rejected** — v85+v86 already merged duplicates + dedup; remaining granular |
| 4 | Operational observable earlier in §1 | 4.0/5 | **Implemented** — δ⟨AB⟩ ∝ cos θ + Lemma 1 moved to "In brief" paragraph |
| 5 | Compress §2.3 + §7 framing | 4.5/5 | **Implemented** — §2.3: SME paragraph −4 lines, "Why overlap-only" −3 lines, Core idea −1 line. §7: Two-phase −8 lines. Total −16 lines |
| 6 | Schematic/visual "1-hour mod" | 2.5/5 | **Rejected** — §4.5 already states ~1 hour; schematics in supplemental (v57) |
| 7 | Novelty crystallization — theorem or protocol? | 4.2/5 | **Implemented** — "In brief" now ends: "The paper's contribution is twofold: a geometric null theorem (Proposition 1) showing that equatorial measurements leave the overlap-only class systematically unexplored, and a single-waveplate protocol (§4–7) enabling its first experimental test." |

### Implemented changes (v88)

| # | Section | Change | Rationale |
|---|---------|--------|-----------|
| 4 | §1 | **Operational observable + novelty in "In brief" (+2 sentences):** Old: "...proposes the null-test protocol (§4–7)." New: "...The predicted signal δ⟨AB⟩ ∝ cos θ is a genuine observable, not a coordinate artifact (Lemma 1, §3.2). The paper's contribution is twofold: a geometric null theorem (Proposition 1) showing that equatorial measurements leave the overlap-only class systematically unexplored, and a single-waveplate protocol (§4–7) enabling its first experimental test." | Operational observable defense was buried at end of Proposition 1 paragraph. Moving to "In brief" preempts "basis artifact" criticism before technical content. Novelty sentence crystallizes what was spread across 3 paragraphs. |
| 5a | §2.3 Core idea | **Trimmed constraint preview (−1 line):** "simplest leading-order form satisfying them"→"simplest form satisfying them." Removed redundancy with full constraint derivation at Eq.(2-3). | Lines 178-181 restate the same constraints in detail. Preview doesn't need "leading-order" qualifier. |
| 5b | §2.3 SME | **SME paragraph condensed (−4 lines):** Cut explicit scale values (~10⁻¹⁷ to <10⁻²³), tightened prose. "functions analogously to the Standard Model Extension (SME) for Lorentz violation [15]. The SME was proposed with..."→"functions analogously to SME coefficients [15]: the SME was proposed with..." | SME scale values are SME-specific — not needed for the methodological analogy. "β is a search parameter; a null result at β ≥ 0.04 constrains"→"β is a search parameter whose null result constrains" — single clause replaces two. |
| 5c | §2.3 Why overlap-only | **Prioritization trimmed (−3 lines):** "Level 0 is prioritized over Levels 1–3: (i)...(ii) whereas higher levels demand progressively more complex designs without an equatorial fixed point to anchor a null test."→"Level 0 is prioritized: (i)...(ii)." | Verbose sub-clause about higher levels cut — already implied by "only level with sharp geometric null" + "only requires single waveplate." |
| 5d | §7 | **Two-phase compressed (−8 lines):** 13→5 lines. Cut redundant Phase 1 hedging ("self-consistent but not loophole-free exclusion," "screening stage," "null result is suggestive but remains open to the detection-loophole objection"), Phase 2 redundancy ("converting the result into a definitive conclusion," "so Phase 2 can proceed immediately...without an intermediate redesign stage"). | Two-phase concept explained at abstract + §1 + §7. §7 paragraph had 4 sentences restating the Phase-1-is-screening idea. Core info preserved: Phase 1 = η≈0.87 screening, Phase 2 = η≥0.91 SNSPD closure, same optics. |

### Regression
Δ: §1 +2 sentences (operational observable + novelty). §2.3 −8 lines. §7 −8 lines. Net: −14 lines. C1/C3/C10/C17 preserved. Two-phase content preserved (shorter). All v84-v87 changes retained.

---

## v87 (2026-05-26) — 3/3-issue RCA (threshold 4.5/5): Abstract tightened + factual opening; §2.3 benchmark explicitly "phenomenological ansatz"

**Scoring summary (3 issues):** 3 implemented (≥4.2/5).

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Abstract ~185 words, fix spread across S1+S4 | 4.7/5 | **Implemented** — Tightened to ~150 words. "operated exclusively at...fixed point" → "single waveplate breaks this cancellation" in S1+S2. Cut "reflecting the experimental scarcity," "optimal trade-off...LF preservation," "Phase 2 closure via SNSPD" detail. |
| 2 | "unnoticed geometric blind spot" overclaim with N=2 | 4.2/5 | **Implemented** — Abstract: "share an unnoticed geometric blind spot"→"have operated exclusively at...a fixed point." Factual, mathematical language. Body text "systematically unexplored" preserved (v79 RCA 4.5/5 — changing = oscillation). Title untouched (v80 freeze). |
| 3 | Benchmark could be misread as physical model | 4.5/5 | **Implemented** — §2.3 Eq.(2) definition: "a benchmark parametrization — the lowest-order scalar..."→"a benchmark parametrization — a phenomenological ansatz, not derived from any underlying physical theory — representing the lowest-order scalar..." |

### Implemented changes (v87)

| # | Section | Change | Rationale |
|---|---------|--------|-----------|
| 1 | Abstract | **Tightened + factual opening (~150 words):** S1: "have operated exclusively at an equatorial measurement geometry (θ = π/2) — a fixed point where..." S2: "A single waveplate breaks this cancellation." Cuts: "reflecting the experimental scarcity," "optimal trade-off between signal strength and LF preservation," "whose positive result would motivate Phase 2 closure via SNSPD upgrade (η ≥ 0.91)." Survey + scope + falsification compressed. | "Operated exclusively at" is factual (both experiments DID operate at θ=π/2), not interpretive. "Fixed point" is mathematical, not anthropomorphic. 150 words vs prior 185 — every sentence carries weight. |
| 2 | Abstract | **Softer claim language:** "share an unnoticed geometric blind spot"→"have operated exclusively at an equatorial measurement geometry (θ = π/2) — a fixed point." Body occurrences of "systematically unexplored" (v79) KEPT — v79 RCA 4.5/5 was deliberate. "Blind spot" retained only in §3.5 title and body where scoped by survey qualifiers. | Reviewer reading abstract first sees factual claim about measurement geometry, not rhetorical claim about blindness. The structural argument (v77 "Structural, not coincidental," v85 "θ as independent DoF") now lands on firmer footing. |
| 3 | §2.3 | **Phenomenological explicit disclaimer (+6 words):** "Equation (2) is a benchmark parametrization — the lowest-order scalar..."→"Equation (2) is a benchmark parametrization — a phenomenological ansatz, not derived from any underlying physical theory — representing the lowest-order scalar..." | The defining paragraph for Eq.(2) now states the phenomenological nature explicitly at the point of definition. Reviewer cannot claim the paper presents Eq.(2) as a physical model. Complements existing disclaimers at §1 ("no claim about existence"), §2.3 SME paragraph, §5.3 ("no existing theory predicts"). |

### Regression
Δ: Abstract −35 words (185→150). §2.3 +6 words. Net: −29 words. C1/C3/C10/C17 preserved. "Systematically unexplored" (v79) preserved in body. Title unchanged. All v84/v85/v86 changes retained.

---

## v86 (2026-05-26) — 3/3-issue RCA (threshold 4.5/5): Abstract restructured (fix in S1); §1 plain-English summary; "benchmark parametrization" dedup

**Scoring summary (3 issues):** 3 implemented (≥4.5/5).

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Abstract buries fix after theorem+survey | 4.7/5 | **Implemented** — S1: "blind spot...and a single waveplate breaks it." Survey moved before proposal. ~185 words. |
| 2 | §1 inaccessible to non-EWF readers | 4.5/5 | **Implemented** — **In brief.** paragraph (3 sentences): plain-English summary before Proposition 1. |
| 3 | "benchmark parametrization" repeated 7× | 4.5/5 | **Implemented** — Cut 4 occurrences (§3.1, §5.3×3). Now 3×: §1, §2.3×2. C10 preserved. |

### Implemented changes (v86)

| # | Section | Change | Rationale |
|---|---------|--------|-----------|
| 1 | Abstract | **Restructured (fix-first):** S1: "...blind spot for the overlap-only class — and a single waveplate breaks it." Survey moved before proposal. "phenomenological null test" cut (implied). "— but not replace —" cut (implicit). ~185 words, 6 sentences. | Prior: blind spot→theorem→survey→proposal. Reader doesn't see payoff until S3. New: hook+fix→theorem→survey→proposal. Fix in sentence 1. |
| 2 | §1 | **Plain-English summary (+3 sentences):** "**In brief.** Every published optical EWF experiment has used — by convention for LF optimization, not by design — the one measurement geometry (θ = π/2) at which an entire class of overlap-dependent quantum deformations cancels identically. A single waveplate breaks this accidental fixed point, enabling the first experimental probe of this class. This paper proves the equatorial cancellation theorem (Proposition 1), surveys the literature (§3.5, Supplemental S1), and proposes the null-test protocol (§4–7)." | Non-EWF physicists need accessible entry point. "By convention, not by design" captures insight without jargon. Three-part "proves...surveys...proposes" previews structure. |
| 3 | §3.1, §5.3 | **"benchmark parametrization" dedup (7→3):** §3.1: "is a benchmark parametrization"→"serves only to quantify." §5.3×3: "For the benchmark parametrization Eq. (2-3)"→"For Eq. (2-3)"; "The benchmark parametrization Eq. (2-3) predicts"→"Eq. (2-3) predicts." Term retained at §1 + §2.3×2 (defining instances). C10 preserved. | By §5.3 reader has seen term 3 times; "Eq. (2-3)" unambiguous. §3.1 cut avoids repetition with §2.3 Core idea. |

### Regression
Δ: Abstract S1 +5 words (fix clause), −3 words (cut "phenomenological null test"). §1 +50 words (plain-English), −10 words (old preview removed). §3.1 −2 words. §5.3 −15 words (4 cuts). Net: ~+25 words. C1/C3/C10/C17 preserved. All v84/v85 changes retained.

---

## v85 (2026-05-26) — 5/10-issue RCA (threshold 4.5/5): θ as independent LF DoF; §3.5 duplicate merge; §1/§9 experimental focus; §2.3 disclaimers consolidated; Information-theoretic overlap

**Scoring summary (10 issues):** 5 implemented (≥4.2/5), 5 rejected (≤3.0/5).

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Toy model Hamiltonian cụ thể hơn | 2.0/5 | **Rejected** — v81 genre boundary: paper is phenomenological null test, not theory derivation |
| 2 | "Chỉ đổi coordinate/gauge" defense | 2.5/5 | **Rejected** — Lemma 1 + φ-scramble + numerical illustration already sufficient (v79 #3 precedent) |
| 3 | Novelty phụ thuộc "chưa ai sweep θ" | 4.5/5 | **Implemented** — §3.5 "Distinction from LF optimization": LF inequality coefficients are structurally independent of θ; θ is genuine independent DoF orthogonal to LF constraint surface |
| 4 | β parameter motivation scale | 3.0/5 | **Rejected** — Already at §5.3 (SME <10⁻²³, CSL ~10⁻¹⁶, weak-meas ~10⁻²); v79 #4/v73 #2/v64 #3 all rejected |
| 5 | Cắt ~25% defensive | 4.2/5 | **Implemented** — §3.5 "Search audit" + "Prior work" merged (80% duplicate, −8 lines) |
| 6 | Theorem "obvious" → emphasize experiment | 4.5/5 | **Implemented** — §1 opening: +1 sentence previewing protocol contribution. §9 rebalanced: finding→consequence flow replaces theorem-name-first |
| 7 | "Blind spot" softer wording | 3.0/5 | **Rejected** — Oscillation (v61 #2, v79 #6); v84 already scoped with "for the overlap-only class" |
| 8 | Consolidate "not replacing QM" disclaimers | 4.5/5 | **Implemented** — §2.3: removed redundant "β is a search parameter, not a theory prediction" from SME closing (duplicate of opening). "Why overlap-only?" closing trimmed (−10 words) |
| 9 | Tolerance simulation in main text | 2.5/5 | **Rejected** — S2 by design (v57 compression); angular tolerance ±11° already in §4.1; v76 #4/v74 #4 precedent |
| 10 | Information-theoretic interpretation | 4.2/5 | **Implemented** — §2.3 Physical context: +3 lines. |⟨b\|d⟩|² = cos²(θ/2) is fidelity between basis states; quantifies basis distinguishability → accessible information |

### Implemented changes (v85)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 3 | §3.5 | **θ as independent LF DoF (+3 lines):** Added to "Distinction from LF optimization": "The LF inequality coefficients (Eq. 1) are structurally independent of θ — the polar angle enters only through the correlator values, which are free parameters in any LF test. θ is therefore a genuine independent degree of freedom orthogonal to the LF constraint surface; LF optimization treats θ as a fixed convention, not as a variable to be tested." | 4.5/5 | Novelty has relied on "nobody varied θ" — an empirical claim. This adds a structural claim: LF inequalities DO NOT constrain θ, so varying it is genuinely new physics reach, not just a literature gap. Makes novelty independent of N=2. |
| 5 | §3.5 | **Search audit + Prior work merged (−8 lines):** Two paragraphs (~13 + 6 = 19 lines) merged into one (11 lines). Removed repeated enumeration of 4 databases, ~200 screened → 47 full-text → 2 identified, Boolean query detail, search period — stated once instead of twice. Key findings preserved: no published EWF varies θ, azimuthal angles optimized, θ fixed without comment, unpublished caveat. | 4.2/5 | "Search audit" (v67) and "Prior work" (v63-v67) accumulated independently. Both describe the same search — databases, screening pipeline, result count. Merging eliminates ~80% overlap. Different from prior "cắt defensive" rounds (v79 #5, v61 #6) which targeted general hedging — this is a specific structural duplicate. |
| 6 | §1, §9 | **Experimental consequence foregrounded:** §1 opening: +1 sentence — "This paper identifies a geometric fixed point shared by all published implementations — and proposes a single-waveplate protocol that breaks it." §9: theorem-as-name opening → finding-then-consequence flow. "The central result is the equatorial cancellation theorem (Proposition 1)..." → "All published optical EWF implementations have operated at an equatorial fixed point (θ = π/2) where every overlap-dependent deformation vanishes identically (Proposition 1)..." | 4.5/5 | §1 previously opened with generic EWF context → Proposition 1 theorem statement. Reader sees "trivial math" before "why it matters." New opening previews BOTH contributions (finding + protocol) in sentence 3. §9 rebalanced: finding leads, theorem named parenthetically, protocol paragraph stands as equal partner. |
| 8 | §2.3 | **Disclaimer consolidation (−15 words):** (i) SME paragraph closing: "β is a search parameter, not a theory prediction; a null result at" → "β is a search parameter; a null result at" (redundant with opening "No existing theory predicts this specific form"). (ii) "Why overlap-only?" closing: "This prioritization is methodological, not predictive: the class is chosen as the natural first null test; whether nature exhibits overlap-dependent deformation is precisely what the experiment tests" → "This prioritization is methodological, not predictive — the experiment tests whether nature exhibits overlap-dependent deformation." | 4.5/5 | v79 #5 rejected consolidating SME across 5 locations. This is different: trimming within-§2.3 redundancy where "not a theory prediction" appears in both SME paragraph opening AND closing. Second occurrence adds no new information. |
| 10 | §2.3 | **Information-theoretic interpretation (+3 lines):** Added to Physical context ¶1: "Information-theoretically, |⟨b\|d⟩|² = cos²(θ/2) is the fidelity between measurement basis states — it quantifies basis distinguishability, which controls accessible information in any quantum measurement [18]." | 4.2/5 | Addresses "why should nature care about overlap?" without violating v81 genre boundary. Basis distinguishability is a standard QI concept — not new physics. The overlap is not an arbitrary scalar; it's the fidelity between measurement bases, a quantity with operational meaning in quantum information. Grounds the overlap-only class in known QI structure. |

### Regression
Δ: §1 +1 sentence (contribution preview). §2.3 Physical context +3 lines (QI interpretation). §2.3 SME −5 words (dedup close). §2.3 Why overlap-only −10 words (dedup close). §3.5 −8 lines (merge). §3.5 Distinction from LF +3 lines (θ as independent DoF). §9 rebalanced (content preserved, emphasis shifted). Net: ~−5 lines. C1/C3/C10/C17 preserved. Title unchanged (v80 freeze). All v84 changes retained.

---

## v84 (2026-05-26) — 3/3-issue RCA (threshold 4.5/5): Abstract "overlap-only" qualifier; §2.3 Physical context expanded; §8.2 + S3 trimmed

*Re-application of v82 changes after session compaction reverted to v81. Title preserved at v77/v81 wording (no title change).*

**Scoring summary (3 issues):** 3 implemented (≥4.2/5).

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Abstract overclaim: "blind spot" without scope qualifier implies universal | 4.8/5 | **Implemented** — Abstract S1: "blind spot" → "blind spot for the overlap-only class: both operate at θ = π/2..." Merged hook + theorem into single sentence. |
| 2 | Physical motivation weak: "simplest class" needs physics grounding | 4.2/5 | **Implemented** — §2.3 Physical context expanded (3→9 lines): two short paragraphs connecting to weak measurement [18] structural analogue, decoherence precedent, and registration-layer coupling. "Speculative mechanism, not a derivation" label preserved. |
| 3 | §8.2 + S3 verbose: interpretive detail dilutes theorem+protocol | 4.5/5 | **Implemented** — §8.2: 25→15 lines (−10). S3.3 interpretations: 40→15 lines (−25, ~60%). S3.4 multi-observer: 10→5 lines. S3.1 contextuality: light trim. |

### Implemented changes (v84)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | Abstract S1 | **Scope qualifier (+4 words):** "share an unnoticed geometric blind spot" → "share an unnoticed geometric blind spot for the overlap-only class: both operate at θ = π/2, where every overlap-dependent deformation...vanishes identically (Proposition 1, equatorial cancellation theorem)." Hook + theorem merged into single sentence. "We prove..." removed as separate sentence (redundant with Proposition 1 naming). | 4.8/5 | S1 without "overlap-only" qualifier implies universal geometric blind spot. Added qualifier immediately scopes the claim. Merge with theorem statement eliminates the 1-sentence gap where reader could form wrong impression. Abstract retains 5-sentence structure (was 6); wording more modest. |
| 2 | §2.3 | **Physical context expanded (+6 lines):** Old: 3 lines (weak measurement + decoherence mention + S3 pointer). New: two short paragraphs — ¶1: weak measurement structural analogue (A_w depends on postselection overlap → basis-alignment dependence is known feature) + decoherence precedent (basis-alignment-dependent coherence loss). ¶2: overlap-only class as parametrization of residual geometric coupling between bases in sequential observation — coupling QM factorization sets to zero but has structural analogues in established phenomena. | 4.2/5 | v69 reduced physical context (12→2 lines, RCA 4.7/5); v74 expanded (2→4, user-persistence); v81 strategic "không cần physics motivation." User request differs: connect to EXISTING physics (weak measurement [18], decoherence, registration), not invent theory. All content grounded in [18]; label preserved. |
| 3 | §8.2, S3.1–S3.4 | **Trim (−35 lines net):** §8.2: θ-sweep (8→5 lines, blind protocol preserved), multi-observer (3→2), platform independence (6→4), locality closure (5→3). S3.1: prose compressed. S3.3: 5 interpretations 40→15 lines (~60% cut; each 7-8→3 lines). S3.4: 10→5 lines. Key message "none predicts, none precludes" preserved. | 4.5/5 | Paper ~4 pages. Theorem + protocol are the core strength. S3.3's detailed interpretation analysis (40 lines for 5 interpretations) disproportionate for phenomenological null-test paper. Core message retained: interpretation-neutral, none predicts Eq. (2-3), none precludes it. |

### Regression
Δ: Abstract S1 +4 words + merge with theorem (−1 sentence, net −22 words). §2.3 +6 lines. §8.2 −10 lines. S3 −30 lines. Net: paper stays ~4 pages. Title unchanged (v80 freeze respected). C1/C3/C10/C17 preserved. No claim changes. "Systematically unexplored" (v79) preserved. N=2 acknowledgment (v75) preserved. β-SME clause (v76) preserved.

---

## v81 (2026-05-26+) — Strategic clarification: Paper genre / physics-motivation boundary

**Not a version change — meta-note recorded in CHANGELOG for future reference.**

### Paper genre: Phenomenological null test with geometric insight

| This paper IS | This paper IS NOT |
|---------------|-------------------|
| "Có một blind spot hình học — hãy test nó" | "Có lý do vật lý mạnh để blind spot này chứa new physics" |
| Geometric insight + experimental protocol | Theory derivation of deformation |
| SME-style: define quantitative target in unconstrained parameter space | Predict new physics from underlying theory |

### Strategic rationale

- Không có theory nào predict overlap-dependent deformation → **bịa physics motivation sẽ là không trung thực, reviewer càng bắt bẻ**
- Sức mạnh của paper nằm ở **geometry insight gốc** (θ = π/2 là fixed point cho MỌI overlap-only deformation — mathematical fact) + **protocol simplicity** (1 waveplate, ~1h)
- §2.3 "Physical context" đã gợi ý weak measurement/decoherence connection với label "speculative mechanism, not a derivation" — đây là mức độ đúng
- SME [15] không chứng minh Lorentz violation phải tồn tại; nó nói "có coefficients chưa constrain, đây là cách đo" — paper này làm cùng một việc

### Decision
**Paper không cần thêm physics motivation.** Đây là lựa chọn chiến lược đúng, không phải điểm yếu. Mọi RCA suggestion "thêm lý do vật lý mạnh" trong tương lai → auto-reject (genre boundary, không phải text-level gap).

---

## v81 (2026-05-26) — 1/1-issue RCA (threshold 4.5/5): Proietti BSM→equatorial equivalence caveat — "Both happen to be equatorial"→"Both correspond to equatorial symmetry conditions"

**Scoring summary (1 issue):** 1 implemented (4.8/5).

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | "Both happen to be equatorial" overclaim — Proietti dùng BSM, không explicit set θ | 4.8/5 | **Implemented** — 2 locations: (i) "Both happen to be equatorial"→"Both correspond to equatorial symmetry conditions — for Bong et al. this is direct (θ = π/2); for Proietti et al. the equivalence follows from the BSM structure (see footnote [a])." (ii) "(both equatorial)"→"(both effectively equatorial; see footnote [a])." |

### Implemented changes (v81)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §3.5 | **BSM equivalence caveat:** Phân biệt Bong (direct θ = π/2) vs Proietti (BSM → effective |⟨b\|d⟩\|² = 1/2). Footnote [a] đã có derivation, giờ language trong text phản ánh rằng Proietti case là equivalence, không phải direct setting. | 4.8/5 | Proietti 2019 không viết "θ = π/2" — họ dùng Bell-state measurement. Map BSM sang equatorial condition là diễn giải thêm. "Both happen to be equatorial" ngụ ý cả hai explicit set θ, gây overclaim. Distinction Bong=direct / Proietti=equivalence chính xác, an toàn với reviewer. Claim A không đổi — gap vẫn là chưa ai vary θ khỏi equatorial condition. |

### Regression
Δ: §3.5 +2 lines (Bong/Proietti distinction). C1/C3/C10/C17 preserved.

---

## v80 (2026-05-26) — 1/4-issue RCA (threshold 4.5/5): Title change REVERTED (RCA overreach); 3 other points REJECTED; **TITLE FROZEN**

**Scoring summary (4 issues):** 0 implemented, 1 reverted (RCA overreach), 3 rejected (≤3.5/5).

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | "Systematically unexplored" → "not yet probed" | 2.5/5 | **Rejected** — Oscillation. v79 vừa set "systematically unexplored." |
| 2 | Tách phenomenology (SME) khỏi toy model | 3.0/5 | **Rejected** — §2.3 đã tách rõ. |
| 3 | Title "Blind to" → trung tính hơn | 4.5/5 → **REVERTED** | RCA sai — title là high-level identity element, không thuộc phạm vi RCA chỉnh sửa thông thường. User override. **Title frozen at v77 wording.** |
| 4 | β~0.04 combined + θ-sweep emphasis | 3.5/5 | **Rejected** — Đã có ở §5.3 + §6 + §8.2. |

### RCA post-mortem (title)
Title "Have Optical Wigner's Friend Experiments Been Blind to a Geometric Degree of Freedom?" được set tại v77 (scope: "Has Every"→"Have Optical"). RCA v80 sai khi approved title change — title là identity element, vượt quá phạm vi RCA text-level review. **Title hiện tại frozen. Mọi thay đổi title trong tương lai phải do user trực tiếp yêu cầu, không qua RCA pipeline.**

### Regression
Δ: Không có thay đổi nội dung nào. Title restored về v77 wording. C1/C3/C10/C17 preserved.

---

## v79 (2026-05-26) — 1/6-issue RCA (threshold 4.5/5): "structurally untested"→"systematically unexplored" (4 occurrences); 5 other points REJECTED

**Scoring summary (6 issues):** 1 implemented (4.5/5), 5 rejected (≤3.5/5).

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Overlap-only model ad-hoc → nhấn mạnh EFT/SME benchmark framework | 3.0/5 | **Rejected** — Already framed as SME benchmark at 4 locations (abstract, §1, §2.3, §5.3). "Benchmark parametrization" + "serves only to quantify experimental sensitivity" + "not a theory prediction." |
| 2 | "Structurally untested" quá mạnh với N=2 → "systematically unexplored" | 4.5/5 | **Implemented** — 4 occurrences replaced: §1 ¶2, §1 Claim A, §2.3, §9 Conclusion. "Untested" ngụ ý field lẽ ra phải test; "unexplored" là observational fact. |
| 3 | "Chỉ đổi basis chứ không có physics mới" → strengthen operational distinction + simulation | 3.0/5 | **Rejected** — Lemma 1 (§3.2) đã chứng minh cos θ không thể bị hấp thụ bởi basis redefinition. φ-scramble control (§7) đã phân biệt geometric signal với birefringence artifacts. |
| 4 | β arbitrary → connect với weak measurement/contextuality/decoherence scales | 3.5/5 | **Rejected** — Connections đã có: weak measurement + decoherence ở §2.3 "Physical context"; contextuality distinction table ở §3.2; ~10⁻² weak-measurement scale ở §5.3. |
| 5 | Paper dài và defensive → cắt repeated disclaimer, nhất là SME | 3.5/5 | **Rejected** — SME ở 5 vị trí: abstract (1 clause), §1 (7 words), §2.3 (full argument), §5.3 (2 refs). Cắt §1 parenthetical chỉ tiết kiệm 7 từ. Cắt §2.3 SME argument sẽ giảm persuasive power. |
| 6 | "Hidden null geometry" narrative thay vì "new physics deformation" | 3.0/5 | **Rejected** — Current narrative đã là "hidden null geometry": hook = "blind spot," theorem = "geometric null point," title = question về blindness. "New physics" framing chỉ có ở proposal section (§4-7) và đã được gọi là "null test." |

### Implemented changes (v79)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 2 | §1 ¶2, §1 Claim A, §2.3, §9 | **"structurally untested"→"systematically unexplored" (4 occurrences, replace_all):** "remained structurally untested" → "remained systematically unexplored"; "leaves the overlap-only class structurally untested" → "leaves the overlap-only class systematically unexplored"; "equatorial measurements leave structurally untested" → "equatorial measurements leave systematically unexplored." | 4.5/5 | "Untested" carries implicit criticism — the field SHOULD have tested this. Với N=2, đó là overstatement. "Unexplored" là observational: θ chưa từng được systematically varied, đó là fact, không phải accusation. Softer, equally accurate, phù hợp với N=2. |

### Regression
Δ: 4 từ thay đổi (mỗi occurrence 2 từ). C1/C3/C10/C17 preserved. Không thay đổi claim nào — chỉ thay đổi mức độ assertion. "Systematically unexplored" vẫn communicate đúng gap: chưa ai systematically probe θ.

---

## v78 (2026-05-26) — 1/4-issue RCA (threshold 4.5/5): Abstract hook precision ("All published"→"The two"); β positive-reason + Phase 1 emphasis + §2.3/§3.2 overlap REJECTED

**Scoring summary (4 issues):** 1 implemented (4.5/5), 3 rejected (≤3.5/5).

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | "All published optical" → ngụ ý large field, thực tế N=2 | 4.5/5 | **Implemented** — Abstract hook: "All published"→"The two published optical Wigner's Friend experiments..." Chính xác N=2, không inflate perceived sample size. |
| 2 | Chưa có lý do positive "tại sao class này đáng kiểm tra ngay bây giờ" | 3.5/5 | **Rejected** — Positive reasons đã có: §2.3 "Why overlap-only?" (geometric null + single waveplate), §3.5 "Scarcity as motivation" (low-cost). Abstract đã 6 câu, thêm positive reason sẽ quá dài. |
| 3 | Phase 1 screening — cần nổi bật hơn ở Abstract | 2.0/5 | **Rejected** — Lần thứ 10 (v68→v78). "loophole-open screening test" + "motivate — but not replace — Phase 2 closure" đã rõ. |
| 4 | Over-edited — §2.3 và §3.2 lặp ý overlap-only class | 3.0/5 | **Rejected** — §2.3 = motivation (WHY this class), §3.2 = formal definition (WHAT it is). Khác chức năng, không lặp nội dung. "Tin vào độc giả" là advice đúng nhưng không có redundant text cụ thể để cắt. |

### Implemented changes (v78)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | Abstract S1 | **Hook precision (1 word):** "All published optical" → "The two published optical Wigner's Friend experiments share an unnoticed geometric blind spot." | 4.5/5 | "All published" là phrasing chuẩn cho large literature — nhưng ở đây N=2. "The two" vừa chính xác tuyệt đối vừa giữ được rhetorical force: "The two...experiments share an unnoticed blind spot" vẫn là hook mạnh. Khác với prior N=2 defenses (thêm explanation) — đây là precision edit ở wording hook. |

### Regression
Δ: Abstract S1 thay 1 từ ("All"→"The two"). Abstract vẫn 6 sentences. C1/C3/C10/C17 preserved. Không thay đổi claim nào.

---

## v77 (2026-05-26) — 2/4-issue RCA (threshold 4.5/5): Abstract hook sentence ("unnoticed geometric blind spot"); §3.5 "Structural, not coincidental" paragraph; β-SME + Phase 1 REJECTED

**Scoring summary (4 issues):** 2 implemented (4.5/5), 2 rejected (≤2.0/5).

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | N=2 quá ít → giải thích non-optical experiments cũng không cover được gap | 4.5/5 | **Implemented** — §3.5: "Structural, not coincidental" paragraph (+7 lines). That both implementations are equatorial follows from LF optimization convention, not from small N. Any EWF experiment on any platform (optical, superconducting, trapped-ion) that optimizes LF violation would adopt θ = π/2 by default. Gap is structural, platform-agnostic. |
| 2 | β không có theory prediction → nhấn mạnh SME analogy ngay abstract | 1.0/5 | **Rejected** — Already implemented in v76. Abstract S3: "a search parameter whose methodological role parallels SME coefficients [15] (§2.3)." |
| 3 | Phase 1 loophole-open → Phase 2 là kết luận cuối, đừng để nghĩ Phase 1 đủ | 2.0/5 | **Rejected** — 8th consecutive rejection (v71→v77). Abstract S5: "loophole-open screening test whose positive result would motivate — but not replace — Phase 2 closure." §7: Phase 2 = "definitive conclusion." |
| 4 | Abstract hơi kỹ thuật nặng → thêm câu mở đầu nêu stake | 4.5/5 | **Implemented** — Abstract: "All published optical Wigner's Friend experiments share an unnoticed geometric blind spot." (9 words) trước S1 theorem statement. Tells reader WHY this matters trước khi nói WHAT was found. |

### Implemented changes (v77)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 4 | Abstract | **Hook sentence (+9 words):** "We prove..." → "All published optical Wigner's Friend experiments share an unnoticed geometric blind spot. We prove..." | 4.5/5 | Abstract trước đây mở đầu bằng "We prove an equatorial cancellation theorem..." — chính xác về mặt kỹ thuật nhưng không trả lời "why should anyone care?" trước khi nêu kết quả. PRA có broad audience; câu hook 9 từ tạo ngữ cảnh: tất cả thí nghiệm Wigner's Friend đều có chung một blind spot. Sau đó theorem statement giải thích blind spot đó là gì. |
| 1 | §3.5 | **"Structural, not coincidental" (+7 lines):** Sau "Tilting the Superobserver opens access to this previously untested sector (§4)," thêm paragraph giải thích: equatorial convention là hệ quả trực tiếp của LF optimization, không phải artifact của N=2 nhỏ. Bất kỳ EWF experiment nào trên bất kỳ nền tảng vật lý nào (optical, superconducting, trapped-ion) mà tối ưu LF violation đều sẽ adopt θ = π/2. Gap là structural, không phải coincidental. | 4.5/5 | N=2 là điểm yếu dai dẳng nhất của paper (v63→v76, 13 version defenses). Tất cả defense trước đây tập trung vào methodology (search audit, scope qualifier, "not a deficiency," scarcity→low-cost). Defense mới này là structural: gap không biến mất nếu có thêm experiment, vì MỌI EWF experiment tối ưu LF đều sẽ equatorial. Lập luận platform-agnostic, không cần cite thêm experiment cụ thể. |

### Regression
Δ: Abstract +1 sentence (9 words, hook). §3.5 +7 lines (structural argument). C1/C3/C10/C17 preserved. Abstract giờ 6 sentences (was 5 since v68). Hook sentence không thay đổi bất kỳ claim nào — chỉ thêm ngữ cảnh "why care."

---

## v76 (2026-05-26) — 1/4-issue RCA (threshold 4.5/5): Abstract S3 β-SME methodological clause; N=2 scoping + Phase 1 reframing + S1→main REJECTED

**Scoring summary (4 issues):** 1 implemented (4.5/5), 3 rejected (≤2.5/5).

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | N=2 survey mỏng → "hạ tông" nhất quán hơn ở abstract | 2.5/5 | **Rejected** — Abstract S2 đã nói "published optical EWF implementations" — chính xác là "trong phạm vi các thí nghiệm quang học đã công bố." v73+v75 đã xử lý scope qualifier + N=2 acknowledgment. Không còn chỗ nào trong abstract nói "chưa ai kiểm tra" mà thiếu scope. |
| 2 | β không có theory prediction → cần 1 câu abstract giải thích tại sao null test vẫn có giá trị | 4.5/5 | **Implemented** — Abstract S3: "providing minimum detectable β ~ 0.07 at 5σ — a search parameter whose methodological role parallels SME coefficients [15] (§2.3) — while preserving..." Giải thích WHY null test có giá trị khoa học dù không ai dự đoán β: giống như SME, giá trị nằm ở việc định nghĩa quantitative experimental target trong parameter space chưa được constrain. |
| 3 | Phase 1 loophole-open → đặt Phase 2 làm mục tiêu chính, Phase 1 là "feasibility check" | 2.5/5 | **Rejected** — 6th consecutive rejection (v71→v76). Abstract S5 đã rõ: "loophole-open screening test" + "motivate — but not replace — Phase 2 closure." §7: Phase 2 là "loophole-closed...definitive conclusion." Framing đã đặt Phase 2 làm đích đến; Phase 1 numerical emphasis là do Phase 1 là novel proposal, không phải do framing sai. |
| 4 | Supplemental S1-S3 chứa nội dung quan trọng → đưa vào main text cho PRA (đặc biệt proof S1) | 2.0/5 | **Rejected** — Trùng v74 #4 (2.0/5). BSM proof sketch đã ở footnote [a] (v70); Bloch sphere proof ở §3.3; search audit ở §3.5; error budget table ở §7. Key results đã trong main text; S1-S3 chứa supplementary detail phù hợp với venue. |

### Implemented changes (v76)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 2 | Abstract S3 | **β-SME methodological clause (+12 words):** "providing minimum detectable β ~ 0.07 at 5σ while preserving..." → "providing minimum detectable β ~ 0.07 at 5σ — a search parameter whose methodological role parallels SME coefficients [15] (§2.3) — while preserving..." | 4.5/5 | Abstract trước đây chỉ nói WHAT (β ~ 0.07, 5σ) mà không nói WHY null test với tham số không được theory nào dự đoán vẫn có giá trị. SME analogy là câu trả lời chuẩn: SME được đề xuất với 19 coefficients không có a priori predictions; giá trị khoa học nằm ở việc định nghĩa quantitative experimental targets. β phục vụ cùng chức năng phương pháp luận. Chưa từng có trong abstract; đây là lần đầu SME được flag ở abstract level. |

### Regression
Δ: Abstract S3 +12 words (SME methodological clause). Abstract vẫn 5 sentences. C1/C3/C10/C17 preserved. Không tạo repetition — SME giờ xuất hiện ở abstract + §1 + §2.3 + §5.3 (4 vị trí methodologically distinct).

---

## v75 (2026-05-26) — 3/4-issue RCA (threshold 4.5/5): Abstract N=2 acknowledgment; §1 Proposition 1 merge (−9 lines); §1 SME methodological flag; Phase 1 rewording REJECTED

**Scoring summary (4 issues):** 3 implemented (≥4.2/5), 1 rejected (2.5/5).

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | N=2 sample nhỏ → thêm acknowledgment trong abstract | 4.8/5 | **Implemented** — Abstract S2: "only two such implementations exist (Proietti 2019, Bong 2020), reflecting the experimental scarcity of this field." Khác với v74 #1 (body text) — đây là lần đầu N=2 được flag trực tiếp trong abstract. |
| 2 | Overlap-only class tự định nghĩa → nhấn mạnh SME comparison | 4.2/5 | **Implemented** (user-persistence exception) — §1 claims paragraph: "it proposes a null-test protocol (analogous in method to the Standard Model Extension [15]; §2.3)." Brief parenthetical flag; SME argument đầy đủ vẫn ở §2.3. |
| 3 | Phase 1 screening → "nói thẳng là screening test, không phải bằng chứng" | 2.5/5 | **Rejected** — 6th consecutive rejection (v71→v75). Abstract S5 đã nói rõ: "loophole-open screening test" + "motivate — but not replace — Phase 2 closure." Nội dung đã đủ. |
| 4 | Introduction quá dài, lặp Proposition 1 → cắt bớt | 4.7/5 | **Implemented** — §1 Proposition 1 merged từ 2 mô tả song song (23 dòng) → 1 unified (14 dòng, −9 lines, −39%). |

### Implemented changes (v75)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | Abstract S2 | **N=2 acknowledgment (+1 line):** "A complete survey...finds none have varied this polar angle" → "...none have varied this polar angle; only two such implementations exist (Proietti 2019, Bong 2020), reflecting the experimental scarcity of this field." | 4.8/5 | Abstract chưa từng explicitly acknowledge sample size. Prior defenses (v70 "Scarcity as motivation," v72 "not a deficiency of the search") đều ở §3.5 body text. Reviewer đọc abstract không biết N=2 cho đến khi tới §3.5 — cảm giác như hidden weakness. Proactive acknowledgment trong abstract biến potential objection thành honest limitation. Khác scope với v74 #1 (body text explanation). |
| 2 | §1 | **SME methodological flag (+7 words):** "it proposes a null-test protocol" → "it proposes a null-test protocol (analogous in method to the Standard Model Extension [15]; §2.3)." | 4.2/5 | SME parallel là lập luận mạnh nhất bào chữa cho "no underlying theory" — nhưng trước đây chỉ xuất hiện từ §2.3. Reviewer hình thành objection "self-defined class" khi đọc §1 có thể không tới §2.3 với open mind. Brief parenthetical flag sớm, không tạo repetition (SME giờ ở §1 + §2.3 + §5.3 — methodologically distinct locations). Dưới 4.5/5 nhưng accepted per user-persistence exception (v74 precedent). |
| 4 | §1 | **Proposition 1 merge (−9 lines, 23→14, −39%):** Hai mô tả song song merged thành 1 unified flow: (1) formal definition → (2) theorem → (3) novelty/finding → (4) Lemma 1. | 4.7/5 | §1 gốc mô tả Proposition 1 hai lần: formal (old lines 37-49) + accessible re-description (old lines 50-60). Hai mô tả tích lũy qua nhiều version không được consolidate. Merged version cho reader mỗi idea đúng 1 lần. Formal definition cũng có ở §3.2; giữ compact version trong §1 đảm bảo self-contained readability. Chưa có CHANGELOG rejection nào; v72 §2.3 condensation là precedent. |

### Regression
Δ: Abstract +1 line (N=2); §1 −9 lines (Proposition 1 merge) + 7 words (SME flag). Net: §1 ~8 lines shorter. No claim changes. C1/C3/C10/C17 preserved. All regression watchlist items intact.

---

## v74 (2026-05-26) — 1/4-issue RCA (threshold 4.5/5): "Physical context" expanded with speculative mechanism; N=2 + Phase 1 + S1 merge REJECTED

**Scoring summary (4 issues):** 1 accepted (4.2/5, user-persistence exception), 3 rejected (<4.5/5).

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | N=2 pool nhỏ → giải thích rõ hơn | 3.5/5 | **Rejected** — Already explained in §3.5 prose: "The small number reflects the reality of the field...not a deficiency of the search" (v72) + "Scarcity as motivation" paragraph... |
| 2 | Overlap-only class → ví dụ cơ chế vật lý speculative | 4.2/5 | **Accepted** (user-persistence exception — 4th request). "Physical context" expanded from 2-line S3 pointer to 4-line speculative example: "If the Superobserver's measurement... |
| 3 | Phase 1 screening emphasis in abstract | 2.0/5 | **Rejected** — 5th consecutive rejection (v71→v72→all-reject→v73→v74). Abstract S5 already: "loophole-open screening test whose positive result would motivate — but not replace —... |
| 4 | Merge S1 proof vào main text cho PRA | 2.0/5 | **Rejected** — Full proof already in §3.3 (Bloch sphere algebra). BSM proof sketch in footnote [a] (v70). S1 contains supplementary detail (query logs, extended derivations) —... |

### Regression
Δ: §2.3 gains 2 lines. Explicitly labeled speculative — does not undermine the methodological-choice framing. C1/C10/C17 preserved.
---

## v73 (2026-05-26) — 1/3-issue RCA (threshold 4.5/5): §1 scope qualifiers moved earlier; β comparison + Phase 1 REJECTED

**Scoring summary (3 issues):** 1 implemented (4.5/5), 2 rejected (<4.5/5).

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | "Một vài chỗ vẫn còn hơi overstate" — N=2 survey | 4.5/5 | **Implemented** — Two scope qualifiers moved earlier in §1: (i) "in actual EWF implementations"→"in published optical EWF implementations" (line 52); (ii) "class that has remained... |
| 2 | β magnitude comparison — "neo giá trị β vào bối cảnh" | 3.5/5 | **Rejected** — Magnitude comparison already in §5.3 (lines 562–570): SME <10⁻²³, CSL ~10⁻¹⁶ s⁻¹, weak measurement ~10⁻², with explicit "comparable to weak-measurement anomalies"... |
| 3 | Phase 1 screening emphasis in abstract | 2.5/5 | **Rejected** — Abstract S5 already says "loophole-open screening test whose positive result would motivate — but not replace — Phase 2 closure." "Screening test" + "motivate but... |

### Regression
Δ: Two phrases modified in §1 (3 words changed, 3 words added). No claim changes. C1/C3/C10/C17 preserved.
---

## v72 (2026-05-26) — 2/4-issue RCA (threshold 4.5/5): §2.3 condensation (−7 lines, duplicate reason cut); "not a deficiency of the search" (§3.5); physical motivation + Phase 1 REJECTED

**Scoring summary (4 issues):** 2 implemented (≥4.0/5), 2 rejected (<4.5/5).

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Overlap-only class chưa có động cơ vật lý → thêm cơ chế decoherence/weak measurement | 2.0/5 | **Rejected** — Textbook oscillation. Weak measurement content was: removed in v53 → restored in v55 → moved to S3 in v69 (RCA 4.7/5: "Keeping a 12-line plausibility argument in... |
| 2 | 2 thí nghiệm → "sample quá nhỏ, sao kết luận được?" | 4.0/5 | **Implemented** — Added "not a deficiency of the search" to §3.5: "The small number reflects the reality of the field — optical EWF implementations remain rare — not a deficiency... |
| 3 | Phase 1 framing → screening rõ hơn + fast path to Phase 2 | 2.8/5 | **Rejected** — Already in abstract S5 ("loophole-open screening test whose positive result would motivate — but not replace — Phase 2 closure") and §7 ("same optical configuration... |
| 4 | §2.3 cần tóm gọn hơn | 4.5/5 | **Implemented** — "Why overlap-only?" paragraph condensed 21→14 lines (−33%): (a) removed reason (ii) "simplest scalar coupling" which verbatim duplicated the opening paragraph's... |

### Implemented changes (v72)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 4 | §2.3 | **"Why overlap-only?" condensation (−7 lines, 21→14):** Two cuts: (a) Removed prioritization reason (ii) "it targets the simplest scalar coupling — any deformation engaging measurement statistics with prior outcomes must involve basis overlap at... |⟨b\| d⟩\ |² is the simplest scalar...Any deformation...must depend on this relationship at lowest order." The opening already makes this point; listing it again as a separate reason was redundant. Renumbered 3 reasons → 2. (b) Compressed methodological-choice framing: "the overlap-only class is chosen as the natural first null test because it combines a sharp geometric prediction (Proposition 1) with minimal experimental cost (one waveplate). Whether nature exhibits overlap-dependent deformation is precisely what the experiment tests — the class definition makes no claim that nature must conform to it" → "the class is chosen as the natural first null test; whether nature exhibits overlap-dependent deformation is precisely what the experiment tests." The removed content restates reasons (i) and (ii) in prose form — the reader just read them. | 4.5/5 | The "Why overlap-only?" paragraph accumulated across 4 versions (v54 base + v66 prioritization + v68 methodological framing). Each addition was individually justified but collectively they created a 21-line paragraph where the same idea ("simplest scalar, lowest order") appeared three times. After the cut, the paragraph has a clean structure: (1) what overlap is and why it's minimal, (2) why Level 0 is tested first (2 reasons), (3) admission that this is methodological, not predictive. The reader encounters each idea exactly once. |
| 2 | §3.5 | **"Not a deficiency of the search" (+few words):** "The small number reflects the reality that optical EWF implementations remain rare" → "The small number reflects the reality of the field — optical EWF implementations remain rare — not a... | 4.0/5 | The N=2 survey has been defended through multiple angles: v63 contextualized rarity, v67 added search audit, v70 added scarcity→low-cost reframing,... |

### Regression
Δ: §2.3 −7 lines; C1/C3/C10/C17 preserved.
---

## v71 (2026-05-26) — 3/5-issue RCA (threshold 4.5/5): β repetition cut (−2 occurrences); "sensitivity"→"minimum detectable β"; inclusion criteria in §3.5 search audit; survey rename + scope-in-abstract + Phase 1 consolidation REJECTED

**Scoring summary (5 issues):** 3 implemented (≥4.2/5), 2 rejected (<4.5/5), 1 already-present (scope in abstract).

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | "Complete survey" → rename + thêm filter criteria | 2.5/5 (rename) + 4.2/5 (criteria) | **Rejected** (rename — 5th attempt, oscillation). **Implemented** (criteria) — Inclusion criteria added to §3.5 search audit: "optical EWF implementation with Friend+Superobserver... |
| 2 | "sensitivity" mơ hồ → "minimum detectable β" | 4.5/5 | **Implemented** — "providing sensitivity β ~ 0.07 at 5σ"→"providing minimum detectable β ~ 0.07 at 5σ" in abstract S3 + §1. "Minimum detectable" is operationally precise: it tells... |
| 3 | Abstract không nói rõ scope limitation | 2.5/5 | **Rejected** — Already present in abstract S4: "The theorem constrains the minimal overlap-only class; broader deformation classes (Levels 1–3, §3.2) lie outside its scope." S1... |
| 4 | Phase 1 messaging scattered → cần gom 1 chỗ | 3.0/5 | **Rejected** — Already clearly stated in two locations: abstract S5 ("loophole-open screening test whose positive result would motivate — but not replace — Phase 2 closure") + §7... |
| 5 | β-search-parameter lặp ~4 lần → cắt repetition | 4.8/5 | **Implemented** — Two cuts: (i) §1 cross-ref removed (v70 addition: "— β is a search parameter, not a theory prediction (§2.3) —" created a 4th occurrence); (ii) §2.3 SME... |

### Implemented changes (v71)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 5 | §1, §2.3 | **β repetition cut (−2 occurrences):** §1: removed v70 cross-ref "— β is a search parameter, not a theory prediction (§2.3) —" reverting to v69 text. §2.3: removed duplicate closing sentence "The parametrization defines quantitative experimental... | 4.8/5 | The β-search-parameter idea accumulated across versions: v54 (no existing theory, §5.3), v65 (SME analogy, §2.3), v70 (cross-ref, §1). Each addition... |
| 2 | Abstract, §1 | **"sensitivity"→"minimum detectable β":** Abstract S3: "providing sensitivity β ~ 0.07 at 5σ"→"providing minimum detectable β ~ 0.07 at 5σ." §1: same change. | 4.5/5 | "Sensitivity" is ambiguous — it could mean the apparatus is sensitive to β values AS LOW AS 0.07 (which is correct) or that the apparatus can MEASURE... |
| 1 | §3.5 | **Inclusion criteria (+3 lines):** Added to search audit: "Inclusion criteria: optical EWF implementation with Friend+Superobserver structure, published in peer-reviewed venue or arXiv, reporting measurement settings from which polar angle θ can be... | 4.2/5 | The search audit (v67) listed databases and screening numbers but not WHAT qualified a paper for inclusion. A reviewer could ask: "How do I know you... |

### Regression
Δ: §1 loses 1 line (cross-ref removed); §2.3 loses 1 line (duplicate sentence removed); §3.5 gains 3 lines (inclusion criteria). "Sensitivity"→"minimum detectable" is a terminology change with no content delta. No C1/C3/C10/C17 violations. All regression watchlist items intact.
---

## v70 (2026-05-26) — 4/5-issue RCA (threshold 4.5/5): BSM proof sketch in footnote [a]; scarcity→low-cost reframing (§3.5); β search-parameter cross-ref (§1); Phase 1→2 optical continuity (§7); "complete survey" REJECTED (oscillation)

**Scoring summary (5 issues):** 4 implemented (≥4.0/5), 1 rejected (<4.5/5).

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | "Complete survey" nghe tự tin — chỉ 2 paper | 2.5/5 | **Rejected** — Oscillation: fourth rename in 4 versions (v67: systematic survey → v68: exhaustive search → v69: complete survey → candidate). Current wording ("complete survey of... |
| 2 | β ~ 0.07 không có lý do vật lý — SME framing chìm | 4.0/5 | **Implemented** — β search-parameter cross-ref added to §1: "providing sensitivity β ~ 0.07 at 5σ (single-setting) — β is a search parameter, not a theory prediction (§2.3) —... |
| 3 | Phase 1 bị dismiss — cần timeline song song | 4.0/5 | **Implemented** — Phase 1→2 optical continuity added to §7: "The same optical configuration serves both phases — only the detectors change — so Phase 2 can proceed immediately... |
| 4 | S1, S2, S3 referenced nhiều không có trong bản | 4.7/5 | **Implemented** — Footnote [a] expanded from 2-line assertion deferring to S1 → 5-line self-contained proof sketch: BSM projects onto 4 Bell states; equal probability + equal... |⟨b\|d⟩\|² = 1/2, identical to equatorial condition §3.3. Full derivation still in S1 but main text is now self-contained |
| 5 | Chỉ 2 thí nghiệm — điểm yếu nhất → reframe | 4.7/5 | **Implemented** — "Scarcity as motivation" paragraph (+9 lines) added to end of §3.5: "The small number of optical EWF implementations — precisely two in two decades — is itself... |

### Implemented changes (v70)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 4 | §3.5 fn[a] | **BSM proof sketch (+3 lines):** Old: "BSM projects onto the Bell basis; \ |⟨ψ\| Φ⁺⟩\ |² = 1/2 for all outcome pairs, functionally equivalent to equatorial measurement (see Supplemental S1 for the derivation)." New: "BSM projects onto the four Bell states...For the singlet-state source used in Proietti et al., each Bell outcome occurs with equal probability and leaves the Friend's recorded outcome equally likely to be H or V — the effective \|⟨b\|d⟩\|² = 1/2 for all (b,d) pairs, identical to the equatorial condition θ = π/2 derived in §3.3. Full derivation in Supplemental S1." | 4.7/5 | The BSM=equatorial claim is load-bearing: Proietti et al. (2019) is one of only two experiments in the survey, and its inclusion depends entirely on the functional-equivalence argument. Deferring the proof entirely to S1 creates a dependency where a skeptical reader cannot assess the claim without the supplemental. The expanded footnote makes the main text self-contained: it states the mechanism (4 Bell states, equal probability), the consequence (1/2 overlap for all pairs), and the connection to §3.3 (identical to equatorial condition). S1 still holds the full derivation for readers who want it. |
| 5 | §3.5 | **Scarcity→low-cost reframing (+9 lines):** New paragraph at end of §3.5: "**Scarcity as motivation.** The small number of optical EWF implementations — precisely two in two decades — is itself an argument for the protocol proposed here. A dedicated... | 4.7/5 | The N=2 survey has been the paper's most persistent vulnerability (v63 contextualized it, v64 softened claims, multiple versions added caveats).... |
| 2 | §1 | **β search-parameter cross-ref (+1 line):** "providing sensitivity β ~ 0.07 at 5σ (single-setting) — β is a search parameter, not a theory prediction (§2.3) — while preserving..." | 4.0/5 | The SME analogy was developed in §2.3 (v65) and reinforced in §5.3, but §1 — where β first appears — gave no hint about what β IS. A reader... |
| 3 | §7 | **Phase 1→2 optical continuity (+3 lines):** After "into a definitive conclusion": "The same optical configuration serves both phases — only the detectors change — so Phase 2 can proceed immediately upon a positive Phase 1 signal without an... | 4.0/5 | The two-phase program (v62-v69) positioned Phase 1 as screening and Phase 2 as closure, but a reviewer could still ask: "If Phase 1 takes a year and... |

### Regression
Δ: §3.5 gains 12 lines (BSM proof + scarcity reframing); §1 gains 1 line (β cross-ref); §7 gains 3 lines (optical continuity). No claim changes. C1/C3/C10/C17 preserved. All regression watchlist items intact.
---

## v69 (2026-05-25) — 5/5-issue RCA (threshold 4.5/5): Abstract falsification clause; "exhaustive search"→"complete survey"; β origin hint; Phase 1≠Phase 2; "Physical context"→S3 pointer

**Scoring summary (5 issues):** 5 implemented (≥3.8/5), 0 rejected. Second all-accept round in paper history (after v63).

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Claim A thiếu falsification trong abstract | 4.7/5 | **Implemented** — "a null δ⟨AB⟩ across a full θ-sweep would falsify the overlap-only class" added to abstract S5 |
| 2 | "Exhaustive search" với N=2 → reviewer khắt khe sẽ hỏi | 3.8/5 | **Implemented** — "exhaustive search"→"complete survey" (abstract + §3.5). Oscillation flag: third rename in 3 versions (v67: systematic survey → v68: exhaustive search → v69:... |
| 3 | β=0.07 xuất hiện không rõ nguồn gốc trong abstract | 4.0/5 | **Implemented** — "θ = 31°" → "the optimal trade-off between signal strength and LF preservation (θ = 31°)" in abstract S3. The "while preserving" clause already communicated the... |
| 4 | Phase 1 bị loophole nhưng đặt ngang Phase 2 | 4.2/5 | **Implemented** — Abstract S5 reworked: "Phase 1 of a two-phase program with SNSPD-upgraded closure" → "loophole-open screening test whose positive result would motivate — but not... |
| 5 | Weak measurement connection (§2.3) mơ hồ — "plausibility argument" | 4.7/5 | **Implemented** — Full "Physical context" paragraph (12 lines: weak measurement + decoherence + toy model + plausibility disclaimer) replaced with compact pointer: "Basis-overlap... |

### Implemented changes (v69)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | Abstract S5 | **Falsification clause (+10 words):** "...a null δ⟨AB⟩ across a full θ-sweep would falsify the overlap-only class." | 4.7/5 | The abstract proposed a null test but never said what specific result would falsify the hypothesis. This is the most fundamental requirement of a... |
| 2 | Abstract S2, §3.5 | **"Exhaustive search"→"complete survey":** Abstract: "A complete survey of published optical EWF implementations..." §3.5: "within our complete survey scope." | 3.8/5 | Third rename (v67→v68→v69). The word "exhaustive" implies searching every possible source, which is an unverifiable claim. "Complete survey" is more... |
| 3 | Abstract S3 | **β origin hint (+6 words):** "θ = 31°" → "the optimal trade-off between signal strength and LF preservation (θ = 31°)." | 4.0/5 | The number 31° appears in the abstract without explanation. While §4.1 and §1 explain the FOM optimization, the abstract should give at least a hint... |
| 4 | Abstract S5 | **Phase 1≠Phase 2 relationship (+15 words):** "Phase 1 of a two-phase program with SNSPD-upgraded closure" → "loophole-open screening test whose positive result would motivate — but not replace — Phase 2 closure via SNSPD upgrade." | 4.2/5 | The old wording listed Phase 1 and Phase 2 as sequential equals. "Motivate but not replace" explicitly subordinates Phase 1 to Phase 2: a positive... |
| 5 | §2.3 | **"Physical context"→S3 pointer (−10 lines):** Old: 12-line paragraph covering weak measurement [18], decoherence, toy model, and plausibility disclaimer. New: 2-line pointer: "Basis-overlap dependence has precedent in weak measurement and... | 4.7/5 | This resolves a tension running from v53→v55→v68. v53 removed weak-measurement motivation; v55 restored it with a "plausibility argument" disclaimer;... |

### Regression
Δ: Abstract gains ~30 words (falsification + β origin + Phase 1≠2) but keeps 5-sentence structure. §2.3 loses 10 lines (Physical context→S3). C1/C3/C10/C17 preserved. All regression watchlist items intact.
---

## v68 (2026-05-25) — 4/5-issue RCA (threshold 4.5/5): Abstract rewrite (5 clean sentences, fewer symbols); "systematic survey"→"exhaustive search"; methodological-choice framing (§2.3); Phase 1 expectations REJECTED

**Scoring summary (5 issues):** 3 implemented (≥4.5/5), 2 rejected (<4.5/5). Note: Issue 3 (β comparison) was addressed implicitly by the abstract rewrite removing the contested phrase; the detailed weak-measurement comparison in §5.3 is retained.

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Overlap-only class thiếu lý do vật lý thuyết phục | 4.2→4.5/5 | **Implemented** — Explicit methodological-choice framing added to §2.3 "Why overlap-only?": "This prioritization is methodological, not predictive: the overlap-only class is... |
| 2 | "Systematic survey" với N=2 → đổi tên | 4.7/5 | **Implemented** — "systematic survey"→"exhaustive search" in Abstract line 2; "systematic search scope"→"exhaustive search scope" in §3.5. "Exhaustive search" is more accurate for... |
| 3 | β ~ 0.07 "comparable to weak-measurement ~10⁻²" — hai thứ khác nhau | — | **Addressed implicitly** — The contested phrase ("comparable to weak-measurement anomaly searches at the ~10⁻² scale [18]") was removed during the abstract rewrite. The detailed... |
| 4 | Phase 1 (η ≈ 0.87) — kỳ vọng cần hạ rõ hơn | 3.0/5 | **Rejected** — Already explicitly stated: "loophole-open screening test" (Abstract v68), "Phase 1 is a screening stage: a positive signal would motivate immediate Phase 2; a null... |
| 5 | Abstract quá dày đặc ký hiệu kỹ thuật cho Phys. Rev. A | 4.8/5 | **Implemented** — Abstract rewritten from 3 long symbol-dense sentences to 5 clean sentences. Removed: explicit formula P = P_QM · g(\ |⟨b\|d⟩\|²) / Z, function signature g: [0,1]→ℝ, "single-setting" qualifier, ~10⁻² comparison [18], "first isolated test within surveyed implementations", "loophole-open null test" (redundant with "loophole-open screening test"). Retained: Proposition 1, θ=π/2, β~0.07, 5σ, 8.6σ, fair-sampling, η≈0.87/0.91, scope hierarchy. Symbol count reduced ~40% |

### Implemented changes (v68)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 5 | Abstract | **Rewrite (14→14 lines, 3→5 sentences):** Old: 3 long sentences packed with symbols. New: S1 (Theorem), S2 (Survey gap), S3 (Proposal + sensitivity), S4 (Scope), S5 (Two-phase program). Symbol count reduced ~40%: removed P = P_QM·g(\ |⟨b\| d⟩\ |²)/Z, g:[0,1]→ℝ, ~10⁻² comparison, "single-setting", "first isolated test within surveyed implementations", redundant "loophole-open null test." Retained: Proposition 1, θ=π/2, β~0.07, 5σ, 8.6σ, fair-sampling, η≈0.87/0.91, scope hierarchy. | 4.8/5 | The abstract accumulated layers across v53-v67: v53 added "phenomenological null test" genre, v54 added illustrative benchmark + qualifiers, v55 added confident voice, v63 added two-phase, v65 added survey bridge, v66 added scope, v67 added β comparison. Each addition was individually justified but collectively the abstract became a dense thicket of notation — P = P_QM·g(\|⟨b\|d⟩\|²)/Z, g:[0,1]→ℝ, θ, β, σ, η, plus qualifiers and parentheticals. For Phys. Rev. A's broad audience, the abstract should communicate WHAT was found and WHY it matters without requiring the reader to parse a formula. The new 5-sentence structure follows: (1) theorem, (2) gap, (3) proposal, (4) scope, (5) limitations. Each sentence does one job. |
| 2 | Abstract, §3.5 | **"Systematic survey"→"exhaustive search":** Abstract S2: "An exhaustive search of published optical EWF implementations (Supplemental S1) finds none have varied this polar angle." §3.5: "Only two published optical EWF experiments exist within our... | 4.7/5 | "Systematic survey" conventionally implies a large body of literature with meta-analytic synthesis. With N=2, the term is misleading — a reviewer... |
| 1 | §2.3 | **Methodological-choice framing (+6 lines):** After Level 0 prioritization (v66), added: "This prioritization is methodological, not predictive: the overlap-only class is chosen as the natural first null test because it combines a sharp geometric... | 4.5/5 | The paper has long struggled with the "why this class?" question. v53 stripped GPT/weak-measurement motivation; v54 added "Why overlap-only?"... |

### Regression
Δ: Abstract restructured; C1/C3/C10/C17 preserved.
---

## v67 (2026-05-25) — 4/4-issue RCA (threshold 4.5/5): Survey search audit (§3.5); β ~10⁻² weak-measurement comparison (Abstract); error budget table (§7); scope limitation (Abstract)

**Scoring summary (4 issues):** 4 implemented (≥4.0/5), 0 rejected. First all-accept round since v63.

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Survey (S1) chưa công bố — reader không tự kiểm chứng được claim | 4.0/5 | **Implemented** — Compact search audit added to §3.5 table footnote: "Search audit: 4 databases...~200 titles screened → 47 full-text examined → 2 published optical EWF... |
| 2 | β ~ 0.07 — reviewer hỏi "tại sao có ý nghĩa?" | 4.7/5 | **Implemented** — Abstract: "sensitivity β ~ 0.07 at 5σ (single-setting) — comparable to weak-measurement anomaly searches at the ~10⁻² scale [18] — while preserving 8.6σ..." |
| 3 | Systematic error chỉ ở S2 — "nói có" không cho thấy số | 4.5/5 | **Implemented** — Compact 6-row error budget table added to §7: source name, control mechanism, vs-Poisson comparison. Qualitative conclusion preserved from S2; exact σ values... |
| 4 | Scope limitation (Level 1–3) buried ở §3.2 | 4.7/5 | **Implemented** — Abstract theorem sentence: "...geometric null point for the overlap-only class (Level 0 of a four-level deformation hierarchy; broader classes in §3.2 lie... |

### Implemented changes (v67)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §3.5 | **Search audit trail (+3 lines):** Added after survey table footnote [a]: "*Search audit:* 4 databases (Google Scholar, arXiv, Web of Science, InspireHEP), Jan 2000–May 2026; ~200 titles screened → 47 full-text examined → 2 published optical EWF... | 4.0/5 | The survey table (already in main text since v53) shows results but not process. A reader skeptical of the "all published EWF experiments are... |
| 2 | Abstract | **β scale comparison (+1 line):** "with sensitivity β ~ 0.07 at 5σ (single-setting) — comparable to weak-measurement anomaly searches at the ~10⁻² scale [18] — while preserving 8.6σ..." | 4.7/5 | The "why is β = 0.07 meaningful?" question is the #2 reviewer reflex after "β is arbitrary." The weak-measurement ~10⁻² scale provides an immediate,... |
| 3 | §7 | **Error budget table (+11 lines):** Replaced single sentence naming six sources with a compact 6-row table: Source / Controlled by / vs. Poisson. All six sources individually < Poisson; RSS total below Poisson floor. Exact σ values and Monte Carlo... | 4.5/5 | v57 compressed §7 from 67→12 lines (RCA 4.7/5), correctly moving detailed analysis to S2. However, the compression removed ALL quantitative structure... |
| 4 | Abstract | **Scope limitation (+1 line):** "geometric null point for the overlap-only class (Level 0 of a four-level deformation hierarchy; broader classes in §3.2 lie outside the theorem's scope)." | 4.7/5 | The abstract previously said "entire overlap-only class" which a scanning reviewer might read as "all possible deformations." The scope qualifier... |

### Regression
Δ: Abstract gains ~2 lines (scope + β scale); §3.5 gains 3 lines (search audit); §7 gains 11 lines (error budget table). No claim changes. C1/C3/C10/C17 preserved. v57 compression not undone (67→12→23 lines, still −66% from pre-v57). All regression watchlist items intact.
---

## v66 (2026-05-25) — 2/4-issue RCA (threshold 4.5/5): Level 0 prioritization (§2.3); LF-violation vs β disentanglement (§4.1); survey-scope expansion and abstract fair-sampling REJECTED

**Scoring summary (4 issues):** 2 implemented (≥4.5/5), 2 rejected (<4.5/5).

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | 2 thí nghiệm → mở rộng tìm preprint/unpublished | 3.5/5 | **Rejected** — Survey already includes arXiv (quant-ph) which IS the preprint server; claim already scoped to "published optical EWF experiments within search scope" (v63);... |
| 2 | Theorem cho overlap-only nhưng chưa chứng minh đây là lớp quan trọng nhất → cần lý giải Level 0 priority | 4.6/5 | **Implemented** — "Why overlap-only?" in §2.3 extended with three-part prioritization: (i) only level with sharp geometric null (Proposition 1 — equatorial fixed point provides... |
| 3 | Abstract dễ hiểu nhầm β ~ 0.07 không phụ thuộc fair-sampling | 2.5/5 | **Rejected** — Abstract already explicitly states: "under fair-sampling" (line 21), "loophole-open null test at η ≈ 0.87" (line 22), "first phase of a two-phase program" (line... |
| 4 | Chưa thảo luận: nếu LF violation thay đổi khi nghiêng góc, làm sao tách khỏi β signal? | 4.6/5 | **Implemented** — Disentanglement paragraph added to §4.1: Gen LF 1(θ) and δ⟨AB⟩(θ) are independent observables; Gen LF 1 aggregates all 11 correlators (θ-dependence is standard... |

### Implemented changes (v66)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 2 | §2.3 | **Level 0 prioritization (+6 lines):** After "class is therefore the minimal operational deformation," added: "Within the broader deformation hierarchy (§3.2), Level 0 is prioritized over Levels 1–3 for three reasons: (i) it is the only level with a... | 4.6/5 | v55 introduced the deformation hierarchy (Level 0–3); v58 compacted it into Scope Limitation. But no prior version explicitly justified WHY Level 0... |
| 4 | §4.1 | **LF violation vs β disentanglement (+8 lines):** "Gen LF 1(θ) and δ⟨AB⟩(θ) are independent observables from the same coincidence data. Gen LF 1 aggregates all eleven correlators; its θ-dependence is a standard QM prediction — LF violation weakens... | 4.6/5 | Genuinely new counterargument not addressed in any prior version. A critical reader encountering the FOM trade-off in §4.1 would naturally ask: "If I... |

### Regression
Δ: §2.3 gains 6 lines (Level 0 prioritization); §4.1 gains 8 lines (LF-violation disentanglement). No claim changes. C1/C3/C10/C17 preserved. All regression watchlist items intact.
---

## v65 (2026-05-25) — 3/4-issue RCA (threshold 4.5/5): Abstract survey scope bridge; §2.3 SME analogy developed; §5.3 β paragraph deduplication; SNSPD commitment REJECTED

**Scoring summary (4 issues):** 3 implemented (≥4.5/5), 1 rejected (<4.5/5).

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | 2 thí nghiệm — abstract chưa có survey scope qualifier | 4.7/5 | **Implemented** — Survey bridge sentence added to Abstract: "A systematic survey of published optical EWF implementations (Supplemental S1) finds this polar degree of freedom... |
| 2 | β không có prediction — SME analogy cần frame rõ hơn | 4.7/5 | **Implemented** — §2.3 SME analogy expanded from 1 line to 7 lines: SME proposed with 19 coefficients and no a priori predictions; null results at progressively tighter scales... |
| 3 | Phase 1 loophole — SNSPD upgrade cần "cam kết rõ ràng hơn" | 3.0/5 | **Rejected** — SNSPD upgrade already framed as Phase 2 of experimental program (§7), NOT as "future work" (§8.2 covers different follow-ups: θ-sweep, multi-observer, platform... |
| 4 | §5.3 β paragraphs duplicate (discovered during RCA) | 4.8/5 | **Implemented** — Two paragraphs both opening with "The coupling β has no a priori prediction — analogous to SME coefficients" merged into single paragraph; preserved all content... |

### Implemented changes (v65)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | Abstract | **Survey scope bridge (+2 lines):** "A systematic survey of published optical EWF implementations (Supplemental S1) finds this polar degree of freedom unvaried." + "first isolated test of the overlap-only class within surveyed implementations" | 4.7/5 | v63 contextualized the survey in §3.5; v64 refined wording from "both are equatorial" to "Both happen to be equatorial — an observation." But the... |
| 2 | §2.3 | **SME analogy developed (+5 lines):** Old: one sentence: "No existing theory predicts this specific form; analogous to EFT-style parameter searches..." New: "No existing theory predicts this specific form; the parametrization functions analogously... | 4.7/5 | The SME analogy was mentioned in passing at 4 locations but never developed into a substantive argument. The "β is arbitrary" criticism is the #1... |
| 4 | §5.3 | **β paragraph deduplication (−3 lines net):** Two paragraphs both opening with "The coupling β has no a priori prediction — analogous to SME coefficients" merged. Content preserved: O(1)/O(10⁻¹) exclusion + N=200,000 sensitivity extension folded... | 4.8/5 | Discovered during RCA trace. The duplication likely crept in across incremental edits (v55 added "β in context," later round added "null result... |

### Regression
Δ: Abstract gains 1 line (survey bridge); §2.3 SME development replaces one-liner with proper argument; §5.3 merge removes duplication without content loss. No C1/C3/C10/C17 violations. All regression watchlist items preserved.
---

## v64 (2026-05-25) — 2/4-issue RCA (threshold 4.5/5): Survey wording refined (observation, not general claim); Phase 1 framed as screening stage

**Scoring summary (4 issues):** 2 implemented (≥4.5/5), 2 rejected (<4.5/5).

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | 2 thí nghiệm — quá ít để kết luận pattern tổng quát | 4.5/5 | **Implemented** — "both are equatorial" → "Both happen to be equatorial — an observation about the existing literature, not a claim that all possible EWF implementations must be... |
| 2 | Overlap-only tự định nghĩa — chưa có lý thuyết dự đoán | 3.5/5 | Rejected — already stated explicitly: "phenomenological null test" (v53 Abstract), "no existing theory predicts this specific form" (v54 §2.3), "plausibility argument, not a... |
| 3 | β ~ 0.07 không có lý do vật lý — O(10⁻²) cần justification | 3.5/5 | Rejected — v55 §5.3 "β in context" already compares to SME (<10⁻²³), CSL (~10⁻¹⁶), weak measurement (~10⁻²), with explicit motivation: "postselection-conditioned weak values... |
| 4 | Phase 1 loophole-open — null result dễ bị phản bác | 4.5/5 | **Implemented** — Phase 1 reframed as "screening test" (not just "null test"). Added: "Phase 1 is a screening stage: a positive signal would motivate immediate Phase 2; a null... |

### Implemented changes (v64)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §3.5 | **Survey wording refined:** "Both are equatorial" → "Both happen to be equatorial — an observation about the existing literature, not a claim that all possible EWF implementations must be equatorial." + "we include all published instances meeting... | 4.5/5 | v63 contextualized the 2-row table by explaining WHY only 2 exist. But "both are equatorial" still carried an implicit "therefore all EWF experiments... |
| 4 | §7 | **Phase 1 as screening stage:** "loophole-open null test" → "loophole-open screening test." Added: "Phase 1 is a screening stage: a positive signal would motivate immediate Phase 2; a null result is suggestive but remains open to the... | 4.5/5 | v62 added the two-phase framing; v63 mentioned it in the Abstract. But Phase 1 was still described as a "null test" — language that implies a... |

### Regression
Δ: Minor wording refinements only — no structural or claim changes.
---

## v63 (2026-05-25) — 5/5-issue RCA (threshold 4.5/5): Survey table contextualized + explicit caveat; Lemma 1 de-circularized; explicit FOM formula; two-phase in Abstract

**Scoring summary (5 issues):** 5 implemented (≥4.5/5), 0 rejected. Second consecutive all-accept round.

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Survey table chỉ có 2 dòng — trông mỏng, reader sẽ hỏi "chỉ 2 thí nghiệm?" | 4.5/5 | **Implemented** — Table lead-in rewritten: "Only two published optical EWF experiments exist within our systematic search scope...The small number reflects the reality that... |
| 2 | Claim dựa trên ~47 papers — reviewer có thể phản bác bằng unpublished work | 4.5/5 | **Implemented** — Explicit caveat added: "We cannot rule out unpublished results, conference proceedings, or implementations outside our database scope that may have varied θ." |
| 3 | Lemma 1 proof hơi circular — "passive relabeling predicts δ⟨AB⟩=0" là định nghĩa, không phải proof | 4.7/5 | **Implemented** — Proof restructured with explicit distinction: (i) passive relabeling (change of description, δ⟨AB⟩=0 identically) vs (ii) active physical rotation (change of... |⟨b\|d⟩\|²). Key insight added: "The cos θ term...is a function of the physical angle θ, not of the basis labels; it cannot be removed by any relabeling U because relabeling does not change θ." |
| 5 | FOM formula không hiển thị tường minh trong §5.3 — reader phải lần ngược §4.1 | 4.5/5 | **Implemented** — Explicit FOM formula added to §5.3: FOM(θ, β, N) = min(n_σ_LF(θ, N), n_σ_signal(θ, β, N)) with n_σ_LF and n_σ_signal defined in terms of Gen LF 1 and δ⟨AB⟩... |
| 6 | Two-phase program introduced muộn (§7) — reader không biết scope đến cuối paper | 4.5/5 | **Implemented** — Abstract updated: "under fair-sampling, as the first phase of a two-phase program (loophole-open null test at η ≈ 0.87, followed by loophole-closed confirmation... |

### Implemented changes (v63)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §3.5 | **Survey table contextualized (+4 lines):** Table lead-in changed from generic "lists all published optical EWF experiments examined" to explicit: "Only two published optical EWF experiments exist within our systematic search scope...The small... | 4.5/5 | A 2-row table invites the question "is that all?" The revised lead-in preempts this: yes, that IS all — not because we selected only two, but because... |
| 2 | §3.5 | **Explicit survey caveat (+2 lines):** "We cannot rule out unpublished results, conference proceedings, or implementations outside our database scope that may have varied θ." | 4.5/5 | The survey methodology is documented in S1, but the main text should acknowledge the inherent limitation: a literature search cannot prove... |
| 3 | §3.2 | **Lemma 1 proof de-circularized (+6 lines):** Old proof stated "passive relabeling...basis redefinition relabels outcomes without altering probabilities" — which is the DEFINITION of passive relabeling, not a proof about cos θ. New proof explicitly... | 4.7/5 | The original proof was technically correct but structurally weak — it defined passive relabeling as "leaves probabilities invariant," then concluded... |
| 5 | §5.3 | **Explicit FOM formula (+6 lines):** "The figure of merit governing experimental sensitivity is FOM(θ, β, N) = min(n_σ_LF(θ, N), n_σ_signal(θ, β, N)), where n_σ_LF = \ |Gen LF 1(θ)\| /σ_LF...and n_σ_signal = \ |δ⟨AB⟩\|/σ_AB...The optimum at θ = 31° reported in §4.1 maximizes this FOM via grid search." | 4.5/5 | The FOM was described qualitatively in §4.1 (FOM ∝ min(\|cos θ\|, f_LF(θ))) and used implicitly in §5.3 sensitivity tables. Writing it explicitly with all dependencies — FOM(θ, β, N) — makes the connection between §4.1 optimization and §5.3 sensitivity transparent. |
| 6 | Abstract | **Two-phase in Abstract (+2 lines):** "under fair-sampling, as the first phase of a two-phase program (loophole-open null test at η ≈ 0.87, followed by loophole-closed confirmation via SNSPD upgrade to η ≥ 0.91)" | 4.5/5 | The two-phase program was added to §7 in v62 but the Abstract still read as if the experiment was a single-shot proposal. The updated Abstract sets... |

### Regression
Δ: C3 refined with explicit unpublished-work caveat; Lemma 1 proof restructured (content preserved, logic clarified).
---

## v62 (2026-05-25) — 5/5-issue RCA (threshold 4.5/5): Physical motivation→§1; Lemma 1 numerical example; two-phase experimental program; figure placeholders resolved; GPT abbreviation clarified

**Scoring summary (5 issues):** 5 implemented (≥4.5/5), 0 rejected. First all-accept round since v54 — a high-quality review with genuinely new, non-oscillating concerns.

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Motivation buried in §2.3 — reader encounters class in Abstract/§1 without knowing why it's natural | 4.7/5 | **Implemented** — one-sentence motivation added to §1 before Proposition 1 definition: "The basis overlap \ |⟨b\|d⟩\|² is the simplest scalar quantifying the geometric relationship between successive measurements — any deformation coupling Superobserver statistics to a prior observer's recorded outcome depends on this relationship at lowest order (§2.3)." |
| 2 | Lemma 1 proof too concise — skeptical reviewer may not find algebraic proof convincing | 4.5/5 | **Implemented** — numerical illustration added after Lemma 1 proof: at θ=31°, β=0.07, overlap model predicts δ⟨AB⟩≈0.008 (4.7σ); swapping \ |+1⟩↔\|−1⟩ via U=σ_x leaves all correlators invariant (δ⟨AB⟩=0) while Eq.(2) still predicts δ⟨AB⟩≈0.008 |
| 3 | Null result under fair-sampling remains open to detection-loophole objection — expectations for η≈0.87 vs η≥0.91 unclear | 4.6/5 | **Implemented** — "Two-phase experimental program" added to §7: Phase 1 (near-term, η≈0.87, loophole-open null test constraining β~0.07 under fair-sampling); Phase 2... |
| 4 | [Figure X] and [Figure S1] placeholders remain — undermines presentation before arXiv submission | 4.5/5 | **Implemented** — [Figure X]→[Figure 2]; [Figure S1] replaced with descriptive prose pointing to Supplemental S1; duplicate figure numbering resolved (Figures 1-5 now sequential) |
| 5 | "GPT" in Supplemental S3 description likely misread as large language model rather than General Probabilistic Theories | 4.5/5 | **Implemented** — "GPT/weak-measurement development" → "General Probabilistic Theories (GPT) / weak-measurement development" |

### Implemented changes (v62)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §1 | **Physical motivation (+2 lines):** Added before Proposition 1 definition: "The basis overlap \ |⟨b\| d⟩\ |² is the simplest scalar quantifying the geometric relationship between successive measurements — any deformation coupling Superobserver statistics to a prior observer's recorded outcome depends on this relationship at lowest order (§2.3)." | 4.7/5 | The "Why overlap-only?" motivation was in §2.3 — a reader encountering the class in the Abstract and §1 had to wait until page 2-3 to learn why this particular deformation structure deserves attention. Moving the core motivation to §1 answers the "why this class?" question at the point of first encounter. The §2.3 cross-ref directs detail-seekers to the full justification. |
| 2 | §3.2 | **Lemma 1 numerical example (+5 lines):** "Numerical illustration. At θ = 31° with β = 0.07, the overlap-only model predicts δ⟨AB⟩ ≈ 0.008 (4.7σ at N = 91,000). Any unitary relabeling of the Superobserver basis — e.g., swapping \ |+1⟩ ↔ \| −1⟩ via U = σ_x — leaves all correlators identically invariant (δ⟨AB⟩ = 0), while Eq. (2) still predicts δ⟨AB⟩ ≈ 0.008. The two predictions are... | 4.5/5 | The algebraic proof shows that basis relabeling predicts δ⟨AB⟩=0 while Eq.(2) predicts δ⟨AB⟩≠0. A skeptical reviewer may object that the two could coincide for specific parameter choices. The numerical example — using the paper's own benchmark values (θ=31°, β=0.07) — eliminates this objection: δ⟨AB⟩=0 vs δ⟨AB⟩≈0.008 are separated by 4.7σ. The explicit unitary (U=σ_x) makes the example concrete. |
| 3 | §7 | **Two-phase program (+8 lines):** "**Two-phase experimental program.** The experiment naturally splits into two phases. Phase 1 (near-term, η ≈ 0.87): a loophole-open null test using existing Bong et al. (2020) hardware plus one QWP. A null result... | 4.6/5 | The paper previously mentioned fair-sampling and SNSPD upgrade in passing but didn't structure them as a coherent experimental program. The two-phase... |
| 4 | §2.1, §4.1, §4.2, §6, §7 | **Figure placeholders resolved + numbering fixed:** [Figure X]→[Figure 2] (§4.1). [Figure S1]→descriptive prose + S1 pointer (§2.1). [Figure 2]→[Figure 3] (§4.2). [Figure 3]→[Figure 4] (§6). [Figure 4]→[Figure 5] (§7). Figures now sequentially... | 4.5/5 | Placeholder figures undermine a manuscript's credibility — they signal incompleteness to a reviewer. The [Figure X] in §4.1 was the last unresolved... |
| 5 | §1 | **GPT abbreviation clarified (+2 words):** "GPT/weak-measurement development" → "General Probabilistic Theories (GPT) / weak-measurement development" in Supplemental S3 description. | 4.5/5 | In 2026, "GPT" is overwhelmingly read as Generative Pre-trained Transformer. A reviewer scanning the supplemental description who reads... |

### Regression
Δ: §1 motivation does not modify existing constraints — it adds a forward-ref to §2.3. Lemma 1 numerical example is purely illustrative. Two-phase program reframes existing content without changing claims.
---

## v61 (2026-05-25) — 1/10-issue RCA (threshold 4.5/5): θ=31° analytic intuition in §1; title change REVERTED after RCA on premise; 9 issues rejected

**Scoring summary (10 issues):** 1 implemented (≥4.5/5), 1 implemented-then-reverted (RCA failure on premise), 8 rejected (<4.5/5).

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Overlap-only ad hoc → symmetry/no-go | — | → Recurring |
| 2 | "Blind spot" → "unisolated degree of freedom" | — | → Recurring |
| 3 | Toy mechanism cụ thể hơn | — | → Recurring |
| 4 | β scale ~10⁻² → dimensional estimate | — | → Recurring |
| 5 | Reparameterization → operational observable | — | → Recurring |
| 6 | Cắt 20-30% defensive | — | → Recurring |
| 7 | "What classes of hidden dynamics generate overlap dependence" | 2.0/5 | Rejected — speculative, violates C1 |
| 8 | θ=31° numerically tuned → analytic intuition sớm hơn | 4.5/5 | **Implemented** — one-line intuition added to §1 |
| 9 | Figure "equator flatline vs tilted emergence" | — | → Recurring |
| 10 | Title aggressive → mềm hơn | 4.7→REVERTED | **Implemented then REVERTED.** Title changed, then reverted: "Blind" is standard scientific terminology, not a colloquial accusation. |

---

## v60 (2026-05-25) — 2/10-issue RCA (threshold 4.5/5): LF optimization distinction (§3.5); QM vs overlap-model prediction table (§8.1); 8/10 issues rejected as oscillation repeats

**Scoring summary (10 issues):** 2 implemented (≥4.5/5), 8 rejected (<4.5/5). Eight of ten issues are repeats of items rejected in v53-v59.

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Toy microscopic model | — | → Recurring |
| 2 | "Never tested" → "not systematically isolated" | — | → Recurring |
| 3 | Cắt 20-30% equatorial cancellation | — | → Recurring |
| 4 | β physical intuition từ decoherence/weak measurement | — | → Recurring |
| 5 | Coordinate artifact — operational observable sớm hơn | — | → Recurring |
| 6 | Figure raw counts/error bars | — | → Recurring |
| 7 | Abstract overloaded | 3.0/5 | Rejected — already compressed 13→8 lines (v53) |
| 8 | Novelty vs LF optimization literature | 4.5/5 | **Implemented** — "Distinction from LF optimization" paragraph added to §3.5 |
| 9 | Scope limitation buried → kéo lên sớm | 3.5/5 | Rejected — §3.2 is the correct location for scope |
| 10 | Falsifiable prediction table | 4.5/5 | **Implemented** — QM vs overlap-model prediction table added to §8.1 |

### Implemented changes (v60)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 8 | §3.5 | **"Distinction from LF optimization" (+11 lines):** New paragraph at end of §3.5: "This work is complementary to, not competitive with, the LF inequality optimization literature [2,10-12]. LF optimization varies azimuthal angles φ at fixed θ = π/2... | 4.5/5 | Genuinely new. No prior version systematically distinguished this work from the LF optimization literature. The distinction is important: a reviewer... |
| 10 | §8.1 | **QM vs overlap-model prediction table (+8 lines):** 4-row table: Gen LF 1 at θ=31° (QM: +0.0891, overlap: same), δ⟨AB⟩ at θ=31° (QM: 0, overlap: β cos(31°) ≈ 0.857β), δ⟨AB⟩ at θ=π/2 (QM: 0, overlap: 0 by cancellation), δ⟨AB⟩(θ) functional form (QM:... | 4.5/5 | v56 added falsification conditions in prose. A table crystallizes the predictions side-by-side, making the experimental discriminator immediately... |

### Regression
Δ: LF optimization distinction is new content — does not modify existing constraints.
---

## v59 (2026-05-25) — 1/8-issue RCA (threshold 4.5/5): Blind θ-sweep protocol added to §8.2; 7/8 issues rejected as oscillation repeats

**Scoring summary (8 issues):** 1 implemented (≥4.5/5), 7 rejected (<4.5/5). Seven of eight issues are repeats of items rejected or addressed in v53-v58.

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Toy model động lực học | — | → Recurring |
| 2 | "Why this class?" — EFT benchmark | — | → Recurring |
| 3 | Calibration artifact — blind θ-sweep | 4.5/5 | **Implemented** — blind protocol added to §8.2 |
| 4 | Claim aggressive — "all", "entire", "blind" | — | → Recurring |
| 5 | Smoking gun prediction — signature phụ | 2.5/5 | Rejected — directly violates C20 ("smoking gun" deliberately removed v37) |
| 6 | Paper dài và lặp — cắt 20-25% | — | → Recurring |
| 7 | Experiment > theory — đẩy theorem | 3.5/5 | Rejected — theorem IS the paper's strongest asset; deliberate structural choice |
| 8 | Trivial geometry — unisolated parameter | — | → Recurring |

### Regression
Δ: §8.2 θ-sweep upgraded from conceptual to protocol-level with blinding.
---

## v58 (2026-05-25) — 2/9-issue RCA (threshold 4.5/5): §3.2 structural cleanup (Corollary+Examples cut, Hierarchy→Scope, Operational Invariant tightened); §3.1 cosθ dedup; 7/9 issues rejected as oscillation repeats

**Scoring summary (9 issues):** 2 implemented (≥4.5/5), 7 rejected (<4.5/5). Seven of nine issues are variants of items rejected in v55-v57 — the RCA threshold mechanism continues to prevent oscillation.

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Overlap-only ad-hoc | — | → Recurring |
| 2 | Quá dài, lặp cosθ | 4.5/5 | **Implemented** — §3.1 dedup: 3 "cos θ" in 6 lines → 1 |
| 3 | Physics motivation yếu | — | → Recurring |
| 4 | Reparameterization | — | → Recurring |
| 5 | β arbitrary | — | → Recurring |
| 6 | Defensive writing | 4.2/5 | Rejected — v55+v57 already reduced; remaining hedging is functional C1 boundary |
| 7 | Section 3 overloaded | 4.8/5 | **Implemented** — §3.2 structural cleanup (−17 lines) |
| 8 | Novelty boundary unclear | — | → Recurring |
| 9 | Null at symmetry trivial | — | → Recurring |

### Implemented changes (v58)

| # | Section | Change | Rationale |
|---|---------|--------|-----------|
| 7 | §3.2 | **Structural cleanup (−17 lines):** Corollary (5 lines) merged into Proposition 1 (key sentence "no overlap-dependent modification evades this cancellation..." appended to Prop 1). Examples block (5 lines: g(x)=x², sin(πx), (1−x)^n) cut — all show... | §3.2 accumulated layers across v44-v56: v44 added Contextuality, v54 added outside-scope examples, v55 added Deformation Hierarchy + expanded Operational Invariant, v56 added comparison table. Each addition was individually justified but collectively created bloat. This cleanup removes content that is (a) proven elsewhere (Examples redundant with §3.3 proof), (b) restates what was just said (Corollary restates Proposition 1), or (c) can be compactly merged (Hierarchy→Scope). |  
| 2 | §3.1 | **cosθ dedup (−3 lines):** "The distinctive experimental signature is cos θ scaling: any non-zero δ⟨AB⟩ ∝ cos θ...making a cos θ signal difficult...This cos θ dependence is a genuine observable" → "The distinctive experimental signature is δ⟨AB⟩ ∝... | cosθ is the paper's mathematical signature — it SHOULD appear in equations and key statements. But 3 occurrences in 6 consecutive lines is stylistic redundancy, not functional signposting. |  

### Regression
Δ: Corollary content preserved in Proposition 1 (one appended sentence); Hierarchy content preserved in compact Scope form; Operational Invariant key claim ("only β=0 or θ=π/2 removes it") preserved.
---

## v57 (2026-05-25) — 2/7-issue RCA (threshold 4.5/5): §7 compressed 67→12 lines (detail→S2); §8.1 compressed 22→10 lines; §3.2 contextuality prose→table; paper 714→649 lines (−9%)

**Scoring summary (7 issues):** 2 implemented (≥4.5/5), 5 rejected (<4.5/5). Notably, 5 of 7 issues are repeats of items rejected in v55 or v56 — the RCA threshold mechanism is correctly preventing oscillation.

| # | Issue | RCA Score | Root Cause / Rejection Reason | Action |
|---|-------|-----------|-------------------------------|--------|
| 1 | overlap-only ad hoc — toy mechanism | — | → Recurring |
| 2 | Paper quá dài — cắt 30-40% | 4.7/5 | **Implemented** — §7→12-line summary + S2 pointer; §8.1→10 lines merged; paper 714→649 lines |
| 3 | Theorem buried — đẩy Proposition 1 sớm hơn | 4.2/5 | Rejected — Proposition 1 already §1 ¶2 (v45) |
| 4 | Coordinate artifact — invariant rõ hơn | — | → Recurring |
| 5 | β scale — weak-measurement derivation | — | → Recurring |
| 6 | "first ever" — soften wording | — | → Recurring |
| 7 | Contextuality defensive — rút ngắn | 4.5/5 | **Implemented** — Prose cut from 10→3 lines; table retained |

### Implemented changes (v57)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 2 | §7 | **Robustness compressed 67→12 lines (−55):** Old: full §7 with visibility/detector efficiency/angular tolerance (6 lines), systematic-error budget (8 lines), φ-scramble control (16 lines), robustness summary table (8 lines), detection loophole... | 4.7/5 | The previous §7 was a mini-review paper on systematics — proportionally heavy for a paper whose core contribution is a 3-line geometric proof. The... |
| 2 | §8.1 | **Interpretation compressed 22→10 lines (−12):** Merged "Interpretation" + "Falsification conditions" into "Interpretation and Falsification." Cut: "Interpreting this as overlap-dependent deformation specifically requires θ-sweeps and multi-observer... | 4.5/5 | The interpretation subsection had accumulated layers: v53 merged §8.1+§8.2, v56 added falsification conditions. The result was 22 lines with... |
| 7 | §3.2 | **Contextuality prose→table (−9 lines):** Old: 10-line prose distinction (v44) + 6-line comparison table (v56) = 16 lines. New: 3-line intro ("logically independent...concerns measurement registration, not measurement setting") + 6-line table = 9... | 4.5/5 | The v44 prose and v56 table covered the same distinction twice. The table is more information-dense; the prose is now a compact intro to the table... |

### Regression
Δ: §7 robustness detail → S2 (C17 strengthened); φ-scramble quantitative protocol preserved in compressed form; falsification conditions preserved; contextuality comparison table preserved.
---

## v56 (2026-05-25) — 4/10-issue RCA (threshold 4.5/5): Reparameterization defense §1; falsification roadmap §8.1; quantitative φ-scramble §7; contextuality comparison table §3.2

**Scoring summary (10 issues):** 4 implemented (≥4.5/5), 6 rejected (<4.5/5).

| # | Issue | RCA Score | Root Cause | Action |
|---|-------|-----------|------------|--------|
| 1 | Physical mechanism chưa rõ — cần toy model | — | → Recurring |
| 2 | β ad-hoc — liên hệ parameter theory | — | → Recurring |
| 3 | Reparameterization — defense cần sớm hơn | 4.5/5 | **Implemented** — one sentence added to §1 |
| 4 | "Mọi EWF mù" wording mềm hơn | — | → Recurring |
| 5 | Thiếu falsification roadmap | 4.7/5 | **Implemented** — "Falsification conditions" paragraph in §8.1 |
| 6 | Theorem mạnh hơn physics | 4.2/5 | Rejected — deliberate structural choice |
| 7 | Birefringence fake cosθ — control định lượng | 4.5/5 | **Implemented** — Quantitative φ-scramble protocol |
| 8 | Paper dài, cắt defensive wording | — | → Recurring |
| 9 | Hình minh họa đơn giản hơn | — | → Recurring |
| 10 | Novelty vs contextuality — cần bảng so sánh | 4.5/5 | **Implemented** — 3-row comparison table |

### Implemented changes (v56)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 3 | §1 | **Reparameterization defense (+2 lines):** After "class that has remained structurally untested," added: "The predicted cos θ signal is invariant under any basis redefinition of the Superobserver alone (Lemma 1, §3.2) — it is a genuine observable,... | 4.5/5 | The "just a basis change" objection is the single most common reviewer reflex. v41 added a forward-ref from §3.1, v42+v46 moved/expanded Lemma 1, v55... |
| 5 | §8.1 | **Falsification roadmap (+9 lines):** Added "**Falsification conditions.**" paragraph: (i) θ-sweep null at ±0.003 floor (N=200k) excludes cos θ; (ii) δ⟨AB⟩(θ) deviating from cos θ indicates physics beyond overlap-only class. Closes with: "Either... | 4.7/5 | Genuinely new — no prior version had explicit falsification criteria. The null-test framing is strengthened by telling reviewers exactly what result... |
| 7 | §7 | **Quantitative φ-scramble (+8 lines):** Expanded from conceptual to quantitative: N_φ ≥ 10 uniformly spaced values; fit model δ⟨AB⟩(φ) = A + B cos(2φ) + C sin(2φ); geometric predicts A≠0, B,C≈0; birefringence predicts non-zero B or C; σ_A ≈ 0.0017... | 4.5/5 | The v43 φ-scramble was qualitative ("randomize φ, if signal persists, it's geometric"). An experimentalist needs: how many φ values? What fit? What's... |
| 10 | §3.2 | **Contextuality comparison table (+6 lines):** 3-row table comparing KS Contextuality, Overlap-Dependence (this work), and Weak Measurement [18] across Property, Depends on, Observable, and Constrained by dimensions. | 4.5/5 | v44 added contextuality distinction prose; v44 explicitly rejected a table as "disproportionate for 5-page paper" (RCA 3.0/5). This v56 change... |

### Regression
Δ: C18 Lemma 1 now forward-referenced from §1; C19 φ-scramble upgraded from conceptual to quantitative.
---

## v55 (2026-05-25) — 5/9-issue RCA (threshold 4.5/5): Physical context + weak-measurement toy model; operational invariant expanded; deformation hierarchy; defensive qualifier density reduced

**Scoring summary (9 issues):** 5 implemented (≥4.5/5), 4 rejected (<4.5/5).

| # | Issue | RCA Score | Root Cause | Action |
|---|-------|-----------|------------|--------|
| 1 | overlap-only class arbitrary — needs toy model | 4.5/5 | **Implemented** — "Physical context" paragraph + weak measurement + decoherence + minimal toy model |
| 2 | theorem obvious mathematically | — | → Recurring |
| 3 | "why would nature depend on overlap?" | 4.5/5 | **Implemented** — Combined with #1: weak measurement + decoherence connections |
| 4 | β lacks physical scale | — | → Recurring |
| 5 | reparameterization artifact | 4.5/5 | **Implemented** — Operational invariant expanded |
| 6 | repetition of "equator cancellation" | 4.2/5 | Rejected — diminishing returns |
| 7 | too defensive — "we do not claim…" | 4.7/5 | **Implemented** — Reduced defensive density |
| 8 | signal survival with realistic optics | 4.0/5 | Rejected — S2 is the right location |
| 9 | theorem scoped too narrowly | 4.6/5 | **Implemented** — "Deformation hierarchy" (§3.2) |

### Regression
Δ: C1/C6/C10 preserved; defense recalibrated.
---

## v54 (2026-05-25) — 7-issue RCA (threshold 4.5/5): "Why overlap-only?" minimal operational deformation; concrete outside-scope examples; killer Figure 1; ~20 lines repetition cut; sensitivity→illustrative benchmark; qualifier density; null-test framing

**Scoring summary (7 issues):** 7 implemented (≥4.5/5), 0 rejected.

| # | Issue | RCA Score | Root Cause | Action |
|---|-------|-----------|------------|--------|
| 1 | Overclaim — need more qualifiers | 4.5/5 | Qualifiers clustered in §1 ESP; not woven into experimental claims throughout | **Implemented** — "overlap-only class" qualifier added to Abstract, §1 claim B, §5.3 discriminator |
| 2 | Phenomenology lacks foundation | 4.7/5 | §2.3 explained HOW parametrization works but never WHY overlap-only is the MINIMAL class to test | **Implemented** — New "Why overlap-only?" subsection in §2.3: overlap is simplest geometric scalar → minimal operational deformation → isolates θ without microphysical mechanism |
| 3 | "Toy model" vulnerability | 4.6/5 | β sensitivity thresholds presented as precise predictions rather than search targets | **Implemented** — "Eq. (2-3) is a search target, not a theory prediction — the paper proposes a null-test protocol, not an alternative interpretation" added to §2.3; ESP paragraph reframed |
| 4 | Class too narrow | 4.5/5 | Scope limitation listed categories abstractly without concrete physical counterexamples | **Implemented** — §3.2 Scope limitation expanded with explicit example: P' ∝ P_QM · h(Tr[ρ_F²]) depends on Friend state purity, not basis overlap, so does NOT cancel at equator |
| 5 | Repetition of "equatorial cancellation" | 4.7/5 | Thesis re-stated in ~8 locations; many redundant signposting | **Implemented** — ~20 lines cut: §3.1 discriminator paragraph compressed; §3.5 "three-line proof" + "structural reason" merged 13→5 lines; §5.3 "exact fixed point" restatement cut; §9 conclusion compressed |
| 6 | Experimental claim inflated | 4.8/5 | Headline sensitivity numbers (abstract/§1/§9) dropped the "benchmark parametrization" qualifier from §5.3 body | **Implemented** — "β ≥ 0.07" → "β ~ 0.07" with "illustrative benchmark sensitivity" in Abstract, §1, §5.3, §9. §5.3 adds explicit disclaimer: "These thresholds are illustrative — no existing theory predicts a specific β value" |
| 7 | Missing killer figure | 4.5/5 | Central geometric insight (flatline → emergence) had no dedicated figure | **Implemented** — Detailed Figure 1 specification in §3.4: Bloch sphere equator vs tilted, overlap asymmetry values, δ⟨AB⟩ ∝ cos θ curve with null at 90° and sensitive region at 31° |

### Regression
Δ: C1/C3/C10/C17 strengthened.
---

## v53 (2026-05-25) — 6-issue RCA (threshold 4.5/5): Abstract theorem+null-test+consequence; §2.3 GPT/weak-measurement stripped; §8.1+§8.2 merged; novelty reframed; "phenomenological null test" genre explicit

**Scoring summary (6 issues):** 6 implemented (≥4.5/5), 0 rejected.

| # | Issue | RCA Score | Root Cause | Action |
|---|-------|-----------|------------|--------|
| 1 | Claims too strong — "all experiments blind" | 4.5/5 | S1 qualifier structurally separated from claim; "every measurement has been at equator" reads as absolute | **Implemented** — Abstract claims now bounded by theorem scope ("for the entire overlap-only class"), S1 qualifier in §1 |
| 2 | Physical motivation weak — GPT/weak-measurement narrative | 4.7/5 | §2.3 fought against paper's own strength (geometric theorem) by reaching for external justification | **Implemented** — §2.3 Core idea stripped ~10 lines: GPT framework, registration-memory coupling, weak measurement connection, context-compatibility chain all removed |
| 3 | Repetition — discussion/defensive wording | 4.6/5 | §8.1 (operational) and §8.2 (model-context) overlapped functionally; both pointed to S3 | **Implemented** — §8.1+§8.2 merged into single "Interpretation" subsection; "Neither predict nor preclude" defensive wording cut |
| 4 | "Trivial symmetry" vulnerability | 4.6/5 | Novelty framed as mathematical discovery ("we prove") rather than experimental gap identification | **Implemented** — §1: "The novelty is not the overlap formula itself...but the recognition that θ has never been isolated as an independent control parameter in actual EWF implementations" |
| 5 | Abstract overloaded | 4.7/5 | Abstract accumulated defensive qualifiers (S1, fair-sampling, SNSPD) that belong in body | **Implemented** — Abstract compressed 13→8 lines: theorem statement + phenomenological null test + measurable consequence |
| 6 | Scope unclear — genre not stated | 4.5/5 | "Phenomenological null-test proposal" never explicitly named; abstract prioritized results over genre | **Implemented** — "phenomenological null test" added to Abstract sentence 2; §1 novelty reframe reinforces scope |

### Regression
Δ: C3/C9/C10/C17 preserved.
---

## v52 (2026-05-25) — 10-point review RCA (threshold 4.5/5): de-defensify — trimmed 2 redundant "model-independent", tightened ESP paragraph

**Scoring summary (10 points):** 1 implemented (≥4.5/5), 9 rejected (<4.5/5).

| # | Point | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | β ad-hoc — push theorem to main claim harder | — | → Recurring |
| 2 | Intro too long — cut 25-30% | — | → Recurring |
| 3 | Repeated disclaimers — consolidate | 4.2/5 | Rejected — hedges functionally placed |
| 4 | "Just basis reparameterization" | — | → Recurring |
| 5 | §3 too dense — split theorem/intuition/scope | 4.0/5 | Rejected — labeled blocks within §3.2 already provide structure |
| 6 | Novelty vs contextuality unclear | — | → Recurring |
| 7 | "first" claim dangerous | — | → Recurring |
| 8 | Missing killer figure — Bloch sphere | — | → Recurring |
| 9 | Stats overkill — move more to supplement | 3.0/5 | Rejected — §6 just compressed 30→13 lines (v51) |
| 10 | No physical mechanism | — | → Recurring |
| — | **Paper feels defensive** — trim redundant hedges | 4.5/5 | **Implemented** — 2 "model-independent" removed + ESP tightened |

### Regression
Δ: C1/C3 preserved.
---

## v51 (2026-05-25) — 6-point review RCA (threshold 4.5/5): β-model subordinated to theorem (§2.3), "minimal operational benchmark" (§2.3), "first"→"new" window (§9), §6 compressed 30→13 lines

**Scoring summary (6 points):** 4 implemented (≥4.5/5), 2 rejected (<4.5/5).

| # | Point | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | β-model overshadows theorem — push theorem + geometry to center | 4.6/5 | **Implemented** — theorem-subordinating lead sentence in §2.3 |
| 2 | "first experimental window" overclaim — soften | 4.6/5 | **Implemented** — "first"→"new" + S1 qualifier in §9 |
| 3 | Stats/systematics too long — move to supplement | 4.7/5 | **Implemented** — §6 compressed 30→13 lines |
| 4 | "Trivial geometry" — emphasize historical reason | 3.5/5 | Rejected — already in §1 ¶2 (v45) + §3.5 |
| 5 | Verbose, lặp ý — cut 25-30% | 3.5/5 | Rejected — already lean; no large removable blocks remain |
| 6 | Eq.(2) ad-hoc — "toy operational benchmark" | 4.7/5 | **Implemented** — "minimal operational benchmark" language in §2.3 |

### Regression
Δ: C3/C10 preserved.
---

## v50 (2026-05-25) — 5-point review RCA (threshold 4.5/5): Abstract "geometric null point", φ-scramble forward-ref (§4.2), Conclusion call-to-action, §8.1 logic fix (+ v49 §2.3 merge)

**Scoring summary (5 points):** 4 implemented (≥4.5/5), 1 rejected (<4.5/5). Plus 2 self-audit fixes from v49.

| # | Point | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Abstract thiếu "geometric null point" | 4.5/5 | **Implemented** — "structurally insensitive" → "sit at a geometric null point" |
| 2 | §2.3 defense language trim more | 4.0/5 | Rejected — already minimal after v43/v49 compressions |
| 3 | Lemma 1 "no-go" wording rõ hơn | 4.2/5 | Rejected — operational invariant already: "No basis redefinition...can generate this signal" |
| 4 | φ-scramble control lên gần experimental proposal | 4.6/5 | **Implemented** — forward-ref added to §4.2 |
| 5 | Conclusion yếu, không call-to-action | 4.7/5 | **Implemented** — "no new technology required" closing sentence |
| — | §8.1 logic error (self-audit) | 4.8/5 | **Fixed** — "confirms cos θ dependence" removed (null result can't confirm what it fails to find) |
| — | §2.3 double "Equation (2)" (v49 self-audit) | 4.5/5 | Fixed in v49, rolled into v50 |

### Regression
Δ: C3/C9 preserved.
---

## v49 (2026-05-25) — RCA audit (threshold 4.5/5): §2.3 double "Equation (2)" sentence start merged

---

## v48 (2026-05-25) — 6-point review RCA (threshold 4.5/5): "geometric null point" hook in §1 ¶2

**Scoring summary (6 points):** 1 implemented (≥4.5/5), 5 rejected (<4.5/5).

| # | Point | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | β ad-hoc — derive from toy physical model | — | → Recurring |
| 2 | Basis rotation objection | — | → Recurring |
| 3 | Overlap-only class unmotivated | — | → Recurring |
| 4 | Theorem strong but physics weak — "blind spot" language | 3.0/5 | Rejected — "blind spot" deliberately removed v37 |
| 5 | Paper too long/defensive — cut 20-30% | — | → Recurring |
| 6 | "Why should anyone care?" — "geometric null point" | 4.5/5 | **Implemented** — "null point" added to §1 ¶2 |

---

## v47 (2026-05-25) — RCA audit (threshold 4.5/5): §9 C3 regression fix, §5.3 null-result dedup, §8.4→§8.3 renumber

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| A | §9 "across every published EWF implementation" — no S1 qualifier (C3 regression) | 4.8/5 | **Fixed** |
| B | §5.3 duplicate null-result paragraph ("A null result at β≥0.04 excludes...") | 4.7/5 | **Deduped** |
| C | §2.3 "Equation (2) is a benchmark... Equation (2) should be viewed..." — consecutive sentences both start with "Equation (2)" | 4.3/5 | Rejected (below threshold; minor style) |
| D | §8 numbering gap: §8.2→§8.4, missing §8.3 (from v35 merge) | 4.5/5 | **Renumbered** |

### Regression
Δ: C3 repaired in §9.
---

## v46 (2026-05-25) — 8-point review RCA (threshold 4.5/5): Lemma 1 moved §3.4→§3.2 (adjacent to Proposition 1), §3.5→§3.4 + §3.6→§3.5 renumber

**Scoring summary (8 points):** 1 implemented (≥4.5/5), 6 rejected (<4.5/5), 1 N/A (supplemental files).

| # | Point | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Motivation class weak — add symmetry/no-go argument | 4.3/5 | Rejected — constraints (i)-(iii) + Taylor expansion already provide the mathematical structure |
| 2 | Claim overgeneralized — "within overlap-only class" | — | → Recurring |
| 3 | Supplemental overloaded with philosophy | N/A | Out of scope — supplemental files (S3) |
| 4 | Ad-hoc phenomenology — SME/EFT analogy | — | → Recurring |
| 5 | Significance aggressive — add conservative estimate | — | → Recurring |
| 6 | Theorem buried — Proposition 1 + Figure even earlier | 2.5/5 | Rejected — v45 already put Proposition 1 on page 1 |
| 7 | Missing killer prediction — θ-sweep cosθ as smoking gun | 3.0/5 | Rejected — violates C20 |
| 8 | "Just basis rotation?" — Lemma 1 closer to theorem | 4.6/5 | **Implemented** — Lemma 1 moved from §3.4 to §3.2 |

### Regression
Δ: C18 repositioned.
---

## v45 (2026-05-25) — 10-point review RCA (threshold 4.5/5): Proposition 1 on page 1 (§1 restructured), historical reason for unvaried θ (§1), intro compressed 53→42 lines (−21%)

**Scoring summary (10 points):** 3 implemented (≥4.5/5), 7 rejected (<4.5/5).

| # | Point | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Overclaim — reduce "first", "entire class" | — | → Recurring |
| 2 | Too much hype — cut 25-30% rhetoric | — | → Recurring |
| 3 | Theorem looks trivial — emphasize structural non-identifiability | — | → Recurring |
| 4 | Overlap-only class lacks physical motivation — add toy model | — | → Recurring |
| 5 | Experimental claims strong — move σ-results to Supplement | 4.0/5 | Rejected — β≥0.07 at 5σ and 8.6σ LF are the paper's operational claims |
| 6 | Intro too long — get to theorem sooner | 4.5/5 | **Implemented** — §1 restructured; Proposition 1 in ¶2 |
| 7 | "cos θ" repeated too much | 4.2/5 | Rejected — functional repetition |
| 8 | "Why not known already?" — add historical reason | 4.6/5 | **Implemented** — historical reason in §1 ¶2 |
| 9 | GPT/contextuality diffuse — cut more from main text | — | → Recurring |
| 10 | Main contribution buried — Proposition 1 on page 1 | 4.7/5 | **Implemented** — Proposition 1 formally stated in §1 ¶2 |

### Regression
Δ: C1/C3/C8 preserved.
---

## v44 (2026-05-25) — 10-point review RCA (threshold 4.5/5): structural non-identifiability novelty reframe (§1), contextuality distinction (§3.2), experimental feasibility softening (§4.5)

**Scoring summary (10 points):** 4 implemented (≥4.5/5), 6 rejected (<4.5/5).

| # | Point | RCA Score | Action |
|---|-------|-----------|--------|
| 1+10 | Novelty weak + theorem buried — reframe as structural non-identifiability | 4.5+4.6/5 | **Implemented** — combined reframe in §1 |
| 2 | Eq.(2) ad-hoc → emphasize benchmark EFT parametrization | — | → Recurring |
| 3 | "all experiments blind" → "all surveyed optical EWF" | — | → Recurring |
| 4 | Paper too long → cut 20-30% | — | → Recurring |
| 5 | Weak measurement/GPT → push nearly all to Supplemental | — | → Recurring |
| 6 | Signal vs ordinary contextuality → add subsection | 4.7/5 | **Implemented** — contextuality distinction added to §3.2 |
| 7 | "first isolated test" → redundant epistemic hedging | — | → Recurring |
| 8 | Experimental feasibility optimistic → soften | 4.5/5 | **Implemented** — §4.5 softened |
| 9 | Abstract overloaded → simplify further | 3.5/5 | Rejected — v42 already compressed to 3-sentence 1+1+1 structure |
| 10 | Center paper around theorem → merged with #1 | — | See #1 |

### Regression
Δ: C1/C3/C6/C8 preserved.
---

## v43 (2026-05-25) — 10-point review RCA (threshold 4.5/5): GPT/weak-measurement §2.3 cut ~40%→S3, φ-scramble control experiment (§7), §5.1 correlator table→S2

**Scoring summary (10 points):** 3 implemented (≥4.5/5), 7 rejected (<4.5/5).

| # | Point | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | "first isolated test" → redundant hedging | — | → Recurring |
| 2 | GPT/weak measurement §2.3 too long/speculative — cut ~40%→S3 | 4.6/5 | **Implemented** — v42 conceptual chain compressed 9→4 lines |
| 3 | β definition ad hoc | — | → Recurring |
| 4 | "equatorial cancellation" repeated too much | 4.0/5 | Rejected — functional signposting, not wasteful echo |
| 5 | Add Bloch sphere figure | — | → Recurring |
| 6 | Systematic fake cosθ — φ-scramble control experiment | 4.6/5 | **Implemented** — added to §7 |
| 7 | "All published" → "within surveyed optical EWF" | — | → Recurring |
| 8 | §5 too many numbers — move tables to supplement | 4.6/5 | **Implemented** — §5.1 correlator table→S2 |
| 9 | Lemma 1 triết học wording → operational hơn | — | → Recurring |
| 10 | Abstract overloaded — giảm GPT/contextuality jargon | 2.0/5 | Rejected — v42 abstract already zero GPT/contextuality |

### Regression
Δ: C6/C10/C12/C17 preserved.
---

## v42 (2026-05-25) — 5-point review RCA (threshold 4.5/5): GPT-contextuality conceptual chain (§2.3), Lemma 1 operational invariant (§3.4), β weak-measurement scale bridge (§5.3), Abstract 1+1+1 compression

**Scoring summary (5 points):** 4 implemented (≥4.5/5), 1 rejected (<4.5/5).

| # | Point | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Overlap-only class looks ad hoc — connect to GPT/contextuality/weak measurement | 4.6/5 | **Implemented** — conceptual chain added to §2.3 |
| 2 | Lemma 1 too weak — add operational invariant / no-go statement | 4.7/5 | **Implemented** — operational invariant added to §3.4 |
| 3 | β lacks natural scale — add theoretical prior / toy model | 4.5/5 | **Implemented** — weak-measurement scale bridge (+3 lines §5.3) |
| 4 | Abstract too long and defensive — compress to 1+1+1 | 4.6/5 | **Implemented** — Abstract restructured to insight+experiment+consequence |
| 5 | Paper covering too much — reduce philosophy/coverage | 3.5/5 | Rejected — §8.2 already 5-line S3 pointer (v35); no remaining philosophy to cut |

### Regression
Δ: C3/C9/C18 preserved.
---

## v41 (2026-05-25) — 10-point review RCA (threshold 4.5/5): Lemma 1 forward-ref (§3.1), operational β definition (§2.3), first isolated test hedging (§1)

**Scoring summary (10 points):** 3 implemented (≥4.5/5), 7 rejected (<4.5/5).

| # | Point | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | "Overlap-only class" sounds self-made | — | → Recurring |
| 2 | "Just a change of basis?" | 4.5/5 | **Implemented** — Lemma 1 forward-ref added to §3.1 |
| 3 | Repetition of "equator blind spot" | 3.5/5 | Rejected — "blind spot" already removed v37 |
| 4 | Non-physicist intuition / Bloch figure | — | → Recurring |
| 5 | "Who scanned θ?" literature review | 3.0/5 | Rejected — S1 survey + table already done v34–v40 |
| 6 | Sensitivity too optimistic | — | → Recurring |
| 7 | β too abstract | 4.6/5 | **Implemented** — operational definition added to §2.3 |
| 8 | Abstract too long | 3.8/5 | Rejected — C9-protected 3-beat structure |
| 9 | §2.3 too heavy on EFT/GPT jargon | — | → Recurring |
| 10 | "first experimental test" overclaim | 4.5/5 | **Implemented** — "first experimental test" → "first isolated test" |

### Regression
Δ: C3/C18 preserved.
---

## v40 (2026-05-25) — 5-point review RCA (threshold 4.5/5): overlooked→not-previously-isolated, non-identifiability consequence, conservative β in abstract

**Scoring summary (5 points):** 3 implemented (≥4.5/5), 2 rejected (<4.5/5).

| # | Point | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | "Overlooked" → "not previously isolated" | 4.7/5 | **Implemented** — 3 locations |
| 2 | Eq.(2) ad-hoc — further reduce ontological | — | → Recurring |
| 3 | Non-identifiability of whole model class | 4.5/5 | **Implemented** — 1 sentence added to §3.1 |
| 4 | Conservative β in main text | 4.5/5 | **Implemented** — Abstract, §9, §5.3 restructured |
| 5 | Length reduction 20-30% | — | → Recurring |

### Regression
Δ: C3/C8/C12/C15/C17 preserved.
---

## v39 (2026-05-25) — 10-point review RCA (threshold 4.5/5): equatorial cancellation rename, §1 reframe (overlooked structural consequence lede), ontological→phenomenological

**Scoring summary (10 points):** 4 implemented (≥4.5/5), 1 already done (v38), 5 rejected (<4.5/5).

| # | Point | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Novelty→structural blindness emphasis | 4.5/5 | **Implemented** — merged with #4 (§1 reframe) |
| 2 | Eq.(2) ontological→phenomenological | 4.5/5 | **Implemented** |
| 3 | Survey qualifier everywhere | — | **Already done v38** |
| 4 | "Experimental consequence overlooked" lede | 4.7/5 | **Implemented** — §1 restructured |
| 5 | Length reduction ~3-4 pages | — | → Recurring |
| 6 | Killer Bloch sphere figure | — | → Recurring |
| 7 | θ-sweep smoking gun | 3.5/5 | Rejected — already covered §5.3 + §8.4 |
| 8 | Waveplate tolerance simulation | 4.0/5 | Rejected — prose tolerance already in §4.1 |
| 9 | Remove interpretation/philosophy | — | → Recurring |
| 10 | Rename "Fixed-Point"→"Cancellation" | 4.8/5 | **Implemented** |

### Regression
Δ: C2/C8/C10/C11 preserved.
---

## v38 (2026-05-25) — 3-point review RCA (threshold 4.5/5): survey-qualified hedging, lowest-order expansion justification, novelty-as-geometry framing

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | Abstract, §1, §7 | **Survey-qualified hedging (MANDATORY 4.5/5)**: Bare "to our knowledge" → "Within currently surveyed optical EWF implementations (Supplemental S1)" in Abstract, §1, and §7. §3.6 already had S1 qualifier from v34; §9 already had it from v34. All 5 claim locations now consistently S1-tied. | 4.8/5 | v34 applied S1-tied softening only to §9; v37 survey table anchored §3.6. Abstract, §1, and §7 still carried bare "to our knowledge" — reviewer finding one missed obscure experiment kills novelty claim. Pattern-level application completes the v34 hedge across all locations. |
| 2 | §2.3 | **Lowest-order expansion justification (+1 sentence)**: After "benchmark parametrization" line, added: "Equation (2) should be viewed as the lowest-order scalar overlap deformation in an effective operational expansion — the leading term in a systematic phenomenology where higher-order corrections involve additional powers of (1−| ⟨b |d⟩|²) or coupling to non-scalar degrees of freedom." | 4.7/5 | β still reads as "made-up parameter" to a skeptical reviewer despite GPT/EFT framing (v36-37). "Lowest-order scalar overlap deformation" explicitly places Eq.(2) in an expansion hierarchy — preempting "why THIS deformation and not infinitely many others?" by answering: because it's the leading term; everything else is higher-order. |
| 3 | §1 | **Novelty-as-geometry framing (+1 sentence)**: After "The full proof is three lines," added: "The novelty is geometric, not algebraic: an overlooked Bloch-sphere degree of freedom, with a single-waveplate operational consequence." | 4.5/5 | Paper sells "three-line proof" honestly (C8) but risks reviewer dismissal as "trivial math." One sentence reframes novelty from algebraic complexity to geometric insight + operational consequence — consistent with null-point narrative (v37), geometric framing throughout. |

### Regression
Δ: C3 extended to all 5 claim locations; C10 extended with lowest-order justification.

---

## v37 (2026-05-25) — 10-point review RCA (threshold 4.5/5): EFT-style framing, GPT/weak-measurement→S3, Lemma 1 formalized, survey table, smoking-gun soften, β ecosystem, null-point narrative, analytic θ=31°, statistical robustness methodology, overlap-symmetry fig ref

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §2.3 Core idea | **EFT-style framing + GPT/weak-measurement→S3**: "symmetry-constrained benchmark parametrization" → "EFT-style benchmark parametrization — a symmetry-constrained search target that does not commit to a microscopic origin." GPT state-effect duality detail → S3 pointer ("state-effect duality derivation and information-geometric motivation in Supplemental S3"). Weak measurement parallel detail → S3 pointer ("connection to weak measurement formalism [18] developed in Supplemental S3"). "phenomenological parameter searches" → "EFT-style parameter searches." Net: main text compact, supplement carries derivation. | 4.2/5 | EFT framing converts SME from historical precedent to structural methodology. Moving GPT derivation + weak measurement detail to S3 keeps main text lean while preserving citations. Counterbalances v36 expansion. |
| 2 | §3.6 | **Survey table added (MANDATORY 4.5/5)**: Bong + Proietti prose bullets → compact survey table (experiment, year, measurement type, θ, equatorial?, ref). Bong: θ = π/2, equatorial. Proietti: BSM, functionally equivalent (footnote). | 4.5/5 | S1 audit evidence existed but was invisible to main-text reader. Table converts claim from "trust our search" to "here's the data — check it yourself." |
| 3 | §3.4 | **Lemma 1 (Non-Absorption) formalized**: Prose defense → numbered Lemma 1 with compact proof. "The cos θ term in Eq. (4) cannot be absorbed by unitary redefinition." Proof: passive relabeling → δ⟨AB⟩=0 vs Eq.(2) couples to Friend outcome d → δ⟨AB⟩∝β cos θ. QED. Cross-reference in §5.3. | 4.0/5 | v26-v35 proof was dressed as exposition. Lemma with QED signals "proved," not "argued." Content identical; packaging is the fix. |
| 4 | §5.3 | **β ecosystem comparison (+8 lines)**: SME photon-sector <10⁻²³, CSL collapse λ≈10⁻¹⁶ s⁻¹, weak-measurement anomalies ~10⁻². β≥0.04 constraint places overlap-dependent deformation at ~10⁻² scale — comparable to weak-measurement anomalies. S3 pointer. | 4.3/5 | β existed in vacuum. Three phenomenological scales bracket target sensitivity — gives β intellectual company without fabricating theory. |
| 5 | §6 | **Statistical robustness methodology**: "Bootstrap resampling...recommendations" → three-part: (i) bootstrap of time-ordered data, (ii) correlated drift model, (iii) fake-signal injection test. | 4.0/5 | Paper delegated validation to implementing lab. Naming three methods shows proposer has thought through realistic failure modes. |
| 6 | §3.1, §5.3 | **smoking-gun→distinctive signature (MANDATORY 4.5/5)**: v36 "smoking-gun...cannot be explained by" → "distinctive...is distinct from standard systematic profiles...difficult to reproduce without overlap-dependent physics." §5.3: "smoking-gun test" removed, "cannot be produced by" → "is distinct from," added Lemma 1 cross-reference. | 4.5/5 | Direct correction of v36 overreach. "Cannot" is absolute — reviewer constructs counterexample. "Distinct from standard profiles" + "difficult to reproduce" preserves logic while falsifiable. |
| 7 | §3.5 | **Overlap-symmetry figure ref**: "[Figure X: Balanced vs tilted overlap geometry — at equator all overlaps = 1/2 (symmetric); at θ≠π/2 basis tilts toward one Friend outcome, creating cos θ asymmetry...]" | 3.8/5 | Core geometric insight never visualized. Below threshold but user-flagged + 1 line cost. |
| 8 | §3.6 closing, §1 | **Null-point narrative**: "convention, not constraint" → "may have unknowingly operated exactly at a geometric null point." §1: "structurally blind" → "may have unknowingly operated at a geometric null point." | 4.3/5 | Strongest narrative previously unstated. Self-evidently true from theorem, more dramatic and more precise than "structurally blind." |
| 9 | §4.1 | **Analytic θ=31° intuition**: "Analytically, the figure of merit approximates FOM(θ) ∝ min(| cos θ |, f_LF(θ)), where f_LF(θ) is a monotonically increasing function of θ...the intermediate optimum emerges from the intersection of these competing trends." | 3.8/5 | θ=31° was black-box grid search. Analytic structure shows optimum is intersection of two monotonic trends — not arbitrary. Below threshold but user-flagged. |
| 10 | §1 | **S3 description expanded**: +GPT state-effect duality derivation, weak measurement connection. S2: +statistical robustness methodology. | 4.0/5 | Reader sees where detailed motivation lives after v37 moved GPT/weak-measurement detail to supplement. |

### Regression
Δ: C17 detail→S3; C18 Lemma 1 formalized; C20 corrected v36 overreach.
---

## v36 (2026-05-25) — 10-point review RCA (threshold 4.5/5): GPT motivation deepened, β as registration-memory coupling, weak measurement cite, cosθ smoking-gun signature, minimal phenomenological class, blind spot→systematically unexplored, optimization landscape fig ref, QWP+timing+stats→S2

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §2.3 Core idea | **GPT motivation deepened (+3 lines)**: "Within the GPT framework [17], Eq. (2) parametrizes the simplest one-parameter deformation of the Born rule" → "Within the GPT framework [17], where measurement statistics arise from a state-effect duality on a convex operational space, Eq. (2) parametrizes the simplest one-parameter deformation of the effect operators that depends on the relative orientation between measurement contexts." GPT was a name-drop (v27, compressed in v29); now it's an argument connecting GPT structure to the specific functional form. | 4.2/5 | GPT bridge was added in v27 but compressed to a shallow citation in v29. Reviewer reads "GPT" as window-dressing unless the paper shows WHY GPT structure naturally accommodates overlap-dependent deformation. State-effect duality + convex operational space = natural home for overlap-dependence. |
| 2 | §2.3 Core idea | **β as registration-memory coupling strength**: "β controls the strength of any departure from perfect factorization" → "β functions as a registration-memory coupling strength: the overlap \| ⟨b\ |d⟩\|² quantifies how compatibly the Superobserver's measurement basis registers the Friend's recorded outcome, and β controls how strongly the registration retains memory of the Friend's outcome orientation." | 4.3/5 | β was defined mathematically as "deformation strength" (v32) but lacked an intuitive physical metaphor. "Registration-memory coupling strength" gives reviewers a concrete mental model without fabricating a microscopic theory. |
| 3 | §2.3 Core idea, Refs | **Weak measurement parallel + cite [18]**: Added "This structure parallels the weak measurement formalism [18], where postselection-conditioned measurement outcomes likewise depend on the overlap between pre- and post-selected states." New reference: Y. Aharonov, D.Z. Albert, and L. Vaidman, Phys. Rev. Lett. 60, 1351 (1988). | 4.5/5 | "Why should nature care about overlap?" — weak measurement is the established physical framework where overlap-dependence is already recognized as a real physical parameter. The conceptual parallel converts "ad hoc" → "natural extension of known physics." |
| 4 | §3.1 | **cosθ smoking-gun signature consolidated (+6 lines)**: New paragraph: "The smoking-gun experimental signature is the cos θ functional form itself: equatorial measurements (θ = π/2) sit at an exact fixed point where all overlap-dependent deformations vanish identically; tilting away from the equator produces a linear onset ∝ cos θ. Any non-zero δ⟨AB⟩ exhibiting this cos θ scaling cannot be explained by standard quantum mechanics with conventional systematic errors — both would produce either null or non-geometric signatures (§5.3, §8.4)." | 4.5/5 | cosθ prediction was distributed across §3.1 (theorem), §5.3 (discriminator), §8.4 (θ-sweep) without a single consolidated statement. "Smoking-gun" paragraph in §3.1 (immediately after main result) gives reviewers the take-home message before they reach experimental sections. |
| 5 | §5.3 | **cosθ as new observable + systematic-error defense**: "The cos θ dependence produces a qualitatively distinct experimental signature that vanishes at θ = π/2 (standard configuration) and is maximal at θ → 0°" → "The cos θ scaling constitutes a new experimental observable...the cos θ signature cannot be produced by conventional systematic errors (which either cancel in δ⟨AB⟩ comparison or produce non-geometric θ-dependence), making it a smoking-gun test for overlap-dependent deformation." | 4.0/5 | cosθ was framed defensively in §3.4 (anti-reparameterization). Framing it as a NEW observable — not just a defense — strengthens the paper's positive contribution. Systematic-error exclusion argument preempts "couldn't this be a calibration artifact?" |
| 6 | §3.2 Scope | **Minimal phenomenological class qualification (+1 line)**: "**Scope limitation.** Proposition 1 constrains the overlap-only class:" → "**Scope limitation.** The overlap-only class is the minimal phenomenological class capturing dependence on \| ⟨b\ |d⟩\|²; we do not claim completeness over all possible deformations. Proposition 1 constrains this class:" | 4.3/5 | v30 scope limitation only said what's OUTSIDE the class. Positive characterization as "minimal phenomenological class" converts a negative boundary into an honest positive statement. "We do not claim completeness" preempts the uniqueness objection. |
| 7 | Abstract, §3.6 heading | **blind spot→systematically unexplored**: Abstract: "common geometric blind spot" → "systematically unexplored geometric degree of freedom". §3.6 heading: "Structural Blind Spot" → "A Systematically Unexplored Polar Angle". | 4.2/5 | "Blind spot" was intentionally chosen in v30 (RCA 4.2/5) as stronger than "appear insensitive." But "blind spot" implies the community overlooked something obvious — evaluative tone that can alienate reviewers. "Systematically unexplored" is a factual description: θ has not been varied, and the structural reason is LF inequality optimization. |
| 8 | §4.1 | **Optimization landscape figure reference (+2 lines)**: Added "[Figure X: Figure of merit vs polar angle θ, showing broad optimum at θ ≈ 31° and 5σ detection boundary spanning θ ∈ [20°, 55°].]" | 3.8/5 | Prose FOM values (v16) are adequate but visual communication is stronger for PRA readers scanning for experimental feasibility. Below threshold (3.8/5) but user-flagged + cost = 1 line. |
| 9 | §4.2, §4.5, §6 | **Engineering/statistical detail → S2 (−13 lines)**: (a) §4.2: Removed QWP retardance tolerance (±2 nm), temperature coefficient (0.01 nm/°C), angular uncertainty (±0.5°) → "QWP specifications...are provided in Supplemental S2." (−4 lines). (b) §4.5: Compressed acquisition timing (91 s per setting, 14 min data, 1 hr total) and drift estimates → 3-line summary + S2 pointer (−5 lines). (c) §6: Compressed statistical model limitations (bootstrap resampling, detector-drift simulation recommendations) → 2-line summary + S2 pointer (−4 lines). | 4.2/5 | v35 de-overpack targeted interpretation/philosophy sections but left engineering details and statistical caveats in main text. For a ~5-page PRA submission, QWP temperature coefficients, acquisition stopwatch timing, and bootstrap methodology belong in supplement. Essential protocol steps and sensitivity estimates retained in main text. |
| 10 | §3.5, §3.6, §4.1, §4.2 positioning | **De-overpack continuation — structural notes preserved, details → supplement**: All conceptual content preserved (physical intuition §3.5 untouched, search methodology §3.6 untouched, calibration §4.4 untouched, sensitivity §5.3 extended). Only implementation-level detail moved to S2. | 4.0/5 | v35 reduced paper from ~627→~600 lines. v36 net change ~+3 lines (additions in §2.3/§3.1/§5.3 offset by compressions in §4.2/§4.5/§6). Paper remains ~5 pages with 18 refs. |

### Regression
Δ: C6+C7 extended (GPT deepened). Blind-spot wording zeroed.
| **Net** | **~600 lines** | **~603 lines** | **+3 lines** |
---

## v35 (2026-05-25) — 2-issue RCA (threshold 4.5/5): §3.4 compress, paper de-overpack (interpretation→S3, search compress, trim verbose sections)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §3.4 | **Compress (−10 lines)**: 18-line defensive exposition → 8-line crisp distinction. Removed: explicit trace formula, POVM equivalence detail, three-observation bullet list. Kept: "passive relabeling relabels outcomes without altering the joint probability distribution" vs "Eq.(2) couples to the physical overlap...which depends on the Friend outcome d — a degree of freedom external to the Superobserver's measurement basis." Added empirical test summary: "passive relabeling predicts δ⟨AB⟩ = 0 for all θ; Eq.(2) predicts δ⟨AB⟩ ∝ β cos θ, verifiable by θ-sweep." | 4.5/5 | §3.4 had grown to 18 lines across v26→v33 as defenses accumulated (non-absorption proof v26, explicit POVM v32, passive-relabeling v33). The core distinction is one sentence: "passive relabeling ≠ coupling to Friend outcome." Three-observation bullet list was redundant with the prose. |
| 2 | §3.6, §8.2+§8.3, §5.3, §3.5 | **Paper de-overpack (−25 lines total)**: (a) §3.6 literature search: 22 lines → 13 lines — removed examined-documents inventory ("We examined the 47-page Supplemental Material of Bong..."), kept search methodology summary + S1 pointer. (b) §8.2+§8.3 merged: "Relation to Quantum Interpretations" (7 lines) + "Illustrative Parametric Model" (8 lines) → single "Interpretation and Model Context" (5 lines) with S3 pointer. Removed δ⟨A₁B₂⟩ = −0.0355 (redundant with §5.3 table) and φ-independence discussion (covered in §5.3). (c) §5.3 Scale context: 5-line SME comparison paragraph → 2-line compact: "A null result at β ≥ 0.04 excludes O(1) and O(10⁻¹) deformation...opening a new parameter space; N = 200,000 extends sensitivity to β ≥ 0.02." SME comparison removed (redundant with §2.3). (d) §3.5 Physical Intuition: 23 lines → 19 lines — removed "In the language of measurement disturbance:" meta-phrase, merged redundant symmetry sentences. Geometric content + measurement disturbance + directional probe + mathematical observation all preserved. | 4.8/5 | The paper had accumulated content across 22 versions without a "main text vs supplement" audit. At 627 lines for a 5-page PRA target, every section was competing for space. The principle: main text = theorem + geometry + minimal protocol + one sensitivity estimate; interpretation + philosophy + detailed methodology → supplement. |

### Regression
Δ: C7 compressed, content preserved.
---

## v34 (2026-05-25) — 4-issue RCA: abstract compression, §2.3 de-lawyer, novelty S1-tied softening, Proposition 1 Definition+compact

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | Abstract | **Compression (−3 lines)**: "of the form P = P_QM · [1 − β · g(overlap)] / Z cancels identically — for any function g whatsoever, not just Eq. (3)" → "P = P_QM · [1 − β · g(overlap)] / Z cancels identically for any function g." "Consequently, existing EWF experiments constrain a smaller theory space than previously assumed: all published implementations operate at the equatorial fixed point and are structurally silent on the overlap-only class." → "Consequently, published EWF implementations are structurally insensitive to the overlap-only class." | 4.3/5 | Abstract was packing 6 distinct pieces of information (theorem, universality, theory-space claim, experiment, sensitivity, loophole). Compressed theory-space sentence from 3 lines to 1 while making it MORE forceful ("structurally insensitive" is sharper than "constrain a smaller theory space than previously assumed"). |
| 2 | §2.3 | **De-lawyer (−12 lines)**: (a) Removed meta-paragraph "Before presenting the theorem, we explain which class..." (3 lines). (b) Compressed Eq.(2) terminology note: "previously termed outcome-dependent coupling in preliminary drafts..." → deleted (2 lines). (c) Compressed constraints: 8-line detailed (i)-(iii) → 4-line compact version: "The three constraints — (i) rotation invariance, (ii) alignment limit g(1)=0, (iii) monotonicity — force the leading-order Taylor expansion g(x) = c₁(1−x) + O((1−x)²)." (d) Removed "Constraints (i)-(iii) are not exhaustive — they are the minimal set for a one-parameter family" (implied by the structure; defense unnecessary). (e) Compressed null test from 5 lines to 2: "The experiment is a null test: standard QM predicts the same LF violation regardless of θ; a θ-dependent signal would indicate a departure from standard QM independently of model class." | 4.5/5 | §2.3 was doing defend+define+motivate+disclaim+compare GPT+compare SME+explain geometry — 7 rhetorical moves in one section. The "lawyer-like" feel came from arguing against imaginary reviewers. Cuts preserve all substantive content while removing meta-commentary and defensive accretion. Section now reads as confident exposition, not preemptive defense. |
| 3 | §9 | **Novelty S1-tied softening**: "Every published EWF experiment has operated at this fixed point; the overlap-only class has therefore remained structurally invisible to all existing tests." → "Within the surveyed literature (Supplemental S1), published EWF implementations have operated at this fixed point; the overlap-only class has therefore remained structurally untested." | 4.3/5 | Absolute novelty claims ("Every published...") are maximally vulnerable to one obscure counterexample. Tying the claim to the S1 audit methodology converts an absolute negative into a methodology-backed finding. "Structurally untested" is more precise than "structurally invisible." |
| 4 | §3.2 | **Proposition 1 formalization**: Added formal **Definition (Overlap-only class)** before Proposition 1: "P'(a,b \| x,y) = P_QM(a,b \ | x,y) · g(\|⟨b\|d⟩\|²) / Z, where g: [0,1] → ℝ is any function and Z normalizes the distribution." Proposition 1 reformatted as compact theorem statement: "Let g be any function. At θ = π/2, \|⟨b\|d⟩\|² = 1/2 for all outcome pairs (b,d). Hence g(\|⟨b\|d⟩\|²) = g(1/2) is constant, and P'(a,b \| x,y) = P_QM(a,b \| x,y). The equatorial plane is a fixed point of every overlap-only deformation. ∎" Title changed from "Universality within overlap-only deformations" → "Equatorial Fixed-Point Theorem." | 4.5/5 | Proposition 1 was prose-heavy ("Therefore...and the modification factor [1 − β · g(...)] / Z reduces to..."). The Definition→Theorem structure makes the mathematical content immediately visible to reviewers scanning for rigor. "Equatorial Fixed-Point Theorem" as the proposition name reinforces the paper's single headline (v31). |

### Regression
Δ: C16 NEW (S1-tied softening §9); C3+C14 extended.
---

## v33 (2026-05-25) — 6-issue RCA: uniqueness→simplest hedge, §3.4 passive-relabeling soften, scope qualifier, SME→phenomenological, repetition de-echo, registration-fidelity structural observation

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §2.3 Core idea | **"Unique"→"simplest" hedge**: "is the unique (to leading order) one-parameter form" → "is the simplest leading-order form satisfying them — every smooth function obeying (i)-(iii) shares the same first-order structure g(x) ∝ (1−x)." | 4.5/5 | "Unique" under unspecified regularity assumptions invites mathematician/philosopher attack. "Simplest" + explicit statement that all share the same leading-order structure is both safer and more precise. |
| 2 | §3.4 | **Passive-relabeling soften**: "they produce identical joint statistics with any second-system measurement" → "under passive basis relabeling, they represent the same physical measurement and the joint statistics are unchanged." | 4.2/5 | "Any second-system measurement" overclaims — technically correct for fixed POVM but could be read as "any operational context." "Passive basis relabeling" is the precise mathematical operation and cannot be misinterpreted. |
| 3 | §3.6 | **Scope qualifier**: "so no equatorial experiment can detect or exclude any member of this class" → "no equatorial experiment can detect or exclude any member of this class, within the overlap-only class" (v32). v33 further refined to: "cannot distinguish standard QM from any overlap-dependent deformation within this class." | 4.0/5 | "Exclude any member" without scope qualifier invites "exclude under THIS parametrization only." Explicit "within this class" + "overlap-dependent deformation" closes the ambiguity. |
| 4 | §2.3 | **SME→phenomenological parameter searches**: "like the Standard Model Extension for Lorentz violation [15], it defines..." → "similar in spirit to phenomenological parameter searches (e.g., the Standard Model Extension for Lorentz violation [15]), it defines..." | 4.2/5 | Quantum foundations reviewers can be allergic to SME analogies when no deep EFT structure exists. "Phenomenological parameter searches" is the genus; SME is an example species. Reduces attack surface while preserving the analogy's force. |
| 5 | §3.6, §9 | **Repetition de-echo**: "constrain a smaller theory space than previously assumed" appeared verbatim in Abstract, §3.6, and §9 (v32). §3.6 reworded to: "The structural implication is that...existing experiments, operating exclusively at this fixed point, cannot distinguish standard QM from any overlap-dependent deformation within this class." §9 reworded to: "Every published EWF experiment has operated at this fixed point; the overlap-only class has therefore remained structurally invisible to all existing tests." | 4.0/5 | Three verbatim repetitions of the same headline sentence across Abstract/body/Conclusion read as padding. Varied wording preserves the claim while avoiding echo. Abstract keeps canonical statement. |
| 6 | §3.5 | **Registration-fidelity structural observation**: Added 5-line mathematical observation after directional probe metaphor. "Mathematically, such terms are the leading-order expression of any smooth registration-fidelity function that depends on measurement alignment: the first-order correction away from perfect alignment generically has the structure 1 − β·(1 − | ⟨b |d⟩|²). Eq.(2-3) isolates this universal geometric structure without committing to a specific physical mechanism." | 3.8/5 | User-requested partial fix. Stops short of a full toy model (which would invite attack as speculative) but demonstrates that the term's structure is mathematically generic — any smooth fidelity function has this leading-order form. Framed as mathematical observation, not physical claim. |

### Regression
Δ: C7 extended; C13+C14 harmonized (de-echo).
---

## v32 (2026-05-25) — 7-issue RCA: Eq.(2) uniqueness+measurement disturbance, universality sharpening, explicit δ⟨AB⟩=0 no-go, practical sensitivity range, defensive tone trim, observer-record alignment narrative, theory-space constraint reframing

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | Abstract, §2.3, §3.5 | **Eq.(2) physical grounding**: §2.3 Core idea — "is the unique (to leading order) one-parameter form satisfying them" replaces "any function...has identical leading-order structure." Added measurement-disturbance framing: "Physically, Eq.(2) parametrizes a residual measurement disturbance: the overlap | ⟨b |d⟩|² quantifies how compatibly the Superobserver's measurement basis registers the Friend's recorded outcome." Harmonized L129 "not its unique member" → "shares the same leading-order structure g(x) ∝ (1−x); Eq.(3) adopts the simplest full representative." | 3.8/5 | User-requested partial fix. GPT bridge (v27) + benchmark (v30) already provide substantial grounding. Strengthening uniqueness claim + measurement-disturbance narrative adds physical motivation without fabricating a toy model. |
| 2 | Abstract, §9 | **Universality sharpening**: "any overlap-dependent modification" → "every overlap-dependent modification." "for every function g" → "for any function g whatsoever." "establish" → "prove" (Abstract). "As its experimental consequence" → "As its direct experimental consequence" (§9). | 4.2/5 | v27/v30/v31 already centered the theorem but language was not maximally forceful. The universality is the paper's single strongest claim — the wording should reflect that. |
| 3 | §3.4 | **Explicit no-go δ⟨AB⟩=0 calculation**: Added explicit unitary POVM equivalence argument. "Under a unitary change of measurement basis | b'⟩ = U |b⟩, the correlator ⟨AB⟩ = Σ_{a,b} a·b·Tr(Π'_a ⊗ Π_b ρ) is identically invariant...Π'_a = U Π_a U†; since {Π'_a} and {Π_a} are unitarily equivalent POVMs on the same Hilbert space, they produce identical joint statistics." Contrasted with Eq.(2): "the modification couples to the Friend outcome d, which is external to the Superobserver's measurement basis." | 4.5/5 | v26 non-absorption proof was qualitative. Reviewer's #1 attack ("isn't this just basis relabeling?") requires quantitative counter-demonstration. Explicit δ⟨AB⟩=0 for unitary case vs δ⟨AB⟩∝β cos θ for Eq.(2) is the decisive discriminator. |
| 4 | §5.3 | **Practical sensitivity range**: Added "Accounting for realistic systematics (§6-7), the practical sensitivity floor is likely β ∼ 0.05–0.10 (single-setting) and β ∼ 0.04–0.06 (combined)." | 4.0/5 | v26 Bayesian + v28 "order-of-magnitude" qualifier + v30 mechanism names already addressed optimism. Explicit range quote preempts "this assumes perfect conditions" objection. |
| 5 | §2.3 IS-NOT, §9 | **Defensive tone trim**: §2.3 IS-NOT triple negation ("not a hidden-variable model, not a collapse modification, not a signal between observers") → single S3 pointer ("ontological classification in Supplemental S3"). §9 removed one "To our knowledge" — theory-space constraint sentence implies novelty without explicit hedge. | 3.8/5 | User-requested partial fix. v29 (−54 lines) + v31 (−25 lines) already cut most defensive accretion. Remaining cuts are surgical: IS-NOT triple was the last redundant negation block; §9 hedge made redundant by theory-space reframing. |
| 6 | §3.5 | **Observer-record alignment narrative**: Extended physical intuition from purely geometric symmetry argument to measurement-disturbance language. "The Superobserver's measurement apparatus is equally aligned with every Friend record — the act of reading the record disturbs both outcomes identically." "At the equator, the registration is perfectly balanced." "The measurement apparatus becomes a directional probe for registration-layer structure." | 4.2/5 | v19+v28 geometric intuition explained WHY geometrically but not WHY physically. "Observer-record alignment" + "measurement disturbance" + "directional probe" provide the physical narrative reviewers will ask for. |
| 7 | Abstract, §3.6, §9 | **Theory-space constraint reframing**: NEW framing: "Consequently, existing EWF experiments constrain a smaller theory space than previously assumed: all published implementations operate at the equatorial fixed point and are structurally silent on the overlap-only class." Applied in Abstract (L18-20), §3.6 (L297-301), §9 (L605-607). §3.6 addition: "no equatorial experiment can detect or exclude any member of this class." §9 addition: "The experiment accesses a geometric degree of freedom that has remained unprobed across every published EWF implementation." | 4.5/5 | Completely new reframing. Converts "we found a blind spot" (negative framing) into "existing experiments constrain a smaller theory space than assumed" (substantive reframing). Addresses the "just a null test" objection by grounding the paper's contribution in what existing experiments FAIL to constrain. |

### Regression
Δ: C7+C9 extended; C13+C14+C15 harmonized.
---

## v31 (2026-05-25) — 9-issue RCA: novelty softening, Eq.(2) motivation repositioned, thesis repetition cuts, theorem-box restructure, experimental feasibility, reparameterization defense, multi-observer → S3, defensive tone reduction, headline consolidation

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | Abstract, §3.6, §9 | **Novelty softening**: "share a structural experimental blind spot" → "share, to our knowledge, a common geometric blind spot". §3.6: "To our knowledge, no published EWF implementation has systematically probed θ". §9: "To our knowledge, no published EWF implementation has probed this geometric degree of freedom." Removed "obvious in hindsight" phrasing (v30 coda cut entirely). | 4.3/5 | Asymmetric hedging — §7 hedged (v28) but §3 and Abstract still absolute. "To our knowledge" consistent throughout. |
| 2 | §2.3 | **Eq.(2) motivation repositioned**: GPT/operational framing (v27 bridge) moved from end of §2.3 to "Core idea" paragraph — now appears BEFORE Eq.(2) first use. "Within the GPT framework [17], Eq.(2) parametrises the simplest one-parameter deformation of the Born rule preserving normalization and remaining operationally admissible." Reader encounters operational grounding before seeing the equation. | 4.4/5 | Temporal ordering — GPT motivation buried after 70 lines (L163 in v30); should precede Eq.(2) at L115. |
| 3 | §1, §2.3, §5.3, §9 | **Thesis repetition cuts (~30 lines)**: Deleted/compressed 7 redundant "not claiming new physics" / "does not claim...exists in nature" instances across §1, §2.3 (two blocks), §5.3, §9. Preserved ESP boundary (§1 L57-61) as the ONE canonical disclaimer. §2.3 ontological classification → 1-line inline. §2.3 null test framing → 2 sentences. §5.3 "no a priori prediction" → 2 sentences. §9 focuses on theorem + experiment, drops "not claiming" echo. | 4.5/5 | Defensive accretion — each v13-v30 round added hedges without global dedup. Repetition reads as lack of confidence. |
| 4 | §3 | **Theorem-box restructure**: §3 reordered to PRA convention. NEW order: §3.1 Main Result (Eq.4) → §3.2 Theorem (Proposition 1 + Corollary + Scope + Examples) → §3.3 Proof (Eqs 5-11) → §3.4 Reparameterization defense → §3.5 Physical Intuition → §3.6 Structural Blind Spot. Previously: proof appeared before theorem statement. Reader now encounters Proposition 1 before its proof. | 4.6/5 | Missing theorem-box pattern — PRA papers lead with boxed theorem, then proof follows. Proposition 1 was buried after 35 lines of proof mechanics. |
| 5 | §4.5 (NEW) | **Experimental feasibility**: NEW 8-line "Practical Feasibility" subsection after §4.4 Calibration. Coincidence rate ~1000/s (Bong 2020) → 91s per setting → 14 min data acquisition. Including calibration: ~1 hour total. SPDC brightness drift <5% over 30 min. Detector dark-count drift ~1% sub-dominant to Poisson. | 4.2/5 | Feasibility gap — protocol paper without back-of-envelope runtime estimate. Reviewer asks "can this actually be done?" |
| 6 | §3.4 (was §5.4) | **Reparameterization defense relocated**: Moved non-absorption proof from §5.4 to §3.4 (immediately after proof, before physical intuition). Expanded with explicit counterexample: "Under unitary basis redefinition | b'⟩ = U |b⟩, the correlator ⟨AB⟩ is invariant — unitary redefinitions produce δ⟨AB⟩ = 0 for all θ. In contrast, Eq.(2) modifies P multiplicatively with a factor depending on physical overlap |⟨b|d⟩|², which changes under θ-rotation." Three-point (a)/(b)/(c) structure preserved + S3 pointer. | 4.5/5 | Over-compression of critical defense — reparameterization objection is #1 reviewer attack. Now reader sees defense immediately after theorem. |
| 7 | §8.4 | **Multi-observer → S3**: "~11× amplification" multi-observer paragraph → replaced with 2-line pointer: "Multi-observer extensions are discussed speculatively in Supplemental S3; these require additional bridge theorems not established here." Full speculative analysis preserved in S3. | 4.3/5 | Speculative claim in main narrative — conditional amplification results from unproven bridge theorems. |
| 8 | §3.6, §9 | **Defensive tone reduction**: Cut all "obvious in hindsight" (2 instances: §3.6 L290 v30, §9 coda v30). Reduced "not claiming X" from 7 to 1 instance (ESP boundary only). §3.6 operational significance → factual: "The three-line proof confirms that θ has been experimentally unexplored." §8.3 "does not depend on this embedding" retained (informative, not defensive). | 4.4/5 | Missing tone pass — content-focused RCA accumulated anxiety markers without tone audit. |
| 9 | Abstract, §1, §9 | **Headline consolidation**: "equatorial fixed-point theorem" established as the paper's single headline. Abstract opens with theorem name + Proposition 1. §1 L34: "This paper establishes the equatorial fixed-point theorem (Proposition 1, §3)." A/B logical distinction preserved but A privileged: "The theorem (Claim A) is the central result; the experimental protocol (Claim B, §4-7) is its direct consequence." §9: leads with "The central result is the equatorial fixed-point theorem (Proposition 1)." | 4.5/5 | A/B split dilutes impact — defensive A/B structure (v27) masked clarity. Single headline privileges the theorem. |

### Regression
Δ: C2+C6 repositioned; C7 moved to §3.5.
---

## v30 (2026-05-25) — 7-issue RCA: structural blind spot framing, Eq.(2) benchmark subordination, trivial-algebra defense, uniqueness scope, statistical conservatism, paper compression, terminology shift

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------| 
| 1 | Abstract, §1, §3 heading, §3.3, §10 | **Novelty reframing**: "appear insensitive" → "structural experimental blind spot" + "unprobed geometric degree of freedom". §3 heading: "Geometric Cancellation" → "Structural Blind Spot". §3.3 heading: "Structural Insensitivity at the Equator" → "Structural Experimental Blind Spot". Abstract leads with "share a structural experimental blind spot". §10: "geometric observation" → "structural experimental blind spot"; added "The algebra is obvious in hindsight; the experimental blind spot is not." | 4.2/5 | Novelty framed as absence of prior work instead of structural impossibility at equator. "Structural blind spot" + "unprobed degree of freedom" are substantive scientific claims, not marketing. |
| 2 | §2.3 Status, §3.1, §5.3 | **Eq.(2) benchmark subordination**: "test parametrization" → "benchmark parametrization" throughout (§2.3 core idea, IS-NOT, Status, GPT). §3.1: added "This result is model-independent...Eq.(2-3) is a benchmark parametrization for quantifying experimental sensitivity; the theorem holds for any overlap function." §2.3 core idea: added "The model-independent theorem (Proposition 1, §3) is the central result; Eq.(2-3) serves as a benchmark parametrization for quantifying experimental sensitivity." §5.3 header: "Outcome-Dependent Modifications" → "Overlap-Dependent Deformations"; opening: "model class" → "benchmark parametrization". | 4.3/5 | Eq.(2) over-defended as if it's THE result. Subordinating to "benchmark" makes theorem the star, Eq.(2) the measurement tool. |
| 3 | §3.3 | **Trivial-algebra defense**: "Although the algebra is compact...non-trivial" → "The algebra is obvious in hindsight...but the geometric degree of freedom θ has been experimentally unexplored...The simplicity of the proof is precisely why the blind spot persisted: equatorial measurement was adopted as a convention, not tested as a constraint." | 4.5/5 | 3-line proof risks "too obvious to publish". Preempt with "obvious but unexplored" — the simplicity IS the explanation for the blind spot. |
| 4 | §3.2 (after Corollary) | **Uniqueness scope boundary**: NEW 7-line "Scope limitation" paragraph. "Proposition 1 and its Corollary constrain the overlap-only class...Broader deformations — depending on the full density matrix, higher-order correlators, or non-geometric variables — lie outside this theorem's scope and remain open." | 4.4/5 | Reviewer: "what about deformations outside overlap-only class?" Explicit scope boundary prevents overstating universality while acknowledging open territory. |
| 5 | §6 Bayesian | **Statistical conservatism**: "modeling uncharacterized systematics as a multiplicative factor" → "modeling uncharacterized systematics (detector drift, waveplate miscalibration, correlated noise from source brightness fluctuations) as a multiplicative factor". | 4.0/5 | 5σ with β≈0.04 looks optimistic without naming specific degradation mechanisms. Three concrete sources now anchor the 20% inflation estimate. |
| 6 | §7, §8 (old) | **Paper compression**: §7.1-7.2 tables → inline summary (5 lines) with "Full μ and η tables in Supplemental S2". §7.3 systematic table → 4-line summary with "Full table in Supplemental S2". §7.4+detection loophole+false-positive+Bell analogy → compressed single-flow section. Old §8 (Loophole Analysis table) → merged into §7 as "Loophole summary" sub-table. Old §9 → §8, old §10 → §9. Net: ~85 lines removed. | 4.0/5 | Paper 7 pages for a 3-line-proof core idea. Robustness details belong in supplement; main text keeps summary + critical loophole defense. |
| 7 | Throughout | **Terminology shift**: "outcome-dependent coupling" → "overlap-dependent deformation" as running term. First use in §2.3 with explicit note: "previously termed 'outcome-dependent coupling' in preliminary drafts; the present name emphasizes geometric content over causal implication." "coupling strength" retained for β. §2.3 heading: "Outcome-Dependent Coupling" → "Overlap-Dependent Deformation". | 4.5/5 | "Outcome-dependent" sounds like hidden variables / retrocausal. "Overlap-dependent deformation" is geometrically precise and neutral. |

### Regression
Δ: C10+C11 NEW (terminology shift); C5 extended.
---

## v29 (2026-05-25) — 10-issue RCA: reviewer tone & positioning overhaul

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | Header | **Version bump**: v28 → v29. | — | Tracking. |
| 2 | Abstract | **3-beat restructure**: "All published...share" → "Existing...appear insensitive to a geometric degree of freedom". Compressed from 15 → 10 lines. Removed intermediate proof steps; leads with observation, consequence, then limitations. | 4.5/5 | Abstract read as proof-of-theorem; reviewer wants concise pitch. 3-beat (observation → experiment → scope) is standard PRA abstract. |
| 3 | §1 | **Claim A soften**: "we prove that all existing...share" → "we show that existing EWF implementations appear insensitive to". | 4.2/5 | "Prove all" invites "but you didn't check X". "Show...appear" matches epistemic status (S1 audit-backed, not exhaustive). |
| 4 | §2.3 Status | **Compress**: 7 lines → 3 lines. Removed "Parametric frameworks routinely precede..." (redundant with SME cite). Single sentence: "Like SME, this is a test parametrization — a target, not a theory." | 4.3/5 | Defensive accretion from v14/v16 — reviewer reads repetition as uncertainty. |
| 5 | §2.3 GPT | **Compress**: 12 lines → 6 lines. Removed detailed constraint-mapping narrative. Kept: "simplest one-parameter deformation... preserves normalization, respects (i)-(iii), remains admissible." | 4.4/5 | v27 GPT bridge over-elaborated admissibility conditions. Compact version signals confidence. |
| 6 | §2.3 null test | **"new physics" → "departure from standard QM"**: "that would indicate new physics independently of which specific model class" → "that would indicate a departure from standard QM predictions independently of model class". | 4.6/5 | "New physics" is marketing language that invites rejection. "Departure from QM predictions" is operationally precise. |
| 7 | §3.3 (after proof) | **Operational significance bridge**: 4-line paragraph — "Although the algebra is compact (three-line proof), its experimental consequence is non-trivial: θ constitutes a previously unprobed geometric parameter..." | 4.0/5 | Gap between compact proof and experimental implications. Reader needs explicit "so what?" bridge. |
| 8 | §5.4 | **Compress**: 9 lines → 4 lines. Full argument moved to Supplemental S3; main text retains (a)/(b)/(c) summary with S3 pointer. | 4.1/5 | Defensive text that duplicates S3 content. Main text needs conclusion, not full proof. |
| 9 | §7.3 | **Detection loophole compress**: 25 lines → 8 lines (two-obs defense) + 13 lines → 12 lines (false-positive argument + fair-sampling + SNSPD merged). Net: −18 lines. Bell-test analogy sharpened to single reference [9]. | 4.5/5 | §7.3 was longest defense section (50+ lines). Redundant elaboration (future loophole-free scenarios, fair-sampling historical recap) removed; substance preserved. |
| 10 | §10 | **Conclusion focus**: 19 lines → 11 lines. "geometric theorem" → "geometric observation". Removed θ-sweep and cos θ functional dependence (already in §9.4). Two clean paragraphs: result + experiment. | 4.3/5 | Conclusion restated material from §3 and §9.4. Compact conclusion signals paper is tight and complete. |

### Regression
Δ: −54 lines (C9 Abstract 3-beat NEW; C6 GPT bridge compressed).
---

## v28 (2026-05-25) — 7-issue RCA: defense compression, physical intuition, universality scoping, sensitivity qualifiers, novelty softening

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §2.3 | **Heading + Core idea reframe**: "Outcome-Dependent Registration" → "Outcome-Dependent Coupling". Core idea uses "symmetry-constrained test parametrization" instead of "phenomenological parametrization". "any smooth function" → "any function" (Prop 1 already covers non-smooth). | 4.2/5 | "Registration" sounds ad hoc / phenomenological. "Coupling" + "test parametrization" aligns with SME analogy and signals no ontological commitment. |
| 2 | Abstract, §2.3, §3.2, §10 | **Universality scoping**: "ANY smooth function" → "any function" (lowercase, drop "smooth" since Prop 1 requires no smoothness). Proposition 1 title: "Universality of equatorial cancellation" → "Universality within overlap-only deformations". Added "overlap-only" qualifier throughout. | 4.4/5 | "ANY smooth g" overstates — reviewer could construct non-overlap dependence. Scoping to "overlap-only deformations" is precise and defensible. |
| 3 | §7, §1 | **Novelty softening**: "the first non-equatorial EWF measurement" → "to our knowledge, the first non-equatorial EWF measurement". §1 ESP boundary: added "to our knowledge" before "the first experimental test of this class". | 4.0/5 | Absolute novelty claims are attack surfaces. "To our knowledge" + S1-backed methodology is both honest and defensible. |
| 4 | §2.3 | **Defense compression (~33%)**: IS-NOT block (10 lines → 6): collapsed three negations into single compound sentence + pointer to S3. Contextuality block (10 lines → 5): removed "physical picture" narrative, kept classification + S3 pointer. Status block (13 lines → 7): compressed SME precedent paragraph by cutting redundant examples. Net: ~19 lines cut. | 4.6/5 | Defensive accretion inflated §2.3 to 80+ lines. Reviewer reads repetition as uncertainty. Compressed prose preserves all logical content while signaling confidence. |
| 5 | §3 (after Examples) | **Physical intuition paragraph**: 8 lines explaining WHY equatorial cancellation occurs. At θ=π/2, | ⟨b |H⟩|²=|⟨b|V⟩|²=1/2 → Superobserver maximally symmetric w.r.t. Friend outcomes → indistinguishable from "no geometric relationship". Tilting breaks this → cos θ asymmetry. | 4.8/5 | Theorem is algebraically clear but physically opaque. Reviewers want to understand WHY, not just verify proof. Intuition bridges formalism to physical picture. |
| 6 | Abstract, §5.3, §10 | **Sensitivity qualifier**: "sensitivity β ≥ 0.04" → "order-of-magnitude sensitivity β ≥ 0.04". Added "(under idealized Poisson statistics; see §6)" to §5.3 threshold statement. | 4.0/5 | Bare "sensitivity" without qualifier invites challenge on systematics. "Order-of-magnitude" is honest and §6 provides Bayesian robustness analysis. |
| 7 | §1 | **Theorem preview**: Added 4-line preview after ESP boundary: "The geometric result itself is compact: f_perp(+1,H) − f_perp(−1,H) = −cos θ (Eq. 4). At θ = π/2, this vanishes for any function of the basis overlap (Proposition 1). The full proof is three lines (§3.2); §2 provides motivation and notation." | 4.3/5 | Reader currently waits until §3.2 to see the theorem. Preview in §1 rewards early reading and signals the paper has a clean, verifiable core result. |

### Regression
Δ: −3 lines (C7 Physical intuition NEW; C8 Theorem preview NEW).
---

## v27 (2026-05-25) — 6-issue RCA: GPT bridge, Proposition 1 (universality), Bayesian robustness, theorem-first positioning, novelty unification

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------| 
| 1 | §2.3 | **GPT/operational bridge expansion**: Replaced shallow POVM mention with explicit GPT framework [17] connection. Eq.(2) = simplest one-parameter deformation within GPT-admissible probability polytope. Constraints (i)-(iii) mapped to GPT admissibility conditions (basis-independence, QM recovery, geometric compatibility). 12 lines replacing 6. | 4.2/5 | "Why THIS modification?" — reviewer wants theoretical grounding deeper than "simplest parametrization". GPT framework provides operational justification without theory commitment. |
| 2 | Abstract, §1, §10 | **Theorem-first positioning**: Abstract restructured — geometry leads, model formula delayed. Proposition 1 cited in abstract. §1 L47-52: "Claim A — the geometric cancellation theorem — is the central result of this paper; Claim B — the experimental protocol — is its direct experimental consequence." §10: leads with "The central result of this paper is a geometric theorem" + Proposition 1 universality. | 4.5/5 | Paper strongest as "geometric blind spot" discovery, not "new outcome-dependent physics". Reviewer more likely to accept theorem than speculative model. |
| 3 | §3.2 | **Proposition 1 + Corollary (formalized universality)**: Replaced informal "Generality" paragraph with numbered Proposition 1: "For ANY function g: [0,1]→ℝ, the modification factor is outcome-independent at θ=π/2." Added Corollary: "No overlap-only deformation evades equatorial cancellation." Added third example g(x)=(1−x)^n. | 4.6/5 | "Infinitely many other deformations exist" — Proposition 1 proves ALL of them cancel at equator. Addresses uniqueness concern by showing the cancellation is universal, making the specific choice of g irrelevant. |
| 4 | §6 | **Bayesian robustness estimate**: 6-line quantitative paragraph. 20% systematic inflation → ~6.5σ effective LF significance, β_min≈0.046. FOM plateau survives up to ~40% inflation. | 4.0/5 | "8.6σ Poisson-only is optimistic" — reviewer wants realistic systematics. Quantitative estimate (not just qualitative v26 recommendation) shows experiment robust under substantial degradation. |
| 5 | §3.3 | **Novelty hedge unification**: Replaced 3-line double-hedged statement ("we are unaware of any...the polar angle does not appear to have been varied") with single sentence: "Within the surveyed literature (S1), we find no published EWF experiment that varies θ from π/2." Single hedge, single sentence. | 4.0/5 | Oscillating strong/soft novelty claims across v17/v19/v25 — unified to one consistent voice. Preserves substance while minimizing attack surface. |
| 6 | Abstract | **Proposition 1 in abstract**: "This cancellation holds for ANY smooth function g of the basis overlap, not just the specific form Eq.(3) (Proposition 1)." Signals universality from first read. | 4.3/5 | Abstract previously pitched specific model; now pitches universal geometric theorem — aligned with "blind spot" positioning. |

---

## v26 (2026-05-25) — 8-issue RCA: POVM bridge, non-absorption proof, naturalness, stats, S3 move, theorem-first

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §2.3 | **POVM/operational bridge**: 6-line "Operational framing" paragraph connecting Eq.(2) to minimal symmetry parametrization of POVM statistics. Emphasizes constraints (i)-(iii) → simplest Born-rule deformation. No theory commitment. | 4.3/5 | "Why THIS modification?" — connects to generalized measurement theory without committing to reconstruction program. |
| 2 | Abstract, §3.3 | **Novelty softening**: Abstract "property" → "insensitivity". §3.3 L262-264: "no EWF experiment has been performed at θ ≠ π/2 for any purpose" → "we are unaware of any EWF experiment performed at θ ≠ π/2". Softens absolute negative while preserving S1-backed methodology. | 4.0/5 | "No prior work identified θ" too strong → soften without regressing v19 systematic-search hedge. |
| 3 | §5.4 (NEW) | **Non-absorption proof**: 3-point argument why Eq.(2) cannot be absorbed into measurement redefinition: (a) unitary preserves trace → δ=0, (b) outcome-pair asymmetry absent from symmetric POVM, (c) θ-sweep empirical discriminator. | 4.4/5 | "This is just adding a bias term" → formal proof it's not gauge-away-able. |
| 4 | §5.3 | **Scale context/naturalness**: 5-line paragraph. Null result at β ≥ 0.04 excludes O(1)/O(10⁻¹). SME comparison (10⁻²³ after decades). First β constraint at ~10⁻² = new parameter space opening. N=200k extends to β ≥ 0.02. | 4.2/5 | β free parameter without natural scale → frame as discovery-phase constraint + scale comparison. |
| 5 | §6, §7.3 | **Statistical robustness**: (a) 10-line "Statistical model limitations" paragraph in §6: Poisson idealization, recommend bootstrap + detector-drift sim. (b) 5-line correlated-systematic note in §7.3: QWP+detector co-variance unmodeled, recommend time-stamped auxiliary data. | 4.0/5 | Sigma estimates "too clean" → acknowledge model limitations + recommend implementing-lab validation. |
| 6 | §2.3 → S3 | **Defense text → supplement**: Moved 25-line contextuality comparison + physical picture from §2.3 to new S3_interpretations.md. Replaced with 10-line compact reference. Net: −15 lines from main text. | 4.1/5 | Paper too long for PRA → move interpretation/philosophy to supplement, keep theorem centerpiece. |
| 7 | Abstract | **Null-test framing**: "structural property" → "structural insensitivity". Aligns abstract with null-test pitch throughout paper. | 4.0/5 | "Foundations speculation" rejection risk → pitch as geometric null test, not new physics of observers. |
| 8 | §3.1 | **Theorem emphasis**: "3.1 — Statement" → "3.1 — Main Result". Combined with Issue 6 compression, theorem becomes visual centerpiece. | 4.2/5 | Theorem buried under phenomenology → theorem-first narrative. |

---

## v25 (2026-05-25) — 12-point review RCA: tone, contextuality, systematics, discriminator

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | Abstract, §1, §3.3, §10 | **Tone softening**: "geometric blind spot" → "structural insensitivity" (4 instances). "first test" → "targeted test". "opens a new axis" → "accesses a previously unprobed geometric degree of freedom". §3.3 heading renamed. | 4.3/5 | Reviewer foundations dị ứng strong marketing wording. Inconsistent softening across sections after v22 only touched §1/§3.3. |
| 2 | Abstract | **A/B distinction**: explicit "Claim A (model-independent theorem)" / "Claim B (null test)" labels in abstract. Mirrors §1 L38-53 structure. | 4.1/5 | Abstract mixed model-independent and assumption-dependent claims without distinction. |
| 3 | §2.3 | **Contextuality comparison**: 13-line paragraph distinguishing Eq.(2) from (a) Kochen-Specker contextuality (no hidden λ), (b) retrocausality, (c) standard measurement contextuality. Dependence is on registration geometry, not measurement context. | 4.2/5 | Reviewer certain to ask "how is this different from contextuality?" v18 IS-NOT paragraph says what Eq.(2) is NOT, but never names Kochen-Specker explicitly. |
| 4 | §3.3 | **Novelty softening**: "To date, no EWF experiment" → "Within the literature surveyed (Supplemental S1), no EWF experiment". Ties claim to methodology. | 4.0/5 | v17 absolute statement ("no EWF experiment has been performed... for any purpose") maximally vulnerable. v19 hedge one paragraph above insufficient. |
| 5 | §5.3 | **Explicit discriminator**: "Standard QM predicts δ⟨AB⟩ = 0 for all θ. Model class predicts δ⟨AB⟩ ∝ β cos θ." Crisp mathematical statement + "not a reparameterization" defense. | 4.5/5 | "Is this genuinely beyond QM?" — discriminator described in prose but never as a displayed statement. |
| 6 | §7.3 (NEW) | **Systematic-error budget table**: 6 sources (QWP drift, birefringence, polarization-dependent loss, calibration offset, detector asymmetry, accidentals). All sub-dominant to σ ≈ 0.0017. Directional argument: all bias δ toward zero, not away. | 4.4/5 | Experimental reviewer will demand consolidated error budget. Individual systematics addressed in v18/v20/v24 but never tabulated. |
| 7 | §10 | **Conclusion reframed**: null-test framing lead. θ-sweep reference added. "Fix:" imperative removed. "A single waveplate opens a new axis" → "accesses a previously unprobed geometric degree of freedom." | 4.0/5 | §10 did not mirror §2.3 null-test framing (v18). |
| 8 | Abstract | **Slimmed**: 15 lines → 12 lines. Removed β ≥ 0.07, μ ≥ 0.92, Δθ ≤ ±5° (moved to body). Kept 8.6σ, β ≥ 0.04, θ = 31°, fair-sampling. | 4.0/5 | 7 numbers in abstract overwhelms first-time reader. |
| 9 | Abstract | **"All existing" → "All published"**: minimal defensive qualifier. | 3.5/5 | Below threshold but costless and ties to S1 audit scope. |
| 10 | §10 | **θ-sweep emphasis**: 1 sentence referencing cos θ functional dependence and θ ∈ [20°, 55°] range (§9.4). | 3.8/5 | Below threshold but user explicitly flagged. Added in §10 only (abstract already dense). |

---

## v24 (2026-05-25) — §2.3 succinct opening + search pipeline + temperature detail

---

## v23 (2026-05-25) — Generality examples + loophole bridge sentence

---

## v22 (2026-05-25) — Intuitive gloss + structural blind-spot explanation

---

## v21 (2026-05-25) — μ-threshold fix + honest abstract + §9.2→S3

---

## v20 (2026-05-25) — f_perp class-representative framing + η-direction analysis

---

## v19 (2026-05-25) — Physical intuition + §2.3 compression + novelty hedge

---

## v18 (2026-05-25) — Ontological clarity + null test framing

---

## v17 (2026-05-25) — Reviewer defense round 2


---

## v16 (2026-05-25) — Reviewer defense round 1


---

## v15 (2026-05-25) — RCA reviewer defense


---

## v14 (2026-05-25) — SME precedent + references


---

## v13 (2026-05-24) — Title + ESP framework audit


---

## v12 (2026-05-24) — Baseline


---


## Recurring Rejected Changes

These objections recurred across ≥4 versions. Each was RCA-scored <4.5/5 every time and is documented once here rather than re-argued per version.

| Topic | Versions Rejected | Root Cause |
|-------|-------------------|------------|
| **β/Eq.(2) ad-hoc — needs physical/ontological motivation** | v30, v32, v33, v36, v39, v40, v41, v43, v44, v45, v48, v52 | Multi-layer defense already: C10 benchmark terminology (v30), lowest-order expansion (v38), phenomenological (v39), measurement disturbance (v32), registration-memory coupling (v36). ESP boundary (C1) prohibits claiming existence in nature (v13). |
| **Paper too long — cut 20-30%** | v39, v40, v43, v44, v45, v48, v52 | Paper already compressed to ~642 lines (~5 pages) via 12+ rounds of cuts (v29 −54L, v30 −26L, v31 −19L, v35 −27L, v43 −3L, v45 −11L, v51 −12L). No large removable blocks remain. |
| **"First"/novelty overclaim — soften further** | v38, v40, v41, v44, v45, v46, v51, v52 | S1 qualifier (C3) applied to all 5 claim locations (v38); "first isolated test" (v41); "new window" (v51). Existing hedging is methodology-backed (S1 audit). |
| **"Just basis rotation" — cosθ is gauge artifact** | v41, v42, v46, v48 | Lemma 1 (v37 formalized) + operational invariant (v42) + forward-ref (v41) + repositioned adjacent to Prop 1 (v46) — 4 defense layers. |
| **Missing killer figure (Bloch sphere)** | v37, v39, v45, v48, v52 | Fig ref exists in §3.5 (v37). Cannot create images in text. |
| **Overlap-only class lacks physical motivation / add toy model** | v33, v36, v37, v45, v48 | ESP boundary (C1): paper does not claim existence in nature. Theorem is structural, not theory-derived. |
| **GPT/contextuality/weak-measurement too speculative** | v39, v43, v44, v45 | GPT derivation → S3 (v37); conceptual chain compressed ~55% (v43). Main text retains 3-4 compact conceptual lines. |
| **Phase 1/Phase 2 framing — "screening test" chưa đủ rõ / cần nhấn mạnh Phase 2 là definitive** | v71, v72, v73, v74, v75, v76, v77 (≥7 consecutive) | Abstract S5 đã rõ: "loophole-open screening test whose positive result would motivate — but not replace — Phase 2 closure." §7: "definitive conclusion." Genre boundary v81: paper là phenomenological null test với two-phase screening architecture. Phase 1 numerical emphasis là do Phase 1 là novel proposal, không phải framing sai. |
| **Abstract hook wording oscillation — "blind spot" vs "operated exclusively at" vs "fixed point"** | v77, v78, v79, v84, v86, v87 | Hook sentence (~10 words) carries dual burden: rhetorical grab + technical precision. These functions conflict — no single wording perfectly satisfies both. Policy: hook's primary function is rhetorical; technical precision lives in S2-S4. As long as hook contains no factual error, wording variants are aesthetic → auto-reject. |
| **Abstract word-count optimization (5↔6 sentences, 150↔185 words)** | v68, v69, v77, v86, v87 | No objective word/sentence target exists — PRA has no formal limit. Without a target, every RCA round finds the abstract either "too long" or "missing key information." Soft range: 150-185 words, 5-6 sentences. Revise only if crossing these bounds. |
| **Abstract structure order oscillation (theorem-first → hook-first → fix-first → factual opening)** | v68, v77, v86, v87 | No external feedback ground truth — all critiques are internal/simulated. Without real reviewer feedback, structure optimization is infinite speculation about an unknown audience. Freeze at v87 structure (factual opening). Revisit only after external feedback (post-arXiv submission). |

---

## FROZEN ITEMS

These are identity/policy-level decisions. RCA pipeline CANNOT auto-approve changes to these items. User override only.

| Item | Frozen Since | Scope | Trigger to Unfreeze |
|------|-------------|-------|---------------------|
| **Title** | v80 (2026-05-26) | Wording frozen at v77: "Have Optical Wigner's Friend Experiments Been Blind to a Geometric Degree of Freedom?" | User explicitly requests title change |
| **Abstract structure order** | v87 (2026-05-26) | Structure frozen at v87: factual opening → theorem → survey → proposal → scope | External reviewer feedback (post-arXiv submission) |
| **§2.3 "Overlap-Dependent Deformation"** | v89 (2026-05-26) | Structure frozen at v89: 4-block hierarchy — (a) Definition & motivation, (b) Methodological role, (c) Physical context (speculative), (d) Null test. ~62 lines. | Genre boundary change (v81 strategic clarification superseded) or external reviewer feedback |
| **§3.5 "An Unisolated Geometric Control Parameter"** | v90 (2026-05-26) | Structure frozen at v90: 3-block hierarchy — (a) Survey findings (table + footnote + search audit), (b) Structural independence from LF optimization, (c) Protocol motivation. ~60 lines. | External reviewer feedback (post-arXiv submission) |
| **§1 "Introduction"** | v91 (2026-05-26) | Structure frozen at v91: 5-block — (a) EWF context (3 lines), (b) "In brief." plain-English summary + ESP/SME, (c) Proposition 1 math-only definition, (d) Protocol preview (3 lines, pointer to §4-7), (e) Claims A+B + verification. ~42 lines. | External reviewer feedback (post-arXiv submission) |

---

## Internal Stability Assessment — v91 (2026-05-26)

**Overall score: 8.0/10 — Internal asymptotic stability reached.**

### 5-Whys RCA

**Q:** Đã đạt trạng thái ổn định tốt nhất chưa?

1. **Why still uncertain?** — Về mặt kỹ thuật, luôn có thể chỉnh sửa thêm. Nhưng câu hỏi thực sự là: *chỉnh sửa thêm có tạo ra cải thiện thật hay chỉ oscillation?*
2. **How to distinguish real improvement vs oscillation?** — CHANGELOG đã ghi nhận oscillation pattern trên 11 topics, tất cả đều bị reject ≥4 lần. Các topic này giờ nằm trong **Recurring Rejected Changes** — hệ thống đã tự nhận diện được ngưỡng bão hòa.
3. **Why is uncertainty still present?** — Toàn bộ 80+ versions (v12→v91) là internal RCA, chưa có external reviewer feedback. **Đây là root cause của uncertainty còn lại.**
4. **Root cause:** Paper đã đạt **internal asymptotic stability** — mọi internal RCA tiếp theo sẽ rơi vào oscillation pattern đã được document. Trạng thái hiện tại là tốt nhất có thể đạt được nếu không có external feedback. Điểm bị trừ (−2.0) đến từ việc thiếu external calibration, không phải từ chất lượng nội tại.

### Stability evidence (strengths)

| Mechanism | Description | Status |
|-----------|------------|--------|
| **FROZEN ITEMS (5)** | Title, Abstract structure, §1, §2.3, §3.5 — all frozen at v87–v91 | Locked |
| **Recurring Rejected Changes (11)** | 11 oscillation patterns auto-rejected: β ad-hoc (12×), "cut 20-30%" (6×), novelty overclaim (8×), Phase 1 framing (7+×), abstract hook wording, abstract word-count, abstract structure order, etc. | Auto-blocked |
| **Regression Constraint Master (C1–C21)** | 21 constraints verified across all versions | Preserved |
| **v81 Genre Boundary** | Paper IS: phenomenological null test with geometric insight / IS NOT: theory derivation | Scope locked |
| **Version density convergence** | v88→v91 all structural consolidation, no content oscillation | Converged |
| **CHANGELOG maturity** | ~1462 lines, 4 dedup rounds, structural tables | Documented |

### Score deductions (−2.0)

| Factor | Impact | Explanation |
|--------|--------|-------------|
| **No external reviewer feedback** | −1.0 | Post-arXiv submission may reveal structural weaknesses invisible to internal RCA. This is the single largest unknown. |
| **N=2 is a hard constraint** | −0.5 | Despite structural defense (v77 "Structural, not coincidental"), this remains a weakness unfixable by internal refinement. |
| **RCA scoring self-referential** | −0.5 | Threshold 4.5/5 calibrated on internal consensus, no external ground truth. Systematic bias risk is low but real. |

### Decision

Paper is **ready for arXiv submission** at current state. Further internal RCA edits are unlikely to produce net improvement — the remaining uncertainty (−2.0) cannot be resolved without external reviewer feedback. After arXiv submission and reviewer response, revisit FROZEN ITEMS and Recurring Rejected Changes with real external data.

---

## Version summary

| Version | Date | Focus | ~Lines | Δ | Refs |
|---------|------|-------|--------|---|------|
| v12 | 2026-05-24 | Baseline — Eq.(12) fix | ~600 | — | 14 |
| v13 | 2026-05-24 | Title + ESP audit | ~600 | 0 | 14 |
| v14 | 2026-05-25 | SME precedent + SNSPD | ~600 | 0 | 16 |
| v15 | 2026-05-25 | RCA defense (VVV-QMRF, loophole, search, §9.4) | ~600 | 0 | 16 |
| v16 | 2026-05-25 | Reviewer defense 1 (S1 audit, θ-sensitivity) | ~600 | 0 | 16 |
| v17 | 2026-05-25 | Reviewer defense 2 (2-obs loophole, constraint scope, β meaning) | ~600 | 0 | 16 |
| v18 | 2026-05-25 | Ontological clarity + null test framing | ~600 | 0 | 16 |
| v19 | 2026-05-25 | Physical intuition + §2.3 compression + novelty hedge | ~600 | 0 | 16 |
| v20 | 2026-05-25 | f_perp class-representative + η-direction | ~600 | 0 | 16 |
| v21 | 2026-05-25 | μ-threshold fix + honest abstract + §9.2→S3 | ~600 | 0 | 16 |
| v22 | 2026-05-25 | Intuitive gloss + blind-spot explanation | ~600 | 0 | 16 |
| v23 | 2026-05-25 | Generality examples + loophole bridge | ~600 | 0 | 16 |
| v24 | 2026-05-25 | §2.3 succinct opening + search pipeline + temperature | ~600 | 0 | 16 |
| v25 | 2026-05-25 | 12-point RCA: tone, contextuality, systematics, discriminator | ~600 | 0 | 16 |
| v26 | 2026-05-25 | POVM bridge, non-absorption proof, naturalness, stats, S3 move | ~600 | −15 | 16 |
| v27 | 2026-05-25 | GPT bridge, Proposition 1, Bayesian, theorem-first, novelty unification | ~600 | 0 | 17 |
| v28 | 2026-05-25 | Defense compression, physical intuition, universality scoping | ~600 | −3 | 17 |
| v29 | 2026-05-25 | Tone overhaul: defensive compression, "new physics" removal | 652 | −54 | 17 |
| v30 | 2026-05-25 | Blind spot framing, benchmark subordination, trivial-algebra, scope, terminology | 626 | −26 | 17 |
| v31 | 2026-05-25 | Novelty softening, Eq.(2) repositioned, thesis cuts, theorem-box, feasibility | 607 | −19 | 17 |
| v32 | 2026-05-25 | Uniqueness+disturbance, δ⟨AB⟩=0 no-go, sensitivity range, theory-space reframing | 634 | +27 | 17 |
| v33 | 2026-05-25 | Simplest hedge, passive-relabeling soften, SME→phenomenological, de-echo | 638 | +4 | 17 |
| v34 | 2026-05-25 | Abstract compress, §2.3 de-lawyer, S1-tied softening, Prop 1 formalization | 627 | −11 | 17 |
| v35 | 2026-05-25 | §3.4 compress, de-overpack (interpretation→S3, search compress) | 600 | −27 | 17 |
| v36 | 2026-05-25 | GPT deepened, β coupling, weak measurement [18], cosθ smoking-gun, S2 moves | 603 | +3 | 18 |
| v37 | 2026-05-25 | EFT-style, Lemma 1 formalized, survey table, soften, β ecosystem, null-point | 630 | +27 | 18 |
| v38 | 2026-05-25 | Survey-qualified hedging, lowest-order justification, novelty-as-geometry | 635 | +5 | 18 |
| v39 | 2026-05-25 | Cancellation rename, §1 reframe (overlooked→structural consequence), ontological→phenomenological | 639 | +4 | 18 |
| v40 | 2026-05-25 | overlooked→not-previously-isolated, non-identifiability, conservative β headline | 643 | +4 | 18 |
| v41 | 2026-05-25 | Lemma 1 forward-ref, operational β definition, "first isolated test" hedging | 648 | +5 | 18 |
| v42 | 2026-05-25 | GPT contextuality chain, Lemma 1 operational invariant, β scale bridge, Abstract 1+1+1 | 655 | +7 | 18 |
| v43 | 2026-05-25 | GPT/weak-meas cut ~40%→S3, φ-scramble control, correlator table→S2 | 652 | −3 | 18 |
| v44 | 2026-05-25 | Structural non-identifiability reframe, contextuality distinction, feasibility softening | 664 | +12 | 18 |
| v45 | 2026-05-25 | Proposition 1 on page 1, historical reason, intro compressed −21% | 653 | −11 | 18 |
| v46 | 2026-05-25 | Lemma 1 moved §3.4→§3.2, section renumber | 653 | 0 | 18 |
| v47 | 2026-05-25 | C3 regression fix (§9), §5.3 dedup, §8.4→§8.3 renumber | 650 | −3 | 18 |
| v48 | 2026-05-25 | "geometric null point" hook in §1 ¶2 | 650 | 0 | 18 |
| v49 | 2026-05-25 | §2.3 double "Equation (2)" fix — rolled into v50 | — | — | 18 |
| v50 | 2026-05-25 | Abstract "null point", φ-scramble forward-ref, Conclusion call-to-action, §8.1 logic fix | 654 | +4 | 18 |
| v51 | 2026-05-25 | β-model subordinated to theorem, "first"→"new", §6 compressed 30→13 lines | 642 | −12 | 18 |
| v52 | 2026-05-25 | De-defensify — 2 "model-independent" removed, ESP tightened | 642 | 0 | 18 |

---

## Regression Constraint Master (canonical — all versions reference this)

| ID | Constraint | Origin | Latest Status |
|----|-----------|--------|---------------|
| C1 | ESP boundary (§1): "This paper does not claim..." | v13 | ✅ Active |
| C2 | Proposition 1 math content unchanged | v27 | ✅ Active |
| C3 | Novelty hedge: "Within the surveyed literature (S1)" | v25 | ✅ Active |
| C4 | §8.2 interpretation-neutrality: "interpretation-neutral by design" | v17 | ✅ Active |
| C5 | §6 Bayesian robustness | v26 | ✅ Active (mechanism names added v30; 3-part methodology named v37) |
| C6 | GPT bridge [17] | v27 | ✅ Active (deepened v36; GPT derivation → S3 v37) |
| C7 | Physical intuition (§3.5) | v28 | ✅ Active (extended v32 observer-record alignment; compressed v35; fig ref v37) |
| C8 | Theorem preview (§1) | v28 | ✅ Active |
| C9 | Abstract 3-beat structure (observation→theorem→consequence→experiment→scope) | v29 | ✅ Active |
| C10 | "benchmark parametrization" terminology | v30 | ✅ Active |
| C11 | "overlap-dependent deformation" terminology | v30 | ✅ Active |
| C12 | Exact numerical values from v12 density-matrix computation | v12 | ✅ Active |
| C13 | §2.3 Core idea ↔ constraint derivation harmonized (unique→simplest hedge v33; Eq.(2) measurement disturbance v32) | v32 | ✅ Active |
| C14 | Theory-space constraint framing across Abstract/§3.6/§9 | v32 | ✅ Active (S1-tied v34; null-point narrative v37) |
| C15 | Practical sensitivity range β∼0.05–0.10 (single), β∼0.04–0.06 (combined) | v32 | ✅ Active |
| C16 | S1-tied novelty softening (§9) | v34 | ✅ Active |
| C17 | GPT/weak-measurement detail in main text → S3 (content preserved in supplement) | v36 | ✅ Active (extended v37) |
| C18 | Lemma 1 (Non-Absorption) formalized in §3.4 | v36 | ✅ Active (extended v37 QED) |
| C19 | All v35 regression constraints (16 items) | v35 | ✅ All preserved |
| C20 | smoking-gun→distinctive signature (§3.1, §5.3): "cannot"→"distinct from" | v36 | ✅ **Corrected v37** (v36 overreach fixed) |
| C21 | v32-specific §2.3↔L129 + §3.4↔§2.3 + theory-space alignment + practical↔Bayesian consistency | v32 | ✅ All harmonized |

**Usage:** Each version entry below references this master. Only items whose STATUS CHANGED or were NEWLY ADDED in that version are listed inline. All other items are `✅ All canonical constraints preserved — see Master.`

---

## RCA methodology

All v13→v37 changes applied via:
1. **5-step RCA** (Define → Trace → Isolate → Fix cause → Verify) per CLAUDE.md Rule Zero
2. **5-Whys** root cause drill (minimum 3 iterations per issue)
3. **Scoring ≥4/5** threshold for mandatory implementation
4. **ESP framework** (Epistemic-Structural-Presentational) for structural audit
5. Fixes scoring 3.0–3.9/5 implemented when user explicitly flagged concern AND fix cost negligible (≤3 sentences)

---

*Generated 2026-05-25, dedup-optimized 2026-05-26. Covers v12 (baseline) through v88 (current).*