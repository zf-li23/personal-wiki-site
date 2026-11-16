"""Dynamics of the Hassell model N_{t+1} = lambda N_t (1 + a N_t)^(-b) in the (lambda, b) plane
(Section 12.1.3). a only scales N, so a = 1.

For each of 260 x 260 parameter pairs the map is iterated 1500 times from N0 = 0.5 N*; the attractor is
classified from the last 64 values: monotonic approach (multiplier F'(N*) in (0, 1)), damped oscillation
(F'(N*) in (-1, 0)), 2-cycle, cycles of period 4-32, and chaos (positive Lyapunov exponent estimated over
the last 600 iterations). Curves: the analytical boundaries b (1 - lambda^(-1/b)) = 1 (F'(N*) = 0) and
= 2 (F'(N*) = -1).
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
lam = np.geomspace(1.05, 1e4, 260)
bb = np.linspace(0.05, 6.0, 260)
L, B = np.meshgrid(lam, bb)
Ns = L ** (1 / B) - 1
mult = 1 - B * (1 - L ** (-1 / B))
N = 0.5 * Ns
s = np.zeros_like(N)
hist = []
for i in range(1500):
    N = L * N * (1 + N) ** (-B)
    N = np.maximum(N, 1e-300)
    if i >= 900:
        d = L * (1 + N) ** (-B) * (1 - B * N / (1 + N))
        s += np.log(np.abs(d) + 1e-300)
    if i >= 1436:
        hist.append(np.log(N))
H = np.array(hist)
lyap = s / 600
cls = np.zeros_like(N, int)
cls[(mult >= 0)] = 0
cls[(mult < 0) & (mult > -1)] = 1
cyc = mult <= -1
spread = np.abs(H - H[-1]).max(axis=0)
per2 = np.abs(H[-1] - H[-3]) < 1e-6
cls[cyc & per2] = 2
cls[cyc & ~per2] = 3
cls[cyc & (lyap > 0.01)] = 4
cmap = ListedColormap([P.fill("positive"), P.light("positive"), P.fill("dna"), P.fill("highlight"),
                       P.fill("negative")])
fig, ax = plt.subplots(figsize=(7.0, 4.8))
ax.pcolormesh(L, B, cls, cmap=cmap, vmin=-0.5, vmax=4.5, shading="auto", rasterized=True)
lc = np.geomspace(1.05, 1e4, 400)
for level, ls in ((1, (0, (3, 2))), (2, "-")):
    bs = []
    for l in lc:
        g = bb * (1 - l ** (-1 / bb)) - level
        idx = np.where(np.diff(np.sign(g)))[0]
        bs.append(bb[idx[0]] if len(idx) else np.nan)
    ax.plot(lc, bs, color=P.ink(), lw=1, ls=ls)
ax.set_xscale("log")
labels = [("monotonic\ndamping", (3, 0.5)), ("damped\noscillation", (40, 1.55)), ("2-cycle", (200, 2.7)),
          ("cycles 4–32", (2500, 3.7)), ("chaos", (2500, 5.2))]
for t, (x0, y0) in labels:
    ax.text(x0, y0, t, fontsize=FS["small"], color=P.on_fill(), ha="center", va="center")
ax.set_xlim(1.05, 1e4)
ax.set_ylim(0.05, 6)
C.style_axes(ax, "λ (net reproductive rate at low density)", "b (type of density dependence)", box=True)
C.title(ax, "Hassell model: dynamics in the (λ, b) plane")
fig.tight_layout()
