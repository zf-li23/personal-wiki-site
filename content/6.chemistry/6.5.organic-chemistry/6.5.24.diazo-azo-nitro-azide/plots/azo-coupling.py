"""Azo coupling of benzenediazonium with phenoxide (SEAr). The oxygen lone pair pushes electrons
through the ring, and the para carbon attacks the terminal nitrogen of the diazonium ion, giving a
cyclohexadienone sigma complex; loss of the para proton restores the aromatic ring and gives
4-hydroxyazobenzene."""

import math

from wikichem import Scheme


def hexagon(angles, centre=(0.0, 0.0)):
    return [(centre[0] + math.cos(math.radians(a)), centre[1] + math.sin(math.radians(a))) for a in angles]


s = Scheme()
ph = s.molecule("[O-:1][C:7]1=[CH:8][CH:9]=[CH:2][CH:5]=[CH:6]1", at=(0, 0), lone_pairs=[1],
                coords=[(-2.0, 0.0)] + hexagon((180, 120, 60, 0, 300, 240)))
dz = s.molecule("[N:11]#[N+:12][c:13]1[cH:14][cH:15][cH:16][cH:17][cH:18]1", at=(2.6, 0.0),
                coords=[(0.0, 0.0), (1.0, 0.0)] + hexagon((180, 120, 60, 0, 300, 240), centre=(3.0, 0.0)))
s.curly(ph.atom(1), ph.bond(1, 7), bend=0.8)
s.curly(ph.bond(7, 8), ph.bond(8, 9), bend=0.7)
s.curly(ph.bond(9, 2), dz.atom(11), bend=-0.6)
s.curly(dz.bond(11, 12), dz.atom(12), bend=-0.7)
s.arrow((7.0, 0), (8.4, 0))
s.molecule("O=C1C=C[CH:3](C=C1)N=Nc1ccccc1", at=(11.8, 0), show_h=[3])
s.draw()

s = Scheme()
s.molecule("O=C1C=C[CH:3](C=C1)N=Nc1ccccc1", at=(0, 0), show_h=[3])
s.arrow((3.0, 0), (4.4, 0), above=r"$-\mathrm{H^+}$")
s.molecule("Oc1ccc(cc1)N=Nc1ccccc1", at=(8.2, 0))
s.draw()
