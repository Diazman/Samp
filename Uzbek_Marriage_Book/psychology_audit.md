# Psychology and evidence audit

Project: *Bir umrlik nikoh*. Audit date: 2026-10-20. Auditor: the authoring AI (Claude). Not a substitute for review by a licensed clinical/counselling psychologist (see §6).

## 1. Method

1. **Extraction.** All author–year citations, all numbers/percentages, all "Ilmiy maʼlumot" boxes, and phrases signalling strong claims ("aniqlangan", "isbotlangan", "har doim", "tadqiqotlar koʻrsatadi") were extracted from `chapters/*.md` with `grep` (commands recorded in the session; reproducible with the patterns in `tools/lint.py`).
2. **Tracing.** Each empirical claim was traced to a source in `source_ledger.md` (section D). Sources were checked by web search at abstract/index level (publisher page, PubMed/PMC, university repository, author lab page, WHO/Pew pages). Full texts were **not** read; effect sizes are quoted only when they appear in the abstract/index record.
3. **Claim-strength review.** Each claim was checked for causal language not justified by correlational designs, for generalisation from Western samples, and for deterministic gender or personality statements.
4. **Safety review.** Every chapter was checked for advice that could excuse abuse, coercion or harmful behaviour, and for joint exercises unsafe for people in abusive relationships.

## 2. Claims and their evidence status

Legend — **E**: established (meta-analysis / large review / official statistics); **S**: supported by specific studies, generalisation limited; **C**: contested or popular-only; **P**: practical suggestion / clinical guidance, labelled as such.

| Ch | Claim in book | Source | Status | Notes / caveat in text |
|---|---|---|---|---|
| 1 | Marital *quality* associated with health (small effects, comparable to health behaviours) | Robles et al. 2014 | E | "aniqlangan" changed to "qayd etilgan… bogʻliq"; causal caveat present |
| 1, 11, 15 | Vulnerability–stress–adaptation model | Karney & Bradbury 1995 | E | presented as a model |
| 1, 13 | Satisfaction declines slightly on average after first child; non-parents decline similarly | Mitnick et al. 2009 | E | both halves stated |
| 2 | Deliberate decisions vs "sliding" | Stanley et al. 2006 | S | caveat: Western cohabitation context |
| 2 | Emotional instability (neuroticism) consistently associated with lower marital satisfaction | Karney & Bradbury 1995 | E | framed as tendency; personal growth emphasised; no determinism |
| 3 | Relationship education: small–moderate effects on quality and communication | Hawkins et al. 2008 | E | "oʻrtacha" → "kichik-oʻrtacha" |
| 3 | Premarital programmes: quality effect not robust with unpublished studies | Fawcett et al. 2010 | E | stated |
| 4, 17 | Romantic love can persist in long marriages; obsessive love not linked to satisfaction | Acevedo & Aron 2009 | S | |
| 4 | Turning toward everyday bids linked to positive affect in later conflict | Driver & Gottman 2004 | S | **Corrected**: earlier draft implied a divorce-prediction result; "86% vs 33%" figures deliberately not used |
| 4, 17 | Novel shared activities → short-term relationship quality gains | Aron et al. 2000 | S/C | small lab studies; mixed replication stated |
| 4, 7 | Friendship/love maps; perpetual problems | Gottman & Silver 1999 | P/C | labelled as popular account from Gottman's observations |
| 5 | Intimacy = disclosure + perceived responsiveness | Reis & Shaver 1988; Laurenceau et al. 1998 | E | |
| 5 | "Five love languages" lacks strong support; "balanced diet" | Impett et al. 2024 | S | |
| 5 | Most psychological gender differences small | Hyde 2005 | E | **Added** to replace an uncited statement |
| 5 | Adult attachment framework | Hazan & Shaver 1987 | E | explicit warning against labelling/diagnosing |
| 5 | Demand–withdraw associated with lower satisfaction/intimacy | Schrodt et al. 2014 | E | "no culprit" framing |
| 6 | Active-constructive responses to good news | Gable et al. 2004 | S | |
| 6 | Conversation start-up predicts course; accepting influence | Carrère & Gottman 1999; Gottman et al. 1998 | S | small US samples |
| 6 | "I"-statements, speaker–listener technique | — | P | presented as practical technique |
| 7 | Criticism, contempt, defensiveness, stonewalling linked to later divorce | Gottman & Levenson 2000; Gottman 1994 | S | **Explicit caveat** that popular "% accuracy" claims are criticised; not used |
| 7 | Flooding; ≥20-minute break | Gottman Institute practitioner guidance | P | labelled as clinical rule of thumb, not validated threshold |
| 7 | Hadith on sitting/lying down when angry | (religious, not psychological) | — | not presented as scientific evidence |
| 11 | Financial disagreements strongest disagreement predictor of divorce; financial status not, once disagreements controlled | Dew et al. 2012 | S | US sample stated |
| 11, 15 | Dyadic coping associated with satisfaction | Falconier et al. 2015 | E | Western samples stated |
| 12 | Triangulation (family systems) | Bowen 1978 | P | conceptual, not empirical claim |
| 13 | Cognitive labour: anticipate, identify, decide, monitor; women did more anticipation/monitoring | Daminger 2019 | S | small qualitative US study stated |
| 13 | 56% of US married adults rate sharing chores "very important" | Pew 2016 | E (survey) | "not Uzbekistan" stated |
| 13 | Spanking associated with detrimental outcomes, not compliance | Gershoff & Grogan-Kaylor 2016 | E | correlational caveat stated |
| 14 | Benevolence vs retaliation/avoidance and conflict resolution | Fincham et al. 2004 | S | |
| 15 | Infertility affects ~17.5% of adults | WHO 2023 | E | |
| 15 | ~10% pregnant / ~13% postpartum women experience mental disorder (mainly depression) | WHO maternal mental health page | E | danger signs and referral advice included |
| 16 | 27% of ever-partnered women 15–49 experienced physical/sexual IPV | Sardinha et al. 2022; WHO 2021 | E | |
| 16 | Female vs male homicides by intimate partner (≈39% vs ≈6%) | Stöckl et al. 2013 | E | **Added** to support a previously uncited claim |
| 16 | Separation/estrangement from controlling partner raises femicide risk | Campbell et al. 2003 | S | **Added**; US study stated |
| 16 | Child witnesses show more problems | Kitzmann et al. 2003 | E | **Added** |
| 16 | Coercive control concept | Stark 2007 | S | conceptual |
| 16 | Cycle of violence | — | C | hedged: "koʻp (lekin hamma emas) holatlarda" |
| 16 | Conjoint therapy generally not advised during active violence | practice guidance (counselling sources) | P | framed as "mutaxassislar odatda tavsiya etmaydi" |
| 17 | Positive/shared humour ↔ satisfaction; aggressive humour negative | Hall 2017 | E | |
| 17 | Everyday gratitude → next-day connection for both partners | Algoe et al. 2010 | S | |
| 17 | Religiousness modestly associated with marital functioning; joint religious activities | Mahoney et al. 2001 | S | mostly US Christian samples stated; wording softened |
| 10 | Virginity testing has no scientific basis | WHO/OHCHR/UN Women 2018 | E | |

## 3. Problems found and corrected

1. **Overstated causal wording** (ch 1: "aniqlangan") → association wording.
2. **Misattributed finding** (ch 4): text implied Driver & Gottman (2004) reported the long-term divorce difference by "turning toward"; corrected to the paper's actual focus (daily interactions and positive affect during conflict); long-term claim attributed to Gottman's popular books and qualified.
3. **Uncited generalisations** supported or softened: gender differences (ch 5, Hyde 2005 added); femicide sex ratio (ch 16, Stöckl 2013 added); separation risk (ch 16, Campbell 2003 added); child witnesses (ch 16, Kitzmann 2003 added); perpetual problems (ch 7, Gottman & Silver 1999 cited as popular source); triangulation (ch 12, Bowen 1978).
4. **Effect-size wording** (ch 3) adjusted to "kichik-oʻrtacha".
5. **Opinion presented as fact** (ch 13, childcare fatigue) reworded as reported experience.
6. **Cycle of violence** hedged as not universal.
7. **Mahoney et al. 2001** summary softened to what could be verified.
8. **Deliberately excluded:** "Gottman predicts divorce with 90%+ accuracy", "5:1 magic ratio", "86% vs 33% turning toward", love-languages as established science, "Mars/Venus" gender claims, any Uzbekistan divorce statistics (not verified).

## 4. Checks against harm

- Every chapter whose exercises involve joint conversation either links to ch 16 or carries a safety note; the workbook opens with a prominent warning not to do joint exercises in abusive relationships.
- Patience, forgiveness and obedience are explicitly limited: ch 8 (obedience only in maʼruf), ch 14 (forgiveness ≠ reconciliation/return to danger), ch 16 (sabr ≠ consent to oppression; joint therapy and family "reconciliation" meetings not advised during active abuse).
- Fictional characters are described by behaviour; no diagnoses are given. Attachment styles are explicitly "not labels".
- Gender: responsibilities and examples are given for both spouses in each relevant chapter; women's household cognitive load and men's emotional-expression barriers are both addressed; abusers of either sex are covered.
- The book repeatedly states it does not replace therapy, medical care or legal/religious advice (front matter, ch 18, colophon).

## 5. Limitations that remain

- Sources were verified at abstract/catalogue level; full texts were not read. Volume/issue/page numbers for Driver & Gottman 2004, Gershoff & Grogan-Kaylor 2016, Hall 2017, Impett et al. 2024, Fawcett et al. 2010 come from the author's knowledge and were not independently confirmed by the searches (the titles, journals and years were).
- Most cited research comes from Western, largely US samples; Uzbek-specific relationship research was not located and is not cited.
- The WHO maternal mental health figures come from a web page that may be updated.
- No Uzbek clinical guideline for couples therapy or IPV screening was located; recommendations follow international practice guidance.

## 6. Items for review by a qualified psychologist

1. Chapter 16 safety-planning steps and wording for Uzbek context.
2. Chapter 10 discussion of sexual difficulties and referral advice.
3. Chapter 15 postpartum depression warning signs.
4. Whether the "20-minute break" guidance and attachment-style descriptions are appropriately hedged for lay readers.
