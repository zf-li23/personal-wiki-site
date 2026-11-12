# The molluscan body plan (schematic sagittal sections, anterior to the left, not to scale).
# A: a generalized mollusc with the main organ systems. B: how the classes modify the same components
# (shell, mantle and mantle cavity, foot, gut from mouth to anus), drawn with the same colours.
import numpy as np
import wikibio as bio
from matplotlib.patches import Circle, Ellipse

P = bio.P
SHELL, MANTLE, FOOT, GUT, NERVE, GILL, HEART = "bone", "positive", "muscle", "endoderm", "neuron", "dna", "blood"


def wash(tok, k=0.55):
    return P.mix(P.fill(tok), P.surface(), 0.78 if P.is_dark() else k)


def blob(ax, pts, tok, z=5, face=None, lw=1.0):
    v = bio.smooth_closed(pts)
    ax.fill(v[:, 0], v[:, 1], facecolor=face or P.fill(tok), edgecolor=P.edge(tok), lw=lw, zorder=z)
    return v


def curve(ax, pts, tok, lw=2.0, z=7, n=120, dashed=False):
    p = np.asarray(pts, float)
    t = np.linspace(0, 1, len(p))
    tt = np.linspace(0, 1, n)
    from scipy.interpolate import make_interp_spline
    k = min(3, len(p) - 1)
    xs = make_interp_spline(t, p[:, 0], k=k)(tt)
    ys = make_interp_spline(t, p[:, 1], k=k)(tt)
    ax.plot(xs, ys, color=P.edge(tok), lw=lw, zorder=z, solid_capstyle="round", ls=(0, (3, 2)) if dashed else "-")
    return np.c_[xs, ys]


def comb(ax, base, tip, n, tok, w=0.28, z=8):
    """A bipectinate ctenidium from base to tip."""
    b, t = np.asarray(base, float), np.asarray(tip, float)
    d = t - b
    L = np.hypot(*d)
    u = d / L
    nn = np.array([-u[1], u[0]])
    ax.plot([b[0], t[0]], [b[1], t[1]], color=P.edge(tok), lw=1.4, zorder=z)
    for s in np.linspace(0.1, 0.95, n):
        c = b + d * s
        ww = w * (1 - 0.5 * s)
        for sg in (-1, 1):
            q = c + nn * sg * ww
            ax.plot([c[0], q[0]], [c[1], q[1]], color=P.edge(tok), lw=1.0, zorder=z)


fig, ax = bio.canvas(30, 21.5)

# ------------------------------------------------------------------ A: generalized mollusc
bio.panel(ax, "A", (0.3, 21.2))
bio.label(ax, (8.2, 21.1), "A generalized mollusc", size="title", bold=True)
# foot
foot = blob(ax, [(2.0, 11.2), (4.0, 10.3), (8.0, 10.1), (12.0, 10.4), (13.6, 11.1), (12.6, 12.0), (8.0, 12.2), (3.6, 12.1)], FOOT, z=3)
# head
blob(ax, [(1.3, 12.0), (1.6, 13.6), (3.0, 14.2), (4.0, 13.4), (3.8, 12.2), (2.4, 11.7)], FOOT, z=3, face=wash(FOOT, 0.35))
curve(ax, [(2.5, 13.9), (1.8, 15.0), (1.1, 15.7)], FOOT, lw=2.4, z=4)  # tentacle
ax.add_patch(Circle((2.7, 13.6), 0.16, facecolor=P.ink(), edgecolor="none", zorder=9))  # eye
# visceral mass
vis = blob(ax, [(3.8, 12.1), (3.9, 14.3), (5.0, 16.3), (7.0, 17.35), (9.9, 17.4), (11.7, 16.5), (12.0, 15.0), (11.7, 12.3), (7.0, 11.9)],
           "neutral", z=4, face=wash("neutral", 0.7))
# mantle (band over the visceral mass, overhanging posteriorly to form the mantle cavity)
mtop = [(3.6, 13.6), (4.3, 16.0), (6.8, 17.7), (9.9, 17.8), (12.3, 16.6), (13.6, 14.5), (14.0, 12.8)]
mant = curve(ax, mtop, MANTLE, lw=5.0, z=6)
# shell above the mantle
sh = np.array([(3.3, 13.7), (4.0, 16.4), (6.7, 18.4), (10.0, 18.5), (12.8, 17.2), (14.3, 14.8), (14.8, 12.7)])
curve(ax, sh, SHELL, lw=9.0, z=5)
# mantle cavity
mc = blob(ax, [(11.7, 12.3), (11.9, 15.0), (12.8, 15.8), (13.6, 14.2), (13.8, 12.6)], MANTLE, z=5, face=wash(MANTLE, 0.55), lw=0.8)
comb(ax, (12.0, 14.6), (13.4, 13.1), 7, GILL, w=0.32, z=9)
# gut: mouth -> buccal cavity with radula -> oesophagus -> stomach -> intestine loop -> anus in mantle cavity
ax.add_patch(Ellipse((3.0, 12.6), 1.3, 0.8, angle=-10, facecolor=wash(GUT, 0.3), edgecolor=P.edge(GUT), lw=0.9, zorder=8))  # buccal mass
curve(ax, [(2.4, 12.5), (3.0, 12.45), (3.55, 12.7)], "neuron", lw=1.6, z=9)  # radula ribbon
g = curve(ax, [(3.6, 12.8), (5.0, 13.6), (6.4, 14.4)], GUT, lw=2.6, z=8)
blob(ax, [(6.2, 14.0), (6.6, 15.3), (7.8, 15.4), (8.2, 14.4), (7.4, 13.8)], GUT, z=8)  # stomach
blob(ax, [(6.0, 15.4), (6.8, 16.6), (8.8, 16.7), (9.6, 15.6), (8.4, 15.4)], "lysosome", z=7, face=wash("lysosome", 0.35))  # digestive gland
curve(ax, [(8.0, 14.2), (9.4, 13.2), (10.5, 13.6), (11.2, 14.6), (12.4, 15.2)], GUT, lw=2.4, z=8)  # intestine
ax.add_patch(Circle((12.45, 15.2), 0.13, facecolor=P.edge(GUT), edgecolor="none", zorder=9))
# pericardium with heart, kidney and gonad
ax.add_patch(Ellipse((10.3, 16.3), 1.9, 1.0, facecolor=wash("cl", 0.45), edgecolor=P.edge("cl"), lw=0.9, zorder=8))
ax.add_patch(Ellipse((10.3, 16.3), 1.0, 0.5, facecolor=P.fill(HEART), edgecolor=P.edge(HEART), lw=0.9, zorder=9))
blob(ax, [(10.9, 14.7), (11.4, 15.8), (11.8, 15.0), (11.5, 14.4)], "vesicle", z=8)  # kidney
blob(ax, [(8.6, 15.6), (9.2, 16.3), (9.6, 15.9), (9.2, 15.4)], "highlight", z=7, face=wash("ovary", 0.2))
# nerve ring and cords
ax.add_patch(Ellipse((3.9, 12.9), 0.7, 1.1, facecolor="none", edgecolor=P.edge(NERVE), lw=1.6, zorder=9))
curve(ax, [(4.1, 12.3), (7.0, 11.4), (11.5, 11.3)], NERVE, lw=1.5, z=9)          # pedal cord
curve(ax, [(4.2, 13.2), (7.0, 13.0), (10.0, 12.6), (11.8, 12.9)], NERVE, lw=1.5, z=9, dashed=True)  # visceral cord
CL = [((2.0, 14.8), (0.6, 18.0), "Head with tentacle and eye"), ((3.0, 12.35), (0.6, 9.4), "Radula in buccal cavity"),
      ((5.0, 11.0), (4.8, 8.6), "Foot"), ((6.5, 18.6), (5.6, 20.3), "Shell"), ((4.6, 16.4), (2.0, 19.2), "Mantle"),
      ((10.3, 16.55), (16.0, 20.0), "Heart in pericardium (coelom)"), ((7.8, 16.2), (16.0, 19.2), "Digestive gland"),
      ((9.2, 15.85), (16.0, 18.4), "Gonad"), ((11.5, 15.3), (16.0, 17.6), "Kidney (metanephridium)"),
      ((12.45, 15.2), (16.0, 16.8), "Anus"), ((7.2, 14.8), (16.0, 16.0), "Stomach"),
      ((13.0, 13.7), (16.0, 14.6), "Ctenidium"), ((8.5, 12.8), (16.0, 13.5), "Visceral (lateral) cord"),
      ((13.5, 12.7), (16.0, 12.6), "Mantle cavity"),
      ((3.9, 13.45), (0.6, 16.6), "Nerve ring"), ((9.0, 11.35), (11.0, 8.6), "Pedal cord")]
for p, q, t in CL:
    bio.callout(ax, p, q, t, size="small")
bio.arrow(ax, (14.6, 10.6), (13.3, 11.6), kind="process", lw=1.0, head=0.18)
bio.arrow(ax, (12.1, 15.9), (13.8, 17.0), kind="process", lw=1.0, head=0.18)
bio.label(ax, (15.0, 10.3), "water in", size="tiny", ha="left", color=P.muted())
bio.label(ax, (14.0, 17.0), "out", size="tiny", ha="left", color=P.muted())
bio.label(ax, (1.0, 10.6), "Anterior", size="tiny", color=P.muted(), ha="left")

# legend
LEG = [(SHELL, "Shell or spicules"), (MANTLE, "Mantle, mantle cavity"), (FOOT, "Foot, head"), (GUT, "Gut"),
       (GILL, "Ctenidium"), (NERVE, "Nervous system")]
for i, (tok, t) in enumerate(LEG):
    x, y = 21.0 + (i % 2) * 4.6, 20.4 - (i // 2) * 0.75
    ax.add_patch(Circle((x, y), 0.22, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=9))
    bio.label(ax, (x + 0.4, y), t, size="small", ha="left")

# ------------------------------------------------------------------ B: the classes
bio.panel(ax, "B", (0.3, 7.9))
CLS = ["Aplacophora", "Polyplacophora", "Monoplacophora", "Gastropoda", "Bivalvia", "Scaphopoda", "Cephalopoda"]
W = 4.2
for i, name in enumerate(CLS):
    x0 = 0.4 + i * W
    cx, cy = x0 + W / 2, 3.6
    bio.label(ax, (cx, 7.6), name, size="small", bold=True)
    if name == "Aplacophora":
        body = blob(ax, [(cx - 1.8, cy), (cx - 1.4, cy + 0.6), (cx + 1.4, cy + 0.6), (cx + 1.9, cy + 0.2), (cx + 1.8, cy - 0.4),
                         (cx + 1.0, cy - 0.6), (cx - 1.4, cy - 0.6)], MANTLE, z=4, face=wash(MANTLE, 0.6))
        for s in np.linspace(-1.5, 1.6, 22):
            ax.plot([cx + s, cx + s + 0.1], [cy + 0.62 - 0.04 * abs(s), cy + 0.85 - 0.04 * abs(s)], color=P.edge(SHELL), lw=1.0, zorder=5)
        ax.plot([cx - 1.2, cx + 1.2], [cy - 0.6, cy - 0.6], color=P.edge(FOOT), lw=2.5, zorder=6)
        curve(ax, [(cx - 1.7, cy), (cx, cy + 0.05), (cx + 1.7, cy - 0.05)], GUT, lw=2.0)
        bio.label(ax, (cx, 1.7), "Spicules; foot a ridge\nor absent", size="tiny", color=P.muted())
    elif name == "Polyplacophora":
        ax.add_patch(Ellipse((cx, cy - 0.45), 3.6, 0.7, facecolor=P.fill(FOOT), edgecolor=P.edge(FOOT), lw=0.9, zorder=3))
        blob(ax, [(cx - 1.8, cy - 0.3), (cx - 1.4, cy + 0.6), (cx + 1.4, cy + 0.6), (cx + 1.8, cy - 0.3)], MANTLE, z=4, face=wash(MANTLE, 0.6))
        for k in range(8):
            xx = cx - 1.5 + k * 0.43
            ax.add_patch(Ellipse((xx, cy + 0.65), 0.55, 0.32, angle=-12, facecolor=P.fill(SHELL), edgecolor=P.edge(SHELL), lw=0.8, zorder=6))
        curve(ax, [(cx - 1.6, cy - 0.15), (cx, cy + 0.1), (cx + 1.6, cy - 0.15)], GUT, lw=2.0)
        bio.label(ax, (cx, 1.7), "8 plates; many gills\nbeside the foot", size="tiny", color=P.muted())
    elif name == "Monoplacophora":
        ax.add_patch(Ellipse((cx, cy - 0.4), 3.2, 0.7, facecolor=P.fill(FOOT), edgecolor=P.edge(FOOT), lw=0.9, zorder=3))
        blob(ax, [(cx - 1.7, cy - 0.2), (cx - 1.2, cy + 0.9), (cx + 0.2, cy + 1.3), (cx + 1.7, cy - 0.2)], SHELL, z=4)
        for k in range(5):
            comb(ax, (cx - 1.1 + k * 0.55, cy - 0.15), (cx - 1.1 + k * 0.55, cy - 0.6), 3, GILL, w=0.12)
        curve(ax, [(cx - 1.5, cy - 0.05), (cx, cy + 0.35), (cx + 1.5, cy - 0.05)], GUT, lw=2.0)
        bio.label(ax, (cx, 1.7), "Cap-shaped shell;\nrepeated gills", size="tiny", color=P.muted())
    elif name == "Gastropoda":
        ax.add_patch(Ellipse((cx - 0.2, cy - 1.0), 3.4, 0.6, facecolor=P.fill(FOOT), edgecolor=P.edge(FOOT), lw=0.9, zorder=3))
        ax.add_patch(Circle((cx + 0.3, cy + 0.6), 1.25, facecolor=P.fill(SHELL), edgecolor=P.edge(SHELL), lw=1.0, zorder=4))
        th = np.linspace(0, 5 * np.pi, 200)
        r = 1.1 * np.exp(-0.17 * th)
        ax.plot(cx + 0.3 + r * np.cos(th), cy + 0.6 + r * np.sin(th), color=P.edge(SHELL), lw=0.9, zorder=5)
        ax.add_patch(Ellipse((cx - 0.75, cy + 0.0), 0.9, 0.55, facecolor=wash(MANTLE, 0.4), edgecolor=P.edge(MANTLE), lw=0.8, zorder=6))
        curve(ax, [(cx - 1.8, cy - 0.7), (cx - 0.4, cy - 0.2), (cx + 0.6, cy + 0.6), (cx - 0.2, cy + 0.4), (cx - 0.8, cy + 0.05)], GUT, lw=1.8)
        bio.label(ax, (cx, 1.7), "Coiled, twisted;\nmantle cavity in front", size="tiny", color=P.muted())
    elif name == "Bivalvia":
        blob(ax, [(cx - 1.8, cy + 0.1), (cx - 1.2, cy + 1.2), (cx + 0.6, cy + 1.3), (cx + 1.8, cy + 0.3), (cx + 1.2, cy - 0.9),
                  (cx - 1.0, cy - 0.9)], SHELL, z=3)
        blob(ax, [(cx - 1.5, cy + 0.1), (cx - 1.0, cy + 1.0), (cx + 0.6, cy + 1.05), (cx + 1.5, cy + 0.3), (cx + 1.0, cy - 0.65),
                  (cx - 0.8, cy - 0.65)], MANTLE, z=4, face=wash(MANTLE, 0.55))
        blob(ax, [(cx - 1.3, cy - 0.3), (cx - 0.9, cy + 0.2), (cx - 0.1, cy - 0.2), (cx - 0.5, cy - 1.0)], FOOT, z=5)
        curve(ax, [(cx - 1.1, cy + 0.5), (cx, cy + 0.85), (cx + 1.2, cy + 0.45)], GUT, lw=1.8)
        comb(ax, (cx + 0.0, cy + 0.2), (cx + 1.2, cy - 0.2), 4, GILL, w=0.2)
        bio.label(ax, (cx, 1.7), "Two valves; head\nreduced; large gills", size="tiny", color=P.muted())
    elif name == "Scaphopoda":
        t = np.linspace(0, 1, 50)
        xs = cx - 1.8 + 3.4 * t
        yc = cy + 0.6 * np.sin(np.pi * t * 0.8)
        w = 0.55 - 0.4 * t
        ax.fill(np.r_[xs, xs[::-1]], np.r_[yc + w, (yc - w)[::-1]], facecolor=P.fill(SHELL), edgecolor=P.edge(SHELL), lw=0.9, zorder=4)
        blob(ax, [(cx - 2.0, cy - 0.2), (cx - 2.3, cy - 0.7), (cx - 1.8, cy - 1.0), (cx - 1.5, cy - 0.4)], FOOT, z=5)
        for k in range(4):
            curve(ax, [(cx - 1.7, cy + 0.2), (cx - 2.0 - 0.1 * k, cy + 0.6 + 0.15 * k), (cx - 2.1 - 0.08 * k, cy + 0.9 + 0.2 * k)], "mrna", lw=0.8, z=6)
        curve(ax, [(cx - 1.6, cy), (cx - 0.2, cy + 0.6), (cx + 0.3, cy + 0.3)], GUT, lw=1.6, z=7)
        bio.label(ax, (cx, 1.7), "Tube open at both ends;\ncaptacula", size="tiny", color=P.muted())
    else:
        blob(ax, [(cx - 0.4, cy + 0.5), (cx + 0.2, cy + 0.9), (cx + 1.9, cy + 0.4), (cx + 1.9, cy - 0.3), (cx + 0.2, cy - 0.6),
                  (cx - 0.4, cy - 0.3)], MANTLE, z=4, face=wash(MANTLE, 0.55))
        ax.add_patch(Ellipse((cx + 1.0, cy + 0.15), 1.5, 0.35, facecolor=P.fill(SHELL), edgecolor=P.edge(SHELL), lw=0.8, zorder=5))
        ax.add_patch(Circle((cx - 0.55, cy + 0.1), 0.42, facecolor=wash(FOOT, 0.35), edgecolor=P.edge(FOOT), lw=0.8, zorder=5))
        for k in range(5):
            curve(ax, [(cx - 0.8, cy + 0.1), (cx - 1.4, cy + 0.4 - 0.25 * k), (cx - 2.0, cy + 0.6 - 0.4 * k)], FOOT, lw=1.6, z=4)
        curve(ax, [(cx - 0.2, cy - 0.45), (cx - 0.5, cy - 0.85)], FOOT, lw=3.0, z=6)
        bio.label(ax, (cx, 1.7), "Arms and funnel from\nthe foot; shell internal\nin squid", size="tiny", color=P.muted())
