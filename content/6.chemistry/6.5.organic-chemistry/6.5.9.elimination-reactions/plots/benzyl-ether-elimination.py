"""Alpha',beta-elimination of benzyl ethyl ether with a very strong base (alkyllithium). The base first
removes a benzylic proton; the carbanion then takes a hydrogen from the ethyl CH3 group through a
five-membered cyclic transition state, while the C-H electrons form the C=C bond and the C-O bond
breaks, releasing ethene and the benzyl alkoxide (shown by labelling with PhCD2OEt)."""

from wikichem import Scheme

s = Scheme()
s.molecule("c1ccccc1COCC", at=(0, 0))
s.arrow((2.6, 0), (4.0, 0), above=r"RLi", below=r"$-$RH")
an = s.molecule("[CH-](*)OCC[H]", coords=[(0, 0), (-0.9, 0.5), (0.9, 0.7), (1.9, 0.35), (1.85, -0.65), (0.75, -1.25)],
                at=(5.6, 0), labels={1: "Ph"}, lone_pairs=[0])
s.curly(an.atom(0), an.atom(5), bend=0.5)
s.curly(an.bond(4, 5), an.bond(3, 4), bend=0.5)
s.curly(an.bond(2, 3), an.atom(2), bend=-0.6)
s.arrow((8.0, 0), (9.4, 0))
s.molecule("[O-]Cc1ccccc1", at=(11.0, 0))
s.plus((12.8, 0))
s.molecule("C=C", at=(13.7, 0))
s.draw()
