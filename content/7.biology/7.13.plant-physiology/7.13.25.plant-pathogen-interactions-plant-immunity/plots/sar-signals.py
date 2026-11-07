# Systemic acquired resistance (SAR). A: a local infection that triggers ETI/HR produces mobile signals
# (N-hydroxypipecolic acid NHP and its precursor pipecolic acid Pip, methyl salicylate MeSA, azelaic acid AzA,
# glycerol-3-phosphate G3P, dehydroabietinal DA; the lipid-transfer protein DIR1 is needed for their phloem
# movement). In distal leaves NHP and SA amplify each other's synthesis (ALD1-SARD4-FMO1 for NHP, ICS1 for SA);
# SA-bound NPR1 enters the nucleus and with TGA transcription factors induces PR genes (PR1, PR2, PR5).
# B: schematic time course after inoculation of one leaf (local SA peaks within about a day; systemic SA and
# resistance develop over 1-2 days and resistance lasts for weeks), modelled with gamma-shaped curves.
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(25.0, 12.0)
bio.panel(ax, "A", (0.3, 11.8))

# a simple rosette-like plant: stem and leaves
stem = [(6.0, 0.8), (6.0, 10.5)]
ax.plot(*zip(*stem), color=P.edge("plant"), lw=4, solid_capstyle="round", zorder=4)
ax.plot([6.0, 6.0], [0.8, 10.5], color=P.edge("phloem"), lw=1.6, ls=(0, (2, 2)), zorder=5)
import matplotlib.patches as mp


def leaf(cx, cy, ang, token, w=4.2, h=1.6):
    ax.add_patch(mp.Ellipse((cx, cy), w, h, angle=ang, facecolor=P.fill(token), edgecolor=P.edge(token), lw=1.2,
                            zorder=3))


leaf(4.05, 2.3, 20, "plant")     # local, infected
leaf(7.95, 5.0, -20, "plant")
leaf(4.05, 7.9, 20, "plant")
leaf(7.95, 9.6, -20, "plant")
for k in range(5):
    ax.add_patch(mp.Circle((2.9 + 0.45 * k, 1.95 + 0.18 * k), 0.17, facecolor=P.fill("negative"),
                           edgecolor=P.edge("negative"), lw=0.8, zorder=6))
bio.label(ax, (3.6, 0.9), "local leaf: infection, ETI, HR", size="small", bold=True)
bio.label(ax, (3.6, 0.4), "SA and Pip/NHP accumulate", size="tiny")
for (x, y) in [(4.05, 7.9), (7.95, 9.6), (7.95, 5.0)]:
    bio.label(ax, (x, y), "SAR", size="small", bold=True, color=P.on_fill())
bio.label(ax, (11.0, 10.9), "distal leaves: primed, PR proteins", size="small", bold=True, ha="right")
bio.arrow(ax, (5.3, 2.9), (5.85, 3.9), kind="process", zorder=8)
bio.arrow(ax, (6.3, 3.6), (6.3, 7.2), kind="process", zorder=8)
sig = ["NHP / Pip", "MeSA", "AzA, G3P", "DA", "(DIR1)"]
for i, t in enumerate(sig):
    bio.label(ax, (5.75, 5.75 - 0.42 * i), t, size="tiny", ha="right")
bio.label(ax, (5.75, 6.25), "phloem signals", size="tiny", ha="right", bold=True)

# distal-cell circuit
x0 = 13.2
bio.box(ax, (x0, 10.6), 2.2, 0.65, token="metabolite", text="NHP", size="small")
bio.box(ax, (x0 + 4.2, 10.6), 2.2, 0.65, token="drug", text="SA", size="small")
bio.arrow(ax, (x0 + 1.15, 10.75), (x0 + 3.05, 10.75), kind="activation")
bio.arrow(ax, (x0 + 3.05, 10.45), (x0 + 1.15, 10.45), kind="activation")
bio.label(ax, (x0, 9.95), "ALD1 → SARD4 → FMO1", size="tiny")
bio.label(ax, (x0 + 3.5, 9.95), "ICS1 (isochorismate)", size="tiny")
bio.protein(ax, (x0 + 5.0, 8.6), 1.5, 0.7, "protein", text="NPR1", size="tiny")
bio.arrow(ax, (x0 + 5.0, 10.25), (x0 + 5.0, 9.0), kind="activation")
bio.label(ax, (x0 + 5.5, 9.55), "binds SA; monomers", size="tiny", ha="left")
bio.label(ax, (x0 + 5.5, 9.2), "enter the nucleus", size="tiny", ha="left")
bio.nucleus(ax, (x0 + 2.2, 7.4), 1.0, pores=6, chromatin=False, nucleolus=False)
bio.label(ax, (x0 + 2.2, 7.55), "TGA + NPR1", size="tiny", bold=True)
bio.label(ax, (x0 + 2.2, 7.15), "PR1, PR2, PR5", size="tiny", italic=True)
bio.arrow(ax, (x0 + 4.25, 8.4), (x0 + 3.1, 7.8), kind="activation")
bio.label(ax, (x0 + 5.9, 7.4), "antimicrobial PR proteins,\nprimed defence", size="tiny", ha="left")

# B: time course
bio.panel(ax, "B", (12.0, 5.9))
pax = charts.axes_at(ax, (13.8, 1.0, 10.6, 4.3))
t = np.linspace(0, 21, 600)


def g(t, k, th):
    y = (t / th) ** k * np.exp(-(t - k * th) / th) / k ** k
    return y


local_sa = g(t, 3, 0.35)
sys_sa = 0.45 * g(t, 4, 0.55)
res = 1 / (1 + np.exp(-(t - 1.8) / 0.35)) * np.exp(-np.clip(t - 6, 0, None) / 20)
pax.plot(t, local_sa, color=charts.line("drug"), lw=2, label="SA, local leaf")
pax.plot(t, sys_sa, color=charts.line("drug"), lw=2, ls="--", label="SA, distal leaf")
pax.plot(t, res, color=charts.line("positive"), lw=2.2, label="resistance of distal leaves")
pax.set_xlim(0, 21)
pax.set_ylim(0, 1.15)
pax.set_yticks([])
pax.legend(frameon=False, fontsize=7.5, loc="upper right", labelcolor=P.ink())
charts.style_axes(pax, "Time after local inoculation / d", "Relative level")
