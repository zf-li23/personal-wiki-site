# Resistance, tolerance and persistence in time-kill curves (model curves, drug far above the MIC).
# Two-state model (Balaban et al. 2004): normal cells n are killed at rate k_n, persisters p at a much
# lower rate k_p; cells switch n -> p at rate a and p -> n at rate b:
#   dn/dt = -(k_n + a) n + b p,   dp/dt = a n - (b + k_p) p.
# Parameters: k_n = 3 per h, k_p = 0.02 per h, a = 1e-6 per h, b = 0.1 per h; persister fraction at the
# start 1e-4 (formed before the drug was added). Tolerant population: all cells killed slowly,
# k = 0.8 per h. Resistant mutant: grows at 0.5 per h despite the drug. MDK99: minimum duration for
# killing 99 % of the population.
# B: survivors of a first treatment regrow without drug (to the same density) and are treated again;
# the new kill curve is again biphasic because persistence is a phenotypic state, not a mutation.
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import expm

import wikibio as bio
from wikibio import charts

P = bio.P
kn, kp, a, b = 3.0, 0.02, 1e-6, 0.1
A = np.array([[-(kn + a), b], [a, -(b + kp)]])
N0, f = 1e7, 1e-4


def kill(t, n0=N0, frac=f):
    x0 = np.array([n0 * (1 - frac), n0 * frac])
    out = np.array([expm(A * ti) @ x0 for ti in t])
    return out[:, 0], out[:, 1]


fig = plt.figure(figsize=(12.5, 4.3))
gs = fig.add_gridspec(1, 2, width_ratios=[1, 1.3], wspace=0.25)
ax = fig.add_subplot(gs[0, 0])
t = np.linspace(0, 8, 300)
n, p = kill(t)
ax.plot(t, n + p, color=charts.line("bacterium"), lw=2.0, label="susceptible, with persisters")
ax.plot(t, n, color=charts.line("bacterium"), lw=1.0, ls=":", label="normal cells only")
ax.plot(t, p, color=charts.line("highlight"), lw=1.0, ls="--", label="persisters")
ax.plot(t, N0 * np.exp(-0.8 * t), color=charts.line("dna"), lw=2.0, label="tolerant")
ax.plot(t, N0 * np.exp(0.5 * t), color=charts.line("negative"), lw=2.0, label="resistant")
for k, tok in ((kn, "bacterium"), (0.8, "dna")):
    mdk = np.log(100) / k
    ax.plot([mdk, mdk], [5, N0 / 100], color=charts.line(tok), lw=0.8, ls="-.")
ax.axhline(N0 / 100, color=P.muted(), lw=0.6, ls=":")
ax.text(7.9, N0 / 100 * 1.4, "99 % killed", ha="right", fontsize=6.8, color=P.muted())
ax.text(1.5, 30, "MDK$_{99}$", fontsize=6.8, color=P.muted(), ha="left")
ax.set_yscale("log")
ax.set_ylim(10, 1e11)
ax.set_xlim(0, 8)
ax.legend(fontsize=6.8, frameon=False, loc="upper left", ncol=2, labelcolor=P.ink())
charts.style_axes(ax, "time in drug / h", "viable cells / (CFU mL$^{-1}$)")
charts.title(ax, "A   Three responses to a bactericidal drug")

ax = fig.add_subplot(gs[0, 1])
t1 = np.linspace(0, 6, 200)
n1, p1 = kill(t1)
surv = n1[-1] + p1[-1]
ax.plot(t1, n1 + p1, color=charts.line("bacterium"), lw=2.0)
# regrowth without drug for 12 h (logistic-like: exponential, capped at N0)
t2 = np.linspace(0, 12, 200)
g = np.minimum(surv * np.exp(1.4 * t2), N0)
ax.plot(6 + t2, g, color=charts.line("bacterium"), lw=1.4, ls="--")
n3, p3 = kill(t1)
ax.plot(18 + t1, n3 + p3, color=charts.line("bacterium"), lw=2.0)
for x0, txt in ((0, "drug"), (18, "drug")):
    ax.axvspan(x0, x0 + 6, color=P.mix(P.fill("drug"), P.surface(), 0.8), lw=0, zorder=0)
    ax.text(x0 + 3, 4e8, txt, ha="center", fontsize=7.5, color=P.ink())
ax.text(12, 4e8, "regrowth, no drug", ha="center", fontsize=7.5, color=P.ink())
ax.set_yscale("log")
ax.set_ylim(10, 1e9)
ax.set_xlim(0, 24)
charts.style_axes(ax, "time / h")
charts.title(ax, "B   Survivors regrow and are killed again in the same way")
