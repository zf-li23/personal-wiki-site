import matplotlib.pyplot as plt

# A skip list with fixed tower heights and the search path for key 38.
keys = [5, 12, 19, 23, 31, 38, 44, 57]
heights = [1, 3, 1, 2, 4, 1, 2, 1]
levels = max(heights)
target = 38
xs = {k: i + 1 for i, k in enumerate(keys)}
x_head, x_tail = 0, len(keys) + 1

fig, ax = plt.subplots(figsize=(10, 3.6))


def box(x, y, text, highlight=False):
    ax.add_patch(plt.Rectangle((x - 0.32, y - 0.22), 0.64, 0.44, fill=False,
                               lw=2.2 if highlight else 1.2, ec="C1" if highlight else "0.35"))
    ax.text(x, y, text, ha="center", va="center", fontsize=10)


for level in range(levels):
    box(x_head, level, "head")
    box(x_tail, level, "tail")
    ax.text(-0.75, level, f"$S_{level}$", ha="right", va="center", fontsize=11)
for k, h in zip(keys, heights):
    for level in range(h):
        box(xs[k], level, str(k), highlight=(k == target and level == 0))

# Horizontal links on each level.
for level in range(levels):
    row = [x_head] + [xs[k] for k, h in zip(keys, heights) if h > level] + [x_tail]
    for a, b in zip(row, row[1:]):
        ax.annotate("", xy=(b - 0.34, level), xytext=(a + 0.34, level),
                    arrowprops=dict(arrowstyle="->", color="0.55", lw=1))

# Search path: go right while the next key is <= target, otherwise go down.
path = [(x_head, levels - 1)]
x, level = x_head, levels - 1
pos = {x_head: float("-inf")} | {xs[k]: k for k in keys}
while True:
    row = [xs[k] for k, h in zip(keys, heights) if h > level and xs[k] > x]
    if row and pos[row[0]] <= target:
        x = row[0]
    elif level > 0:
        level -= 1
    else:
        break
    path.append((x, level))
for (a, la), (b, lb) in zip(path, path[1:]):
    ax.annotate("", xy=(b, lb), xytext=(a, la),
                arrowprops=dict(arrowstyle="->", color="C1", lw=2.2,
                                shrinkA=10, shrinkB=10, connectionstyle="arc3,rad=0.0"))

ax.set_xlim(-1.4, x_tail + 0.6)
ax.set_ylim(-0.6, levels - 0.4)
ax.axis("off")
ax.set_title("search(38): move right while the next key is at most 38, otherwise move down", fontsize=10)
fig.tight_layout()
