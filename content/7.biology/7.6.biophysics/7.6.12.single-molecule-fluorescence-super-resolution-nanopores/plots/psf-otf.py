# Image formation in a diffraction-limited microscope (emission 600 nm, NA 1.4).
# A: the Airy point spread function [2 J1(v)/v]^2, v = 2 pi NA r / lambda, and its Gaussian approximation with
#    sigma = 0.21 lambda/NA; the first zero lies at 0.61 lambda/NA (Rayleigh distance).
# B: two point sources at the Rayleigh distance and at half of it: the summed image has a 26 % dip at the
#    Rayleigh distance and none at half of it.
# C: the optical transfer function of an aberration-free circular pupil (incoherent imaging),
#    OTF(s) = (2/pi)(arccos s - s sqrt(1 - s^2)), s = k / k_c, which vanishes beyond the cutoff
#    k_c = 2 NA / lambda: the microscope is a low-pass filter.
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import j1

import wikibio as bio
from wikibio import charts

P = bio.P
lam, NA = 600.0, 1.4
r = np.linspace(-800, 800, 2001)


def airy(x):
    v = 2 * np.pi * NA * x / lam
    v = np.where(np.abs(v) < 1e-9, 1e-9, v)
    return (2 * j1(v) / v) ** 2


fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.0))
ax = axs[0]
s = 0.21 * lam / NA
ax.plot(r, airy(r), color=charts.line("dna"), lw=1.8, label="Airy pattern")
ax.plot(r, np.exp(-r**2 / (2 * s**2)), color=charts.line("negative"), lw=1.2, ls="--", label=f"Gaussian, σ = {s:.0f} nm")
d = 0.61 * lam / NA
ax.axvline(d, color=P.muted(), lw=0.7, ls=":")
ax.text(d + 15, 0.6, f"0.61 λ/NA\n= {d:.0f} nm", fontsize=8, color=P.muted())
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(ax, "radial position / nm", "intensity")
charts.title(ax, "A   Point spread function")

ax = axs[1]
for sep, tok, lab in ((d, "dna", "Rayleigh distance"), (0.5 * d, "rna", "half of it")):
    img = airy(r - sep / 2) + airy(r + sep / 2)
    ax.plot(r, img / img.max(), color=charts.line(tok), lw=1.8, label=f"{lab}: {sep:.0f} nm")
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
ax.set_ylim(0, 1.25)
charts.style_axes(ax, "position / nm", "normalized image")
charts.title(ax, "B   Two-point resolution")

ax = axs[2]
kc = 2 * NA / lam * 1000
k = np.linspace(0, 1.2 * kc, 400)
sv = np.clip(k / kc, 0, 1)
otf = 2 / np.pi * (np.arccos(sv) - sv * np.sqrt(1 - sv**2))
ax.plot(k, otf, color=charts.line("dna"), lw=1.8)
ax.axvline(kc, color=P.muted(), lw=0.7, ls=":")
ax.text(kc * 0.62, 0.8, f"cutoff 2NA/λ\n= {kc:.2f} µm⁻¹\n(period {1000 / kc:.0f} nm)", fontsize=8, color=P.ink())
charts.style_axes(ax, "spatial frequency / µm⁻¹", "OTF")
charts.title(ax, "C   Optical transfer function")
fig.tight_layout()
