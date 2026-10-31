# Length scales of life on a logarithmic axis from 0.1 nm to 100 m.
# Each object is placed at its characteristic size (largest dimension); icons are not drawn to scale
# with one another, only their positions on the axis carry the size.
# Below the axis: the ranges covered by electron microscopy, light microscopy and the naked eye, with the
# diffraction limit of light (about 200 nm) and the resolution of the eye (about 0.1 mm) marked.
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(17.0, 6.2)

X0, DEC = 0.9, 1.3  # canvas x of 1e-10 m, canvas units per decade
Y = 2.3             # axis height


def X(m):
    return X0 + DEC * (np.log10(m) + 10)


# axis
ax.plot([X(1e-10), X(1e2)], [Y, Y], color=P.ink(), lw=1.1, zorder=5)
names = {-10: "0.1 nm", -9: "1 nm", -8: "10 nm", -7: "100 nm", -6: "1 µm", -5: "10 µm", -4: "100 µm",
         -3: "1 mm", -2: "1 cm", -1: "10 cm", 0: "1 m", 1: "10 m", 2: "100 m"}
for e, t in names.items():
    x = X(10.0 ** e)
    ax.plot([x, x], [Y, Y - 0.12], color=P.ink(), lw=0.9, zorder=5)
    bio.label(ax, (x, Y - 0.22), t, size="tiny", va="top")
    if e < 2:
        for k in range(2, 10):
            xm = X(k * 10.0 ** e)
            ax.plot([xm, xm], [Y, Y - 0.06], color=P.muted(), lw=0.5, zorder=5)
bio.label(ax, (X(1e2) + 0.15, Y), "size", size="small", ha="left", color=P.muted())

# methods bands below the axis
bands = [(1e-10, 1e-4, 0.95, "electron microscopy", "dna"),
         (2e-7, 1e-3, 0.55, "light microscopy", "positive"),
         (1e-4, 1e2, 0.15, "naked eye", "neutral")]
for a, b, yy, txt, tok in bands:
    ax.add_patch(FancyBboxPatch((X(a), yy), X(b) - X(a), 0.3, boxstyle="round,pad=0,rounding_size=0.12",
                                         facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.7, zorder=3))
    bio.label(ax, ((X(a) + X(b)) / 2, yy + 0.15), txt, size="tiny", color=P.on_fill())
ax.plot([X(2e-7)] * 2, [0.55, 1.95], color=P.muted(), lw=0.6, ls=":", zorder=2)
bio.label(ax, (X(2e-7) + 0.05, 1.75), "diffraction limit", size="tiny", ha="left", color=P.muted())

# objects: (size in m, label, kind, extra)
items = [
    (1.0e-10, "atom\n(C, 0.15 nm)", "atom", None),
    (5.0e-9, "protein\n(5 nm)", "icon", ("dbcls/protein", 0.85, None)),
    (2.5e-8, "ribosome\n(25 nm)", "icon", ("bioicons/ribosome", 0.8, None)),
    (1.2e-7, "HIV virion\n(120 nm)", "icon", ("servier/hiv", 0.85, None)),
    (2.0e-6, "$\\it{E.\\ coli}$\n(2 µm)", "icon", ("phylopic/e-coli", 0.75, "positive")),
    (8.0e-6, "red blood cell\n(8 µm)", "icon", ("servier/red-blood-cell", 0.8, None)),
    (3.0e-5, "animal cell\n(10–30 µm)", "icon", ("servier/cell", 0.95, None)),
    (3.0e-3, "fruit fly\n(3 mm)", "icon", ("phylopic/drosophila", 0.8, "animal")),
    (9.0e-2, "mouse\n(9 cm)", "icon", ("phylopic/mouse", 0.75, "animal")),
    (1.7, "human\n(1.7 m)", "icon", ("phylopic/human", 1.1, "animal")),
    (2.5e1, "blue whale\n(25–30 m)", "icon", ("phylopic/baleen-whale", 0.55, "animal")),
]
for i, (size, txt, kind, extra) in enumerate(items):
    x = X(size)
    yc = 3.55
    ax.plot([x, x], [Y, Y + 0.45], color=P.muted(), lw=0.7, zorder=4)
    ax.add_patch(Circle((x, Y), 0.05, color=P.ink(), zorder=6))
    if kind == "atom":
        ax.add_patch(Circle((x, yc), 0.22, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.8, zorder=8))
        ax.add_patch(Circle((x, yc), 0.42, fill=False, edgecolor=P.muted(), lw=0.6, ls=(0, (2, 2)), zorder=8))
    else:
        icon_id, h, tok = extra
        if icon_id == "dbcls/protein":
            bio.icon(ax, "dbcls/protein", at=(x, yc), height=h)
        elif icon_id == "bioicons/ribosome":
            bio.icon(ax, "bioicons/ribosome", at=(x, yc), height=h)
        elif icon_id == "servier/hiv":
            bio.icon(ax, "servier/hiv", at=(x, yc), height=h)
        elif icon_id == "phylopic/e-coli":
            bio.icon(ax, "phylopic/e-coli", at=(x, yc), height=h, color=tok)
        elif icon_id == "servier/red-blood-cell":
            bio.icon(ax, "servier/red-blood-cell", at=(x, yc), height=h)
        elif icon_id == "servier/cell":
            bio.icon(ax, "servier/cell", at=(x, yc), height=h)
        elif icon_id == "phylopic/drosophila":
            bio.icon(ax, "phylopic/drosophila", at=(x, yc), height=h, color=tok)
        elif icon_id == "phylopic/mouse":
            bio.icon(ax, "phylopic/mouse", at=(x, yc), height=h, color=tok)
        elif icon_id == "phylopic/human":
            bio.icon(ax, "phylopic/human", at=(x, yc), height=h, color=tok)
        elif icon_id == "phylopic/baleen-whale":
            bio.icon(ax, "phylopic/baleen-whale", at=(x, yc), height=h, color=tok)
    ty = 4.55 if i % 2 == 0 else 5.45
    bio.label(ax, (x, ty), txt, size="tiny")

bio.label(ax, (0.3, 6.0), "Lengths of life (logarithmic scale)", size="small", ha="left", bold=True)
