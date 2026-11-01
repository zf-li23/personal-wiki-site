"""Estimating the new fraction of each mRNA from metabolic labeling with T>C conversions (simulated
SLAM-seq-like reads). A: numbers of T>C conversions per read for one gene (400 reads, about 28 uridines
each, 30% of molecules made during the labeling): reads from new RNA carry conversions with probability
p_c = 0.04 per uridine, reads from old RNA only sequencing errors (p_e = 0.001). The binomial mixture
(lines) is fitted by the EM algorithm. B: the new fraction of 300 genes estimated by the mixture (dark)
and by the naive share of reads with at least one conversion (light): the naive estimate misses the new
molecules whose reads carry no conversion. C: half-life from the new fraction theta after labeling for
t = 2 h in cells doubling every 24 h, t_1/2 = ln 2 / k_deg with k_deg = -ln(1 - theta)/t - ln 2 / 24 h."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
pc, pe = 0.04, 0.001


def simulate(theta, n_reads):
    nU = rng.binomial(100, 0.28, n_reads)
    new = rng.random(n_reads) < theta
    k = rng.binomial(nU, np.where(new, pc, pe))
    return nU, k


def em(nU, k, iters=200):
    th = 0.5
    l1 = stats.binom.pmf(k, nU, pc)
    l0 = stats.binom.pmf(k, nU, pe)
    for _ in range(iters):
        w = th * l1 / (th * l1 + (1 - th) * l0)
        th = w.mean()
    return th


fig, axs = plt.subplots(1, 3, figsize=(12.4, 3.6))
fig.subplots_adjust(left=0.06, right=0.99, bottom=0.17, top=0.88, wspace=0.3)
ax = axs[0]
nU, k = simulate(0.3, 400)
th = em(nU, k)
kk = np.arange(0, 9)
obs = np.bincount(k, minlength=9)[:9]
ax.bar(kk, obs, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.5, label="reads")
mix_new = np.array([th * stats.binom.pmf(x, nU, pc).sum() for x in kk])
mix_old = np.array([(1 - th) * stats.binom.pmf(x, nU, pe).sum() for x in kk])
ax.plot(kk, mix_old, "o-", color=charts.line("dna"), ms=3.5, lw=1.2, label="old RNA component")
ax.plot(kk, mix_new, "o-", color=charts.line("rna"), ms=3.5, lw=1.2, label="new RNA component")
naive = np.mean(k > 0)
ax.text(0.97, 0.55, f"true new fraction 0.30\nEM estimate {th:.3f}\nreads with >= 1 T>C: {naive:.3f}",
        transform=ax.transAxes, ha="right", fontsize=7.5, color=P.ink())
ax.legend(frameon=False, fontsize=7.5)
charts.style_axes(ax, "T>C conversions per read", "reads")
charts.title(ax, "A  A binomial mixture")
print("A", th, naive)

ax = axs[1]
thetas = rng.uniform(0.02, 0.9, 300)
est, nv = [], []
for t in thetas:
    nU, k = simulate(t, 300)
    est.append(em(nU, k)); nv.append(np.mean(k > 0))
est, nv = np.array(est), np.array(nv)
ax.scatter(thetas, nv, s=6, lw=0, color=P.fill("rna"), label="share of reads with a conversion")
ax.scatter(thetas, est, s=6, lw=0, color=charts.line("dna"), label="mixture model (EM)")
ax.plot([0, 1], [0, 1], color=P.muted(), lw=0.7, ls="--")
ax.legend(frameon=False, fontsize=7.5, loc="upper left")
charts.style_axes(ax, "true new fraction", "estimated new fraction")
charts.title(ax, "B  Estimates for 300 genes")
print("B rmse em", np.sqrt(np.mean((est - thetas) ** 2)), "slope naive", np.polyfit(thetas, nv, 1))

ax = axs[2]
t, mu = 2.0, np.log(2) / 24
g = np.linspace(0.06, 0.95, 300)
kd = -np.log(1 - g) / t - mu
ax.plot(g, np.log(2) / kd, color=charts.line("dna"), lw=1.6)
for th0, tok, dy in [(0.3, "dna", 1.0), (0.2325, "rna", 14.0)]:
    h = np.log(2) / (-np.log(1 - th0) / t - mu)
    ax.plot(th0, h, "o", color=charts.line(tok), ms=5)
    ax.annotate(f"theta = {th0:.2f}: {h:.1f} h", (th0, h), xytext=(th0 + 0.1, h + dy), fontsize=7.5, color=P.ink(),
                arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))
ax.set_yscale("log")
charts.style_axes(ax, "new fraction theta after 2 h", "half-life (h)")
charts.title(ax, "C  From new fraction to half-life")
