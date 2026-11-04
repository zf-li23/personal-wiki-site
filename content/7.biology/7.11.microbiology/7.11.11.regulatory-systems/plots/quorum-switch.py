"""Quorum sensing in Vibrio (Aliivibrio) fischeri and a minimal model of its switch.
A: the lux circuit. LuxI synthesizes the acyl homoserine lactone 3-oxo-C6-HSL (dots), which crosses the
   membrane freely; bound to LuxR it activates the luxICDABEG operon (luciferase and the enzymes that
   make its aldehyde substrate), and therefore more LuxI: a positive feedback loop.
B: steady states of the scaled model da/dt = rho (1 + beta h(a)) - a, h(a) = a^2 / (1 + a^2), with
   beta = 20: autoinducer a against scaled cell density rho. Solid: stable, dashed: unstable. Between the
   two saddle-node points the system is bistable; arrows mark the jumps (hysteresis).
C: a culture growing logistically (rho, grey) switches abruptly when rho crosses the upper fold; without
   feedback (beta = 0) the signal and the output rise gradually."""

import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch

import wikibio as bio
from wikibio import charts
from wikibio import genetics as G

P = bio.P
fig, ax = bio.canvas(27.0, 9.4)
bio.panel(ax, "A", (0.2, 9.3))

# cell
ax.add_patch(FancyBboxPatch((0.8, 0.9), 8.6, 6.6, boxstyle="round,pad=0,rounding_size=1.6",
                            facecolor=P.fill("cytoplasm"), edgecolor=P.edge("bacterium"), lw=2.0, zorder=1))
bio.label(ax, (1.4, 7.1), "cell", size="tiny", color=P.muted(), ha="left")
gl = G.construct(ax, 1.4, 2.0, [{"kind": "cds", "text": "luxR", "width": 1.6, "token": "dna", "reverse": True},
                                {"kind": "promoter", "reverse": True}, {"kind": "operator"}, {"kind": "promoter"},
                                {"kind": "cds", "text": "luxI", "width": 1.4, "token": "dna"},
                                {"kind": "cds", "text": "CDABEG", "width": 2.4, "token": "dna"}], unit=0.45, gap=0.06)
bio.label(ax, (gl[2]["centre"], 1.35), "lux box", size="tiny", color=P.muted())


def protein(xy, text, token):
    bio.box(ax, xy, 1.4, 0.7, token=token, text=text, size="tiny", radius=0.3, zorder=12)


def ahl(xy, r=0.16):
    ax.add_patch(Circle(xy, r, facecolor=P.fill("metabolite"), edgecolor=P.edge("metabolite"), lw=0.8, zorder=13))


protein((gl[4]["centre"], 4.0), "LuxI", "enzyme")
protein((gl[0]["centre"] + 0.2, 4.0), "LuxR", "positive")
bio.arrow(ax, (gl[4]["centre"], 2.45), (gl[4]["centre"], 3.6), kind="process", lw=1.0, head=0.18)
bio.arrow(ax, (gl[0]["centre"] + 0.2, 2.45), (gl[0]["centre"] + 0.2, 3.6), kind="process", lw=1.0, head=0.18)
for xy in [(5.9, 5.0), (6.4, 5.4), (5.4, 5.6), (3.7, 5.0)]:
    ahl(xy)
bio.arrow(ax, (gl[4]["centre"] + 0.2, 4.4), (6.0, 4.85), kind="process", lw=0.9, head=0.15)
ahl((gl[0]["centre"] + 0.8, 4.35))
bio.arrow(ax, (3.5, 4.95), (gl[0]["centre"] + 0.95, 4.5), kind="link", lw=0.9)
bio.arrow(ax, (gl[0]["centre"] + 0.6, 3.65), (gl[2]["centre"], 2.45), kind="activation", lw=1.1, head=0.2)
bio.label(ax, (1.6, 3.0), "LuxR-AHL", size="tiny", color=P.muted())
for xy in [(10.3, 6.2), (10.8, 4.7), (10.2, 3.2), (11.0, 7.4), (9.9, 8.1)]:
    ahl(xy)
bio.arrow(ax, (6.7, 5.6), (9.8, 6.3), kind="process", lw=0.9, head=0.15, bend=0.1)
bio.arrow(ax, (10.0, 4.4), (7.0, 4.9), kind="process", lw=0.9, head=0.15, bend=0.1)
bio.label(ax, (10.6, 8.75), "AHL diffuses\nfreely", size="tiny", color=P.muted())
bio.label(ax, (7.2, 1.35), "luciferase → light", size="tiny", color=P.edge("highlight"))

# model
beta = 20.0
h = lambda a: a ** 2 / (1 + a ** 2)
a = np.logspace(-3, np.log10(30), 2000)
rho = a / (1 + beta * h(a))
d = np.gradient(rho, a)
stable = d > 0
bio.panel(ax, "B", (12.0, 9.3))
pax = charts.axes_at(ax, (13.5, 1.6, 5.3, 6.6))
for seg in np.split(np.arange(a.size), np.where(np.diff(stable))[0] + 1):
    st = stable[seg[0]]
    pax.plot(rho[seg], a[seg], color=charts.line("protein" if st else "neutral"), lw=2.0 if st else 1.3,
             ls="-" if st else "--")
u = np.roots([1 + beta, 2 - beta, 1])
af = np.sqrt(np.sort(u))
rf = af / (1 + beta * h(af))
pax.annotate("", xy=(rf[0], 1.8), xytext=(rf[0], af[0]),
             arrowprops=dict(arrowstyle="->", color=P.edge("positive"), lw=1.2))
pax.annotate("", xy=(rf[1], 0.12), xytext=(rf[1], af[1]),
             arrowprops=dict(arrowstyle="->", color=P.edge("negative"), lw=1.2))
pax.set_xscale("log")
pax.set_yscale("log")
pax.set_xlim(0.01, 1)
pax.set_ylim(0.005, 30)
charts.style_axes(pax, "scaled cell density ρ", "autoinducer a")
charts.title(pax, "Bistable switch (β = 20)")

# C: growing culture
bio.panel(ax, "C", (20.0, 9.3))
cax = charts.axes_at(ax, (21.5, 1.6, 5.2, 6.6))
t = np.linspace(0, 12, 3000)
r_t = 0.002 * np.exp(0.8 * t) / (1 + 0.002 * (np.exp(0.8 * t) - 1))
for b, ls, tok, name in ((beta, "-", "highlight", "with feedback"), (0.0, "--", "dna", "no feedback")):
    x = np.zeros_like(t)
    x[0] = 0.002
    dt = t[1] - t[0]
    for k in range(1, t.size):
        x[k] = x[k - 1] + dt * 6.0 * (r_t[k - 1] * (1 + b * h(x[k - 1])) - x[k - 1])
    out = h(x)
    cax.plot(t, out, color=charts.line(tok), lw=2.0, ls=ls, label=f"output h(a), {name}")
cax.plot(t, r_t, color=charts.line("neutral"), lw=1.3, ls=":", label="cell density ρ")
cax.set_xlim(0, 12)
cax.set_ylim(0, 1.05)
cax.legend(fontsize=6.6, frameon=False, loc="upper left")
charts.style_axes(cax, "time (a.u.)", "level")
charts.title(cax, "A growing culture")
