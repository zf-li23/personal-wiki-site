"""Evolutionary rescue in a quantitative-genetic model. Individual fitness is Gaussian around an optimum
theta, so that a population with mean z and phenotypic variance V_P has mean fitness
W = W0 exp(-(z - theta)^2 / (2 V_s)) with V_s = omega^2 + V_P, and the mean evolves by
dz = V_A (theta - z) / V_s per generation. Numbers follow Beverton-Holt growth with ceiling K and
Poisson sampling. Parameters: W0 = 1.3, V_s = 10, phenotype in units of its SD.
A: the optimum jumps by 3.5 at generation 0. With V_A = 0.1 and K = 1000 the population almost always
dies out (median of 200 runs and four individual runs); a larger additive variance (V_A = 0.4) or a larger
carrying capacity (K = 20000) lets adaptation catch up before numbers fall to zero. The fraction of the 200 runs
that survive is given in the legend. B: deterministic dynamics when the optimum moves steadily at rate b;
the lag of the mean behind the optimum settles at b V_s / V_A and the population persists only below the
critical rate b_c = V_A sqrt(2 ln W0 / V_s) (here V_A = 0.3, b_c = 0.069)."""
import numpy as np
import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
W0, Vs, delta = 1.3, 10.0, 3.5
T = 150


def run(VA, K, rng, reps=200):
    N = np.full(reps, float(K))
    zbar = 0.0
    out = np.empty((T + 1, reps))
    out[0] = N
    for t in range(1, T + 1):
        W = W0 * np.exp(-((zbar - delta) ** 2) / (2 * Vs))
        exp_n = W * N / (1 + (W0 - 1) * N / K)
        N = rng.poisson(exp_n).astype(float)
        zbar += VA * (delta - zbar) / Vs
        out[t] = N
    return out


rng = np.random.default_rng(0)
cases = [(0.1, 1000, "small $V_A$, small $K$", "negative"), (0.4, 1000, "large $V_A$", "plant"),
         (0.1, 20000, "large $K$", "dna")]
fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.0))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.14, top=0.9, wspace=0.28)
a = axs[0]
tt = np.arange(T + 1)
for VA, K, lab, tok in cases:
    out = run(VA, K, rng)
    surv = (out[-1] > 0).mean()
    for j in range(4):
        a.plot(tt, np.maximum(out[:, j], 0.8), color=charts.line(tok), lw=0.5, alpha=0.5)
    a.plot(tt, np.maximum(np.median(out, axis=1), 0.8), color=charts.line(tok), lw=2,
           label=f"{lab}: {surv:.0%} survive")
a.set_yscale("log")
a.set_ylim(0.8, 4e4)
a.axvline(0, color=P.muted(), lw=0.8, ls=":")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(a, "generation after the change", "population size $N$")
charts.title(a, "A  Sudden change of the optimum")

b = axs[1]
VA = 0.3
bc = VA * np.sqrt(2 * np.log(W0) / Vs)
for rate, tok in ((0.5 * bc, "plant"), (0.9 * bc, "dna"), (1.2 * bc, "negative")):
    N, zbar, Ns = 1000.0, 0.0, []
    for t in range(400):
        theta = rate * t
        W = W0 * np.exp(-((zbar - theta) ** 2) / (2 * Vs))
        N = W * N / (1 + (W0 - 1) * N / 1000)
        zbar += VA * (theta - zbar) / Vs
        Ns.append(max(N, 1e-3))
    b.plot(np.arange(400), Ns, color=charts.line(tok), lw=2, label=f"$b = {rate / bc:.1f}\\,b_c$")
b.set_yscale("log")
b.set_ylim(1, 3000)
b.axhline(1, color=P.muted(), lw=0.8)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(b, "generation", "population size $N$")
charts.title(b, "B  Steadily moving optimum")
