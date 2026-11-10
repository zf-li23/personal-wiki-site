# Clonal selection theory, the four postulates: (4) during development, randomly generated receptors are
# tested against self and self-reactive cells are deleted; (1) each mature naive lymphocyte carries one
# receptor specificity; (2) antigen binds and activates only the matching cell; (3) the selected cell
# proliferates into a clone with the same receptor, which differentiates into effector and memory cells.
import numpy as np

import wikibio as bio
from wikibio import immuno

P = bio.P
fig, ax = bio.canvas(24.0, 9.2)
SPEC = ["protein", "enzyme", "receptor", "antibody", "channel", "carbohydrate"]

# ---- development -------------------------------------------------------------------------------------
bio.label(ax, (3.6, 8.75), "Development", size="title", bold=True)
immuno.immune_cell(ax, (1.2, 5.0), r=0.6, token="neutral", text="progenitor")
for k, tok in enumerate(SPEC[:4]):
    y = 7.2 - k * 1.55
    bio.arrow(ax, (1.9, 5.0), (3.4, y), kind="process", head=0.15)
    immuno.immune_cell(ax, (4.2, y), r=0.5, token="neutral", receptor_token=tok, receptors=6, seed=k)
# a self antigen bound by the cell with the third receptor: deleted
ys = 7.2 - 2 * 1.55
bio.protein(ax, (5.55, ys + 0.05), 0.55, 0.42, "metabolite", text="self", size="tiny")
bio.label(ax, (6.4, ys), "binds self:\ndeleted (4)", size="tiny", ha="left", color=P.edge("negative"))
for s in (-1, 1):
    ax.plot([4.2 - 0.55, 4.2 + 0.55], [ys - 0.55 * s, ys + 0.55 * s], color=P.edge("negative"), lw=2.2, zorder=30)
bio.label(ax, (3.6, 0.65), "random receptors are generated,\nthen tested against self", size="tiny")

# ---- naive repertoire and selection --------------------------------------------------------------------
bio.label(ax, (11.6, 8.75), "Mature naive repertoire", size="title", bold=True)
pos = [(9.4, 6.6), (11.0, 6.6), (12.6, 6.6), (9.4, 4.3), (11.0, 4.3), (12.6, 4.3)]
for k, (xy, tok) in enumerate(zip(pos, SPEC)):
    immuno.immune_cell(ax, xy, r=0.55, token="neutral", receptor_token=tok, receptors=7, seed=10 + k)
sel = 4  # the "channel" receptor
ag = (pos[sel][0], 2.35)
bio.virus(ax, ag, 0.36, kind="enveloped")
bio.label(ax, (ag[0] + 0.55, ag[1]), "antigen", size="small", ha="left")
bio.arrow(ax, (ag[0], ag[1] + 0.45), (pos[sel][0], pos[sel][1] - 0.75), kind="process", head=0.16)
bio.label(ax, (11.0, 8.05), "one receptor specificity per cell (1)", size="tiny")
bio.label(ax, (11.0, 1.2), "antigen selects the cell whose\nreceptor fits (2)", size="tiny")

# ---- clonal expansion and differentiation ---------------------------------------------------------------
bio.label(ax, (19.6, 8.75), "Clonal expansion (3)", size="title", bold=True)
bio.arrow(ax, (13.6, 4.3), (15.4, 4.9), kind="process")
cx, cy = 16.6, 4.9
for k, (dx, dy) in enumerate(((0, 0), (0.95, 0.55), (0.95, -0.55), (-0.1, 1.1), (-0.1, -1.1), (1.9, 0))):
    immuno.immune_cell(ax, (cx + dx, cy + dy), r=0.42, token="neutral", receptor_token=SPEC[sel], receptors=6,
                       seed=20 + k)
bio.arrow(ax, (19.0, 5.6), (20.3, 6.7), kind="process")
bio.arrow(ax, (19.0, 4.2), (20.3, 3.1), kind="process")
immuno.immune_cell(ax, (21.0, 7.0), r=0.62, token="highlight", receptor_token=SPEC[sel], receptors=7, seed=31)
bio.label(ax, (21.0, 8.0), "effector cells", size="small")
bio.label(ax, (21.0, 5.85), "clear the antigen,\nthen mostly die", size="tiny")
immuno.immune_cell(ax, (21.0, 2.9), r=0.5, kind="memory", token="neutral", receptor_token=SPEC[sel], receptors=6,
                   seed=32)
bio.label(ax, (21.0, 1.85), "memory cells", size="small")
bio.label(ax, (21.0, 1.15), "long-lived, more numerous\nthan the naive precursor", size="tiny")
