"""Wolff rearrangement (Arndt-Eistert homologation), drawn from the carbanion resonance structure of
the alpha-diazoketone. The C2 lone pair forms the C1=C2 pi bond, the phenyl group migrates from C1 to
C2 with its bonding pair, and N2 leaves: one step gives the ketene. Water adds to the ketene and the
enol tautomerizes to phenylacetic acid, one carbon longer than benzoic acid."""

import math

from wikichem import Scheme

s = Scheme()
dk = s.molecule("[cH]1[cH][cH][cH][cH][c:6]1[C:1](=[O:2])[CH-:3][N+:4]#[N:5]", at=(0, 0), lone_pairs=[3])
s.curly(dk.atom(3), dk.bond(1, 3), bend=0.8)
s.curly(dk.bond(6, 1), dk.atom(3), bend=1.3)
s.curly(dk.bond(3, 4), dk.atom(4), bend=0.7)
s.arrow((3.0, 0), (4.6, 0), above=r"$h\nu$ or $\mathrm{Ag^+}$", below=r"$-\mathrm{N_2}$")
ring = [(math.cos(math.radians(a)), math.sin(math.radians(a))) for a in (120, 60, 0, 300, 240, 180)]
s.molecule("c1ccccc1[CH:7]=[C:8]=O", at=(8.6, 0), show_carbons=[8],
           coords=ring + [(-1.87, 0.5), (-2.73, 0.0), (-3.6, -0.5)])
s.arrow((10.0, 0), (11.4, 0), above=r"$\mathrm{H_2O}$")
s.molecule("c1ccccc1CC(=O)O", at=(13.5, 0))
s.draw()
