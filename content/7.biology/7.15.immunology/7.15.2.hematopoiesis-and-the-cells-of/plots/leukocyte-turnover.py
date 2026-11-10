# Steady state of blood cell production: P = N / tau. A: pool sizes and the daily production they imply
# (orders of magnitude from the literature). B: first-order model dN/dt = P - N/tau after a fourfold
# increase in production (emergency granulopoiesis), with and without release of the marrow reserve,
# and the same step for a pool with tau = 1 year.
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(22.0, 8.6)

# ---- A ------------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 8.5))
CELLS = [  # name, pool N, mean lifespan tau in days
    ("erythrocytes", 2.5e13, 120.0),
    ("platelets", 1.5e12, 9.0),
    ("neutrophils", 4.5e10, 10 / 24),
    ("monocytes", 2.0e9, 1.0),
    ("eosinophils", 1.0e9, 0.75),
    ("T cells", 4.0e11, 365.0),
]
pl = quant.Plot(ax, (2.4, 1.6, 8.6, 5.6), xlim=(0, len(CELLS)), ylim=(1e8, 1e14), ylog=True,
                ylabel="cells (log scale)", xticks=[],
                yticks=[(1e8, "10⁸"), (1e10, "10¹⁰"), (1e12, "10¹²"), (1e14, "10¹⁴")], grid=True)
for k, (name, n, tau) in enumerate(CELLS):
    x0 = k + 0.12
    pl.bars([x0, x0 + 0.36], [n], "neutral")
    pl.bars([x0 + 0.38, x0 + 0.74], [n / tau], "dna")
    bio.label(ax, (pl.X(k + 0.5), 1.3), name, size="tiny", rotation=30, ha="right", va="top")
pl.legend([("pool N", "neutral", "-"), ("production per day, N/τ", "dna", "-")], at=(5.6, 7.75))

# ---- B ------------------------------------------------------------------------------------------------
bio.panel(ax, "B", (12.0, 8.5))
t = np.linspace(-0.5, 3.0, 701)  # days
tau = 10 / 24


def step(tau_d, reserve=0.0):
    n = np.ones_like(t)
    m = t >= 0
    n[m] = 4 - 3 * np.exp(-t[m] / tau_d)
    if reserve:
        # marrow reserve released over a few hours, then washed out with the blood half-life
        n[m] += reserve * (np.exp(-t[m] / tau_d) - np.exp(-t[m] / 0.08)) / (1 - 0.08 / tau_d)
    return n


pl2 = quant.Plot(ax, (13.6, 1.6, 7.8, 5.6), xlim=(-0.5, 3.0), ylim=(0, 6), xlabel="time / days",
                 ylabel="blood count (relative)", xticks=[0, 1, 2, 3], yticks=[0, 1, 2, 4, 6])
pl2.vline(0, text="production × 4", top=True)
pl2.line(t, step(tau), "drug", lw=2.0)
pl2.line(t, step(tau, reserve=5.0), "drug", lw=1.4, dashed=True)
pl2.line(t, step(365.0), "dna", lw=1.8, dotted=True)
pl2.legend([("neutrophils, τ = 10 h", "drug", "-"), ("+ marrow reserve", "drug", "--"),
            ("pool with τ = 1 year", "dna", ":")], at=(17.6, 7.3))
