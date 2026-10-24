"""Inhibition of acetylcholinesterase by sarin and its reactivation by pralidoxime. Top: the
active-site serine (Enz-CH2-OH) attacks phosphorus while histidine (only its imidazole ring is
drawn) takes the O-H proton; fluoride leaves (substitution at phosphorus through a
five-coordinate transition state), so the serine is phosphonylated and the enzyme can no longer
hydrolyse acetylcholine. Bottom: the oximate of pralidoxime (2-PAM), an alpha-effect nucleophile,
attacks the same phosphorus and the serine oxygen leaves, regenerating the enzyme; this works
only before the phosphonyl-enzyme 'ages' by loss of the isopropyl group."""

import math

from wikichem import Scheme


def facing(smiles, k, angle):
    m = Scheme().molecule(smiles)
    v = m.xy(k) - m.coords.mean(axis=0)
    return angle - math.degrees(math.atan2(v[1], v[0]))


s = Scheme()
ser = s.molecule("*CO[H]", coords=[(-3.3, 0.6), (-2.3, 0.6), (-1.5, 0.0), (-1.5, -1.0)], lone_pairs=[2], labels={0: "Enz"})
IM = "*c1cnc[nH]1"
im = s.molecule(IM, at=(-3.0, -2.6), rotate=facing(IM, 3, 20), lone_pairs=[3], labels={0: "His"})
sar = s.molecule("*P(C)(=O)F", coords=[(0.9, 0.8), (0, 0), (0, -1.0), (0, 1.0), (1.1, -0.1)], at=(0.2, 0),
                 lone_pairs=[4], labels={0: "$i$PrO"})
s.curly(im.atom(3), ser.atom(3), bend=-0.4)
s.curly(ser.bond(2, 3), sar.atom(1), bend=0.5)
s.curly(sar.bond(1, 4), sar.atom(4), bend=-0.6)
s.arrow((2.4, 0), (3.8, 0))
x = 6.4
s.molecule("*COP(C)(=O)*", coords=[(-2.2, 0.6), (-1.2, 0.6), (-0.4, 0.0), (0.6, 0.0), (0.6, -1.0), (0.6, 1.0), (1.6, 0.0)],
           at=(x, 0), labels={0: "Enz", 6: "O$i$Pr"})
s.text((x, -1.5), "inactive enzyme", size=11)
s.plus((x + 2.9, 0))
s.molecule("[F-]", at=(x + 3.7, 0))
s.plus((x + 4.6, 0))
s.molecule("*c1c[nH+]c[nH]1", at=(x + 6.2, 0), labels={0: "His"})

y = -6.0
PAM = "C[n+]1ccccc1/C=N/[O-]"
pam = s.molecule(PAM, at=(-3.6, y), rotate=facing(PAM, 9, 0), lone_pairs=[9])
ph = s.molecule("*COP(C)(=O)*", coords=[(-2.2, 1.4), (-1.2, 1.4), (-0.6, 0.6), (0.4, 0.0), (0.4, -1.0), (0.4, 1.0), (1.4, 0.0)],
                at=(0.6, y), labels={0: "Enz", 6: "O$i$Pr"})
s.curly(pam.atom(9), ph.atom(3), bend=-0.4)
s.curly(ph.bond(2, 3), ph.atom(2), bend=0.6)
s.arrow((3.0, y), (4.4, y))
x = 8.6
s.molecule("C[n+]1ccccc1/C=N/OP(C)(=O)*", at=(x, y), labels={13: "O$i$Pr"})
s.plus((x + 3.4, y))
s.molecule("*C[O-]", coords=[(0, 0), (1.0, 0), (1.6, -0.8)], at=(x + 4.2, y), labels={0: "Enz"})
s.draw()
