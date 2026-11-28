# Commuter ebike (repairable, under $2,000)

Data: [`lists/ebike.yaml`](../../lists/ebike.yaml) → item `commuter-ebike`
Checked: 2026-11-27

## Already owned (learned 2026-11-27)

Josh has a **RadMission** and likes it. Wants hybrid style, not fat tire; eyeing ~$1k.
- CPSC warning (Nov 2025) covers Rad battery models RP-1304, RAD-S1304Y, HL-RP-S1304 sold with RadWagon 4,
  RadCity HS 4 / ST 3, RadRover HS 5 / ST 1, RadRunner 1/2/Plus, RadExpand 5. **RadMission is not listed** —
  still check the battery label for those model numbers.
- Rad Life Mobility (new owner) still sells RadMission parts on radpowerbikes.com (headlight $45, seat $45,
  fenders $29 out of stock) and lists a RadMission battery pack on radpowerbikes.ca ($599 CAD). No US battery
  listing found. No warranty for bikes bought before Dec 15, 2025.
- RadMission is a simple single-speed hub bike; keeping it running is likely the cheapest repairable option.

## Need

Commute + errands (Josh picked "Commute/errands, under $2,000"). Must have a record of repairability:
standard bike parts any shop stocks, spare batteries sold by the brand, a brand likely to still exist in
5 years, and somewhere to get it fixed. Colorado winters → removable battery so it can be charged and
stored indoors (lithium cells shouldn't be charged below freezing).

## What "repairable" means at this price

- **Under $2k = hub motors.** The good motor repairability data (Bosch, Yamaha/Giant, Bafang mid-drives)
  is for $2.5k+ bikes. Hub motors are simple and rarely fail; what breaks is the battery, controller,
  display, wiring — all brand-specific. So the brand's parts store and survival matter more than the motor.
- **Battery is the #1 failure.** Wertgarantie data (via CyclingAbout) puts battery issues at ~41–44% of
  ebike faults. A brand that sells spare packs at a fair price is the biggest repairability signal.
- **Standard wear parts:** Shimano drivetrain + 6-bolt hydraulic rotors = any shop can service brakes/gears.
- **Brand survival is real risk.** Rad Power Bikes: CPSC warned owners to stop using two battery models
  (31+ fires, Nov 2025), Chapter 11 Dec 2025, warranties for bikes bought before then not honored, sold to
  Life EV Group Mar 2026 (Wikipedia). Avoid Rad and unknown Amazon brands.
- **No federal US right-to-repair law for ebikes.** EU rules (Feb 2027) will require user-replaceable
  batteries, but nothing binds US sales.

## Options summary

Prices/links live in the YAML. All checked 2026-11-27 via page fetch (Chrome extension was offline).

| | Aventon Level 4 REC | Trek FX+ 2 Stagger | Lectric XP4 750 | Ride1Up Vorsa |
|---|---|---|---|---|
| BF price | $1,799 (−$200) | $1,599.93 (Trek "comp. value" $2,499.99) | $1,299 (−$532) | $1,345 Lite / $1,445 Standard |
| Battery | 733Wh, removable, LG cells | 250Wh integrated (+250Wh extender option) | 840Wh, removable | 720Wh, removable, Samsung |
| Spare battery | $499 | n/a (extender only) | $350 | $475 |
| Drivetrain/brakes | Shimano Altus 8, Tektro hydraulic 6-bolt | Shimano 9, hydraulic | Shimano Altus 8 (summary), 602 hydraulic | Shimano Acera 8, Star Union hydraulic |
| Warranty | 2 yr + lifetime frame | Trek dealer warranty | 1 yr | 1 yr |
| Service | 2,000+ partner shops | Trek dealers (local stock not checked) | Mail-order parts only | Mail-order parts only |

## Recommendation (revised 2026-11-27 after deep dive)

**Buy:** Velotric Discover 3, $1,899 — if a step-through frame is OK.
**Runner-up:** Aventon Level 4 REC, $1,799.
**Cheapest solid pick:** Lectric XP4 750, $1,299 (folding).

**Why Velotric moved ahead:**
- Warranty: battery + electrical 3 yr (free with registration in 60 days; battery 3 yr/400 cycles), frame 10 yr.
  Aventon: 2 yr.
- Parts continuity: Discover 2 and 3 batteries interchangeable (after firmware update); spare battery sold.
- Local service: Longmont Bicycle Company is a Velotric showcase shop (110 Emery St, Longmont; 303-834-9994).
- Owner reports (EBR forum, 2024): one documented display failure — Velotric shipped a new display in ~3 days.
  Older 2023 Discover 1 complaints (brake adapter, cheap BB) not seen on newer models. Thin data.
- No CPSC recalls found for Velotric.

**Why Aventon dropped to runner-up:** the Level 4 REC runs Aventon's full ACU platform — 4G, GPS, electronic
lock, password display, app-managed firmware/security (Aventon's own REC-vs-ADV guide: REC gets "the same
platform"). More connected electronics = more single-source failure points. EBR thread (May–Oct 2026): one
Level 4 ADV owner's ECU failed twice (E34 init failure, then ~20 errors at 1,655 mi); dealer couldn't fix,
Aventon eventually swapped the whole bike after weeks waiting on inventory. One owner, ADV not REC, but same
ACU. Aventon's only CPSC recall: Sinch.2 (2024, controller software, fixed free at dealers). Upside remains:
2,000+ shops, CyclErie (Erie, CO) sells/services Aventon, $100 cheaper, step-over frame available.
Caveat: Velotric's own app/lock electronics not checked; may have similar connected parts.

## Evidence quality (say plainly)

- No independent long-term repair/failure data exists for any of these four hub-motor bikes. Owner
  evidence is anecdotal: EBR forum (2024) — Lectric "good customer service"; Aventon "LBS support" but
  "spotty customer service"; Ride1Up product reviews — replacement brake/throttle parts shipped next day.
- Motor reliability stats (CyclingAbout) cover mid-drives, not these hubs. CyclingAbout relies on polls with
  self-selection bias.
- Deal roundups (Electric Bike Report, Electrek) use affiliate links. EbikeBC and Cemoto right-to-repair
  articles are brand blogs; used only for the checklist, not facts.
- No sale end dates shown on any page. Aventon/Ride1Up buy-box prices read from page tables/upsells, not
  rendered buy box — re-check at checkout.

## Heybike (Josh asked 2026-11-27)

Venus is the commuter pick: $1,499 on heybike.com (affiliate codes claim $999 — unverified), 680Wh
removable battery, Shimano Altus, hydraulic brakes, light at 50 lb. Lower on repairability than Aventon:
- Warranty page headline says 2 years, but its "not covered" list says frame/motor/controller/display are
  warrantied only one week after delivery. Contradictory; get battery/motor terms in writing.
- Heybike's own Aug 2024 post admits parts resolution "remains a challenge", 10-20 days for warranty parts.
  UK Trustpilot (2024) reports ~2-month waits for small parts shipped from China.
- No Venus spare battery listed; Ranger spare battery sold out ($459).
- Third-party shop repairs reimbursed only with prior approval; no service network.
- PopSci test bike: battery-cover latch broke (Heybike sent replacement fast), chain dropped.
Verdict: fine budget bike, not a repairability pick. If $999 code works it undercuts Lectric, but Lectric
has spare batteries in stock and better support anecdotes.

## Black Friday codes / extras (checked 2026-11-27)

- No codes found for Aventon, Lectric, Ride1Up or Trek; deals are automatic. Aventon adds free lock + suspension
  seatpost; Lectric bundles accessories; Ride1Up accessories up to 40% off. Trek FX+ 2: no extra deal found.
- Heybike Venus: EBR500 / 9T5T500 claimed $500 off → $999 (affiliate sites; not on Heybike page).
- Heybike owner sentiment: Trustpilot US 4.1 / 1,779 reviews, 15% 1-star; themes = replacements eventually come
  but battery swaps can take weeks-months. Slickdeals owners: slow but helpful support. Reddit not reachable
  from this session; only secondhand "horror stories" mention.

## Lectric XPress Lite reviews (checked 2026-11-28)

- Class: ships as Class 2 (EBR spec list); Class 1/2/3 selectable in display menu (hold + and -). PIN lock not
  mentioned in any review.
- Range: 42 mi lowest assist, 22-24 mi max/fast (EBR, Electric Bike Report, RiderGuide). Expect less in cold.
- Build: "solid", no creaks, nothing broke in testing (3 reviewers). Brakes average-to-good.
- Cons: one frame size (~5'3"-6'1" fit per EBR), rigid fork + 1.95" tires are harsh on potholes, louder motor
  (80 dB vs 65 dB XPress 2, RiderGuide), small battery, rack/fenders extra, 275 lb payload.
- Prototype 350W motor overheated; Lectric moved to 500W before launch. New model (Oct 2026), so no long-term data.
- All three reviews use affiliate links; EBR got units from Lectric.

## Other vendors (checked 2026-11-27)

- Upway certified refurb Level 4 REC $1,549 (size S only, 3 mi); 1-yr Upway warranty instead of 2-yr.
- Mike's Bikes: Level 4 REC $1,799 same as direct, ends 11/30, + up to $400 store rewards.
- Velotric: Breeze 1 $1,699 with free spare battery (best spare-battery value seen); Discover 3 $1,899.
  3-yr warranty with registration. Repair record not researched yet.
- REI sale page showed no ebikes under $2k.
- Aventon/Upway "Re-Frame" trade-in at Aventon Signature Dealers ($200 bonus was 2025; 2026 unconfirmed).

## Other brands (checked 2026-11-27)

- **Velotric Discover 3, $1,899** — strongest challenger to Aventon: 3-yr battery/electrical warranty with
  registration, battery interchangeable with previous gen (good parts-continuity sign), spare sold, Longmont CO
  showcase shop for service. Step-through only, 61 lb. EBR review: sealed hub, solid build, 87 mi Eco range.
  Risk: ~6-yr-old VC-funded private company; dealers stock only batteries/chargers, other parts ordered.
- **Monarc Marker, $1,999** — Bafang motor (most serviceable brand per CyclingAbout), 2 batteries, 5-yr warranty.
  88 lb fat tire; better for snow than commuting.
- **Tenways CGO600 Pro, ~$1,499** (Oct price) — 37 lb, light, but 360Wh, stock in and out. Repair record unknown.
- **Priority** — belt-drive bikes (E-Coast/Glide $1,799) = minimal drivetrain maintenance; cruiser-style; specs
  and sale prices not visible.
- **Specialized Turbo Vado 3.0, from $2,099.99** — mid-drive + big dealer network; over budget, proprietary.

## Before buying

- Confirm a nearby shop on Aventon's dealer locator will service it (some shops only service what they sell).
- Ask if the shop can source Aventon controller/display, not just brakes/gears.
- Winter: bring battery in; charge above freezing.

## Sources

- [CyclingAbout — most serviceable ebike motors](https://www.cyclingabout.com/most-serviceable-repairable-ebike-motors/)
- [CyclingAbout — motor reliability data](https://www.cyclingabout.com/best-ebike-motors-for-reliability/)
- [Wikipedia — Rad Power Bikes](https://en.wikipedia.org/wiki/Rad_Power_Bikes)
- [EBR forum — Lectric vs Aventon vs Globe](https://forums.electricbikereview.com/threads/lectric-vs-aventon-vs-globe.56123)
- [Electric Bike Report — Black Friday deals](https://electricbikereport.com/black-friday-and-cyber-monday-electric-bike-deals/) (affiliate)
- [Electrek — best ebikes by price](https://electrek.co/2026/10/17/here-are-the-best-electric-bikes-you-can-buy-at-every-price-level/) (affiliate)
- [EBR Vorsa review](https://electricbikereport.com/ride1up-vorsa-review)
