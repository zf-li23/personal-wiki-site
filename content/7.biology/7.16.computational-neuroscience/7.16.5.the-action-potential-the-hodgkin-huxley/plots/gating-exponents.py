"""Why m^3 h and n^4: the exponent of a gating variable shapes the delay of a conductance. Voltage steps
from -65 mV in the Hodgkin-Huxley model (6.3 C). A: potassium conductance g_K(t) proportional to n^p
for a step to 0 mV (n relaxes with tau_n(0 mV), the conductance is normalized to its final value):
p = 1 starts at full speed, p = 4 has the sigmoidal delay seen in the voltage clamp. B: sodium
conductance proportional to m^p h for a step to -20 mV, normalized to the peak of the p = 3 curve:
the exponent controls the onset and the amplitude, h the decay. C: a stochastic channel made of four
independent two-state gates (rates alpha_n(0 mV), beta_n(0 mV), Markov chain, time step 0.02 ms): single
channels open after a random latency (grey), the average of 400 channels (colour) is n^4 (black)."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts, neuro

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 3, figsize=(10.4, 3.2))
fig.subplots_adjust(wspace=0.32, left=0.06, right=0.99, bottom=0.17, top=0.88)

am0, bm0, ah0, bh0, an0, bn0 = [float(x) for x in neuro.hh_rates(-65.0)]
m0, h0, n0 = neuro.hh_steady(-65.0)
t = np.linspace(0, 12, 600)

ax = axs[0]
an, bn = [float(x) for x in neuro.hh_rates(0.0)[4:6]]
ninf, taun = an / (an + bn), 1 / (an + bn)
n = ninf + (float(n0) - ninf) * np.exp(-t / taun)
cols = {1: "neutral", 2: "dna", 4: "blood", 6: "highlight"}
for p, tok in cols.items():
    g = n ** p
    g = (g - float(n0) ** p) / (ninf ** p - float(n0) ** p)
    ax.plot(t, g, color=charts.line(tok), lw=1.8 if p == 4 else 1.2, label=f"$p = {p}$")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "time after step / ms", "$g_\\mathrm{K}$ (normalized)")
charts.title(ax, "A  $g_\\mathrm{K} \\propto n^p$, step to 0 mV")

ax = axs[1]
V = -20.0
am, bm, ah, bh = [float(x) for x in neuro.hh_rates(V)[:4]]
minf, taum = am / (am + bm), 1 / (am + bm)
hinf, tauh = ah / (ah + bh), 1 / (ah + bh)
tt = np.linspace(0, 8, 600)
m = minf + (float(m0) - minf) * np.exp(-tt / taum)
h = hinf + (float(h0) - hinf) * np.exp(-tt / tauh)
ref = (m ** 3 * h).max()
for p, tok in [(1, "neutral"), (2, "dna"), (3, "blood"), (4, "highlight")]:
    ax.plot(tt, m ** p * h / ref, color=charts.line(tok), lw=1.8 if p == 3 else 1.2, label=f"$p = {p}$")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "time after step / ms", "$g_\\mathrm{Na}$ (rel. to $p=3$ peak)")
charts.title(ax, "B  $g_\\mathrm{Na} \\propto m^p h$, step to $-20$ mV")

ax = axs[2]
rng = np.random.default_rng(0)
dt, Nch = 0.02, 400
ts = np.arange(0, 12, dt)
state = np.zeros((Nch, 4), bool)
# start in the stationary distribution at -65 mV
state[:] = rng.random((Nch, 4)) < float(n0)
open_frac = np.empty(len(ts))
single = np.empty((len(ts), 3))
pa, pb = 1 - np.exp(-an * dt), 1 - np.exp(-bn * dt)
for k in range(len(ts)):
    op = state.all(1)
    open_frac[k] = op.mean()
    single[k] = op[:3]
    u = rng.random(state.shape)
    state = np.where(state, u > pb, u < pa)
for j in range(3):
    ax.step(ts, single[:, j] * 0.1 - 0.17 * (j + 1), where="post", color=P.muted(), lw=0.9)
ax.plot(ts, open_frac, color=charts.line("k"), lw=1.4, label="mean of 400")
ax.plot(t, ((ninf + (float(n0) - ninf) * np.exp(-t / taun)) ** 4), color=P.ink(), lw=1.2, label="$n^4$")
ax.set_ylim(-0.6, 1.05); ax.set_yticks([0, 0.5, 1])
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(ax, "time after step / ms", "open fraction")
charts.title(ax, "C  Four independent gates")
