"""Regioselectivity of electrophilic substitution of indole (bromination). Top: attack at C3 puts the
positive charge on C2, next to nitrogen; the iminium structure keeps the benzene ring intact. Bottom:
attack at C2 puts the charge on C3 (benzylic); nitrogen can share it only in a structure that
disrupts the aromatic sextet of the benzene ring."""

from wikichem import Scheme

BENZO = "[c:4]2[cH:5][cH:6][cH:7][cH:8][c:9]12"
DX = 5.2


def row(s, y, smiles, sp3, title, notes):
    first = s.molecule(smiles[0], at=(0, y), show_h=[sp3])
    for i, smi in enumerate(smiles[1:], start=1):
        x = DX * (i - 0.5)
        s.arrow((x - 0.35, y), (x + 0.35, y), kind="resonance")
        s.molecule(smi, at=(DX * i, y), like=first)
    s.text((-3.4, y), title, size=10)
    for i, note in enumerate(notes):
        s.text((DX * i, y - 2.0), note, size=9)


s = Scheme()
row(s, 0, ["[NH:1]1[CH+:2][CH:3](Br)" + BENZO,
           "[NH+:1]1=[CH:2][C:3]9(Br)" + BENZO + ".[H]9"], 3, "C3 attack",
    ["", "iminium, benzene intact"])
row(s, -5.0, ["[NH:1]1[CH:2](Br)[CH+:3]" + BENZO,
              "[NH+:1]1[C:2]9(Br)[CH:3]=[C:4]2[CH:5]=[CH:6][CH:7]=[CH:8][C:9]2=1.[H]9"], 2, "C2 attack",
    ["", "benzene sextet lost"])
s.draw()
