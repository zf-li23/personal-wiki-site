"""Bromination of cyclohexene. Step 1: the pi bond attacks one bromine and the Br-Br bond breaks,
giving a cyclic bromonium ion and bromide. Step 2: bromide opens the ring from the face opposite to
the bridging bromine (an SN2-like backside attack), so the two bromines end up trans: anti addition,
racemic trans-1,2-dibromocyclohexane."""

import numpy as np
from wikichem import Scheme


def fixed(s, smiles, coords, at=(0, 0), lone_pairs=()):
    """Place a structure at hand-chosen atom coordinates (SMILES order, in bond lengths)."""
    return s.molecule(smiles, at=at, coords=coords, lone_pairs=list(lone_pairs))


# Hexagon with a vertical left edge: atoms 0 (top left) and 1 (bottom left), then clockwise round.
ang = np.radians([150, 210, 270, 330, 30, 90])
ring = [(np.cos(t), np.sin(t)) for t in ang]
order = [ring[0], ring[1], ring[2], ring[3], ring[4], ring[5]]

s = Scheme()
alkene = fixed(s, "C1=CCCCC1", order)
br2 = fixed(s, "BrBr", [(-2.0, 0), (-3.1, 0)], lone_pairs=(0, 1))
s.curly(alkene.bond(0, 1), br2.atom(0), bend=0.5)
s.curly(br2.bond(0, 1), br2.atom(1), bend=-0.9)
s.arrow((1.5, 0), (3.0, 0))

x = 5.8
ion = fixed(s, "C12CCCCC1[Br+]2", [ring[0], ring[5], ring[4], ring[3], ring[2], ring[1], (-2.0, 0)], at=(x, 0))
bromide = fixed(s, "[Br-]", [(x + 0.2, -2.4)], lone_pairs=(0,))
s.curly(bromide.atom(0), ion.atom(5), bend=-0.3)
s.curly(ion.bond(5, 6), ion.atom(6), bend=0.9)
s.arrow((x + 1.6, 0), (x + 3.1, 0))

s.molecule("Br[C@@H]1CCCC[C@H]1Br", at=(x + 5.2, 0))
s.text((-0.9, -2.0), "cyclohexene")
s.text((x - 0.6, 1.6), "bromonium ion")
s.text((x + 5.2, -2.0), "trans (racemic)")
s.draw()
