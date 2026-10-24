"""Hofmann rearrangement of propanamide. Top row: bromine in base brominates the nitrogen; the
remaining N-H of the N-bromoamide is now acidic and is removed. The key step is concerted: the
nitrogen lone pair forms the C=N bond, the ethyl group migrates from carbon to nitrogen with its
bonding pair (retaining its configuration), and bromide leaves. Bottom row: hydroxide adds to the
isocyanate; the carbamate is protonated to the carbamic acid, which loses CO2 to give ethylamine,
one carbon shorter than the amide."""

from wikichem import Scheme

s = Scheme()
y1, y2 = 0.0, -4.4  # the two rows
s.molecule("CCC(N)=O", at=(0, y1))
s.text((0, y1 - 1.9), "propanamide")
s.arrow((1.5, y1), (3.1, y1), above=r"Br$_2$, HO$^-$")
s.molecule("CCC(=O)NBr", at=(5.0, y1))
s.text((5.0, y1 - 1.6), "N-bromoamide")
s.arrow((7.0, y1), (8.4, y1), kind="equilibrium", above=r"HO$^-$")
an = s.molecule("CCC(=O)[N-]Br", at=(10.4, y1), lone_pairs=[4])
s.curly(an.atom(4), an.bond(2, 4), bend=0.7)
s.curly(an.bond(1, 2), an.atom(4), bend=-0.6)
s.curly(an.bond(4, 5), an.atom(5), bend=0.8)
s.arrow((12.4, y1), (13.8, y1), below=r"$-\mathrm{Br}^-$")
s.molecule("CCN=C=O", at=(15.4, y1), show_carbons=[3])
s.text((15.4, y1 - 1.6), "ethyl isocyanate")

oh = s.molecule("[OH-]", at=(-0.4, y2 + 1.3), lone_pairs=True)
iso = s.molecule("CCN=C=O", at=(1.6, y2), show_carbons=[3], lone_pairs=[2])
s.curly(oh.atom(0), iso.atom(3), bend=0.4)
s.curly(iso.bond(2, 3), iso.atom(2), bend=0.8)
s.arrow((3.4, y2), (4.8, y2))
s.molecule("CCNC(=O)[O-]", at=(6.4, y2))
s.text((6.4, y2 - 1.6), "carbamate")
s.arrow((8.0, y2), (9.4, y2), above=r"H$^+$")
s.molecule("CCNC(=O)O", at=(11.0, y2))
s.text((11.0, y2 - 1.6), "carbamic acid")
s.arrow((13.0, y2), (14.6, y2), below=r"$-\mathrm{CO_2}$")
s.molecule("CCN", at=(15.9, y2))
s.text((15.9, y2 - 1.6), "ethylamine")
s.draw()
