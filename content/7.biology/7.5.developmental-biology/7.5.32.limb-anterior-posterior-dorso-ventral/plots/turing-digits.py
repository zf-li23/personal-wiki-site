"""Digits as a Turing pattern laid down at a growing tip (Section 32.5).

Schnakenberg kinetics (an activator u, standing for Sox9-promoting BMP activity, and a faster-diffusing inhibitor v):
u_t = Du lap u + g (a - u + u^2 v), v_t = Dv lap v + g (b - u^2 v), a = 0.1, b = 0.9, Du = 1, Dv = 40, with no-flux
sides. The autopod is a strip of width 60 (antero-posterior) that grows distally: only the distal 12 rows react
(the active zone under the AER); one row is added at the tip every 150 time steps, and rows that fall behind the
active zone are frozen (they differentiate). The kinetic rate g sets the wavelength (proportional to 1/sqrt(g));
the "Hox dose" h enters as g = 0.9 / h^2, so lowering distal Hox dosage shortens the wavelength (Sheth et al. 2012).
A-C: frozen patterns of u (cartilage where u is high) for h = 1, 0.8, 0.6. D: the number of condensations across
the strip from one-dimensional runs, against h.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q
from matplotlib.colors import LinearSegmentedColormap

P = bio.P
rng = np.random.default_rng(1)
a_, b_, Du, Dv = 0.1, 0.9, 1.0, 40.0
u0, v0 = a_ + b_, b_ / (a_ + b_) ** 2


def lap_x(A):
    out = np.empty_like(A)
    out[..., 1:-1] = A[..., 2:] - 2 * A[..., 1:-1] + A[..., :-2]
    out[..., 0] = A[..., 1] - A[..., 0]
    out[..., -1] = A[..., -2] - A[..., -1]
    return out


def grow(h, W=60, rows=90, act=12, every=150, dt=0.004):
    g = 0.9 / h ** 2
    U = np.full((act, W), u0) + rng.normal(0, 0.01, (act, W))
    V = np.full((act, W), v0)
    frozen = []
    nsteps = every * (rows - act)
    for s in range(nsteps):
        lu = lap_x(U)
        lv = lap_x(V)
        lu[1:-1] += U[2:] - 2 * U[1:-1] + U[:-2]
        lv[1:-1] += V[2:] - 2 * V[1:-1] + V[:-2]
        lu[0] += U[1] - U[0]
        lv[0] += V[1] - V[0]
        lu[-1] += U[-2] - U[-1]
        lv[-1] += V[-2] - V[-1]
        r = U * U * V
        U = U + dt * (Du * lu + g * (a_ - U + r))
        V = V + dt * (Dv * lv + g * (b_ - r))
        if (s + 1) % every == 0:
            frozen.append(U[0].copy())
            U = np.vstack([U[1:], U[-1:] + rng.normal(0, 0.01, (1, W))])
            V = np.vstack([V[1:], V[-1:]])
    return np.array(frozen + list(U))


def count1d(h, W=60, steps=6000, dt=0.004):
    g = 0.9 / h ** 2
    u = u0 + rng.normal(0, 0.01, W)
    v = np.full(W, v0)
    for _ in range(steps):
        r = u * u * v
        u, v = u + dt * (Du * lap_x(u) + g * (a_ - u + r)), v + dt * (Dv * lap_x(v) + g * (b_ - r))
    hi = u > u.mean()
    return int(np.sum(hi[1:] & ~hi[:-1]) + hi[0])


cmap = LinearSegmentedColormap.from_list("c", [P.surface(), P.fill("phalanges"), P.edge("phalanges")])
fig, ax = bio.canvas(30.0, 9.0)
for k, h in enumerate((1.0, 0.8, 0.6)):
    F = grow(h)
    x0 = 0.9 + 6.6 * k
    pa = C.axes_at(ax, (x0, 1.2, 5.6, 6.6))
    pa.imshow(F, origin="lower", cmap=cmap, aspect="auto", interpolation="bilinear",
              vmin=np.percentile(F, 5), vmax=np.percentile(F, 99))
    pa.set_xticks([])
    pa.set_yticks([])
    for sp in pa.spines.values():
        sp.set_color(P.muted())
        sp.set_linewidth(0.6)
    bio.panel(ax, "ABC"[k], (x0 - 0.5, 8.9))
    bio.label(ax, (x0 + 2.8, 8.4), f"Hox dose h = {h:g}", size="small")
bio.label(ax, (0.9, 0.7), "posterior", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (6.5, 0.7), "anterior", size="tiny", color=P.muted(), ha="right")
ax.annotate("", xy=(0.5, 7.6), xytext=(0.5, 1.4), arrowprops=dict(arrowstyle="->", color=P.muted(), lw=0.8))
bio.label(ax, (0.25, 4.5), "growth (proximal → distal)", size="tiny", color=P.muted(), rotation=90)

hs = np.linspace(0.45, 1.3, 14)
ns = [count1d(h) for h in hs]
pd_ = C.axes_at(ax, (21.6, 1.4, 7.6, 6.2))
pd_.plot(hs, ns, "o-", color=Q.line_color("phalanges"), ms=4.5, lw=1.3)
pd_.set_xlim(0.4, 1.35)
pd_.set_ylim(0, max(ns) + 1)
C.style_axes(pd_, "distal Hox dose h", "number of condensations")
bio.panel(ax, "D", (20.4, 8.9))
bio.label(ax, (21.6, 8.4), "Condensations across the autopod", size="small", ha="left")
