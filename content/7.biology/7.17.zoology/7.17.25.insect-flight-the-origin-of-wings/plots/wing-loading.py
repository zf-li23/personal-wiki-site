# Wing loading (weight per total wing area) against body mass for representative insects, approximate
# values of body mass and total wing area (both pairs, both sides) from typical published morphology;
# not a fitted dataset. A: log-log plot with an isometric reference line (slope 1/3: geometric similarity
# predicts W/S proportional to m^(1/3)). B: relative specific induced power for hovering, proportional to
# the square root of the loading (Eq. 25.4 with swept area proportional to wing area), scaled to the
# cabbage white butterfly.
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
g = 9.81
# name, mass (kg), total wing area (m^2), asynchronous flight muscle
D = [("Encarsia", 25e-9, 0.5e-6, True), ("Drosophila", 1.0e-6, 3.8e-6, True),
     ("cabbage white", 50e-6, 1500e-6, False), ("honey bee", 100e-6, 50e-6, True),
     ("bumblebee", 175e-6, 80e-6, True), ("dragonfly (Anax)", 1.0e-3, 2000e-6, False),
     ("hawkmoth (Manduca)", 1.6e-3, 1800e-6, False), ("desert locust", 2.0e-3, 3200e-6, False)]
fig, ax = bio.canvas(24, 10)
bio.panel(ax, "A", (0.2, 9.7))
bio.panel(ax, "B", (12.4, 9.7))
a = charts.axes_at(ax, (2.0, 1.6, 8.8, 7.4))
b = charts.axes_at(ax, (15.6, 1.6, 7.6, 7.4))
ref = None
names, rel = [], []
for name, m, S, asyn in D:
    wl = m * g / S
    col = charts.line("negative" if asyn else "channel")
    a.scatter(m * 1e3, wl, s=36, facecolor=col if asyn else "none", edgecolor=col, lw=1.2, zorder=5)
    if name in ("honey bee", "dragonfly (Anax)"):
        a.text(m * 1e3 / 1.25, wl, name, fontsize=7, color=P.ink(), va="center", ha="right")
    else:
        a.text(m * 1e3 * 1.25, wl * 1.05, name, fontsize=7, color=P.ink(), va="center")
    names.append(name)
    rel.append(np.sqrt(wl))
    if name == "cabbage white":
        ref = np.sqrt(wl)
mm = np.logspace(-5, 1, 10)
a.plot(mm, 2.6 * (mm / 1.0e-3) ** (1 / 3), color=P.muted(), ls=(0, (4, 3)), lw=1)
a.set_xscale("log"); a.set_yscale("log")
a.set_xlim(1e-5, 30); a.set_ylim(0.1, 60)
charts.style_axes(a, "Body mass m / g", "Wing loading W/S / (N m$^{-2}$)")
a.text(1.3e-5, 40, "filled: asynchronous flight muscle\nopen: synchronous\ndashed: slope 1/3 (isometry)",
       fontsize=7, color=P.muted(), va="top")
order = np.argsort(rel)
y = np.arange(len(order))
for yi, k in zip(y, order):
    asyn = D[k][3]
    tok = "negative" if asyn else "channel"
    b.barh(yi, rel[k] / ref, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.7, height=0.7)
b.set_yticks(y)
b.set_yticklabels([names[k] for k in order], fontsize=7)
b.set_xlim(0, 9)
charts.style_axes(b, "Relative induced power per unit mass")
