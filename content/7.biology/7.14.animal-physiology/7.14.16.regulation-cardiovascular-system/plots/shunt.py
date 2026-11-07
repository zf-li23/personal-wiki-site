"""Intracardiac shunting in an undivided ventricle, and arterial pressures across vertebrates.

A: if one ventricle ejects into the systemic and pulmonary circuits at the same pressure, flows divide in
inverse proportion to resistance, Q_p/Q_s = R_s/R_p. Pulmonary vasoconstriction (apnoea, diving) raises R_p
and diverts blood from the lungs (net right-to-left shunt); during ventilation R_p falls (left-to-right shunt).
With a fully divided heart Q_p = Q_s regardless of resistance.
B: representative mean arterial pressures (approximate; values vary between studies, species and temperature).
Fish: ventral aorta (before the gills) and dorsal aorta (after the gills). Others: systemic and pulmonary arteries.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
fig, (ax, bx) = plt.subplots(1, 2, figsize=(11.5, 4.3), gridspec_kw={"width_ratios": [1, 1.25]})
ratio = np.logspace(-1, 1, 200)
ax.loglog(ratio, 1 / ratio, color=P.edge("dna"), lw=2.2, label="undivided ventricle: Q$_p$/Q$_s$ = R$_s$/R$_p$")
ax.axhline(1, color=P.edge("blood"), lw=1.8, ls="--", label="divided heart (bird, mammal)")
ax.plot([0.5], [2], "o", color=P.ink(), ms=6)
ax.annotate("breathing:\nL-to-R shunt", xy=(0.5, 2), xytext=(0.13, 3.5), fontsize=8, color=P.muted(),
            arrowprops=dict(arrowstyle="->", color=P.muted()))
ax.plot([4], [0.25], "o", color=P.ink(), ms=6)
ax.annotate("apnoea or diving:\nR-to-L shunt", xy=(4, 0.25), xytext=(1.3, 0.13), fontsize=8, color=P.muted(),
            arrowprops=dict(arrowstyle="->", color=P.muted()))
ax.set_xlabel("Pulmonary / systemic resistance R$_p$/R$_s$")
ax.set_ylabel("Pulmonary / systemic flow Q$_p$/Q$_s$")
ax.legend(frameon=False, fontsize=7.5, loc="upper right")
ax.set_title("A  Resistance steers the shunt", loc="left", fontsize=10)

groups = ["Trout", "Frog", "Turtle", "Python", "Monitor\nlizard", "Alligator", "Chicken", "Human"]
sysp = [40, 30, 35, 60, 70, 65, 140, 93]
pulp = [28, 25, 30, 20, 20, 18, 20, 15]
x = np.arange(len(groups))
bx.bar(x - 0.2, sysp, 0.4, color=P.fill("blood"), edgecolor=P.edge("blood"), label="systemic (fish: ventral aorta)")
bx.bar(x + 0.2, pulp, 0.4, color=P.fill("dna"), edgecolor=P.edge("dna"), label="pulmonary (fish: dorsal aorta)")
bx.set_xticks(x)
bx.set_xticklabels(groups, fontsize=8)
bx.set_ylabel("Mean arterial pressure / mmHg (approx.)")
bx.set_ylim(0, 160)
bx.legend(frameon=False, fontsize=7.5, loc="upper left")
bx.set_title("B  Pressure separation evolved several times", loc="left", fontsize=10)
for a in (ax, bx):
    a.grid(True, alpha=0.3, which="both" if a is ax else "major")
fig.tight_layout()
