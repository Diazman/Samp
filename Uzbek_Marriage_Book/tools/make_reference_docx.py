#!/usr/bin/env python3
"""Create build/reference.docx: pandoc's default reference doc restyled for the book.

A5 page, serif body, page breaks before part (H1) and chapter (H2) headings,
right-to-left "Arabic Quote" paragraph style, Uzbek (Latin) proofing language.
"""
import subprocess, sys
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Mm, Pt, RGBColor

out = sys.argv[1]
subprocess.run(["pandoc", "-o", out, "--print-default-data-file", "reference.docx"], check=True)
doc = Document(out)

sec = doc.sections[0]
sec.page_width, sec.page_height = Mm(148), Mm(210)
sec.left_margin = sec.right_margin = Mm(18)
sec.top_margin, sec.bottom_margin = Mm(20), Mm(20)

BODY = "Cambria"
STYLES = {s.name: s for s in doc.styles}


def set_lang(style, lang="uz-Latn-UZ"):
    rpr = style.element.get_or_add_rPr()
    el = rpr.find(qn("w:lang"))
    if el is None:
        el = OxmlElement("w:lang"); rpr.append(el)
    el.set(qn("w:val"), lang); el.set(qn("w:bidi"), "ar-SA")


for name in ["Normal", "Body Text", "First Paragraph", "Compact", "Block Text"]:
    try:
        st = STYLES[name]
    except KeyError:
        continue
    st.font.name = BODY
    st.font.size = Pt(11)
    st.element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:hAnsi"), BODY)
    pf = st.paragraph_format
    pf.space_after = Pt(6)
    pf.line_spacing = 1.15
    set_lang(st)

STYLES["Block Text"].paragraph_format.left_indent = Mm(6)
STYLES["Block Text"].font.size = Pt(10.5)

for name, size, brk in [("Heading 1", 20, True), ("Heading 2", 16, True), ("Heading 3", 12.5, False),
                        ("Title", 26, False), ("Subtitle", 14, False)]:
    st = STYLES[name]
    st.font.name = BODY
    st.font.size = Pt(size)
    st.font.color.rgb = RGBColor(0x3b, 0x2f, 0x1e)
    st.paragraph_format.page_break_before = brk
    st.paragraph_format.keep_with_next = True
    if name in ("Heading 1", "Title", "Subtitle"):
        st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_lang(st)

st = STYLES["Title"]
st.paragraph_format.space_before = Pt(120)

ar = doc.styles.add_style("Arabic Quote", WD_STYLE_TYPE.PARAGRAPH)
ar.base_style = STYLES["Normal"]
ar.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.RIGHT
ar.paragraph_format.space_after = Pt(6)
ppr = ar.element.get_or_add_pPr()
ppr.append(OxmlElement("w:bidi"))
rpr = ar.element.get_or_add_rPr()
fonts = rpr.get_or_add_rFonts()
for attr in ("w:ascii", "w:hAnsi", "w:cs"):
    fonts.set(qn(attr), "Traditional Arabic")
rtl = OxmlElement("w:rtl"); rpr.append(rtl)
for tag in ("w:sz", "w:szCs"):
    e = OxmlElement(tag); e.set(qn("w:val"), "30"); rpr.append(e)
set_lang(ar, "ar-SA")

doc.save(out)
print("reference doc:", out)
