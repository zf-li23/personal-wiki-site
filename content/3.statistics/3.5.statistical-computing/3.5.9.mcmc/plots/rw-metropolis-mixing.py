"""Random walk Metropolis for the N(0, 1) target with uniform proposals on (x - a, x + a):
trace plots for a = 0.1, 2.5 and 30 started at x = 10, and the sample autocorrelations."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n = 2000
widths = (0.1, 2.5, 30.0)
colors = ("C3", "C0", "C1")


def rwm(a, x0=10.0):
    x = np.empty(n)
    x[0] = x0
    acc = 0
    for t in range(n - 1):
        y = x[t] + (2 * rng.uniform() - 1) * a
        if rng.uniform() < np.exp((x[t] ** 2 - y ** 2) / 2):
            x[t + 1] = y
            acc += 1
        else:
            x[t + 1] = x[t]
    return x, acc / (n - 1)


def acf(x, lags):
    x = x - x.mean()
    v = np.dot(x, x)
    return np.array([np.dot(x[: len(x) - k], x[k:]) / v for k in lags])


fig = plt.figure(figsize=(10.5, 6.2))
grid = fig.add_gridspec(3, 2, width_ratios=(2.2, 1))
lags = np.arange(0, 41)
ax_acf = fig.add_subplot(grid[:, 1])
burn = 200
for row, (a, col) in enumerate(zip(widths, colors)):
    chain, rate = rwm(a)
    ax = fig.add_subplot(grid[row, 0])
    ax.plot(chain, color=col, lw=0.7)
    ax.axvline(burn, color="C7", ls=":", lw=1)
    ax.set_ylabel("X_t")
    ax.set_title(f"a = {a:g}: acceptance rate {rate:.2f}", fontsize=9)
    ax.grid(alpha=0.3)
    if row == 2:
        ax.set_xlabel("iteration t (dotted line: burn-in 200)")
    ax_acf.plot(lags, acf(chain[burn:], lags), "o-", ms=3, color=col, label=f"a = {a:g}")
ax_acf.axhline(0, color="C7", lw=1)
ax_acf.set_xlabel("lag k")
ax_acf.set_ylabel("sample autocorrelation after burn-in")
ax_acf.set_title("Autocorrelation", fontsize=10)
ax_acf.legend(fontsize=8)
ax_acf.grid(alpha=0.3)
fig.tight_layout()
