"""Firing patterns of the Izhikevich simple model (Izhikevich 2003): dv/dt = 0.04 v^2 + 5 v + 140 - u + I,
du/dt = a (b v - u), and when v reaches +30 mV: v <- c, u <- u + d (v in mV, t in ms). Parameters (a, b, c, d)
from Izhikevich (2003, 2007): regular spiking RS (0.02, 0.2, -65, 8), intrinsically bursting IB (0.02,
0.2, -55, 4), chattering CH (0.02, 0.2, -50, 2), fast spiking FS (0.1, 0.2, -65, 2), low-threshold spiking
LTS (0.02, 0.25, -65, 2), thalamocortical TC (0.02, 0.25, -65, 0.05). Each panel: a step of current I = 10
from t = 20 ms (TC: the cell is held at I = -10 and released to I = 0 at t = 120 ms, which evokes a rebound
burst). Integration: Euler with dt = 0.1 ms from the resting state. Bottom row: the (v, u) plane for RS and IB, with the
v-nullcline (parabola) at I = 10, the u-nullcline (line u = b v) and the trajectory (resets not drawn):
a high reset c (IB) lands above the parabola's minimum and fires again at once, producing the initial burst;
and the instantaneous firing rate (1/ISI) against interval number for RS, FS and LTS over 600 ms."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
TYPES = [("RS  regular spiking", (0.02, 0.2, -65, 8)), ("IB  intrinsically bursting", (0.02, 0.2, -55, 4)),
         ("CH  chattering", (0.02, 0.2, -50, 2)), ("FS  fast spiking", (0.1, 0.2, -65, 2)),
         ("LTS  low-threshold spiking", (0.02, 0.25, -65, 2)), ("TC  rebound burst", (0.02, 0.25, -65, 0.05))]


def rest(b, I=0.0):
    """Lower root of 0.04 v^2 + (5 - b) v + 140 + I = 0: the resting potential."""
    A, B, C = 0.04, 5 - b, 140 + I
    return (-B - np.sqrt(B * B - 4 * A * C)) / (2 * A)


def simulate(a, b, c, d, Ifun, T=220.0, dt=0.1, v0=None):
    t = np.arange(0, T, dt)
    v = rest(b, Ifun(0.0)) if v0 is None else v0
    u = b * v
    vs = np.empty(len(t)); us = np.empty(len(t))
    for k, tt in enumerate(t):
        I = Ifun(tt)
        v = v + dt * (0.04 * v * v + 5 * v + 140 - u + I)
        u = u + dt * a * (b * v - u)
        if v >= 30:
            vs[k] = 30.0; v = c; u = u + d; us[k] = np.nan
            continue
        else:
            vs[k] = v
        us[k] = u
    return t, vs, us


fig, axs = plt.subplots(3, 3, figsize=(10.4, 6.4))
fig.subplots_adjust(wspace=0.25, hspace=0.62, left=0.06, right=0.99, bottom=0.08, top=0.94)
flat = [axs[0, 0], axs[0, 1], axs[0, 2], axs[1, 0], axs[1, 1], axs[1, 2]]
for ax, (name, (a, b, c, d)) in zip(flat, TYPES):
    if name.startswith("TC"):
        # settle at I = -10 first, then release
        Ifun = lambda t: -10.0 if t < 120 else 0.0
        t, v, u = simulate(a, b, c, d, Ifun, T=300.0)
        sel = t >= 80
        t, v = t[sel] - 80, v[sel]
        Ishow = np.where(t + 80 < 120, -10.0, 0.0)
    else:
        Ifun = lambda t: 10.0 if t >= 20 else 0.0
        t, v, u = simulate(a, b, c, d, Ifun)
        Ishow = np.where(t >= 20, 10.0, 0.0)
    ax.plot(t, v, color=charts.line("blood"), lw=0.9)
    ax.plot(t, -95 + Ishow * 0.8, color=P.muted(), lw=0.9)
    ax.set_ylim(-110, 40); ax.set_yticks([-80, -40, 0])
    charts.style_axes(ax, "t / ms", "$v$ / mV")
    charts.title(ax, name)

# bottom row: two (v, u) planes and the adaptation of the instantaneous rate
for ax, k in [(axs[2, 0], 0), (axs[2, 1], 1)]:
    name, (a, b, c, d) = TYPES[k]
    t, v, u = simulate(a, b, c, d, lambda t: 10.0 if t >= 20 else 0.0, T=300.0)
    vv = np.linspace(-80, 30, 300)
    ax.plot(vv, 0.04 * vv**2 + 5 * vv + 140 + 10, color=charts.line("neuron"), lw=1.1, label="$v$-nullcline ($I = 10$)")
    ax.plot(vv, b * vv, color=charts.line("dna"), lw=1.1, label="$u$-nullcline")
    vplot = np.where(np.isnan(u), np.nan, v)
    ax.plot(vplot, u, color=charts.line("blood"), lw=0.8, label="trajectory")
    ax.axvline(c, color=P.muted(), lw=0.7, ls=":")
    ax.set_xlim(-80, 32); ax.set_ylim(-16, 12)
    if k == 0:
        ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
    charts.style_axes(ax, "$v$ / mV", "$u$")
    charts.title(ax, name.split()[0] + " in the $(v, u)$ plane (reset $c$ dotted)")

ax = axs[2, 2]
for k, tok in [(0, "blood"), (3, "dna"), (4, "neuron")]:
    name, (a, b, c, d) = TYPES[k]
    t, v, u = simulate(a, b, c, d, lambda t: 10.0 if t >= 20 else 0.0, T=600.0)
    ts = t[v >= 30]
    ax.plot(np.arange(1, len(ts)), 1000 / np.diff(ts), "o-", ms=2.5, lw=1.0, color=charts.line(tok), label=name.split()[0])
ax.set_xlim(0, 25)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right", ncol=3)
charts.style_axes(ax, "interspike interval number", "rate / Hz")
charts.title(ax, "Adaptation of the rate (I = 10)")
