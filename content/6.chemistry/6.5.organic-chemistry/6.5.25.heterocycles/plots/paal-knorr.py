"""Paal-Knorr pyrrole synthesis from hexane-2,5-dione and methylamine. Top: the amine adds to one
carbonyl group and proton transfer gives the hemiaminal. Bottom: the hemiaminal nitrogen attacks the
second carbonyl group (ring closure, rate-determining), giving a 2,5-dihydroxypyrrolidine that loses
two molecules of water to give 1,2,5-trimethylpyrrole."""

from wikichem import Scheme

s = Scheme()
dk = s.molecule("C[C:2](=[O:7])CCC(C)=O", at=(0, 0))
me = s.molecule("C[NH2:1]", at=(dk.xy(2)[0] - 0.3, dk.xy(2)[1] - 2.0), lone_pairs=[1])
s.curly(me.atom(1), dk.atom(2), bend=0.3)
s.curly(dk.bond(2, 7), dk.atom(7), bend=0.6)
s.arrow((3.0, 0), (4.4, 0), kind="equilibrium", above="proton", below="transfer")
s.molecule("CC(O)(NC)CCC(C)=O", at=(7.8, 0))
s.draw()

s = Scheme()
h = s.molecule("C[C:2]([OH:7])([NH:1]C)[CH2:3][CH2:4][C:5](C)=[O:6]", at=(0, 0), lone_pairs=[1],
               coords=[(-1.75, 0.1), (-0.81, -0.26), (-1.3, -1.1), (0.0, -0.85), (0.0, -1.85),
                       (-0.5, 0.69), (0.5, 0.69), (0.81, -0.26), (1.75, 0.1), (1.3, -1.1)])
s.curly(h.atom(1), h.atom(5), bend=-0.5)
s.curly(h.bond(5, 6), h.atom(6), bend=-0.6)
s.arrow((2.4, 0), (3.8, 0), above="ring closure")
s.molecule("CC1(O)CCC(C)(O)N1C", at=(5.6, 0))
s.arrow((7.9, 0), (9.3, 0), below=r"$-2\,\mathrm{H_2O}$")
s.molecule("Cc1ccc(C)n1C", at=(11.0, 0))
s.draw()
