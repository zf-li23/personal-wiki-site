import numpy as np
import matplotlib.pyplot as plt


def lagrange_eval(nodes, values, x):
    """Evaluate the Lagrange interpolation polynomial at the points x."""
    total = np.zeros_like(x)
    for i, (ai, bi) in enumerate(zip(nodes, values)):
        Li = np.ones_like(x)
        for j, aj in enumerate(nodes):
            if j != i:
                Li *= (x - aj) / (ai - aj)
        total += bi * Li
    return total


def f(x):
    return 1 / (1 + 25 * x**2)


x = np.linspace(-1, 1, 1001)
fig, axes = plt.subplots(1, 2, figsize=(12, 4.8), sharey=True)
for ax, kind in zip(axes, ["equispaced", "Chebyshev"]):
    ax.plot(x, f(x), color="tab:gray", lw=4, alpha=0.8, label="f(x) = 1/(1 + 25x^2)")
    for n, c in [(6, "tab:blue"), (10, "tab:orange"), (14, "tab:red")]:
        if kind == "equispaced":
            nodes = np.linspace(-1, 1, n + 1)
        else:
            nodes = np.cos((2 * np.arange(n + 1) + 1) * np.pi / (2 * n + 2))
        ax.plot(x, lagrange_eval(nodes, f(nodes), x), color=c, lw=1.6,
                label=f"degree {n}")
        if n == 14:
            ax.plot(nodes, f(nodes), "o", color=c, ms=5)
    ax.set_ylim(-1.5, 2.0)
    ax.grid(True, alpha=0.3)
    ax.set_xlabel("x")
    ax.set_title(f"{kind} nodes (dots: the 15 nodes for degree 14)", fontsize=11)
    ax.legend(loc="upper center", fontsize=9)
fig.suptitle("Lagrange interpolation of the Runge function", fontsize=12)
fig.tight_layout()
