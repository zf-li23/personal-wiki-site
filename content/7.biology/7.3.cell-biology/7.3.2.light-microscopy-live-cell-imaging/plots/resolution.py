# Diffraction and the resolution of a light microscope.
# A: the lateral image of a point source (the Airy pattern, I(v) = [2 J1(v)/v]^2 with v = 2 pi NA r / lambda)
#    for two point sources separated by 1.0, 0.75 and 0.5 times the Rayleigh distance d = 0.61 lambda / NA
#    (lambda = 520 nm, NA = 1.4); at d the summed profile still dips to about 73% between the peaks.
# B: lateral (0.61 lambda / NA) and axial (about 2 n lambda / NA^2, n = 1.515 for oil) resolution against NA
#    for green emission; markers for typical dry (0.75, 0.95), water-immersion (1.2) and oil (1.4) objectives.
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import j1

import wikibio as bio
from wikibio import charts

P = bio.P
lam, NA = 520.0, 1.4
d = 0.61 * lam / NA


def airy(r):
    v = 2 * np.pi * NA * np.asarray(r, float) / lam
    v = np.where(np.abs(v) < 1e-9, 1e-9, v)
    return (2 * j1(v) / v) ** 2


fig, axs = plt.subplots(1, 2, figsize=(11.0, 3.8), gridspec_kw={"width_ratios": [1.4, 1]})
ax = axs[0]
x = np.linspace(-700, 700, 1401)
for k, (f, tok) in enumerate(((1.0, "positive"), (0.75, "highlight"), (0.5, "negative"))):
    s = f * d
    I = airy(x - s / 2) + airy(x + s / 2)
    off = 1.2 * (2 - k)
    ax.plot(x, I / I.max() * 1.0 + off, color=charts.line(tok), lw=1.8)
    ax.plot(x, airy(x - s / 2) + off, color=P.muted(), lw=0.7, ls=":")
    ax.plot(x, airy(x + s / 2) + off, color=P.muted(), lw=0.7, ls=":")
    ax.text(720, off + 0.5, f"separation {f:g} d\n({s:.0f} nm)", fontsize=7.5, color=P.ink(), va="center")
ax.set_xlim(-700, 1150)
ax.set_yticks([])
charts.style_axes(ax, "position in the image plane / nm")
ax.spines["left"].set_visible(False)
ax.set_title(f"A   Two point sources (λ = {lam:.0f} nm, NA = {NA}); d = 0.61λ/NA = {d:.0f} nm", loc="left",
             fontsize=9, color=P.ink())

ax = axs[1]
na = np.linspace(0.2, 1.45, 200)
ax.plot(na, 0.61 * lam / na, color=charts.line("dna"), lw=1.8, label="lateral 0.61λ/NA")
ax.plot(na, 2 * 1.515 * lam / na**2, color=charts.line("rna"), lw=1.8, label="axial ≈ 2nλ/NA²")
for v, txt in ((0.75, "dry 20×"), (0.95, "dry 40×"), (1.2, "water 60×"), (1.4, "oil 100×")):
    ax.axvline(v, color=P.muted(), lw=0.6, ls=":")
    ax.text(v - 0.02, 7000, txt, fontsize=7, color=P.muted(), rotation=90, ha="right", va="top")
ax.set_yscale("log")
ax.set_xlim(0.2, 1.45)
ax.set_ylim(150, 8000)
ax.set_yticks([200, 500, 1000, 2000, 5000])
ax.set_yticklabels(["200", "500", "1000", "2000", "5000"])
ax.minorticks_off()
ax.legend(fontsize=7, frameon=False, loc="lower left")
charts.style_axes(ax, "numerical aperture NA = n sin θ", "resolution / nm")
ax.set_title("B   Resolution and aperture", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
