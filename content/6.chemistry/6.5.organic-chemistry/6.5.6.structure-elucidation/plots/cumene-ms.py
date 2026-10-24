"""Benzylic cleavage in the EI spectra of the two C9H12 isomers of the worked example. Top: the cumene
molecular ion (m/z 120) loses a methyl radical from the benzylic carbon, giving the
1-phenylethyl cation m/z 105 (base peak), stabilised by delocalisation into the ring. Bottom:
propylbenzene loses an ethyl radical instead; the benzyl cation (m/z 91) rearranges to the
aromatic tropylium ion, so its base peak is m/z 91."""

from wikichem import Scheme

s = Scheme()

y = 0.0
s.molecule("CC(C)c1ccccc1", at=(0, y))
s.text((-1.9, y), "[", size=34)
s.text((1.9, y), "]", size=34)
s.text((2.3, y + 0.9), r"$+\bullet$")
s.text((0, y - 2.0), "cumene, $m/z$ 120")
s.arrow((3.0, y), (4.6, y), below=r"$-$CH$_3^{\bullet}$")
s.molecule("C[CH+]c1ccccc1", at=(7.0, y))
s.text((7.0, y - 2.0), "$m/z$ 105")

y = -4.2
s.molecule("CCCc1ccccc1", at=(-0.3, y))
s.text((-3.0, y), "[", size=34)
s.text((2.3, y), "]", size=34)
s.text((2.7, y + 0.9), r"$+\bullet$")
s.text((0, y - 2.0), "propylbenzene, $m/z$ 120")
s.arrow((3.0, y), (4.6, y), below=r"$-$C$_2$H$_5^{\bullet}$")
s.molecule("[CH2+]c1ccccc1", at=(6.8, y))
s.arrow((8.4, y), (9.8, y))
s.molecule("C1=CC=C[CH+]C=C1", at=(11.1, y))
s.text((9.0, y - 2.0), "benzyl / tropylium, $m/z$ 91")
s.draw()
