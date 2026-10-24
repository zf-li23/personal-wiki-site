"""[3,3]-Sigmatropic shifts. Figure 1: Cope rearrangement of a 1,5-hexadiene (3-methyl-1,5-hexadiene
gives the more substituted (E)-1,5-heptadiene). Figure 2: Claisen rearrangement of allyl vinyl ether
to pent-4-enal (the strong C=O bond makes it irreversible). Figure 3: aromatic Claisen rearrangement
of allyl phenyl ether: the [3,3] shift gives a cyclohexadienone, which tautomerizes to 2-allylphenol."""

exec(open("fixedmol.txt").read())

h = ring(6, start=0)  # h[0] right, counter-clockwise; drawn as a chair-like six-atom array


# Figure 1: Cope. Atoms of C=CC(C)CC=C: 0 C1, 1 C2, 2 C3, 3 Me, 4 C4, 5 C5, 6 C6; the new bond C1-C6.
s = Scheme()
cope = fixed(s, "C=CC(C)CC=C", [h[5], h[0], h[1], (1.0, 1.75), h[2], h[3], h[4]])
s.partial(cope.xy(0), cope.xy(6))
s.curly(cope.bond(5, 6), (cope.xy(0) + cope.xy(6)) / 2, bend=0.5)
s.curly(cope.bond(2, 4), cope.bond(4, 5), bend=-0.6)
s.curly(cope.bond(0, 1), cope.bond(1, 2), bend=-0.5)
s.text((0, -1.75), "3-methyl-1,5-hexadiene")
s.arrow((1.7, 0), (3.1, 0), above=r"[3,3], $\Delta$")
fixed(s, "CC=CCCC=C", [(1.0, 1.75), h[1], h[0], h[5], h[4], h[3], h[2]], at=(4.7, 0))
s.text((4.7, -1.75), "(E)-1,5-heptadiene")
s.draw()

# Figure 2: Claisen. Atoms of C=COCC=C: 0 C, 1 C, 2 O, 3 C, 4 C, 5 C; the O-C3 bond breaks, C0-C5 forms.
s = Scheme()
cl = fixed(s, "C=COCC=C", [h[5], h[0], h[1], h[2], h[3], h[4]], lone_pairs=(2,))
s.partial(cl.xy(0), cl.xy(5))
s.curly(cl.bond(4, 5), (cl.xy(0) + cl.xy(5)) / 2, bend=0.5)
s.curly(cl.bond(2, 3), cl.bond(3, 4), bend=-0.6)
s.curly(cl.bond(0, 1), cl.bond(1, 2), bend=-0.5)
s.text((0, -1.75), "allyl vinyl ether")
s.arrow((1.7, 0), (3.1, 0), above=r"[3,3], $\Delta$")
fixed(s, "O=CCCC=C", [h[1], h[0], h[5], h[4], h[3], h[2]], at=(4.7, 0), lone_pairs=(0,))
s.text((4.7, -1.75), "pent-4-enal")
s.draw()

# Figure 3: aromatic Claisen rearrangement.
s = Scheme()
s.molecule("C=CCOc1ccccc1", at=(0, 0), lone_pairs=[4])
s.arrow((3.0, 0), (4.4, 0), above=r"[3,3]", below=r"200 $^\circ$C")
s.molecule("C=CCC1C=CC=CC1=O", at=(7.0, 0))
s.text((7.0, -1.9), "dienone")
s.arrow((9.6, 0), (11.0, 0), above="tautomerize")
s.molecule("C=CCc1ccccc1O", at=(13.6, 0))
s.text((13.6, -1.9), "2-allylphenol")
s.draw()
