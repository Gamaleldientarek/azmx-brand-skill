# Changelog

All notable changes to the AZMX Brand Skill.

---

## v1.2.0 — 2026-07-22

**Designed PDF forms.** The skill now covers printed A4 documents and fillable PDF forms end to end, from Figma design through to stamped AcroForm fields. Validated on a real build: the AZMX Employee Information Form, 3 × A4, 99 form fields.

### Added

- **`references/pdf-forms.md`** — the full four-stage pipeline: design in Figma → export to PDF → stamp fields with pdf-lib → verify. Covers the A4 canvas spec, table construction, the `FIELD · ` naming convention, brand treatments for forms, both export routes, the coordinate transform, and a five-check verification table.
- **`scripts/build-pdf-form.mjs`** — parameterised field stamper. Places AcroForm text fields and checkboxes at exact coordinates, embeds Azm X for field text, and validates the spec before writing. Supports `--expect` (hard-fail on field-count drift), `--flatten`, `--font`, and `--size`.
- **`scripts/extract-figma-fields.js`** — pulls every `FIELD · ` rectangle out of a Figma design and emits the JSON spec, warning on duplicate ids, non-snake_case names, and off-spec frame sizes.
- **`scripts/package.json`** — declares `pdf-lib` and `@pdf-lib/fontkit`. Run `npm install` inside `scripts/` once before first use.

### Changed

- `SKILL.md` — frontmatter description now triggers on printed A4 documents and fillable PDF forms; the reference index points to `references/pdf-forms.md`.
- `.gitignore` — ignores `scripts/node_modules/` and `scripts/package-lock.json`.

### Findings worth keeping

- **Use 24 px form rows, not 32 px.** A 32 px row is the intuitive choice for Acrobat, but on a dense A4 form it overflowed all three pages (−254 / −166 / −90 px) and forced multi-column grids and paired sections that broke fidelity with the source document. At 24 px (≈ 8.5 mm, a standard field height) the faithful single-column layout fits with 18 / 54 / 55 px clearance. Row height is a cheaper lever than layout compression — reach for it first.
- **Design A4 at 595 × 842 px.** That maps 1:1 onto A4 in PDF points, so Figma coordinates become PDF coordinates with no scale factor anywhere in the pipeline.
- **Acrobat's "Prepare Form" auto-detect is never needed.** The designer already knows every field rectangle, so fields are placed deterministically with readable names instead of `Text1…Text47`.
- **`setFontSize()` must follow `addToPage()`** in pdf-lib, or it throws `No /DA (default appearance) entry found`. This is the most likely error in the pipeline.
- **Node resolves bare imports from the importing file**, so `scripts/` needs its own `node_modules`; installing pdf-lib in your working project is not enough.

---

## v1.1 — 2026-07-20

### Changed

- **Chevrons banned as backgrounds** (owner decision). No oversized ghost chevrons bleeding off corners, no navy-on-navy or low-opacity chevron field textures, no concentric chevron arc backdrops, no chevron art behind content. Backgrounds stay clean: solid surface, or gradient on event surfaces only. Where a layout feels empty, the answer is negative space.
- `references/icons.md` added — the Phosphor icon system, with icons confined to functional UI and kept off editorial brand surfaces.

---

## v1.0 — 2026-07-20

Initial release. Colour palette and ramps, typography rules, the chevron system, layout essentials, logo variants, Azm X and thmanyah serif display font files, the email design system, the voice and tone guide, and the 242-image brand library with its index and recolour prompts.
