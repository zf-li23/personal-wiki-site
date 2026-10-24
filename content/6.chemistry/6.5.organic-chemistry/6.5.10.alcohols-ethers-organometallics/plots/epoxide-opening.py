"""Ring opening of 2,2-dimethyloxirane. Top, basic conditions: methoxide attacks the less hindered
CH2 carbon in an SN2 reaction; the ring strain makes the alkoxide a feasible leaving group, and
protonation gives 1-methoxy-2-methylpropan-2-ol. Bottom, acidic conditions: the protonated epoxide
has a long, weak bond to the tertiary carbon, which carries most of the positive charge; methanol
attacks that carbon from the back side (SN2 with SN1 character), giving 2-methoxy-2-methylpropan-1-ol."""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Polygon

from wikichem import Scheme

s = Scheme(scale=0.46)
CLEAR = 0.32  # hand-drawn bonds stop short of a text label
EXTRA = []  # hand-drawn wedges, hashes and dots, added to the axes after s.draw()


def reach(*points):
    """Make sure the figure bounds include these points (an empty text marks them)."""
    for p in points:
        s.text(p, "")


def bond(a, b, kind="plain", clear_a=False, clear_b=True, dashed=False, order=1):
    """A bond drawn by hand from a to b; kind: plain, wedge or hash (narrow end at a)."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    u = (b - a) / np.linalg.norm(b - a)
    if clear_a:
        a = a + CLEAR * u
    if clear_b:
        b = b - CLEAR * u
    n = np.array([-u[1], u[0]])
    reach(a, b)
    if dashed:
        s.partial(a, b)
        return

    def draw(ax, ink):
        if kind == "wedge":
            ax.add_patch(Polygon([a, b + 0.1 * n, b - 0.1 * n], closed=True, color=ink, lw=0))
        elif kind == "hash":
            for t in np.linspace(0.15, 1, 7):
                p = a + t * (b - a)
                w = 0.1 * t
                ax.plot([p[0] - w * n[0], p[0] + w * n[0]], [p[1] - w * n[1], p[1] + w * n[1]], color=ink, lw=1.1)
        else:
            for o in ([0.0] if order == 1 else [-0.08, 0.08]):
                p, q = a + o * n, b + o * n
                ax.plot([p[0], q[0]], [p[1], q[1]], color=ink, lw=1.4, solid_capstyle="round")

    EXTRA.append(draw)


def label(at, text, size=None):
    s.text(at, text, size=size)


def centre(c, groups):
    """Draw a stereocentre at c; groups: (offset, text, kind)."""
    c = np.asarray(c, float)
    for off, text, kind in groups:
        p = c + np.asarray(off, float)
        bond(c, p, kind, clear_b=text is not None)
        if text is not None:
            label(p, text)


def pt(x, y):
    return np.array([x, y], float)


def dots(c, d):
    """A lone pair drawn beside a text label: centre c, unit direction d."""
    c, d = np.asarray(c, float), np.asarray(d, float)
    t = np.array([-d[1], d[0]])
    reach(c)

    def draw(ax, ink):
        for k in (-1, 1):
            p = c + 0.06 * k * t
            ax.plot(*p, marker="o", ms=1.8, color=ink)

    EXTRA.append(draw)


def lobe(c, w=1.1, h=0.55):
    """An unshaded orbital lobe (ellipse) centred at c."""
    c = np.asarray(c, float)
    reach(c - pt(w / 2, h / 2), c + pt(w / 2, h / 2))
    EXTRA.append(lambda ax, ink: ax.add_patch(Ellipse(tuple(c), w, h, fill=False, color=ink, lw=1.1)))


def fixed(smiles, coords, at=(0, 0), lone_pairs=()):
    """Place a structure at hand-chosen atom coordinates (SMILES order, in bond lengths)."""
    return s.molecule(smiles, coords=coords, at=at, lone_pairs=list(lone_pairs))


def finish():
    fig, ax = s.draw()
    ink = plt.rcParams["text.color"]
    for f in EXTRA:
        f(ax, ink)


EP = [(-0.55, 0.85), (0, 0), (-1.0, -0.2), (1.0, 0), (0.5, -0.85)]  # Me, Cq, Me, CH2, O

y = 0.0
s.text((-3.2, y), "base")
ep = fixed("CC1(C)CO1", EP, at=(0, y), lone_pairs=(4,))
label(pt(2.3, y + 1.5), r"CH$_3$O$^-$")
s.curly(pt(1.9, y + 1.2), ep.atom(3), bend=0.3)
s.curly(ep.bond(3, 4), ep.atom(4), bend=-0.7)
s.arrow((2.8, y), (4.2, y), above="SN2")
s.molecule("CC(C)([O-])COC", at=(6.0, y))
s.arrow((7.8, y), (9.2, y), above="MeOH")
s.molecule("CC(C)(O)COC", at=(11.0, y))
s.text((11.0, y - 1.7), "attack at the less substituted carbon", size=10)

y = -4.2
s.text((-3.2, y), "acid")
pe = fixed("CC1(C)C[OH+]1", EP, at=(0, y), lone_pairs=(4,))
label(pt(-1.9, y + 1.7), r"CH$_3$OH")
s.curly(pt(-1.4, y + 1.35), pt(-0.1, y + 0.15), bend=-0.3)
s.curly(pe.bond(1, 4), pe.atom(4), bend=0.7)
s.arrow((2.8, y), (4.2, y), below=r"$-\,\mathrm{H^+}$")
s.molecule("CC(C)(OC)CO", at=(6.4, y), flip=True)
s.text((6.4, y - 1.9), "attack at the more substituted carbon", size=10)
finish()
