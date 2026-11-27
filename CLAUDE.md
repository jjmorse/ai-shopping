# Agent conventions

- Markdown + YAML, plus small Python scripts in `scripts/` where they help (stdlib + PyYAML only; add deps to `requirements.txt`).
- Prices, status, offers go in `lists/<list>.yaml` (schema: `templates/list.yaml`). Reasoning goes in markdown notes.
- New research note: copy `templates/research.md` to `research/<category>/<kebab-item>.md`.
- Every option needs `url` and `checked: YYYY-MM-DD`. Set `sale_ends` when known.
- Prefer price per unit (per kg, per oz, per count) when comparing.
- Give one clear recommendation plus runner-up; say why.
- Set the item's `research:` path and `status`. Run `python3 scripts/validate.py` before committing.
- Don't buy, sign in, or add to carts. Research only.
