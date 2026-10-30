"""Murray's law (Formula 29.5.1). A: the cost per unit length of a vessel carrying a flow Q against its radius:
viscous dissipation (Poiseuille), falling as 1/r^4, plus the metabolic cost of the blood volume, rising as r^2;
the total is minimal at r* proportional to Q^(1/3) (all scaled to the optimum). B: a symmetric tree built by the
rule: at each branch point the cube of the parent radius equals the sum of the cubes of the daughters (daughters
2^(-1/3) = 0.79 times the parent), with the optimal branching half-angle of 37.5 degrees; line widths are
proportional to radius and segment lengths to radius. Under the rule the wall shear stress is the same in every
vessel, the signal that endothelial cells use to remodel vessels towards it."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
fig, (a, b) = plt.subplots(1, 2, figsize=(10.2, 4.2))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.14, top=0.88, wspace=0.18)
r = np.linspace(0.45, 2.0, 300)
diss = 1 / r**4 / 3
vol = r**2 * 2 / 3
a.plot(r, diss, color=charts.line("dna"), lw=1.5, label=r"dissipation $\propto r^{-4}$")
a.plot(r, vol, color=charts.line("blood"), lw=1.5, label=r"blood volume $\propto r^{2}$")
a.plot(r, diss + vol, color=P_.ink(), lw=2.0, label="total cost")
a.plot([1], [1], "o", color=P_.ink(), ms=6)
a.axvline(1, color=P_.muted(), lw=0.7, ls=":")
a.set_ylim(0, 3)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper right")
charts.style_axes(a, r"radius $r/r^*$", "cost per unit length (scaled)")
charts.title(a, "A  An optimal radius")
th = np.radians(37.5)


def grow(x, y, ang, rad, gen):
    L = 9 * rad
    x2, y2 = x + L * np.cos(ang), y + L * np.sin(ang)
    b.plot([x, x2], [y, y2], color=charts.line("blood"), lw=rad * 9, solid_capstyle="round")
    if gen < 6:
        for s in (1, -1):
            grow(x2, y2, ang + s * th, rad * 2 ** (-1 / 3), gen + 1)


grow(0, 0, np.pi / 2, 1.0, 0)
b.set_aspect("equal")
b.set_xticks([])
b.set_yticks([])
for sp in b.spines.values():
    sp.set_visible(False)
charts.title(b, r"B  $r_0^3 = r_1^3 + r_2^3$, half-angle 37.5$^\circ$")
