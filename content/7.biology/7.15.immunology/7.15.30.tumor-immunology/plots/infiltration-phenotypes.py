# Three spatial patterns of immune infiltration in a tumor (schematic; positions are random with a fixed seed).
# Tumor nests are drawn as one large region of tumor cells (small red discs); CD8 T cells are blue dots.
#   immune desert: almost no T cells; immune excluded: T cells stay in the stroma around the nest;
#   inflamed: T cells infiltrate the tumor nest.
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
fig, axs = plt.subplots(1, 3, figsize=(10, 3.4))
titles = ["Immune desert", "Immune excluded", "Inflamed"]
for k, ax in enumerate(axs):
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.add_patch(Circle((0, 0), 0.9, facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=1.2, alpha=0.35 if False else 1, zorder=1))
    pts = []
    while len(pts) < 160:
        q = rng.uniform(-0.88, 0.88, 2)
        if np.hypot(*q) < 0.88:
            pts.append(q)
    for q in pts:
        ax.add_patch(Circle(q, 0.03, facecolor=P.fill("highlight"), edgecolor="none", zorder=2))
    n_t = (6, 70, 70)[k]
    tc = []
    while len(tc) < n_t:
        q = rng.uniform(-1.45, 1.45, 2)
        r = np.hypot(*q)
        if k == 0 and r > 0.95:
            tc.append(q)
        elif k == 1 and 0.95 < r < 1.4:
            tc.append(q)
        elif k == 2 and r < 1.4 and (r < 0.88 or rng.random() < 0.3):
            tc.append(q)
    for q in tc:
        ax.add_patch(Circle(q, 0.06, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.6, zorder=3))
    ax.set_title(titles[k], fontsize=8, color=P.ink(), weight="bold")
fig.tight_layout()
