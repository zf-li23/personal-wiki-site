"""Electron-donating and electron-withdrawing conjugation. (a) In methoxyethene the oxygen lone pair
is delocalized into the C=C pi bond (+M): the terminal carbon becomes electron rich. (b) In
propenal the C=C pi electrons are delocalized toward the carbonyl oxygen (-M): the terminal carbon
becomes electron poor. The right-hand structures are minor, charge-separated contributors that show
where the charge goes."""

from wikichem import Scheme

s = Scheme(scale=0.46)

y = 0.0
s.text((-2.4, y), "(a)")
a = s.molecule("C=COC", at=(0.0, y), lone_pairs=[2])
s.curly(a.atom(2), a.bond(1, 2), bend=-0.9)
s.curly(a.bond(0, 1), a.atom(0), bend=-0.9)
s.arrow((1.9, y), (3.1, y), kind="resonance")
s.molecule("[CH2-]C=[O+]C", at=(5.0, y), lone_pairs=[0, 2])
s.text((7.6, y), "+M")

y = -3.0
s.text((-2.4, y), "(b)")
b = s.molecule("C=CC=O", at=(0.0, y), lone_pairs=[3])
s.curly(b.bond(0, 1), b.bond(1, 2), bend=0.9)
s.curly(b.bond(2, 3), b.atom(3), bend=0.9)
s.arrow((1.9, y), (3.1, y), kind="resonance")
s.molecule("[CH2+]C=C[O-]", at=(5.0, y), lone_pairs=[3])
s.text((7.6, y), "$-$M")
s.draw()
