# Sequential blockade of folate synthesis and how drug interactions are measured.
# A: bacterial folate pathway: dihydropteroate synthase (DHPS) joins the pterin (DHPPP) to
#    p-aminobenzoate (PABA), sulfonamides compete with PABA; dihydrofolate reductase (DHFR) reduces
#    dihydrofolate (DHF) to tetrahydrofolate (THF), trimethoprim competes with DHF. Humans take up
#    folate from the diet and lack DHPS.
# B: simulated checkerboard: twofold dilutions of drug A (columns) and drug B (rows) in units of their
#    MICs. Inhibition follows a Hill curve in an "effective dose" u = a + b + beta*a*b (a, b in units
#    of the concentrations giving half inhibition, Hill coefficient 2, beta = 6: synergy); wells with
#    inhibition below 90 % are turbid. The outlined well gives the lowest FIC index.
# C: isoboles (combinations giving the same effect, 90 % inhibition) in MIC units: Loewe additivity
#    (straight line, FICI = 1), the Bliss-independence isobole for the same two Hill curves, a synergistic
#    and an antagonistic example (power-law isoboles), and the synergy region FICI <= 0.5.
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

import wikibio as bio
from wikibio import charts

P = bio.P
fig = plt.figure(figsize=(14.5, 4.6))
gs = fig.add_gridspec(1, 3, width_ratios=[1.45, 1, 1], wspace=0.3)

# ---- A: pathway ---------------------------------------------------------------------------------------------
ax = fig.add_subplot(gs[0, 0])
ax.set_xlim(0, 14)
ax.set_ylim(0, 9)
ax.set_aspect("equal")
ax.axis("off")
charts.title(ax, "A   Folate synthesis in bacteria")
node = dict(token="metabolite", size="tiny")
bio.box(ax, (2.0, 7.6), 2.6, 0.75, text="GTP", **node)
bio.box(ax, (2.0, 5.6), 2.6, 0.75, text="DHPPP (pterin)", **node)
bio.box(ax, (6.4, 7.6), 2.0, 0.75, text="PABA", **node)
bio.box(ax, (6.4, 4.2), 3.0, 0.75, text="dihydropteroate", **node)
bio.box(ax, (6.4, 2.4), 2.0, 0.75, text="DHF", **node)
bio.box(ax, (10.6, 2.4), 2.0, 0.75, text="THF", **node)
bio.arrow(ax, (2.0, 7.2), (2.0, 6.0), kind="process", lw=1.0, head=0.16)
bio.label(ax, (2.2, 6.6), "several steps", size="tiny", ha="left", color=P.muted())
bio.arrow(ax, (3.3, 5.4), (5.5, 4.4), kind="process", lw=1.0, head=0.16)
bio.arrow(ax, (6.4, 7.2), (6.4, 4.6), kind="process", lw=1.0, head=0.16)
bio.label(ax, (6.2, 5.9), "DHPS", size="tiny", ha="right", color=P.muted())
bio.arrow(ax, (6.4, 3.8), (6.4, 2.8), kind="process", lw=1.0, head=0.16)
bio.label(ax, (6.6, 3.3), "+ Glu (DHFS)", size="tiny", ha="left", color=P.muted())
bio.arrow(ax, (7.4, 2.4), (9.6, 2.4), kind="process", lw=1.0, head=0.16)
bio.label(ax, (8.5, 2.75), "DHFR", size="tiny", color=P.muted())
bio.label(ax, (11.8, 2.4), "purines,\nthymidylate,\nMet, fMet", size="tiny", ha="left", color=P.muted())
bio.box(ax, (10.0, 6.2), 2.9, 0.8, token="drug", text="sulfonamides", size="tiny")
bio.arrow(ax, (8.55, 6.0), (6.7, 5.7), kind="inhibition", lw=1.2)
bio.box(ax, (8.5, 0.8), 2.9, 0.8, token="drug", text="trimethoprim", size="tiny")
bio.arrow(ax, (8.5, 1.2), (8.5, 2.2), kind="inhibition", lw=1.2)
bio.label(ax, (2.4, 1.6), "humans: dietary folate\n(no DHPS; own DHFR)", size="tiny", color=P.muted())

# ---- B: checkerboard ----------------------------------------------------------------------------------------
n, beta = 2.0, 6.0
x90 = 9 ** (1 / n)  # u giving 90 % inhibition; MIC of each drug alone in half-inhibition units


def inhib(a, b):  # a, b in units of the single-drug MIC
    u = a * x90 + b * x90 + beta * (a * x90) * (b * x90)
    return u ** n / (1 + u ** n)


ax = fig.add_subplot(gs[0, 1])
levels = [0] + [2.0 ** k for k in range(-5, 2)]  # 0, 1/32 ... 2 x MIC
best = (9, None)
for i, a in enumerate(levels):
    for j, b in enumerate(levels):
        grow = inhib(a, b) < 0.9
        col = P.mix(P.fill("bacterium"), P.surface(), 0.1) if grow else P.mix(P.fill("metabolite"), P.surface(), 0.85)
        ax.add_patch(Rectangle((i, j), 0.92, 0.92, facecolor=col, edgecolor=P.muted(), lw=0.4))
        if not grow and a > 0 and b > 0 and a + b < best[0]:
            best = (a + b, (i, j))
i, j = best[1]
ax.add_patch(Rectangle((i - 0.04, j - 0.04), 1.0, 1.0, fill=False, edgecolor=P.ink(), lw=1.6))
ax.text(i + 1.1, j + 0.46, f"FICI = {best[0]:.2f}", ha="left", va="center", fontsize=7, color=P.ink(), bbox=dict(boxstyle="round,pad=0.15", fc=P.surface(), ec="none"))
lab = ["0"] + ["1/32", "1/16", "1/8", "1/4", "1/2", "1", "2"]
ax.set_xticks(np.arange(len(levels)) + 0.46)
ax.set_xticklabels(lab, rotation=60)
ax.set_yticks(np.arange(len(levels)) + 0.46)
ax.set_yticklabels(lab)
ax.set_xlim(-0.2, len(levels))
ax.set_ylim(-0.2, len(levels))
ax.set_aspect("equal")
charts.style_axes(ax, "drug A / MIC$_A$", "drug B / MIC$_B$")
charts.title(ax, "B   Checkerboard (synergy)")

# ---- C: isoboles --------------------------------------------------------------------------------------------
ax = fig.add_subplot(gs[0, 2])
s = np.linspace(0, 1, 200)
ax.plot(s, 1 - s, color=P.ink(), lw=1.5, label="Loewe additivity")
# Bliss isobole: (1 - E_A)(1 - E_B) = 0.1 with E = x^n/(1 + x^n), x = a*x90
aa = np.linspace(0, 1, 400)
EA = (aa * x90) ** n / (1 + (aa * x90) ** n)
EB = 1 - 0.1 / np.maximum(1 - EA, 1e-9)
ok = EB > 0
xb = np.where(ok, (EB / (1 - EB)) ** (1 / n) / x90, np.nan)
ax.plot(aa, xb, color=charts.line("dna"), lw=1.5, ls="--", label="Bliss independence")
# synergistic and antagonistic examples (power-law isoboles)
ax.plot(s, (1 - s ** 0.45) ** (1 / 0.45), color=charts.line("positive"), lw=1.5, label="synergy")
ax.plot(s, (1 - s ** 3.0) ** (1 / 3.0), color=charts.line("negative"), lw=1.5, label="antagonism")
ax.fill_between(s * 0.5, 0, 0.5 - s * 0.5, color=P.mix(P.fill("positive"), P.surface(), 0.7), lw=0)
ax.text(0.08, 0.1, "FICI ≤ 0.5", fontsize=7, color=charts.line("positive"))
ax.set_xlim(0, 1.25)
ax.set_ylim(0, 1.25)
ax.set_aspect("equal")
ax.legend(fontsize=7, frameon=False, loc="upper right", labelcolor=P.ink())
charts.style_axes(ax, "drug A / MIC$_A$", "drug B / MIC$_B$")
charts.title(ax, "C   Isoboles at 90 % inhibition")
