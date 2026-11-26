# Agent conventions

- Markdown + YAML. No scripts or build steps unless asked.
- Prices, status, offers go in `lists/<list>.yaml` (schema: `templates/list.yaml`). Reasoning goes in markdown notes.
- New research note: copy `templates/research.md` to `research/<category>/<kebab-item>.md`.
- Every option needs `url` and `checked: YYYY-MM-DD`. Set `sale_ends` when known.
- Prefer price per unit (per kg, per oz, per count) when comparing.
- Give one clear recommendation plus runner-up; say why.
- Set the item's `research:` path and `status`. Keep YAML valid (run `python3 -c "import yaml,sys;[yaml.safe_load(open(f)) for f in sys.argv[1:]]" lists/*.yaml`).
- Don't buy, sign in, or add to carts. Research only.
