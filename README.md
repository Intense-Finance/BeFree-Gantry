# BeFree Gantry

Made by Intense Finance (https://if.finance)

A dark, industrial **Gantry 5** theme for WordPress. It blends the **BeFree** look (navy, gold, Barlow Condensed, chamfered "industrial" cards) with the **if.finance** neon palette (lime "live" accents and cyan links).

* Version: **1.1.1**
* Requires: WordPress 6.0+ and the free **[Gantry 5 Framework](https://gantry.org/) plugin**
* Gantry 5 framework: **minimum 5.5**, **recommended 5.6.5** (WordPress.org plugin, 19 October 2026). See [Gantry 5.6.5](#gantry-565).
* PHP: **8.1+** with Gantry 5.5.25 and 5.6.x (the 5.6.5 plugin declares `Requires PHP: 8.1.0`). Gantry 5.5.0 itself allowed PHP 5.6.20.
* License: **GNU GPL v3 or later** (see [License](#license))
* Read the launch story on if.finance: [BeFree Gantry: a dark, industrial WordPress theme](https://if.finance/befree-gantry-wordpress-theme/)

![BeFree Gantry: meld home, desktop](docs/previews/meld-home-desktop.png)

| Article | Mobile (390 px) | Industrial variant |
|---|---|---|
| ![Article](docs/previews/meld-article.png) | ![Mobile](docs/previews/meld-home-mobile-390.png) | ![Industrial](docs/previews/meld-industrial-variant.png) |

---

## Install

1. Install and activate the **Gantry 5 Framework** plugin, recommended version **5.6.5**. Update it from **Plugins** in WordPress, or install it from [wordpress.org/plugins/gantry5](https://wordpress.org/plugins/gantry5/). The theme also runs on Gantry 5.5 or newer. BeFree Gantry does not work without the plugin, and it does not bundle Nucleus.
2. Download `befree-gantry-1.1.1.zip` from the GitHub release and check its SHA-256 against `befree-gantry-1.1.1.zip.sha256`.
3. In WordPress, go to **Appearance > Themes > Add New > Upload Theme**, pick the zip, then click **Install Now** and **Activate**.
4. Open **Gantry 5 > BeFree Gantry** to choose a style preset, layout and particles.
5. Optional: assign your menu in **Gantry 5 > Menu** or in the Menu particle, and add widgets to the `slideshow`, `sidebar`, `aside`, `feature-1/2/3`, `subfeature` and `footer` positions.

Updates are manual. Upload the new zip and WordPress will offer to replace the theme. Your Gantry settings live in `wp-content/themes/befree-gantry/custom/` and are kept. This theme does not call home or use an update server.

## Style presets

Pick a preset in **Gantry 5 > Styles > Presets**. Every text and background pair passes WCAG AA (at least 4.5:1). The check is in [`tools/palettes.py`](tools/palettes.py).

| Preset | Thumbnail | Look | Lowest contrast |
|---|---|---|---|
| **Meld Neon** (default) | ![](docs/previews/presets/meld-neon.png) | if.finance lime and cyan on BeFree dark industrial | 5.69:1 |
| **Industrial** | ![](docs/previews/presets/industrial.png) | Hazard stripes, blueprint grid, chamfered cards, gold-plate titles, grayscale images | 5.69:1 |
| **BeFree Navy** | ![](docs/previews/presets/befree-navy.png) | BeFree's own navy and gold | 6.69:1 |
| **Bloom** | ![](docs/previews/presets/bloom.png) | Violet, rose and amber on a bright ground | 5.98:1 |
| **Lime Terminal** | ![](docs/previews/presets/lime-terminal.png) | Lime leads on near-black, terminal style | 6.97:1 |
| **Light Paper** | ![](docs/previews/presets/light-paper.png) | Light surfaces on BeFree paper `#e7eef6`, with a navy nav and footer | 5.57:1 |

## Switching styles

Presets are chosen on the **Base Outline**. The Home outline shipped with this theme does not store colors of its own, so pages that use it inherit that preset. Do not copy color values into a child outline: a color saved there overrides Base.

1. Open **Gantry 5 > Styles** on the **Base Outline**, pick a preset and save.
2. If a page still shows the old colors, recompile the CSS (**Gantry 5 > Recompile/clear cache**) and then purge the LiteSpeed (or other page) cache.
3. Save custom CSS raw so `>` is not encoded.

Theme rules use the BeFree variables, for example `var(--bf-bg)`, `var(--bf-text)`, `var(--bf-link)`, `var(--bf-gold)`, `var(--bf-navy)` and `var(--bf-live)`. Use those in custom CSS instead of a preset's hex colors, and do not add `!important` to a hardcoded palette. If a filter saved `&gt;` in place of `>`, the selector matches nothing. On compile, the theme decodes `&gt;`, `&lt;`, `&amp;` and `&quot;` in `custom/scss` and `custom/css` and writes the raw file back. An outline that still has its own checked Styles colors keeps them until those overrides are cleared and the outline is saved.

### Styles > BeFree Meld

Each preset fills a new **BeFree Meld** style section. You can also edit it directly:

| Setting | Purpose |
|---|---|
| Look | `Standard`, `Industrial` (hazard stripe, blueprint grid, chamfers, `.bf-stamp`) or `Light` |
| Card Radius | Corner radius for cards and panels (14px by default, 0px for Industrial) |
| Gold / Gold Text / Gold Button Text | Primary button, rules and eyebrow text. Keep Gold Text at 4.5:1 or better on Card |
| Card / Raised / Line | Card surface, image wells and borders |
| Muted / Navy / Paper / Ink | Secondary text, navy panels (blockquotes, `bf-navy`), nav labels and dark ink |

The standard Gantry sections (Base, Accent, Header, Navigation, Slideshow, Showcase, Feature, Main, Subfeature, Footer, Off-Canvas) still work as in Hydrogen. **Accent 1** is the lime "live" color and **Accent 2** is the cyan link color, except in Bloom, where Accent 1 is violet and Accent 2 is rose. Light Paper is unchanged.

## Layout presets

Pick one in **Gantry 5 > Layout > Load**:

| Layout | Thumbnail | Structure |
|---|---|---|
| **Default** | ![](docs/previews/layouts/befree-right-sidebar.png) | Main (70%) and right sidebar (30%) with the Sister Site block |
| **Left Sidebar** | ![](docs/previews/layouts/befree-left-sidebar.png) | Sidebar (30%) and main (70%) |
| **Both Sidebars** | ![](docs/previews/layouts/befree-both-sidebars.png) | 22% / 56% / 22%, with the Sister Site block in the aside |
| **Full Width** | ![](docs/previews/layouts/befree-full-width.png) | No sidebar. Sister Site in the subfeature row |
| **Magazine Home** | ![](docs/previews/layouts/befree-magazine.png) | Showcase hero, 3-up feature grid (`feature-1..3`), main and sidebar, then subfeature. Used by the *Home* outline |
| **Offline** | ![](docs/previews/layouts/befree-offline.png) | Maintenance / offline page |
| **Error** | ![](docs/previews/layouts/befree-error.png) | 404 / error page |

Every content layout above includes an empty **Slideshow** row directly under Navigation. Offline and body-only do not. With nothing in the row, Gantry draws no markup, so a page looks the same as before.

## Slideshow

The section sits directly under the navigation and above the body. BeFree's header is the logo bar, so the slider is its own section and is not part of the header.

It is empty until you drop something in it. The section setting **Layout** is **Fullwidth (Flushed Content)** (`boxed: 2`), which is edge to edge, with no content padding. The gear menu on the section can switch that to **Fullwidth (Boxed Content)** if the slider should sit in the page column. Colors are under **Styles > Slideshow**. An outline saved before 1.1.0 has no Slideshow colors of its own; the band then uses that outline's Main colors.

**Latest Posts Slider (new in 1.2.0).** With the free [MetaSlider](https://wordpress.org/plugins/ml-slider/) plugin active, drag the **Latest Posts Slider** particle into the Slideshow section (or use the shortcode `[befree_latest_slider]` anywhere). On first view the theme creates one MetaSlider slideshow, **BeFree Latest Posts**, with one slide per post for the latest 20 published posts that have a featured image, newest first. Each slide shows the featured image, the post title as caption, and links to the post. The slides rebuild automatically when a post is published, updated, unpublished or deleted, or its featured image changes. Slides you add to that slideshow by hand are kept. It runs edge to edge at every width (360px phones to 3840px 4K): the image covers the band (2.4:1 on desktop, capped at 1600px tall; taller on phones), and the caption scales with the viewport. Colors use `--bf-slideshow-bg` and `--bf-gold`. Change the count with the `befree_latest_slider_count` filter and the MetaSlider settings with `befree_latest_slider_settings`. Without MetaSlider the particle prints nothing.

**Homepage only, wide story area.** Put the Latest Posts Slider particle in the **Home** outline (assigned to the front page) and leave Base's Slideshow empty; other pages then use Base with no slider. To widen the content below the slider to 1600px, add `bf-wide` under CSS Classes on the Home outline's Showcase, Feature, Main container and Subfeature sections. Change the width with `--bf-wide-max`.

**MetaSlider widget.** In **Gantry 5 > Layout**, open the Slideshow section and drag in a **Widget Block** particle. Set **Block Key** to `slideshow` (any key made of letters, numbers and hyphens works; `slideshow` matches the section). In **Appearance > Widgets**, or the block widget editor, add the MetaSlider widget to that block. The single **Widget** particle still works if you pick one MetaSlider widget, but WordPress 5.8+ marks it deprecated in favor of Widget Block.

**MetaSlider shortcode.** Drag a **Custom HTML** particle into Slideshow. Paste the shortcode MetaSlider gives you, for example `[metaslider id="123"]`. Enable **Process shortcodes**. Leave **Process Twig** off unless the HTML uses Twig.

Widget chrome (card fill, padding, and the Industrial chamfer) is turned off inside `#g-slideshow` only, so the slider can run full width. Sidebar, feature and main widgets are styled as before. Chart embeds live in the main content and are not targeted.

On an outline you have already saved, the theme update does not rewrite `custom/config/`. That is what keeps the homepage charts and the rest of a saved layout in place. Do not use **Layout > Load** on that outline: Load replaces the whole layout. To add the section by hand, edit `custom/config/<outline>/layout.yaml` and insert this directly under `/navigation/`:

```yaml
  /slideshow/: { }
```

And under `structure:`:

```yaml
  slideshow:
    type: section
    attributes:
      boxed: 2
```

Open **Gantry 5 > Layout** again and drop the particle in. If the section is still empty, or the widget block has no widgets, the front end skips it.

## Sister Site particle

Add **Sister Site** from the particle list, or use the copy already in the Default, Both Sidebars and Full Width layouts.

![Sister Site block](docs/previews/sister-block.png)

Fields: enabled, eyebrow, left/right pair labels, title and accented title part, URL and URL label, text, buttons (text, link, style `gold`/`ghost`/`neon`, target `_self`/`_blank`), note, hazard stripe on/off, and CSS class. All output is escaped. Links are plain `<a>` tags with no tracking, scripts or redirects, and `_blank` links get `rel="noopener noreferrer"`. The defaults point to `https://slopcore.army/` and `https://if.finance/slopcore/`, and you can change them in the particle settings.

## Fonts

**Barlow Condensed** (headings: 500, 600, 700) and **Outfit** (body: variable 400 to 600) ship as local **WOFF2** files in `befree-gantry/fonts/`. They are licensed under the [SIL Open Font License 1.1](befree-gantry/fonts/OFL.txt). The site makes no request to Google.

To load them from Google Fonts instead, open **Styles > Base** and pick *Barlow Condensed* and *Outfit* from the Google section of the Gantry font picker.

WOFF2 works in every current browser. No EOT, TTF or SVG fallbacks are included.

## Charts and TradingView widgets

Chart embeds are left as they are. The **only** CSS rule that touches them recolors the `.tradingview-widget-copyright` link to the footer text color (the live accent on hover). Custom HTML and Block widgets, where charts usually live, get no added padding, clipping or chamfers, so chart widths and heights stay as embedded.

## Gantry 5.6.5

Recommended framework version is **5.6.5** for WordPress. It was published to the [WordPress.org plugin directory](https://wordpress.org/plugins/gantry5/) on 19 October 2026 (changelog date 15 October 2026). The [gantry/gantry5](https://github.com/gantry/gantry5) GitHub tags still stop at 5.6.0, and [gantry.org/downloads](https://gantry.org/downloads) was still offering the 5.6.4 packages when this theme was checked on 4 November 2026. Install or update the plugin from WordPress itself.

5.6.5 is compatible with this theme. The changes are in the framework plugin, not in theme templates or SCSS. The theme floor stays Gantry 5.5. The plugin still requires PHP 8.1.0 and lists WordPress tested up to 7.1.4.

From the WordPress.org changelog for 5.6.5:

* **Security.** An unauthenticated particle AJAX request with an invalid outline could show the detailed debug error page, including environment, cookie, session and POST data. The debug page is now limited to debug mode or administrators, the handler checks the outline, and secret values are masked. Patchstack records this as CVE-2026-110889 for versions through 5.6.4.
* **Security.** Invalid particle AJAX requests return HTTP 404 with a JSON content type. Detailed error pages are not shown to logged-out visitors, including when debug mode is on.
* jQuery, jQuery UI, Bootstrap 2–5 and MooTools are bundled instead of loaded from third-party CDNs.
* The admin changelog is read from the bundled readme instead of a remote URL.
* The file picker uses `WP_Filesystem` when it sets permissions.

## Local test (1.0.0, presets updated in 1.1.0)

These were rendered on WordPress (latest, SQLite integration), Gantry 5.6.4 and PHP 8.3, with the theme activated and Gantry SCSS compiled live. The sample images are test-only and are not shipped in the theme. Bloom replaced Cyan Night in 1.1.0, so its cell is the preset thumbnail rather than a new WordPress capture. The other captures still match: Slideshow is empty and is not drawn, and the homepage charts stay in the main content.

| Meld Neon home | Industrial home | Light Paper single |
|---|---|---|
| ![](docs/previews/wp-test/wp-home-meld-neon-1440.png) | ![](docs/previews/wp-test/wp-home-industrial-1440.png) | ![](docs/previews/wp-test/wp-single-light-paper-1440.png) |
| **BeFree Navy** | **Bloom** (preset thumbnail) | **Lime Terminal** |
| ![](docs/previews/wp-test/wp-home-befree-navy-1440.png) | ![](docs/previews/presets/bloom.png) | ![](docs/previews/wp-test/wp-home-lime-terminal-1440.png) |
| **Layout: Left Sidebar** | **Layout: Both Sidebars** | **Layout: Full Width** |
| ![](docs/previews/wp-test/wp-layout-left_sidebar-1440.png) | ![](docs/previews/wp-test/wp-layout-both_sidebars-1440.png) | ![](docs/previews/wp-test/wp-layout-full_width-1440.png) |
| **Mobile 390 px** | **Layout: Default** | **404** |
| ![](docs/previews/wp-test/wp-home-meld-neon-390.png) | ![](docs/previews/wp-test/wp-layout-default-1440.png) | ![](docs/previews/wp-test/wp-404-error-1440.png) |

## Screenshots

BeFree Gantry 1.2.1 with the BeFree Navy style, on the [iw.je](https://iw.je) test site.

| **Home, desktop 1440 px** | **Menu dropdown** |
| --- | --- |
| ![Home page, desktop 1440 px](docs/previews/screenshots/home-desktop-1440.jpg) | ![Menu dropdown, 1440 px](docs/previews/screenshots/menu-dropdown-1440.jpg) |
| **Single post** | **Full home page** |
| ![Single post, 1440 px](docs/previews/screenshots/single-post-1440.jpg) | ![Full home page](docs/previews/screenshots/home-full-1920.jpg) |
| **Mobile 390 px** | **Mobile menu** |
| ![Mobile, 390 px](docs/previews/screenshots/mobile-390.jpg) | ![Mobile menu open, 390 px](docs/previews/screenshots/mobile-390-menu.jpg) |

## Repository layout

```
befree-gantry/     the installable theme (zip this folder)
  gantry/          theme.yaml, presets.yaml
  blueprints/      style and particle settings (styles/befree.yaml = BeFree Meld, styles/slideshow.yaml = Slideshow)
  layouts/         layout presets (Slideshow under Navigation)
  particles/       sister-site particle (.yaml + .html.twig)
  scss/            befree-gantry.scss, befree-gantry/_meld.scss, _sister.scss
  fonts/           Barlow Condensed + Outfit WOFF2, OFL.txt
docs/previews/     screenshots and thumbnails used in this README
tools/             build.sh (zip + sha256), palettes.py (WCAG check),
                   gen_presets.py, make_thumbs.py, wp_test.sh (local test helper)
```

To build, run `tools/build.sh`. It writes `dist/befree-gantry-<version>.zip` and a `.sha256` file.

## Credits

* **Gantry 5 Hydrogen** theme, Copyright (C) 2007 - 2022 Tiger12, LLC (originally created by RocketTheme, LLC). GNU GPL v2 or later. BeFree Gantry is a modified version of it.
* **Gantry 5 Framework**, Copyright (C) Tiger12, LLC / RocketTheme, LLC. MIT / GNU GPL v2 or later. It is a separate plugin and is not bundled.
* **Barlow Condensed**, Copyright 2017 The Barlow Project Authors. SIL OFL 1.1.
* **Outfit**, Copyright 2021 The Outfit Project Authors. SIL OFL 1.1.
* The BeFree palette and industrial styling were reimplemented from Intense Finance's own BeFree design. The if.finance neon palette is Intense Finance's own.
* No paid or "Pro" RocketTheme code is used.

## License

Copyright (C) 2026 Intense Finance. It is based on Hydrogen, Copyright (C) 2007 - 2022 Tiger12, LLC.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either **version 3** of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. The full text is in [LICENSE](LICENSE).

Hydrogen is licensed "GPL v2 or later", which allows this version to be distributed under GPL v3 or later. The bundled fonts stay under the SIL Open Font License 1.1 ([`fonts/OFL.txt`](befree-gantry/fonts/OFL.txt)).
