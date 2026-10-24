"""Hydroboration-oxidation of propene (methyl groups stand for the other alkyl groups on boron). Figure 1: the four-centre transition state:
boron adds to the less substituted carbon and hydride to the other, on the same face (syn), in one
concerted but asynchronous step (the more substituted carbon carries partial positive charge).
Figure 2: oxidation: hydroperoxide adds to boron, then an alkyl group migrates from B to O with
retention of configuration while hydroxide leaves; hydrolysis of the borate gives the alcohol."""

import numpy as np
from wikichem import Scheme


def fixed(s, smiles, coords, at=(0, 0), lone_pairs=()):
    """Place a structure at hand-chosen atom coordinates (SMILES order, in bond lengths)."""
    return s.molecule(smiles, at=at, coords=coords, lone_pairs=list(lone_pairs))


# Figure 1: alkene + BH3, curved arrows, and the four-centre transition state.
s = Scheme()
alkene = fixed(s, "CC=C", [(-0.9, -0.5), (0, 0), (1.2, 0)])
borane = fixed(s, "B([H])([H])[H]", [(1.2, 1.3), (1.95, 1.75), (0.45, 1.75), (0.0, 1.3)])
s.curly(alkene.bond(1, 2), borane.atom(0), bend=-0.6)
s.curly(borane.bond(0, 3), alkene.atom(1), bend=0.4)
s.text((0.3, -1.4), r"propene + BH$_3$")
s.arrow((2.8, 0.5), (4.2, 0.5))

x = 5.8
ts = fixed(s, "CC=C", [(-0.9, -0.5), (0, 0), (1.2, 0)], at=(x, 0))
s.partial((x + 1.2, 0.25), (x + 1.2, 1.05))
s.partial((x, 0.25), (x, 1.1))
s.partial((x + 0.25, 1.3), (x + 0.95, 1.3))
s.text((x + 1.2, 1.3), "B")
s.text((x, 1.3), "H")
s.text((x + 1.55, 1.85), r"H$_2$")
s.text((x - 0.35, 0.0), r"$\delta^+$", size=10)
s.text((x + 1.65, 1.0), r"$\delta^-$", size=10)
s.text((x + 0.4, -1.4), "four-centre TS")
s.text((x + 2.1, 0.6), r"$\ddagger$", size=16)
s.arrow((x + 2.6, 0.5), (x + 4.0, 0.5))
s.molecule("CCCB", at=(x + 5.4, 0.3))
s.text((x + 5.4, -1.4), "propylborane")
s.draw()

# Figure 2: oxidation of the trialkylborane by alkaline hydrogen peroxide.
s = Scheme()
borate = s.molecule("C[B-](C)(C)OO", at=(0, 0), lone_pairs=[4, 5])
s.curly(borate.bond(1, 2), borate.atom(4), bend=0.5)
s.curly(borate.bond(4, 5), borate.atom(5), bend=-0.6)
s.text((0, -1.7), "hydroperoxide adduct")
s.arrow((2.0, 0), (3.6, 0), above=r"$-\mathrm{HO}^-$", below="R: B to O")
s.molecule("CB(C)OC", at=(5.2, 0))
s.arrow((6.8, 0), (8.6, 0), above=r"repeat, then", below=r"NaOH, H$_2$O")
s.molecule("CO", at=(9.6, 0))
s.text((12.4, 0), r"+  B(OH)$_4^-$")
s.draw()
