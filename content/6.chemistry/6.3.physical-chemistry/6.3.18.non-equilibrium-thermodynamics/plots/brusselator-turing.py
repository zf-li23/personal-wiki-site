"""Turing instability of the Brusselator with diffusion (a = 4.5, Dx = 2, Dy = 16):
growth rate of a perturbation exp(i q r + lambda t) versus q, and a 2D pattern grown from
small random noise (periodic box, semi-implicit Fourier spectral time stepping)."""

import numpy as np
import matplotlib.pyplot as plt

a, Dx, Dy = 4.5, 2.0, 16.0
eta = np.sqrt(Dx / Dy)
bT = (1 + a * eta) ** 2          # Turing threshold
bH = 1 + a * a                    # Hopf threshold of the well-mixed system


def growth(b, q):
    lam = []
    for qq in q:
        J = np.array([[b - 1 - Dx * qq**2, a * a], [-b, -a * a - Dy * qq**2]])
        lam.append(np.linalg.eigvals(J).real.max())
    return np.array(lam)


fig, axes = plt.subplots(1, 2, figsize=(12, 5.0), gridspec_kw={"width_ratios": [1.15, 1]})
ax = axes[0]
q = np.linspace(0, 2.0, 400)
for b, c in [(5.5, "C0"), (bT, "C2"), (7.5, "C3")]:
    ax.plot(q, growth(b, q), color=c, lw=2, label=f"b = {b:.2f}")
ax.axhline(0, color="0.5", lw=1)
qc = np.sqrt(a / np.sqrt(Dx * Dy))
ax.axvline(qc, color="0.5", ls=":", lw=1)
ax.text(qc + 0.03, 0.25, "q_c", color="0.4")
ax.set_ylim(-1.5, 0.6)
ax.set_xlabel("wavenumber q")
ax.set_ylabel("largest Re λ")
ax.set_title(f"dispersion relation (Turing threshold b_T = {bT:.2f}, Hopf b_H = {bH:.2f})", fontsize=10)
ax.legend(loc="lower left")

# 2D simulation at b = 7.5
b = 7.5
n, L = 128, 64.0
k = 2 * np.pi * np.fft.fftfreq(n, d=L / n)
K2 = k[:, None] ** 2 + k[None, :] ** 2
rng = np.random.default_rng(0)
x = a + 0.01 * rng.standard_normal((n, n))
y = b / a + 0.01 * rng.standard_normal((n, n))
dt, steps = 0.01, 8000
ex = 1.0 / (1.0 + dt * Dx * K2)
ey = 1.0 / (1.0 + dt * Dy * K2)
for _ in range(steps):
    x2y = x * x * y
    fx = a - (b + 1) * x + x2y
    fy = b * x - x2y
    x = np.fft.ifft2((np.fft.fft2(x + dt * fx)) * ex).real
    y = np.fft.ifft2((np.fft.fft2(y + dt * fy)) * ey).real
ax = axes[1]
im = ax.imshow(x, extent=[0, L, 0, L], origin="lower", cmap="viridis")
fig.colorbar(im, ax=ax, label="x")
ax.set_title(f"pattern at t = {dt * steps:g} (b = {b:g}), wavelength 2π/q_c = {2 * np.pi / qc:.1f}", fontsize=10)
ax.set_xlabel("position")
ax.set_ylabel("position")
fig.tight_layout()
