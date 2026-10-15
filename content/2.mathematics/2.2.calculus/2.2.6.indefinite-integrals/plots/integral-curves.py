import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**2 - 1


def F(x):
    return x**3 / 3 - x


fig, ax = plt.subplots(figsize=(7.5, 5.5))

# slope field: short segments with slope f(x), independent of y
gx, gy = np.meshgrid(np.linspace(-2.4, 2.4, 21), np.linspace(-3, 3, 19))
slope = f(gx)
length = 0.18
dx = length / np.sqrt(1 + slope**2)
ax.plot(np.array([gx - dx, gx + dx]).reshape(2, -1),
        np.array([gy - slope * dx, gy + slope * dx]).reshape(2, -1),
        color="gray", lw=0.9, alpha=0.7)

xs = np.linspace(-2.5, 2.5, 400)
cmap = plt.get_cmap("plasma")
consts = np.arange(-2, 2.01, 0.5)
for i, c in enumerate(consts):
    ax.plot(xs, F(xs) + c, color=cmap(0.85 * i / (len(consts) - 1)), lw=1.6,
            label=rf"$C = {c:g}$" if c in (-2, 0, 2) else None)

x0 = 1.5
for c in consts:
    y0 = F(x0) + c
    seg = np.linspace(x0 - 0.25, x0 + 0.25, 2)
    ax.plot(seg, y0 + f(x0) * (seg - x0), color="C2", lw=2.2)
ax.axvline(x0, color="C2", lw=1, ls=":")
ax.text(x0 - 0.05, -2.85, r"at $x = x_0$: the same slope $f(x_0)$ on every curve", color="C2", fontsize=9, ha="right")

ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-3, 3)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.set_title(r"Integral curves $y = \frac{x^3}{3} - x + C$ of $f(x) = x^2 - 1$ in its slope field")
ax.legend(loc="upper left", fontsize=9)
fig.tight_layout()
