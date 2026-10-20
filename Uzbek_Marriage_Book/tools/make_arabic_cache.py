#!/usr/bin/env python3
"""Build research/arabic_cache.json: exact Arabic text for every {{AYAH:..}} and
{{HADITH:..}} token used in chapters/*.md, taken from the offline datasets.

Usage: make_arabic_cache.py --data DIR   (DIR as for islamic_lookup.py)

Hadith tokens use the form {{HADITH:urn}} where urn is the sunnah.com dataset
URN (see source_ledger.md). Only the matn field (content) is stored.
"""
import argparse, glob, json, os, re, sqlite3

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    p = argparse.ArgumentParser(); p.add_argument("--data", required=True); o = p.parse_args()
    text = "".join(open(f, encoding="utf-8").read() for f in sorted(glob.glob(os.path.join(ROOT, "chapters", "*.md"))))
    quran = json.load(open(os.path.join(o.data, "q/package/dist/quran.json"), encoding="utf-8"))
    db = sqlite3.connect(os.path.join(o.data, "h/package/data/hadith.db"))
    cache = {"ayah": {}, "hadith": {}}
    for ref in sorted(set(re.findall(r"\{\{AYAH:([0-9:\-@]+)\}\}", text))):
        if "@" in ref:  # word-range fragment of a single verse: s:v@a-b
            sv, rng = ref.split("@"); s, v = sv.split(":"); wa, wb = map(int, rng.split("-"))
            words = quran[int(s) - 1]["verses"][int(v) - 1]["text"].split()
            cache["ayah"][ref] = "… " + " ".join(words[wa - 1:wb]) + " …"
            continue
        s, v = ref.split(":"); a, b = (v.split("-") + [v])[:2]
        verses = quran[int(s) - 1]["verses"]
        parts = [f"{verses[n-1]['text']} ﴿{to_ar_digits(n)}﴾" for n in range(int(a), int(b) + 1)]
        cache["ayah"][ref] = " ".join(parts)
    for urn in sorted(set(re.findall(r"\{\{HADITH:([0-9]+)\}\}", text))):
        row = db.execute("select c7 from hadith_content where c0=?", (int(urn),)).fetchone()
        if not row:
            raise SystemExit(f"hadith urn {urn} not found")
        cache["hadith"][urn] = re.sub(r"[‏‎]|\s+", " ", row[0]).strip(" ‏.،")
    out = os.path.join(ROOT, "research", "arabic_cache.json")
    json.dump(cache, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"wrote {out}: {len(cache['ayah'])} ayah refs, {len(cache['hadith'])} hadith")

def to_ar_digits(n):
    return str(n).translate(str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩"))

if __name__ == "__main__":
    main()
