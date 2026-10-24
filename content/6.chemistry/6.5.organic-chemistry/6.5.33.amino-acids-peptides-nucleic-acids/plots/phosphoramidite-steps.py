"""The other steps of the phosphoramidite cycle and the final deprotection (R, R' the two
nucleosides joined by the new linkage, CEO the 2-cyanoethoxy group). Top: detritylation with
dichloro- or trichloroacetic acid in dichloromethane; the protonated 5'-ether ionizes (SN1) to
the orange 4,4'-dimethoxytrityl cation, whose absorbance at 498 nm measures the yield of each
cycle (drawn here with plain phenyl groups). Middle: oxidation with iodine in aqueous pyridine;
phosphorus attacks iodine, water adds to the iodophosphonium ion and HI is lost, giving the
stable P(V) phosphate triester. Bottom: in aqueous ammonia the cyanoethyl group is removed by
E1cb elimination of acrylonitrile, leaving the phosphodiester anion of natural DNA."""

from wikichem import Scheme

s = Scheme()
y = 0.0
tr = s.molecule("*[OH+]C(c1ccccc1)(c1ccccc1)c1ccccc1", at=(0.0, y), labels={0: "5$'$-nucleoside"})
s.curly(tr.bond(1, 2), tr.atom(1), bend=0.6)
s.arrow((2.8, y), (4.2, y), above="SN1")
s.molecule("[C+](c1ccccc1)(c1ccccc1)c1ccccc1", at=(6.4, y))
s.text((6.4, y - 2.6), "trityl cation (DMTr$^+$ is orange)")
s.plus((9.4, y))
s.molecule("*O", at=(11.4, y), labels={0: "5$'$-nucleoside"})

y = -5.6
ph = s.molecule("*OP(*)O*", at=(0.0, y), labels={0: "R$'$", 3: "CEO", 5: "R"}, lone_pairs=[2])
i2 = s.molecule("II", at=(1.8, y + 1.6))
s.curly(ph.atom(2), i2.atom(0), bend=-0.5)
s.curly(i2.bond(0, 1), i2.atom(1), bend=-0.7)
s.arrow((2.6, y), (4.0, y), above=r"$-$I$^-$")
ip = s.molecule("*O[P+](I)(*)O*", at=(6.0, y), labels={0: "R$'$", 4: "CEO", 6: "R"})
w = s.molecule("O", at=(8.0, y + 1.4), lone_pairs=[0])
s.curly(w.atom(0), ip.atom(2), bend=0.5)
s.arrow((8.4, y - 0.4), (9.8, y - 0.4), above=r"$-$HI", below=r"$-$H$^+$")
s.molecule("*OP(=O)(*)O*", at=(12.0, y), labels={0: "R$'$", 4: "CEO", 6: "R"})
s.text((12.0, y - 1.8), "phosphate triester, P(V)")

y = -11.0
ce = s.molecule("*OP(=O)(OCCC#N)O*", at=(0.0, y), labels={0: "R$'$", 10: "R"}, show_h=[6])
nh3 = s.molecule("N", at=(-2.6, y - 2.0), lone_pairs=[0])
s.curly(nh3.atom(0), ce.h(6), bend=-0.4)
s.curly(ce.bond(6, 11), ce.bond(5, 6), bend=-0.6)
s.curly(ce.bond(4, 5), ce.atom(4), bend=0.6)
s.arrow((3.4, y), (4.8, y), above=r"NH$_3$, H$_2$O", below="E1cb")
s.molecule("*OP(=O)([O-])O*", at=(7.2, y), labels={0: "R$'$", 6: "R"})
s.text((7.2, y - 1.8), "phosphodiester")
s.plus((9.8, y))
s.molecule("C=CC#N", at=(11.4, y))
s.text((11.4, y - 1.0), "acrylonitrile")
s.draw()
