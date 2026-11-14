"""The mesolimbic reward system in a schematic sagittal section of a rat brain (anterior to the left)."""
import numpy as np
from matplotlib.patches import Ellipse, PathPatch
from matplotlib.path import Path

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(22, 11)
# brain outline: forebrain, cerebellum, brainstem
pts = bio.smooth_closed([(1.2, 5.6), (2.5, 8.4), (6, 9.6), (11, 9.7), (14.5, 9.0), (15.8, 8.3), (18.6, 8.6), (20.4, 7.2),
                         (20.6, 5.4), (19.5, 4.2), (21.2, 3.2), (21.0, 2.4), (16, 3.0), (12, 2.7), (8, 2.9), (4, 3.4), (1.8, 4.3)])
ax.add_patch(PathPatch(Path(pts), facecolor=P.fill("cytoplasm"), edgecolor=P.edge("neuron"), lw=1.2, zorder=2))
ax.add_patch(Ellipse((18.4, 6.4), 3.6, 3.4, facecolor=P.fill("extracellular"), edgecolor=P.muted(), lw=0.8, zorder=3))
bio.label(ax, (18.4, 6.4), "cerebellum", size="tiny", color=P.muted())
ax.add_patch(Ellipse((1.6, 5.0), 1.6, 1.2, facecolor=P.fill("extracellular"), edgecolor=P.muted(), lw=0.8, zorder=3))
bio.label(ax, (1.6, 6.0), "olfactory bulb", size="tiny", color=P.muted())

regions = {
    "PFC": ((3.6, 7.3), "receptor", "PFC"),
    "NAc": ((5.4, 4.8), "highlight", "NAc"),
    "VP": ((7.4, 3.8), "neutral", "VP"),
    "Amy": ((10.0, 4.0), "drug", "Amygdala"),
    "Hip": ((8.2, 8.3), "enzyme", "Hippocampus"),
    "LH": ((10.2, 6.0), "metabolite", "LH"),
    "VTA": ((13.0, 4.6), "positive", "VTA"),
    "PPT": ((15.6, 4.2), "channel", "PPT"),
}
for k, (xy, tok, name) in regions.items():
    w = 1.0 + 0.2 * len(name)
    bio.box(ax, xy, w, 0.9, tok, text=name, size="small", zorder=8)


def link(a, b, kind="activation", bend=0.0, color=None, dashed=False):
    bio.arrow(ax, a, b, kind=kind, bend=bend, color=color, dashed=dashed, bg=P.fill("cytoplasm"))


da = P.edge("positive")
link((12.1, 4.9), (6.3, 5.0), kind="process", bend=0.12, color=da)      # VTA -> NAc
link((12.6, 5.15), (4.4, 7.5), kind="process", bend=-0.18, color=da)      # VTA -> PFC
link((3.9, 6.8), (5.0, 5.3))                                             # PFC -> NAc
link((9.6, 4.45), (6.4, 4.7), bend=-0.1)                                 # Amy -> NAc
link((7.7, 7.85), (5.9, 5.3), bend=0.05)                                # Hip -> NAc
link((5.8, 4.3), (7.0, 4.0), kind="inhibition")                          # NAc -| VP
link((10.9, 5.6), (12.4, 5.1), bend=0.0)                               # LH -> VTA
link((14.9, 4.3), (13.9, 4.5))                                           # PPT -> VTA
bio.label(ax, (8.1, 1.9), "dopamine", size="small", color=da, ha="left")
ax.plot([7.0, 7.9], [1.9, 1.9], color=da, lw=1.6)
bio.label(ax, (12.2, 1.9), "other connections", size="small", ha="left")
ax.plot([11.1, 12.0], [1.9, 1.9], color=P.ink(), lw=1.2)
ax.set_ylim(1.2, 10.4)
