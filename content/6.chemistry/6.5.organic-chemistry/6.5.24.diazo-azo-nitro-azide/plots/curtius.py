"""Curtius rearrangement of pivaloyl azide, drawn from the resonance structure with a negative
nitrogen next to the carbonyl. In one concerted step the tert-butyl group migrates from carbon to the
adjacent nitrogen while N2 leaves, giving tert-butyl isocyanate (configuration of the migrating
carbon is retained). Water adds to the isocyanate; the carbamic acid loses CO2 to give the amine."""

from wikichem import Scheme

s = Scheme()
az = s.molecule("C[C:5](C)(C)[C:1](=O)[N-:2][N+:3]#[N:4]", at=(0, 0), lone_pairs=[2],
                coords=[(-1.37, 1.37), (-0.87, 0.5), (-1.87, 0.5), (-0.87, -0.5), (0.0, 1.0), (0.0, 2.0),
                        (0.87, 0.5), (1.87, 0.5), (2.87, 0.5)])
s.curly(az.bond(5, 1), az.atom(2), bend=-0.5)
s.curly(az.atom(2), az.bond(1, 2), bend=-0.9)
s.curly(az.bond(2, 3), az.atom(3), bend=0.6)
s.arrow((3.6, 0.5), (5.0, 0.5), above="heat", below=r"$-\mathrm{N_2}$")
s.molecule("CC(C)(C)N=[C:1]=O", at=(7.1, 0.5), show_carbons=[1],
           coords=[(-1.37, 0.87), (-0.87, 0.0), (-1.37, -0.87), (-1.87, 0.0), (0.13, 0.0), (1.13, 0.0), (2.13, 0.0)])
s.arrow((9.7, 0.5), (11.1, 0.5), above=r"$\mathrm{H_2O}$")
s.molecule("CC(C)(C)NC(=O)O", at=(12.9, 0.5))
s.arrow((14.6, 0.5), (16.0, 0.5), below=r"$-\mathrm{CO_2}$")
s.molecule("CC(C)(C)N", at=(17.2, 0.5))
s.draw()
