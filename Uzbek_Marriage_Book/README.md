# Bir umrlik nikoh

*Mehr-muhabbat, rahm-shafqat va baxtli oila qurish sanʼati*

This is an original nonfiction book in Uzbek (Latin script) about building a happy, lifelong marriage. It draws on three things:

- authentic Islamic sources: Qurʼan with sura and verse, hadith with collection, number and grade;
- evidence-informed psychology;
- moral and practical reasoning.

The book was prepared with an AI (Claude), and the colophon says so. It should be reviewed by a qualified Islamic scholar, a family psychologist and an Uzbek copy editor before printing; see `editorial_report.md` §4.

## Deliverables

| File | Contents |
|---|---|
| `manuscript_uz.md` | Complete manuscript (generated; do not edit — edit `chapters/` instead) |
| `manuscript_uz.docx` | Word edition: A5, table of contents, right-to-left "Arabic Quote" style |
| `manuscript_uz.epub` | EPUB 3 edition with embedded Amiri Quran font; passes EPUBCheck |
| `workbook_uz.md` | Appendix A (couples' workbook) as a standalone file |
| `references_uz.md` | Appendix E (references) as a standalone file |
| `source_ledger.md` | Every Qurʼan, hadith, psychology and law item, with its verification status |
| `islamic_audit.md` | Islamic source audit: method, counts, corrections, items for human review |
| `psychology_audit.md` | Psychology fact-check: claim strength, corrections, harm checks |
| `editorial_report.md` | Editing passes A–G, validation results, remaining issues |
| `progress.md` | Stage tracker |
| `project_plan.md`, `style_guide.md`, `source_policy.md` | Planning documents |

## Source layout

- `chapters/` holds the source of truth, one Markdown file per unit, assembled in filename order:
  - `00_front.md`: preface;
  - `01`–`18`: the chapters;
  - `19_xulosa.md`: conclusion;
  - `89`–`95`: appendices and colophon.
- Arabic text is never typed by hand. Chapters contain tokens that the build replaces with Arabic from `research/arabic_cache.json`:
  - `{{AYAH:30:21}}` for a verse;
  - `{{AYAH:2:187@8-13}}` for a word range within a verse;
  - `{{HADITH:<sunnah.com urn>}}` for a hadith.
- `assets/` holds the metadata, EPUB CSS, and the Amiri Quran font (SIL OFL 1.1; licence in `assets/fonts/`).
- `tools/` holds the build and check scripts. Each script's header docstring explains its use.

## Requirements

- Python 3.10 or later, with `python-docx` and `epubcheck` (the PyPI package bundles the EPUBCheck jar and needs Java).
- pandoc 3.x (built with 3.1.3).
- Optional: LibreOffice, for a DOCX → PDF check.

## Reference datasets

The datasets are needed only to regenerate the Arabic cache and to re-check references. They are not stored in the repository.

```sh
D=/path/to/data && mkdir -p $D && cd $D
npm pack quran-json@3.1.2 hadith@1.3.0
mkdir -p q h && tar -xzf quran-json-3.1.2.tgz -C q && tar -xzf hadith-1.3.0.tgz -C h
```

This produces:

- `$D/q/package/dist/quran.json` and `quran_en.json`: Uthmani text from QuranEnc, plus Saheeh International and other translations;
- `$D/h/package/data/hadith.db`: SQLite database of sunnah.com data.

The Amiri Quran font in `assets/fonts/` came from the npm package `@fontsource/amiri-quran` (5.3.0).

## Build and check

Run these from this directory:

```sh
python3 -I tools/make_arabic_cache.py --data $D   # only after adding/changing AYAH/HADITH tokens
python3 tools/build.py                            # manuscript_uz.md/.docx/.epub, workbook_uz.md, references_uz.md
python3 -I tools/check_refs.py --data $D          # resolves every Qurʼan/hadith citation → research/refs_report.md
python3 tools/lint.py                             # orthography, stray Cyrillic, leftover tokens, repetition, word counts
python3 -m epubcheck manuscript_uz.epub           # EPUB validation
```

To skip slow outputs, run `python3 tools/build.py --no-docx --no-epub`.

`tools/islamic_lookup.py --data $D quran 4:130` (subcommands `quran`, `hadith`, `search`, `arsearch`) looks up a verse or hadith while editing.

## Editing conventions

- Apostrophes: write Uzbek with ʻ (U+02BB, as in oʻ, gʻ) and ʼ (U+02BC). The build's normaliser converts `o'`, `g'` and apostrophes between letters automatically.
- Headings:
  - `#` for parts;
  - `##` for chapters ("N-bob. …");
  - `###` for sections;
  - add `{.unnumbered}` to headings outside the numbering.
- Labelled boxes are blockquotes that start with `> **Diniy manba.**`, `> **Ilmiy maʼlumot.**` or `> **Diqqat.**`.
- Every new religious or empirical claim must first be added to `source_ledger.md` and verified; see `source_policy.md`.
