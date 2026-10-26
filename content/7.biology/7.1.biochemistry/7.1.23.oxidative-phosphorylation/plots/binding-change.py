"""Binding-change mechanism and rotational catalysis of ATP synthase.
(A) F1 viewed from the membrane: three alpha (gray) and three beta subunits around gamma (green); in each
120-degree step of gamma the beta-ADP (loose) site closes into beta-ATP (tight), the beta-ATP site opens into
beta-empty and releases ATP, and the empty site binds ADP + Pi. (B) Simulated single-molecule rotation of F1
hydrolyzing ATP at low concentration (as in the actin-filament experiments of Yasuda, Kinosita and Yoshida):
gamma turns in 120-degree steps separated by exponentially distributed dwells whose mean, 1/(k_on [ATP]),
shortens as [ATP] rises; k_on = 3e7 M^-1 s^-1 (seed 0)."""

import numpy as np

import wikibio as bio
from wikibio import bioenergetics as be
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(20.0, 8.6)

bio.panel(ax, "A", (0.1, 8.5))
seq = [("ATP", "empty", "ADP"), ("empty", "ADP", "ATP"), ("ADP", "ATP", "empty")]
for k, states in enumerate(seq):
    c = (1.9 + 3.6 * k, 4.4)
    be.f1_top(ax, c, 1.1, states=states)
    if k < 2:
        bio.arrow(ax, (c[0] + 1.35, c[1] + 0.95), (c[0] + 2.25, c[1] + 0.95), kind="process", color=P.ink(), head=0.18)
        bio.label(ax, (c[0] + 1.8, c[1] + 1.25), "120°", size="tiny")
bio.label(ax, (5.5, 1.75), "loose (ADP + Pᵢ) → tight (ATP) → open (empty): 3 ATP per turn", size="tiny")
bio.label(ax, (5.5, 1.25), "γ (green) holds the β subunit it faces in the open conformation", size="tiny", color=P.muted())

bio.panel(ax, "B", (11.0, 8.5))
a = charts.axes_at(ax, (12.6, 1.3, 7.0, 6.4))
rng = np.random.default_rng(0)
kon = 3e7
for conc, tok in ((0.06e-6, "enzyme"), (0.2e-6, "receptor"), (0.6e-6, "channel")):
    rate = kon * conc
    t, ang, T, A = 0.0, 0.0, [0.0], [0.0]
    while t < 2.0:
        t += rng.exponential(1 / rate)
        T += [t, t]
        A += [ang, ang + 1 / 3]
        ang += 1 / 3
    a.plot(T, A, color=charts.line(tok), lw=1.5, label=f"[ATP] = {conc * 1e6:g} µM")
a.set_xlim(0, 2)
a.set_ylim(0, 14)
a.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(a, "t / s", "revolutions of γ")
charts.title(a, "Discrete 120° steps")
