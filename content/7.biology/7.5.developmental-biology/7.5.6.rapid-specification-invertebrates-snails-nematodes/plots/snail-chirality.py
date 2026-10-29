"""Shell coiling in the pond snail Lymnaea stagnalis is a maternal effect. The dextral allele D is dominant
over the sinistral allele d, but the coiling of each snail is set by the genotype of its mother, which
determines the chirality of the third cleavage through the maternal formin Lsdia1 (see text). A cross of a dd
female with a DD male gives Dd offspring that are all sinistral, like their mother's genotype requires;
these Dd snails, self-fertilized (Lymnaea is hermaphroditic), produce DD, Dd and dd offspring in the ratio
1:2:1, all dextral because their mother is Dd; only in the next generation do the dd snails reveal their
genotype, producing sinistral offspring. The phenotype lags the genotype by one generation."""
import numpy as np
import wikibio as bio
from matplotlib.patches import Ellipse

P = bio.P
fig, ax = bio.canvas(22, 9.6)


def shell(c, s=0.9, sinistral=False, tok="animal"):
    """A high-spired shell, apex up, aperture facing the viewer: on the right if dextral, on the left if sinistral."""
    m = -1 if sinistral else 1
    t = np.linspace(0, 1, 60)
    left = np.c_[-0.05 - 0.5 * t**0.8, 0.95 - 1.75 * t]
    right = np.c_[0.05 + 0.62 * t**0.8, 0.95 - 1.55 * t]
    bottom = np.c_[np.linspace(0.67, -0.55, 30), -0.6 - 0.25 * np.sin(np.linspace(0, np.pi, 30))]
    out = np.vstack([right, bottom, left[::-1]]) * [m, 1] * s + c
    bio.shape(ax, out, tok, lw=1.1, zorder=4)
    for k, y0 in enumerate((0.55, 0.15, -0.25)):  # sutures between whorls, sloping down towards the aperture
        w = 0.25 + 0.17 * k
        xx = np.linspace(-w, w, 20)
        yy = y0 - 0.18 * (xx + w) / (2 * w) - 0.05 * np.sin(np.pi * (xx + w) / (2 * w))
        ax.plot(c[0] + m * s * xx, c[1] + s * yy, color=P.edge(tok), lw=1.0, zorder=5)
    ap = (c[0] + m * 0.28 * s, c[1] - 0.45 * s)
    ax.add_patch(Ellipse(ap, 0.42 * s, 0.62 * s, angle=-15 * m, facecolor=P.surface(), edgecolor=P.edge(tok), lw=1.0, zorder=6))


def snail(x, y, geno, sinistral, sex=None):
    shell((x, y), 0.75, sinistral, "receptor" if sinistral else "channel")
    bio.label(ax, (x, y - 1.05), geno, size="small", italic=True)
    bio.label(ax, (x, y - 1.45), "sinistral" if sinistral else "dextral", size="tiny", color=P.muted())
    if sex:
        bio.label(ax, (x, y + 1.0), sex, size="tiny", color=P.muted())


rows = [8.0, 5.0, 2.0]
for y, g in zip(rows, ("P", "F1", "F2")):
    bio.label(ax, (0.6, y), g, size="small", bold=True)
snail(3.0, rows[0], "dd", True, "mother")
bio.label(ax, (4.6, rows[0]), "×", size="title")
snail(6.2, rows[0], "DD", False, "father (sperm only)")
ax.plot([4.6, 4.6], [rows[0] - 0.3, rows[1] + 0.9], color=P.ink(), lw=1.0)
snail(4.6, rows[1], "Dd", True)
bio.label(ax, (8.6, rows[1] + 0.3), "genotype Dd (dextral allele dominant),\nbut sinistral: the mother was dd", size="tiny", ha="left")
bio.label(ax, (5.9, rows[1] - 0.2), "selfed", size="tiny", color=P.muted(), ha="left")
ax.plot([4.6, 4.6], [rows[1] - 1.75, rows[2] + 1.45], color=P.ink(), lw=1.0)
ax.plot([2.4, 8.4], [rows[2] + 1.45, rows[2] + 1.45], color=P.ink(), lw=1.0)
for x, g in ((2.4, "DD"), (4.4, "Dd"), (6.4, "Dd"), (8.4, "dd")):
    ax.plot([x, x], [rows[2] + 1.45, rows[2] + 1.0], color=P.ink(), lw=1.0)
    snail(x, rows[2], g, False)
bio.label(ax, (9.6, rows[2] + 1.0), "1 : 2 : 1, all dextral: the mother was Dd", size="tiny", ha="left")
bio.arrow(ax, (9.3, rows[2] - 0.4), (13.9, rows[2] - 0.4), kind="process", head=0.2, dashed=True)
snail(15.0, rows[2], "offspring of dd", True)
bio.label(ax, (11.6, rows[2] - 0.75), "dd snails as mothers", size="tiny", color=P.muted())
bio.label(ax, (12.0, 8.5), "Third cleavage, seen from the animal pole", size="small", bold=True, ha="left")
from wikibio import embryology as E  # noqa: E402
E.cleavage(ax, (13.8, 6.6), 0.9, "spiral")
E.cleavage(ax, (18.6, 6.6), 0.9, "spiral-sinistral")
bio.label(ax, (13.8, 5.0), "dextral: clockwise", size="tiny")
bio.label(ax, (18.6, 5.0), "sinistral: anticlockwise", size="tiny")
