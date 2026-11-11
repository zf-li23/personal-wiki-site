"""Phenomena of the Hodgkin-Huxley model (squid axon, 6.3 C, rest -65 mV). A: threshold and all-or-none
response to 0.5 ms current pulses of 6, 12, 13.2, 13.6 and 20 uA/cm2 (threshold between 13.2 and
13.6: near threshold the spike is delayed). B: refractoriness: a first suprathreshold
pulse (40 uA/cm2, 0.5 ms) followed by a second pulse of the same size after intervals of 20, 12, 8 and
5 ms. C: anode-break excitation: a 20 ms hyperpolarizing current of -3 uA/cm2 ends and the membrane
fires a spike without any depolarizing input. D: repetitive firing for steady current, frequency
(from spike times of a 400 ms simulation) against current: firing starts above 6 uA/cm2 at a
frequency of about 58 Hz (class 2)."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts, neuro

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(2, 2, figsize=(10.0, 5.8))
fig.subplots_adjust(wspace=0.28, hspace=0.5, left=0.07, right=0.99, bottom=0.1, top=0.93)
dt = 0.01


def pulse(t, t0, w, amp):
    return np.where((t >= t0) & (t < t0 + w), amp, 0.0)


ax = axs[0, 0]
t = np.arange(0, 15, dt)
amps = [6, 12, 13.2, 13.6, 20]
I = np.stack([pulse(t, 1, 0.5, a) for a in amps], 1)
V = neuro.hh_simulate(I, t)[0]
for j, a in enumerate(amps):
    ax.plot(t, V[:, j], color=charts.line(["neutral", "dna", "highlight", "blood", "negative"][j]), lw=1.4,
            label=f"{a:g} $\\mu$A cm$^{{-2}}$")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right", ncol=2)
charts.style_axes(ax, "t / ms", "$V$ / mV")
charts.title(ax, "A  Threshold and all-or-none")

ax = axs[0, 1]
t = np.arange(0, 40, dt)
gaps = [20, 12, 8, 5]
I = np.stack([pulse(t, 2, 0.5, 40) + pulse(t, 2 + g, 0.5, 40) for g in gaps], 1)
V = neuro.hh_simulate(I, t)[0]
for j, g in enumerate(gaps):
    ax.plot(t, V[:, j] - 0 * j, color=charts.line(["neuron", "dna", "highlight", "blood"][j]), lw=1.2, label=f"interval {g} ms")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "t / ms", "$V$ / mV")
charts.title(ax, "B  Refractory period")

ax = axs[1, 0]
t = np.arange(0, 60, dt)
Ib = np.where((t >= 5) & (t < 25), -3.0, 0.0)
Vb = neuro.hh_simulate(Ib[:, None], t)[0][:, 0]
ax.plot(t, Vb, color=charts.line("blood"), lw=1.5)
ax2 = ax.twinx()
ax2.plot(t, Ib, color=P.muted(), lw=1.0)
ax2.set_ylim(-12, 6)
ax2.set_ylabel("$I$ / $\\mu$A cm$^{-2}$", fontsize=FT["small"], color=P.muted())
charts.style_axes(ax2, None, None, box=True)
charts.style_axes(ax, "t / ms", "$V$ / mV")
charts.title(ax, "C  Anode-break excitation")

ax = axs[1, 1]
Is = np.arange(0, 21, 1.0)
t = np.arange(0, 400, 0.02)
Ia = np.tile(Is, (len(t), 1))
V = neuro.hh_simulate(Ia, t)[0]
f = []
for j in range(len(Is)):
    v = V[:, j]
    up = np.where((v[:-1] < 0) & (v[1:] >= 0))[0]
    tu = t[up]
    tu = tu[tu > 50]
    f.append(1000 / np.mean(np.diff(tu)) if len(tu) > 2 else 0.0)
ax.plot(Is, f, "o-", ms=3.5, color=charts.line("neuron"), lw=1.4)
ax.set_xlabel("")
charts.style_axes(ax, "$I_\\mathrm{ext}$ / $\\mu$A cm$^{-2}$", "firing rate / Hz")
charts.title(ax, "D  Repetitive firing: onset at nonzero rate")
