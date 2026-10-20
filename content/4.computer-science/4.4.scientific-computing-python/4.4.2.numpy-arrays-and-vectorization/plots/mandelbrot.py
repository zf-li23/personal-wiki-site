"""Escape-time picture of the Mandelbrot set, computed without a loop over
pixels: broadcasting builds the grid of c values and a boolean mask selects
the points that are still iterating."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import PowerNorm

re = np.linspace(-2.2, 0.8, 900)
im = np.linspace(-1.2, 1.2, 720)
c = re[np.newaxis, :] + 1j * im[:, np.newaxis]   # (720, 1) + (1, 900) -> (720, 900)

z = np.zeros_like(c)
escape = np.full(c.shape, 60)          # iteration at which |z| first exceeds 2
active = np.ones(c.shape, dtype=bool)  # points that have not escaped yet
for k in range(60):
    z[active] = z[active] ** 2 + c[active]
    escaped = active & (np.abs(z) > 2)
    escape[escaped] = k
    active &= ~escaped

fig, ax = plt.subplots(figsize=(7.5, 6))
img = ax.imshow(escape, extent=(re[0], re[-1], im[0], im[-1]), origin="lower",
                cmap="magma", norm=PowerNorm(0.5), interpolation="nearest")
ax.set_xlabel("Re c")
ax.set_ylabel("Im c")
ax.set_title("Mandelbrot set: iterations until |z| > 2 (60 = did not escape)")
fig.colorbar(img, ax=ax, shrink=0.8, label="escape iteration")
fig.tight_layout()
