# Action at a distance. A: four hypotheses for how an enhancer-bound activator reaches the promoter (schematic).
# B: the catenane experiment (Dunaway and Droge 1989): attP x attB recombination splits one plasmid carrying an
# enhancer (E) and a promoter (P) into two interlocked rings. C: effective concentration of a looped site,
# Eq. (14.3): j = (3 / (2 pi L b))^(3/2) / N_A for a Gaussian chain, naked DNA with Kuhn length b = 100 nm and
# 0.34 nm/bp (dashed below 500 bp, where stiffness invalidates it); for comparison a chromatin-like decay ~ s^-1
# (the Hi-C contact scaling) drawn through the DNA value at 5 kb; shaded: typical nuclear TF concentrations.
import numpy as np
from matplotlib.patches import Circle
import wikibio as bio
from wikibio import charts as C

P = bio.P
fig, ax = bio.canvas(24.0, 13.0)
NA = 6.022e23

# ---- A: four hypotheses
bio.panel(ax, "A", (0.1, 12.9))
bio.label(ax, (0.6, 12.55), "Four hypotheses", size="normal", bold=True, ha="left")
names = ["topology change", "sliding", "looping", "facilitated tracking"]
for k, name in enumerate(names):
    x0, y0 = 0.6 + k * 5.9, 8.4
    bio.label(ax, (x0 + 2.6, y0 + 3.1), name, size="small", bold=True)
    if name == "looping":
        t = np.radians(np.linspace(240, -60, 120))
        ax.plot(x0 + 2.6 + 1.15 * np.cos(t), y0 + 1.7 + 1.15 * np.sin(t), color=P.edge("dna"), lw=2.2)
        ax.plot([x0, x0 + 2.03], [y0 + 0.5, y0 + 0.7], color=P.edge("dna"), lw=2.2)
        ax.plot([x0 + 3.17, x0 + 5.2], [y0 + 0.7, y0 + 0.5], color=P.edge("dna"), lw=2.2)
        bio.box(ax, (x0 + 1.7, y0 + 0.5), 0.6, 0.3, "highlight", None, radius=0.05, zorder=12)
        bio.protein(ax, (x0 + 2.25, y0 + 1.0), 0.8, 0.6, "rna", None, zorder=13)
        bio.protein(ax, (x0 + 3.1, y0 + 0.95), 1.0, 0.7, "enzyme", None, zorder=13)
        bio.label(ax, (x0 + 1.7, y0 + 0.05), "E", size="tiny")
        bio.label(ax, (x0 + 3.4, y0 + 0.05), "P", size="tiny")
        continue
    ax.plot([x0, x0 + 5.2], [y0 + 0.5, y0 + 0.5], color=P.edge("dna"), lw=2.2, zorder=8)
    bio.box(ax, (x0 + 0.9, y0 + 0.5), 0.6, 0.3, "highlight", None, radius=0.05, zorder=12)
    bio.label(ax, (x0 + 0.9, y0 + 0.05), "E", size="tiny")
    bio.protein(ax, (x0 + 4.4, y0 + 1.0), 1.0, 0.7, "enzyme", None, zorder=13)
    bio.label(ax, (x0 + 4.4, y0 + 0.05), "P", size="tiny")
    if name == "topology change":
        t = np.linspace(x0 + 1.4, x0 + 3.8, 200)
        ax.plot(t, y0 + 0.5 + 0.18 * np.sin((t - t[0]) * 9), color=P.edge("dna2"), lw=1.3, zorder=9)
        bio.protein(ax, (x0 + 0.9, y0 + 1.0), 0.8, 0.6, "rna", None, zorder=13)
        bio.label(ax, (x0 + 2.6, y0 + 1.25), "altered DNA structure\npropagates", size="tiny", color=P.muted())
    elif name == "sliding":
        bio.protein(ax, (x0 + 0.9, y0 + 1.0), 0.8, 0.6, "rna", None, zorder=13)
        bio.protein(ax, (x0 + 3.5, y0 + 1.0), 0.8, 0.6, "rna", None, zorder=13)
        bio.arrow(ax, (x0 + 1.45, y0 + 1.5), (x0 + 3.1, y0 + 1.5), kind="process")
    else:
        t = np.linspace(0, np.pi, 50)
        ax.plot(x0 + 1.7 + 0.8 * np.cos(t), y0 + 0.5 + 1.2 * np.sin(t), color=P.edge("dna"), lw=2.2, zorder=9)
        bio.protein(ax, (x0 + 1.75, y0 + 0.95), 1.2, 0.7, "rna", None, zorder=13)
        bio.arrow(ax, (x0 + 2.5, y0 + 1.75), (x0 + 3.7, y0 + 1.75), kind="process")
        bio.label(ax, (x0 + 3.1, y0 + 2.15), "loop grows", size="tiny", color=P.muted())

# ---- B: catenane
bio.panel(ax, "B", (0.1, 7.3))
bio.label(ax, (0.6, 6.95), "The catenane experiment", size="normal", bold=True, ha="left")


def ring(c, r, tok):
    ax.add_patch(Circle(c, r, fill=False, edgecolor=P.edge(tok), lw=2.4, zorder=8))


ring((2.6, 3.4), 1.7, "dna")
for ang, txt, tok in [(90, "E", "highlight"), (270, "P", "enzyme"), (0, "attP", "receptor"), (180, "attB", "receptor")]:
    a = np.radians(ang)
    p = (2.6 + 1.7 * np.cos(a), 3.4 + 1.7 * np.sin(a))
    bio.box(ax, p, 0.75, 0.42, tok, txt, size="tiny", radius=0.06, zorder=12)
bio.arrow(ax, (4.9, 3.4), (6.6, 3.4), kind="process")
bio.label(ax, (5.75, 3.9), "λ integrase", size="tiny")
ring((8.3, 3.4), 1.3, "dna")
ring((10.1, 3.4), 1.3, "dna2")
bio.box(ax, (7.0, 3.4), 0.6, 0.42, "highlight", "E", size="tiny", radius=0.06, zorder=12)
bio.box(ax, (11.4, 3.4), 0.6, 0.42, "enzyme", "P", size="tiny", radius=0.06, zorder=12)
bio.label(ax, (9.2, 1.4), "E and P on interlocked rings:\nP is activated", size="tiny")
bio.label(ax, (9.2, 0.55), "separate rings: no activation", size="tiny", color=P.muted())

# ---- C: effective concentration
c = C.axes_at(ax, (15.2, 1.3, 7.8, 5.3))
s = np.logspace(2, 6, 400)            # bp
b = 100.0                              # nm
L = 0.34 * s
j = (3 / (2 * np.pi * L * b)) ** 1.5 * 1e24 / NA * 1e9   # nM
ok = s >= 500
c.plot(s[ok], j[ok], color=C.line("dna"), lw=2.0, label="naked DNA (Gaussian chain), ∝ $s^{-3/2}$")
c.plot(s[~ok], j[~ok], color=C.line("dna"), lw=1.4, ls=(0, (3, 2)))
j5 = np.interp(5e3, s, j)
c.plot(s, j5 * (5e3 / s), color=C.line("chromatin"), lw=2.0, ls=(0, (5, 2)), label="chromatin-like decay ∝ $s^{-1}$")
c.axhspan(1, 100, color=P.fill("highlight"), alpha=0.35, lw=0)
c.text(1.3e5, 30, "TF concentrations\n1–100 nM", fontsize=bio.core.FONT["tiny"], color=P.muted())
c.plot([3e3], [np.interp(3e3, s, j)], "o", ms=5, mfc=P.fill("dna"), mec=C.line("dna"))
c.text(3.4e3, np.interp(3e3, s, j) * 1.4, "3 kb: ≈17 nM", fontsize=bio.core.FONT["tiny"], color=P.ink())
c.set_xscale("log")
c.set_yscale("log")
c.set_xlim(1e2, 1e6)
c.set_ylim(1e-3, 3e3)
c.set_xticks([1e2, 1e3, 1e4, 1e5, 1e6], ["100 bp", "1 kb", "10 kb", "100 kb", "1 Mb"])
C.style_axes(c, "enhancer–promoter separation $s$", "effective concentration $j$ / nM")
c.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "C", (13.6, 7.3))
bio.label(ax, (14.1, 6.95), "Effective concentration of a looped enhancer", size="normal", bold=True, ha="left")
