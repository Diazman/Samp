# Style guide and glossary (Uslub qoʻllanmasi va atamalar)

## Orthography
- Uzbek Latin (1995 alphabet, current usage). Letters: oʻ Oʻ gʻ Gʻ written with U+02BB (ʻ). Tutuq belgisi: U+02BC (ʼ) — maʼno, sanʼat, eʼtibor, masʼuliyat, Qurʼon, taʼlim, sheʼr, jurʼat.
- No ASCII apostrophe (') inside Uzbek words in the final text; `tools/lint.py` checks this.
- Quotation marks: «…» for Uzbek quotations and dialogue lines quoted inline; dialogues set as "— " (em dash) lines.
- Numbers: 1–10 in words in prose where natural; percentages as "17,5 foiz" (comma decimal).
- References in parentheses: (Gottman va Levenson, 2000); (Buxoriy, 5090); (Rum surasi, 21-oyat).

## Voice
- Warm, direct, respectful "siz" form. Never preachy without a reason; every exhortation is paired with an explanation.
- Gender-balanced: each chapter gives responsibilities and examples for both spouses.
- No stereotyping of regions, professions or ethnic groups. Mothers-in-law are not villains by default.
- Distinguish: *dinimiz buyuradi* (clear text) / *ulamolarning koʻpchiligi…* (interpretation) / *odatimizda…* (custom) / *tavsiya qilamiz* (advice).
- Do not diagnose fictional characters; describe behaviour.

## Islamic formulae
- After the Prophet's name: "sollallohu alayhi vasallam" (first mention per chapter in full; later "Paygʻambarimiz" with ﷺ symbol allowed once per chapter). Companions: "roziyallohu anhu/anho" on first mention per chapter.
- Allah — "Alloh taolo" / "Alloh".

## Name and title transliteration
| Arabic/English | Book form |
|---|---|
| Sahih al-Bukhari | Imom Buxoriy, «Sahih» (short: Buxoriy) |
| Sahih Muslim | Imom Muslim, «Sahih» (short: Muslim) |
| Sunan Abi Dawud | Abu Dovud |
| Jamiʻ at-Tirmidhi | Termiziy |
| Sunan an-Nasaʼi | Nasoiy |
| Sunan Ibn Majah | Ibn Moja |
| al-Adab al-Mufrad | Buxoriy, «Al-Adab al-mufrad» |
| Ashʼ-Shamaʼil | Termiziy, «Shamoil» |
| ʻAʼisha | Oisha onamiz (roziyallohu anho) |
| Khadija | Xadicha onamiz |
| Umm Salama | Ummu Salama onamiz |
| Abu Hurayra | Abu Hurayra |
| Hanafi | hanafiy mazhabi |

## Glossary (Atamalar lugʻati) — consistent terms
| Uzbek term used | Meaning / source term |
|---|---|
| sakinat (xotirjamlik) | sukun, Rum 30:21 |
| mavadda (mehr-muhabbat) | mawadda |
| rahmat, rahm-shafqat | rahma |
| maʼruf (yaxshilik, urf-odatdagi munosib muomala) | maʻruf, Niso 4:19 |
| mahr | mahr |
| nafaqa | nafaqa (maintenance) |
| qavvomlik (gʻamxoʻrlik masʼuliyati) | qiwama, Niso 4:34 |
| shuro / maslahat | shura |
| xulʼ | khulʻ (wife-initiated separation) |
| taloq | talaq |
| hakam | arbitrator, Niso 4:35 |
| nushuz | nushuz (serious marital rebellion/aversion; applied to both spouses in 4:34, 4:128) |
| hayo | modesty |
| gʻiybat | backbiting |
| ishonch | trust |
| xiyonat | betrayal / infidelity |
| zoʻravonlik | violence / abuse |
| majburlovchi nazorat | coercive control |
| bogʻlanish uslubi | attachment style |
| eʼtiborli javob (javobgarlik) | responsiveness |
| oʻzaro tiklanish urinishi | repair attempt |
| "toʻlib-toshish" (fiziologik) | flooding |
| koʻrinmas yuk (aqliy yuk) | mental load |
| hissiy murojaat | bid for connection |
| oilaviy psixolog / oilaviy maslahatchi | couples therapist / counsellor |

## Formatting of chapter elements
- `## N-bob. Title` as chapter heading (H1 is reserved for part titles in the build: `# I qism. …`).
- Boxes rendered as blockquotes with bold lead: `> **Ilmiy maʼlumot.** …`, `> **Diniy manba.** …`, `> **Diqqat.** …`.
- Exercises: `### Birgalikda bajaring` ; questions: `### Mulohaza uchun savollar` ; summary: `### Bob xulosasi`.
- Arabic: `{{AYAH:s:v}}` or `{{AYAH:s:v-w}}` tokens in chapter sources are expanded at build time from `research/arabic_cache.json`; hadith Arabic via `{{HADITH:key}}`.
