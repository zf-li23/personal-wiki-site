# Absorption, circular dichroism and optical rotatory dispersion of one optically active band
# (Gaussian band at 220 nm in energy, width 2800 cm^-1, positive rotational strength).
# CD has the shape of the absorption band; ORD is its Kramers-Kronig transform, here the Dawson function:
# it crosses zero at the band maximum, with a peak on the long-wavelength side and a trough on the short side
# (positive Cotton effect), and its tails extend far outside the band.
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import dawsn

import wikibio as bio
from wikibio import charts

P = bio.P
lam = np.linspace(170, 300, 800)
nu = 1e7 / lam
nu0, w = 1e7 / 220, 2800.0
x = (nu - nu0) / w
absb = np.exp(-x**2)
cd = 0.6 * np.exp(-x**2)
ord_ = 0.6 * (2 / np.sqrt(np.pi)) * dawsn(-x)
fig, ax = plt.subplots(figsize=(7.0, 4.0))
ax.plot(lam, absb, color=P.muted(), lw=1.4, ls="--", label="absorption ε")
ax.plot(lam, cd, color=charts.line("dna"), lw=2.0, label="CD  Δε")
ax.plot(lam, ord_, color=charts.line("rna"), lw=2.0, label="ORD  [Φ]")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.axvline(220, color=P.muted(), lw=0.6, ls=":")
ax.text(223, -0.12, "λmax: ORD = 0", fontsize=8, color=P.muted())
ax.text(245, 0.42, "peak (long λ)", fontsize=8, color=charts.line("rna"))
ax.text(176, -0.45, "trough (short λ)", fontsize=8, color=charts.line("rna"))
ax.legend(fontsize=8, frameon=False, loc="upper right")
charts.style_axes(ax, "wavelength / nm", "signal (rel.)")
charts.title(ax, "Positive Cotton effect")
fig.tight_layout()
