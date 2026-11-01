"""Growth with and without preferential attachment (m = 3 edges per new vertex, N = 100000).
A: degree k_i(t) of the vertices added at t_i = 10, 100, 1000 and 10000 in a Barabasi-Albert graph
(averaged over the vertices t_i, ..., t_i + t_i/20 and four realizations),
with the continuum prediction m (t/t_i)^(1/2). B: degree distributions with preferential attachment
(power law, exact form 2m(m+1)/k(k+1)(k+2)) and with uniform attachment (geometric, exact form
(m/(m+1))^(k-m)/(m+1)), logarithmic bins."""

import numpy as np
import matplotlib.pyplot as plt
import wikigraph as G

rng = np.random.default_rng(5)
N, m = 100000, 3
tracked = (10, 100, 1000, 10000)
checkpoints = np.unique(np.round(np.logspace(1, 5, 60)).astype(int))


def grow(preferential):
    pool = np.empty(2 * m * N, dtype=np.int64)
    deg = np.zeros(N, dtype=np.int64)
    size = 0
    for v in range(m + 1):
        for u in range(v):
            pool[size:size + 2] = (u, v)
            size += 2
            deg[u] += 1
            deg[v] += 1
    history = {t: [] for t in tracked}
    for v in range(m + 1, N):
        chosen = set()
        while len(chosen) < m:
            chosen.add(int(pool[rng.integers(size)]) if preferential else int(rng.integers(v)))
        for u in chosen:
            pool[size:size + 2] = (u, v)
            size += 2
            deg[u] += 1
        deg[v] += m
        if v + 1 in set_checkpoints:
            for t in tracked:
                if t + t // 20 < v:
                    history[t].append((v + 1, deg[t:t + 1 + t // 20].mean()))
    return deg, history


set_checkpoints = set(checkpoints.tolist())
runs = [grow(True) for _ in range(4)]
deg_pa = runs[0][0]
hist = {t: np.mean([np.array(r[1][t]) for r in runs], axis=0) for t in tracked}
deg_u, _ = grow(False)

fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.0, 3.5))
fig.subplots_adjust(wspace=0.3, left=0.08, right=0.98, bottom=0.16, top=0.9)
for t, col in zip(tracked, (G.RED, G.AMBER, G.GREEN, G.BLUE)):
    h = np.array(hist[t])
    ax.loglog(h[:, 0], h[:, 1], "o", ms=3, color=col, label=rf"$t_i = {t}$")
    tt = np.logspace(np.log10(t), 5, 50)
    ax.loglog(tt, m * np.sqrt(tt / t), color=col, lw=0.9)
ax.set_xlabel(r"time $t$ (number of vertices)")
ax.set_ylabel(r"degree $k_i(t)$")
ax.set_title(r"A  $k_i(t) = m\,(t/t_i)^{1/2}$", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper left")

for k, col, name in ((deg_pa, G.RED, "preferential attachment"), (deg_u, G.BLUE, "uniform attachment")):
    edges = np.unique(np.floor(np.logspace(np.log10(m), np.log10(k.max() + 1), 26)).astype(int))
    h, _ = np.histogram(k, bins=edges)
    mid = np.sqrt(edges[:-1] * (edges[1:] - 1).clip(edges[:-1]))
    bx.loglog(mid[h > 0], (h / np.diff(edges) / N)[h > 0], "o", ms=3.5, color=col, label=name)
kk = np.arange(m, 2000)
bx.loglog(kk, 2 * m * (m + 1) / (kk * (kk + 1) * (kk + 2)), color=G.RED, lw=0.9)
kk = np.arange(m, 60)
bx.loglog(kk, (m / (m + 1)) ** (kk - m) / (m + 1), color=G.BLUE, lw=0.9)
bx.set_ylim(1e-9, 1)
bx.set_xlabel(r"degree $k$")
bx.set_ylabel(r"$p_k$")
bx.set_title("B  both ingredients are needed", loc="left", fontsize=10)
bx.legend(frameon=False, fontsize=8, loc="lower left")
