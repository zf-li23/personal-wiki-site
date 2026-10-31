# The Patterson function of two-dimensional toy crystals.
# A: three atoms (Z = 30, 16, 8) in a 20 x 20 A cell of plane group p1, shown by their Fourier
#    synthesis (B = 6 A^2, d_min = 1.2 A).
# B: its Patterson function P(u) = (1/A) sum |F(h)|^2 cos(2 pi h.u), computed from the intensities alone.
#    It has N(N - 1) = 6 cross peaks at the interatomic vectors r_j - r_k (labelled by the pair) and the
#    origin peak; peak heights are proportional to Z_j Z_k, and the map is centrosymmetric.
# C: a heavy atom (Z = 80) and 40 light atoms (Z = 6, random positions) in plane group p2, in which
#    every atom at r has a partner at -r. The Patterson of the intensities is dominated by the
#    heavy-atom self-vector at 2 r_H (a Harker peak, marked), from which r_H follows; the light-atom
#    vectors form a low background. In B and C the mean intensity is subtracted from |F|^2 before the
#    synthesis, which lowers the origin peak (seen in the corners) and leaves the cross peaks.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
ink, muted = P.ink(), P.muted()
hl = charts.line("highlight")

cell = 20.0
hmax = 17
hh = np.arange(-hmax, hmax + 1)
H, K = np.meshgrid(hh, hh, indexing="ij")
s2 = (H**2 + K**2) / cell**2
keep = s2 <= 1 / 1.2**2
ng = 140
g = np.arange(ng) / ng
E = np.exp(-2j * np.pi * np.outer(hh, g))         # (h, x)


def sf(frac, Z, B=6.0):
    F = np.zeros(H.shape, complex)
    for (fx, fy), z in zip(frac, Z):
        F += z * np.exp(2j * np.pi * (H * fx + K * fy))
    return np.where(keep, F * np.exp(-B / 4 * s2), 0)


def synth(C):
    return np.real(E.T @ C @ E).T


def patterson(F):
    I = np.abs(F) ** 2
    I = np.where(keep, I - I[keep].mean(), 0)
    return synth(I)


fracA = np.array([[0.22, 0.30], [0.58, 0.40], [0.40, 0.72]])
ZA = np.array([30, 16, 8])
FA = sf(fracA, ZA)
rhoA = synth(FA)
PA = patterson(FA)

rng = np.random.default_rng(0)
light = rng.uniform(0, 1, size=(20, 2))
rH = np.array([0.14, 0.21])
fracC = np.vstack([rH, -rH, light, -light]) % 1
ZC = np.array([80, 80] + [6] * 40)
PC = patterson(sf(fracC, ZC))

fig, axs = plt.subplots(1, 3, figsize=(13, 4.3))
ext = (0, cell, 0, cell)
kw = dict(origin="lower", extent=ext, interpolation="bilinear")

ax = axs[0]
r = rhoA / rhoA.max()
ax.imshow(np.ma.masked_less(r, 0.05), cmap="Blues", vmin=-0.3, vmax=1, **kw)
for (fx, fy), z, name in zip(fracA, ZA, "123"):
    ax.text(fx * cell + 0.9, fy * cell + 0.9, f"{name} (Z = {z})", fontsize=8, color=ink)
ax.set_title("A  structure (p1)", fontsize=9, loc="left", color=ink)
charts.style_axes(ax, "x / Å", "y / Å", box=True)

ax = axs[1]
p = PA / PA.max()
ax.imshow(np.ma.masked_less(p, 0.06), cmap="Oranges", vmin=-0.3, vmax=1, **kw)
for j in range(3):
    for k in range(3):
        if j != k:
            u = ((fracA[j] - fracA[k]) % 1) * cell
            ax.text(u[0] + 0.6, u[1] + 0.6, f"{j + 1}{k + 1}", fontsize=7.5, color=ink)
ax.set_title("B  Patterson of A", fontsize=9, loc="left", color=ink)
charts.style_axes(ax, "u / Å", "v / Å", box=True)

ax = axs[2]
p = PC / PC.max()
ax.imshow(np.ma.masked_less(p, 0.08), cmap="Oranges", vmin=-0.3, vmax=1, **kw)
u = ((2 * rH) % 1) * cell
ax.plot(*u, "o", ms=16, mfc="none", mec=hl, mew=1.6)
ax.text(u[0] + 1.3, u[1] - 0.4, r"Harker peak at $2\boldsymbol{r}_{\mathrm{H}}$", fontsize=8, color=hl)
u2 = ((-2 * rH) % 1) * cell
ax.plot(*u2, "o", ms=16, mfc="none", mec=hl, mew=1.6)
ax.set_title("C  heavy atom + 40 light atoms (p2)", fontsize=9, loc="left", color=ink)
charts.style_axes(ax, "u / Å", "v / Å", box=True)
fig.tight_layout()
