"""Prion-like spread of pathology on a connectome: network diffusion with local autocatalytic growth.

Synthetic connectome: 40 regions on a ring of 4 lobes (10 regions each); connection weights decay with
distance along the ring (exp(-d / 2)) plus a few random long-range links; L = D - W is the graph Laplacian.
Pathology x_k in [0, 1] obeys a Fisher-KPP equation on the graph:
  dx/dt = -rho L x + alpha x (1 - x),   rho = 0.08, alpha = 0.6 (time in years),
seeded with x = 0.05 in region 0 ("entorhinal cortex"). Pure diffusion (alpha = 0) is the network
diffusion model of Raj et al. 2012; the growth term makes misfolding self-templating.
A: pathology in each region against time, regions ordered by shortest-path distance from the seed.
B: time courses of three regions at increasing distance; the arrival times grow with distance, giving a
staging sequence.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.sparse.csgraph import shortest_path

import wikibio as bio

P = bio.P
rng = np.random.default_rng(4)
n = 40
idx = np.arange(n)
d = np.abs(idx[:, None] - idx[None, :])
d = np.minimum(d, n - d)
W = np.exp(-d / 2.0)
np.fill_diagonal(W, 0)
for _ in range(6):
    i, j = rng.choice(n, 2, replace=False)
    W[i, j] = W[j, i] = 0.5
L = np.diag(W.sum(1)) - W
rho, alpha = 0.08, 0.6


def rhs(t, x):
    return -rho * L @ x + alpha * x * (1 - x)


x0 = np.zeros(n)
x0[0] = 0.05
T = np.linspace(0, 40, 400)
sol = solve_ivp(rhs, (0, 40), x0, t_eval=T, rtol=1e-7)
X = sol.y
dist = shortest_path(1.0 / np.where(W > 0, W, np.inf), directed=False)[0]
order = np.argsort(dist)

fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.9), gridspec_kw={"width_ratios": [1.3, 1]})
ax = axs[0]
im = ax.imshow(X[order], aspect="auto", origin="lower", extent=[0, 40, 0, n], cmap="Reds", vmin=0, vmax=1)
ax.set_xlabel("Time / years")
ax.set_ylabel("Region (ordered by distance from seed)")
ax.set_title("A  Spread over the connectome", loc="left", fontsize=10)
fig.colorbar(im, ax=ax, fraction=0.046, label="Pathology $x$")
ax = axs[1]
for k, col in zip((order[0], order[12], order[30]), (P.edge("negative"), P.edge("protein"), P.edge("dna"))):
    ax.plot(T, X[k], color=col, lw=1.8, label=f"region at path length {dist[k]:.1f}")
ax.set_xlabel("Time / years")
ax.set_ylabel("Pathology $x$")
ax.legend(frameon=False, fontsize=7.5, loc="lower right")
ax.set_title("B  Staging by distance", loc="left", fontsize=10)
ax.grid(True, alpha=0.3)
fig.tight_layout()
