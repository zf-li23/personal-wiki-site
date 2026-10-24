"""Dehalogenation of 1,2-dibromoethane with zinc. Zinc inserts into one C-Br bond (by electron
transfer from the metal surface), giving a 2-bromoethylzinc bromide; the electrons of the polar
C-Zn bond then form the pi bond while bromide leaves from the neighbouring carbon, giving ethene
and ZnBr2."""

from wikichem import Scheme

s = Scheme()
s.molecule("BrCCBr", at=(0, 0))
s.plus((1.6, 0))
s.text((2.3, 0), "Zn")
s.arrow((3.0, 0), (4.4, 0), above="insertion")
org = s.molecule("BrCC[Zn]Br", at=(6.6, 0), lone_pairs=[0])
s.curly(org.bond(2, 3), org.bond(1, 2), bend=-0.8)
s.curly(org.bond(0, 1), org.atom(0), bend=-0.8)
s.arrow((8.8, 0), (10.2, 0))
s.molecule("C=C", at=(11.2, 0))
s.plus((12.3, 0))
s.text((13.3, 0), r"ZnBr$_2$")
s.draw()
