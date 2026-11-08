# Daily fluid balance of the human gastrointestinal tract (typical adult values, L/day), drawn as an
# alluvial (Sankey) diagram. Inputs to the small intestine: diet 2.0, saliva 1.0, gastric juice 1.5,
# pancreatic juice 1.0, bile 1.0, intestinal secretions incl. Brunner's glands 2.0 (total 8.5). The jejunum absorbs about 5.5
# and the ileum 1.5, so about 1.5 L/day passes the ileocecal valve; the colon absorbs 1.4 and about
# 0.1 L/day leaves in the feces. Only about 1 % of the fluid that enters the gut is lost.
import matplotlib.pyplot as plt
import numpy as np

inputs = [("diet", 2.0), ("saliva", 1.0), ("gastric juice", 1.5), ("pancreatic juice", 1.0),
          ("bile", 1.0), ("intestinal secretion", 2.0)]
mid = [("absorbed in jejunum", 5.5, "#2a9d8f"), ("absorbed in ileum", 1.5, "#2a9d8f"),
       ("to colon", 1.5, "#d9822b")]
right = [("absorbed in colon", 1.4, "#2a9d8f"), ("feces", 0.1, "#c0392b")]
GAP, W = 0.12, 0.25
fig, ax = plt.subplots(figsize=(11, 5.4))


def band(x0, y0a, y0b, x1, y1a, y1b, color, alpha=0.45):
    s = np.linspace(0, 1, 60)
    w = 3 * s ** 2 - 2 * s ** 3
    x = x0 + (x1 - x0) * s
    ax.fill_between(x, y0a + (y1a - y0a) * w, y0b + (y1b - y0b) * w, color=color, alpha=alpha, lw=0)


# column 1: inputs stacked, merging into one block at x = 1
y = 0.0
total = sum(v for _, v in inputs)
blocks = []
for name, v in inputs:
    blocks.append((y, y + v))
    ax.add_patch(plt.Rectangle((0, y), W, v, color="#2f6fb5"))
    ax.text(-0.08, y + v / 2, f"{name}  {v:.1f}", ha="right", va="center", fontsize=9)
    y += v + GAP
ystart = (y - GAP - total) / 2
yy = ystart
for (a, b), (_, v) in zip(blocks, inputs):
    band(W, a, b, 2.0, yy, yy + v, "#2f6fb5")
    yy += v
ax.add_patch(plt.Rectangle((2.0, ystart), W, total, color="#2f6fb5"))
ax.text(2.0 + W / 2, ystart + total + 0.15, "small intestine\n8.5 L/day", ha="center", va="bottom",
        fontsize=9.5, fontweight="bold")
# column 2 -> outputs of the small intestine, placed top-down
y2 = ystart + total + 0.6
outs = []
for name, v, c in mid:
    y2 -= v + 0.35
    outs.append((name, v, c, y2))
top = ystart + total
cur = top
for name, v, c, y2 in outs:
    band(2.0 + W, cur - v, cur, 4.0, y2, y2 + v, c)
    ax.add_patch(plt.Rectangle((4.0, y2), W, v, color=c))
    cur -= v
    if name != "to colon":
        ax.text(4.0 + W + 0.08, y2 + v / 2, f"{name}  {v:.1f}", va="center", fontsize=9)
yc = outs[-1][3]
ax.text(4.0 + W / 2, yc - 0.15, "colon\n1.5 L/day", ha="center", va="top", fontsize=9.5,
        fontweight="bold")
# column 3: colon outputs
cur = yc + 1.5
y3 = yc + 1.0
for name, v, c in right:
    band(4.0 + W, cur - v, cur, 6.0, y3, y3 + v, c)
    ax.add_patch(plt.Rectangle((6.0, y3), W, v, color=c))
    ax.text(6.0 + W + 0.08, y3 + v / 2, f"{name}  {v:.1f}", va="center", fontsize=9)
    cur -= v
    y3 -= 0.6
ax.set_xlim(-2.2, 8.2)
ax.set_ylim(-1.2, y + 0.4)
ax.axis("off")
ax.set_title("Fluid entering and leaving the gut (L/day)", fontsize=11, fontweight="bold", loc="left")
