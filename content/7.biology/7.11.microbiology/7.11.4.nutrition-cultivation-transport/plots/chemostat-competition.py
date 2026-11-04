"""Competition of two species for one limiting substrate in a chemostat (Monod kinetics).
dN_i/dt = (mu_i(S) - D) N_i,  dS/dt = D (S0 - S) - sum mu_i(S) N_i / Y,  mu_i = mu_max_i S / (Ks_i + S).
Species A: mu_max 1.0 per h, Ks 2 mg/L (fast, low affinity); species B: mu_max 0.5 per h, Ks 0.2 mg/L
(slow, high affinity). Yield Y = 0.5 mg biomass per mg substrate for both; S0 = 20 mg/L. Break-even
concentration R* = Ks D / (mu_max - D); the curves cross at D = 4/9 per h."""

import numpy as np
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P = bio.P
mu = {"A": 1.0, "B": 0.5}
ks = {"A": 2.0, "B": 0.2}
Y, S0 = 0.5, 20.0
tok = {"A": "drug", "B": "enzyme"}


def rstar(s, D):
    return np.where(D < mu[s], ks[s] * D / (mu[s] - D), np.nan)


def run(D, T):
    def f(t, z):
        nA, nB, S = z
        mA, mB = mu["A"] * S / (ks["A"] + S), mu["B"] * S / (ks["B"] + S)
        return [(mA - D) * nA, (mB - D) * nB, D * (S0 - S) - (mA * nA + mB * nB) / Y]
    t = np.linspace(0, T, 1500)
    sol = solve_ivp(f, (0, T), [0.05, 0.05, S0], t_eval=t, method="LSODA", rtol=1e-8, atol=1e-10)
    return sol.t, sol.y


fig, ax = bio.canvas(27.0, 8.6)
a = charts.axes_at(ax, (1.6, 1.4, 6.6, 6.0))
D = np.linspace(0.005, 0.499, 400)
DA = np.linspace(0.005, 0.8, 400)
a.plot(DA, rstar("A", DA), color=charts.line(tok["A"]), lw=2.0, label="A: fast, low affinity")
a.plot(D, rstar("B", D), color=charts.line(tok["B"]), lw=2.0, label="B: slow, high affinity")
dc = 4 / 9
a.axvline(dc, color=P.muted(), lw=0.8, ls="--")
a.text(dc + 0.06, 3.75, "crossover", fontsize=bio.core.FONT["tiny"], color=P.muted())
for Dm in (0.2, 0.47):
    a.plot([Dm], [0.05], marker="v", color=P.ink(), ms=5, clip_on=False)
a.set_xlim(0, 0.8)
a.set_ylim(0, 4)
a.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(a, r"dilution rate $D$ / h$^{-1}$", r"$R^*$ / (mg L$^{-1}$)")
charts.title(a, "A  Break-even concentration")

for k, (Dm, T, ttl) in enumerate([(0.2, 250, "B  D = 0.2 h⁻¹: B wins"), (0.47, 120, "C  D = 0.47 h⁻¹: A wins")]):
    t, (nA, nB, S) = run(Dm, T)
    b = charts.axes_at(ax, (10.4 + k * 8.4, 1.4, 6.0, 6.0))
    b.semilogy(t, np.maximum(nA, 1e-6), color=charts.line(tok["A"]), lw=2.0, label="A")
    b.semilogy(t, np.maximum(nB, 1e-6), color=charts.line(tok["B"]), lw=2.0, label="B")
    b.semilogy(t, np.maximum(S, 1e-6), color=P.muted(), lw=1.2, ls="--", label="substrate S")
    b.set_ylim(1e-4, 40)
    b.set_xlim(0, T)
    b.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
    charts.style_axes(b, "t / h", r"biomass, $S$ / (mg L$^{-1}$)")
    charts.title(b, ttl)
