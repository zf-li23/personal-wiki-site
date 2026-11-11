"""jPCA-style analysis of rotational population dynamics.

8 conditions; the latent state is 6-dimensional with two rotation planes (angular frequencies
2 pi x 2.0 and 2 pi x 3.2 rad/s) decaying with time constant 0.4 s, started from condition-specific
states, observed for 0.6 s in 10 ms bins; 80 neurons = random linear read-out of the latent state
plus Gaussian noise (s.d. 0.05). For comparison, "random" data: independent smooth Gaussian processes
(length 0.1 s) in the 6 latent dimensions for each condition (no rotational structure).
Analysis: PCA of the condition-by-time data to 6 dimensions; least squares fit of x' = x M with M
unconstrained or skew-symmetric (M = -M^T); the jPC plane is the pair of eigenvectors of the
skew-symmetric M with the largest imaginary part.
A: condition trajectories in the first jPC plane (dots mark the start). B: the first jPC against
time. C: fraction of the variance of x' explained by the skew-symmetric and by the unconstrained fits
for the rotational and the random data.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import expm

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
dt, T, nc, N = 0.01, 61, 8, 80
t = np.arange(T) * dt


def rot(w):
    return np.array([[0, -w], [w, 0]])


Om = np.zeros((6, 6))
Om[:2, :2] = rot(2 * np.pi * 2.0)
Om[2:4, 2:4] = rot(2 * np.pi * 3.2)
A = Om - np.eye(6) / 0.4
Z0 = rng.normal(0, 1, (nc, 6)) * np.array([1, 1, 0.6, 0.6, 0, 0])
Zrot = np.array([[expm(A * ti) @ z0 for ti in t] for z0 in Z0])      # (nc, T, 6)
K = np.exp(-(t[:, None] - t[None, :]) ** 2 / (2 * 0.1 ** 2)) + 1e-6 * np.eye(T)
Zrnd = np.array([np.linalg.cholesky(K) @ rng.normal(size=(T, 6)) for _ in range(nc)]) * 0.7
W = rng.normal(0, 1, (6, N)) / np.sqrt(6)


def analyse(Z):
    Y = Z @ W + rng.normal(0, 0.05, (nc, T, N))
    Yc = Y - Y.mean((0, 1))
    flat = Yc.reshape(-1, N)
    Vt = np.linalg.svd(flat, full_matrices=False)[2][:6]
    X = Yc @ Vt.T                                            # (nc, T, 6)
    dX = np.gradient(X, dt, axis=1)
    Xf, dXf = X.reshape(-1, 6), dX.reshape(-1, 6)
    Mfull = np.linalg.lstsq(Xf, dXf, rcond=None)[0]
    basis = []
    for i in range(6):
        for j in range(i + 1, 6):
            B = np.zeros((6, 6))
            B[i, j], B[j, i] = 1, -1
            basis.append((Xf @ B).ravel())
    c = np.linalg.lstsq(np.array(basis).T, dXf.ravel(), rcond=None)[0]
    Msk = np.zeros((6, 6))
    idx = 0
    for i in range(6):
        for j in range(i + 1, 6):
            Msk[i, j], Msk[j, i] = c[idx], -c[idx]
            idx += 1
    tot = (dXf ** 2).sum()
    return X, Msk, 1 - ((dXf - Xf @ Msk) ** 2).sum() / tot, 1 - ((dXf - Xf @ Mfull) ** 2).sum() / tot


X, Msk, r2s, r2f = analyse(Zrot)
_, _, r2s_r, r2f_r = analyse(Zrnd)
ev, evec = np.linalg.eig(Msk.T)     # row-vector convention x' = x M  ->  x'^T = M^T x^T
k = np.argmax(ev.imag)
u = evec[:, k]
plane = np.c_[u.real, u.imag]
plane /= np.linalg.norm(plane, axis=0)
J = X @ plane                                               # (nc, T, 2)
freq = ev[k].imag / (2 * np.pi)

fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.1))
ax = axs[0]
cmap = plt.get_cmap("viridis")
for c in range(nc):
    col = cmap(c / (nc - 1))
    ax.plot(J[c, :, 0], J[c, :, 1], color=col, lw=1.5)
    ax.plot(J[c, 0, 0], J[c, 0, 1], "o", color=col, ms=4)
ax.set_aspect("equal")
ax.set_xlabel("jPC 1")
ax.set_ylabel("jPC 2")
ax.set_title(f"A  Rotation plane ({freq:.1f} Hz)", loc="left", fontsize=10)
ax = axs[1]
for c in range(nc):
    ax.plot(t * 1e3, J[c, :, 0], color=cmap(c / (nc - 1)), lw=1.3)
ax.set_xlabel("Time / ms")
ax.set_ylabel("jPC 1")
ax.set_title("B  Condition-wise oscillation", loc="left", fontsize=10)
ax = axs[2]
x = np.arange(2)
ax.bar(x - 0.18, [r2s, r2s_r], 0.34, color=P.fill("rna"), edgecolor=P.edge("rna"), label="skew-symmetric M")
ax.bar(x + 0.18, [r2f, r2f_r], 0.34, color=P.fill("dna"), edgecolor=P.edge("dna"), label="unconstrained M")
ax.set_xticks(x)
ax.set_xticklabels(["rotational\ndata", "random smooth\ndata"], fontsize=8.5)
ax.set_ylabel("R$^2$ of x'")
ax.set_ylim(0, 1.15)
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax.set_title("C  Fit of linear dynamics", loc="left", fontsize=10)
fig.tight_layout()
