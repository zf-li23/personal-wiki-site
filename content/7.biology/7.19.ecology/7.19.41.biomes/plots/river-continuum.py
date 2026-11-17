# River continuum concept (Vannote et al. 1980), schematic values.
# A: ratio of gross primary production to community respiration (P/R) against stream order.
# B: relative composition of benthic invertebrates by functional feeding group, interpolated
#    between the three reaches of the concept (orders 1-3, 4-6, 7-12).
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P
order = np.linspace(1, 12, 200)
# smooth hump of log(P/R): heterotrophic headwaters, autotrophic middle reaches, heterotrophic large rivers
logpr = -0.42 + 0.8 * np.exp(-((order - 5.0) / 2.0) ** 2) + 0.01 * (order - 1)
pr = 10 ** logpr

fig, (a, b) = plt.subplots(1, 2, figsize=(10.6, 4.4))
a.axhline(1, color=P.muted(), lw=0.9, ls="--")
a.fill_between(order, 1, pr, where=pr >= 1, color=P.fill("plant"), alpha=0.5, lw=0)
a.fill_between(order, pr, 1, where=pr < 1, color=P.fill("animal"), alpha=0.5, lw=0)
a.plot(order, pr, color=P.ink(), lw=2)
a.set_yscale("log")
a.set_ylim(0.2, 5)
a.set_yticks([0.25, 0.5, 1, 2, 4], ["0.25", "0.5", "1", "2", "4"])
a.set_xlim(1, 12)
a.set_xlabel("Stream order")
a.set_ylabel("P/R (gross production / respiration)")
a.text(2.0, 0.3, "heterotrophic\n(P/R < 1)", fontsize=8, ha="center", color=P.ink())
a.text(5.0, 3.0, "autotrophic\n(P/R > 1)", fontsize=8, ha="center", color=P.ink())
a.text(10.0, 0.3, "heterotrophic\n(P/R < 1)", fontsize=8, ha="center", color=P.ink())
for x, t in ((2, "headwaters\n(shaded)"), (5, "middle reaches"), (9.5, "large river")):
    a.text(x, 4.7, t, fontsize=7.5, ha="center", va="top", color=P.muted())
a.set_title("A  Production and respiration", loc="left", fontweight="bold")

# functional feeding groups (% of benthic invertebrates) at reach centres
xs = [2, 5, 9.5]
groups = [("shredders", "carbohydrate", [35, 5, 0]), ("collectors", "dna", [45, 50, 85]),
          ("grazers (scrapers)", "antibody", [5, 30, 0]), ("predators", "negative", [15, 15, 15])]
ys = [np.interp(order, xs, g[2]) for g in groups]
tot = np.sum(ys, axis=0)
ys = [y / tot * 100 for y in ys]
b.stackplot(order, *ys, colors=[P.fill(g[1]) for g in groups], edgecolor=P.surface(), lw=0.5,
            labels=[g[0] for g in groups])
b.set_xlim(1, 12)
b.set_ylim(0, 100)
b.set_xlabel("Stream order")
b.set_ylabel("Share of benthic invertebrates / %")
b.legend(frameon=False, fontsize=7.5, loc="upper left", bbox_to_anchor=(1.0, 1.0))
b.set_title("B  Functional feeding groups", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
