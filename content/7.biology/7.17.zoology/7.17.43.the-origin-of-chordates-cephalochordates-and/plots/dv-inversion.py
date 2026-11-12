# Dorsoventral inversion, schematic cross-sections: (A) acorn worm, (B) lancelet, each anatomical dorsal
# side up, with the BMP (dark) and Chordin (light) domains of the embryonic ectoderm; (C) the acorn-worm
# section turned upside down brings nerve cord, vessels and gill openings into the chordate positions.
import numpy as np
import wikibio as bio
from matplotlib.patches import Circle, Wedge, Ellipse

P = bio.P
fig, ax = bio.canvas(27.0, 10.6)
SIG = "protein"
NERVE, NOTO, GUT, BLOOD = "neuron", "drug", "endoderm", "blood"
R = 2.3


def ring(cx, cy, bmp_up):
    """Body wall: the half facing up is BMP (dark) when bmp_up, otherwise Chordin (light)."""
    up, down = (P.fill(SIG), P.light(SIG)) if bmp_up else (P.light(SIG), P.fill(SIG))
    ax.add_patch(Wedge((cx, cy), R, 0, 180, width=0.55, facecolor=up, edgecolor=P.edge(SIG), lw=0.9, zorder=4))
    ax.add_patch(Wedge((cx, cy), R, 180, 360, width=0.55, facecolor=down, edgecolor=P.edge(SIG), lw=0.9, zorder=4))
    ax.add_patch(Circle((cx, cy), R - 0.55, facecolor=P.mix(P.light("neutral"), P.surface(), 0.5),
                        edgecolor=P.edge("neutral"), lw=0.6, zorder=3))


def flow(c, forward, r=0.22):
    """A vessel in cross-section: a dot (blood toward the viewer = forward) or a cross (away = backward)."""
    ax.add_patch(Circle(c, r, facecolor=P.fill(BLOOD), edgecolor=P.edge(BLOOD), lw=0.9, zorder=7))
    if forward:
        ax.add_patch(Circle(c, r * 0.3, facecolor=P.on_fill(), edgecolor=P.on_fill(), zorder=8))
    else:
        d = r * 0.6
        for s in (1, -1):
            ax.plot([c[0] - d, c[0] + d], [c[1] - s * d, c[1] + s * d], color=P.on_fill(), lw=1.1, zorder=8)


def acorn_worm(cx, cy, flip=False):
    s = -1 if flip else 1
    ring(cx, cy, bmp_up=not flip)
    ax.add_patch(Ellipse((cx, cy - s * 0.15), 1.9, 1.5, facecolor=P.light(GUT), edgecolor=P.edge(GUT), lw=0.9,
                         zorder=5))
    for dx in (-0.45, 0.45):                                          # gill slits to dorsal gill pores
        ax.plot([cx + dx, cx + dx * 1.15], [cy + s * 0.45, cy + s * (R - 0.05)], color=P.edge(GUT), lw=2.4,
                zorder=5.5, solid_capstyle="round")
        ax.plot([cx + dx, cx + dx * 1.15], [cy + s * 0.45, cy + s * (R - 0.05)], color=P.surface(), lw=1.0,
                zorder=5.6, solid_capstyle="round")
    ax.add_patch(Ellipse((cx, cy - s * (R - 0.28)), 0.9, 0.36, facecolor=P.fill(NERVE), edgecolor=P.edge(NERVE),
                         lw=0.9, zorder=6))                           # main (ventral) nerve cord
    ax.add_patch(Ellipse((cx, cy + s * (R - 0.28)), 0.36, 0.22, facecolor=P.fill(NERVE), edgecolor=P.edge(NERVE),
                         lw=0.9, zorder=6))                           # small dorsal cord
    flow((cx, cy + s * 0.95), forward=True)                           # dorsal vessel, forward
    flow((cx, cy - s * 1.15), forward=False)                          # ventral vessel, backward
    return dict(main=(cx, cy - s * (R - 0.28)), small=(cx, cy + s * (R - 0.28)), pore=(cx + 0.5, cy + s * (R - 0.1)),
                dv=(cx, cy + s * 0.95), vv=(cx, cy - s * 1.15), gut=(cx - 0.4, cy - s * 0.2))


def lancelet(cx, cy):
    ring(cx, cy, bmp_up=False)
    ax.add_patch(Circle((cx, cy + R - 0.32), 0.3, facecolor=P.fill(NERVE), edgecolor=P.edge(NERVE), lw=0.9, zorder=6))
    ax.add_patch(Circle((cx, cy + 0.95), 0.45, facecolor=P.fill(NOTO), edgecolor=P.edge(NOTO), lw=0.9, zorder=6))
    flow((cx, cy + 0.3), forward=False)                               # dorsal aorta, backward
    ax.add_patch(Ellipse((cx, cy - 0.55), 1.6, 1.2, facecolor=P.light(GUT), edgecolor=P.edge(GUT), lw=0.9, zorder=5))
    ax.add_patch(Ellipse((cx, cy - 1.05), 0.6, 0.24, facecolor=P.fill(GUT), edgecolor=P.edge(GUT), lw=0.9, zorder=5.5))
    flow((cx, cy - 1.42), forward=True)                               # ventral aorta (heart), forward
    for dx in (-0.55, 0.55):                                          # slits open ventrolaterally into the atrium
        ax.plot([cx + dx, cx + dx * 1.9], [cy - 0.8, cy - (R - 0.45)], color=P.edge(GUT), lw=2.4, zorder=5.5,
                solid_capstyle="round")
        ax.plot([cx + dx, cx + dx * 1.9], [cy - 0.8, cy - (R - 0.45)], color=P.surface(), lw=1.0, zorder=5.6,
                solid_capstyle="round")
    return dict(nc=(cx, cy + R - 0.32), noto=(cx, cy + 0.95), da=(cx, cy + 0.3), endo=(cx, cy - 1.05),
                va=(cx, cy - 1.42), slit=(cx + 1.0, cy - 1.45), gut=(cx - 0.4, cy - 0.45))


Y = 5.4
C = bio.callout
# (A) acorn worm
a = acorn_worm(4.2, Y)
bio.panel(ax, "A", (0.4, 10.1))
bio.label(ax, (4.2, 9.6), "Acorn worm", size="normal", bold=True)
C(ax, a["small"], (1.0, 8.6), "Dorsal cord")
C(ax, a["pore"], (7.6, 8.6), "Gill pores (dorsal)")
C(ax, a["dv"], (8.0, 7.2), "Dorsal vessel: forward")
C(ax, a["gut"], (0.6, 4.6), "Pharynx")
C(ax, a["vv"], (8.0, 3.6), "Ventral vessel: backward")
C(ax, a["main"], (2.0, 1.6), "Main nerve cord (ventral)")
bio.label(ax, (4.2, 1.0), "BMP dorsal, Chordin ventral", size="small")

# (B) lancelet
b = lancelet(13.4, Y)
bio.panel(ax, "B", (9.6, 10.1))
bio.label(ax, (13.4, 9.6), "Lancelet", size="normal", bold=True)
C(ax, b["nc"], (16.6, 9.0), "Nerve cord (dorsal)")
C(ax, b["noto"], (16.8, 8.1), "Notochord")
C(ax, b["da"], (17.2, 7.0), "Dorsal aorta: backward")
C(ax, b["gut"], (9.8, 4.6), "Pharynx")
C(ax, b["endo"], (9.8, 3.0), "Endostyle")
C(ax, b["slit"], (17.2, 3.6), "Slits open ventrally")
C(ax, b["va"], (14.8, 1.6), "Ventral aorta: forward")
bio.label(ax, (13.4, 1.0), "Chordin dorsal, BMP ventral", size="small")

# (C) the acorn-worm section inverted
bio.panel(ax, "C", (19.2, 10.1))
bio.label(ax, (23.6, 9.6), "Acorn worm inverted", size="normal", bold=True)
c = acorn_worm(23.6, Y, flip=True)
bio.arrow(ax, (20.0, 7.6), (20.0, 3.2), kind="process", bend=0.5, lw=1.2, head=0.22, color=P.muted())
bio.label(ax, (19.6, 5.4), "180°", size="small", rotation=90)
C(ax, c["main"], (26.4, 8.6), "Main cord now dorsal")
C(ax, c["dv"], (26.6, 2.8), "Forward vessel now ventral")
C(ax, c["pore"], (26.6, 1.7), "Gill openings now ventral")
bio.label(ax, (23.6, 0.6), "but the mouth (ventral in both) must move or form anew", size="small")

# legend
for k, (face, txt) in enumerate(((P.fill(SIG), "BMP domain"), (P.light(SIG), "Chordin domain"))):
    x = 0.8 + k * 3.4
    ax.add_patch(Wedge((x, 0.25), 0.22, 0, 360, facecolor=face, edgecolor=P.edge(SIG), lw=0.8, zorder=5))
    bio.label(ax, (x + 0.35, 0.25), txt, size="small", ha="left")
flow((8.0, 0.25), True, r=0.18)
bio.label(ax, (8.3, 0.25), "blood toward the head", size="small", ha="left")
flow((12.6, 0.25), False, r=0.18)
bio.label(ax, (12.9, 0.25), "blood toward the tail", size="small", ha="left")
