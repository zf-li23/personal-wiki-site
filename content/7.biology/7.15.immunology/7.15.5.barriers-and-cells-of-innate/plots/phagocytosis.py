# Phagocytosis and phagosome maturation: (1) recognition by opsonic (Fc, complement) or pattern-recognition
# receptors, (2) engulfment into a phagosome, (3) maturation (Rab5 -> Rab7, V-ATPase acidification, fusion
# with lysosomes), (4) killing and degradation in the phagolysosome, (5) peptide loading on MHC class II.
import numpy as np
from matplotlib.patches import Circle, Ellipse

import wikibio as bio
from wikibio import immuno

P = bio.P
fig, ax = bio.canvas(24.0, 9.0)
c0 = (12.0, 3.6)
bio.cell(ax, c0, 11.2, 3.2, kind="animal", seed=4)
bio.nucleus(ax, (18.6, 3.1), 1.3, pores=8)
bio.label(ax, (12.0, 0.2), "Macrophage", size="small", bold=True)
ytop = c0[1] + 3.2


def bacterium(c, r=0.45, angle=0, coated=True):
    ax.add_patch(Ellipse(c, 2 * r * 1.6, 2 * r, angle=angle, facecolor=P.fill("bacterium"), edgecolor=P.edge("bacterium"),
                         lw=1.0, zorder=14))
    if coated:
        for a in np.linspace(0, 2 * np.pi, 8, endpoint=False):
            ax.add_patch(Circle((c[0] + 1.75 * r * np.cos(a) * 0.95, c[1] + 1.1 * r * np.sin(a)), 0.07,
                                facecolor=P.fill("antibody"), edgecolor=P.edge("antibody"), lw=0.4, zorder=15))


# 1 recognition at the surface
bacterium((2.6, ytop + 0.9))
for dx in (-0.6, 0.0, 0.6):
    ax.plot([2.6 + dx, 2.6 + dx], [ytop - 0.05, ytop + 0.45], color=P.edge("receptor"), lw=2.0, zorder=13)
bio.label(ax, (2.6, ytop + 2.0), "1  recognition\n(Fc / complement receptors, PRRs)", size="tiny")
# 2 engulfment: a cup of membrane
th = np.linspace(np.pi * 0.05, np.pi * 0.95, 60)
ax.plot(6.2 + 1.1 * np.cos(th + np.pi), ytop - 0.1 + 1.0 * np.sin(-th + np.pi) * -1, color=P.edge("membrane"), lw=2.4, zorder=13)
bacterium((6.2, ytop - 0.1))
bio.label(ax, (6.2, ytop + 1.55), "2  engulfment\n(actin-driven)", size="tiny")
# 3 early phagosome (Rab5) -> late (Rab7, acid) with lysosomes fusing
for x, txt, tok in ((7.6, "Rab5", "vesicle"), (11.0, "Rab7, pH 4.5", "lysosome")):
    ax.add_patch(Circle((x, 3.9), 0.95, facecolor=P.light(tok), edgecolor=P.edge(tok), lw=1.4, zorder=12))
    bacterium((x, 3.9), r=0.42, coated=False)
    bio.label(ax, (x, 2.65), txt, size="tiny")
for k in range(4):
    a = 0.6 + k * 1.2
    ax.add_patch(Circle((11.0 + 0.95 * np.cos(a), 3.9 + 0.95 * np.sin(a)), 0.11, facecolor=P.fill("h"),
                        edgecolor=P.edge("h"), lw=0.4, zorder=13))
bio.lysosome(ax, (12.6, 5.2), 0.38)
bio.lysosome(ax, (12.9, 2.6), 0.32)
bio.arrow(ax, (12.3, 4.95), (11.85, 4.5), kind="process", head=0.12)
bio.arrow(ax, (12.6, 2.8), (11.8, 3.3), kind="process", head=0.12)
bio.arrow(ax, (6.4, ytop - 0.9), (7.2, 4.8), kind="process", head=0.14)
bio.arrow(ax, (8.6, 3.9), (10.0, 3.9), kind="process", head=0.14)
bio.label(ax, (9.3, 6.1), "3  maturation", size="tiny")
# 4 phagolysosome with killing
ax.add_patch(Circle((14.6, 3.9), 1.05, facecolor=P.fill("lysosome"), edgecolor=P.edge("lysosome"), lw=1.4, zorder=12))
for a in np.linspace(0, 2 * np.pi, 6, endpoint=False):
    ax.add_patch(Circle((14.6 + 0.5 * np.cos(a), 3.9 + 0.5 * np.sin(a)), 0.13, facecolor=P.fill("bacterium"),
                        edgecolor=P.edge("bacterium"), lw=0.5, zorder=13))
bio.arrow(ax, (12.0, 3.9), (13.45, 3.9), kind="process", head=0.14)
bio.label(ax, (14.6, 2.45), "4  phagolysosome:\nROS, hydrolases, peptides", size="tiny", va="top")
# 5 MHC II at the surface
bio.arrow(ax, (15.3, 4.8), (15.8, ytop - 0.6), kind="process", head=0.14, bend=-0.2)
immuno.mhc_ii(ax, 16.0, ytop - 0.05, up=1, h=0.42, labels=False)
bio.label(ax, (17.4, ytop + 1.3), "5  peptide on MHC II\n→ CD4⁺ T cells", size="tiny")
