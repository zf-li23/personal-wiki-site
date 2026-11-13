"""Water against air as a respiratory medium: ratios of physical properties (water / air) at 20 C and
101.3 kPa, fresh water in equilibrium with air (standard handbook values: CRC Handbook of Chemistry and
Physics). O2 concentration 0.284 mmol/L in water and 8.71 mmol/L in air; O2 diffusion coefficient
2.0e-9 and 2.0e-5 m^2/s; Krogh's diffusion constant K = D * (dc/dp), the product of the diffusion
coefficient and the capacitance; density 998 and 1.204 kg/m^3; dynamic viscosity 1.00e-3 and
1.81e-5 Pa s; volumetric heat capacity 4.18 MJ and 1.21 kJ per m^3 per K.

Bars to the left of 1 are properties in which water is poorer than air (less oxygen, slower
diffusion); bars to the right are those in which water is costlier to move or drains more heat.
"""

import numpy as np
from matplotlib.patches import Rectangle

import wikibio as bio
from wikibio import quant

P = bio.P
ROWS = [("O$_2$ concentration", 0.284 / 8.71),
        ("O$_2$ diffusion coefficient", 2.0e-9 / 2.0e-5),
        ("Krogh diffusion constant", (2.0e-9 * 0.284 / 21.2) / (2.0e-5 * 8.71 / 21.2)),
        ("density", 998 / 1.204),
        ("dynamic viscosity", 1.00e-3 / 1.81e-5),
        ("heat capacity per volume", 4.18e6 / 1.21e3)]

fig, ax = bio.canvas(20.0, 8.6)
p = quant.Plot(ax, (6.4, 1.4, 12.6, 6.0), xlim=(1e-6, 1e4), ylim=(0, len(ROWS)), xlog=True,
               xlabel="ratio water / air (logarithmic)", frame=None,
               xticks=[(1e-6, "10$^{-6}$"), (1e-4, "10$^{-4}$"), (1e-2, "10$^{-2}$"), (1, "1"), (1e2, "10$^{2}$"), (1e4, "10$^{4}$")])
ax.plot([p.X(1e-6), p.X(1e4)], [1.4, 1.4], color=P.muted(), lw=0.8, zorder=6)
p.vline(1, token="ink", dashed=False, lw=1.0)
for i, (name, r) in enumerate(ROWS):
    y = len(ROWS) - i - 0.5
    tok = "dna" if r < 1 else "negative"
    x0, x1 = sorted((float(p.X(1)), float(p.X(r))))
    yc = float(p.Y(y))
    ax.add_patch(Rectangle((x0, yc - 0.32), x1 - x0, 0.64, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.7, zorder=7))
    bio.label(ax, (6.2, yc), name, size="small", ha="right")
    v = 1 / r if r < 1 else r
    v = float(f"{v:.2g}")
    txt = f"1/{v:,.0f}" if r < 1 else f"{v:,.0f}×"
    if r < 1:
        bio.label(ax, (x0 + 0.15, yc), txt, size="tiny", ha="left", color=P.on_fill())
    else:
        bio.label(ax, (x1 + 0.12, yc), txt, size="tiny", ha="left")
bio.label(ax, (float(p.X(1e-3)), 7.95), "water is poorer", size="small", color=quant.line_color("dna"))
bio.label(ax, (float(p.X(1e2)), 7.95), "water is costlier", size="small", color=quant.line_color("negative"))
