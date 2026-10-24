"""Pummerer rearrangement of methyl phenyl sulfoxide in acetic anhydride (Ac = acetyl). Top: the
sulfoxide oxygen attacks a carbonyl carbon of the anhydride; loss of acetate gives an
acyloxysulfonium ion. Middle: acetate removes a proton from the S-methyl group; the C-H electrons
form the C=S bond while the S-O bond breaks and acetate leaves, giving a thionium ion
(PhS+=CH2). Bottom: acetate adds to the thionium carbon and the C=S pi electrons return to
sulfur, giving the alpha-acetoxy sulfide: the carbon next to sulfur has been oxidized while the
sulfur has been reduced."""

from wikichem import Scheme

s = Scheme()
so = s.molecule("C[S+](*)[O-]", coords=[(-0.5, 0.87), (0, 0), (-0.5, -0.87), (1.0, 0)], lone_pairs=[3], labels={2: "Ph"})
anh = s.molecule("CC(=O)OC(C)=O", coords=[(3.0, 1.6), (2.5, 0.73), (1.5, 0.73), (3.0, -0.13), (2.5, -1.0), (3.0, -1.87), (1.5, -1.0)],
                 lone_pairs=[2])
s.curly(so.atom(3), anh.atom(1), bend=-0.4)
s.curly(anh.bond(1, 2), anh.atom(2), bend=0.6)
s.arrow((4.0, 0), (5.6, 0), above="$-$AcO$^-$")
x = 7.4
s.molecule("C[S+](*)OC(C)=O", coords=[(-0.5, 0.87), (0, 0), (-0.5, -0.87), (1.0, 0), (1.5, 0.87), (1.0, 1.73), (2.5, 0.87)],
           at=(x, 0), labels={2: "Ph"})

y = -4.6
ac = s.molecule("[H]C([H])([H])[S+](*)OC(C)=O",
                coords=[(-1.0, 1.73), (-0.5, 0.87), (-1.45, 0.55), (0.35, 1.45), (0, 0), (-0.5, -0.87), (1.0, 0), (1.5, 0.87), (1.0, 1.73), (2.5, 0.87)],
                at=(0.6, y), labels={5: "Ph"})
aco = s.molecule("CC(=O)[O-]", coords=[(-3.6, 1.2), (-3.1, 2.07), (-3.6, 2.94), (-2.1, 2.07)], at=(0, y), lone_pairs=[3])
s.curly(aco.atom(3), ac.atom(0), bend=-0.4)
s.curly(ac.bond(0, 1), ac.bond(1, 4), bend=0.7)
s.curly(ac.bond(4, 6), ac.atom(6), bend=-0.6)
s.arrow((4.0, y), (5.6, y), above="$-$AcOH, $-$AcO$^-$")
x = 7.4
s.molecule("C=[S+]*", coords=[(-0.5, 0.87), (0, 0), (1.0, 0)], at=(x, y), labels={2: "Ph"})
s.text((x + 0.2, y - 1.0), "thionium ion", size=11)

y2 = -8.6
th = s.molecule("C=[S+]*", coords=[(-0.5, 0.87), (0, 0), (1.0, 0)], at=(1.4, y2), labels={2: "Ph"})
aco2 = s.molecule("CC(=O)[O-]", coords=[(-2.6, 0.0), (-2.1, 0.87), (-2.6, 1.73), (-1.1, 0.87)], at=(0, y2), lone_pairs=[3])
s.curly(aco2.atom(3), th.atom(0), bend=-0.4)
s.curly(th.bond(0, 1), th.atom(1), bend=-0.6)
s.arrow((3.2, y2), (4.6, y2))
s.molecule("CC(=O)OCS*", coords=[(0, 0), (0.5, 0.87), (0, 1.73), (1.5, 0.87), (2.0, 0), (3.0, 0), (3.5, 0.87)], at=(7.4, y2),
           labels={6: "Ph"})
s.draw()
