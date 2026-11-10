# Schematic marker x cell-type expression matrix (hand-assigned levels 0/1/2, not measured data).
# 2 = expressed on essentially all cells of the type, 1 = low or on a subset, 0 = absent.
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

import wikibio as bio

P = bio.P
cells = ["CD4 T", "Treg", "CD8 T", "NK", "B", "Plasma", "Monocyte", "Macrophage", "cDC", "pDC", "Neutrophil", "Mast"]
levels = {
    "CD45":   [2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2],
    "CD3":    [2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "CD4":    [2, 2, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    "CD8":    [0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    "CD56":   [0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    "CD19":   [0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0],
    "CD20":   [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
    "CD138":  [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
    "CD14":   [0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0],
    "CD68":   [0, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0],
    "CD163":  [0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0],
    "HLA-DR": [0, 0, 0, 0, 2, 1, 2, 2, 2, 2, 0, 0],
    "CD11c":  [0, 0, 0, 1, 0, 0, 2, 1, 2, 0, 1, 0],
    "CD123":  [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
    "CD15":   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
    "CD117":  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    "FOXP3":  [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
}
rows = list(levels)
M = np.array([levels[r] for r in rows])
alphas = {0: 0.0, 1: 0.4, 2: 1.0}
fig, ax = plt.subplots(figsize=(8.2, 5.6))
for i in range(M.shape[0]):
    for j in range(M.shape[1]):
        ax.add_patch(Rectangle((j, i), 0.92, 0.88, facecolor=P.fill("protein"), edgecolor=P.edge("protein") if M[i, j] else P.muted(),
                               lw=0.6 if M[i, j] else 0.3, alpha=alphas[int(M[i, j])] if M[i, j] else 1.0, fill=bool(M[i, j])))
ax.set_xlim(-0.1, M.shape[1])
ax.set_ylim(M.shape[0], -0.1)
ax.set_xticks(np.arange(M.shape[1]) + 0.46)
ax.set_xticklabels(cells, rotation=40, ha="left", fontsize=8, color=P.ink())
ax.xaxis.tick_top()
ax.set_yticks(np.arange(M.shape[0]) + 0.44)
ax.set_yticklabels(rows, fontsize=8, color=P.ink())
for s in ax.spines.values():
    s.set_visible(False)
ax.tick_params(length=0)
ax.set_title("Schematic expression levels (filled: high, light: low or subset, empty: absent)", fontsize=8, color=P.ink(), pad=36)
fig.tight_layout()
