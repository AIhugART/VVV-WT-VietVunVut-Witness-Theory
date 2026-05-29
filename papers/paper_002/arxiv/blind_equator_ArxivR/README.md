# arXiv Submission Package: blind_equator_ArxivR

**Paper:** Have Optical Wigner's Friend Experiments Been Blind to a Geometric Degree of Freedom?
**Author:** VietVunVut (Viet - Nguyen Xuan)
**Email:** viet@vvvqmrf.com | **Web:** https://vvvqmrf.com
**Date:** 2026-05-26
**Target:** arXiv quant-ph → Phys. Rev. A

## File Inventory

### Main Paper
| File | Description |
|------|-------------|
| `main.tex` | LaTeX source (revtex4-2, v91) — 9 sections + 18 references |
| `main.bib` | BibTeX bibliography (18 entries) — alternative to inline thebibliography |
| `main.pdf` | Compiled PDF — 9 pages (pre-verified compilation) |

### Figures (5)
| File | Figure | Content |
|------|--------|---------|
| `fig1_bloch_equatorial_vs_tilted.png` | Fig 1 | Bloch sphere: equatorial vs tilted geometry |
| `fig2_fom_vs_theta.png` | Fig 2 | Figure of merit vs polar angle θ |
| `fig3_optical_path.png` | Fig 3 | Optical path with QWP insertion |
| `fig4_monte_carlo.png` | Fig 4 | Monte Carlo histogram of Gen LF 1 |
| `fig5_fom_vs_mu.png` | Fig 5 | FOM vs visibility μ |

### Supplemental Material
| File | Description |
|------|-------------|
| `supplemental.tex` | LaTeX source — S1 (proof + literature search), S2 (numerical methods + robustness), S3 (interpretations + GPT context) |
| `supplemental.pdf` | Compiled supplemental PDF — 5 pages |

## arXiv Upload Instructions

1. Go to https://arxiv.org/submit
2. Upload `main.tex` as the main LaTeX file
3. Upload all 5 `.png` figure files
4. Upload `supplemental.tex` as ancillary file (or compile + upload `supplemental.pdf` separately)
5. Select category: `quant-ph` (Quantum Physics)
6. The `main.tex` uses `\begin{thebibliography}` (inline) — no BibTeX run needed

## Compilation Notes

- **LaTeX engine:** pdfLaTeX
- **Document class:** revtex4-2 (requires REVTeX 4.2 package from APS)
- **Compilation command:** `pdflatex main.tex` × 2 (to resolve cross-references)
- **Figure format:** PNG (pdflatex supports PNG; convert to PDF for smaller file size if needed)
- **Supplemental:** Standalone compilation with `pdflatex supplemental.tex`

## Pre-Compilation Checklist

- [x] main.tex compiles cleanly (9 pages, 0 undefined references)
- [x] supplemental.tex compiles cleanly (5 pages)
- [x] All 18 references match manuscript.md v91
- [x] Title matches frozen v77 wording
- [x] All 9 sections present
- [x] Proposition 1 + Lemma 1 present
- [x] All tables converted from markdown to LaTeX
- [x] Survey audit table (S3.5) with footnote [a] present
- [x] 5 figures included

## Known Caveats

- **fig1 and fig2** are placeholder PNGs (content from old EWF schematic and 2D heatmap respectively). The .md figure descriptions call for: (1) Bloch sphere visualization with equatorial vs tilted panels, and (2) FOM vs θ curve. Replace these two PNGs with proper artwork for final submission.
- **fig3, fig4, fig5** match the manuscript.md figure descriptions (optical path, Monte Carlo, FOM vs μ).
- The `supplemental.tex` compiles independently with `\documentclass{article}`. For arXiv, upload as ancillary/supplementary material.
