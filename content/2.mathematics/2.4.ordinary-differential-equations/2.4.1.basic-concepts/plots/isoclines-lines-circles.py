"""Direction fields of y' = y/x (rays) and y' = -x/y (circles) with isoclines."""

import numpy as np
import matplotlib.pyplot as plt


def field(ax, slope, title):
    g = np.linspace(-2, 2, 17)
    X, Y = np.meshgrid(g, g)
    keep = ~((X == 0) & (Y == 0))
    X, Y = X[keep], Y[keep]
    with np.errstate(divide="ignore", invalid="ignore"):
        S = slope(X, Y)
    finite = np.isfinite(S)
    S0 = np.where(finite, S, 0.0)
    # unit line elements; vertical where the slope is infinite
    U = np.where(finite, 1 / np.sqrt(1 + S0**2), 0.0)
    V = np.where(finite, S0 / np.sqrt(1 + S0**2), 1.0)
    ax.quiver(X, Y, U, V, angles="xy", headwidth=0, headlength=0, headaxislength=0,
              pivot="middle", scale=22, width=0.004, color="0.5")
    ax.set_xlim(-2.1, 2.1)
    ax.set_ylim(-2.1, 2.1)
    ax.set_aspect("equal")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(title)


fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 5))

field(a1, lambda x, y: y / x, "y' = y/x: integral curves are rays")
t = np.linspace(0.05, 3, 50)
for th in np.linspace(0, 2 * np.pi, 16, endpoint=False):
    a1.plot(t * np.cos(th), t * np.sin(th), color="C0", lw=1.4)

field(a2, lambda x, y: -x / y, "y' = -x/y: integral curves are circles")
phi = np.linspace(0, 2 * np.pi, 300)
for r in [0.5, 1.0, 1.5, 2.0]:
    a2.plot(r * np.cos(phi), r * np.sin(phi), color="C0", lw=1.4)
xs = np.linspace(-2.1, 2.1, 10)
for k in [-1, 1, 3]:
    a2.plot(xs, -xs / k, color="C3", lw=1.0, ls="--")
a2.plot([], [], color="C3", ls="--", label="isoclines y = -x/k (k = -1, 1, 3)")
a2.legend(loc="upper right", fontsize=8)
fig.tight_layout()
