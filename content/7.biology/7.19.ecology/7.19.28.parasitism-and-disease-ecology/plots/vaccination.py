"""Vaccination (Section 28.3.2).
A: the critical vaccination coverage p_c = 1 - 1/R0, with approximate ranges of R0 for several
infections (commonly cited values, from Anderson and May 1991 and later estimates).
B: incomplete vaccination of newborns against rubella (R0 = 7, rectangular survival to L = 70
years, coverage p): the force of infection Lambda, from the endemic condition that the mean
susceptible fraction equals 1/R0, falls with p; the mean age at infection 1/Lambda rises (left axis).
Right axis, relative to p = 0: total infections fall in proportion to the coverage gap, but
infections at ages 15-45 (childbearing age) fall much more slowly and can even rise slightly at low
coverage, because the infections that remain are shifted to older ages.
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT

fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.3))
ax = axes[0]
R = np.linspace(1, 20, 400)
ax.plot(R, 1 - 1 / R, color=P.ink(), lw=1.5)
ax.fill_between(R, 1 - 1 / R, 1, color=P.light("positive"), lw=0)
ax.text(8, 0.97, "coverage sufficient for elimination", fontsize=FS["tiny"], color=P.on_fill(), va="top")
ranges = [("seasonal influenza", 1.2, 1.8, (0.3, 0.06)), ("SARS-CoV-2 (2020)", 2.5, 3.5, (0.6, -0.03)),
          ("smallpox, polio, rubella", 4, 7, (0.4, -0.05)), ("mumps", 10, 12, (-0.2, -0.06)),
          ("measles, pertussis", 12, 18, (-1.0, -0.06))]
for name, lo, hi, (dx, dy) in ranges:
    rr = np.linspace(lo, hi, 50)
    ax.plot(rr, 1 - 1 / rr, color=C.line("negative"), lw=4, solid_capstyle="butt")
    ax.text(hi + dx, 1 - 1 / hi + dy, name, va="center", fontsize=FS["tiny"], color=P.ink())
ax.set_xlim(1, 20)
ax.set_ylim(0, 1)
C.style_axes(ax, "Basic reproduction number R0", "Critical coverage p_c = 1 − 1/R0")
C.title(ax, "A  Herd immunity threshold")

ax = axes[1]
from scipy.optimize import brentq
R0, L = 7.0, 70.0
p = np.linspace(0, 1 - 1 / R0 - 1e-3, 300)
Lam = np.array([brentq(lambda x: (1 - pp) * (1 - np.exp(-x * L)) / (x * L) - 1 / R0, 1e-6, 10) for pp in p])
total = (1 - p) * (1 - np.exp(-Lam * L))
child = (1 - p) * (np.exp(-15 * Lam) - np.exp(-45 * Lam))
ax.plot(p, 1 / Lam, color=C.line("dna"), lw=1.5, label="mean age at infection")
ax.set_ylim(0, 60)
C.style_axes(ax, "Vaccination coverage p", "Mean age at infection (years)")
ax2 = ax.twinx()
ax2.plot(p, total / total[0], color=P.muted(), lw=1.3, ls=(0, (4, 2)), label="all infections (relative)")
ax2.plot(p, child / child[0], color=C.line("negative"), lw=1.5, label="infections at ages 15–45 (relative)")
ax2.set_ylim(0, 1.3)
C.style_axes(ax2, None, "Infections relative to p = 0")
ax2.spines["right"].set_visible(True)
ax2.spines["right"].set_color(P.muted())
ax.axvline(1 - 1 / R0, color=P.muted(), lw=0.8)
ax.text(1 - 1 / R0 - 0.01, 57, "p_c", ha="right", va="top", fontsize=FS["tiny"], color=P.muted())
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, fontsize=FS["tiny"], frameon=False, loc="upper left")
C.title(ax, "B  Rubella: partial vaccination raises the age at infection")
fig.tight_layout()
