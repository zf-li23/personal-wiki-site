"""Absolute and relative regulation in one-component reaction-diffusion (energy integral A'^2/2 + phi(A) = K).

A: a smooth potential phi with a minimum gives A'' = -omega^2 (A - A0): the steady profile is A0 + C cos(omega x),
whose wavelength 2 pi / omega is fixed by the kinetics. Tissues of length pi / omega and 2 pi / omega therefore
carry one and two half-cycles: the pattern does not scale (absolute regulation). B: a potential with a kink at
A0, phi = omega1 (A - A0) above and -omega2 (A - A0) below, gives two parabolic pieces joined at A = A0; the
crossing point sits at the fixed fraction omega1 / (omega1 + omega2) of the tissue for every length L (here
omega1 = 1, omega2 = 2.5, L = 1 and 2, profiles rescaled by their amplitude): relative regulation of the
boundary.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(22.0, 9.0)
om = np.pi
pa = C.axes_at(ax, (1.6, 1.4, 8.4, 6.2))
for L, tk, ls in ((1.0, "protein", "-"), (2.0, "negative", (0, (4, 2)))):
    xs = np.linspace(0, L, 300)
    pa.plot(xs / L, np.cos(om * xs), color=Q.line_color(tk), lw=1.8, ls=ls, label=f"L = {L:g} (π/ω units)")
pa.axhline(0, color=P.muted(), lw=0.7)
pa.set_xlim(0, 1)
pa.set_ylim(-1.15, 1.35)
C.style_axes(pa, "x / L", "(A − A₀) / C")
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.3, 8.5))
bio.label(ax, (1.6, 8.5), "Smooth potential: fixed wavelength", size="small", bold=True, ha="left")

w1, w2 = 1.0, 2.5
pb = C.axes_at(ax, (13.0, 1.4, 8.4, 6.2))
for L, tk, ls in ((1.0, "protein", "-"), (2.0, "negative", (0, (4, 2)))):
    K = L / (np.sqrt(2) * (1 / w1 + 1 / w2))
    xn, xm = -np.sqrt(2) * K / w2, np.sqrt(2) * K / w1
    xs = np.linspace(xn, xm, 400)
    A = np.where(xs >= 0, np.sqrt(2) * K * xs - w1 * xs**2 / 2, np.sqrt(2) * K * xs + w2 * xs**2 / 2)
    pb.plot((xs - xn) / L, A / np.abs(A).max(), color=Q.line_color(tk), lw=1.8, ls=ls, label=f"L = {L:g}")
pb.axhline(0, color=P.muted(), lw=0.7)
pb.axvline(w1 / (w1 + w2), color=P.edge("highlight"), lw=0.9, ls=(0, (2, 2)))
pb.text(w1 / (w1 + w2) + 0.02, -0.9, "ω₁/(ω₁+ω₂)", color=P.edge("highlight"), fontsize=bio.core.FONT["tiny"])
pb.set_xlim(0, 1)
pb.set_ylim(-1.15, 1.35)
C.style_axes(pb, "x / L", "(A − A₀) / max|A − A₀|")
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (11.8, 8.5))
bio.label(ax, (13.0, 8.5), "Kinked potential: the boundary scales", size="small", bold=True, ha="left")
