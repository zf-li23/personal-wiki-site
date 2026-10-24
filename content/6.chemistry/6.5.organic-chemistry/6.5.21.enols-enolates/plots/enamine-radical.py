"""Radical step of the enamine-photoredox alpha-alkylation of aldehydes (Nicewicz and MacMillan,
2008). The electron-poor diethyl malonyl radical, made by one-electron reduction of diethyl
bromomalonate, adds to the electron-rich C=C of the chiral enamine: one electron of the pi bond pairs
with the radical to form the new C-C bond and the other stays on the carbon next to nitrogen. The
alpha-amino radical is oxidised by one electron to the iminium ion, which is hydrolysed to the
alkylated aldehyde and the amine catalyst. R2N: the imidazolidinone catalyst."""

from wikichem import Scheme

s = Scheme()
en = s.molecule("CC=CN(*)*", coords=[(0, 0), (0.87, 0.5), (1.73, 0), (2.6, 0.5), (3.46, 0), (2.6, 1.5)],
                at=(-1.3, -1.0), labels={4: "R", 5: "R"})
rad = s.molecule("[CH](C(=O)OCC)C(=O)OCC", at=(en.xy(1)[0], en.xy(1)[1] + 2.4))
mid = (rad.xy(0) + en.xy(1)) / 2
s.curly(rad.atom(0), mid, bend=-0.4, single=True)
s.curly(en.bond(1, 2), mid, bend=0.4, single=True)
s.curly(en.bond(1, 2), en.atom(2), bend=0.8, single=True)
s.text((0.0, -2.0), "chiral enamine")
s.arrow((2.8, 0), (4.2, 0))
s.molecule("CC(C(C(=O)OCC)C(=O)OCC)[CH]N(*)*", at=(7.2, 0), labels={15: "R", 16: "R"})
s.text((7.2, -2.4), r"$\alpha$-amino radical")
s.arrow((9.6, 0), (11.0, 0), above=r"$-$e$^-$")
s.molecule("CC(C(C(=O)OCC)C(=O)OCC)C=[N+](*)*", at=(14.0, 0.4), labels={15: "R", 16: "R"})
s.text((14.0, -3.2), "iminium ion")
s.draw()
