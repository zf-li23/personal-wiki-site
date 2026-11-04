# How a virus is counted.
# A: the plaque assay - a tenfold dilution series plated on lawns, with the titre computed from a
#    countable plate (17 plaques from 0.1 ml of the 1e-6 dilution -> 1.7e8 PFU/ml).
# B: the dose-response curve of the assay: one-hit kinetics give a straight line (one particle suffices),
#    two-hit kinetics a parabola.
# C: an end-point dilution assay scored for cytopathic effect in ten wells per dilution, with the 50 %
#    end point computed by the Reed-Muench and Spearman-Karber methods from the same data.
# D: particle-to-PFU ratios of representative viruses (ranges from Flint et al., Principles of Virology, 2015).
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

import wikibio as bio
from wikibio import charts
from wikibio import stats as S

P = bio.P
fig = plt.figure(figsize=(15.0, 4.6))
gs = fig.add_gridspec(1, 4, width_ratios=[1.35, 0.85, 1.15, 0.95], wspace=0.34)

# ---------------------------------------------------------------- A: plaque assay
ax = fig.add_subplot(gs[0, 0])
ax.set_xlim(0, 10.6)
ax.set_ylim(0, 10.2)
ax.set_aspect("equal")
ax.axis("off")
charts.title(ax, "A   The plaque assay")
tubes = S.dilution_series(ax, (0.35, 7.3), n=6, token="virus", dx=1.65, w=0.75, h=1.5, factor="1:10", fill_frac=0.6)
for (tx, ty), lab in zip(tubes, ["$10^{-2}$", "$10^{-3}$", "$10^{-4}$", "$10^{-5}$", "$10^{-6}$", "$10^{-7}$"]):
    bio.label(ax, (tx, ty - 0.45), lab, size="tiny", color=P.muted())
rng = np.random.default_rng(4)
plates = [(2.0, 3.4, None, "too many\nto count", "$10^{-4}$"), (5.3, 3.4, 17, "17 plaques", "$10^{-6}$"),
          (8.6, 3.4, 2, "2 plaques", "$10^{-7}$")]
for px, py, n, txt, dil in plates:
    ax.add_patch(Circle((px, py), 1.45, facecolor=P.mix(P.fill("bacterium"), P.surface(), 0.25),
                        edgecolor=P.edge("bacterium"), lw=1.1, zorder=5))
    if n is None:
        pts = rng.uniform(-1, 1, (60, 2))
        pts = pts[np.linalg.norm(pts, axis=1) < 0.93] * 1.3
        for q in pts:
            ax.add_patch(Circle((px + q[0], py + q[1]), 0.17, facecolor=P.surface(), edgecolor="none", zorder=6))
    else:
        pts = rng.uniform(-1, 1, (300, 2))
        pts = pts[np.linalg.norm(pts, axis=1) < 0.85][:n] * 1.35
        for q in pts:
            ax.add_patch(Circle((px + q[0], py + q[1]), 0.17, facecolor=P.surface(), edgecolor=P.edge("neutral"),
                                lw=0.4, zorder=6))
    bio.label(ax, (px, py - 1.85), txt, size="tiny", color=P.muted())
    bio.label(ax, (px, py + 1.7), dil, size="tiny", color=P.muted())
    bio.arrow(ax, (px, 6.6), (px, 5.3), kind="process", lw=0.9, head=0.18, color=P.muted())
bio.label(ax, (5.3, 0.5), "titre = 17 × 10 × $10^{6}$ = 1.7 × $10^{8}$ PFU/ml", size="small")

# ---------------------------------------------------------------- B: dose-response
ax = fig.add_subplot(gs[0, 1])
x = np.linspace(0, 1, 200)
ax.plot(x, 24 * x, color=charts.line("dna"), lw=2.0, label="one hit: $\\propto$ dose")
ax.plot(x, 24 * x ** 2, color=charts.line("drug"), lw=2.0, ls=(0, (4, 2.2)), label="two hits: $\\propto$ dose$^2$")
ax.set_xlim(0, 1.02)
ax.set_ylim(0, 26)
ax.legend(fontsize=6.8, frameon=False, loc="upper left", labelcolor=P.ink())
charts.style_axes(ax, "relative virus concentration", "plaques")
charts.title(ax, "B   Dose–response")

# ---------------------------------------------------------------- C: end-point dilution
ax = fig.add_subplot(gs[0, 2])
ax.set_xlim(0, 10.4)
ax.set_ylim(0, 8.4)
ax.set_aspect("equal")
ax.axis("off")
charts.title(ax, "C   End-point dilution (TCID$_{50}$)")
pos = [1.0, 1.0, 0.9, 0.4, 0.1, 0.0]           # fraction of 10 wells with cytopathic effect
dil = [-2, -3, -4, -5, -6, -7]
rng = np.random.default_rng(7)
grid = np.zeros((len(pos), 10))
for i, p_ in enumerate(pos):
    k = int(round(p_ * 10))
    idx = rng.permutation(10)[:k]
    grid[i, idx] = 1.0
box = S.well_plate(ax, (0.6, 2.9), grid, cell=0.52, token="negative")
for i, (p_, d) in enumerate(zip(pos, dil)):
    y = box[1] + box[3] - 0.11 - (i + 0.5) * 0.52
    bio.label(ax, (0.45, y), f"$10^{{{d}}}$", size="tiny", color=P.muted(), ha="right")
    bio.label(ax, (box[0] + box[2] + 0.15, y), f"{int(p_ * 10)}/10", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (box[0] + box[2] / 2, box[1] + box[3] + 0.35), "10 wells per dilution, scored for cytopathic effect",
          size="tiny", color=P.muted())
# the two estimators, computed from the data above
d_step = 1.0
sp = dil[0] + d_step / 2 - d_step * sum(pos)                     # Spearman-Karber
above, below = 0.9, 0.4                                          # nearest fractions straddling 0.5 (cumulative form)
cum_pos = np.cumsum(pos[::-1])[::-1]                             # cumulative positives from the bottom
cum_neg = np.cumsum([1 - p_ for p_ in pos])
ratio = cum_pos / (cum_pos + cum_neg)
i0 = int(np.argmax(ratio < 0.5)) - 1
pd = (ratio[i0] - 0.5) / (ratio[i0] - ratio[i0 + 1])
rm = dil[i0] - pd * d_step                                       # Reed-Muench
bio.label(ax, (0.6, 2.1), f"Reed–Muench:  $\\log_{{10}}$ end point = {rm:.2f}".replace("-", "−"), size="tiny", ha="left")
bio.label(ax, (0.6, 1.5), f"Spearman–Kärber:  $x_0 + d/2 - d\\sum p_i$ = {sp:.2f}".replace("= -", "= −"), size="tiny", ha="left")
bio.label(ax, (0.6, 0.8), f"$\\approx 10^{{{-sp:.1f}}}$ TCID$_{{50}}$ per 0.1 ml  "
                          f"$\\approx$ 0.7 × that in PFU", size="tiny", ha="left")

# ---------------------------------------------------------------- D: particle-to-PFU ratios
ax = fig.add_subplot(gs[0, 3])
rows = [("papillomavirus", 1e4, 1e4), ("poliovirus", 30, 1000), ("herpes simplex", 50, 200),
        ("simian virus 40", 100, 200), ("adenovirus", 20, 100), ("influenza virus", 20, 50),
        ("reovirus", 10, 10), ("Semliki Forest virus", 1, 2), ("many bacteriophages", 1, 1)]
y = np.arange(len(rows))[::-1]
for yi, (name, lo, hi) in zip(y, rows):
    tok = "positive" if hi <= 2 else "highlight" if hi <= 100 else "negative"
    c = charts.line(tok)
    if hi > lo:
        ax.plot([lo, hi], [yi, yi], color=c, lw=3.2, solid_capstyle="round")
    ax.plot([lo], [yi], "o", ms=4.5, color=c)
    ax.plot([hi], [yi], "o", ms=4.5, color=c)
ax.set_xscale("log")
ax.set_xlim(0.6, 3e4)
ax.set_yticks(y)
ax.set_yticklabels([r[0] for r in rows], fontsize=7)
ax.set_ylim(-0.8, len(rows) - 0.2)
charts.style_axes(ax, "particles per plaque-forming unit")
charts.title(ax, "D   Particle-to-PFU ratio")
