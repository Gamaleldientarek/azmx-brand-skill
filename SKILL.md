---
name: azmx-brand
description: Apply the official AZMX brand identity to any deliverable. Use whenever work involves AZMX branding, AZMX presentations, proposals, emails, reports, social graphics, web pages, or documents, or when the user mentions AZMX colors, the chevron, Dark Navy, Electric blue, thmanyah serif, or Azm X fonts. Provides the full color palette, typography rules, logo files, and web fonts.
---

# AZMX Brand Skill

AZMX is a Saudi UX and innovation design studio. This skill encodes its official brand system so every deliverable comes out on-brand without re-briefing.

One-line ethos: deep navy, electric blue, generous white space, serif personality, the chevron as the only recurring graphic device. **Restraint is the luxury.**

For the complete handbook (component specs, slide archetypes, Figma implementation), read `references/design-system.md`. For every color tone, read `references/colors.md`.

## Core palette

| Token | Hex | Role |
|---|---|---|
| Electric | `#001AFF` | Hero accent. Use like punctuation: sparse, decisive. Never a large fill behind text. |
| Dark Navy | `#040038` | The premium dark surface. |
| Light Blue | `#5D8FFF` | The accent partner on dark surfaces. Safe for large soft fills. |
| White | `#FFFFFF` | Default editorial light surface, and text on dark. |
| Blue 50 | `#F0F5FF` | Quiet secondary light surface, table zebra, panels. |
| Neutral 900 | `#111927` | Body text on light. |

The two blues have strict roles. Electric is the call-to-attention on light surfaces: eyebrows, key numerals, the one highlighted word. Light Blue plays that role on navy, where Electric fails contrast at small sizes. Never swap them.

Gradient (event surfaces only: covers, dividers, closings): linear 145 degrees, `#040038` to `#001AFF`, mid-stop `#01006E` at 55 percent. Never behind dense body copy.

Red `#FF2B3C`, Yellow `#FED340`, Green `#22C36F` exist only for semantic RAG data dots. No other secondary color appears on brand surfaces.

## Typography

Two families carry the entire voice. Font files ship in `assets/fonts/`, ready-made CSS in `assets/fonts.css`.

- **thmanyah serif display**: titles, stats, quotes, brand numerals. Weights: Light, Regular, Medium, Bold, Black. It has no italic; express emphasis through scale, weight, and color only.
- **Azm X Variable** (sans, supports English and Arabic): body, labels, tables, UI. Weights: Thin, ExtraLight, Light, Regular, Medium, SemiBold, Bold, Heavy.

Rules: serif carries personality, sans carries information. Never set body copy in serif, never set a hero in sans. Eyebrows are Azm X SemiBold, UPPERCASE, tracked wide. Stat numerals pair a serif figure with a sans Medium suffix on one baseline.

## The chevron

The rightward chevron is the only graphic device. Sanctioned uses: photo mask, oversized corner bleed, stacked-in-motion trio, concentric arcs, section tick, and list bullet. One big chevron gesture per surface, always pointing in the reading direction. No icon packs, no clip art, no 3D blobs, no glows, no drop-shadow cards.

## Layout essentials

- 8 px baseline grid. Spacing scale, the only permitted values: 8, 16, 24, 40, 64, 96, 128, 160.
- Left-aligned, top-weighted, asymmetric by default. Only closings are centered.
- Decoration is exactly three things: chevron, gradient, hairline (1 px rules).
- One deliberate grid-break per surface signals human craft.
- Presentation canvas: 1920 x 1080, margins 120 left/right, safe area 100 px, body measure 6 to 7 columns max.

## Human-craft guardrails

These read as AI or template tells; never do them: rounded-corner cards with drop shadows everywhere, centered everything, equal-length padded columns, plain numerals in default sans, generic icons, Electric as a large text background, gradients behind paragraphs, uniform 16 px spacing everywhere, scattered chevrons.

## Assets

| Asset | Path | Use |
|---|---|---|
| Logo, colored | `assets/logo/azmx-logo-colored.svg` | Default on white |
| Logo, navy dark | `assets/logo/azmx-logo-navy-dark.svg` | Monochrome on light surfaces |
| Logo, white | `assets/logo/azmx-logo-white.svg` | On navy or gradient |
| Favicon | `assets/logo/azmx-favicon.png` | Browser-tab icon for any AZMX web deliverable: the white chevron on Electric, 100 x 100 px |
| Azm X fonts | `assets/fonts/azmx/*.ttf` | Sans, EN + AR |
| thmanyah fonts | `assets/fonts/thmanyah/*.woff2` (web), `*.otf` (desktop) | Serif display |
| Font-face CSS | `assets/fonts.css` | Drop into any HTML deliverable |

Logos are optically centered, never bounding-box centered, and never cross the 100 px safe area. On dark surfaces use the White variant, on light use Navy Dark or Colored.

## Workflow

1. Identify the surface (navy, white, blue-50, or gradient) and apply its text colors from `references/colors.md`.
2. Load the two font families from `assets/fonts.css` for any HTML/web deliverable, or embed the TTF/OTF files for documents.
3. Place the correct logo variant for the surface.
4. Apply one chevron gesture maximum, pointing right.
5. Check the guardrails table above before delivering. When in doubt, remove decoration. Restraint is the luxury.
