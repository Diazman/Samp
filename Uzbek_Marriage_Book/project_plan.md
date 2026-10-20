# Project plan — "Bir umrlik nikoh"

Internal working document (English for the production team; all reader-facing text is Uzbek).

## 1. Book identity

- **Title (final):** Bir umrlik nikoh
- **Subtitle:** Mehr-muhabbat, rahm-shafqat va baxtli oila qurish sanʼati
- **Why changed from the working title:** "mehr-muhabbat va rahm-shafqat" mirrors the Qurʼanic pair *mawadda wa rahma* (Rum 30:21), which is the book's organising verse; "muhabbat" alone loses the "mehr" (warm affection) shade.
- **Language:** Uzbek, Latin script (oʻ, gʻ with U+02BB; tutuq belgisi ʼ U+02BC). Arabic quotations in Arabic script.
- **Audience:** Uzbek-speaking Muslim adults — engaged couples, newlyweds, long-married couples, parents preparing children for marriage, imams and counsellors who want a balanced text.
- **Target length:** 45,000–55,000 Uzbek words (Uzbek is agglutinative, so this corresponds to roughly 65–75k English words of content).

## 2. Three foundations and how claims are kept apart

| Claim type | How it is marked in the text |
|---|---|
| Empirical psychology | "tadqiqotlar koʻrsatadiki…" + author/year in brackets, e.g. (Gottman va Levenson, 2000); strength qualifiers ("bogʻliqlik", "bashorat qiladi", not "sabab boʻladi" unless experimental) |
| Islamic primary texts | Arabic + Uzbek meaning translation + reference (sura:oyat; collection, number, grade) |
| Scholarly interpretation | Named scholar or madhhab, "ulamolarning bir qismi…", disagreements stated |
| Practical advice | Imperative / "tavsiya", no citation, framed as editorial guidance |

## 3. Structure and chapter map

| # | Uzbek title | Brief scope (from brief) |
|---|---|---|
| — | Soʻzboshi: Ushbu kitob kimlar uchun va qanday oʻqiladi | aims, limits, safety note |
| I qism | **Poydevor** | |
| 1 | Baxtli nikoh nima? | success ≠ longevity; sakinat, mawadda, rahma; satisfaction research (topic 1) |
| 2 | Turmush oʻrtogʻini oqilona tanlash | character, values, compatibility, attraction, consent, red flags (topic 2) |
| 3 | Nikohga tayyorgarlik | emotional, spiritual, practical, financial preparation; premarital education (topic 3) |
| II qism | **Muhabbat va tushunish** | |
| 4 | Mehr-muhabbat, rahm-shafqat va doʻstlik | love vs. mercy, friendship, attraction over time (topic 4) |
| 5 | Bir-birini tushunish: ehtiyojlar, fe'l-atvor va bogʻlanish | needs, personality, attachment, responsiveness; love-languages critique (topic 5) |
| 6 | Muloqot sanʼati | listening, I-statements, needs, difficult conversations (topic 6) |
| 7 | Nizo, gʻazab va yarashuv | four horsemen, flooding, repair, apology, compromise, arbitration (topic 7) |
| III qism | **Huquq, ishonch va yaqinlik** | |
| 8 | Islomda nikoh: huquqlar, burchlar, maslahat va adolat | rights/duties, qiwama in context, shura, culture vs. religion, 4:34 handled responsibly (topic 8) |
| 9 | Ishonch, vafo va chegaralar | fidelity, privacy, jealousy, phones, rebuilding trust (topic 9) |
| 10 | Yaqinlik: mehr, rozilik va hayo | intimacy ethics, consent, differing desire, privacy (topic 10) |
| IV qism | **Kundalik hayot** | |
| 11 | Pul, qarz va oila iqtisodi | nafaqa, wife's property, debt, budget, decisions (topic 11) |
| 12 | Ota-ona, qaynona-qaynota va qarindoshlar | birr al-walidayn + spouse rights, separate dwelling, boundaries (topic 12) |
| 13 | Uy yumushlari, farzand tarbiyasi va koʻrinmas yuk | housework, childcare, mental load, Prophet's example (topic 13) |
| V qism | **Sinovlar va oʻsish** | |
| 14 | Kechirim, ranjish va shaxsiy oʻsish | forgiveness research, resentment, expectations (topic 14) |
| 15 | Hayot sinovlari | children, infertility, illness, grief, unemployment, migration (topic 15) |
| 16 | Xavf belgilari: zoʻravonlik, nazorat, qaramlik va xiyonat | abuse, coercive control, addiction, betrayal, safety planning, khulʼ (topic 18) |
| VI qism | **Umrbod** | |
| 17 | Yillar osha: doʻstlik, hazil, romantika va maʼnaviy hamrohlik | friendship, novelty, humour, shared worship, gratitude, purpose (topics 16–17) |
| 18 | Nikohni parvarish qilish: kundalik, haftalik, oylik, yillik odatlar va umrbod reja | rituals, check-ins, life-stage plan (topics 19–20) |
| — | Xulosa | |
| Ilovalar | A. Juftliklar uchun ish daftari (also standalone workbook_uz.md); B. Yordam manbalari; C. Atamalar lugʻati; D. Guruhlar va kurslar uchun qoʻllanma; E. Manbalar | |

Chapter template: opening scene → problem → what research shows → what Islamic sources teach → moral reasoning/responsibility → practical steps → dialogue/example → exercise ("Birgalikda bajaring") → reflection questions → "Bob xulosasi".

## 4. Research plan

1. Islamic primary texts: offline Qurʼan dataset (npm `quran-json` 3.1.2: Uthmani text from QuranEnc, Saheeh International EN, E. Kuliev RU) and offline hadith database (npm `hadith` 1.3.0, sunnah.com data with Darussalam/Albani grades). Every Qurʼan and hadith reference is looked up by `tools/islamic_lookup.py` and recorded in the ledger.
2. Scholarly interpretation (4:34, maskan, housework, khulʼ): web search of established fatwa bodies and classical citations; presented with attribution and disagreement, flagged for human scholarly review.
3. Psychology: web search for primary papers/meta-analyses (Gottman, Karney & Bradbury, Gable, Algoe, Aron, Hawkins, Robles, Fincham, Schrodt, Falconier, Mitnick, Impett, Hall, Hazan & Shaver, Reis & Shaver, Stanley).
4. Safety and law: Uzbekistan law ZRU-561 (2019), 1146 hotline, Criminal Code art. 126; WHO violence and infertility data.

## 5. Constraints discovered at Stage 1

- Direct internet hosts (sunnah.com, quran.com, alquran.cloud) are blocked from the container; WebSearch works; npm/PyPI registries work. Hence offline datasets are the primary verification route.
- No published Uzbek Qurʼan translation is accessible offline. Uzbek renderings in the book are **the author's own meaning translations**, cross-checked against Saheeh International (EN) and Kuliev (RU). This is disclosed in the book and in the Islamic audit.
- EPUBCheck: installed from PyPI (`epubcheck` 5.3.0 wrapper with bundled jar).
