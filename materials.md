# Materials — everything, with specs

Two lists: the small builds (what the tutorial actually builds) and the
home-scale system (what it would take to power a house). Costs are rough USD.

---

## Small builds (TUTORIAL.md)

### Build 1 — Faraday flashlight (~$10)

| Item | Spec | Qty | Notes |
|------|------|-----|-------|
| Enameled copper wire | 26 AWG, ~10 m | 1 | "magnet wire" — the lacquer is the insulation |
| Neodymium disc magnets | 10 mm × 5 mm, N42+ | 2–4 | stack them into a slug |
| Cardboard/plastic tube | ~15–18 mm inner diameter | 1 | paper-towel roll or pen body |
| LED | 3 mm or 5 mm, any color | 1 | |
| Tape | electrical or masking | — | |
| Multimeter | basic AC/DC | 1 | $5–15, reusable for everything |

### Build 2 — Hand-crank dynamo (~$35)

| Item | Spec | Qty | Notes |
|------|------|-----|-------|
| Enameled copper wire | 24–26 AWG, ~20 m | 1 | for 3–6 flat coils |
| Neodymium disc magnets | 15 mm × 4 mm, N42–N52 | 8 | alternated N/S on the rotor |
| Rotor disc | 3D-print / plywood / old CD | 1 | ~15–20 cm diameter |
| Stator board | plywood / plastic, same size | 1 | holds the coils |
| Axle | 6–8 mm bolt or steel rod | 1 | |
| Bearing / bushings | skate bearing or tight tube | 2 | |
| Crank | bolt + wood handle, or bent rod | 1 | |
| Bridge rectifier | 4× 1N4007 diodes, or a 1 A bridge module | 1 | |
| Capacitor | 470–1000 µF, 16 V+ | 1 | mind polarity |
| LED + resistor | any LED, 330 Ω–1 kΩ | 1 | |
| Stand | wood block or printed frame | 1 | |

### Build 3 — Wind turbine (Build 2 +)

| Item | Spec | Qty | Notes |
|------|------|-----|-------|
| Blades | 3× cut from a bottle / plywood / printed | 1 set | |
| Pivot/post | swivel mount | 1 | lets it face the wind |
| Buck converter (optional) | DC-DC to 5 V | 1 | for charging a power bank |

### Storage add-ons (storage.md)

| Item | Spec | Qty | Notes |
|------|------|-----|-------|
| Buck converter | DC-DC, set to 5 V | 1 | charges a power bank safely |
| Power bank | any | 1 | has BMS + charge circuit built in |
| — or — charge controller | 12/24 V PWM or MPPT | 1 | for a real 12 V battery |
| — and battery | 12 V sealed lead-acid or LiFePO4 | 1 | LiFePO4 needs a BMS |

---

## Home-scale system (home-power.md)

For a ~10 kW off-grid solar + battery system powering 5 ACs, fridge, TV,
computer, and 10 lights.

| Component | Spec | Qty | Rough cost (USD) |
|-----------|------|-----|------------------|
| Solar panels | ~500 W each (mono PERC) | ~20 (10 kW) | $6,000–8,000 |
| MPPT charge controller | 100 A, 150 V input | 2–4 | $1,000–2,000 |
| Battery bank | LiFePO4, 48 V | 20–40 kWh | $6,000–12,000 |
| Inverter | 10 kW pure sine, surge-rated | 1 | $2,000–4,000 |
| Racking + mounting | roof or ground | 1 set | $1,000–2,000 |
| Wiring, breakers, fuses, disconnects | UL-listed, sized to code | — | $1,000–3,000 |
| Transfer switch / sub-panel | manual or automatic | 1 | $500–1,500 |
| Electrician labor | licensed | — | $3,000–8,000 |
| **Total** | | | **$20,000–39,000** |

**Order of work (and why):**

1. **Load audit** — measure what each appliance actually draws (a $30 clamp
   meter). Real numbers beat estimates.
2. **Reduce load first** — the cheapest kilowatt is the one you don't use
   (more efficient ACs, LED lights, insulation).
3. **Source** — solar is the default; wind/hydro only if your site has a real
   resource.
4. **Storage** — size the battery to cover your nights and the load you
   actually need to run off-grid.
5. **Electrician** — the panel, breakers, and transfer switch are done by a
   licensed pro, never DIY.

---

## Where to buy

- Magnet wire, neodymium magnets, diodes, capacitors: electronics suppliers
  and hobby marketplaces (search "magnet wire 26 AWG", "neodymium disc
  magnets N52", "1N4007 diode kit").
- Solar panels, MPPT controllers, LiFePO4 batteries, inverters: dedicated
  solar suppliers and battery distributors. Buy batteries with an integrated
  BMS and known-brand cells.
- Multimeter and clamp meter: any hardware store — get a meter that reads both
  AC and DC, and a clamp meter for the load audit.
