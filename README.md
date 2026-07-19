# AZMX Brand Skill

The official AZMX brand system, packaged as an Agent Skill for Claude Code and other AI agents. Install it once and every deliverable (decks, emails, reports, web pages, social graphics, documents) comes out in the AZMX identity without re-briefing the agent.

Deep navy, electric blue, generous white space, serif personality, the chevron as the only graphic device. Restraint is the luxury.

## What's inside

- `SKILL.md`: the condensed brand rules the agent loads automatically
- `references/design-system.md`: the full AZMX Design System handbook (v1.1: chevrons banned as backgrounds)
- `references/colors.md`: every color tone (primary, blue ramp 50 to 1000, neutrals, RAG, surfaces, text-by-surface)
- `references/email-design-system.md`: the AZMX Email Design System v1 (RTL rules, 3-layer fonts, themes, components)
- `references/voice-and-tone.md`: how AZMX sounds, EN and AR, plus the no-AI-tells writing mechanics
- `assets/templates/`: ready-to-fill email skeleton and the full email component showcase
- `assets/logo/`: the AZMX logo in Colored, Navy Dark, and White SVG variants, plus the chevron favicon
- `assets/fonts/`: Azm X (TTF, English and Arabic) and thmanyah serif display (woff2 for web, OTF for desktop)
- `assets/fonts.css`: ready-made @font-face rules plus CSS variables for the palette

## Install (for AZMX team members)

You need access to this private repo (ask Gamal for an invite) and [Claude Code](https://claude.com/claude-code) or any agent that supports Agent Skills.

```bash
npx skills add Gamaleldientarek/azmx-brand-skill -g
```

That's it. Next time you ask Claude for anything AZMX-branded, the skill kicks in automatically. You can also invoke it directly with `/azmx-brand`.

To update to the latest version later:

```bash
npx skills update azmx-brand
```

## Quick palette reference

| Token | Hex |
|---|---|
| Electric | `#001AFF` |
| Dark Navy | `#040038` |
| Light Blue | `#5D8FFF` |
| Blue 50 | `#F0F5FF` |
| Neutral 900 | `#111927` |

Full ramps and usage rules live in `references/colors.md`.

## License note

The thmanyah serif display and Azm X font files are licensed for AZMX use only. This repo is private for that reason. Do not redistribute the fonts outside the team.

Built by [gamaleldien.com](https://gamaleldien.com) (ccreative@azmx.sa). Design system v1.1, encoded from the New Direction Library Figma file.
