"""The Swift-Hohenberg equation du/dt = eps u - (laplacian + qc^2)^2 u + gamma u^2 - u^3 (qc = 1).
A: growth rate sigma(q) = eps - (qc^2 - q^2)^2 of a Fourier mode of the uniform state u = 0 for
eps = -0.1, 0 and 0.2: for eps > 0 a band of wave numbers around qc is unstable. B: a pattern grown
from small random noise for eps = 0.2, gamma = 0 (stripes, periodic box of 16 wavelengths, time 300).
C: the same with a quadratic term, eps = 0.1, gamma = 1, which breaks the symmetry u -> -u and
selects hexagons of spots. Pseudo-spectral integration, 128 x 128 grid, semi-implicit time steps."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(5)
cmap = LinearSegmentedColormap.from_list("sh", [P.surface(), P.fill("protein"), P.edge("protein")])


def simulate(eps, gamma, n=128, waves=16, T=300.0, dt=0.5):
    L = waves * 2 * np.pi
    k = 2 * np.pi * np.fft.fftfreq(n, d=L / n)
    kx, ky = np.meshgrid(k, k)
    lin = eps - (1 - (kx ** 2 + ky ** 2)) ** 2
    u = 0.01 * rng.standard_normal((n, n))
    uh = np.fft.fft2(u)
    for _ in range(int(T / dt)):
        u = np.real(np.fft.ifft2(uh))
        nh = np.fft.fft2(gamma * u ** 2 - u ** 3)
        uh = (uh + dt * nh) / (1 - dt * lin)
    return np.real(np.fft.ifft2(uh)), L


fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.5), gridspec_kw=dict(width_ratios=(1.15, 1, 1)))
fig.subplots_adjust(wspace=0.3, left=0.06, right=0.98, bottom=0.15, top=0.88)
ax = axs[0]
q = np.linspace(0, 1.6, 300)
for eps, tok in ((-0.1, "neutral"), (0.0, "receptor"), (0.2, "enzyme")):
    ax.plot(q, eps - (1 - q ** 2) ** 2, color=charts.line(tok), lw=1.4, label=rf"$\varepsilon = {eps:g}$")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.axvline(1, color=P.muted(), lw=0.6, ls=":")
ax.set_ylim(-0.6, 0.3)
ax.legend(frameon=False, fontsize=7, loc="upper left")
charts.style_axes(ax, r"wave number $q/q_{\mathrm{c}}$", r"growth rate $\sigma$")
charts.title(ax, "A  dispersion relation")

for ax, (eps, gamma, ttl) in zip(axs[1:], ((0.2, 0.0, r"B  stripes, $\gamma = 0$"), (0.1, 1.0, r"C  hexagons, $\gamma = 1$"))):
    u, L = simulate(eps, gamma)
    ax.imshow(u, cmap=cmap, extent=(0, L / (2 * np.pi), 0, L / (2 * np.pi)), interpolation="bilinear")
    charts.style_axes(ax, r"x / wavelength", None, box=True)
    charts.title(ax, ttl)
