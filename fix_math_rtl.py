#!/usr/bin/env python3
"""Patch MyST build output so KaTeX math renders LTR inside RTL Persian pages."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

KATEX_OPEN = re.compile(r'<span class="katex"(?![^>]*\sdir=)')
KATEX_HTML_OPEN = re.compile(r'<span class="katex-html"(?![^>]*\sdir=)')


def patch_html(value: str) -> str:
    if not value or "katex" not in value:
        return value
    value = KATEX_OPEN.sub('<span class="katex" dir="ltr"', value)
    value = KATEX_HTML_OPEN.sub('<span class="katex-html" dir="ltr"', value)
    return value


def patch_node(node: dict) -> bool:
    changed = False
    if node.get("type") in {"inlineMath", "math"} and isinstance(node.get("html"), str):
        patched = patch_html(node["html"])
        if patched != node["html"]:
            node["html"] = patched
            changed = True
    for key in ("children", "mdast", "parts"):
        child = node.get(key)
        if isinstance(child, list):
            for item in child:
                if isinstance(item, dict) and patch_node(item):
                    changed = True
        elif isinstance(child, dict) and patch_node(child):
            changed = True
    return changed


def patch_json_file(path: Path) -> bool:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not patch_node(data):
        return False
    path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    return True


def patch_static_html(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    patched = patch_html(text)
    if patched == text:
        return False
    path.write_text(patched, encoding="utf-8")
    return True


def main() -> int:
    root = Path(__file__).resolve().parent
    build_roots = [root / "_build" / "site" / "content", root / "_build" / "html"]

    json_count = 0
    content_dir = build_roots[0]
    if content_dir.is_dir():
        for path in content_dir.glob("*.json"):
            if patch_json_file(path):
                json_count += 1

    html_count = 0
    html_dir = build_roots[1]
    if html_dir.is_dir():
        for path in html_dir.rglob("*.html"):
            if patch_static_html(path):
                html_count += 1

    print(f"Patched {json_count} content JSON file(s) and {html_count} HTML file(s).")
    if json_count == 0 and html_count == 0:
        print("Nothing to patch — run after `myst build`.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
