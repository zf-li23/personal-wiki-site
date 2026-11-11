"""Two-variable models of the action potential. A: the Rinzel reduction of the Hodgkin-Huxley model:
m = m_inf(V) and h = 0.89 - 1.1 n turn the four-variable model into a planar system in (V, n). Shown:
the nullclines of the reduced system (I = 0, rest -65 mV), the projection of the full 4D HH trajectory after
a 20 uA/cm2, 0.5 ms pulse in grey, and the trajectory of the reduced model
started from the same state after the pulse (colour). B: voltage of the full and the reduced model.
C: FitzHugh-Nagumo model dv/dt = v - v^3/3 - w + I, dw/dt = 0.08 (v + 0.7 - 0.8 w): nullclines for
I = 0 (rest) and I = 0.5 (limit cycle), and the limit cycle (relaxation oscillation).
D: time courses of v for I = 0 with a pulse, and for I = 0.5."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts, neuro

P = bio.P
FT = bio.core.FONT
p = neuro.HH
fig, axs = plt.subplots(2, 2, figsize=(10.0, 6.0))
fig.subplots_adjust(wspace=0.3, hspace=0.5, left=0.07, right=0.99, bottom=0.09, top=0.93)


def rinzel(t, y, I):
    V, n = y
    m, _, _ = neuro.hh_steady(V)
    h = 0.89 - 1.1 * n
    am, bm, ah, bh, an, bn = neuro.hh_rates(V)
    iion = p["gNa"] * m**3 * h * (V - p["ENa"]) + p["gK"] * n**4 * (V - p["EK"]) + p["gL"] * (V - p["EL"])
    return [I - iion, an * (1 - n) - bn * n]


# full HH after a pulse
t = np.arange(0, 20, 0.01)
I = np.where((t >= 1) & (t < 1.5), 20.0, 0.0)
Vf, mf, hf, nf = neuro.hh_simulate(I[:, None], t)
Vf, mf, hf, nf = Vf[:, 0], mf[:, 0], hf[:, 0], nf[:, 0]
k = int(1.5 / 0.01)
s = solve_ivp(rinzel, [0, 18.5], [Vf[k], nf[k]], args=(0.0,), max_step=0.01, rtol=1e-8)

ax = axs[0, 0]
V = np.linspace(-85, 60, 500)
m, _, ninf = neuro.hh_steady(V)
n_nc = ninf
# V-nullcline of reduced system: solve for n at each V (monotone in n)
from scipy.optimize import brentq
vn = []
for v in V:
    mm = float(neuro.hh_steady(v)[0])
    g = lambda n: -(p["gNa"] * mm**3 * (0.89 - 1.1 * n) * (v - p["ENa"]) + p["gK"] * n**4 * (v - p["EK"]) + p["gL"] * (v - p["EL"]))
    try:
        vn.append(brentq(g, -0.5, 1.5))
    except ValueError:
        vn.append(np.nan)
ax.plot(V, vn, color=charts.line("neuron"), lw=1.5, label="$V$-nullcline")
ax.plot(V, n_nc, color=charts.line("highlight"), lw=1.5, label="$n$-nullcline")
ax.plot(Vf[k:], nf[k:], color=P.muted(), lw=2.2, label="full HH (projected)")
ax.plot(s.y[0], s.y[1], color=charts.line("blood"), lw=1.2, label="reduced model")
ax.set_xlim(-85, 60); ax.set_ylim(0.2, 0.85)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "$V$ / mV", "$n$")
charts.title(ax, "A  Rinzel reduction of the HH model")

ax = axs[0, 1]
ax.plot(t[k:] - 1.5, Vf[k:], color=P.muted(), lw=2.2, label="full HH")
ax.plot(s.t, s.y[0], color=charts.line("blood"), lw=1.2, label="reduced")
ax.set_xlim(0, 18)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "time after pulse / ms", "$V$ / mV")
charts.title(ax, "B  The reduction keeps the spike")


def fhn(t, y, I):
    v, w = y
    return [v - v**3 / 3 - w + I, 0.08 * (v + 0.7 - 0.8 * w)]


ax = axs[1, 0]
v = np.linspace(-2.6, 2.6, 400)
for I, tok in [(0.0, "neuron"), (0.5, "negative")]:
    ax.plot(v, v - v**3 / 3 + I, color=charts.line(tok), lw=1.5, label=f"$v$-nullcline, $I = {I}$")
ax.plot(v, (v + 0.7) / 0.8, color=charts.line("highlight"), lw=1.5, label="$w$-nullcline")
y0 = [-1.2, -0.62]
s1 = solve_ivp(fhn, [0, 30], [-0.4, -0.625], args=(0.0,), max_step=0.02)
s2 = solve_ivp(fhn, [0, 200], [-1.0, 0.0], args=(0.5,), max_step=0.02)
sel = s2.t > 100
ax.plot(s1.y[0], s1.y[1], color=charts.line("dna"), lw=1.3)
ax.plot(s2.y[0][sel], s2.y[1][sel], color=charts.line("blood"), lw=1.3)
ax.set_xlim(-2.6, 2.6); ax.set_ylim(-1.5, 2.5)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "$v$", "$w$")
charts.title(ax, "C  FitzHugh-Nagumo model")

ax = axs[1, 1]
ax.plot(s1.t, s1.y[0], color=charts.line("dna"), lw=1.3, label="$I = 0$, pulse to $v = -0.4$")
ax.plot(s2.t[sel] - 100, s2.y[0][sel], color=charts.line("blood"), lw=1.3, label="$I = 0.5$")
ax.set_xlim(0, 100); ax.set_ylim(-2.3, 2.9)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right", ncol=2)
charts.style_axes(ax, "t", "$v$")
charts.title(ax, "D  Excitable and oscillating regimes")
