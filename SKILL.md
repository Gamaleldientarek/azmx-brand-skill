---
name: azmx-brand
description: Apply the official AZMX brand identity to any deliverable. Use whenever work involves AZMX branding, AZMX presentations, proposals, emails, newsletters, reports, social graphics, web pages, documents, or copywriting in the AZMX voice, or when the user mentions AZMX colors, the chevron, Dark Navy, Electric blue, thmanyah serif, or Azm X fonts. Provides the full color palette, typography rules, logo files, web fonts, the email design system, and the voice and tone guide.
---

# AZMX Brand Skill

AZMX is a Saudi UX and innovation design studio. This skill encodes its official brand system so every deliverable comes out on-brand without re-briefing.

One-line ethos: deep navy, electric blue, generous white space, serif personality, the chevron as the only recurring graphic device. **Restraint is the luxury.**

For the complete handbook (component specs, slide archetypes, Figma implementation), read `references/design-system.md`. For every color tone, read `references/colors.md`. For the exact live Figma variables (all 233: colors with dark mode, fonts, type scale, spacing, radii, opacity), read `references/figma-tokens.md`. For any HTML email or newsletter, read `references/email-design-system.md` and start from `assets/templates/email-starter-skeleton.html`. For any written copy, follow `references/voice-and-tone.md`. When a deliverable needs imagery, pick from the 222 brand images catalogued in `references/image-library.md` (selection and colour-pairing rules) and `references/image-index.md` (every file with its dominant colour, safe text colour, and direct download link).

Images are dark surfaces. 221 of the 222 measure below 0.18 luminance, so text over them follows the Navy row of the text-colour table: White title, Blue 100 body, Light Blue eyebrow. Never Electric for text on an image; Electric appears over imagery only as a chevron tick or a single active rule. The White section is the one exception, taking Navy text with Electric accents.

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

The rightward chevron is the only graphic device, and it is **functional, never background decoration**. Sanctioned uses: photo mask, stacked-in-motion hero trio (foreground compositional art), section tick, and list bullet. One big chevron gesture per surface, always pointing in the reading direction. No icon packs, no clip art, no 3D blobs, no glows, no drop-shadow cards.

**Banned (owner decision, 2026-07-20): chevrons as backgrounds.** No oversized ghost chevrons bleeding off corners, no navy-on-navy or low-opacity chevron field textures, no concentric chevron arc backdrops, no chevron art placed behind or under content. Backgrounds stay clean: solid surface, gradient (event surfaces only), and nothing else. If a layout feels empty without a background device, the answer is negative space, not a chevron.

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
| Image library | `assets/images/` | 222 AZMX brand images in 8 sections. Default to `gradient/` and `blue/`; see `references/image-library.md` |
| Email skeleton | `assets/templates/email-starter-skeleton.html` | Blank ready-to-fill AZMX email, default blue theme |
| Email components | `assets/templates/email-component-showcase.html` | Every email component rendered once, copy-paste markup |

Logos are optically centered, never bounding-box centered, and never cross the 100 px safe area. On dark surfaces use the White variant, on light use Navy Dark or Colored.

## Use the image library

Any visual deliverable that needs imagery **uses this library** rather than generic stock, a placeholder, a flat colour block, or a newly generated image. 222 images ship with the skill; there is almost always a fit.

**How to reference them, by deliverable type:**

- **HTML, email, or web page**: use the public URL so the file works for anyone who opens it —
  `https://raw.githubusercontent.com/Gamaleldientarek/azmx-brand-skill/main/assets/images/blue/blue-014.jpg`
  Local relative paths only when the deliverable ships alongside the skill folder.
- **Word, PowerPoint, PDF, or any document build**: embed the local file from `assets/images/<section>/`.
- **Figma**: upload the local file as an image fill, and prefer the chevron photo mask over a plain rectangle.
- **Anything the user will hand-edit later**: give them the filename and the gallery link, https://gamaleldientarek.github.io/azmx-brand-skill/

**Picking one:**

1. Default to `blue/` for general surfaces and `gradient/` for covers, dividers, and closings.
2. Check `references/image-index.md` for the image's dominant colour and safe text colour before laying type over it.
3. When several images fit, name two or three candidates and let the user choose. Do not silently pick, exactly as with colour tokens.
4. Never invent or download outside imagery for an AZMX deliverable without saying so first. If nothing in the library fits, say that plainly and ask before sourcing elsewhere.

Images are dark surfaces: White titles, Blue 100 body, Light Blue eyebrows, and Electric only as a chevron tick or single rule. The `white/` section is the exception, taking Navy text with Electric accents.

## Ask before you color

Before applying any accent or fill color, confirm the token with the user. Ask a direct question such as:

> "Which color token should I use here: Primary Electric `#001AFF`, or another token from the palette (Light Blue, Dark Navy, a Blue-ramp step, a neutral)?"

Rules for this step:

- Never silently pick an accent color when more than one token could fit. One short question, then proceed.
- If the user names a token that is not in `references/colors.md`, ask them to share its hex value. Use the value they give, and offer to add it to `references/colors.md` so the palette stays the single source of truth.
- Skip the question only when the choice is already forced by the system (for example: body text on white is always Neutral 900, text on navy is always White / Blue 100, RAG dots are always Red / Yellow / Green).

## Workflow

1. Identify the surface (navy, white, blue-50, or gradient) and apply its text colors from `references/colors.md`.
2. Confirm the accent color token with the user (see "Ask before you color" above).
3. Load the two font families from `assets/fonts.css` for any HTML/web deliverable, or embed the TTF/OTF files for documents.
4. If the deliverable needs imagery, pick from the image library (see "Use the image library" above). Never substitute generic stock or a placeholder.
5. Place the correct logo variant for the surface.
6. Apply one chevron gesture maximum, pointing right.
7. For emails and newsletters: follow `references/email-design-system.md` (Arabic RTL rules are non-negotiable) and build from the email skeleton template.
8. For all written copy: apply `references/voice-and-tone.md`, including its no-AI-tells mechanics.
9. Check the guardrails table above before delivering. When in doubt, remove decoration. Restraint is the luxury.
