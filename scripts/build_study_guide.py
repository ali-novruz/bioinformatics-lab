"""Build the Azerbaijani guide from reviewed Markdown; requires reportlab.

Usage: python scripts/build_study_guide.py [--font-dir /path/to/fonts]
Windows Arial or Linux DejaVu Sans font files are supported.
"""

import argparse
import html
import json
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--font-dir", type=Path)
    args = parser.parse_args()
    font_dir = args.font_dir or next(
        (
            p
            for p in [
                Path("C:/Windows/Fonts"),
                Path("/usr/share/fonts/truetype/dejavu"),
            ]
            if p.exists()
        ),
        None,
    )
    if font_dir is None:
        raise SystemExit("Pass --font-dir with Arial or DejaVu Sans fonts")
    arial = (font_dir / "arial.ttf").exists()
    names = (
        ["arial.ttf", "arialbd.ttf"]
        if arial
        else ["DejaVuSans.ttf", "DejaVuSans-Bold.ttf"]
    )
    for family, name in zip(["Guide", "GuideBold"], names, strict=True):
        pdfmetrics.registerFont(TTFont(family, str(font_dir / name)))
    pdfmetrics.registerFontFamily(
        "Guide",
        normal="Guide",
        bold="GuideBold",
        italic="Guide",
        boldItalic="GuideBold",
    )
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="BodyAZ",
            fontName="Guide",
            fontSize=10.4,
            leading=15.6,
            spaceAfter=9,
            textColor=colors.HexColor("#233846"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="HeadingAZ",
            fontName="GuideBold",
            fontSize=21,
            leading=27,
            spaceAfter=17,
            textColor=colors.HexColor("#146773"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="SubAZ",
            fontName="GuideBold",
            fontSize=13,
            leading=18,
            spaceBefore=12,
            spaceAfter=7,
            keepWithNext=True,
            textColor=colors.HexColor("#146773"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="SmallAZ", fontName="Guide", fontSize=8, leading=11, spaceAfter=5
        )
    )
    styles.add(
        ParagraphStyle(name="TableAZ", fontName="Guide", fontSize=8.2, leading=11)
    )
    styles.add(
        ParagraphStyle(
            name="CoverAZ",
            fontName="GuideBold",
            fontSize=34,
            leading=41,
            textColor=colors.HexColor("#146773"),
            spaceAfter=25,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CodeAZ",
            fontName="Courier",
            fontSize=7.8,
            leading=11,
            backColor=colors.HexColor("#eef5f5"),
            borderPadding=9,
            spaceAfter=12,
        )
    )
    story = []

    def inline(text):
        text = html.escape(text)
        text = re.sub(
            r"\[([^]]+)\]\(([^)]+)\)",
            lambda m: (
                '<link href="' + m[2] + '" color="#146773">' + m[1] + "</link>"
                if m[2].startswith("https://")
                else m[1]
            ),
            text,
        )
        text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)
        text = re.sub(r"`([^`]+)`", r'<font color="#146773">\1</font>', text)
        return text.replace("—", "-").replace("–", "-")

    def para(text, style="BodyAZ"):
        story.append(Paragraph(inline(text), styles[style]))

    def markdown(text):
        lines = text.splitlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                i += 1
                continue
            if line.startswith("```"):
                code = []
                i += 1
                while i < len(lines) and not lines[i].startswith("```"):
                    code.append(lines[i])
                    i += 1
                story.append(Preformatted("\n".join(code), styles["CodeAZ"]))
            elif line.startswith("|"):
                rows = []
                while i < len(lines) and lines[i].strip().startswith("|"):
                    cells = [x.strip() for x in lines[i].strip().strip("|").split("|")]
                    if not all(re.fullmatch(r"[-: ]+", x) for x in cells):
                        rows.append(
                            [Paragraph(inline(x), styles["TableAZ"]) for x in cells]
                        )
                    i += 1
                available = A4[0] - 100
                ncols = len(rows[0])
                first = 38 if ncols == 4 else 98
                widths = [first] + [(available - first) / (ncols - 1)] * (ncols - 1)
                table = Table(rows, colWidths=widths, repeatRows=1, hAlign="LEFT")
                table.setStyle(
                    TableStyle(
                        [
                            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#dceff0")),
                            ("VALIGN", (0, 0), (-1, -1), "TOP"),
                            (
                                "GRID",
                                (0, 0),
                                (-1, -1),
                                0.35,
                                colors.HexColor("#c8d6dd"),
                            ),
                            ("LEFTPADDING", (0, 0), (-1, -1), 6),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                            ("TOPPADDING", (0, 0), (-1, -1), 5),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                        ]
                    )
                )
                story.extend([table, Spacer(1, 12)])
                continue
            elif line.startswith("# "):
                para(line[2:], "HeadingAZ")
            elif line.startswith("##"):
                para(line.lstrip("# ").strip(), "SubAZ")
            else:
                para(line)
            i += 1

    story.append(Spacer(1, 70))
    para("BIOINFORMATICS RESEARCH LAB", "SubAZ")
    para("Bioinformatika\npraktikumu".replace("\n", " "), "CoverAZ")
    para(
        "UNEC materiallarından mənbəli konspektlər, işlək layihələr və özünü yoxlama tapşırıqları."
    )
    story.append(Spacer(1, 24))
    para("8 dərs · 3 laboratoriya · 24 tapşırıq", "SubAZ")
    para("16 sentyabr 2026 | Şəxsi tədris nəşri")
    para(
        "Bu bələdçi təqdim edilmiş dərslərdən seçilmiş hissələr əsasında repo üçün yenidən hazırlanıb. UNEC-in rəsmi dərsliyi və ya klinik istifadə təlimatı deyil."
    )
    para("Repo: https://github.com/ali-novruz/bioinformatics-lab", "SmallAZ")
    para(
        "Mənbələr: resources/unec/catalog.csv; kitablar: resources/books/pdf-manifest.json. Elektron repo bütün kodu, nəticələri və tam mənbə linklərini saxlayır.",
        "SmallAZ",
    )
    story.append(PageBreak())
    handbook = (ROOT / "docs/unec/handbook.md").read_text(encoding="utf-8")
    for chapter in re.split(r"(?m)^## ", handbook)[1:]:
        markdown("# " + chapter)
        story.append(PageBreak())
    for name in ["course-plan.md", "exercises.md", "errata.md"]:
        content = (ROOT / "docs/unec" / name).read_text(encoding="utf-8")
        if name == "exercises.md":
            sections = re.split(r"(?m)^## ", content)
            markdown(sections[0])
            for section in sections[1:]:
                start = len(story)
                markdown("## " + section)
                group = story[start:]
                del story[start:]
                story.append(KeepTogether(group))
        else:
            markdown(content)
        story.append(PageBreak())
    para("Mənbə və PDF kitabxanası", "HeadingAZ")
    para(
        "Konspektdə U ilə başlayan kimliklər orijinal UNEC faylının son dörd rəqəmidir. Məsələn U4252: UNEC__1789524252.pptx. Abzaslar yerli mətn çıxarışının, PDF səhifələri fiziki səhifələrin nömrələridir. Seçilmiş hissələr oxunub; bütün kitablar və şəkil ağırlıqlı slaydlar tam yoxlanmış sayılmır."
    )
    for book in json.loads(
        (ROOT / "resources/books/pdf-manifest.json").read_text(encoding="utf-8")
    )["books"]:
        para(book["title"], "SubAZ")
        para(book["author"] + " | " + str(book["pages"]) + " səhifə.")
        para(book["path"], "SmallAZ")
        para(book["license"], "SmallAZ")
    para(
        "Orijinal mənbələr dəyişdirilməyib. İstifadəçinin təqdim etdiyi iki kitab üçün açıq yayım lisenziyası müəyyən edilməyib. Müəllif hüquqları saxlanılır. Yeni konspektlə orijinal kitabların müəllifliyi bir-birindən ayrıdır."
    )
    para("Yekun qeyd", "SubAZ")
    para(
        "Təlim nəticəsi yalnız yüksək model balı deyil: mənbəni tapmaq, düzgün sual qurmaq, analizi təkrarlamaq və nəticənin sərhədini izah etməkdir."
    )

    destination = ROOT / "resources/unec/bioinformatika-praktikum.pdf"

    def footer(canvas, doc):
        canvas.setStrokeColor(colors.HexColor("#b7d4d7"))
        canvas.line(50, 48, A4[0] - 50, 48)
        canvas.setFont("Guide", 8)
        canvas.setFillColor(colors.HexColor("#49606b"))
        canvas.drawString(50, 34, "Bioinformatics Research Lab | Praktikum 2026")
        canvas.drawRightString(A4[0] - 50, 34, str(doc.page))

    doc = SimpleDocTemplate(
        str(destination),
        pagesize=A4,
        rightMargin=50,
        leftMargin=50,
        topMargin=45,
        bottomMargin=65,
        title="Bioinformatika praktikumu",
        author="Bioinformatics Research Lab",
        pageCompression=1,
    )
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(destination)


if __name__ == "__main__":
    main()
