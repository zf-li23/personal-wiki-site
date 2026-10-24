"""Release of acetic acid from 2-nitrobenzyl acetate (a photocage). Top: the excited nitro group
abstracts a benzylic hydrogen (1,5-hydrogen atom transfer, as in photoenolization), giving the
aci-nitro tautomer, a quinonoid nitronic acid; the nitronate oxygen adds to the exocyclic carbon
while the ring regains its aromaticity, closing a 1,3-dihydro-2,1-benzisoxazol-1-ol. Bottom: this
ring opens to the nitroso hemiacylal, which collapses to 2-nitrosobenzaldehyde and the free acid."""

from wikichem import Scheme

s = Scheme()
y = 0.0
s.molecule("CC(=O)OCc1ccccc1[N+](=O)[O-]", at=(0.0, y))
s.text((0.0, y - 3.2), "2-nitrobenzyl acetate")
s.arrow((2.6, y), (4.2, y), above=r"$h\nu$", below="1,5-HAT")
a = s.molecule("CC(=O)OC=C1C=CC=CC1=[N+](O)[O-]", at=(7.0, y), lone_pairs=[13])
s.curly(a.atom(13), a.atom(4), bend=-0.6)
s.curly(a.bond(4, 5), a.bond(5, 10), bend=-0.6)
s.curly(a.bond(10, 11), a.atom(11), bend=0.6)
s.text((7.0, y - 3.2), "aci-nitro intermediate")
s.arrow((9.6, y), (11.0, y))
s.molecule("CC(=O)OC1ON(O)c2ccccc21", at=(13.6, y))
s.text((13.6, y - 3.2), "benzisoxazolol")
y2 = -6.6
s.arrow((-0.6, y2), (1.0, y2), above="ring opening")
s.molecule("CC(=O)OC(O)c1ccccc1N=O", at=(4.4, y2))
s.text((4.4, y2 - 3.2), "nitroso hemiacylal")
s.arrow((7.2, y2), (8.6, y2))
s.molecule("O=Cc1ccccc1N=O", at=(11.8, y2))
s.text((11.6, y2 - 3.2), "2-nitrosobenzaldehyde")
s.plus((14.0, y2))
s.molecule("CC(=O)O", at=(15.4, y2))
s.text((15.6, y2 - 3.2), "acetic acid")
s.draw()
