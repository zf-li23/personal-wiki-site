"""Electrophilic fluorination of ethyl 2-oxocyclohexane-1-carboxylate with Selectfluor (drawn as
its dication; the BF4- counterions are omitted). The enol of the beta-keto ester is the
nucleophile: the O-H lone pair pushes the C=C electrons onto fluorine and the weak N-F bond
breaks toward the cationic nitrogen (an SN2-type fluorine transfer; for some substrates a
single-electron pathway competes). Loss of the proton from the carbonyl oxygen gives the
alpha-fluoro keto ester."""

import math

from wikichem import Scheme


def facing(smiles, k, angle):
    m = Scheme().molecule(smiles)
    v = m.xy(k) - m.coords.mean(axis=0)
    return angle - math.degrees(math.atan2(v[1], v[0]))


SF = "F[N+]12CC[N+](CCl)(CC1)CC2"
s = Scheme()
en = s.molecule("CCOC(=O)C1=C(O)CCCC1", at=(0, 0), rotate=0, lone_pairs=[7])
sf = s.molecule(SF, at=(-0.6, -3.8), rotate=facing(SF, 0, 90), lone_pairs=[])
s.curly(en.atom(7), en.bond(6, 7), bend=-0.6)
s.curly(en.bond(5, 6), sf.atom(0), bend=-0.5)
s.curly(sf.bond(0, 1), sf.atom(1), bend=0.6)
s.arrow((3.4, 0), (4.8, 0), above="$-$H$^+$")
s.molecule("CCOC(=O)C1(F)CCCCC1=O", at=(7.2, 0))
s.draw()
