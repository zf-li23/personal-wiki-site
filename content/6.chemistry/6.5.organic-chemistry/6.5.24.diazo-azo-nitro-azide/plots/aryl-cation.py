"""Hydrolysis of an arenediazonium salt to a phenol (SN1-type). On warming in aqueous sulfuric acid
the C-N bond breaks, N2 leaves with the bonding electrons, and an aryl cation is formed (slow step;
the empty orbital is an sp2 orbital in the ring plane, so the cation is very unstable). Water, the
only nucleophile present (HSO4- is even weaker), captures it at once, and loss of a proton gives
4-methylphenol."""

from wikichem import Scheme

s = Scheme()
d = s.molecule("Cc1ccc(cc1)[N+]#N", at=(0, 0))
s.curly(d.bond(4, 7), d.atom(7), bend=0.6)
s.arrow((2.8, 0), (4.2, 0), above="slow", below=r"$-$N$_2$")
ac = s.molecule("Cc1cc[c+]cc1", at=(5.8, 0))
w = s.molecule("O", at=(ac.xy(4)[0] + 1.6, ac.xy(4)[1] + 0.2), lone_pairs=True)
s.curly(w.atom(0), ac.atom(4), bend=0.4)
s.text((5.8, -1.8), "aryl cation")
s.arrow((8.4, 0), (9.8, 0), below=r"$-$H$^+$")
s.molecule("Cc1ccc(O)cc1", at=(11.6, 0))
s.draw()
