"""Newton's method and BFGS with backtracking on Himmelblau's function."""

import numpy as np
import matplotlib.pyplot as plt


def g(x):
    return (x[0] ** 2 + x[1] - 11) ** 2 + (x[0] + x[1] ** 2 - 7) ** 2


def grad(x):
    return np.array([4 * x[0] ** 3 + 4 * x[0] * x[1] - 42 * x[0] + 2 * x[1] ** 2 - 14,
                     2 * x[0] ** 2 - 26 * x[1] - 22 + 4 * x[0] * x[1] + 4 * x[1] ** 3])


def hess(x):
    return np.array([[12 * x[0] ** 2 + 4 * x[1] - 42, 4 * (x[0] + x[1])],
                     [4 * (x[0] + x[1]), 12 * x[1] ** 2 + 4 * x[0] - 26]])


def newton(x, itr=40):
    path = [x]
    for _ in range(itr):
        x = x - np.linalg.solve(hess(x), grad(x))
        path.append(x)
    return np.array(path)


def bfgs(x, itr=40):
    M = np.eye(2)  # initial Hessian approximation
    path = [x]
    for _ in range(itr):
        d = np.linalg.solve(M, grad(x))
        alpha = 1.0
        xt = x - alpha * d
        while g(xt) > g(x):  # backtracking: halve until downhill
            alpha /= 2
            xt = x - alpha * d
        z, y = xt - x, grad(xt) - grad(x)
        if y @ z > 1e-12:  # curvature condition keeps M positive definite
            Mz = M @ z
            M = M - np.outer(Mz, Mz) / (z @ Mz) + np.outer(y, y) / (y @ z)
        x = xt
        path.append(x)
    return np.array(path)


x1 = np.linspace(-5, 5, 400)
x2 = np.linspace(-5, 5, 400)
X1, X2 = np.meshgrid(x1, x2)
Z = g(np.array([X1, X2]))

fig, ax = plt.subplots(figsize=(7.2, 6.2))
cs = ax.contour(X1, X2, np.log1p(Z), levels=25, cmap="viridis", linewidths=0.7)
runs = [("Newton from (-2, -2)", newton(np.array([-2.0, -2.0])), "C3", "o"),
        ("BFGS from (-2, -2)", bfgs(np.array([-2.0, -2.0])), "C1", "s"),
        ("BFGS from (-4, 0)", bfgs(np.array([-4.0, 0.0])), "C0", "^")]
for label, p, c, m in runs:
    ax.plot(p[:, 0], p[:, 1], ls="--", marker=m, ms=4, lw=1.2, color=c,
            label=f"{label} -> ({p[-1, 0]:.3f}, {p[-1, 1]:.3f})")
minima = np.array([[3, 2], [-2.805118, 3.131312], [-3.779310, -3.283186], [3.584428, -1.848126]])
ax.plot(minima[:, 0], minima[:, 1], "kx", ms=9, mew=2, label="local minima (g = 0)")
ax.plot(-0.270845, -0.923039, "k+", ms=11, mew=2, label="local maximum")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Himmelblau's function: contours of log(1 + g)", fontsize=10)
ax.legend(fontsize=8, loc="upper left", framealpha=0.85)
ax.set_aspect("equal")
fig.tight_layout()
