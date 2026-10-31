"""Traction force microscopy by Fourier-transform traction cytometry. A: a synthetic traction field of a
contractile cell on an elastic substrate (two adhesion zones at the ends of a cell 40 um long pulling
inward, peak 600 Pa) on a 64 x 64 grid of 1 um pixels. B: the substrate surface displacements it
produces (color: magnitude; arrows), computed with the Boussinesq solution for an elastic half-space,
u(k) = G(k) T(k), G_ij(k) = 2(1 + nu)/(E k) [delta_ij - nu k_i k_j/k^2], for E = 10 kPa, nu = 0.48,
with measurement noise of 20 nm added. C: tractions recovered from the noisy displacements by inverting
G(k) with Tikhonov (zeroth-order) regularization; the total force is recovered within a few percent, at
the price of blurred adhesions and an underestimated peak traction (the regularization trades
resolution for noise suppression). The strain energy delivered to the substrate is the work the
cell does on it, U = (1/2) integral of T.u."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.5))
fig.subplots_adjust(wspace=0.15, left=0.02, right=0.98, bottom=0.08, top=0.86)
n, dx = 64, 1e-6
E, nu = 1e4, 0.48
x = (np.arange(n) - n / 2) * dx
X, Y = np.meshgrid(x, x)
T = np.zeros((2, n, n))
for cx, sgn in [(-17e-6, 1), (17e-6, -1)]:
    g = np.exp(-((X - cx) ** 2 + Y ** 2) / (2 * (2.5e-6) ** 2))
    T[0] += sgn * 600 * g
k = 2 * np.pi * np.fft.fftfreq(n, d=dx)
KX, KY = np.meshgrid(k, k)
K = np.sqrt(KX ** 2 + KY ** 2)
K[0, 0] = 1.0
pref = 2 * (1 + nu) / (E * K)
G = np.array([[pref * (1 - nu * KX ** 2 / K ** 2), pref * (-nu * KX * KY / K ** 2)],
              [pref * (-nu * KX * KY / K ** 2), pref * (1 - nu * KY ** 2 / K ** 2)]])
G[:, :, 0, 0] = 0
Tk = np.fft.fft2(T)
uk = np.einsum("ijab,jab->iab", G, Tk)
u = np.real(np.fft.ifft2(uk))
rng = np.random.default_rng(0)
un = u + 20e-9 * rng.standard_normal(u.shape)
ukn = np.fft.fft2(un)
lam = 4e-10  # regularization (units of G, m/Pa)
Tr = np.zeros_like(Tk)
for a in range(n):
    for b in range(n):
        Gm = G[:, :, a, b]
        A = Gm.conj().T @ Gm + lam ** 2 * np.eye(2)
        Tr[:, a, b] = np.linalg.solve(A, Gm.conj().T @ ukn[:, a, b])
Tr = np.real(np.fft.ifft2(Tr))

s = slice(None, None, 4)
for ax, F, title, scale, cmap_tok in [(axs[0], T, "A  Imposed traction / Pa", 1, "traction"),
                                      (axs[1], u * 1e6, r"B  Displacement / $\mu$m", 1, "disp"),
                                      (axs[2], Tr, "C  Recovered traction / Pa", 1, "traction")]:
    mag = np.hypot(F[0], F[1])
    im = ax.imshow(mag, origin="lower", extent=[x[0] * 1e6, x[-1] * 1e6, x[0] * 1e6, x[-1] * 1e6], cmap="viridis",
                   vmin=0, vmax=600 if cmap_tok == "traction" else mag.max())
    sc = 600 / 8 if cmap_tok == "traction" else 0.35 / 8
    ax.quiver(X[s, s] * 1e6, Y[s, s] * 1e6, F[0][s, s], F[1][s, s], color="white", width=0.004, angles="xy",
              scale_units="xy", scale=sc)
    cb = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.02)
    cb.ax.tick_params(labelsize=FT["tiny"], colors=P.muted(), labelcolor=P.ink())
    ax.set_xticks([]); ax.set_yticks([])
    charts.title(ax, title)
F_true = np.sum(T[0][:, : n // 2]) * dx * dx
F_rec = np.sum(Tr[0][:, : n // 2]) * dx * dx
axs[2].text(0.02, 0.03, f"force per end: {F_true * 1e9:.0f} nN imposed, {F_rec * 1e9:.0f} nN recovered",
            transform=axs[2].transAxes, fontsize=FT["tiny"], color="white")
