"""Lossen rearrangement of O-acetyl benzohydroxamic acid. The hydroxamic acid itself does not
rearrange: its oxygen is first acylated (or sulfonylated) so that a carboxylate can leave from
nitrogen. Base removes the N-H proton; the nitrogen lone pair forms C=N while the phenyl group
migrates with its electron pair from carbon to nitrogen and acetate leaves, in one concerted step,
giving phenyl isocyanate. Water converts the isocyanate into aniline and CO2."""

from wikichem import Scheme

s = Scheme(scale=0.4)
y = 0.0
s.molecule("O=C(NOC(C)=O)c1ccccc1", at=(0.0, y))
s.text((0.0, y - 2.4), "O-acetyl hydroxamic acid")
s.arrow((3.2, y), (4.6, y), above=r"base", below=r"$-\,\mathrm{H^+}$")
a = s.molecule("O=C([N-]OC(C)=O)c1ccccc1", at=(8.0, y), lone_pairs=[2])
s.curly(a.atom(2), a.bond(1, 2), bend=0.6)
s.curly(a.bond(1, 7), a.atom(2), bend=-0.7)
s.curly(a.bond(2, 3), a.atom(3), bend=0.6)
s.text((8.0, y - 2.4), "N-anion")
s.arrow((11.2, y), (12.6, y), below=r"$-\,\mathrm{CH_3CO_2^-}$")
s.molecule("O=C=Nc1ccccc1", at=(16.0, y), show_carbons=[1])
s.text((16.0, y - 2.4), "phenyl isocyanate")
s.arrow((18.4, y), (19.8, y), above=r"H$_2$O", below=r"$-\,\mathrm{CO_2}$")
s.molecule("Nc1ccccc1", at=(21.6, y))
s.text((21.6, y - 2.4), "aniline")
s.draw()
