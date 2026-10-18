"""High leverage, outlier, influential point: fits with and without the marked observation."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
x = np.arange(1.0, 10.0)
y = 5 + 9 * x + 6 * rng.normal(size=x.size)
cases = [
    ("A: high leverage, on the trend", 20.0, 5 + 9 * 20.0),
    ("B: outlier, low leverage", 5.0, 10.0),
    ("C: high leverage and outlier", 20.0, 50.0),
]
grid = np.array([0.0, 22.0])
fig, axes = plt.subplots(1, 3, figsize=(11, 4.0), sharey=True)
for ax, (title, xo, yo) in zip(axes, cases):
    xa, ya = np.append(x, xo), np.append(y, yo)
    n, p = xa.size, 2
    X = np.column_stack([np.ones(n), xa])
    H = X @ np.linalg.solve(X.T @ X, X.T)
    h = np.diag(H)[-1]
    b = np.linalg.lstsq(X, ya, rcond=None)[0]
    e = ya - X @ b
    mse = e @ e / (n - p)
    cook = e[-1] ** 2 / (p * mse) * h / (1 - h) ** 2
    t = e[-1] * np.sqrt((n - p - 1) / (e @ e * (1 - h) - e[-1] ** 2))
    b1, b0 = np.polyfit(x, y, 1)
    ax.plot(x, y, "o", color="C0", ms=5)
    ax.plot([xo], [yo], "^", color="C3", ms=9)
    ax.plot(grid, b[0] + b[1] * grid, color="C3", lw=1.5, label="all data")
    ax.plot(grid, b0 + b1 * grid, color="C0", lw=1.5, ls="--", label="without triangle")
    ax.set_title(f"{title}\nh = {h:.2f}, t = {t:.1f}, D = {cook:.2f}", fontsize=10)
    ax.set_xlabel("X")
    ax.grid(alpha=0.3)
axes[0].set_ylabel("Y")
axes[0].legend(fontsize=9, loc="upper left")
fig.tight_layout()
