"""Three ways of making radicals by homolysis, drawn with one-electron (fishhook) arrows.
(1) Light splits Cl2 into two chlorine atoms. (2) AIBN loses N2 on heating and gives two
2-cyano-2-propyl radicals. (3) Dibenzoyl peroxide breaks at the weak O-O bond; each benzoyloxyl
radical can then lose CO2 (a beta-scission) to give a phenyl radical."""

from wikichem import Scheme


# (1) Cl-Cl homolysis.
s = Scheme()
cl2 = s.molecule("ClCl", at=(0, 0))
s.curly(cl2.bond(0, 1), cl2.atom(0), bend=-1.1, single=True)
s.curly(cl2.bond(0, 1), cl2.atom(1), bend=1.1, single=True)
s.arrow((1.3, 0), (2.9, 0), above=r"$h\nu$ or heat")
for x in (3.7, 5.6):
    s.molecule("[Cl]", at=(x, 0))
s.plus((4.65, 0))
s.text((0, -1.1), r"$\Delta H = +243$ kJ mol$^{-1}$", size=10)
s.draw()

# (2) AIBN -> 2 (CH3)2C(.)CN + N2.
s = Scheme()
aibn = s.molecule("CC(C)(C#N)/N=N/C(C)(C)C#N", at=(0, 0))
s.curly(aibn.bond(1, 5), aibn.atom(1), bend=-0.9, single=True)
s.curly(aibn.bond(1, 5), aibn.bond(5, 6), bend=0.9, single=True)
s.curly(aibn.bond(6, 7), aibn.bond(5, 6), bend=-0.9, single=True)
s.curly(aibn.bond(6, 7), aibn.atom(7), bend=0.9, single=True)
s.text((0, -1.8), "AIBN", size=11)
s.arrow((3.3, 0), (4.9, 0), above="60-80 °C")
s.text((5.5, 0), "2", size=14)
s.molecule("C[C](C)C#N", at=(7.1, 0.2))
s.plus((8.6, 0))
s.molecule("N#N", at=(9.8, 0))
s.draw()

# (3) Dibenzoyl peroxide: O-O homolysis, then loss of CO2 from the benzoyloxyl radical.
s = Scheme()
bpo = s.molecule("O=C(OOC(=O)c1ccccc1)c1ccccc1", at=(0, 0), rotate=0)
s.curly(bpo.bond(2, 3), bpo.atom(2), bend=0.9, single=True)
s.curly(bpo.bond(2, 3), bpo.atom(3), bend=-0.9, single=True)
s.text((0, -2.6), "dibenzoyl peroxide (BPO)", size=11)
s.arrow((3.6, 0), (5.0, 0), above="80 °C")
bz = s.molecule("O=C([O])c1ccccc1", at=(7.0, 0))
s.curly(bz.atom(2), bz.bond(1, 2), bend=0.9, single=True)
s.curly(bz.bond(1, 3), bz.bond(1, 2), bend=0.8, single=True)
s.curly(bz.bond(1, 3), bz.atom(3), bend=-0.8, single=True)
s.text((7.0, -2.6), "benzoyloxyl", size=11)
s.text((5.6, 0), "2", size=14)
s.arrow((9.0, 0), (10.4, 0), above=r"$-$CO$_2$")
s.molecule("[c]1ccccc1", at=(11.9, 0))
s.text((11.9, -2.6), "phenyl", size=11)
s.draw()
