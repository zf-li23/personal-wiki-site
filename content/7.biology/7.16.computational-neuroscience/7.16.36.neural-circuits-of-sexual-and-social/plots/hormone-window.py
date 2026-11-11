"""Schematic of the organizational and activational effects of gonadal steroids in rodents.

Testosterone (log scale) in male rats: a perinatal surge (late gestation to the first postnatal days),
low juvenile levels, a rise at puberty. The shaded window marks the sensitive period in which estradiol
(aromatized from testosterone in the brain) organizes sexually dimorphic circuits (e.g. SDN-POA);
in adults the same hormones activate behavior. Levels are illustrative, not data.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
t = np.linspace(-6, 70, 800)  # days from birth
male = 0.05 + 2.0 * np.exp(-0.5 * ((t + 1) / 2.2) ** 2) + 1.6 / (1 + np.exp(-(t - 45) / 4))
female = 0.05 + 0.04 / (1 + np.exp(-(t - 40) / 4))

fig, ax = plt.subplots(figsize=(8, 3.4))
ax.axvspan(-4, 10, color=P.light("highlight"), zorder=0)
ax.axvspan(45, 70, color=P.light("neutral"), zorder=0)
ax.semilogy(t, male, color=P.edge("dna"), lw=2.2, label="male testosterone")
ax.semilogy(t, female, color=P.edge("negative"), lw=2.2, ls="--", label="female testosterone")
ax.text(3, 4.5, "organizational\nwindow", ha="center", fontsize=8.5, color=P.muted())
ax.text(57.5, 4.5, "activational\n(adult)", ha="center", fontsize=8.5, color=P.muted())
ax.axvline(0, color=P.muted(), lw=0.8, ls=":")
ax.text(0.5, 0.06, "birth", fontsize=8, color=P.muted())
ax.set_ylim(0.03, 10)
ax.set_xlim(-6, 70)
ax.set_xlabel("Age / days from birth (rat)")
ax.set_ylabel("Plasma testosterone (rel.)")
ax.legend(frameon=False, fontsize=8.5, loc="center right")
ax.grid(True, alpha=0.3, which="both")
fig.tight_layout()
