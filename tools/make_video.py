#!/usr/bin/env python3
"""Generate the DYNAMO assembly video: SVG frames -> PNG -> MP4.

Run:  python3 tools/make_video.py
Output:  video/dynamo-tutorial.mp4  (and video/frames/*.png)

Requires resvg (SVG -> PNG) and ffmpeg (PNG -> MP4) on PATH.
"""
import os, subprocess, shutil, sys, math

W, H = 1280, 720
INK, GRAY, HAIR, ACCENT, COPPER = "#0b0b0c", "#6c6c73", "#e6e6e9", "#2563eb", "#d97706"
FONT = "Helvetica Neue, Helvetica, Arial, sans-serif"

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRAMES = os.path.join(ROOT, "video", "frames")
OUT = os.path.join(ROOT, "video", "dynamo-tutorial.mp4")

RESVG = shutil.which("resvg") or os.path.expanduser("~/.local/bin/resvg")
FFMPEG = shutil.which("ffmpeg") or os.path.expanduser("~/.hermes/tools/ffmpeg-9.0.1-darwin-arm64/ffmpeg")


def bolt_points(cx, cy, s):
    """A lightning bolt centered at (cx, cy), bounding size ~s."""
    pts = [(0.542, 0.083), (0.125, 0.583), (0.5, 0.583),
           (0.458, 0.917), (0.875, 0.417), (0.5, 0.417)]
    out = []
    for x, y in pts:
        out.append(f"{cx + (x - 0.5) * s:.1f},{cy + (y - 0.5) * s:.1f}")
    return " ".join(out)


def logo_mark(cx, cy, s, color=INK):
    r = s * 0.62
    return (
        f'<circle cx="{cx}" cy="{cy}" r="{r:.0f}" fill="none" stroke="{color}" stroke-width="{s*0.14:.0f}"/>'
        f'<polygon points="{bolt_points(cx, cy, s * 0.62)}" fill="{color}"/>'
    )


def text(x, y, s, size, weight=400, fill=INK, anchor="start", ls="0", style=""):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{FONT}" '
            f'font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'letter-spacing="{ls}">{s}</text>')


def frame(title, subtitle, diagram, step=None):
    step_label = f"STEP {step} / 12" if step else "BUILD · HAND-CRANK DYNAMO"
    header = (
        f'<rect width="{W}" height="{H}" fill="#ffffff"/>'
        f'<rect x="0" y="0" width="{W}" height="5" fill="{INK}"/>'
        + text(56, 58, "DYNAMO", 22, 700, INK, "start", "0.22em")
        + text(W - 56, 58, step_label, 18, 400, GRAY, "end", "0.14em")
    )
    title_block = (
        text(640, 140, title, 44, 700, INK, "middle")
        + text(640, 178, subtitle, 22, 400, GRAY, "middle")
    )
    footer = text(640, H - 40, "github.com/0xklen/dynamo · electricity from magnets, not magic",
                  18, 400, GRAY, "middle", "0.06em")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}">{header}{title_block}{diagram}{footer}</svg>')


def coil(cx, cy, w, h, color=INK):
    """A flat coil: nested rounded rects."""
    els = []
    n = 7
    for i in range(n):
        f = i / n
        els.append(f'<rect x="{cx - w/2*(1-f)}" y="{cy - h/2*(1-f)}" '
                   f'width="{w*(1-f)}" height="{h*(1-f)}" rx="12" '
                   f'fill="none" stroke="{color}" stroke-width="3"/>')
    return "".join(els)


def magnet(cx, cy, w, h, label, color="#9aa0a6"):
    return (f'<rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" rx="6" fill="{color}"/>'
            f'<text x="{cx}" y="{cy+5}" text-anchor="middle" font-family="{FONT}" '
            f'font-size="18" font-weight="700" fill="#ffffff">{label}</text>')


def arrow(x1, y1, x2, y2, color=GRAY):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="3"/>'
            f'<polygon points="{x2},{y2} {x2-12},{y2-7} {x2-12},{y2+7}" fill="{color}"/>')


# ---- scenes (diagram SVGs drawn in the region y ~ 210..600) ----

def s_title():
    return logo_mark(640, 400, 340)

def s_parts():
    items = ["Magnet wire", "Magnets", "Rotor disc", "Axle + bearing",
             "Bridge rectifier", "Capacitor", "LED", "Multimeter"]
    els = []
    for i, it in enumerate(items):
        col, row = i % 2, i // 2
        x = 360 + col * 400
        y = 250 + row * 90
        els.append(f'<rect x="{x-14}" y="{y-24}" width="24" height="24" rx="6" fill="{HAIR}"/>')
        els.append(text(x + 28, y, it, 26, 400, INK, "start"))
    return "".join(els)

def s_coil():
    return (f'<rect x="470" y="230" width="120" height="320" rx="14" fill="{HAIR}"/>'
            + coil(530, 390, 260, 180)
            + arrow(620, 250, 720, 250)
            + text(730, 258, "wind tight", 22, 400, GRAY))

def s_scrape():
    return (coil(530, 360, 240, 160)
            + f'<line x1="530" y1="470" x2="430" y2="560" stroke="{INK}" stroke-width="5"/>'
            + f'<line x1="530" y1="470" x2="630" y2="560" stroke="{INK}" stroke-width="5"/>'
            + f'<line x1="430" y1="560" x2="380" y2="560" stroke="{COPPER}" stroke-width="9"/>'
            + f'<line x1="630" y1="560" x2="680" y2="560" stroke="{COPPER}" stroke-width="9"/>'
            + text(640, 610, "sand the ends to shiny copper", 24, 400, INK, "middle"))

def s_magnets():
    import math
    els = [f'<circle cx="640" cy="410" r="150" fill="none" stroke="{INK}" stroke-width="4"/>']
    for i in range(8):
        a = math.radians(i * 45 - 90)
        x = 640 + 150 * math.cos(a)
        y = 410 + 150 * math.sin(a)
        lbl = "N" if i % 2 == 0 else "S"
        els.append(magnet(x, y, 44, 44, lbl))
    els.append(text(640, 610, "alternate N and S around the ring", 24, 400, INK, "middle"))
    return "".join(els)

def s_gap():
    return (f'<rect x="380" y="300" width="520" height="46" rx="12" fill="{INK}"/>'
            + text(640, 275, "rotor + magnets", 22, 400, GRAY, "middle")
            + f'<rect x="380" y="470" width="520" height="46" rx="12" fill="{HAIR}" stroke="{INK}" stroke-width="3"/>'
            + text(640, 560, "stator + coils", 22, 400, GRAY, "middle")
            + f'<line x1="920" y1="346" x2="920" y2="470" stroke="{ACCENT}" stroke-width="3"/>'
            + f'<polygon points="912,470 928,470 920,452" fill="{ACCENT}"/>'
            + f'<polygon points="912,346 928,346 920,364" fill="{ACCENT}"/>'
            + text(950, 415, "2-3 mm", 22, 600, ACCENT))

def s_series():
    els = [coil(320, 400, 180, 150), coil(640, 400, 180, 150), coil(960, 400, 180, 150)]
    els.append(f'<line x1="410" y1="400" x2="550" y2="400" stroke="{INK}" stroke-width="4"/>')
    els.append(f'<line x1="730" y1="400" x2="870" y2="400" stroke="{INK}" stroke-width="4"/>')
    els.append(f'<line x1="320" y1="475" x2="230" y2="560" stroke="{INK}" stroke-width="4"/>')
    els.append(f'<line x1="960" y1="475" x2="1050" y2="560" stroke="{INK}" stroke-width="4"/>')
    els.append(text(200, 600, "out A", 20, 600, GRAY))
    els.append(text(1070, 600, "out B", 20, 600, GRAY))
    els.append(text(640, 600, "all coils in series add voltage", 24, 400, INK, "middle"))
    return "".join(els)

def diode_edge(x1, y1, x2, y2, sym=14):
    """A connecting line with a small standard diode symbol (triangle -> bar)
    at its midpoint, oriented along the edge."""
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    px, py = -uy, ux
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    base = (mx - ux * sym, my - uy * sym)
    tip = (mx + ux * sym, my + uy * sym)
    b1 = (base[0] + px * sym, base[1] + py * sym)
    b2 = (base[0] - px * sym, base[1] - py * sym)
    c1 = (tip[0] + px * sym, tip[1] + py * sym)
    c2 = (tip[0] - px * sym, tip[1] - py * sym)
    return (f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{INK}" stroke-width="4"/>'
            f'<polygon points="{b1[0]:.0f},{b1[1]:.0f} {tip[0]:.0f},{tip[1]:.0f} {b2[0]:.0f},{b2[1]:.0f}" fill="{INK}"/>'
            f'<line x1="{c1[0]:.0f}" y1="{c1[1]:.0f}" x2="{c2[0]:.0f}" y2="{c2[1]:.0f}" stroke="{INK}" stroke-width="4"/>')


def s_rectifier():
    L, R, T, B = (420, 430), (860, 430), (640, 300), (640, 560)
    els = [
        diode_edge(*L, *T), diode_edge(*R, *T),   # anodes at AC, cathodes at +
        diode_edge(*B, *L), diode_edge(*B, *R),   # anodes at -, cathodes at AC
    ]
    els.append(f'<line x1="{L[0]-70}" y1="{L[1]}" x2="{L[0]}" y2="{L[1]}" stroke="{INK}" stroke-width="4"/>')
    els.append(f'<line x1="{R[0]}" y1="{R[1]}" x2="{R[0]+70}" y2="{R[1]}" stroke="{INK}" stroke-width="4"/>')
    els.append(f'<line x1="{T[0]}" y1="{T[1]-60}" x2="{T[0]}" y2="{T[1]}" stroke="{INK}" stroke-width="4"/>')
    els.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{B[0]}" y2="{B[1]+60}" stroke="{INK}" stroke-width="4"/>')
    els.append(text(L[0] - 80, L[1] + 8, "AC ~", 22, 600, GRAY, "middle"))
    els.append(text(R[0] + 80, R[1] + 8, "AC ~", 22, 600, GRAY, "middle"))
    els.append(text(T[0], T[1] - 74, "+ DC out", 24, 700, INK, "middle"))
    els.append(text(B[0], B[1] + 92, "− DC out", 24, 700, INK, "middle"))
    return "".join(els)

def s_cap_led():
    # capacitor = two plates, LED = triangle + bar
    return (f'<line x1="480" y1="300" x2="480" y2="480" stroke="{INK}" stroke-width="8"/>'
            f'<line x1="520" y1="300" x2="520" y2="480" stroke="{INK}" stroke-width="8"/>'
            + text(500, 520, "capacitor", 20, 400, GRAY, "middle")
            + f'<polygon points="740,300 820,390 740,480" fill="{ACCENT}"/>'
            + f'<line x1="820" y1="300" x2="820" y2="480" stroke="{INK}" stroke-width="6"/>'
            + text(780, 520, "LED", 20, 400, GRAY, "middle")
            + f'<line x1="560" y1="390" x2="700" y2="390" stroke="{INK}" stroke-width="4"/>'
            + f'<line x1="560" y1="390" x2="700" y2="390" stroke="{INK}" stroke-width="4"/>')

def s_test():
    return (f'<rect x="780" y="300" width="220" height="180" rx="16" fill="{INK}"/>'
            + f'<rect x="800" y="320" width="180" height="60" rx="8" fill="#ffffff"/>'
            + text(890, 362, "3.2 V", 34, 700, INK, "middle")
            + text(890, 420, "~ AC volts", 18, 400, "#9aa0a6", "middle")
            + f'<line x1="820" y1="480" x2="700" y2="560" stroke="{INK}" stroke-width="4"/>'
            + f'<line x1="940" y1="480" x2="1060" y2="560" stroke="{INK}" stroke-width="4"/>'
            + f'<circle cx="400" cy="430" r="90" fill="none" stroke="{INK}" stroke-width="10"/>'
            + f'<line x1="400" y1="430" x2="470" y2="360" stroke="{INK}" stroke-width="10"/>'
            + f'<circle cx="470" cy="360" r="14" fill="{INK}"/>'
            + text(400, 590, "crank + read", 24, 400, INK, "middle"))

def s_store():
    return (f'<rect x="300" y="350" width="280" height="120" rx="14" fill="{HAIR}" stroke="{INK}" stroke-width="3"/>'
            + text(440, 395, "generator", 24, 600, INK, "middle")
            + text(440, 425, "rectified DC", 18, 400, GRAY, "middle")
            + arrow(590, 410, 650, 410)
            + f'<rect x="700" y="350" width="280" height="120" rx="14" fill="{INK}"/>'
            + text(840, 395, "battery", 24, 600, "#ffffff", "middle")
            + text(840, 425, "power bank / 12V", 18, 400, "#9aa0a6", "middle")
            + text(640, 540, "rectify -> regulate -> charge controller -> battery", 22, 400, GRAY, "middle"))

def s_outro():
    return (logo_mark(640, 390, 300)
            + text(640, 590, "scale it: wind · water · solar", 24, 600, INK, "middle"))


STEPS = [
    ("Build a hand-crank generator", "electricity from magnets — no free energy, just physics", s_title, None),
    ("What you need", "a full parts list is in materials.md", s_parts, 1),
    ("Wind the coil", "wrap 100-150 turns around a mandrel, keep them tight", s_coil, 2),
    ("Scrape the wire ends", "the lacquer is insulation — sand it off to bare copper", s_scrape, 3),
    ("Mount the magnets", "glue them in a ring, flipping N/S on every other one", s_magnets, 4),
    ("Fit the axle and air gap", "rotor spins 2-3 mm from the coils — close, not touching", s_gap, 5),
    ("Wire the coils in series", "coil A end -> coil B start, so the voltages add", s_series, 6),
    ("Add the bridge rectifier", "four diodes steer the AC into one-direction DC", s_rectifier, 7),
    ("Capacitor and LED", "the capacitor smooths, the LED shows the power", s_cap_led, 8),
    ("Crank and measure", "spin the rotor and read the multimeter", s_test, 9),
    ("Store the power", "charge a power bank, or a 12V battery via a controller", s_store, 10),
    ("You built a generator", "this is what a power plant does, scaled up", s_outro, None),
]


def main():
    os.makedirs(FRAMES, exist_ok=True)
    for i, (title, sub, scene, step) in enumerate(STEPS, 1):
        svg = frame(title, sub, scene(), step)
        with open(os.path.join(FRAMES, f"frame{i:02d}.svg"), "w") as f:
            f.write(svg)
    # render PNGs
    for i in range(1, len(STEPS) + 1):
        subprocess.run([RESVG, os.path.join(FRAMES, f"frame{i:02d}.svg"),
                        os.path.join(FRAMES, f"frame{i:02d}.png")], check=True)
    # encode: each frame held 5s
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    cmd = [FFMPEG, "-y", "-framerate", "0.2",
           "-i", os.path.join(FRAMES, "frame%02d.png"),
           "-c:v", "libx264", "-r", "30", "-pix_fmt", "yuv420p",
           "-vf", "scale=1280:720", OUT]
    subprocess.run(cmd, check=True, capture_output=True)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
