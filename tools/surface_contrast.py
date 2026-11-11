#!/usr/bin/env python3
"""WCAG AA check for surfaces that paint their own background.

Mirrors mixins/_contrast.scss: white text when luminance <= 0.1833,
otherwise the preset gold-ink when that clears 4.5:1, otherwise black.
Run from the repo root: python3 tools/surface_contrast.py
"""
import colorsys
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PRESETS = json.load(open(os.path.join(HERE, "palettes.json")))
WHITE_MAX_L = 0.1833

FIXED = [
    ("pre", "#1a2332", "#f6f6f6"),
    ("pre link", "#0a3a6b", "#f6f6f6"),
    ("pre code", "#237794", "#f6f6f6"),
    ("code", "#9c1d3d", "#f9f2f4"),
    ("kbd", "#1a2332", "#f6f6f6"),
    ("box1 text", "#595959", "#ffffff"),
    ("box2 text", "#4a4a4a", "#e0e0e0"),
    ("box link fallback", "#0a3a6b", "#ffffff"),
    ("box link fallback on box2", "#0a3a6b", "#e0e0e0"),
    ("alert", "#816638", "#fcf8e3"),
    ("alert success", "#396e3a", "#dff0d8"),
    ("alert error", "#9d3f3d", "#f2dede"),
    ("alert info", "#2d6885", "#d9edf7"),
]


def rgb(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def luminance(h):
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in rgb(h)]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def contrast(fg, bg):
    a, b = luminance(fg), luminance(bg)
    return (max(a, b) + 0.05) / (min(a, b) + 0.05)


def adjust(h, d_l):
    r, g, b = rgb(h)
    hue, light, sat = colorsys.rgb_to_hls(r, g, b)
    light = min(1, max(0, light + d_l / 100))
    r, g, b = colorsys.hls_to_rgb(hue, light, sat)
    return "#{:02x}{:02x}{:02x}".format(round(r * 255), round(g * 255), round(b * 255))


def on_color(bg, ink):
    if luminance(bg) <= WHITE_MAX_L:
        return "#ffffff"
    if contrast(ink, bg) >= 4.5:
        return ink
    return "#000000"


def on_preferred(bg, preferred, ink):
    if contrast(preferred, bg) >= 4.5:
        return preferred
    return on_color(bg, ink)


def main():
    fails = []

    def check(preset, name, fg, bg):
        ratio = contrast(fg, bg)
        if ratio < 4.5:
            fails.append((preset, name, round(ratio, 2), fg, bg))

    for name, fg, bg in FIXED:
        check("all", name, fg, bg)

    for key, p in PRESETS.items():
        ink = p["gold_ink"]
        light = p["variant"] == "light"
        quote_bg = p["card"] if light else p["navy"]
        quote_tx = p["paper"] if light else p["nav_tx"]
        head_bg = adjust(p["line"], 10)
        box1_link = p["link"] if contrast(p["link"], "#ffffff") >= 4.5 else "#0a3a6b"
        box2_link = p["link"] if contrast(p["link"], "#e0e0e0") >= 4.5 else "#0a3a6b"
        panel_link = p["link"] if contrast(p["link"], p["navy"]) >= 4.5 else on_color(p["navy"], ink)
        quote_link = p["link"] if contrast(p["link"], quote_bg) >= 4.5 else on_color(quote_bg, ink)
        pairs = [
            ("box3", on_color(p["live"], ink), p["live"]),
            ("box4", on_color(p["link"], ink), p["link"]),
            ("box1 link", box1_link, "#ffffff"),
            ("box2 link", box2_link, "#e0e0e0"),
            ("quote", quote_tx, quote_bg),
            ("quote link", quote_link, quote_bg),
            ("th", on_preferred(head_bg, p["text"], ink), head_bg),
            ("showcase button", on_preferred(p["link"], p["showcase_tx"], ink), p["link"]),
            ("offcanvas button", on_preferred(p["link"], p["off_tx"], ink), p["link"]),
            ("header link", on_preferred(p["header_bg"], p["header_tx"], ink), p["header_bg"]),
            ("panel text", p["nav_tx"], p["navy"]),
            ("panel link", panel_link, p["navy"]),
            ("text on card", p["text"], p["card"]),
            ("link on card", p["link"], p["card"]),
        ]
        for name, fg, bg in pairs:
            check(key, name, fg, bg)

    if fails:
        for item in fails:
            print("FAIL", *item)
        print("%d pair(s) under 4.5:1" % len(fails))
        return 1
    print("surface contrast OK (%d presets, fixed fills included)" % len(PRESETS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
