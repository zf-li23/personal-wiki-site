"""The Hodgkin-Huxley model of the squid giant axon (6.3 C, rest -65 mV; gNa 120, gK 36, gL 0.3 mS/cm2,
ENa 50, EK -77 mV, Cm 1 uF/cm2). A: steady states m_inf, h_inf, n_inf and time constants of the gates
against membrane potential. B: simulated voltage clamp: steps from -65 mV to -40, -10 and +20 mV;
the Na+ conductance rises within a millisecond and inactivates, the K+ conductance rises with a delay
(sigmoidal, n^4) and stays. C: space-clamped action potentials after brief current pulses (0.5 ms):
two subthreshold pulses decay, a suprathreshold pulse gives the all-or-none spike. D: the gating variables
and the ionic currents during the spike. E: firing frequency for steady current injection: the HH axon
starts firing at a nonzero frequency (about 60 Hz) above a threshold current, a type II neuron."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts
from wikibio import neuro

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 5, figsize=(13.6, 3.1))
fig.subplots_adjust(wspace=0.6, left=0.045, right=0.99, bottom=0.17, top=0.87)
p = neuro.HH

ax = axs[0]
V = np.linspace(-100, 40, 300)
m, h, n = neuro.hh_steady(V)
am, bm, ah, bh, an, bn = neuro.hh_rates(V)
for y, tok, lab in [(m, "na", r"$m_\infty$"), (h, "blood", r"$h_\infty$"), (n, "k", r"$n_\infty$")]:
    ax.plot(V, y, color=charts.line(tok), lw=1.6, label=lab)
ax2 = ax.twinx()
for r, tok in [(1 / (am + bm), "na"), (1 / (ah + bh), "blood"), (1 / (an + bn), "k")]:
    ax2.plot(V, r, "--", color=charts.line(tok), lw=1.0)
charts.style_axes(ax2, None, None, box=True)
ax2.set_ylabel(r"$\tau$ / ms (dashed)", fontsize=FT["small"], color=P.ink())
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center left")
charts.style_axes(ax, "V / mV", "steady state")
charts.title(ax, "A  Gates")

ax = axs[1]
t = np.arange(0, 8, 0.01)
for Vc, tok in [(-40, "dna"), (-10, "bacterium"), (20, "blood")]:
    m0, h0, n0 = neuro.hh_steady(-65.0)
    am, bm, ah, bh, an, bn = [float(x) for x in neuro.hh_rates(Vc)]
    minf, taum = am / (am + bm), 1 / (am + bm)
    hinf, tauh = ah / (ah + bh), 1 / (ah + bh)
    ninf, taun = an / (an + bn), 1 / (an + bn)
    mm = minf + (m0 - minf) * np.exp(-t / taum)
    hh = hinf + (h0 - hinf) * np.exp(-t / tauh)
    nn = ninf + (n0 - ninf) * np.exp(-t / taun)
    ax.plot(t, p["gNa"] * mm ** 3 * hh, color=charts.line(tok), lw=1.5, label=f"{Vc} mV")
    ax.plot(t, p["gK"] * nn ** 4, "--", color=charts.line(tok), lw=1.2)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right", title="g_Na solid, g_K dashed",
          title_fontsize=FT["tiny"])
charts.style_axes(ax, "time after step / ms", r"conductance / mS cm$^{-2}$")
charts.title(ax, "B  Voltage clamp")

ax = axs[2]
t = np.arange(0, 20, 0.01)
for amp, tok in [(5.0, "neutral"), (10.0, "dna"), (40.0, "blood")]:
    I = np.where((t > 1) & (t < 1.5), amp, 0.0)
    Vt, _, _, _ = neuro.hh_simulate(I[:, None], t)
    ax.plot(t, Vt[:, 0], color=charts.line(tok), lw=1.5, label=rf"{amp:g} $\mu$A cm$^{{-2}}$")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "time / ms", "V / mV")
charts.title(ax, "C  Threshold")

ax = axs[3]
I = np.where((t > 1) & (t < 1.5), 40.0, 0.0)
Vt, mt, ht, nt = [x[:, 0] for x in neuro.hh_simulate(I[:, None], t)]
INa = p["gNa"] * mt ** 3 * ht * (Vt - p["ENa"])
IK = p["gK"] * nt ** 4 * (Vt - p["EK"])
ax.plot(t, mt, color=charts.line("na"), lw=1.4, label="m")
ax.plot(t, ht, color=charts.line("blood"), lw=1.4, label="h")
ax.plot(t, nt, color=charts.line("k"), lw=1.4, label="n")
ax3 = ax.twinx()
ax3.plot(t, INa / 1000, ":", color=charts.line("na"), lw=1.1)
ax3.plot(t, IK / 1000, ":", color=charts.line("k"), lw=1.1)
charts.style_axes(ax3, None, None, box=True)
ax3.set_ylabel(r"$I$ / mA cm$^{-2}$ (dotted)", fontsize=FT["small"], color=P.ink())
ax.set_xlim(0, 10)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "time / ms", "gating variable")
charts.title(ax, "D  Inside the spike")

ax = axs[4]
Is = np.linspace(0, 40, 41)
t = np.arange(0, 300, 0.02)
Vt, _, _, _ = neuro.hh_simulate(np.tile(Is, (len(t), 1)), t)
f = []
for j in range(len(Is)):
    v = Vt[:, j]
    up = np.where((v[1:] > 0) & (v[:-1] <= 0))[0]
    up = up[t[up] > 100]
    f.append(len(up) / 0.2)
ax.plot(Is, f, "o-", ms=3, color=charts.line("neuron"), lw=1.4)
charts.style_axes(ax, r"steady current / $\mu$A cm$^{-2}$", "firing rate / Hz")
charts.title(ax, "E  f-I curve")
