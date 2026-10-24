"""Addition of a Grignard reagent to a ketone (ethylmagnesium bromide and acetophenone; the phenyl
group is written as a label). Magnesium coordinates to the carbonyl oxygen (dashed bond) and
activates it as a Lewis acid; the C-Mg bond pair then moves onto the carbonyl carbon while the C=O
pi pair moves onto oxygen, giving the magnesium alkoxide. Acidic workup gives the tertiary alcohol."""

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
ket = s.molecule("CC(=O)*", coords=[(-0.87, 0.5), (0, 0), (0.87, 0.5), (0, -1.0)], labels={3: "Ph"}, lone_pairs=[2])
eg = s.molecule("CC[Mg]Br", coords=[(2.0, -2.2), (1.4, -1.35), (2.3, -0.6), (3.3, -0.75)])
s.partial(ket.atom(2), eg.atom(2))
s.curly(eg.bond(1, 2), ket.atom(1), bend=-0.4)
s.curly(ket.bond(1, 2), ket.atom(2), bend=0.8)
row(s, [("arrow", None), "CCC(C)(O[Mg]Br)c1ccccc1", ("arrow", r"H$_3$O$^+$"), "CCC(C)(O)c1ccccc1"], x=3.6, y=-0.4)
s.draw()
