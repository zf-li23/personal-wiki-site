# Negative pressure under a curved air-water interface, Psi_p = -2T/r (contact angle 0, T = 0.0728 N/m at
# 20 C), over five orders of magnitude of the radius of curvature, with the structures in which it acts:
# capillary rise in a xylem vessel (r = 20 um: rise only 0.74 m, -0.007 MPa); drained soil pores and the
# field-capacity range; a clay pore (1 um: -0.15 MPa); the menisci in leaf cell walls (0.5 to 0.01 um:
# -0.3 to -15 MPa, after Taiz); and the air-seeding threshold of pit-membrane pores (10-100 nm).
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(18.0, 10.0)
pa = charts.axes_at(ax, (2.4, 1.6, 14.6, 7.6))
T = 0.0728
r = np.logspace(-8.3, -3.7, 300)
pa.plot(r * 1e6, 2 * T / r / 1e6, color=charts.line("dna"), lw=2.0)
marks = [(20e-6, "vessel lumen (20 µm):\ncapillary rise 0.74 m", "plant", (6, 0.0009)),
         (1e-6, "clay pore (1 µm)", "cell_wall", (3.0, 0.35)),
         (0.5e-6, "cell-wall meniscus 0.5 µm", "rna", (0.12, 0.08)),
         (0.05e-6, "0.05 µm", "rna", (0.12, 2.0)),
         (0.01e-6, "0.01 µm: −15 MPa", "rna", (0.022, 40))]
for rr, txt, tok, at in marks:
    y = 2 * T / rr / 1e6
    col = charts.line(tok)
    pa.plot([rr * 1e6], [y], "o", ms=6, color=col)
    pa.annotate(txt, (rr * 1e6, y), at, fontsize=7.5, color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
pa.axvspan(0.01, 0.1, color=P.mix(P.muted(), P.surface(), 0.85), lw=0)
pa.text(0.032, 0.0006, "pit-membrane\npores", fontsize=7.5, color=P.muted(), ha="center")
pa.axhspan(0.01, 0.033, color=P.mix(charts.line("plant"), P.surface(), 0.8), lw=0)
pa.text(150, 0.018, "field capacity", fontsize=7.5, color=P.muted(), ha="right", va="center")
pa.axhline(1.5, color=P.muted(), lw=0.7, ls="--")
pa.text(150, 1.75, "permanent wilting point (1.5 MPa)", fontsize=7.5, color=P.muted(), ha="right")
pa.set_xscale("log")
pa.set_yscale("log")
pa.set_xlim(0.005, 200)
pa.set_ylim(0.0003, 100)
charts.style_axes(pa, "radius of curvature r / µm", "tension −Ψp = 2T/r / MPa")
