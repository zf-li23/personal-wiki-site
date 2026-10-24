"""Why the two methyl groups of N,N-dimethylformamide give two 1H NMR signals at room temperature.
The nitrogen lone pair is delocalised into the carbonyl group, so the C-N bond has partial double-bond
character and the molecule is planar; one methyl group is cis to oxygen and the other trans. Rotation
about C-N exchanges them, but its barrier (about 87 kJ/mol) makes the exchange slow on the NMR time
scale until the sample is heated well above 100 C."""

from wikichem import Scheme

s = Scheme()
# atoms: 1 O, 2 C, 3 N, 4 CH3 (cis to O), 5 CH3 (trans to O)
a = s.molecule("[O:1]=[CH:2][N:3]([CH3:4])[CH3:5]", at=(0, 0), lone_pairs=[1, 3])
s.curly(a.atom(3), a.bond(2, 3), bend=-0.6)
s.curly(a.bond(1, 2), a.atom(1), bend=-0.7)
s.label(a.atom(4), "a", angle=0, dist=0.4)
s.label(a.atom(5), "b", angle=90, dist=0.4)
s.arrow((1.9, 0), (3.3, 0), kind="resonance")
b = s.molecule("[O-:1][CH:2]=[N+:3]([CH3:4])[CH3:5]", at=(5.2, 0), like=a, lone_pairs=[1])
s.label(b.atom(4), "a", angle=0, dist=0.4)
s.label(b.atom(5), "b", angle=90, dist=0.4)
s.text((2.6, -2.0), "Me$^{a}$ and Me$^{b}$ exchange only by C-N rotation, $\\Delta G^{\\ddagger} \\approx 87$ kJ/mol", size=11)
s.draw()
