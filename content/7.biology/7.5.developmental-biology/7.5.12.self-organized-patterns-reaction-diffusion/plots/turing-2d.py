"""Two-dimensional Gierer-Meinhardt patterns: spots or stripes depending on activator saturation.

Model: a_t = eps2 lap a + a^2 / (h (1 + kappa a^2)) - a, tau h_t = D lap h + a^2 - h, with eps2 = 0.02, D = 1,
tau = 0.3, on a periodic 20 x 20 square (80 x 80 grid, semi-implicit Fourier time stepping), started from the
uniform state with 5 % noise. Without strong saturation (kappa = 0.1) the activator forms isolated peaks on a
roughly hexagonal lattice; with stronger saturation (kappa = 0.45) the peaks cannot grow tall, the activated
regions spread sideways and form stripes and labyrinths. The spacing is set by the kinetics and the diffusion
coefficients, not by the size of the square.
"""

import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import wikibio as bio
from wikibio import charts as C

P = bio.P


def run(kap, n=80, L=20.0, e2=0.02, D=1.0, tau=0.3, T=240.0, dt=0.04):
    k = 2 * np.pi * np.fft.fftfreq(n, d=L / n)
    K2 = k[:, None] ** 2 + k[None, :] ** 2
    a0 = 1.0
    for _ in range(300):
        a0 = 0.5 * a0 + 0.5 / (1 + kap * a0 * a0)
    rng = np.random.default_rng(1)
    a = a0 * (1 + 0.05 * rng.standard_normal((n, n)))
    h = np.full((n, n), a0 * a0)
    Ea = 1 / (1 + dt * e2 * K2)
    Eh = 1 / (1 + dt * D / tau * K2)
    for _ in range(int(T / dt)):
        f = a * a / (h * (1 + kap * a * a)) - a
        g = (a * a - h) / tau
        a = np.fft.ifft2(np.fft.fft2(a + dt * f) * Ea).real
        h = np.maximum(np.fft.ifft2(np.fft.fft2(h + dt * g) * Eh).real, 1e-6)
    return a


cmap = LinearSegmentedColormap.from_list("act", [P.surface(), P.fill("protein")])
fig, ax = bio.canvas(20.0, 11.0)
for i, (kap, title) in enumerate(((0.1, "κ = 0.1: spots"), (0.45, "κ = 0.45: stripes"))):
    a = run(kap)
    sub = C.axes_at(ax, (1.0 + 9.6 * i, 1.0, 8.4, 8.4))
    sub.imshow(a, cmap=cmap, origin="lower", extent=[0, 20, 0, 20], interpolation="bilinear")
    sub.set_xticks([])
    sub.set_yticks([])
    for sp in sub.spines.values():
        sp.set_color(P.muted())
    bio.label(ax, (1.0 + 9.6 * i, 10.2), title, size="small", bold=True, ha="left")
