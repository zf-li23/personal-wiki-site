"""Conjugate (1,4-) addition of methanethiolate to cyclohex-2-en-1-one. The nucleophile attacks the
beta carbon; the C=C pi electrons move between the alpha carbon and the carbonyl carbon, and the
C=O pi electrons move onto oxygen, giving an enolate. Protonation (on oxygen, then tautomerisation,
or directly on the alpha carbon) gives the saturated 3-substituted ketone."""

from wikichem import Scheme

s = Scheme()
nu = s.molecule("C[S-]", at=(2.4, 1.4), lone_pairs=[1])
en = s.molecule("O=C1C=CCCC1", at=(0, 0), lone_pairs=[0])
s.curly(nu.atom(1), en.atom(3), bend=0.4)
s.curly(en.bond(2, 3), en.bond(1, 2), bend=0.8)
s.curly(en.bond(0, 1), en.atom(0), bend=0.8)
s.arrow((3.2, 0), (4.6, 0))
s.molecule("[O-]C1=CC(SC)CCC1", at=(6.6, 0))
s.text((6.6, -2.0), "enolate", size=13)
s.arrow((8.8, 0), (10.2, 0), above=r"MeSH", below=r"$-$MeS$^-$")
s.molecule("O=C1CC(SC)CCC1", at=(12.2, 0))
s.draw()
