"""Strecker synthesis of alanine. Top: acetaldehyde and ammonia give an imine (protonated to the
iminium ion under the reaction conditions, NH4Cl/NaCN); cyanide adds to the iminium carbon,
giving the alpha-aminonitrile. Bottom: acid hydrolysis of the nitrile gives the racemic
amino acid. Cyanide attacks the planar iminium ion equally from both faces."""

from wikichem import Scheme

s = Scheme()
y = 0.0
s.molecule("CC=O", at=(-0.4, y))
s.plus((0.9, y))
s.molecule("N", at=(1.6, y))
s.arrow((2.3, y), (3.7, y), above=r"$-$H$_2$O", below=r"H$^+$", kind="equilibrium")
im = s.molecule("C[CH]=[NH2+]", at=(5.1, y))
cn = s.molecule("[C-]#N", at=(5.4, y - 2.0), lone_pairs=[0])
s.curly(cn.atom(0), im.atom(1), bend=-0.4)
s.curly(im.bond(1, 2), im.atom(2), bend=-0.8)
s.text((5.1, y + 1.2), "iminium ion")
s.arrow((6.6, y), (8.0, y))
s.molecule("CC(N)C#N", at=(9.5, y))
s.text((9.5, y - 1.6), r"$\alpha$-aminonitrile")
s.arrow((11.0, y), (12.6, y), above=r"H$_3$O$^+$", below="heat")
s.molecule("CC([NH3+])C(=O)[O-]", at=(14.2, y))
s.text((14.2, y - 1.6), "(R,S)-alanine")
s.draw()
