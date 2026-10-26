# Binding of a transcription factor A to a single DNA site B by mass action, A + B <-> AB, with the factor in
# excess (pseudo-first order): d theta / dt = k_on [A] (1 - theta) - k_off theta.
# Illustrative constants: k_on = 1e8 M^-1 s^-1 (near the diffusion limit), K_D = 1 nM, so k_off = 0.1 s^-1
# (mean residence time 1/k_off = 10 s).
# A: occupancy theta(t) after mixing at t = 0 for [A] = 0.3, 1, 3 and 10 nM (solid), approaching
#    theta_eq = [A] / ([A] + K_D) with rate k_obs = k_on [A] + k_off; dashed: dissociation after the free
#    factor is removed (chase) at t = 30 s, which proceeds at k_off whatever [A] was.
# B: the observed rate is linear in the concentration: slope k_on, intercept k_off (points: the four
#    concentrations of A).
# C: why specificity lies in k_off: for a fixed, diffusion-limited k_on = 1e8 M^-1 s^-1, the residence time
#    1/k_off = 1/(k_on K_D) spans from milliseconds on nonspecific DNA (K_D ~ 10 uM) through seconds for a
#    typical specific site (1 nM) to hours for a very tight site (1 pM).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
KON, KD = 1e8, 1e-9
KOFF = KON * KD

fig, axs = plt.subplots(1, 3, figsize=(13.0, 3.9), gridspec_kw={"width_ratios": [1.2, 0.9, 1.0]})

ax = axs[0]
t1 = np.linspace(0, 30, 300)
t2 = np.linspace(30, 60, 300)
concs = (0.3e-9, 1e-9, 3e-9, 10e-9)
toks = ("neutral", "dna", "protein", "negative")
for a, tok in zip(concs, toks):
    kobs = KON * a + KOFF
    th_eq = a / (a + KD)
    th = th_eq * (1 - np.exp(-kobs * t1))
    ax.plot(t1, th, color=charts.line(tok), lw=1.8, label=f"[A] = {a * 1e9:g} nM")
    ax.plot(t2, th[-1] * np.exp(-KOFF * (t2 - 30)), color=charts.line(tok), lw=1.3, ls=(0, (4, 2.4)))
ax.axvline(30, color=P.muted(), lw=0.7, ls=":")
ax.text(30.6, 0.97, "chase", fontsize=7, color=P.muted(), va="top")
ax.set_xlim(0, 60)
ax.set_ylim(0, 1)
ax.legend(fontsize=7, frameon=False, loc="upper right", bbox_to_anchor=(0.98, 0.86))
charts.style_axes(ax, "t / s", "site occupancy θ")
ax.set_title("A   Association and dissociation", loc="left", fontsize=9, color=P.ink())

ax = axs[1]
a = np.linspace(0, 11e-9, 50)
ax.plot(a * 1e9, KON * a + KOFF, color=charts.line("dna"), lw=1.8)
for c, tok in zip(concs, toks):
    ax.plot([c * 1e9], [KON * c + KOFF], "o", color=charts.line(tok), ms=5)
ax.text(1.4, 0.06, "intercept k_off", fontsize=7, color=P.muted())
ax.text(5.6, 0.45, "slope k_on", fontsize=7, color=P.muted())
ax.set_xlim(0, 11)
ax.set_ylim(0, 1.25)
charts.style_axes(ax, "[A] / nM", "k_obs / s⁻¹")
ax.set_title("B   k_obs = k_on[A] + k_off", loc="left", fontsize=9, color=P.ink())

ax = axs[2]
kd = np.logspace(-13, -5, 100)
tau = 1 / (KON * kd)
ax.loglog(kd, tau, color=charts.line("protein"), lw=1.8)
for y, txt in ((1e-3, "1 ms"), (1, "1 s"), (60, "1 min"), (3600, "1 h")):
    ax.axhline(y, color=P.muted(), lw=0.5, ls=":")
    ax.text(2e-13, y * 1.3, txt, fontsize=7, color=P.muted())
for x, txt in ((1e-5, "nonspecific\nDNA"), (1e-9, "typical\nspecific site"), (1e-12, "very tight\nsite")):
    ax.plot([x], [1 / (KON * x)], "o", color=charts.line("negative"), ms=4.5)
    ax.text(x * 1.6, 1 / (KON * x) * 1.6, txt, fontsize=7, color=P.ink(), va="bottom")
ax.set_xlim(1e-13 / 2, 2e-5)
ax.set_ylim(1e-4, 3e5)
charts.style_axes(ax, "K_D / M", "residence time 1/k_off / s")
ax.set_title("C   Affinity is lifetime", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
