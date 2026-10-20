"""Gradient descent on f(x) = (10 x1^2 + x2^2) / 2 with different step size rules, and conjugate gradient."""

import numpy as np
import matplotlib.pyplot as plt

A = np.diag([10.0, 1.0])
x0 = np.array([2.0, 20.0])


def f(x):
    return 0.5 * x @ A @ x


def grad(x):
    return A @ x


def fixed(alpha, k):
    x, path = x0.copy(), [x0.copy()]
    for _ in range(k):
        x = x - alpha * grad(x)
        path.append(x.copy())
    return np.array(path)


def backtracking(k, beta=0.8, c=0.5):
    x, path = x0.copy(), [x0.copy()]
    for _ in range(k):
        gx, a = grad(x), 1.0
        while f(x - a * gx) > f(x) - c * a * gx @ gx:  # Armijo condition
            a *= beta
        x = x - a * gx
        path.append(x.copy())
    return np.array(path)


def exact(k):
    x, path = x0.copy(), [x0.copy()]
    for _ in range(k):
        r = -grad(x)
        x = x + (r @ r) / (r @ A @ r) * r
        path.append(x.copy())
    return np.array(path)


def conjugate_gradient():
    x = x0.copy()
    r = -grad(x)
    d = r.copy()
    path = [x.copy()]
    for _ in range(2):
        a = (r @ r) / (d @ A @ d)
        x = x + a * d
        r_new = r - a * A @ d
        d = r_new + (r_new @ r_new) / (r @ r) * d
        r = r_new
        path.append(x.copy())
    return np.array(path)


runs = [("fixed step 0.35: diverges", fixed(0.35, 6)),
        ("fixed step 0.01: slow (100 steps)", fixed(0.01, 100)),
        ("fixed step 0.1 = 1/L", fixed(0.1, 40)),
        ("backtracking, beta = 0.8", backtracking(40)),
        ("exact line search: zig-zag", exact(40)),
        ("conjugate gradient: 2 steps", conjugate_gradient())]

g1, g2 = np.meshgrid(np.linspace(-20, 20, 300), np.linspace(-20, 20, 300))
F = 0.5 * (10 * g1 ** 2 + g2 ** 2)
fig, axes = plt.subplots(2, 3, figsize=(11, 7.6))
for ax, (title, p) in zip(axes.flat, runs):
    ax.contour(g1, g2, F, levels=[1, 10, 50, 200, 500, 1000, 2000], colors="gray", linewidths=0.6)
    ax.plot(p[:, 0], p[:, 1], "o-", ms=3, lw=1, color="C3")
    ax.plot(0, 0, "*", ms=10, color="C0")
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 22)
    ax.set_title(f"{title}\nf(x_t) after {len(p) - 1} steps: {f(p[-1]):.2e}", fontsize=9)
    ax.set_aspect("equal")
fig.tight_layout()
