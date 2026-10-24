"""Alkylation of a ketone enolate. LDA removes an alpha proton of cyclohexanone completely at
-78 C, giving the lithium enolate (drawn as the free enolate). The enolate attacks iodomethane with
its carbon end (the C=C pi bond) in an SN2 reaction: the oxygen lone pair pushes, the pi electrons
form the new C-C bond and iodide leaves. The product is 2-methylcyclohexanone."""

from wikichem import Scheme


s = Scheme()
s.molecule("O=C1CCCCC1", at=(0, 0))
s.arrow((1.4, 0), (3.4, 0), above="LDA", below="THF, $-78$ °C")
e = s.molecule("[O-]C1=CCCCC1", at=(5.0, 0), rotate=60, flip=True, lone_pairs=[0])
mei = s.molecule("CI", at=(7.4, -1.2), lone_pairs=[1])
s.curly(e.atom(0), e.bond(0, 1), bend=0.7)
s.curly(e.bond(1, 2), mei.atom(0), bend=0.4)
s.curly(mei.bond(0, 1), mei.atom(1), bend=0.7)
s.text((5.0, -1.9), "lithium enolate")
s.arrow((8.6, 0), (10.0, 0), above="SN2", below=r"$-$I$^-$")
s.molecule("O=C1CCCCC1C", at=(11.8, 0))
s.draw()
