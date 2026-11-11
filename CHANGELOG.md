# Changelog

All notable changes to BeFree Gantry are documented here. This project uses [Semantic Versioning](https://semver.org/).

## [1.2.2] - 2026-11-11

### Fixed
- Light surfaces now set a text color. On dark presets, `pre` / `.wp-block-preformatted`, `.box1`, `.box2`, alerts and the same kind of fill inherited `--bf-text` (light) and were unreadable. Each fill has a `--bf-*-bg` / `--bf-*-text` pair. Headings, `strong` and links inside those fills are included. Checked pairs are at least 4.5:1 on all six presets (`python3 tools/surface_contrast.py`).

### Notes
- Backgrounds of `pre`, code, boxes and alerts are unchanged. On BeFree Navy the preformatted block stays `#f6f6f6`; its text is `#1a2332` (was the light body color, 1.08:1).
- Striped WordPress tables no longer use the default `#f0f0f0` row. The stripe is an 8% tint of the body text so it stays on the preset.

## [1.2.1] - 2026-11-04

### Changed
- **Readable text defaults** (`_readable.scss`, loaded last): body text 1.125rem with line-height 1.6; main menu 1.0625rem (dropdowns 1rem); content-array details 90% -> 1rem; widget titles 1.15rem -> 1.3rem; sidebar and footer text 1.0625rem; post and page content 1.125rem with line-height 1.7.

### Notes
- Headings, charts and iframes are unchanged. All sizes are rem.
- `custom/scss/custom.scss` still loads after the theme CSS, so sites with their own size rules look the same.

## [1.2.0] - 2026-11-04

### Added
- **Latest Posts Slider** for MetaSlider (free): `includes/latest-slider.php`, the `latest-slider` particle and the `[befree_latest_slider]` shortcode. One MetaSlider slideshow is kept in sync with the latest 20 published posts that have a featured image (newest first): featured image, title caption, link to the post. Rebuilt on publish, update, unpublish, delete and featured-image change. Hand-added slides are not touched. Filters: `befree_latest_slider_count`, `befree_latest_slider_settings`.
- **Wide container** (`_wide.scss`): add the CSS class `bf-wide` to a section (gear menu > CSS Classes) and its content grows to a centered 1600px container, fluid below that. Width is `--bf-wide-max` (default `1600px`). Sections without the class are unchanged.
- Full-width slider styles in `_slideshow.scss`: when the Slideshow section holds this slider it drops its padding and container width, the image covers a responsive band (`clamp()`), and the caption scales from phones to 4K.

### Notes
- Does nothing unless MetaSlider is active. Layout presets are unchanged; add the particle to the Slideshow section yourself.
- Style presets, the Sister Site particle, chart and TradingView rules are unchanged.

## [1.1.1] - 2026-11-04

### Fixed
- Preset switching follows the **Base Outline**. The shipped Home outline stores no colors, so it inherits the Base preset. Build refuses to package a child outline or `config/` path that contains style overrides.
- Theme CSS uses the BeFree variables (`--bf-bg`, `--bf-text`, `--bf-link`, `--bf-gold`, `--bf-navy`, `--bf-live`, plus the section tokens such as `--bf-main-bg` and `--bf-footer-text`) instead of hex values taken from one preset. Section bands, cards, the Sister Site particle, pagination and comment chrome follow those variables.
- Custom CSS saved through a filter that encoded `>` as `&gt;` is decoded in `custom/scss` and `custom/css` before Gantry compiles it, then written back raw. The compiler is `\BeFree\Gantry\ScssCompiler`, which only adds that decode step.

### Changed
- Recommended Gantry framework version is **5.6.5**. The minimum stays 5.5.

### Notes
- All six style presets, every layout preset, the Slideshow section, the Sister Site particle, and the single TradingView copyright-link rule are unchanged.
- Outlines already saved under `custom/` are not rewritten. A child outline that has its own Styles colors keeps them until those overrides are cleared. That is Gantry's normal per-outline behavior.
- No compatibility alias is shipped. In 1.1.0 the folder, text domain and SCSS names were already `befree-gantry`, and nothing in the theme still loaded another theme id.

### Upstream (Gantry 5.6.5)
Checked the WordPress.org plugin changelog for **5.6.5** (changelog date 15 October 2026, published 19 October 2026). GitHub tags on `gantry/gantry5` still stop at 5.6.0, and gantry.org/downloads was still listing the 5.6.4 packages on 4 November 2026. The 5.6.5 changes are in the framework plugin. This theme's templates and SCSS do not need a matching fork, and the runtime floor stays Gantry 5.5.

- **Security:** an unauthenticated particle AJAX request with an invalid outline could show the detailed debug error page (environment, cookie, session and POST data). 5.6.5 limits that page to debug mode or administrators, validates the outline, and masks secrets. Patchstack records this for versions through 5.6.4 as CVE-2026-110889.
- **Security:** invalid particle AJAX requests return HTTP 404 with a JSON content type. Logged-out visitors do not get the detailed error page, including when debug mode is on.
- jQuery, jQuery UI, Bootstrap 2–5 and MooTools are bundled instead of loaded from a CDN.
- The admin changelog is read from the bundled readme, not a remote URL.
- The file picker uses `WP_Filesystem` for permissions.

## [1.1.0] - 2026-11-03

### Added
- A **Slideshow** section directly under Navigation and above the page body. It is an empty section in the Default, Left Sidebar, Both Sidebars, Full Width, Magazine Home, Home and Error layout presets, so it shows up in the Gantry Layout Manager. Layout is Fullwidth (Flushed Content). Styling matches the other BeFree sections, slider markup stays within the viewport on small screens, and the section is not rendered when nothing is assigned.
- **Bloom**, a light style preset in the popular violet / rose / amber palette (bright accents on a light ground). Every checked text and background pair meets WCAG AA. The lowest pair is 5.98:1.

### Removed
- **Cyan Night** (the old preset4). It was the most redundant dark preset: the same lime-and-cyan accents as Meld Neon, with cyan leading. The preset4 id is kept, so an outline that points at preset4 still resolves. Colors already saved on an outline are not rewritten. Light Paper is unchanged.

### Changed
- Theme author is Intense Finance (https://if.finance) in the WordPress theme header, the Gantry About details, and the PHP file headers. The original Hydrogen copyright lines stay.

### Notes
- Existing layout particles are untouched, including the homepage hero, sidebars, Sister Site block and `system-content` (where the stock charts live). An empty Slideshow section produces no markup. Outlines already saved in `custom/` are not edited by the theme update.

### Upstream (Gantry 5.6.4)
Checked the official release at that time, **Gantry 5.6.4** (3 September 2026), and the WordPress Hydrogen theme zip from that release (`wordpress-tpl_g5_hydrogen_v5.6.4.zip`). BeFree was already built from Hydrogen 5.6.4. After the rename, the shared PHP templates, Twig views, blueprints, and SCSS match that zip except for BeFree's own palette, layouts, Slideshow section, and particles. Those BeFree changes stay. Light Paper and the chart rules were not edited in this pass.

The warning to put custom code in `custom/functions.php` matches the current Gantry 5 theme text. The runtime floor stays Gantry 5.5. The private RocketTheme updater block is still not included.

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
