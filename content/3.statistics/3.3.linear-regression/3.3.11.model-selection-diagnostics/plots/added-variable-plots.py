"""Added-variable plots: the curvature of a quadratic effect shows up after adjusting for the other variable."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n = 40
income = rng.uniform(25, 80, n)
risk = np.clip(5 + 0.03 * (income - 50) + rng.normal(0, 2, n), 1, 10)
insur = -100 + 0.08 * income ** 2 + 5 * risk + rng.normal(0, 8, n)


def resid(y, cols):
    X = np.column_stack([np.ones(n)] + cols)
    return y - X @ np.linalg.lstsq(X, y, rcond=None)[0]


fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
for ax, (name, xk, other) in zip(axes, [("income", income, risk), ("risk", risk, income)]):
    ry = resid(insur, [other])
    rx = resid(xk, [other])
    slope = (rx @ ry) / (rx @ rx)
    grid = np.linspace(rx.min(), rx.max(), 2)
    ax.plot(rx, ry, "o", color="C0", alpha=0.8)
    ax.plot(grid, slope * grid, color="C3", lw=2, label=f"slope = b_k = {slope:.2f}")
    if name == "income":
        order = np.argsort(rx)
        smooth = np.polyval(np.polyfit(rx, ry, 2), rx[order])
        ax.plot(rx[order], smooth, color="C2", lw=1.5, ls="--", label="quadratic fit to the plot")
    ax.set_xlabel(f"{name} | others")
    ax.set_ylabel("insurance | others")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)
fig.suptitle("Added-variable plots for a model that is linear in income and risk", fontsize=11)
fig.tight_layout()
