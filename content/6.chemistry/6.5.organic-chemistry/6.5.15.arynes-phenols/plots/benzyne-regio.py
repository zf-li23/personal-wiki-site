"""Regioselectivity of nucleophilic addition to 3-substituted benzynes.
Figure 1, 3-methoxybenzyne and amide. Top (observed): NH2- adds to C1, remote from OCH3, and the new
aryl anion is left at C2, next to the electronegative OCH3 group (the lone pair is in an sp2 orbital in
the ring plane, so only the -I effect acts); protonation gives 3-methoxyaniline only. Bottom (not
observed): addition to C2 would leave the anion at C1, far from OCH3.
Figure 2, 1-chloro-3-(trifluoromethyl)benzene: the most acidic H is H2, between Cl and CF3, so the
elimination gives 3-(trifluoromethyl)benzyne; addition then follows the same rule (anion next to CF3)
and only 3-(trifluoromethyl)aniline forms."""

exec(open("helpers.txt").read())

ARYNE = "C[O:7][C:3]1=[CH:4][CH:5]=[CH:6][C:1]#[C:2]1"
GOOD = "C[O:7][C:3]1=[CH:4][CH:5]=[CH:6][C:1]([NH2:8])=[C-:2]1"
BAD = "C[O:7][C:3]1=[CH:4][CH:5]=[CH:6][C-:1]=[C:2]1[NH2:8]"
RING = [1, 2, 3, 4, 5, 6]

s = Scheme()
for y, target, other, smi, product, note in ((0, 1, 2, GOOD, "COc1cccc(N)c1", "anion next to OCH$_3$: favored"),
                                            (-4.6, 2, 1, BAD, "COc1ccccc1N", "anion far from OCH$_3$: not observed")):
    a = s.molecule(ARYNE, at=(0, y))
    t = a.xy(target)
    out = t - ring_centre(a, RING)
    nh2 = s.molecule("[NH2-]", at=t + 1.5 * out / np.linalg.norm(out), lone_pairs=True)
    s.curly(nh2.atom(0), a.atom(target), bend=0.4)
    s.curly(a.bond(1, 2), a.atom(other), bend=0.8)
    s.arrow((2.2, y), (3.4, y))
    an = s.molecule(smi, at=(5.2, y), lone_pairs=[other])
    s.arrow((7.0, y), (8.2, y), above=r"NH$_3$")
    s.molecule(product, at=(10.4, y))
    s.text((5.2, y - 2.0), note, size=10)

s.draw()

s = Scheme()
sub = s.molecule("[Cl:9][C:1]1=[CH:2][C:3](C(F)(F)F)=[CH:4][CH:5]=[CH:6]1", at=(0, 0), show_h=[2], rotate=-90)
h = sub.h(2)
nh2 = s.molecule("[NH2-]", at=h.xy + (1.4, 1.0), lone_pairs=True)
s.curly(nh2.atom(0), h, bend=0.4)
s.curly(bond_to(sub, 2, h), sub.atom(2), bend=-0.9)
s.text((0, -2.6), "H2: between Cl and CF$_3$", size=10)
s.arrow((2.8, 0), (4.4, 0), above=r"$-$NH$_3$, $-$Cl$^-$")
ar = s.molecule("[C:1]1#[C:2][C:3](C(F)(F)F)=[CH:4][CH:5]=[CH:6]1", at=(6.6, 0), rotate=-90)
s.arrow((8.6, 0), (10.0, 0), above=r"NH$_2^-$, NH$_3$")
s.molecule("Nc1cccc(C(F)(F)F)c1", at=(12.0, 0))
s.text((12.0, -2.6), "3-(trifluoromethyl)aniline only", size=10)
s.draw()
