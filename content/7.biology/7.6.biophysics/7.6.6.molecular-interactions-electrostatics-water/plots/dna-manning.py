"""Counterion condensation on DNA. A: cross-section of B-DNA (radius 1 nm, one phosphate charge per
0.17 nm of length, so the Manning parameter is xi = l_B/b = 4.2): about three quarters of the
phosphate charge is neutralized by counterions held close to the backbone (condensed layer),
and the rest is screened by the diffuse ionic atmosphere beyond, over a Debye length. B: fraction
of the line charge neutralized by condensed counterions of valence z, theta = 1 - 1/(z xi) for
z xi > 1, against xi, with single- and double-stranded DNA and F-actin marked. C: salt
dependence of the binding constant of a protein that forms Z ion pairs with DNA:
d lg K / d lg[M+] = -0.88 Z (counterion release), shown for Z = 3, 6 and 10 with K normalized at
0.1 M."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import wikibio as bio
from wikibio import charts

P = bio.P
fig = plt.figure(figsize=(10.5, 3.5))
axA = fig.add_axes([0.02, 0.08, 0.27, 0.82])
axB = fig.add_axes([0.40, 0.16, 0.25, 0.72])
axC = fig.add_axes([0.73, 0.16, 0.25, 0.72])

ax = axA
ax.set_xlim(-3.2, 3.2)
ax.set_ylim(-3.2, 3.2)
ax.set_aspect("equal")
ax.axis("off")
ax.add_patch(Circle((0, 0), 3.0, facecolor=P.fill("extracellular"), edgecolor="none", zorder=0))
ax.add_patch(Circle((0, 0), 1.45, facecolor=P.mix(P.fill("na"), P.surface(), 0.75), edgecolor="none", zorder=1))
ax.add_patch(Circle((0, 0), 1.0, facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=1.0, zorder=2))
ang = np.linspace(0, 2 * np.pi, 12, endpoint=False)
for k, t in enumerate(ang):
    ax.add_patch(Circle((0.92 * np.cos(t), 0.92 * np.sin(t)), 0.13, facecolor=P.fill("negative"), edgecolor=P.edge("negative"),
                        lw=0.6, zorder=3))
    ax.text(0.92 * np.cos(t), 0.92 * np.sin(t), "−", ha="center", va="center", fontsize=6, color=P.on_fill(), zorder=4)
    if k % 4 != 3:
        tt = t + 0.25
        ax.add_patch(Circle((1.22 * np.cos(tt), 1.22 * np.sin(tt)), 0.11, facecolor=P.fill("na"), edgecolor=P.edge("na"),
                            lw=0.6, zorder=3))
rng = np.random.default_rng(2)
for _ in range(26):
    rr, tt = rng.uniform(1.7, 2.9), rng.uniform(0, 2 * np.pi)
    cation = rng.uniform() < 0.62
    tok = "na" if cation else "cl"
    ax.add_patch(Circle((rr * np.cos(tt), rr * np.sin(tt)), 0.1, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.5, zorder=3))
bio.label(ax, (0, 0), "B-DNA\n(end view)", size="tiny", color=P.on_fill())
bio.callout(ax, (1.25, -0.6), (2.1, -3.05), "condensed layer", size="tiny")
bio.callout(ax, (-2.2, -1.5), (-1.9, -3.05), "diffuse atmosphere", size="tiny")
ax.text(-3.1, 3.1, "A", fontsize=bio.core.FONT["title"], weight="bold", color=P.ink(), va="top")

ax = axB
xi = np.linspace(0.2, 6, 300)
for z, tok in ((1, "na"), (2, "mg"), (3, "protein")):
    th = np.where(z * xi > 1, 1 - 1 / (z * xi), 0)
    ax.plot(xi, th, color=charts.line(tok), lw=1.8, label=f"z = {z}")
for xv, txt in ((1.2, "ssDNA"), (2.8, "F-actin"), (4.2, "dsDNA")):
    ax.axvline(xv, color=P.muted(), lw=0.5, ls=":")
    ax.text(xv + 0.07, 0.03, txt, fontsize=bio.core.FONT["tiny"], color=P.ink(), rotation=90, va="bottom")
ax.set_ylim(0, 1)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"Manning parameter $\xi = \ell_\mathrm{B}/b$", "fraction neutralized")
charts.title(ax, r"B  $\theta = 1 - 1/z\xi$")

ax = axC
salt = np.logspace(-2.3, 0, 200)
for Z, tok in ((3, "neutral"), (6, "enzyme"), (10, "blood")):
    ax.plot(salt, -0.88 * Z * np.log10(salt / 0.1), color=charts.line(tok), lw=1.8, label=f"Z = {Z} ion pairs")
ax.axhline(0, color=P.muted(), lw=0.5)
ax.set_xscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, r"$[\mathrm{Na^+}]$ / M", r"$\lg[K(c)/K(0.1\,\mathrm{M})]$")
charts.title(ax, "C  Counterion release")
