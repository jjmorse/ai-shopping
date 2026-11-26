# ai-shopping

AI-assisted shopping research. Each thing I want to buy gets a list entry and, when it needs real research, a note with options, prices, and a recommendation.

## Layout

```
lists/                  Shopping lists (what to buy). One file per list.
research/<category>/    One note per item or product family (what to buy, where, why).
templates/              Copy these to start a new list or research note.
CLAUDE.md               Conventions for AI agents working in this repo.
```

## Workflow

1. **Capture** — add items to a list in `lists/` (or point an agent at a source list, e.g. OurGroceries).
2. **Research** — for each item worth comparing, an agent copies `templates/research.md` into `research/<category>/<item>.md` and fills it: requirements, options, prices with source links and check dates, recommendation.
3. **Decide** — review the note, mark the list item `decided` / `bought` / `skip`.
4. **Refresh** — prices go stale fast. Re-check before buying; update the `Checked` date.

## Status values

`todo` → `researching` → `decided` → `bought` (or `skip`)

## Current lists

- [Black Friday 2026](lists/black-friday-2026.md)
- [3D printing filament](lists/filament.md)
