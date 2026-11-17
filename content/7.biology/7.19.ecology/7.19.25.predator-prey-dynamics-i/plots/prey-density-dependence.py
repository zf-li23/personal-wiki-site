"""Lotka-Volterra predation with logistic prey (Section 25.3).

Dimensionless form x' = x(1 - x - y), y' = alpha y (x - beta), with x = N/K, y = aP/r,
alpha = caK/r and beta = m/(caK) = N*/K.
A: phase plane for alpha = 2, beta = 0.25: the prey isocline is the line y = 1 - x, the predator
isocline the line x = beta; the trajectory spirals into the stable focus (beta, 1 - beta).
B: the same trajectory as time series (damped oscillations), compared with beta = 0.6 (fast damping).
C: classification of the coexistence equilibrium in the (beta, alpha) plane: predator extinct
for beta >= 1, stable focus above the curve alpha = beta / [4 (1 - beta)], stable node below it.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
prey, pred = C.line("dna"), C.line("negative")


def run(alpha, beta, z0, T):
    f = lambda t, z: [z[0] * (1 - z[0] - z[1]), alpha * z[1] * (z[0] - beta)]
    return solve_ivp(f, [0, T], z0, max_step=0.02, rtol=1e-9, atol=1e-10)


fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.3))
ax = axes[0]
s = run(2.0, 0.25, [0.9, 0.05], 60)
ax.plot(s.y[0], s.y[1], color=P.ink(), lw=1.1)
xx = np.linspace(0, 1, 50)
ax.plot(xx, 1 - xx, color=prey, ls=(0, (4, 2)), lw=1.1)
ax.axvline(0.25, color=pred, ls=(0, (4, 2)), lw=1.1)
ax.plot(0.25, 0.75, "o", color=P.ink(), ms=5)
ax.text(0.62, 0.42, "prey isocline\ny = 1 - x", color=prey, fontsize=FS["tiny"])
ax.text(0.27, 1.32, "predator isocline x = β", color=pred, fontsize=FS["tiny"])
ax.set_xlim(0, 1.0)
ax.set_ylim(0, 1.4)
C.style_axes(ax, "Prey x = N/K", "Predator y = aP/r")
C.title(ax, "A  Spiral into a stable focus")

ax = axes[1]
ax.plot(s.t, s.y[0], color=prey, lw=1.3, label="prey, β = 0.25")
ax.plot(s.t, s.y[1], color=pred, lw=1.3, label="predator, β = 0.25")
s2 = run(2.0, 0.6, [0.9, 0.05], 60)
ax.plot(s2.t, s2.y[0], color=prey, lw=0.9, ls=(0, (2, 1.5)), label="prey, β = 0.6")
ax.plot(s2.t, s2.y[1], color=pred, lw=0.9, ls=(0, (2, 1.5)), label="predator, β = 0.6")
ax.legend(fontsize=FS["tiny"], frameon=False, ncol=2, loc="upper right")
ax.set_ylim(0, 1.5)
C.style_axes(ax, "Dimensionless time rt", "Density")
C.title(ax, "B  Damped oscillations (α = 2)")

ax = axes[2]
b = np.linspace(0.001, 0.999, 400)
ab = b / (4 * (1 - b))
ax.fill_between(b, 0, np.minimum(ab, 5), color=P.light("dna"), lw=0)
ax.fill_between(b, np.minimum(ab, 5), 5, color=P.light("positive"), lw=0)
ax.axvspan(1, 1.3, color=P.light("negative"), lw=0)
ax.plot(b, ab, color=P.ink(), lw=1.0)
ax.text(0.86, 0.45, "stable\nnode", ha="center", fontsize=FS["tiny"], color=P.on_fill())
ax.text(0.45, 3.6, "stable focus\n(damped oscillations)", ha="center", fontsize=FS["tiny"], color=P.on_fill())
ax.text(1.15, 2.5, "predator\nextinct", ha="center", fontsize=FS["tiny"], color=P.on_fill())
ax.set_xlim(0, 1.3)
ax.set_ylim(0, 5)
C.style_axes(ax, "β = N*/K", "α = caK/r")
C.title(ax, "C  Type of the coexistence equilibrium")
fig.tight_layout()
