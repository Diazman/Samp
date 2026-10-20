# Progress tracker

**Current stage:** 9 — final quality gate complete
**Last updated:** 2026-10-20

## Completed

- **Stage 1 (Plan):** `project_plan.md`, `style_guide.md`, `source_policy.md`.
- **Stage 2 (Research):**
  - offline Qurʼan and hadith datasets;
  - `tools/islamic_lookup.py`;
  - `source_ledger.md`, covering:
    - Qurʼan Q01–Q61;
    - hadith H01–H95;
    - psychology P01–P43;
    - law L01–L05.
- **Stage 3 (Writing):**
  - preface;
  - 18 chapters in six parts;
  - conclusion;
  - appendices A–E;
  - colophon.
- **Stage 4 (Islamic audit):** `islamic_audit.md`. Final build: 64 Qurʼan refs and 79 hadith refs, 0 failures.
- **Stage 5 (Psychology audit):** `psychology_audit.md`.
- **Stage 6 (Editing):** passes A–G in `editorial_report.md`; full proofread of every source file.
- **Stage 7 (Workbook):** Appendix A → `workbook_uz.md`. It includes:
  - 40 questions;
  - exercises for listening, repair, gratitude, emotions and boundaries;
  - the money and household guide with tables;
  - the weekly council template;
  - the disagreement checklist;
  - the 30-day plan;
  - the maintenance checklist;
  - extras.
- **Stage 8 (Publishing):** all outputs built.
  - EPUBCheck: 0 errors, 0 warnings.
  - DOCX checked by zip test, python-docx read, and LibreOffice conversion to PDF (272 pages, visual check).
  - EPUB render checked in Chromium.
  - `README.md` written.
- **Stage 9 (Final gate):**
  - lint: 0 errors;
  - `check_refs`: 0 failures;
  - word count: 45,510 by `wc` / about 42,900 Latin-script words.

## Unresolved issues (need human experts)

See `editorial_report.md` §4, `islamic_audit.md` §6 and `psychology_audit.md` §5–6. In summary:

- The 4:34 tafsir reports were verified only through secondary sources.
- The Hanafi positions on housing and housework need checking against primary fiqh texts.
- The Uzbek verse translations should be compared with an established translation.
- Muslim 1468 b / 1469 numbering differs between editions.
- Some volume and page numbers in the bibliography were not independently confirmed.
- The ambulance number 103 was not re-verified online.
- A native Uzbek copy edit is still needed.

## Files

- **Deliverables:** `manuscript_uz.md`, `manuscript_uz.docx`, `manuscript_uz.epub`, `workbook_uz.md`, `references_uz.md`, `source_ledger.md`, `islamic_audit.md`, `psychology_audit.md`, `editorial_report.md`, `README.md`.
- **Sources:** `chapters/*.md`, `assets/`, `tools/`, `research/`.

## Exact next action

None required from the author. Next step is human expert review (scholar, psychologist, Uzbek editor), then commit/push if the user requests it.
