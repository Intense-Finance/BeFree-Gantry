# Changelog

All notable changes to BeFree Gantry are documented here. This project uses [Semantic Versioning](https://semver.org/).

## [1.0.0] - 2026-11-01

### Added
- First release: a Gantry 5 theme for WordPress that blends BeFree's navy and gold industrial look with the if.finance neon palette (lime and cyan).
- Six style presets: Meld Neon (default), Industrial, BeFree Navy, Cyan Night, Lime Terminal and Light Paper. Every text and background pair meets WCAG AA (4.5:1 or better).
- Layout presets: Default (main + right sidebar), Left Sidebar, Both Sidebars, Full Width, Magazine Home (showcase hero + 3-up feature grid) and Offline/Error. Thumbnails appear in the Gantry admin.
- A new **Styles > BeFree Meld** section with the look (Standard / Industrial / Light), card radius and ten palette colors.
- A **Sister Site** particle with configurable eyebrow, pair labels, title, URL chip, text, buttons (gold / ghost / neon) and note. It uses plain links and does no tracking.
- Bundled Barlow Condensed (500/600/700) and Outfit (variable 400 to 600) WOFF2 fonts under the SIL Open Font License 1.1 (`fonts/OFL.txt`).
- Block variations: `bf-card`, `bf-navy`, `bf-glow`, `bf-hazard`. Utility classes: `bf-eyebrow`, `bf-live`, `bf-card`, `bf-panel`, `bf-stats`, `bf-pills`, `bf-btn-*`, `bf-dropcap` and others.

### Changed (from Gantry 5 Hydrogen 5.6.4)
- Renamed the theme to `befree-gantry` (folder, text domain, SCSS files and language template), following the Gantry "Changing the Name of a Theme" guide.
- Relicensed as GNU GPL v3 or later, which Hydrogen's "GPL v2 or later" terms allow. The original copyright notices are kept.

### Removed
- Hydrogen's private Gantry update-server client (`private/`), `MD5SUMS`, the Hydrogen installer class, and the bundled Roboto fonts.

### Notes
- Chart and TradingView embeds are left unstyled. The only rule touching them recolors the `.tradingview-widget-copyright` link. Custom HTML and Block widgets get no added padding or clipping, so chart widths stay exactly as embedded.
