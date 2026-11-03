"""Ecological character displacement along a resource axis.

Two species, traits z1, z2, abundances N1, N2. K(z) = exp(-z^2 / (2 sK^2)), sK = 1;
alpha(z, z') = exp(-(z - z')^2 / (2 sa^2)), sa = 0.6. dN_i/dt = r N_i (1 - sum_j alpha(z_i, z_j) N_j / K(z_i)),
dz_i/dt = G d/dz [1 - sum_j alpha(z, z_j) N_j / K(z)] at z = z_i (r = 1, G = 0.02).
Start z = -0.1, 0.1, N = 0.4 each.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio.quant import odeint_rk4

P = bio.P
FS = bio.core.FONT
sK, sa, r, G = 1.0, 0.6, 1.0, 0.02
K = lambda z: np.exp(-z ** 2 / (2 * sK ** 2))  # noqa: E731
A = lambda z, w: np.exp(-(z - w) ** 2 / (2 * sa ** 2))  # noqa: E731


def growth(z, zs, Ns):
    return 1 - sum(A(z, w) * n for w, n in zip(zs, Ns)) / K(z)


def f(_, v):
    z, N = v[:2], v[2:]
    dz = np.array([G * (growth(zi + 1e-5, z, N) - growth(zi - 1e-5, z, N)) / 2e-5 for zi in z])
    dN = np.array([r * N[i] * growth(z[i], z, N) for i in range(2)])
    return np.concatenate([dz, dN])


t = np.linspace(0, 3000, 3001)
Y = odeint_rk4(f, np.array([-0.1, 0.1, 0.4, 0.4]), t)
fig, ax = bio.canvas(30.0, 10.0)
pa = C.axes_at(ax, (2.2, 1.6, 11.5, 6.8))
pa.plot(t, Y[:, 0], color=C.line("dna"), lw=1.9, label="species 1")
pa.plot(t, Y[:, 1], color=C.line("rna"), lw=1.9, label="species 2")
pa.axhline(0, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pa.set_xlim(0, 3000)
C.style_axes(pa, "time", "mean trait z (resource used)")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="center right")
bio.panel(ax, "A", (0.2, 9.8))
bio.label(ax, (2.2, 9.4), "Divergence in sympatry", size="small", bold=True, ha="left")
pb = C.axes_at(ax, (17.5, 1.6, 11.0, 6.8))
zz = np.linspace(-3, 3, 400)
pb.fill_between(zz, K(zz), color=P.muted(), alpha=0.25, lw=0, label="resource K(z)")
for i, tok in ((0, "dna"), (1, "rna")):
    zi, Ni = Y[-1, i], Y[-1, 2 + i]
    pb.plot(zz, Ni * np.exp(-(zz - zi) ** 2 / (2 * (sa / np.sqrt(2)) ** 2)), color=C.line(tok), lw=1.9,
            label=f"species {i + 1} (z = {zi:.2f})")
pb.set_xlim(-3, 3)
pb.set_ylim(0, 1.1)
C.style_axes(pb, "resource axis z", "resource use (schematic)")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (15.7, 9.8))
bio.label(ax, (17.5, 9.4), "Equilibrium positions", size="small", bold=True, ha="left")
