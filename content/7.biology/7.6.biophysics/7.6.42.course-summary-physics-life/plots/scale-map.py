"""A map of the models of the course on axes of length and time.

Each point marks the characteristic length and time of a process treated by a model of the course,
labelled with the chapter (7.6.n) where it is developed; colours mark the three directions
(molecular, cell, quantitative biology). Values are those of the chapters: retinal isomerization
200 fs, rotational correlation 14 ns for a = 2.5 nm, a kinesin step of 8 nm every 10 ms, an F1 step
of 120 degrees at 130 Hz, a Min oscillation of 60 s across a 3 um cell, a mitotic trigger wave of
60 um/min, an action potential at about 20 m/s, a doubling time near an hour, MscL
channels relieving an osmotic shock in about 100 ms. Evolution (41) is a
band: it has no length scale of its own. The diagonal lines are the two clocks that recur
throughout: diffusion, t = L^2/(6D), for a small molecule in water (D = 1000 um^2/s) and a protein
in cytoplasm (D = 10 um^2/s), and directed transport at v = 1 um/s, t = L/v; for the protein the
crossover lies at L* = 6D/v = 60 um (7.6.5)."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

import wikibio as bio
from wikibio import charts

P = bio.P
F = bio.core.FONT
M, C, Q = "protein", "membrane", "dna"

# (label, L [m], t [s], part, label offset in points (dx, dy), ha)
pts = [
    ("bond vibrations, MD step (6, 15)", 1.5e-10, 1e-14, M, (6, 0), "left"),
    ("retinal isomerization (18)", 1.5e-9, 2e-13, M, (6, 0), "left"),
    ("Förster transfer (11, 18)", 5e-9, 1e-9, M, (6, -2), "left"),
    ("rotational diffusion (5, 13)", 2.5e-9, 1.4e-8, M, (-6, 4), "right"),
    ("electron transfer (18)", 1e-9, 1e-7, M, (-6, 0), "right"),
    ("radical pairs (19)", 2.5e-9, 1e-6, M, (6, 0), "left"),
    ("channel gating, MWC (4, 30)", 5e-9, 1e-3, M, (6, -7), "left"),
    ("folding (16)", 3e-9, 1e-1, M, (-6, 0), "right"),
    ("bond rupture, Jarzynski (17)", 2e-8, 1e0, M, (-6, 6), "right"),
    ("F₁ step (28)", 1.2e-8, 2.6e-3, C, (6, -4), "left"),
    ("kinesin step (27)", 8e-9, 1e-2, C, (6, 2), "left"),
    ("MscL osmotic valve (25)", 1e-6, 1.2e-1, C, (-6, 2), "right"),
    ("subdiffusion of mRNA (23)", 3e-7, 3e0, C, (6, 0), "left"),
    ("vesicle budding (24)", 1e-7, 6e1, C, (-6, 0), "right"),
    ("swimming at low Re (22)", 2e-6, 8e-2, C, (6, 0), "left"),
    ("search and capture (26)", 1e-5, 1.2e3, C, (6, 4), "left"),
    ("cell migration (31)", 5e-5, 6e3, C, (6, 0), "left"),
    ("condensate coarsening (29)", 2e-6, 1e6, C, (6, 0), "left"),
    ("action potential (30)", 2e-2, 1e-3, C, (6, 0), "left"),
    ("run and tumble (35)", 2e-5, 1e0, Q, (6, -9), "left"),
    ("Min oscillation (36)", 3e-6, 6e1, Q, (6, 0), "left"),
    ("mitotic trigger wave (36)", 1e-3, 1e3, Q, (6, 0), "left"),
    ("mRNA, protein noise (32)", 1.5e-6, 3e2, Q, (-6, 0), "right"),
    ("doubling, growth laws (39)", 1e-6, 2.5e3, Q, (-6, 0), "right"),
    ("cell cycle (34)", 5e-6, 5.4e3, Q, (6, 4), "left"),
    ("circadian clock (33)", 1.5e-6, 8.6e4, Q, (-6, 0), "right"),
    ("bacterial vortices (37)", 5e-5, 1e0, Q, (6, 7), "left"),
    ("bird flocks (37)", 5e1, 1e0, Q, (-6, 0), "right"),
]

fig, ax = plt.subplots(figsize=(10.0, 6.8))
fig.subplots_adjust(left=0.09, right=0.97, bottom=0.09, top=0.93)

ax.add_patch(Rectangle((1e-10, 1e5), 1e2, 1e10, facecolor=P.fill(Q), edgecolor="none", alpha=0.18, zorder=1))
ax.text(3e-3, 3e8, "evolution of populations (41): days to billions of years", fontsize=F["tiny"],
        color=P.ink(), ha="center", zorder=6)

L = np.logspace(-10, 2, 200)
ax.plot(L, L ** 2 / (6 * 1e-9), color=P.muted(), lw=0.9, ls="--", zorder=2)
ax.plot(L, L ** 2 / (6 * 1e-11), color=P.muted(), lw=0.9, ls="--", zorder=2)
ax.plot(L, L / 1e-6, color=P.muted(), lw=0.9, ls=":", zorder=2)
ax.text(4e-2, 6e4, "diffusion, small molecule", fontsize=F["tiny"], color=P.muted(), rotation=0, ha="left")
ax.text(1.2e-3, 3.5e4, "diffusion, protein", fontsize=F["tiny"], color=P.muted(), ha="left")
ax.text(1.5e1, 4e5, "motor, 1 µm/s", fontsize=F["tiny"], color=P.muted(), ha="left")
ax.plot([6e-5], [6e1], "x", color=P.muted(), ms=5, zorder=3)
ax.annotate("L* = 6D/v", (6e-5, 6e1), xytext=(-6, -12), textcoords="offset points", fontsize=F["tiny"],
            color=P.muted(), ha="right")

for lab, x, t, tok, (dx, dy), ha in pts:
    ax.plot([x], [t], "o", ms=5.5, mfc=P.fill(tok), mec=P.edge(tok), mew=0.9, zorder=5)
    ax.annotate(lab, (x, t), xytext=(dx, dy), textcoords="offset points", fontsize=F["tiny"], color=P.ink(),
                ha=ha, va="center", zorder=6)

ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1e-10, 1e2)
ax.set_ylim(3e-15, 1e10)
ax.set_xticks([10.0 ** e for e in range(-10, 3)])
ax.set_xticklabels(["0.1 nm", "1 nm", "10 nm", "100 nm", "1 µm", "10 µm", "100 µm", "1 mm", "1 cm", "10 cm",
                    "1 m", "10 m", "100 m"])
ax.set_yticks([1e-15, 1e-12, 1e-9, 1e-6, 1e-3, 1e0, 3.6e3, 8.64e4, 3.15e7])
ax.set_yticklabels(["1 fs", "1 ps", "1 ns", "1 µs", "1 ms", "1 s", "1 h", "1 day", "1 year"])
ax.minorticks_off()
charts.style_axes(ax, "length", "time")
for i, (tok, lab) in enumerate(((M, "molecular biophysics"), (C, "cell biophysics"), (Q, "quantitative biology"))):
    y = 3e-14 * 30.0 ** (-i)
    ax.plot([1e-1], [y * 1e3], "o", ms=6, mfc=P.fill(tok), mec=P.edge(tok), mew=0.9)
    ax.annotate(lab, (1e-1, y * 1e3), xytext=(7, 0), textcoords="offset points", fontsize=F["tiny"],
                color=P.ink(), va="center")
charts.title(ax, "Processes and models of the course by length and time (chapters 7.6.n)")
