# Model: the power required for flapping flight as a function of airspeed (after Pennycuick 1989, 2008).
# Induced power P_ind = k (M g)^2 / (2 rho V S_d), with disc area S_d = pi b^2 / 4 and k = 1.2; parasite
# power P_par = rho V^3 S_b C_Db / 2, with body frontal area S_b = 0.00813 M^0.666 m^2 and C_Db = 0.1;
# profile power taken as constant, 1.2 times the absolute minimum of P_ind + P_par. (A) A pigeon
# (M = 0.40 kg, span b = 0.67 m): the U-shaped curve, the minimum-power speed V_mp and the maximum-range
# speed V_mr (tangent from the origin). (B) Scaling: with geometric similarity the minimum power per unit
# mass rises as M^(1/6), while the power available from the flight muscles per unit mass is assumed to
# fall as M^(-1/3) (wingbeat frequency falls with size); the curves are calibrated (schematically) to
# cross at about 12-15 kg, the size of the heaviest flapping fliers (bustards, swans).
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
g, rho, k, CD = 9.81, 1.23, 1.2, 0.1


def powers(M, b, V):
    Sd = np.pi * b ** 2 / 4
    Sb = 0.00813 * M ** 0.666
    ind = k * (M * g) ** 2 / (2 * rho * V * Sd)
    par = 0.5 * rho * V ** 3 * Sb * CD
    pro = 1.2 * np.min(ind + par)
    return ind, par, np.full_like(V, pro)


fig, ax = bio.canvas(23, 8.8)
V = np.linspace(3, 30, 400)
ind, par, pro = powers(0.40, 0.67, V)
tot = ind + par + pro
p = quant.Plot(ax, (1.8, 1.4, 8.6, 6.2), xlim=(0, 30), ylim=(0, 12), xlabel="airspeed / m s-1",
               ylabel="mechanical power / W", xticks=[0, 10, 20, 30], yticks=[0, 4, 8, 12])
p.line(V, tot, "dna", text="total", at=0.93, dy=0.2)
p.line(V, ind, "mrna", dashed=True, text="induced", at=0.04, dy=0.3)
p.line(V, par, "positive", dashed=True, text="parasite", at=0.86, dy=-0.6)
p.line(V, pro, "muted", dotted=True, text="profile", at=0.6, dy=0.15)
imp = np.argmin(tot)
imr = np.argmin(tot / V)
p.points([V[imp]], [tot[imp]], "dna")
p.text(V[imp], tot[imp] + 0.8, "V_mp", ha="center")
p.line(np.r_[0, V[imr] * 1.25], np.r_[0, tot[imr] / V[imr] * V[imr] * 1.25], "muted", lw=0.9)
p.points([V[imr]], [tot[imr]], "dna", hollow=True)
p.text(V[imr] + 0.4, tot[imr] - 0.9, "V_mr", ha="left")
bio.panel(ax, "A", (0.4, 8.4))
bio.label(ax, (6.1, 8.3), "pigeon, 0.4 kg", size="small", color=P.muted())

M = np.logspace(-2.5, 1.7, 200)
req = M ** (1 / 6)
avail = 12 ** 0.5 * M ** (-1 / 3)
scale = 1 / req[0]
q = quant.Plot(ax, (13.6, 1.4, 8.4, 6.2), xlim=(0.003, 50), ylim=(0.3, 30), xlog=True, ylog=True,
               xlabel="body mass / kg", ylabel="power per unit mass (relative)",
               xticks=[0.01, 0.1, 1, 10], yticks=[1, 3, 10, 30])
q.line(M, req * scale, "dna", text="minimum power required ~ M^(1/6)", at=0.05, dy=-0.55)
q.line(M, avail * scale, "mrna")
q.text(0.3, 12, "power available ~ M^(-1/3)", token="mrna", ha="left")
mc = 12.0
q.vline(mc, text="upper limit ~ 12-15 kg", size="tiny")
bio.panel(ax, "B", (12.2, 8.4))
