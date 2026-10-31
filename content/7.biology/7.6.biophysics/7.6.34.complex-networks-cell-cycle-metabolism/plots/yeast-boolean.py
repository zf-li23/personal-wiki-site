"""The Boolean network of the budding-yeast cell cycle (Li, Long, Lu, Ouyang and Tang, 2004).
A: the eleven nodes and their interactions (green: activation, a_ij = +1; red: inhibition,
a_ij = -1); Cln3, Cln1,2, Swi5, Cdc20/Cdc14 and Mcm1/SFF also degrade spontaneously when not
activated. Each node is updated synchronously by S_i(t+1) = 1 if sum_j a_ij S_j(t) > 0, 0 if < 0,
and keeps its state (or decays, for the self-degrading nodes) if the sum is zero. B: the trajectory
from the excited G1 state (Cln3 switched on by cell size): 12 steps through the phases of the
cycle (G1 at steps 1-3, S at 4, G2 at 5, M at 6-9, exit to G1 at 10-11), back to the stationary
G1 state (coloured: on). C: sizes of the basins of attraction of the seven
fixed points among all 2^11 = 2048 states: 1764 states (86 %) flow to the biological G1 state."""

import itertools
import numpy as np
import matplotlib.pyplot as plt
import wikigraph as G
import wikibio as bio
from wikibio import charts

P = bio.P
N = ["Cln3", "MBF", "SBF", "Cln1,2", "Cdh1", "Swi5", "Cdc20", "Clb5,6", "Sic1", "Clb1,2", "Mcm1"]
I = {n: i for i, n in enumerate(N)}
act = [("Cln3", "MBF"), ("Cln3", "SBF"), ("MBF", "Clb5,6"), ("SBF", "Cln1,2"), ("Clb5,6", "Mcm1"),
       ("Clb5,6", "Clb1,2"), ("Clb1,2", "Mcm1"), ("Clb1,2", "Cdc20"), ("Mcm1", "Clb1,2"), ("Mcm1", "Cdc20"),
       ("Mcm1", "Swi5"), ("Cdc20", "Swi5"), ("Cdc20", "Cdh1"), ("Cdc20", "Sic1"), ("Swi5", "Sic1")]
inh = [("Cln1,2", "Sic1"), ("Cln1,2", "Cdh1"), ("Clb5,6", "Sic1"), ("Clb5,6", "Cdh1"), ("Clb1,2", "Sic1"),
       ("Clb1,2", "Cdh1"), ("Clb1,2", "SBF"), ("Clb1,2", "MBF"), ("Clb1,2", "Swi5"), ("Cdc20", "Clb5,6"),
       ("Cdc20", "Clb1,2"), ("Sic1", "Clb5,6"), ("Sic1", "Clb1,2"), ("Cdh1", "Clb1,2")]
selfdeg = np.array([n in ("Cln3", "Cln1,2", "Swi5", "Cdc20", "Mcm1") for n in N])
A = np.zeros((11, 11), int)
for a, b in act:
    A[I[b], I[a]] = 1
for a, b in inh:
    A[I[b], I[a]] = -1


def step(s):
    h = A @ s
    new = np.where(h > 0, 1, np.where(h < 0, 0, s))
    return np.where((h == 0) & selfdeg, 0, new)


basins = {}
for bits in itertools.product((0, 1), repeat=11):
    s = np.array(bits)
    seen = set()
    while tuple(s) not in seen:
        seen.add(tuple(s))
        s = step(s)
    basins[tuple(s)] = basins.get(tuple(s), 0) + 1

fig = plt.figure(figsize=(11.0, 4.0))
gs = fig.add_gridspec(1, 3, width_ratios=(1.25, 1.1, 0.9), wspace=0.35, left=0.02, right=0.98, bottom=0.14, top=0.9)
ax = fig.add_subplot(gs[0])
pos = {"Cln3": (2.5, 6.0), "MBF": (1.3, 5.0), "SBF": (3.7, 5.0), "Clb5,6": (0.3, 3.7), "Cln1,2": (4.7, 3.7),
       "Clb1,2": (2.5, 3.2), "Sic1": (0.8, 1.8), "Cdh1": (4.2, 1.8), "Mcm1": (2.5, 4.6), "Cdc20": (2.5, 0.6),
       "Swi5": (0.3, 0.3)}
ax.set_xlim(-0.6, 5.6)
ax.set_ylim(-0.4, 6.6)
ax.set_aspect("equal")
ax.axis("off")
edges = act + inh
hl = {e: G.GREEN for e in act}
hl.update({e: G.RED for e in inh})
G.draw(ax, pos, edges, directed=True, highlight=hl, radius=0.36, width=0.55,
       vertex_labels={n: n for n in N})
for t in ax.texts:
    t.set_fontsize(6.5)
charts.title(ax, "A  Network")

ax = fig.add_subplot(gs[1])
s = np.array([1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0])
traj = [s]
for _ in range(12):
    s = step(s)
    traj.append(s)
T = np.array(traj).T
from matplotlib.colors import ListedColormap
ax.imshow(T, cmap=ListedColormap([P.light("neutral"), P.fill("protein")]), aspect="auto", vmin=0, vmax=1,
          interpolation="nearest")
ax.set_yticks(range(11))
ax.set_yticklabels(N)
ax.set_xticks(range(13))
charts.style_axes(ax, "time step", None, box=True)
charts.title(ax, "B  The biological pathway")

ax = fig.add_subplot(gs[2])
sizes = sorted(basins.values(), reverse=True)
ax.bar(range(1, len(sizes) + 1), sizes, color=[P.fill("protein")] + [P.fill("neutral")] * (len(sizes) - 1),
       edgecolor=[P.edge("protein")] + [P.edge("neutral")] * (len(sizes) - 1), lw=0.6)
for i, v in enumerate(sizes):
    ax.text(i + 1, v * 1.15, str(v), ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_yscale("log")
ax.set_ylim(0.7, 5000)
ax.set_xticks(range(1, len(sizes) + 1))
charts.style_axes(ax, "fixed point (rank)", "basin size (states)")
charts.title(ax, "C  Basins of attraction")
