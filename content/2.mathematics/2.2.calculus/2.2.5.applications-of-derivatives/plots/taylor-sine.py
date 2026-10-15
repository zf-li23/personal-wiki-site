import numpy as np
import matplotlib.pyplot as plt
from math import factorial

x = np.linspace(-2 * np.pi, 2 * np.pi, 800)
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, np.sin(x), color="black", lw=2.4, label=r"$\sin x$")

cmap = plt.get_cmap("viridis")
orders = [1, 3, 5, 7, 9, 11]
for i, n in enumerate(orders):
    p = np.zeros_like(x)
    for k in range((n + 1) // 2):
        p += (-1) ** k * x ** (2 * k + 1) / factorial(2 * k + 1)
    ax.plot(x, p, color=cmap(0.85 * i / (len(orders) - 1)), lw=1.3, label=rf"$P_{{{n}}}(x)$")

ax.set_xlim(-2 * np.pi, 2 * np.pi)
ax.set_ylim(-2.5, 2.5)
ax.set_xticks(np.arange(-2, 3) * np.pi)
ax.set_xticklabels([r"$-2\pi$", r"$-\pi$", r"$0$", r"$\pi$", r"$2\pi$"])
ax.axhline(0, color="gray", lw=0.6)
ax.set_title(r"Taylor polynomials of $\sin x$ at $0$: higher order, wider agreement")
ax.legend(loc="upper left", fontsize=9, ncol=2)
ax.grid(True, alpha=0.3)
fig.tight_layout()
