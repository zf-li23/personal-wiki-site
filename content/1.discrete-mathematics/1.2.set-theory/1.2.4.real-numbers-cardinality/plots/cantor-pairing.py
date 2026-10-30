"""N x N is countable (Theorem 4.7.1): enumerate the pairs (m, n) along the diagonals m + n = d. The d-th
diagonal has d + 1 points and is preceded by d(d + 1)/2 points, so (m, n) receives the number
pi(m, n) = (m + n)(m + n + 1)/2 + n, a bijection from N x N onto N."""

import matplotlib.pyplot as plt

K = 5
order = [(d - n, n) for d in range(K + 1) for n in range(d + 1)]
fig, ax = plt.subplots(figsize=(6.6, 6.2))
for k in range(len(order) - 1):
    (m, n), (m2, n2) = order[k], order[k + 1]
    if m + n == m2 + n2:   # along a diagonal
        ax.annotate("", (m2, n2), (m, n), arrowprops=dict(arrowstyle="-|>", color="C0", lw=1.4, shrinkA=10, shrinkB=10))
    else:                  # jump to the start of the next diagonal
        ax.annotate("", (m2, n2), (m, n), arrowprops=dict(arrowstyle="-|>", color="0.6", lw=0.8, ls="--",
                                                          shrinkA=10, shrinkB=10))
for k, (m, n) in enumerate(order):
    ax.text(m, n, str(k), ha="center", va="center", fontsize=11, zorder=3,
            bbox=dict(boxstyle="circle,pad=0.25", fc="C1", alpha=0.22, ec="C1"))
ax.set_xticks(range(K + 1))
ax.set_yticks(range(K + 1))
ax.set_xlabel("$m$")
ax.set_ylabel("$n$")
ax.set_xlim(-0.6, K + 0.6)
ax.set_ylim(-0.6, K + 0.6)
ax.set_aspect("equal")
ax.set_title(r"$\pi(m, n) = \frac{(m+n)(m+n+1)}{2} + n$", fontsize=12)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
