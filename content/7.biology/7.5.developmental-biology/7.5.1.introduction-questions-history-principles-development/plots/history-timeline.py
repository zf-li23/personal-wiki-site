"""Milestones in the history of developmental biology on a broken time axis.

Four segments with different scales (antiquity; 1650-1800; 1800-1900; 1900-2025) so that the dense
twentieth century stays readable. Events are coloured by theme: the debate on preformation and
epigenesis, cells and inheritance, experimental embryology, and genetics and molecular biology.
"""

from matplotlib.patches import Circle

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30, 11.6)

# piecewise-linear axis: (year0, year1, x0, x1)
SEG = [(-400, -300, 1.0, 2.6), (1640, 1800, 3.4, 9.0), (1800, 1900, 9.8, 16.2), (1900, 2025, 17.0, 29.2)]


def X(year):
    for y0, y1, x0, x1 in SEG:
        if y0 <= year <= y1:
            return x0 + (year - y0) / (y1 - y0) * (x1 - x0)
    raise ValueError(year)


ya = 5.6
for y0, y1, x0, x1 in SEG:
    ax.plot([x0, x1], [ya, ya], color=P.ink(), lw=2.0, solid_capstyle="butt", zorder=5)
for (a, b) in zip(SEG[:-1], SEG[1:]):  # break marks
    xm = (a[3] + b[2]) / 2
    for dx in (-0.12, 0.12):
        ax.plot([xm + dx - 0.1, xm + dx + 0.1], [ya - 0.22, ya + 0.22], color=P.ink(), lw=1.2, zorder=5)
ticks = [-350, 1650, 1700, 1750, 1800, 1850, 1900, 1925, 1950, 1975, 2000, 2025]
for t in ticks:
    x = X(t)
    ax.plot([x, x], [ya - 0.12, ya + 0.12], color=P.ink(), lw=1.0, zorder=5)
    bio.label(ax, (x, ya - 0.42), "350 BCE" if t < 0 else str(t), size="tiny", color=P.muted())

THEME = {"debate": "lipid_head", "cells": "enzyme", "exp": "receptor", "gen": "dna"}
events = [
    (-350, "Aristotle: epigenesis;\nholoblastic vs meroblastic", "debate", 1),
    (1651, "Harvey: ex ovo omnia", "debate", -1),
    (1672, "Malpighi: chick embryo\nunder the microscope", "debate", 2),
    (1694, "Hartsoeker: homunculus\nin the sperm (drawn)", "debate", -2),
    (1762, "Bonnet: encapsulation\n(emboîtement)", "debate", 1),
    (1767, "Wolff: the gut forms\nby folding (epigenesis)", "debate", -1),
    (1828, "von Baer: germ layers,\nvon Baer's laws", "cells", 2),
    (1839, "Schleiden, Schwann:\ncell theory", "cells", -2),
    (1876, "Hertwig: two nuclei\nfuse at fertilization", "cells", 1),
    (1888, "Roux: half-embryos", "exp", -1),
    (1892, "Weismann: germ plasm;\nDriesch: whole larvae\nfrom half embryos", "exp", 3),
    (1909, "Johannsen:\ngenotype, phenotype", "gen", -3),
    (1924, "Spemann and Mangold:\nthe organizer", "exp", 1),
    (1957, "Waddington:\nthe landscape", "gen", -1),
    (1962, "Gurdon: frogs from\nintestinal nuclei", "exp", 2),
    (1980, "Nüsslein-Volhard and\nWieschaus: fly screen", "gen", -2),
    (1996, "Dolly", "exp", 3),
    (2006, "Yamanaka:\niPS cells", "gen", -3),
    (2012, "CRISPR-Cas9;\nsingle-cell omics", "gen", 1),
    (2023, "stem-cell\nembryo models", "exp", -1),
]
for year, text, theme, lev in events:
    x = X(year)
    tok = THEME[theme]
    y = ya + (0.9 + 1.25 * (abs(lev) - 1)) * (1 if lev > 0 else -1) + (0.25 if lev < 0 else 0)
    ax.plot([x, x], [ya, y], color=P.edge(tok), lw=0.9, zorder=4)
    ax.add_patch(Circle((x, ya), 0.12, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.9, zorder=6))
    bio.label(ax, (x, y + (0.08 if lev > 0 else -0.08)), text, size="tiny", va="bottom" if lev > 0 else "top")

# legend
items = [("Preformation and epigenesis", "debate"), ("Cells, nuclei, inheritance", "cells"),
         ("Experimental embryology", "exp"), ("Genetics and molecular biology", "gen")]
for k, (t, th) in enumerate(items):
    x = 1.0 + k * 7.2
    bio.box(ax, (x + 0.25, 0.45), 0.45, 0.32, THEME[th])
    bio.label(ax, (x + 0.65, 0.45), t, size="small", ha="left")
