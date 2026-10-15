import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 0.25 * x**3 - x + 2


def df(x):
    return 0.75 * x**2 - 1


x0 = 1.6
y0 = f(x0)
xs = np.linspace(-0.3, 3.6, 400)

fig, ax = plt.subplots(figsize=(7.5, 5))
ax.plot(xs, f(xs), color="C0", lw=2, label=r"$y = f(x)$")

steps = [1.3, 0.85, 0.5, 0.2]
cmap = plt.get_cmap("Oranges")
for i, h in enumerate(steps):
    x1 = x0 + h
    slope = (f(x1) - y0) / h
    color = cmap(0.35 + 0.15 * i)
    ax.plot(xs, y0 + slope * (xs - x0), color=color, lw=1.2, ls="--",
            label=rf"secant, $\Delta x = {h}$, slope ${slope:.2f}$")
    ax.plot([x1], [f(x1)], "o", color=color, ms=5)

ax.plot(xs, y0 + df(x0) * (xs - x0), color="C3", lw=2,
        label=rf"tangent, slope $f'(x_0) = {df(x0):.2f}$")
ax.plot([x0], [y0], "o", color="C3", ms=7)
ax.annotate(r"$M(x_0, f(x_0))$", xy=(x0, y0), xytext=(x0 - 1.25, y0 + 0.9),
            arrowprops=dict(arrowstyle="->", lw=0.8))
ax.annotate(r"$Q$ moves toward $M$", xy=(x0 + 0.35, f(x0 + 0.35)),
            xytext=(x0 + 0.55, f(x0 + 0.35) - 1.1),
            arrowprops=dict(arrowstyle="->", lw=0.8))

ax.set_xlim(-0.3, 3.6)
ax.set_ylim(-0.5, 6.5)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.set_title(r"Secants $MQ$ approach the tangent as $\Delta x \to 0$")
ax.grid(True, alpha=0.3)
ax.legend(loc="upper left", fontsize=8.5)
fig.tight_layout()
