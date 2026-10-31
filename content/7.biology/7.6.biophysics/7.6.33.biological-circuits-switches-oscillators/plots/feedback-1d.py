"""One-dimensional feedback. A: positive autoregulation dx/dt = b0 + V x^2/(K^2 + x^2) - d x
(K = 1, d = 1, b0 = 0.1): production curves for V = 1.5, 2.2 and 3.2 against the degradation line;
their intersections are the fixed points (filled: stable, open: unstable), and the arrows on the
axis show the flow for V = 2.2. B: the fixed points against V: two saddle-node bifurcations bound a
bistable range in which the state depends on history (hysteresis, arrows). C: negative
autoregulation as homeostasis: steady-state level against the degradation rate constant d for an
unregulated gene (x* = b/d) and for a strongly self-repressing gene (dx/dt = V/(1 + (x/K)^4) - d x
with V = 20, K = 1), normalized at d = 1."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
b0, K, d = 0.1, 1.0, 1.0
prod = lambda x, V: b0 + V * x ** 2 / (K ** 2 + x ** 2)


def fixed(V):
    xs = np.linspace(0, 6, 6001)
    g = prod(xs, V) - d * xs
    out = []
    for i in np.where(np.sign(g[1:]) != np.sign(g[:-1]))[0]:
        r = brentq(lambda x: prod(x, V) - d * x, xs[i], xs[i + 1])
        h = 1e-6
        slope = (prod(r + h, V) - prod(r - h, V)) / (2 * h) - d
        out.append((r, slope < 0))
    return out


fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.3))
fig.subplots_adjust(wspace=0.32, left=0.06, right=0.98, bottom=0.17, top=0.88)
ax = axs[0]
x = np.linspace(0, 4, 400)
ax.plot(x, d * x, color=P.ink(), lw=1.2, label="degradation d x")
for V, tok in ((1.5, "dna"), (2.2, "protein"), (3.2, "blood")):
    ax.plot(x, prod(x, V), color=charts.line(tok), lw=1.5, label=f"production, V = {V}")
    for r, st in fixed(V):
        ax.plot(r, d * r, "o", ms=5, mfc=charts.line(tok) if st else P.surface(), mec=charts.line(tok))
fp = [r for r, st in fixed(2.2)]
for x0, x1 in (((fp[0] + fp[1]) / 2 + 0.05, (fp[0] + fp[1]) / 2 - 0.1),
               ((fp[1] + fp[2]) / 2 - 0.2, (fp[1] + fp[2]) / 2 + 0.2), (fp[2] + 0.8, fp[2] + 0.4)):
    ax.annotate("", (x1, -0.12), (x0, -0.12), arrowprops=dict(arrowstyle="->", color=P.ink(), lw=0.9))
ax.set_ylim(-0.25, 4)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "x", "rate")
charts.title(ax, "A  Production and removal")

ax = axs[1]
Vs = np.linspace(0.5, 4.5, 400)
st_x, st_V, un_x, un_V = [], [], [], []
for V in Vs:
    for r, st in fixed(V):
        (st_x if st else un_x).append(r)
        (st_V if st else un_V).append(V)
ax.plot(st_V, st_x, ".", ms=1.6, color=charts.line("protein"))
ax.plot(un_V, un_x, ".", ms=1.0, color=P.muted())
up = max(v for v in st_V if v < 3.0 and min(r for r, st in fixed(v)) < 0.5 and len(fixed(v)) == 3)
lo = min(un_V)
ax.annotate("", (up, 1.9), (up, 0.25), arrowprops=dict(arrowstyle="->", color=charts.line("blood"), lw=1.0))
ax.annotate("", (lo, 0.25), (lo, 1.2), arrowprops=dict(arrowstyle="->", color=charts.line("dna"), lw=1.0))
ax.text(2.25, 0.62, "unstable", fontsize=bio.core.FONT["tiny"], color=P.muted())
charts.style_axes(ax, "maximal production V", "fixed points x*")
charts.title(ax, "B  Bistability and hysteresis")

ax = axs[2]
ds = np.linspace(0.5, 2.0, 100)
xs_nar = [brentq(lambda x: 20 / (1 + (x / K) ** 4) - dd * x, 1e-6, 50) for dd in ds]
x1 = brentq(lambda x: 20 / (1 + (x / K) ** 4) - x, 1e-6, 50)
ax.plot(ds, 1 / ds, color=charts.line("dna"), lw=1.5, label="unregulated")
ax.plot(ds, np.array(xs_nar) / x1, color=charts.line("protein"), lw=1.5, label="negative autoregulation")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink())
charts.style_axes(ax, "degradation rate constant d", "relative steady state")
charts.title(ax, "C  Homeostasis")
