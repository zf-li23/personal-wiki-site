"""Altitude, oxygen and the HIF oxygen sensor.

A: barometric pressure from the standard atmosphere, P = 101.325 (1 - 2.25577e-5 z)^5.25588 kPa, and the inspired O2
partial pressure 0.2095 (P - 6.27 kPa) (air saturated with water vapour at 37 C). The standard atmosphere
underestimates the pressure on the summit of Everest, measured at about 33.7 kPa.
B: steady-state HIF-alpha in a minimal model: constant synthesis k_s and degradation
k_0 + k_max [O2] / (K_m + [O2]) by prolyl hydroxylase (PHD) and VHL. K_m of PHD2 for O2 about 250 uM (in vitro);
k_0 = 0.05 k_max. HIF-alpha relative to its level at 0 uM O2 with the reference PHD activity.
Curves for PHD activity (k_max) 0.5, 1 and 2 times the reference. Shaded: typical range of tissue O2.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
fig, (ax, bx) = plt.subplots(1, 2, figsize=(12.0, 4.5))
z = np.linspace(0, 9000, 300)
pb = 101.325 * (1 - 2.25577e-5 * z) ** 5.25588
pio2 = 0.2095 * (pb - 6.27)
ax.plot(z, pb, color=P.edge("dna"), lw=2.0, label="barometric pressure")
ax.plot(z, pio2, color=P.edge("negative"), lw=2.0, label="inspired $P_{\\mathrm{O_2}}$")
for zz, name in ((0, "sea level"), (3650, "Lhasa"), (5000, "5000 m"), (8849, "Qomolangma")):
    p = 101.325 * (1 - 2.25577e-5 * zz) ** 5.25588
    ax.plot([zz, zz], [0, p], color=P.muted(), lw=0.8, ls=":")
    ax.text(zz + 80, p + 2, f"{name}\n{p / 101.325 * 100:.0f}%", fontsize=7.5, color=P.muted())
ax.set_xlim(0, 9500)
ax.set_ylim(0, 115)
ax.set_xlabel("altitude / m")
ax.set_ylabel("pressure / kPa")
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax.set_title("A  Oxygen partial pressure falls with altitude", loc="left", fontsize=10)

o2 = np.linspace(0, 200, 400)
Km = 250.0
ref = 1 / 0.05
for f, tok, ls in ((0.5, "rna", "--"), (1.0, "enzyme", "-"), (2.0, "plant", ":")):
    hif = 1 / (0.05 + f * o2 / (Km + o2))
    bx.plot(o2, hif / ref, color=P.edge(tok), lw=2.0, ls=ls, label=f"PHD activity $\\times${f:g}")
bx.axvspan(5, 60, color=P.fill("neutral"), alpha=0.3, lw=0)
bx.text(32, 0.9, "typical\ntissue O$_2$", ha="center", fontsize=8, color=P.muted())
bx.set_xlim(0, 200)
bx.set_ylim(0, 1.05)
bx.set_xlabel("O$_2$ concentration / $\\mu$M")
bx.set_ylabel("HIF-$\\alpha$ (relative)")
bx.legend(frameon=False, fontsize=8, loc="upper right")
bx.set_title("B  HIF-$\\alpha$ stabilization as an O$_2$ sensor", loc="left", fontsize=10)
for a in (ax, bx):
    for s in ("top", "right"):
        a.spines[s].set_visible(False)
fig.tight_layout()
