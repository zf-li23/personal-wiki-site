"""A minimal model of AgRP neuron activity: need minus predicted nutrient (Formula 34.3.1).

a(t) = max(D(t) - s(t), 0), with D the energy deficit and s a sensory prediction of the coming nutrient.
Cue (food presented) at t = 0: s rises with tau_on = 0.1 min toward v * D.
If food is eaten and is nutritive, gut signals lower D (tau_D = 8 min) and s is "confirmed";
if food is inaccessible, the unconfirmed prediction decays with tau_off = 3 min.
Fed state: D = 0.2. Units are arbitrary (normalized activity), schematic of Chen et al. 2015 / Betley et al. 2015.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
dt = 0.01
t = np.arange(-3, 20, dt)


def run(D0, eat, v=0.8, tau_on=0.1, tau_off=3.0, tau_D=8.0):
    """Deficit D falls only if nutritive food is eaten; the prediction s tracks v*D while confirmed."""
    D = np.where(t < 0, D0, D0 * (0.3 + 0.7 * np.exp(-np.clip(t, 0, None) / tau_D))) if eat else np.full_like(t, D0)
    s = np.zeros_like(t)
    for i in range(1, len(t)):
        if t[i] < 0:
            continue
        if eat or t[i] < 0.3:
            target, tau = v * D[i], tau_on
        else:
            target, tau = 0.0, tau_off
        s[i] = s[i - 1] + dt * (target - s[i - 1]) / tau
    return np.maximum(D - s, 0.0)


fig, ax = plt.subplots(figsize=(7.5, 3.6))
ax.plot(t, run(1.0, True), color=P.edge("dna"), lw=2.2, label="Fasted, food presented and eaten")
ax.plot(t, run(1.0, False), color=P.edge("negative"), lw=2.2, ls="--", label="Fasted, food seen but inaccessible")
ax.plot(t, run(0.2, True), color=P.edge("neutral"), lw=2.2, label="Fed, food presented and eaten")
ax.axvline(0, color=P.muted(), lw=0.8)
ax.text(0.2, 1.05, "food presented", fontsize=8.5, color=P.muted())
ax.set_xlabel("Time from food presentation / min")
ax.set_ylabel("AgRP population activity (norm.)")
ax.set_ylim(-0.03, 1.15)
ax.set_xlim(-3, 20)
ax.grid(True, alpha=0.3)
ax.legend(frameon=False, fontsize=8, loc="center right")
fig.tight_layout()
