# Wound- and herbivore-induced defence (schematic). A caterpillar chews a leaf: damage plus elicitors in its
# oral secretions (fatty acid-amino acid conjugates such as volicitin) trigger Ca2+ fluxes and MAPKs; jasmonic
# acid is made from linolenic acid (13-LOX, AOS, AOC -> OPDA in the chloroplast; OPR3 and beta-oxidation in the
# peroxisome) and conjugated to JA-Ile by JAR1; JA-Ile joins COI1 and JAZ, JAZ is degraded and MYC2 activates
# defence genes. Outputs: direct defences (proteinase inhibitors, polyphenol oxidase, nicotine, glucosinolates)
# and indirect defences (herbivore-induced volatiles: terpenoids, green-leaf volatiles, methyl salicylate) that
# attract parasitoid wasps and prime neighbouring plants. GLR3.3/3.6-dependent electrical signals carry the
# alarm to other leaves at up to about 9 cm per minute (Mousavi et al. 2013).
import matplotlib.patches as mp
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26.0, 12.0)

# plant: stem and two leaves
ax.plot([3.2, 3.2], [0.6, 10.8], color=P.edge("plant"), lw=4, solid_capstyle="round", zorder=3)
ax.add_patch(mp.Ellipse((5.4, 8.6), 4.6, 1.8, angle=15, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.2, zorder=4))
ax.add_patch(mp.Ellipse((5.2, 3.6), 4.4, 1.7, angle=12, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.2, zorder=4))
# bite marks on upper leaf
for k in range(3):
    ax.add_patch(mp.Circle((7.15 + 0.15 * k, 9.45 - 0.33 * k), 0.28, facecolor=P.surface(), edgecolor="none", zorder=5))
# caterpillar
for k in range(7):
    ax.add_patch(mp.Circle((5.0 + 0.38 * k, 9.75 + 0.06 * np.sin(k)), 0.24 if k else 0.27, facecolor=P.fill("animal"),
                           edgecolor=P.edge("animal"), lw=0.9, zorder=6))
bio.label(ax, (5.9, 10.55), "chewing caterpillar", size="small")
bio.label(ax, (5.9, 7.0), "wounded leaf", size="tiny", color=P.muted())
bio.label(ax, (5.2, 2.1), "distal leaf: defences induced", size="tiny", color=P.muted())
# electrical signal along the stem
bio.arrow(ax, (3.55, 7.6), (3.55, 4.6), kind="process", dashed=True)
bio.label(ax, (2.9, 6.6), "electrical", size="tiny", ha="right")
bio.label(ax, (2.9, 6.2), "signal", size="tiny", ha="right")
bio.label(ax, (2.9, 5.8), "GLR3.3/3.6", size="tiny", ha="right", italic=False)
bio.label(ax, (2.9, 5.35), "≤ 9 cm min⁻¹", size="tiny", ha="right")

# signalling chain (cell)
x0 = 13.0
bio.box(ax, (x0, 10.9), 5.4, 0.75, token="neutral", text="wounding + oral secretions (FACs)", size="small")
bio.box(ax, (x0, 9.6), 5.4, 0.75, token="ca", text="Ca²⁺ influx, CPKs, MAPKs", size="small")
bio.box(ax, (x0, 8.3), 5.4, 0.75, token="chloroplast", text="18:3 → 13-LOX, AOS, AOC → OPDA", size="small")
bio.box(ax, (x0, 7.0), 5.4, 0.75, token="peroxisome", text="OPR3, β-oxidation → JA", size="small")
bio.box(ax, (x0, 5.7), 5.4, 0.75, token="drug", text="JAR1: JA → JA-Ile", size="small")
bio.box(ax, (x0, 4.4), 5.4, 0.75, token="protein", text="COI1-JAZ: JAZ degraded → MYC2", size="small")
for y in (10.5, 9.2, 7.9, 6.6, 5.3):
    bio.arrow(ax, (x0, y), (x0, y - 0.5), kind="process")
bio.label(ax, (x0 + 2.9, 8.3), "chloroplast", size="tiny", ha="left", color=P.muted())
bio.label(ax, (x0 + 2.9, 7.0), "peroxisome", size="tiny", ha="left", color=P.muted())
bio.arrow(ax, (8.0, 9.6), (10.2, 10.6), kind="process")

# outputs
bio.box(ax, (10.0, 2.2), 5.6, 1.4, token="positive", text=None)
bio.label(ax, (10.0, 2.6), "Direct defence", size="small", bold=True, color=P.on_fill())
bio.label(ax, (10.0, 2.0), "proteinase inhibitors, PPO,", size="tiny", color=P.on_fill())
bio.label(ax, (10.0, 1.65), "nicotine, glucosinolates", size="tiny", color=P.on_fill())
bio.box(ax, (17.0, 2.2), 5.6, 1.4, token="highlight", text=None)
bio.label(ax, (17.0, 2.6), "Indirect defence", size="small", bold=True, color=P.on_fill())
bio.label(ax, (17.0, 2.0), "volatiles: terpenoids, GLVs,", size="tiny", color=P.on_fill())
bio.label(ax, (17.0, 1.65), "methyl salicylate; EFN", size="tiny", color=P.on_fill())
bio.arrow(ax, (12.0, 4.0), (10.6, 2.95), kind="activation")
bio.arrow(ax, (14.0, 4.0), (16.4, 2.95), kind="activation")

# volatile plume, wasp and neighbour
for k, (x, y) in enumerate([(20.3, 3.2), (20.9, 3.9), (21.5, 4.6), (22.1, 5.3), (22.7, 6.0)]):
    ax.add_patch(mp.Circle((x, y), 0.12 + 0.03 * k, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.6, zorder=6))
# wasp: head, thorax, abdomen, wings
wx, wy = 23.6, 7.4
ax.add_patch(mp.Ellipse((wx + 0.9, wy - 0.15), 1.1, 0.42, angle=-15, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=1, zorder=7))
ax.add_patch(mp.Circle((wx, wy), 0.26, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=1, zorder=7))
ax.add_patch(mp.Circle((wx - 0.42, wy + 0.05), 0.18, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=1, zorder=7))
ax.add_patch(mp.Ellipse((wx + 0.25, wy + 0.5), 1.1, 0.4, angle=25, facecolor=P.light("channel"), edgecolor=P.edge("channel"), lw=0.8, zorder=6))
ax.plot([wx - 0.55, wx - 0.95], [wy + 0.15, wy + 0.55], color=P.edge("animal"), lw=1)
bio.label(ax, (wx + 0.3, wy + 1.55), "parasitoid wasp", size="small")
bio.label(ax, (wx + 0.3, wy + 1.15), "lays eggs in the caterpillar", size="tiny", color=P.muted())
bio.arrow(ax, (22.9, 6.3), (23.3, 6.9), kind="activation")
ax.plot([24.6, 24.6], [0.6, 4.2], color=P.edge("plant"), lw=3.2, solid_capstyle="round", zorder=3)
ax.add_patch(mp.Ellipse((23.6, 3.6), 2.0, 0.8, angle=-20, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.1, zorder=4))
bio.label(ax, (24.6, 0.25), "neighbour: primed", size="tiny")
