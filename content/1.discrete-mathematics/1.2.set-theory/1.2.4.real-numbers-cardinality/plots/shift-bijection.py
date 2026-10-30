"""Infinite sets are equinumerous with proper subsets (Corollary 4.3.2). A: n -> n + 1 is a bijection
from N onto N minus {0}; B: n -> 2n is a bijection from N onto the even numbers. Every element of the
lower row is hit exactly once and neither row runs out."""

import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 1, figsize=(9, 4.6))
cases = [("A", r"$n \mapsto n + 1$", lambda n: n + 1, r"$\mathbb{N}\setminus\{0\}$"),
         ("B", r"$n \mapsto 2n$", lambda n: 2 * n, "even numbers")]
N = 7
for ax, (letter, title, f, target) in zip(axes, cases):
    for n in range(N):
        ax.text(n, 1, f"${n}$", ha="center", va="center", fontsize=13,
                bbox=dict(boxstyle="circle,pad=0.3", fc="C0", alpha=0.18, ec="C0"))
        ax.text(n, 0, f"${f(n)}$", ha="center", va="center", fontsize=13,
                bbox=dict(boxstyle="circle,pad=0.3", fc="C1", alpha=0.18, ec="C1"))
        ax.annotate("", (n, 0.24), (n, 0.76), arrowprops=dict(arrowstyle="-|>", color="0.45", lw=1.2))
    for y in (0, 1):
        ax.text(N - 0.2, y, r"$\cdots$", ha="left", va="center", fontsize=14)
    ax.text(-0.9, 1, r"$\mathbb{N}$", ha="right", va="center", fontsize=13)
    ax.text(-0.9, 0, target, ha="right", va="center", fontsize=12)
    ax.text(-3.0, 1.6, f"{letter}   {title}", ha="left", va="center", fontsize=12, weight="bold")
    ax.set_xlim(-3.1, N + 0.6)
    ax.set_ylim(-0.5, 1.9)
    ax.axis("off")
fig.tight_layout()
