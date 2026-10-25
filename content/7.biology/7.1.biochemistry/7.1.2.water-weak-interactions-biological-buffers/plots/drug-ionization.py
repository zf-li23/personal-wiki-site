# pH and drug absorption: fraction of a drug in its uncharged (membrane-permeant) form as a function of pH,
# from the Henderson-Hasselbalch equation. Weak acid: aspirin (carboxyl pKa 3.5), uncharged = HA.
# Weak base: lidocaine (tertiary amine pKa 7.9), uncharged = B. Shaded: stomach and small-intestine pH;
# dashed line: blood plasma. Points: aspirin at pH 2.0 (97 % uncharged) and pH 5.0 (3 %).
import numpy as np
import wikibio as bio
from wikibio import charts as C

pH = np.linspace(0, 12, 500)
acid = 1 / (1 + 10 ** (pH - 3.5))
base = 1 / (1 + 10 ** (7.9 - pH))

fig, ax = bio.canvas(14, 8.0)
a = C.axes_at(ax, (1.9, 1.5, 11.4, 6.0))
band = bio.P.mix(bio.P.surface(), bio.P.muted(), 0.22)
F = bio.core.FONT["tiny"]
for lo, hi, text in [(1.5, 3.5, "stomach"), (6.0, 7.5, "small intestine")]:
    a.axvspan(lo, hi, color=band, lw=0)
    a.text((lo + hi) / 2, 104, text, ha="center", fontsize=F, color=bio.P.ink())
a.axvline(7.4, color=bio.P.muted(), lw=0.8, ls=(0, (3, 3)))
a.text(7.55, 50, "plasma", fontsize=F, color=bio.P.muted(), rotation=90, va="center")
a.plot(pH, 100 * acid, color=C.line("drug"), lw=2.2)
a.plot(pH, 100 * base, color=C.line("dna"), lw=2.2)
for x in (2.0, 5.0):
    y = 100 / (1 + 10 ** (x - 3.5))
    a.plot([x], [y], "o", ms=5, mfc=bio.P.fill("drug"), mec=C.line("drug"))
    a.annotate(f"{y:.0f} %", (x, y), (x + 0.3, y + (6 if y < 50 else -10)), fontsize=F, color=bio.P.ink())
a.text(4.1, 58, "aspirin (weak acid, pK$_a$ 3.5):\nuncharged HA", fontsize=F, color=C.line("drug"))
a.text(9.0, 78, "lidocaine (weak base, pK$_a$ 7.9):\nuncharged B", fontsize=F, color=C.line("dna"))
a.set_xlim(0, 12)
a.set_ylim(0, 110)
a.set_yticks([0, 25, 50, 75, 100])
C.style_axes(a, "pH", "uncharged form / %")
