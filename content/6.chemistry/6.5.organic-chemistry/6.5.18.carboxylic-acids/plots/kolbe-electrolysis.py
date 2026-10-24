"""Kolbe electrolysis of a carboxylate (propanoate). At the anode the carboxylate loses one electron
and gives an acyloxyl radical, which loses CO2 within nanoseconds: one fishhook from the radical
oxygen and one from the C-C bond form the second C=O, the other electron of the C-C bond stays on
the ethyl carbon. Two ethyl radicals formed close together on the electrode surface couple."""

from wikichem import Scheme

s = Scheme()
y = -2.0  # caption line
s.molecule("CCC(=O)[O-]", at=(0, 0), rotate=120)
s.text((0, y), "propanoate")
s.arrow((1.6, 0), (3.1, 0), above="anode", below=r"$-\mathrm{e}^-$")
rad = s.molecule("CCC(=O)[O]", at=(4.8, 0), rotate=120)
s.curly(rad.atom(4), rad.bond(2, 4), bend=-0.6, single=True)
s.curly(rad.bond(1, 2), rad.bond(2, 4), bend=0.6, single=True)
s.curly(rad.bond(1, 2), rad.atom(1), bend=-0.7, single=True)
s.text((4.8, y), "acyloxyl radical")
s.arrow((6.5, 0), (7.9, 0), below=r"$-\mathrm{CO_2}$")
s.molecule("C[CH2]", at=(9.0, 0))
s.text((9.0, y), "ethyl radical")
s.arrow((10.1, 0), (11.5, 0), above=r"$\times 2$")
s.molecule("CCCC", at=(13.2, 0))
s.text((13.2, y), "butane")
s.draw()
