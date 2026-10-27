"""A minimal model of beta-catenin control by the destruction complex.

beta-catenin B (nM) is made at a constant rate nu and degraded by two routes: slowly by complex-independent
turnover (k_b) and rapidly by the destruction complex (k_dc D), whose activity D (relative to wild type)
is inhibited by Wnt W: dB/dt = nu - (k_b + k_dc D) B, D = a (1 - 0.9 W/(1 + W)), a = 1 for wild type,
0.5 with one functional APC allele, 0 without APC. Parameters (per minute): nu = 0.8 nM/min,
k_dc = ln 2/30 (half-life 30 min when the complex is active), k_b = ln 2/360 (6 h when it is not); the basal
level is then about 32 nM, close to the 35 nM measured by Lee and colleagues (2003) in Xenopus extracts.
A: steady state against Wnt: a sigmoid on a log scale, and APC loss raises beta-catenin to the Wnt-on level
whatever the Wnt concentration. B: switching Wnt on at t = 0 and off at 8 h: the level rises slowly
(time constant 1/(k_b + 0.11 k_dc), about 4 h) and falls quickly (1/(k_b + k_dc), about 40 min), because
the response time is set by the removal rate (7.2.22).
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

P = bio.P
FS = bio.core.FONT["tiny"]
ln2 = np.log(2)
nu, kdc, kb = 0.8, ln2 / 30, ln2 / 360


def Dact(W, a):
    return a * (1 - 0.9 * W / (1 + W))


fig, ax = bio.canvas(20.0, 7.0)
bio.panel(ax, "A", (0.1, 6.9))
pa = charts.axes_at(ax, (1.6, 1.2, 7.6, 4.9))
W = np.logspace(-3, 3, 300)
for a, tok, name in ((1.0, "positive", "wild type"), (0.5, "highlight", "APC +/−"), (0.0, "negative", "APC −/−")):
    pa.plot(W, nu / (kb + kdc * Dact(W, a)), color=charts.line(tok), lw=1.9, label=name)
pa.set_xscale("log")
pa.set_xlim(1e-3, 1e3)
pa.set_ylim(0, 460)
pa.legend(frameon=False, fontsize=FS, labelcolor=P.ink(), loc="upper left")
charts.style_axes(pa, "Wnt (relative units)", "steady-state β-catenin / nM")
charts.title(pa, "Steady state: Wnt inhibits the destruction complex")

bio.panel(ax, "B", (10.4, 6.9))
pb = charts.axes_at(ax, (11.8, 1.2, 7.6, 4.9))


def wnt(t):
    return 100.0 if 0 <= t < 480 else 0.0


t = np.linspace(-60, 720, 2000)
sol = solve_ivp(lambda tt, y: [nu - (kb + kdc * Dact(wnt(tt), 1.0)) * y[0]], (-60, 720), [nu / (kb + kdc)],
                t_eval=t, max_step=1.0)
pb.axvspan(0, 8, color=P.fill("drug"), alpha=0.18, lw=0)
pb.text(4, 205, "Wnt present", fontsize=FS, color=P.muted(), ha="center")
pb.plot(sol.t / 60, sol.y[0], color=charts.line("positive"), lw=2.0)
pb.set_xlim(-1, 12)
pb.set_ylim(0, 230)
charts.style_axes(pb, "time / h", "β-catenin / nM")
charts.title(pb, "Slow on, fast off")
