# Powering a home — the honest version

You asked to run a home: 5 air conditioners, a fridge, a TV, a computer, and
10 lights. This page does the math and tells you what it actually takes — and
what the DYNAMO magnet generator can and cannot do.

---

## Your load, estimated

| Load | Typical watts (running) | Qty | Subtotal |
|------|--------------------------|-----|----------|
| Air conditioner (window, ~1 hp) | 1,000–1,500 W | 5 | 5,000–7,500 W |
| Refrigerator | 200–400 W | 1 | 200–400 W |
| TV | 100–300 W | 1 | 100–300 W |
| Computer (desktop) | 200–500 W | 1 | 200–500 W |
| Lights (LED) | 10–15 W | 10 | 100–150 W |

**Running total: roughly 5.6–8.9 kW.** If any of the ACs are central/split
units (3–5 kW each), the total is higher — 10 kW or more.

**Surge:** AC compressors and fridges pull 2–3× their running watts for the
first second they start. So the system must also survive **15–20 kW momentary
peaks**, not just the running load.

**Energy:** a home drawing ~8 kW around the clock uses ~190 kWh per day. That
number — the *energy*, not the *power* — is what actually sizes a system.

## Why a magnet generator won't do it

A generator does not make energy. It converts it:

```
mechanical energy in  ──►  electrical energy out
```

The repo's hand-crank build makes **1–10 watts while you crank**. Your home
needs **~8,000 watts continuously**. That is a 1,000–8,000× gap, and it is not
a gap that more magnets or more coils can close — because the missing 8 kW has
to come from *somewhere* mechanical: a 15+ horsepower engine burning fuel, a
water turbine with real head pressure, or the wind. "Free energy" from magnets
is impossible; energy is conserved (see [theory.md](theory.md), section 7).

So the magnet generator is the **physics and the education**. It is not the
home's power source. Here is what is.

## What actually powers a home

A real home system has four parts, and the magnet/coil part is only the last
one (the generator). The other three are what people usually miss:

1. **A real energy source.** Sun (solar panels), wind, falling water, the grid,
   or a fuel generator. This is the actual "fuel." No source = no power.
2. **Battery storage.** To run things at night (or when there's no sun/wind),
   you store energy in a big battery bank — exactly the "store it like solar"
   idea from [storage.md](storage.md).
3. **Power conversion.** A charge controller to manage the battery, and an
   inverter to turn battery DC into the AC your appliances use.
4. **The wiring and safety layer.** Breakers, disconnects, and a transfer
   switch — done by a licensed electrician.

## The realistic path: solar + battery

For a home with this load, the standard answer is a **grid-tied or off-grid
solar + battery system**. It uses the *identical* storage chain from
[storage.md](storage.md), just scaled up and fed by panels instead of a magnet.

A ~10 kW system sized for this home looks roughly like:

| Component | Spec | Rough cost (USD) |
|-----------|------|------------------|
| Solar panels | ~20 × 500 W = 10 kW | $6,000–8,000 |
| Charge controller (MPPT) | 2–4 × 100 A | $1,000–2,000 |
| Battery bank (LiFePO4) | 20–40 kWh | $6,000–12,000 |
| Inverter (pure sine) | 10 kW, surge-rated | $2,000–4,000 |
| Mounting, wiring, breakers, disconnects | — | $2,000–5,000 |
| Electrician (mains work) | licensed | $3,000–8,000 |
| **Total** | | **$20,000–39,000** |

**The honest bottom line:** running 5 ACs off-grid is a major project — the
air conditioning alone dominates the bill. Cheaper paths, in order:

1. **Stay on the grid** and reduce the AC load (the cheapest option by far).
2. **Grid-tied solar** — panels offset your bill; no battery needed.
3. **Hybrid** — solar + a smaller battery for the essentials (lights, fridge,
   computer), not the ACs.
4. **Full off-grid** — the $20–40k system above, only worth it if you have no
   reliable grid.

## Safety — read this

- **Mains / 240 V wiring is not DIY.** A licensed electrician must do the
  panel, breakers, and transfer switch. Wrong wiring kills and starts fires.
- **Battery banks store serious energy.** A 20 kWh LiFePO4 bank can dump
  thousands of amps into a short. Fuses, proper cable sizing, and a BMS are
  not optional.
- **Inverters output lethal voltage.** Treat the AC side with the same respect
  as grid power.

---

**What this repo is for:** the physics ([theory.md](theory.md)), the builds
([TUTORIAL.md](TUTORIAL.md)), the storage chain ([storage.md](storage.md)),
and the full materials list ([materials.md](materials.md)). The magnet
generator teaches you the law; solar + battery is what powers the house.
