# SIR epidemics at several R0, the final-size relation, and the effect of overdispersed transmission.
import numpy as np
from matplotlib.patches import Rectangle
from scipy import optimize, stats

import wikibio as bio
from wikibio import quant

P = bio.P
rng = np.random.default_rng(0)
fig, ax = bio.canvas(19.0, 6.4)


def sir(R0, gamma=0.2, i0=1e-4, T=240.0, dt=0.05):
    """Classical SIR with beta = R0 * gamma; returns time, infectious fraction and recovered fraction."""
    n = int(T / dt)
    s, i, r = 1 - i0, i0, 0.0
    S, I, R = np.empty(n), np.empty(n), np.empty(n)
    beta = R0 * gamma
    for k in range(n):
        S[k], I[k], R[k] = s, i, r
        ds = -beta * s * i
        di = beta * s * i - gamma * i
        s, i, r = s + dt * ds, i + dt * di, r + dt * gamma * i
    return np.arange(n) * dt, I, R


# ---------------------------------------------------------------- A: epidemic curves
bio.panel(ax, "A", (0.1, 6.1))
pA = quant.Plot(ax, (1.5, 1.0, 4.6, 4.3), xlim=(0, 180), ylim=(0, 0.32),
                xlabel="time / days", ylabel="infectious fraction",
                xticks=[0, 60, 120, 180], yticks=[(0, "0"), (0.1, "10 %"), (0.2, "20 %"), (0.3, "30 %")])
for R0, tok in ((1.5, "dna"), (2.5, "enzyme"), (4.0, "negative")):
    t, I, _ = sir(R0)
    pA.line(t, I, tok, text=f"$R_0 = {R0}$", at=float(np.argmax(I)) / len(t) + 0.02, size="tiny")
bio.label(ax, (3.8, 5.65), "the same infectious period in all three", size="tiny", color=P.muted())

# ---------------------------------------------------------------- B: final size
bio.panel(ax, "B", (6.5, 6.1))
pB = quant.Plot(ax, (8.0, 1.0, 4.2, 4.3), xlim=(1, 7), ylim=(0, 1.0),
                xlabel="$R_0$", ylabel="fraction ever infected $r_\\infty$", ylabel_offset=1.25,
                xticks=[1, 3, 5, 7], yticks=[(0, "0"), (0.5, "50 %"), (1.0, "100 %")])
R0s = np.linspace(1.001, 7, 300)
final = np.array([optimize.brentq(lambda r, R=R: 1 - r - np.exp(-R * r), 1e-9, 1 - 1e-12) for R in R0s])
pB.line(R0s, final, "ink", lw=1.8)
for R0, name in ((1.5, "seasonal influenza"), (2.5, "ancestral SARS-CoV-2"), (6.0, "pertussis")):
    r = optimize.brentq(lambda r: 1 - r - np.exp(-R0 * r), 1e-9, 1 - 1e-12)
    pB.points(R0, r, token="negative", r=0.08)
    pB.text(R0 + 0.12, r - 0.07, name, size="tiny", ha="left", color=P.muted())
bio.label(ax, (10.1, 5.65), "$1 - r_\\infty = \\mathrm{e}^{-R_0 r_\\infty}$", size="tiny", color=P.muted())

# ---------------------------------------------------------------- C: superspreading
bio.panel(ax, "C", (12.6, 6.1))
pC = quant.Plot(ax, (14.2, 1.0, 4.0, 4.3), xlim=(0, 10), ylim=(0, 0.8),
                xlabel="secondary cases from one infection", ylabel="probability",
                xticks=[0, 5, 10], yticks=[(0, "0"), (0.4, "0.4"), (0.8, "0.8")])
R0 = 2.0
xs = np.arange(0, 11)
for k, tok, dx in ((10.0, "dna", -0.12), (0.5, "enzyme", 0.0), (0.1, "negative", 0.12)):
    p = k / (k + R0)
    pmf = stats.nbinom.pmf(xs, k, p)
    for x, y in zip(xs, pmf):
        x0, x1 = pC.X(x - 0.3 + dx * 2), pC.X(x + 0.3 + dx * 2)
        y0, y1 = pC.Y(0), pC.Y(min(y, 0.8))
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, facecolor=P.fill(tok),
                               edgecolor=P.edge(tok), lw=0.6, zorder=7))
    # share of transmission from the most infectious 10 %
    draws = stats.nbinom.rvs(k, p, size=200000, random_state=1)
    top = np.sort(draws)[int(0.9 * draws.size):]
    pC.text(9.8, 0.78 - 0.07 * (0 if k == 10 else 1 if k == 0.5 else 2),
            f"$k = {k:g}$: top 10 % cause {100 * top.sum() / draws.sum():.0f} %", size="tiny", ha="right",
            token=tok)
bio.label(ax, (16.2, 5.65), "mean fixed at $R_0 = 2$, dispersion $k$ varied", size="tiny", color=P.muted())
