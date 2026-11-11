"""Sparse coding of image patches (Olshausen and Field 1996) on synthetic "dead leaves" images.

Images: 30 images of 128 x 128 pixels, each made of 300 overlapping opaque discs and ellipses of
random size (power-law radii), orientation and grey level, so that they contain edges at all
orientations and a roughly 1/k^2 power spectrum. Images are whitened with the filter
k exp(-(k/k0)^4) and normalized. Patches: 8 x 8 pixels.
Model: patch x = Phi a + noise; inference by ISTA, minimizing |x - Phi a|^2/2 + lam |a|_1
(lam = 0.4, 40 iterations); learning by Phi <- Phi + eta (x - Phi a) a^T, columns renormalized;
64 basis functions, 1800 batches of 100 patches.
A: the learned basis functions. B: histogram of coefficients (sparse, heavy tailed) compared with
coefficients of the same patches projected on the principal components (pixel basis rotated).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
S = 128
yy, xx = np.mgrid[0:S, 0:S]


def dead_leaves():
    im = np.full((S, S), rng.uniform(0, 1))
    for _ in range(300):
        rad = 4 * rng.pareto(1.5) + 3
        rad = min(rad, 50)
        a, b = rad, rad * rng.uniform(0.3, 1)
        th = rng.uniform(0, np.pi)
        cx, cy = rng.uniform(-10, S + 10, 2)
        u = (xx - cx) * np.cos(th) + (yy - cy) * np.sin(th)
        v = -(xx - cx) * np.sin(th) + (yy - cy) * np.cos(th)
        im[(u / a) ** 2 + (v / b) ** 2 < 1] = rng.uniform(0, 1)
    return im


fx = np.fft.fftfreq(S)
KX, KY = np.meshgrid(fx, fx)
K = np.sqrt(KX**2 + KY**2)
filt = K * np.exp(-(K / 0.35) ** 4)
imgs = []
for _ in range(30):
    im = dead_leaves()
    w = np.real(np.fft.ifft2(np.fft.fft2(im - im.mean()) * filt))
    imgs.append(w / w.std())
imgs = np.array(imgs)

p, M = 8, 64


def patches(n):
    i = rng.integers(0, 30, n)
    x = rng.integers(4, S - p - 4, n)
    y = rng.integers(4, S - p - 4, n)
    return np.array([imgs[a, b:b + p, c:c + p].ravel() for a, b, c in zip(i, y, x)]).T


Phi = rng.normal(size=(p * p, M))
Phi /= np.linalg.norm(Phi, axis=0)
lam, eta = 0.4, 0.08


def infer(X, Phi, n_it=40):
    L = np.linalg.norm(Phi, 2) ** 2
    A = np.zeros((M, X.shape[1]))
    for _ in range(n_it):
        A = A + Phi.T @ (X - Phi @ A) / L
        A = np.sign(A) * np.maximum(np.abs(A) - lam / L, 0)
    return A


for it in range(1800):
    X = patches(100)
    A = infer(X, Phi)
    Phi += eta * (X - Phi @ A) @ A.T / 100
    Phi /= np.linalg.norm(Phi, axis=0)

fig = plt.figure(figsize=(12, 5.0))
order = np.argsort(-np.abs(infer(patches(2000), Phi)).mean(1))
for j, m in enumerate(order):
    ax = fig.add_axes([0.02 + (j % 8) * 0.06, 0.78 - (j // 8) * 0.1, 0.055, 0.09])
    b = Phi[:, m].reshape(p, p)
    v = np.abs(b).max()
    ax.imshow(b, cmap="gray", vmin=-v, vmax=v, interpolation="nearest")
    ax.set_xticks([])
    ax.set_yticks([])
fig.text(0.02, 0.93, "A  64 learned basis functions (8 x 8 pixels)", fontsize=10)

bx = fig.add_axes([0.58, 0.14, 0.4, 0.72])
Xt = patches(4000)
At = infer(Xt, Phi).ravel()
C = np.cov(Xt)
ev, U = np.linalg.eigh(C)
Ap = (U.T @ Xt).ravel()
bins = np.linspace(-4, 4, 81)
bx.hist(Ap / Ap.std(), bins=bins, density=True, histtype="step", color=P.edge("rna"), lw=1.5,
        label="principal-component coefficients")
bx.hist(At / At.std(), bins=bins, density=True, histtype="step", color=P.edge("dna"), lw=1.5,
        label=f"sparse coefficients ({100 * np.mean(At == 0):.0f} % exactly zero)")
bx.set_yscale("log")
bx.set_xlabel("Coefficient / SD")
bx.set_ylabel("Probability density")
bx.legend(frameon=False, fontsize=8, loc="upper right")
bx.set_title("B  Sparse coefficients are heavy tailed", loc="left", fontsize=10)
