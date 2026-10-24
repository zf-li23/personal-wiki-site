"""Directing effects of an alkyl group and a halogen: resonance structures of the sigma complexes for
para bromination. Toluene (top): one structure puts the positive charge on C1, a tertiary carbon
stabilized by hyperconjugation with the methyl group. Chlorobenzene (bottom): the chlorine lone pair
can share the charge on C1 (chloronium structure, every atom with an octet), which is why halogens
direct ortho/para although their -I effect makes the ring slower to react than benzene."""

exec(open("helpers.txt").read())

RING = [1, 2, 3, 4, 5, 6]


def row(s, y, sub, sub_onium, note1, note_onium, title, x0=0.0, dx=4.4):
    first = s.molecule(f"[C:1]1({sub})=[CH:2][CH2:3][CH:4](Br)[CH:5]=[CH:6]1", at=(x0, y), show_h=[4], rotate=90)
    rest = [f"[CH:1]1({sub})[CH:2]=[CH:3][C:4]9(Br)[CH:5]=[CH:6]1.[H]9",
            f"[C:1]1({sub})[CH:2]=[CH:3][C:4]9(Br)[CH2:5][CH:6]=1.[H]9"]
    plus = [3, 1, 5]
    notes = ["", note1, ""]
    if sub_onium:
        rest.append(f"[C:1]1({sub_onium})[CH:2]=[CH:3][C:4]9(Br)[CH:5]=[CH:6]1.[H]9")
        plus.append(None)
        notes.append(note_onium)
    mols = [first] + [s.molecule(t, at=(x0 + dx * (i + 1), y), like=first) for i, t in enumerate(rest)]
    for i, (m, k) in enumerate(zip(mols, plus)):
        if k:
            charge(s, m, k, RING)
        if i:
            s.arrow((x0 + dx * (i - 0.5) - 0.35, y), (x0 + dx * (i - 0.5) + 0.35, y), kind="resonance")
        if notes[i]:
            s.text((x0 + dx * i, y - 2.95), notes[i], size=9)
    s.text((x0 - 2.6, y), title, size=10)


s = Scheme()
row(s, 0, "C", None, "+ on tertiary C1", "", "toluene")
row(s, -6.2, "Cl", "=[Cl+]", "+ on C1", "chloronium: all octets", "PhCl")
s.draw()
