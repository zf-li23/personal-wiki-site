"""Hyperconjugation in curved-arrow language. (a) sigma-p hyperconjugation in the ethyl cation, written
as "no-bond resonance": the electrons of a C-H bond next to the cationic carbon move into the C-C
region, so in the minor structure the proton is detached and a C=C bond has formed. (b) Negative
hyperconjugation in chloromethyl methyl ether: an oxygen lone pair moves into the C-Cl sigma* orbital,
written as the structure with an O=C double bond and a chloride ion. Neither minor structure is a real
species; they show where the electron density goes."""

from wikichem import Scheme

s = Scheme()
y = 0.0
s.text((-2.4, y), "(a)")
c = s.molecule("C[CH2+]", at=(0, y), show_h=[0])
s.curly(c.bond(0, 2), c.bond(0, 1), bend=0.7)
s.arrow((1.6, y), (2.6, y), kind="resonance")
dx = 4.2
pts = [tuple(c.xy(k)) for k in (3, 0, 4, 1)]
s.molecule("[H]C([H])=C", coords=pts, at=(dx, 0))
hx, hy = c.xy(2)
s.text((hx + dx, hy), r"H$^+$")

y = -3.4
s.text((-2.4, y), "(b)")
e = s.molecule("COCCl", at=(0, y), lone_pairs=[1, 3])
s.curly(e.atom(1), e.bond(1, 2), bend=-0.7)
s.curly(e.bond(2, 3), e.atom(3), bend=-0.7)
s.arrow((2.0, y), (3.0, y), kind="resonance")
s.molecule("C[O+]=C", at=(4.6, y), lone_pairs=[1])
s.molecule("[Cl-]", at=(6.4, y), lone_pairs=True)
s.draw()
