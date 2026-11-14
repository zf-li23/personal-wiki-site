"""Why sharing blood is cheap for the donor and valuable for the recipient (after Wilkinson 1984).

An illustrative curve of body mass after a blood meal, as a percentage of the fed mass, m(t) = 70 + 30 exp(-t / 33.5)
(t in hours): mass falls fast at first, as the meal is digested and water excreted, then more slowly, and the bat
dies of starvation at 75%, about 60 h after feeding. A donor that fed two hours ago (D) gives 5% of its fed mass to
a hungry roost-mate (R) at 77%: the donor moves to D', losing C of its remaining hours before starvation, and the
recipient to R', gaining B hours. Because the curve decelerates, B is several times C.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
tau, lo, death = 33.5, 70.0, 75.0
m = lambda t: lo + 30 * np.exp(-t / tau)  # noqa: E731
tinv = lambda x: -tau * np.log((x - lo) / 30)  # noqa: E731
td = tinv(death)

fig, ax = bio.canvas(18.0, 10.0)
pa = Ch.axes_at(ax, (2.6, 1.8, 14.5, 7.4))
t = np.linspace(0, td, 300)
pa.plot(td - t, m(t), color=Ch.line("blood"), lw=1.8)
pa.axhline(death, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pa.text(58, death - 1.3, "death from starvation", fontsize=FS["tiny"], color=P.muted(), va="top")
tD, tR = 2.0, tinv(77.0)
for t0, name, tok in ((tD, "D", "dna"), (tR, "R", "rna")):
    m0 = m(t0)
    t1 = tinv(m0 - 5) if name == "D" else tinv(m0 + 5)
    pa.plot([td - t0], [m0], "o", ms=6, color=Ch.line(tok))
    pa.plot([td - t1], [m(t1)], "o", ms=6, color=Ch.line(tok), mfc=P.surface())
    pa.annotate("", (td - t1, m(t1)), (td - t0, m0), arrowprops=dict(arrowstyle="->", color=Ch.line(tok), lw=1.2))
    pa.text(td - t0 + (0.8 if name == "D" else -0.8), m0 + 0.8, name, fontsize=FS["small"], color=Ch.line(tok),
            ha="left" if name == "D" else "right")
    pa.text(td - t1 + (0.8 if name == "D" else -0.8), m(t1) + (-1.8 if name == "D" else 0.8), name + "′",
            fontsize=FS["small"], color=Ch.line(tok), ha="left" if name == "D" else "right")
    hrs = abs(t1 - t0)
    lab = f"C ≈ {hrs:.0f} h lost" if name == "D" else f"B ≈ {hrs:.0f} h gained"
    pa.text(td - (t0 + t1) / 2, 103 if name == "D" else 90, lab, fontsize=FS["tiny"], color=Ch.line(tok), ha="center")
pa.set_xlim(62, -1)
pa.set_ylim(70, 106)
Ch.style_axes(pa, "hours remaining before death from starvation", "mass, % of fed mass")
