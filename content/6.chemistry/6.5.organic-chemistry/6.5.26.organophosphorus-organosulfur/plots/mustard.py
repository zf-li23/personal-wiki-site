"""Sulfur mustard alkylates DNA by neighbouring-group participation. The sulfur lone pair displaces
chloride intramolecularly, giving a strained three-membered episulfonium (thiiranium) ion; a
nucleophile (in DNA, N7 of guanine, written Nu) opens the ring by SN2. The second chloroethyl arm
reacts the same way, so one molecule can cross-link two strands."""

from wikichem import Scheme

s = Scheme()
m = s.molecule("ClCCSCCCl", coords=[(-1.3, 1.5), (-0.8, 0.63), (0.2, 0.63), (0.7, -0.23), (1.7, -0.23), (2.2, 0.63), (3.2, 0.63)],
               lone_pairs=[3])
s.curly(m.atom(3, pair=0), m.atom(1), bend=0.4)
s.curly(m.bond(0, 1), m.atom(0), bend=0.6)
s.arrow((4.0, 0.3), (5.4, 0.3), above="$-$Cl$^-$")
ep = s.molecule("C1C[S+]1CCCl", coords=[(-0.5, 0.87), (0.5, 0.87), (0.0, 0.0), (0.5, -0.87), (1.5, -0.87), (2.0, 0.0)],
                at=(7.0, 0.3))
nu = s.molecule("*", at=(6.0, 2.3), labels={0: "Nu:"})
s.curly(nu.atom(0), ep.atom(0), bend=0.5)
s.curly(ep.bond(0, 2), ep.atom(2), bend=0.6)
s.arrow((10.0, 0.3), (11.4, 0.3))
s.molecule("*CCSCCCl", coords=[(-1.3, 1.5), (-0.8, 0.63), (0.2, 0.63), (0.7, -0.23), (1.7, -0.23), (2.2, 0.63), (3.2, 0.63)],
           at=(13.2, 0.3), labels={0: "Nu$^+$"})
s.draw()
