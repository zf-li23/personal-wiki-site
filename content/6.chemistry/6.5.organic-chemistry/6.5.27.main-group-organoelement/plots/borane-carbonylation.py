"""Carbonylation of a trialkylborane, first step. The carbon lone pair of carbon monoxide fills the
empty p orbital of boron, giving a borate 'ate' complex; an ethyl group then migrates with its
bonding electrons from the negatively charged boron to the electron-poor carbonyl carbon (a
1,2-metallate shift, with retention of configuration at the migrating carbon), and the C=O pi
electrons move onto oxygen. Further migrations and the oxidative work-up give aldehydes, ketones or
tertiary alcohols."""

from wikichem import Scheme

s = Scheme()
b = s.molecule("CCB(CC)CC", coords=[(-1.87, 0.5), (-1.0, 0), (0, 0), (0.5, 0.87), (1.5, 0.87), (0.5, -0.87), (1.5, -0.87)])
co = s.molecule("[C-]#[O+]", coords=[(-0.3, -2.4), (0.7, -2.4)], lone_pairs=[0])
s.curly(co.atom(0), b.atom(2), bend=-0.4)
s.arrow((2.6, 0), (4.0, 0))
x = 6.6
ate = s.molecule("CC[B-](CC)(CC)C#[O+]",
                 coords=[(-1.87, 0.5), (-1.0, 0), (0, 0), (0.5, 0.87), (1.5, 0.87), (0.0, -1.0), (-0.87, -1.5), (1.0, 0), (2.0, 0)],
                 at=(x, 0))
s.curly(ate.bond(2, 3), ate.bond(2, 7), bend=-0.6)
s.curly(ate.bond(7, 8), ate.atom(8), bend=-0.6)
s.arrow((x + 3.0, 0), (x + 4.4, 0), above="1,2-shift")
s.molecule("CCB(CC)C(=O)CC",
           coords=[(-1.87, 0.5), (-1.0, 0), (0, 0), (0.0, -1.0), (-0.87, -1.5), (1.0, 0), (1.5, -0.87), (1.5, 0.87), (2.5, 0.87)],
           at=(x + 6.6, 0))
s.draw()
