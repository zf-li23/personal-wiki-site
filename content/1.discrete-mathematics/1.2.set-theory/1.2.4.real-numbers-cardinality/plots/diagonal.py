"""Cantor's diagonal argument (proof of Theorem 4.2.3): list any countable sequence f(0), f(1), ... of
decimal expansions in [0, 1); change the n-th digit of f(n) (to 4 if it is 5, to 5 otherwise). The
resulting number b differs from every f(n) in its n-th digit, so it is missing from the list."""

import matplotlib.pyplot as plt

rows = ["3141592", "2500000", "7182818", "1414213", "6180339", "7500000", "9999999"]
b = "".join("4" if r[i] == "5" else "5" for i, r in enumerate(rows))

fig, ax = plt.subplots(figsize=(8, 5.6))
for i, r in enumerate(rows):
    y = len(rows) - i
    ax.text(-0.4, y, f"$f({i}) = 0.$", ha="right", va="center", fontsize=13)
    for j, d in enumerate(r):
        if i == j:
            ax.add_patch(plt.Rectangle((j - 0.38, y - 0.38), 0.76, 0.76, fc="C1", alpha=0.25, ec="C1", lw=1.5))
        ax.text(j, y, d, ha="center", va="center", fontsize=13, color="C1" if i == j else None)
    ax.text(len(r) + 0.2, y, r"$\cdots$", ha="left", va="center", fontsize=13)
ax.text(len(rows) // 2, 0.35, r"$\vdots$", ha="center", va="center", fontsize=13)
ax.plot([-2.6, len(rows) + 0.8], [-0.3, -0.3], color="0.6", lw=1.0)
ax.text(-0.4, -1.0, r"$b = 0.$", ha="right", va="center", fontsize=13, color="C3")
for j, d in enumerate(b):
    ax.text(j, -1.0, d, ha="center", va="center", fontsize=13, color="C3")
ax.text(len(b) + 0.2, -1.0, r"$\cdots$", ha="left", va="center", fontsize=13, color="C3")
ax.text(len(b) / 2 - 0.5, -1.9, r"the $n$-th digit of $b$ differs from the $n$-th digit of $f(n)$",
        ha="center", va="center", fontsize=11)
ax.set_xlim(-2.8, len(rows) + 1)
ax.set_ylim(-2.3, len(rows) + 0.7)
ax.axis("off")
