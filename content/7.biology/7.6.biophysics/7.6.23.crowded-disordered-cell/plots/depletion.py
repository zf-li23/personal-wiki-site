"""Depletion attraction (Asakura-Oosawa model). Two spheres of radius R = 1 um in a solution of
small crowders of radius r at number density n: the crowders are excluded from a shell of
thickness r around each sphere; when the shells overlap, the volume available to the crowders
grows by the overlap V_ov(D) and the free energy falls by Pi V_ov, with Pi = n kB T.
A: interaction free energy against the surface separation h = D - 2R for r = 2 nm and n = 0.5, 1
and 2 mM. B: depletion force F = -dW/dD; at h = r, F is close to pi n kB T r R, about 15 pN at
1 mM. C: contact free energy W(0) = (3/2) phi (R/r) kB T (for R >> r) at a fixed crowder volume
fraction phi = 0.1, against the size ratio: at the same volume fraction, small crowders attract
large particles far more strongly; between two proteins of the crowders' size the attraction is
only a fraction of kB T."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
kT, NA = 4.1e-21, 6.022e23
R, r = 1e-6, 2e-9


def Vov(D, R, r):
    return np.where(D < 2 * (R + r), 2 * np.pi / 3 * (R + r - D / 2) ** 2 * (2 * R + 2 * r + D / 2), 0.0)


fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.2))
fig.subplots_adjust(wspace=0.4, left=0.07, right=0.97, bottom=0.18, top=0.87)
h = np.linspace(0, 2.6 * r, 400)
D = 2 * R + h
for cm, tok in ((0.5, "dna"), (1.0, "bacterium"), (2.0, "blood")):
    Pi = cm * NA * kT  # cm mM = cm mol/m^3
    W = -Pi * Vov(D, R, r)
    F = Pi * np.pi * np.where(D < 2 * (R + r), (R + r) ** 2 - D**2 / 4, 0.0)
    axs[0].plot(h * 1e9, W / kT, color=charts.line(tok), lw=1.7, label=f"{cm:g} mM")
    axs[1].plot(h * 1e9, F * 1e12, color=charts.line(tok), lw=1.7, label=f"{cm:g} mM")
axs[1].axvline(2.0, color=P.muted(), lw=0.6, ls=":")
axs[0].legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(axs[0], "surface separation h / nm", r"W / $k_{\mathrm{B}}T$")
charts.title(axs[0], r"A  Potential ($R = 1\,\mu$m, $r = 2$ nm)")
charts.style_axes(axs[1], "surface separation h / nm", "attractive force / pN")
charts.title(axs[1], "B  Force")

ax = axs[2]
ratio = np.logspace(0, 3, 200)
phi = 0.1
Wc = []
for q in ratio:
    rr = 1.0
    RR = q
    n = phi / (4 / 3 * np.pi * rr**3)
    Wc.append(n * Vov(2 * RR, RR, rr))
ax.plot(ratio, Wc, color=charts.line("blood"), lw=1.8, label="exact overlap")
ax.plot(ratio, 1.5 * phi * ratio, color=P.muted(), lw=1.0, ls="--", label=r"$\frac{3}{2}\varphi R/r$")
ax.axhline(1, color=P.muted(), lw=0.6, ls=":")
ax.set_xscale("log"); ax.set_yscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "size ratio R / r", r"contact $-W$ / $k_{\mathrm{B}}T$")
charts.title(ax, r"C  At fixed $\varphi = 0.1$")
