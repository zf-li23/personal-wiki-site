"""A timeline of the discoveries of cell biology that the course describes, in five lanes.

The axis is compressed tenfold before 1950 so that the dense second half of the twentieth century
can be read. Filled diamonds mark Nobel Prizes for work in the lane; every event is one dated in a
chapter of 7.3 (the chapter number is given in parentheses).
"""

import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
FS = 6.9


def X(year):
    """Piecewise-linear time axis: 0.1 unit per year before 1950, 1 unit per year after."""
    return (year - 1650) * 0.1 if year < 1950 else 30 + (year - 1950)


n = 5
lanes = [  # (name, token, events: (year, label, level, nobel))
    ("seeing and dissecting", "dna", [
        (1665, "Hooke: cells (1)", 0, False), (1838, "Schleiden, Schwann (1)", 1, False),
        (1855, "Virchow (1)", 0, False), (1898, "Golgi apparatus (1)", 1, False),
        (1934, "phase contrast (2)", 0, True), (1951, "HeLa (3)", 1, False),
        (1955, "de Duve: lysosome (11)", 0, False), (1974, "fractionation, EM (1)", 1, True),
        (1975, "hybridomas (3)", 0, True), (2014, "super-resolution (2)", 1, True),
    ]),
    ("membranes and traffic", "golgi", [
        (1925, "Gorter–Grendel bilayer (4)", 0, False), (1959, "unit membrane (4)", 1, False),
        (1970, "Frye–Edidin (4)", 0, False), (1972, "fluid mosaic (4)", 1, False),
        (1975, "signal hypothesis (6)", 0, True), (1980, "sec mutants (9)", 1, True),
        (1985, "LDL receptor (10)", 0, True), (1993, "atg mutants (11)", 1, True),
        (2005, "Rab conversion (8)", 0, False), (2010, "Piezo channels (5)", 1, True),
    ]),
    ("cytoskeleton and motors", "protein", [
        (1971, "sliding microtubules (14)", 0, False), (1984, "dynamic instability (14)", 1, False),
        (1985, "kinesin (14)", 0, False), (1991, "keratin and EBS (15)", 1, False),
    ]),
    ("cell cycle", "chromatin", [
        (1970, "cell fusion, PCC (20)", 0, False), (1971, "cdc mutants (20)", 1, True),
        (1983, "cyclin (20)", 0, True), (1989, "cyclin synthesis drives the clock (20)", 1, False),
        (2003, "Cdk1 hysteresis (20)", 0, False), (2004, "p53 pulses (22)", 1, False),
        (2008, "Rb–E2F bistability (22)", 0, False),
    ]),
    ("cell society", "negative", [
        (1961, "Hayflick limit (25)", 0, False), (1962, "Gurdon: nuclear transfer (24)", 1, True),
        (1963, "differential adhesion (23)", 0, False), (1971, "two hits (26)", 1, False),
        (1976, "v-src from c-src (26)", 0, True), (1996, "Dolly; cytochrome c (24, 25)", 1, False),
        (2000, "hallmarks of cancer (26)", 0, False), (2002, "death genes of C. elegans (25)", 1, True),
        (2006, "iPS cells (24)", 0, True), (2018, "checkpoint blockade (26)", 1, True),
    ]),
]

fig, ax = plt.subplots(figsize=(14.0, 9.0))
LW, GAP = 10.0, 2.0  # lane width (x units) and minimum vertical spacing of labels (y units)
for i, (name, tok, events) in enumerate(lanes):
    x0 = i * LW
    ax.plot([x0, x0], [X(1650), X(2025)], color=P.edge(tok), lw=1.2, alpha=0.6)
    ax.text(x0, X(1650) - 3.5, name, ha="left", va="bottom", fontsize=8.5, color=P.ink(), weight="bold")
    ylab = -1e9
    for year, txt, lev, nobel in sorted(events):
        y = X(year)
        ylab = max(y, ylab + GAP)
        ax.plot([x0, x0 + 0.6, x0 + 1.0], [y, ylab, ylab], color=P.muted(), lw=0.5)
        ax.plot([x0], [y], "D" if nobel else "o", ms=6 if nobel else 5, color=P.fill(tok), mec=P.edge(tok), mew=1.0,
                zorder=5)
        ax.text(x0 + 1.2, ylab, f"{year}  {txt}", ha="left", va="center", fontsize=FS, color=P.ink())
ticks = [1650, 1700, 1800, 1900, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
ax.set_yticks([X(t) for t in ticks])
ax.set_yticklabels([str(t) for t in ticks])
for t in ticks:
    ax.axhline(X(t), color=P.muted(), lw=0.3, alpha=0.35, zorder=0)
ax.axhline(X(1950), color=P.muted(), lw=0.8, ls=":")
ax.text(-2.2, X(1950) - 1.0, "before 1950: ×10 compressed", ha="right", va="bottom", fontsize=FS, color=P.muted())
ax.set_ylim(X(2026), X(1650) - 5)
ax.set_xlim(-1.0, n * LW + 1.0)
ax.set_xticks([])
charts.style_axes(ax, None, "year")
ax.spines["bottom"].set_visible(False)
ax.plot([], [], "D", color=P.fill("neutral"), mec=P.edge("neutral"), label="Nobel Prize for the work")
ax.legend(frameon=False, fontsize=FS + 0.5, loc="lower right", labelcolor=P.ink())
fig.tight_layout()
