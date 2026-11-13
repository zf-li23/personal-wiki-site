# Model: estimating body mass from limb bones. Campione and Evans (2012) fitted, for 200 living quadrupedal
# mammals and reptiles, log10(M) = 2.749 log10(C) - 1.104, where M is body mass in g and C the sum of the
# least circumferences of the humerus and femur in mm. (A) The fitted relation (solid) compared with geometric
# similarity, M proportional to C^3 (dashed, through the same point at 1 t); typical masses of a dog, a
# horse and an elephant are marked, and the range of large sauropods (20-70 t). (B) Because C grows as
# M^0.364, faster than the M^0.333 of geometric similarity but slower than M^0.5, the axial stress in the
# limb bones (proportional to M / C^2) still rises as M^0.27: a 50 t sauropod loads its bones about 7 times
# more per unit area than a 30 kg dog, unless posture and bone shape compensate.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(23, 8.5)
M = np.logspace(3, 8, 200)                         # g, 1 kg to 100 t


def circ(m):
    return 10 ** ((np.log10(m) + 1.104) / 2.749)


C = circ(M)
p = quant.Plot(ax, (1.8, 1.4, 8.4, 6.0), xlim=(30, 3000), ylim=(1e3, 1e8), xlog=True, ylog=True,
               xlabel="humerus + femur circumference / mm", ylabel="body mass / g",
               xticks=[30, 100, 300, 1000, 3000], yticks=[(1e3, "1 kg"), (1e4, "10 kg"), (1e5, "100 kg"),
                                                         (1e6, "1 t"), (1e7, "10 t"), (1e8, "100 t")])
p.line(C, M, "dna")
p.text(40, 3e6, "log M = 2.749 log C - 1.104", token="dna", ha="left")
p.text(40, 1.2e6, "(Campione & Evans 2012)", token="dna", ha="left")
c1 = circ(1e6)
Cg = np.logspace(np.log10(30), np.log10(3000), 100)
Mg = 1e6 * (Cg / c1) ** 3
keep = (Mg > 1e3) & (Mg < 1e8)
p.line(Cg[keep], Mg[keep], "muted", dashed=True, text="geometric similarity, M ~ C^3", at=0.3, dy=-0.9)
for m, name in ((3e4, "dog"), (5e5, "horse"), (6e6, "elephant")):
    p.points([circ(m)], [m], "dna")
    p.text(circ(m) * 1.15, m / 2.2, name, ha="left")
p.span(circ(2e7), circ(7e7), "highlight", text="large sauropods")
bio.panel(ax, "A", (0.4, 8.1))

q = quant.Plot(ax, (13.6, 1.4, 8.4, 6.0), xlim=(1e3, 1e8), ylim=(0.5, 30), xlog=True, ylog=True,
               xlabel="body mass", ylabel="relative bone stress (dog = 1)",
               xticks=[(1e3, "1 kg"), (1e5, "100 kg"), (1e7, "10 t")], yticks=[1, 3, 10, 30])
s = (M / C ** 2) / (3e4 / circ(3e4) ** 2)
q.line(M, s, "mrna", text="stress ~ M^0.27", at=0.55, dy=0.3)
q.hline(1, text="dog", size="tiny")
bio.panel(ax, "B", (12.2, 8.1))
