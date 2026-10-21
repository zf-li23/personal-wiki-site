import matplotlib.pyplot as plt

# Binary-to-Gray converter on a PLA: G3 = B3, G_i = B_{i+1} xor B_i
# Each product term lists (input index, polarity) pairs; polarity 1 = true, 0 = complement.
terms = [
    [(3, 1)],
    [(3, 1), (2, 0)],
    [(3, 0), (2, 1)],
    [(2, 1), (1, 0)],
    [(2, 0), (1, 1)],
    [(1, 1), (0, 0)],
    [(1, 0), (0, 1)],
]
outputs = {3: [0], 2: [1, 2], 1: [3, 4], 0: [5, 6]}  # G_i -> product terms

fig, ax = plt.subplots(figsize=(8.6, 5.0))
n_terms = len(terms)
row_y = [n_terms - 1 - k for k in range(n_terms)]
top = n_terms - 0.3

# AND plane: one vertical line per input literal
lit_x = {}
x = 0.0
for i in [3, 2, 1, 0]:
    for pol in (1, 0):
        lit_x[(i, pol)] = x
        ax.plot([x, x], [-0.6, top], color="C0", lw=1.0)
        label = f"$B_{i}$" if pol else rf"$\bar B_{i}$"
        ax.text(x, top + 0.15, label, ha="center", va="bottom", fontsize=10)
        x += 0.8
and_right = x - 0.4

# OR plane: one vertical line per output
or_x = {}
x = and_right + 1.6
for i in [3, 2, 1, 0]:
    or_x[i] = x
    ax.plot([x, x], [-0.6, top], color="C1", lw=1.0)
    ax.text(x, -0.75, f"$G_{i}$", ha="center", va="top", fontsize=10)
    x += 0.8
or_right = x - 0.4

for k, y in enumerate(row_y):
    ax.plot([-0.4, or_right], [y, y], color="0.45", lw=0.9)
    ax.text(and_right + 0.8, y + 0.12, f"$P_{k}$", ha="center", va="bottom", fontsize=9)
    for i, pol in terms[k]:
        ax.plot(lit_x[(i, pol)], y, "o", color="C0", ms=6)
for i, ks in outputs.items():
    for k in ks:
        ax.plot(or_x[i], row_y[k], "o", color="C1", ms=6)

ax.text((-0.4 + and_right) / 2, -1.45, "AND plane (programmable)", ha="center", fontsize=10, color="C0")
ax.text((or_x[3] + or_x[0]) / 2, -1.45, "OR plane (programmable)", ha="center", fontsize=10, color="C1")
ax.set_xlim(-0.8, or_right + 0.9)
ax.set_ylim(-1.8, top + 0.8)
ax.axis("off")
ax.set_title("PLA for binary-to-Gray conversion: 7 product terms (dots mark programmed connections)", fontsize=10)
fig.tight_layout()
