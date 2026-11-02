"""Cost-benefit selection of regulation and of the coherent feed-forward loop.
A: which design of a gene Z has the highest fitness (Formula 17.4.1), as a function of the demand p
(fraction of time Z is useful) and of the cost r of a regulatory system relative to the production
cost c of Z, for a benefit b = 3c: never express, regulate, or express constitutively.
B: integrated fitness of one input pulse of duration D (units: removal time 1/alpha of Z, cost c beta
per unit time, linear benefit reaching 2 c beta at steady state). Simple regulation (solid) loses
fitness in pulses shorter than D_c = 1.59 (the short-pulse approximation gives 2 c beta/(b' beta) = 1,
dotted); a feed-forward loop with delay T_ON = 1 (dashed) ignores short pulses and loses the first
T_ON of long ones.
C: selection in an environment of brief pulses (duration D1, probability p) and long pulses (D2 = 20 D1)
against the benefit-to-cost ratio b(Z_st)/(c beta): the FFL wins above p = 1 - c beta/b(Z_st) (line)."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
cols = ListedColormap([P.fill("neutral"), P.fill("protein"), P.fill("positive")])

fig, axs = plt.subplots(1, 3, figsize=(11, 3.5))
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.17, top=0.86, wspace=0.34)

ax = axs[0]
bc = 3.0
p, rc = np.meshgrid(np.linspace(0, 1, 401), np.linspace(0, 1, 401))
F1 = p * bc - 1.0
F2 = p * bc - p - rc
F3 = np.zeros_like(p)
best = np.argmax(np.stack([F3, F2, F1]), 0)
ax.imshow(best, origin="lower", extent=(0, 1, 0, 1), cmap=cols, vmin=0, vmax=2, aspect="auto")
ax.text(0.06, 0.55, "never\nexpress", fontsize=8, color=P.on_fill())
ax.text(0.50, 0.12, "regulate", fontsize=8, color=P.on_fill())
ax.text(0.70, 0.70, "always\nexpress", fontsize=8, color=P.on_fill())
charts.style_axes(ax, "demand p", "relative cost of regulation r/c")
charts.title(ax, "A  To regulate or not (b = 3c)")

ax = axs[1]
D = np.linspace(0, 5, 400)


def phi(D):
    D = np.maximum(D, 0)
    return -D + 2.0 * (D - (1 - np.exp(-D)))


Dc = brentq(phi, 0.5, 3)
ax.plot(D, phi(D), color=charts.line("protein"), lw=1.6, label="simple regulation")
ax.plot(D, np.where(D > 1, phi(D - 1), 0), "--", color=charts.line("negative"), lw=1.4, label="FFL, T_ON = 1")
ax.plot(D, -D + D**2 / 2, ":", color=P.muted(), lw=1.2, label="short-pulse approximation")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.plot([Dc], [0], "o", ms=4, color=charts.line("protein"))
ax.annotate(f"D_c = {Dc:.2f}", (Dc, 0), (Dc + 0.3, -0.45), fontsize=7, color=P.ink())
ax.set_ylim(-0.8, 3.5)
ax.legend(fontsize=7, frameon=False, loc="upper left")
charts.style_axes(ax, "pulse duration D (1/alpha)", "fitness per pulse (c beta / alpha)")
charts.title(ax, "B  Brief pulses cost fitness")

ax = axs[2]
B, pp = np.meshgrid(np.linspace(0, 4, 401), np.linspace(0, 1, 401))
D1, D2 = 1.0, 20.0
Fs = (1 - pp) * (B - 1) * D2 - pp * D1
Ff = (1 - pp) * (B - 1) * (D2 - D1)
best = np.where((Ff > Fs) & (Ff > 0), 2, np.where((Fs >= Ff) & (Fs > 0), 1, 0))
ax.imshow(best, origin="lower", extent=(0, 4, 0, 1), cmap=cols, vmin=0, vmax=2, aspect="auto")
bb = np.linspace(1, 4, 100)
ax.plot(bb, 1 - 1 / bb, color=P.ink(), lw=1.0)
ax.text(0.15, 0.45, "neither", fontsize=8, color=P.on_fill())
ax.text(2.3, 0.25, "simple\nregulation", fontsize=8, color=P.on_fill())
ax.text(2.6, 0.85, "FFL", fontsize=8, color=P.on_fill())
charts.style_axes(ax, "benefit-to-cost ratio b(Z_st)/(c beta)", "probability p of a brief pulse")
charts.title(ax, "C  When the FFL is selected")
