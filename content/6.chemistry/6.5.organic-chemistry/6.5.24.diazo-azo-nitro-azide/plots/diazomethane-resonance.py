"""Resonance structures of diazomethane. Moving the terminal nitrogen lone pair into the N-N bond
and the C=N pi electrons onto carbon converts CH2=N(+)=N(-) into CH2(-)-N(+)#N. The second structure
shows why the carbon is nucleophilic and basic (it takes a proton from carboxylic acids, or adds to
an acyl chloride), and why N2 is the leaving group once the carbon has bonded."""

from wikichem import Scheme

s = Scheme()
a = s.molecule("C=[N+]=[N-]", at=(0, 0), lone_pairs=[2])
s.curly(a.atom(2), a.bond(1, 2), bend=0.7)
s.curly(a.bond(0, 1), a.atom(0), bend=0.7)
s.arrow((1.6, 0), (2.8, 0), kind="resonance")
s.molecule("[CH2-][N+]#N", at=(4.4, 0), like=a, lone_pairs=[0])
s.text((4.4, -1.7), "nucleophilic carbon")
s.draw()
