"""SN1 solvolysis of (R)-3-bromo-3-methylhexane in water. Slow ionization gives a planar (sp2)
tertiary carbocation; its empty p orbital can be attacked by water from either face. Attack from
the face opposite to the departing bromide gives the inverted (S) alcohol, attack from the same
face the (R) alcohol, after loss of a proton. Because the bromide still shields the front face
for a short time (ion pairs), inversion slightly exceeds retention."""

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



Pr, Et, Me = r"C$_3$H$_7$", r"C$_2$H$_5$", r"CH$_3$"

# Substrate
c1 = pt(0, 0)
centre(c1, [((-0.45, 1.05), Me, "plain"), ((-0.95, -0.5), Et, "wedge"), ((-0.15, -1.1), Pr, "hash")])
label(pt(1.4, 0), "Br")
bond(c1, pt(1.4, 0))
s.curly(pt(0.6, 0.06), pt(1.45, 0.4), bend=0.6)
s.text((0.0, -2.0), "(R)")
s.arrow((2.2, 0), (3.6, 0), above="slow", below=r"$-\,\mathrm{Br^-}$")

# Planar cation seen edge-on, with its empty p orbital
c2 = pt(7.4, 0)
centre(c2, [((0.0, 1.1), Me, "plain"), ((-0.7, -0.95), Et, "wedge"), ((0.7, -0.95), Pr, "hash")])
label(c2 + pt(0.3, 0.35), "+", size=12)



lobe(c2 - pt(0.62, 0))
lobe(c2 + pt(0.62, 0))
for sx, tag in ((-1, "a"), (1, "b")):
    w = c2 + pt(sx * 2.6, 0.0)
    label(w, r"H$_2$O")
    s.curly(w + pt(-sx * 0.1, 0.32), c2 + pt(sx * 0.55, 0.3), bend=sx * -0.35)
    s.text(w + pt(0, -0.6), tag, size=11)
s.text(c2 + pt(0, -2.0), "planar carbocation")

# Products
s.arrow((10.4, 0.6), (11.6, 1.9), above="a")
s.arrow((10.4, -0.6), (11.6, -1.9), below="b")
c3 = pt(13.9, 2.4)
label(c3 - pt(1.4, 0), "HO")
bond(c3, c3 - pt(1.4, 0))
centre(c3, [((0.45, 1.05), Me, "plain"), ((0.95, -0.5), Et, "wedge"), ((0.15, -1.1), Pr, "hash")])
s.text(c3 + pt(2.6, 0), "(S), inversion")
c4 = pt(13.3, -2.4)
label(c4 + pt(1.4, 0), "OH")
bond(c4, c4 + pt(1.4, 0))
centre(c4, [((-0.45, 1.05), Me, "plain"), ((-0.95, -0.5), Et, "wedge"), ((-0.15, -1.1), Pr, "hash")])
s.text(c4 + pt(3.2, 0), "(R), retention")
s.text((13.9, -4.3), r"(after loss of H$^+$; inversion slightly exceeds retention)", size=10)
finish()
