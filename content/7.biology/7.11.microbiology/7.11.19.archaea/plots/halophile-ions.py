"""The salt-in strategy of Halobacterium salinarum. A: ion concentrations in the medium and in the cells
(data from Christian and Waltho 1962, as tabulated by Madigan et al. 2019): the cells exclude Na+ and
accumulate K+ to a concentration higher than that of Na+ outside, with Cl- as the main counter-ion.
B: schematic of a cell. K+ is taken up and Na+ exported; the glycoprotein S-layer, rich in acidic amino
acids, is stabilized by Na+ outside; the cytoplasmic proteins are acidic and require high K+;
bacteriorhodopsin, made when O2 is scarce, pumps protons out in the light, and ATP synthase uses the
proton gradient."""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(24, 9)
bio.panel(ax, "A", (0.2, 8.8))
bio.panel(ax, "B", (11.0, 8.8))
pax = charts.axes_at(ax, (1.8, 1.6, 7.6, 6.4))
ions = ["Na$^+$", "K$^+$", "Mg$^{2+}$", "Cl$^-$"]
med = [4.0, 0.032, 0.13, 4.0]
cel = [1.4, 4.6, 0.12, 3.6]
x = np.arange(4)
pax.bar(x - 0.2, med, 0.38, color=P.fill("extracellular"), edgecolor=P.edge("extracellular"), label="medium")
pax.bar(x + 0.2, cel, 0.38, color=P.fill("k"), edgecolor=P.edge("k"), label="cells")
pax.set_xticks(x)
pax.set_xticklabels(ions)
pax.legend(fontsize=7, frameon=False)
charts.style_axes(pax, None, "concentration / M")

# B: cell schematic
ax.add_patch(FancyBboxPatch((12.6, 2.0), 9.6, 5.0, boxstyle="round,pad=0,rounding_size=1.2",
                            facecolor=P.light("cytoplasm"), edgecolor=P.edge("membrane"), lw=2.2, zorder=3))
ax.add_patch(FancyBboxPatch((12.35, 1.75), 10.1, 5.5, boxstyle="round,pad=0,rounding_size=1.35", fill=False,
                            edgecolor=P.edge("cell_wall"), lw=1.0, ls=(0, (2, 1.5)), zorder=3))
bio.label(ax, (17.4, 7.65), "S-layer: acidic glycoprotein stabilized by Na+", size="tiny", color=P.edge("cell_wall"))
bio.label(ax, (17.4, 4.6), "cytoplasm: about 4-5 M K+", size="small")
bio.label(ax, (17.4, 4.05), "acidic proteins, K+-dependent ribosomes", size="tiny", color=P.muted())
# bacteriorhodopsin and ATP synthase on top membrane
bio.box(ax, (14.6, 7.0), 1.3, 0.7, token="receptor", text="BR", size="small", zorder=8)
bio.arrow(ax, (14.6, 6.6), (14.6, 8.2), kind="process", color=P.edge("h"))
bio.label(ax, (15.0, 8.25), "H+", size="tiny", ha="left")
bio.arrow(ax, (13.4, 8.6), (14.2, 7.5), kind="process", color=P.edge("highlight"))
bio.label(ax, (13.1, 8.6), "light", size="tiny", ha="right", color=P.edge("highlight"))
bio.box(ax, (20.2, 7.0), 1.3, 0.7, token="atp_synthase", text="ATPase", size="tiny", zorder=8)
bio.arrow(ax, (20.2, 8.2), (20.2, 6.6), kind="process", color=P.edge("h"))
bio.label(ax, (20.6, 8.25), "H+", size="tiny", ha="left")
bio.label(ax, (20.2, 5.9), "ADP + Pi -> ATP", size="tiny")
# K+ in, Na+ out at bottom
bio.box(ax, (15.4, 2.0), 1.2, 0.6, token="channel", text="K+", size="tiny", zorder=8)
bio.arrow(ax, (15.4, 0.9), (15.4, 2.9), kind="process", color=P.edge("k"))
bio.box(ax, (19.4, 2.0), 1.2, 0.6, token="enzyme", text="Na+", size="tiny", zorder=8)
bio.arrow(ax, (19.4, 2.9), (19.4, 0.9), kind="process", color=P.edge("na"))
bio.label(ax, (17.4, 0.7), "outside: about 4 M NaCl", size="small")
