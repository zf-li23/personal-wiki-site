"""Deoxyfluorination of (S)-octan-2-ol with DAST (Et2N-SF3; the hexyl group written C6H13). Top: the
alcohol oxygen attacks sulfur and fluoride is displaced; loss of HF gives an alkoxyaminosulfur
difluoride, in which the OH has become a good leaving group. Bottom: fluoride attacks the carbinol
carbon from the back (SN2), so (R)-2-fluorooctane forms with inversion and Et2N-S(=O)F leaves.
Carbocation-prone substrates can instead rearrange or eliminate."""

from wikichem import Scheme

s = Scheme()
AL = [(0, -1.0), (0, 0), (-0.87, 0.5), (-0.87, 1.5), (0.87, 0.5)]
alc = s.molecule("C[C@H](O[H])*", coords=AL, at=(0, 0), lone_pairs=[2], labels={4: "C$_6$H$_{13}$"})
dast = s.molecule("*S(F)(F)F", coords=[(-2.4, -0.3), (-2.4, 0.8), (-2.4, 1.8), (-3.3, 1.3), (-3.5, 0.6)], at=(0, 0),
                  lone_pairs=[4], labels={0: "Et$_2$N"})
s.curly(alc.atom(2), dast.atom(1), bend=0.4)
s.curly(dast.bond(1, 4), dast.atom(4), bend=-0.6)
s.arrow((1.8, 0), (3.2, 0), above="$-$HF")
x = 6.2
OS = [(0, -1.0), (0, 0), (-0.87, 0.5), (-1.87, 0.5), (-2.37, 1.37), (-2.37, -0.37), (-2.87, 0.5), (0.87, 0.5)]
s.molecule("C[C@H](OS(F)(F)*)*", coords=OS, at=(x, 0), labels={6: "NEt$_2$", 7: "C$_6$H$_{13}$"})

y = -4.4
os_ = s.molecule("C[C@H](OS(F)(F)*)*", coords=OS, at=(0.8, y), labels={6: "NEt$_2$", 7: "C$_6$H$_{13}$"})
f = s.molecule("[F-]", at=(2.4, y - 0.9), lone_pairs=True)
s.curly(f.atom(0), os_.atom(1), bend=-0.5)
s.curly(os_.bond(1, 2), os_.atom(2), bend=0.6)
s.arrow((3.6, y), (5.0, y), above="SN2")
s.molecule("C[C@@H](F)*", coords=[(0, -1.0), (0, 0), (-0.87, 0.5), (0.87, 0.5)], at=(6.6, y), labels={3: "C$_6$H$_{13}$"})
s.plus((8.6, y))
s.molecule("O=S(F)*", coords=[(0, 1.0), (0, 0), (-0.87, -0.5), (0.87, -0.5)], at=(9.8, y), labels={3: "NEt$_2$"})
s.draw()
