# The contrast transfer function (CTF) of a 300 kV microscope (lambda = 0.0197 A, Cs = 2.7 mm),
# in the convention chi(k) = pi lambda df k^2 - (pi/2) Cs lambda^3 k^4 with underfocus df > 0 and
# CTF(k) = -[sqrt(1 - A^2) sin chi + A cos chi], amplitude contrast A = 0.07.
# A: CTF at df = 1.0 um multiplied by the envelopes: spatial coherence (illumination semi-angle
#    alpha = 0.02 mrad), temporal coherence (focal spread delta = 4 nm) and a B-factor of 50 A^2 for
#    specimen motion, damage and detector; the grey band is the total envelope.
# B: undamped CTF at three defoci at low spatial frequency: larger defocus raises the contrast of
#    the lowest frequencies but makes the oscillations faster; the first zero moves to lower k.
# C: the lowest frequencies: conventional imaging (amplitude contrast only, near zero), the CTF at
#    df = 0.5 um, and an ideal phase plate (extra phase shift pi/2) at df = 0.5 um, which transfers
#    the lowest frequencies at full strength.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
lam, Cs, A = 0.019687, 2.7e7, 0.07          # A, A
alpha, delta, B = 0.02e-3, 40.0, 50.0       # rad, A, A^2


def chi(k, df, phase=0.0):
    return np.pi * lam * df * k**2 - 0.5 * np.pi * Cs * lam**3 * k**4 + phase


def ctf(k, df, phase=0.0):
    c = chi(k, df, phase)
    return -(np.sqrt(1 - A**2) * np.sin(c) + A * np.cos(c))


def envelope(k, df):
    es = np.exp(-(np.pi * alpha) ** 2 * (Cs * lam**2 * k**3 - df * k) ** 2)
    et = np.exp(-0.5 * (np.pi * lam * delta) ** 2 * k**4)
    eb = np.exp(-B * k**2 / 4)
    return es * et * eb


fig, axs = plt.subplots(1, 3, figsize=(14, 4.0), gridspec_kw={"width_ratios": [1.5, 1.2, 1.0]})
ax = axs[0]
k = np.linspace(0, 0.5, 3000)
df = 1.0e4
E = envelope(k, df)
ax.fill_between(k, -E, E, color=P.light("neutral"), lw=0)
ax.plot(k, ctf(k, df) * E, color=charts.line("protein"), lw=1.0)
ax.axhline(0, color=P.muted(), lw=0.6)
for d in (10, 5, 3, 2.5):
    ax.axvline(1 / d, color=P.muted(), lw=0.5, ls=":")
    ax.text(1 / d, 1.03, f"{d} Å", ha="center", fontsize=7, color=P.muted())
ax.set_xlim(0, 0.5)
ax.set_ylim(-1.05, 1.1)
charts.style_axes(ax, "spatial frequency k / Å⁻¹", "CTF × envelope")
charts.title(ax, "A   Δf = 1.0 µm, with envelopes")

ax = axs[1]
k = np.linspace(0, 0.1, 2000)
for dfu, tok in ((0.5, "dna"), (1.5, "positive"), (3.0, "negative")):
    ax.plot(k, ctf(k, dfu * 1e4), color=charts.line(tok), lw=1.3, label=f"Δf = {dfu} µm")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_xlim(0, 0.1)
ax.set_ylim(-1.1, 1.1)
ax.legend(fontsize=7, loc="lower right", framealpha=0.9, facecolor=P.surface(), edgecolor=P.muted())
charts.style_axes(ax, "k / Å⁻¹", "CTF")
charts.title(ax, "B   Effect of defocus")

ax = axs[2]
k = np.linspace(0, 0.06, 600)
ax.plot(k, ctf(k, 0.0), color=charts.line("neutral"), lw=1.4, label="in focus (−A)")
ax.plot(k, ctf(k, 0.5e4), color=charts.line("dna"), lw=1.4, label="Δf = 0.5 µm")
ax.plot(k, ctf(k, 0.5e4, np.pi / 2), color=charts.line("highlight"), lw=1.6, label="phase plate, Δf = 0.5 µm")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_xlim(0, 0.06)
ax.set_ylim(-1.1, 1.1)
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "k / Å⁻¹", "CTF")
charts.title(ax, "C   Lowest frequencies")
fig.tight_layout()
