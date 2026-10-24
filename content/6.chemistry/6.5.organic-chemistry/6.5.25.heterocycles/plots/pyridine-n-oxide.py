"""Pyridine N-oxide is activated at C4. Top: the oxygen lone pair forms an N=O bond and the ring pi
electrons are pushed on to C4 (resonance structure with negative charge at C4; C2 and C6 are
analogous). Bottom: the nitronium ion attacks C4 from this electron-rich position; the sigma complex
loses a proton to give 4-nitropyridine N-oxide, from which PCl3 removes the oxygen."""

from wikichem import Scheme

s = Scheme()
y = 0.0
a = s.molecule("[O-][n+]1ccccc1", at=(0, y), lone_pairs=[0])
s.curly(a.atom(0), a.bond(0, 1), bend=0.6)
s.curly(a.bond(1, 2), a.bond(2, 3), bend=0.6)
s.curly(a.bond(3, 4), a.atom(4), bend=0.6)
s.arrow((1.6, y), (2.8, y), kind="resonance")
b = s.molecule("O=[N+]1C=C[CH-]C=C1", at=(4.4, y), like=a, lone_pairs=[4])
no2 = s.molecule("O=[N+]=O", at=(b.xy(4)[0] + 2.0, b.xy(4)[1] + 0.2), lone_pairs=[0])
s.curly(b.atom(4), no2.atom(1), bend=-0.4)
s.curly(no2.bond(0, 1), no2.atom(0), bend=-0.6)

y = -4.4
s.arrow((-1.6, y), (-0.2, y))
s.molecule("O=[N+]1C=CC([N+](=O)[O-])C=C1", at=(2.0, y))
s.text((2.0, y - 2.6), "sigma complex")
s.arrow((4.4, y), (5.8, y), below=r"$-$H$^+$")
s.molecule("[O-][n+]1ccc(cc1)[N+](=O)[O-]", at=(8.0, y))
s.arrow((10.2, y), (11.6, y), above=r"PCl$_3$")
s.molecule("[O-][N+](=O)c1ccncc1", at=(13.4, y))
s.draw()
