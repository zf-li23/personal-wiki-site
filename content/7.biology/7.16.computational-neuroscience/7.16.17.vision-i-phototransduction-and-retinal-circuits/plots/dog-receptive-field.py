"""Difference-of-Gaussians (DoG) receptive field of a retinal ganglion cell.

W(x, y) = A_c/(2 pi sc^2) exp(-r^2/2sc^2) - A_s/(2 pi ss^2) exp(-r^2/2ss^2),
sc = 0.1 deg, ss = 0.3 deg (center and surround radii), A_s/A_c = 0.85.
A: radial profile (and its two Gaussian components). B: area summation, the response to a centered
spot of radius rho: R(rho) = A_c (1 - exp(-rho^2/2sc^2)) - A_s (1 - exp(-rho^2/2ss^2)).
C: spatial-frequency tuning (2D Fourier transform of W at frequency k, cycles per degree):
W~(k) = A_c exp(-2 pi^2 sc^2 k^2) - A_s exp(-2 pi^2 ss^2 k^2), for three surround strengths.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
sc, ss = 0.1, 0.3
Ac = 1.0


def W(r, As):
    return Ac / (2 * np.pi * sc**2) * np.exp(-r**2 / (2 * sc**2)) - As / (2 * np.pi * ss**2) * np.exp(-r**2 / (2 * ss**2))


fig, axs = plt.subplots(1, 3, figsize=(13, 4.0))
r = np.linspace(-1, 1, 400)
ax = axs[0]
As = 0.85
ax.plot(r, Ac / (2 * np.pi * sc**2) * np.exp(-r**2 / (2 * sc**2)), color=P.edge("positive"), lw=1, ls="--",
        label="center Gaussian")
ax.plot(r, -As / (2 * np.pi * ss**2) * np.exp(-r**2 / (2 * ss**2)), color=P.edge("negative"), lw=1, ls="--",
        label="surround Gaussian")
ax.plot(r, W(r, As), color=P.ink(), lw=2, label="DoG")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_xlabel("Position / deg")
ax.set_ylabel("Sensitivity / deg$^{-2}$")
ax.legend(frameon=False, fontsize=8)
ax.set_title("A  ON-center receptive field", loc="left", fontsize=10)

bx = axs[1]
rho = np.linspace(0, 1.2, 300)
for As, c in ((0.0, P.edge("dna")), (0.5, P.edge("rna")), (0.85, P.edge("positive"))):
    R = Ac * (1 - np.exp(-rho**2 / (2 * sc**2))) - As * (1 - np.exp(-rho**2 / (2 * ss**2)))
    bx.plot(rho, R, color=c, lw=1.8, label=f"A$_s$/A$_c$ = {As}")
bx.set_xlabel("Spot radius / deg")
bx.set_ylabel("Response (relative)")
bx.legend(frameon=False, fontsize=8)
bx.set_title("B  Area summation: an optimal spot size", loc="left", fontsize=10)

cx = axs[2]
k = np.logspace(-1, 1, 300)
for As, c in ((0.0, P.edge("dna")), (0.5, P.edge("rna")), (0.85, P.edge("positive"))):
    Wk = Ac * np.exp(-2 * np.pi**2 * sc**2 * k**2) - As * np.exp(-2 * np.pi**2 * ss**2 * k**2)
    cx.plot(k, Wk, color=c, lw=1.8, label=f"A$_s$/A$_c$ = {As}")
cx.set_xscale("log")
cx.set_xlabel("Spatial frequency / cycles per deg")
cx.set_ylabel("Gain")
cx.legend(frameon=False, fontsize=8, loc="upper right")
cx.set_title("C  Spatial-frequency tuning: low-pass to band-pass", loc="left", fontsize=10)
fig.tight_layout()
