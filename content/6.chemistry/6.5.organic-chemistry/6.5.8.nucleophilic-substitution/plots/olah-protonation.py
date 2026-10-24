"""Preparing a persistent carbocation (Olah). In superacid the C=C pi electrons of isobutene take a
proton, which bonds to the CH2 end, so that the positive charge sits on the tertiary carbon; the very
weakly nucleophilic SbF6- (or FSO3SbF5-) counterion does not capture the tert-butyl cation."""

from wikichem import Scheme

s = Scheme()
ib = s.molecule("C=C(C)C", coords=[(0, 0.65), (0, -0.65), (-1.1, -1.3), (1.1, -1.3)])
ha = s.molecule("[H]*", coords=[(1.9, 0.9), (3.2, 0.9)], labels={1: "A"})
s.curly(ib.bond(0, 1), ha.atom(0), bend=-0.6)
s.curly(ha.bond(0, 1), ha.xy(1) + (0.2, -0.35), bend=-0.8)
s.text((1.6, -2.2), r"HA = HF$\cdot$SbF$_5$ or FSO$_3$H$\cdot$SbF$_5$, $-70\,^\circ$C, SO$_2$ClF", size=9)
s.arrow((4.2, -0.2), (5.6, -0.2))
s.molecule("C[C+](C)C", at=(6.9, -0.2))
s.plus((8.2, -0.2))
s.text((9.2, -0.2), r"SbF$_6^-$")
s.text((6.9, -1.5), r"$^{13}$C: $\delta$ 335", size=10)
s.draw()
