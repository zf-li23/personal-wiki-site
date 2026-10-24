"""Minisci reaction. The tert-butyl radical (from pivalic acid by silver-catalysed oxidative
decarboxylation) adds to C2 of protonated 4-methylquinoline: one electron of the C2=N pi bond pairs
with the radical electron, the other stays on nitrogen (aminium radical cation). Oxidation and loss
of protons restore the aromatic ring, giving 2-tert-butyl-4-methylquinoline."""

from wikichem import Scheme

s = Scheme()
q = s.molecule("CC1=C[CH:2]=[NH+:1]c2ccccc12", at=(0, 0), rotate=90)
r = s.molecule("[C:9](C)(C)C", at=(q.xy(2)[0] + 0.6, q.xy(2)[1] + 2.2))
meet = (q.xy(2) + r.xy(9)) / 2
s.curly(r.atom(9), meet, bend=-0.5, single=True)
s.curly(q.bond(2, 1), meet, bend=0.6, single=True)
s.curly(q.bond(2, 1), q.atom(1), bend=-0.7, single=True)
s.arrow((2.4, 0), (3.8, 0))
s.molecule("CC1=C[CH:2]([C:9](C)(C)C)[NH+:1]c2ccccc12", at=(6.2, 0), rotate=90)
s.arrow((8.6, 0), (10.0, 0), above=r"$-\mathrm{e^-}$", below=r"$-2\,\mathrm{H^+}$")
s.molecule("Cc1cc(nc2ccccc12)C(C)(C)C", at=(12.4, 0), rotate=90)
s.draw()
