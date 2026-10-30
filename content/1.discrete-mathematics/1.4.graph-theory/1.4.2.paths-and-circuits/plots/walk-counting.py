import matplotlib.pyplot as plt
import numpy as np
import wikigraph as G

# the digraph D of Section 1.4 of Chapter 1
pos = {"v1": (0, 1.0), "v2": (1.8, 2.0), "v3": (1.8, 0), "v4": (3.6, 1.0)}
names = {v: f"$v_{v[1]}$" for v in pos}
arcs = [("v1", "v2"), ("v1", "v3"), ("v2", "v3"), ("v3", "v4"), ("v4", "v2")]
titles = ["length 2: $v_1 v_3 v_4$", "length 3: $v_1 v_2 v_3 v_4$", "closed, length 3: $v_2 v_3 v_4 v_2$"]
fig, axes = G.panels(3, 3.6, 2.0, titles=titles)
walks = [["v1", "v3", "v4"], ["v1", "v2", "v3", "v4"], ["v2", "v3", "v4", "v2"]]
for ax, w, c in zip(axes, walks, [G.BLUE, G.RED, G.GREEN]):
    hl = {(w[k], w[k + 1]): c for k in range(len(w) - 1)}
    hl[w[0]] = c
    G.draw(ax, pos, arcs, directed=True, highlight=hl, vertex_labels=names)

A = np.array([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 1, 0, 0]])
fig2, mats = plt.subplots(1, 3, figsize=(8.4, 2.4))
vs = [f"$v_{i}$" for i in range(1, 5)]
for ax, k in zip(mats, [1, 2, 3]):
    M = np.linalg.matrix_power(A, k)
    for i in range(4):
        for j in range(4):
            x = M[i, j]
            mark = (k, i, j) in {(2, 0, 3), (3, 0, 3), (3, 1, 1), (3, 2, 2), (3, 3, 3)}
            ax.text(j, i, str(x), ha="center", va="center", fontsize=11,
                    color=G.RED if mark else (G.INK if x else G.GREY), fontweight="bold" if x else "normal")
    ax.set_xlim(-0.6, 3.6)
    ax.set_ylim(3.6, -0.6)
    ax.set_xticks(range(4), vs)
    ax.set_yticks(range(4), vs)
    ax.xaxis.tick_top()
    ax.tick_params(length=0)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_title(f"$A^{k}$" if k > 1 else "$A$", pad=22, fontsize=11)
fig2.tight_layout()
