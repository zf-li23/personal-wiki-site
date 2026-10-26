"""The optimization model of glycogen structure (Melendez-Hevia, Waddell and Shelton 1993).

A particle has t tiers of chains of g_c residues; every inner (B) chain carries two branches, the outer
tier consists of unbranched A chains. Then C_A = 2^(t-1), C_T = 2^t - 1, G_T = g_c C_T,
G_PT = (g_c - 4) C_A (phosphorylase stops 4 residues from a branch point), tier thickness
0.12 g_c + 0.35 nm, particle volume V_s = (4/3) pi t^3 (0.12 g_c + 0.35)^3 nm^3, and the quality
function f = G_T C_A G_PT / V_s, whose maximum in g_c does not depend on t.
A: a particle with 5 tiers (schematic; B chains blue, A chains green). B: f against g_c, normalized.
C: glucose residues per particle and, for g_c = 13, the volume fraction of the outermost tier occupied by
glucose residues (0.18 nm^3 per residue, from a density of 1.5 g/cm^3): it would exceed 1 beyond 13 tiers.
"""

import numpy as np
from matplotlib.patches import Circle

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(25.0, 9.6)

# --- A: tier schematic ----------------------------------------------------------------------------
bio.panel(ax, "A", (0.3, 9.2))
c = np.array([4.0, 4.6])
T, R = 5, 0.78


def grow(p, ang, tier, spread):
    q = c + (tier) * R * np.array([np.cos(ang), np.sin(ang)])
    outer = tier == T
    ax.plot([p[0], q[0]], [p[1], q[1]], color=P.edge("carbohydrate" if outer else "dna"), lw=1.6 if outer else 2.0,
            solid_capstyle="round", zorder=10)
    if not outer:
        for s in (-1, 1):
            grow(q, ang + s * spread / 2, tier + 1, spread / 2)


for k in range(2):  # the glycogenin dimer primes two chains
    grow(c, np.pi / 2 + k * np.pi, 1, np.pi)
ax.add_patch(Circle(c, 0.22, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=1.0, zorder=12))
for t in range(1, T + 1):
    ax.add_patch(Circle(c, t * R, fill=False, edgecolor=P.muted(), lw=0.5, ls=(0, (2, 2)), zorder=5))
bio.label(ax, (c[0], 0.35), "glycogenin core; tiers of chains\n(B chains with 2 branches, A chains outermost)",
          size="tiny", color=P.muted())

# --- B: quality function ---------------------------------------------------------------------------
g = np.linspace(5, 40, 600)
f = g * (g - 4) / (0.12 * g + 0.35) ** 3
B = charts.axes_at(ax, (10.0, 1.4, 5.8, 6.8))
B.plot(g, f / f.max(), color=charts.line("carbohydrate"), lw=2.0)
gopt = g[f.argmax()]
B.axvline(gopt, color=P.muted(), lw=0.8, ls="--")
B.text(gopt + 0.6, 0.15, f"optimum $g_c$ = {gopt:.1f}", fontsize=bio.core.FONT["tiny"], color=P.ink())
B.axvspan(12, 14, color=P.fill("highlight"), alpha=0.3, lw=0)
B.text(13, 1.04, "observed", ha="center", fontsize=bio.core.FONT["tiny"], color=P.muted())
B.set_xlim(5, 40)
B.set_ylim(0, 1.1)
charts.style_axes(B, "residues per chain, $g_c$", "quality function $f$ (relative)")
bio.panel(ax, "B", (8.4, 9.2))

# --- C: size and crowding against the number of tiers ---------------------------------------------------
t = np.arange(4, 15)
d = 0.12 * 13 + 0.35
GT = 13 * (2.0**t - 1)
frac = 13 * 2.0 ** (t - 1) * 0.18 / (4 / 3 * np.pi * d**3 * (t**3 - (t - 1) ** 3))
C = charts.axes_at(ax, (18.0, 1.4, 5.8, 6.8))
C.semilogy(t, GT, "o-", color=charts.line("dna"), lw=1.8, ms=4, label="glucose residues $G_T$")
C.set_ylim(50, 5e5)
C2 = C.twinx()
C2.plot(t, frac, "s--", color=charts.line("negative"), lw=1.8, ms=4, label="outer tier filled (fraction)")
C2.axhline(1, color=charts.line("negative"), lw=0.8)
C2.set_ylim(0, 1.4)
C.axvline(12, color=P.muted(), lw=0.8, ls="--")
C.set_xlim(4, 14.5)
charts.style_axes(C, "number of tiers, t", "glucose residues per particle")
charts.style_axes(C2, None, "volume fraction of outer tier", box=True)
h1, l1 = C.get_legend_handles_labels()
h2, l2 = C2.get_legend_handles_labels()
C.legend(h1 + h2, l1 + l2, frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "C", (16.4, 9.2))
