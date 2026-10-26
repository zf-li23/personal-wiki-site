# Switching a gene on: the two-stage model of 7.2.22 with a delay,
#   dm/dt = k_m H(t - tau) - (k_deg,m + mu) m,   dp/dt = k_p m - (k_deg,p + mu) p,
# where H is the unit step, tau the time from promoter activation to the first translatable mRNA, and
# mu = ln 2 / (doubling time) the dilution by growth. Curves are normalized to their steady states, so
# k_m and k_p drop out. Parameters are the round numbers stated in the course (7.2.1, 7.2.18, 7.2.22):
# A, an E. coli gene: tau = 0.5 min (a 1 kb gene takes about 20-50 s, and ribosomes translate the mRNA
#    while it is being made), mRNA half-life 3 min, a stable protein removed only by dilution, doubling 30 min;
# B, a human gene: tau = 30 min (a median 25 kb gene at 2.4 kb/min takes about 10 min, processing and export
#    another tens of minutes), mRNA half-life 9 h, protein half-life 2 d, doubling 24 h (solid); dashed, a
#    short-lived regulator with mRNA half-life 1 h and protein half-life 1 h, same delay.
# Dots mark the time at which each curve reaches half of its steady state.
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

P = bio.P
LN2 = np.log(2)


def run(tau, tm, tp, td, tmax):
    mu = LN2 / td
    am = LN2 / tm + mu
    ap = (LN2 / tp if tp else 0.0) + mu
    t = np.linspace(0, tmax, 3000)

    def f(tt, y):
        m, p = y
        return [(1.0 if tt >= tau else 0.0) - am * m, m - ap * p]

    s = solve_ivp(f, (0, tmax), [0.0, 0.0], t_eval=t, max_step=tmax / 2000, rtol=1e-8)
    m, p = s.y[0] * am, s.y[1] * am * ap  # normalize by the steady states 1/am and 1/(am ap)
    return t, m, p


def half(t, y):
    return t[np.argmax(y >= 0.5)]


fig, axs = plt.subplots(1, 2, figsize=(11.0, 3.9))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.16, top=0.86, wspace=0.25)

ax = axs[0]
t, m, p = run(0.5, 3.0, None, 30.0, 150.0)
for y, tok, name in ((m, "mrna", "mRNA"), (p, "protein", "protein")):
    ax.plot(t, y, color=charts.line(tok), lw=1.8, label=name)
    th = half(t, y)
    ax.plot([th], [0.5], "o", color=charts.line(tok), ms=4.5)
    ax.text(th + 3, 0.44, f"{th:.0f} min", fontsize=7, color=charts.line(tok), va="top")
ax.axhline(0.5, color=P.muted(), lw=0.6, ls=":")
ax.set_xlim(0, 150)
ax.set_ylim(0, 1.05)
ax.legend(fontsize=7, frameon=False, loc="lower right")
charts.style_axes(ax, "t / min", "level / steady state")
ax.set_title("A   $\\mathit{E.\\ coli}$ gene: the protein follows dilution", loc="left", fontsize=9, color=P.ink())

ax = axs[1]
t, m, p = run(0.5, 9.0, 48.0, 24.0, 120.0)
t2, m2, p2 = run(0.5, 1.0, 1.0, 24.0, 120.0)
for y, tok, name, ls in ((m, "mrna", "mRNA", "-"), (p, "protein", "protein", "-"), (m2, "mrna", "mRNA, regulator", "--"),
                         (p2, "protein", "protein, regulator", "--")):
    ax.plot(t, y if ls == "-" else y, color=charts.line(tok), lw=1.8 if ls == "-" else 1.2, ls=ls if ls == "-" else (0, (4, 2.4)),
            label=name)
for y, tok, dx, dy in ((m, "mrna", 2, -0.06), (p, "protein", 2, -0.06), (p2, "protein", 2, 0.12)):
    th = half(t, y)
    ax.plot([th], [0.5], "o", color=charts.line(tok), ms=4.5)
    ax.text(th + dx, 0.5 + dy, f"{th:.1f} h" if th < 10 else f"{th:.0f} h", fontsize=7, color=charts.line(tok), va="top" if dy < 0 else "bottom")
ax.axhline(0.5, color=P.muted(), lw=0.6, ls=":")
ax.set_xlim(0, 120)
ax.set_ylim(0, 1.05)
ax.set_xticks([0, 24, 48, 72, 96, 120])
ax.legend(fontsize=7, frameon=False, loc="lower right")
charts.style_axes(ax, "t / h", "level / steady state")
ax.set_title("B   Human gene: hours to days, unless products are unstable", loc="left", fontsize=9, color=P.ink())
