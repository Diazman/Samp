#!/usr/bin/env python3
"""Orthographic normalisation for Uzbek Latin text.

- o' / g' (any apostrophe variant) -> oʻ / gʻ (U+02BB)
- apostrophe between two letters (tutuq belgisi) -> ʼ (U+02BC)
Arabic-script lines and fenced code are left untouched.
"""
import re, sys

APOS = "'’‘`´"
OG = re.compile(r"([oOgG])[" + APOS + r"](?=[^\W\d_]|\b)")
TUTUQ = re.compile(r"(?<=[A-Za-zʻ])[" + APOS + r"](?=[A-Za-z])")
ARABIC = re.compile(r"[؀-ۿ]")


def normalize_line(line):
    if ARABIC.search(line):
        return line
    line = OG.sub(lambda m: m.group(1) + "ʻ", line)
    line = TUTUQ.sub("ʼ", line)
    return line


def normalize_text(text):
    return "\n".join(normalize_line(l) for l in text.split("\n"))


if __name__ == "__main__":
    for path in sys.argv[1:]:
        t = open(path, encoding="utf-8").read()
        n = normalize_text(t)
        if n != t:
            open(path, "w", encoding="utf-8").write(n)
            print("normalized", path)
