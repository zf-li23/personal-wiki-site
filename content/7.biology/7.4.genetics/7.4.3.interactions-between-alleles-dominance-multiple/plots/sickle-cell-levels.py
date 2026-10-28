"""Dominance of the sickle-cell allele (HBB Glu6Val) at five levels of observation, for the genotypes
A/A, A/S and S/S. Protein: hemoglobin A (blue) and S (red) molecules. Red cells at normal and at low oxygen:
normal discs versus sickled cells (schematic proportions). Anemia: red-cell count (relative). Malaria:
resistance to Plasmodium falciparum. Relation of S to A at each level is given on the right."""
import numpy as np
from matplotlib.patches import Circle

import wikibio as bio
from wikibio import ecology

P = bio.P
fig, ax = bio.canvas(26.0, 13.0)
cols = {"A/A": 8.0, "A/S": 13.2, "S/S": 18.4}
rows = [("Hemoglobin\npolypeptides", 11.0, "codominant"), ("Red cells,\nnormal O₂", 8.8, "recessive"),
        ("Red cells,\nlow O₂", 6.6, "incompletely dominant"), ("Anemia\n(red-cell count)", 4.4, "recessive"),
        ("Malaria\nresistance", 2.2, "dominant")]
for g, x in cols.items():
    a, b = g.split("/")
    bio.label(ax, (x, 12.5), "$Hb\\beta^{" + a + "}/Hb\\beta^{" + b + "}$", size="normal", bold=True)
for name, y, rel in rows:
    bio.label(ax, (0.4, y), name, size="small", ha="left", bold=True)
    bio.label(ax, (21.3, y), rel, size="small", ha="left", color=P.edge("highlight"))
    ax.plot([0.3, 25.7], [y - 1.1, y - 1.1], color=P.mix(P.muted(), P.surface(), 0.6), lw=0.6)
bio.label(ax, (21.3, 12.5), "S relative to A", size="normal", bold=True, ha="left")

rng = np.random.default_rng(3)
# row 1: protein molecules
for g, x in cols.items():
    nS = {"A/A": 0, "A/S": 4, "S/S": 8}[g]
    toks = ["negative"] * nS + ["dna"] * (8 - nS)
    rng.shuffle(toks)
    for i, t in enumerate(toks):
        cx, cy = x - 1.5 + (i % 4) * 1.0, 11.35 - (i // 4) * 0.7
        ax.add_patch(Circle((cx, cy), 0.25, facecolor=P.fill(t), edgecolor=P.edge(t), lw=0.7, zorder=10))
bio.label(ax, (8.0, 10.1), "A only", size="tiny", color=P.muted())
bio.label(ax, (13.2, 10.1), "A and S", size="tiny", color=P.muted())
bio.label(ax, (18.4, 10.1), "S only", size="tiny", color=P.muted())


def cells(x, y, n_sickle, n=4):
    for i in range(n):
        cx = x - 1.65 + i * 1.1
        if i < n_sickle:
            ecology.fit_icon(ax, "servier/sickle-cell", (cx, y), 0.95, 0.75)
        else:
            ecology.fit_icon(ax, "servier/red-blood-cell", (cx, y), 0.9, 0.65)


for g, x in cols.items():
    cells(x, 8.8, {"A/A": 0, "A/S": 0, "S/S": 3}[g])
    cells(x, 6.6, {"A/A": 0, "A/S": 1, "S/S": 4}[g])
    # anemia: red-cell count as a bar
    val = {"A/A": 1.0, "A/S": 1.0, "S/S": 0.5}[g]
    ax.add_patch(bio.core.FancyBboxPatch((x - 1.8, 4.1), 3.6 * val, 0.55, boxstyle="round,pad=0,rounding_size=0.1",
                                         facecolor=P.fill("blood"), edgecolor=P.edge("blood"), lw=0.8, zorder=10))
    ax.add_patch(bio.core.FancyBboxPatch((x - 1.8, 4.1), 3.6, 0.55, boxstyle="round,pad=0,rounding_size=0.1",
                                         fill=False, edgecolor=P.muted(), lw=0.6, zorder=11))
    bio.label(ax, (x, 3.75), {"A/A": "normal", "A/S": "normal", "S/S": "severe anemia"}[g], size="tiny",
              color=P.muted())
    res = {"A/A": ("susceptible", "negative"), "A/S": ("resistant", "positive"), "S/S": ("resistant (but ill)", "positive")}[g]
    bio.box(ax, (x, 2.2), 3.4, 0.8, token=res[1], text=res[0], size="small")
