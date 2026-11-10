"""Cox-Stuart pairing for the annual mileages of cars and trucks, 1970-83."""

import numpy as np
import matplotlib.pyplot as plt

years = np.arange(1970, 1984)
series = {
    "Cars": np.array([9.8, 9.9, 10.0, 9.8, 9.2, 9.4, 9.5, 9.6, 9.8, 9.3, 8.9, 8.7, 9.2, 9.3]),
    "Trucks": np.array([11.5, 11.5, 12.2, 11.5, 10.9, 10.6, 11.1, 11.1, 11.0, 10.8, 11.4, 12.3, 11.2, 11.2]),
}
m = len(years) // 2

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for ax, (name, x) in zip(axes, series.items()):
    ax.plot(years, x, "o-", color="gray", lw=1, zorder=1)
    plus = minus = 0
    for i in range(m):
        d = x[i + m] - x[i]
        color = "C0" if d > 0 else "C3"
        plus += d > 0
        minus += d < 0
        ax.annotate("", xy=(years[i + m], x[i + m]), xytext=(years[i], x[i]),
                    arrowprops=dict(arrowstyle="->", color=color, lw=1.2, alpha=0.8,
                                    connectionstyle="arc3,rad=-0.25"))
    ax.axvline(years[m] - 0.5, color="gray", ls=":", lw=1)
    ax.set_title(f"{name}: {plus} plus, {minus} minus signs")
    ax.set_xlabel("year")
    ax.set_ylabel("mean annual mileage (thousand miles)")
    ax.grid(alpha=0.3)
fig.suptitle("Cox-Stuart test: pair x_i with x_(i+7); blue = increase, red = decrease")
fig.tight_layout()
