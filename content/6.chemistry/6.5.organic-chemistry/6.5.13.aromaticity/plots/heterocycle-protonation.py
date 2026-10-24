"""Where aromatic heterocycles take a proton. Top: the nitrogen lone pair of pyridine lies in an sp2
orbital in the ring plane, outside the pi system; it bonds to the proton and the pyridinium ion keeps
its 6 pi electrons (pKa of pyridinium 5.23). Bottom: the nitrogen lone pair of pyrrole is part of the
6-pi system; protonation therefore occurs at C2, with the nitrogen lone pair pushing through the ring
to give an iminium ion (the conjugate acid has pKa -3.8); the aromatic sextet is lost either way."""

exec(open("helpers.txt").read())


def nearest_h(mol, target):
    return min((mol.h(0, i) for i in range(3)), key=lambda p: np.linalg.norm(p.xy - target))


s = Scheme()
py = s.molecule("[n:1]1ccccc1", at=(0, 0), rotate=0, lone_pairs=[1])
h3o = s.molecule("[OH3+]", at=py.xy(1) + (1.9, 0.0) if py.xy(1)[0] > 0 else py.xy(1) + (-1.9, 0.0), show_h=[0])
hp = nearest_h(h3o, py.xy(1))
s.curly(py.atom(1), hp, bend=0.4)
s.curly(bond_to(h3o, 0, hp), h3o.atom(0), bend=0.8)
s.arrow((3.4, 0), (4.6, 0))
s.molecule("[nH+:1]1ccccc1", at=(6.0, 0), like=py)
s.text((6.0, -1.8), "pyridinium: still 6 pi", size=10)

y = -4.2
pr = s.molecule("[NH:1]1[CH:2]=[CH:3][CH:4]=[CH:5]1", at=(0, y), rotate=0, lone_pairs=[1])
out = pr.xy(2) - ring_centre(pr, [1, 2, 3, 4, 5])
h3o = s.molecule("[OH3+]", at=pr.xy(2) + 2.2 * out / np.linalg.norm(out), show_h=[0])
hp = nearest_h(h3o, pr.xy(2))
s.curly(pr.atom(1), pr.bond(1, 5), bend=0.7)
s.curly(pr.bond(5, 4), pr.bond(4, 3), bend=0.7)
s.curly(pr.bond(3, 2), hp, bend=0.4)
s.curly(bond_to(h3o, 0, hp), h3o.atom(0), bend=0.8)
s.arrow((3.4, y), (4.6, y))
s.molecule("[NH+:1]1[CH2:2][CH:3]=[CH:4][CH:5]=1", at=(6.0, y), like=pr)
s.text((6.0, y - 1.8), "C2-protonated pyrrole (iminium)", size=10)
s.draw()
