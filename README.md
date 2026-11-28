# ai-shopping

AI-assisted shopping research. Each thing I want to buy gets a list entry and, when it needs real research, a note with options, prices, and a recommendation.

## Layout

```
lists/*.yaml            Structured data: items, status, budget, price options. One file per list.
research/<category>/    Markdown notes: reasoning and recommendation per item or product family.
templates/              Copy these to start a new list or research note.
scripts/                Helpers: validate.py (schema check), report.py (best offer per item).
CLAUDE.md               Conventions for AI agents working in this repo.
```

## Workflow

1. **Capture** — add items to a list in `lists/<list>.yaml` (or point an agent at a source list, e.g. OurGroceries).
2. **Research** — agent adds price offers to the item's `options:` in YAML (with `url` + `checked` date), and for items worth comparing writes `research/<category>/<item>.md` from `templates/research.md` with the reasoning and recommendation.
3. **Decide** — review, set `status` and `pick` in YAML.
4. **Refresh** — prices go stale fast. Re-check before buying; update `checked`.

## Status values

`todo` → `researching` → `decided` → `bought` (or `skip`)

## Current lists

- [Black Friday 2026](lists/black-friday-2026.yaml)
- [3D printing filament](lists/filament.yaml)
- [Ebike](lists/ebike.yaml)
- [Cashback routes, BF/CM 2026](lists/cashback-2026.yaml)

## Data format

See [`templates/list.yaml`](templates/list.yaml) for the full annotated schema. Key rules:

- Prices in USD, numbers not strings. `unit` + `unit_qty` let tools compute price per kg/oz/count.
- Every option has `url` and `checked` (YYYY-MM-DD).
- YAML is source of truth for prices and status; markdown is for reasoning. Don't duplicate price tables in notes.

## Scripts

```
pip install -r requirements.txt
python3 scripts/validate.py          # schema check for lists/*.yaml
python3 scripts/report.py            # markdown table: best offer + unit price per item, flags stale prices
```
