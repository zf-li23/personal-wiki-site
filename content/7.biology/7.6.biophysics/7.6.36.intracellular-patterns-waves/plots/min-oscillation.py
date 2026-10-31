"""Pole-to-pole oscillation of the Min proteins in a one-dimensional reaction-diffusion model
(Howard, Rutenberg and de Vet, 2001). Cytoplasmic MinD (D) binds the membrane (d) at rate
s1 D/(1 + s1' e) and is released by membrane MinE (e) at rate s2 e d; cytoplasmic MinE (E) binds
to the membrane where MinD is (s3 D E) and is released at rate s4 e/(1 + s4' D); D_D = 0.28 and
D_E = 0.6 um^2/s, s1 = 20 /s, s1' = 0.028 um, s2 = 0.0063 um/s, s3 = 0.04 um/s, s4 = 0.8 /s,
s4' = 0.027 um (all rates and diffusion coefficients then multiplied by 2.5, which only speeds up
the dynamics), mean densities 1500 MinD and 85 MinE per um, no-flux ends. A: kymograph of membrane
MinD in a 2.5-um cell: it accumulates at one pole, then the other. B: membrane MinD averaged over
400 s (MinC rides on it) along the cell, lowest at midcell, where the FtsZ ring can form. C: in a
filamentous cell of 8 um the pole-to-pole pattern is lost; bands of MinD form in the interior and
travel over a few micrometers, the beginning of the multiple bands observed in long cells."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import wikibio as bio
from wikibio import charts

P = bio.P
cmap = LinearSegmentedColormap.from_list("mind", [P.surface(), P.fill("dna"), P.edge("dna")])
K = 2.5   # all rates and diffusion coefficients scaled by K: same patterns, K times faster
DD, DE = 0.28 * K, 0.6 * K
s1, s1p, s2, s3, s4, s4p = 20.0 * K, 0.028, 0.0063 * K, 0.04 * K, 0.8 * K, 0.027


def run(L, T, dx=0.1, dt=0.003, Dm=1500.0, Em=85.0, seed=0):
    n = int(round(L / dx))
    rng = np.random.default_rng(seed)
    D = Dm * 0.5 * (1 + 0.05 * rng.random(n))
    d = Dm * 0.5 * (1 + 0.05 * rng.random(n))
    E = np.full(n, Em * 0.5)
    e = Em * 0.5 * (1 + 0.3 * np.linspace(-1, 1, n))

    def lap(u):
        out = np.empty_like(u)
        out[1:-1] = u[2:] - 2 * u[1:-1] + u[:-2]
        out[0] = u[1] - u[0]
        out[-1] = u[-2] - u[-1]
        return out / dx ** 2

    every = int(round(0.5 / dt))
    rec = []
    for i in range(int(T / dt)):
        a = s1 * D / (1 + s1p * e)
        b = s2 * e * d
        c = s3 * D * E
        f = s4 * e / (1 + s4p * D)
        D += dt * (DD * lap(D) - a + b)
        d += dt * (a - b)
        E += dt * (DE * lap(E) - c + f)
        e += dt * (c - f)
        if i % every == 0:
            rec.append(d.copy())
    x = (np.arange(n) + 0.5) * dx
    return x, np.array(rec)


fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.4), gridspec_kw=dict(width_ratios=(1, 0.8, 1.3)))
fig.subplots_adjust(wspace=0.4, left=0.06, right=0.97, bottom=0.16, top=0.88)

x, r_all = run(2.5, 700)
r = r_all[-400:]
ax = axs[0]
ax.imshow(r, aspect="auto", origin="lower", extent=(0, 2.5, 0, r.shape[0] / 2), cmap=cmap, interpolation="bilinear")
charts.style_axes(ax, r"position along cell / $\mu$m", "time / s", box=True)
charts.title(ax, "A  membrane MinD, 2.5 µm cell")

ax = axs[1]
prof = r_all[600:].mean(axis=0)
ax.plot(x, prof / prof.max(), color=charts.line("dna"), lw=1.6)
ax.axvline(1.25, color=P.muted(), lw=0.6, ls=":")
ax.set_ylim(0, 1.05)
charts.style_axes(ax, r"position / $\mu$m", "time-averaged MinD (rel.)")
charts.title(ax, "B  time average")

x8, r8 = run(8.0, 800, seed=2)
r8 = r8[-400:]
ax = axs[2]
ax.imshow(r8, aspect="auto", origin="lower", extent=(0, 8, 0, r8.shape[0] / 2), cmap=cmap, interpolation="bilinear")
charts.style_axes(ax, r"position along filament / $\mu$m", None, box=True)
charts.title(ax, "C  filamentous cell, 8 µm")
