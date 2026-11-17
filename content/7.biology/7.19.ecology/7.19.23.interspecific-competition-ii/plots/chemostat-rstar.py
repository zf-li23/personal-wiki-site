"""Competition for one resource in a chemostat: the R* rule.

Model: dR/dt = D (S - R) - sum_i mu_i(R) N_i / Y_i, dN_i/dt = N_i (mu_i(R) - D), with Monod growth
mu_i(R) = mu_max,i R / (k_i + R) (Hsu, Hubbell and Waltman 1977; Tilman 1982). Parameters (simulated):
dilution rate D = 0.25 per day, supply concentration S = 10 (arbitrary units), yields Y_i = 1;
species 1: mu_max = 1.0, k = 2, so R*_1 = D k / (mu_max - D) = 0.67; species 2: mu_max = 1.5, k = 5,
so R*_2 = 1.0. A: per capita growth rates against R; the horizontal line D is the loss rate, and each
species' R* is where its curve crosses it. Species 2 grows faster when the resource is abundant but
needs more of it to balance its losses. B: dynamics from N1 = N2 = 0.1 and R = S: species 2 increases
first, the resource is drawn down to R*_1 (dashed), and species 2, which cannot grow at this level,
is washed out.
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 12.0)
D, S = 0.25, 10.0
mu = [(1.0, 2.0), (1.5, 5.0)]
c = [Q.line_color("dna"), Q.line_color("rna")]
rstar = [D * k / (m - D) for m, k in mu]

pa = C.axes_at(ax, (2.4, 1.8, 11.0, 8.6))
R = np.linspace(0, 10, 400)
for (m, k), col, rs, i in zip(mu, c, rstar, (1, 2)):
    pa.plot(R, m * R / (k + R), color=col, lw=1.8, label=f"species {i}")
    pa.plot([rs, rs], [0, D], color=col, lw=0.9, ls=(0, (3, 2)))
    pa.text(rs, -0.06, f"$R^*_{i}$", color=col, fontsize=FS["tiny"], ha="center", va="top")
pa.axhline(D, color=P.muted(), lw=1.0)
pa.text(9.8, D + 0.02, "loss rate D", fontsize=FS["tiny"], color=P.muted(), ha="right")
pa.set_xlim(0, 10)
pa.set_ylim(0, 1.0)
C.style_axes(pa, "resource concentration R", "per capita growth rate (per day)")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.4, 11.6))
bio.label(ax, (2.4, 11.2), "Monod growth and R*", size="small", bold=True, ha="left")


def f(t, y):
    r, n1, n2 = y
    g1 = mu[0][0] * r / (mu[0][1] + r)
    g2 = mu[1][0] * r / (mu[1][1] + r)
    return [D * (S - r) - g1 * n1 - g2 * n2, n1 * (g1 - D), n2 * (g2 - D)]


t = np.linspace(0, 150, 800)
s = solve_ivp(f, (0, 150), [S, 0.1, 0.1], t_eval=t, rtol=1e-9)
pb = C.axes_at(ax, (17.0, 1.8, 11.5, 8.6))
pb.plot(t, s.y[1], color=c[0], lw=1.8, label="species 1, $N_1$")
pb.plot(t, s.y[2], color=c[1], lw=1.8, label="species 2, $N_2$")
pb.plot(t, s.y[0], color=P.ink(), lw=1.2, label="resource R")
pb.axhline(rstar[0], color=c[0], lw=0.8, ls=(0, (3, 2)))
pb.set_xlim(0, 150)
pb.set_ylim(0, 10.5)
C.style_axes(pb, "time (days)", "density or concentration")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="center right")
bio.panel(ax, "B", (15.0, 11.6))
bio.label(ax, (17.0, 11.2), "The species with the lower R* wins", size="small", bold=True, ha="left")
