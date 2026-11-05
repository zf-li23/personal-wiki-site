"""Light-response curves of a sun leaf and a shade leaf from the non-rectangular hyperbola
theta*Ag^2 - (phi*I + Amax)*Ag + phi*I*Amax = 0 (smaller root), A = Ag - Rd. Illustrative parameters:
sun Amax = 25, Rd = 2; shade Amax = 7, Rd = 0.4 (umol m^-2 s^-1); phi = 0.05, theta = 0.8 for both.
A: full range with light saturation; B: low-light range with the light compensation points.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
phi, theta = 0.05, 0.8
leaves = [("Sun leaf", 25.0, 2.0, P.edge("rna")), ("Shade leaf", 7.0, 0.4, P.edge("dna"))]


def net(I, amax, rd):
    b = phi * I + amax
    ag = (b - np.sqrt(b * b - 4 * theta * phi * I * amax)) / (2 * theta)
    return ag - rd


fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 4.2))
I1, I2 = np.linspace(0, 2000, 400), np.linspace(0, 120, 400)
for name, amax, rd, col in leaves:
    a.plot(I1, net(I1, amax, rd), color=col, lw=2, label=name)
    b.plot(I2, net(I2, amax, rd), color=col, lw=2, label=name)
    lcp = I2[np.argmin(np.abs(net(I2, amax, rd)))]
    b.plot([lcp], [0], "o", color=col, ms=6)
    b.annotate(f"compensation\n{lcp:.0f}", (lcp, 0), xytext=(lcp + 4, -1.6 if rd > 1 else 0.9), fontsize=8, color=col)
for ax in (a, b):
    ax.axhline(0, color=P.muted(), lw=0.8)
    ax.set_xlabel("Photon flux density $I$ / µmol m$^{-2}$ s$^{-1}$")
    ax.set_ylabel("Net photosynthesis $A$ / µmol m$^{-2}$ s$^{-1}$")
    ax.legend(frameon=False, fontsize=8, loc="lower right")
    ax.grid(True, alpha=0.3)
a.set_title("A  Full light range", loc="left", fontsize=10)
b.set_title("B  Low light", loc="left", fontsize=10)
b.set_ylim(-2.5, 4.5)
fig.tight_layout()
