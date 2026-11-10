# IL-2 competition between effector T cells (Teff, the producers) and regulatory T cells (Treg, constitutive CD25).
# Quasi-steady IL-2 balance per Teff cell (Eqs. 11.1-11.2 of the page), concentrations in units of the high-affinity K_D:
#   p = (u_T r + u_E) f + d K f/(1 - f),    f = L/(K + L)   (fraction of high-affinity receptors occupied)
# r = Treg:Teff ratio; Teff expand only when f > f_c = mu/r_E.
import numpy as np
from scipy.optimize import brentq

import wikibio as bio
from wikibio import quant

P = bio.P
K, D_, UE, UT, RE, MU = 1.0, 0.05, 0.2, 3.0, 1.0, 0.3
FC = MU / RE


def f_star(p, r):
    A = UT * r + UE
    g = lambda f: A * f + D_ * K * f / (1 - f) - p
    return brentq(g, 0, 1 - 1e-12)


fig, ax = bio.canvas(16.0, 7.0)
bio.panel(ax, "A", (0.1, 6.85))
bio.label(ax, (4.6, 6.7), "Treg ratio sets the IL-2 signal", size="title", bold=True)
pa = quant.Plot(ax, (1.4, 1.2, 6.2, 4.8), xlim=(0, 3), ylim=(0, 1), xlabel="Treg : Teff ratio $r$",
                ylabel="receptor occupancy $f$", xticks=[0, 1, 2, 3], yticks=[0, 0.3, 0.5, 1], ylabel_offset=0.9)
rs = np.linspace(0, 3, 200)
for p, tok in ((0.5, "channel"), (1.0, "negative"), (2.0, "enzyme")):
    pa.line(rs, [f_star(p, r) for r in rs], tok, lw=1.8)
pa.legend([("$p = 0.5$", "channel", "-"), ("$p = 1$", "negative", "-"), ("$p = 2$", "enzyme", "-")], (pa.X(1.9), pa.Y(0.95)))
pa.hline(FC, dashed=True)
bio.label(ax, (pa.X(3), pa.Y(0.015)), "dashed: expansion threshold $f_\\mathrm{c}$", size="tiny", color=P.muted(), ha="right")
rc = ((1.0 - D_ * K * FC / (1 - FC)) / FC - UE) / UT
pa.points([rc], [FC], "negative", r=0.09)
pa.vline(rc, token="negative", top=False)

bio.panel(ax, "B", (8.8, 6.85))
bio.label(ax, (12.9, 6.7), "IL-2 output of Teff cells", size="title", bold=True)
pb = quant.Plot(ax, (10.2, 1.2, 5.2, 4.8), xlim=(0.01, 20), ylim=(0, 1), xlog=True, xlabel="IL-2 production per Teff cell $p$",
                ylabel="receptor occupancy $f$", xticks=[(0.01, "0.01"), (0.1, "0.1"), (1, "1"), (10, "10")], yticks=[0, 0.3, 0.5, 1],
                ylabel_offset=0.9)
ps = np.logspace(-2, np.log10(20), 200)
for r, tok in ((0, "muted"), (0.5, "channel"), (1, "enzyme"), (2, "negative")):
    pb.line(ps, [f_star(p, r) for p in ps], tok, lw=1.8)
pb.legend([("$r = 0$", "muted", "-"), ("$r = 0.5$", "channel", "-"), ("$r = 1$", "enzyme", "-"), ("$r = 2$", "negative", "-")],
          (pb.X(0.012), pb.Y(0.9)))
pb.hline(FC, dashed=True)
