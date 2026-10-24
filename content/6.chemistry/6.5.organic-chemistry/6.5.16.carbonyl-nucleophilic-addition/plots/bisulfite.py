"""Addition of hydrogensulfite to acetone. The soft, polarizable lone pair on sulfur (not oxygen)
attacks the carbonyl carbon and the C=O pi pair moves onto oxygen; proton transfer from the SO3H
group to the alkoxide gives the sodium alpha-hydroxysulfonate, which crystallizes from the
saturated solution."""

from wikichem import Scheme

def extent(smiles, **kw):
    """Horizontal extent of a structure as it would be drawn (laid out on a scratch scheme)."""
    c = Scheme().molecule(smiles, **kw).coords
    return c[:, 0].min(), c[:, 0].max()


def row(s, items, x=0.0, y=0.0, gap=0.7, arrow=1.5):
    """Lay out structures, plus signs and reaction arrows from left to right; returns the placed molecules and the end x."""
    placed = []
    for it in items:
        if isinstance(it, tuple) and it[0] == "arrow":
            s.arrow((x + 0.1, y), (x + 0.1 + arrow, y), above=it[1], below=it[2] if len(it) > 2 else None)
            x += arrow + 0.2
        elif it == "+":
            s.plus((x + 0.45, y))
            x += 0.9
        else:
            smi, kw = (it, {}) if isinstance(it, str) else it
            lo, hi = extent(smi, **kw)
            m = s.molecule(smi, at=(x + gap - lo, y), **kw)
            placed.append(m)
            x += gap + (hi - lo) + gap
    return placed, x

s = Scheme()
hs = s.molecule("O=S([O-])O", at=(-1.6, 0.6), lone_pairs=[1])
ket = s.molecule("CC(C)=O", at=(0.6, 0.0), lone_pairs=[3])
s.curly(hs.atom(1), ket.atom(1), bend=-0.4)
s.curly(ket.bond(1, 3), ket.atom(3), bend=-0.7)
row(s, [("arrow", None), "CC(C)([O-])S(=O)(=O)O", ("arrow", "proton", "transfer"), "CC(C)(O)S(=O)(=O)[O-]"], x=2.0)
s.draw()
