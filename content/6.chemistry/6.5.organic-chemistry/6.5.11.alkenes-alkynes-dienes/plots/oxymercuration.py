"""Oxymercuration-demercuration of 2-methylpropene. The electrophile AcOHg+ forms a bridged
mercurinium ion; the C-Hg bond to the more substituted carbon is longer and that carbon carries
more positive charge, so water attacks there (Markovnikov, anti to Hg). Loss of a proton gives the
organomercurial, and NaBH4 replaces C-Hg by C-H (a radical step, not shown)."""

import numpy as np
from wikichem import Scheme


def fixed(s, smiles, coords, at=(0, 0), lone_pairs=()):
    """Place a structure at hand-chosen atom coordinates (SMILES order, in bond lengths)."""
    return s.molecule(smiles, at=at, coords=coords, lone_pairs=list(lone_pairs))


s = Scheme(scale=0.4)
ion = fixed(s, "CC1(C)C[Hg+]1OC(C)=O",
            [(-0.87, 0.5), (0, 0), (-0.87, -0.5), (1.3, 0), (0.65, 1.15), (0.65, 2.25), (1.52, 2.75), (1.52, 3.75), (2.39, 2.25)])
water = s.molecule("O", at=(0.0, -1.9), lone_pairs=True, explicit_h=True)
s.curly(water.atom(0), ion.atom(1), bend=-0.3)
s.curly(ion.bond(1, 4), ion.atom(4), bend=0.5)
s.text((0.6, -3.2), "mercurinium ion")
s.arrow((2.9, 0.4), (4.4, 0.4), above=r"$-\mathrm{H}^+$")
s.molecule("CC(C)(O)C[Hg]OC(C)=O", at=(7.0, 0.4))
s.arrow((9.8, 0.4), (11.4, 0.4), above=r"NaBH$_4$", below="NaOH")
s.molecule("CC(C)(C)O", at=(12.7, 0.4))
s.text((12.7, -1.2), "Markovnikov alcohol")
s.draw()
