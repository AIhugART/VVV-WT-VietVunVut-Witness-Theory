Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# VVV-QMRF-EX Compass Index

**Role:** Compass only — intelligence about K-rho relationships, structural stress points, and prioritization. NOT a structure import.

**Rule (CLAUDE.md):** `Internal-first, VVV-QMRF-EX-verified, selectively imported.`

---

## 1. EX Status Summary

| Metric | Value |
|--------|-------|
| Version | v1.7 COMPLETE (commit d8ec025, c1b3168, 8d07bdd) |
| Raw coverage (v1.6) | 92.3% |
| Raw coverage (v1.7) | 86.5% |
| KE-SC stress score | 3.5 -> 4.0 (v1.7 bump) |
| Tier 1+2 gates | PASS |

## 2. Key Stress Points (for VVV-QMRF Core Prioritization)

| Stress Point | EX Node | KE-SC | Relevance to Core |
|-------------|---------|-------|-------------------|
| K5 multi-observer cross-context firing | EX_NODE_K5_CTX | 4.0 | Directly relevant — K5 firing is the mechanism for distinguishability |
| V_prov/V_final lifecycle | EX_NODE_V_LIFECYCLE | 3.8 | F1/F7b cascade — validity split is load-bearing |
| K9 bridge parameter sensitivity | EX_NODE_K9_BETA | 3.7 | beta=0 best-fit — stress matches empirical result |
| T4 N-observer colimit | EX_NODE_T4_COLIMIT | 3.5 | P11a-G0 gate — needed for 3-observer prediction |
| FR assumption chain C | EX_NODE_FR_CHAIN | 3.5 | K5 V_prov breaks chain — EX confirms this is the right mechanism |

## 3. EX Structural Boundaries

- EX edges are **not imported** into VVV-QMRF core
- EX node IDs may be cited in `EX-MARGIN` notes for prioritization context
- EX KE-SC scores are compass bearings, not axioms
- VVV-QMRF core derives from K1–K8 only; EX provides external validation

## 4. EX Folder Map

| Path | Content |
|------|---------|
| `source_snapshot/framework/` | E1–E17 postulate formalizations |
| `source_snapshot/category/` | Registration category analyses (15 categories) |
| `source_snapshot/system_be/` | Buddhist Epistemology SOT (system_be_full.md) |
| `source_snapshot/system_qm/` | Quantum Mechanics SOT |
| `source_snapshot/vvv_qmrf_core/` | VVV-QMRF core snapshot (schema_guide, bridge, edge, node) |
| `source_snapshot/be_263_audit/` | BE 263-node audit cycle |
| `reviews/` | RCA inventory, phase audits, impact isolation |
| `archives/` | Phase 7 logs, README |

---

*VVV-QMRF-EX Compass Index — 2026-05-23. EX v1.7. Compass role: intelligence only, no structure import.*
