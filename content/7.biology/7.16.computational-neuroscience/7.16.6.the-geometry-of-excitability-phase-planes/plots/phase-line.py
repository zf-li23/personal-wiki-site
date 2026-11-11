"""One-dimensional dynamics of the persistent sodium model (Izhikevich 2007, Eq. 3.1 form): C dV/dt =
I - g_L (V - E_L) - g_Na m_inf(V) (V - E_Na) with m_inf a Boltzmann function (V_1/2 = -20 mV, k = 15 mV),
C = 1, E_L = -80, g_L = 8, g_Na = 20, E_Na = 60 (mV, mS/cm2, uA/cm2). A: the right-hand side F(V) for three
values of I: its zeros are equilibria, the sign gives the flow (arrows). B: bifurcation diagram, V* against
I: stable and unstable equilibria; two saddle-node bifurcations bound a bistable range.
C: time courses for I = 0 starting at V(0) just below and just above the threshold equilibrium (-56.5 mV):
the voltage either returns to rest or jumps to the depolarized equilibrium."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
EL, gL, gNa, ENa = -80.0, 8.0, 20.0, 60.0
minf = lambda V: 1 / (1 + np.exp((-20 - V) / 15))
F = lambda V, I: I - gL * (V - EL) - gNa * minf(V) * (V - ENa)
dF = lambda V, I: (F(V + 1e-4, I) - F(V - 1e-4, I)) / 2e-4


def equilibria(I):
    Vs = np.linspace(-90, 60, 3001); g = F(Vs, I)
    return [brentq(lambda V: F(V, I), Vs[i], Vs[i + 1]) for i in range(len(Vs) - 1) if g[i] * g[i + 1] < 0]


fig, axs = plt.subplots(1, 3, figsize=(10.4, 3.3))
fig.subplots_adjust(wspace=0.34, left=0.06, right=0.99, bottom=0.17, top=0.88)
V = np.linspace(-90, 40, 600)

ax = axs[0]
for I, tok, lab in [(-20, "neutral", "$I = -20$"), (0, "neuron", "$I = 0$"), (10, "highlight", "$I = 10$")]:
    ax.plot(V, F(V, I), color=charts.line(tok), lw=1.5, label=lab)
    for e in equilibria(I):
        ax.plot([e], [0], "o", ms=5, mfc=("white" if dF(e, I) > 0 else charts.line(tok)), mec=charts.line(tok), zorder=5)
ax.axhline(0, color=P.muted(), lw=0.7)
for x0, x1 in [(-90, -68), (-60, -64), (-54, 15), (22, 18)]:
    pass
ax.set_ylim(-250, 250)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "$V$ / mV", "$C\\,\\mathrm{d}V/\\mathrm{d}t$ / $\\mu$A cm$^{-2}$")
charts.title(ax, "A  Right-hand side and equilibria")

ax = axs[1]
Is = np.linspace(-130, 20, 1200)
stable, unstable = [], []
for I in Is:
    for e in equilibria(I):
        (stable if dF(e, I) < 0 else unstable).append((I, e))
st, un = np.array(stable), np.array(unstable)
ax.plot(st[:, 0], st[:, 1], ".", ms=1.6, color=charts.line("neuron"))
ax.plot(un[:, 0], un[:, 1], ".", ms=1.0, color=charts.line("negative"))
ax.plot([], [], "o", ms=3, color=charts.line("neuron"), label="stable")
ax.plot([], [], "o", ms=3, color=charts.line("negative"), label="unstable")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center left", bbox_to_anchor=(0.0, 0.62))
charts.style_axes(ax, "$I$ / $\\mu$A cm$^{-2}$", "equilibrium $V^*$ / mV")
charts.title(ax, "B  Two saddle-node bifurcations")

ax = axs[2]
for V0, tok in [(-60, "neutral"), (-57, "dna"), (-56, "highlight"), (-55, "blood"), (-50, "negative")]:
    s = solve_ivp(lambda t, y: [F(y[0], 0.0)], [0, 4], [V0], max_step=0.01)
    ax.plot(s.t, s.y[0], color=charts.line(tok), lw=1.3, label=f"$V(0) = {V0}$")
ax.axhline(equilibria(0.0)[1], color=P.muted(), lw=0.7, ls=":")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(ax, "t / ms", "$V$ / mV")
charts.title(ax, "C  Threshold at the unstable equilibrium")
