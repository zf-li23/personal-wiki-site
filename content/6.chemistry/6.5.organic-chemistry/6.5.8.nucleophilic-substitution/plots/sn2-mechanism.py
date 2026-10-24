"""SN2 reaction of hydroxide with (R)-2-bromobutane. The lone pair of the nucleophile attacks the
carbon from the side opposite to bromine (backside attack, into the C-Br sigma* orbital) while the
C-Br bond breaks. In the trigonal-bipyramidal transition state the O...C...Br axis is linear and
the three other groups lie in a plane; the carbon then turns inside out like an umbrella in the
wind, giving (S)-butan-2-ol (Walden inversion)."""

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


# Reactants: hydroxide approaches from the left, bromine leaves to the right.
c1 = pt(0, 0)
label(pt(-2.6, 0), "HO")
label(pt(-2.2, 0.32), "$-$", size=10)

dots(pt(-2.05, 0), (1, 0))
dots(pt(-2.4, -0.32), (0, -1))
centre(c1, [((-0.45, 1.05), r"CH$_3$", "plain"), ((-0.9, -0.5), r"C$_2$H$_5$", "wedge"), ((-0.15, -1.1), "H", "hash")])
label(pt(1.4, 0), "Br")
bond(c1, pt(1.4, 0))
s.curly(pt(-1.95, 0.08), c1 - pt(0.2, -0.05), bend=0.3)
s.curly(pt(0.6, 0.06), pt(1.45, 0.4), bend=0.6)
s.text((0.0, -2.1), "(R)-2-bromobutane")
s.arrow((2.5, 0), (3.8, 0))

# Transition state
c2 = pt(6.9, 0)
for dx, t in ((-1.9, "HO"), (1.9, "Br")):
    label(c2 + pt(dx, 0), t)
    bond(c2, c2 + pt(dx, 0), dashed=True)
    s.text(c2 + pt(dx, 0.5), r"$\delta^-$", size=10)
centre(c2, [((0.0, 1.1), r"CH$_3$", "plain"), ((-0.6, -0.85), r"C$_2$H$_5$", "wedge"), ((0.6, -0.85), "H", "hash")])
s.text(c2 + pt(-2.6, 0), "[", size=44)
s.text(c2 + pt(2.6, 0), "]", size=44)
s.text(c2 + pt(2.95, 1.05), r"$\ddagger$", size=13)
s.text(c2 + pt(0, -2.1), "transition state")
s.arrow((10.2, 0), (11.5, 0))

# Product: the umbrella has turned inside out.
c3 = pt(13.9, 0)
label(c3 - pt(1.4, 0), "HO")
bond(c3, c3 - pt(1.4, 0))
centre(c3, [((0.45, 1.05), r"CH$_3$", "plain"), ((0.9, -0.5), r"C$_2$H$_5$", "wedge"), ((0.15, -1.1), "H", "hash")])
s.plus((16.0, 0.0))
s.molecule("[Br-]", at=(17.1, 0.0), lone_pairs=True)
s.text((13.9, -2.1), "(S)-butan-2-ol")
finish()
