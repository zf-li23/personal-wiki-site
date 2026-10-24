"""Ring opening of a nitrospiropyran (1',3',3'-trimethyl-6-nitrospiro[chromene-2,2'-indoline]) by
light or by mechanical force. The spiro C-O bond breaks heterolytically: the C-O electron pair goes
to the phenolate oxygen while the indoline nitrogen lone pair forms a C=N+ bond. After cis-trans
isomerization of the central double bond the planar, conjugated merocyanine zwitterion is coloured;
heat or visible light closes the ring again."""

from wikichem import Scheme

s = Scheme()
y = 0.0
sp = s.molecule("CN1c2ccccc2C(C)(C)C13Oc1ccc(cc1C=C3)[N+](=O)[O-]", at=(0.0, y), lone_pairs=[1])
s.curly(sp.bond(11, 12), sp.atom(12), bend=0.6)
s.curly(sp.atom(1), sp.bond(1, 11), bend=0.6)
s.text((0.0, y - 5.2), "spiropyran (colourless)")
s.arrow((3.6, y), (5.2, y), above=r"$h\nu$ or force", below=r"heat, $h\nu'$", kind="equilibrium")
s.molecule("C[N+]1=C(/C=C/c2cc([N+](=O)[O-])ccc2[O-])C(C)(C)c2ccccc21", at=(10.0, y))
s.text((10.0, y - 5.2), "merocyanine (coloured)")
s.draw()
