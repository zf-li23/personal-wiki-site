# Why magnetosomes have the size they have.
# A: Neel relaxation time of the magnetization of a magnetite cube of edge d, tau = tau0 exp(K V / kT),
#    tau0 = 1e-9 s, effective anisotropy constant K = 1.1e4 J m^-3, V = d^3, T = 293 K. Below about 25 nm the
#    moment flips by thermal activation faster than a second (superparamagnetic: no permanent moment); the
#    upper limit of a single magnetic domain for equidimensional magnetite is roughly 80-100 nm (larger for
#    elongated crystals); above it, domain walls reduce the net moment. Shaded: the size range of most
#    magnetosome crystals (35-120 nm).
# B: magnetic energy in units of kT in the geomagnetic field (50 uT) for one crystal and for chains of 10 and
#    20 crystals, m = Ms V per crystal with Ms = 4.8e5 A m^-1; a moment is a useful compass when xi = mB/kT
#    exceeds a few.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
kT = 1.380649e-23 * 293
K, Ms, tau0, B = 1.1e4, 4.8e5, 1e-9, 50e-6
d = np.linspace(5e-9, 150e-9, 400)
V = d**3
fig, axs = plt.subplots(1, 2, figsize=(11.4, 4.0))

ax = axs[0]
logtau = np.log10(tau0) + K * V / kT / np.log(10)
ax.plot(d * 1e9, logtau, color=charts.line("mitochondrion"), lw=1.8)
ax.axvspan(35, 120, color=P.fill("mitochondrion"), alpha=0.2, lw=0)
for t, lab in ((1.0, "1 s"), (3.15e7, "1 year"), (3.15e16, "1 billion years")):
    ax.axhline(np.log10(t), color=P.muted(), lw=0.6, ls=":")
    ax.text(147, np.log10(t) + 0.8, lab, fontsize=6.8, ha="right", color=P.muted())
ax.axvline(90, color=charts.line("rna"), lw=0.9, ls="--")
ax.text(92, -6, "multidomain\nabove ~90 nm", fontsize=6.8, color=charts.line("rna"))
ax.text(6, 4, "super-\npara-\nmagnetic", fontsize=6.8, color=P.ink())
ax.text(45, 30, "magnetosomes", fontsize=6.8, color=P.ink())
ax.set_ylim(-10, 40)
ax.set_xlim(5, 150)
charts.style_axes(ax, "crystal edge d / nm", "log₁₀ (relaxation time / s)")
charts.title(ax, "A   The single-domain window")

ax = axs[1]
for n, tok in ((1, "neutral"), (10, "enzyme"), (20, "dna")):
    ax.semilogy(d * 1e9, n * Ms * V * B / kT, color=charts.line(tok), lw=1.7, label=f"{n} crystal{'s' if n > 1 else ''}")
ax.axhline(1, color=P.muted(), lw=0.6, ls=":")
ax.axvspan(35, 120, color=P.fill("mitochondrion"), alpha=0.2, lw=0)
ax.text(8, 1.3, "mB = kBT", fontsize=6.8, color=P.muted())
ax.legend(fontsize=7, frameon=False, loc="upper left")
ax.set_xlim(5, 150)
charts.style_axes(ax, "crystal edge d / nm", "mB / kBT in 50 μT")
charts.title(ax, "B   A chain makes a compass")
fig.tight_layout()
