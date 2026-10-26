# The gene regulation function and how it was measured in single cells (after the design of Rosenfeld,
# Young, Alon, Swain and Elowitz, 2005; simulated, illustrative numbers).
# A: repression functions f(X) = beta / (1 + (X/K)^n) for n = 1, 2 and 4 (log concentration axis): the Hill
#    coefficient sets how many-fold X must change to move the output from 90 % to 10 % of maximum,
#    81^(1/n): 81-fold for n = 1, 9-fold for n = 2, 3-fold for n = 4.
# B: the dilution experiment. A fluorescent repressor X (stable, removed only by dilution) is made up to
#    t = 0 and then switched off, so X falls by half every cell cycle; the target promoter produces Y at the
#    rate f(X) with K = 1 (in units of the initial X / 50), n = 2, and Y is diluted at the same rate. Y stays
#    near zero while X >> K and rises once X has been diluted below K (dashed: X). Plotting the production
#    rate of Y, dY/dt + alpha Y, against X at each moment traces f(X).
# C: counting molecules by the binomial partition at division. A mother cell with n molecules gives its
#    daughters n1 ~ Bin(n, 1/2) and n - n1; with a fluorescence nu per molecule, the daughters' intensities
#    y1, y2 satisfy <(y1 - y2)^2> = nu (y1 + y2). Points: 3000 simulated divisions with nu = 50 a.u. per
#    molecule and 0.5 % measurement noise; the fitted slope recovers nu.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
LN2 = np.log(2)
fig, axs = plt.subplots(1, 3, figsize=(13.0, 3.9))

ax = axs[0]
x = np.logspace(-2, 2, 400)
for n, tok in ((1, "neutral"), (2, "dna"), (4, "negative")):
    ax.semilogx(x, 1 / (1 + x ** n), color=charts.line(tok), lw=1.8, label=f"n = {n}")
    lo, hi = (1 / 9) ** (1 / n), 9 ** (1 / n)
    ax.plot([lo, hi], [0.9, 0.1], "o", color=charts.line(tok), ms=3.5)
ax.axhline(0.9, color=P.muted(), lw=0.5, ls=":")
ax.axhline(0.1, color=P.muted(), lw=0.5, ls=":")
ax.axvline(1, color=P.muted(), lw=0.5, ls=":")
ax.text(1.1, 0.53, "X = K", fontsize=7, color=P.muted())
ax.set_ylim(0, 1.05)
ax.legend(fontsize=7, frameon=False, loc="lower left")
charts.style_axes(ax, "repressor X / K", "f(X) / β")
ax.set_title("A   f(X) = β / (1 + (X/K)ⁿ)", loc="left", fontsize=9, color=P.ink())

ax = axs[1]
t = np.linspace(0, 9, 900)
X0, K, n = 50.0, 1.0, 2
X = X0 * np.exp(-LN2 * t)
f = 1 / (1 + (X / K) ** n)
Y = np.zeros_like(t)
for i in range(1, len(t)):
    dt = t[i] - t[i - 1]
    Y[i] = Y[i - 1] + dt * (f[i - 1] - LN2 * Y[i - 1])
ax.plot(t, Y / (1 / LN2), color=charts.line("positive"), lw=1.8, label="target output Y / Y_max")
ax.plot(t, X / X0, color=charts.line("dna"), lw=1.4, ls=(0, (4, 2.4)), label="repressor X / X(0)")
tk = np.log2(X0 / K)
ax.axvline(tk, color=P.muted(), lw=0.6, ls=":")
ax.text(tk + 0.1, 0.92, "X = K", fontsize=7, color=P.muted())
ax.set_xlim(0, 9)
ax.set_ylim(0, 1.05)
ax.legend(fontsize=7, frameon=False, loc="center right")
charts.style_axes(ax, "t / cell cycles after repressor shut-off", "relative level")
ax.set_title("B   Dilution reveals f(X)", loc="left", fontsize=9, color=P.ink())

ax = axs[2]
rng = np.random.default_rng(0)
nu = 50.0
nm = rng.integers(20, 600, 3000)
n1 = rng.binomial(nm, 0.5)
y1 = nu * n1 * (1 + 0.005 * rng.standard_normal(3000))
y2 = nu * (nm - n1) * (1 + 0.005 * rng.standard_normal(3000))
tot = y1 + y2
d2 = (y1 - y2) ** 2
ax.plot(tot / 1e3, d2 / 1e3, ".", color=P.fill("protein"), ms=2.2, alpha=0.6)
edges = np.linspace(tot.min(), tot.max(), 12)
mid = 0.5 * (edges[1:] + edges[:-1])
mean = [d2[(tot >= a) & (tot < b)].mean() for a, b in zip(edges[:-1], edges[1:])]
ax.plot(mid / 1e3, np.array(mean) / 1e3, "o", color=charts.line("negative"), ms=5, label="binned mean")
slope = np.sum(tot * d2) / np.sum(tot * tot)
xx = np.linspace(0, tot.max(), 10)
ax.plot(xx / 1e3, slope * xx / 1e3, color=charts.line("negative"), lw=1.4, label=f"fit: ν = {slope:.0f} a.u.")
ax.set_xlim(0, tot.max() / 1e3)
ax.set_ylim(0, np.percentile(d2, 99) / 1e3)
ax.legend(fontsize=7, frameon=False, loc="upper left")
charts.style_axes(ax, "y₁ + y₂ / 10³ a.u.", "(y₁ − y₂)² / 10³ a.u.²")
ax.set_title("C   Binomial partition calibrates ν", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
