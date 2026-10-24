"""Neighbouring-group participation in the hydrolysis of (S)-2-bromopropanoate with dilute base.
Step 1: the carboxylate oxygen, held next to the reaction centre, displaces bromide from the back
side (intramolecular SN2, first inversion) and gives a strained alpha-lactone. Step 2: water or
hydroxide opens the three-membered ring at the same carbon, again from the back side (second
inversion). Two inversions add up to overall retention: (S)-lactate."""

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


Me, H = r"CH$_3$", "H"

# Substrate: carboxylate on the upper left, bromine on the right.
c1 = pt(0, 0)
k1 = pt(-0.55, 1.0)  # carboxylate carbon (bare vertex)
centre(c1, [((-0.9, -0.5), Me, "wedge"), ((-0.15, -1.1), H, "hash")])
bond(c1, k1, clear_b=False)
label(k1 + pt(0.35, 1.0), "O")
bond(k1, k1 + pt(0.35, 1.0), order=2)
label(k1 + pt(-1.1, -0.35), "O")
label(k1 + pt(-0.75, -0.05), "$-$", size=10)
bond(k1, k1 + pt(-1.1, -0.35))
dots(k1 + pt(-1.1, -0.72), (0, -1))
label(pt(1.4, 0), "Br")
bond(c1, pt(1.4, 0))
s.curly(k1 + pt(-1.05, -0.7), c1 - pt(0.25, -0.05), bend=0.45)
s.curly(pt(0.6, 0.06), pt(1.45, 0.4), bend=0.6)
s.text((0.0, -2.0), "(S)-2-bromopropanoate")
s.arrow((2.2, 0.2), (3.6, 0.2), above="slow", below=r"$-\,\mathrm{Br^-}$")

# alpha-Lactone: the ring oxygen sits on the left of C2, the other groups point right.
c2 = pt(6.2, 0)
o2 = c2 + pt(-1.2, 0.0)
k2 = c2 + pt(-0.6, 1.0)
label(o2, "O")
bond(c2, o2)
bond(c2, k2, clear_b=False)
bond(k2, o2)
label(k2 + pt(0.0, 1.15), "O")
bond(k2, k2 + pt(0, 1.15), order=2)
centre(c2, [((0.6, -0.95), Me, "wedge"), ((0.8, 0.7), H, "hash")])
label(c2 + pt(2.3, 0.0), r"HO$^-$")
s.curly(c2 + pt(1.85, 0.15), c2 + pt(0.25, 0.05), bend=0.35)
s.curly(c2 + pt(-0.5, -0.05), o2 + pt(0.2, -0.35), bend=0.7)
s.text(c2 + pt(-0.3, -2.0), r"$\alpha$-lactone (inverted)")
s.arrow((9.4, 0.2), (10.8, 0.2), above="fast")

# Product: hydroxyl on the right, as bromine was: retention.
c3 = pt(13.0, 0)
k3 = c3 + pt(-0.55, 1.0)
centre(c3, [((-0.9, -0.5), Me, "wedge"), ((-0.15, -1.1), H, "hash")])
bond(c3, k3, clear_b=False)
label(k3 + pt(0.35, 1.0), "O")
bond(k3, k3 + pt(0.35, 1.0), order=2)
label(k3 + pt(-1.15, -0.35), r"O$^-$")
bond(k3, k3 + pt(-1.0, -0.3))
label(c3 + pt(1.4, 0), "OH")
bond(c3, c3 + pt(1.4, 0))
s.text(c3 + pt(0, -2.0), "(S)-lactate (retention)")
finish()
