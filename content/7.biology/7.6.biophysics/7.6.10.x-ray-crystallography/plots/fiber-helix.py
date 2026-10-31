# Fiber diffraction of helices (Cochran-Crick-Vand theory), computed for B-DNA-like parameters.
# Point scatterers (the phosphates) lie on a helix of radius r = 1.0 nm and pitch P = 3.4 nm with u = 10
# units per turn. For a fiber (cylindrical average) the intensity is confined to layer lines Z = l/P and
#     I_l(R) = S_l * sum_{n = l - 10 m} J_n(2 pi R r)^2,
# where only Bessel orders allowed by the selection rule l = n + 10 m contribute and S_l is the strand
# factor. A: a single helix (S_l = 1). B: two identical helices displaced along the axis by 3P/8, as
# the two backbones of B-DNA are (major and minor grooves), S_l = |1 + exp(2 pi i l 3/8)|^2.
# The layer lines are drawn with a Gaussian width of 0.035 nm^-1 and the whole pattern is multiplied by
# exp(-0.3 (R^2 + Z^2)) (nm^-2) to mimic disorder; the display shows I^0.35. Since the first
# maximum of J_n lies at 2 pi R r ~ n + 1, the strongest spot moves outward linearly with l and the pattern forms the helix cross; the meridional
# reflection on l = 10 (R = 0, J_0) reports the 0.34 nm rise per unit.
# C: the strand factor S_l. It vanishes for l = 4, the missing fourth layer line of B-DNA.
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import jv

import wikibio as bio
from wikibio import charts

P = bio.P
ink, muted = P.ink(), P.muted()

r, pitch, u = 1.0, 3.4, 10
delta = 3 / 8
Rmax, lmax = 2.0, 10
R = np.linspace(0, Rmax, 260)
Zgrid = np.linspace(0, (lmax + 0.6) / pitch, 420)


def pattern(strand):
    img = np.zeros((Zgrid.size, R.size))
    for l in range(0, lmax + 1):
        Il = np.zeros_like(R)
        for m in range(-3, 4):
            nn = l - u * m
            Il += jv(nn, 2 * np.pi * R * r) ** 2
        S = abs(1 + np.exp(2j * np.pi * l * delta)) ** 2 if strand == 2 else 1.0
        prof = np.exp(-((Zgrid - l / pitch) ** 2) / (2 * 0.035**2))
        img += S * np.outer(prof, Il)
    RR, ZZ = np.meshgrid(R, Zgrid)
    img *= np.exp(-0.3 * (RR**2 + ZZ**2))
    full = np.hstack([img[:, ::-1], img])
    full = np.vstack([full[::-1], full])
    return full / full.max()


fig, axs = plt.subplots(1, 3, figsize=(13, 4.6), gridspec_kw={"width_ratios": [1, 1, 0.9]})
ext = (-Rmax, Rmax, -Zgrid[-1], Zgrid[-1])
for ax, strands, title in ((axs[0], 1, "A  single helix"), (axs[1], 2, "B  double helix, offset 3P/8")):
    img = pattern(strands)
    ax.imshow(img**0.35, origin="lower", extent=ext, cmap="magma", aspect="auto", vmin=0, vmax=0.75,
              interpolation="bilinear")
    for l in (1, 4, 10):
        ax.text(Rmax + 0.05, l / pitch, f"l = {l}", fontsize=7, color=muted, va="center")
    ax.set_title(title, fontsize=9, loc="left", color=ink)
    charts.style_axes(ax, r"$R$ / nm$^{-1}$", r"$Z$ / nm$^{-1}$", box=True)

ax = axs[2]
ls = np.arange(0, 11)
S = np.abs(1 + np.exp(2j * np.pi * ls * delta)) ** 2
ax.bar(ls, S, color=charts.line("dna"), width=0.6)
ax.bar([4], [0.06], color=charts.line("negative"), width=0.6)
ax.text(4, 0.2, "missing\n4th\nlayer\nline", ha="center", va="bottom", fontsize=7.5, color=ink)
ax.set_xticks(ls)
ax.set_ylim(0, 4.3)
ax.set_title(r"C  strand factor $|1 + \mathrm{e}^{2\pi\mathrm{i}l\cdot 3/8}|^2$", fontsize=9, loc="left",
             color=ink)
charts.style_axes(ax, "layer line l", r"$S_l$")
fig.tight_layout()
