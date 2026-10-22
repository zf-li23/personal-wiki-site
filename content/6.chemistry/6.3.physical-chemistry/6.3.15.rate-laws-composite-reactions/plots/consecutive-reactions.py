"""Consecutive first-order reactions A -> B -> C solved with the matrix exponential,
for several ratios k2/k1 (k1 fixed); the dots mark t_max and y_max of the intermediate."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm

k1 = 1.0
ratios = [0.2, 1.0, 5.0, 50.0]
t = np.linspace(0, 8, 400)
c0 = np.array([1.0, 0.0, 0.0])

fig, axs = plt.subplots(1, 4, figsize=(13, 3.3), sharey=True)
for ax, r in zip(axs, ratios):
    k2 = r * k1
    K = np.array([[-k1, 0, 0], [k1, -k2, 0], [0, k2, 0]])
    c = np.array([expm(K * ti) @ c0 for ti in t])
    ax.plot(t, c[:, 0], color="C0", label="A")
    ax.plot(t, c[:, 1], color="C1", label="B (intermediate)")
    ax.plot(t, c[:, 2], color="C2", label="C")
    if r == 1.0:
        tmax, ymax = 1 / k1, np.exp(-1)
    else:
        tmax = np.log(k2 / k1) / (k2 - k1)
        ymax = (k1 / k2) ** (k2 / (k2 - k1))
    ax.plot([tmax], [ymax], "o", color="C1", ms=4)
    ax.set_title(rf"$k_2/k_1 = {r:g}$", fontsize=10)
    ax.set_xlabel(r"$k_1 t$")
axs[0].set_ylabel(r"$c/c_{\mathrm{A},0}$")
axs[0].legend(frameon=False, fontsize=8)
fig.tight_layout()
