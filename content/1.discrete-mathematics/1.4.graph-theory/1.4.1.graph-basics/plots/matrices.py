import matplotlib.pyplot as plt
import numpy as np

# The example digraph D of Section 1.4: e1=(1,2), e2=(1,3), e3=(2,3), e4=(3,4), e5=(4,2)
edges = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 1)]
n, m = 4, len(edges)
A = np.zeros((n, n), int)
B = np.zeros((n, m), int)
for j, (u, v) in enumerate(edges):
    A[u, v] = 1
    B[u, j], B[v, j] = 1, -1
L = B @ B.T

BLUE, RED, GREY = "#2563eb", "#dc2626", "#94a3b8"


def show(ax, M, title, rows, cols):
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            x = M[i, j]
            colour = BLUE if x > 0 else RED if x < 0 else GREY
            ax.text(j, i, str(x).replace("-", "\u2212"), ha="center", va="center", fontsize=11, color=colour,
                    fontweight="bold" if x else "normal")
    ax.set_xlim(-0.6, M.shape[1] - 0.4)
    ax.set_ylim(M.shape[0] - 0.4, -0.6)
    ax.set_xticks(range(M.shape[1]), cols)
    ax.set_yticks(range(M.shape[0]), rows)
    ax.tick_params(length=0)
    ax.xaxis.tick_top()
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_title(title, pad=24, fontsize=11)


fig, axes = plt.subplots(1, 3, figsize=(9.6, 2.6), gridspec_kw={"width_ratios": [4, 5, 4]})
vs = [f"$v_{i}$" for i in range(1, n + 1)]
show(axes[0], A, "adjacency matrix $A$", vs, vs)
show(axes[1], B, "incidence matrix $B$", vs, [f"$e_{j}$" for j in range(1, m + 1)])
show(axes[2], L, "$BB^{\\mathsf{T}} = D - (A + A^{\\mathsf{T}})$", vs, vs)
fig.tight_layout()
