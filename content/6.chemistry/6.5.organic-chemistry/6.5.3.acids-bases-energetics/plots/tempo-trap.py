"""Trapping a radical intermediate with TEMPO. The persistent nitroxide radical
(2,2,6,6-tetramethylpiperidin-1-yloxyl) does not abstract hydrogen or start chains, but couples
with a carbon radical almost at the diffusion limit: one electron from each radical (fishhook
arrows) forms the new C-O bond of an alkoxyamine, which can be isolated and identified."""

from wikichem import Scheme

s = Scheme()
t = s.molecule("CC1(C)CCCC(C)(C)N1[O]", at=(0, 0), rotate=90)
b = s.molecule("[CH2]c1ccccc1", at=(3.6, 1.2))
mid = (t.xy(10) + b.xy(0)) / 2
s.curly(t.atom(10), mid, bend=-0.6, single=True)
s.curly(b.atom(0), mid, bend=0.6, single=True)
s.text((0, -2.4), "TEMPO")
s.text((3.8, -0.9), "benzyl radical")
s.arrow((5.6, 0), (6.8, 0))
s.molecule("CC1(C)CCCC(C)(C)N1OCc1ccccc1", at=(10.2, 0))
s.text((10.2, -2.4), "alkoxyamine (isolable)")
s.draw()
