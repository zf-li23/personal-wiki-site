# A three-level model of the hypothalamus-pituitary-thyroid axis (all variables relative to the normal
# steady state; time in days):
#   dR/dt = kR (u / (1 + (T/KR)^2) * cR - R)        TRH, half-life ~5 min
#   dS/dt = kS (R / (1 + (T/KS)^4) * cS - S)        TSH, half-life ~1 h; pituitary feedback is steep
#   dT/dt = kT (g S - T) + dose                     T4 (free), half-life 7 d; g = thyroid capacity
# KR = 0.7, KS = 0.5 put the normal state on the steep part of the feedback curves (TSH can rise ~50-fold).
# The constants cR, cS make R = S = T = 1 at g = 1. Feedback acts on both the TRH neurons and,
# more strongly, the thyrotrophs, as in the long feedback loop. Parameters are illustrative.
# A: thyroid capacity falls to 40 % at day 10 (autoimmune thyroiditis): TSH rises and largely restores T4.
# B: total thyroidectomy at day 10 (g = 0), then a constant levothyroxine replacement from day 60.
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

P = bio.P
kR = np.log(2) / (5 / 1440)
kS = np.log(2) / (1 / 24)
kT = np.log(2) / 7.0
KR, KS = 0.7, 0.5
cR = 1 + (1 / KR) ** 2
cS = 1 + (1 / KS) ** 4


def rhs(t, y, g, dose):
    R, S, T = y
    return [kR * (cR / (1 + (T / KR) ** 2) - R),
            kS * (R * cS / (1 + (T / KS) ** 4) - S),
            kT * (g(t) * S - T) + dose(t)]


def run(g, dose, t_end=120):
    sol = solve_ivp(rhs, (0, t_end), [1, 1, 1], args=(g, dose), method="LSODA", max_step=0.05,
                    rtol=1e-7, atol=1e-9, dense_output=True)
    t = np.linspace(0, t_end, 2000)
    return t, sol.sol(t)


fig, ax = bio.canvas(24.0, 9.6)
cases = [
    ("A", "Partial loss of thyroid capacity (g → 0.4)", lambda t: 1.0 if t < 10 else 0.4, lambda t: 0.0),
    ("B", "Thyroidectomy, then T4 replacement", lambda t: 1.0 if t < 10 else 0.0,
     lambda t: kT * 1.0 if t >= 60 else 0.0),
]
for col, (letter, title, g, dose) in enumerate(cases):
    x0 = 2.2 + 12.4 * col
    bio.panel(ax, letter, (x0 - 2.0, 9.5))
    p = charts.axes_at(ax, (x0, 1.5, 8.8, 6.9))
    t, (R, S, T) = run(g, dose)
    p.semilogy(t, S, color=charts.line("dna"), lw=1.8, label="TSH")
    p.semilogy(t, R, color=charts.line("protein"), lw=1.2, ls="--", label="TRH")
    p.semilogy(t, np.maximum(T, 1e-3), color=charts.line("positive"), lw=1.8, label="T4 (free)")
    p.axvline(10, color=P.muted(), lw=0.7, ls=":")
    if col == 1:
        p.axvline(60, color=P.muted(), lw=0.7, ls=":")
        p.text(61, 0.012, "replacement\nstarts", fontsize=7.0, color=P.muted(), va="bottom")
    p.text(11, 0.012 if col else 0.35, "thyroid capacity\nchanged", fontsize=7.0, color=P.muted(), va="bottom")
    leg = p.legend(loc="upper right", fontsize=7.3, frameon=False)
    for txt in leg.get_texts():
        txt.set_color(P.ink())
    p.set_xlim(0, 120)
    p.set_ylim(0.01, 100) if col else p.set_ylim(0.3, 10)
    charts.style_axes(p, "time / d", "relative to normal (log)")
    charts.title(p, title)
    if col == 0:
        p.text(118, T[-1] * 0.9, f"T4 settles at {T[-1]:.2f}", fontsize=7.2, color=charts.line("positive"),
               ha="right", va="top")
        p.text(118, S[-1] * 1.08, f"TSH settles at {S[-1]:.1f}", fontsize=7.2, color=charts.line("dna"),
               ha="right", va="bottom")
