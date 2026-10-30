"""Eversion of the leg disc and the energy model of segment shape (Section 33.4).

A: the third-instar leg disc as concentric folds; Distal-less in the centre (tarsus, claw), dachshund in the middle
(femur, tibia), homothorax at the rim (coxa); B: the everted leg, the centre of the disc telescoped out to become
the distal tip. C: Percus's energy model for a segment of fixed area A: bending energy D/(2R^2) per unit area plus
boundary energies alpha / L (circumferential boundaries) and beta / R (longitudinal boundaries). The total energy
E(R) = D A / (2 R^2) + 2 pi alpha R + beta A / R has a minimum at the radius where alpha R^2 = L (D + beta R); curves of
the optimal length-to-radius ratio L / R against R for three values of beta / alpha (D = 2, alpha = 1).
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import limbdev as LD
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(28.0, 10.0)
bio.panel(ax, "A", (0.2, 9.8))
r = LD.leg_disc(ax, (3.6, 5.2), 3.0)
for name, xy in r.items():
    pass
for name, txt, xy in (("claw", "Dll: claw", (0.5, 9.2)), ("tarsus", "Dll: tarsus", (0.5, 8.4)), ("tibia", "dac: tibia", (6.8, 9.2)),
                      ("femur", "dac: femur", (6.8, 8.4)), ("trochanter", "trochanter", (6.8, 1.6)), ("coxa", "hth: coxa", (6.8, 0.8))):
    bio.callout(ax, r[name], xy, txt, size="tiny")

bio.panel(ax, "B", (9.0, 9.8))
seg = LD.telescoped_leg(ax, (11.2, 9.2), 8.4)
for name in ("coxa", "trochanter", "femur", "tibia", "tarsus", "claw"):
    bio.callout(ax, seg[name], (12.6, seg[name][1]), name, size="tiny")

bio.panel(ax, "C", (15.6, 9.8))
pa = C.axes_at(ax, (17.2, 1.6, 10.0, 7.2))
R = np.linspace(0.2, 6, 300)
D, al = 2.0, 1.0
for be, tk in ((0.0, "channel"), (0.5, "positive"), (2.0, "drug")):
    L = al * R**2 / (D + be * R)
    pa.plot(R, L / R, color=Q.line_color(tk), lw=1.7, label=f"β/α = {be:g}")
pa.set_xlim(0, 6)
pa.set_ylim(0, 3.2)
C.style_axes(pa, "segment radius R (scaled)", "optimal L / R")
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
