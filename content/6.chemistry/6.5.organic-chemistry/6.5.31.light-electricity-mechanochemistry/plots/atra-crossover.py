"""Organic steps of the photoredox atom-transfer radical addition of diethyl bromomalonate to
pent-4-en-1-ol (E = CO2Et). Top: one-electron reduction by *Ru(II) breaks the C-Br bond
(dissociative electron transfer) and the malonyl radical adds to the terminal carbon of the
alkene (fishhook arrows), giving a secondary alkyl radical. Bottom: Ru(III) oxidizes this radical
to a carbocation (radical-polar crossover), which is captured either by bromide (the addition
product) or, intramolecularly, by the hydroxyl group (5-exo cyclization to a tetrahydrofuran)."""

import numpy as np
from wikichem import Scheme


def shift(p, d):
    return np.asarray(p.xy if hasattr(p, "xy") else p, float) + np.asarray(d, float)


s = Scheme()
y = 0.0
s.molecule("*C(Br)*", at=(0.0, y), labels={0: "E", 3: "E"})
s.arrow((1.4, y), (3.2, y), above=r"$^*$Ru$^{2+}$ (+e$^-$)", below=r"$-$Br$^-$")
r = s.molecule("*[CH]*", at=(4.6, y + 1.2), labels={0: "E", 2: "E"})
al = s.molecule("C=CCCCO", at=(7.6, y - 0.6), flip=True)
m = (r.xy(1) + al.xy(0)) / 2
s.curly(r.atom(1), m, bend=0.5, single=True)
s.curly(shift(al.bond(0, 1), (0.0, 0.15)), m, bend=-0.6, single=True)
s.curly(shift(al.bond(0, 1), (0.0, -0.15)), shift(al.atom(1), (0.0, -0.35)), bend=0.6, single=True)
s.text((6.6, y - 2.4), "malonyl radical + pent-4-en-1-ol")
s.arrow((10.6, y), (12.0, y))
s.molecule("*C(*)C[CH]CCCO", at=(15.4, y), labels={0: "E", 2: "E"}, flip=True)
s.text((15.4, y - 2.4), "secondary alkyl radical")
y2 = -6.0
s.arrow((0.0, y2), (1.8, y2), above=r"Ru$^{3+}$", below=r"$-$e$^-$")
s.molecule("*C(*)C[CH+]CCCO", at=(5.2, y2), labels={0: "E", 2: "E"}, flip=True)
s.text((5.2, y2 - 2.4), "carbocation")
s.arrow((8.8, y2 + 0.6), (10.4, y2 + 1.6), above=r"Br$^-$")
s.molecule("*C(*)CC(Br)CCCO", at=(14.0, y2 + 2.0), labels={0: "E", 2: "E"}, flip=True)
s.text((14.0, y2 + 0.0), "ATRA product")
s.arrow((8.8, y2 - 0.6), (10.4, y2 - 1.6), below=r"5-exo, $-$H$^+$")
s.molecule("*C(*)CC1CCCO1", at=(13.6, y2 - 2.6), labels={0: "E", 2: "E"}, flip=True)
s.text((13.6, y2 - 4.8), "tetrahydrofuran (about 10%)")
s.draw()
