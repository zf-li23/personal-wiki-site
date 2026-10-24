"""Reduction of a nitrile to a primary amine with LiAlH4. Top: hydride from AlH4- adds to the
nitrile carbon and the C=N pi electrons move onto nitrogen, giving an imine anion bound to aluminium.
Bottom: a second hydride adds to the C=N carbon of this imine salt, giving a dianionic aluminium
amide, which aqueous work-up protonates to pentan-1-amine; the carbon chain gains a CH2 relative to
the alkyl halide the nitrile was made from."""

from wikichem import Scheme

s = Scheme()
y = 0.0
n = s.molecule("CCCCC#N", at=(0, y), lone_pairs=[5])
c = n.xy(4)
al = s.molecule("[H]*", coords=[(c[0] - 0.2, c[1] + 1.5), (c[0] - 0.2, c[1] + 2.5)], labels={1: r"AlH$_3^-$"})
s.curly(al.bond(0, 1), n.atom(4), bend=0.5)
s.curly(n.bond(4, 5), n.atom(5), bend=-0.6)
s.arrow((3.2, y), (4.6, y))
im = s.molecule("CCCCC=N*", at=(7.4, y), labels={6: r"AlH$_3^-$"})
s.text((7.4, y - 1.6), "imine salt")

y = -4.0
im2 = s.molecule("CCCCC=N*", at=(0, y), labels={6: r"AlH$_3^-$"}, lone_pairs=[5])
c2 = im2.xy(4)
al2 = s.molecule("[H]*", coords=[(c2[0] - 0.3, c2[1] - 1.5), (c2[0] - 0.3, c2[1] - 2.5)], labels={1: r"AlH$_3^-$"})
s.curly(al2.bond(0, 1), im2.atom(4), bend=-0.5)
s.curly(im2.bond(4, 5), im2.atom(5), bend=0.6)
s.arrow((3.2, y), (4.6, y), above=r"then H$_2$O")
s.molecule("CCCCCN", at=(7.0, y))
s.text((7.0, y - 1.4), "pentan-1-amine")
s.draw()
