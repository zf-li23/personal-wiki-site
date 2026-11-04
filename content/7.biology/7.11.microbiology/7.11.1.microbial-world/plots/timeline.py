"""Milestones of microbiology 1660-2020 on a time axis, grouped in four bands."""
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(28, 10.5)
x0, x1, t0, t1 = 1.0, 27.0, 1650, 2025


def X(t):
    # broken axis: 1655-1690 and 1855-2020
    if t < 1800:
        return 1.0 + (t - 1655) / 35 * 3.0
    return 5.2 + (t - 1855) / 165 * 21.8


yaxis = 1.6
ax.plot([X(1655), X(1690)], [yaxis, yaxis], color=P.ink(), lw=1.2)
ax.plot([X(1855), X(2020)], [yaxis, yaxis], color=P.ink(), lw=1.2)
for xb in (X(1690) + 0.35, X(1855) - 0.35):
    ax.plot([xb - 0.12, xb + 0.12], [yaxis - 0.2, yaxis + 0.2], color=P.ink(), lw=1.0)
for t in [1660, 1670, 1680] + list(range(1860, 2021, 20)):
    ax.plot([X(t), X(t)], [yaxis, yaxis - 0.15], color=P.ink(), lw=0.8)
    bio.label(ax, (X(t), yaxis - 0.5), str(t), size="tiny", color=P.muted())
BANDS = [("Microscopy", "neutral"), ("Culture and disease", "bacterium"), ("Chemotherapy", "drug"),
         ("Molecular era", "dna")]
EVENTS = [
    (1665, "Hooke:\nMicrographia", 0, 1), (1676, "Leeuwenhoek:\nanimalcules", 0, 2),
    (1861, "Pasteur: swan-\nnecked flasks", 1, 1), (1867, "Lister: antiseptic\nsurgery", 1, 4),
    (1876, "Cohn: endospores;\nKoch: anthrax", 1, 2), (1882, "agar; tuberculosis\nbacillus", 1, 3),
    (1884, "Gram stain", 1, 5), (1887, "Petri dish;\nchemolithotrophy", 1, 6),
    (1898, "Beijerinck:\nvirus concept", 1, 1),
    (1910, "Ehrlich:\nSalvarsan", 2, 3), (1928, "Fleming:\npenicillin", 2, 1), (1943, "streptomycin", 2, 4),
    (1944, "DNA is the\ntransforming\nprinciple", 3, 1), (1961, "operon", 3, 3), (1973, "recombinant\nDNA", 3, 3),
    (1977, "Woese and Fox:\nArchaea", 3, 4), (1990, "three\ndomains", 3, 5), (1995, "first bacterial\ngenome", 3, 6),
    (2010, "synthetic\ngenome", 3, 7)]
for t, text, band, lev in EVENTS:
    tok = BANDS[band][1]
    x = X(t)
    yt = yaxis + 0.4 + 1.12 * lev
    ax.plot([x, x], [yaxis, yt - 0.2], color=P.muted(), lw=0.6, zorder=2)
    ax.plot([x], [yaxis], "o", ms=5.5, color=P.fill(tok), markeredgecolor=P.edge(tok), zorder=12)
    bio.label(ax, (x, yt), text, size="tiny", va="bottom")
for i, (name, tok) in enumerate(BANDS):
    xx = 1.4 + i * 4.6
    ax.plot([xx], [9.9], "o", ms=7, color=P.fill(tok), markeredgecolor=P.edge(tok))
    bio.label(ax, (xx + 0.3, 9.9), name, size="small", ha="left")
