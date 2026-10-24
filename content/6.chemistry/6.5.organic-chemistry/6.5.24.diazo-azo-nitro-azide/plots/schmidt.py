"""Schmidt reaction of a ketone (acetone), key step. Hydrazoic acid adds to the protonated carbonyl
group; loss of water gives the iminodiazonium ion. The alkyl group anti to the departing N2 migrates
from carbon to nitrogen as N2 leaves, giving a nitrilium ion; water adds to it and tautomerization
gives the amide (N-methylacetamide)."""

from wikichem import Scheme

s = Scheme()
im = s.molecule("[CH3:6][C:1](=[N:2][N+:3]#[N:4])[CH3:5]", at=(0, 0),
                coords=[(-0.5, 0.87), (0.0, 0.0), (1.0, 0.0), (1.5, 0.87), (2.0, 1.73), (-0.5, -0.87)])
s.curly(im.bond(5, 1), im.atom(2), bend=-0.6)
s.curly(im.bond(2, 3), im.atom(3), bend=0.6)
s.arrow((2.6, 0), (4.0, 0), below=r"$-\mathrm{N_2}$")
s.molecule("C[C:1]#[N+]C", at=(5.8, 0), show_carbons=[1], coords=[(-1.5, 0.0), (-0.5, 0.0), (0.5, 0.0), (1.5, 0.0)])
s.arrow((7.8, 0), (9.2, 0), above=r"$\mathrm{H_2O}$", below=r"$-\mathrm{H^+}$")
s.molecule("CC(O)=NC", at=(11.0, 0))
s.arrow((12.6, 0), (14.0, 0), kind="equilibrium")
s.molecule("CC(=O)NC", at=(15.5, 0))
s.draw()
