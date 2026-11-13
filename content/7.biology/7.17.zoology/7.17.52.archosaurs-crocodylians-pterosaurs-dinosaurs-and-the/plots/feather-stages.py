# The developmental model of feather evolution (Prum 1999; Prum and Brush 2002), schematic. Each stage adds
# one developmental novelty of the feather follicle: I, a single hollow cylinder (the follicle collar);
# II, a tuft of barbs fused at the base (barb ridges in the collar); IIIa, barbs fused to a central rachis
# (helical growth of barb ridges); IIIb, barbs with barbules (differentiation of barbule plates); IIIa+b and
# IV, a closed pennaceous vane in which hooked distal barbules interlock with grooved proximal ones; V,
# asymmetrical flight feathers and other specializations. Below: fossil taxa with feathers of each stage
# (examples from the Jehol and Yanliao biotas of northeastern China and from Solnhofen; assignments of
# fossil integument to stages are partly uncertain).
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27, 10.5)
INK = P.edge("lipid")
FILL = P.fill("lipid")


def line(pts, lw=1.4, c=None):
    pts = np.asarray(pts)
    ax.plot(pts[:, 0], pts[:, 1], color=c or INK, lw=lw, solid_capstyle="round", zorder=6)


def tube(x, y, h, w=0.22):
    bio.shape(ax, [(x - w / 2, y), (x + w / 2, y), (x + w / 2, y + h), (x - w / 2, y + h)], token="lipid", lw=1.0)


def barbs_tuft(x, y, h, n=7, spread=0.9):
    tube(x, y, 0.5)
    for k in range(n):
        a = np.radians(90 + (k - (n - 1) / 2) * spread * 12)
        line([(x, y + 0.5), (x + h * np.cos(a), y + 0.5 + h * np.sin(a))], lw=1.1)


def vane(x, y, h, w=0.8, barbules=False, closed=False, asym=1.0):
    tube(x, y, 0.6)
    line([(x, y + 0.6), (x, y + h)], lw=2.0)
    ys = np.linspace(y + 0.9, y + h - 0.2, 11)
    for yy in ys:
        frac = (yy - y) / h
        wl = w * np.sin(np.pi * min(0.98, frac + 0.05)) * (2 - asym)
        wr = w * np.sin(np.pi * min(0.98, frac + 0.05)) * asym
        for side, ww in ((-1, wl), (1, wr)):
            end = (x + side * ww, yy + 0.35 * ww)
            line([(x, yy), end], lw=1.0)
            if barbules:
                for t in np.linspace(0.25, 0.85, 3):
                    p = (x + side * ww * t, yy + 0.35 * ww * t)
                    line([p, (p[0] + side * 0.12, p[1] + 0.16)], lw=0.6)
    if closed:
        pts = [(x, y + 0.75)]
        for yy in ys:
            frac = (yy - y) / h
            pts.append((x - w * np.sin(np.pi * min(0.98, frac + 0.05)) * (2 - asym), yy + 0.35 * w * np.sin(np.pi * min(0.98, frac + 0.05)) * (2 - asym)))
        pts.append((x, y + h + 0.15))
        for yy in ys[::-1]:
            frac = (yy - y) / h
            pts.append((x + w * np.sin(np.pi * min(0.98, frac + 0.05)) * asym, yy + 0.35 * w * np.sin(np.pi * min(0.98, frac + 0.05)) * asym))
        bio.shape(ax, pts, token="lipid", lw=0.9, zorder=4, alpha=0.45)


X = [2.0, 5.6, 9.2, 12.8, 16.6, 20.6, 24.6]
Y = 3.6
titles = ["I", "II", "IIIa", "IIIb", "IIIa+b", "IV", "V"]
subs = ["hollow filament", "tuft of barbs", "barbs on a rachis", "barbs with barbules",
        "open vane", "closed vane", "asymmetric vane"]
fossils = ["Sinosauropteryx, Beipiaosaurus", "Sinornithosaurus, Dilong", "(rarely preserved)", "(not known alone)",
           "contour feathers of paravians", "Caudipteryx, Anchiornis", "Microraptor, Archaeopteryx"]
line([(X[0], Y), (X[0], Y + 4.0)], lw=4.0)
barbs_tuft(X[1], Y, 3.4)
tube(X[2], Y, 0.6)
line([(X[2], Y + 0.6), (X[2], Y + 4.2)], lw=2.0)
for yy in np.linspace(Y + 1.0, Y + 4.0, 8):
    for s in (-1, 1):
        line([(X[2], yy), (X[2] + s * 0.7, yy + 0.4)], lw=1.0)
barbs_tuft(X[3], Y, 3.4)
for k in range(7):
    a = np.radians(90 + (k - 3) * 0.9 * 12)
    for t in (0.35, 0.6, 0.85):
        p = (X[3] + 3.4 * t * np.cos(a), Y + 0.5 + 3.4 * t * np.sin(a))
        line([p, (p[0] + 0.15, p[1] + 0.12)], lw=0.6)
        line([p, (p[0] - 0.15, p[1] + 0.12)], lw=0.6)
vane(X[4], Y, 4.4, w=0.9, barbules=True)
vane(X[5], Y, 4.4, w=0.9, barbules=False, closed=True)
vane(X[6], Y, 4.4, w=0.95, barbules=False, closed=True, asym=0.55)
for i, x in enumerate(X):
    bio.label(ax, (x, 9.7), titles[i], size="normal", bold=True)
    bio.label(ax, (x, 9.15), subs[i], size="tiny", color=P.muted())
    bio.label(ax, (x, 2.9), fossils[i], size="tiny", italic=True)
for a, b in zip(X[:-1], X[1:]):
    bio.arrow(ax, (a + 1.0, 1.9), (b - 1.0, 1.9), kind="process", head=0.16)
bio.label(ax, (13.4, 1.2), "each stage requires the follicle novelty of the previous one", size="tiny",
          color=P.muted())
bio.label(ax, (13.4, 0.55), "follicle collar -> barb ridges -> helical growth -> barbules -> hooklets -> asymmetry",
          size="tiny", color=P.muted())
