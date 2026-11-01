"""Domains and their boundaries in a Hi-C map (the simulated, ICE-balanced chromosome of the previous
figure: 300 bins of 40 kb with domains of 6-21 bins). A: the balanced matrix for bins 100-200 with the
true domain boundaries (ticks at the top edge) and the boundaries called from the insulation score (dashed lines).
B: the insulation score, log2 of the mean contact frequency in a 5 x 5-bin square sliding along the
diagonal (relative to its chromosome-wide mean): boundaries are local minima deeper than 0.4 below the
higher of the two neighboring maxima; the extra minima (all seven) lie at switches between
compartments, which also reduce contacts across them. C: the directionality index of Dixon and colleagues (2012) with a
window of 10 bins: upstream (A) and downstream (B) contact sums give DI = sign(B - A) [(A - E)^2/E +
(B - E)^2/E], E = (A + B)/2; it switches from negative to positive at the start of each domain."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
n = 300
# compartments and domains
comp = np.empty(n, int); i = 0; c = 0
while i < n:
    L = rng.integers(15, 40); comp[i:i + L] = c; c = 1 - c; i += L
tad = np.empty(n, int); i = 0; t = 0
while i < n:
    L = rng.integers(6, 22); tad[i:i + L] = t; t += 1; i += L
I, J = np.indices((n, n))
s = np.abs(I - J) + 1
E = 1.0 / s
cf = np.where(comp[I] == comp[J], np.where(comp[I] == 0, 1.6, 1.3), 0.7)
tf = np.where(tad[I] == tad[J], 2.5, 1.0)
E = E * cf * tf
b = rng.lognormal(0, 0.4, n)
b[rng.choice(n, 9, replace=False)] = 0.0
lam = np.outer(b, b) * E
lam *= 3e6 / np.triu(lam).sum()
Mu = rng.poisson(np.triu(lam))
M = Mu + np.triu(Mu, 1).T

# ICE
good = M.sum(1) > np.quantile(M.sum(1), 0.02)
W = M[np.ix_(good, good)].astype(float)
scale = np.ones(good.sum())
for it in range(200):
    r = W.sum(1)
    r /= r.mean()
    W /= np.outer(r, r)
    scale *= r
    if np.max(np.abs(r - 1)) < 1e-3:
        break
print("ICE iterations", it + 1, "corr(scale, true b)", round(np.corrcoef(scale, b[good])[0, 1], 4),
      "removed bins", (~good).sum())
B = np.full((n, n), np.nan)
B[np.ix_(good, good)] = W


nb = n
Bz = np.where(np.isfinite(B), B, 0.0)
w = 5
ins = np.full(nb, np.nan)
for i in range(w, nb - w):
    sq = B[i - w:i, i + 1:i + 1 + w]
    ins[i] = np.nanmean(sq)
ins = np.log2(ins / np.nanmean(ins))
# boundaries: local minima with depth > 0.1
cand = [i for i in range(w + 1, nb - w - 1) if np.isfinite(ins[i]) and ins[i] <= np.nanmin(ins[i - 2:i + 3])]
called = []
for i in cand:
    lo, hi = max(w, i - 8), min(nb - w, i + 9)
    left = np.nanmax(ins[lo:i + 1]); right = np.nanmax(ins[i:hi])
    if min(left, right) - ins[i] > 0.4:
        called.append(i)
called = np.array(called)
true_b = np.flatnonzero(np.diff(tad)) + 0.5          # boundary between bin k and k+1
tb = true_b[(true_b > w + 1) & (true_b < nb - w - 1)]
hit_c = np.array([np.min(np.abs(tb - c)) <= 1.5 for c in called])
hit_t = np.array([np.min(np.abs(called - t)) <= 1.5 for t in tb])
cb = np.flatnonzero(np.diff(comp)) + 0.5
false = called[~hit_c]
print("false calls at compartment switches", int(sum(np.min(np.abs(cb - f)) <= 2 for f in false)), "of", false.size)
print("boundaries true", tb.size, "called", called.size, "precision", round(hit_c.mean(), 3), "recall", round(hit_t.mean(), 3))
# directionality index
wd = 10
DI = np.full(nb, np.nan)
for i in range(wd, nb - wd):
    A = np.nansum(B[i, i - wd:i]); Bd = np.nansum(B[i, i + 1:i + 1 + wd])
    Ex = (A + Bd) / 2
    if Ex > 0:
        DI[i] = np.sign(Bd - A) * ((A - Ex) ** 2 / Ex + (Bd - Ex) ** 2 / Ex)

lo, hi = 100, 200
fig = plt.figure(figsize=(12.4, 4.0))
gs = fig.add_gridspec(2, 2, width_ratios=[1, 1.5], height_ratios=[1, 1], left=0.05, right=0.99, bottom=0.14,
                      top=0.9, wspace=0.18, hspace=0.45)
ax = fig.add_subplot(gs[:, 0])
sub = B[lo:hi, lo:hi]
ax.imshow(np.log10(sub / np.nanmean(sub) + 0.05), cmap="Reds", interpolation="nearest",
          extent=(lo - 0.5, hi - 0.5, hi - 0.5, lo - 0.5))
for t in true_b[(true_b > lo) & (true_b < hi)]:
    ax.plot([t, t], [lo - 0.5, lo + 2.5], color=P.ink(), lw=1.4)
for c in called[(called > lo) & (called < hi)]:
    ax.axvline(c + 0.5, color=charts.line("dna"), lw=0.7, ls="--")
ax.set_xlim(lo - 0.5, hi - 0.5); ax.set_ylim(hi - 0.5, lo - 0.5)
charts.style_axes(ax, "bin", "bin", box=True)
charts.title(ax, "A  Balanced map, bins 100-200", loc="left")
x = np.arange(nb)
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(x, ins, color=charts.line("dna"), lw=1.2)
for t in tb:
    ax2.axvline(t, color=P.muted(), lw=0.5, ls=":")
ax2.plot(called, ins[called], "v", color=charts.line("negative"), ms=4)
charts.style_axes(ax2, None, "insulation (log2)")
charts.title(ax2, f"B  Insulation score: {hit_t.sum()} of {tb.size} boundaries found, {(~hit_c).sum()} false")
ax3 = fig.add_subplot(gs[1, 1], sharex=ax2)
ax3.bar(x, np.where(DI > 0, DI, 0), width=1, color=P.fill("negative"), lw=0)
ax3.bar(x, np.where(DI < 0, DI, 0), width=1, color=P.fill("dna"), lw=0)
for t in tb:
    ax3.axvline(t, color=P.muted(), lw=0.5, ls=":")
charts.style_axes(ax3, "bin (dotted: true boundaries)", "DI")
charts.title(ax3, "C  Directionality index")
