"""Making aromatic ions. Figure 1: hydride (from NaH) removes a proton from the CH2 group of
cyclopentadiene (H2 is released); the cyclopentadienyl anion has five equivalent resonance structures,
so the charge and the six pi electrons are spread evenly over all five carbons. Figure 2: the trityl
cation abstracts a hydride from the CH2 group of cycloheptatriene (the C-H bond pair moves to the
cationic carbon); the tropylium ion, with six pi electrons over seven carbons, forms."""

exec(open("helpers.txt").read())

FORMS = ["[CH-:1]1[CH:2]=[CH:3][CH:4]=[CH:5]1",
         "[CH:1]1=[CH:2][CH-:3][CH:4]=[CH:5]1",
         "[CH:1]1=[CH:2][CH:3]=[CH:4][CH-:5]1",
         "[CH:1]1[CH-:2][CH:3]=[CH:4][CH:5]=1",
         "[CH:1]1[CH:2]=[CH:3][CH-:4][CH:5]=1"]
CHARGED = [1, 3, 5, 2, 4]

s = Scheme()
cp = s.molecule("[CH2:1]1[CH:2]=[CH:3][CH:4]=[CH:5]1", at=(0, 0), show_h=[1], rotate=0)
h = max((cp.h(1, i) for i in range(2)), key=lambda p: p.xy[1])
hyd = s.molecule("[H-]", at=h.xy + (1.3, 0.6))
s.curly(hyd.atom(0), h, bend=0.5)
s.curly(bond_to(cp, 1, h), cp.atom(1), bend=-0.9)
s.arrow((2.6, 0), (3.8, 0), above="NaH", below=r"$-$H$_2$")
dx = 3.2
first = None
for i, (smi, k) in enumerate(zip(FORMS, CHARGED)):
    m = s.molecule(smi, at=(5.6 + dx * i, 0), lone_pairs=[k], **({"rotate": 0} if first is None else {"like": first}))
    first = first or m
    if i:
        s.arrow((5.6 + dx * (i - 0.5) - 0.3, 0), (5.6 + dx * (i - 0.5) + 0.3, 0), kind="resonance")
s.text((5.6 + 2 * dx, -1.8), "cyclopentadienyl anion: 6 pi electrons, five equivalent structures", size=10)
s.draw()

s = Scheme()
c7 = s.molecule("[CH2:1]1[CH:2]=[CH:3][CH:4]=[CH:5][CH:6]=[CH:7]1", at=(0, 0), show_h=[1], rotate=0)
h = min((c7.h(1, i) for i in range(2)), key=lambda p: p.xy[0] + p.xy[1])
tr = s.molecule("[C+:8]([*:9])([*:10])[*:11]", at=h.xy + (-1.6, -1.6), labels={9: "Ph", 10: "Ph", 11: "Ph"})
s.curly(bond_to(c7, 1, h), tr.atom(8), bend=0.5)
s.arrow((2.4, 0), (3.6, 0))
t = s.molecule("[CH+:1]1[CH:2]=[CH:3][CH:4]=[CH:5][CH:6]=[CH:7]1", at=(5.2, 0))
s.text((5.2, -1.9), "tropylium ion", size=10)
s.plus((7.0, 0))
s.molecule("[CH:8]([*:9])([*:10])[*:11]", at=(8.4, 0), labels={9: "Ph", 10: "Ph", 11: "Ph"})
s.draw()
