# Demixing kinetics: the Cahn-Hilliard equation with the Flory-Huggins free energy,
#   d phi / dt = M laplacian( f'(phi) - kappa laplacian phi ),
#   f(phi) = (phi/N) ln phi + (1 - phi) ln(1 - phi) + chi phi (1 - phi),
# for N = 10 and chi = 1.1 (critical point phi_c = 0.240, chi_c = 0.866), on a periodic 128 x 128 grid
# (dimensionless units: M = 1, kappa = 1, grid spacing 1), semi-implicit pseudo-spectral time stepping with a
# linear stabilizing term. Initial state: uniform phi_0 plus small random fluctuations (amplitude 0.01).
# Top row: phi_0 = 0.24, near the critical composition: fluctuations of one wavelength grow everywhere at once
#   (spinodal decomposition), giving elongated, partly interconnected domains that pinch off and coarsen.
# Bottom row: phi_0 = 0.12, inside the spinodal but off-critical: the dense phase appears as droplets that grow
#   and coarsen (small droplets dissolve and large ones grow).
# Colour: polymer volume fraction phi (dense phase dark); times in the same dimensionless units.
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

import wikibio as bio

P = bio.P
N, CHI, KAPPA = 10, 1.1, 1.0
L = 128
k = 2 * np.pi * np.fft.fftfreq(L)
KX, KY = np.meshgrid(k, k, indexing="ij")
K2 = KX ** 2 + KY ** 2


def mu(phi):
    return (np.log(phi) + 1) / N - np.log(1 - phi) - 1 + CHI * (1 - 2 * phi)


def run(phi0, times, dt=0.05, A=4.0, seed=1):
    rng = np.random.default_rng(seed)
    phi = phi0 + 0.01 * rng.standard_normal((L, L))
    phi = np.clip(phi, 1e-4, 1 - 1e-4)
    denom = 1 + dt * K2 * (A + KAPPA * K2)
    out, t, i = [], 0.0, 0
    for target in times:
        while t < target - 1e-9:
            nl = np.fft.fft2(mu(phi) - A * phi)
            ph = (np.fft.fft2(phi) - dt * K2 * nl) / denom
            phi = np.clip(np.real(np.fft.ifft2(ph)), 1e-6, 1 - 1e-6)
            t += dt
            i += 1
        out.append(phi.copy())
    return out


times = [60, 300, 1500]
rows = [(0.24, "φ₀ = 0.24 (near critical)"), (0.12, "φ₀ = 0.12 (off-critical)")]
light, dense = P.mix(P.fill("nucleolus"), P.surface(), 0.75), P.edge("nucleolus")
cmap = LinearSegmentedColormap.from_list("phi", [light, dense])
fig, axs = plt.subplots(2, 3, figsize=(8.4, 5.9))
for r, (phi0, name) in enumerate(rows):
    snaps = run(phi0, times)
    for c, (tt, s) in enumerate(zip(times, snaps)):
        ax = axs[r, c]
        ax.imshow(s, cmap=cmap, vmin=0.0, vmax=0.75, interpolation="bilinear")
        ax.set_xticks([])
        ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_color(P.muted())
            sp.set_linewidth(0.6)
        ax.set_title(f"t = {tt}", fontsize=8, color=P.ink())
        if c == 0:
            ax.set_ylabel(name, fontsize=8, color=P.ink())
fig.tight_layout()
