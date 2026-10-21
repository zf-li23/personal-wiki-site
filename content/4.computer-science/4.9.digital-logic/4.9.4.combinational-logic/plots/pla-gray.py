"""A PLA converting 4-bit binary B3..B0 to Gray code G3..G0. Each horizontal line
is a product term formed in the programmable AND plane (a dot connects an input
literal); each output column ORs the product terms marked in the OR plane."""

import matplotlib.pyplot as plt

FG = plt.rcParams["text.color"]

literals = []
for i in (3, 2, 1, 0):
    literals += [(i, 1), (i, 0)]          # (bit, polarity): B_i and its complement
products = [  # list of (bit, polarity) per product term
    [(3, 1)],
    [(3, 1), (2, 0)], [(3, 0), (2, 1)],
    [(2, 1), (1, 0)], [(2, 0), (1, 1)],
    [(1, 1), (0, 0)], [(1, 0), (0, 1)],
]
outputs = {3: [0], 2: [1, 2], 1: [3, 4], 0: [5, 6]}

fig, ax = plt.subplots(figsize=(9, 5))
n_lit, n_p = len(literals), len(products)
x_or0 = n_lit + 1.0
for j, (bit, pol) in enumerate(literals):
    ax.plot([j, j], [0.6, -n_p - 0.4], color=FG, lw=1)
    name = f"B_{bit}" if pol else rf"\overline{{B_{bit}}}"
    ax.text(j, 0.9, f"${name}$", ha="center", color=FG, fontsize=10)
for k, term in enumerate(products):
    y = -k - 0.5
    ax.plot([-0.6, x_or0 + 3.6], [y, y], color=FG, lw=1)
    ax.text(-0.9, y, f"$P_{k + 1}$", ha="right", va="center", color=FG, fontsize=10)
    for (bit, pol) in term:
        j = literals.index((bit, pol))
        ax.plot(j, y, "o", color="C0", ms=7)
for c, (bit, ks) in enumerate(sorted(outputs.items(), reverse=True)):
    x = x_or0 + c
    ax.plot([x, x], [0.2, -n_p - 0.4], color=FG, lw=1)
    ax.text(x, -n_p - 0.9, f"$G_{bit}$", ha="center", color=FG, fontsize=10)
    for k in ks:
        ax.plot(x, -k - 0.5, "o", color="C1", ms=7)
ax.axvline(n_lit - 0.2 + 0.7, color="gray", lw=0.8, ls=":")
ax.text((n_lit - 1) / 2, -n_p - 1.5, "AND plane (programmable)", ha="center", color=FG, fontsize=9)
ax.text(x_or0 + 1.5, -n_p - 1.5, "OR plane (programmable)", ha="center", color=FG, fontsize=9)
ax.set_xlim(-1.8, x_or0 + 4)
ax.set_ylim(-n_p - 1.9, 1.4)
ax.set_aspect("equal")
ax.axis("off")
fig.tight_layout()
