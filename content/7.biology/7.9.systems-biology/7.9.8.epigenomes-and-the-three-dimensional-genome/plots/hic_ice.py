"""From raw Hi-C counts to compartments (simulated chromosome of 300 bins of 40 kb). The expected contact
frequency of bins i and j falls as 1/s with their separation s (in bins), is raised within the same
compartment (A-A by 1.6, B-B by 1.3, A-B lowered to 0.7) and within the same domain (by 2.5); each bin
has a visibility bias b_i (log-normal, s.d. 0.4; 3 % of bins unmappable), and the counts are Poisson with
about 3 million contacts. A: raw counts (log scale): stripes of bins with high or low visibility. B: after
iterative correction (ICE): rows and columns rescaled until every bin has the same total. C: the Pearson
correlation matrix of the observed/expected matrix (each diagonal divided by its mean) shows the plaid
pattern of compartments. D: its first eigenvector E1, oriented so that positive values fall on the
gene-rich (A) compartment, against the true compartments (bars)."""

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

# P(s)
ps = np.array([np.nanmean(np.diagonal(B, k)) for k in range(1, 100)])
kk = np.arange(1, 100)
fitm = (kk >= 3) & (kk <= 60)
slope = np.polyfit(np.log(kk[fitm]), np.log(ps[fitm]), 1)[0]
print("P(s) slope 3-60 bins", round(slope, 3))

# observed / expected and E1
OE = np.full((n, n), np.nan)
for k in range(n):
    d = np.diagonal(B, k)
    m = np.nanmean(d) if np.isfinite(d).any() else np.nan
    idx = np.arange(n - k)
    OE[idx, idx + k] = d / m
    OE[idx + k, idx] = d / m
G = OE[np.ix_(good, good)]
np.fill_diagonal(G, 1.0)
C = np.corrcoef(np.log(G + 1e-3))
w, V = np.linalg.eigh(C)
e1 = V[:, -1]
truth = (comp[good] == 0).astype(float)
if np.corrcoef(e1, truth)[0, 1] < 0:
    e1 = -e1
acc = np.mean((e1 > 0) == (truth == 1))
print("E1 sign agreement", round(acc, 4), "var explained", round(w[-1] / w.sum(), 3))

fig, axs = plt.subplots(1, 4, figsize=(13.4, 3.6), gridspec_kw={"width_ratios": [1, 1, 1, 1.15]})
fig.subplots_adjust(left=0.04, right=0.99, bottom=0.16, top=0.88, wspace=0.3)
ax = axs[0]
ax.imshow(np.log10(M + 1), cmap="Reds", interpolation="nearest")
charts.style_axes(ax, "bin", "bin", box=True)
charts.title(ax, "A  Raw counts (log)")
ax = axs[1]
ax.imshow(np.log10(B * np.nanmean(M[np.ix_(good, good)]) / np.nanmean(B) + 1), cmap="Reds", interpolation="nearest")
charts.style_axes(ax, "bin", None, box=True)
charts.title(ax, "B  After ICE balancing")
ax = axs[2]
Cf = np.full((n, n), np.nan)
Cf[np.ix_(good, good)] = C
ax.imshow(Cf, cmap="RdBu_r", vmin=-0.6, vmax=0.6, interpolation="nearest")
charts.style_axes(ax, "bin", None, box=True)
charts.title(ax, "C  Correlation of O/E")
ax = axs[3]
x = np.arange(n)[good]
ax.fill_between(x, 0, e1, where=e1 > 0, color=P.fill("negative"), lw=0, step="mid")
ax.fill_between(x, 0, e1, where=e1 <= 0, color=P.fill("dna"), lw=0, step="mid")
yb = e1.min() * 1.25
ax.scatter(np.arange(n), np.full(n, yb), c=[charts.line("negative") if v == 0 else charts.line("dna") for v in comp],
           marker="|", s=40, lw=1.2)
ax.text(n * 0.5, yb * 1.12, "true compartments (red A, blue B)", fontsize=7, color=P.ink(), ha="center", va="top")
ax.set_ylim(yb * 1.35, e1.max() * 1.1)
ax.axhline(0, color=P.muted(), lw=0.6)
charts.style_axes(ax, "bin", "E1")
charts.title(ax, f"D  First eigenvector ({100 * acc:.0f}% agree)")
