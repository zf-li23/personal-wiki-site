"""Regioselectivity of electrophilic substitution of pyrrole (bromination). Top row: attack at C2 gives
a sigma complex with three resonance structures (positive charge on C3, C5 and N). Bottom row: attack
at C3 gives only two (positive charge on C2 and N); the C4=C5 bond is cross-conjugated. In both rows
the structure with the positive nitrogen (an iminium ion, every atom with an octet) is the major
contributor."""

from wikichem import Scheme

DX = 3.6


def row(s, y, smiles, sp3, title):
    first = s.molecule(smiles[0], at=(0, y), show_h=[sp3], rotate=-90)
    for i, smi in enumerate(smiles[1:], start=1):
        x = DX * (i - 0.5)
        s.arrow((x - 0.35, y), (x + 0.35, y), kind="resonance")
        s.molecule(smi, at=(DX * i, y), like=first)
    s.text((-2.4, y), title, size=10)


s = Scheme()
row(s, 0, ["[NH:1]1[CH:2](Br)[CH+:3][CH:4]=[CH:5]1",
           "[NH:1]1[C:2]9(Br)[CH:3]=[CH:4][CH+:5]1.[H]9",
           "[NH+:1]1[C:2]9(Br)[CH:3]=[CH:4][CH:5]=1.[H]9"], 2, "C2 attack")
row(s, -4.2, ["[NH:1]1[CH+:2][CH:3](Br)[CH:4]=[CH:5]1",
              "[NH+:1]1=[CH:2][C:3]9(Br)[CH:4]=[CH:5]1.[H]9"], 3, "C3 attack")
s.draw()
