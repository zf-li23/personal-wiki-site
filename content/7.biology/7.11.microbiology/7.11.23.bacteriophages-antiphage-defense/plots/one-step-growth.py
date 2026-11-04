# Resolving one cycle of phage growth: the three classical experiments, simulated from the same model.
# Model: an infected cell assembles particles linearly from the end of the eclipse period (12 min) at a
# rate that reaches the burst size (100) at its own lysis time, drawn from a normal distribution with
# mean 25 min and s.d. 3 min (truncated below 15 min).
# A: the one-step growth experiment - infective centres measured by plating the whole culture.
# B: the premature-lysis experiment - samples lysed artificially before the cells burst; infectious
#    particles appear only after the eclipse period, and the DNA pool rises earlier.
# C: the single-burst experiment - the culture distributed into many small tubes with on average 0.6
#    infected cells per tube; the distribution of yields per occupied tube is wide.
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
ECL, MEAN, SD, BURST = 12.0, 25.0, 3.0, 100.0

fig = plt.figure(figsize=(13.8, 4.3))
gs = fig.add_gridspec(1, 3, width_ratios=[1.15, 1.05, 1.0], wspace=0.33)

t = np.linspace(0, 50, 800)
F = norm.cdf(t, MEAN, SD)                                  # fraction of infected cells already lysed
inside = np.clip((t - ECL) / (MEAN - ECL), 0, 1.4) * BURST  # particles inside a cell that has not yet lysed

# ---------------------------------------------------------------- A: one-step growth
ax = fig.add_subplot(gs[0, 0])
centres = (1 - F) + F * BURST                              # infective centres per originally infected cell
ax.plot(t, centres, color=charts.line("dna"), lw=2.1)
ax.set_yscale("log")
ax.set_ylim(0.6, 300)
ax.set_xlim(0, 50)
for x0, x1, txt, tok in ((0, 19.5, "latent period", "highlight"), (19.5, 31, "rise", "positive"),
                         (31, 50, "plateau", "neutral")):
    ax.axvspan(x0, x1, color=P.mix(P.fill(tok), P.surface(), 0.8 if not P.is_dark() else 0.88), zorder=0)
    ax.text((x0 + x1) / 2, 215, txt, fontsize=7, color=P.muted(), ha="center", va="top")
ax.annotate("", xy=(44, 1), xytext=(44, BURST), arrowprops=dict(arrowstyle="<->", color=P.muted(), lw=0.9))
ax.text(41.5, 4.0, "burst size =\nplateau / latent-period level\n= 100", fontsize=7, color=P.muted(),
        va="center", ha="right")
charts.style_axes(ax, "time after infection / min", "plaque-forming units per infected cell")
charts.title(ax, "A   One-step growth (Ellis and Delbrück)")

# ---------------------------------------------------------------- B: premature lysis
ax = fig.add_subplot(gs[0, 1])
intra = (1 - F) * inside + F * BURST                       # all particles present, cells lysed artificially
dna = np.minimum(np.clip((t - 5) / (MEAN - 5), 0, None) * BURST * 1.5, 165.0)
ax.plot(t, intra, color=charts.line("dna"), lw=2.1, label="infectious particles (total)")
ax.plot(t, dna, color=charts.line("rna"), lw=1.7, ls=(0, (1, 1.8)), label="phage DNA (genome equivalents)")
ax.plot(t, F * BURST, color=charts.line("drug"), lw=1.7, ls=(0, (4, 2.2)), label="free phage in the medium")
ax.axvspan(0, ECL, color=P.mix(P.fill("highlight"), P.surface(), 0.8 if not P.is_dark() else 0.88), zorder=0)
ax.text(ECL / 2, 196, "eclipse", fontsize=7, color=P.muted(), ha="center", va="top")
ax.set_xlim(0, 50)
ax.set_ylim(0, 205)
ax.legend(fontsize=7, frameon=False, loc="upper left", labelcolor=P.ink())
charts.style_axes(ax, "time after infection / min", "phage equivalents per infected cell")
charts.title(ax, "B   Premature lysis (Doermann)")

# ---------------------------------------------------------------- C: single bursts
ax = fig.add_subplot(gs[0, 2])
n_tubes = 400
cells = rng.poisson(0.6, n_tubes)                          # infected cells per tube
yields = np.array([rng.gamma(shape=6.25, scale=BURST / 6.25, size=c).sum() for c in cells])  # CV = 0.4 per burst
occupied = yields[cells > 0]
bins = np.arange(0, 420, 25)
ax.hist(occupied, bins=bins, color=P.fill("virus"), edgecolor=P.edge("virus"), lw=0.6)
ax.axvline(occupied.mean(), color=charts.line("negative"), lw=1.4, ls=(0, (4, 2.2)))
ax.text(occupied.mean() + 8, ax.get_ylim()[1] * 0.95, f"mean per occupied tube {occupied.mean():.0f};\n"
        f"corrected for tubes with more than\none infected cell, {BURST:.0f}", fontsize=7,
        color=charts.line("negative"), va="top")
ax.text(205, ax.get_ylim()[1] * 0.62, f"{int((cells == 0).sum())} of {n_tubes} tubes\nempty (not shown);\n"
        f"{int((cells > 1).sum())} with more\nthan one infected cell", fontsize=7, color=P.muted())
charts.style_axes(ax, "phages recovered from one tube", "tubes")
charts.title(ax, "C   Single bursts: one cell at a time")
