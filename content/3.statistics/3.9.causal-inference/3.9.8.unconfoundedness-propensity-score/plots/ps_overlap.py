"""Estimated propensity score and linearized propensity score by treatment group (simulated data)."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n = 3000
x1 = rng.normal(0, 1, n)
x2 = rng.normal(0, 1, n)
x3 = rng.binomial(1, 0.4, n)
logit = -2.2 + 1.6 * x1 + 0.8 * x2 + 0.9 * x3 + 0.3 * x1 * x2
w = rng.random(n) < 1 / (1 + np.exp(-logit))



def logistic_newton(h, w, steps=25):
    """Maximum likelihood logistic regression by Newton-Raphson, started at the constant-only fit."""
    phi = np.zeros(h.shape[1])
    phi[0] = np.log(w.mean() / (1 - w.mean()))
    for _ in range(steps):
        e = 1 / (1 + np.exp(-h @ phi))
        grad = h.T @ (w - e)
        hess = -(h * (e * (1 - e))[:, None]).T @ h
        phi = phi - np.linalg.solve(hess, grad)
    return phi


h = np.column_stack([np.ones(n), x1, x2, x3, x1 * x2])
phi_hat = logistic_newton(h, w.astype(float))
e_hat = 1 / (1 + np.exp(-h @ phi_hat))
l_hat = np.log(e_hat / (1 - e_hat))

fig, axes = plt.subplots(1, 2, figsize=(11, 3.8))
for ax, values, label, bins in [
    (axes[0], e_hat, "estimated propensity score", np.linspace(0, 1, 41)),
    (axes[1], l_hat, "linearized propensity score", np.linspace(l_hat.min(), l_hat.max(), 41)),
]:
    ax.hist(values[~w], bins=bins, density=True, alpha=0.55, color="C0",
            label=f"control (N = {(~w).sum()})")
    ax.hist(values[w], bins=bins, density=True, alpha=0.55, color="C3",
            label=f"treated (N = {w.sum()})")
    ax.set_xlabel(label)
    ax.set_ylabel("density")
    ax.legend(fontsize=8)
axes[0].set_title("Propensity score", fontsize=10)
axes[1].set_title("Log odds of the propensity score", fontsize=10)
fig.tight_layout()
