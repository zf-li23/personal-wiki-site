# Magnetic tweezers: force calibration and rotation-extension ("hat") curves of DNA (simplified model).
# A 10 kbp DNA (contour length L_c = 3.4 um, bending persistence length A = 50 nm, twist persistence length
# C = 100 nm) tethers a superparamagnetic bead to a surface at 25 C.
# A: the bead is an inverted pendulum of length l (the extension): transverse stiffness F/l, so
#    <dx^2> = kT l / F; extension l(F) from the Marko-Siggia worm-like chain. B: extension against turns n
#    added by rotating the magnets. Twisting stores torque tau = 2 pi n kT C / L_c until it reaches the
#    buckling torque tau_b ~ sqrt(2 A kT F); then each turn converts into a plectoneme loop and shortens the
#    tether by about 2 pi sqrt(A kT / (2F)). Above about 0.5 pN, negative turns melt the duplex instead and the
#    curve stays flat on that side.
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq

import wikibio as bio
from wikibio import charts

P = bio.P
kT, A, C, Lc = 4.11, 50.0, 100.0, 3400.0


def wlc_ext(F):
    g = lambda r: kT / A * (r + 1 / (4 * (1 - r) ** 2) - 0.25) - F
    return Lc * brentq(g, 0, 1 - 1e-9)


fig, axs = plt.subplots(1, 2, figsize=(12, 4.2))
F = np.logspace(-2, 1.3, 100)
ext = np.array([wlc_ext(f) for f in F])
axs[0].loglog(F, np.sqrt(kT * ext / F), color=charts.line("enzyme"), lw=1.8)
for f0 in (0.1, 1, 10):
    l = wlc_ext(f0)
    axs[0].plot(f0, np.sqrt(kT * l / f0), "o", color=charts.line("enzyme"), ms=4)
    axs[0].text(f0 * 1.15, np.sqrt(kT * l / f0) * 1.1, f"{f0:g} pN: l = {l / 1000:.2f} µm", fontsize=7.5, color=P.ink())
charts.style_axes(axs[0], "force F / pN", "transverse fluctuation √⟨δx²⟩ / nm")
charts.title(axs[0], "A   Force from Brownian motion: F = kT l/⟨δx²⟩")

n = np.linspace(-90, 90, 1801)
for f0, tok in ((0.25, "dna"), (0.5, "neutral"), (1.0, "enzyme"), (3.0, "rna")):
    z0 = wlc_ext(f0)
    nb = np.sqrt(2 * A * kT * f0) * Lc / (2 * np.pi * kT * C)
    q = 2 * np.pi * np.sqrt(A * kT / (2 * f0))
    z = z0 - q * np.clip(np.abs(n) - nb, 0, None)
    if f0 > 0.5:
        z = np.where(n < 0, z0, z)       # negative supercoils melt DNA instead of forming plectonemes
    axs[1].plot(n, np.clip(z, 0, None) / 1000, color=charts.line(tok), lw=1.8, label=f"F = {f0:g} pN")
charts.style_axes(axs[1], "turns added n", "extension / µm")
axs[1].legend(fontsize=7.5, frameon=False, loc="lower center")
axs[1].text(-88, 3.25, "negative supercoiling", fontsize=7.5, color=P.muted())
axs[1].text(40, 3.25, "positive supercoiling", fontsize=7.5, color=P.muted())
axs[1].set_ylim(0, 3.45)
charts.title(axs[1], "B   Rotation–extension curves (simplified model)")
fig.tight_layout()
