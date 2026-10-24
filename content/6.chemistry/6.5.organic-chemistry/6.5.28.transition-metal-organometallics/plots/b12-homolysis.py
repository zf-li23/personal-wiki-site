"""Radical chemistry of coenzyme B12 (adenosylcobalamin; the cobalt sits in the corrin ring, not drawn, Ado =
the rest of 5'-deoxyadenosine). Top: the weak Co-C bond (about 130 kJ/mol) breaks homolytically
in the enzyme, one electron going to each atom: cob(II)alamin and the 5'-deoxyadenosyl radical.
Bottom: the primary radical abstracts a hydrogen atom from the substrate (here a C-H of
methylmalonyl-CoA, written R-H), giving 5'-deoxyadenosine and a substrate radical that undergoes
the skeletal rearrangement."""

from wikichem import Scheme

s = Scheme()
s.text((0, 0), "Co$^{\\mathrm{III}}$", size=13)
s.text((2.6, 0), "CH$_2$Ado", size=13)
s.curly((1.15, 0.0), (0.7, 0.5), bend=-0.6, single=True)
s.curly((1.15, 0.0), (1.6, 0.5), bend=0.6, single=True)
s.arrow((4.8, 0), (6.2, 0), above="enzyme")
s.text((7.6, 0), "Co$^{\\mathrm{II}}\\cdot$", size=13)
s.plus((9.0, 0))
s.molecule("[CH2]*", coords=[(0, 0), (0.9, 0.5)], at=(10.2, 0), labels={1: "Ado"}, show_carbons=[0])

y = -3.0
r = s.molecule("[CH2]*", coords=[(0, 0), (-0.9, 0.5)], at=(0, y), labels={1: "Ado"}, show_carbons=[0])
sub = s.molecule("[H]*", coords=[(2.0, 0), (3.0, 0)], at=(0, y), labels={1: "R"})
mid = (1.0, y)
s.curly(r.atom(0), mid, bend=-0.6, single=True)
s.curly(sub.bond(0, 1), mid, bend=0.7, single=True)
s.curly(sub.bond(0, 1), sub.atom(1), bend=-0.7, single=True)
s.arrow((3.8, y), (5.2, y))
s.molecule("*C", coords=[(0, 0.5), (0.9, 0)], at=(6.2, y), labels={0: "Ado"}, show_carbons=[1])
s.plus((8.4, y))
s.text((9.3, y), "R$\\cdot$", size=13)
fig, ax = s.draw()
ax.plot([0.6, 1.7], [0.0, 0.0], color="k", lw=1.4)  # the Co-C bond
