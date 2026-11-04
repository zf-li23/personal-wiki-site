# Probabilistic identification from a panel of biochemical tests.
# A: identification matrix, the percentage of strains of each taxon positive in each test (rounded typical
#    values for five Enterobacterales; illustrative, not a reference table), and the results of an unknown
#    isolate (+/-) in the bottom row.
# B: (log scale) the likelihood of the unknown's result pattern under each taxon, L_j = prod_i p_ij^x_i (1 - p_ij)^(1 - x_i),
#    with p clipped to [0.01, 0.99], normalized over the taxa (equal priors). The pattern of the unknown
#    (indole -, MR +, VP -, citrate +, urease -, H2S +, lactose -, lysine decarboxylase +) gives Salmonella
#    a normalized likelihood above 99.99 %; Proteus mirabilis follows at about 0.007 %.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
tests = ["indole", "methyl red", "Voges-\nProskauer", "citrate", "urease", "H$_2$S", "lactose", "lysine\ndecarb."]
taxa = ["Escherichia coli", "Klebsiella pneumoniae", "Enterobacter cloacae", "Proteus mirabilis", "Salmonella enterica"]
pct = np.array([
    [98, 99, 1, 1, 1, 1, 95, 90],
    [1, 10, 98, 98, 95, 1, 98, 98],
    [1, 5, 99, 99, 65, 1, 93, 1],
    [2, 97, 50, 65, 98, 98, 2, 1],
    [1, 99, 1, 95, 1, 95, 1, 98],
], float)
x = np.array([0, 1, 0, 1, 0, 1, 0, 1])
p = np.clip(pct / 100, 0.01, 0.99)
L = np.prod(np.where(x == 1, p, 1 - p), axis=1)
post = L / L.sum()

fig, axs = plt.subplots(1, 2, figsize=(12.0, 3.9), gridspec_kw=dict(wspace=0.55, width_ratios=[1.7, 1]))
ax = axs[0]
grid = np.vstack([pct, x * 100])
cmap = plt.matplotlib.colors.LinearSegmentedColormap.from_list("pos", [P.surface(), P.fill("dna"), P.edge("dna")])
ax.imshow(grid, cmap=cmap, vmin=0, vmax=100, aspect="auto")
for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        if i < len(taxa):
            txt, col = f"{pct[i, j]:.0f}", (P.on_fill() if pct[i, j] > 45 else P.ink())
        else:
            txt, col = ("+" if x[j] else "–"), (P.on_fill() if x[j] else P.ink())
        ax.text(j, i, txt, ha="center", va="center", fontsize=7.5, color=col, weight="bold" if i == len(taxa) else None)
ax.axhline(len(taxa) - 0.5, color=P.ink(), lw=1.2)
ax.set_xticks(range(len(tests)))
ax.set_xticklabels(tests, fontsize=6.8)
ax.set_yticks(range(len(taxa) + 1))
ax.set_yticklabels(taxa + ["unknown isolate"], fontsize=7)
for k, t in enumerate(ax.get_yticklabels()):
    if k < len(taxa):
        t.set_style("italic")
charts.style_axes(ax)
ax.tick_params(length=0)
for sp in ax.spines.values():
    sp.set_visible(False)
charts.title(ax, "A   Percentage of strains positive")

ax = axs[1]
y = np.arange(len(taxa))
lg = np.log10(post)
ax.barh(y, lg - (-10), left=-10,
        color=[charts.line("positive") if k == post.argmax() else charts.line("neutral") for k in y])
ax.set_yticks(y)
ax.set_yticklabels(taxa, fontsize=7, style="italic")
ax.invert_yaxis()
ax.set_xlim(-10, 1.2)
for k in y:
    txt = f"{post[k] * 100:.2f} %" if post[k] > 1e-4 else f"10$^{{{lg[k]:.0f}}}$"
    ax.text(lg[k] + 0.25, k, txt, va="center", ha="left", fontsize=7, color=P.ink())
charts.style_axes(ax, "log$_{10}$ normalized likelihood")
charts.title(ax, "B   Identification of the unknown")
