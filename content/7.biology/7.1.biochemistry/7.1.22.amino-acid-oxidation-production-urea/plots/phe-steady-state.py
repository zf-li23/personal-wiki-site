"""Why phenylketonuria is a threshold disease, and why diet works: a one-compartment model of plasma
phenylalanine. dF/dt = I - f Vmax F/(Km + F) - k F, with I the net input of Phe (diet plus protein turnover
minus use for protein synthesis), f the residual phenylalanine hydroxylase activity (1 = normal), Km the
apparent Michaelis constant of hydroxylation and k a slow first-order loss (transamination to phenylpyruvate,
urinary excretion). Illustrative parameters: Km = 300 uM, Vmax = 57.6 uM/h, k = 0.0067 /h, I = 10 uM/h on a
normal diet (normal steady state 60 uM), 2 uM/h on a Phe-restricted diet.
(A) Steady-state [Phe] against residual activity: as f falls toward I/Vmax the hydroxylase saturates and
[Phe] rises steeply to the level set by the slow route (~1500 uM). (B) Plasma [Phe] after birth in a child
with 1% residual activity: untreated, and with a restricted diet from day 7."""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

import wikibio as bio
from wikibio import charts

P = bio.P
KM, VMAX, K = 300.0, 57.6, 0.0067


def rate(F, I, f):
    return I - f * VMAX * F / (KM + F) - K * F


def steady(I, f):
    return brentq(lambda F: rate(F, I, f), 0.0, 1e5)


fig, ax = bio.canvas(19.0, 8.4)
a = charts.axes_at(ax, (2.0, 1.4, 7.2, 6.2))
fs = np.logspace(-3, 0, 200)
for I, tok, name in ((10.0, "negative", "normal diet"), (2.0, "positive", "Phe-restricted diet")):
    a.plot(fs * 100, [steady(I, f) for f in fs], color=charts.line(tok), lw=2.0, label=name)
a.axhspan(120, 360, color=P.mix(P.fill("positive"), P.surface(), 0.6), lw=0)
a.axhline(1200, color=P.muted(), lw=0.8, ls="--")
a.text(0.12, 1260, "classic PKU (> 1200 µM)", fontsize=bio.core.FONT["tiny"], color=P.muted())
a.text(0.12, 200, "treatment target", fontsize=bio.core.FONT["tiny"], color=P.edge("positive"))
a.set_xscale("log")
a.set_xlim(0.1, 100)
a.set_ylim(0, 1700)
a.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(a, "residual PAH activity / % of normal", "steady-state [Phe] / µM")
charts.title(a, "A  Threshold in the steady state")

b = charts.axes_at(ax, (11.4, 1.4, 7.2, 6.2))
f = 0.01
t1 = np.linspace(0, 40 * 24, 800)
sol = solve_ivp(lambda t, y: [rate(y[0], 10.0, f)], (0, t1[-1]), [60.0], t_eval=t1, rtol=1e-8)
b.plot(t1 / 24, sol.y[0], color=charts.line("negative"), lw=2.0, label="untreated")
ta = np.linspace(0, 7 * 24, 200)
s1 = solve_ivp(lambda t, y: [rate(y[0], 10.0, f)], (0, ta[-1]), [60.0], t_eval=ta, rtol=1e-8)
tb = np.linspace(7 * 24, 40 * 24, 600)
s2 = solve_ivp(lambda t, y: [rate(y[0], 2.0, f)], (tb[0], tb[-1]), [s1.y[0][-1]], t_eval=tb, rtol=1e-8)
b.plot(np.r_[ta, tb] / 24, np.r_[s1.y[0], s2.y[0]], color=charts.line("positive"), lw=2.0, label="diet from day 7")
b.axhspan(120, 360, color=P.mix(P.fill("positive"), P.surface(), 0.6), lw=0)
b.axvline(7, color=P.muted(), lw=0.8, ls=":")
b.set_xlim(0, 40)
b.set_ylim(0, 1700)
b.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(b, "age / days", "plasma [Phe] / µM")
charts.title(b, "B  1% residual activity after birth")
