"""The LPA model of the flour beetle Tribolium castaneum (Section 12.6.2).

L_{t+1} = b A_t exp(-c_el L_t - c_ea A_t), P_{t+1} = (1 - mu_l) L_t,
A_{t+1} = P_t exp(-c_pa A_t) + (1 - mu_a) A_t  (time step two weeks),
with the parameter estimates of Dennis et al. (1997): b = 6.598, c_el = 0.01209, c_ea = 0.01155,
mu_l = 0.2055, and adult mortality set experimentally to mu_a = 0.96. The recruitment parameter c_pa
(cannibalism of pupae by adults) is varied.
A: bifurcation diagram of adult numbers against c_pa (1500 transient steps, 150 plotted); dashed lines:
the values imposed in the experiments of Costantino et al. (1997).
B: the largest Lyapunov exponent (product of Jacobians, 3000 steps).
C: phase portraits (L, A) of the attractor at c_pa = 0.05 (8-cycle), 0.10 (invariant loop), 0.35 (chaos)
and 1.0 (3-cycle).
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
b, cel, cea, mul, mua = 6.598, 0.01209, 0.01155, 0.2055, 0.96


def step(L, Pp, A, cpa):
    return b * A * np.exp(-cel * L - cea * A), (1 - mul) * L, Pp * np.exp(-cpa * A) + (1 - mua) * A


cp = np.linspace(0.0, 1.0, 800)
L = np.full_like(cp, 100.0)
Pp = np.full_like(cp, 100.0)
A = np.full_like(cp, 100.0)
for _ in range(1500):
    L, Pp, A = step(L, Pp, A, cp)
X, Y = [], []
for _ in range(150):
    L, Pp, A = step(L, Pp, A, cp)
    X.append(cp)
    Y.append(A)
lyap = np.zeros_like(cp)
v = np.ones((3, len(cp))) / np.sqrt(3)
for _ in range(3000):
    e = np.exp(-cel * L - cea * A)
    ea = np.exp(-cp * A)
    v0 = b * e * (-cel * A * v[0] + (1 - cea * A) * v[2])
    v1 = (1 - mul) * v[0]
    v2 = ea * v[1] + (-cp * Pp * ea + 1 - mua) * v[2]
    v = np.array([v0, v1, v2])
    nv = np.linalg.norm(v, axis=0)
    lyap += np.log(nv)
    v /= nv
    L, Pp, A = step(L, Pp, A, cp)
lyap /= 3000

fig = plt.figure(figsize=(13.0, 4.6))
gs = fig.add_gridspec(2, 3, width_ratios=[1.5, 0.05, 1.0], height_ratios=[1.6, 1], wspace=0.25)
ax = fig.add_subplot(gs[0, 0])
ax.plot(np.concatenate(X), np.concatenate(Y), ",", color=P.ink(), alpha=0.35, rasterized=True)
for c in (0.0, 0.05, 0.10, 0.25, 0.35, 0.50, 1.0):
    ax.axvline(c, color=C.line("rna"), lw=0.6, ls=(0, (3, 2)))
ax.set_ylim(0, 200)
C.style_axes(ax, None, "adults A")
C.title(ax, "A  Bifurcation diagram (μₐ = 0.96)")
ax2 = fig.add_subplot(gs[1, 0], sharex=ax)
ax2.plot(cp, lyap, color=C.line("dna"), lw=0.9)
ax2.fill_between(cp, 0, lyap, where=lyap > 0, color=P.fill("negative"), alpha=0.6, lw=0)
ax2.axhline(0, color=P.muted(), lw=0.7)
ax2.set_ylim(-0.4, 0.2)
C.style_axes(ax2, "cannibalism of pupae by adults, c_pa", "λ")
C.title(ax2, "B  Largest Lyapunov exponent")
sub = gs[:, 2].subgridspec(2, 2, hspace=0.45, wspace=0.35)
for k, (c, name) in enumerate(((0.05, "8-cycle"), (0.10, "invariant loop"), (0.35, "chaos"), (1.0, "3-cycle"))):
    a3 = fig.add_subplot(sub[k // 2, k % 2])
    L1, P1, A1 = 100.0, 100.0, 100.0
    for _ in range(3000):
        L1, P1, A1 = step(L1, P1, A1, c)
    pts = []
    for _ in range(1500):
        L1, P1, A1 = step(L1, P1, A1, c)
        pts.append((L1, A1))
    pts = np.array(pts)
    a3.plot(pts[:, 0], pts[:, 1], ".", ms=1.5 if k in (1, 2) else 5, color=C.line("rna"))
    C.style_axes(a3, "L", "A", size="tiny")
    C.title(a3, f"c_pa = {c:g}: {name}", size="tiny")
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.12, top=0.93)
