#!/usr/bin/env python3
"""Extract every Qurʼan and hadith citation from chapters/*.md and check it
against the offline datasets.

Usage: check_refs.py --data DIR [--report research/refs_report.md]

Checks:
  * Qurʼan: sura name <-> number mapping, verse numbers exist; writes the
    surrounding Uzbek sentence next to the Saheeh International text so the
    meaning translation can be reviewed by a human.
  * Hadith: collection + number exists in the sunnah.com dataset; reports the
    dataset grade so that grade statements in the text can be compared.
Exit status 1 if any citation fails to resolve.
"""
import argparse, glob, json, os, re, sqlite3, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SURA = {  # Uzbek name used in the book -> number
    "Fotiha": 1, "Baqara": 2, "Oli Imron": 3, "Niso": 4, "Moida": 5, "Aʼrof": 7, "Tavba": 9,
    "Yusuf": 12, "Raʼd": 13, "Ibrohim": 14, "Nahl": 16, "Isro": 17, "Toho": 20, "Anbiyo": 21,
    "Nur": 24, "Furqon": 25, "Rum": 30, "Ahzob": 33, "Fussilat": 41, "Shuro": 42, "Hujurot": 49,
    "Hashr": 59, "Tagʻobun": 64, "Taloq": 65, "Tahrim": 66, "Shams": 91, "Sharh": 94,
}
COLL = {"Buxoriy": 1, "Muslim": 2, "Nasoiy": 3, "Abu Dovud": 10, "Termiziy": 30, "Ibn Moja": 38}

Q_RE = re.compile(r"(" + "|".join(map(re.escape, SURA)) + r")(?: surasi)?,\s*(\d+)(?:[–-](\d+))?(?:-oyat)")
Q_SHORT_RE = re.compile(r"\((" + "|".join(map(re.escape, SURA)) + r"),\s*(\d+)\)")
H_RE = re.compile(r"(" + "|".join(map(re.escape, COLL)) + r")(?: rivoyati)?[;,]?\s*(?:sunnah\.com raqamlashida\s*)?(\d{1,4}(?:\s?[a-z])?)(?:[–-](\d{1,4}))?")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--data", required=True)
    ap.add_argument("--report", default=os.path.join(ROOT, "research", "refs_report.md"))
    a = ap.parse_args()
    quran = json.load(open(os.path.join(a.data, "q/package/dist/quran_en.json"), encoding="utf-8"))
    db = sqlite3.connect(os.path.join(a.data, "h/package/data/hadith.db"))
    out, fails = ["# Reference check report (auto-generated)\n"], 0
    qseen, hseen = {}, {}
    for f in sorted(glob.glob(os.path.join(ROOT, "chapters", "*.md"))):
        name = os.path.basename(f)
        for ln, line in enumerate(open(f, encoding="utf-8"), 1):
            for m in list(Q_RE.finditer(line)) + list(Q_SHORT_RE.finditer(line)):
                s = SURA[m.group(1)]; v1 = int(m.group(2))
                v2 = int(m.group(3)) if m.lastindex and m.lastindex >= 3 and m.group(3) else v1
                ok = v2 <= quran[s - 1]["total_verses"]
                key = f"{s}:{v1}" + (f"-{v2}" if v2 != v1 else "")
                qseen.setdefault(key, []).append((name, ln, line.strip()[:400], ok))
                fails += not ok
            for m in H_RE.finditer(line):
                coll, num = m.group(1), m.group(2).replace(" ", " ")
                base = re.match(r"\d+", num).group(0)
                pat = re.compile(r"(^|[ ,])" + base + r"([ ,a-z]|$)")
                rows = [r for r in db.execute("select c0,c4,c13 from hadith_content where c1=?", (COLL[coll],)) if pat.search(r[1])]
                grades = sorted({(db.execute("select c7 from hadith_en_content where c0=?", (r[0],)).fetchone() or [""])[0].strip() for r in rows})
                if coll == "Termiziy" and not rows:
                    alt = db.execute("select c7 from hadith_en_content where c2=30 and c8 like ?", (f"%Hadith {base}%",)).fetchall()
                    rows, grades = alt, sorted({g[0].strip() for g in alt})
                ok = bool(rows)
                hseen.setdefault(f"{coll} {num}", []).append((name, ln, ok, grades))
                fails += not ok
    out.append(f"## Qurʼan citations ({len(qseen)} distinct)\n")
    for key in sorted(qseen, key=lambda k: [int(x) for x in re.split(r"[:-]", k)]):
        s, rest = key.split(":"); v1 = int(rest.split("-")[0]); v2 = int(rest.split("-")[-1])
        en = " ".join(quran[int(s) - 1]["verses"][v - 1]["translation"] for v in range(v1, v2 + 1))
        uses = qseen[key]
        out.append(f"### {key} ({quran[int(s)-1]['transliteration']}) — {'OK' if all(u[3] for u in uses) else 'FAIL'}\n")
        out.append(f"- **Saheeh Intl:** {en}")
        for n, ln, ctx, _ in uses:
            out.append(f"- `{n}:{ln}` — {ctx}")
        out.append("")
    out.append(f"## Hadith citations ({len(hseen)} distinct)\n")
    out.append("| Citation | Resolves | Dataset grade(s) | Locations |\n|---|---|---|---|")
    for key in sorted(hseen):
        uses = hseen[key]
        out.append(f"| {key} | {'OK' if all(u[2] for u in uses) else 'FAIL'} | {'; '.join(uses[0][3]) or '—'} | {', '.join(f'{u[0]}:{u[1]}' for u in uses)} |")
    open(a.report, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(f"Qurʼan refs: {len(qseen)} distinct; hadith refs: {len(hseen)} distinct; failures: {fails}")
    print("report:", a.report)
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
