"""Sampling distributions of mark-recapture estimators.

A: closed population of N = 400; M = 50 animals marked; second sample of n = 60, so the number of marked animals
recaptured m is hypergeometric (expected 7.5). 50 000 simulated studies. Lincoln-Petersen N = M n / m (undefined when
m = 0, about 0.03 % of studies, which are dropped) and Chapman N = (M + 1)(n + 1)/(m + 1) - 1.
B: heterogeneity of catchability. Each animal has capture probability p_i drawn from a beta distribution with mean
0.14 and coefficient of variation CV; both samples are binomial draws with these p_i (so the same animals tend to be
caught twice). Mean Chapman estimate (and its 10-90 % range) over 4000 studies against CV.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
N, M, n = 400, 50, 60
m = rng.hypergeometric(M, N - M, n, size=50000)
lp = M * n / m[m > 0]
ch = (M + 1) * (n + 1) / (m + 1) - 1

fig, (ax, bx) = plt.subplots(1, 2, figsize=(12.0, 4.5))
bins = np.arange(0, 1600, 50)
ax.hist(lp, bins=bins, density=True, histtype="step", lw=1.8, color=P.edge("rna"), label="Lincoln–Petersen")
ax.hist(ch, bins=bins, density=True, histtype="step", lw=1.8, color=P.edge("dna"), label="Chapman")
ax.axvline(N, color=P.ink(), lw=1.2, ls="--")
ax.text(N - 15, ax.get_ylim()[1] * 0.95, "true $N$ = 400", ha="right", fontsize=8, color=P.ink())
ax.axvline(lp.mean(), color=P.edge("rna"), lw=1.0, ls=":")
ax.axvline(ch.mean(), color=P.edge("dna"), lw=1.0, ls=":")
ax.text(900, ax.get_ylim()[1] * 0.6,
        f"mean (dotted):\nLincoln–Petersen {lp.mean():.0f}\nChapman {ch.mean():.0f}", fontsize=8, color=P.muted())
ax.set_xlim(0, 1500)
ax.set_xlabel("estimated population size $\\hat N$")
ax.set_ylabel("probability density")
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax.set_title("A  Sampling distributions ($M$ = 50, $n$ = 60)", loc="left", fontsize=10)

cvs = np.linspace(0.01, 1.2, 13)
means, q10, q90 = [], [], []
pbar = 0.14
for cv in cvs:
    var = (cv * pbar) ** 2
    s = pbar * (1 - pbar) / var - 1
    a, b = pbar * s, (1 - pbar) * s
    est = []
    for _ in range(4000):
        p = rng.beta(a, b, N)
        c1 = rng.random(N) < p
        c2 = rng.random(N) < p
        Mi, ni, mi = c1.sum(), c2.sum(), (c1 & c2).sum()
        est.append((Mi + 1) * (ni + 1) / (mi + 1) - 1)
    est = np.array(est)
    means.append(est.mean())
    q10.append(np.quantile(est, 0.1))
    q90.append(np.quantile(est, 0.9))
bx.fill_between(cvs, q10, q90, color=P.fill("dna"), alpha=0.3, lw=0, label="10–90 % of estimates")
bx.plot(cvs, means, color=P.edge("dna"), lw=2.0, marker="o", ms=4, label="mean Chapman estimate")
bx.axhline(N, color=P.ink(), lw=1.2, ls="--")
bx.set_xlim(0, 1.2)
bx.set_ylim(0, 800)
bx.set_xlabel("coefficient of variation of catchability")
bx.set_ylabel("estimated population size $\\hat N$")
bx.legend(frameon=False, fontsize=8, loc="upper right")
bx.set_title("B  Unequal catchability biases $\\hat N$ downward", loc="left", fontsize=10)
for x in (ax, bx):
    for s in ("top", "right"):
        x.spines[s].set_visible(False)
fig.tight_layout()
