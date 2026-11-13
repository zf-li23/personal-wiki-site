# Cranial nerves of a shark and their relation to the pharyngeal arches, schematic lateral view (anterior left).
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax = bio.canvas(24, 10.4)
head = vs.smooth([(0.4, 5.0), (1.5, 7.4), (6.0, 8.4), (14.0, 8.6), (22.5, 8.2), (23.5, 5.0), (22.5, 2.0), (14.0, 1.6),
                  (6.0, 2.0), (2.0, 3.0)])
bio.shape(ax, head, token="animal", zorder=1)
# brain
brain = vs.smooth([(3.6, 6.6), (5.0, 7.3), (8.0, 7.2), (11.0, 7.0), (14.5, 6.9), (14.5, 6.3), (11.0, 6.1), (8.0, 6.2),
                   (5.0, 6.0)])
bio.shape(ax, brain, token="neuron", zorder=4)
ax.plot([14.5, 23.0], [6.6, 6.5], color=P.edge("neuron"), lw=4, zorder=4)
bio.shape(ax, vs.oval((2.3, 6.3), 0.7, 0.45), token="receptor", zorder=4, lw=0.8)       # olfactory sac
bio.shape(ax, vs.oval((5.6, 5.2), 0.75, 0.75), token="nucleus", zorder=4, lw=0.8)       # eye
bio.shape(ax, vs.oval((10.8, 6.0), 0.8, 0.45), token="extracellular", zorder=4, lw=0.8)  # inner ear
# gill slits (spiracle + 5)
slits = [8.6, 12.4, 13.6, 14.8, 16.0, 17.2]
for i, x in enumerate(slits):
    h = 0.5 if i == 0 else 1.5
    ax.plot([x, x], [3.6 - (0 if i else -1.2), 3.6 + h - (0 if i else -1.2)], color=P.ink(), lw=2.2, zorder=5,
            solid_capstyle="round")


def nerve(pts, col, lw=2.0, z=6):
    p = np.asarray(pts, float)
    ax.plot(p[:, 0], p[:, 1], color=col, lw=lw, zorder=z, solid_capstyle="round", solid_joinstyle="round")


N = P.edge("neuron")
nerve([(3.6, 6.6), (2.6, 6.4)], N)                                         # I
nerve([(6.5, 6.3), (5.9, 5.6)], N)                                         # II
nerve([(7.2, 6.2), (6.4, 5.0)], P.edge("muscle"), lw=1.4)                  # III, IV, VI
V = vs.edge("meckel")
nerve([(8.8, 6.3), (6.5, 6.8), (2.0, 7.0)], V)                             # V1 ophthalmic
nerve([(8.8, 6.3), (6.0, 4.4), (2.8, 4.0)], V)                             # V2 maxillary
nerve([(8.8, 6.3), (7.6, 3.4), (5.0, 2.6)], V)                             # V3 mandibular
VII = vs.edge("hyomandibula")
nerve([(9.6, 6.2), (8.3, 4.6)], VII)                                       # pretrematic (spiracle)
nerve([(9.6, 6.2), (9.6, 3.0), (9.0, 2.3)], VII)                           # posttrematic, hyoid
nerve([(10.4, 6.1), (10.8, 6.0)], P.edge("extracellular"))                 # VIII
IX = vs.edge("arch_3")
nerve([(11.4, 6.1), (12.2, 5.3), (12.1, 3.6)], IX)
nerve([(11.4, 6.1), (12.7, 5.3), (12.8, 3.4)], IX, lw=1.4)
X = vs.edge("arch_4")
for x in slits[2:]:
    nerve([(12.6, 6.2), (x - 0.25, 5.4), (x - 0.2, 3.6)], X, lw=1.6)
    nerve([(12.6, 6.2), (x + 0.3, 5.3), (x + 0.35, 3.4)], X, lw=1.1)
nerve([(12.6, 6.2), (17.8, 5.2), (21.5, 3.4)], X, lw=2.2)                  # visceral branch
LL = P.edge("dna")
nerve([(9.9, 6.6), (6.5, 7.6), (1.8, 6.6)], LL, lw=1.3)                    # anterior lateral line nerve
nerve([(12.0, 6.9), (17.0, 7.3), (23.0, 7.2)], LL, lw=1.3)                 # posterior lateral line nerve
lab = [((2.9, 6.45), (1.6, 9.2), "I olfactory"), ((6.1, 5.85), (4.4, 9.2), "II optic"),
       ((6.8, 5.6), (6.5, 0.7), "III, IV, VI eye muscles"), ((4.0, 6.9), (2.4, 9.8), "V ophthalmic"),
       ((3.6, 4.1), (1.0, 3.2), "V maxillary"), ((6.0, 2.9), (3.6, 0.9), "V mandibular (arch 1)"),
       ((9.4, 3.2), (9.6, 0.7), "VII (hyoid arch)"), ((10.8, 6.0), (11.4, 9.5), "VIII inner ear"),
       ((12.15, 4.3), (12.4, 0.2), "IX (arch 3)"), ((15.0, 4.6), (15.6, 0.7), "X (arches 4-7)"),
       ((20.0, 4.1), (20.5, 0.9), "X visceral branch"), ((5.0, 7.4), (4.8, 9.8), "anterior lateral line nerve"),
       ((19.0, 7.25), (18.5, 9.4), "posterior lateral line nerve"), ((8.6, 5.0), (8.6, 9.0), "spiracle")]
for p, q, s in lab:
    bio.callout(ax, p, q, s, size="tiny")
