Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# VVV-QMRF Testable Prediction Campaign — Public Evidence Ledger

**Framework:** VietVunVut Quantum Measurement Registration Framework (VVV-QMRF)  
**Campaign:** Testable Prediction Section  
**Document type:** Public evidence ledger / public disclosure and critique log  
**Date:** 2026-05-17  
**Status:** Internal control file for future public releases  

> **DISCLAIMER:** VVV-QMRF is independent Class D personal research, not Standard Quantum Mechanics, not peer-reviewed or experimentally validated, and not for real-world technical use. Full boundary protocol: `DISCLAIMER.md`.

---

## 1. Purpose

This ledger records public-facing evidence for external versions of the Testable Prediction Campaign papers.

Public evidence means timestamped disclosure, submission record, public critique, public response, and version history. It does not mean peer review unless the venue is a peer-reviewed venue and acceptance is documented. It does not mean experimental validation unless independent empirical evidence is supplied.

---

## 2. Public Evidence Entry Schema

Use this schema after the user explicitly approves a public submission, post, or release:

```yaml
public_evidence_id: "PUB-TP-000"
external_paper_id: "EXT-TP-00"
internal_source_id: "INT-TP-00"
public_title: "title used publicly"
public_version: "v0.1 | v1.0 | etc."
date_posted_or_submitted: "YYYY-MM-DD"
venue_type: "scientific_journal | preprint_archive | public_forum | reddit | github_public | other"
venue_name: "name of venue"
venue_url_or_reference: "URL or citation record, added only after user-approved posting"
public_evidence_type: "timestamp | submission_record | public_post | critique_thread | reviewer_feedback | response_note"
claim_ids:
  - "C-TP-00-000"
status_disclaimer_present: true
claim_status_public: "theoretical proposal | conjecture | testability target | comparison | revised"
validation_status: "not_peer_reviewed | peer_review_pending | peer_reviewed | not_experimentally_validated | experimentally_checked"
critique_summary: "short summary after public feedback exists"
response_file: "relative/path/to/response.md or pending"
boundary: "what this public evidence does not establish"
```

---

## 3. Approved Public Wording Rules

Every external release must include a status block equivalent to:

```text
Status and Scope:
This paper is part of the VVV-QMRF Testable Prediction Campaign. VVV-QMRF is an independent registration-layer research framework. It is not Standard Quantum Mechanics, not peer-reviewed, not experimentally validated, and not a replacement for the Born rule, unitary evolution, density-matrix dynamics, or physical collapse models. The paper presents a bounded theoretical proposal and invites critique.
```

When posting to informal public venues, add:

```text
This is shared for conceptual and technical critique, not as established physics.
```

---

## 4. Public Evidence Status Levels

| Status | Meaning | Allowed wording |
|---|---|---|
| `draft_not_public` | External draft exists but has not been released. | Internal only. |
| `public_disclosed` | A version was publicly posted or shared. | Publicly disclosed proposal. |
| `public_critiqued` | Public comments or critique exist. | Public critique received. |
| `revised_after_critique` | A later version responds to critique. | Revised after public feedback. |
| `submitted` | Submitted to a venue. | Submitted, not accepted. |
| `accepted_or_published` | Venue acceptance or publication exists. | Published/accepted, with venue details. |
| `peer_reviewed` | Peer review completed and documented. | Peer-reviewed only if documented. |
| `experimentally_checked` | Independent empirical check exists. | Experimentally checked only with documented evidence. |

---

## 5. Planned Public Evidence Slots

| Public Evidence ID | External Paper | Intended public route | Current status |
|---|---|---|---|
| PUB-TP-001 | EXT-TP-01 Valid Registered Measurement | Public research note / critique post | draft_not_public |
| PUB-TP-002 | EXT-TP-02 Control Cases | Public research note / critique post | draft_not_public |
| PUB-TP-003 | EXT-TP-03 K-side Registration Space | Technical critique post | draft_not_public |
| PUB-TP-004 | EXT-TP-04 EWF Incommensurability | Scientific outlet / public critique | draft_not_public |
| PUB-TP-005 | EXT-TP-05 Disconfirmation Target | Scientific outlet / public critique | draft_not_public |
| PUB-TP-006 | EXT-TP-06 Interpretation Positioning | Public explainer / discussion | draft_not_public |

---

## 6. Public Release Non-Claims

Public evidence does not establish:

```text
peer review
experimental validation
acceptance by the physics community
replacement of Standard Quantum Mechanics
proof of a physical collapse mechanism
proof that Buddhist Epistemology is physics
```

Public evidence may establish:

```text
timestamped disclosure
public availability
public critique received
response history
version history
claim refinement over time
```

---

## 7. Posting and Submission Rule

No external posting, submission, upload, or comment should be performed from this project without explicit user approval for that specific action and venue.
