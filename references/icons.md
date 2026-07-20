# AZMX Icons

**Library: [Phosphor Icons](https://phosphoricons.com)** — MIT licensed, free for client work, no attribution required. 9,000+ icons, every one available in six weights.

Phosphor was chosen because it is the only major open library where weight is consistent across the entire set. AZMX's voice runs on weight contrast (serif against sans, Light through Black), so icons can follow the same discipline as the type instead of sitting at one fixed stroke.

## Where icons are allowed

This is the important part, because the design system otherwise treats icon packs as an AI tell and names the chevron as the only recurring graphic device. Both remain true.

| Context | Icons | Reason |
|---|---|---|
| Product UI, app screens, dashboards, data tables, forms | **Allowed** | Function needs affordances that type alone cannot carry |
| Web page utility (navigation, download, external link, copy, close) | **Allowed** | Same reason, kept minimal |
| Decks, covers, dividers, closings, reports, brand editorial surfaces | **Never** | The chevron is the only device here. An icon row on a slide is the AI tell the system exists to prevent |
| Emails | **Rarely** | Only functional (calendar, location, link). Never decorative bullets — the chevron bullet is the system's bullet |

Icons never replace the chevron. The chevron remains the list bullet, the section tick, the photo mask, and the page-number flow tick everywhere.

## Locked usage

Pick once per deliverable and do not mix:

- **Weight: Regular** for UI at default. `Light` is permitted on dark surfaces where Regular reads heavy; `Bold` only for a single emphasis moment. Never Fill or Duotone — they fight the flat, hairline character of the system.
- **Size: 20 px** for inline UI controls, **24 px** standalone, **32 px** for a feature anchor. All are on the 8 px grid.
- **Stroke** should read at the same visual weight as the system's 1 px hairlines. Do not scale an icon up and leave a hairline stroke looking thin beside it.

## Colour by surface

| Surface | Icon colour | Notes |
|---|---|---|
| White or Blue 50 | Neutral 900 `#111927` | Electric `#001AFF` only for the single active or primary icon |
| Navy, gradient, or a library image | White `#FFFFFF` | Light Blue `#5D8FFF` for secondary or inactive. Never Electric — it fails contrast on dark |

One accent icon per surface at most. The same restraint that governs Electric text governs Electric icons.

## Pairing with labels

Prefer icon plus label. A standalone icon is only acceptable for universally understood controls (close, back, download, external link), and it must still carry an `aria-label`. An icon-only button with no accessible name is an accessibility failure, not a style choice.

## Implementation

Web, no build step:

```html
<script src="https://unpkg.com/@phosphor-icons/web"></script>
<i class="ph ph-arrow-right" style="font-size:20px;color:var(--azmx-electric)"></i>
```

React:

```bash
npm install @phosphor-icons/react
```

```jsx
import { ArrowRight } from "@phosphor-icons/react";
<ArrowRight size={20} weight="regular" color="#111927" />
```

For decks, documents, and Figma, download the individual SVG from phosphoricons.com and set its stroke to the surface colour above rather than importing the whole set.
