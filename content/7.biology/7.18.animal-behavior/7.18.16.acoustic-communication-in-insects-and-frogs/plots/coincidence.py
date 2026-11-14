"""Recognizing the pulse rhythm with a delay line and a coincidence detector
(after Schoeneich, Kostarakos and Hedwig 2015).

Ascending neuron AN1 copies each sound pulse. Branch 1: AN1 excites LN2, which inhibits LN5;
LN5 fires a post-inhibitory rebound burst a fixed delay after the end of each pulse.
Branch 2: AN1 excites the coincidence-detector LN3 directly. LN3 responds strongly only when the
rebound from the previous pulse arrives together with the direct excitation by the next pulse,
i.e. when the pulse period matches pulse duration + rebound delay. A feature-detector neuron (LN4)
integrates LN3 output. Model: pulses of duration D = period / 2, rebound delay 18.5 ms (Gaussian
window, s.d. 3.5 ms); the direct AN1 input to LN3 is phasic (an onset transient decaying with 4 ms);
LN3 output per chirp = summed product of the two inputs, maximal when period = D + delay = 2 x delay.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
dt = 0.1
delay, width = 18.5, 3.5


def responses(period, n=4):
    t = np.arange(0, n * period + 60, dt)
    D = period / 2
    an1 = np.zeros_like(t)
    onset = np.zeros_like(t)
    reb = np.zeros_like(t)
    for k in range(n):
        on = k * period
        an1[(t >= on) & (t < on + D)] = 1
        m = t >= on
        onset[m] += np.exp(-(t[m] - on) / 4.0)
        reb += np.exp(-0.5 * ((t - (on + D + delay)) / width) ** 2)
    ln3 = onset * reb
    return t, an1, reb, ln3


fig, axs = plt.subplots(1, 3, figsize=(11.5, 3.6), gridspec_kw={"width_ratios": [1.2, 1.2, 1]})
for ax, period, title in ((axs[0], 34.0, "A  Pulse period 34 ms (natural)"), (axs[1], 60.0, "B  Pulse period 60 ms")):
    t, an1, reb, ln3 = responses(period)
    ax.fill_between(t, 2.2, 2.2 + 0.8 * an1, color=P.fill("dna"), lw=0)
    ax.plot(t, 1.1 + 0.8 * reb, color=P.edge("rna"), lw=1.5)
    ax.fill_between(t, 0, 0.9 * ln3 / 1.0, color=P.fill("negative"), lw=0)
    ax.set_yticks([0.4, 1.5, 2.6]); ax.set_yticklabels(["LN3\n(coincidence)", "LN5\n(rebound)", "AN1\n(pulses)"], fontsize=8)
    ax.set_xlabel("Time / ms")
    ax.set_title(title, loc="left", fontweight="bold", fontsize=9.5)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
periods = np.linspace(16, 100, 169)
out = [responses(p)[3].sum() * dt for p in periods]
out = np.array(out) / max(out)
axs[2].plot(periods, out, color=P.edge("negative"), lw=2, label="LN3/LN4 output")
best = periods[np.argmax(out)]
axs[2].axvline(best, color=P.muted(), ls=":", lw=0.8)
axs[2].text(best + 2, 0.95, f"best period ≈ {best:.0f} ms", fontsize=7.5, color=P.muted())
axs[2].set_xlabel("Pulse period / ms (duty cycle 50 %)")
axs[2].set_ylabel("Response per chirp (norm.)")
axs[2].set_title("C  Band-pass tuning", loc="left", fontweight="bold", fontsize=9.5)
for s in ("top", "right"):
    axs[2].spines[s].set_visible(False)
fig.tight_layout()
