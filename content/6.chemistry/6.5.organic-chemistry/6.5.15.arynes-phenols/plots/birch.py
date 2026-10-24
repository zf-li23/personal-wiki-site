"""Birch reduction of benzene (Na, liquid NH3, EtOH): electron, proton, electron, proton.
Top: a solvated electron enters the LUMO of benzene; the radical anion (drawn as one resonance
structure) takes a proton from ethanol at a carbanion carbon. Bottom: the cyclohexadienyl radical
takes a second electron; the cyclohexadienyl (pentadienyl) anion is protonated at its central carbon,
giving the non-conjugated cyclohexa-1,4-diene."""

exec(open("helpers.txt").read())

s = Scheme()
s.molecule("C1=CC=CC=C1", at=(0, 0))
s.arrow((1.4, 0), (2.6, 0), above=r"e$^-$(NH$_3$)")
ra = s.molecule("[CH-:1]1[CH:2]=[CH:3][CH:4][CH:5]=[CH:6]1", at=(4.2, 0), lone_pairs=[1], rotate=90)
etoh = s.molecule("CCO", at=ra.xy(1) + (2.3, -0.5), show_h=[2], lone_pairs=[2])
s.curly(ra.atom(1), etoh.h(2), bend=0.3)
s.curly(bond_to(etoh, 2, etoh.h(2)), etoh.atom(2), bend=1.2)
s.arrow((7.4, 0), (8.6, 0), above=r"$-$EtO$^-$")
s.molecule("[CH2:1]1[CH:2]=[CH:3][CH:4][CH:5]=[CH:6]1", at=(10.2, 0), rotate=90)
s.text((4.2, 1.8), "radical anion", size=10)
s.text((10.2, 1.8), "cyclohexadienyl radical", size=10)

y = -4.8
s.molecule("[CH2:1]1[CH:2]=[CH:3][CH:4][CH:5]=[CH:6]1", at=(0, y), rotate=90)
s.arrow((1.4, y), (2.6, y), above=r"e$^-$(NH$_3$)")
an = s.molecule("[CH2:1]1[CH:2]=[CH:3][CH-:4][CH:5]=[CH:6]1", at=(4.2, y), lone_pairs=[4], rotate=90)
etoh = s.molecule("CCO", at=an.xy(4) + (1.8, 1.0), show_h=[2], lone_pairs=[2])
s.curly(an.atom(4), etoh.h(2), bend=-0.3)
s.curly(bond_to(etoh, 2, etoh.h(2)), etoh.atom(2), bend=-0.9)
s.arrow((7.0, y), (8.2, y), above=r"$-$EtO$^-$")
s.molecule("C1C=CCC=C1", at=(9.8, y), rotate=90)
s.text((4.2, y - 1.9), "cyclohexadienyl anion", size=10)
s.text((9.8, y - 1.9), "cyclohexa-1,4-diene", size=10)
s.draw()
