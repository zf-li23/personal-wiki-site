import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq


def f(x):
    return 0.08 * x**3 - 0.6 * x**2 + 1.2 * x + 1.5


def df(x):
    return 0.24 * x**2 - 1.2 * x + 1.2


a, b = 0.3, 5.6
k = (f(b) - f(a)) / (b - a)
xs = np.linspace(-0.2, 6.1, 400)

# points where f'(xi) equals the slope of the chord
grid = np.linspace(a, b, 2000)
g = df(grid) - k
xis = [brentq(lambda t: df(t) - k, grid[i], grid[i + 1])
       for i in range(len(grid) - 1) if g[i] * g[i + 1] < 0]

fig, ax = plt.subplots(figsize=(7.5, 4.8))
ax.plot(xs, f(xs), color="C0", lw=2, label=r"$y = f(x)$")
ax.plot([a, b], [f(a), f(b)], color="gray", lw=1.5,
        label=r"chord, slope $\frac{f(b) - f(a)}{b - a}$")
ax.plot([a, b], [f(a), f(b)], "o", color="gray", ms=5)
for i, xi in enumerate(xis):
    ax.plot(xs, f(xi) + k * (xs - xi), color="C3", lw=1.2, ls="--",
            label=r"tangent with $f'(\xi) = \frac{f(b) - f(a)}{b - a}$" if i == 0 else None)
    ax.plot([xi], [f(xi)], "o", color="C3", ms=6)
    ax.plot([xi, xi], [0, f(xi)], color="C3", lw=0.7, ls=":")
    ax.text(xi, 0.08, rf"$\xi_{i + 1}$", ha="center", color="C3", fontsize=12)
for x, name in [(a, "a"), (b, "b")]:
    ax.plot([x, x], [0, f(x)], color="gray", lw=0.7, ls=":")
    ax.text(x, 0.08, rf"${name}$", ha="center", fontsize=12)
ax.set_xlim(-0.2, 6.1)
ax.set_ylim(0, 4.2)
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("Mean value theorem: some tangent is parallel to the chord")
ax.legend(loc="upper left", fontsize=9)
fig.tight_layout()
