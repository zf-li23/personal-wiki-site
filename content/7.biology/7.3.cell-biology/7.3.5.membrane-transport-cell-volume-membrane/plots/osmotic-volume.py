"""Cell volume and osmolarity.

A: osmotic fragility of erythrocytes. Each cell follows the Boyle-van 't Hoff relation
V/V0 = b + (1 - b) Pi0/Pi with osmotically inactive fraction b = 0.4 and lyses when its volume reaches
that of a sphere with its surface area (critical volume V_c/V0: normal cells mean 1.7, spherocytes 1.25,
both with 6 % cell-to-cell variation). NaCl concentration is taken proportional to osmolarity
(0.9 % = 290 mOsm/L).
B: regulatory volume decrease. A cell in 290 mOsm/L medium (b = 0.3) is transferred at t = 1 min to
200 mOsm/L. Water equilibrates within seconds; volume-activated K+ and Cl- channels then release KCl
at a rate proportional to the excess of volume above a set point (1.05 V0). Dashed: without the channels
the cell stays swollen at the Boyle-van 't Hoff volume.
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.stats import norm
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(22.0, 8.0)

# ---- A: fragility curves
bio.panel(ax, "A", (0.1, 7.8))
pa = charts.axes_at(ax, (1.7, 1.3, 8.2, 5.8))
b = 0.4
nacl = np.linspace(0.2, 0.9, 400)
ratio = nacl / 0.9  # Pi / Pi0
vol = b + (1 - b) / ratio
for vc, tok, name in ((1.7, "dna", "normal (biconcave)"), (1.25, "negative", "hereditary spherocytosis")):
    lysed = norm.cdf(vol, loc=vc, scale=0.06 * vc) * 100
    pa.plot(nacl, lysed, color=charts.line(tok), lw=2.0, label=name)
pa.set_xlim(0.9, 0.2)
pa.set_ylim(0, 102)
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(pa, "NaCl / % (w/v)", "hemolysis / %")
charts.title(pa, "Osmotic fragility test (model)")

# ---- B: regulatory volume decrease
bio.panel(ax, "B", (11.3, 7.8))
pb = charts.axes_at(ax, (12.9, 1.3, 7.6, 5.8))
bb = 0.3
S0 = 290 * (1 - bb)


def rhs(t, y, ks):
    V, S = y
    pio = 290.0 if t < 1 else 200.0
    dV = 20.0 * (S / (V - bb) - pio) / 290  # water: fast (seconds)
    dS = -ks * max(V - 1.05, 0.0)
    return [dV, dS]


t = np.linspace(0, 20, 2000)
for ks, tok, ls, name in ((40.0, "dna", "-", "with volume-activated K⁺ and Cl⁻ channels"), (0.0, "neutral", (0, (4, 2)), "channels blocked")):
    s = solve_ivp(rhs, [0, 20], [1.0, S0], args=(ks,), t_eval=t, method="LSODA", max_step=0.002)
    pb.plot(s.t, s.y[0], color=charts.line(tok), lw=1.9, ls=ls, label=name)
pb.axvline(1, color=P.muted(), lw=0.6, ls=(0, (3, 2)))
pb.text(1.3, 1.36, "290 → 200 mOsm L⁻¹", fontsize=bio.core.FONT["tiny"], color=P.muted(), ha="left")
pb.set_xlim(0, 20)
pb.set_ylim(0.95, 1.4)
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(pb, "time / min", "relative volume V/V₀")
charts.title(pb, "Regulatory volume decrease")
