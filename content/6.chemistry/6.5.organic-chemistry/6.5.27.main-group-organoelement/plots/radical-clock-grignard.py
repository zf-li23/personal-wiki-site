"""Evidence for radicals in Grignard formation: 6-bromohex-1-ene. Single-electron transfer from the
magnesium surface into the C-Br sigma* orbital gives a radical anion that loses bromide; the
hex-5-enyl radical is partly trapped by the surface as hex-5-enylmagnesium bromide, but part of it
cyclizes first (5-exo-trig, k about 2e5 s-1 at 25 C): the radical electron and one pi electron
form the new C-C bond while the other pi electron moves to the terminal carbon. The
cyclopentylmethyl radical then gives cyclopentylmethylmagnesium bromide."""

from wikichem import Scheme

s = Scheme()
s.molecule("C=CCCCCBr", at=(0, 0))
s.arrow((2.8, 0), (4.4, 0), above="Mg (SET)", below="$-$Br$^-$")
x = 6.8
PENT = [(0, 0.85), (0.81, 0.26), (0.5, -0.69), (-0.5, -0.69), (-0.81, 0.26)]
r = s.molecule("[CH2]CCCC=C", coords=[(0, 1.0), (-0.95, 0.31), (-0.59, -0.81), (0.59, -0.81), (0.95, 0.31), (1.9, 0.9)], at=(x, 0))
gap = r.bond(0, 4)
s.partial(r.atom(0), r.atom(4))
s.curly(r.atom(0), gap, bend=0.5, single=True)
s.curly(r.bond(4, 5), gap, bend=-0.6, single=True)
s.curly(r.bond(4, 5), r.atom(5), bend=-0.6, single=True)
s.text((x + 0.3, -1.6), "hex-5-enyl radical (forming bond dashed)", size=11)
s.arrow((x + 2.8, 0), (x + 4.2, 0), above="5-exo")
s.molecule("[CH2]C1CCCC1", at=(x + 6.0, 0))
s.arrow((x + 7.8, 0), (x + 9.2, 0), above="Mg surface")
s.molecule("Br[Mg]CC1CCCC1", at=(x + 11.4, 0))
s.draw()
