"""Dynamical compensation in a beta-cell-insulin-glucose (BIG) model with illustrative parameters:
dG/dt = m(t) - s I G, dI/dt = q B G^2 - gamma I (time in hours, gamma = 2 per hour, basal input
m0 = 5 mM per hour, a meal adds 10 mM with time constant 0.5 h), and on the time scale of days
dB/dt = B mu(G) with mu(G0) = 0 at G0 = 5 mM (mu0 = 0.1 per day; second zero at 12 mM).
A: meal responses of the minimal model (beta-cell mass B fixed) for insulin sensitivity s = 1, 0.5 and
0.1: the fasting level rises as s^(-1/3) and the excursion grows.
B: insulin sensitivity halves on day 10. Fasting glucose jumps to 6.3 mM and returns to 5 mM over
weeks as the beta-cell mass doubles (glucose and insulin on the fast time scale are at their
quasi-steady state).
C: meal responses before the drop (day 0), during the transient (day 12) and after compensation
(day 150): glucose (solid) is the same before and after; insulin (dashed, right axis) is twice as high."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P = bio.P
G0, G1, m0, gam, mu0 = 5.0, 12.0, 5.0, 2.0, 0.1
qB1 = gam * (m0 / G0) / G0**2


def mu(G):
    return mu0 * (G / G0 - 1) * (1 - G / G1) * G1 / (G1 - G0)


def meal_run(s, qB, T=6.0):
    Gs = (m0 * gam / (s * qB)) ** (1 / 3)
    Is = m0 / (s * Gs)

    def rhs(t, z):
        G, I = z
        return [m0 + 10.0 * np.exp(-t / 0.5) / 0.5 - s * I * G, qB * G**2 - gam * I]

    t = np.linspace(0, T, 300)
    r = solve_ivp(rhs, (0, T), [Gs, Is], t_eval=t, rtol=1e-8, atol=1e-10)
    return t, r.y[0], r.y[1]


fig, axs = plt.subplots(1, 3, figsize=(11, 3.4))
fig.subplots_adjust(left=0.06, right=0.94, bottom=0.17, top=0.86, wspace=0.42)

ax = axs[0]
for s, tok in [(1.0, "protein"), (0.5, "highlight"), (0.1, "negative")]:
    t, G, _ = meal_run(s, qB1)
    ax.plot(t, G, color=charts.line(tok), lw=1.5, label=f"s = {s:g}")
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "time after meal (h)", "glucose G (mM)")
charts.title(ax, "A  Minimal model, fixed B")


def slow(t, z):
    s = 1.0 if t < 10 else 0.5
    G = (m0 * gam / (s * qB1 * np.exp(z[0]))) ** (1 / 3)
    return [mu(G)]


ts = np.linspace(0, 150, 1501)
r = solve_ivp(slow, (0, 150), [0.0], t_eval=ts, max_step=0.1, rtol=1e-9)
B = np.exp(r.y[0])
sv = np.where(ts < 10, 1.0, 0.5)
Gq = (m0 * gam / (sv * qB1 * B)) ** (1 / 3)
ax = axs[1]
ax.plot(ts, Gq, color=charts.line("negative"), lw=1.5, label="fasting glucose (mM)")
ax.plot(ts, 5 * B, color=charts.line("protein"), lw=1.5, label="5 x beta-cell mass B")
ax.axvline(10, color=P.muted(), lw=0.7, ls=":")
ax.text(11, 9.2, "s halves", fontsize=7, color=P.muted())
ax.set_ylim(4, 10.5)
ax.legend(fontsize=7, frameon=False, loc="lower right")
charts.style_axes(ax, "time (days)", "level")
charts.title(ax, "B  Slow compensation by beta cells")

ax = axs[2]
axr = ax.twinx()
for day, tok in [(0, "protein"), (12, "highlight"), (150, "positive")]:
    s = 1.0 if day < 10 else 0.5
    qB = qB1 * np.interp(day, ts, B)
    t, G, I = meal_run(s, qB)
    ax.plot(t, G, color=charts.line(tok), lw=1.8 if day != 150 else 1.2, label=f"day {day}")
    axr.plot(t, I, "--", color=charts.line(tok), lw=1.0)
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "time after meal (h)", "glucose G (mM)")
charts.style_axes(axr, None, "insulin I (dashed)", box=True)
charts.title(ax, "C  Same glucose, more insulin")
