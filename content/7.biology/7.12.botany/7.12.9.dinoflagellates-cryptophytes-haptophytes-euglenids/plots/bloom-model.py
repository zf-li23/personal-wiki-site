"""A simple nutrient-algae-toxin model of a lake bloom (Eq. 9.1, illustrative parameters).
dN/dt = D (N_in - N) - mu A / Y;  dA/dt = mu A - (m + D) A;  dT/dt = q A - (k + D) T;
mu = mu_max f(t) N / (K + N). f(t): seasonal temperature and light factor. Two nutrient loadings are compared:
oligotrophic (N_in = 0.05 mg/L) and eutrophic (N_in = 0.5 mg/L with a runoff pulse at day 180).
mu_max = 0.8 /d, K = 0.02 mg/L, Y = 50 (ug algal carbon per mg nutrient, arbitrary units), m = 0.1 /d,
D = 0.01 /d, q = 0.02 /d, k = 0.03 /d."""
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
mu_max, K, Y, m, D, q, k = 0.8, 0.02, 50.0, 0.1, 0.01, 0.02, 0.03
t = np.linspace(0, 365, 3651)
dt = t[1] - t[0]


def f(tt):
    return np.clip(0.5 * (1 - np.cos(2 * np.pi * (tt - 30) / 365)), 0, 1) ** 2


def nin(tt, base, pulse):
    return base + (pulse * np.exp(-((tt - 180) / 4.0) ** 2) if pulse else 0)


def run(base, pulse):
    N, A, T = base, 0.05, 0.0
    out = np.zeros((len(t), 3))
    for i, tt in enumerate(t):
        out[i] = N, A, T
        mu = mu_max * f(tt) * N / (K + N)
        dN = D * (nin(tt, base, pulse) - N) - mu * A / Y
        dA = mu * A - (m + D) * A
        dT = q * A - (k + D) * T
        N, A, T = max(N + dN * dt, 0), max(A + dA * dt, 1e-4), T + dT * dt
    return out


lo = run(0.05, 0)
hi = run(0.5, 8.0)
fig, ax = bio.canvas(30, 15)
boxes = [(1.6, 8.6, 12.0, 5.2), (16.6, 8.6, 12.0, 5.2), (1.6, 1.4, 12.0, 5.2), (16.6, 1.4, 12.0, 5.2)]
xt = [0, 90, 180, 270, 365]
# A
pa = quant.Plot(ax, boxes[0], xlim=(0, 365), ylim=(0, 1.0), xlabel="day of year", ylabel="f(t)", xticks=xt, yticks=[0, 0.5, 1])
pa.line(t, f(t), token="highlight", lw=1.6, text="f(t)", at=0.45)
bio.panel(ax, "A", (0.2, 14.8))
bio.label(ax, (7.6, 14.4), "Seasonal factor", size="small", bold=True)
pa.text(300, 0.85, "eutrophic lake: runoff pulse at day 180", size="tiny")
# B algae
mx = hi[:, 1].max() * 1.1
pb = quant.Plot(ax, boxes[1], xlim=(0, 365), ylim=(0, mx), xlabel="day of year", ylabel="algae A", xticks=xt,
                yticks=[0, round(mx / 2), round(mx)])
pb.line(t, lo[:, 1], token="dna", lw=1.4, dashed=True, text="oligotrophic", at=0.15)
pb.line(t, hi[:, 1], token="plant", lw=1.8, text="eutrophic", at=0.62)
bio.panel(ax, "B", (15.2, 14.8))
bio.label(ax, (22.6, 14.4), "Algal biomass", size="small", bold=True)
# C nutrient
pc = quant.Plot(ax, boxes[2], xlim=(0, 365), ylim=(0, 0.6), xlabel="day of year", ylabel=r"N / mg L$^{-1}$", xticks=xt, yticks=[0, 0.3, 0.6])
pc.line(t, lo[:, 0], token="dna", lw=1.4, dashed=True)
pc.line(t, np.minimum(hi[:, 0], 0.6), token="plant", lw=1.8)
bio.panel(ax, "C", (0.2, 7.6))
bio.label(ax, (7.6, 7.2), "Nutrient", size="small", bold=True)
# D toxin
mt = hi[:, 2].max() * 1.1
pd = quant.Plot(ax, boxes[3], xlim=(0, 365), ylim=(0, mt), xlabel="day of year", ylabel="toxin T", xticks=xt,
                yticks=[0, round(mt / 2, 1), round(mt, 1)])
pd.line(t, lo[:, 2], token="dna", lw=1.4, dashed=True)
pd.line(t, hi[:, 2], token="negative", lw=1.8)
bio.panel(ax, "D", (15.2, 7.6))
bio.label(ax, (22.6, 7.2), "Dissolved toxin", size="small", bold=True)
