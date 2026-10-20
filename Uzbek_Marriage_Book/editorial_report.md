# Editorial report — *Bir umrlik nikoh*

Date: 2026-10-20. Editor: the authoring AI (Claude). This report covers editing stage 6, passes A–G. The specialist audits are in `islamic_audit.md` and `psychology_audit.md`.

## 1. Final shape of the book

| Part | Contents |
|---|---|
| Front matter | Preface (Soʻzboshi): audience, the three foundations, the box legend, what the book cannot do, an emergency notice, a reading guide, and a note on Arabic text and translations |
| I. Poydevor | Chapters 1–3: what a happy marriage is; choosing a spouse; preparing for marriage |
| II. Muhabbat va muloqot | Chapters 4–7: everyday love; understanding each other; communication; conflict and repair |
| III. Huquq, ishonch va yaqinlik | Chapters 8–10: rights and duties; trust and boundaries; intimacy |
| IV. Kundalik hayot | Chapters 11–13: money; parents and in-laws; housework, parenting and the invisible load |
| V. Sinovlar | Chapters 14–16: forgiveness; life trials; warning signs and abuse |
| VI. Yillar osha | Chapters 17–18: friendship and spirituality over the years; habits that keep a marriage going |
| Conclusion | Key lessons, notes for different readers, and a closing duʼa |
| Appendices | A workbook; B help resources; C glossary; D course guide for group leaders; E references; colophon |

All 20 topics in the brief are covered (topic → chapter map in `project_plan.md`).

**Word count (final build):**

- `manuscript_uz.md`: 45,510 words by `wc -w`, including Arabic text, table syntax and markup.
- Latin-script prose: about 42,900 words, counted by `tools/lint.py`.
- The workbook (Appendix A) accounts for about 2,440 of those Latin-script words.

The brief asked for about 45k–60k words. The book reaches 45k only on the `wc` count; on a prose-only count it is about 2k short. It sits at the bottom of the range.

## 2. Passes performed

**A. Structural.**

- Heading hierarchy fixed: H1 for parts, H2 for chapters, H3 for sections.
- Every chapter follows the same pattern:
  - an opening story;
  - religious, scientific and warning boxes;
  - a "Birgalikda bajaring" exercise;
  - reflection questions;
  - a chapter summary.
- Appendix files renumbered so they sort correctly (91 B … 95 colophon).
- Chapter cross-references (e.g., "(7-bob)") were spot-checked while proofreading.

**B. Developmental.** Substantive sections were added where chapters were thin:

- chapters 1–4, 6, 7, 9–17 and appendix D during drafting;
- in the final pass, ch 18 ("Raqamli davrda nikohni asrash odatlari") and the conclusion ("Turli oʻquvchilarga bir necha soʻz").

The Islamic, empirical and practical layers are kept visibly separate with labelled boxes.

**C. Repetition.**

- `tools/lint.py` reports no repeated sentences.
- A repeated hadith qudsi in ch 16 was replaced with a cross-reference to ch 8.
- Some key texts recur on purpose as the book's framing texts (Rum 30:21 in ch 1 and the conclusion; Tirmidhi 3895 in ch 1, ch 8 and the conclusion).

**D. Cultural and religious sensitivity.**

- Husbands and wives receive matching duties and examples. The duties chapter (8) reads each obligation "toward oneself first".
- The book separates religious obligation from local custom. It includes:
  - a "din va odat" exercise;
  - a section on the bride's service in the in-laws' home, presented as custom and kindness, not as a ruling;
  - in-law content written with respect for parents.
- No exercise is recommended for couples where there is fear or abuse. The workbook opens with a safety warning.
- Patience is never presented as consent to oppression.

**E. Language.**

Applied across all source files:

- Uzbek Latin orthography: ʻ (U+02BB) and ʼ (U+02BC), applied by `tools/normalize.py`.
- «» quotation marks and em-dash dialogue.
- Honorific plurals for the Prophet ﷺ and the Mothers of the Believers (e.g., "dedilar").
- Consistent sen/siz register: "siz" when addressing the reader, "sen" inside spouse dialogue.
- Grammar fixes (e.g., "xatoim" → "xatom").
- No Cyrillic characters, emoji, or ASCII apostrophes inside words (checked by lint).

**F. Fact re-check.**

- Every Qurʼan and hadith citation was re-resolved by `tools/check_refs.py`: 64 distinct Qurʼan references and 79 distinct hadith references, with 0 failures.
- One new citation (Niso 4:130, in the conclusion) was verified against the dataset and added to the ledger as Q61.
- Psychology claims were re-checked against `psychology_audit.md`; the new sections add no empirical claims.
- Help numbers carry a date ("2026-yil holatiga koʻra").

**G. Proofread.** All of these files were read in full and corrected:

- chapters 00–19;
- appendices A–E;
- the colophon.

Corrections included:

- workbook question 4 rewritten for clarity;
- the "Uch yaxshilik" exercise renamed "Kunning yaxshiligi" so the title matches the task;
- the apology steps in the workbook aligned with the six steps in ch 7;
- the colophon font note limited to the EPUB edition.

## 3. Validation (final build, 2026-10-20)

| Check | Result |
|---|---|
| `tools/check_refs.py` | 64 Qurʼan refs, 79 hadith refs, 0 failures |
| `tools/lint.py` | 0 errors. 10 warnings, all for "very long sentence"; every one is a false positive where a table or Arabic block was counted as one sentence |
| EPUBCheck (jar bundled with Python `epubcheck`) | 0 fatals, 0 errors, 0 warnings, 0 infos |
| EPUB render (Chromium via Playwright) | Amiri Quran font applied to `.arabic` blocks; `dir=rtl`; ʻ/ʼ/«» render correctly (screenshot checked) |
| DOCX: zip integrity | `testzip` OK |
| DOCX: python-docx read | 2,142 paragraphs; 16 tables; 19 "Arabic Quote" paragraphs; A5 page (148×210 mm); 0 ASCII apostrophes inside words |
| DOCX → PDF (LibreOffice headless) | 272 pages. Rendered pages checked visually: Uzbek characters correct, Arabic right-to-left |

Pandoc prints a warning that it has no uz-Latn translation file. The result is harmless: the generated table of contents is titled "Mundarija" through the metadata.

## 4. Remaining issues (need human experts)

- **Islamic scholarly review.** Seven items, listed in `islamic_audit.md` §6. The main ones:
  - the 4:34 section;
  - the Hanafi positions on housing and housework;
  - the Uzbek meaning translations of the verses.
- **Psychologist review.** Four items, listed in `psychology_audit.md` §6.
- **Bibliographic details.** Some volume and page numbers were not independently confirmed (`psychology_audit.md` §5).
- **Help numbers.** The ambulance number (103) was not re-verified online. All numbers should be checked before printing.
- **Language editing.** A native Uzbek copy editor should do a final read. The text was written and proofread by an AI.
- **Sentence length.** Some long sentences in chapters 7, 8 and 11 sit next to tables and boxes; a human editor may want to split them.
