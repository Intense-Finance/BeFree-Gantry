# Changelog

All notable changes to BeFree Gantry are documented here. This project uses [Semantic Versioning](https://semver.org/).

## [1.1.0] - 2026-11-03

### Added
- A **Slideshow** section directly under Navigation and above the page body, following Helium's empty section pattern (Helium puts its slider in the header band under the nav). It is part of the Default, Left Sidebar, Both Sidebars, Full Width, Magazine Home, Home and Error layout presets, so it shows up in the Gantry Layout Manager. Layout is Fullwidth (Flushed Content). Styling matches the other BeFree sections, slider markup stays within the viewport on small screens, and the section is not rendered when nothing is assigned.
- **Bloom**, a light style preset in the popular violet / rose / amber palette (bright accents on a light ground). Every checked text and background pair meets WCAG AA. The lowest pair is 5.98:1.

### Removed
- **Cyan Night** (the old preset4). It was the most redundant dark preset: the same lime-and-cyan accents as Meld Neon, with cyan leading. The preset4 id is kept, so an outline that points at preset4 still resolves. Colors already saved on an outline are not rewritten. Light Paper is unchanged.

### Notes
- Existing layout particles are untouched, including the homepage hero, sidebars, Sister Site block and `system-content` (where the stock charts live). An empty Slideshow section produces no markup. Outlines already saved in `custom/` are not edited by the theme update.

### Upstream (Gantry 5.6.4)
Checked the latest official release, **Gantry 5.6.4** (3 September 2026), and the WordPress Hydrogen and Helium theme zips from that same release (`wordpress-tpl_g5_hydrogen_v5.6.4.zip`, `wordpress-tpl_g5_helium_v5.6.4.zip`). BeFree was already built from Hydrogen 5.6.4. After the rename, the shared PHP templates, Twig views, blueprints, and SCSS match that zip except for BeFree's own palette, layouts, Slideshow section, and particles. Those BeFree changes stay. Light Paper and the chart rules were not edited in this pass.

Brought in from Helium 5.6.4 `functions.php` (Hydrogen 5.6.4 still has the older text): the warning to put custom code in `custom/functions.php`, and the note that this file is PHP 5.6 compatible rather than PHP 5.2. The runtime floor stays Gantry 5.5. The private RocketTheme updater block is still not included.

Not copied, because they are not in the WordPress theme:

- GitHub `develop` is **5.6.5** (not a release; gantry.org marks CI builds as not for production). Its changes are in the framework plugin: particle AJAX returns 404 instead of a Whoops page for anonymous requests, detailed errors are admin-only, vendor scripts are bundled instead of loaded from a CDN, and Joomla's `includes/gantry.php` uses `?Gantry $gantry = null` for PHP 8.4. The WordPress theme's `includes/gantry.php` does not have that signature. Nucleus is not bundled in this theme.

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
