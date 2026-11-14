"""Habitat, frequency and the range of a call (illustrative parameters).

Level L(r) = L0 - 20 log10(r) - alpha(f) r with L0 = 90 dB at 1 m.
Forest excess attenuation alpha = 0.004 + 0.006 f^1.5 dB/m (f in kHz); grassland alpha = 0.0015 + 0.0012 f^2.
Noise spectrum level falls with frequency (wind, distant sources); urban noise adds a low-frequency hump.
Detection when L(r) exceeds noise + 10 dB (critical ratio margin).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
L0 = 90.0


def alpha_forest(f):
    return 0.004 + 0.006 * f ** 1.5 + 0.02 * np.exp(-f / 0.6)   # last term: ground effect at low f


def alpha_open(f):
    return 0.0015 + 0.0012 * f ** 2


def noise(f, urban=False):
    n = 32 - 8 * np.log2(f / 0.5)
    n = np.maximum(n, 8)
    if urban:
        n = n + 30 * np.exp(-((np.log2(f) - np.log2(0.6)) / 1.4) ** 2)
    return n


def level(r, f, alpha):
    return L0 - 20 * np.log10(r) - alpha(f) * r


def det_dist(f, alpha, urban=False):
    r = np.logspace(0, 4, 4000)
    ok = level(r, f, alpha) > noise(f, urban) + 10
    return r[ok][-1] if ok.any() else 1.0


fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 3.9))
r = np.logspace(0, 3, 300)
for f, tok in ((2, "dna"), (4, "positive"), (8, "rna")):
    a.semilogx(r, level(r, f, alpha_forest), color=P.edge(tok), lw=1.8, label=f"{f} kHz")
    a.hlines(noise(f) + 10, 1, 1000, color=P.edge(tok), ls=":", lw=0.9)
a.semilogx(r, L0 - 20 * np.log10(r), color=P.muted(), lw=1, ls="--", label="spreading only")
a.set_xlabel("Distance / m")
a.set_ylabel("Received level / dB")
a.set_ylim(0, 95)
a.legend(frameon=False, fontsize=8, loc="lower left")
a.text(1.3, 33, "dotted: noise + detection margin", fontsize=7.5, color=P.muted())
a.set_title("A  forest", loc="left", fontweight="bold")

fs = np.linspace(0.3, 12, 200)
b.plot(fs, [det_dist(f, alpha_forest) for f in fs], color=P.edge("positive"), lw=1.8, label="forest")
b.plot(fs, [det_dist(f, alpha_open) for f in fs], color=P.edge("rna"), lw=1.8, label="grassland")
b.plot(fs, [det_dist(f, alpha_open, urban=True) for f in fs], color=P.edge("negative"), lw=1.6, ls="--",
       label="grassland + urban noise")
b.set_xlabel("Frequency / kHz")
b.set_ylabel("Detection distance / m")
b.set_xlim(0, 12); b.set_ylim(0, None)
b.legend(frameon=False, fontsize=8)
b.set_title("B", loc="left", fontweight="bold")
for ax in (a, b):
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
fig.tight_layout()
