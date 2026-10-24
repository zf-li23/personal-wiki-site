"""Gold(I)-catalysed glycosylation with a glycosyl ortho-alkynylbenzoate (Yu), on a
tetrahydropyranyl model of the donor. Top: Ph3PAu+ coordinates the alkyne (the gold-activated pi
bond is drawn with Au on the proximal carbon) and the ester carbonyl oxygen attacks the distal
alkyne carbon (6-endo-dig), giving an isochromenylium (cyclic oxocarbenium) ion with a vinyl-gold
group. Bottom: the ring oxygen of the sugar expels this neutral isochromen-1-one, releasing the
glycosyl oxocarbenium ion that the acceptor captures; protodeauration of the vinyl-gold species
regenerates the catalyst."""

from wikichem import Scheme

s = Scheme()
y = 0.0
d = s.molecule("*C#Cc1ccccc1C(=O)OC1CCCCO1", at=(0.0, y), labels={0: "Bu"}, lone_pairs=[10])
au = (d.xy(2) + d.xy(1)) / 2
s.text((au[0] + 0.1, au[1] + 1.0), r"[Au]$^+$", size=11)
s.curly(d.atom(10), d.atom(1), bend=0.5)
s.curly(d.bond(1, 2), (au[0] + 0.1, au[1] + 0.7), bend=0.6)
s.text((0.0, y - 3.6), "glycosyl o-alkynylbenzoate")
s.arrow((3.2, y), (4.6, y), above=r"Ph$_3$PAu$^+$", below="6-endo-dig")
i = s.molecule("*C1=C(*)c2ccccc2C(OC2CCCCO2)=[O+]1", at=(7.8, y), labels={0: "Bu", 3: "[Au]"}, lone_pairs=[17])
s.curly(i.atom(17), i.bond(12, 17), bend=0.6)
s.curly(i.bond(11, 12), i.bond(10, 11), bend=0.6)
s.curly(i.bond(10, 18), i.atom(18), bend=-0.6)
s.text((7.8, y - 3.8), "isochromenylium ion")
s.arrow((10.8, y), (12.2, y))
s.molecule("C1CC[O+]=CC1", at=(13.4, y + 1.2))
s.plus((13.4, y - 0.2))
s.molecule("*C1=C(*)c2ccccc2C(=O)O1", at=(14.6, y - 1.8), labels={0: "Bu", 3: "[Au]"})
s.draw()
