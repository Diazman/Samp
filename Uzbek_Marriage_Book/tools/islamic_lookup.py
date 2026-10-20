#!/usr/bin/env python3
"""Offline lookup of Quran verses and hadith for source verification.

Usage:
  islamic_lookup.py --data DIR quran 30:21 [2:187 ...]
  islamic_lookup.py --data DIR hadith bukhari 5090
  islamic_lookup.py --data DIR search "best of you" [--coll tirmidhi]

DIR must contain q/package/dist/quran_en.json (npm quran-json 3.1.2) and
h/package/data/hadith.db (npm hadith 1.3.0, sunnah.com data).
"""
import argparse, json, sqlite3, sys, os

COLL = {"bukhari": 1, "muslim": 2, "nasai": 3, "abudawud": 10, "tirmidhi": 30,
        "ibnmajah": 38, "malik": 40, "ahmad": 50, "nawawi40": 101, "riyadussalihin": 110,
        "mishkat": 113, "adab": 115, "shamail": 130, "bulugh": 200}

def quran(data, refs):
    d = json.load(open(os.path.join(data, "q/package/dist/quran_en.json")))
    for ref in refs:
        s, v = ref.split(":")
        v1, v2 = (v.split("-") + [v])[:2]
        sura = d[int(s) - 1]
        for n in range(int(v1), int(v2) + 1):
            ay = sura["verses"][n - 1]
            print(f"[{s}:{n}] {sura['transliteration']}\nAR: {ay['text']}\nEN: {ay['translation']}\n")

def hadith(data, coll, num):
    c = sqlite3.connect(os.path.join(data, "h/package/data/hadith.db"))
    cid = COLL[coll]
    import re
    pat = re.compile(r"(^|[ ,])" + re.escape(str(num)) + r"([ ,a-z]|$)")
    rows = [r for r in c.execute("select c0,c4,c6,c7,c8,c13 from hadith_content where c1=?", (cid,)) if pat.search(r[1])]
    if not rows:
        print("NOT FOUND"); return
    for urn, disp, pre, ar, post, grade in rows:
        en = c.execute("select c3,c4,c5,c7,c8 from hadith_en_content where c0=?", (urn,)).fetchone()
        print(f"{coll} {disp} (urn {urn})\nAR grade: {grade}\nAR: {pre} {ar} {post}")
        if en:
            print(f"EN: {en[0]} {en[1]} {en[2]}\nEN grade: {en[3]}\nREF: {en[4]}")
        print()

def search(data, term, coll=None, limit=15):
    c = sqlite3.connect(os.path.join(data, "h/package/data/hadith.db"))
    q = "select c0,c2,c4,c7,c8 from hadith_en_content where c4 like ?"
    args = [f"%{term}%"]
    if coll:
        q += " and c2=?"; args.append(COLL[coll])
    for urn, cid, txt, grade, ref in c.execute(q + f" limit {limit}", args):
        name = [k for k, v in COLL.items() if v == cid]
        print(f"--- {name} | {ref.splitlines()[0] if ref else ''} | grade: {grade}\n{txt[:500]}\n")

def strip(t):
    import re
    t = re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u200f\u200e]", "", t or "")
    return t.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا").replace("ى", "ي").replace("ة", "ه")

def arsearch(data, term, limit=15):
    c = sqlite3.connect(os.path.join(data, "h/package/data/hadith.db"))
    t = strip(term); n = 0
    for urn, cid, disp, ar, grade in c.execute("select c0,c1,c4,c7,c13 from hadith_content"):
        if t in strip(ar):
            name = [k for k, v in COLL.items() if v == cid]
            print(f"--- {name} {disp} (urn {urn}) grade: {grade}\n{ar[:400]}\n")
            n += 1
            if n >= limit: break

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--data", required=True)
    sub = p.add_subparsers(dest="cmd")
    a = sub.add_parser("quran"); a.add_argument("refs", nargs="+")
    b = sub.add_parser("hadith"); b.add_argument("coll"); b.add_argument("num")
    s = sub.add_parser("search"); s.add_argument("term"); s.add_argument("--coll"); s.add_argument("--limit", type=int, default=15)
    r = sub.add_parser("arsearch"); r.add_argument("term"); r.add_argument("--limit", type=int, default=15)
    o = p.parse_args()
    if o.cmd == "arsearch": arsearch(o.data, o.term, o.limit)
    if o.cmd == "quran": quran(o.data, o.refs)
    elif o.cmd == "hadith": hadith(o.data, o.coll, o.num)
    elif o.cmd == "search": search(o.data, o.term, o.coll, o.limit)
