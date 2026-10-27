# One current model of the origin of the eukaryotic cell (after Imachi et al. 2020 and Baum & Baum 2014; a
# hypothesis, not an observation). 1: an Asgard archaeon with membrane protrusions lives in close metabolic
# partnership with an alpha-proteobacterium. 2: the protrusions surround the bacterium. 3: fusion of the
# protrusions encloses the endosymbiont; the internal membranes become the endomembrane system and the
# nuclear envelope. 4: the last eukaryotic common ancestor (LECA), with nucleus, ER and mitochondria.
# 5: in the plant lineage a cyanobacterium is engulfed later and becomes the chloroplast.
import numpy as np
from matplotlib.patches import Circle, PathPatch
from matplotlib.path import Path

import wikibio as bio
from wikibio import microbio

P = bio.P
fig, ax = bio.canvas(26, 8.6)


def body(center, rx, ry, token, seed, z=4, wobble=0.05):
    o = bio.blob(center, rx, ry, wobble=wobble, seed=seed, k=9)
    ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill(token), edgecolor=P.edge(token), lw=1.4, zorder=z))
    return o


def protrusions(center, r, n, length, seed, token="cytoplasm"):
    rng = np.random.default_rng(seed)
    for k in range(n):
        a = 2 * np.pi * k / n + rng.uniform(-0.2, 0.2)
        L = length * rng.uniform(0.7, 1.1)
        x0, y0 = center[0] + r * np.cos(a), center[1] + r * np.sin(a)
        x1, y1 = center[0] + (r + L) * np.cos(a), center[1] + (r + L) * np.sin(a)
        ax.plot([x0, x1], [y0, y1], color=P.edge(token), lw=5.0, solid_capstyle="round", zorder=3)
        ax.plot([x0, x1], [y0, y1], color=P.fill(token), lw=3.4, solid_capstyle="round", zorder=3.1)


def dna_loop(center, rx, ry, token="dna"):
    t = np.linspace(0, 2 * np.pi, 200)
    ax.plot(center[0] + rx * np.cos(t) + 0.06 * np.sin(6 * t), center[1] + ry * np.sin(t), color=P.edge(token), lw=1.0, zorder=9)


y = 4.8
# 1. partnership
body((2.6, y), 1.3, 1.2, "cytoplasm", 1)
protrusions((2.6, y), 1.2, 9, 0.9, 1)
dna_loop((2.6, y), 0.5, 0.35, "nucleus")
microbio.bacillus(ax, (4.6, y - 1.8), 1.0, 0.5, angle=30, token="mitochondrion")
bio.label(ax, (2.6, 1.3), "1  Asgard archaeon\n+ α-proteobacterium", size="small")

# 2. engulfment
body((8.2, y), 1.4, 1.3, "cytoplasm", 2)
protrusions((8.2, y), 1.3, 7, 0.8, 2)
for a in (-0.3, 0.3, 0.9):
    ax.plot([8.2 + 1.3 * np.cos(a), 9.9 + 0.7 * np.cos(a + 0.2)], [y + 1.3 * np.sin(a), y + 0.7 * np.sin(a + 0.2)],
            color=P.edge("cytoplasm"), lw=5.0, solid_capstyle="round", zorder=3)
    ax.plot([8.2 + 1.3 * np.cos(a), 9.9 + 0.7 * np.cos(a + 0.2)], [y + 1.3 * np.sin(a), y + 0.7 * np.sin(a + 0.2)],
            color=P.fill("cytoplasm"), lw=3.4, solid_capstyle="round", zorder=3.1)
microbio.bacillus(ax, (10.0, y + 0.25), 1.0, 0.5, angle=10, token="mitochondrion", zorder=6)
dna_loop((7.9, y), 0.5, 0.35, "nucleus")
bio.label(ax, (8.6, 1.3), "2  protrusions\nsurround the partner", size="small")

# 3. enclosure and internal membranes
o = body((14.0, y), 1.9, 1.7, "cytoplasm", 3)
t = np.linspace(0.3, 2 * np.pi - 0.3, 100)
ax.plot(13.6 + 0.75 * np.cos(t), y + 0.2 + 0.6 * np.sin(t), color=P.edge("nucleus"), lw=1.6, zorder=8)
ax.plot(13.6 + 0.62 * np.cos(t), y + 0.2 + 0.48 * np.sin(t), color=P.edge("nucleus"), lw=0.9, zorder=8)
dna_loop((13.6, y + 0.2), 0.35, 0.22, "nucleus")
microbio.bacillus(ax, (14.8, y - 0.9), 0.9, 0.45, angle=-10, token="mitochondrion", zorder=7)
ax.add_patch(Circle((14.8, y - 0.9), 0.62, fill=False, edgecolor=P.edge("cytoplasm"), lw=0.9, ls=(0, (2, 1.5)), zorder=7))
bio.label(ax, (14.0, 1.3), "3  endosymbiont enclosed;\ninner membranes form", size="small")

# 4. LECA
body((20.0, y), 2.0, 1.8, "cytoplasm", 4)
bio.nucleus(ax, (19.5, y + 0.35), 0.75, pores=7, nucleolus=False)
bio.er(ax, (20.9, y + 0.9), 0.9, 0.5, sheets=2, angle=-30)
bio.mitochondrion(ax, (20.6, y - 0.9), 0.85, 0.36, angle=15)
bio.mitochondrion(ax, (19.0, y - 1.0), 0.75, 0.34, angle=-30)
bio.label(ax, (20.0, 1.3), "4  last eukaryotic\ncommon ancestor", size="small")

# 5. plant lineage
body((24.4, y + 1.6), 1.25, 1.1, "cytoplasm", 5)
bio.nucleus(ax, (24.0, y + 2.0), 0.45, pores=5, nucleolus=False, chromatin=False)
bio.chloroplast(ax, (24.7, y + 1.1), 0.9, 0.4, angle=15, grana=3)
bio.label(ax, (24.4, y - 0.1), "5  + cyanobacterium:\nchloroplast (plants, algae)", size="small")

for a, b in (((5.0, y), (6.4, y)), ((10.9, y - 0.6), (11.9, y - 0.6)), ((16.1, y), (17.8, y))):
    bio.arrow(ax, a, b, kind="process")
bio.arrow(ax, (22.1, y + 0.6), (23.0, y + 1.3), kind="process")
