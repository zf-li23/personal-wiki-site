"""The rate-maximizing producer-scrounger game (after Vickery et al. 1991; Giraldeau and Caraco 2000).

A group of G foragers: G - S producers each find a patch of F items at rate lambda; the finder eats a items
(the finder's share) before the S scroungers arrive, and the remaining F - a items are divided equally among the
finder and the scroungers. Intake rates: W_P = lambda [a + (F - a)/(S + 1)], W_S = lambda (G - S)(F - a)/(S + 1).
They are equal at S* = G (1 - a/F) - 1. A, B: G = 6, F = 10, lambda = 1, with a small (a = 2) and a large
(a = 5) finder's share. C: the equilibrium proportion of scroungers 1 - a/F - 1/G.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
G, F = 6, 10.0


def rates(S, a):
    return a + (F - a) / (S + 1), (G - S) * (F - a) / (S + 1)


fig, ax = bio.canvas(33.0, 10.0)
for k, (a, title) in enumerate(((2.0, "small finder's share (a = 2)"), (5.0, "large finder's share (a = 5)"))):
    x0 = 2.4 + 11.2 * k
    p = Ch.axes_at(ax, (x0, 1.7, 8.0, 7.0))
    S = np.linspace(0, G - 0.0, 200)
    wp, ws = rates(S, a)
    p.plot(S, wp, color=Ch.line("dna"), lw=1.7)
    p.plot(S[S >= 1], ws[S >= 1], color=Ch.line("rna"), lw=1.7)
    Si = np.arange(0, G)
    wpi, wsi = rates(Si, a)
    p.plot(Si, wpi, "o", color=Ch.line("dna"), ms=3.5)
    p.plot(Si[1:], wsi[1:], "o", color=Ch.line("rna"), ms=3.5)
    s_star = G * (1 - a / F) - 1
    p.axvline(s_star, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
    p.text(s_star + 0.08, 24, f"$S^*$ = {s_star:.1f}", fontsize=FS["tiny"], color=P.muted())
    p.text(0.15, rates(0.15, a)[0] + 1.4, "producer", fontsize=FS["tiny"], color=Ch.line("dna"))
    p.text(1.15, rates(1.15, a)[1] + 1.4, "scrounger", fontsize=FS["tiny"], color=Ch.line("rna"))
    p.set_xlim(0, G)
    p.set_ylim(0, 26)
    Ch.style_axes(p, "number of scroungers S (group of 6)", "intake rate / (items per unit time)")
    Ch.title(p, title)
    bio.panel(ax, "AB"[k], (x0 - 2.1, 9.8))

pc = Ch.axes_at(ax, (24.8, 1.7, 7.4, 7.0))
af = np.linspace(0, 1, 200)
for g, tok in ((3, "protein"), (6, "rna"), (20, "dna")):
    ph = np.clip(1 - af - 1 / g, 0, 1)
    pc.plot(af, ph, color=Ch.line(tok), lw=1.7)
    pc.text(0.03, 1 - 1 / g + 0.02, f"G = {g}", fontsize=FS["tiny"], color=Ch.line(tok), va="bottom")
pc.set_xlim(0, 1)
pc.set_ylim(0, 1)
Ch.style_axes(pc, "finder's share a / F", "equilibrium proportion of scroungers")
bio.panel(ax, "C", (22.7, 9.8))
