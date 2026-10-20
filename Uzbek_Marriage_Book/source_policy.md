# Source-verification policy

1. **No fabrication.** No statistic, study, verse, hadith, grade, scholar's view, bibliographic detail or URL enters the manuscript unless it is in `source_ledger.md` with a verification status.
2. **Statuses:**
   - `VERIFIED-PRIMARY` — checked against the primary text (Qurʼan Arabic text; hadith Arabic + collection number + grade in the sunnah.com dataset).
   - `VERIFIED-SECONDARY` — bibliographic details and main finding confirmed through at least one reliable index or abstract (publisher page, PubMed/PMC, university repository, author lab page), full text not read.
   - `QUALIFIED` — used only with explicit hedging in text (e.g., practitioner guideline, contested interpretation).
   - `NEEDS-HUMAN-REVIEW` — retained but flagged for a qualified scholar/clinician.
   - `REMOVED` — considered and excluded (kept in ledger for transparency).
3. **Hadith rules.** Cite collection + number in the numbering of the sunnah.com dataset (Fuʼad ʻAbd al-Baqi for Bukhari, Muslim, Ibn Majah; Muhyi al-Din ʻAbd al-Hamid for Abu Dawud; Abu Ghudda for Nasaʼi). State the grade for anything outside Bukhari/Muslim, naming the grader (Albaniy / Dorussalom nashri). Weak (daʼif) reports are not used as evidence; if mentioned, it is to correct a popular misconception, labelled as weak.
4. **Qurʼan translations** are the author's meaning renderings; checked against Saheeh International (EN) and E. Kuliev (RU). Bracketed explanatory words are marked with brackets.
5. **Psychology rules.** Correlational findings are described as associations. No "% accuracy" divorce-prediction claims. Effect sizes only when verified. Practice recommendations (e.g., 20-minute break) are labelled as clinical guidance, not proven thresholds.
6. **Law and hotlines** are restricted to items verified in at least one official or institutional source and are dated ("2026-yil oktyabr holatiga").
7. After every substantive edit, the reference check (`tools/check_refs.py`) is re-run.
