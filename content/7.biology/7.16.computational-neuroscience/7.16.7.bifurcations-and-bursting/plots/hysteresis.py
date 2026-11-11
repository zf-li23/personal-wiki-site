"""Bistability and hysteresis near a subcritical Andronov-Hopf bifurcation, in the persistent sodium plus
potassium model with a low-threshold K+ current (Izhikevich 2007, Eqs. 4.1-4.2; parameters as panel C of
the bifurcation figure: E_L = -78, g_L = 1, g_Na = 4, g_K = 4 mS/cm2, m_inf V_1/2 = -30, k = 7 mV, n_inf
V_1/2 = -45, k = 5 mV, tau = 1 ms). A: a staircase of current steps (40, 45, 52, 45,
40 uA/cm2, 150 ms each; grey, labels in uA/cm2): at 45 the neuron stays at rest on the way up but keeps
spiking on the way down; spiking starts above the Hopf point (48.8) and stops below the fold of limit
cycles (42.5). B: at a constant I = 45 (bistable) a brief depolarizing pulse (20 uA/cm2, 1 ms)
switches the neuron from rest to spiking, and an identical pulse at the right phase switches it back.
C: phase plane at I = 45: the stable focus (rest), the unstable limit cycle around it (dashed, found by
integrating backward in time) that separates the two basins, and the stable spiking limit cycle."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
EL, gL, gNa, gK = -78.0, 1.0, 4.0, 4.0
minf = lambda V: 1 / (1 + np.exp((-30 - V) / 7))
ninf = lambda V: 1 / (1 + np.exp((-45 - V) / 5))


def f(y, I):
    V, n = y
    return np.array([I - gL * (V - EL) - gNa * minf(V) * (V - 60) - gK * n * (V + 90), ninf(V) - n])


def run(y, Ifun, T, dt=0.02, sign=1.0):
    t = np.arange(0, T, dt)
    y = np.array(y, float)
    out = np.empty((len(t),) + y.shape)
    for i, tt in enumerate(t):
        out[i] = y
        I = Ifun(tt)
        k1 = sign * f(y, I); k2 = sign * f(y + dt / 2 * k1, I); k3 = sign * f(y + dt / 2 * k2, I); k4 = sign * f(y + dt * k3, I)
        y = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return t, out


def rest(I):
    V = brentq(lambda V: I - gL * (V - EL) - gNa * minf(V) * (V - 60) - gK * ninf(V) * (V + 90), -70, -40)
    return np.array([V, ninf(V)])


fig, axs = plt.subplots(1, 3, figsize=(10.6, 3.3), gridspec_kw=dict(width_ratios=[1.0, 1.25, 1.0]))
fig.subplots_adjust(wspace=0.32, left=0.06, right=0.99, bottom=0.17, top=0.88)

# A: staircase of current up and down
ax = axs[0]
levels = [40.0, 45.0, 52.0, 45.0, 40.0]
stair = lambda t: levels[min(int(t // 150), len(levels) - 1)]
t, o = run(rest(40.0), stair, 750, dt=0.02)
ax.plot(t, o[:, 0], color=charts.line("blood"), lw=0.6)
Ist = np.array([stair(tt) for tt in t])
ax.plot(t, 25 + (Ist - 40) * 1.5, color=P.muted(), lw=1.0)
for k, L in enumerate(levels):
    ax.text(75 + 150 * k, 26 + (L - 40) * 1.5, f"{L:g}", fontsize=FT["tiny"], color=P.muted(), ha="center", va="bottom")
ax.set_ylim(-80, 60); ax.set_yticks([-80, -60, -40, -20, 0])
charts.style_axes(ax, "t / ms", "$V$ / mV")
charts.title(ax, "A  Hysteresis (current steps)")

# B: switching on and off with identical pulses at I = 45
ax = axs[1]
I0 = 45.0
y_r = rest(I0)
t1, o1 = run(y_r, lambda t: I0 + (20 if 10 <= t < 11 else 0), 70)
y_s = o1[-1]
# find a pulse onset (after 70 ms) that returns the state to rest: test candidates in parallel
dt = 0.02
cand = np.arange(0, 6.0, 0.1)
y = np.repeat(y_s[:, None], len(cand), 1)
tt = np.arange(0, 50, dt)
for k, s in enumerate(tt):
    Ivec = I0 + np.where((cand <= s) & (s < cand + 1), 20.0, 0.0)
    k1 = f(y, Ivec); k2 = f(y + dt / 2 * k1, Ivec); k3 = f(y + dt / 2 * k2, Ivec); k4 = f(y + dt * k3, Ivec)
    y = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
ok = np.abs(y[0] - y_r[0]) < 1.0
t_stop = 70 + cand[np.argmax(ok)] if ok.any() else 75.0
pulse = lambda t: I0 + (20 if (10 <= t < 11) or (t_stop <= t < t_stop + 1) else 0)
t, o = run(y_r, pulse, 130)
ax.plot(t, o[:, 0], color=charts.line("blood"), lw=1.1)
for t0 in (10, t_stop):
    ax.annotate("", xy=(t0 + 0.5, -66), xytext=(t0 + 0.5, -78),
                arrowprops=dict(arrowstyle="-|>", color=P.ink(), lw=0.9))
ax.text(10.5, -80, "pulse", fontsize=FT["tiny"], color=P.ink(), ha="center", va="top")
ax.text(t_stop + 0.5, -80, "same pulse", fontsize=FT["tiny"], color=P.ink(), ha="center", va="top")
ax.set_ylim(-88, 8)
charts.style_axes(ax, "t / ms", "$V$ / mV")
charts.title(ax, "B  Switching at $I = 45$")

# C: phase plane with the unstable cycle
ax = axs[2]
_, ob = run(y_r + np.array([0.05, 0.0]), lambda t: I0, 60, dt=0.01, sign=-1.0)
uc = ob[int(0.6 * len(ob)):]
ax.plot(uc[:, 0], uc[:, 1], "--", color=charts.line("negative"), lw=1.3, label="unstable cycle")
sc = o1[int(40 / 0.02):]
ax.plot(sc[:, 0], sc[:, 1], color=charts.line("highlight"), lw=1.5, label="spiking cycle")
Vg = np.linspace(-75, 10, 300)
nV = (I0 - gL * (Vg - EL) - gNa * minf(Vg) * (Vg - 60)) / (gK * (Vg + 90))
ax.plot(Vg, nV, color=charts.line("neuron"), lw=0.9, label="$V$-nullcline")
ax.plot(Vg, ninf(Vg), color=charts.line("dna"), lw=0.9, label="$n$-nullcline")
ax.plot(*y_r, "o", ms=5, color=charts.line("neuron"), mec=P.ink(), mew=0.6)
ax.set_xlim(-75, 10); ax.set_ylim(-0.02, 1.0)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "$V$ / mV", "$n$")
charts.title(ax, "C  Two attractors at $I = 45$")
