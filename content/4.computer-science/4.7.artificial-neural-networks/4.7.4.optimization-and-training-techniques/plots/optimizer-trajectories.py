"""Trajectories of gradient descent, momentum, Nesterov, RMSProp and Adam
on an ill-conditioned quadratic (left) and on the Rosenbrock function (middle),
and the loss on the Rosenbrock function against the iteration (right)."""

import numpy as np
import matplotlib.pyplot as plt


def quad(w):
    return 0.5 * (w[0] ** 2 + 25 * w[1] ** 2), np.array([w[0], 25 * w[1]])


def rosen(w):
    x, y = w
    f = (1 - x) ** 2 + 100 * (y - x ** 2) ** 2
    return f, np.array([-2 * (1 - x) - 400 * x * (y - x ** 2), 200 * (y - x ** 2)])


def run(fun, w0, method, lr, steps, beta=0.9, beta2=0.999, eps=1e-8):
    w = np.array(w0, float)
    v = np.zeros(2)
    s = np.zeros(2)
    path, losses = [w.copy()], [fun(w)[0]]
    for t in range(1, steps + 1):
        if method == "Nesterov":
            g = fun(w - lr * beta * v)[1]      # gradient at the look-ahead point
            v = beta * v + g
            w = w - lr * v
        else:
            g = fun(w)[1]
            if method == "GD":
                w = w - lr * g
            elif method == "momentum":
                v = beta * v + g
                w = w - lr * v
            elif method == "RMSProp":
                s = 0.9 * s + 0.1 * g * g
                w = w - lr * g / (np.sqrt(s) + eps)
            elif method == "Adam":
                v = beta * v + (1 - beta) * g
                s = beta2 * s + (1 - beta2) * g * g
                w = w - lr * (v / (1 - beta ** t)) / (np.sqrt(s / (1 - beta2 ** t)) + eps)
        path.append(w.copy())
        losses.append(fun(w)[0])
    return np.array(path), np.array(losses)


methods = ["GD", "momentum", "Nesterov", "RMSProp", "Adam"]
quad_lr = {"GD": 0.075, "momentum": 0.012, "Nesterov": 0.012, "RMSProp": 0.15, "Adam": 0.3}
rosen_lr = {"GD": 1e-3, "momentum": 2e-4, "Nesterov": 2e-4, "RMSProp": 5e-3, "Adam": 0.02}
styles = dict(zip(methods, ["-", "-", "--", "-.", "-"]))

fig, axes = plt.subplots(1, 3, figsize=(13, 4.2))
ax = axes[0]
X, Y = np.meshgrid(np.linspace(-6, 6, 300), np.linspace(-2.2, 2.2, 300))
ax.contour(X, Y, 0.5 * (X ** 2 + 25 * Y ** 2), levels=np.geomspace(0.05, 60, 14), colors="C7", linewidths=0.5)
for m in methods:
    p, _ = run(quad, [-5.5, 1.5], m, quad_lr[m], 40)
    ax.plot(p[:, 0], p[:, 1], styles[m], lw=1.3, marker=".", ms=3, label=m)
ax.plot(0, 0, "k*", ms=9)
ax.set_title("quadratic, condition number 25 (40 steps)", fontsize=10)
ax.set_xlabel("$w_1$")
ax.set_ylabel("$w_2$")
ax.legend(fontsize=8, loc="lower right")

ax = axes[1]
X, Y = np.meshgrid(np.linspace(-2, 2, 400), np.linspace(-1, 3, 400))
ax.contour(X, Y, (1 - X) ** 2 + 100 * (Y - X ** 2) ** 2, levels=np.geomspace(0.1, 2500, 18), colors="C7", linewidths=0.5)
curves = {}
for m in methods:
    p, losses = run(rosen, [-1.5, 2.0], m, rosen_lr[m], 3000)
    curves[m] = losses
    ax.plot(p[:, 0], p[:, 1], styles[m], lw=1.3, label=m)
ax.plot(1, 1, "k*", ms=9)
ax.set_title("Rosenbrock function (3000 steps)", fontsize=10)
ax.set_xlabel("$w_1$")
ax.set_ylabel("$w_2$")

ax = axes[2]
for m in methods:
    ax.semilogy(curves[m] + 1e-16, styles[m], lw=1.3, label=m)
ax.set_title("Rosenbrock: loss", fontsize=10)
ax.set_xlabel("iteration")
ax.set_ylim(1e-10, 1e2)
ax.grid(alpha=0.3)
fig.tight_layout()
