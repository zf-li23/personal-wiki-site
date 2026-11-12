# Relatedness in colonies of social Hymenoptera. A: relatedness of a worker to colony members when the queen
# mated once (haplodiploid genetics). B: mean relatedness among workers, r = 1/4 + 1/(2k), for k matings with
# equal paternity, compared with r = 1/2 to own offspring.
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(22, 9.5)
a = charts.axes_at(ax, (2.6, 1.6, 8.6, 6.8))
names = ["full sister", "mother", "own offspring", "full nephew", "brother", "half sister", "half nephew"]
vals = [0.75, 0.5, 0.5, 0.375, 0.25, 0.25, 0.125]
toks = ["positive", "neutral", "enzyme", "neutral", "negative", "neutral", "neutral"]
y = np.arange(len(names))[::-1]
a.barh(y, vals, color=[P.fill(t) for t in toks], edgecolor=[P.edge(t) for t in toks], lw=0.7, height=0.62)
a.set_yticks(y)
a.set_yticklabels(names, fontsize=7)
for yi, v in zip(y, vals):
    a.text(v + 0.015, yi, f"{v:g}", va="center", fontsize=7, color=P.ink())
a.axvline(0.5, color=P.muted(), ls="--", lw=0.8)
a.set_xlim(0, 0.9)
a.set_xlabel("Relatedness of a worker, r")
a.set_title("A  Single mating", fontsize=8, loc="left")
b = charts.axes_at(ax, (13.2, 1.6, 8.2, 6.8))
k = np.arange(1, 21)
r = 0.25 + 1 / (2 * k)
b.plot(k, r, "o-", color=P.edge("positive"), ms=3.5, lw=1.4)
b.axhline(0.5, color=P.muted(), ls="--", lw=0.8)
b.axhline(0.25, color=P.muted(), ls=":", lw=0.8)
b.text(20, 0.51, "own offspring, r = 1/2", ha="right", va="bottom", fontsize=7, color=P.muted())
b.text(20, 0.243, "half sisters, r = 1/4", ha="right", va="top", fontsize=7, color=P.muted())
b.annotate("most ants, primitively\neusocial bees and wasps", xy=(1, 0.75), xytext=(4, 0.7), fontsize=7, color=P.ink(),
           arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
b.annotate("honey bee (about 12)", xy=(12, 0.25 + 1 / 24), xytext=(10, 0.4), fontsize=7, color=P.ink(),
           arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
b.set_xlim(0, 21)
b.set_ylim(0.2, 0.8)
b.set_xlabel("Number of males the queen mated with, k")
b.set_ylabel("Mean relatedness among workers")
b.set_title("B  Multiple mating", fontsize=8, loc="left")
