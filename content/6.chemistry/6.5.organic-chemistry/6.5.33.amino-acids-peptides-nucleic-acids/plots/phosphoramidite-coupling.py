"""The coupling step of phosphoramidite oligonucleotide synthesis (abbreviations: R'O is the
3'-oxygen of the incoming DMTr-protected nucleoside, ROH the free 5'-hydroxyl of the
support-bound chain, CEO the 2-cyanoethoxy group). Top: the activator (1H-tetrazole, pKa 4.9,
or 5-ethylthiotetrazole) protonates the diisopropylamino nitrogen, and the tetrazolide anion
displaces diisopropylamine from phosphorus (nucleophilic catalysis), giving a highly reactive
tetrazolyl phosphoramidite. Bottom: the 5'-OH attacks phosphorus and tetrazole leaves, giving
the P(III) phosphite triester."""

from wikichem import Scheme

s = Scheme()
y = 0.0
am = s.molecule("*OP(*)[NH+](C(C)C)C(C)C", at=(0.0, y), labels={0: "R$'$", 3: "CEO"})
tz = s.molecule("c1nn[n-]n1", at=(-3.0, y - 1.4), lone_pairs=[3])
s.curly(tz.atom(3), am.atom(2), bend=0.4)
s.curly(am.bond(2, 4), am.atom(4), bend=-0.6)
s.text((0.0, y - 2.4), "protonated phosphoramidite")
s.arrow((2.6, y), (4.2, y), above=r"$-$HN$i$Pr$_2$")
s.molecule("*OP(*)n1cnnn1", at=(7.2, y), labels={0: "R$'$", 3: "CEO"})
s.text((7.2, y - 2.4), "tetrazolyl phosphoramidite")

y = -5.4
t = s.molecule("*OP(*)n1cnnn1", at=(0.0, y), labels={0: "R$'$", 3: "CEO"}, lone_pairs=[2])
roh = s.molecule("*O", at=(-3.0, y - 0.6), labels={0: "R"}, lone_pairs=[1])
s.curly(roh.atom(1), t.atom(2), bend=0.4)
s.curly(t.bond(2, 4), t.atom(4), bend=-0.6)
s.arrow((2.6, y), (4.2, y), above=r"$-$tetrazole")
s.molecule("*OP(*)O*", at=(6.4, y), labels={0: "R$'$", 3: "CEO", 5: "R"})
s.text((6.4, y - 1.8), "phosphite triester, P(III)")
s.draw()
