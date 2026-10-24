"""Key step of the Mannich reaction. Formaldehyde and dimethylamine condense (with loss of water)
to the dimethylmethyleneammonium (iminium) ion, a strong electrophile. The enol of acetone attacks
its carbon: the oxygen lone pair pushes, the C=C pi electrons form the new C-C bond and the C=N pi
electrons move onto nitrogen. Loss of the proton from oxygen gives the beta-amino ketone (Mannich
base)."""

from wikichem import Scheme

s = Scheme()
s.molecule("C=O", at=(-6.6, 0.4))
s.plus((-5.6, 0.2))
s.molecule("CNC", at=(-4.4, 0.2))
s.arrow((-3.4, 0.2), (-2.0, 0.2), kind="equilibrium", above=r"H$^+$", below=r"$-$H$_2$O")
im = s.molecule("C=[N+](C)C", at=(-0.4, -1.9))
enol = s.molecule("C=C(O)C", at=(-0.6, 2.0), rotate=180, lone_pairs=[2])
s.curly(enol.atom(2), enol.bond(1, 2), bend=-0.7)
s.curly(enol.bond(0, 1), im.atom(0), bend=-0.5)
s.curly(im.bond(0, 1), im.atom(1), bend=0.7)
s.text((2.3, -2.0), "iminium ion")
s.text((1.2, 2.9), "enol")
s.arrow((2.0, 0.2), (3.4, 0.2))
s.molecule("CC(=[OH+])CCN(C)C", at=(5.4, 0.2))
s.arrow((7.4, 0.2), (8.8, 0.2), above=r"$-$H$^+$")
s.molecule("CC(=O)CCN(C)C", at=(10.8, 0.2))
s.text((10.8, -1.3), "Mannich base")
s.draw()
