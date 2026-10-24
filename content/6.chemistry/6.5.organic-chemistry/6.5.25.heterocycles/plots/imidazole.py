"""Imidazole is both a base and an acid. Protonation at N3 gives the imidazolium ion, whose two
resonance structures are equivalent (charge shared by both nitrogens); loss of the N1-H proton gives
the imidazolide anion, whose charge is likewise shared by both nitrogens."""

from wikichem import Scheme

s = Scheme()
imid = s.molecule("[NH:1]1[CH:2]=[N:3][CH:4]=[CH:5]1", at=(0, 0), rotate=90)
s.arrow((1.6, 0.4), (3.0, 0.4), kind="equilibrium", above=r"$\mathrm{H^+}$", below=r"p$K_\mathrm{a}$ 6.99")
a = s.molecule("[NH:1]1[CH:2]=[NH+:3][CH:4]=[CH:5]1", at=(4.6, 0), like=imid)
s.arrow((5.9, 0), (6.9, 0), kind="resonance")
s.molecule("[NH+:1]1=[CH:2][NH:3][CH:4]=[CH:5]1", at=(8.4, 0), like=imid)
s.draw()

s = Scheme()
imid = s.molecule("[NH:1]1[CH:2]=[N:3][CH:4]=[CH:5]1", at=(0, 0), rotate=90)
s.arrow((1.6, 0.4), (3.0, 0.4), kind="equilibrium", above=r"$-\mathrm{H^+}$", below=r"p$K_\mathrm{a}$ 14.5")
s.molecule("[N-:1]1[CH:2]=[N:3][CH:4]=[CH:5]1", at=(4.6, 0), like=imid)
s.arrow((5.9, 0), (6.9, 0), kind="resonance")
s.molecule("[N:1]1=[CH:2][N-:3][CH:4]=[CH:5]1", at=(8.4, 0), like=imid)
s.draw()
