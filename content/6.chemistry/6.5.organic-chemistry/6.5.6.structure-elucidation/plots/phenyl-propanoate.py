"""Schematic spectra of the unknown C9H10O2 (phenyl propanoate). Left: EI mass spectrum (sticks,
approximate intensities): M+. 150 with M+1 about 10 % of M, base peak m/z 94 (phenol radical
cation, M - CH3CH=C=O) and m/z 57 (CH3CH2CO+). Right: simulated 1H NMR at 400 MHz: 7.38
(2 H, meta), 7.23 (1 H, para), 7.08 (2 H, ortho), 2.59 (2 H, q, J = 7.5 Hz), 1.26 (3 H, t)."""

import numpy as np
import matplotlib.pyplot as plt
from math import comb

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.6), gridspec_kw={"width_ratios": [1, 1.5]})

ms = {27: 9, 28: 6, 29: 30, 39: 10, 51: 4, 57: 45, 65: 9, 66: 7, 77: 4, 94: 100, 95: 7, 150: 20, 151: 2.0}
for mz, i in ms.items():
    ax1.plot([mz, mz], [0, i], color="C0", lw=1.6)
for mz in (29, 57, 94, 150):
    ax1.text(mz, ms[mz] + 3, str(mz), ha="center", fontsize=8)
ax1.set_xlim(20, 160)
ax1.set_ylim(0, 112)
ax1.set_xlabel("$m/z$")
ax1.set_ylabel("relative intensity / %")
ax1.set_title("EI mass spectrum", fontsize=10)

MHZ, w = 400.0, 0.8
x = np.linspace(0.5, 8.0, 60000)
y = np.zeros_like(x)


def add(d, n, mult=0, j=0.0):
    global y
    for k in range(mult + 1):
        c = d * MHZ + (k - mult / 2) * j
        y += n * comb(mult, k) / 2**mult * w / np.pi / ((x * MHZ - c) ** 2 + w**2)


add(7.38, 2, 2, 7.9)
add(7.23, 1, 2, 7.4)
add(7.08, 2, 1, 7.7)
add(2.59, 2, 3, 7.5)
add(1.26, 3, 2, 7.5)
ax2.plot(x, y / y.max(), color="C0", lw=1)
for d, t in [(2.59, "2 H, q"), (1.26, "3 H, t")]:
    ax2.text(d, 1.04, t, ha="center", fontsize=8)
ins = ax2.inset_axes([0.22, 0.3, 0.42, 0.6])
sel = (x > 6.95) & (x < 7.5)
ins.plot(x[sel], y[sel] / y.max(), color="C0", lw=1)
ins.set_xlim(7.5, 6.95)
ins.set_yticks([])
ins.tick_params(labelsize=7)
for d, t in [(7.38, "2 H (meta)"), (7.23, "1 H (para)"), (7.08, "2 H (ortho)")]:
    ins.text(d, 1.08, t, ha="center", fontsize=7)
ins.set_ylim(0, 1.3)
ax2.set_xlim(8.0, 0.5)
ax2.set_ylim(0, 1.18)
ax2.set_yticks([])
ax2.set_xlabel(r"$\delta$ / ppm")
ax2.set_title(r"$^1$H NMR (CDCl$_3$)", fontsize=10)
fig.tight_layout()
