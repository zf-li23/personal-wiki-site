"""+M effect of chlorine in chlorobenzene. A lone pair on chlorine moves into the ring, and the
negative charge is passed around to the two ortho carbons and the para carbon. These charge-separated
structures are minor contributors (chlorine's -I effect dominates overall), but they explain why
electron density builds up at the ortho and para positions."""

from rdkit.Chem import BondType

from wikichem import Scheme

s = Scheme(scale=0.4)
RING = "[CH:2]=[CH:3][CH:4]=[CH:5][CH:6]=1"
first = s.molecule("[Cl:7][c:1]1[cH:2][cH:3][cH:4][cH:5][cH:6]1", at=(0, 0), rotate=90, lone_pairs=[7])


def double(m, a, b):
    """Whether the bond between mapped atoms a and b is drawn double (RDKit chooses the Kekule form)."""
    ia = [x.GetIdx() for x in m.mol.GetAtoms() if x.GetAtomMapNum() == a][0]
    ib = [x.GetIdx() for x in m.mol.GetAtoms() if x.GetAtomMapNum() == b][0]
    return m.mol.GetBondBetweenAtoms(ia, ib).GetBondType() == BondType.DOUBLE


o, m_, p, m2, o2 = (2, 3, 4, 5, 6) if double(first, 1, 2) else (6, 5, 4, 3, 2)
ring = {o: 1, m_: 0, p: 0, m2: 0, o2: 0}


def smiles(neg, doubles, cl_double):
    """Chlorobenzene resonance structure: carbon `neg` carries the charge, `doubles` lists ring double bonds."""
    atoms = {k: f"[CH:{k}]" if k != neg else f"[CH-:{k}]" for k in range(2, 7)}
    c1 = "[C:1]"
    cl = "[Cl+:7]=" if cl_double else "[Cl:7]"
    order = [1, 2, 3, 4, 5, 6]
    bonds = {}
    for a, b in zip(order, order[1:] + [1]):
        bonds[(a, b)] = "=" if (a, b) in doubles or (b, a) in doubles else ""
    text = cl + c1 + "1" + bonds[(1, 2)] + atoms[2] + bonds[(2, 3)] + atoms[3] + bonds[(3, 4)] + atoms[4] + bonds[(4, 5)] + atoms[5] + bonds[(5, 6)] + atoms[6] + bonds[(6, 1)] + "1"
    return text


s.curly(first.atom(7), first.bond(7, 1), bend=-0.6)
s.curly(first.bond(1, o), first.atom(o), bend=-0.7)
x = 4.2
a = s.molecule(smiles(o, [(m_, p), (m2, o2)], True), at=(x, 0), like=first, lone_pairs=[o, 7])
s.curly(a.atom(o), a.bond(o, m_), bend=-0.7)
s.curly(a.bond(m_, p), a.atom(p), bend=-0.7)
s.arrow((1.6, 0), (2.4, 0), kind="resonance")
b = s.molecule(smiles(p, [(o, m_), (m2, o2)], True), at=(2 * x, 0), like=first, lone_pairs=[p, 7])
s.curly(b.atom(p), b.bond(p, m2), bend=-0.7)
s.curly(b.bond(m2, o2), b.atom(o2), bend=-0.7)
s.arrow((x + 1.6, 0), (x + 2.4, 0), kind="resonance")
s.molecule(smiles(o2, [(o, m_), (p, m2)], True), at=(3 * x, 0), like=first, lone_pairs=[o2, 7])
s.arrow((2 * x + 1.6, 0), (2 * x + 2.4, 0), kind="resonance")
for i, t in enumerate(["", "ortho", "para", "ortho"]):
    s.text((i * x, -2.3), t, size=10)
s.draw()
