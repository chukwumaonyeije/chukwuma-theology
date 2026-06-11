"""
Convert demas-vespers-FINAL.html slides to a 2-up PDF (2 slides per page).
Each slide is 1280×720 (16:9). Output page is US Letter landscape,
with two slides stacked vertically per page.
"""

import os, tempfile
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

HTML_PATH = Path("C:/Users/onyei/Projects/chukwuma-theology/demas-vespers-FINAL.html")
OUT_PDF   = HTML_PATH.parent / "demas-vespers-FINAL-2up-grayscale.pdf"

SLIDE_W, SLIDE_H = 1280, 720
TOTAL_SLIDES = 31

# ── 1. Capture every slide as a PNG ──────────────────────────────────────────
def capture_slides(tmp_dir: str) -> list[Path]:
    paths = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": SLIDE_W, "height": SLIDE_H})
        page.goto(HTML_PATH.as_uri(), wait_until="networkidle")

        for idx in range(TOTAL_SLIDES):
            # navigate to slide via keyboard (→ arrow) or by calling the JS helper
            if idx > 0:
                page.keyboard.press("ArrowRight")
                page.wait_for_timeout(120)

            img_path = Path(tmp_dir) / f"slide_{idx:03d}.png"
            page.screenshot(path=str(img_path))
            # Convert to grayscale in-place
            img = Image.open(img_path).convert("L")
            img.save(img_path)
            paths.append(img_path)
            print(f"  captured slide {idx+1}/{TOTAL_SLIDES}")

        browser.close()
    return paths

# ── 2. Build 2-up PDF ────────────────────────────────────────────────────────
def build_pdf(slide_paths: list[Path], out_path: Path):
    # Page dimensions: US Letter portrait (612 × 792 pt)
    # We want two slides per page with a small margin between them.
    PAGE_W, PAGE_H = letter          # 612 × 792 pt
    MARGIN   = 18                    # pt (0.25 in)
    GAP      = 10                    # pt between the two slides

    available_w = PAGE_W - 2 * MARGIN
    # Each slide gets half the height minus gap
    slot_h = (PAGE_H - 2 * MARGIN - GAP) / 2

    # Scale slide to fit the slot while preserving 16:9 aspect
    scale = min(available_w / SLIDE_W, slot_h / SLIDE_H)
    draw_w = SLIDE_W * scale
    draw_h = SLIDE_H * scale

    x_offset = MARGIN + (available_w - draw_w) / 2   # center horizontally

    c = canvas.Canvas(str(out_path), pagesize=letter)

    for i, slide_path in enumerate(slide_paths):
        slot_index = i % 2          # 0 = top, 1 = bottom

        if slot_index == 0:
            # start a new page (except the very first)
            if i > 0:
                c.showPage()
            y_top = (PAGE_H - MARGIN - draw_h)   # top slot y (PDF coords from bottom)
        else:
            y_top = MARGIN                        # bottom slot y

        c.drawImage(str(slide_path), x_offset, y_top, width=draw_w, height=draw_h)

    # Flush last page
    c.showPage()
    c.save()
    print(f"\nSaved: {out_path}")

# ── Main ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp:
        print("Capturing slides…")
        slides = capture_slides(tmp)
        print("Building PDF…")
        build_pdf(slides, OUT_PDF)
