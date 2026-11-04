# Three fates of a bacterium taken up by a macrophage: killed, held in a modified vacuole, or free in the cytosol.
import numpy as np
from matplotlib.patches import Circle, Rectangle

import wikibio as bio
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(19.0, 8.4)
bio.label(ax, (9.5, 8.15), "What happens after a macrophage engulfs a bacterium", size="title", bold=True)

W = 5.9


def frame(x0, letter, title, subtitle):
    bio.panel(ax, letter, (x0 - 0.15, 7.6))
    ax.add_patch(Rectangle((x0, 0.5), W, 6.8, facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=0))
    bio.label(ax, (x0 + W / 2, 7.55), title, size="small", bold=True)
    bio.label(ax, (x0 + W / 2, 7.18), subtitle, size="tiny", color=P.muted())
    bio.label(ax, (x0 + 0.15, 0.72), "macrophage cytoplasm", size="tiny", color=P.muted(), ha="left")


def phagosome(center, r, token="vesicle", bacteria=1, gram="-"):
    bio.vesicle(ax, center, r, token=token)
    for k in range(bacteria):
        M.bacillus(ax, (center[0] + (k - (bacteria - 1) / 2) * 0.55, center[1]), 0.85, 0.32,
                   angle=20 * (k % 2), gram=gram)


# ================================================================ A: killed
X = 0.3
frame(X, "A", "The normal course", "maturation and killing")
phagosome((X + W / 2, 6.0), 0.85)
bio.label(ax, (X + W / 2, 5.0), "phagosome", size="tiny", color=P.muted())
bio.arrow(ax, (X + W / 2, 4.85), (X + W / 2, 4.45), kind="process")
bio.box(ax, (X + W / 2, 4.05), 4.6, 0.75, token="lysosome", radius=0.15)
bio.label(ax, (X + W / 2, 4.05), "v-ATPase pumps H⁺: pH ≈ 4.5", size="tiny", color=P.on_fill())
bio.arrow(ax, (X + W / 2, 3.6), (X + W / 2, 3.25), kind="process")
bio.box(ax, (X + W / 2, 2.85), 4.6, 0.75, token="lysosome", radius=0.15)
bio.label(ax, (X + W / 2, 2.85), "fusion with lysosomes", size="tiny", color=P.on_fill())
bio.arrow(ax, (X + W / 2, 2.4), (X + W / 2, 2.05), kind="process")
bio.box(ax, (X + W / 2, 1.5), 4.6, 1.0, token="negative", radius=0.15)
bio.label(ax, (X + W / 2, 1.5), "hydrolases, peptides, metal\nstarvation, oxidative burst: killed",
          size="tiny", color=P.on_fill())

# ================================================================ B: a modified vacuole
X = 6.55
frame(X, "B", "Maturation arrested or diverted", "the vacuole is made habitable")
phagosome((X + W / 2, 5.75), 0.95, token="er", bacteria=2)
for k in range(7):
    a = 2 * np.pi * k / 7
    ax.add_patch(Circle((X + W / 2 + 1.25 * np.cos(a), 5.75 + 1.25 * np.sin(a)), 0.13,
                        facecolor=P.fill("er"), edgecolor=P.edge("er"), lw=0.8, zorder=11))
bio.label(ax, (X + W / 2, 4.35), "ER-derived vesicles and ribosomes\nrecruited to the vacuole", size="tiny",
          color=P.muted())
rows = [("Mycobacterium tuberculosis", "keeps coronin 1 on the vacuole,\nexcludes the proton pump,\nsecretes the phosphatase SapM"),
        ("Legionella pneumophila", "≈300 effectors through Dot/Icm\nbuild an ER-like compartment"),
        ("Salmonella enterica", "SPI-2 effectors remodel the\n$\\it{Salmonella}$-containing vacuole")]
for k, (sp, txt) in enumerate(rows):
    y = 3.5 - k * 1.05
    bio.label(ax, (X + 0.3, y + 0.28), sp, size="tiny", bold=True, italic=True, ha="left")
    bio.label(ax, (X + 0.3, y - 0.2), txt, size="tiny", color=P.muted(), ha="left")

# ================================================================ C: escape to the cytosol
X = 12.8
frame(X, "C", "Escape into the cytosol", "and spread into the next cell")
phagosome((X + 1.6, 6.3), 0.8)
bio.label(ax, (X + 1.4, 5.15), "listeriolysin O +\nphospholipases perforate\nthe vacuole", size="tiny", color=P.muted())
bio.arrow(ax, (X + 2.3, 6.0), (X + 3.2, 5.3), kind="process")
M.bacillus(ax, (X + 3.6, 5.0), 0.9, 0.34, angle=-20, gram="+")
bio.label(ax, (X + 4.2, 4.5), "replicates in\nthe cytosol", size="tiny", color=P.muted())

# actin comet tail pushing the bacterium into a protrusion
M.bacillus(ax, (X + 2.0, 2.9), 0.9, 0.34, angle=0, gram="+")
for k in range(16):
    bio.structures.actin(ax, (X + 1.5 - k * 0.07, 2.9 + 0.22 * np.sin(k)), (X + 1.1 - k * 0.07, 2.9 - 0.2 * np.sin(k)),
                         r=0.04)
bio.label(ax, (X + 2.6, 2.35), "actin comet tail", size="tiny", color=P.muted())
bio.arrow(ax, (X + 2.6, 2.9), (X + 3.6, 2.9), kind="process")
ax.add_patch(Rectangle((X + 3.9, 1.7), 1.9, 2.2, facecolor=P.fill("animal"), edgecolor=P.edge("animal"),
                       lw=1.0, zorder=3))
M.bacillus(ax, (X + 4.8, 2.9), 0.9, 0.34, gram="+", zorder=12)
bio.label(ax, (X + W / 2, 1.25), "the next cell is entered\nwithout ever leaving a cytosol", size="tiny", color=P.muted())
