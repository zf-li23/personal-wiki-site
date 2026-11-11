"""A spiking half-center oscillator: two adapting LIF neurons coupled by reciprocal inhibition.

C dV/dt = -g_L (V - E_L) - g_a a (V - E_K) - g_syn s_other (V - E_inh) + I_ext,
tau_a da/dt = -a (a jumps by 1 at each spike), tau_s ds/dt = -s (s jumps by 1 at each spike).
g_L = 10 nS, C = 200 pF (tau_m = 20 ms), E_L = -65 mV, V_th = -50 mV, V_reset = -60 mV,
E_K = -80 mV, g_a = 0.6 nS per spike, E_inh = -80 mV, g_syn = 10 nS, tau_s = 10 ms, I_ext = 600 pA,
plus small independent noise.
A: membrane potentials of the two neurons (tau_a = 300 ms): bursts alternate; each burst ends when
   adaptation has built up enough for the inhibited partner to escape.
B: burst period against the adaptation increment g_a: faster adaptation ends bursts sooner, so the
   rhythm is set by the slow process.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
dt = 0.2  # ms
C, gL, EL, Vth, Vr, EK, Einh = 200.0, 10.0, -65.0, -50.0, -60.0, -80.0, -80.0
ga, gs, ts, I = 0.6, 10.0, 10.0, 600.0


def run(ta, T=3000.0, record=False, ga=ga):
    n = int(T / dt)
    V = np.array([-60.0, -55.0])
    a = np.zeros(2)
    s = np.zeros(2)
    Vs = np.empty((n, 2)) if record else None
    spikes = [[], []]
    for k in range(n):
        Isyn = gs * s[::-1] * (V - Einh)
        dV = (-gL * (V - EL) - ga * a * (V - EK) - Isyn + I) / C
        V = V + dt * dV + rng.normal(0, 0.1, 2)
        a -= dt * a / ta
        s -= dt * s / ts
        fired = V >= Vth
        if record:
            Vs[k] = np.where(fired, 0.0, V)
        for j in np.where(fired)[0]:
            spikes[j].append(k * dt)
        V[fired] = Vr
        a[fired] += 1
        s[fired] += 1
    return Vs, spikes


def period(spikes):
    sp = np.array(spikes[0])
    if len(sp) < 4:
        return np.nan
    gaps = np.diff(sp)
    onsets = sp[1:][gaps > 60.0]
    onsets = onsets[onsets > 1000]
    return np.mean(np.diff(onsets)) if len(onsets) > 2 else np.nan


fig, axs = plt.subplots(1, 2, figsize=(12, 3.9), gridspec_kw={"width_ratios": [2.2, 1]})
Vs, sp = run(300.0, T=3000.0, record=True)
t = np.arange(len(Vs)) * dt
ax = axs[0]
ax.plot(t, Vs[:, 0] + 75, color=P.edge("dna"), lw=0.7, label="neuron 1 (flexor half-center)")
ax.plot(t, Vs[:, 1], color=P.edge("negative"), lw=0.7, label="neuron 2 (extensor half-center)")
ax.set_xlim(500, 3000)
ax.set_ylim(-75, 92)
ax.set_yticks([])
ax.set_xlabel("Time / ms")
ax.set_ylabel("Membrane potential (offset)")
ax.set_title("A  Alternating bursts", loc="left", fontsize=10)
ax.text(505, 80, "neuron 1 (flexor half-center)", fontsize=8, color=P.edge("dna"), va="bottom")
ax.text(505, 3, "neuron 2 (extensor half-center)", fontsize=8, color=P.edge("negative"), va="bottom")
ax = axs[1]
gas = np.array([0.3, 0.45, 0.6, 0.9, 1.2, 1.8])
per = [period(run(300.0, ga=g)[1]) for g in gas]
ax.plot(gas, per, "o-", color=P.edge("dna"), lw=1.8)
ax.set_xlabel("Adaptation per spike $g_a$ / nS")
ax.set_ylabel("Burst period / ms")
ax.set_title("B  The slow process sets the rhythm", loc="left", fontsize=10)
for a_ in axs:
    a_.grid(True, alpha=0.3)
fig.tight_layout()
