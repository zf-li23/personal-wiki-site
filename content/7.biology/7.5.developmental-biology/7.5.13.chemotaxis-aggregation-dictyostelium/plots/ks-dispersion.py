"""Linear instability of chemotactic aggregation.

A: Keller-Segel model linearized about uniform cells a0 and attractant rho0: sigma^2 + A sigma + B = 0 with
A = (mu0 + nu0) k^2 - alpha0 and B = mu0 nu0 k^4 - (mu0 alpha0 + kappa0 f0) k^2 (mu0 = 1 cell motility,
nu0 = 1 attractant diffusion, alpha0 = -1 net attractant decay). The growth rate (larger root) is shown for
Delta = mu0 alpha0 + kappa0 f0 = -0.2, 0.1, 0.4 and 1: the band of unstable wave numbers starts at k = 0, i.e. at
infinite wavelength, and the fastest mode k^2 = Delta / (2 mu0 nu0) moves out as Delta grows.
B: a chemotaxis-augmented Turing system: two attractants with kinetics alpha = [[2, -3], [5, -5]], diffusion
nu1 = 1, nu2 = 4, cells producing both (f / mu = 1) and moving up the gradient of the first only (kappa1 = 1,
kappa2 = 0), mu = 1. Without chemotaxis the chemical system is stable at every k (dashed); with it, a band of
finite wave numbers becomes unstable, barely for kappa1 = 1 (the example is just past threshold: 7 > 2 sqrt(12))
and clearly for kappa1 = 1.5: chemotaxis realizes a latent diffusive instability.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(24.0, 9.2)
mu0, nu0, al0 = 1.0, 1.0, -1.0
k = np.linspace(0, 1.2, 500)
pa = C.axes_at(ax, (1.8, 1.4, 8.8, 6.4))
for D, tk in ((-0.2, "neutral"), (0.1, "na"), (0.4, "protein"), (1.0, "negative")):
    A = (mu0 + nu0) * k**2 - al0
    B = mu0 * nu0 * k**4 - D * k**2
    s = (-A + np.sqrt(A * A - 4 * B)) / 2
    pa.plot(k, s, color=Q.line_color(tk), lw=1.8, label=f"Δ = {D:g}")
pa.axhline(0, color=P.muted(), lw=0.8)
pa.set_xlim(0, 1.2)
pa.set_ylim(-0.25, 0.25)
C.style_axes(pa, "wave number k", "growth rate σ")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "A", (0.3, 8.6))
bio.label(ax, (1.8, 8.6), "Keller-Segel: unstable from k = 0", size="small", bold=True, ha="left")

al = np.array([[2.0, -3.0], [5.0, -5.0]])
nu = np.array([1.0, 4.0])
f = np.array([1.0, 1.0])
kap = np.array([1.0, 0.0])
mu = 1.0
k = np.linspace(0, 2.0, 600)


def rate(kk, chem=True, k1=1.0):
    if not chem:
        M = al - np.diag(nu) * kk**2
        return np.linalg.eigvals(M).real.max()
    M = np.zeros((3, 3))
    M[:2, :2] = al - np.diag(nu) * kk**2
    M[:2, 2] = f
    M[2, :2] = np.array([k1, 0.0]) * kk**2
    M[2, 2] = -mu * kk**2
    ev = np.linalg.eigvals(M).real
    return ev.max()


pb = C.axes_at(ax, (14.2, 1.4, 8.8, 6.4))
pb.plot(k, [rate(x, False) for x in k], color=P.muted(), lw=1.4, ls=(0, (4, 2)), label="chemicals alone")
pb.plot(k[1:], [rate(x) for x in k[1:]], color=Q.line_color("protein"), lw=1.8, label="with chemotaxis, κ₁ = 1")
pb.plot(k[1:], [rate(x, k1=1.5) for x in k[1:]], color=Q.line_color("negative"), lw=1.8, label="with chemotaxis, κ₁ = 1.5")
pb.axhline(0, color=P.muted(), lw=0.8)
pb.set_xlim(0, 2.0)
pb.set_ylim(-1.2, 0.45)
C.style_axes(pb, "wave number k", "largest growth rate")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "B", (12.7, 8.6))
bio.label(ax, (14.2, 8.6), "Chemotaxis creates a finite wavelength", size="small", bold=True, ha="left")
