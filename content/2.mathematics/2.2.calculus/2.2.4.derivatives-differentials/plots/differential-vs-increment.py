import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 0.15 * x**2 + 0.5


def df(x):
    return 0.3 * x


x0, dx = 1.5, 2.2
x1 = x0 + dx
y0, y1 = f(x0), f(x1)
dy = df(x0) * dx

xs = np.linspace(0, 4.6, 300)
fig, ax = plt.subplots(figsize=(7.5, 5))
ax.plot(xs, f(xs), color="C0", lw=2, label=r"$y = f(x)$")
ax.plot(xs, y0 + df(x0) * (xs - x0), color="C3", lw=1.5,
        label=r"tangent $y = f(x_0) + f'(x_0)(x - x_0)$")

ax.plot([x0, x1], [y0, y0], color="gray", lw=1, ls=":")
ax.plot([x1, x1], [0, y1], color="gray", lw=0.8, ls=":")
ax.plot([x0, x0], [0, y0], color="gray", lw=0.8, ls=":")
ax.plot([x0, x1], [y0, y1], "o", color="C0", ms=5)

# increment of the function and the differential, drawn as vertical brackets
ax.annotate("", xy=(x1 + 0.12, y1), xytext=(x1 + 0.12, y0),
            arrowprops=dict(arrowstyle="<->", color="C0", lw=1.5))
ax.text(x1 + 0.2, (y0 + y1) / 2, r"$\Delta y$", color="C0", fontsize=13, va="center")
ax.annotate("", xy=(x1 - 0.12, y0 + dy), xytext=(x1 - 0.12, y0),
            arrowprops=dict(arrowstyle="<->", color="C3", lw=1.5))
ax.text(x1 - 0.95, y0 + dy / 2, r"$\mathrm{d}y = f'(x_0)\,\Delta x$", color="C3",
        fontsize=11, va="center")
ax.text(x1 - 0.55, y0 + dy + (y1 - y0 - dy) / 2, r"$o(\Delta x)$", fontsize=11, va="center")
ax.annotate("", xy=(x1, y0 - 0.12), xytext=(x0, y0 - 0.12),
            arrowprops=dict(arrowstyle="<->", color="gray", lw=1))
ax.text((x0 + x1) / 2, y0 - 0.32, r"$\Delta x = \mathrm{d}x$", ha="center", fontsize=11)

ax.set_xticks([x0, x1])
ax.set_xticklabels([r"$x_0$", r"$x_0 + \Delta x$"])
ax.set_yticks([])
ax.set_xlim(0, 4.8)
ax.set_ylim(0, 3.9)
ax.set_title(r"$\Delta y = \mathrm{d}y + o(\Delta x)$: the differential is the increment along the tangent")
ax.legend(loc="upper left", fontsize=9)
fig.tight_layout()
