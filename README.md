<div align="center">

<img src="assets/logo.svg" width="110" alt="DYNAMO">

# DYNAMO

**Spin a magnet. Make electricity.**

Electromagnetic induction — the physics, the parts, and three builds you can do at home.

[![stars](https://img.shields.io/github/stars/0xklen/dynamo?style=flat-square&labelColor=000000&color=000000)](https://github.com/0xklen/dynamo/stargazers)
[![last commit](https://img.shields.io/github/last-commit/0xklen/dynamo?style=flat-square&labelColor=000000&color=000000)](https://github.com/0xklen/dynamo/commits/main)
[![license](https://img.shields.io/github/license/0xklen/dynamo?style=flat-square&labelColor=000000&color=000000)](LICENSE)
[![builds](https://img.shields.io/badge/builds-3-000000?style=flat-square&labelColor=000000)](#the-builds)
[![no code](https://img.shields.io/badge/software-none-000000?style=flat-square&labelColor=000000)](#what-this-is)

</div>

---

## What this is

A complete, from-scratch guide to generating electricity with a magnet. No
magic, no "free energy" nonsense — just the one physical law that powers every
generator on Earth, the parts to buy, and three working builds that go from a
blinking LED to a hand-crank generator that charges a capacitor.

Everything here is real, tested physics. If a step in the tutorial doesn't
produce a reading on your multimeter, something is wired wrong — not the law.

## The one law

**Faraday's law of induction.** A changing magnetic field through a coil of
wire induces a voltage. Move the magnet, or move the coil, and current flows.

```
emf = -N · ΔΦ / Δt
```

- `emf` — the voltage you generate (volts)
- `N` — number of turns of wire in the coil
- `ΔΦ / Δt` — how fast the magnetic flux through the coil is changing

The minus sign is **Lenz's law**: the induced current always pushes back
against the motion that caused it. That resistance is literally where your
muscle effort (or the wind, or falling water) goes.

Read the full derivation in [theory.md](theory.md).

## What you need

| Part | What it's for | Rough cost |
|------|---------------|------------|
| Enameled copper wire (24–28 AWG) | The coil — the thing voltage is induced in | ~$8 |
| Neodymium magnets (N42–N52) | The moving magnetic field | ~$10 |
| A rotor (disc, wheel, or sliding tube) | Carries the magnets in a circle | ~$2 |
| An axle + bearing (or a dowel + straw) | Lets the rotor spin freely | ~$3 |
| Bridge rectifier (4× 1N4007 diodes) | Turns the AC output into DC | ~$1 |
| Capacitor (100–1000 µF) | Smooths the output | ~$1 |
| LED + resistor | Visible proof it works | ~$1 |
| Multimeter | Measures the voltage/current | ~$10 |

Total: **under $35** for the biggest build; the first build is under $10.

Full specs and buying notes are in the tutorial.

## The three builds

1. **The Faraday Flashlight** — a magnet sliding through a coil lights an LED.
   No soldering, no frame, under $10, done in 20 minutes. Start here.

2. **The Hand-Crank Dynamo** — a rotor disc of magnets spinning past flat
   coils, a bridge rectifier, and a capacitor. A real axial-flux generator
   that you crank by hand.

3. **The Wind Turbine** — the same axial-flux build with blades on the rotor,
   mounted to catch the wind.

Each build is a full step-by-step in [TUTORIAL.md](TUTORIAL.md), with wiring,
a test procedure, and troubleshooting.

## Quick start

```bash
git clone https://github.com/0xklen/dynamo
cd dynamo
```

1. Read [theory.md](theory.md) — 10 minutes, and the builds will make sense
   instead of being magic.
2. Follow [TUTORIAL.md](TUTORIAL.md) — build the Faraday flashlight first.
3. When the LED blinks, move up to the hand-crank dynamo.
4. To keep the power for later, read [storage.md](storage.md) — the charge
   chain, battery chemistry, charge controllers, and the BMS. Same physics as
   a solar setup.

## Repo layout

```
dynamo/
├── README.md       this page
├── theory.md       the physics — Faraday, Lenz, AC/DC, how to get more voltage
├── TUTORIAL.md     three builds, step by step, with troubleshooting
├── storage.md      batteries — the charge chain, chemistry, controllers, BMS, safety
├── assets/
│   ├── logo.svg    the mark (a coil and a bolt)
│   └── logo.png    512px raster
└── LICENSE         MIT
```

## FAQ

**Is this free energy / perpetual motion?**
No. It is a converter: mechanical energy in, electrical energy out. The harder
you crank (against the magnetic back-force), the more electricity you get.
Energy is conserved, always.

**Does a magnet just sitting next to a coil make electricity?**
No. The field has to *change*. Static magnet + static coil = nothing. Move
either one, and you get voltage.

**How do I get more voltage?**
Four levers: more turns `N`, stronger magnets `B`, more area `A`, and more
speed `ΔΦ/Δt`. Or put an iron core in the coil to concentrate the field. All
covered in [theory.md](theory.md).

**AC or DC?**
A spinning magnet naturally produces AC (the voltage reverses every half turn).
Rectify it to DC with four diodes. The tutorial shows the exact wiring.

**How does this relate to a real power plant?**
Identical physics. A plant just spins a huge magnet (or electromagnet) inside
a huge coil using steam, falling water, or wind instead of your hand.

**How do I store it in a battery?**
You can't wire the generator straight to a battery — you need a rectifier, a
voltage regulator, and a charge controller (and a BMS for lithium). The full
chain, battery chemistry, and safety are in [storage.md](storage.md). It is
the same chain a solar panel uses.

## License

MIT — see [LICENSE](LICENSE). Build it, teach it, sell the kits. The physics
isn't mine to own.

<div align="center">

*every power plant on Earth is just this page, scaled up*

</div>
