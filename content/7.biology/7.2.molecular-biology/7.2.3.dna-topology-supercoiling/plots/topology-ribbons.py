# Linking number = twist + writhe for a closed duplex (two strands drawn around the duplex axis; the darker
# strand passes in front where it is drawn on top). A: a relaxed planar circle, Lk = Tw = 12, Wr = 0.
# B: the same circle after two turns have been removed (Lk = 10) and the axis kept flat: Tw = 10, the helix
# is underwound and strained. C: the same molecule (Lk = 10) with the strain taken up by the axis coiling
# on itself: Tw = 12 again, and two negative crossings of the axis give Wr = -2 (an interwound, plectonemic
# supercoil). Converting B into C needs no strand breakage; changing Lk (A into B) does.
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(20, 7.6)


def duplex(axis, turns, width=0.34, over=None):
    """Draw two strands around a closed axis polyline; ``over`` gives each point's layer (0 under, 1 over)."""
    axis = np.asarray(axis, float)
    seg = np.diff(np.vstack([axis, axis[:1]]), axis=0)
    s = np.r_[0, np.cumsum(np.hypot(*seg.T))][:-1]
    s = s / (s[-1] + np.hypot(*seg[-1]))
    tang = seg / np.hypot(*seg.T)[:, None]
    nrm = np.c_[-tang[:, 1], tang[:, 0]]
    phi = 2 * np.pi * turns * s
    layer = np.zeros(len(axis)) if over is None else over
    # a halo along the axis of the upper arm, so that the arm below appears interrupted
    halo = (width + 0.28) * 0.45 * 72
    for i in np.where(layer > 0.5)[0]:
        j = (i + 1) % len(axis)
        ax.plot([axis[i, 0], axis[j, 0]], [axis[i, 1], axis[j, 1]], color=P.surface(), lw=halo,
                solid_capstyle="butt", zorder=13)
    for sign, tok in ((1, "dna"), (-1, "dna2")):
        pts = axis + (sign * width / 2 * np.cos(phi))[:, None] * nrm
        front = sign * np.sin(phi) > 0
        for i in range(len(pts)):
            j = (i + 1) % len(pts)
            col = P.edge(tok) if front[i] else P.mix(P.fill(tok), P.surface(), 0.25)
            z = 10 + 4 * layer[i] + (2 if front[i] else 0)
            ax.plot([pts[i, 0], pts[j, 0]], [pts[i, 1], pts[j, 1]], color=col, lw=2.4,
                    solid_capstyle="round", zorder=z)


def circle(c, r, n=900):
    t = np.linspace(0, 2 * np.pi, n, endpoint=False)
    return np.c_[c[0] + r * np.cos(t), c[1] + r * np.sin(t)]


def caption(x, lines):
    for k, text in enumerate(lines):
        bio.label(ax, (x, 1.15 - 0.45 * k), text, size="small")


# A and B: planar circles
duplex(circle((2.6, 4.4), 1.8), 12)
caption(2.6, ["Relaxed", "Lk = 12, Tw = 12, Wr = 0"])
bio.panel(ax, "A", (0.2, 7.3))
duplex(circle((8.6, 4.4), 1.8), 10)
caption(8.6, ["Underwound, axis flat", "Lk = 10, Tw = 10, Wr = 0"])
bio.panel(ax, "B", (6.2, 7.3))
bio.arrow(ax, (4.75, 4.4), (6.45, 4.4), kind="process")
bio.label(ax, (5.6, 4.7), "break, unwind\n2 turns, reseal", size="tiny", va="bottom")

# C: interwound loop x = A cos t, y = b sin 3t (two self-crossings of the axis)
t = np.linspace(0, 2 * np.pi, 1400, endpoint=False)
A, b, cx, cy = 3.6, 1.25, 15.9, 4.4
axis = np.c_[cx + A * np.cos(t), cy + b * np.sin(3 * t)]
# at each crossing (t = pi/3 with -pi/3, and 2pi/3 with -2pi/3) choose which arm is on top so that
# the crossing sign is negative: sign = sign of the z-component of (t_over x t_under)
over = np.zeros(len(t))
for tc in (np.pi / 3, 2 * np.pi / 3):
    d1 = np.array([-A * np.sin(tc), 3 * b * np.cos(3 * tc)])       # tangent of the arm at +tc
    d2 = np.array([-A * np.sin(-tc), 3 * b * np.cos(-3 * tc)])     # tangent of the arm at -tc
    top = tc if (d1[0] * d2[1] - d1[1] * d2[0]) < 0 else -tc
    near = np.abs(np.angle(np.exp(1j * (t - top)))) < 0.22
    over[near] = 1
duplex(axis, 12, over=over)
caption(cx, ["Supercoiled (interwound)", "Lk = 10, Tw = 12, Wr = −2"])
bio.panel(ax, "C", (11.8, 7.3))
bio.arrow(ax, (10.65, 4.4), (12.0, 4.4), kind="process")
bio.label(ax, (11.3, 4.7), "no break", size="tiny", va="bottom")
