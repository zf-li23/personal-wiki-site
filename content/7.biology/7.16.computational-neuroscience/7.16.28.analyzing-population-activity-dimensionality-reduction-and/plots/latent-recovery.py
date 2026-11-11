"""Recovering a smooth low-dimensional latent state from single-trial Poisson spike counts.

Latent z(t): two independent Gaussian processes (squared-exponential kernel, length 12 bins),
300 bins. 40 neurons with rate exp(-1.0 + c_i . z(t)) per bin, random loadings c_i (s.d. 0.6) so the
mean count is about 0.4 per bin. Estimators of the 2-D latent (best linear map to the true latent,
R^2 averaged over the two coordinates, mean of 20 repeats): PCA of square-root counts, PCA of
square-root counts smoothed in time (Gaussian, s.d. 4 bins), and factor analysis (EM, 2 factors)
followed by Gaussian-process smoothing of the factor scores ("FA + GP smoothing").
A: true latent trajectory and the three estimates (one repeat, aligned by least squares).
B: R^2 of the three methods over the repeats.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d

import wikibio as bio

P = bio.P
rng = np.random.default_rng(2)
T, N, L = 300, 40, 12.0
tt = np.arange(T)
K = np.exp(-(tt[:, None] - tt[None, :]) ** 2 / (2 * L ** 2)) + 1e-6 * np.eye(T)
Lk = np.linalg.cholesky(K)


def sim():
    z = Lk @ rng.normal(size=(T, 2))
    C = rng.normal(0, 0.6, (N, 2))
    y = rng.poisson(np.exp(-1.0 + z @ C.T))
    return z, y


def pca2(y):
    x = np.sqrt(y)
    x = x - x.mean(0)
    return np.linalg.svd(x, full_matrices=False)[0][:, :2] * 1.0


def fa(x, k=2, it=60):
    n, d = x.shape
    S = x.T @ x / n
    w = np.linalg.svd(x, full_matrices=False)[2][:k].T * 0.5
    psi = np.var(x, 0)
    for _ in range(it):
        G = np.linalg.inv(np.eye(k) + w.T @ (w / psi[:, None]))
        Ez = x @ (w / psi[:, None]) @ G
        Ezz = n * G + Ez.T @ Ez
        w = (x.T @ Ez) @ np.linalg.inv(Ezz)
        psi = np.maximum(np.diag(S - w @ (Ez.T @ x) / n), 1e-3)
    G = np.linalg.inv(np.eye(k) + w.T @ (w / psi[:, None]))
    return x @ (w / psi[:, None]) @ G, np.diag(G)


def r2(est, z):
    A = np.c_[est, np.ones(len(est))]
    b = np.linalg.lstsq(A, z, rcond=None)[0]
    res = z - A @ b
    return np.mean(1 - res.var(0) / z.var(0)), A @ b


res = {"PCA": [], "smoothed PCA": [], "FA + GP smoothing": []}
keep = None
for rep in range(20):
    z, y = sim()
    x = np.sqrt(y)
    x = x - x.mean(0)
    e1 = pca2(y)
    e2 = np.linalg.svd(gaussian_filter1d(x, 4, axis=0), full_matrices=False)[0][:, :2]
    sc, gv = fa(x)
    sm = np.zeros_like(sc)
    for j in range(2):
        sm[:, j] = K @ np.linalg.solve(K + gv[j] * np.eye(T), sc[:, j])
    out = {}
    for name, e in (("PCA", e1), ("smoothed PCA", e2), ("FA + GP smoothing", sm)):
        v, fit = r2(e, z)
        res[name].append(v)
        out[name] = fit
    if rep == 0:
        keep = (z, out)

fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.1), gridspec_kw={"width_ratios": [1.6, 1]})
ax = axs[0]
z, out = keep
ax.plot(z[:, 0], z[:, 1], color=P.ink(), lw=2.2, label="true latent")
for (name, fit), c in zip(out.items(), (P.edge("dna"), P.edge("protein"), P.edge("rna"))):
    ax.plot(fit[:, 0], fit[:, 1], color=c, lw=0.6 if name == "PCA" else 1.2, alpha=0.6 if name == "PCA" else 0.95, label=name)
ax.set_aspect("equal")
ax.set_xlabel("Latent coordinate 1")
ax.set_ylabel("Latent coordinate 2")
ax.legend(frameon=False, fontsize=7.5, loc="best")
ax.set_title("A  One 300-bin trial", loc="left", fontsize=10)
ax = axs[1]
names = list(res)
means = [np.mean(res[n]) for n in names]
sds = [np.std(res[n]) for n in names]
ax.bar(range(3), means, yerr=sds, color=[P.fill("dna"), P.fill("protein"), P.fill("rna")],
       edgecolor=[P.edge("dna"), P.edge("protein"), P.edge("rna")], capsize=3)
ax.set_xticks(range(3))
ax.set_xticklabels(["PCA", "smoothed\nPCA", "FA + GP\nsmoothing"], fontsize=8)
ax.set_ylabel("R$^2$ of the latent (mean of 20 trials)")
ax.set_ylim(0, 1)
ax.set_title("B  Accuracy", loc="left", fontsize=10)
fig.tight_layout()
