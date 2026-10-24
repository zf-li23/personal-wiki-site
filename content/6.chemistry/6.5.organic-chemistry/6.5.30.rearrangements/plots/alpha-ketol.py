"""alpha-Ketol rearrangement of 1-acetylcyclopentan-1-ol in base (a model of the ring expansion of
17alpha-hydroxy-20-keto steroids to D-homosteroids). The alkoxide re-forms a C=O bond while a ring
C-C bond migrates with its electron pair to the neighbouring ketone carbon, whose pi electrons move
onto oxygen. The five-membered ring becomes a six-membered ring and the hydroxyl and carbonyl have
exchanged places: protonation gives 2-hydroxy-2-methylcyclohexan-1-one. The reaction is reversible
and the equilibrium favours the more stable isomer."""

from wikichem import Scheme

s = Scheme()
y = 0.0
m = s.molecule("CC(=O)C1([O-])CCCC1", at=(0.0, y), lone_pairs=[4], rotate=-40)
s.curly(m.atom(4), m.bond(3, 4), bend=0.6)
s.curly(m.bond(3, 5), m.atom(1), bend=0.6)
s.curly(m.bond(1, 2), m.atom(2), bend=-0.6)
s.text((0.0, y - 2.4), "alkoxide of the alpha-ketol")
s.arrow((2.4, y), (3.9, y), above="1,2-shift")
s.molecule("O=C1CCCCC1(C)[O-]", at=(6.0, y))
s.arrow((8.1, y), (9.5, y), above=r"H$^+$")
s.molecule("O=C1CCCCC1(C)O", at=(11.6, y))
s.text((11.6, y - 2.4), "2-hydroxy-2-methylcyclohexanone")
s.draw()
