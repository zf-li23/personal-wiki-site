"""SN1 hydrolysis of 2-bromo-2-methylpropane written as elementary steps. Step 1 (slow,
rate-determining): heterolysis of the C-Br bond gives the tert-butyl cation. Step 2 (fast): a water
molecule attacks the cation and gives an oxonium ion. Step 3 (fast): proton transfer to a second
water molecule gives 2-methylpropan-2-ol. The rate law v = k[t-BuBr] reflects step 1 only."""

from wikichem import Scheme

s = Scheme(scale=0.46)

# Step 1
y = 0.0
s.text((-2.6, y), "1")
tbu = s.molecule("CC(C)(C)Br", at=(0.0, y), rotate=-60, lone_pairs=[4])
s.curly(tbu.bond(1, 4), tbu.atom(4), bend=0.9)
s.arrow((2.2, y), (3.8, y), above="slow")
s.molecule("C[C+](C)C", at=(5.3, y))
s.plus((6.9, y))
s.molecule("[Br-]", at=(7.9, y), lone_pairs=True)

# Step 2
y = -3.6
s.text((-2.6, y), "2")
cation = s.molecule("C[C+](C)C", at=(0.0, y))
water = s.molecule("O", at=(2.3, y), rotate=90, lone_pairs=True, explicit_h=True)
s.curly(water.atom(0), cation.atom(1), bend=0.35)
s.arrow((3.4, y), (4.8, y), above="fast")
s.molecule("CC(C)(C)[OH2+]", at=(6.4, y), lone_pairs=[4])

# Step 3: proton transfer to water, written over the arrow.
y = -7.0
s.text((-2.6, y), "3")
s.molecule("CC(C)(C)[OH2+]", at=(0.0, y), rotate=-60, lone_pairs=[4])
s.arrow((2.0, y), (4.4, y), above=r"$+\,\mathrm{H_2O}$", below=r"$-\,\mathrm{H_3O^+}$")
s.molecule("CC(C)(C)O", at=(6.0, y), rotate=-60, lone_pairs=[4])
s.draw()
