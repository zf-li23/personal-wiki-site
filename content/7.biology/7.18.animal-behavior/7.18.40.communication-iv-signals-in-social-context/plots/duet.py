"""Schematic spectrogram of an antiphonal duet (plain-tailed wren style): male and female syllables alternate."""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
fig, ax = plt.subplots(figsize=(10, 3.2))
t0 = 0.0
period = 0.32
for k in range(6):
    tm = t0 + k * period
    tt = np.linspace(0, 0.11, 40)
    ax.plot((tm + tt) * 1e3, 2.2 + 1.6 * np.sin(np.pi * tt / 0.11), color=P.edge("dna"), lw=3.2)   # male: arched note
    tf = tm + 0.15
    tt2 = np.linspace(0, 0.12, 40)
    ax.plot((tf + tt2) * 1e3, 4.6 - 1.8 * tt2 / 0.12, color=P.edge("rna"), lw=3.2)                # female: downsweep
    ax.plot((tf + tt2) * 1e3, 2 * (4.6 - 1.8 * tt2 / 0.12), color=P.edge("rna"), lw=1.2, alpha=0.5)
ax.plot([0, period * 1e3], [9.6, 9.6], color=P.muted(), lw=4, solid_capstyle="butt")
ax.text(period * 500, 9.9, "one cycle", ha="center", fontsize=8, color=P.muted())
ax.text(55, 0.8, "male", color=P.edge("dna"), fontsize=9, ha="center")
ax.text(210, 0.8, "female", color=P.edge("rna"), fontsize=9, ha="center")
ax.annotate("", (150, 3.2), (110, 3.2), arrowprops=dict(arrowstyle="<->", color=P.muted(), lw=0.8))
ax.text(130, 2.6, "gap", fontsize=7.5, ha="center", color=P.muted())
ax.set_xlim(-20, 6 * period * 1e3 + 20); ax.set_ylim(0, 10.8)
ax.set_xlabel("Time / ms"); ax.set_ylabel("Frequency / kHz")
for sp in ("top", "right"):
    ax.spines[sp].set_visible(False)
fig.tight_layout()
