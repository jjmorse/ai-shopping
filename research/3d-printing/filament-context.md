# Filament choices and existing supply

Data: [`lists/filament.yaml`](../../lists/filament.yaml) → items `silk-pla-silver`, `silk-pla-gold`, `pla-black`, `petg-clear`, `pla-brown`, and `tpu-black`.

Recorded: 2026-11-27 from this conversation's earlier research and Josh's observations. Prices and inventory status live in YAML. This import does not recheck stock, sale prices, or previously linked pages.

## Need

Josh uses a Bambu X2D with AMS 2 Pro for board-game organizers and pieces, household/camper utility parts, and toys. He already ordered a large PLA color assortment; additional materials should fill a specific gap. The original printer budget was roughly $500, with room up to $800 for a justified upgrade; the X2D is now owned.

For newer silk/black offers and their original recommendations, see the [2026-11-27 deal research](filament.md). Those offers and their verification dates were preserved from the merged filament PR; this note supplies earlier ownership and material context.

## Options summary

| Material | Useful differences | Best fit here |
|---|---|---|
| Ordinary PLA | Easy to print, rigid, good detail; can deform in heat and is relatively brittle | Most indoor organizers, trays, decorative pieces, and initial prototypes |
| PLA+ | Modified PLA; often tougher and less brittle, but the label is not a standardized grade | Handled parts where a specific product's impact performance justifies its price |
| HS PLA | Marketed for faster extrusion/printing; does not itself establish toughness, heat resistance, or color depth | The Kingroon pack already owned; tune its profile rather than assuming it needs replacement |
| PETG | More ductile and generally more heat tolerant than ordinary PLA; drying and tuning matter | Selected utility parts; verify actual temperature and mechanical requirements for camper use |
| Clear PETG | Rigid and translucent; ordinary printed walls are not automatically glass-clear | Light covers, windows, and experiments with translucency |
| TPU | Flexible; hardness and formulation determine how rubbery it feels | Feet, bumpers, grips, and flexible cases; see [TPU note](tpu.md) |
| Silk PLA | Decorative shine; do not assume ordinary PLA's mechanical performance | Silver tokens, ornaments, and decorative board-game pieces |
| Wood-filled PLA | Wood-like color/finish; texture can visibly differ from adjacent ordinary PLA | Optional aesthetic material, not necessary to obtain a brown color |

PLA+ is brand-specific: eSUN's published [PLA+ technical data sheet](https://uk.esun3d.com/media/esun/catalog/certification/product/PLA/PLA_-TDS-en.pdf) lists heat deflection around 54°C, illustrating why “+” alone does not solve hot-camper use. Compare each formulation's data rather than treating all PLA+ as stronger, stiffer, faster, or more heat resistant. Neither PLA+ nor HS guarantees a darker black.

## Recommendation

**Buy:** Fill remaining material/color gaps deliberately: flexible black TPU if that checkout has not been completed, clear PETG when there is a translucency project, and silver or brown PLA for specific game pieces.

**Runner-up:** Continue using the Kingroon PLA supply before buying another bulk pack. Keep the newer silver, gold, and black shopping entries and their researched offers; gold was lower priority than silver in the earlier discussion, but the newer list is preserved.

**Why:** Ordinary PLA already covers the organizer projects. A bulk discount does not establish a need for more kilograms, and buying filament to avoid shipping only saves money when the added material will be used.

## Inventory and reusable spools

- The confirmed Kingroon HS pack contains white, gray, black, red, blue, yellow, purple, green, pink, and teal. It does not contain brown or orange.
- Kingroon PETG was shown at final checkout, but payment completion was not confirmed. Check order history before buying duplicate PETG colors.
- “Filament with spool” from Bambu includes a reusable spool; “refill” needs a compatible empty spool. A PETG spool can later hold a compatible PLA refill; the material originally on it does not reserve it for PETG.
- Kingroon plastic spools are not established to split apart and accept Bambu refills. Being plastic is not the same as being a reusable refill spool.
- Reuse an empty compatible spool as it becomes available. Buy additional spools only for refills that need to be mounted at the same time; the total number of refills owned is not the number of empty spools required immediately.

## Drying and storage

Use the filament manufacturer's temperature/time guidance and a dryer that actually reaches that temperature, with spool heat tolerance checked first. A sealed container with desiccant maintains dryness; it is not equivalent to actively drying a wet spool. The AMS 2 Pro's documented maximum drying temperature is 65°C, so it cannot deliver a 70°C drying instruction as written.

The [X2D manual](https://csm.bblcdn.com/hub/7c58718aaa2e40edab56efb87419a96a.pdf) and [Bambu PETG Translucent product page](https://us.store.bambulab.com/products/petg-translucent) were the primary references. Earlier guidance for that PETG was 65°C for 8 hours; recheck the exact product's current instructions before drying.

## Related research

- [Black PLA comparison](black-pla.md)
- [Filament supplier evidence](filament-providers.md)
- [TPU choice and feeding](tpu.md)
- [Printer setup, nozzles, and purchase lessons](x2d.md)
- [Board-game organizer shortlist](board-game-organizers.md)
