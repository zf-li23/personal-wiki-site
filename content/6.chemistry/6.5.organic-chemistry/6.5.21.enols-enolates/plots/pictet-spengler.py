"""Pictet-Spengler cyclisation of dopamine with acetaldehyde. The iminium ion formed from the amine
and the aldehyde is attacked by the electron-rich catechol ring at the carbon ortho to the side chain
and para to a hydroxy group: the ring pi electrons form the new C-C bond and the C=N electrons move
onto nitrogen. The arenium ion (its positive charge delocalised onto the para oxygen) loses a proton
and rearomatises, giving salsolinol, a 1,2,3,4-tetrahydroisoquinoline."""

from wikichem import Scheme

s = Scheme()
prod = s.molecule("CC1NCCc2c1cc(O)c(O)c2", at=(13.0, 0))
s.text((13.0, -2.3), "salsolinol")
# atom order matches the product: CH3, C1, N, CH2, CH2, ring C (chain), ring C (attacked), ...
im = s.molecule("CC=[NH+]CCc1ccc(O)c(O)c1", at=(0, 0), like=prod)
s.curly(im.bond(6, 7), im.atom(1), bend=-0.6)
s.curly(im.bond(1, 2), im.atom(2), bend=-0.6)
s.text((0, -2.3), "iminium ion")
s.arrow((2.6, 0), (4.0, 0))
s.molecule("CC1[NH2+]CCC2C1C=C(O)C(=[OH+])C=2", at=(6.2, 0), like=prod)
s.text((6.2, -2.3), "arenium ion")
s.arrow((9.2, 0), (10.6, 0), above=r"$-$2 H$^+$")
s.draw()
