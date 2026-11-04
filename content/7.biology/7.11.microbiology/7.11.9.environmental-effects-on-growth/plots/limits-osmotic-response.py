# Temperature limits of life and the osmotic response of a bacterium.
# A: upper temperature limits for growth of groups of organisms (data from Madigan et al. 2019; ranges drawn as
#    bars from their lower to upper value). Above about 65 C only prokaryotes, above 95 C only archaea grow;
#    the record is 122 C (Methanopyrus kandleri strain 116).
# B: the two-stage response of Escherichia coli to a sudden increase in external osmolarity at t = 0 (model
#    curves, arbitrary units, after the sequence described for E. coli): K+ is taken up within minutes and
#    glutamate is made as its counterion; over the following hour, glycine betaine taken up from the medium
#    (or trehalose made by the cell) replaces most of the K+ glutamate, and growth resumes. Modeled as
#    first-order relaxations: K+ rises with a time constant of 3 min and decays towards a lower level with a
#    time constant of 25 min once betaine (time constant 20 min, starting after 5 min) accumulates.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 2, figsize=(13.0, 4.3), gridspec_kw=dict(width_ratios=[1.1, 1.0], wspace=0.55))

ax = axs[0]
groups = [("fish and other aquatic vertebrates", 38, 38, "animal"), ("insects", 45, 50, "animal"),
          ("vascular plants", 45, 45, "plant"), ("mosses", 50, 50, "plant"), ("protozoa", 56, 56, "neutral"),
          ("algae", 55, 60, "plant"), ("fungi", 60, 62, "highlight"), ("cyanobacteria", 70, 73, "dna"),
          ("anoxygenic phototrophs", 70, 73, "dna"), ("Bacteria (chemotrophs)", 95, 95, "bacterium"),
          ("Archaea (chemotrophs)", 122, 122, "negative")]
for k, (name, lo, hi, tok) in enumerate(groups):
    y = len(groups) - k
    ax.barh(y, hi, color=P.mix(P.fill(tok), P.surface(), 0.35), edgecolor=P.edge(tok), lw=0.8, height=0.65)
    if hi > lo:
        ax.plot([lo, hi], [y, y], color=P.edge(tok), lw=2.2)
    ax.text(hi + 2, y, f"{lo}" if lo == hi else f"{lo}–{hi}", va="center", fontsize=6.8, color=P.ink())
ax.set_yticks(range(len(groups), 0, -1), [g[0] for g in groups], fontsize=7)
ax.axvline(65, color=P.muted(), lw=0.8, ls=":")
ax.text(66, 0.2, "prokaryotes only", fontsize=6.8, color=P.muted())
ax.set_xlim(0, 135)
ax.set_ylim(0, len(groups) + 0.8)
charts.style_axes(ax, "upper temperature limit for growth / $^\\circ$C", None)
charts.title(ax, "A   Upper temperature limits of life")

ax = axs[1]
t = np.linspace(-10, 90, 600)
tt = np.clip(t, 0, None)
bet = np.where(t > 5, 1 - np.exp(-(t - 5) / 20), 0.0)
k_up = 1 - np.exp(-tt / 3)
K = np.where(t < 0, 0.2, 0.2 + k_up * (1.0 - 0.6 * bet))
glu = np.where(t < 0, 0.25, 0.25 + 0.8 * k_up * (1.0 - 0.6 * bet))
growth = np.where(t < 0, 1.0, np.where(t < 2, 0.0, 0.8 * bet))
ax.axvline(0, color=P.ink(), lw=0.8)
ax.text(1, 1.32, "osmotic upshock", fontsize=6.8, color=P.ink())
ax.plot(t, K, color=charts.line("k"), lw=2.0, label="cytoplasmic K$^+$")
ax.plot(t, glu, color=charts.line("metabolite"), lw=1.6, ls="--", label="glutamate")
ax.plot(t, 1.1 * bet, color=charts.line("positive"), lw=2.0, label="glycine betaine")
ax.plot(t, growth, color=P.muted(), lw=1.3, ls=":", label="growth rate (relative)")
ax.set_ylim(0, 1.45)
ax.set_xlim(-10, 90)
ax.set_yticks([])
ax.legend(fontsize=6.8, frameon=False, loc="lower right")
charts.style_axes(ax, "time after upshock / min", "amount (arbitrary units)")
charts.title(ax, "B   The osmotic response of $E.\\ coli$")
