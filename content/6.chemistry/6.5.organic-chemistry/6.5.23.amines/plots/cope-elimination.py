"""Cope elimination of N,N-dimethylbutan-2-amine N-oxide. The negatively charged oxygen of the amine
oxide removes a beta hydrogen on the same side of the C-N bond, through a planar five-membered
cyclic transition state: the C-H electrons form the C=C bond and the C-N bond breaks onto nitrogen
(syn elimination, Ei mechanism, no external base). As in the Hofmann elimination the less
substituted alkene, but-1-ene, is the main product; the other product is N,N-dimethylhydroxylamine."""

from wikichem import Scheme

s = Scheme()
# atoms: 0 H, 1 C1 (beta), 2 C2 (alpha), 3 C3, 4 C4, 5 N, 6 Me, 7 Me, 8 O
xy = [(0, 1.0), (0.95, 0.31), (0.59, -0.81), (1.3, -1.52), (2.3, -1.45), (-0.59, -0.81), (-0.9, -1.76),
      (-1.55, -0.5), (-0.95, 0.31)]
ox = s.molecule("[H]CC(CC)[N+](C)(C)[O-]", coords=xy, at=(0, 0), lone_pairs=[8])
s.partial(ox.atom(8), ox.atom(0))
s.curly(ox.atom(8), ox.atom(0), bend=-0.4)
s.curly(ox.bond(0, 1), ox.bond(1, 2), bend=-0.6)
s.curly(ox.bond(2, 5), ox.atom(5), bend=-0.5)
s.text((0.3, -2.6), "five-membered cyclic TS (syn)")
s.arrow((3.0, 0), (4.4, 0), above=r"120 $^\circ$C")
s.molecule("C=CCC", at=(5.8, 0))
s.plus((7.2, 0))
s.molecule("CN(C)O", at=(8.4, 0))
s.draw()
