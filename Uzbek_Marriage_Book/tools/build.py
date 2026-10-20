#!/usr/bin/env python3
"""Assemble chapters into manuscript_uz.md and build DOCX + EPUB with pandoc.

Usage: python3 tools/build.py [--no-docx] [--no-epub]

Inputs : chapters/*.md (sorted by name), research/arabic_cache.json,
         assets/metadata.yaml, assets/epub.css, assets/fonts/AmiriQuran.woff2
Outputs: manuscript_uz.md, manuscript_uz.docx, manuscript_uz.epub,
         workbook_uz.md (from chapters/90_ilova_a_ish_daftari.md)
"""
import argparse, glob, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from normalize import normalize_text  # noqa: E402

TOKEN = re.compile(r"^((?:> ?)*)\{\{(AYAH|HADITH):([0-9:\-@]+)\}\}\s*$")


def expand_tokens(text, cache):
    out = []
    for line in text.splitlines():
        m = TOKEN.match(line)
        if not m:
            if "{{" in line:
                raise SystemExit(f"unexpanded token inside text: {line[:80]}")
            out.append(line)
            continue
        prefix, kind, ref = m.groups()
        arabic = cache["ayah" if kind == "AYAH" else "hadith"].get(ref)
        if arabic is None:
            raise SystemExit(f"missing Arabic cache entry for {kind}:{ref} — run tools/make_arabic_cache.py")
        out += [f'{prefix}::: {{.arabic dir="rtl" lang="ar"}}', f"{prefix}{arabic}", f"{prefix}:::"]
    return "\n".join(out) + "\n"


def assemble():
    cache = json.load(open(os.path.join(ROOT, "research", "arabic_cache.json"), encoding="utf-8"))
    files = sorted(glob.glob(os.path.join(ROOT, "chapters", "*.md")))
    body = []
    for f in files:
        txt = normalize_text(open(f, encoding="utf-8").read())
        body.append(expand_tokens(txt, cache))
    meta = open(os.path.join(ROOT, "assets", "metadata.yaml"), encoding="utf-8").read()
    manuscript = meta.rstrip() + "\n\n" + "\n\n".join(b.strip() + "\n" for b in body)
    open(os.path.join(ROOT, "manuscript_uz.md"), "w", encoding="utf-8").write(manuscript)
    def standalone(prefix, title, out):
        src = [f for f in files if os.path.basename(f).startswith(prefix)]
        if not src:
            return
        txt = expand_tokens(normalize_text(open(src[0], encoding="utf-8").read()), cache)
        txt = re.sub(r"^#(#+) ", r"\1 ", txt, flags=re.M)  # promote headings one level
        meta = f'---\ntitle: "{title}"\nlang: uz-Latn\n---\n\n'
        open(os.path.join(ROOT, out), "w", encoding="utf-8").write(meta + txt)
    standalone("90_", "Bir umrlik nikoh — Juftliklar uchun ish daftari", "workbook_uz.md")
    standalone("94_", "Bir umrlik nikoh — Manbalar", "references_uz.md")
    print(f"assembled {len(files)} files -> manuscript_uz.md")


def run(cmd):
    print("+", " ".join(cmd))
    subprocess.run(cmd, check=True, cwd=ROOT)


def build_docx():
    ref = os.path.join(ROOT, "build", "reference.docx")
    run([sys.executable, os.path.join(ROOT, "tools", "make_reference_docx.py"), ref])
    run(["pandoc", "manuscript_uz.md", "-o", "manuscript_uz.docx", "--from", "markdown",
         "--reference-doc", ref, "--toc", "--toc-depth=2",
         "--lua-filter", "tools/docx_filter.lua"])
    run([sys.executable, os.path.join(ROOT, "tools", "postprocess_docx.py"), "manuscript_uz.docx"])


def build_epub():
    run(["pandoc", "manuscript_uz.md", "-o", "manuscript_uz.epub", "--from", "markdown",
         "--to", "epub3", "--toc", "--toc-depth=2", "--split-level=2",
         "--css", "assets/epub.css", "--epub-embed-font", "assets/fonts/AmiriQuran.woff2",
         "--epub-title-page=true"])


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-docx", action="store_true")
    ap.add_argument("--no-epub", action="store_true")
    a = ap.parse_args()
    assemble()
    if not a.no_docx:
        build_docx()
    if not a.no_epub:
        build_epub()
