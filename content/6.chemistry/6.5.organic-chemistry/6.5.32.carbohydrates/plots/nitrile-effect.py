"""The nitrile effect in glycosylation, on a model pyranosyl donor with a non-participating
2-O-methyl group. Acetonitrile adds to the oxocarbenium ion mainly from the axial (alpha) face,
giving an alpha-nitrilium ion (cis to the C2 substituent in this drawing). The acceptor then
displaces acetonitrile from the opposite face in an SN2-like step, so the product is the
equatorial (beta, here 1,2-trans) glycoside."""

from wikichem import Scheme

s = Scheme()
y = 0.0
ox = s.molecule("CO[C@@H]1CCCO[CH+]1", at=(0.0, y))
mecn = s.molecule("CC#N", at=(2.4, y + 1.6), lone_pairs=[2])
s.curly(mecn.atom(2), ox.atom(7), bend=0.4)
s.text((0.0, y - 2.2), "oxocarbenium ion")
s.arrow((3.4, y), (4.8, y), above="MeCN", below="alpha face")
n = s.molecule("CC#[N+][C@H]1OCCC[C@H]1OC", at=(7.4, y))
me = s.molecule("CO", at=(9.6, y - 1.8), lone_pairs=[1])
s.curly(me.atom(1), n.atom(3), bend=-0.4)
s.curly(n.bond(2, 3), n.atom(2), bend=0.6)
s.text((7.4, y - 2.6), "alpha-nitrilium ion")
s.arrow((10.6, y), (12.0, y), above=r"$-$MeCN", below=r"$-$H$^+$")
s.molecule("CO[C@@H]1OCCC[C@H]1OC", at=(14.4, y))
s.text((14.4, y - 2.2), "beta (1,2-trans) glycoside")
s.draw()
