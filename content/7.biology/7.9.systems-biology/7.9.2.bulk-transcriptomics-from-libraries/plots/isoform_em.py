"""Estimating isoform abundances by the EM algorithm. A: a gene with two isoforms, T1 (exons 1, 2, 3;
1200 nt) and T2 (exons 1 and 3; 1000 nt), and the three compatibility classes of 100-nt reads: reads
inside exon 1 or exon 3 fit both isoforms, reads touching exon 2 fit only T1, reads across the
exon 1-exon 3 junction fit only T2. 2000 reads were simulated from transcript fractions
rho = (0.3, 0.7). B: EM iterations for the read fractions alpha_T1 from five starting values; all
converge to the maximum-likelihood estimate (dashed). C: the log-likelihood increases at every
iteration, as it must for EM."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
ex = [400, 200, 600]
read = 100
L = np.array([sum(ex), ex[0] + ex[2]])
eff = L - read + 1
rho = np.array([0.3, 0.7])
w = rho * eff / np.sum(rho * eff)
N = 2000
src = rng.choice(2, N, p=w)
start = np.array([rng.integers(0, eff[t]) for t in src])
cls = np.empty(N, int)  # 0: both, 1: T1 only, 2: T2 only
for i, (t, s) in enumerate(zip(src, start)):
    e = s + read
    if t == 0:
        cls[i] = 0 if (e <= ex[0] or s >= ex[0] + ex[1]) else 1
    else:
        cls[i] = 0 if (e <= ex[0] or s >= ex[0]) else 2
n = np.bincount(cls, minlength=3)
compat = np.array([[1, 1], [1, 0], [0, 1]], float)


def loglik(a):
    return np.sum(n * np.log(compat @ (a / eff)))


def em(a, it=40):
    path = [a.copy()]
    for _ in range(it):
        q = compat * (a / eff)
        q /= q.sum(1, keepdims=True)
        a = (n[:, None] * q).sum(0) / N
        path.append(a.copy())
    return np.array(path)


fig = plt.figure(figsize=(12, 3.6))
ax = fig.add_axes([0.02, 0.08, 0.36, 0.82])
ax.set_xlim(0, 13)
ax.set_ylim(0, 6)
ax.axis("off")
x0, sc = 0.6, 0.006
for row, (name, keep) in enumerate([("T1", [0, 1, 2]), ("T2", [0, 2])]):
    y = 5 - row * 1.4
    bio.label(ax, (0.3, y), name, size="small", ha="right")
    x = x0
    prev = None
    for k in keep:
        wdt = ex[k] * 0.0085
        bio.box(ax, (x + wdt / 2, y), wdt, 0.55, ["dna", "rna", "enzyme"][k], text=f"exon {k + 1}", size="tiny", radius=0.08)
        if prev is not None:
            ax.plot([prev, x], [y, y], color=P.muted(), lw=1)
        prev = x + wdt
        x = prev + 0.35
counts = ["both isoforms", "T1 only", "T2 only"]
for k in range(3):
    bio.label(ax, (0.6, 2.2 - 0.6 * k), f"{counts[k]}: {n[k]} reads", size="small", ha="left")
bio.label(ax, (0.6, 0.35), f"effective lengths {eff[0]} and {eff[1]} nt", size="tiny", ha="left", color=P.muted())
charts.title(fig.add_axes([0.02, 0.9, 0.3, 0.05], frame_on=False), "A  Two isoforms, three read classes")
fig.axes[-1].axis("off")

b = fig.add_axes([0.45, 0.17, 0.24, 0.7])
c = fig.add_axes([0.76, 0.17, 0.23, 0.7])
paths = [em(np.array([a0, 1 - a0])) for a0 in [0.02, 0.2, 0.5, 0.8, 0.98]]
mle = paths[2][-1]
for p, tok in zip(paths, ["dna", "rna", "enzyme", "protein", "receptor"]):
    b.plot(p[:, 0], color=charts.line(tok), lw=1.4, marker="o", ms=2)
    c.plot([loglik(a) for a in p], color=charts.line(tok), lw=1.4)
b.axhline(mle[0], color=P.muted(), ls="--", lw=0.8)
b.set_xlim(0, 25)
c.set_xlim(0, 25)
c.set_ylim(loglik(mle) - 60, loglik(mle) + 5)
charts.style_axes(b, "EM iteration", "read fraction alpha(T1)")
charts.title(b, "B  Convergence of the estimate")
charts.style_axes(c, "EM iteration", "log-likelihood")
charts.title(c, "C  Monotone ascent")
rho_hat = (mle / eff) / np.sum(mle / eff)
b.text(0.35, 0.08, f"MLE: alpha = ({mle[0]:.3f}, {mle[1]:.3f})\nrho = ({rho_hat[0]:.3f}, {rho_hat[1]:.3f})",
       transform=b.transAxes, fontsize=7.5, color=P.ink())
