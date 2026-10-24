"""Resonance structures generated with curved arrows, which move only pi electrons and lone pairs on
a fixed skeleton. (a) Allyl cation: a pi bond moves toward the positive charge. (b) Acetate: a lone
pair forms a pi bond while the other pi bond moves onto oxygen. (c) Acetamide: the nitrogen lone pair
is delocalized onto oxygen (the charge-separated form is the minor contributor). (d) Enolate of
acetone: the negative charge is shared by carbon and oxygen."""

from wikichem import Scheme

s = Scheme(scale=0.46)
GAP = 4.4  # horizontal distance between the two contributors


def row(y, tag, left, right, arrows, left_pairs=False, right_pairs=False):
    s.text((-2.6, y), tag)
    a = s.molecule(left, at=(0.0, y), lone_pairs=left_pairs)
    arrows(a)
    s.arrow((1.6, y), (2.8, y), kind="resonance")
    b = s.molecule(right, at=(GAP, y), lone_pairs=right_pairs)
    return a, b


# (a) allyl cation
row(0.0, "(a)", "C=C[CH2+]", "[CH2+]C=C", lambda m: s.curly(m.bond(0, 1), m.bond(1, 2), bend=0.6))

# (b) acetate
def acetate(m):
    s.curly(m.atom(3), m.bond(1, 3), bend=0.5)
    s.curly(m.bond(1, 2), m.atom(2), bend=0.6)


row(-3.2, "(b)", "CC(=O)[O-]", "CC([O-])=O", acetate, left_pairs=[2, 3], right_pairs=[2, 3])

# (c) acetamide
def amide(m):
    s.curly(m.atom(2), m.bond(1, 2), bend=-0.5)
    s.curly(m.bond(1, 3), m.atom(3), bend=-0.6)


row(-6.6, "(c)", "CC(N)=O", "CC(=[NH2+])[O-]", amide, left_pairs=[2, 3], right_pairs=[3])

# (d) enolate of acetone
def enolate(m):
    s.curly(m.atom(0), m.bond(0, 1), bend=-0.5)
    s.curly(m.bond(1, 3), m.atom(3), bend=-0.6)


row(-10.0, "(d)", "[CH2-]C(C)=O", "C=C(C)[O-]", enolate, left_pairs=[0, 3], right_pairs=[3])

s.draw()
