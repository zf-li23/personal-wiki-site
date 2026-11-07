"""Feedforward inhibition narrows the integration window of a pyramidal cell.

Passive point neuron: C dV/dt = -g_L (V - E_L) - g_e(t)(V - E_e) - g_i(t)(V - E_i), with tau_m = C/g_L =
15 ms, E_L = -65 mV, E_e = 0 mV, E_i = -70 mV; synaptic conductances are alpha functions (tau_e = 1 ms,
tau_i = 4 ms; peaks in units of g_L). Each afferent volley excites the cell directly and, after a disynaptic delay
delta = 1.5 ms, through an inhibitory interneuron (g_i peak = 6 x g_e peak, g_e peak = 0.3 g_L), as in hippocampal CA1
(Pouille and Scanziani 2001). Values are illustrative.
A: response to one volley without and with feedforward inhibition.
B: peak depolarisation produced by two volleys as a function of their separation. Without
inhibition the two EPSPs sum over ~tau_m; with feedforward inhibition only volleys within a few ms sum.
C: shunting shortens the effective time constant, tau_eff = tau_m / (1 + g_shunt R_in) (R_in = 100 MOhm).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
dt = 0.02
t = np.arange(0, 60, dt)
EL, Ee, Ei, tau_m = -65.0, 0.0, -70.0, 15.0


def alpha(t0, tau):
    s = np.clip(t - t0, 0, None)
    return (s / tau) * np.exp(1 - s / tau)


def run(onsets, ffi, ge=0.3, delay=1.5, ratio=6.0):
    g_e = sum(ge * alpha(o, 1.0) for o in onsets)
    g_i = sum(ratio * ge * alpha(o + delay, 4.0) for o in onsets) if ffi else 0 * t
    V = np.empty_like(t)
    v = EL
    for k in range(len(t)):
        v += dt * (-(v - EL) - g_e[k] * (v - Ee) - g_i[k] * (v - Ei)) / tau_m
        V[k] = v
    return V


fig, axs = plt.subplots(1, 3, figsize=(12.5, 3.9))
ax = axs[0]
ax.plot(t, run([5], False), color=P.edge("positive"), lw=2, label="excitation only")
ax.plot(t, run([5], True), color=P.ink(), lw=2, label="with feedforward inhibition")
ax.set_xlim(0, 40)
ax.set_xlabel("Time / ms")
ax.set_ylabel("Membrane potential / mV")
ax.legend(frameon=False, fontsize=8)
ax.set_title("A  One volley", loc="left", fontsize=10)

ax = axs[1]
dts = np.linspace(0, 25, 51)
for ffi, c, name in ((False, P.edge("positive"), "excitation only"), (True, P.ink(), "with feedforward inhibition")):
    single = run([5], ffi).max() - EL
    pk = np.array([run([5, 5 + d], ffi).max() - EL for d in dts])
    ax.plot(dts, pk / single, color=c, lw=2, label=name)
ax.axhline(1, color=P.muted(), lw=0.8, ls=":")
ax.set_xlabel("Interval between two volleys / ms")
ax.set_ylabel("Peak depolarisation / single volley")
ax.legend(frameon=False, fontsize=8)
ax.set_title("B  Integration window", loc="left", fontsize=10)

ax = axs[2]
g = np.linspace(0, 40, 200)
ax.plot(g, tau_m / (1 + g * 1e-9 * 100e6) * 10 / tau_m, color=P.edge("negative"), lw=2)
ax.set_xlabel("Shunting conductance $g_{\\mathrm{shunt}}$ / nS")
ax.set_ylabel("$\\tau_{\\mathrm{eff}}$ / ms ($\\tau_m$ = 10 ms)")
ax.plot([10], [5], "o", color=P.ink(), ms=5)
ax.text(11.5, 5.2, "10 nS halves $\\tau$", fontsize=8.5, color=P.ink())
ax.set_title("C  $\\tau_{\\mathrm{eff}} = \\tau_m/(1 + g R_{\\mathrm{in}})$", loc="left", fontsize=10)
for x in axs:
    x.grid(True, alpha=0.3)
fig.tight_layout()
