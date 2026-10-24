"""Native chemical ligation. Top: the thiolate of the N-terminal cysteine of peptide 2 attacks the
C-terminal thioester of peptide 1 (transthioesterification; this step is reversible and is
catalysed by an added aryl thiol); the alkyl thiol is released. Bottom: the new thioester sits
five atoms from the cysteine amino group, which attacks its carbonyl carbon through a
five-membered cyclic tetrahedral intermediate; the C-S bond breaks and the thiolate leaves.
This S-to-N acyl shift is irreversible and gives a native peptide bond with a free cysteine
side chain at the ligation site."""

from wikichem import Scheme

s = Scheme()
y = 0.0
te = s.molecule("*C(=O)SCC", at=(0.0, y), labels={0: "peptide 1"})
cys = s.molecule("[S-]C[C@H](N)C(=O)*", at=(5.0, y + 1.2), lone_pairs=[0], labels={6: "peptide 2"})
s.curly(cys.atom(0), te.atom(1), bend=0.5)
s.curly(te.bond(1, 2), te.atom(2), bend=-0.7)
s.arrow((7.2, y), (8.6, y), above=r"$-$EtS$^-$", kind="equilibrium")
s.molecule("*C(=O)SC[C@H](N)C(=O)*", at=(11.4, y), labels={0: "peptide 1", 9: "peptide 2"})
s.text((11.4, y - 3.1), "thioester-linked intermediate")

y = -6.0
i = s.molecule("*C(=O)SC[C@H](N)C(=O)*", at=(0.0, y), labels={0: "peptide 1", 9: "peptide 2"}, lone_pairs=[6])
s.curly(i.atom(6), i.atom(1), bend=0.7)
s.curly(i.bond(1, 2), i.atom(2), bend=-0.7)
s.arrow((3.0, y), (4.6, y), above="S-to-N shift", below="via 5-ring")
s.molecule("*C(=O)N[C@@H](CS)C(=O)*", at=(8.2, y), labels={0: "peptide 1", 9: "peptide 2"})
s.text((8.2, y - 2.4), "native peptide bond at Cys")
s.draw()
