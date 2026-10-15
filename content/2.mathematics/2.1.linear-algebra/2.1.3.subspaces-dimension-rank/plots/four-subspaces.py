"""The four fundamental subspaces of the rank-one matrix A = [[1, 2], [3, 6]] and the action
of A on a vector x = x_r + x_n (row-space part plus null-space part)."""

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1.0, 2.0], [3.0, 6.0]])
row = np.array([1.0, 2.0])     # spans the row space R(A^T)
null = np.array([2.0, -1.0])   # spans the null space N(A)
col = np.array([1.0, 3.0])     # spans the column space R(A)
left = np.array([3.0, -1.0])   # spans the left null space N(A^T)

x = np.array([1.0, 0.5])
x_r = (x @ row) / (row @ row) * row
x_n = x - x_r
b = A @ x


def line(ax, d, lim, color, label):
    d = d / np.linalg.norm(d)
    ax.plot([-lim * d[0], lim * d[0]], [-lim * d[1], lim * d[1]], color=color, lw=2.2, label=label)


def arrow(ax, start, end, color, lw=1.8):
    ax.annotate("", xy=end, xytext=start,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                shrinkA=0, shrinkB=0, mutation_scale=13))


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 5))

# Domain R^n (here n = 2): row space and null space
line(ax1, row, 4, "C0", "row space $\\mathcal{R}(A^{\\mathsf{T}})$, dim $r = 1$")
line(ax1, null, 4, "C2", "null space $\\mathcal{N}(A)$, dim $n - r = 1$")
s = np.linspace(-2.5, 2.5, 2)
ax1.plot(x[0] + s * null[0], x[1] + s * null[1], color="C3", lw=1.0, ls="--",
         label="solutions of $Ax = b$: $x + \\mathcal{N}(A)$")
ax1.plot([x_r[0], x[0]], [x_r[1], x[1]], color="0.6", lw=0.8, ls=":")
ax1.plot([x_n[0], x[0]], [x_n[1], x[1]], color="0.6", lw=0.8, ls=":")
arrow(ax1, (0, 0), x_r, "C0")
arrow(ax1, (0, 0), x_n, "C2")
arrow(ax1, (0, 0), x, "C3", lw=2.2)
ax1.text(x_r[0] - 0.45, x_r[1] - 0.05, "$x_r$", color="C0", fontsize=12)
ax1.text(x_n[0] + 0.05, x_n[1] - 0.35, "$x_n$", color="C2", fontsize=12)
ax1.text(x[0] + 0.1, x[1] + 0.05, "$x$", color="C3", fontsize=12)
ax1.set_xlim(-2.2, 2.6)
ax1.set_ylim(-2.2, 2.6)
ax1.set_title("Domain $\\mathbb{R}^n$")

# Codomain R^m (here m = 2): column space and left null space
line(ax2, col, 9, "C1", "column space $\\mathcal{R}(A)$, dim $r = 1$")
line(ax2, left, 9, "C4", "left null space $\\mathcal{N}(A^{\\mathsf{T}})$, dim $m - r = 1$")
arrow(ax2, (0, 0), b, "C3", lw=2.2)
ax2.plot(0, 0, "o", color="C2", ms=6, zorder=5)
ax2.text(b[0] + 0.2, b[1] - 0.2, "$b = Ax = Ax_r$", color="C3", fontsize=12)
ax2.text(0.3, -1.0, "$Ax_n = 0$", color="C2", fontsize=12)
ax2.set_xlim(-6, 7)
ax2.set_ylim(-6, 7)
ax2.set_title("Codomain $\\mathbb{R}^m$")

for ax in (ax1, ax2):
    ax.axhline(0, color="0.6", lw=0.5)
    ax.axvline(0, color="0.6", lw=0.5)
    ax.set_aspect("equal")
    ax.legend(loc="lower left", fontsize=8.5)
fig.suptitle("Rows of $A$: $(1, 2)$ and $(3, 6)$; rank $r = 1$; the map $x \\mapsto Ax$ sends $\\mathbb{R}^n$ onto $\\mathcal{R}(A)$",
             fontsize=11)
fig.tight_layout()
