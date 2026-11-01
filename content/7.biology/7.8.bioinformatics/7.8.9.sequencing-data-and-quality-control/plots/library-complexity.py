# Library complexity and duplicate reads. If a library contains C distinct molecules and n reads are drawn at random,
# the number of distinct molecules seen is C(1 - exp(-n/C)) (Formula 9.4.2), so the duplicate fraction grows with
# depth and falls with complexity. A: distinct reads against total reads for C = 1e8, 6.6e8 and 3e9 molecules; the
# point marks a run with 400 million reads of which 300 million are distinct, which implies C = 6.6e8.
# B: duplicate fraction 1 - distinct/n for the same libraries.
import numpy as np
from scipy import optimize
import wikibio as bio
from wikibio import charts as C

P = bio.P
fig, ax = bio.canvas(24.0, 9.0)
n = np.linspace(1e6, 2e9, 400)
n_obs, d_obs = 4e8, 3e8
C_obs = optimize.brentq(lambda c: c * (1 - np.exp(-n_obs / c)) - d_obs, d_obs, 1e12)
libs = [(1e8, "protein", "C = 1.0e8"), (C_obs, "dna", f"C = {C_obs / 1e8:.1f}e8"), (3e9, "positive", "C = 3.0e9")]
a = C.axes_at(ax, (1.8, 1.4, 9.0, 6.8))
b = C.axes_at(ax, (13.6, 1.4, 9.0, 6.8))
for c, tok, lab in libs:
    d = c * (1 - np.exp(-n / c))
    a.plot(n / 1e6, d / 1e6, color=C.line(tok), lw=1.8, label=lab)
    b.plot(n / 1e6, 100 * (1 - d / n), color=C.line(tok), lw=1.8, label=lab)
a.plot(n / 1e6, n / 1e6, color=P.muted(), lw=0.9, ls=(0, (3, 2)), label="no duplicates")
a.plot([n_obs / 1e6], [d_obs / 1e6], "o", color=C.line("negative"), ms=6)
a.text(n_obs / 1e6 + 60, d_obs / 1e6 - 80, "400 M reads,\n300 M distinct", fontsize=bio.core.FONT["tiny"], color=P.ink())
b.plot([n_obs / 1e6], [25], "o", color=C.line("negative"), ms=6)
a.set_xlim(0, 2000)
a.set_ylim(0, 2000)
b.set_xlim(0, 2000)
b.set_ylim(0, 100)
C.style_axes(a, "reads sequenced (millions)", "distinct molecules observed (millions)")
C.style_axes(b, "reads sequenced (millions)", "duplicate reads (%)")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.1, 8.9))
bio.panel(ax, "B", (11.9, 8.9))
