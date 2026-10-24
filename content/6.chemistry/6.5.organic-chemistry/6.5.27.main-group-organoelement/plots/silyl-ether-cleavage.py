"""Fluoride removes a tert-butyldimethylsilyl (TBS) ether. Fluoride attacks silicon, which can take
a fifth ligand (a pentacoordinate siliconate, trigonal bipyramidal); the Si-O bond then breaks and
the alkoxide leaves. The strong Si-F bond (about 565 kJ/mol, against about 452 for Si-O) makes
the cleavage essentially irreversible; water or acid in the work-up protonates the alkoxide."""

from wikichem import Scheme

s = Scheme()
tbs = s.molecule("CC(C)(C)[Si](C)(C)OCc1ccccc1",
                 coords=[(-2.0, 0.87), (-1.5, 0), (-2.0, -0.87), (-2.5, 0.2), (-0.5, 0), (-0.5, 1.0), (-0.5, -1.0),
                         (0.5, 0), (1.0, 0.87), (2.0, 0.87), (2.5, 1.73), (3.5, 1.73), (4.0, 0.87), (3.5, 0), (2.5, 0)],
                 lone_pairs=[])
f = s.molecule("[F-]", at=(-0.9, 2.4), lone_pairs=True)
s.curly(f.atom(0), tbs.atom(4), bend=0.4)
s.curly(tbs.bond(4, 7), tbs.atom(7), bend=0.6)
s.arrow((4.8, 0.5), (6.2, 0.5), above="TBAF")
s.molecule("CC(C)(C)[Si](C)(C)F", at=(8.0, 0.5))
s.plus((9.8, 0.5))
s.molecule("[O-]Cc1ccccc1", at=(11.6, 0.5), lone_pairs=[0])
s.draw()
