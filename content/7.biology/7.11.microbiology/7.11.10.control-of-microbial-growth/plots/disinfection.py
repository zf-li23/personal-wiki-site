# Chemical disinfection.
# A: the Chick-Watson model, ln(N/N0) = -k C^n t, for a disinfectant at three concentrations with n = 1 and
#    k = 0.46 L mg^-1 min^-1 (illustrative): survival falls linearly on a log scale at a rate proportional to C.
# B: the exposure time for a 99 % (2-log) kill, t = ln(100) / (k C^n), against concentration on log-log axes:
#    the slope is -n. For n = 1 the product C t is constant (the "Ct value" used in water treatment); for
#    n > 1 dilution weakens the agent more than proportionally (phenols and alcohols have large n), for n < 1
#    less than proportionally.
# C: the approximate order of resistance of microorganisms and infectious agents to chemical disinfectants
#    (the commonly cited hierarchy; the order of neighbouring groups depends on the agent).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig = plt.figure(figsize=(14.0, 4.3))
gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 1.15], wspace=0.33)

ax = fig.add_subplot(gs[0, 0])
k = 0.46
t = np.linspace(0, 10, 200)
for C, tok in ((0.5, "dna"), (1.0, "highlight"), (2.0, "negative")):
    ax.plot(t, np.exp(-k * C * t), color=charts.line(tok), lw=2.0, label=f"$C$ = {C:g} mg L$^{{-1}}$")
ax.set_yscale("log")
ax.set_ylim(1e-6, 1.5)
ax.legend(fontsize=6.8, frameon=False, loc="lower left")
charts.style_axes(ax, "contact time $t$ / min", "surviving fraction $N/N_0$")
charts.title(ax, "A   Chick–Watson kinetics")

ax = fig.add_subplot(gs[0, 1])
C = np.logspace(-1, 1, 100)
for n, tok in ((0.5, "dna"), (1.0, "ink"), (2.0, "negative")):
    tt = np.log(100) / (k * C**n)
    ax.plot(C, tt, color=charts.line(tok) if tok != "ink" else P.ink(), lw=2.0, label=f"$n$ = {n:g}")
ax.set_xscale("log")
ax.set_yscale("log")
ax.legend(fontsize=6.8, frameon=False, loc="upper right")
ax.text(0.12, 0.4, "slope $= -n$;\n$n = 1$: $Ct$ constant", fontsize=6.8, color=P.ink())
charts.style_axes(ax, "concentration $C$ / (mg L$^{-1}$)", "time for 99 % kill / min")
charts.title(ax, "B   Concentration exponent $n$")

ax = fig.add_subplot(gs[0, 2])
ax.set_xlim(0, 10)
ax.set_ylim(0, 9.4)
ax.axis("off")
charts.title(ax, "C   Resistance to disinfectants")
groups = [("prions", "neutral"), ("bacterial endospores", "highlight"), ("protozoan oocysts", "plant"),
          ("mycobacteria", "bacterium"), ("small nonenveloped viruses", "virus"), ("fungi", "plant"),
          ("vegetative bacteria", "bacterium"), ("enveloped viruses", "virus")]
for i, (name, tok) in enumerate(groups):
    y = 8.4 - i * 1.05
    w = 7.0 - i * 0.55
    bio.box(ax, (1.5 + w / 2, y), w, 0.8, token=tok, text=name, size="tiny")
ax.annotate("", xy=(0.6, 8.6), xytext=(0.6, 0.9), arrowprops=dict(arrowstyle="-|>", color=P.ink(), lw=1.2))
ax.text(0.35, 4.75, "more resistant", rotation=90, ha="center", va="center", fontsize=7.2, color=P.ink())
