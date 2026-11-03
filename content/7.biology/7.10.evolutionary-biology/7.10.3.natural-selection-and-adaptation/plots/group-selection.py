"""Selection within and between groups (Section 3.3.3), in a trait-group model. Each generation the
population is divided at random into groups of n individuals. An altruist pays a cost c = 0.1 in
fitness and adds b/n = 0.4/n to the fitness of every member of its group, itself included. Within every
group altruists do worse than the selfish members, but groups with more altruists are more productive;
all offspring then mix and form new groups. A: the frequency p of altruists, computed exactly over the
binomial distribution of group compositions. Altruism spreads when b/n > c (n = 2), and declines
otherwise (n = 5, 20). B: one generation with n = 2 and p = 0.5 (Simpson's paradox): in each kind of
mixed group the altruist fraction falls (within-group selection), yet the overall fraction rises, because
the groups with altruists produce more offspring (between-group selection)."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
b_, c = 0.4, 0.1


def step(p, n):
    k = np.arange(n + 1)
    w = binom.pmf(k, n, p)
    alt = k * (1 - c + b_ * k / n)
    tot = n + b_ * k - c * k
    return (w * alt).sum() / (w * tot).sum()


fig, (a, bx) = plt.subplots(1, 2, figsize=(9.6, 3.4), gridspec_kw={"width_ratios": [1.2, 1]})
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.88, wspace=0.3)
T = 300
for n, tok in ((2, "positive"), (5, "atp"), (20, "negative")):
    p = [0.1]
    for _ in range(T):
        p.append(step(p[-1], n))
    a.plot(np.arange(T + 1), p, color=charts.line(tok), lw=1.6, label=f"$n = {n}$: $b/n = {b_ / n:.2f}$")
a.axhline(0.1, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
a.set_ylim(0, 1)
charts.style_axes(a, "generation", "frequency of altruists $p$")
charts.title(a, f"A  Spread or loss ($c = {c}$)")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")

n, p = 2, 0.5
labels, before, after = [], [], []
for k in range(n + 1):
    fa, fs = 1 - c + b_ * k / n, 1 + b_ * k / n
    tot = k * fa + (n - k) * fs
    labels.append(f"{k} of {n}\naltruists")
    before.append(k / n)
    after.append(k * fa / tot)
x = np.arange(n + 1)
bx.bar(x - 0.18, before, 0.34, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.6, label="parents")
bx.bar(x + 0.18, after, 0.34, color=P.fill("positive"), edgecolor=P.edge("positive"), lw=0.6, label="offspring")
p1 = step(p, n)
bx.bar([3.2 - 0.18], [p], 0.34, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.6)
bx.bar([3.2 + 0.18], [p1], 0.34, color=P.fill("positive"), edgecolor=P.edge("positive"), lw=0.6)
bx.text(3.2 + 0.18, p1 + 0.03, f"{p1:.3f}", ha="center", fontsize=FT["tiny"], color=P.ink())
bx.text(1.18, after[1] + 0.03, f"{after[1]:.3f}", ha="center", fontsize=FT["tiny"], color=P.ink())
bx.set_xticks(list(x) + [3.2])
bx.set_xticklabels(labels + ["whole\npopulation"])
bx.set_ylim(0, 1.1)
charts.style_axes(bx, None, "fraction of altruists")
charts.title(bx, "B  One generation, $n = 2$, $p = 0.5$")
bx.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
