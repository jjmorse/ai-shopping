# Black flexible TPU

Data: [`lists/filament.yaml`](../../lists/filament.yaml) → item `tpu-black`.

Recorded: 2026-11-27 from earlier conversation research. The historical Bambu checkout is in YAML; it is not a current offer or proof of completed payment.

## Need

Flexible material for grips, bumpers, feet, and cases. The external feeder now fits after Josh moved the printer's orientation, so AMS compatibility is no longer necessary to solve a space constraint.

## Options summary

| Product | Trade-off |
|---|---|
| [Bambu TPU 95A HF](https://us.store.bambulab.com/products/tpu-95a-hf) | Softer, more rubber-like choice; HF formulation and Bambu profile; requires external feeding |
| [Bambu TPU for AMS](https://us.store.bambulab.com/products/tpu-for-ams) | Firmer 68D material designed for AMS feeding; convenience comes with different flexibility |
| [3DHoJor TPU, Amazon listing considered](https://www.amazon.com/dp/B0DF2VLNPN) | Budget 95A alternative; the inspected variant was clear, not the desired black, and was not established to be high-flow |
| Geeetech bulk TPU | Large commitment before identifying actual flexible-print needs; confirm exact hardness, color, and feeding instructions rather than assuming AMS support |

Shore A and Shore D are different hardness scales. The numbers 95A and 68D should not be compared as though they were points on one scale. Clear TPU is flexible and does not substitute for rigid clear PETG.

## Recommendation

**Buy:** Josh favored black Bambu TPU 95A HF using his Bambu PayPal coupon, while holding off on more hotends. Confirm whether that order was completed before treating it as still outstanding.

**Runner-up:** A single spool of another established 95A TPU if buying without the coupon and its delivered price is materially better. There is no reason to use an expiring Bambu-only credit as though it can be redeemed at Amazon.

**Why:** The external-feed issue is resolved, and the softer material adds a capability that the existing PLA and PETG do not provide.

## Printing and drying

1. Use the existing 0.4 mm main hotend for the initial TPU prints.
2. Dry according to the exact material's instructions. Bambu's earlier 95A HF guidance was 70°C for 8 hours and storage below 20% RH; recheck the [product page](https://us.store.bambulab.com/products/tpu-95a-hf) before use. AMS 2 Pro tops out at 65°C, so it does not achieve that 70°C target.
3. Feed 95A HF through the external path to the main hotend, bypassing the AMS and filament buffer as described in the [X2D manual](https://csm.bblcdn.com/hub/7c58718aaa2e40edab56efb87419a96a.pdf).
4. Start with the matching Bambu material profile and a small part. Do not use a 0.2 mm nozzle for this first TPU trial.

## Owner evidence for the budget alternative

The 3DHoJor evidence was mixed: a [FlashForge owner reported successful TPU prints](https://www.reddit.com/r/FlashForge/comments/1v9qgoz/creator_5_pro_2nd_round_of_tpu_95a/), while a [Bambu discussion included feeding/underextrusion problems](https://www.reddit.com/r/BambuLab/comments/1tanza6/tpu_suggestions_please/). Those are individual experiences on different machines, not a measured defect rate or proof that all spools perform alike.
