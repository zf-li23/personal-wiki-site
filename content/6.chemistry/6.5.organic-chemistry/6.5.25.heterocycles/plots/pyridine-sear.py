"""Why electrophilic substitution of pyridine goes to C3. Top: attack at C3 (bromination shown)
gives a sigma complex whose three resonance structures put the positive charge on C2, C4 and C6,
never on nitrogen. Bottom: attack at C2 gives one resonance structure with the positive charge on
nitrogen, which then has only six valence electrons; this structure is very unfavourable, so the
C2 (and likewise C4) sigma complexes lie much higher in energy."""

from wikichem import Scheme

s = Scheme()
y = 0.0
a = s.molecule("N1[CH+]C(Br)C=CC=1", at=(0, y))
s.arrow((1.5, y), (2.7, y), kind="resonance")
s.molecule("N1=CC(Br)[CH+]C=C1", at=(4.2, y), like=a)
s.arrow((5.7, y), (6.9, y), kind="resonance")
s.molecule("N1=CC(Br)C=C[CH+]1", at=(8.4, y), like=a)
s.text((4.2, y - 2.0), "attack at C3: N never carries the positive charge")

y = -4.6
d = s.molecule("N1C(Br)[CH+]C=CC=1", at=(0, y))
s.arrow((1.5, y), (2.7, y), kind="resonance")
s.molecule("N1C(Br)C=C[CH+]C=1", at=(4.2, y), like=d)
s.arrow((5.7, y), (6.9, y), kind="resonance")
s.molecule("*1C(Br)C=CC=C1", at=(8.4, y), like=d, labels={0: r"N$^+$"})
s.text((4.2, y - 2.0), "attack at C2: one structure has N$^+$ with only six electrons")
s.draw()
