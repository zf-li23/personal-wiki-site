"""Conjugation in Spirogyra (schematic). A: scalariform conjugation between two filaments; the stages run
from left to right (vegetative cells, papillae meet, a gamete passes through the conjugation tube, zygotes
in the lower, female filament; the upper, male filament is left with empty cells). B: lateral
conjugation between neighbouring cells of one filament: empty cells alternate with zygote-containing
cells. C: the zygote rests with a thick wall; at germination meiosis gives four nuclei, three degenerate,
and the survivor grows into a new filament."""
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(32, 14)
CW, CH = 2.0, 1.0  # cell length and width


def cellbox(x, y, empty=False, z=4):
    bio.shape(ax, [[x, y - CH / 2], [x + CW, y - CH / 2], [x + CW, y + CH / 2], [x, y + CH / 2]],
              token="cell_wall", lw=1.0, zorder=z)
    bio.shape(ax, [[x + 0.06, y - CH / 2 + 0.06], [x + CW - 0.06, y - CH / 2 + 0.06], [x + CW - 0.06, y + CH / 2 - 0.06],
                   [x + 0.06, y + CH / 2 - 0.06]], token="extracellular" if empty else "vacuole", lw=0, zorder=z + 1)


def spiral(x, y, z=7):
    t = np.linspace(0, 1, 120)
    xs = x + 0.1 + t * (CW - 0.2)
    ys = y + 0.36 * np.sin(2 * np.pi * 2.2 * t)
    ax.plot(xs, ys, color=P.edge("chloroplast"), lw=3.2, zorder=z, solid_capstyle="round")
    ax.plot(xs, ys, color=P.fill("chloroplast"), lw=2.0, zorder=z + 0.1, solid_capstyle="round")
    for k in range(5):  # pyrenoids along the band
        i = 10 + k * 23
        bio.shape(ax, np.c_[xs[i] + 0.06 * np.cos(np.linspace(0, 6.3, 12)), ys[i] + 0.06 * np.sin(np.linspace(0, 6.3, 12))],
                  token="enzyme", lw=0.4, zorder=z + 0.2)
    bio.shape(ax, np.c_[x + CW / 2 + 0.12 * np.cos(np.linspace(0, 6.3, 20)), y + 0.1 * np.sin(np.linspace(0, 6.3, 20))],
              token="nucleus", lw=0.6, zorder=z + 0.3)


def blob(c, rx, ry, token="chloroplast", z=8):
    t = np.linspace(0, 2 * np.pi, 40)
    bio.shape(ax, np.c_[c[0] + rx * np.cos(t), c[1] + ry * np.sin(t)], token=token, lw=0.8, zorder=z)


def zygote(c, z=8):
    blob(c, 0.48, 0.34, token="animal", z=z)
    blob(c, 0.34, 0.22, token="lipid", z=z + 1)


def tube(x, y0, y1, w=0.34, z=3):
    bio.shape(ax, [[x - w / 2, y0], [x + w / 2, y0], [x + w / 2, y1], [x - w / 2, y1]], token="cell_wall", lw=0.8, zorder=z)


# ---------------- A: scalariform ----------------
bio.panel(ax, "A", (0.2, 13.8))
bio.label(ax, (8.0, 13.3), "Scalariform conjugation", size="normal", bold=True)
YT, YB = 10.6, 7.6
x0 = 1.2
for i in range(7):
    x = x0 + i * CW
    stage = i // 2 if i < 6 else 3
    cellbox(x, YT, empty=(i >= 4))
    cellbox(x, YB)
    cx = x + CW / 2
    if i < 2:
        spiral(x, YT)
        spiral(x, YB)
    elif i < 4:
        # papillae fused into a tube; gametes contracting / passing
        tube(cx, YB + CH / 2, YT - CH / 2)
        if i == 2:
            blob((cx, YT), 0.6, 0.32)
            blob((cx, YB), 0.6, 0.32)
        else:
            blob((cx, (YT + YB) / 2 + 0.25), 0.16, 0.45)
            blob((cx, YB), 0.6, 0.32)
            bio.arrow(ax, (cx + 0.4, YT - 0.2), (cx + 0.4, YB + 0.35), kind="process", head=0.15, color=P.muted())
    else:
        tube(cx, YB + CH / 2, YT - CH / 2)
        zygote((cx, YB))
bio.label(ax, (x0 - 0.2, YT), "♂", size="normal", ha="right")
bio.label(ax, (x0 - 0.2, YB), "♀", size="normal", ha="right")
bio.callout(ax, (x0 + 0.7, YT + 0.3), (x0 + 1.2, YT + 1.6), "Spiral chloroplast", size="small")
bio.callout(ax, (x0 + 5 * CW, (YT + YB) / 2), (x0 + 5 * CW + 0.6, YT + 1.6), "Conjugation tube", size="small")
bio.callout(ax, (x0 + 3 * CW + CW / 2, (YT + YB) / 2 + 0.25), (x0 + 3 * CW - 0.2, YT + 1.6), "Gamete moving", size="small")
bio.callout(ax, (x0 + 4 * CW + CW / 2, YB - 0.2), (x0 + 4 * CW + 1.2, YB - 1.4), "Zygote", size="small")
bio.callout(ax, (x0 + 6 * CW + 1.0, YT), (x0 + 6 * CW + 1.6, YT + 1.6), "Empty cell", size="small")

# ---------------- B: lateral ----------------
bio.panel(ax, "B", (17.2, 13.8))
bio.label(ax, (24.0, 13.3), "Lateral conjugation", size="normal", bold=True)
YL = 9.1
x1 = 18.0
for i in range(6):
    x = x1 + i * CW
    cellbox(x, YL, empty=(i % 2 == 0))
    if i % 2 == 1:
        zygote((x + CW / 2, YL))
for i in (1, 3, 5):  # tube bulging around the cross wall
    xc = x1 + i * CW
    t = np.linspace(0, np.pi, 30)
    ax.plot(xc + 0.55 * np.cos(t), YL - CH / 2 - 0.35 * np.sin(t), color=P.edge("cell_wall"), lw=1.0, zorder=3)
bio.callout(ax, (x1 + CW + 0.1, YL - 0.82), (x1 + CW + 0.6, YL - 2.1), "Tube across the cross wall", size="small")
bio.callout(ax, (x1 + 1.0, YL), (x1 + 0.4, YL + 1.6), "Empty cell", size="small")
bio.callout(ax, (x1 + 3 * CW + 1.0, YL), (x1 + 3 * CW + 1.6, YL + 1.6), "Zygote", size="small")

# ---------------- C: zygote germination ----------------
bio.panel(ax, "C", (0.2, 5.0))
bio.label(ax, (16.0, 4.6), "Zygote: rest, meiosis, germination", size="normal", bold=True)
xs = [4.0, 10.0, 16.0, 23.0]
for k, x in enumerate(xs):
    c = (x, 2.2)
    if k < 3:
        blob(c, 0.9, 0.62, token="animal", z=4)
        blob(c, 0.7, 0.45, token="lipid" if k == 0 else "chloroplast", z=5)
    if k == 0:
        bio.label(ax, (x, 0.9), "Thick-walled zygote (2n)", size="small")
    if k == 1:
        for dx, dy in ((-0.3, 0.15), (0.3, 0.15), (-0.3, -0.18), (0.3, -0.18)):
            blob((x + dx, 2.2 + dy), 0.11, 0.11, token="nucleus", z=7)
        bio.label(ax, (x, 0.9), "Meiosis: 4 nuclei (n)", size="small")
    if k == 2:
        blob((x, 2.2), 0.15, 0.15, token="nucleus", z=7)
        for dx, dy in ((-0.4, 0.2), (0.4, 0.2), (0.0, -0.3)):
            blob((x + dx, 2.2 + dy), 0.07, 0.07, token="neutral", z=7)
        bio.label(ax, (x, 0.9), "3 nuclei degenerate", size="small")
    if k == 3:
        blob((x - 2.0, 2.2), 0.9, 0.62, token="animal", z=4)
        for j in range(3):
            cellbox(x - 1.4 + j * CW, 2.2)
            spiral(x - 1.4 + j * CW, 2.2)
        bio.label(ax, (x + 1.6, 0.9), "Germination: new filament (n)", size="small")
for a, b in zip(xs[:-1], xs[1:]):
    bio.arrow(ax, (a + 1.4, 2.2), (b - (3.4 if b == xs[-1] else 1.3), 2.2), kind="process", head=0.18)
