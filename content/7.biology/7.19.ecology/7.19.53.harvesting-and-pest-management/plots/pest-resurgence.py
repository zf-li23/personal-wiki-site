"""Pest resurgence and secondary pest outbreaks in a pest-enemy model (Section 53.3.2).

Pest N with logistic growth, natural enemy P with a linear functional response:
    dN/dt = r N (1 - N/K) - a N P,   dP/dt = c a N P - m P,
r = 1, K = 10, a = 1, c = 0.5, m = 1, with an economic injury level EIL = 4 (dashed);
unsprayed equilibrium N* = m/(ca) = 2, P* = (r/a)(1 - N*/K) = 0.8.
A: one insecticide application at t = 20 kills 90% of the pests and either 95% of the enemies
(broad-spectrum) or none (selective). B: equilibrium pest density under continuous spraying with
extra per capita mortality s on the pest and 1.5 s on the enemy (broad) or 0 (selective),
Proposition 53.3.2: N* = (m + h_E)/(ca) while the enemy persists, otherwise K (1 - h_N / r).
C: a secondary pest with the same parameters and its own enemy; sprays every 8 time units aimed at
the key pest kill 20% of the secondary pest and 95% of its enemy.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
cb, cs, cn, ce = C.line("negative"), C.line("dna"), C.line("plant"), C.line("protein")
r, K, a, c, m = 1.0, 10.0, 1.0, 0.5, 1.0
EIL = 4.0


def rhs(t, y):
    n, p = y
    return [r * n * (1 - n / K) - a * n * p, c * a * n * p - m * p]


def pulsed(times, kill_n, kill_p, t_end, y0=(2.0, 0.8)):
    ts, ys = [], []
    y = np.array(y0, float)
    t0 = 0.0
    for tk in list(times) + [t_end]:
        s = solve_ivp(rhs, (t0, tk), y, max_step=0.05)
        ts.append(s.t)
        ys.append(s.y)
        y = s.y[:, -1].copy()
        if tk < t_end:
            y *= [1 - kill_n, 1 - kill_p]
        t0 = tk
    return np.concatenate(ts), np.concatenate(ys, axis=1)


fig, axes = plt.subplots(1, 3, figsize=(13, 3.9))
ax = axes[0]
for kp, col, lab in ((0.95, cb, "broad-spectrum (enemies −95%)"), (0.0, cs, "selective (enemies spared)")):
    t, y = pulsed([20.0], 0.9, kp, 60.0)
    ax.plot(t, y[0], color=col, lw=2, label=lab)
ax.axhline(EIL, color=P.muted(), lw=0.9, ls=(0, (4, 2)))
ax.text(59, EIL + 0.15, "EIL", color=P.muted(), fontsize=FS["tiny"], ha="right")
ax.axhline(2, color=P.muted(), lw=0.6, ls=":")
ax.annotate("spray", (20, 0.3), (24, 1.0), fontsize=FS["tiny"], color=P.ink(),
            arrowprops=dict(arrowstyle="-|>", color=P.muted(), lw=0.9))
ax.set_xlim(0, 60)
ax.set_ylim(0, 9)
C.style_axes(ax, "time (units of 1/r)", "pest density")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
C.title(ax, "A  Resurgence after one application")

ax = axes[1]
s = np.linspace(0, 1, 400)
for sig, col, lab in ((1.5, cb, "broad-spectrum"), (0.0, cs, "selective")):
    hN, hE = s, sig * s
    with_enemy = (m + hE) / (c * a)
    no_enemy = np.clip(K * (1 - hN / r), 0, None)
    ax.plot(s, np.minimum(with_enemy, no_enemy), color=col, lw=2.2, label=lab)
ax.plot(s, np.clip(K * (1 - s / r), 0, None), color=P.muted(), lw=1, ls=":", label="no enemies")
ax.axhline(EIL, color=P.muted(), lw=0.9, ls=(0, (4, 2)))
ax.set_xlim(0, 1)
ax.set_ylim(0, 10.5)
C.style_axes(ax, "spray mortality on the pest, h_N (units of r)", "equilibrium pest density N*")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
C.title(ax, "B  Continuous spraying (Proposition 53.3.2)")

ax = axes[2]
sprays = np.arange(10.0, 60.0, 8.0)
t, y = pulsed(sprays, 0.2, 0.95, 70.0)
ax.plot(t, y[0], color=cb, lw=2, label="secondary pest")
ax.plot(t, 2 * y[1], color=ce, lw=1.2, label="its enemy (×2)")
for tk in sprays:
    ax.axvline(tk, color=P.muted(), lw=0.5, ls=":")
ax.axhline(EIL, color=P.muted(), lw=0.9, ls=(0, (4, 2)))
ax.text(69, EIL + 0.15, "EIL", color=P.muted(), fontsize=FS["tiny"], ha="right")
ax.set_xlim(0, 70)
ax.set_ylim(0, 11)
C.style_axes(ax, "time (sprays against the key pest dotted)", "density")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
C.title(ax, "C  A secondary pest outbreak")
fig.tight_layout()
