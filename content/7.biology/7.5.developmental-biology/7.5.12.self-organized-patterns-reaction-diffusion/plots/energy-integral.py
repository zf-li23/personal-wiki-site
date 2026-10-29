"""The inhomogeneous steady state of the second Turing system in the limit of a non-diffusing activator.

With f(a, h) = a(h - 1)/16 - 3/4 = 0 the activator follows a = A(h) = 12 / (h - 1), and the inhibitor obeys
nu h'' + g(A(h), h) = 0 with g = 1 - 3h / (4(h - 1)). The energy integral nu h'^2 / 2 + V(h) = E holds with
V(h) = (h - 4)/4 - (3/4) ln((h - 1)/3), a potential with its minimum at the uniform state h = 4. A: V(h). B: the
phase plane (h, h'): closed curves are traversed by the steady pattern, x playing the role of time, and a pattern
on an interval with no-flux ends is a path between two turning points (h' = 0). C: the half-period chi(E), the
length of tissue needed for one traversal (nu = 1/4): it tends to pi sqrt(12 nu) as E -> 0 and increases with E,
so a tissue shorter than chi_min stays uniform and a long tissue can hold several half-cycles.
"""

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
nu = 0.25


def V(h):
    return (h - 4) / 4 - 0.75 * np.log((h - 1) / 3)


fig, ax = bio.canvas(30.0, 9.2)
h = np.linspace(1.6, 12, 500)
pa = C.axes_at(ax, (1.6, 1.4, 7.4, 6.4))
pa.plot(h, V(h), color=Q.line_color("protein"), lw=1.8)
Es = (0.05, 0.2, 0.5)
for E, tk in zip(Es, ("na", "highlight", "negative")):
    pa.axhline(E, color=Q.line_color(tk), lw=0.9, ls=(0, (3, 2)))
pa.set_xlim(1.6, 12)
pa.set_ylim(-0.05, 0.9)
C.style_axes(pa, "inhibitor h", "V(h)")
bio.panel(ax, "A", (0.3, 8.6))
bio.label(ax, (1.6, 8.6), "Potential of the energy integral", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (11.6, 1.4, 7.4, 6.4))
chi = []
for E, tk in zip(Es, ("na", "highlight", "negative")):
    lo = brentq(lambda x: V(x) - E, 1.0001, 4)
    hi = brentq(lambda x: V(x) - E, 4, 200)
    hh = np.linspace(lo, hi, 400)
    hp = np.sqrt(np.maximum(2 * (E - V(hh)) / nu, 0))
    pb.plot(hh, hp, color=Q.line_color(tk), lw=1.6, label=f"E = {E:g}")
    pb.plot(hh, -hp, color=Q.line_color(tk), lw=1.6)
pb.plot([4], [0], "o", color=P.ink(), ms=4)
pb.set_xlim(1.6, 12)
C.style_axes(pb, "h", "h′")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (10.3, 8.6))
bio.label(ax, (11.6, 8.6), "Phase plane: ν h′²/2 + V(h) = E", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (21.6, 1.4, 7.4, 6.4))
EE = np.logspace(-4, 0.2, 40)
for E in EE:
    lo = brentq(lambda x: V(x) - E, 1.0000001, 4)
    hi = brentq(lambda x: V(x) - E, 4, 1e4)
    # substitution h = mid + half sin(theta) removes the end singularities
    mid, half = (hi + lo) / 2, (hi - lo) / 2
    val = quad(lambda th: half * np.cos(th) / np.sqrt(max(E - V(mid + half * np.sin(th)), 1e-300)), -np.pi / 2, np.pi / 2, limit=200)[0]
    chi.append(np.sqrt(nu / 2) * val)
pc.semilogx(EE, chi, color=Q.line_color("protein"), lw=1.8)
pc.axhline(np.pi * np.sqrt(12 * nu), color=P.edge("highlight"), lw=0.9, ls=(0, (2, 2)))
pc.text(1.2e-4, np.pi * np.sqrt(12 * nu) + 0.4, "π √(12ν)", color=P.edge("highlight"), fontsize=FS["tiny"])
pc.set_ylim(0, max(chi) * 1.1)
C.style_axes(pc, "energy E (log scale)", "half-period χ(E)")
bio.panel(ax, "C", (20.3, 8.6))
bio.label(ax, (21.6, 8.6), "Length of one half-cycle", size="small", bold=True, ha="left")
