"""Interrupted electrophilic substitution of furan (Br2 in methanol). The furan pi electrons attack
bromine at C2, pushed by the ring oxygen lone pair; the sigma complex is an oxocarbenium ion with the
positive charge stabilised by oxygen at C5. Because rearomatisation gains little (furan has a small
aromatic stabilisation), methanol captures C5 instead of a proton being lost: a 1,4-addition. A second
substitution of the allylic bromide by methanol gives 2,5-dimethoxy-2,5-dihydrofuran."""

from wikichem import Scheme

s = Scheme()
f = s.molecule("c1ccoc1", at=(0, 0), lone_pairs=[3])
br = s.molecule("BrBr", at=(f.xy(4)[0] + 1.5, f.xy(4)[1] + 0.9), lone_pairs=True)
s.curly(f.atom(3), f.bond(2, 3), bend=0.6)
s.curly(f.bond(1, 2), f.bond(0, 1), bend=0.6)
s.curly(f.bond(0, 4), br.atom(0), bend=-0.5)
s.curly(br.bond(0, 1), br.atom(1), bend=-0.6)
s.arrow((3.0, 0), (4.4, 0), below=r"$-$Br$^-$")
ox = s.molecule("C1=CC=[O+]C1Br", at=(5.8, 0))
me = s.molecule("CO", at=(ox.xy(2)[0] - 0.4, ox.xy(2)[1] - 2.0), lone_pairs=[1])
s.curly(me.atom(1), ox.atom(2), bend=0.4)
s.curly(ox.bond(2, 3), ox.atom(3), bend=0.6)
s.text((6.4, 1.6), "oxocarbenium ion")
s.arrow((7.6, 0), (9.0, 0), above=r"$-$H$^+$")
s.molecule("COC1C=CC(Br)O1", at=(10.8, 0))
s.arrow((12.9, 0), (14.3, 0), above="MeOH", below=r"$-$HBr")
s.molecule("COC1C=CC(OC)O1", at=(16.4, 0))
s.draw()
