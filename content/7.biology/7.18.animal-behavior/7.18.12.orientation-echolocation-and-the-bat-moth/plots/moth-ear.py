"""Two receptor cells, two defenses: the noctuid moth ear read against distance.

Spikes per call pulse of the A1 and A2 cells are modeled as sigmoid functions of sound level
(A1 threshold 45 dB SPL, A2 25 dB less sensitive; first-spike latency shortens with level).
B converts level to distance for a bat call of 120 dB SPL at 10 cm at about 30 kHz
(spherical spreading plus 0.8 dB/m absorption). Values are illustrative but match the
orders of magnitude measured by Roeder and later workers.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
L = np.linspace(20, 110, 300)


def spikes(L, T, nmax=8.0, w=5.0):
    return nmax / (1 + np.exp(-(L - T - 2 * w) / w))


TA1, TA2 = 45.0, 70.0
fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 3.9))
a.plot(L, spikes(L, TA1), color=P.edge("dna"), lw=2, label="A1")
a.plot(L, spikes(L, TA2), color=P.edge("negative"), lw=2, label="A2")
a.axvline(TA1, color=P.edge("dna"), ls=":", lw=0.8)
a.axvline(TA2, color=P.edge("negative"), ls=":", lw=0.8)
a.set_xlabel("Sound level at the moth / dB SPL")
a.set_ylabel("Spikes per call")
a.legend(frameon=False, fontsize=8, loc="upper left")
a.set_title("A", loc="left", fontweight="bold")
ax2 = a.twinx()
lat = 4 + 18 * np.exp(-(L - TA1) / 12)
lat[L < TA1] = np.nan
ax2.plot(L, lat, color=P.edge("dna"), ls="--", lw=1)
ax2.set_ylabel("A1 first-spike latency / ms (dashed)", fontsize=8)
ax2.set_ylim(0, 30)
ax2.spines["top"].set_visible(False)

r = np.logspace(-0.5, 1.8, 400)
Lr = 120 - 20 * np.log10(r / 0.1) - 0.8 * (r - 0.1)
b.plot(r, spikes(Lr, TA1), color=P.edge("dna"), lw=2, label="A1")
b.plot(r, spikes(Lr, TA2), color=P.edge("negative"), lw=2, label="A2")
b.axvspan(0.3, 3.0, color=P.light("negative"), alpha=0.5, lw=0)
b.axvspan(3.0, 35, color=P.light("dna"), alpha=0.35, lw=0)
b.text(1.0, 8.6, "erratic flight,\npower dive", fontsize=8, ha="center", color=P.edge("negative"))
b.text(10, 8.6, "turn away from the bat\n(negative phonotaxis)", fontsize=8, ha="center", color=P.edge("dna"))
b.annotate("bat can detect\nthe moth (≈ 3–5 m)", (4, 0.6), (12, 3.2), fontsize=7.5, color=P.ink(),
           arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
b.set_xscale("log")
b.set_xlim(0.3, 60)
b.set_ylim(0, 10)
b.invert_xaxis()
b.set_xlabel("Distance of the bat / m")
b.set_ylabel("Spikes per call")
b.set_title("B", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
