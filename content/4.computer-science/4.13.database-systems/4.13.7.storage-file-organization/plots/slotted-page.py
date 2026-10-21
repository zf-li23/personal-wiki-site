"""Schematic (not to scale) of a slotted page: header, slot array, free space, records."""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

fig, ax = plt.subplots(figsize=(8.5, 3.0))
y, h = 1.0, 1.0


def box(x0, w, color, label, text_color="white", hatch=None):
    ax.add_patch(Rectangle((x0, y), w, h, facecolor=color, edgecolor="black",
                           linewidth=0.8, hatch=hatch))
    ax.text(x0 + w / 2, y + h / 2, label, ha="center", va="center",
            fontsize=9, color=text_color)


# header
box(0.0, 1.4, "C7", "header")
# slot array: slot 3 is unused (its record was deleted)
slot_x = [1.4 + 0.6 * i for i in range(4)]
for i, x in enumerate(slot_x):
    box(x, 0.6, "C0" if i != 2 else "none", str(i + 1),
        text_color="white" if i != 2 else "0.4")
free_x0 = slot_x[-1] + 0.6
# records, placed from the end of the page leftwards: slot 1 -> rightmost
rec = {1: (10.4, 1.1), 2: (9.3, 1.5), 4: (7.8, 1.5)}
for rid, (x1, w) in rec.items():
    box(x1 - w, w, "C2", f"record {rid}")
free_x1 = min(x1 - w for x1, w in rec.values())
box(free_x0, free_x1 - free_x0, "none", "free space", text_color="0.4")

for i, x in enumerate(slot_x):
    rid = i + 1
    if rid not in rec:
        continue
    x1, w = rec[rid]
    ax.add_patch(FancyArrowPatch((x + 0.3, y + h), (x1 - w / 2, y + h),
                                 connectionstyle="arc3,rad=-0.25", arrowstyle="-|>",
                                 mutation_scale=10, lw=0.9, color="C0"))

ax.annotate("slot array: (offset, length) per slot;\ngrows to the right",
            xy=(2.6, y), xytext=(1.2, 0.05), fontsize=8.5, ha="left",
            arrowprops=dict(arrowstyle="-", lw=0.6))
ax.annotate("records grow to the left\nfrom the end of the page",
            xy=(8.0, y), xytext=(7.0, 0.05), fontsize=8.5, ha="left",
            arrowprops=dict(arrowstyle="-", lw=0.6))
ax.annotate("header: slot count,\nstart and end of free space",
            xy=(0.7, y), xytext=(-0.1, -0.75), fontsize=8.5, ha="left",
            arrowprops=dict(arrowstyle="-", lw=0.6))
ax.text(0.0, 2.15, "byte 0", fontsize=8, ha="left")
ax.text(10.4, 2.15, "end of page", fontsize=8, ha="right")
ax.set_xlim(-0.2, 10.6)
ax.set_ylim(-0.9, 3.4)
ax.axis("off")
fig.tight_layout()
