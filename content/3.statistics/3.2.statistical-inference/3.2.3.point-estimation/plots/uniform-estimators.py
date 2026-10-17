"""Bias, variance and MSE of three estimators of beta for U(0, beta)."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
beta = 2.0
reps = 5000
ns = np.arange(5, 201, 5)
names = ["2 * mean (moment)", "X_(n) (MLE)", "(n+1)/n * X_(n)"]
stats = {k: np.zeros((len(ns), 3)) for k in ("bias", "var", "mse")}
for i, n in enumerate(ns):
    x = rng.uniform(0, beta, size=(reps, n))
    xmax = x.max(axis=1)
    ests = [2 * x.mean(axis=1), xmax, (n + 1) / n * xmax]
    for j, e in enumerate(ests):
        stats["bias"][i, j] = e.mean() - beta
        stats["var"][i, j] = e.var()
        stats["mse"][i, j] = np.mean((e - beta) ** 2)

fig, axes = plt.subplots(1, 3, figsize=(12, 3.8))
titles = {"bias": "bias", "var": "variance", "mse": "mean squared error"}
for ax, key in zip(axes, ("bias", "var", "mse")):
    for j in range(3):
        ax.plot(ns, stats[key][:, j], lw=1.8, label=names[j])
    if key == "bias":
        ax.axhline(0, color="0.5", lw=0.8)
    else:
        ax.set_yscale("log")
    ax.set_xlabel("sample size n")
    ax.set_title(titles[key])
axes[0].legend(frameon=False)
fig.tight_layout()
