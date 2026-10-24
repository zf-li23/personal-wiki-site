"""N-Nitrosation of a secondary amine. The lone pair of dimethylamine attacks the nitrogen of the
nitrosonium ion and one pi bond of N=O moves onto oxygen; loss of a proton from the N-nitrosoammonium
ion gives N-nitrosodimethylamine (NDMA). With no second N-H, the reaction cannot go on to a diazonium
ion, as it does for primary amines."""

from wikichem import Scheme

s = Scheme()
am = s.molecule("CNC", at=(0, 0), lone_pairs=[1])
no = s.molecule("N#[O+]", at=(2.0, 1.0), lone_pairs=[0, 1])
s.curly(am.atom(1), no.atom(0), bend=-0.4)
s.curly(no.bond(0, 1), no.atom(1), bend=-0.6)
s.text((1.0, -1.4), r"NO$^+$ from HONO + H$^+$")
s.arrow((3.4, 0), (4.8, 0))
s.molecule("C[NH+](C)N=O", at=(6.2, 0))
s.arrow((7.6, 0), (9.0, 0), above=r"$-$H$^+$")
s.molecule("CN(C)N=O", at=(10.9, 0))
s.text((10.9, -1.4), "NDMA")
s.draw()
