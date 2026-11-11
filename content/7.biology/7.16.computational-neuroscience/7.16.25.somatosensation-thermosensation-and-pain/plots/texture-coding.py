"""Duplex coding of texture by tactile afferents (schematic model).

A: spatial code. A row of raised dots (height profile) is scanned across a fingertip. SA1 afferents
with Gaussian receptive fields (s.d. 0.5 mm, spaced 1 mm) respond to the local indentation
(rectified linear response). Dots 3 mm apart produce an isomorphic image in the population;
dots 0.6 mm apart are blurred into a nearly uniform response.
B: temporal code. A fine grating of spatial period lambda scanned at speed v vibrates the skin at
frequency v / lambda. The Pacinian (PC) afferent response is modelled as the gain of a band-pass
filter (second-order high-pass with corner 120 Hz times first-order low-pass with corner 400 Hz),
plotted against spatial period for scanning speeds of 40 and 80 mm/s: the response depends on
v / lambda, so the same surface drives the PC channel at a frequency that scales with speed.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
x = np.linspace(-8, 8, 2000)  # mm
dx = x[1] - x[0]


def surface(spacing, width=0.25):
    centres = np.arange(-6, 6.01, spacing)
    return sum(np.exp(-((x - c) ** 2) / (2 * width**2)) for c in centres)


fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.2))
ax = axs[0]
rf_pos = np.arange(-7, 7.01, 0.5)
for k, (sp, c) in enumerate(((3.0, P.edge("dna")), (0.6, P.edge("rna")))):
    h = surface(sp)
    resp = [np.clip((h * np.exp(-((x - p) ** 2) / (2 * 0.5**2))).sum() * dx, 0, None) for p in rf_pos]
    resp = np.array(resp) / max(resp)
    off = -1.6 * k
    ax.fill_between(x, off + 0.9, off + 0.9 + 0.35 * h / h.max(), color=P.fill("neutral"), lw=0)
    ax.bar(rf_pos, 0.8 * resp, width=0.35, bottom=off, color=P.fill("dna") if k == 0 else P.fill("rna"),
           edgecolor=c, lw=0.6)
    ax.text(7.4, off + 0.6, f"dots {sp} mm apart", fontsize=8, color=c, va="center")
ax.set_xlim(-7.5, 11)
ax.set_yticks([])
ax.set_xlabel("Position on the skin / mm (bars: SA1 afferents)")
ax.set_title("A  Spatial code: SA1 population", loc="left", fontsize=10)
for s in ("left", "top", "right"):
    ax.spines[s].set_visible(False)

ax = axs[1]
lam = np.logspace(-2, 0, 300)  # mm


def pc_gain(f):
    hp = (f / 120) ** 2 / (1 + (f / 120) ** 2)
    lp = 1 / np.sqrt(1 + (f / 400) ** 2)
    return hp * lp


for v, c in ((40, P.edge("dna")), (80, P.edge("rna"))):
    g = pc_gain(v / lam)
    ax.semilogx(lam * 1e3, g / pc_gain(np.array([250.0]))[0], color=c, lw=2, label=f"scan at {v} mm/s")
ax.set_xlabel("Spatial period of the grating / um")
ax.set_ylabel("PC response (relative)")
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax.set_title("B  Temporal code: Pacinian afferents", loc="left", fontsize=10)
fig.tight_layout()
