"""Where the mass and the neurons of the human brain are (isotropic fractionator data).

Adult male brains (n = 4; Azevedo et al. 2009): total mass 1509 g, of which cerebral cortex (grey and
white matter) 1233 g, cerebellum 154 g, rest of brain (brainstem, diencephalon, basal ganglia) 118 g;
neurons 86.1e9 in total: cerebral cortex 16.3e9, cerebellum 69.0e9, rest 0.69e9; non-neuronal cells
84.6e9: 60.8e9, 16.0e9 and 7.7e9.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
parts = ["cerebral cortex", "cerebellum", "rest of brain"]
toks = ["protein", "enzyme", "neutral"]
data = {"mass\n(1509 g)": [1233, 154, 118], "neurons\n(86 x 10$^9$)": [16.3, 69.0, 0.69],
        "other cells\n(85 x 10$^9$)": [60.8, 16.0, 7.7]}

fig, ax = plt.subplots(figsize=(7.2, 4.0))
cols = list(data)
for j, c in enumerate(cols):
    v = np.array(data[c], float)
    f = v / v.sum() * 100
    left = 0.0
    for k, (part, tok) in enumerate(zip(parts, toks)):
        ax.barh(j, f[k], left=left, color=P.fill(tok), edgecolor=P.edge(tok), lw=1,
                label=part if j == 0 else None)
        if f[k] > 6:
            ax.text(left + f[k] / 2, j, f"{f[k]:.0f} %", ha="center", va="center", fontsize=9, color=P.on_fill())
        left += f[k]
ax.set_yticks(range(len(cols)))
ax.set_yticklabels(cols, fontsize=9)
ax.invert_yaxis()
ax.set_xlim(0, 100)
ax.set_xlabel("Share of the whole brain / %")
ax.legend(frameon=False, fontsize=8.5, ncol=3, loc="upper center", bbox_to_anchor=(0.5, 1.13))
fig.tight_layout()
