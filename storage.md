# Storing the electricity in a battery

A generator makes electricity; a battery keeps it. But you cannot connect one
to the other directly. This page is the storage half of the system — the part
that makes the power from a magnet generator (or a solar panel, or a wind
turbine) actually usable later.

---

## Why you can't just wire the generator to a battery

Two reasons:

1. **The voltage is all over the place.** Crank slow and you get 2 V; crank
   fast and you get 20 V. A battery wants a controlled, specific voltage. Feed
   it the wrong one and nothing useful happens, or the battery dies.

2. **Overcharge and over-discharge destroy batteries.** Push a battery past
   its full voltage and it overheats (lithium: fire risk) or boils (lead-acid).
   Drain it below its floor and it sulfates (lead-acid) or kills a cell
   (lithium). Batteries want a babysitter.

So between the generator and the battery you insert a **charge chain**.

## The chain

```
generator ──► rectifier ──► voltage regulator ──► charge controller ──► battery
                                                       │
                                                       └──► BMS (lithium only)
                                                              │
                                          (optional) inverter ──► AC loads
```

| Stage | What it does |
|-------|--------------|
| **Rectifier** | AC → DC (the 4-diode bridge you already built) |
| **Voltage regulator** | Buck/boost converter that turns the wild 2–20 V into the battery's charge voltage |
| **Charge controller** | The brain: charges in stages, stops when full, cuts off when empty |
| **BMS** | Battery management system — per-cell protection for lithium packs |
| **Inverter** | Optional: DC battery → household AC |

For a small magnet generator, stages 1–3 are the minimum. Lithium adds the
BMS.

## The charge controller (the part everyone skips)

This is the same device a solar panel uses, and for the same reason: the
source is unregulated, the battery is not. Two kinds:

- **PWM** — simple, cheap, fine for small builds. Switches the source on and
  off to hold the target voltage.
- **MPPT** — actively tracks the source's best power point and converts the
  excess voltage into extra current. Worth it for solar panels; overkill for a
  hand crank.

Charge stages (lead-acid): **bulk** (full current to ~80%) → **absorption**
(hold voltage, taper current) → **float** (trickle to keep it topped up).
Lithium instead uses **CC/CV**: constant current until the voltage ceiling,
then constant voltage with tapering current, then stop. The controller does
this; you don't.

## Choosing the battery

| Chemistry | Voltage | Pros | Cons | Needs |
|-----------|---------|------|------|-------|
| Lead-acid (AGM/sealed) | 12 V | Forgiving, cheap, loves float | Heavy, ~500 cycles, don't drain below 50% | Charge controller |
| LiFePO4 | 12.8 V | Light, 2000–5000 cycles, safe | Pricier | Charge controller + BMS |
| Li-ion (18650 pack) | 3.7 V/cell | Most energy per gram | Real fire risk if mistreated | BMS is mandatory |

For a first battery, **12 V sealed lead-acid or LiFePO4** with a proper charge
controller is the sane choice. Raw 18650s wired straight to anything is how
fires happen.

## The two realistic paths

### Small: charge a USB power bank

The easiest safe storage there is. A power bank already contains a BMS, a
charge controller, and protection circuits.

```
generator ──► rectifier ──► buck converter to 5 V ──► power bank USB input
```

- Use a buck module set to a clean 5 V.
- The power bank charges exactly as if plugged into a wall.
- All the safety is built in. You can't overcharge or over-discharge it.

### Medium: a real 12 V battery bank

```
generator ──► rectifier ──► buck/boost regulator ──► charge controller ──► 12 V battery
```

- Match the regulator output to the controller's input range (most take
  12–24 V in).
- The controller manages the battery. For lithium, it (or the battery) must
  include a BMS.
- Add a 12 V → 5 V USB converter, or a 12 V inverter, on the output side to
  run real loads.

## The honest reality check

A hand-crank magnet generator makes **1–10 W while you crank**. A "big" solar
battery — say 12 V × 100 Ah = **1200 Wh** — would take 120 to 1200 hours of
continuous cranking to fill. That is not a plan; it is a gym routine.

This is exactly why solar panels power storage systems: a panel sustains tens
of watts for hours a day, unattended. The physics of *storing* it is identical
whether the source is a magnet, a panel, or a turbine — but the source has to
actually produce more energy than you use.

**What this means for the DYNAMO builds:**

- Build 2 (hand-crank) → charge a **power bank** or a small **AA/NiMH or LiFePO4
  cell**. Practical and real.
- Build 3 (wind turbine) → add the full chain and charge a **12 V battery**
  over a windy day. Still slow, but it runs unattended.
- To run a house off a battery bank, the magnet generator has to be driven by
  something that sustains power — falling water or wind — not your arm.

## Safety, stated plainly

- **Lithium is not a toy.** Always use a BMS with lithium cells, never bypass
  it, never short the terminals.
- **Lead-acid off-gasses hydrogen** when overcharged. Charge it in a vented
  space, no sparks nearby.
- **Match voltages.** A regulator set wrong, or a controller wired backward,
  destroys the battery. Measure before you connect.
- **Fuses.** Put a fuse between the battery and anything downstream. Batteries
  can deliver enormous current into a short.

---

**Back to the builds:** [TUTORIAL.md](TUTORIAL.md)
