# Changelog

All notable changes to the AZMX Brand Skill.

---

## v1.3.0 — 2026-07-22

**Icons: ask, never assume.** Owner decision. The previous rule banned icons outright on decks, covers, dividers, closings, and reports, permitting them in functional UI only. That was wrong — AZMX uses icons across decks, reports, and other deliverables. Icons are now permitted on **any** surface, and the agent must **ask the user before adding them**.

### Changed

- **`references/icons.md`** — "Where icons are allowed" replaced with **"Ask before you use icons"**, mirroring the existing "Ask before you color" rule. Icons are permitted everywhere; the agent asks once before placing the first one and never decides silently in either direction. The context table now reads Ask / Ask-default-yes rather than Never.
- **`SKILL.md`** — Icons section rewritten to the ask-first rule. The chevron section no longer says "no icon packs". The human-craft guardrail now names the actual tell — *scattered decorative icon rows standing in for content* — instead of "generic icons". New workflow step 7: ask about icons before placing any.
- **`references/design-system.md`** — the anti-pattern table and the deck decoration rule no longer ban icon packs; both defer to `icons.md`.
- **`references/pdf-forms.md`** — the form brand-rules section said "No icons", contradicting `icons.md`. Corrected to the ask-first rule, with guidance that icons on a form belong on functional instructions rather than field labels.

### What did not change

The discipline that keeps icons from reading as an AI tell is unchanged, and it was never the ban: one weight, one size step per surface, Regular (never Fill or Duotone), at most one Electric accent, icons paired with labels, and an `aria-label` on any standalone icon. **Icons still never replace the chevron** as bullet, section tick, photo mask, or page-number flow tick — they sit alongside it.

### Added

- **`scripts/build-pdf-form.mjs`** now supports dropdown fields: `"type": "select"` with an `options` array and an optional `default`. Validation rejects a `select` with no options, and a `default` that is not one of its own options. First used for the Account Currency field (SAR / USD / EUR / GBP) on the AZMX Bank Information Form.

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
