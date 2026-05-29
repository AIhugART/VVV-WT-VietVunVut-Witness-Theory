# So Sánh Chi Tiết / Detailed Comparison
## Tài liệu A: [System + Axiom Mapping](../Buddhist_Epistemology_and_Quantum_Measurement_system_axioms_mapping.md) (BE→QM epistemological mapping, 1057 dòng)
## Tài liệu B: [QM Unified Concept Table](../../published_documents/QM_Measurement_Unified_Concept_Table.md) (QM concept reference, 131 dòng)

---

## 1. TỔNG QUAN / OVERVIEW

| Tiêu chí | Tài liệu A (Axioms Mapping) | Tài liệu B (QM Concept Table) |
|---|---|---|
| **Mục đích** | Ánh xạ cấu trúc BE→QM theo 6 tier + 4 axiom | Bảng tra cứu 105 khái niệm QM thuần túy |
| **Hệ thống gốc** | Pramāṇavāda (Dignāga/Dharmakīrti) → QM | QM thuần (Susskind 2014 + Jordan/Siddiqi 2024) |
| **Cấu trúc** | 6 Tiers, 30 nodes, 39 edges, 19 BIAN, 4 axioms | 11 categories, 105 concepts, bảng phẳng |
| **Nguồn** | Tổng hợp triết học so sánh | Hai sách giáo khoa vật lý có RCA |
| **Ngôn ngữ** | Sanskrit/Pāli + English + QM formalism | English + QM formalism + flags Việt |
| **Độ dài** | ~98KB / 1057 dòng | ~45KB / 131 dòng |
| **Tính chất** | Interpretive-analytical (diễn giải phân tích) | Descriptive-referential (mô tả tham chiếu) |

---

## 2. PHẠM VI PHỦ / COVERAGE COMPARISON

### 2a. Các khái niệm QM trong B mà A có ánh xạ BE

| B# | QM Concept (B) | A Tier Item | Correspondence Type (A) | Đánh giá |
|---|---|---|---|---|
| 2 | Quantum State (ket vector) | T1.03 (ψ ↔ Anumāna) | Structural parallel | ✅ Đúng — cả hai là biểu diễn gián tiếp |
| 5 | Superposition | T3.02 (ψ ↔ Sāmānyalakṣaṇa) | Strong parallel | ✅ Đúng — cả hai là abstract construct |
| 8 | Four Postulates of QM | T1.01 (Measurement operator ↔ Pramāṇa) | Structural with divergence | ✅ Hợp lý |
| 14 | Projective Measurement (PVM) | T1.02 (Eigenvalue readout ↔ Pratyakṣa) | Strong parallel | ✅ Đúng — terminal non-inferential event |
| 16 | Born Rule | T5.07 (Born rule ↔ Vyāpti) | Strong parallel | ✅ Đúng — cả hai underived invariant |
| 17 | Observable (Hermitian) | T2.02 (Observable ↔ Viṣaya) | Strong structural | ✅ Đúng — epistemic target vs causal ground |
| 19 | Measurement (Physical Act) | T1.01 (Pramāṇa) + T1.02 (Pratyakṣa) | Structural | ✅ Hợp lý |
| 22 | Post-Measurement State Update | T3.01 (Eigenstate ↔ Svalakṣaṇa) | Strong parallel | ✅ Đúng |
| 23 | Measurement Backaction | T4.01 (Bhrānti — disturbance aspect) | Functional | ⚠️ Yếu — backaction ≠ error |
| 27 | Info–Disturbance Trade-off | T2.05/T2.07 (BIAN-6/7 area) | No direct mapping | ✅ Đúng rằng không có mapping |
| 47 | Entanglement | T3.08 (BIAN-10 — reverse gap) | Partial / BIAN-10 | ✅ Đúng — BE chỉ cung cấp N_BE_00021 làm source analogue; IRB là extension relation |
| 70 | Uncertainty ΔA | T6.05 (Apoha ↔ Complementarity) | Structural at meta-semantic | ⚠️ Gián tiếp |
| 74 | Complementarity (Bohr) | T6.05 (Apoha / exclusion theory) | Structural parallel | ✅ Đúng |
| 76 | Time Evolution (Unitarity) | T5.15 (Schrödinger ↔ Tadutpatti) | Partial | ✅ Đúng |
| 81 | Wavefunction Collapse | T1.02 + T2.05 (BIAN-2/6/16/17) | Multiple BIAN gaps | ✅ Đúng — core asymmetry |
| 87 | Quantum Zeno Effect | T3.04 (Kṣaṇikavāda — BIAN-8) | Partial structural | ⚠️ Gián tiếp |
| 90 | Bell's Inequality | T3.05 (Svabhāva denial) | Negative structural parallel | ✅ Đúng — strongest convergence |
| 91 | Hidden Variable Theories | T3.05 (Svabhāva concept) | Negative parallel | ✅ Đúng |
| 93 | Copenhagen Interpretation | T6.01-T6.02 (BIAN-16/17) | BIAN gaps | ✅ Đúng |
| 94 | Heisenberg Cut | T6.04/Axiom 4 (Dvisatya) | Functional parallel | ✅ Đúng |
| 95 | Decoherence | T6.02 (BIAN-17 — regress) | BIAN gap area | ✅ Đúng |
| 100 | Classical Realism vs Quantum Indeterminacy | T3.05 + T6.06 | Core convergence | ✅ Đúng |
| 101 | Interpretation Maxim | T6.06 (Arthakriyā ↔ praxis) | Deep meta-parallel | ✅ Đúng |

### 2b. Các khái niệm QM trong B mà A KHÔNG ánh xạ (73 concepts)

| Category | B Concepts NOT mapped in A | Count | Lý do |
|---|---|---|---|
| **I. Quantum Foundations** | Qubit (#1), Hilbert Space (#4), Phase Factor (#6), Complex Numbers (#7), Quantum Logic (#9), Degrees of Freedom (#10), Gedankenexperiment (#11), Wave-Particle Duality (#12), Wave Function ψ(x) (#13) | 9 | A dùng ψ ở mức trừu tượng, không đi vào toán học cụ thể |
| **II. Measurement Fund.** | Three Cardinal Properties (#15), Projection Operator (#18), von Neumann Model (#20), System-Meter Coupling (#21), POVM (#24), Density Matrix (#25) | 6 | A mapping ở mức epistemic, không ở mức formalism |
| **III. Generalized/Weak** | Kraus Operators (#26), Info-Disturbance (#27), Weak Measurement (#28), Weak Value (#29), Amplification (#30), Generalized Eigenvalues (#31), Partial Collapse (#32), Null Measurement (#33), Quantum Bayesian (#34), Unselective Measurement (#35) | 10 | Toàn bộ category này không có mapping BE |
| **IV. Continuous Meas.** | Diffusive (#36), Jump (#37), Trajectory (#38), SSE (#39), SME (#40), Wiener (#41), Jump Operator (#42), Strength κ (#43), Path Integral (#44) | 9 | Toàn bộ category không có mapping BE |
| **V. Entanglement** | Tensor Product (#45), Product State (#46), Max Entangled (#48), Singlet (#49), Triplet (#50), Composite Observables (#51), Entanglement by Measurement (#52) | 7 | Chỉ Entanglement (#47) được ánh xạ (BIAN-10) |
| **VI. Spin Systems** | Spin (#53), Pauli (#54), Component States (#55), Polarization (#56), Magnetic Field (#57) | 5 | Spin domain không có BE equivalent |
| **VII. Detectors/Limits** | Linear Detector (#58–69), SQL, Squeezed States, Heisenberg Limit, Josephson, etc. | 12 | Engineering/experimental — ngoài scope epistemic |
| **VIII. Uncertainty** | Uncertainty ΔA (#70), Generalized UP (#71), Simultaneously Measurable (#72), Joint Measurement (#73) | 4 | Chỉ Complementarity (#74) được ánh xạ |
| **IX. Dynamics** | Hamiltonian (#75), Schrödinger Eq. (#77), Poisson-Commutator (#78), Canonical Quantization (#79), Classical Limit (#80), Momentum (#82), Particle Hamiltonian (#83), Harmonic Oscillator (#84), Particle in Box (#85), QND (#86) | 10 | Dynamics phần lớn ngoài scope epistemic |
| **X. Historical** | Stern-Gerlach (#88), EPR (#89), Einstein-Bohr (#92), Schrödinger Cat (#96), HOM (#97), BB84 (#98), Quantum Info Era (#99) | 7 | Lịch sử/thí nghiệm cụ thể — không nằm trong scope |
| **XI. Applications** | Reversal (#102), Feedback (#103), Canonical Phase (#104), Error Correction (#105) | 4 | Ứng dụng — ngoài scope |

**Tổng: 73/105 concepts trong B không có mapping trong A.**

---

## 3. ĐÁNH GIÁ ĐÚNG / SAI — TRUE / FALSE

| # | Luận điểm kiểm tra | Verdict | Giải thích |
|---|---|---|---|
| 1 | **A ánh xạ đúng Born Rule (#16) ↔ Vyāpti?** | ✅ Đúng | Cả hai: underived invariant, empirically confirmed, not foundationally derived. B xác nhận: "Born (1926) linked modulus squared to probability density." A xác nhận: "Not derived from deeper first principles." |
| 2 | **A ánh xạ đúng Projective Measurement (#14) ↔ Pratyakṣa?** | ✅ Đúng | B: "system collapses into single eigenstate." A: "terminal, non-inferential epistemic event." Cấu trúc tương đồng. |
| 3 | **A ánh xạ đúng Observable (#17) ↔ Viṣaya?** | ✅ Đúng | B: "measurable physical quantity, Hermitian operator." A: "epistemic target distinguished from causal ground." Viṣaya-artha ↔ observable-state. |
| 4 | **A ánh xạ đúng Superposition (#5) ↔ Sāmānyalakṣaṇa?** | ✅ Đúng | B: "linear combination, coherent superposition." A: "abstract construct that dissolves upon contact with real instance." |
| 5 | **A ánh xạ đúng Bell (#90) ↔ Svabhāva denial?** | ✅ Đúng | B: "local realistic hidden-variable theories ruled out." A: "denial of context-independent intrinsic properties." Cùng structural result. |
| 6 | **A ánh xạ đúng Entanglement (#47) ↔ BIAN-10?** | ✅ Đúng | B: "correlation with no classical analogue, cannot be factorized." A: "third type beyond tādātmya/tadutpatti." BE genuinely lacks this. |
| 7 | **A ánh xạ đúng Heisenberg Cut (#94) ↔ Dvisatya?** | ⚠️ Đúng nhưng yếu | B: "boundary between quantum and classical domains, movable, arbitrary." A: "quantum-classical boundary is epistemic." Tương đồng cấu trúc nhưng Dvisatya có nội dung sâu hơn (saṃvṛti/paramārtha). |
| 8 | **A ánh xạ đúng Complementarity (#74) ↔ Apoha?** | ✅ Đúng | B: "mutually exclusive arrangements reveal complementary aspects." A: "meaning through exclusion." Cả hai ground meaning in exclusion relations. |
| 9 | **A ánh xạ đúng Collapse (#81) ↔ BIAN-2/16/17?** | ✅ Đúng | B: "collapse not described by Schrödinger equation; requires projection postulate or external meter." A: "absence of self-certifying epistemic layer = measurement problem." |
| 10 | **A ánh xạ đúng Interpretation Maxim (#101) ↔ Arthakriyā?** | ✅ Đúng | B: "interpretation judged by whether it leads to new insights." A: "validity grounded in practical efficacy." Deepest meta-convergence. |
| 11 | **A bỏ qua POVM (#24) / Kraus (#26) — đúng hay sai?** | ⚠️ Thiếu sót | B mô tả generalized measurement rất chi tiết (10 concepts). A chỉ đề cập projective measurement. POVM/Kraus mở rộng measurement concept — A nên thảo luận. |
| 12 | **A bỏ qua Weak Measurement (#28-32) — đúng hay sai?** | ⚠️ Thiếu sót | Weak measurement cho phép partial collapse, partial information — liên quan trực tiếp đến BIAN-8 (kṣaṇikavāda) và gradual epistemic update. A bỏ lỡ cơ hội mapping. |
| 13 | **A bỏ qua Quantum Trajectory (#38) — đúng hay sai?** | ⚠️ Thiếu sót | Trajectory = real-time state tracking — liên quan đến santāna (causal series) trong BIAN-19. Missed opportunity. |
| 14 | **A bỏ qua Decoherence (#95) chi tiết — đúng hay sai?** | ⚠️ Thiếu sót | B: "environment dictates decoherence; decoherence alone does not explain individual outcomes." A chỉ đề cập ngắn. Cần phân tích sâu hơn. |
| 15 | **A bỏ qua Null Measurement (#33) — đúng hay sai?** | ❌ Sai | B: "absence of click constitutes measurement; information from silence." A có BIAN-9 (Abhāva/anupalabdhi) nhưng không cross-reference concept #33. Missed direct parallel. |

---

## 4. ĐÁNH GIÁ TỐT / XẤU — STRENGTHS / WEAKNESSES

### Tài liệu A — Axioms Mapping

| Tiêu chí | Đánh giá | Lý do |
|---|---|---|
| **Chiều sâu triết học** | ✅ Rất tốt | 6 tiers + 4 axioms + BIAN index — phân tích đa chiều, có hệ thống |
| **BIAN gap analysis** | ✅ Rất tốt | 19 gaps xác định chính xác, phân bổ theo axiom, insight "Axiom 3 carries 11/19" |
| **Correspondence classification** | ✅ Tốt | Strong/moderate/functional/partial/negative — phân loại rõ ràng |
| **Node/Edge formal system** | ✅ Tốt | 30 nodes + 39 edges — traceable, reproducible |
| **Phạm vi QM phủ** | ❌ Xấu | Chỉ phủ ~32/105 concepts trong B. Bỏ toàn bộ: generalized measurement, weak measurement, continuous measurement, spin systems, detectors, dynamics |
| **QM formalism accuracy** | ⚠️ Trung bình | Mô tả QM ở mức trừu tượng cao. Không sai nhưng thiếu chi tiết kỹ thuật. Không đề cập POVM, Kraus, SME |
| **Missed mapping opportunities** | ❌ Xấu | Null measurement (#33) ↔ BIAN-9, Partial collapse (#32) ↔ BIAN-8, Quantum trajectory (#38) ↔ BIAN-19 — đều bị bỏ lỡ |

### Tài liệu B — QM Concept Table

| Tiêu chí | Đánh giá | Lý do |
|---|---|---|
| **Phạm vi phủ QM** | ✅ Rất tốt | 105 concepts, 11 categories, từ foundations đến applications |
| **Độ chính xác vật lý** | ✅ Rất tốt | Có RCA verification, formulas chính xác, citations rõ ràng |
| **Source tracking** | ✅ Rất tốt | S/J/S+J flags, [NGOẠI SUY]/[PARTIAL]/[SUY DIỄN] flags |
| **Generalized measurement** | ✅ Rất tốt | 10 concepts (Category III) — POVM, Kraus, weak values, partial collapse |
| **Continuous measurement** | ✅ Rất tốt | 9 concepts (Category IV) — SSE, SME, trajectories, quantum jumps |
| **Thiếu chiều BE** | ❌ Xấu | Không có bất kỳ mapping triết học nào. Thuần mô tả vật lý |
| **Thiếu epistemic analysis** | ❌ Xấu | Không phân tích tại sao measurement problem tồn tại ở mức epistemic |
| **Tổ chức** | ⚠️ Trung bình | Bảng phẳng duy nhất — khó thấy mối liên hệ giữa concepts |

---

## 5. GAPS CẦN BỔ SUNG — MISSED MAPPING OPPORTUNITIES

| B# | QM Concept | A BIAN liên quan | Mapping tiềm năng | Mức độ quan trọng |
|---|---|---|---|---|
| 33 | Null Measurement | BIAN-9 (Abhāva) | "Information from silence" ↔ Anupalabdhi. Direct parallel mà A bỏ lỡ | **Cao** |
| 32 | Partial Wavefunction Collapse | BIAN-8 (Kṣaṇikavāda) | Gradual collapse ↔ causal series of momentary states (santāna) | **Cao** |
| 28 | Weak Measurement | T2.07 (Nirvikalpaka) | Negligible disturbance ↔ near-nirvikalpaka observation | **Trung bình** |
| 38 | Quantum Trajectory | BIAN-19 (Anātmavāda) | Real-time state tracking ↔ observer as causal process, not substance | **Cao** |
| 34 | Quantum Bayesian Update | T6.03 (Svataḥ/Parataḥ) | Bayesian posterior ↔ parataḥ prāmāṇya (extrinsic validation) | **Trung bình** |
| 27 | Info-Disturbance Trade-off | T2.05 (BIAN-6) | Continuous spectrum between no-info and full-collapse ↔ svasaṃvedana spectrum | **Trung bình** |
| 24 | POVM | T1.01 (Pramāṇa) | Generalized measurement ↔ expanded pramāṇa concept | **Cao** |
| 86 | QND Measurement | T5.08 (Kevalānvayin) | Repeated measurement yields same result ↔ universal positive mark | **Thấp** |
| 87 | Quantum Zeno Effect | T3.04 (Kṣaṇikavāda) | Freezing by observation ↔ dissolution of kṣaṇikavāda under continuous observation | **Trung bình** |
| 102 | Measurement Reversal | T4.04 (Bādhaka pramāṇa) | Undoing collapse ↔ epistemic override? New terrain for BIAN-12 | **Cao** |

---

## 6. BẢNG TƯƠNG QUAN CATEGORY / CROSS-REFERENCE TABLE

| B Category | B Concept Count | A Concepts Mapped | A BIAN Gaps | Coverage |
|---|---|---|---|---|
| I. Quantum Foundations | 13 | 4 (State, Superposition, Postulates, Logic) | 0 | 31% |
| II. Measurement Fundamentals | 12 | 6 (PVM, Born, Observable, Measurement, Post-update, Backaction) | BIAN-2,6,16,17 | 50% |
| III. Generalized & Weak | 10 | 0 | — | **0%** |
| IV. Continuous Measurement | 9 | 0 | — | **0%** |
| V. Entanglement | 8 | 1 (Entanglement — BIAN-10) | BIAN-10 | 13% |
| VI. Spin Systems | 5 | 0 | — | **0%** |
| VII. Detectors/Limits | 12 | 0 | — | **0%** |
| VIII. Uncertainty & Complementarity | 5 | 1 (Complementarity) | 0 | 20% |
| IX. Dynamics | 13 | 2 (Unitarity, Collapse) | BIAN-8 | 15% |
| X. Historical & Philosophical | 14 | 6 (Bell, Hidden Variables, Copenhagen, Heisenberg Cut, Decoherence, Realism vs Indeterminacy, Maxim) | BIAN-3,15 | 43% |
| XI. Applications | 4 | 0 | — | **0%** |

**Kết luận: A phủ tốt nhất Categories II (50%) và X (43%). A hoàn toàn bỏ trống Categories III, IV, VI, VII, XI (0%).**

---

## 7. KẾT LUẬN TỔNG HỢP / SYNTHESIS

### Đúng (True)
1. **A đúng** khi ánh xạ Born Rule ↔ Vyāpti, Observable ↔ Viṣaya, Eigenstate ↔ Svalakṣaṇa, Superposition ↔ Sāmānyalakṣaṇa. Tất cả đều được B xác nhận về mặt nội dung vật lý.
2. **A đúng** khi xác định Bell/Kochen-Specker ↔ Svabhāva denial là strongest convergence. B xác nhận: "local hidden-variable theories ruled out."
3. **A đúng** khi xác định measurement problem ↔ absence of Svasaṃvedana (BIAN-2/16/17). B xác nhận: collapse "not described by Schrödinger equation" (#81), von Neumann model requires "external meter" (#20).
4. **A đúng** khi xác định Entanglement = BIAN-10 (reverse gap). B xác nhận: "no classical analogue" (#47).

### Sai / Thiếu sót (False / Missing)
1. **A thiếu** toàn bộ generalized measurement theory (POVM, Kraus, weak measurement, weak values). B có 10 concepts chi tiết. Đây là thiếu sót nghiêm trọng vì generalized measurement mở rộng epistemic scope.
2. **A thiếu** continuous measurement và quantum trajectories. B có 9 concepts. Quantum trajectory ↔ santāna (BIAN-19) là mapping tiềm năng bị bỏ lỡ.
3. **A thiếu** null measurement (#33) cross-reference với BIAN-9 (abhāva). Đây là lỗi rõ ràng nhất.
4. **A thiếu** measurement reversal (#102) — có thể liên quan trực tiếp đến BIAN-12 (bādhaka pramāṇa).

### Tốt (Good)
- **A tốt** ở chiều sâu triết học, BIAN gap analysis, axiom distribution, node/edge formalism.
- **B tốt** ở phạm vi phủ QM, độ chính xác vật lý, source tracking, RCA verification.

### Xấu (Bad)
- **A xấu** ở phạm vi phủ QM (chỉ 32/105 concepts). Projection bias: A chỉ mapping phần QM phù hợp với BE, bỏ qua phần lớn QM formalism.
- **B xấu** ở chiều triết học (= 0). Không có epistemic analysis.

### Khuyến nghị
> **Tài liệu A cần bổ sung:** Generalized measurement (POVM/Kraus ↔ expanded Pramāṇa), Weak measurement (↔ near-nirvikalpaka), Null measurement (↔ Abhāva), Quantum trajectory (↔ Santāna/Anātmavāda), Measurement reversal (↔ Bādhaka pramāṇa). Điều này sẽ nâng coverage từ ~30% lên ~50% và khắc phục projection bias.

---
*Created: 2026-05-10 | Comparison of system_axioms_mapping.md vs QM_Measurement_Unified_Concept_Table.md*
