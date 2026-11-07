"""Lateral inhibition sharpens two-point discrimination (schematic 1-D model).

Receptors every 0.25 mm; each afferent has a Gaussian receptive field of width sigma
(1 mm, fingertip-like; 8 mm, back-like). Two point stimuli separated by d excite the array;
the central layer sums afferents with the same Gaussian and subtracts a broader inhibitory
surround (difference of Gaussians: surround width 2 sigma, weight w = 0.9; output rectified).
A: activity profiles for d = 3.2 mm (sigma = 1 mm) without and with lateral inhibition.
B: depth of the dip between the two peaks (1 - trough/peak) against separation; the
separation at which the dip first exceeds 10 % is taken as the two-point threshold.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
x = np.arange(-60, 60, 0.05)


def profile(d, sigma, w):
    s = np.exp(-((x - d / 2) ** 2) / (2 * sigma**2)) + np.exp(-((x + d / 2) ** 2) / (2 * sigma**2))
    k = np.arange(-6 * sigma, 6 * sigma, 0.05)
    ex = np.exp(-k**2 / (2 * sigma**2))
    ex /= ex.sum()
    inh = np.exp(-k**2 / (2 * (2 * sigma) ** 2))
    inh /= inh.sum()
    r = np.convolve(s, ex - w * inh, mode="same")
    return np.clip(r, 0, None)


def dip(d, sigma, w):
    r = profile(d, sigma, w)
    peak = r.max()
    trough = r[np.argmin(np.abs(x))]
    return 1 - trough / peak if peak > 0 else 0


fig, (ax, bx) = plt.subplots(1, 2, figsize=(11, 4.0))
d = 3.2
for w, c, lab in ((0.0, P.edge("dna"), "no inhibition"), (0.9, P.edge("rna"), "with lateral inhibition")):
    r = profile(d, 1.0, w)
    ax.plot(x, r / r.max(), color=c, lw=2, label=lab)
for s in (-d / 2, d / 2):
    ax.axvline(s, color=P.muted(), lw=0.8, ls=":")
ax.set_xlim(-6, 6)
ax.set_ylim(0, 1.1)
ax.set_xlabel("Position on skin / mm")
ax.set_ylabel("Central activity (normalised)")
ax.legend(frameon=False, fontsize=8, loc="lower center")
ax.set_title("A  Two points 3.2 mm apart", loc="left", fontsize=10)

for sigma, ls in ((1.0, "-"), (8.0, "--")):
    ds = np.linspace(0.2, 12 * sigma, 120)
    for w, c in ((0.0, P.edge("dna")), (0.9, P.edge("rna"))):
        dd = np.array([dip(v, sigma, w) for v in ds])
        bx.plot(ds, dd, color=c, lw=1.8, ls=ls)
        i = np.argmax(dd > 0.1)
        bx.plot(ds[i], 0.1, "o", color=c, ms=4)
bx.axhline(0.1, color=P.muted(), lw=0.7, ls=":")
bx.set_xscale("log")
bx.set_xlabel("Separation / mm")
bx.set_ylabel("Dip depth between peaks")
bx.text(4.2, 0.45, r"$\sigma$ = 1 mm (fingertip)", fontsize=8, color=P.muted())
bx.text(34, 0.3, r"$\sigma$ = 8 mm (back)", fontsize=8, color=P.muted())
bx.plot([], [], color=P.edge("dna"), label="no inhibition")
bx.plot([], [], color=P.edge("rna"), label="with lateral inhibition")
bx.legend(frameon=False, fontsize=8, loc="upper left")
bx.set_title("B  Threshold scales with receptive field", loc="left", fontsize=10)
for a in (ax, bx):
    a.grid(True, alpha=0.3)
fig.tight_layout()
