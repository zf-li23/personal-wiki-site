"""Milestones of genetics on a time axis (1860-2025). Upper side: transmission, mapping, population and
quantitative genetics; lower side: molecular genetics and technology. Stem heights alternate so that labels
do not overlap; the chapter (or course) where each event is treated is given in parentheses."""
from matplotlib.patches import Circle

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30.0, 12.0)
x0, x1, y0 = 1.0, 29.0, 6.0
t0, t1 = 1860, 2025


def X(year):
    return x0 + (year - t0) / (t1 - t0) * (x1 - x0)


ax.plot([x0, x1], [y0, y0], color=P.ink(), lw=1.6, zorder=5)
for yr in range(1860, 2030, 20):
    ax.plot([X(yr), X(yr)], [y0 - 0.12, y0 + 0.12], color=P.ink(), lw=1.0, zorder=5)
    bio.label(ax, (X(yr), y0 - 0.22 if yr % 40 else y0 + 0.25), str(yr), size="tiny", color=P.muted(),
              va="top" if yr % 40 else "bottom")

upper = [  # transmission and mapping: (year, text, stem height, label side)
    (1866, "Mendel's laws (7.4.2)", 1.4, "R"),
    (1900, "Rediscovery (7.4.2)", 2.6, "L"),
    (1903, "Chromosome theory (7.4.5)", 4.2, "L"),
    (1910, "Morgan: X-linked white (7.4.6)", 4.4, "R"),
    (1913, "Sturtevant: first map (7.4.8)", 3.2, "R"),
    (1930, "Population genetics\n1918-1932 (7.4.22)", 1.6, "R"),
    (1950, "McClintock: transposons (7.4.17)", 3.4, "R"),
    (1955, "Benzer: fine structure (7.4.13)", 1.4, "R"),
    (1990, "Human Genome Project\n1990-2003 (7.4.14)", 2.6, "L"),
    (2005, "GWAS (7.4.25)", 4.2, "L"),
]
lower = [  # molecular genetics and technology
    (1927, "Muller: X-ray mutagenesis (7.4.12)", 1.4, "L"),
    (1941, "One gene-one enzyme (7.4.13)", 2.8, "L"),
    (1944, "DNA is the genetic material\n(Avery 1944, Hershey-Chase 1952)", 4.4, "R"),
    (1953, "Double helix (7.2)", 2.4, "R"),
    (1961, "Genetic code (7.2)", 1.2, "R"),
    (1975, "Recombinant DNA and\nsequencing (7.2.5)", 3.4, "R"),
    (1989, "Knockout mice (7.4.19)", 1.6, "R"),
    (2012, "CRISPR-Cas9 (7.4.19)", 3.0, "L"),
    (2022, "T2T human genome\n(7.4.14)", 4.6, "L"),
]
for items, sgn, tok in ((upper, 1, "positive"), (lower, -1, "dna")):
    for yr, text, hgt, side in items:
        x, y = X(yr), y0 + sgn * (0.5 + hgt)
        ax.plot([x, x], [y0, y - sgn * 0.12], color=P.muted(), lw=0.7, zorder=4)
        ax.add_patch(Circle((x, y0), 0.11, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=6))
        right = side == "R"
        bio.label(ax, (x + (0.08 if right else -0.08), y), text, size="small", ha="left" if right else "right",
                  va="bottom" if sgn > 0 else "top")
bio.label(ax, (x0, 11.7), "Transmission, mapping, populations", size="normal", bold=True, ha="left",
          color=P.edge("positive"))
bio.label(ax, (x0, 0.3), "Molecular genetics and technology", size="normal", bold=True, ha="left",
          color=P.edge("dna"))
