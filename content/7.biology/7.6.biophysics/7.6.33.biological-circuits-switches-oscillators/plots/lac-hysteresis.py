"""A minimal model of the lac operon's positive feedback with a non-metabolizable inducer.
Expression x (relative to full induction) obeys dx/dt = 1/(1 + rho/(1 + y^2)) - x, where
rho = 200 is the repression factor of LacI and y = T (delta + x) is the internal inducer, imported
by the permease LacY (proportional to x) plus a small leak delta = 0.01, with the external inducer T
in units of the repressor's inducer affinity. A: production (curves) and dilution (line) on
logarithmic axes for T = 20, 40 and 70; at T = 40 three fixed points. B: steady states against T
(solid: stable, dashed: unstable) and the states reached by cells that start uninduced (rising
sweep) or fully induced (falling sweep): the two histories differ between T = 28 and 58."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P = bio.P
rho, delta = 200.0, 0.01
prod = lambda x, T: 1 / (1 + rho / (1 + (T * (delta + x)) ** 2))

fig, axs = plt.subplots(1, 2, figsize=(9.0, 3.4))
fig.subplots_adjust(wspace=0.3, left=0.08, right=0.98, bottom=0.17, top=0.88)
ax = axs[0]
x = np.logspace(-3.2, 0.1, 400)
ax.plot(x, x, color=P.ink(), lw=1.2, label="dilution x")
for T, tok in ((20, "dna"), (40, "protein"), (70, "blood")):
    ax.plot(x, prod(x, T), color=charts.line(tok), lw=1.5, label=f"production, T = {T}")
ax.set_xscale("log")
ax.set_yscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "expression x", "rate")
charts.title(ax, "A  Three fixed points at T = 40")

ax = axs[1]
Ts = np.logspace(0.8, 2.3, 400)
xx = np.logspace(-4, 0.1, 40000)
for T in Ts:
    g = prod(xx, T) - xx
    idx = np.where(np.sign(g[1:]) != np.sign(g[:-1]))[0]
    for i in idx:
        st = g[i] > 0
        ax.plot(T, xx[i], ".", ms=1.5, color=charts.line("protein") if st else P.muted())
up, down = [], []
xs = 0.0
for T in Ts:
    xs = solve_ivp(lambda t, y: prod(y, T) - y, (0, 60), [xs], rtol=1e-8).y[0, -1]
    up.append(xs)
xs = 1.0
for T in Ts[::-1]:
    xs = solve_ivp(lambda t, y: prod(y, T) - y, (0, 60), [xs], rtol=1e-8).y[0, -1]
    down.append(xs)
ax.plot(Ts, up, color=charts.line("dna"), lw=1.0, label="from uninduced")
ax.plot(Ts[::-1], down, color=charts.line("blood"), lw=1.0, label="from induced")
ax.set_xscale("log")
ax.set_yscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "external inducer T", "steady expression x*")
charts.title(ax, "B  Hysteresis")
