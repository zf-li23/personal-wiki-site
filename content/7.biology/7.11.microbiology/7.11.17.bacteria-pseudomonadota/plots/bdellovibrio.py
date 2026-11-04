"""The predatory life cycle of Bdellovibrio bacteriovorus and a simple model of predation.
A: an attack-phase cell swims to a Gram-negative prey cell, attaches by its non-flagellated pole, opens
a pore in the outer membrane and enters the periplasm; the prey rounds up into a bdelloplast. Inside, the
predator digests the prey's contents and grows into a long filament, which divides at several sites at
once into progeny that develop flagella and are released when the prey cell lyses (about 3-4 h at 30 C).
B: Formula 17.6.1 solved for prey suspended in buffer (no prey growth), 1e8 prey cells per mL, three
initial ratios of predator to prey; solid lines are prey not yet attacked, dashed lines free predators (illustrative parameters: k = 2e-8 mL/h, tau = 3.5 h, Y = 4 progeny per
prey, m = 0.02 per h)."""
import numpy as np
from matplotlib.patches import Circle, Ellipse
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(26, 10)
bio.panel(ax, "A", (0.2, 9.8))
bio.panel(ax, "B", (15.0, 9.8))

cx, cy, R = 7.2, 5.0, 3.3
angles = [90, 30, -30, -90, -150, 150]
pts = [(cx + R * np.cos(np.radians(a)), cy + R * np.sin(np.radians(a))) for a in angles]
steps = ["attack phase", "attachment", "entry into periplasm", "growth as a filament",
         "septation", "lysis and release"]
for i in range(6):
    a0, a1 = np.radians(angles[i] - 17), np.radians(angles[(i + 1) % 6] + 17)
    p0 = (cx + R * np.cos(a0), cy + R * np.sin(a0))
    p1 = (cx + R * np.cos(a1), cy + R * np.sin(a1))
    bio.arrow(ax, p0, p1, kind="process", bend=-0.18, color=P.muted())


def prey(c, rounded=False):
    if rounded:
        ax.add_patch(Ellipse(c, 1.9, 1.6, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=1.1, zorder=6))
        ax.add_patch(Ellipse(c, 1.55, 1.25, fill=False, edgecolor=P.edge("neutral"), lw=0.7, ls="--", zorder=6))
    else:
        M.bacillus(ax, c, 2.0, 0.8, token="neutral")


x, y = pts[0]
M.vibrio(ax, (x, y), 0.8, 0.3, angle=0, flagella="monotrichous", flagellum_length=0.8)
x, y = pts[1]
prey((x, y))
M.vibrio(ax, (x - 0.15, y + 0.62), 0.7, 0.28, angle=95, flagella="monotrichous", flagellum_length=0.6)
x, y = pts[2]
prey((x, y), rounded=True)
M.vibrio(ax, (x + 0.3, y + 0.25), 0.6, 0.26, angle=-20, flagella=None)
x, y = pts[3]
prey((x, y), rounded=True)
t = np.linspace(-0.55, 0.55, 40)
ax.plot(x + t, y + 0.25 * np.sin(5 * t), color=P.edge("gram_neg"), lw=4.5, solid_capstyle="round", zorder=8)
x, y = pts[4]
prey((x, y), rounded=True)
for k in range(5):
    tt = np.linspace(-0.6 + k * 0.26, -0.6 + k * 0.26 + 0.13, 10)
    ax.plot(x + tt, y + 0.25 * np.sin(5 * tt), color=P.edge("gram_neg"), lw=4.5, solid_capstyle="round", zorder=8)
x, y = pts[5]
for k, (dx, dy, a) in enumerate([(-0.6, 0.5, 30), (0.5, 0.6, -20), (-0.7, -0.4, 160), (0.4, -0.5, 200), (0.0, 0.0, 80)]):
    M.vibrio(ax, (x + dx, y + dy), 0.6, 0.25, angle=a, flagella="monotrichous", flagellum_length=0.5)
lab = [(0, 1.0, "center"), (1.6, 0.0, "left"), (1.6, 0.0, "left"), (0, -1.3, "center"), (-1.6, 0.0, "right"),
       (-1.6, 0.0, "right")]
for (dx, dy, ha), (x, y), s in zip(lab, pts, steps):
    bio.label(ax, (x + dx, y + dy), s, size="small", ha=ha)
bio.label(ax, (cx, cy + 0.2), "about 3-4 h", size="small", color=P.muted())
bio.label(ax, (cx, cy - 0.35), "3-6 progeny per prey", size="small", color=P.muted())

# B: model
k, tau, Y, m = 2e-8, 3.5, 4.0, 0.02


def rhs(t, z):
    N, B, Pr = z
    a = k * N * Pr
    return [-a, a - B / tau, Y * B / tau - a - m * Pr]


pax = charts.axes_at(ax, (16.8, 1.6, 8.6, 7.4))
tt = np.linspace(0, 24, 400)
for ratio, tok in [(0.01, "dna"), (0.1, "enzyme"), (1.0, "negative")]:
    s = solve_ivp(rhs, (0, 24), [1e8, 0, 1e8 * ratio], t_eval=tt, rtol=1e-8, atol=1.0)
    N, B, Pr = s.y
    pax.plot(tt, np.maximum(N, 1), color=charts.line(tok), lw=1.6, label=f"free prey, predator:prey = {ratio:g}")
    pax.plot(tt, np.maximum(Pr, 1), color=charts.line(tok), lw=1.2, ls="--")
pax.set_yscale("log")
pax.set_ylim(1e1, 3e9)
pax.set_xlim(0, 24)
pax.set_xticks([0, 6, 12, 18, 24])
pax.plot([], [], color=P.muted(), ls="--", lw=1.2, label="free predators (dashed)")
pax.legend(fontsize=6.8, frameon=False, loc="lower right")
charts.style_axes(pax, "time / h", "cells per mL")
