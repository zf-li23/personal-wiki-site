"""Testing vicariance with a dated phylogeny (schematic, Section 30.4.2). Three land masses A, B, C
separate at two rifts (shaded bands: A from B+C at 80 Myr ago, B from C at 50 Myr ago). Left: a clade
whose divergences coincide with, or predate, the rifts, as vicariance predicts. Right: a clade with the
same branching order whose divergences are much younger than the rifts; the land masses were already
separated when the lineages split, so the lineages must have crossed water by dispersal. The ages and
the two clades are hypothetical."""
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
ink, muted = P.ink(), P.muted()
fig, axes = plt.subplots(1, 2, figsize=(10.0, 3.6), sharey=True)
fig.subplots_adjust(left=0.04, right=0.97, bottom=0.17, top=0.86, wspace=0.12)

AREA_TOK = {"A": "dna", "B": "rna", "C": "plant"}
RIFTS = [(80, "A | B+C rift"), (50, "B | C rift")]


def tree(ax, n1, n2, title):
    # topology (A, (B, C)); tips at y = 2, 1, 0
    ys = {"A": 2.0, "B": 1.0, "C": 0.0}
    ax.plot([n2, n2], [0.0, 1.0], color=ink, lw=1.6)
    ax.plot([n1, n1], [0.5, 2.0], color=ink, lw=1.6)
    ax.plot([n1 + 8, n1], [1.25, 1.25], color=ink, lw=1.6)
    ax.plot([n1, n2], [0.5, 0.5], color=ink, lw=1.6)
    for a, y in ys.items():
        x0 = n1 if a == "A" else n2
        ax.plot([x0, 0], [y, y], color=charts.line(AREA_TOK[a]), lw=2.4)
        ax.text(-2, y, f"area {a}", va="center", ha="left", fontsize=FT["small"], color=ink)
    for x, lab in ((n1, f"{n1} Myr"), (n2, f"{n2} Myr")):
        ax.plot([x], [1.25 if x == n1 else 0.5], "o", ms=5, color=ink)
    ax.text(n1 + 1, 1.36, f"{n1} Myr", fontsize=FT["tiny"], color=ink, ha="right")
    ax.text(n2 + 1, 0.61, f"{n2} Myr", fontsize=FT["tiny"], color=ink, ha="right")
    for x, lab in RIFTS:
        ax.axvspan(x - 2, x + 2, color=P.fill("highlight"), alpha=0.6, lw=0)
        ax.text(x, 2.45, lab, ha="center", fontsize=FT["tiny"], color=muted)
    ax.set_xlim(100, -14)
    ax.set_ylim(-0.5, 2.7)
    ax.set_yticks([])
    charts.style_axes(ax, "time (Myr ago)")
    ax.spines["left"].set_visible(False)
    charts.title(ax, title)


tree(axes[0], 84, 52, "A  Splits match the rifts: vicariance")
tree(axes[1], 30, 12, "B  Splits postdate the rifts: dispersal")
