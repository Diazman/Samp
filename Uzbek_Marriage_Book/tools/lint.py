#!/usr/bin/env python3
"""Quality lint for the assembled manuscript (run after tools/build.py).

Checks: leftover ASCII apostrophes in Latin words, Cyrillic letters, placeholder
markers, unexpanded tokens, duplicated sentences across the book, very long
sentences, per-chapter word counts. Exit 1 on hard errors.
"""
import collections, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(ROOT, sys.argv[1] if len(sys.argv) > 1 else "manuscript_uz.md")
text = open(path, encoding="utf-8").read()
body = text.split("\n---\n", 1)[1] if text.startswith("---") else text
errors, warnings = [], []

# English titles in the reference list legitimately contain apostrophes.
uz_lines = [(i, l) for i, l in enumerate(body.splitlines(), 1) if not re.search(r"\*[A-Z][^*]*\*|\(\d{4}\)\.", l)]
for i, l in uz_lines:
    if re.search(r"[A-Za-zʻ]'[A-Za-z]|[oOgG]'", l):
        errors.append(f"ASCII apostrophe line {i}: {l[:90]}")
    if re.search(r"[Ѐ-ӿ]", l):
        errors.append(f"Cyrillic letter line {i}: {l[:90]}")
for pat in [r"\bTODO\b", r"\bXXX\b", r"\bTBD\b", r"\{\{", r"\[\.\.\.\]", r"lorem ipsum", r"PLACEHOLDER"]:
    for m in re.finditer(pat, body, flags=re.I):
        errors.append(f"placeholder/token '{m.group(0)}' near: {body[max(0,m.start()-40):m.start()+40]!r}")

# duplicate sentences (>= 12 words) anywhere in the book
sents = re.split(r"(?<=[.!?»])\s+", re.sub(r"\s+", " ", body))
seen = collections.Counter(s.strip() for s in sents if len(s.split()) >= 12 and not s.startswith(("|", ">", "-")))
for s, n in seen.items():
    if n > 1:
        warnings.append(f"sentence repeated {n}x: {s[:110]}")

long = [s for s in sents if len(s.split()) > 60 and not s.lstrip().startswith("|")]
for s in long:
    warnings.append(f"very long sentence ({len(s.split())} words): {s[:90]}")

# chapter word counts
chapters = re.split(r"\n(?=## )", body)
counts = []
for c in chapters:
    title = c.splitlines()[0].strip("# ").split("{")[0].strip()
    words = len(re.findall(r"[^\W\d_][\wʻʼ'-]*", re.sub(r"[؀-ۿ]+", "", c)))
    counts.append((title, words))
total = sum(w for _, w in counts)

print(f"Total Latin-script words (approx.): {total}")
for t, w in counts:
    print(f"  {w:6d}  {t[:70]}")
for w in warnings:
    print("WARN ", w)
for e in errors:
    print("ERROR", e)
print(f"{len(errors)} errors, {len(warnings)} warnings")
sys.exit(1 if errors else 0)
