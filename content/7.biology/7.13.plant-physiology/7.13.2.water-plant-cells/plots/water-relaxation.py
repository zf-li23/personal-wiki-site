# Osmotic equilibration of a single cell after a step change of the external water potential.
# The cell (Psi = -0.2 MPa) is transferred to pure water (Psi_o = 0). Volume flux J_v = L_p (Psi_o - Psi);
# because dPsi/dV = (eps - Psi_s) / V, the cell water potential relaxes exponentially with
# tau = V / [A L_p (eps - Psi_s)] and half-time t_1/2 = 0.693 tau.
# Cylindrical cell: radius 20 um, length 100 um (V/A = 8.3 um); eps = 10 MPa, Psi_s = -0.8 MPa.
# Two membrane hydraulic conductivities: aquaporins mostly closed (L_p = 2e-7 m s-1 MPa-1) and open
# (L_p = 2e-6 m s-1 MPa-1).
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(24.0, 9.6)
r, L = 20e-6, 100e-6
V_A = r * L / (2 * L + 2 * r)
EPS, PSIS, PSI0 = 10.0, -0.8, -0.2
t = np.linspace(0, 10, 500)
cases = [(2e-6, "dna", "L_p = 2×10⁻⁶ m s⁻¹ MPa⁻¹ (aquaporins open)", (0.9, -0.06)),
         (2e-7, "rna", "L_p = 2×10⁻⁷ m s⁻¹ MPa⁻¹ (aquaporins closed)", (3.3, -0.12))]

bio.panel(ax, "A", (0.2, 9.5))
pa = charts.axes_at(ax, (2.2, 1.5, 8.6, 6.9))
bio.panel(ax, "B", (12.6, 9.5))
pb = charts.axes_at(ax, (14.6, 1.5, 8.6, 6.9))
for lp, tok, txt, at in cases:
    tau = V_A / (lp * (EPS - PSIS))
    psi = PSI0 * np.exp(-t / tau)
    jv = lp * (0 - psi) * 1e6  # um s-1
    c = charts.line(tok)
    pa.plot(t, psi, color=c, lw=1.8, label=txt)
    pb.plot(t, jv, color=c, lw=1.8, label=txt)
    th = 0.693 * tau
    pa.plot([th], [PSI0 / 2], "o", ms=4.5, color=c)
    pa.annotate(f"t½ = {th:.2f} s", (th, PSI0 / 2), at, fontsize=7.5, color=c)
pa.axhline(PSI0 / 2, color=P.muted(), lw=0.6, ls=":")
pa.set_ylim(-0.21, 0.01)
pa.set_xlim(0, 10)
charts.style_axes(pa, "t / s", "Ψ_cell / MPa")
charts.title(pa, "Cell water potential after transfer to pure water")
pb.set_xlim(0, 10)
pb.set_ylim(0, 0.42)
leg = pb.legend(loc="upper right", frameon=False, fontsize=8)
for tt in leg.get_texts():
    tt.set_color(P.ink())
charts.style_axes(pb, "t / s", "J_v / (µm s⁻¹)")
charts.title(pb, "Volume flux into the cell, J_v = L_p ΔΨ")
