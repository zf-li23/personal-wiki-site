"""Convergence of the power method for symmetric matrices with different eigenvalue ratios."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n = 50
Q, _ = np.linalg.qr(rng.standard_normal((n, n)))
q0 = rng.standard_normal(n)
q0 /= np.linalg.norm(q0)
iters = np.arange(1, 81)

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))
for ratio, c in zip([0.5, 0.8, 0.95], ["C0", "C1", "C3"]):
    lam = np.concatenate([[1.0, ratio], ratio * rng.uniform(0, 1, n - 2)])
    A = Q @ np.diag(lam) @ Q.T
    x1 = Q[:, 0]
    q, err_val, err_vec = q0.copy(), [], []
    for _ in iters:
        z = A @ q
        q = z / np.linalg.norm(z)
        err_val.append(abs(q @ A @ q - 1.0))  # Rayleigh quotient versus lambda_1 = 1
        err_vec.append(np.linalg.norm(q - np.sign(q @ x1) * x1))
    axes[0].semilogy(iters, err_vec, color=c, lw=1.5, label=f"|lambda2/lambda1| = {ratio}")
    axes[0].semilogy(iters, err_vec[0] * ratio ** (iters - 1.0), color=c, lw=0.8, ls="--")
    axes[1].semilogy(iters, np.maximum(err_val, 1e-17), color=c, lw=1.5, label=f"|lambda2/lambda1| = {ratio}")
    axes[1].semilogy(iters, err_val[0] * ratio ** (2 * (iters - 1.0)), color=c, lw=0.8, ls="--")

axes[0].set_title("Eigenvector error (dashed: ratio^k)")
axes[1].set_title("Eigenvalue error (dashed: ratio^(2k))")
axes[0].set_ylabel("||q_k - x_1||")
axes[1].set_ylabel("|q_k^T A q_k - lambda_1|")
for ax in axes:
    ax.set_xlabel("iteration k")
    ax.set_ylim(1e-17, 10)
    ax.grid(alpha=0.3)
    ax.legend(loc="lower left")
fig.tight_layout()
