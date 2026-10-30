import matplotlib.pyplot as plt
import numpy as np
import wikigraph as G

A = np.array([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 1, 0, 0]])
P = A.copy()
stages = [P.copy()]
for i in range(4):
    for j in range(4):
        for k in range(4):
            P[j, k] |= P[j, i] & P[i, k]
    stages.append(P.copy())

fig, axes = plt.subplots(1, 5, figsize=(11.0, 2.5))
vs = [f"$v_{i}$" for i in range(1, 5)]
for s, ax in enumerate(axes):
    M = stages[s]
    if s:
        # the pivot row and column of this round
        ax.add_patch(plt.Rectangle((-0.5, s - 1.5), 4, 1, color=G.AMBER, alpha=0.18, lw=0))
        ax.add_patch(plt.Rectangle((s - 1.5, -0.5), 1, 4, color=G.AMBER, alpha=0.18, lw=0))
    for i in range(4):
        for j in range(4):
            new = s > 0 and M[i, j] and not stages[s - 1][i, j]
            ax.text(j, i, str(M[i, j]), ha="center", va="center", fontsize=11,
                    color=G.RED if new else (G.INK if M[i, j] else G.GREY),
                    fontweight="bold" if M[i, j] else "normal")
    ax.set_xlim(-0.6, 3.6)
    ax.set_ylim(3.6, -0.6)
    ax.set_xticks(range(4), vs)
    ax.set_yticks(range(4), vs)
    ax.xaxis.tick_top()
    ax.tick_params(length=0, labelsize=9)
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_title(f"$P^{{({s})}}$" + ("" if s == 0 else f", pivot $v_{s}$"), pad=20, fontsize=10)
fig.tight_layout()
