"""Interaural time difference (ITD) and a Jeffress-type coincidence-detector array.

A: ITD versus azimuth for a spherical head of radius a = 8.75 cm, c = 343 m/s:
Woodworth's high-frequency formula ITD = (a/c)(theta + sin theta) and the low-frequency
(diffraction) value 3 (a/c) sin theta (Kuhn 1977). Dotted: a 10 microsecond discrimination threshold.
B: detectors with internal delays d_k compare phase-locked inputs from the two ears; for a tone of
frequency f the rate is modelled as exp(kappa (cos(2 pi f (ITD - d_k)) - 1)), kappa = 2.
At 500 Hz each detector has one peak within the physiological range; at 1.5 kHz the period
(0.67 ms) is shorter than twice the maximal ITD, so peaks repeat and the code becomes ambiguous.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
a, c = 0.0875, 343.0
th = np.linspace(0, np.pi / 2, 300)
wood = a / c * (th + np.sin(th)) * 1e6
low = 3 * a / c * np.sin(th) * 1e6

fig, axs = plt.subplots(1, 3, figsize=(13, 4.0))
ax = axs[0]
ax.plot(np.degrees(th), wood, color=P.edge("dna"), lw=2, label="Woodworth (high frequency)")
ax.plot(np.degrees(th), low, color=P.edge("rna"), lw=2, ls="--", label="3(a/c) sin θ (low frequency)")
ax.axhline(10, color=P.muted(), lw=0.8, ls=":")
ax.text(60, 25, "10 µs threshold ≈ 1° near midline", fontsize=8, color=P.muted(), ha="center")
ax.set_xlabel("Azimuth θ / degrees (0 = straight ahead)")
ax.set_ylabel("ITD / µs")
ax.set_xlim(0, 90)
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("A  ITD of a spherical head", loc="left", fontsize=10)

itd = np.linspace(-0.7, 0.7, 600)
delays = np.linspace(-0.6, 0.6, 7)
cmap = [P.edge("dna"), P.edge("enzyme"), P.edge("protein"), P.ink(), P.edge("protein"),
        P.edge("enzyme"), P.edge("dna")]
for k, (f, title) in enumerate(((500, "B  Detector array, 500 Hz"),
                               (1500, "C  Detector array, 1.5 kHz"))):
    bx = axs[k + 1]
    for d, col in zip(delays, cmap):
        r = np.exp(2 * (np.cos(2 * np.pi * f * 1e-3 * (itd - d)) - 1))
        bx.plot(itd, r, color=col, lw=1.4)
    bx.axvspan(-0.66, 0.66, color=P.fill("highlight"), alpha=0.2, lw=0)
    bx.set_xlabel("ITD / ms (positive: sound leads at the left ear)")
    bx.set_ylabel("Detector rate (normalised)")
    bx.set_xlim(-0.7, 0.7)
    bx.set_ylim(0, 1.15)
    bx.set_title(title, loc="left", fontsize=10)
axs[1].text(0, 1.07, "best delays -0.6 ... +0.6 ms", fontsize=8, color=P.muted(), ha="center")
fig.tight_layout()
