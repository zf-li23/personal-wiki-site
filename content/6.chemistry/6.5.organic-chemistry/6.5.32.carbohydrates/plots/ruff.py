"""Ruff degradation, drawn on the top carbons of an aldonic acid (R = the rest of the chain).
Fe(III) (or Fe(II)/H2O2) takes one electron from the carboxylate, giving an acyloxyl radical,
which loses CO2 (fishhook arrows: one electron of the C1-C2 bond pairs with the oxygen radical,
the other stays on C2). The alpha-hydroxyalkyl radical is oxidized by a second electron transfer
and loses a proton, so C2 becomes the aldehyde of the aldose with one carbon fewer."""

import numpy as np
from wikichem import Scheme


def shift(p, d):
    return np.asarray(p.xy if hasattr(p, "xy") else p, float) + np.asarray(d, float)


s = Scheme()
y = 0.0
s.molecule("*[C@@H](O)[C@H](O)C(=O)[O-]", at=(0.0, y), labels={0: "R"})
s.text((0.0, y - 2.4), "aldonate")
s.arrow((2.2, y), (3.6, y), above=r"Fe$^{3+}$", below=r"$-$e$^-$")
r = s.molecule("*[C@@H](O)[C@H](O)C(=O)[O]", at=(5.8, y), labels={0: "R"})
m = (r.xy(5) + r.xy(7)) / 2
s.curly(r.atom(7), m, bend=0.5, single=True)
s.curly(shift(r.bond(3, 5), (0.1, 0.12)), m, bend=-0.5, single=True)
s.curly(shift(r.bond(3, 5), (-0.1, -0.12)), shift(r.atom(3), (0.1, -0.35)), bend=0.6, single=True)
s.text((5.8, y - 2.4), "acyloxyl radical")
s.arrow((8.0, y), (9.4, y), above=r"$-$CO$_2$")
s.molecule("*[C@@H](O)[CH]O", at=(11.2, y), labels={0: "R"})
s.text((11.2, y - 2.4), "alpha-hydroxyalkyl radical")
s.arrow((13.0, y), (14.4, y), above=r"$-$e$^-$", below=r"$-$H$^+$")
s.molecule("*[C@@H](O)C=O", at=(16.0, y), labels={0: "R"})
s.text((16.0, y - 2.4), "aldose $-$ 1 C")
s.draw()
