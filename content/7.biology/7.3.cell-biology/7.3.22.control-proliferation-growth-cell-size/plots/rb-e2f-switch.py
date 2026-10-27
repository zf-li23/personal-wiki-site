"""The Rb-E2F bistable switch and the restriction point (model of Yao et al. 2008, Nat. Cell Biol. 10:476).

Variables (arbitrary concentration units, time in hours): Myc M, free E2F E, cyclin D-Cdk4/6 CD, cyclin
E-Cdk2 CE, unphosphorylated Rb R, phosphorylated Rb RP and the Rb-E2F complex RE. A mitogen (serum) level S
induces Myc and cyclin D; Myc induces E2F (and, with E2F, cyclin E); E2F induces itself and cyclin E; Rb binds
and inhibits E2F; cyclin D-Cdk4/6 and cyclin E-Cdk2 phosphorylate Rb (free or bound to E2F, releasing E2F);
a phosphatase dephosphorylates RP:
  dM/dt  = kM S/(KS+S) - dM M
  dE/dt  = kE fM fE + kb fM + kP1 CD RE/(KCD+RE) + kP2 CE RE/(KCE+RE) - dE E - kRE R E
  dCD/dt = kCD fM + kCDS S/(KS+S) - dCD CD,      dCE/dt = kCE fM fE - dCE CE
  dR/dt  = kR + kDP RP/(KRP+RP) - kRE R E - kP1 CD R/(KCD+R) - kP2 CE R/(KCE+R) - dR R
  dRP/dt = (phosphorylation of R and RE) - kDP RP/(KRP+RP) - dRP RP
  dRE/dt = kRE R E - (phosphorylation of RE) - dRE RE
with fM = M/(KM+M), fE = E/(KE+E) and the parameter values of Yao et al. (kb = 0.03).
(A) Steady-state free E2F against the mitogen level, reached from quiescence (rising S) or from the E2F-on
state (falling S): two stable states over a range of S (bistability) and hysteresis.
(B) Restriction point: quiescent cells receive a high mitogen level (S = 5) for the given time, after which S
is lowered to 0.2 (inside the bistable range). Short pulses leave E2F off; pulses long enough for E2F to pass
the unstable threshold commit the cells, and E2F stays on without further stimulation.
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

p = dict(kE=0.4, kM=1.0, kCD=0.03, kCDS=0.45, kR=0.18, kRE=180, kb=0.03, KS=0.5, kCE=0.35, dM=0.7, dE=0.25, dCD=1.5,
         dCE=1.0, dR=0.06, dRP=0.06, dRE=0.03, kP1=18, kP2=18, kDP=3.6, KM=0.15, KE=0.15, KCD=0.92, KCE=0.92, KRP=0.01)


def rhs(t, y, S):
    M, E, CD, CE, R, RP, RE = y
    q = p
    fm = M / (q["KM"] + M)
    fe = E / (q["KE"] + E)
    fs = S / (q["KS"] + S)
    pR = q["kP1"] * CD * R / (q["KCD"] + R) + q["kP2"] * CE * R / (q["KCE"] + R)
    pRE = q["kP1"] * CD * RE / (q["KCD"] + RE) + q["kP2"] * CE * RE / (q["KCE"] + RE)
    dp = q["kDP"] * RP / (q["KRP"] + RP)
    return [q["kM"] * fs - q["dM"] * M,
            q["kE"] * fm * fe + q["kb"] * fm + pRE - q["dE"] * E - q["kRE"] * R * E,
            q["kCD"] * fm + q["kCDS"] * fs - q["dCD"] * CD,
            q["kCE"] * fm * fe - q["dCE"] * CE,
            q["kR"] + dp - q["kRE"] * R * E - pR - q["dR"] * R,
            pR + pRE - dp - q["dRP"] * RP,
            q["kRE"] * R * E - pRE - q["dRE"] * RE]


def run(y0, S, T, n=200):
    s = solve_ivp(rhs, (0, T), y0, args=(S,), method="LSODA", dense_output=True, rtol=1e-7, atol=1e-10)
    t = np.linspace(0, T, n)
    return t, s.sol(t)


_, Y = run([0, 0, 0, 0, 0.4, 0, 0.25], 0.0, 1000, 2)
off = Y[:, -1]

fig, ax = bio.canvas(24.0, 9.0)
bio.panel(ax, "A", (0.2, 8.8))
a = charts.axes_at(ax, (1.8, 1.5, 9.0, 6.6))
Ss = np.logspace(-2, 1, 40)
up, down = [], []
y = off.copy()
for S in Ss:
    y = run(y, S, 300, 2)[1][:, -1]
    up.append(y[1])
for S in Ss[::-1]:
    y = run(y, S, 300, 2)[1][:, -1]
    down.append(y[1])
a.plot(Ss, up, "o-", color=charts.line("channel"), ms=3, lw=1.4, label="from quiescence (S rising)")
a.plot(Ss[::-1], down, "s-", color=charts.line("negative"), ms=3, lw=1.4, label="from E2F on (S falling)")
a.set_xscale("log")
a.set_xlim(0.01, 10)
a.set_ylim(-0.05, 1.5)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(a, "mitogen level S (serum, relative)", "free E2F (steady state)")

bio.panel(ax, "B", (12.0, 8.8))
b = charts.axes_at(ax, (13.6, 1.5, 9.8, 6.6))
for T, tok in ((12, "neutral"), (18, "channel"), (20, "drug"), (22, "positive"), (26, "negative")):
    t1, Y1 = run(off, 5.0, T, 120)
    t2, Y2 = run(Y1[:, -1], 0.2, 40, 160)
    b.plot(np.r_[t1, T + t2], np.r_[Y1[1], Y2[1]], color=charts.line(tok), lw=1.6, label=f"pulse {T} h")
    b.plot([T], [Y1[1, -1]], "o", ms=3.5, color=charts.line(tok))
b.set_xlim(0, 60)
b.set_ylim(-0.05, 1.4)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(b, "time after mitogen addition / h", "free E2F")
b.text(1, 1.3, "S = 5 during the pulse (dot marks its end), then S = 0.2", fontsize=FT["tiny"], color=P.muted())
