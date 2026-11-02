"""Competing risks (simulation, seed 0). 500 patients with two causes of death acting independently with
constant cause-specific hazards, 0.10 per year (cause 1, e.g. death from the cancer) and 0.15 per year
(cause 2, other causes), and uniform administrative censoring between 5 and 15 years.

A: for cause 1, one minus the Kaplan-Meier estimate that treats deaths from cause 2 as censored, the
Aalen-Johansen estimate of the cumulative incidence function and the true cumulative incidence
0.4 (1 - exp(-0.25 t)). The naive estimate answers a question about a world without cause 2 and
overstates the probability of dying from cause 1. B: the estimated cumulative incidences of the two causes
and the overall survival add up to one at every time.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
n, l1, l2 = 500, 0.10, 0.15
t1, t2 = rng.exponential(1 / l1, n), rng.exponential(1 / l2, n)
c = rng.uniform(5, 15, n)
T = np.minimum.reduce([t1, t2, c])
cause = np.where(T == c, 0, np.where(t1 < t2, 1, 2))
ts = np.unique(T[cause > 0])
S, F1, F2, Snaive = 1.0, 0.0, 0.0, 1.0
grid, s_all, f1, f2, naive = [0.0], [1.0], [0.0], [0.0], [1.0]
for t in ts:
    r = (T >= t).sum()
    d1 = ((T == t) & (cause == 1)).sum()
    d2 = ((T == t) & (cause == 2)).sum()
    F1 += S * d1 / r
    F2 += S * d2 / r
    S *= 1 - (d1 + d2) / r
    Snaive *= 1 - d1 / r
    grid.append(t)
    s_all.append(S)
    f1.append(F1)
    f2.append(F2)
    naive.append(Snaive)
grid, s_all, f1, f2, naive = map(np.array, (grid, s_all, f1, f2, naive))
tt = np.linspace(0, 15, 300)
true1 = l1 / (l1 + l2) * (1 - np.exp(-(l1 + l2) * tt))

fig, axs = plt.subplots(1, 2, figsize=(10, 3.6))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.16, top=0.87, wspace=0.25)
ax = axs[0]
ax.step(grid, 1 - naive, where="post", color=charts.line("neutral"), lw=1.6, label="1 - KM (other deaths censored)")
ax.step(grid, f1, where="post", color=charts.line("rna"), lw=1.8, label="cumulative incidence (Aalen-Johansen)")
ax.plot(tt, true1, color=charts.line("rna"), lw=1, ls="--", label="true cumulative incidence")
ax.plot(tt, 1 - np.exp(-l1 * tt), color=charts.line("neutral"), lw=1, ls="--", label="1 - exp(-0.10 t)")
ax.set_xlim(0, 15)
ax.set_ylim(0, 1)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "years", "probability of death from cause 1")
charts.title(ax, "A  Naive Kaplan-Meier vs cumulative incidence")
ax = axs[1]
ax.fill_between(grid, 0, f1, step="post", color=P.fill("rna"), alpha=0.8, lw=0, label="dead of cause 1")
ax.fill_between(grid, f1, f1 + f2, step="post", color=P.fill("protein"), alpha=0.8, lw=0, label="dead of cause 2")
ax.fill_between(grid, f1 + f2, 1, step="post", color=P.fill("dna"), alpha=0.5, lw=0, label="alive")
ax.set_xlim(0, grid.max())
ax.set_ylim(0, 1)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "years", "probability")
charts.title(ax, "B  The state probabilities add up to one")
