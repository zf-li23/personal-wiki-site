"""Chichibabin reaction. Top: the amide ion adds to C2 of pyridine and the C2=N pi electrons move onto
nitrogen; the nitrogen lone pair then re-forms the C=N bond and the C2-H bonding pair leaves as a
hydride ion. Bottom: the hydride removes a proton from the amino group, releasing H2 and driving the
reaction; aqueous work-up gives 2-aminopyridine."""

from wikichem import Scheme

s = Scheme()
py = s.molecule("[CH:2]1=[N:1][CH:6]=[CH:5][CH:4]=[CH:3]1", at=(0, 0), rotate=-30)
nh2 = s.molecule("[NH2-:9]", at=(py.xy(2)[0] - 0.7, py.xy(2)[1] + 1.8), lone_pairs=True)
s.curly(nh2.atom(9), py.atom(2), bend=0.3)
s.curly(py.bond(2, 1), py.atom(1), bend=0.9)
s.arrow((2.0, 0), (3.2, 0))
ad = s.molecule("[CH:2]1([NH2:7])[N-:1][CH:6]=[CH:5][CH:4]=[CH:3]1", at=(5.4, 0), lone_pairs=[1], show_h=[2])
s.curly(ad.atom(1), ad.bond(1, 2), bend=0.8)
h = ad.h(2)
s.curly((h.xy + ad.xy(2)) / 2, h, bend=-0.8)
s.arrow((7.6, 0), (8.8, 0))
s.molecule("Nc1ccccn1", at=(10.6, 0))
s.plus((12.4, 0))
s.text((13.2, 0), r"$\mathrm{H^-}$")
s.draw()

s = Scheme()
ap = s.molecule("[NH2:7]c1ccccn1", at=(0, 0), show_h=[7])
hpos = ap.h(7, 0).xy + (-1.5, 0.5)
s.text(hpos, r"$\mathrm{H^-}$")
s.curly(hpos + (0.3, 0.0), ap.h(7, 0), bend=-0.4)
s.curly((ap.h(7, 0).xy + ap.xy(7)) / 2, ap.atom(7), bend=0.8)
s.arrow((2.2, 0), (3.4, 0))
s.molecule("[NH-]c1ccccn1", at=(5.2, 0))
s.plus((7.0, 0))
s.molecule("[H][H]", at=(7.9, 0), coords=[(-0.5, 0.0), (0.5, 0.0)])
s.arrow((9.0, 0), (10.2, 0), above=r"$\mathrm{H_2O}$")
s.molecule("Nc1ccccn1", at=(12.0, 0))
s.draw()
