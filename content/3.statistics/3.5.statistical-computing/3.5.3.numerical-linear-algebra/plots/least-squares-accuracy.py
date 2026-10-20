"""Relative error of least squares solutions by the normal equations, Householder QR and the SVD."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
m, n = 100, 10
U, _ = np.linalg.qr(rng.standard_normal((m, n)))
V, _ = np.linalg.qr(rng.standard_normal((n, n)))
x_true = np.ones(n)

kappas = np.logspace(0, 12, 25)
err = {"normal equations (Cholesky)": [], "Householder QR": [], "SVD": []}
for k in kappas:
    A = U @ np.diag(np.logspace(0, -np.log10(k), n)) @ V.T
    b = A @ x_true  # consistent system: zero residual
    # normal equations; fall back to a general solver once A^T A is numerically singular
    try:
        L = np.linalg.cholesky(A.T @ A)
        x_ne = np.linalg.solve(L.T, np.linalg.solve(L, A.T @ b))
    except np.linalg.LinAlgError:
        x_ne = np.full(n, np.nan)
    Q, R = np.linalg.qr(A)
    x_qr = np.linalg.solve(R, Q.T @ b)
    Us, s, Vt = np.linalg.svd(A, full_matrices=False)
    x_svd = Vt.T @ ((Us.T @ b) / s)
    for name, x in zip(err, [x_ne, x_qr, x_svd]):
        err[name].append(np.linalg.norm(x - x_true) / np.linalg.norm(x_true))

eps = np.finfo(float).eps
fig, ax = plt.subplots(figsize=(7, 4.6))
for (name, vals), c, mk in zip(err.items(), ["C3", "C0", "C2"], ["o", "s", "^"]):
    ax.loglog(kappas, vals, marker=mk, ms=4, lw=1.4, color=c, label=name)
ax.loglog(kappas, eps * kappas, ls="--", lw=1, color="gray", label="eps * kappa")
ax.loglog(kappas, eps * kappas**2, ls=":", lw=1, color="gray", label="eps * kappa^2")
ax.set_ylim(1e-17, 1e3)
ax.set_xlabel("condition number kappa(A)")
ax.set_ylabel("relative error of x")
ax.set_title("Least squares with A = U diag(s) V^T (100 x 10), b = A x")
ax.legend(loc="upper left", fontsize=9)
ax.grid(alpha=0.3, which="both")
fig.tight_layout()
