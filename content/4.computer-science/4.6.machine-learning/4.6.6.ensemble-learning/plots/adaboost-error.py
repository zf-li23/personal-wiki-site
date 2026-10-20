"""AdaBoost with decision stumps on a circular concept: decision regions, errors and the training-error bound."""

import numpy as np
import matplotlib.pyplot as plt


def fit_stump(X, y, w):
    best = (np.inf, 0, 0.0, 1)
    for j in range(X.shape[1]):
        for thr in np.unique(X[:, j]):
            err = w[np.where(X[:, j] > thr, 1, -1) != y].sum()
            for sign, e in ((1, err), (-1, 1 - err)):
                if e < best[0]:
                    best = (e, j, thr, sign)
    return best


def stump(X, j, thr, sign):
    return sign * np.where(X[:, j] > thr, 1, -1)


rng = np.random.default_rng(0)
X = rng.uniform(-1, 1, (500, 2))
y = np.where(X[:, 0] ** 2 + X[:, 1] ** 2 < 0.5, 1, -1)
Xtr, ytr, Xte, yte = X[:300], y[:300], X[300:], y[300:]

T = 200
w = np.full(len(ytr), 1 / len(ytr))
Ftr, Fte = np.zeros(len(ytr)), np.zeros(len(yte))
grid = np.linspace(-1, 1, 200)
G = np.array(np.meshgrid(grid, grid)).reshape(2, -1).T
Fg = np.zeros(len(G))
train_err, test_err, bound = [], [], []
b = 1.0
for t in range(T):
    eps, j, thr, sign = fit_stump(Xtr, ytr, w)
    alpha = 0.5 * np.log((1 - eps) / eps)
    h = stump(Xtr, j, thr, sign)
    w = w * np.exp(-alpha * ytr * h)
    w /= w.sum()
    Ftr += alpha * h
    Fte += alpha * stump(Xte, j, thr, sign)
    Fg += alpha * stump(G, j, thr, sign)
    b *= 2 * np.sqrt(eps * (1 - eps))
    train_err.append(np.mean(np.sign(Ftr) != ytr))
    test_err.append(np.mean(np.sign(Fte) != yte))
    bound.append(b)

fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))
ax = axes[0]
ax.contourf(grid, grid, np.sign(Fg).reshape(200, 200), levels=[-2, 0, 2], colors=["C0", "C3"], alpha=0.2)
ax.scatter(Xtr[ytr == 1, 0], Xtr[ytr == 1, 1], s=10, color="C3", label="+1")
ax.scatter(Xtr[ytr == -1, 0], Xtr[ytr == -1, 1], s=10, color="C0", label="-1")
ax.add_patch(plt.Circle((0, 0), np.sqrt(0.5), fill=False, ls="--", color="gray"))
ax.set_aspect("equal")
ax.set_title(f"decision regions after T = {T} stumps")
ax.legend(loc="upper right", fontsize=8)
ax = axes[1]
ts = np.arange(1, T + 1)
ax.plot(ts, bound, label=r"bound $\prod_t 2\sqrt{\varepsilon_t(1-\varepsilon_t)}$")
ax.plot(ts, train_err, label="training error")
ax.plot(ts, test_err, label="test error")
ax.set_xscale("log")
ax.set_xlabel("number of rounds T")
ax.set_ylabel("error")
ax.set_title("AdaBoost errors")
ax.legend(fontsize=8)
fig.tight_layout()
