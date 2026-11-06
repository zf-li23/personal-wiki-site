# Physiology of a legume root nodule. A: oxygen concentration along a radius of the nodule (schematic profile):
# air-saturated in the outer cortex (about 250 uM), falling steeply across the variable oxygen diffusion barrier in
# the inner cortex to 20-40 nM in the central infected zone, where leghemoglobin (Km for O2 about 10 nM)
# carries O2 to the bacteroid oxidase (Km about 7 nM). B: exchange in an infected cell: sucrose from the phloem
# is broken down and converted via PEP carboxylase to malate, which is taken up by the bacteroids inside the
# symbiosome; nitrogenase reduces N2 to NH3 (16 ATP and 8 electrons per N2, one H2 released); NH3/NH4+ crosses
# the symbiosome membrane and is assimilated by GS-GOGAT in the host cytosol and plastids; temperate legumes export
# the nitrogen in the xylem as amides (asparagine, glutamine), tropical legumes as ureides (allantoin, allantoic acid).
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch

import wikibio as bio
from wikibio import charts

P = bio.P
fig = plt.figure(figsize=(14.5, 5.6))
axA = fig.add_axes([0.06, 0.16, 0.30, 0.72])
r = np.linspace(0, 1, 400)  # 0 centre, 1 surface
barrier = 0.72
o2 = np.where(r > barrier + 0.06, 250, 0.03 + (250 - 0.03) / (1 + np.exp(-(r - barrier - 0.02) / 0.012)))
axA.axvspan(0, 0.66, color=P.fill("rna"), alpha=0.35, lw=0)
axA.axvspan(0.68, 0.78, color=P.fill("neutral"), alpha=0.6, lw=0)
axA.plot(r, o2, color=charts.line("dna"), lw=2.2)
axA.set_yscale("log")
axA.set_ylim(0.01, 1000)
axA.set_xlim(0, 1)
axA.text(0.33, 0.2, "infected zone\n20–40 nM O$_2$\n(leghemoglobin)", ha="center", fontsize=7.2, color=P.ink())
axA.text(0.73, 400, "diffusion\nbarrier", ha="center", fontsize=7, color=P.ink())
axA.text(0.9, 20, "outer\ncortex", ha="center", fontsize=7, color=P.ink())
charts.style_axes(axA, "relative distance from nodule centre", "free O$_2$ / µM")
charts.title(axA, "A   Oxygen profile")

ax = fig.add_axes([0.40, 0.02, 0.58, 0.96])
ax.set_xlim(0, 20)
ax.set_ylim(0, 10)
ax.set_aspect("equal")
ax.axis("off")
bio.panel(ax, "B", (0.1, 9.7))
bio.label(ax, (0.7, 9.65), "Infected cell", size="title", ha="left", va="top")
ax.add_patch(FancyBboxPatch((1.0, 1.0), 13.0, 7.8, boxstyle="round,pad=0,rounding_size=0.6", facecolor=P.fill("cytoplasm"),
                            edgecolor=P.edge("cell_wall"), lw=2.0, zorder=1))
for k, (cx, cy) in enumerate([(4.0, 5.6), (7.5, 4.0), (10.6, 6.0), (5.2, 2.6), (11.2, 2.8)]):
    ax.add_patch(Ellipse((cx, cy), 2.6, 1.5, facecolor=P.fill("vesicle"), edgecolor=P.edge("membrane"), lw=1.2, zorder=3))
    ax.add_patch(Ellipse((cx, cy), 1.8, 0.85, facecolor=P.fill("bacterium"), edgecolor=P.edge("bacterium"), lw=1.0, zorder=4))
bio.label(ax, (7.5, 4.0), "bacteroid", size="tiny")
bio.callout(ax, (10.6 + 1.25, 6.3), (13.0, 7.9), "symbiosome membrane")
# nitrogenase reaction in the central bacteroid
bio.label(ax, (7.5, 5.25), "N₂ + 8 H⁺ + 8 e⁻ + 16 ATP → 2 NH₃ + H₂", size="tiny", bold=True)
# leghemoglobin dots
rng = np.random.default_rng(3)
for _ in range(40):
    x, y = rng.uniform(1.6, 13.4), rng.uniform(1.4, 8.4)
    if all(np.hypot(x - cx, (y - cy) * 1.6) > 1.6 for cx, cy in [(4.0, 5.6), (7.5, 4.0), (10.6, 6.0), (5.2, 2.6), (11.2, 2.8)]):
        ax.add_patch(Circle((x, y), 0.09, facecolor=P.fill("blood"), edgecolor="none", zorder=2))
bio.label(ax, (2.6, 8.2), "leghemoglobin (O₂ carrier)", size="tiny", color=P.edge("blood"), ha="left")
# inputs and outputs
bio.arrow(ax, (16.5, 7.6), (13.2, 7.0), kind="process")
bio.label(ax, (17.6, 8.0), "sucrose\n(phloem)", size="small")
bio.label(ax, (12.0, 6.95), "malate", size="tiny")
bio.arrow(ax, (12.2, 6.6), (11.6, 6.25), kind="process")
bio.arrow(ax, (8.6, 3.7), (13.6, 2.2), kind="process", color=P.edge("rna"))
bio.label(ax, (11.6, 3.55), "NH₄⁺ → GS–GOGAT", size="tiny", color=P.edge("rna"))
bio.arrow(ax, (13.9, 2.0), (16.6, 2.0), kind="process", color=P.edge("rna"))
bio.label(ax, (17.9, 2.9), "xylem export", size="small", bold=True)
bio.label(ax, (17.9, 2.0), "temperate: Asn, Gln", size="tiny")
bio.label(ax, (17.9, 1.5), "tropical: ureides", size="tiny")
bio.arrow(ax, (16.6, 5.0), (13.8, 5.0), kind="process", color=P.edge("dna"))
bio.label(ax, (17.6, 5.3), "O₂ (low)", size="small", color=P.edge("dna"))
bio.arrow(ax, (1.2, 4.2), (-0.3, 4.2), kind="process", dashed=True, color=P.muted())
bio.label(ax, (0.5, 3.6), "H₂", size="tiny", color=P.muted())
