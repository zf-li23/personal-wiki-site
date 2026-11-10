# The intestinal mucosa as an immune organ. Left: villus epithelium with goblet cells, intraepithelial
# lymphocytes and the mucus layer; IgA plasma cells in the lamina propria secrete dimeric IgA, which pIgR
# carries across the epithelium (transcytosis) and releases as secretory IgA into the mucus. Right: a
# Peyer's patch: the follicle-associated epithelium with an M cell that transports luminal antigen to
# dendritic cells of the subepithelial dome, above a B-cell follicle with a germinal centre and a T-cell zone.
# Induction happens in the patch; effector cells reach the lamina propria via lymph and blood.
import numpy as np
from matplotlib.patches import Ellipse, Rectangle

import wikibio as bio
from wikibio import immuno

P = bio.P
rng = np.random.default_rng(4)
fig, ax = bio.canvas(28, 13)
ye = 8.0  # top of the epithelium

# lumen, mucus layers
ax.add_patch(Rectangle((0, ye + 0.05), 28, 4.95, facecolor=P.fill("extracellular"), edgecolor="none", zorder=0))
ax.add_patch(Rectangle((0, ye + 0.05), 15.2, 1.1, facecolor=P.fill("carbohydrate"), edgecolor="none", alpha=0.35, zorder=1))
bio.label(ax, (0.3, ye + 0.6), "mucus (with sIgA,\nantimicrobial peptides)", size="tiny", ha="left")
bio.label(ax, (0.3, 12.5), "Lumen: commensal microbes, food antigens", size="small", ha="left")
for k in range(26):
    x, y = rng.uniform(0.5, 27.5), rng.uniform(ye + 1.6, 12.0)
    bio.shape(ax, bio.blob((x, y), 0.28, 0.13, wobble=0.02, seed=k, angle=rng.uniform(0, 3)), "bacterium", zorder=3)

# lamina propria
ax.add_patch(Rectangle((0, 0), 28, ye - 1.3, facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=0))
bio.label(ax, (0.3, 0.4), "Lamina propria", size="small", ha="left")

# epithelium (left part)
w = 0.75
for k in range(20):
    x = 0.4 + k * w
    tok = "golgi" if k in (3, 11, 17) else "lipid_head"
    bio.box(ax, (x + w / 2, ye - 0.65), w - 0.04, 1.3, tok, radius=0.08, lw=0.8)
    ax.add_patch(Ellipse((x + w / 2, ye - 0.95), 0.32, 0.38, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"),
                         lw=0.6, zorder=11))
bio.callout(ax, (0.4 + 3.5 * w, ye - 0.2), (2.0, ye + 2.0), "goblet cell")
# intraepithelial lymphocytes
for x in (0.4 + 6 * w, 0.4 + 14 * w):
    immuno.immune_cell(ax, (x, ye - 0.45), r=0.24, token="cd8", seed=int(x * 10), zorder=13)
bio.callout(ax, (0.4 + 14 * w, ye - 0.45), (11.6, ye + 2.0), "IEL (CD8αα, γδ T)")
# IgA plasma cells and transcytosis
for k, x in enumerate((3.0, 7.5, 12.0)):
    immuno.immune_cell(ax, (x, 4.6), r=0.55, kind="plasma", token="neutral", seed=20 + k)
bio.label(ax, (7.5, 3.6), "IgA plasma cells: dimeric IgA (J chain)", size="tiny")
xs = 0.4 + 9.5 * w
bio.arrow(ax, (7.9, 5.2), (xs - 0.1, ye - 1.35), kind="process", head=0.15)
bio.arrow(ax, (xs, ye - 1.2), (xs, ye + 0.45), kind="process", head=0.15, lw=2.0, color=P.edge("antibody"))
bio.label(ax, (xs + 0.45, ye + 1.45), "pIgR transcytosis →\nsecretory IgA", size="tiny", ha="left")
for k in range(5):
    bio.antibody(ax, (4.5 + 1.8 * k, ye + 0.65), size=0.26, angle=180 if k % 2 else 0)
# lamina propria cells
immuno.immune_cell(ax, (5.2, 2.2), r=0.42, kind="dendritic", token="receptor", seed=31)
bio.label(ax, (5.9, 2.2), "CD103⁺ DC (RA, TGF-β)", size="tiny", ha="left")
immuno.immune_cell(ax, (10.6, 2.0), r=0.3, token="cd4", seed=32)
bio.label(ax, (11.0, 2.0), "Treg, Th17", size="tiny", ha="left")
immuno.immune_cell(ax, (1.8, 2.4), r=0.36, kind="dendritic", token="neutral", seed=33)
bio.label(ax, (1.8, 1.6), "macrophage", size="tiny")
immuno.immune_cell(ax, (13.6, 3.0), r=0.28, token="enzyme", seed=34)
bio.label(ax, (13.6, 2.4), "ILC3", size="tiny")

# Peyer's patch (right)
cx = 21.5
ax.add_patch(Ellipse((cx, ye - 0.3), 11.5, 3.4, facecolor=P.fill("extracellular"), edgecolor="none", zorder=1))
for k in range(13):
    x = 15.6 + k * 0.92
    tok = "positive" if k == 6 else "lipid_head"
    y = ye - 0.55 + 0.9 * np.cos((x - cx) / 6.0 * np.pi / 2) - 0.6
    bio.box(ax, (x + 0.46, y), 0.88, 1.0 if k != 6 else 0.75, tok, radius=0.08, lw=0.8)
bio.label(ax, (cx + 0.5, ye + 1.55), "M cell", size="tiny")
bio.arrow(ax, (cx + 0.46, ye + 1.2), (cx + 0.46, ye - 0.9), kind="process", head=0.15)
bio.label(ax, (cx + 3.4, ye + 1.05), "follicle-associated epithelium", size="tiny")
immuno.immune_cell(ax, (cx + 0.2, ye - 1.7), r=0.4, kind="dendritic", token="receptor", seed=40)
bio.label(ax, (cx + 1.2, ye - 1.7), "subepithelial dome DCs", size="tiny", ha="left")
ax.add_patch(Ellipse((cx, 3.8), 5.6, 3.4, facecolor=P.light("antibody"), edgecolor=P.edge("antibody"), lw=1.0, zorder=2))
ax.add_patch(Ellipse((cx, 3.7), 2.8, 1.7, facecolor=P.fill("antibody"), edgecolor="none", alpha=0.6, zorder=3))
bio.label(ax, (cx, 3.7), "germinal centre\n(IgA switching)", size="tiny", color=P.on_fill())
bio.label(ax, (cx, 1.75), "B-cell follicle", size="tiny")
bio.box(ax, (cx + 4.3, 3.2), 2.2, 1.6, "dna2")
bio.label(ax, (cx + 4.3, 3.2), "T-cell\nzone", size="tiny", color=P.on_fill())
bio.label(ax, (cx, 0.4), "Peyer's patch (inductive site)", size="small")
bio.arrow(ax, (cx - 3.2, 2.6), (14.5, 1.3), kind="process", dashed=True, bend=0.2)
bio.label(ax, (16.2, 0.9), "lymph → blood → lamina propria\n(α4β7, CCR9 homing)", size="tiny")
