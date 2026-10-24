"""Henry (nitroaldol) reaction of nitromethane with benzaldehyde. Hydroxide removes an alpha hydrogen
of nitromethane; the nitronate anion (negative charge shared with the oxygens) attacks the carbonyl
carbon with its carbon atom, and the alkoxide takes a proton from water to give
2-nitro-1-phenylethanol."""

from wikichem import Scheme

s = Scheme()
nm = s.molecule("[H:4][CH2:1][N+:2](=O)[O-:3]", at=(0, 0), coords=[(-1.0, 0.8), (-1.0, -0.2), (0.0, -0.2), (0.5, 0.67), (0.5, -1.07)])
oh = s.molecule("[OH-:9]", at=(-2.6, 1.4), lone_pairs=True)
s.curly(oh.atom(9), nm.atom(4), bend=-0.4)
s.curly(nm.bond(4, 1), nm.bond(1, 2), bend=0.6)
s.curly(nm.bond(2, 3), nm.atom(3), bend=0.6)
s.arrow((1.6, 0), (3.0, 0), kind="equilibrium")
a = s.molecule("[CH2:1]=[N+:2]([O-])[O-]", at=(4.6, 0), lone_pairs=False)
s.arrow((5.9, 0), (6.9, 0), kind="resonance")
b = s.molecule("[CH2-:1][N+:2](=O)[O-]", at=(8.3, 0), lone_pairs=[1])
s.draw()

s = Scheme()
import math
nit = s.molecule("[CH2-:1][N+:2](=O)[O-]", at=(0, 0), lone_pairs=[1],
                 coords=[(0.0, 0.0), (1.0, 0.0), (1.5, 0.87), (1.5, -0.87)])
ring = [(-3.47 + math.cos(math.radians(a)), 0.1 + math.sin(math.radians(a))) for a in (0, 60, 120, 180, 240, 300)]
ald = s.molecule("[O:5]=[CH:6]c1ccccc1", at=(0, 0), coords=[(-1.6, 1.6), (-1.6, 0.6)] + ring)
s.curly(nit.atom(1), ald.atom(6), bend=0.4)
s.curly(ald.bond(5, 6), ald.atom(5), bend=-0.6)
s.arrow((2.4, 0), (3.8, 0))
s.molecule("[O-]C(C[N+](=O)[O-])c1ccccc1", at=(6.8, 0))
s.arrow((9.7, 0), (11.1, 0), above=r"$\mathrm{H_2O}$", below=r"$-\mathrm{OH^-}$")
s.molecule("OC(C[N+](=O)[O-])c1ccccc1", at=(14.0, 0))
s.draw()
