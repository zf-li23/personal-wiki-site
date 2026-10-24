"""Ritter reaction of tert-butanol with acetonitrile in concentrated sulfuric acid. The tertiary
cation, formed by ionization of the protonated alcohol, is attacked by the nitrogen lone pair of the
nitrile (the nitrile behaves as a weak nucleophile, like a proton acceptor). The nitrilium ion is
captured by water at carbon; tautomerization of the imidic acid gives N-tert-butylacetamide."""

from wikichem import Scheme

s = Scheme()
y = -1.8  # caption line
cat = s.molecule("C[C+](C)C", at=(0, 0))
nit = s.molecule("CC#N", at=(2.2, 0.0), lone_pairs=[2], flip=True)
s.curly(nit.atom(2), cat.atom(1), bend=-0.5)
s.text((0, y), "tert-butyl cation")
s.arrow((3.6, 0), (5.0, 0))
ni = s.molecule("CC#[N+]C(C)(C)C", at=(6.8, 0))
w = s.molecule("O", at=(5.2, 1.6), lone_pairs=True)
s.curly(w.atom(0), ni.atom(1), bend=0.4)
s.curly(ni.bond(1, 2), ni.atom(2), bend=0.7)
s.text((6.8, y), "nitrilium ion")
s.arrow((8.6, 0), (10.0, 0), above=r"$-\mathrm{H}^+$", below="tautomerism")
s.molecule("CC(=O)NC(C)(C)C", at=(12.2, 0))
s.text((12.2, y), "N-tert-butylacetamide")
s.draw()
