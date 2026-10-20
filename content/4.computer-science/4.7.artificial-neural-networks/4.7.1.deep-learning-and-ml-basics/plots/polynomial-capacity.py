"""Capacity and generalization on a toy regression problem: noisy samples of
sin(2 pi x) fitted by least-squares polynomials of degree 1, 3 and 12, and the
training and test root-mean-square errors as functions of the degree."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)


def target(x):
    return np.sin(2 * np.pi * x)


n_train, noise = 15, 0.25
x_train = np.sort(rng.uniform(0, 1, n_train))
y_train = target(x_train) + noise * rng.standard_normal(n_train)
x_test = rng.uniform(0, 1, 2000)
y_test = target(x_test) + noise * rng.standard_normal(x_test.size)


def fit(degree):
    # a Legendre basis keeps the least-squares problem well conditioned
    return np.polynomial.Legendre.fit(x_train, y_train, degree, domain=[0, 1])


def rmse(p, x, y):
    return np.sqrt(np.mean((p(x) - y) ** 2))


fig, axes = plt.subplots(1, 4, figsize=(14, 3.4))
grid = np.linspace(0, 1, 400)
titles = {1: "degree 1: underfitting", 3: "degree 3: appropriate", 12: "degree 12: overfitting"}
for ax, degree in zip(axes[:3], titles):
    p = fit(degree)
    ax.plot(grid, target(grid), color="C7", lw=1, ls="--", label="true function")
    ax.plot(grid, p(grid), color="C0", lw=1.8, label="fitted polynomial")
    ax.scatter(x_train, y_train, s=18, color="C1", zorder=3, label="training data")
    ax.set_ylim(-1.8, 1.8)
    ax.set_title(titles[degree], fontsize=10)
    ax.set_xlabel("x")
axes[0].legend(fontsize=7, loc="lower left")

degrees = np.arange(0, 14)
train_err = [rmse(fit(d), x_train, y_train) for d in degrees]
test_err = [rmse(fit(d), x_test, y_test) for d in degrees]
ax = axes[3]
ax.plot(degrees, train_err, "o-", color="C0", ms=4, label="training error")
ax.plot(degrees, test_err, "s-", color="C3", ms=4, label="test error")
ax.axhline(noise, color="C7", lw=1, ls=":", label="noise level")
best = degrees[int(np.argmin(test_err))]
ax.axvline(best, color="C2", lw=1, ls="--", label="optimal capacity")
ax.set_yscale("log")
ax.set_xlabel("polynomial degree (capacity)")
ax.set_ylabel("RMSE")
ax.set_title("error against capacity", fontsize=10)
ax.legend(fontsize=7)
ax.grid(alpha=0.3)
fig.tight_layout()
