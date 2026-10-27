"""A minimal model of the embryonic cell-cycle oscillator (after Novak and Tyson 1993; Pomerening et al. 2003, 2005).

Variables: C, total cyclin B-Cdk1 (nM; Cdk1 is in excess, so every cyclin is bound); u, active
(dephosphorylated) cyclin B-Cdk1 (nM); A, fraction of APC/C-Cdc20 that is active.
    dC/dt = ks - kd(A) C
    du/dt = k25(u) (C - u) - kwee(u) u - kd(A) u
    dA/dt = ka u^m / (Ka^m + u^m) (1 - A) - ki A
with kd(A) = kd0 + kd1 A (APC/C-dependent cyclin destruction), k25(u) = k25' + k25'' H(u) (Cdc25 activated by
Cdk1), kwee(u) = kw' + kw'' (1 - H(u)) (Wee1 inhibited by Cdk1) and H(u) = u^4 / (K^4 + u^4).
Parameters: ks = 2 nM/min, kd0 = 0.01, kd1 = 0.4, k25' = 0.03, k25'' = 1, kw' = 0.02, kw'' = 0.2 (all per min),
K = Ka = 20 nM, m = 4, ka = 0.3, ki = 0.08 per min. Newly made cyclin joins the inactive pool (it is
phosphorylated by Wee1 at once).
(A) Self-sustained oscillations (period about 65 min): cyclin accumulates slowly, Cdk1 switches on abruptly,
activates APC/C with a delay and is destroyed.
(B) The (C, u) plane. The S-shaped curve is the set of steady states of u for nondegradable cyclin (A = 0): the
response of Cdk1 to cyclin is bistable, switching on at about 43 nM and off at about 24 nM (hysteresis, as
measured in Xenopus extracts by Pomerening et al. and Sha et al. 2003). The limit cycle (solid loop) runs along
the lower branch, jumps up shortly after passing the right fold, and is pulled back down by APC/C.
(C) Removing the positive feedback (k25'' = kw'' = 0, constant Cdc25 and Wee1 rates of 0.1 per min) leaves only
the negative loop through APC/C: the oscillation is damped and the system settles to a steady state.
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

BASE = dict(ks=2.0, K=20.0, n=4, k25a=0.03, k25b=1.0, kwa=0.02, kwb=0.2, kd0=0.01, kd1=0.4, ka=0.3, Ka=20.0, m=4,
            ki=0.08)


def H(u, p):
    return u ** p["n"] / (p["K"] ** p["n"] + u ** p["n"])


def rhs(t, y, p):
    C, u, A = y
    h = H(u, p)
    kd = p["kd0"] + p["kd1"] * A
    du = (p["k25a"] + p["k25b"] * h) * (C - u) - (p["kwa"] + p["kwb"] * (1 - h)) * u - kd * u
    dC = p["ks"] - kd * C
    g = u ** p["m"] / (p["Ka"] ** p["m"] + u ** p["m"])
    dA = p["ka"] * g * (1 - A) - p["ki"] * A
    return [dC, du, dA]


def run(p, T=400):
    s = solve_ivp(rhs, (0, T), [0.0, 0.0, 0.0], args=(p,), max_step=0.2, rtol=1e-8, atol=1e-10)
    return s.t, s.y


t, (C, u, A) = run(BASE)

fig, ax = bio.canvas(27.0, 9.0)
bio.panel(ax, "A", (0.2, 8.8))
a = charts.axes_at(ax, (1.6, 1.5, 7.2, 6.4))
a.plot(t, C, color=charts.line("protein"), lw=1.6, label="total cyclin B–Cdk1, C")
a.plot(t, u, color=charts.line("negative"), lw=1.9, label="active Cdk1, u")
a.plot(t, 60 * A, color=charts.line("enzyme"), lw=1.3, ls="--", label="APC/C activity (× 60 nM)")
a.set_xlim(0, 300)
a.set_ylim(0, 75)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left", ncol=1)
charts.style_axes(a, "time / min", "concentration / nM")

# ----- B: phase plane
bio.panel(ax, "B", (9.6, 8.8))
b = charts.axes_at(ax, (11.0, 1.5, 7.0, 6.4))
p = BASE
us = np.linspace(0.01, 75, 6000)
h = H(us, p)
k25 = p["k25a"] + p["k25b"] * h
kw = p["kwa"] + p["kwb"] * (1 - h) + p["kd0"]
Css = us * (k25 + kw) / k25          # steady states of u for fixed C with A = 0
dC = np.gradient(Css, us)
stable = dC > 0
for mask, ls in ((stable, "-"), (~stable, "--")):
    y = np.where(mask, us, np.nan)
    b.plot(Css, y, color=charts.line("neutral"), lw=1.6, ls=ls)
folds = np.where(np.diff(np.sign(dC)))[0]
for i in folds:
    b.plot([Css[i]], [us[i]], "o", ms=4, color=charts.line("neutral"))
    b.annotate(f"{Css[i]:.0f} nM", (Css[i], us[i]), xytext=(4, -10 if us[i] < 15 else 6), textcoords="offset points",
               fontsize=FT["tiny"], color=P.muted())
late = t > 150
b.plot(C[late], u[late], color=charts.line("negative"), lw=1.6)
# direction marks on the cycle
for frac in (0.2, 0.55, 0.8):
    k = np.where(late)[0][int(frac * late.sum() / 2.2)]
    b.annotate("", xy=(C[k + 3], u[k + 3]), xytext=(C[k], u[k]),
               arrowprops=dict(arrowstyle="-|>", color=charts.line("negative"), lw=1.0, mutation_scale=13))
b.text(52, 50, "upper branch:\nCdk1 on", fontsize=FT["tiny"], color=P.muted(), ha="center")
b.text(3, 9, "lower branch:\nCdk1 off\n(Wee1 wins)", fontsize=FT["tiny"], color=P.muted(), ha="left")
b.set_xlim(0, 75)
b.set_ylim(0, 75)
charts.style_axes(b, "total cyclin B–Cdk1 C / nM", "active Cdk1 u / nM")

# ----- C: without positive feedback
bio.panel(ax, "C", (18.8, 8.8))
c = charts.axes_at(ax, (20.2, 1.5, 6.4, 6.4))
q = dict(BASE, k25b=0.0, kwb=0.0, k25a=0.1, kwa=0.1)
t2, (C2, u2, A2) = run(q)
c.plot(t, u, color=charts.line("negative"), lw=1.6, label="with positive feedback")
c.plot(t2, u2, color=charts.line("channel"), lw=1.6, label="Cdc25, Wee1 constant")
c.set_xlim(0, 400)
c.set_ylim(0, 60)
c.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(c, "time / min", "active Cdk1 u / nM")
