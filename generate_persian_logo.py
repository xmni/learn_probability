#!/usr/bin/env python3
"""Generate Persian logos (logo.png, logo-dark.png, favicon.ico) for یادگیری احتمال."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

import arabic_reshaper
from bidi.algorithm import get_display

ROOT = Path(__file__).resolve().parent
FONT_BOLD = ROOT / "assets/fonts/Vazirmatn-Bold.ttf"
FONT_MEDIUM = ROOT / "assets/fonts/Vazirmatn-Medium.ttf"
ORIGINAL = ROOT / "assets/original-logo.png"

WIDTH, HEIGHT = 1298, 432
DIE_WIDTH = 420
TEXT_X = 480
LINE1 = "یادگیری"
LINE2 = "احتمال"


def _shape(text: str) -> str:
    return get_display(arabic_reshaper.reshape(text))


def _load_die() -> Image.Image:
    src = Image.open(ORIGINAL).convert("RGBA")
    die = src.crop((0, 0, DIE_WIDTH, HEIGHT))
    return die


def _text_color(dark: bool) -> tuple[int, int, int, int]:
    if dark:
        return (255, 255, 255, 255)
    return (58, 72, 88, 255)


def _make_logo(dark: bool) -> Image.Image:
    canvas = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    die = _load_die()
    canvas.paste(die, (0, 0), die)

    draw = ImageDraw.Draw(canvas)
    color = _text_color(dark)

    font_top = ImageFont.truetype(str(FONT_MEDIUM), 96)
    font_bottom = ImageFont.truetype(str(FONT_BOLD), 118)

    y1 = 72
    y2 = 210
    draw.text((TEXT_X, y1), _shape(LINE1), font=font_top, fill=color)
    draw.text((TEXT_X, y2), _shape(LINE2), font=font_bottom, fill=color)

    return canvas


def _make_favicon(die: Image.Image) -> Image.Image:
    size = 64
    fav = die.resize((size, size), Image.Resampling.LANCZOS)
    return fav


def main() -> None:
    die = _load_die()

    logo = _make_logo(dark=False)
    logo_dark = _make_logo(dark=True)

    logo.save(ROOT / "logo.png", optimize=True)
    logo_dark.save(ROOT / "logo-dark.png", optimize=True)

    favicon = _make_favicon(die)
    favicon.save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])

    print("Wrote logo.png, logo-dark.png, favicon.ico")


if __name__ == "__main__":
    main()
