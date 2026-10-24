"""Sandmeyer reaction with CuCl (single-electron mechanism). (1) Cu(I) transfers one electron to the
diazonium ion, giving the aryldiazenyl radical and CuCl2. (2) The C-N bond breaks homolytically and
N2 leaves, giving the phenyl radical. (3) The phenyl radical abstracts a chlorine atom from CuCl2,
giving chlorobenzene and regenerating Cu(I)."""

import math

from wikichem import Scheme

RING = [(math.cos(math.radians(a)) - 1.0, math.sin(math.radians(a))) for a in (180, 120, 60, 0, 300, 240)]

# (1) electron transfer and (2) loss of N2
s = Scheme()
s.molecule("c1ccc(cc1)[N+]#N", at=(0, 0), coords=RING + [(1.0, 0.0), (2.0, 0.0)])
s.arrow((2.6, 0), (4.2, 0), above="CuCl", below=r"$-\mathrm{CuCl_2}$")
dz = s.molecule("c1cc[c:6](cc1)[N:7]=[N:8]", at=(6.6, 0), coords=RING + [(1.0, 0.0), (1.5, 0.87)])
s.curly(dz.bond(6, 7), dz.atom(6), bend=1.2, single=True)
s.curly(dz.bond(6, 7), dz.bond(7, 8), bend=-1.0, single=True)
s.curly(dz.atom(8), dz.bond(7, 8), bend=-1.0, single=True)
s.arrow((9.2, 0), (10.6, 0))
s.molecule("[c]1ccccc1", at=(12.0, 0), rotate=180)
s.plus((13.7, 0))
s.molecule("N#N", at=(14.6, 0))
s.draw()

# (3) chlorine atom transfer
s = Scheme()
hexagon = [(math.cos(math.radians(a)), math.sin(math.radians(a))) for a in (0, 60, 120, 180, 240, 300)]
ph = s.molecule("[c:1]1ccccc1", at=(0, 0), coords=hexagon)
cu = s.molecule("[Cl:2][Cu:3]Cl", at=(4.4, 0), coords=[(-1.0, 0.0), (0.0, 0.0), (1.0, 0.0)])
meet = (ph.xy(1) + cu.xy(2)) / 2
s.curly(ph.atom(1), meet, bend=-0.5, single=True)
s.curly(cu.bond(2, 3), meet, bend=0.5, single=True)
s.curly(cu.bond(2, 3), cu.atom(3), bend=-1.2, single=True)
s.arrow((6.2, 0), (7.6, 0))
s.molecule("Clc1ccccc1", at=(9.4, 0), rotate=180)
s.plus((11.3, 0))
s.molecule("Cl[Cu]", at=(12.3, 0))
s.draw()
