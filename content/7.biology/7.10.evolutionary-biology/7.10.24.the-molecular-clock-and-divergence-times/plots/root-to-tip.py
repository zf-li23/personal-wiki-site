"""Dating with sampling times (simulation). A: a genealogy of 40 virus sequences sampled between 1990
and 2020 under a serially sampled coalescent (constant population size, N_e g = 6 years), drawn on a
time axis. Substitutions accumulate along the branches under a strict clock of 2 x 10^-3 substitutions
per site per year in a genome region of 1500 sites (Poisson numbers of changes). B: root-to-tip
regression: the number of substitutions per site from the root to each tip against its sampling date
(dots), with the least-squares line; its slope estimates the rate and its intercept with the time
axis (zero divergence) estimates the date of the root. Dotted vertical line: true root date. The
estimates are close but not exact, and the points are not independent, because tips share the
branches near the root."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(21)
n, Ng, rate, L = 40, 6.0, 2e-3, 1500
samp = np.sort(rng.uniform(1990, 2020, n))[::-1]
# backward in time from 2020: lineages enter at sampling dates, coalesce at rate k(k-1)/2 / Ng
t = 2020.0
pending = list(range(n))
active = []
date = {i: samp[i] for i in range(n)}
kids = {}
nid = n
while pending or len(active) > 1:
    k = len(active)
    rate_c = k * (k - 1) / 2 / Ng
    w = rng.exponential(1 / rate_c) if rate_c > 0 else np.inf
    nxt = date[pending[0]] if pending else -np.inf
    if pending and t - w < nxt:
        t = nxt
        active.append(pending.pop(0))
        continue
    t -= w
    i, j = rng.choice(len(active), 2, replace=False)
    a, b = active[i], active[j]
    active = [x for q, x in enumerate(active) if q not in (i, j)] + [nid]
    kids[nid] = (a, b)
    date[nid] = t
    nid += 1
root = active[0]
subs = {root: 0.0}


def walk(i):
    for k in kids.get(i, ()):
        subs[k] = subs[i] + rng.poisson(rate * L * (date[k] - date[i])) / L
        walk(k)


walk(root)


def order(i):
    return [i] if i not in kids else order(kids[i][0]) + order(kids[i][1])


tips = order(root)
y = {tp: q for q, tp in enumerate(tips)}


def sety(i):
    if i in kids:
        for k in kids[i]:
            sety(k)
        y[i] = np.mean([y[k] for k in kids[i]])


sety(root)
fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 4.0))
fig.subplots_adjust(left=0.05, right=0.98, bottom=0.14, top=0.9, wspace=0.25)
for pa, (c1, c2) in kids.items():
    for c in (c1, c2):
        a.plot([date[pa], date[c]], [y[c], y[c]], color=charts.line("rna"), lw=1.1)
    a.plot([date[pa], date[pa]], [y[c1], y[c2]], color=charts.line("rna"), lw=1.1)
a.scatter([date[tp] for tp in tips], [y[tp] for tp in tips], s=8, color=P.ink(), zorder=4)
a.set_yticks([])
a.spines["left"].set_visible(False)
charts.style_axes(a, "year")
charts.title(a, "A  A serially sampled genealogy")
x = np.array([date[tp] for tp in tips])
d = np.array([subs[tp] for tp in tips])
slope, icpt = np.polyfit(x, d, 1)
root_hat = -icpt / slope
xx = np.linspace(min(root_hat, date[root]) - 2, 2021, 50)
b.scatter(x, d, s=12, color=charts.line("rna"), zorder=4)
b.plot(xx, slope * xx + icpt, color=P.ink(), lw=1.2)
b.axvline(date[root], color=P.muted(), lw=0.8, ls=":")
b.axhline(0, color=P.muted(), lw=0.6)
b.text(0.03, 0.92, f"estimated rate {slope * 1e3:.2f} x $10^{{-3}}$ per site per year (true 2.00)\n"
       f"estimated root {root_hat:.1f} (true {date[root]:.1f})", transform=b.transAxes,
       fontsize=FT["tiny"], color=P.ink(), va="top")
charts.style_axes(b, "sampling date (year)", "root-to-tip divergence (subst./site)")
charts.title(b, "B  Root-to-tip regression")
