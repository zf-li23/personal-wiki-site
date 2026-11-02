"""Hazard functions and the survival curves they imply (schematic parameter values, time in years).

A: constant hazard (exponential), decreasing and increasing Weibull hazards (shape 0.6 and 2), and a
Gompertz hazard that grows exponentially with time. B: the corresponding survival functions
S(t) = exp(-H(t)); all four have the same median of 5 years. C: log(-log S(t)) against log t: Weibull
models are straight lines with slope equal to the shape parameter, which is the basis of the log-log
check of proportional hazards.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
t = np.linspace(0.01, 15, 600)
med = 5.0
models = []
for k, tok, name in [(1.0, "neutral", "exponential (constant)"), (0.6, "dna", "Weibull, shape 0.6 (decreasing)"),
                     (2.0, "rna", "Weibull, shape 2 (increasing)")]:
    eta = med / np.log(2) ** (1 / k)
    H = (t / eta) ** k
    h = k / eta * (t / eta) ** (k - 1)
    models.append((h, H, tok, name))
g = 0.4  # Gompertz h = b exp(g t), median 5 years
b = g * np.log(2) / (np.exp(g * med) - 1)
models.append((b * np.exp(g * t), b / g * (np.exp(g * t) - 1), "plant", "Gompertz (exponential growth)"))

fig, axs = plt.subplots(1, 3, figsize=(11, 3.4))
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.17, top=0.86, wspace=0.3)
for h, H, tok, name in models:
    axs[0].plot(t, h, color=charts.line(tok), lw=1.6)
    axs[1].plot(t, np.exp(-H), color=charts.line(tok), lw=1.6, label=name)
    axs[2].plot(np.log(t), np.log(H), color=charts.line(tok), lw=1.6)
axs[0].set_ylim(0, 0.6)
axs[1].legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right", bbox_to_anchor=(1.02, 1.0))
axs[1].axhline(0.5, color=P.muted(), lw=0.6, ls=":")
axs[1].axvline(med, color=P.muted(), lw=0.6, ls=":")
axs[1].set_ylim(0, 1.02)
axs[2].set_xlim(np.log(0.2), np.log(15))
axs[2].set_ylim(-5, 3)
charts.style_axes(axs[0], "time t / years", "hazard h(t) / per year")
charts.style_axes(axs[1], "time t / years", "survival S(t)")
charts.style_axes(axs[2], "log t", "log(-log S(t)) = log H(t)")
charts.title(axs[0], "A  Hazard functions")
charts.title(axs[1], "B  Survival functions (same median)")
charts.title(axs[2], "C  Log-log scale")
