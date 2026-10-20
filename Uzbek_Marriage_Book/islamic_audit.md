# Islamic source verification report

Project: *Bir umrlik nikoh* (Uzbek manuscript). Audit date: 2026-10-20. Auditor: the authoring AI (Claude). This is **not** a substitute for review by a qualified Islamic scholar; items needing that review are listed in §6.

## 1. Method

1. **Extraction.** `tools/check_refs.py` scans every chapter file for Qurʼan citations (sura name + verse) and hadith citations (Buxoriy, Muslim, Abu Dovud, Termiziy, Nasoiy, Ibn Moja + number). Citations it cannot parse (al-Adab al-Mufrad, Shamoil, Abu Dovud 2178 in prose form, Ahzob 33:35 and Oli Imron 3:102 in prose form) were extracted manually with `grep`.
2. **Primary-text check.**
   - Qurʼan: every reference resolved against the Uthmani text (QuranEnc, via npm `quran-json` 3.1.2). The Arabic printed in the book is inserted automatically from this dataset by the build (`{{AYAH:…}}` tokens → `research/arabic_cache.json`), so no Arabic was typed by hand.
   - Hadith: every reference resolved against the sunnah.com database (npm `hadith` 1.3.0): Arabic text, English translation, numbering and the grade carried by the dataset. Arabic hadith matn in the book is likewise inserted automatically by URN.
3. **Translation review.** For each Qurʼan citation the Uzbek meaning translation in the book was read side by side with Saheeh International (EN) and checked against E. Kuliev (RU) where wording was in doubt (report: `research/refs_report.md`). For each hadith the Uzbek rendering was compared with the dataset's English translation.
4. **Grading check.** Every grade statement in the text ("Albaniy sahih degan", "Dorussalom nashrida hasan", etc.) was compared with the dataset grade. Bukhari and Muslim narrations are cited without a grade note.
5. **Context check.** Each verse/hadith was checked for whether its use in the book fits its context (e.g., divorce-context verses used for general principles).
6. **Rulings check.** Every statement of a religious ruling or scholarly position was listed and classified (clear text / scholarly interpretation / disputed / custom).

## 2. Results — counts

| Item | Count | Resolved | Failed |
|---|---|---|---|
| Distinct Qurʼan citations (auto-parsed by `tools/check_refs.py`, final build) | 64 | 64 | 0 |
| Distinct hadith citations (auto-parsed, final build) | 79 | 79 | 0 |
| Hadith citations checked manually | 4 (Adab 594, Shamoil 341, Abu Dovud 2178, Buxoriy 5361) | 4 | 0 |
| Grade statements in text | 22 | 22 consistent with dataset | 0 |
| Arabic blocks in book | 12 Qurʼan + 7 hadith (19 blocks) | all from dataset | — |

## 3. Corrections made during the audit

| # | Location | Problem | Action |
|---|---|---|---|
| 1 | Ch 8 (Abu Dovud 2146) | Narration summarised without the intermediate step (ʻUmar's complaint and the temporary permission) — selective quotation | Full sequence now given |
| 2 | Ch 1, Ch 19 (Termiziy 3895) | Uzbek rendering ungrammatical ("eng yaxshi boʻlganingizman"); Arabic block contained a final clause not translated | Re-translated; final clause ("when your companion dies, leave him") now translated |
| 3 | Ch 9 (Baqara 2:187) | Full long verse printed in Arabic while only "they are garments for you…" was translated | Build now prints only the relevant words (fragment token `2:187@8-13`) |
| 4 | Ch 8, Ch 16 (Baqara 2:231) | Verse about retaining a divorced wife used as if addressed to marriage generally | Context stated explicitly; general principle drawn with wording "bu tamoyil umumiy" |
| 5 | Ch 8 (Taloq 65:6) | Verse about housing divorced women in ʻidda used for wife's housing right | Added note that scholars derive the wife's right *a fortiori* |
| 6 | Ch 7 (Niso 4:35) | "If they both desire reconciliation" — referent disputed (arbiters vs spouses) | Both readings indicated |
| 7 | Ch 7 (Hujurot 49:11) | "lā talmizū" rendered "ayblamanglar" (too weak) | → "haqoratlamanglar (ayblab kamsitmanglar)" |
| 8 | Ch 12 (Isro 17:23) | "lā tanharhumā" rendered "ozor berma" (too general) | → "jerkima" |
| 9 | Ch 1 | Unsupported attribution "some exegetes linked mawadda to youthful love" | Removed; replaced with neutral lexical note |
| 10 | Ch 2 | Popular hadith "if one whose religion and character please you proposes…" (Termiziy 1084) graded *daʼif* by Darussalam | Not used |
| 11 | Ch 7 | Popular hadith "make wudu when angry" (Abu Dovud 4784) graded *daʼif* by al-Albani | Not used as evidence; reader told it is weak |
| 12 | Ch 16 | Popular "most hated permissible act is divorce" (Abu Dovud 2178) graded *daʼif* by al-Albani | Mentioned only to state its weakness and that it cannot justify keeping someone in danger |
| 13 | Planning | "Lā ḍarar wa lā ḍirār" (Ibn Moja 2340) graded *daʼif* by Darussalam (others: hasan) | Not used; Qurʼanic evidence (2:231, 65:6) used instead |
| 14 | Planning | "Every son of Adam errs…" (Termiziy 2499) graded *daʼif* by Darussalam | Not used |
| 15 | Ch 17 (Abu Dovud 1308) | Explanation of "sprinkling water" presented as fact | Reworded as the author's opinion |

## 4. Numbering notes

- Muslim, "lā yafrak muʼminun muʼminatan…": the dataset labels it **1468 b**; many printed editions number it **1469**. The book cites "sunnah.com raqamlashida 1468 b; Riyozus-solihin, 275".
- Termiziy 3895 ("khayrukum khayrukum li-ahlihi"): the dataset's Arabic numbering shows 4269, its English reference "Vol. 1, Book 46, Hadith 3895"; 3895 is the widely used number and is cited.
- Buxoriy 2731–2732, 5143–5144, 5185–5186 are combined entries in the Fuʼad ʻAbd al-Baqi numbering.
- The book's front matter and Appendix E tell readers that numbering may differ by edition.

## 5. Classification of religious rulings and positions stated in the book

| Statement | Basis | Classification in text |
|---|---|---|
| Consent of the bride/groom is required | Buxoriy 5136, 5138 | Clear text |
| Mahr is the wife's property | Niso 4:4 | Clear text |
| Husband owes maintenance per means | Baqara 2:233; Taloq 65:7; Buxoriy 5364; Muslim 1218 | Clear text |
| Wife's earnings/property are her own | Niso 4:32; general fiqh | Clear text + scholarly consensus (stated generally) |
| Obedience only in maʼruf, never in sin | Buxoriy 7257; Muslim 1840 | Clear text |
| Qiwama = responsibility of care/provision | Niso 4:34 + "koʻp ulamolar" | Interpretation, attributed |
| 4:34 third step: restrictions (ghayr mubarrih; siwak report; al-Shafiʻi "leaving it is better"; no face; Prophet never struck) | Muslim 1218; Abu Dovud 2142, 2146; Muslim 2328; Tabari/Razi via secondary sources | Primary texts verified; classical attributions **secondary-source only** (flagged in text) |
| Contemporary scholars differ on 4:34's application; none permits injurious/humiliating violence | General statement | Interpretation; flagged for scholar review |
| Nushuz applies to both spouses | Niso 4:34, 4:128 | Clear text |
| Wife's right to separate lockable quarters (Hanafi) | al-Haskafi, Ibn ʻAbidin via fatwa sites | Scholarly position, attributed to Hanafi madhhab, flagged |
| Serving parents-in-law not obligatory per most scholars; virtue (ihsan) | Inferred from fatwa sources | Interpretation, flagged |
| Housework: Hanafi discussion (not judicially enforceable) | Mentioned only implicitly | Book avoids a definitive ruling; reader referred to local scholar |
| Wife may seek khulʼ | Baqara 2:229; Buxoriy 5273 | Clear text |
| Refusal of intimacy hadith does not permit force; recognised excuses | Buxoriy 3237/5193 + Baqara 2:231, Niso 4:19, Rum 30:21 + "ulamolar uzrlarni eʼtirof etgan" | Text + interpretation, flagged |
| Menstruation: abstain from intercourse | Baqara 2:222 | Clear text |
| Riba forbidden; modern finance complex | Baqara 2:275 | Clear text + referral to scholar |
| Repentance for wrongs against people requires seeking their forgiveness/restitution | General scholarly statement ("koʻp ulamolar") | Interpretation |
| Polygamy: conditions are complex fiqh; secret marriage destroys trust; criminal in Uzbek law | Law (Criminal Code art. 126) | Legal fact + ethical point; no fiqh ruling given |
| Assisted reproduction: fiqh conditions exist | — | Referral to scholar only |
| Preservation of life as a higher objective of Shariʻa | General maqasid principle | Interpretation, stated generally |

## 6. Unresolved items requiring human scholarly review

1. **Niso 4:34 section (ch 8).** The Ibn ʻAbbas/ʻAtaʼ report (al-Tabari) and al-Shafiʻi's statement (as quoted by al-Razi) were verified only through secondary sources; chains and exact wording should be checked in the tafsir texts. The overall framing should be reviewed by a qualified Hanafi scholar familiar with Uzbek context.
2. **Hanafi maskan position (ch 12)** — check *al-Durr al-Mukhtar* / *Radd al-Muhtar* directly.
3. **Daughter-in-law's service to in-laws (ch 8, 12)** — "most scholars do not consider it obligatory" is a summary; a scholar should confirm wording.
4. **Excuses for refusing intimacy (ch 10)** — summary of scholarly positions; confirm.
5. **Uzbek meaning translations of all Qurʼan verses** — author's own renderings; compare with an established Uzbek translation (e.g., Abdulaziz Mansur; Shayx Muhammad Sodiq Muhammad Yusuf) before print.
6. **Muslim 1468 b / 1469 numbering** — confirm against the print edition the publisher prefers.
7. **Ch 16 statement on contemporary scholarship** ("none permits injurious/humiliating violence") — reasonable summary but should be confirmed by a scholar.

## 7. Conclusion

All Qurʼan and hadith references in the manuscript resolve to the cited sources; all Arabic text is machine-inserted from the primary datasets; no hadith graded weak is used as evidence; grade statements match the dataset; translations were reviewed and nine corrections were made. Interpretive and fiqh statements are attributed and qualified, and the most sensitive ones are listed above for qualified human review.
