"""Corey-Chaykovsky epoxidation of cyclohexanone with dimethylsulfonium methylide. The ylide carbon
adds to the carbonyl carbon; the alkoxide then attacks the CH2 group from the back in an
intramolecular SN2 reaction and displaces dimethyl sulfide, a good leaving group, giving the spiro
epoxide. (A phosphorus ylide would instead let oxygen bond to phosphorus: Wittig reaction.)"""

from wikichem import Scheme

s = Scheme()
yl = s.molecule("[CH2-][S+](C)C", at=(-2.4, 1.2), lone_pairs=[0])
ket = s.molecule("O=C1CCCCC1", at=(0.4, 0), lone_pairs=[0])
s.curly(yl.atom(0), ket.atom(1), bend=-0.4)
s.curly(ket.bond(0, 1), ket.atom(0), bend=-0.9)
s.arrow((2.0, 0), (3.4, 0))
bet = s.molecule("[O-]C1(C[S+](C)C)CCCCC1", at=(5.4, 0), lone_pairs=[0])
s.curly(bet.atom(0), bet.atom(2), bend=0.6)
s.curly(bet.bond(2, 3), bet.atom(3), bend=-0.6)
s.arrow((7.6, 0), (9.0, 0))
s.molecule("C1CCC2(CC1)CO2", at=(10.6, 0))
s.plus((12.8, 0))
s.molecule("CSC", at=(14.0, 0))
s.draw()
