"""Meinwald rearrangement of trans-stilbene oxide with BF3. The Lewis acid binds the epoxide oxygen
and one C-O bond breaks, giving a benzylic cation next to a carbon that carries the O-BF3 group. A
phenyl group on that carbon migrates with its electron pair to the cationic carbon, the oxygen lone
pair forms the C=O bond and BF3 is released: the product is diphenylacetaldehyde (aryl migrates in
preference to H)."""

from wikichem import Scheme

s = Scheme(scale=0.4)
y = 0.0
e = s.molecule("F[B-](F)(F)[O+]1C(c2ccccc2)C1c1ccccc1", at=(0.0, y))
s.curly(e.bond(4, 12), e.atom(4), bend=-0.5)
s.text((0.0, y - 3.0), r"epoxide-BF$_3$ complex")
s.arrow((3.4, y), (4.8, y))
c = s.molecule("F[B-](F)(F)OC(c1ccccc1)[CH+]c1ccccc1", at=(8.2, y), lone_pairs=[4])
s.curly(c.bond(5, 6), c.atom(12), bend=-0.6)
s.curly(c.atom(4), c.bond(4, 5), bend=0.6)
s.curly(c.bond(1, 4), c.atom(1), bend=-0.9)
s.text((8.2, y - 3.0), "benzylic cation")
s.arrow((11.6, y), (13.0, y), above="1,2-Ph shift", below=r"$-\,\mathrm{BF_3}$")
s.molecule("O=CC(c1ccccc1)c1ccccc1", at=(15.4, y))
s.text((15.4, y - 3.0), "diphenylacetaldehyde")
s.draw()
