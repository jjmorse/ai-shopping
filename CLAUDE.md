# Agent conventions

- Markdown + YAML, plus small Python scripts in `scripts/` where they help (stdlib + PyYAML only; add deps to `requirements.txt`).
- Prices, status, offers go in `lists/<list>.yaml` (schema: `templates/list.yaml`). Reasoning goes in markdown notes.
- New research note: copy `templates/research.md` to `research/<category>/<kebab-item>.md`.
- Every option needs `url` and `checked: YYYY-MM-DD`. Set `sale_ends` when known.
- Prefer price per unit (per kg, per oz, per count) when comparing.
- Give one clear recommendation plus runner-up; say why.
- Set the item's `research:` path and `status`. Run `python3 scripts/validate.py` before committing.
- Don't buy, sign in, or add to carts. Research only.

## Research standards (learned 2026-11-27)

- Deal sites and fetch summaries are leads, not facts. Open the actual retailer product page before recommending: confirm in stock, buy-box price (not a sponsored ad, collection page, or "comp. value"), and photos match the requested form factor.
- Give direct product links (`/dp/<ASIN>`, product URL), not search links, unless nothing verified exists — then say so.
- If the browser fails, retry before reporting it offline; never repeat an old failure as current.
- Back quality/security claims with evidence (independent tests, teardown, owner reports) and flag vendor/affiliate sources. Say plainly when no evidence exists.
- Check what the person already owns before suggesting a purchase; maintenance can beat replacement.
- Marketplaces (AliExpress etc.): signed-out prices may be new-shopper only and shipping is often extra per store. Show price + shipping, compare per unit, and tell the person to check the cart total. Note platform coupons (e.g. $7 off $39) and whether combining items into one order helps.
- Compare bundles by what's actually inside (colors, weights per spool), not just the pack price.
- Preserve user-reported results separately from manufacturer claims and forum anecdotes. Complaint counts without a sales denominator are not measured failure rates; distinguish material, color, batch, seller, and machine.
- A checkout/cart screenshot is not confirmation of payment. Keep confirmed purchases, selected purchases, and unresolved checkout status distinct; never infer remaining coupon balance from an old cart.
- When importing earlier research, record the import date without resetting the source's verification date. Keep historical prices in YAML `price_history` with their price basis and uncertain observation date; do not present them as current `options`.
- For filament, verify net kilograms, spool versus refill, exact color/formulation, and feeding compatibility. “PLA+” and “HS” do not establish a standardized mechanical grade or color depth. Do not assume a plastic spool can accept a refill.
- For organizers, verify the actual edition, expansions, sleeve dimensions, bed fit, and hardware. A similar game title or a newer edition does not establish compatibility.
