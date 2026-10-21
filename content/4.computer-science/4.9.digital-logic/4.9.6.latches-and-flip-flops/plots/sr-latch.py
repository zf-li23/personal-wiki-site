import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle

LW = 1.8


def gate(ax, x, y, nor=False, w=1.2, h=1.0):
    """Draw a two-input NAND (or NOR) gate whose body starts at (x, y - h/2).

    Returns the coordinates of the upper input, the lower input and the output."""
    if nor:
        # NOR: curved back, pointed front
        t = np.linspace(-1, 1, 50)
        ax.plot(x + 0.18 * (1 - t**2), y + t * h / 2, lw=LW, color="C0")
        tt = np.linspace(0, 1, 50)
        ax.plot(x + w * tt, y + h / 2 - 0.5 * h * tt**2, lw=LW, color="C0")
        ax.plot(x + w * tt, y - h / 2 + 0.5 * h * tt**2, lw=LW, color="C0")
        tip = x + w
        back = x + 0.14
    else:
        # NAND: straight back, semicircular front
        ax.plot([x + w / 2, x, x, x + w / 2], [y + h / 2, y + h / 2, y - h / 2, y - h / 2], lw=LW, color="C0")
        ax.add_patch(Arc((x + w / 2, y), h, h, theta1=-90, theta2=90, lw=LW, color="C0"))
        tip = x + w / 2 + h / 2
        back = x
    r = 0.09
    ax.add_patch(Circle((tip + r, y), r, fill=False, lw=LW, color="C0"))
    return (back, y + 0.25 * h), (back, y - 0.25 * h), (tip + 2 * r, y)


def wire(ax, pts, color="C1"):
    xs, ys = zip(*pts)
    ax.plot(xs, ys, lw=1.4, color=color)


fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.6))
for ax, nor in zip(axes, [False, True]):
    a1, b1, o1 = gate(ax, 2.0, 2.0, nor)
    a2, b2, o2 = gate(ax, 2.0, 0.0, nor)
    end = o1[0] + 1.3
    # outputs
    wire(ax, [o1, (end, o1[1])])
    wire(ax, [o2, (end, o2[1])])
    # external inputs
    wire(ax, [(0.4, a1[1]), a1])
    wire(ax, [(0.4, b2[1]), b2])
    # cross-coupled feedback
    k = o1[0] + 0.45
    wire(ax, [(k, o1[1]), (k, 1.35), (1.5, 0.65), (1.5, a2[1]), a2])
    wire(ax, [(k, o2[1]), (k, 0.65), (1.5, 1.35), (1.5, b1[1]), b1])
    for p in [(k, o1[1]), (k, o2[1])]:
        ax.add_patch(Circle(p, 0.05, color="C1"))
    if nor:
        top_in, bot_in, top_out, bot_out = "$R$", "$S$", "$Q$", r"$\overline{Q}$"
        title = "NOR form: active-high inputs"
    else:
        top_in, bot_in, top_out, bot_out = r"$\overline{S}$", r"$\overline{R}$", "$Q$", r"$\overline{Q}$"
        title = "NAND form: active-low inputs"
    ax.text(0.3, a1[1], top_in, ha="right", va="center", fontsize=13)
    ax.text(0.3, b2[1], bot_in, ha="right", va="center", fontsize=13)
    ax.text(end + 0.1, o1[1], top_out, ha="left", va="center", fontsize=13)
    ax.text(end + 0.1, o2[1], bot_out, ha="left", va="center", fontsize=13)
    ax.set_title(title, fontsize=11)
    ax.set_xlim(-0.4, end + 0.7)
    ax.set_ylim(-0.8, 2.8)
    ax.set_aspect("equal")
    ax.axis("off")
fig.tight_layout()
