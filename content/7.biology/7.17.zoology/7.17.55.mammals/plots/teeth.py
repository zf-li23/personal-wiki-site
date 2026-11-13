# (A) Heterodont dentition of a generalized placental mammal (the ancestral formula I 3/3, C 1/1, P 4/4,
# M 3/3 = 44, close to that of the pig), left side in lateral view, with the tooth classes coloured, and the
# dental formulae of some representative species. (B) Occlusal (crown) views of upper molars of the main
# crown types (schematic): tribosphenic (opossum, insectivores), bunodont with low rounded cusps (pig,
# primates), selenodont with crescent-shaped ridges (deer, cattle), lophodont with transverse ridges
# (rhinoceros, tapir), and the secodont carnassial blade formed by the upper fourth premolar and lower first
# molar of carnivorans (cat). Cusps and ridges in dark shading.
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(25, 12.5)
COL = {"I": "dna", "C": "mrna", "P": "positive", "M": "highlight"}


def tooth(x, y, w, h, kind, up=True, cusps=1):
    s = 1 if up else -1
    base = y
    tip = y - s * h
    if kind == "C":
        pts = [(x, base), (x + w, base), (x + w * 0.55, tip), (x + w * 0.4, tip + s * 0.1)]
    elif kind == "I":
        pts = [(x, base), (x + w, base), (x + w * 0.85, tip), (x + w * 0.15, tip)]
    else:
        pts = [(x, base), (x + w, base)]
        for k in range(cusps, 0, -1):
            xc = x + w * (k - 0.5) / cusps
            pts += [(xc + w / cusps * 0.35, tip + s * 0.18), (xc, tip), (xc - w / cusps * 0.35, tip + s * 0.18)]
    bio.shape(ax, pts, token=COL[kind], lw=0.9, zorder=6)


row = [("I", 0.45, 0.9, 1)] * 3 + [("C", 0.6, 1.6, 1)] + [("P", 0.8, 0.95, 1)] * 2 + [("P", 0.9, 1.0, 2)] * 2 + \
      [("M", 1.15, 1.0, 3)] * 3
x = 1.0
for kind, w, h, c in row:
    tooth(x, 9.4, w, h, kind, up=True, cusps=c)
    tooth(x + 0.05, 6.9, w, h * 0.95, kind, up=False, cusps=c)
    x += w + 0.12
ax.plot([0.8, x], [9.4, 9.4], color=P.muted(), lw=1.2)
ax.plot([0.8, x], [6.9, 6.9], color=P.muted(), lw=1.2)
bio.label(ax, (0.6, 9.9), "upper jaw", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (0.6, 6.4), "lower jaw", size="tiny", color=P.muted(), ha="left")
for i, (k, name) in enumerate((("I", "incisors 3"), ("C", "canine 1"), ("P", "premolars 4"), ("M", "molars 3"))):
    bio.box(ax, (1.4 + 2.6 * i, 5.5), 0.4, 0.3, token=COL[k])
    bio.label(ax, (1.8 + 2.6 * i, 5.5), name, size="tiny", ha="left")
bio.label(ax, (5.5, 11.6), "I 3/3  C 1/1  P 4/4  M 3/3  = 44", size="normal", bold=True)
bio.panel(ax, "A", (0.4, 12.5))
F = [("pig", "3.1.4.3 / 3.1.4.3 = 44"), ("dog", "3.1.4.2 / 3.1.4.3 = 42"), ("cat", "3.1.3.1 / 3.1.2.1 = 30"),
     ("human", "2.1.2.3 / 2.1.2.3 = 32"), ("rabbit", "2.0.3.3 / 1.0.2.3 = 28"), ("rat", "1.0.0.3 / 1.0.0.3 = 16"),
     ("cattle", "0.0.3.3 / 3.1.3.3 = 32"), ("opossum", "5.1.3.4 / 4.1.3.4 = 50")]
bio.label(ax, (1.0, 4.5), "Dental formulae (upper / lower; I.C.P.M)", size="small", bold=True, ha="left")
for i, (sp, f) in enumerate(F):
    yy = 3.8 - 0.55 * (i % 4)
    xx = 1.0 + 6.0 * (i // 4)
    bio.label(ax, (xx, yy), sp, size="tiny", ha="left")
    bio.label(ax, (xx + 1.6, yy), f, size="tiny", ha="left")

# (B) occlusal patterns
bio.panel(ax, "B", (14.2, 12.5))
cx = [15.6, 19.0, 22.4, 15.6, 19.0]
cy = [9.6, 9.6, 9.6, 4.6, 4.6]
names = ["tribosphenic", "bunodont", "selenodont", "lophodont", "secodont (carnassial)"]
ex = ["opossum, shrews", "pig, primates", "deer, cattle", "rhinoceros, tapir", "cat, dog"]
dark = "neutral"
for i in range(5):
    x0, y0 = cx[i], cy[i]
    if i == 4:
        outline = [(x0 - 1.4, y0 - 0.6), (x0 + 1.4, y0 - 0.6), (x0 + 1.2, y0 + 0.4), (x0 - 1.3, y0 + 0.5)]
    elif i == 0:
        outline = [(x0 - 1.3, y0 + 1.0), (x0 + 1.3, y0 + 1.0), (x0 + 0.3, y0 - 1.2)]
    else:
        outline = bio.smooth_closed([(x0 - 1.3, y0 - 1.1), (x0 + 1.3, y0 - 1.1), (x0 + 1.35, y0 + 1.1),
                                     (x0 - 1.35, y0 + 1.1)]).tolist() if hasattr(bio, "smooth_closed") else \
            [(x0 - 1.3, y0 - 1.1), (x0 + 1.3, y0 - 1.1), (x0 + 1.35, y0 + 1.1), (x0 - 1.35, y0 + 1.1)]
    bio.shape(ax, outline, token="bone", lw=1.0, zorder=5)
    if i == 0:
        for (px, py, nm) in ((x0 - 0.75, y0 + 0.65, "pa"), (x0 + 0.75, y0 + 0.65, "me"), (x0 + 0.15, y0 - 0.7, "pr")):
            bio.shape(ax, np.c_[px + 0.28 * np.cos(np.linspace(0, 6.28, 30)), py + 0.28 * np.sin(np.linspace(0, 6.28, 30))].tolist(), token=dark, zorder=6)
            bio.label(ax, (px, py), nm, size="tiny", color=P.on_fill())
    elif i == 1:
        for px in (x0 - 0.6, x0 + 0.6):
            for py in (y0 - 0.5, y0 + 0.5):
                bio.shape(ax, np.c_[px + 0.35 * np.cos(np.linspace(0, 6.28, 30)), py + 0.35 * np.sin(np.linspace(0, 6.28, 30))].tolist(), token=dark, zorder=6)
    elif i == 2:
        for px in (x0 - 0.6, x0 + 0.6):
            for py in (y0 - 0.5, y0 + 0.5):
                a = np.linspace(-1.2, 1.2, 20)
                arc = np.c_[px - 0.15 + 0.4 * np.cos(a), py + 0.45 * np.sin(a)]
                ax.plot(arc[:, 0], arc[:, 1], color=P.edge(dark), lw=3.0, zorder=6, solid_capstyle="round")
    elif i == 3:
        ax.plot([x0 - 1.1, x0 + 1.1], [y0 + 0.9, y0 + 0.9], color=P.edge(dark), lw=3.5, zorder=6)
        ax.plot([x0 - 1.0, x0 + 0.6], [y0 + 0.7, y0 - 0.2], color=P.edge(dark), lw=3.5, zorder=6)
        ax.plot([x0 - 1.0, x0 + 0.6], [y0 - 0.1, y0 - 0.95], color=P.edge(dark), lw=3.5, zorder=6)
    else:
        ax.plot([x0 - 1.2, x0 - 0.3, x0 + 0.2, x0 + 1.1], [y0 + 0.2, y0 - 0.1, y0 + 0.15, y0 - 0.15],
                color=P.edge(dark), lw=3.5, zorder=6)
    bio.label(ax, (x0, y0 - 1.7), names[i], size="small", bold=True)
    bio.label(ax, (x0, y0 - 2.2), ex[i], size="tiny", color=P.muted())
bio.label(ax, (22.4, 4.6), "pa paracone\nme metacone\npr protocone", size="tiny", color=P.muted(), ha="center")
