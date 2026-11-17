"""Snowshoe hare and Canada lynx pelts, 1900-1920 (thousands), the series reproduced in many
textbooks from the Hudson's Bay Company fur returns compiled by MacLulich (1937) and Elton and
Nicholson (1942). Section 26.5.1.
A: data and the Lotka-Volterra model fitted by least squares on the log scale (initial densities and
the four rates estimated; Nelder-Mead). B: the data in the phase plane, labelled every five years: in this
period both loops run anticlockwise, as the model predicts; dashed: the fitted model orbit.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
years = np.arange(1900, 1921)
hare = np.array([30.0, 47.2, 70.2, 77.4, 36.3, 20.6, 18.1, 21.4, 22.0, 25.4,
                 27.1, 40.3, 57.0, 76.6, 52.3, 19.5, 11.2, 7.6, 14.6, 16.2, 24.7])
lynx = np.array([4.0, 6.1, 9.8, 35.2, 59.4, 41.7, 19.0, 13.0, 8.3, 9.1,
                 7.4, 8.0, 12.3, 19.5, 45.7, 51.1, 29.7, 15.8, 9.7, 10.1, 8.6])
tt = years - 1900.0


def lv(t, z, r, a, ca, m):
    N, Q = z
    return [r * N - a * N * Q, ca * N * Q - m * Q]


def solve(p, teval):
    r, a, ca, m, N0, Q0 = np.exp(p)
    return solve_ivp(lv, [0, teval[-1]], [N0, Q0], t_eval=teval, args=(r, a, ca, m), rtol=1e-8, atol=1e-8)


def loss(p):
    s = solve(p, tt)
    if s.status != 0 or s.y.shape[1] != tt.size or np.any(s.y <= 0):
        return 1e6
    return np.sum((np.log(s.y[0]) - np.log(hare)) ** 2 + (np.log(s.y[1]) - np.log(lynx)) ** 2)


p0 = np.log([0.55, 0.028, 0.024, 0.8, 30.0, 4.0])
best = min((minimize(loss, p0 + dp, method="Nelder-Mead", options=dict(maxiter=6000, xatol=1e-6, fatol=1e-8))
            for dp in [0.0, 0.1, -0.1]), key=lambda res: res.fun)
r, a, ca, m, N0, Q0 = np.exp(best.x)
print(f"r={r:.3f} a={a:.4f} ca={ca:.4f} m={m:.3f} period={2*np.pi/np.sqrt(r*m):.1f} "
      f"N*={m/ca:.1f} P*={r/a:.1f} SS={best.fun:.2f}")
tf = np.linspace(0, 20, 400)
fit = solve(best.x, tf)

fig, axes = plt.subplots(1, 2, figsize=(12.5, 4.4), gridspec_kw=dict(width_ratios=[1.4, 1]))
ax = axes[0]
ax.plot(years, hare, "o", color=C.line("dna"), ms=4, label="hare pelts")
ax.plot(years, lynx, "s", color=C.line("negative"), ms=4, label="lynx pelts")
ax.plot(1900 + tf, fit.y[0], color=C.line("dna"), lw=1.2, label="model hare")
ax.plot(1900 + tf, fit.y[1], color=C.line("negative"), lw=1.2, label="model lynx")
ax.legend(fontsize=FS["tiny"], frameon=False, ncol=2, loc="upper center")
ax.set_ylim(0, 100)
C.style_axes(ax, "Year", "Pelts (thousands)")
C.title(ax, "A  Data and fitted Lotka–Volterra model")

ax = axes[1]
ax.plot(hare, lynx, "-", color=P.muted(), lw=0.8)
for i in range(len(years) - 1):
    ax.annotate("", xy=(hare[i + 1], lynx[i + 1]), xytext=(hare[i], lynx[i]),
                arrowprops=dict(arrowstyle="-|>", color=P.ink(),
                                lw=0.9, shrinkA=2, shrinkB=2))
for yr, h, l in zip(years, hare, lynx):
    if yr % 5 == 0:
        ax.text(h + 1, l + 1.2, str(yr), fontsize=FS["tiny"], color=P.ink())
ax.plot(fit.y[0], fit.y[1], color=C.line("dna"), lw=1.0, ls=(0, (3, 2)), label="model orbit")
ax.legend(fontsize=FS["tiny"], frameon=False, loc="upper right")
C.style_axes(ax, "Hare pelts (thousands)", "Lynx pelts (thousands)")
C.title(ax, "B  Phase plane")
fig.tight_layout()
