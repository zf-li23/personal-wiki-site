"""Converting an alcohol into a tosylate keeps its configuration. Top: the oxygen lone pair of
(R)-2-octanol attacks sulfur of tosyl chloride and chloride leaves; pyridine removes the proton from
the oxonium ion. Only the O-H bond is broken, the C-O bond is untouched. Bottom: bromide then attacks
the stereocentre from the back (SN2), displacing the tosylate anion with inversion, giving
(S)-2-bromooctane. Ar = 4-methylphenyl, R = n-hexyl."""

from wikichem import Scheme

s = Scheme()
al = s.molecule("C[C@@H]([OH:1])*", at=(0, 0), lone_pairs=[1], labels={3: "R"})
o = al.xy(1)
ts = s.molecule("*[S:2](=O)(=O)[Cl:3]", coords=[(o[0] + 3.0, o[1] + 1.2), (o[0] + 1.8, o[1] + 0.6), (o[0] + 1.8, o[1] + 1.9), (o[0] + 1.8, o[1] - 0.7), (o[0] + 3.0, o[1] - 0.2)], labels={0: "Ar"}, lone_pairs=[3])
s.curly(al.atom(1), ts.atom(2), bend=-0.4)
s.curly(ts.bond(2, 3), ts.atom(3), bend=-0.7)
s.arrow((o[0] + 3.9, 0.3), (o[0] + 5.1, 0.3), below=r"$-$Cl$^-$")
x = o[0] + 7.0
ox = s.molecule("C[C@@H]([OH+:1][S](=O)(=O)*)*", at=(x, 0.3), labels={6: "Ar", 7: "R"}, show_h=[1])
hx = ox.h(1).xy
py = s.molecule("n1ccccc1", at=(hx[0] + 2.2, hx[1] + 0.4), lone_pairs=[0], rotate=0)
s.curly(py.atom(0), ox.h(1), bend=0.4)
s.curly((ox.xy(1) + ox.h(1).xy) / 2, ox.atom(1), bend=0.8)
s.arrow((x + 3.3, -0.6), (x + 4.6, -0.6), below=r"$-$pyH$^+$")
s.molecule("C[C@@H](OS(=O)(=O)*)*", at=(x + 6.4, -0.3), labels={6: "Ar", 7: "R"})
s.text((x + 6.4, -1.9), "(R)-2-octyl tosylate", size=10)
s.draw()

s = Scheme()
br = s.molecule("[Br-]", at=(-2.2, 0), lone_pairs=True)
# same atom order as the SMILES of the tosylate above: CH3, C*, O, S, O, O, Ar, R
t = s.molecule("C[C@@H:1]([O:2]S(=O)(=O)*)*", coords=[(-0.4, 1.2), (0, 0), (1.3, 0), (2.4, 0.6), (2.0, 1.7), (2.8, -0.4), (3.6, 1.2), (-0.4, -1.2)], labels={6: "Ar", 7: "R"})
s.curly(br.atom(0), t.atom(1), bend=0.3)
s.curly(t.bond(1, 2), t.xy(2) + (0.0, -0.4), bend=-0.6)
s.arrow((4.3, 0), (5.7, 0), above="SN2", below="inversion")
s.molecule("C[C@H](Br)*", at=(7.0, 0), labels={3: "R"})
s.text((7.0, -1.3), "(S)-2-bromooctane", size=10)
s.plus((8.4, 0))
s.text((9.3, 0), r"TsO$^-$")
s.draw()
