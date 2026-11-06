# Pressure-volume curve of a leaf from a model (illustrative parameters, typical of a mesophytic leaf).
# Relative water content R (1 = full turgor); a fraction a = 0.15 of the water is apoplastic and
# osmotically inactive, so the symplastic relative water content is Rs = (R - a) / (1 - a).
# Solute potential: Psi_s = pi0 / Rs with pi0 = -1.2 MPa (osmotic potential at full turgor).
# Turgor: Psi_p = eps * (Rs - Rs_tlp) above the turgor loss point, bulk elastic modulus eps = 12 MPa,
# chosen so that Psi_p = -pi0 at Rs = 1; below the turgor loss point Psi_p = 0.
# A: Psi, Psi_s and Psi_p against R (water potential falls steeply while turgor lasts).
# B: the Tyree-Hammel plot used with the pressure chamber: 1 / (-Psi) against water lost (1 - R).
#    Below the turgor loss point the points lie on a straight line; extrapolated to 1 - R = 0 it gives
#    -1 / pi0, and its x-intercept is the symplastic water fraction 1 - a.
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(24.0, 9.6)
A_APO, PI0, EPS = 0.15, -1.2, 12.0
RS_TLP = 1 + PI0 / EPS


def model(R):
    rs = (R - A_APO) / (1 - A_APO)
    ps = PI0 / rs
    pp = np.where(rs > RS_TLP, EPS * (rs - RS_TLP), 0.0)
    return ps, pp, ps + pp


R_TLP = A_APO + RS_TLP * (1 - A_APO)
PSI_TLP = PI0 / RS_TLP

# ---- A ------------------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.2, 9.5))
pa = charts.axes_at(ax, (2.2, 1.5, 8.6, 6.9))
R = np.linspace(0.70, 1.0, 400)
ps, pp, pw = model(R)
pa.axhline(0, color=P.muted(), lw=0.7)
pa.plot(R, ps, color=charts.line("metabolite"), lw=1.6)
pa.plot(R, pp, color=charts.line("cell_wall"), lw=1.6)
pa.plot(R, pw, color=charts.line("dna"), lw=2.0, zorder=5)
pa.axvline(R_TLP, color=P.muted(), lw=0.8, ls="--")
pa.text(R_TLP - 0.005, -0.12, "turgor loss point", fontsize=7.5, color=P.muted(), ha="left", va="top")
pa.text(0.955, 0.95, "Ψp", color=charts.line("cell_wall"), fontsize=9, ha="right")
pa.text(0.72, -1.95, "Ψs", color=charts.line("metabolite"), fontsize=9)
pa.text(0.955, -0.62, "Ψw", color=charts.line("dna"), fontsize=9)
pa.set_xlim(1.0, 0.70)
pa.set_ylim(-2.4, 1.3)
charts.style_axes(pa, "relative water content R", "Ψ / MPa")
charts.title(pa, "Water potential components")

# ---- B ------------------------------------------------------------------------------------------------------
bio.panel(ax, "B", (12.6, 9.5))
pb = charts.axes_at(ax, (14.6, 1.5, 8.6, 6.9))
rng = np.random.default_rng(0)
Rm = np.linspace(0.985, 0.72, 16)
_, _, wm = model(Rm)
y = -1 / wm * (1 + rng.normal(0, 0.015, Rm.size))
x = 1 - Rm
pb.plot(x, y, "o", ms=4.5, color=charts.line("dna"), label="simulated measurements")
xl = np.linspace(0, 1 - A_APO, 50)
yl = (-1 / PI0) * (1 - xl / (1 - A_APO))
pb.plot(xl, yl, color=charts.line("rna"), lw=1.2, ls="--")
pb.plot([0], [-1 / PI0], "s", ms=5, color=charts.line("rna"))
pb.annotate("−1/π₀ → π₀ = −1.2 MPa", (0, -1 / PI0), (0.12, 1.25), fontsize=7.5, color=P.ink(),
            arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
pb.plot([1 - R_TLP], [-1 / PSI_TLP], "^", ms=6, color=charts.line("highlight"))
pb.annotate("turgor loss point\nΨ = " + f"{PSI_TLP:.2f}".replace("-", "−") + " MPa", (1 - R_TLP, -1 / PSI_TLP), (0.22, 0.92), fontsize=7.5,
            color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
pb.annotate("x-intercept: 1 − a\n(symplastic water)", (1 - A_APO, 0), (0.55, 0.3), fontsize=7.5, color=P.ink(),
            arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
pb.set_xlim(0, 0.9)
pb.set_ylim(0, 1.6)
leg = pb.legend(loc="upper right", frameon=False, fontsize=8)
for t in leg.get_texts():
    t.set_color(P.ink())
charts.style_axes(pb, "water lost 1 − R", "1 / (−Ψ) / MPa⁻¹")
charts.title(pb, "Pressure-volume (Tyree-Hammel) plot")
