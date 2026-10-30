"""The chamber model of condensation number in the growing limb bud (Section 32.5.2, after Percus and Childress).

A: a fibronectin-like morphogen A in a rectangular chamber of length a (proximo-distal) and width b
(antero-posterior), no flux across the sides y = 0, b, fluxes M0 and M1 at x = 0 and x = a, linearized kinetics
A_t = r (A - A0) + D lap A. The separated steady solution has n transverse half-cycles with
(n pi / b)^2 = r / D + lambda^2 / a^2, lambda = ln(M1 / M0). Curves: the real n(a) for r b^2 / D = pi^2 and
lambda = 4 (flux boundaries) and for a closed (Neumann) chamber, (n pi / b)^2 = r / D - pi^2 / a^2, with
r b^2 / D = 25 pi^2; steps: the largest whole number of half-cycles that fits. B: an inhibitor I that blocks the
channels of cell-to-cell transfer lowers the effective diffusivity, D / D0 = (K + A) / (K (1 + K_I I) + A)
(here A / K = 1), and increases n at fixed a.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(24.0, 9.5)
a = np.linspace(0.18, 3.0, 400)
lam = 4.0
n_flux = np.sqrt(np.pi**2 + lam**2 / a**2) / np.pi
q = 25 * np.pi**2 - np.pi**2 / a**2
n_neu = np.where(q > 0, np.sqrt(np.clip(q, 0, None)) / np.pi, np.nan)
pa = C.axes_at(ax, (1.8, 1.5, 8.6, 6.6))
pa.plot(a, n_flux, color=Q.line_color("phalanges"), lw=1.6, label="flux boundaries")
pa.plot(a, np.floor(n_flux), color=Q.line_color("phalanges"), lw=1.0, ls=(0, (2, 1.5)))
pa.plot(a, n_neu, color=Q.line_color("channel"), lw=1.6, label="closed chamber")
pa.plot(a, np.floor(n_neu), color=Q.line_color("channel"), lw=1.0, ls=(0, (2, 1.5)))
pa.set_xlim(3.0, 0.18)
pa.set_ylim(0, 7.5)
C.style_axes(pa, "chamber length a / b  (decreasing with time →)", "transverse half-cycles n")
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
for txt, xx, yy in (("stylopod", 2.6, 1.25), ("zeugopod", 1.15, 2.2), ("autopod", 0.75, 5.6)):
    pa.text(xx, yy, txt, fontsize=bio.core.FONT["tiny"], color=P.muted())
bio.panel(ax, "A", (0.3, 9.3))
bio.label(ax, (1.8, 9.1), "Number of condensations against chamber length", size="small", bold=True, ha="left", va="top")

pb = C.axes_at(ax, (14.0, 1.5, 8.6, 6.6))
I = np.linspace(0, 6, 200)
for KI, tk in ((0.5, "highlight"), (1.0, "drug"), (2.0, "protein")):
    Dr = 2.0 / (1 + KI * I + 1)
    n = np.sqrt(np.pi**2 / Dr + lam**2 / 1.0**2) / np.pi
    pb.plot(I, n, color=Q.line_color(tk), lw=1.6, label=f"$K_I K$ = {KI:g}")
pb.set_xlim(0, 6)
C.style_axes(pb, "inhibitor (hyaluronate) I / K", "n at a = b")
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (12.5, 9.3))
bio.label(ax, (14.0, 9.1), "Channel blocking lowers D and raises n", size="small", bold=True, ha="left", va="top")
