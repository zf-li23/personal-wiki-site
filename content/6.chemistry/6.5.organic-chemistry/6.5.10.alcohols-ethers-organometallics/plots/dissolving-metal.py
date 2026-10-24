"""Reduction of an alkyl halide by a dissolving metal (Na or Li in liquid ammonia). One electron from
the metal breaks the C-X bond into an alkyl radical and halide; a second electron turns the radical
into a carbanion, which takes a proton from ammonia."""

from wikichem import Scheme

s = Scheme()
s.text((-1.8, 0.9), r"e$^-$ (Na)")
rx = s.molecule("ClC1CCCCC1", at=(0.4, -0.2), lone_pairs=[0])
s.curly((-1.3, 0.6), rx.bond(0, 1), bend=-0.4, single=True)
s.curly(rx.bond(0, 1), rx.atom(0), bend=0.9, single=True)
s.arrow((2.2, 0), (3.6, 0), below=r"$-$Cl$^-$")
s.molecule("[CH]1CCCCC1", at=(4.8, 0))
s.arrow((6.0, 0), (7.4, 0), above=r"e$^-$")
an = s.molecule("[CH-]1CCCCC1", at=(8.6, 0), lone_pairs=[0])
nh = s.molecule("N", at=(7.0, -2.2), explicit_h=True, lone_pairs=[0], rotate=150)
s.curly(an.atom(0), nh.atom(1), bend=-0.4)
s.curly(nh.bond(0, 1), nh.atom(0), bend=-0.8)
s.arrow((11.8, 0), (13.2, 0), below=r"$-$NH$_2^-$")
s.molecule("C1CCCCC1", at=(14.4, 0))
s.draw()
