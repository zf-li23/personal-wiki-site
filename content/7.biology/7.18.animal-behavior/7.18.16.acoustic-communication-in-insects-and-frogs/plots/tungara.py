"""The tungara frog's call and the female inner ear (schematic, after Ryan and colleagues).

A: frequency-time sketch of a complex call: a whine sweeping from about 900 to 400 Hz in 350 ms
(fundamental and second harmonic), followed by a chuck of 40 ms whose harmonics of a ~220 Hz
fundamental carry most energy near 2.5 kHz. B: approximate call spectra (relative level) of the
whine and the chuck against the inverted tuning curves (threshold) of the two auditory end organs:
the amphibian papilla (low frequencies, best near 0.6 kHz) and the basilar papilla (best near 2.1 kHz
in females). The chuck's dominant frequency falls on the basilar papilla.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 3.8))
t = np.linspace(0, 0.35, 200)
f0 = 900 * (400 / 900) ** (t / 0.35)
a.plot(t * 1e3, f0 / 1e3, color=P.edge("dna"), lw=3, label="whine")
a.plot(t * 1e3, 2 * f0 / 1e3, color=P.edge("dna"), lw=1.2, alpha=0.6)
for k in range(1, 22):
    f = 0.22 * k
    lw = 3 * np.exp(-((f - 2.5) / 0.8) ** 2) + 0.3
    a.plot([370, 410], [f, f], color=P.edge("rna"), lw=lw, solid_capstyle="butt")
a.text(390, 5.0, "chuck", ha="center", fontsize=8, color=P.edge("rna"))
a.text(150, 1.25, "whine", fontsize=8, color=P.edge("dna"))
a.set_xlim(-10, 430); a.set_ylim(0, 5.4)
a.set_xlabel("Time / ms"); a.set_ylabel("Frequency / kHz")
a.set_title("A", loc="left", fontweight="bold")
f = np.linspace(0.1, 5, 500)
spec_w = np.exp(-((f - 0.65) / 0.25) ** 2)
spec_c = np.exp(-((f - 2.5) / 0.6) ** 2) * 0.8
b.fill_between(f, 0, spec_w, color=P.light("dna"), alpha=0.8, lw=0, label="whine spectrum")
b.fill_between(f, 0, spec_c, color=P.light("rna"), alpha=0.8, lw=0, label="chuck spectrum")
b2 = b.twinx()
thr_ap = 40 + 30 * (np.log(f / 0.6) / np.log(3)) ** 2
thr_bp = 45 + 120 * (np.log(f / 2.1)) ** 2
b2.plot(f, thr_ap, color=P.edge("dna"), lw=2, label="amphibian papilla")
b2.plot(f, thr_bp, color=P.edge("negative"), lw=2, label="basilar papilla")
b2.set_ylim(100, 30)
b2.set_ylabel("Threshold / dB SPL (inverted)")
b.set_xlabel("Frequency / kHz"); b.set_ylabel("Relative call energy")
b.set_ylim(0, 1.3); b.set_xlim(0.1, 5)
h1, l1 = b.get_legend_handles_labels(); h2, l2 = b2.get_legend_handles_labels()
b.legend(h1 + h2, l1 + l2, frameon=False, fontsize=7.5, loc="upper right")
b.set_title("B", loc="left", fontweight="bold")
for ax in (a, b):
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
b2.spines["top"].set_visible(False)
fig.tight_layout()
