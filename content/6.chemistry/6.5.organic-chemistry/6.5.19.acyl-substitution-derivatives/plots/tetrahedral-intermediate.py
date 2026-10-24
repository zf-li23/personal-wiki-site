"""Nucleophilic acyl substitution by addition-elimination: alkaline hydrolysis of methyl acetate
(BAc2). Hydroxide adds to the carbonyl carbon and the C=O pi bond moves onto oxygen, giving the
tetrahedral intermediate. The alkoxide oxygen pushes back down, expelling methoxide. The final
proton transfer from acetic acid (pKa 4.76) to methoxide (conjugate acid pKa 15.5) is downhill by
about eleven pKa units and makes the overall reaction irreversible."""

from wikichem import Scheme

s = Scheme()
y = -1.9  # caption line
oh = s.molecule("[OH-]", at=(-2.2, 1.1), lone_pairs=True)
ester = s.molecule("CC(=O)OC", at=(0, 0), lone_pairs=[2])
s.curly(oh.atom(0), ester.atom(1), bend=0.4)
s.curly(ester.bond(1, 2), ester.atom(2), bend=-0.8)
s.text((-0.6, y), "methyl acetate")
s.arrow((1.8, 0), (3.2, 0), kind="equilibrium", above="slow")
ti = s.molecule("CC([O-])(O)OC", at=(5.0, 0), lone_pairs=[2])
s.curly(ti.atom(2), ti.bond(1, 2), bend=0.7)
s.curly(ti.bond(1, 4), ti.atom(4), bend=-0.6)
s.text((5.0, y), "tetrahedral intermediate")
s.arrow((6.9, 0), (8.3, 0), kind="equilibrium")
s.molecule("CC(=O)O", at=(9.3, 0))
s.plus((10.4, 0))
s.molecule("C[O-]", at=(11.3, 0))
s.arrow((12.3, 0), (14.1, 0), above="fast", below="proton transfer")
s.molecule("CC(=O)[O-]", at=(15.4, 0))
s.plus((16.6, 0))
s.molecule("CO", at=(17.6, 0))
s.text((16.5, y), "acetate + methanol")
s.draw()
