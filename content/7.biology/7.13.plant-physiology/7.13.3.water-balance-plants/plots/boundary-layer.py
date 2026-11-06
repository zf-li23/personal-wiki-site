# Transpiration through stomatal and boundary-layer conductances in series:
# E = g_t * (w_leaf - w_air), 1/g_t = 1/g_s + 1/g_b, with mole fractions of water vapour w.
# Leaf and air at 25 C, air at 50 % relative humidity, pressure 101.3 kPa: w_leaf = 0.0313, w_air = 0.0156.
# Boundary-layer conductance for water vapour of a flat leaf (Campbell and Norman): g_b = 0.147 sqrt(u/d)
# mol m-2 s-1, leaf dimension d = 0.05 m; still air u = 0.2 m/s (g_b = 0.29), wind u = 3 m/s (g_b = 1.14).
# Leaf temperature is held fixed (in reality the boundary layer also couples leaf temperature to the air).
# A: E against stomatal conductance. B: the stomatal sensitivity d ln E / d ln g_s = g_b / (g_s + g_b):
#    near 1 the stomata control transpiration; near 0 the boundary layer does.
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(24.0, 9.6)
es = 0.6108 * np.exp(17.27 * 25 / (25 + 237.3))  # kPa
wl, wa = es / 101.3, 0.5 * es / 101.3
gs = np.linspace(0.001, 1.0, 400)
winds = [(0.2, "rna", "still air, u = 0.2 m s⁻¹"), (3.0, "dna", "wind, u = 3 m s⁻¹")]

bio.panel(ax, "A", (0.2, 9.5))
pa = charts.axes_at(ax, (2.2, 1.5, 8.6, 6.9))
bio.panel(ax, "B", (12.6, 9.5))
pb = charts.axes_at(ax, (14.6, 1.5, 8.6, 6.9))
for u, tok, txt in winds:
    gb = 0.147 * np.sqrt(u / 0.05)
    E = (wl - wa) / (1 / gs + 1 / gb) * 1e3
    col = charts.line(tok)
    pa.plot(gs, E, color=col, lw=1.9, label=f"{txt} (g_b = {gb:.2f})")
    pa.axhline((wl - wa) * gb * 1e3, color=col, lw=0.7, ls=":")
    pb.plot(gs, gb / (gs + gb), color=col, lw=1.9, label=txt)
pa.text(0.98, (wl - wa) * 0.294 * 1e3 + 0.25, "limit g_s → ∞", fontsize=7.5, color=P.muted(), ha="right")
pa.set_xlim(0, 1)
pa.set_ylim(0, 12)
leg = pa.legend(loc="upper left", frameon=False, fontsize=8)
for t in leg.get_texts():
    t.set_color(P.ink())
charts.style_axes(pa, "stomatal conductance g_s / (mol m⁻² s⁻¹)", "E / (mmol m⁻² s⁻¹)")
charts.title(pa, "Transpiration rate")
pb.set_xlim(0, 1)
pb.set_ylim(0, 1.02)
pb.text(0.5, 0.93, "stomatal control", fontsize=8, color=P.muted(), ha="center")
pb.text(0.7, 0.2, "boundary-layer control", fontsize=8, color=P.muted(), ha="center")
leg = pb.legend(loc="lower left", frameon=False, fontsize=8)
for t in leg.get_texts():
    t.set_color(P.ink())
charts.style_axes(pb, "stomatal conductance g_s / (mol m⁻² s⁻¹)", "d ln E / d ln g_s")
charts.title(pb, "How much do stomata control E?")
