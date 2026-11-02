"""The incoherent type-1 feed-forward loop (I1-FFL): X activates Z and its repressor Y.

A: logic input functions, complete repression (dY/dt = 1 - Y, dZ/dt = theta(Y < 0.5) - Z after an ON
step of Sx at t = 0): Z rises until Y crosses its threshold at t = ln 2 and then decays: a pulse.
B: Hill input functions, partial repression: dY/dt = 1 - Y, dZ/dt = beta g(Y) - Z with
g(Y) = 1/F + (1 - 1/F)/(1 + (Y/K)^2), F = 5, K = 0.1, beta = 1/g(1) so that Z_st = 1. The I1-FFL reaches
half of its steady state at t = 0.156, simple regulation (dZ/dt = 1 - Z) at ln 2 = 0.693: 4.4-fold faster.
C: steady-state dose response. Z_st = [X/(0.1 + X)] / (1 + (Y/0.3)^2) with Y = X/(10 + X) (activation of Z
at a lower threshold than of Y): a biphasic (inverse-U) response, which becomes monotonic when the
repressor's site is deleted.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P = bio.P
col_y, col_z, col_s = charts.line("protein"), charts.line("positive"), P.muted()
fig, axes = plt.subplots(1, 3, figsize=(11, 3.4))
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.17, top=0.86, wspace=0.32)

ax = axes[0]
dt = 1e-3
t = np.arange(0, 6, dt)
Y = 1 - np.exp(-t)
Z = np.zeros_like(t)
for i in range(1, len(t)):
    Z[i] = Z[i - 1] + dt * (float(Y[i - 1] < 0.5) - Z[i - 1])
ax.plot(t, Y, color=col_y, lw=1.4, label="Y (repressor)")
ax.plot(t, Z, color=col_z, lw=1.8, label="Z")
ax.axhline(0.5, color=P.muted(), lw=0.7, ls=":")
ax.text(5.9, 0.53, "K_YZ", fontsize=7, color=P.ink(), ha="right")
ax.set_ylim(0, 1.3)
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "time after ON step (1/alpha)", "level")
charts.title(ax, "A  Complete repression: a pulse")

ax = axes[1]
F, K = 5.0, 0.1
g = lambda y: 1 / F + (1 - 1 / F) / (1 + (y / K) ** 2)
beta = 1 / g(1.0)
s = solve_ivp(lambda tt, z: [1 - z[0], beta * g(z[0]) - z[1]], (0, 5), [0, 0], max_step=0.001, dense_output=True)
tt = np.linspace(0, 5, 50001)
Zf = s.sol(tt)[1]
Zs = 1 - np.exp(-tt)
t_ffl = tt[np.argmax(Zf >= 0.5)]
ax.plot(tt, Zs, color=col_s, lw=1.3, ls="--", label="simple regulation")
ax.plot(tt, Zf, color=col_z, lw=1.8, label="I1-FFL")
ax.axhline(0.5, color=P.muted(), lw=0.7, ls=":")
for x, lab in [(t_ffl, f"{t_ffl:.2f}"), (np.log(2), "0.69")]:
    ax.plot([x, x], [0, 0.5], color=P.muted(), lw=0.7)
    ax.text(x + 0.04, 0.03, lab, fontsize=7, color=P.ink())
ax.set_ylim(0, 1.3)
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "time after ON step (1/alpha)", "Z / Z_st")
charts.title(ax, "B  Partial repression: faster response")

ax = axes[2]
X = np.logspace(-2, 3, 400)
act = X / (0.1 + X)
Yst = X / (10 + X)
ax.semilogx(X, act / act.max(), color=col_s, lw=1.3, ls="--", label="repressor site deleted")
zz = act / (1 + (Yst / 0.3) ** 2)
ax.semilogx(X, zz / act.max(), color=col_z, lw=1.8, label="I1-FFL")
ax.set_ylim(0, 1.2)
ax.legend(fontsize=7, frameon=False, loc="upper left")
charts.style_axes(ax, "input X (arbitrary units)", "steady-state Z")
charts.title(ax, "C  Biphasic dose response")
