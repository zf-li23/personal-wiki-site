"""Euler polygons for y' = x + y, y(0) = 0 on [0, 1] compared with y = e^x - x - 1."""

import numpy as np
import matplotlib.pyplot as plt

f = lambda x, y: x + y
fig, ax = plt.subplots(figsize=(7, 4.8))
xs = np.linspace(0, 1, 300)
ax.plot(xs, np.exp(xs) - xs - 1, color="k", lw=2.6, alpha=0.75, label="exact solution")
for i, n in enumerate([2, 4, 8, 16]):
    h = 1.0 / n
    px, py = [0.0], [0.0]
    for k in range(n):
        py.append(py[-1] + f(px[-1], py[-1]) * h)
        px.append(px[-1] + h)
    ax.plot(px, py, "-o", ms=3, lw=1.5, color=f"C{i}", label=f"Euler polygon, n = {n}")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Euler polygons for y' = x + y, y(0) = 0")
ax.legend(loc="upper left", fontsize=9)
fig.tight_layout()
