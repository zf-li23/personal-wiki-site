# Production-removal dynamics of a protein Y, dY/dt = beta - alpha Y, alpha = alpha_deg + alpha_dil.
# Time is measured in cell cycles; a stable protein is removed only by dilution, alpha = ln 2 per cell cycle.
# A: simple regulation. Production switched on at t = 0 (solid) or off (dashed), for a stable protein
#    (alpha = ln 2, response time T_1/2 = one cell cycle) and for a protein actively degraded with a half-life
#    of 0.2 cell cycle (alpha = 5 ln 2): the response time does not depend on beta.
# B: negative autoregulation, dY/dt = beta_max / (1 + (Y/K)^n) - alpha Y with n = 2, beta_max equal to
#    five times the production alpha Y* of simple regulation and K = 0.5 chosen so that both circuits reach the
#    same steady state Y* = 1: the strong initial production is cut back as Y approaches K, and half of Y* is
#    reached about five times faster than by simple regulation with the same
#    steady state (Rosenfeld, Elowitz and Alon, 2002, measured about fivefold with TetR). Turning off is not
#    accelerated: it is set by alpha.
# C: positive autoregulation, dY/dt = beta_0 + beta_1 Y^n / (K^n + Y^n) - alpha Y with n = 4, K = 1,
#    beta_0 = 0.05, beta_1 = 1.3, alpha = ln 2: production (solid) and removal (straight line) for the graphical
#    analysis of steady states. Three intersections: two stable (filled) and one unstable (open) steady state,
#    so the circuit is bistable and remembers its past (a cell switched on stays on).
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

import wikibio as bio
from wikibio import charts

P = bio.P
LN2 = np.log(2)
fig, axs = plt.subplots(1, 3, figsize=(13.0, 3.9))

ax = axs[0]
t = np.linspace(0, 4, 400)
for a, tok, name in ((LN2, "dna", "stable: removal by dilution"), (5 * LN2, "negative", "degraded, t½ = 0.2 cycle")):
    ax.plot(t, 1 - np.exp(-a * t), color=charts.line(tok), lw=1.8, label=name)
    ax.plot(t, np.exp(-a * t), color=charts.line(tok), lw=1.2, ls=(0, (4, 2.4)))
    th = LN2 / a
    ax.plot([th], [0.5], "o", color=charts.line(tok), ms=4.5)
ax.axhline(0.5, color=P.muted(), lw=0.6, ls=":")
ax.set_xlim(0, 4)
ax.set_ylim(0, 1.02)
ax.legend(fontsize=7, frameon=False, loc="center right")
charts.style_axes(ax, "t / cell cycles", "Y / Y*  (on: solid, off: dashed)")
ax.set_title("A   Response time T½ = ln 2 / α", loc="left", fontsize=9, color=P.ink())

ax = axs[1]
K, n = 1.0, 2
bmax = 5 * LN2  # five times the production rate alpha Y* of simple regulation
# choose K' so that Y* = 1: bmax / (1 + (1/K')^2) = ln 2 -> (1/K')^2 = bmax / ln 2 - 1
Kp = 1 / np.sqrt(bmax / LN2 - 1)
nar = solve_ivp(lambda tt, y: [bmax / (1 + (y[0] / Kp) ** n) - LN2 * y[0]], (0, 4), [0.0], t_eval=t, rtol=1e-8)
ax.plot(t, 1 - np.exp(-LN2 * t), color=charts.line("dna"), lw=1.8, label="simple regulation")
ax.plot(t, nar.y[0], color=charts.line("positive"), lw=1.8, label="negative autoregulation")
t_s = LN2 / LN2
t_n = t[np.argmax(nar.y[0] >= 0.5)]
ax.plot([t_s, t_n], [0.5, 0.5], "o", color=P.ink(), ms=3.5)
ax.text(t_n + 0.06, 0.56, f"T½ = {t_n:.2f}", fontsize=7, color=charts.line("positive"))
ax.text(t_s + 0.08, 0.42, "T½ = 1", fontsize=7, color=charts.line("dna"))
ax.axhline(0.5, color=P.muted(), lw=0.6, ls=":")
ax.set_xlim(0, 4)
ax.set_ylim(0, 1.1)
ax.legend(fontsize=7, frameon=False, loc="lower right")
charts.style_axes(ax, "t / cell cycles", "Y / Y*")
ax.set_title("B   Negative autoregulation speeds up", loc="left", fontsize=9, color=P.ink())

ax = axs[2]
b0, b1 = 0.05, 1.3
y = np.linspace(0, 2.6, 400)
prod = b0 + b1 * y ** 4 / (1 + y ** 4)
ax.plot(y, prod, color=charts.line("positive"), lw=1.8, label="production f(Y)")
ax.plot(y, LN2 * y, color=charts.line("negative"), lw=1.6, label="removal αY")
g = lambda yy: b0 + b1 * yy ** 4 / (1 + yy ** 4) - LN2 * yy
grid = np.linspace(1e-6, 2.6, 2000)
roots = [brentq(g, grid[i], grid[i + 1]) for i in range(len(grid) - 1) if g(grid[i]) * g(grid[i + 1]) < 0]
for k, r in enumerate(roots):
    stable = k != 1
    ax.plot([r], [LN2 * r], "o", ms=6, color=P.ink(), mfc=P.ink() if stable else P.surface())
ax.text(roots[0] + 0.1, LN2 * roots[0] - 0.12, "off", fontsize=7, color=P.ink())
ax.text(roots[2] + 0.06, LN2 * roots[2] - 0.17, "on", fontsize=7, color=P.ink())
ax.text(roots[1] + 0.06, LN2 * roots[1] - 0.2, "threshold\n(unstable)", fontsize=7, color=P.muted())
ax.set_xlim(0, 2.6)
ax.set_ylim(0, 1.8)
ax.legend(fontsize=7, frameon=False, loc="upper left")
charts.style_axes(ax, "Y (units of K)", "rate / (K per cell cycle)")
ax.set_title("C   Positive autoregulation: bistability", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
