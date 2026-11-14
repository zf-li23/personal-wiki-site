"""A sensitive period from two processes: maturation of competence and self-termination by experience.

Competence c(t) rises logistically after hatching (half-maximum at 10 h). Plasticity is c(t)(1 - S(t)), where S is
the fraction of the plastic capacity already committed by visual experience: dS/dt = k e c (1 - S), with
exposure e = 1 in normal light and e = 0.05 in dark rearing. The strength of imprinting on a test object shown for
one hour at age a is proportional to the plasticity at a. Illustrative parameters.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
t = np.linspace(0, 72, 1441)
dt = t[1] - t[0]
c = 1 / (1 + np.exp(-(t - 10.0) / 2.5))
k = 0.12


def plasticity(e):
    S = np.zeros_like(t)
    for i in range(1, len(t)):
        S[i] = S[i - 1] + k * e * c[i - 1] * (1 - S[i - 1]) * dt
    return c * (1 - S), S


pl_n, S_n = plasticity(1.0)
pl_d, S_d = plasticity(0.05)
fig, ax = bio.canvas(28.0, 10.0)
pa = C.axes_at(ax, (2.4, 1.6, 10.6, 7.2))
pa.plot(t, c, color=C.line("neutral"), lw=1.5, ls=(0, (4, 2)))
pa.plot(t, 1 - S_n, color=C.line("dna"), lw=1.5, ls=(0, (1, 1.5)))
pa.plot(t, pl_n, color=C.line("negative"), lw=2.0)
pa.text(40, 1.02, "competence c(t): maturation", color=C.line("neutral"), fontsize=FS["tiny"], va="bottom")
pa.text(30, 0.1, "uncommitted capacity 1 − S(t)", color=C.line("dna"), fontsize=FS["tiny"])
pa.text(17, 0.72, "plasticity", color=C.line("negative"), fontsize=FS["tiny"], ha="left")
pa.set_xlim(0, 72)
pa.set_ylim(0, 1.12)
C.style_axes(pa, "age after hatching / h", "relative value")
bio.panel(ax, "A", (0.4, 9.7))
pb = C.axes_at(ax, (16.6, 1.6, 10.6, 7.2))
pb.plot(t, pl_n / pl_n.max(), color=C.line("negative"), lw=2.0)
pb.plot(t, pl_d / pl_n.max(), color=C.line("protein"), lw=2.0)
i = np.argmax(pl_n)
pb.text(t[i] + 1, 1.02, f"peak {t[i]:.0f} h", color=C.line("negative"), fontsize=FS["tiny"], va="bottom")
pb.text(70, pl_n[-1] / pl_n.max() + 0.04, "reared in light", color=C.line("negative"), fontsize=FS["tiny"], ha="right")
pb.text(70, min(pl_d[-1] / pl_n.max(), 2.1) + 0.04, "reared in dark", color=C.line("protein"), fontsize=FS["tiny"], ha="right")
pb.set_xlim(0, 72)
pb.set_ylim(0, 2.3)
C.style_axes(pb, "age at first exposure to the test object / h", "strength of imprinting (relative)")
bio.panel(ax, "B", (14.6, 9.7))
