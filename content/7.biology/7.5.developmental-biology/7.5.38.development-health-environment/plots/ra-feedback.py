"""Why an excess of retinoic acid can end as a deficiency: a two-variable feedback model (Formula 38.4.4).

R: retinoic acid in the tissue (relative units), synthesized at rate s (by RALDH) plus an external dose u(t),
degraded at rate (k0 + k C) R, where C is the level of the RA-inducible degrading enzyme CYP26.
C is induced by RA with a Hill function and turns over slowly (rate delta):
    dR/dt = s + u(t) - (k0 + k C) R,      dC/dt = c0 + a R^n / (K^n + R^n) - delta C.
Parameters (illustrative): s = 1, k0 = 0.2, k = 1, c0 = 0.05, a = 0.6, K = 1.5, n = 2, delta = 0.05 per hour
(C half-life about 14 h); time in hours. A pulse u = U for 6 h starting at t = 10 h.
A: time courses for U = 10 (R and C relative to their steady states). B: the largest fall of R below its steady
state and the time R spends more than 20 % below it, against the pulse amplitude U.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
s, k0, k, c0, a, K, n, delta = 1.0, 0.2, 1.0, 0.05, 0.6, 1.5, 2.0, 0.05


def c_of_r(r):
    return (c0 + a * r**n / (K**n + r**n)) / delta


Rs = brentq(lambda r: s - (k0 + k * c_of_r(r)) * r, 1e-6, 10)
Cs = c_of_r(Rs)


def run(U, t_end=150.0):
    def f(t, y):
        u = U if 10 <= t < 16 else 0.0
        R, C = y
        return [s + u - (k0 + k * C) * R, c0 + a * R**n / (K**n + R**n) - delta * C]

    t = np.linspace(0, t_end, 3001)
    sol = solve_ivp(f, (0, t_end), [Rs, Cs], t_eval=t, max_step=0.05, rtol=1e-8)
    return sol.t, sol.y[0] / Rs, sol.y[1] / Cs


fig, axs = plt.subplots(1, 2, figsize=(11.0, 3.7))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.16, top=0.86, wspace=0.3)
t, r, c = run(10.0)
A = axs[0]
A.axvspan(10, 16, color=P.light("drug"), lw=0)
A.text(13, 0.15, "RA dose", fontsize=FT["tiny"], color=P.ink(), ha="center")
A.semilogy(t, r, color=charts.line("metabolite"), lw=1.8, label="RA (R / R*)")
A.semilogy(t, c, color=charts.line("enzyme"), lw=1.8, label="CYP26 (C / C*)")
A.axhline(1, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
A.axhline(0.8, color=charts.line("negative"), lw=0.7, ls=(0, (1, 1.5)))
A.text(150, 0.74, "20 % below steady state", fontsize=FT["tiny"], color=charts.line("negative"), ha="right", va="top")
A.set_ylim(0.1, 20)
A.set_xlim(0, 150)
A.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(A, "time / h", "relative level (log scale)")
charts.title(A, "A  A 6 h pulse of excess RA (U = 10)")

B = axs[1]
Us = np.linspace(0.5, 30, 40)
dip, dur = [], []
for U in Us:
    tt, rr, _ = run(U, 300.0)
    after = tt > 16
    dip.append(100 * (1 - rr[after].min()))
    dur.append(np.sum(rr[after] < 0.8) * (tt[1] - tt[0]))
B.plot(Us, dip, color=charts.line("negative"), lw=1.8, label="largest fall of R / %")
B.set_ylim(0, 100)
charts.style_axes(B, "pulse amplitude U", "largest fall of R below R* / %")
B2 = B.twinx()
B2.plot(Us, dur, color=charts.line("dna"), lw=1.8, ls=(0, (4, 2)))
B2.set_ylabel("time with R < 0.8 R* / h", fontsize=FT["small"], color=charts.line("dna"))
B2.tick_params(colors=P.muted(), labelcolor=P.ink(), labelsize=FT["tiny"])
for sp in ("top", "left", "bottom"):
    B2.spines[sp].set_visible(False)
B2.spines["right"].set_color(P.muted())
B.text(1, 92, "solid: depth of the deficit\ndashed: its duration", fontsize=FT["tiny"], color=P.ink(), va="top")
charts.title(B, "B  Larger doses, deeper and longer deficits")
