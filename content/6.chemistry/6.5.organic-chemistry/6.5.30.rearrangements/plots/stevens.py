"""Stevens rearrangement of benzyldimethyl(phenacyl)ammonium bromide. Hydroxide removes the acidic
proton between the carbonyl group and the ammonium nitrogen, giving an ammonium ylide. The N-benzyl
bond breaks homolytically (fishhook arrows); the benzyl radical and the captodatively stabilized
radical anion recombine at carbon within the solvent cage, so the benzyl group ends up on the former
ylide carbon with its configuration largely retained. Product: 2-(dimethylamino)-1,3-diphenylpropan-1-one."""

from wikichem import Scheme

s = Scheme(scale=0.4)
y = 0.0
s.molecule("O=C(C[N+](C)(C)Cc1ccccc1)c1ccccc1", at=(0.0, y))
s.text((0.0, y - 4.0), r"ammonium salt (Br$^-$)")
s.arrow((4.0, y), (5.4, y), above=r"NaOH", below=r"$-\,\mathrm{H_2O}$")
a = s.molecule("O=C([CH-][N+](C)(C)Cc1ccccc1)c1ccccc1", at=(9.4, y))
s.curly(a.bond(3, 6), a.atom(6), bend=-0.7, single=True)
s.curly(a.bond(3, 6), a.atom(3), bend=0.7, single=True)
s.text((9.4, y - 4.0), "ammonium ylide")
s.arrow((13.5, y), (15.5, y), above="radical pair", below="recombination")
s.molecule("O=C(C(N(C)C)Cc1ccccc1)c1ccccc1", at=(18.6, y), rotate=-30)
s.text((18.6, y - 4.0), "Stevens product")
s.draw()
