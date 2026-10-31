# The thermodynamic uncertainty relation (Theorem 38.4.1). A: the uncertainty product
# Q = Var(J_t) <S_t> / (<J_t>^2 kB) in the long-time limit, for the one-state motor (a biased random walk,
# Q = x coth(x/2) with x the affinity per step) and for 3000 random four-state networks (all six
# edges, rates log-uniform over four decades, the current counting net transitions 0 -> 1), computed
# exactly from the scaled cumulant generating function (largest eigenvalue of the tilted generator).
# Every point lies above 2. B: the minimum dissipation per step that a motor with randomness r must
# pay (TUR, 2 kBT / r) and the dissipation of the one-state motor with the same r; kinesin's randomness
# at saturating ATP (about 0.5) requires at least 4 kBT per 8-nm step, against about 20 kBT available.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
n = 4
edges = [(i, j) for i in range(n) for j in range(i + 1, n)]


def scgf(W, d, s):
    Ls = W * np.exp(s * d)
    Ls = Ls - np.diag(W.sum(0))
    return np.max(np.linalg.eigvals(Ls).real)


Qs, xs = [], []
for _ in range(3000):
    W = np.zeros((n, n))
    for i, j in edges:
        W[j, i] = 10 ** rng.uniform(-2, 2)
        W[i, j] = 10 ** rng.uniform(-2, 2)
    d = np.zeros((n, n))
    d[1, 0], d[0, 1] = 1.0, -1.0  # +1 for a jump 0 -> 1, -1 for 1 -> 0
    h = 1e-3
    l_p, l_m = scgf(W, d, h), scgf(W, d, -h)
    mean = (l_p - l_m) / (2 * h)
    var = (l_p + l_m) / h**2  # lambda(0) = 0
    L = W - np.diag(W.sum(0))
    p = np.linalg.lstsq(np.vstack([L, np.ones(n)]), np.r_[np.zeros(n), 1.0], rcond=None)[0]
    sig = sum((W[j, i] * p[i] - W[i, j] * p[j]) * np.log(W[j, i] * p[i] / (W[i, j] * p[j])) for i, j in edges)
    if abs(mean) < 1e-6 or sig < 1e-8:
        continue
    Qs.append(var * sig / mean**2)
    xs.append(sig / abs(mean))
Qs, xs = np.array(Qs), np.array(xs)

fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.0))
ax = axs[0]
ax.scatter(xs, Qs, s=4, color=charts.line("protein"), alpha=0.35, lw=0, label="random 4-state networks")
x = np.logspace(-2, 3, 300)
ax.plot(x, x / np.tanh(x / 2), color=charts.line("negative"), lw=2.0, label="one-state motor $x\\coth(x/2)$")
ax.axhline(2, color=P.ink(), lw=1.0, ls="--", label="TUR bound $Q = 2$")
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlim(1e-2, 1e3); ax.set_ylim(1, 1e4)
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(ax, "entropy produced per unit current $\\sigma/(k_{\\mathrm{B}}\\langle J\\rangle)$",
                  "uncertainty product $Q$")
charts.title(ax, "A   No current beats the bound")

ax = axs[1]
r = np.linspace(0.12, 3, 300)
ax.plot(r, 2 / r, color=P.ink(), lw=1.4, ls="--", label="TUR: $\\Delta\\mu_{\\min} = 2k_{\\mathrm{B}}T/r$")
rr = r[r > 1.0005]
ax.plot(rr, 2 * np.arctanh(1 / rr), color=charts.line("negative"), lw=2.0, label="one-state motor")
ax.axvline(1, color=P.muted(), lw=0.6)
ax.plot([0.5], [4], "o", color=charts.line("enzyme"), ms=6)
ax.annotate("kinesin, $r\\approx 0.5$:\nat least 4 $k_{\\mathrm{B}}T$ per step\n(about 20 $k_{\\mathrm{B}}T$ available)",
            (0.5, 4), (1.45, 7.5), fontsize=7.5, color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
ax.text(1.05, 15, "$r < 1$ needs\nhidden substeps", fontsize=7.5, color=P.muted())
ax.set_ylim(0, 18)
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
charts.style_axes(ax, "randomness parameter $r$", "dissipation per step / $k_{\\mathrm{B}}T$")
charts.title(ax, "B   Regularity costs free energy")
fig.tight_layout()
