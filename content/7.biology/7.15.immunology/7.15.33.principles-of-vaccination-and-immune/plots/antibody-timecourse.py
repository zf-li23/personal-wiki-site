# Antibody titre after passive and active immunisation (phenomenological model, illustrative parameters).
# Each antigen dose k given at time t_k adds a response
#   a_k (1 - exp(-(t - t_k)/tau_r)) [ (1 - phi_k) exp(-ln2 (t - t_k)/T_s) + phi_k exp(-ln2 (t - t_k)/T_l) ],
# a short-lived component (short-lived plasma cells, half-life T_s = 30 d) and a long-lived component (long-lived plasma
# cells, T_l = 730 d); tau_r = 4 d sets the rise to the peak. A passive dose of IgG just decays with the IgG half-life
# of 21 d (FcRn recycling). Titres are relative units; the dashed line is an assumed protective threshold (10).
#   dose 1 (prime):          a = 100,  phi = 0.10
#   boost after 4 weeks:     a = 600,  phi = 0.25
#   boost after 6 months:    a = 2500, phi = 0.35   (more affinity maturation, less antibody left to mask the antigen)
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
TS, TL, TAU, T_IGG, THR = 30.0, 730.0, 4.0, 21.0, 10.0


def dose(t, t0, a, phi):
    d = np.clip(t - t0, 0, None)
    return np.where(t >= t0, a * (1 - np.exp(-d / TAU)) * ((1 - phi) * np.exp(-np.log(2) * d / TS)
                                                           + phi * np.exp(-np.log(2) * d / TL)), 0.0)


def passive(t, a=100.0):
    return np.where(t >= 0, a * np.exp(-np.log(2) * np.clip(t, 0, None) / T_IGG), 0.0)


t = np.linspace(0, 720, 4000)
prime = dose(t, 0, 100, 0.10)
boost28 = prime + dose(t, 28, 600, 0.25)
boost180 = prime + dose(t, 180, 2500, 0.35)

fig, axs = plt.subplots(1, 2, figsize=(10, 3.6))
ax = axs[0]
ax.plot(t, np.maximum(passive(t), 1e-1), color=charts.line("enzyme"), lw=1.6, label="passive (IgG transfer)")
ax.plot(t, prime, color=charts.line("protein"), lw=1.6, label="active, one dose")
ax.axhline(THR, color=P.edge("negative"), lw=0.9, ls="--")
ax.text(355, THR * 1.15, "assumed protective threshold", fontsize=7, color=P.edge("negative"), ha="right")
ax.set_yscale("log")
ax.set_ylim(1, 300)
ax.set_xlim(0, 360)
ax.legend(frameon=False, fontsize=7, labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, "time / days", "antibody titre (relative, log scale)")
charts.title(ax, "A")

ax = axs[1]
ax.plot(t, prime, color=charts.line("protein"), lw=1.2, ls=":", label="one dose")
ax.plot(t, boost28, color=charts.line("receptor"), lw=1.6, label="boost at 4 weeks")
ax.plot(t, boost180, color=charts.line("negative"), lw=1.6, label="boost at 6 months")
ax.axhline(THR, color=P.edge("negative"), lw=0.9, ls="--")
ax.set_yscale("log")
ax.set_ylim(1, 5000)
ax.set_xlim(0, 720)
ax.legend(frameon=False, fontsize=7, labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "time / days", "antibody titre (relative, log scale)")
charts.title(ax, "B")
fig.tight_layout()
