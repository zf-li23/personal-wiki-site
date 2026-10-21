"""Single-electron double-slit experiment: hits drawn one by one from |psi1 + psi2|^2 build up the fringes;
the bottom panel compares |psi1|^2 + |psi2|^2 (no interference) with |psi1 + psi2|^2."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)

# Fraunhofer amplitudes in the dimensionless screen coordinate x (fringe spacing 1), slit width a = d / 4.
x = np.linspace(-6, 6, 4000)
beta = np.pi * x / 4
envelope = np.sinc(beta / np.pi)
psi1 = envelope * np.exp(1j * np.pi * x) / np.sqrt(2)
psi2 = envelope * np.exp(-1j * np.pi * x) / np.sqrt(2)
P1 = np.abs(psi1) ** 2
P2 = np.abs(psi2) ** 2
P12 = np.abs(psi1 + psi2) ** 2

cdf = np.cumsum(P12)
cdf /= cdf[-1]

counts = [10, 100, 3000, 20000]
fig = plt.figure(figsize=(10.5, 6.0))
gs = fig.add_gridspec(2, 4, height_ratios=[1.5, 1.0])
for k, n in enumerate(counts):
    ax = fig.add_subplot(gs[0, k])
    xs = np.interp(rng.random(n), cdf, x)
    ys = rng.random(n)
    ax.scatter(xs, ys, s=4 if n < 1000 else 0.4, color="C0", alpha=1.0 if n < 1000 else 0.5, lw=0)
    ax.set_xlim(-6, 6)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"N = {n} electrons", fontsize=10)

ax = fig.add_subplot(gs[1, :])
ax.plot(x, P12, color="C0", lw=1.8, label="both slits open: |ψ1 + ψ2|²")
ax.plot(x, P1 + P2, color="C3", lw=1.5, ls="--", label="|ψ1|² + |ψ2|² (which-slit known)")
ax.plot(x, P1, color="0.5", lw=1.0, ls=":", label="|ψ1|² alone")
ax.set_xlim(-6, 6)
ax.set_ylim(0, 2.1)
ax.set_xlabel("position on the screen  x  (units of fringe spacing)")
ax.set_ylabel("probability density")
ax.legend(loc="upper right", fontsize=8, frameon=False)

fig.tight_layout()
