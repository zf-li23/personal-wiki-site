"""Errors of bisection, fixed-point iterations, the secant method and Newton's method for x + log(x) = 0."""

import numpy as np
import matplotlib.pyplot as plt

f = lambda x: x + np.log(x)
df = lambda x: 1 + 1 / x
x_star = 0.5671432904097838  # the omega constant, root of x + log(x) = 0


def bisection(a, b, n):
    out = []
    for _ in range(n):
        m = (a + b) / 2
        out.append(m)
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m
    return out


def fixed_point(G, x, n):
    out = []
    for _ in range(n):
        x = G(x)
        out.append(x)
    return out


def secant(x0, x1, n):
    out = []
    for _ in range(n):
        if f(x1) == f(x0):
            break
        x0, x1 = x1, x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        out.append(x1)
    return out


def newton(x, n):
    out = []
    for _ in range(n):
        x = x - f(x) / df(x)
        out.append(x)
    return out


n = 40
runs = {
    "bisection on [0.1, 1]": bisection(0.1, 1.0, n),
    "fixed point G2(x) = exp(-x)": fixed_point(lambda x: np.exp(-x), 1.0, n),
    "fixed point G3(x) = (x + exp(-x))/2": fixed_point(lambda x: (x + np.exp(-x)) / 2, 1.0, n),
    "secant from 1, 0.9": secant(1.0, 0.9, n),
    "Newton from 1": newton(1.0, n),
}

fig, ax = plt.subplots(figsize=(7.5, 4.6))
for (label, xs), c, mk in zip(runs.items(), ["C0", "C1", "C2", "C4", "C3"], ["o", "s", "^", "D", "v"]):
    err = np.abs(np.array(xs) - x_star)
    err = np.where(err == 0, np.nan, err)
    ax.semilogy(np.arange(1, len(xs) + 1), err, marker=mk, ms=3.5, lw=1.3, color=c, label=label)
ax.set_xlabel("iteration t")
ax.set_ylabel("|x(t) - x*|")
ax.set_title("Root of f(x) = x + log(x): linear versus superlinear convergence")
ax.set_ylim(1e-17, 1)
ax.grid(alpha=0.3)
ax.legend(loc="upper right", fontsize=9)
fig.tight_layout()
