"""Host-parasitoid dynamics in space (Section 27.4), after Hassell, Comins and May (1991).

A coupled map lattice: on each cell of a 50 x 50 grid the Nicholson-Bailey model runs with
lam = 2, a = 1, c = 1; then a fraction muH of the hosts and muP of the parasitoids in each cell
moves, in equal parts, to the eight neighbouring cells (individuals leaving the grid are lost).
The simulation starts with hosts and parasitoids in the central cell only and runs 1500 generations.
A-C: host density (log scale; background colour = few hosts, green = many) at generation 1500 for (muH, muP) = (0.5, 0.5):
spiral waves; (0.05, 0.3): spatial chaos; (0.05, 0.9): a checkerboard texture with irregular patches, close to the
"crystal lattice" regime of Hassell, Comins and May.
D: total host number over the last 300 generations for the spiral case; the local dynamics are
violently unstable, but the regional populations persist.
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT


def disperse(X, mu):
    Z = np.zeros((X.shape[0] + 2, X.shape[1] + 2))
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx or dy:
                Z[1 + dx:Z.shape[0] - 1 + dx, 1 + dy:Z.shape[1] - 1 + dy] += mu * X / 8
    return (1 - mu) * X + Z[1:-1, 1:-1]


def run(n, muH, muP, T, lam=2.0, a=1.0):
    H = np.zeros((n, n))
    Q = np.zeros((n, n))
    H[n // 2, n // 2], Q[n // 2, n // 2] = 1.0, 0.1
    tot = []
    for _ in range(T):
        e = np.exp(-a * Q)
        H, Q = lam * H * e, H * (1 - e)
        H, Q = disperse(H, muH), disperse(Q, muP)
        tot.append(H.sum())
    return H, np.array(tot)


fig = plt.figure(figsize=(13.5, 4.0))
gs = fig.add_gridspec(1, 4, width_ratios=[1, 1, 1, 1.4])
cmap = plt.matplotlib.colors.LinearSegmentedColormap.from_list("h", [P.surface(), P.fill("positive"), P.edge("positive")])
for i, (muH, muP, lab) in enumerate([(0.5, 0.5, "A  Spirals"), (0.05, 0.3, "B  Spatial chaos"),
                                     (0.05, 0.9, "C  Checkerboard and patches")]):
    H, tot = run(50, muH, muP, 1500)
    ax = fig.add_subplot(gs[0, i])
    ax.imshow(np.log10(H + 1e-4), cmap=cmap, vmin=-3, vmax=1.5, interpolation="nearest")
    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_color(P.muted())
    C.title(ax, f"{lab}\nμH = {muH}, μP = {muP}")
    if i == 0:
        spiral_tot = tot
ax = fig.add_subplot(gs[0, 3])
ax.plot(np.arange(1200, 1500), spiral_tot[1200:] / 2500, color=C.line("positive"), lw=1.0)
ax.set_ylim(0, None)
C.style_axes(ax, "Generation", "Mean hosts per cell")
C.title(ax, "D  Regional persistence (spirals)")
fig.tight_layout()
