"""Sulfonation and desulfonation. (1) A pi bond of benzene attacks the sulfur of SO3 and an S=O pi
bond moves onto oxygen: the sigma complex is a zwitterion (sulfonate anion, ring cation).
(2) A base (water or hydrogen sulfate) removes the proton from the sp3 carbon; the benzenesulfonate ion is then
protonated to benzenesulfonic acid. (3) Desulfonation is the reverse: in hot dilute acid the ring is
protonated at the ipso carbon, and the C-S bond breaks to release SO3 (taken up by water as H2SO4)."""

exec(open("helpers.txt").read())

RING = [1, 2, 3, 4, 5, 6]
SIG = "[CH:1]1([S:7](=O)(=O)[O-])[CH:2]=[CH:3][CH:4]=[CH:5][CH2:6]1"
IPSO = SIG

s = Scheme()
b = s.molecule("c1ccccc1", at=(0, 0), rotate=30)
so3 = s.molecule("[O:8]=[S:7](=O)=O", at=(0.3, 2.6), rotate=180, lone_pairs=[8])
s.curly(b.bond(0, 1), so3.atom(7), bend=-0.5)
s.curly(so3.bond(8, 7), so3.atom(8), bend=0.8)
s.arrow((1.8, 0.3), (3.2, 0.3), above="slow")
a = s.molecule(SIG, at=(5.0, 0), show_h=[1], rotate=-60)
charge(s, a, 6, RING)
h = a.h(1)
base = s.molecule("O", at=h.xy + (-0.3, -1.7), lone_pairs=True)
s.curly(base.atom(0), h, bend=-0.4)
s.curly(bond_to(a, 1, h), a.bond(1, 6), bend=-0.9)
s.arrow((8.4, 0), (9.6, 0), above="fast")
s.molecule("[O-]S(=O)(=O)c1ccccc1", at=(11.5, 0))
s.arrow((13.3, 0), (14.5, 0), above=r"H$^+$", kind="equilibrium")
s.molecule("OS(=O)(=O)c1ccccc1", at=(16.4, 0))
s.draw()

s = Scheme()
ar = s.molecule("[O-][S:7](=O)(=O)[C:1]1=[CH:2][CH:3]=[CH:4][CH:5]=[CH:6]1", at=(0, 0))
out = ar.xy(2) - ring_centre(ar, RING)
h3o = s.molecule("[OH3+]", at=ar.xy(2) + 2.3 * out / np.linalg.norm(out) + (0.9, 0), show_h=[0])
hp = min((h3o.h(0, i) for i in range(3)), key=lambda p: np.linalg.norm(p.xy - ar.bond(1, 2).xy))
s.curly(ar.bond(1, 2), hp, bend=0.4)
s.curly(bond_to(h3o, 0, hp), h3o.atom(0), bend=-0.9)
s.arrow((3.4, 0), (4.6, 0), above=r"H$_3$O$^+$, heat")
a = s.molecule(IPSO, at=(6.8, 0), show_h=[1], rotate=-60)
charge(s, a, 6, RING)
s.curly(a.bond(1, 7), a.bond(1, 6), bend=-0.9)
s.arrow((9.0, 0), (10.2, 0), above="fast")
s.molecule("c1ccccc1", at=(11.4, 0))
s.plus((12.8, 0))
s.text((14.0, 0), r"SO$_3$")
s.text((7.0, -2.6), "protonation at the ipso carbon", size=10)
s.draw()
