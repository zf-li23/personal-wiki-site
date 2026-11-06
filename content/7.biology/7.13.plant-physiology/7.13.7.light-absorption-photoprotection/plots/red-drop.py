"""Red drop and Emerson enhancement in a two-photosystem model, and the effect of state transitions.

Each linear electron needs one photon absorbed by PSII and one by PSI, so under limiting light the O2
quantum yield is proportional to 2 min(f1, f2), where f1 and f2 = 1 - f1 are the fractions of absorbed
photons delivered to PSI and PSII. Model: f1 = 0.42 at short wavelengths (state 1: PSII favoured) rising
to about 1 beyond 700 nm, where only PSI absorbs (logistic step at 692 nm). State 2 moves part of LHCII to
PSI (f1 + 0.08 where PSII still absorbs). A: f1 and f2; B: relative quantum yield; C: O2 evolution under a
fixed 700 nm beam (photon flux 1) when a 650 nm beam of increasing flux is added, compared with the sum of
the two beams given separately. Illustrative parameters.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
lam = np.linspace(600, 730, 521)
step = 1 / (1 + np.exp(-(lam - 692) / 5.0))


def f1(l, shift=0.0):
    s = 1 / (1 + np.exp(-(np.asarray(l) - 692) / 5.0))
    base = 0.42 + shift
    return base + (1 - base) * s


fig, axs = plt.subplots(1, 3, figsize=(13, 4.0))
a, b, c = axs
a.plot(lam, f1(lam), color=P.edge("plant"), lw=2, label="PSI, state 1")
a.plot(lam, 1 - f1(lam), color=P.edge("enzyme"), lw=2, label="PSII, state 1")
a.plot(lam, f1(lam, 0.08), color=P.edge("plant"), lw=1.4, ls="--", label="PSI, state 2")
a.plot(lam, 1 - f1(lam, 0.08), color=P.edge("enzyme"), lw=1.4, ls="--", label="PSII, state 2")
a.axhline(0.5, color=P.muted(), lw=0.8, ls=":")
a.set_ylim(0, 1.05)
a.set_xlabel("Wavelength $\\lambda$ / nm")
a.set_ylabel("Fraction of absorbed photons")
a.legend(frameon=False, fontsize=8, loc="upper left")
a.set_title("A  Excitation partition", loc="left", fontsize=10)

for shift, ls, name in ((0.0, "-", "state 1"), (0.08, "--", "state 2")):
    q = 2 * np.minimum(f1(lam, shift), 1 - f1(lam, shift))
    b.plot(lam, q, color=P.edge("rna"), lw=2 if shift == 0 else 1.5, ls=ls, label=name)
b.set_ylim(0, 1.05)
b.set_xlabel("Wavelength $\\lambda$ / nm")
b.set_ylabel("Relative quantum yield of O$_2$")
b.annotate("red drop", (700, 0.55), xytext=(660, 0.3), fontsize=9, color=P.ink(),
           arrowprops=dict(arrowstyle="->", color=P.muted()))
b.legend(frameon=False, fontsize=8, loc="lower left")
b.set_title("B  Red drop", loc="left", fontsize=10)

I1 = 1.0
I2 = np.linspace(0, 1.5, 151)
p1, p2 = f1(700), f1(650)


def rate(i1, i2):
    return np.minimum(i1 * p1 + i2 * p2, i1 * (1 - p1) + i2 * (1 - p2))


both = rate(I1, I2)
sep = rate(I1, 0) + rate(0, I2)
c.plot(I2, both, color=P.edge("rna"), lw=2, label="700 nm + 650 nm together")
c.plot(I2, sep, color=P.edge("dna"), lw=1.6, ls="--", label="sum of beams given separately")
c.fill_between(I2, sep, both, where=both > sep, color=P.mix(P.fill("highlight"), P.surface(), 0.4), lw=0)
c.text(0.62, 0.28, "enhancement", fontsize=9, color=P.ink())
c.set_xlabel("Photon flux of the 650 nm beam (700 nm beam = 1)")
c.set_ylabel("O$_2$ evolution (relative)")
c.legend(frameon=False, fontsize=8, loc="upper left")
c.set_title("C  Emerson enhancement", loc="left", fontsize=10)
for ax in axs:
    ax.grid(True, alpha=0.3)
fig.tight_layout()
