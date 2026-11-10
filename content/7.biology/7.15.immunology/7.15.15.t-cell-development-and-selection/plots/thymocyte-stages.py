# Stages of alpha-beta T-cell development in the (mouse) thymus, drawn as a path from the cortico-medullary
# junction (entry), out to the subcapsular zone (DN stages), back through the cortex (DP) to the medulla (SP).
# Below the cells: a marker/event table (filled square = expressed or occurring). DN substages use the mouse
# CD44/CD25 markers; human thymocytes are staged with CD34, CD7 and CD1a instead.
from matplotlib.patches import FancyBboxPatch, Rectangle

import wikibio as bio
from wikibio import immuno

P = bio.P
fig, ax = bio.canvas(24, 12)

# zones
zones = [("Cortico-medullary\njunction (entry)", 0.4, 3.4, "extracellular"), ("Subcapsular zone", 3.4, 10.6, "cytoplasm"),
         ("Cortex", 10.6, 16.6, "nucleus"), ("Medulla", 16.6, 23.6, "vacuole")]
for name, a, b, tok in zones:
    ax.add_patch(Rectangle((a, 7.1), b - a, 4.5, facecolor=P.fill(tok), edgecolor="none", zorder=1))
    bio.label(ax, ((a + b) / 2, 11.25), name, size="small", bold=True)

stages = [("Progenitor", 1.9, "neutral"), ("DN1", 4.4, "neutral"), ("DN2", 6.2, "neutral"), ("DN3", 8.0, "highlight"),
          ("DN4", 9.7, "highlight"), ("DP", 12.6, "protein"), ("DP (selecting)", 15.0, "protein"),
          ("CD4 SP", 18.6, "drug"), ("CD8 SP", 21.6, "positive")]
yc = 9.1
for k, (name, x, tok) in enumerate(stages):
    immuno.immune_cell(ax, (x, yc), r=0.62, kind="lymphocyte", token=tok, seed=k)
    bio.label(ax, (x, yc - 1.05), name, size="tiny", bold=True)
for (n1, x1, _), (n2, x2, _) in zip(stages[:-3], stages[1:-2]):
    bio.arrow(ax, (x1 + 0.72, yc), (x2 - 0.72, yc), kind="process")
bio.arrow(ax, (15.7, yc + 0.3), (17.9, yc + 0.75), kind="process")
bio.arrow(ax, (15.7, yc - 0.3), (20.9, yc - 0.5), kind="process", bend=0.12)
# checkpoints
for x, txt in ((8.9, "β-selection\n(pre-TCR)"), (13.8, "positive\nselection (cTEC)"), (17.6, "negative\nselection")):
    bio.label(ax, (x, 7.55), txt, size="tiny", color=P.edge("negative"))

# marker table
rows = ["CD44", "CD25", "CD4", "CD8", "TCRβ rearranged", "pre-TCR (pTα)", "TCRα rearranged", "surface αβTCR", "RAG"]
on = {
    "CD44": [None, 1, 1, 0, 0, 0, 0, 0, 0], "CD25": [None, 0, 1, 1, 0, 0, 0, 0, 0],
    "CD4": [0, 0, 0, 0, 0, 1, 1, 1, 0], "CD8": [0, 0, 0, 0, 0, 1, 1, 0, 1],
    "TCRβ rearranged": [0, 0, 0.5, 1, 1, 1, 1, 1, 1], "pre-TCR (pTα)": [0, 0, 0, 1, 1, 0, 0, 0, 0],
    "TCRα rearranged": [0, 0, 0, 0, 0, 1, 1, 1, 1], "surface αβTCR": [0, 0, 0, 0, 0, 0.5, 1, 1, 1],
    "RAG": [0, 0, 1, 1, 0, 1, 1, 0, 0],
}
y0, dy = 6.5, 0.68
for i, r in enumerate(rows):
    yy = y0 - i * dy
    bio.label(ax, (0.5, yy), r, size="tiny", ha="left")
    for (name, x, tok), v in list(zip(stages, on[r]))[1:]:
        if v == 0:
            ax.add_patch(Rectangle((x - 0.22, yy - 0.22), 0.44, 0.44, facecolor="none", edgecolor=P.muted(), lw=0.6))
        else:
            ax.add_patch(Rectangle((x - 0.22, yy - 0.22), 0.44 if v == 1 else 0.22, 0.44, facecolor=P.fill("dna"),
                                   edgecolor=P.edge("dna"), lw=0.6))
            if v != 1:
                ax.add_patch(Rectangle((x - 0.22, yy - 0.22), 0.44, 0.44, facecolor="none", edgecolor=P.edge("dna"), lw=0.6))
bio.label(ax, (23.6, 0.25), "filled: present; half: beginning", size="tiny", ha="right", color=P.muted())
