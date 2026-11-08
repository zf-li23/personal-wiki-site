"""Allometric scaling of physiological variables in mammals, Y = a M^b (M in kg).

Coefficients from classical compilations (Schmidt-Nielsen 1984; Calder 1984):
basal metabolic rate 3.4 W M^0.75; mass-specific metabolic rate 3.4 W/kg M^-0.25;
heart rate 241 /min M^-0.25; breathing rate 53.5 /min M^-0.26; blood volume 65 mL M^1.02;
heart mass 5.8 g M^0.98; lung volume 53.5 mL M^1.06; brain mass about 10 g M^0.73 (fitted in
7.14.46); maximum life span 11.8 yr M^0.20.
A: each variable divided by its value at 1 kg, so lines cross at (1, 1).
B: heartbeats and breaths per lifetime (rate x life span), almost independent of size.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
M = np.logspace(-2.3, 4, 100)
lines = [
    ("lung volume", 1.06, P.edge("dna"), "-"),
    ("blood volume", 1.02, P.edge("rna"), "-"),
    ("heart mass", 0.98, P.edge("muscle"), "--"),
    ("basal metabolic rate", 0.75, P.edge("enzyme"), "-"),
    ("brain mass", 0.73, P.edge("neuron"), "--"),
    ("life span", 0.20, P.edge("plant"), "-"),
    ("mass-specific metabolic rate", -0.25, P.edge("enzyme"), ":"),
    ("heart rate", -0.25, P.edge("protein"), "-"),
    ("breathing rate", -0.26, P.edge("protein"), "--"),
]
fig, (ax, bx) = plt.subplots(1, 2, figsize=(11.5, 4.6), gridspec_kw=dict(width_ratios=[1.4, 1]))
for lab, b, c, ls in lines:
    ax.loglog(M, M**b, color=c, ls=ls, lw=1.8, label=f"{lab} ($M^{{{b:g}}}$)")
for name, m in (("mouse", 0.025), ("rat", 0.3), ("human", 70), ("elephant", 4000)):
    ax.axvline(m, color=P.muted(), lw=0.6, alpha=0.6)
    ax.text(m * 1.1, 2e-3, name, rotation=90, fontsize=7, color=P.muted(), va="bottom")
ax.set_xlabel("Body mass M / kg")
ax.set_ylabel("Value relative to a 1 kg mammal")
ax.legend(frameon=False, fontsize=7, loc="upper left")
ax.set_ylim(1e-3, 1e5)
ax.set_title("A  Volumes scale with M, rates with M^(-1/4)", loc="left", fontsize=10)
ax.grid(True, which="major", alpha=0.3)

minutes = 11.8 * M**0.20 * 365.25 * 24 * 60
beats = 241 * M**-0.25 * minutes
breaths = 53.5 * M**-0.26 * minutes
bx.loglog(M, beats, color=P.edge("protein"), lw=2, label="heartbeats per life span")
bx.loglog(M, breaths, color=P.edge("protein"), lw=2, ls="--", label="breaths per life span")
bx.set_ylim(1e7, 1e10)
bx.set_xlabel("Body mass M / kg")
bx.set_ylabel("Count per maximum life span")
bx.legend(frameon=False, fontsize=8, loc="lower left")
bx.set_title("B  About 10^9 beats, whatever the size", loc="left", fontsize=10)
bx.grid(True, which="both", alpha=0.3)
fig.tight_layout()
print(beats[[0, -1]], breaths[[0, -1]])
