"""The four kinds of bifurcation met in the course, each drawn for one model of the course.

A  Transcritical: Levins metapopulation with habitat destruction (Theorem 16.4.1),
   p* = 1 - D - e/c; the occupied state meets p = 0 and exchanges stability at D = 1 - e/c.
B  Saddle-node with hysteresis: Carpenter lake model (Proposition 46.2.2),
   dx/dt = a - x + r x^q / (1 + x^q), r = 1, q = 8; equilibria a = x - r x^q/(1 + x^q).
C  Transcritical and Hopf: Rosenzweig-MacArthur model (Definition 26.1.1), scaled
   dx/dt = x (1 - x / kappa) - x y / (1 + x),  dy/dt = y (gamma x / (1 + x) - delta),
   gamma = 2, delta = 0.5: predator invades at kappa = x* = delta/(gamma - delta) = 1/3, Hopf at
   kappa_H = 1 + 2 x* = 5/3 (Proposition 26.1.1); prey range on the limit cycle from simulation.
D  Period doubling: Ricker map N' = N exp(r (1 - N)) (Section 12.1), first doubling at r = 2.
Solid: stable; dashed: unstable.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
cs, cu, cc = C.line("dna"), C.line("negative"), C.line("positive")
dash = (0, (3, 2))

fig, axes = plt.subplots(1, 4, figsize=(15.0, 3.9))

# A: transcritical, Levins with habitat destruction
ax = axes[0]
e_over_c = 0.3
D = np.linspace(0, 1, 300)
Dc = 1 - e_over_c
ax.plot(D[D <= Dc], 1 - e_over_c - D[D <= Dc], color=cs, lw=2)
ax.plot(D[D <= Dc], 0 * D[D <= Dc], color=cu, lw=1.4, ls=dash)
ax.plot(D[D >= Dc], 0 * D[D >= Dc], color=cs, lw=2)
ax.plot(D[D >= Dc], 1 - e_over_c - D[D >= Dc], color=cu, lw=1.4, ls=dash)
ax.plot([Dc], [0], "o", color=cs, ms=5)
ax.text(Dc - 0.03, 0.1, "threshold\nD = 1 − e/c", fontsize=FS["tiny"], color=P.ink(), ha="right")
ax.set_xlim(0, 1)
ax.set_ylim(-0.2, 0.8)
C.style_axes(ax, "habitat destroyed D", "occupancy p*")
C.title(ax, "A  Transcritical: persistence threshold")

# B: saddle-node folds and hysteresis, Carpenter lake
ax = axes[1]
r, q = 1.0, 8
x = np.linspace(0.0, 1.6, 2000)
a = x - r * x**q / (1 + x**q)
da = np.gradient(a, x)
stable = da > 0
for mask, col, ls, lw in ((stable, cs, "-", 2), (~stable, cu, dash, 1.4)):
    seg = np.where(mask, x, np.nan)
    ax.plot(np.where(mask, a, np.nan), seg, color=col, ls=ls, lw=lw)
idx = np.where(np.diff(np.sign(da)) != 0)[0]
folds = [(a[i], x[i]) for i in idx]
for af, xf in folds:
    ax.plot([af], [xf], "o", color=cu, ms=5)
if len(folds) == 2:
    (a_hi, x_hi), (a_lo, x_lo) = folds
    up = x[np.argmin(np.abs(a[x > x_lo] - a_hi)) + np.sum(x <= x_lo)]
    dn = x[np.argmin(np.abs(a[x < x_hi] - a_lo))]
    ax.annotate("", (a_hi, up), (a_hi, x_hi), arrowprops=dict(arrowstyle="-|>", color=P.muted(), lw=0.9))
    ax.annotate("", (a_lo, dn), (a_lo, x_lo), arrowprops=dict(arrowstyle="-|>", color=P.muted(), lw=0.9))
ax.text(0.02, 1.45, "eutrophic", fontsize=FS["tiny"], color=P.ink())
ax.text(0.56, 0.3, "oligotrophic", fontsize=FS["tiny"], color=P.ink())
ax.set_xlim(0, 0.8)
ax.set_ylim(0, 1.6)
C.style_axes(ax, "phosphorus input a", "lake phosphorus x*")
C.title(ax, "B  Saddle-node: folds and hysteresis")

# C: transcritical and Hopf, Rosenzweig-MacArthur
ax = axes[2]
gamma, delta = 2.0, 0.5
xs = delta / (gamma - delta)
kH = 1 + 2 * xs


def rm(t, z, kap):
    x_, y_ = z
    f = x_ / (1 + x_)
    return [x_ * (1 - x_ / kap) - y_ * f, y_ * (gamma * f - delta)]


kap = np.linspace(0.05, 5.0, 400)
ax.plot(kap[kap <= xs], kap[kap <= xs], color=cs, lw=2)
ax.plot(kap[kap > xs], kap[kap > xs], color=cu, lw=1.4, ls=dash)
k1 = kap[(kap > xs) & (kap <= kH)]
k2 = kap[kap > kH]
ax.plot(k1, xs + 0 * k1, color=cs, lw=2)
ax.plot(k2, xs + 0 * k2, color=cu, lw=1.4, ls=dash)
kc = np.linspace(kH + 0.02, 5.0, 26)
lo, hi = [], []
for k in kc:
    s = solve_ivp(rm, (0, 600), [xs * 1.1, 0.5], args=(k,), rtol=1e-8, atol=1e-10, max_step=0.5)
    tail = s.y[0][s.t > 400]
    lo.append(tail.min())
    hi.append(tail.max())
ax.plot(kc, hi, color=cc, lw=2, label="limit cycle (prey max, min)")
ax.plot(kc, lo, color=cc, lw=2)
ax.plot([xs, kH], [xs, xs], "o", color=cs, ms=5)
ax.text(xs + 0.1, 0.9, "predator\ninvades", fontsize=FS["tiny"], color=P.ink())
ax.text(kH + 0.05, 0.05, "Hopf", fontsize=FS["tiny"], color=P.ink())
ax.set_yscale("log")
ax.set_ylim(0.01, 6)
ax.set_xlim(0, 5)
C.style_axes(ax, "enrichment κ", "prey density x")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
C.title(ax, "C  Transcritical and Hopf: enrichment")

# D: period doubling, Ricker map
ax = axes[3]
rr = np.linspace(1.5, 3.6, 1400)
n = np.full_like(rr, 0.5)
for _ in range(600):
    n = n * np.exp(rr * (1 - n))
pts_r, pts_n = [], []
for _ in range(120):
    n = n * np.exp(rr * (1 - n))
    pts_r.append(rr)
    pts_n.append(n.copy())
ax.plot(np.concatenate(pts_r), np.concatenate(pts_n), ",", color=cs, alpha=0.6, rasterized=True)
ax.axvline(2.0, color=P.muted(), lw=0.6, ls=":")
ax.axvline(2.6924, color=P.muted(), lw=0.6, ls=":")
ax.text(2.03, 3.4, "2-cycle", fontsize=FS["tiny"], color=P.ink())
ax.text(2.72, 3.4, "chaos", fontsize=FS["tiny"], color=P.ink())
ax.set_xlim(1.5, 3.6)
ax.set_ylim(0, 3.8)
C.style_axes(ax, "growth rate r", "density N (scaled by K)")
C.title(ax, "D  Period doubling: discrete generations")

fig.tight_layout()
