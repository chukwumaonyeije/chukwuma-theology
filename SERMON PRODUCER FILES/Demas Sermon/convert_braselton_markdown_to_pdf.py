from __future__ import annotations

import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
)


ROOT = Path(r"C:\Users\onyei\Projects\chukwuma-theology\Demas Sermon")
OUTPUT_DIR = ROOT / "Braselton"

SOURCE_FILES = [
    ROOT / "Braselton Sermon Draft - Two Men, One Gospel.md",
    ROOT / "Braselton Sermon Long Manuscript - Two Men, One Gospel.md",
    ROOT / "Braselton Sermon Notes - Two Men, One Gospel.md",
    ROOT / "Braselton Sermon References - Demas and Luke.md",
    ROOT / "brasleton-podcast-script.md",
    ROOT / "brasleton-sermon-draft.md",
    ROOT / "brasleton-sermon-long.md",
    ROOT / "brasleton-sermon-notation.md",
    ROOT / "brasleton-sermon-references.md",
]


def normalize_inline(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<font face='Courier'>\1</font>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="TitleCenter",
            parent=styles["Title"],
            alignment=TA_CENTER,
            fontSize=20,
            leading=24,
            spaceAfter=18,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Heading1Custom",
            parent=styles["Heading1"],
            fontSize=16,
            leading=20,
            spaceBefore=8,
            spaceAfter=10,
            textColor=colors.HexColor("#1f3b2d"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="Heading2Custom",
            parent=styles["Heading2"],
            fontSize=13,
            leading=16,
            spaceBefore=6,
            spaceAfter=8,
            textColor=colors.HexColor("#2d4739"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="Heading3Custom",
            parent=styles["Heading3"],
            fontSize=11,
            leading=14,
            spaceBefore=4,
            spaceAfter=6,
            textColor=colors.HexColor("#3f5b4d"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyCustom",
            parent=styles["BodyText"],
            fontSize=10.5,
            leading=14,
            spaceAfter=7,
        )
    )
    styles.add(
        ParagraphStyle(
            name="QuoteCustom",
            parent=styles["BodyText"],
            fontSize=10.5,
            leading=14,
            leftIndent=18,
            textColor=colors.HexColor("#4a4a4a"),
            italic=True,
            borderPadding=6,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="MetaCustom",
            parent=styles["BodyText"],
            fontSize=9.5,
            leading=12,
            textColor=colors.HexColor("#666666"),
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CodeCustom",
            parent=styles["Code"],
            fontName="Courier",
            fontSize=8.8,
            leading=11,
            leftIndent=12,
            backColor=colors.HexColor("#f4f4f4"),
        )
    )
    return styles


def flush_paragraph(buffer, story, styles):
    if not buffer:
        return
    text = " ".join(line.strip() for line in buffer).strip()
    if text:
        style = styles["MetaCustom"] if text.startswith("**Texts:**") or text.startswith("**Title:**") else styles["BodyCustom"]
        story.append(Paragraph(normalize_inline(text), style))
    buffer.clear()


def flush_bullets(items, story, styles):
    if not items:
        return
    flow = ListFlowable(
        [
            ListItem(Paragraph(normalize_inline(item), styles["BodyCustom"]))
            for item in items
        ],
        bulletType="bullet",
        start="circle",
        leftIndent=18,
    )
    story.append(flow)
    story.append(Spacer(1, 0.08 * inch))
    items.clear()


def convert_markdown(source: Path, destination: Path) -> None:
    styles = build_styles()
    story = []
    paragraph_buffer = []
    bullet_buffer = []
    in_code = False
    code_lines = []

    lines = source.read_text(encoding="utf-8").splitlines()

    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()

        if stripped == "```":
            flush_paragraph(paragraph_buffer, story, styles)
            flush_bullets(bullet_buffer, story, styles)
            if in_code:
                story.append(Preformatted("\n".join(code_lines), styles["CodeCustom"]))
                story.append(Spacer(1, 0.08 * inch))
                code_lines.clear()
                in_code = False
            else:
                in_code = True
            continue

        if in_code:
            code_lines.append(line)
            continue

        if not stripped:
            flush_paragraph(paragraph_buffer, story, styles)
            flush_bullets(bullet_buffer, story, styles)
            continue

        if stripped == "---":
            flush_paragraph(paragraph_buffer, story, styles)
            flush_bullets(bullet_buffer, story, styles)
            story.append(PageBreak())
            continue

        if stripped.startswith("# "):
            flush_paragraph(paragraph_buffer, story, styles)
            flush_bullets(bullet_buffer, story, styles)
            style = styles["TitleCenter"] if not story else styles["Heading1Custom"]
            story.append(Paragraph(normalize_inline(stripped[2:].strip()), style))
            continue

        if stripped.startswith("## "):
            flush_paragraph(paragraph_buffer, story, styles)
            flush_bullets(bullet_buffer, story, styles)
            story.append(Paragraph(normalize_inline(stripped[3:].strip()), styles["Heading2Custom"]))
            continue

        if stripped.startswith("### "):
            flush_paragraph(paragraph_buffer, story, styles)
            flush_bullets(bullet_buffer, story, styles)
            story.append(Paragraph(normalize_inline(stripped[4:].strip()), styles["Heading3Custom"]))
            continue

        if stripped.startswith("> "):
            flush_paragraph(paragraph_buffer, story, styles)
            flush_bullets(bullet_buffer, story, styles)
            story.append(Paragraph(normalize_inline(stripped[2:].strip()), styles["QuoteCustom"]))
            continue

        if stripped.startswith("- "):
            flush_paragraph(paragraph_buffer, story, styles)
            bullet_buffer.append(stripped[2:].strip())
            continue

        paragraph_buffer.append(line)

    flush_paragraph(paragraph_buffer, story, styles)
    flush_bullets(bullet_buffer, story, styles)

    doc = SimpleDocTemplate(
        str(destination),
        pagesize=letter,
        leftMargin=0.8 * inch,
        rightMargin=0.8 * inch,
        topMargin=0.7 * inch,
        bottomMargin=0.7 * inch,
        title=source.stem,
        author="OpenAI Codex",
    )
    doc.build(story)


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    for source in SOURCE_FILES:
        if not source.exists():
            raise FileNotFoundError(source)
        destination = OUTPUT_DIR / f"{source.stem}.pdf"
        convert_markdown(source, destination)
        print(destination)


if __name__ == "__main__":
    main()
