"""Menshutkin reaction: triethylamine and iodomethane give a quaternary ammonium salt by SN2. The
nitrogen lone pair attacks the methyl carbon from the side opposite to iodine. In the transition
state (centre) the N...C bond is partly formed and the C...I bond partly broken, the three methyl
hydrogens lie in one plane, and charge has already separated (partial plus on N, partial minus on
I). Because two neutral molecules become an ion pair, polar solvents stabilise the transition state
strongly and speed the reaction up."""

from wikichem import Scheme

s = Scheme()
ET3N = [(0, 1.73), (-0.5, 0.87), (0, 0), (-1.0, 0), (-1.87, 0.5), (-0.5, -0.87), (0, -1.73)]
am = s.molecule("CCN(CC)CC", coords=ET3N, at=(0, 0), lone_pairs=[2])
mi = s.molecule("CI", at=(2.2, 0), lone_pairs=[1])
s.curly(am.atom(2), mi.atom(0), bend=-0.3)
s.curly(mi.bond(0, 1), mi.atom(1), bend=-0.6)
s.arrow((3.6, 0), (4.8, 0))
# transition state: Et3N ... CH3 ... I in a line, the methyl flattened
cx = 8.6
ts = s.molecule("CCN(CC)CC", coords=ET3N, at=(cx - 1.6, 0))
ny = ts.xy(2)[1]
me = s.molecule("[H]C([H])[H]", coords=[(0.0, 0.95), (0.0, 0.0), (-0.35, -0.85), (0.45, -0.7)], at=(cx, ny),
                labels={1: "C"})
iod = s.molecule("*", at=(cx + 1.6, ny), labels={0: "I"})
s.partial(ts.atom(2), me.atom(1))
s.partial(me.atom(1), iod.atom(0))
s.label(ts.atom(2), r"$\delta+$", angle=110, dist=0.55)
s.label(iod.atom(0), r"$\delta-$", angle=70, dist=0.55)
s.text((cx, ny - 2.0), "transition state")
s.arrow((cx + 2.6, 0), (cx + 3.8, 0))
s.molecule("CC[N+](CC)(CC)C", at=(cx + 5.4, 0))
s.molecule("[I-]", at=(cx + 8.0, 0), lone_pairs=True)
s.draw()
