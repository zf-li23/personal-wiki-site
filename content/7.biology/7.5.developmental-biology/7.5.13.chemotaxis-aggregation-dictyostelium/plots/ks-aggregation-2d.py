"""Chemotactic aggregation in two dimensions (Keller-Segel model with volume filling).

Cells a and attractant rho on a periodic 20 x 20 square (64 x 64 grid):
a_t = mu lap a - div(kappa a (1 - a / a_max) grad rho),  rho_t = nu lap rho + a - rho,
with mu = 0.1, kappa = 1, nu = 1, a_max = 4, started from a = 1 with 5 % noise. Here Delta = mu alpha0 + kappa_eff f0
= -0.1 + 0.75 > 0, so the uniform state is unstable. Small clusters appear first, attract the cells around them
and coarsen into a few aggregates whose density is capped at a_max: the volume-filling term (cells cannot pile
up indefinitely) prevents the finite-time collapse of the classical model. Upwind fluxes keep the density
positive; time steps are semi-implicit in Fourier space.
"""

import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import wikibio as bio
from wikibio import charts as C

P = bio.P


def flux(a, r, kap, amax, dx, ax_):
    ap = np.roll(a, -1, ax_)
    g = (np.roll(r, -1, ax_) - r) / dx
    up = np.where(g > 0, a, ap)
    dn = np.where(g > 0, ap, a)
    return kap * g * up * np.clip(1 - dn / amax, 0, None)


def run(n=64, L=20.0, mu=0.1, kap=1.0, nu=1.0, amax=4.0, dt=0.005, times=(6.0, 15.0, 40.0)):
    dx = L / n
    k = 2 * np.pi * np.fft.fftfreq(n, d=dx)
    K2 = k[:, None] ** 2 + k[None, :] ** 2
    rng = np.random.default_rng(0)
    a = 1 + 0.05 * rng.standard_normal((n, n))
    r = a.copy()
    Ea = 1 / (1 + dt * mu * K2)
    Er = 1 / (1 + dt * (nu * K2 + 1))
    out = []
    steps = [int(round(t / dt)) for t in times]
    for i in range(1, steps[-1] + 1):
        Fx = flux(a, r, kap, amax, dx, 0)
        Fy = flux(a, r, kap, amax, dx, 1)
        div = (Fx - np.roll(Fx, 1, 0)) / dx + (Fy - np.roll(Fy, 1, 1)) / dx
        a = np.fft.ifft2(np.fft.fft2(a - dt * div) * Ea).real
        r = np.fft.ifft2(np.fft.fft2(r + dt * a) * Er).real
        if i in steps:
            out.append(a.copy())
    return times, out


times, snaps = run()
cmap = LinearSegmentedColormap.from_list("cells", [P.surface(), P.fill("animal")])
fig, ax = bio.canvas(28.0, 10.6)
for i, (t, a) in enumerate(zip(times, snaps)):
    sub = C.axes_at(ax, (0.8 + 9.2 * i, 1.0, 8.4, 8.4))
    sub.imshow(a, cmap=cmap, origin="lower", extent=[0, 20, 0, 20], vmin=0, vmax=4, interpolation="bilinear")
    sub.set_xticks([])
    sub.set_yticks([])
    for sp in sub.spines.values():
        sp.set_color(P.muted())
    bio.label(ax, (0.8 + 9.2 * i, 9.9), f"t = {t:g}: max density {a.max():.2f}", size="small", bold=True, ha="left")
