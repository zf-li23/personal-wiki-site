"""The basic electron movements written with curved arrows. (a) Nucleophilic attack with loss of a
leaving group in one step (SN2: hydroxide and chloromethane). (b) Heterolysis: loss of a leaving
group gives a carbocation. (c) Proton transfer: water takes the proton of HCl. (d) Rearrangement:
a 1,2-methyl shift turns a secondary carbocation into a tertiary one. (e) Homolysis of Cl2 written
with two fishhook (one-electron) arrows."""

from wikichem import Scheme

s = Scheme(scale=0.46)


def label(y, text):
    s.text((-3.2, y), text)


# (a) SN2: HO- + CH3Cl -> CH3OH + Cl-
y = 0.0
label(y, "(a)")
oh = s.molecule("[OH-]", at=(-1.6, y), lone_pairs=True)
mecl = s.molecule("CCl", at=(1.0, y), lone_pairs=[1])
s.curly(oh.atom(0), mecl.atom(0), bend=-0.45)
s.curly(mecl.bond(0, 1), mecl.atom(1), bend=-0.6)
s.arrow((2.9, y), (4.4, y))
s.molecule("CO", at=(5.6, y), lone_pairs=[1])
s.plus((7.0, y))
s.molecule("[Cl-]", at=(8.0, y), lone_pairs=True)

# (b) heterolysis: tert-butyl bromide -> tert-butyl cation + bromide
y = -3.4
label(y, "(b)")
tbu = s.molecule("CC(C)(C)Br", at=(0.0, y), rotate=-60, lone_pairs=[4])
s.curly(tbu.bond(1, 4), tbu.atom(4), bend=0.9)
s.arrow((2.2, y), (3.7, y))
s.molecule("C[C+](C)C", at=(5.2, y))
s.plus((6.8, y))
s.molecule("[Br-]", at=(7.8, y), lone_pairs=True)

# (c) proton transfer: H2O + HCl -> H3O+ + Cl-
y = -6.6
label(y, "(c)")
water = s.molecule("O", at=(-1.5, y), lone_pairs=True, explicit_h=True)
hcl = s.molecule("Cl", at=(1.1, y), lone_pairs=True, explicit_h=True, flip=True)
s.curly(water.atom(0), hcl.atom(1), bend=-0.5)
s.curly(hcl.bond(0, 1), hcl.atom(0), bend=-0.7)
s.arrow((2.6, y), (4.1, y))
s.molecule("[OH3+]", at=(5.4, y), explicit_h=True, lone_pairs=True)
s.plus((6.8, y))
s.molecule("[Cl-]", at=(7.8, y), lone_pairs=True)

# (d) 1,2-methyl shift: 3,3-dimethylbutan-2-yl cation -> 2,3-dimethylbutan-2-yl cation
y = -10.0
label(y, "(d)")
sec = s.molecule("CC(C)(C)[CH+]C", at=(0.0, y), rotate=30)
s.curly(sec.bond(1, 0), sec.atom(4), bend=-0.6)
s.arrow((2.2, y), (3.7, y))
s.molecule("C[C+](C)C(C)C", at=(5.6, y))
s.text((5.6, y - 1.6), "tertiary cation")
s.text((0.0, y - 1.6), "secondary cation")

# (e) homolysis of Cl2 with fishhook arrows
y = -13.6
label(y, "(e)")
cl2 = s.molecule("ClCl", at=(0.0, y))
mid = cl2.bond(0, 1)
s.curly(mid, cl2.atom(0) , bend=-1.2, single=True)
s.curly(mid, cl2.atom(1), bend=1.2, single=True)
s.arrow((2.2, y), (3.7, y), above=r"$h\nu$")
s.text((5.0, y), r"$\mathrm{Cl}\!\cdot$", size=13)
s.plus((6.2, y))
s.text((7.4, y), r"$\cdot\mathrm{Cl}$", size=13)
s.draw()
