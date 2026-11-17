# A: production efficiency P/A of animal groups (Humphreys 1979).
# B: trophic transfer efficiency CE x AE x PE (Proposition 43.3.1) for three illustrative chains.
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P
groups = [("Insectivores", 0.86, "negative"), ("Birds", 1.29, "negative"), ("Small mammals", 1.51, "negative"),
          ("Other mammals", 3.14, "negative"), ("Fish and social insects", 9.77, "dna"),
          ("Non-insect invertebrates", 25.0, "dna"), ("Non-social insects", 40.7, "dna")]
fig, (a, b) = plt.subplots(1, 2, figsize=(11.0, 4.4), gridspec_kw=dict(width_ratios=[1.1, 1]))
y = np.arange(len(groups))
for i, (n, v, tok) in enumerate(groups):
    a.barh(i, v, color=P.fill(tok), edgecolor=P.edge(tok))
    a.text(v * 1.08, i, f"{v:g}%", va="center", fontsize=8, color=P.ink())
a.set_yticks(y, [g[0] for g in groups])
a.set_xscale("log")
a.set_xlim(0.5, 100)
a.set_xlabel("Production efficiency P/A / % (log scale)")
a.text(0.6, 6.6, "red: endotherms   blue: ectotherms", fontsize=7.5, color=P.muted())
a.set_title("A  Production efficiency (Humphreys 1979)", loc="left", fontweight="bold")

chains = [("Forest\nmammal herbivore", 0.05, 0.50, 0.02), ("Grassland\ninsect herbivore", 0.25, 0.35, 0.40),
          ("Plankton\nzooplankton", 0.60, 0.60, 0.30)]
x = np.arange(len(chains))
wdt = 0.2
for j, (lab, tok) in enumerate((("CE", "plant"), ("AE", "antibody"), ("PE", "protein"))):
    a_ = [c[1 + j] * 100 for c in chains]
    b.bar(x + (j - 1.5) * wdt, a_, wdt, color=P.fill(tok), edgecolor=P.edge(tok), label=lab)
te = [c[1] * c[2] * c[3] * 100 for c in chains]
b.bar(x + 1.5 * wdt, te, wdt, color=P.fill("negative"), edgecolor=P.edge("negative"), label="CE × AE × PE")
for xi, v in zip(x, te):
    b.text(xi + 1.5 * wdt, v * 1.15, f"{v:.2g}%", ha="center", fontsize=8, color=P.ink())
b.axhline(10, color=P.muted(), lw=0.9, ls="--")
b.text(2.45, 11, "10%", fontsize=7.5, color=P.muted())
b.set_yscale("log")
b.set_ylim(0.03, 150)
b.set_xticks(x, [c[0] for c in chains], fontsize=8)
b.set_ylabel("Efficiency / % (log scale)")
b.legend(frameon=False, fontsize=7.5, loc="upper left", ncol=2)
b.set_title("B  Transfer efficiency", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
