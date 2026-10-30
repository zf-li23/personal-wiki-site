"""The Shh-Gremlin1-FGF feedback loop and its self-termination (Section 32.3; a minimal model in the spirit of
Benazet et al. 2009, all quantities scaled).

A: the network (open arrows activation, bars inhibition): AER-FGF maintains Shh in the ZPA; Shh induces Grem1 in the
mesenchyme; Grem1 antagonizes BMP, which would repress the AER-FGFs; BMP also starts Grem1 early; high FGF represses
Grem1. Descendants of Shh-expressing cells cannot express Grem1, so as the limb grows a gap d = v t opens between
the source of Shh and the Grem1 domain, which weakens the Shh -> Grem1 link by exp(-d / ell).
B: time courses with v = 0.05 (Shh, Grem1, AER-FGF, BMP): the loop is switched on by BMP-induced Grem1, peaks and
then shuts itself down as the gap grows. C: the same with v = 0 (no gap): the loop stays on.
dS/dt = [F^2 / (0.25 + F^2) - S] / 2, dG/dt = [(0.35 B + 3 S exp(-v t / 0.8)) / (1 + (F / 1.5)^4) - G] / 3,
dB/dt = 1 - B - 2 G B, dF/dt = [0.15 + 1.2 / (1 + (B / 0.4)^4) - F] / 2.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q
from scipy.integrate import solve_ivp

P = bio.P
fig, ax = bio.canvas(30.0, 9.6)


def rhs(t, y, v):
    S, G, B, F = y
    dS = F**2 / (0.25 + F**2) - S
    dG = (0.35 * B + 3 * S * np.exp(-v * t / 0.8)) / (1 + (F / 1.5) ** 4) - G
    dB = 1.0 - B - 2.0 * G * B
    dF = 0.15 + 1.2 / (1 + (B / 0.4) ** 4) - F
    return [dS / 2, dG / 3, dB, dF / 2]


bio.panel(ax, "A", (0.2, 9.4))
N = {"fgf": (2.4, 7.2, "AER-FGF", "ectoderm"), "shh": (7.0, 7.2, "Shh (ZPA)", "protein"),
     "grem": (7.0, 3.4, "Grem1", "positive"), "bmp": (2.4, 3.4, "BMP", "highlight")}
for k, (x, y, t, tk) in N.items():
    bio.box(ax, (x, y), 2.9, 1.0, tk, t, size="small")
bio.arrow(ax, (3.9, 7.35), (5.5, 7.35), kind="activation", lw=1.1)
bio.arrow(ax, (7.0, 6.65), (7.0, 3.95), kind="activation", lw=1.1)
bio.label(ax, (7.25, 5.3), "weakens as\ngap d grows", size="tiny", color=P.muted(), ha="left")
bio.arrow(ax, (5.5, 3.4), (3.9, 3.4), kind="inhibition", lw=1.1)
bio.arrow(ax, (2.4, 3.95), (2.4, 6.65), kind="inhibition", lw=1.1)
bio.arrow(ax, (3.5, 2.85), (5.9, 2.85), kind="activation", lw=0.9, bend=0.35, dashed=True)
bio.label(ax, (4.7, 1.75), "early: BMP induces Grem1", size="tiny", color=P.muted())
bio.arrow(ax, (3.2, 6.65), (6.2, 3.95), kind="inhibition", lw=0.9, dashed=True)
bio.label(ax, (4.0, 5.7), "high FGF", size="tiny", color=P.muted())

t = np.linspace(0, 150, 600)
names = [("Shh", "protein"), ("Grem1", "positive"), ("BMP", "highlight"), ("AER-FGF", "ectoderm")]
for k, (v, title) in enumerate(((0.05, "Growth separates Shh and Grem1: the loop terminates"), (0.0, "No separation: the loop persists"))):
    sol = solve_ivp(rhs, (0, 150), [0.0, 0.0, 1.0, 0.15], args=(v,), t_eval=t, max_step=0.5)
    x0 = 12.0 + 9.2 * k
    pa = C.axes_at(ax, (x0, 1.4, 7.6, 6.8))
    for i, (nm, tk) in enumerate(names):
        pa.plot(t, sol.y[i], color=Q.line_color(tk), lw=1.6, label=nm)
    pa.set_xlim(0, 150)
    pa.set_ylim(0, 1.45 if k == 0 else 1.05 * sol.y.max())
    C.style_axes(pa, "time (scaled)", "level (scaled)" if k == 0 else None)
    if k == 0:
        pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right", ncol=2)
    bio.panel(ax, "BC"[k], (x0 - 1.2, 9.4))
    bio.label(ax, (x0, 9.1), title, size="small", bold=True, ha="left", va="top")
