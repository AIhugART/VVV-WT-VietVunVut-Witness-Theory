Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Zenodo Upload Checklist — Working Paper v3.0

**Record:** https://zenodo.org/doi/10.5281/zenodo.20289260 (concept DOI → all versions)
**Action:** Create "New version" (v3.0) in the existing record
**Date:** 2026-05-28

---

## Files in this folder

| File | Purpose |
|---|---|
| `VVV-QMRF_Working_Paper_v3.0.pdf` | **Primary upload** — PDF generated 2026-05-28 (447 KB, pdflatex) |
| `VVV-QMRF_Working_Paper_v3.0.md` | Markdown source (alternative upload if PDF rejected) |
| `latex_header.tex` | pdflatex Unicode header used for PDF generation (not uploaded) |
| `zenodo_metadata.json` | Copy-paste source for all metadata fields |
| `UPLOAD_CHECKLIST.md` | This file |

---

## Step-by-step Upload

### Step 1 — Open existing record
- Go to: https://zenodo.org/doi/10.5281/zenodo.20289260
- Click **"New version"** button (top right of record)

### Step 2 — Upload file
- Delete any old files if prompted
- Upload: **`VVV-QMRF_Working_Paper_v3.0.pdf`** (preferred — renders inline on Zenodo)
- Alternative: `VVV-QMRF_Working_Paper_v3.0.md` if PDF upload fails

### Step 3 — Fill metadata (copy from `zenodo_metadata.json`)

| Field | Value |
|---|---|
| **Title** | When Does a Physical Interaction Become a Valid Registered Measurement? A VVV-QMRF Registration-Layer Framework with the K9_E Class C Testable Hypothesis and an Experimental Specification for Extended Wigner's Friend |
| **Upload type** | Publication → Working paper |
| **Publication date** | 2026-05-28 |
| **Version** | 3.0 |
| **Author name** | Nguyen Xuan, Viet |
| **Author affiliation** | Independent Researcher, Vietnam |
| **License** | Creative Commons Attribution 4.0 International (CC BY 4.0) |
| **Language** | English |

### Step 4 — Description
Copy the `"description"` field from `zenodo_metadata.json` (the long paragraph text).

### Step 5 — Keywords (add one by one)
```
quantum measurement
quantum foundations
Extended Wigner's Friend
K9_E probability postulate
registration framework
Buddhist epistemology
Pramana
K-side incommensurability
Born rule extension
K-space axiomatization
Frauchiger-Renner paradox
Modified Bong Protocol
waveplate EWF experiment
```

### Step 6 — Related identifiers
Add these in the "Related/alternate identifiers" section:

| Identifier | Relation | Scheme |
|---|---|---|
| `10.5281/zenodo.20356782` | Is new version of | DOI |
| `10.5281/zenodo.20289261` | Is new version of | DOI |

### Step 7 — Notes
Copy the `"notes"` field from `zenodo_metadata.json`.

### Step 8 — Publish
- Click **"Save draft"** first → verify all fields
- Click **"Publish"**
- Note the new **version DOI** (format: `10.5281/zenodo.XXXXXXXX`)

---

## After publishing — update project files

Once Zenodo assigns the v3.0 version DOI, update these files:

| File | Change needed |
|---|---|
| `papers/paper_003/VVV-QMRF_Working_Paper_v3.0.md` | Ref [15]: add v3.0 DOI |
| `papers/paper_003/VVV-QMRF_Working_Paper_v3.0_draft.md` | Same as above |
| `documents/research_documents/project_vvv_qmrf_class_c/index.md` | Add v3.0 DOI to Zenodo section |
| `CLAUDE.md` | Update Zenodo DOI note with concept DOI + v3.0 DOI |
| `memory/project_zenodo_dois.md` | Update memory file |

---

## DOI Reference Summary

| DOI | Type | Points to |
|---|---|---|
| `10.5281/zenodo.20289260` | **Concept DOI** | Always → latest version |
| `10.5281/zenodo.20289261` | Version DOI | v2.0 (May 19, 2026) |
| `10.5281/zenodo.20356782` | Version DOI | v2 (May 23, 2026) |
| `10.5281/zenodo.20431310` | Version DOI | **v3.0** (published 2026-05-28) |

---

*Checklist v1.0 — 2026-05-28*
