"""Forward and inverse problems for the simplest model of gene induction, dx/dt = beta - alpha x with
x(0) = 0, so that x(t) = (beta/alpha)(1 - exp(-alpha t)). A: the forward problem, trajectories for
three parameter sets (lines), and two data sets simulated from beta = 1, alpha = 0.5 with 10%
Gaussian noise: a full time course (circles, t = 0.5 ... 8) and an early-only one (squares,
t = 0.25 ... 1). B, C: the inverse problem, the sum of squared residuals over the (alpha, beta)
plane for the two designs (shading and contours at 2, 4 and 8 times the minimum; cross: true value;
dot: least-squares estimate). The full time course bounds both parameters, which are correlated
because the plateau fixes their ratio beta/alpha; the early points constrain only the initial
slope beta, and any alpha in the plotted range fits them almost equally well."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)


def x(t, a, b):
    return b / a * (1 - np.exp(-a * t))


fig, axs = plt.subplots(1, 3, figsize=(11, 3.5))
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.17, top=0.88, wspace=0.32)
t = np.linspace(0, 8, 200)
ax = axs[0]
for (a, b), tok in [((0.5, 1.0), "dna"), ((0.25, 0.6), "rna"), ((1.0, 1.5), "enzyme")]:
    ax.plot(t, x(t, a, b), color=charts.line(tok), lw=1.6, label=rf"$\alpha$ = {a}, $\beta$ = {b}")
tf = np.arange(0.5, 8.01, 0.5)
te = np.linspace(0.25, 1.0, 16)
yf = x(tf, 0.5, 1.0) * (1 + 0.1 * rng.standard_normal(tf.size))
ye = x(te, 0.5, 1.0) * (1 + 0.1 * rng.standard_normal(te.size))
ax.plot(tf, yf, "o", ms=4, mfc="none", color=P.ink())
ax.plot(te, ye, "s", ms=3.5, color=charts.line("negative"))
ax.legend(frameon=False, fontsize=7, loc="lower right")
charts.style_axes(ax, "time t", "expression x(t)")
charts.title(ax, "A  Forward: parameters to data")

A, B = np.meshgrid(np.linspace(0.05, 1.5, 300), np.linspace(0.3, 2.0, 300))
for ax, tt, yy, ttl in [(axs[1], tf, yf, "B  Inverse: full time course"), (axs[2], te, ye, "C  Inverse: early points only")]:
    sse = sum((x(ti, A, B) - yi) ** 2 for ti, yi in zip(tt, yy))
    m = sse.min()
    ax.contourf(A, B, sse, levels=[0, m, 2 * m, 4 * m, 8 * m],
                colors=[P.fill("dna"), P.fill("dna2"), P.light("dna2"), P.light("neutral")])
    ax.contour(A, B, sse, levels=[2 * m, 4 * m, 8 * m], colors=[P.edge("dna")], linewidths=0.7)
    ax.plot(0.5, 1.0, "x", color=P.ink(), ms=7, mew=1.6)
    i = np.unravel_index(np.argmin(sse), sse.shape)
    ax.plot(A[i], B[i], "o", ms=4, color=charts.line("negative"))
    charts.style_axes(ax, r"degradation rate $\alpha$", r"production rate $\beta$")
    charts.title(ax, ttl)
