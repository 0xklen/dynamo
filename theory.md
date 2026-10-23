# Theory — how a magnet makes electricity

Everything below is the whole story. Read it once and the builds stop being
magic and become obvious.

---

## 1. The field

A magnet produces a magnetic field. We draw it as field lines flowing out of
the north pole, looping around, and entering the south pole. The field is
strongest at the poles and weakens with distance.

The quantity that matters is **magnetic flux** — how much field passes through
a given area:

```
Φ = B · A · cos θ
```

- `B` — magnetic field strength (tesla)
- `A` — area of the loop (m²)
- `θ` — angle between the field and the loop's face

A coil held face-on to a strong magnet has high flux. Edge-on, `cos 90° = 0`,
so the flux is zero.

## 2. Faraday's law

The law is one line:

```
emf = -N · ΔΦ / Δt
```

The induced voltage (`emf`) equals the number of coil turns (`N`) times the
**rate of change** of flux. Three consequences:

1. **No change, no voltage.** A magnet sitting still inside a coil induces
   nothing. `ΔΦ/Δt = 0`.
2. **Faster change, more voltage.** Sliding or spinning the magnet faster makes
   `ΔΦ/Δt` bigger, so `emf` goes up.
3. **More turns, more voltage.** Ten turns give ten times the voltage of one
   turn, for the same change.

The flux changes every time the magnet moves toward the coil, away from it, or
rotates so its poles sweep past.

## 3. Lenz's law (the minus sign)

The induced current makes its own magnetic field that **opposes** the change
that produced it. This is why cranking a generator gets harder when you draw
more current — you are fighting the back-field.

This is not a flaw. It is the law that says energy is conserved: the work you
put in against that resistance is exactly what comes out as electricity.

## 4. Why a spinning magnet gives AC

Spin a magnet past a coil. As the north pole approaches, voltage builds in one
direction. As it passes and the south pole approaches, voltage builds in the
*other* direction. One full rotation = one full reversal = **alternating
current (AC)**.

A voltmeter across the coil shows a sine wave: positive, zero, negative, zero,
repeat.

## 5. Turning AC into DC

Most small loads (LEDs, phones, batteries) want direct current (DC) — one
steady direction. The fix is a **bridge rectifier**: four diodes arranged so
that whichever way the current is flowing, it gets steered onto the same two
output wires.

```
        AC in ─┬─►|─┬─  + DC out
               │    │
        AC in ─┴─|◄─┴─  - DC out
```

- Each diode conducts in one direction only.
- Whichever half of the wave is positive, two diodes route it to `+` and the
  other two return it from `-`.
- Result: the negative half of the wave flips up, giving a bumpy but
  one-directional output.

Add a capacitor across the DC output to smooth the bumps into something close
to steady DC.

## 6. The four levers that raise voltage

From `emf = -N · ΔΦ/Δt` and `Φ = B · A · cos θ`, there are exactly four ways
to get more voltage out of a build:

| Lever | How | Effect |
|-------|-----|--------|
| Turns `N` | More windings on the coil | Linear — double the turns, double the volts |
| Field `B` | Stronger magnets (N52 vs N35), closer gap | Linear in field strength |
| Area `A` | Bigger coil face | Linear in area |
| Speed `ΔΦ/Δt` | Spin or slide faster | Linear in speed |

One more trick that doesn't appear in the equation directly: put an **iron
core** inside the coil. Iron concentrates the field lines through the coil,
effectively raising `B` inside the loop by a huge factor. This is why real
generators and transformers are built around iron, not air.

## 7. Energy conservation — the honest part

A generator is a converter, never a source. The electrical power out equals the
mechanical power in, minus losses (wire resistance → heat, friction, eddy
currents in any iron core).

```
P_in (mechanical)  =  P_out (electrical)  +  losses
```

You cannot build a magnet machine that spins itself forever and also lights a
lamp. Every "free energy magnet motor" you see online is either a hidden
battery, a measurement error, or a scam. The physics has been settled since
1831.

## 8. The three generator topologies

**Linear (shake).** A magnet slides back and forth through a coil. Simplest,
lowest output. Used in Faraday flashlights and shake-to-charge toys.

**Axial flux (disc).** Flat coils and magnets face each other across a narrow
air gap on two parallel discs. One disc spins. Easiest home build with the
best power-to-effort ratio. This is what the tutorial's hand-crank and wind
builds use.

**Radial flux (cylinder).** Magnets on the outside of a spinning cylinder,
coils around the outside (or vice-versa). This is how a car alternator and
most industrial generators are built — harder to DIY but very compact.

## 9. How a power plant uses all of this

A power plant burns fuel (or splits atoms) to boil water into steam, which
spins a turbine, which spins a magnet inside a stationary coil — literally
Faraday's law with a very big `N`, a very strong `B`, and a very fast
`ΔΦ/Δt`. Hydro plants use falling water to spin the same magnet. Wind turbines
use the wind. The electrical part is identical in every case.

---

**Next:** [TUTORIAL.md](TUTORIAL.md) — turn this into hardware.
