"""A Waddington landscape from a two-gene toggle switch (simulated). Two genes repress each other,
dx/dt = a/(1 + y^2) - x and dy/dt = a/(1 + x^2) - y with a = 3, plus Gaussian noise of strength
sigma = 0.2 (Langevin dynamics, Euler-Maruyama steps of 0.01). A: the quasi-potential U = -ln p(x, y)
estimated from the stationary distribution of 4000 simulated cells; the two valleys are the attractors
(x, y) = (2.62, 0.38) and (0.38, 2.62), separated by a saddle at (1.21, 1.21); thin lines are the
nullclines; ten trajectories started near the saddle fall into one valley or the other (colored by the valley reached). B: the probability
that a cell started at the saddle ends in the x-high valley when the inputs are biased,
a_x = a(1 + delta), a_y = a(1 - delta), for two noise levels: a small bias decides the fate of most cells
when the noise is weak, while strong noise makes the decision graded."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
a, n, dt = 3.0, 2.0, 0.01


def drift(x, y, ax_=a, ay_=a):
    return ax_ / (1 + y ** n) - x, ay_ / (1 + x ** n) - y


def run(x, y, steps, sigma, ax_=a, ay_=a):
    for _ in range(steps):
        fx, fy = drift(x, y, ax_, ay_)
        x = np.abs(x + fx * dt + sigma * np.sqrt(dt) * rng.standard_normal(x.shape))
        y = np.abs(y + fy * dt + sigma * np.sqrt(dt) * rng.standard_normal(y.shape))
    return x, y


fig, axs = plt.subplots(1, 2, figsize=(9.6, 4.0), gridspec_kw={"width_ratios": [1.15, 1]})
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.15, top=0.9, wspace=0.28)

# A: quasi-potential from the stationary distribution
sigma = 0.2
N = 4000
x0 = rng.uniform(0, 3, N)
y0 = rng.uniform(0, 3, N)
xs, ys = [], []
x, y = run(x0, y0, 800, sigma)
for _ in range(20):
    x, y = run(x, y, 100, sigma)
    xs.append(x.copy()); ys.append(y.copy())
xs = np.concatenate(xs); ys = np.concatenate(ys)
edges = np.linspace(0, 3.4, 69)
H, _, _ = np.histogram2d(xs, ys, bins=[edges, edges], density=True)
U = -np.log(H.T + 1e-3)
U -= U.min()
cen = 0.5 * (edges[1:] + edges[:-1])
ax = axs[0]
cs = ax.contourf(cen, cen, np.where(U < 7.0, U, np.nan), levels=np.linspace(0, 7.0, 15), cmap="Blues_r")
g = np.linspace(0, 3.4, 200)
ax.plot(a / (1 + g ** n), g, color=P.muted(), lw=0.8)
ax.plot(g, a / (1 + g ** n), color=P.muted(), lw=0.8)
for t in range(10):
    xt, yt = [np.array([1.21 + 0.02 * rng.standard_normal()])], [np.array([1.21 + 0.02 * rng.standard_normal()])]
    for _ in range(100):
        xn, yn = run(xt[-1], yt[-1], 10, sigma)
        xt.append(xn); yt.append(yn)
    xt, yt = np.concatenate(xt), np.concatenate(yt)
    ax.plot(xt, yt, color=charts.line("rna" if xt[-1] > yt[-1] else "positive"), lw=0.8, alpha=0.9)
for px, py, lab in [(2.618, 0.382, "attractor 1"), (0.382, 2.618, "attractor 2"), (1.213, 1.213, "saddle")]:
    ax.plot(px, py, "o" if lab != "saddle" else "s", color=P.ink(), ms=5, mfc=P.surface() if lab == "saddle" else P.ink())
    ax.text(px + 0.1, py + 0.12, lab, fontsize=7.5, color=P.ink(),
            bbox=dict(boxstyle="round,pad=0.15", fc=P.surface(), ec="none", alpha=0.8))
ax.set_xlim(0, 3.4); ax.set_ylim(0, 3.4)
ax.set_aspect("equal")
cb = fig.colorbar(cs, ax=ax, fraction=0.046, pad=0.03)
cb.ax.tick_params(labelsize=7, colors=P.muted(), labelcolor=P.ink())
cb.set_label("quasi-potential  -ln p", fontsize=7.5, color=P.ink())
charts.style_axes(ax, "gene X", "gene Y")
charts.title(ax, "A  Landscape of a toggle switch")
print("U at saddle bin", U[np.searchsorted(cen, 1.21), np.searchsorted(cen, 1.21)])

# B: commitment probability under biased inputs
ax = axs[1]
deltas = np.linspace(-0.1, 0.1, 11)
for sig, tok, mk in [(0.15, "dna", "o-"), (0.45, "rna", "s-")]:
    pr = []
    for d in deltas:
        M = 1000
        x, y = run(np.full(M, 1.2134), np.full(M, 1.2134), 1500, sig, a * (1 + d), a * (1 - d))
        pr.append(np.mean(x > y))
    pr = np.array(pr)
    ax.plot(deltas, pr, mk, color=charts.line(tok), ms=4, lw=1.4, label=f"noise sigma = {sig}")
    print("B", sig, np.round(pr, 3))
ax.axhline(0.5, color=P.muted(), lw=0.6, ls="--")
ax.legend(frameon=False, fontsize=7.5, loc="upper left")
ax.set_ylim(-0.02, 1.02)
charts.style_axes(ax, "input bias delta", "fraction of cells in attractor 1")
charts.title(ax, "B  A small bias decides the fate")
