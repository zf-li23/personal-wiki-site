"""Generation of the electrophiles of SEAr.
(1) Bromination: Br2 gives a lone pair to FeBr3; the polarized Br-Br bond of the complex is then
attacked by the arene, and the Br-Br bond breaks heterolytically (FeBr4- leaves).
(2) Nitration: sulfuric acid protonates the OH of nitric acid; water leaves and the nitronium ion
O=N+=O forms.
(3) Friedel-Crafts acylation: the acyl chloride gives a chlorine lone pair to AlCl3; the C-Cl bond
breaks and the resonance-stabilized acylium ion forms.
(4) Friedel-Crafts alkylation with 1-chloropropane: as the C-Cl bond ionizes, a hydride shifts from
C2 to C1, so the secondary 2-propyl cation (not the primary cation) alkylates the ring."""

exec(open("helpers.txt").read())

# (1) bromination
s = Scheme()
br2 = s.molecule("BrBr", at=(0, 0), lone_pairs=True)
fe = s.molecule("Br[Fe](Br)Br", at=(2.6, 0))
s.curly(br2.atom(1), fe.atom(1), bend=-0.5)
s.arrow((4.0, 0), (5.2, 0))
cx = s.molecule("Br[Br+][Fe-](Br)(Br)Br", at=(7.2, 0), lone_pairs=[0])
benz = s.molecule("C1=CC=CC=C1", at=(7.0, 2.6))
s.curly(benz.bond(4, 5), cx.atom(0), bend=0.5)
s.curly(cx.bond(0, 1), cx.atom(1), bend=-0.7)
s.arrow((9.4, 0.8), (10.6, 0.8))
s.text((12.3, 1.2), "sigma complex", size=10)
s.text((12.3, 0.4), r"+ FeBr$_4^-$", size=11)
s.draw()

# (2) nitronium ion
s = Scheme()
hno3 = s.molecule("O[N+](=O)[O-]", at=(0, 0), lone_pairs=[0])
acid = s.molecule("OS(=O)(=O)O", at=(2.8, 0.6), show_h=[0])
s.curly(hno3.atom(0), acid.h(0), bend=-0.4)
s.curly(bond_to(acid, 0, acid.h(0)), acid.atom(0), bend=-0.8)
s.arrow((4.5, 0), (5.6, 0), above=r"$-$HSO$_4^-$")
prot = s.molecule("[OH2+][N+](=O)[O-]", at=(7.4, 0), lone_pairs=[3])
s.curly(prot.bond(0, 1), prot.atom(0), bend=0.7)
s.curly(prot.atom(3), prot.bond(1, 3), bend=0.7)
s.arrow((8.8, 0), (9.9, 0), above=r"$-$H$_2$O")
s.molecule("O=[N+]=O", at=(11.2, 0))
s.text((11.2, -0.8), "nitronium ion", size=10)
s.draw()

# (3) acylium ion
s = Scheme()
acyl = s.molecule("CC(=O)Cl", at=(0, 0), lone_pairs=[3])
al = s.molecule("Cl[Al](Cl)Cl", at=(2.6, 0))
s.curly(acyl.atom(3), al.atom(1), bend=-0.5)
s.arrow((3.9, 0), (5.0, 0))
cx = s.molecule("CC(=O)[Cl+][Al-](Cl)(Cl)Cl", at=(6.9, 0))
s.curly(cx.bond(1, 3), cx.atom(3), bend=0.8)
s.arrow((8.9, 0), (10.0, 0), above=r"$-$AlCl$_4^-$")
a1 = s.molecule("C[C+]=O", at=(11.2, 0), lone_pairs=[2])
s.curly(a1.atom(2), a1.bond(1, 2), bend=0.8)
s.arrow((12.3, 0), (13.2, 0), kind="resonance")
s.molecule("CC#[O+]", at=(14.4, 0))
s.text((12.8, -1.0), "acylium ion", size=10)
s.draw()

# (4) hydride shift during alkylation
s = Scheme()
cx = s.molecule("CCC[Cl+][Al-](Cl)(Cl)Cl", at=(0, 0), show_h=[1])
h = cx.h(1)
s.curly(cx.bond(2, 3), cx.atom(3), bend=-0.6)
s.curly(bond_to(cx, 1, h), cx.atom(2), bend=-0.6)
s.arrow((2.6, 0), (3.8, 0), above=r"$-$AlCl$_4^-$")
cat = s.molecule("CCC", at=(5.0, 0))
s.text(cat.xy(1) + (0, 0.45), "+")
s.text((5.0, -0.9), "2-propyl cation", size=10)
s.arrow((6.2, 0), (7.4, 0), above="benzene")
s.molecule("CC(C)c1ccccc1", at=(8.9, 0))
s.text((8.9, -2.5), "cumene (major)", size=10)
s.draw()
