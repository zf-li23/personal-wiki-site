"""Why OCH3 directs ortho/para and NO2 directs meta: resonance structures of the sigma complexes for
para (top row) and meta (bottom row) bromination. Anisole, para attack: one structure puts the
positive charge on C1, where the oxygen lone pair can share it (oxonium structure, every atom with an
octet). Meta attack never puts the charge on C1. Nitrobenzene, para attack: one structure puts the
positive charge on C1, next to the positive nitrogen (strongly destabilizing); meta attack avoids it."""

exec(open("helpers.txt").read())

RING = [1, 2, 3, 4, 5, 6]


def row(s, y, first, others, plus, notes, x0=0.0, dx=4.4):
    """First structure laid out by RDKit (H on the sp3 carbon drawn), the others reuse its layout."""
    sp3 = first[1]
    m0 = s.molecule(first[0], at=(x0, y), show_h=[sp3], rotate=first[2])
    mols = [m0] + [s.molecule(t, at=(x0 + dx * (i + 1), y), like=m0) for i, t in enumerate(others)]
    for i, (m, k) in enumerate(zip(mols, plus)):
        if k:
            charge(s, m, k, RING)
        if i:
            s.arrow((x0 + dx * (i - 0.5) - 0.35, y), (x0 + dx * (i - 0.5) + 0.35, y), kind="resonance")
        if notes[i]:
            s.text((x0 + dx * i, y - 2.95), notes[i], size=9)
    return mols


def figure(sub, sub_oxonium, title_para, title_meta, notes_para, notes_meta):
    s = Scheme()
    para = (f"[C:1]1({sub})=[CH:2][CH2:3][CH:4](Br)[CH:5]=[CH:6]1", 4, 90)
    para_rest = [f"[CH:1]1({sub})[CH:2]=[CH:3][C:4]9(Br)[CH:5]=[CH:6]1.[H]9",
                 f"[C:1]1({sub})[CH:2]=[CH:3][C:4]9(Br)[CH2:5][CH:6]=1.[H]9"]
    plus = [3, 1, 5]
    if sub_oxonium:
        para_rest.append(f"[C:1]1({sub_oxonium})[CH:2]=[CH:3][C:4]9(Br)[CH:5]=[CH:6]1.[H]9")
        plus.append(None)
    row(s, 0, para, para_rest, plus, notes_para)
    s.text((-2.6, 0), title_para, size=10)
    meta = (f"[C:1]1({sub})[CH2:2][CH:3](Br)[CH:4]=[CH:5][CH:6]=1", 3, 30)
    meta_rest = [f"[C:1]1({sub})=[CH:2][C:3]9(Br)[CH2:4][CH:5]=[CH:6]1.[H]9",
                 f"[C:1]1({sub})=[CH:2][C:3]9(Br)[CH:4]=[CH:5][CH2:6]1.[H]9"]
    row(s, -6.2, meta, meta_rest, [2, 4, 6], notes_meta)
    s.text((-2.6, -6.2), title_meta, size=10)
    s.draw()


figure("OC", "=[O+]C", "para", "meta", ["", "+ on C1", "", "oxonium: all octets"], ["", "", "", ""])
figure("[N+](=O)[O-]", None, "para", "meta", ["", "+ next to N+ (bad)", ""], ["", "", ""])
