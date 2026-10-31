"""A minimal model of heterocyst patterning in a growing filament of Anabaena. Vegetative cells
grow exponentially (doubling time 20 h) and divide; heterocysts neither grow nor divide and secrete
an inhibitor (the PatS/HetN peptide) that spreads along the filament and decays, giving each cell
the inhibitor level I = sum over heterocysts of exp(-d/lambda), d the distance in cell lengths and
lambda = 2.5 cells. A vegetative cell whose inhibitor level is below a threshold theta = 0.15
commits to the heterocyst fate at rate 0.2 per hour. A: positions of heterocysts (dots) along a
filament that starts from 30 vegetative cells after nitrogen step-down, against time; new
heterocysts appear midway between old ones as the intervals grow. B: distribution of the number of
vegetative cells between neighboring heterocysts after 60 h in 200 filaments (bars), compared with
the geometric distribution of the same mean expected if heterocysts were placed at random (line):
lateral inhibition produces a regular spacing of about ten cells."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(2)
lam, theta, kd, dt, gr = 2.5, 0.15, 0.2, 0.1, np.log(2) / 20


def filament(T=60.0, n0=30, record=False):
    size = list(rng.uniform(1, 2, n0))
    het = [False] * n0
    events = []
    for step in range(int(T / dt)):
        size = np.array(size)
        het = np.array(het)
        centers = np.cumsum(size) - size / 2
        hpos = centers[het]
        if hpos.size:
            # distance in cell lengths approximated by distance / mean cell size
            d = np.abs(centers[:, None] - hpos[None, :]) / 1.5
            inh = np.exp(-d / lam).sum(axis=1)
        else:
            inh = np.zeros(size.size)
        commit = (~het) & (inh < theta) & (rng.random(size.size) < kd * dt)
        het = het | commit
        size = np.where(het, size, size * np.exp(gr * dt))
        new_size, new_het = [], []
        for s, h in zip(size, het):
            if not h and s >= 2.0:
                new_size += [s / 2, s / 2]
                new_het += [False, False]
            else:
                new_size.append(s)
                new_het.append(h)
        size, het = new_size, new_het
        if record and step % 10 == 0:
            c = np.cumsum(size) - np.array(size) / 2
            events.append((step * dt, c[np.array(het)], np.sum(size)))
    return np.array(het), events


fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.4), gridspec_kw=dict(width_ratios=(1.3, 1)))
fig.subplots_adjust(wspace=0.3, left=0.07, right=0.98, bottom=0.16, top=0.88)
ax = axs[0]
_, ev = filament(record=True)
for t, hp, total in ev:
    ax.plot(hp, np.full(hp.size, t), "o", color=charts.line("plant"), ms=2.2)
    ax.plot([0, total], [t, t], color=P.muted(), lw=0.25, alpha=0.6)
charts.style_axes(ax, "position along filament (initial cell lengths)", "time after N step-down / h")
charts.title(ax, "A  heterocysts in a growing filament")

gaps = []
for _ in range(200):
    het, _ = filament()
    idx = np.flatnonzero(het)
    gaps += list(np.diff(idx) - 1)
gaps = np.array(gaps)
ax = axs[1]
bins = np.arange(0, 26)
ax.bar(bins, np.bincount(gaps, minlength=26)[:26] / gaps.size, width=0.85, color=P.fill("plant"), lw=0)
m = gaps.mean()
p = 1 / (m + 1)
ax.plot(bins, p * (1 - p) ** bins, "o-", color=P.ink(), ms=2.5, lw=0.9)
ax.text(0.55, 0.9, f"mean {m:.1f} cells", transform=ax.transAxes, fontsize=7, color=P.ink())
charts.style_axes(ax, "vegetative cells between heterocysts", "fraction of intervals")
charts.title(ax, "B  regular spacing")
