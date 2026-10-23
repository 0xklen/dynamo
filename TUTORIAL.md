# Tutorial — three working builds

Build them in order. Build 1 proves the physics in 20 minutes. Build 2 is a
real generator. Build 3 makes it turn by itself.

---

## Safety first

- **Neodymium magnets are dangerous.** Two of them can snap together hard
  enough to shatter and pinch skin. Keep them apart, keep them away from
  pacemakers, cards, and hard drives.
- **Scrape the enamel off the wire ends.** Magnet wire is coated in a clear
  insulating lacquer. It looks like bare copper but does not conduct until you
  scrape or sand it.
- Build 1 and 2 produce low voltage and are safe. Do not wire anything here
  into mains power.

---

# Build 1 — The Faraday flashlight (shake light)

A magnet sliding through a coil. No soldering, no frame.

## Parts

| Item | Spec |
|------|------|
| Enameled copper wire | 26 AWG, ~10 m |
| Neodymium magnets | 2–4 disc magnets, ~10 mm × 5 mm, N42+ |
| Cardboard tube | from a paper-towel roll, or a plastic pen body |
| LED | any 3 mm or 5 mm |
| Tape | electrical or masking |

## Tools

- A ruler or dowel to wind the coil on
- Sandpaper or a knife (to scrape wire ends)
- A multimeter (to see what's happening)

## Steps

1. **Wind the coil.** Tape one end of the wire to the tube, leaving a ~15 cm
   tail. Wrap 300–600 turns around the middle of the tube. Keep the turns
   tight and together. Leave another ~15 cm tail.

2. **Scrape the ends.** Sand the last 2 cm of both tails until they are shiny
   copper. This is the most common failure point — if the LED does nothing,
   this is why.

3. **Connect the LED.** Touch one scraped end to each leg of the LED. Polarity
   doesn't matter for a blink — the current reverses anyway.

4. **Make the slug.** Stack 2–4 disc magnets so they form a cylinder that
   slides freely inside the tube.

5. **Shake.** Drop the magnet slug into the tube, cap both ends, and shake it
   along the axis. The LED should blink on every pass.

## What you're seeing

The magnet passes through the coil: flux rises to a peak and falls, twice per
shake (once in, once out). Each rise and fall is a `ΔΦ/Δt`, so each pass is a
voltage pulse. Shake faster → brighter blinks.

## Test it

Set the multimeter to **AC volts**, clip the probes to the two wire tails, and
shake. You'll see spikes of a few hundred millivolts to a couple of volts,
depending on turns and how hard you shake.

## Troubleshooting

- **No light** — the enamel isn't scraped off. Scrape harder, test continuity
  with the meter.
- **Weak blinks** — more turns, stronger/bigger magnets, or a tighter tube so
  the magnet moves faster.
- **Magnet sticks in the tube** — the tube is too tight, or the slug is too
  wide. Use one fewer magnet.

---

# Build 2 — The hand-crank dynamo (axial flux)

A real generator: a spinning disc of magnets past flat coils, rectified to DC,
with a capacitor to hold the charge.

## How it works

An **axial-flux** machine: two parallel discs face each other across a small
air gap. One disc carries magnets (the **rotor**), the other carries flat
coils (the **stator**). When the rotor spins, each coil sees a north pole then
a south pole sweep past — a full AC cycle per magnet pair.

## Parts

| Item | Spec | Qty |
|------|------|-----|
| Enameled copper wire | 24–26 AWG, ~20 m | 1 |
| Neodymium disc magnets | 15 mm × 4 mm, N42–N52 | 8 |
| Rotor disc | 3D-printed, plywood, or a CD | 1 |
| Stator board | plywood / plastic, same diameter | 1 |
| Axle | 6–8 mm bolt or steel rod | 1 |
| Bearing / bushings | skate bearing or tight-fitting tube | 2 |
| Crank | a bolt + wooden handle, or a bent rod | 1 |
| Bridge rectifier | 4× 1N4007 diodes (or a 1A bridge module) | 1 |
| Capacitor | 470–1000 µF, 16 V+ | 1 |
| LED + resistor | any LED, 330–1 kΩ | 1 |
| Stand | wood block or 3D-printed frame | 1 |

## Steps

1. **Make the stator coils.** Wind 3–6 flat coils: wrap 100–150 turns of wire
   around a small mandrel (a 3 cm dowel or a AA battery), then slide it off,
   pinch it flat, and tape it into a pancake ~3–4 cm across. Scrape the ends.
   Glue the coils to the stator board in a ring, evenly spaced, all wound the
   same direction.

2. **Mount the magnets.** Glue 8 disc magnets to the rotor disc in a ring that
   lines up with the coils, **alternating north and south** (flip every other
   magnet). The north/south alternation is what makes the flux reverse — skip
   it and you get very little output. Check the pattern by dangling a test
   magnet: adjacent magnets should attract/repel alternately.

3. **Fit the axle and bearing.** Drill the center of both discs, mount the
   rotor on the axle so it spins freely, and fix the stator in place facing
   it. The gap between magnets and coils should be **2–3 mm** — as close as
   you can get without touching.

4. **Wire the coils in series.** Coil A end → coil B start → coil B end → coil
   C start, and so on, so all the voltages add. Bring out two final leads.
   (All coils must be wound the same direction for this to add instead of
   cancel — if output is near zero, reverse one coil's leads.)

5. **Add the bridge rectifier.** Wire the two leads to the AC inputs of the
   bridge (the `~` pins). The `+` and `-` pins are now DC out.

6. **Add the capacitor and LED.** Capacitor across `+`/`-` (mind the polarity,
   stripe = negative). LED + resistor across the capacitor.

7. **Crank.** Spin the rotor by hand. The LED should light. Crank faster → the
   LED gets brighter and the capacitor holds the charge so it stays lit
   briefly after you stop.

## Test it

- **No load:** meter on AC volts across the coil leads (before the rectifier).
  Expect a volt to several volts while cranking.
- **After the rectifier:** meter on DC volts. You should see a positive voltage
  that rises with crank speed.
- **Loaded:** the LED stays lit a moment after you stop cranking, fed by the
  capacitor.

## Troubleshooting

- **No output** — magnets not alternating N/S, or coils not in phase (reverse
  one coil's leads), or the gap is too wide.
- **Output cancels** — one coil is wound backward. Reverse its two leads.
- **LED flickers hard** — normal at low speed; the capacitor smooths it.
  Increase the capacitor value for steadier light.
- **Very weak** — more turns, stronger magnets, or a smaller air gap.

---

# Build 3 — The wind turbine

Everything from Build 2, with blades instead of a crank.

## Changes from Build 2

1. **Blades.** Cut 3 blades from a plastic bottle or light plywood, or print
   a small 3-blade hub. Mount them on the rotor disc (or on a shaft in front
   of it) so the rotor spins when wind hits it.

2. **Pivot.** Put the whole assembly on a swivel so it can turn to face the
   wind. A simple post + a bolt through the base is enough.

3. **Charge a battery (optional).** Add a small buck converter to regulate the
   rectified output to 5 V and feed a rechargeable AA or a supercapacitor.

## Notes

- A small home build makes **milliwatts to a watt or two** in a stiff breeze —
  enough to light an LED or trickle-charge a battery, not to run a house.
- The same rotor/stator from Build 2, driven by falling water instead of wind,
  is a working **hydro** generator.

---

## Where the three builds fit

| Build | Type | Output | Difficulty |
|-------|------|--------|------------|
| 1. Faraday flashlight | Linear | < 1 V pulses | Trivial |
| 2. Hand-crank dynamo | Axial flux | 1–10 V DC | Moderate |
| 3. Wind turbine | Axial flux | 1–5 V DC, continuous | Moderate |

All three obey the same equation: `emf = -N · ΔΦ/Δt`. Get Build 2 cranking and
you have understood and built what a power plant does.
