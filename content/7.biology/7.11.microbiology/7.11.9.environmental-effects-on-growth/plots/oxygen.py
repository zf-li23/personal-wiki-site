# Oxygen classes and the detoxification of reactive oxygen species (schematic).
# A: growth in tubes of thioglycolate broth. Thioglycolate reduces O2 in the medium, so O2 enters only from the
#    surface; the redox dye resazurin is pink where the medium is oxidized (top band). Dots show where colonies
#    grow: obligate aerobes only at the surface; obligate anaerobes only in the depth; facultative anaerobes
#    throughout but most densely at the top (respiration yields more energy); microaerophiles in a band just
#    below the surface; aerotolerant anaerobes evenly throughout (they only ferment).
# B: the four-electron reduction of O2 to water, one electron at a time, with the reactive intermediates
#    superoxide, hydrogen peroxide and the hydroxyl radical (formed from H2O2 and Fe2+, the Fenton reaction),
#    and the enzymes that remove them: superoxide dismutase (SOD), superoxide reductase (SOR, in some strict
#    anaerobes; no O2 is produced), catalase and peroxidase.
import numpy as np
from matplotlib.patches import FancyBboxPatch, PathPatch, Rectangle
from matplotlib.path import Path

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27, 9.6)

# ---- A: tubes ---------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 9.5))
bio.label(ax, (0.9, 9.25), "Growth in thioglycolate broth", size="small", bold=True, ha="left")
names = ["obligate\naerobe", "obligate\nanaerobe", "facultative\nanaerobe", "micro-\naerophile", "aerotolerant\nanaerobe"]
rng = np.random.default_rng(4)
W, H, y0 = 1.25, 6.4, 1.6
broth = P.mix(P.fill("metabolite"), P.surface(), 0.75)
pink = P.mix(P.fill("receptor"), P.surface(), 0.35)
for k, name in enumerate(names):
    x = 0.8 + k * 2.4
    r = W / 2
    th = np.linspace(np.pi, 2 * np.pi, 40)
    body = np.r_[[[x, y0 + H - 0.6]], np.c_[x + r + r * np.cos(th), y0 + r + r * np.sin(th)], [[x + W, y0 + H - 0.6]]]
    ax.add_patch(PathPatch(Path(body), facecolor=broth, edgecolor="none", zorder=2))
    ax.add_patch(Rectangle((x, y0 + H - 1.25), W, 0.65, facecolor=pink, edgecolor="none", zorder=3))
    wall = np.r_[[[x, y0 + H]], np.c_[x + r + r * np.cos(th), y0 + r + r * np.sin(th)], [[x + W, y0 + H]]]
    ax.add_patch(PathPatch(Path(wall), fill=False, edgecolor=P.muted(), lw=1.2, zorder=5))
    top = y0 + H - 0.65
    # colony density as a function of depth d (0 at the surface)
    d = rng.uniform(0, H - 0.9, 900)
    if k == 0:
        p = np.exp(-d / 0.25)
    elif k == 1:
        p = 1 / (1 + np.exp(-(d - 2.0) / 0.25))
    elif k == 2:
        p = 0.35 + 0.65 * np.exp(-d / 0.5)
    elif k == 3:
        p = np.exp(-((d - 0.85) / 0.25) ** 2)
    else:
        p = np.full_like(d, 0.45)
    keep = rng.uniform(0, 1, d.size) < p * (1.0 if k in (0, 3) else 0.55)
    xs = rng.uniform(x + 0.12, x + W - 0.12, d.size)
    ys = top - d
    inside = ys > y0 + 0.15
    ax.scatter(xs[keep & inside], ys[keep & inside], s=3.5, color=P.edge("bacterium"), lw=0, zorder=4)
    bio.label(ax, (x + W / 2, y0 - 0.55), name, size="tiny")
bio.callout(ax, (0.8 + 4 * 2.4 + W, y0 + H - 0.95), (13.0, y0 + H - 0.4), "oxidized\n(resazurin\npink)", size="tiny")
bio.callout(ax, (0.8 + 4 * 2.4 + W, y0 + 2.5), (13.0, y0 + 2.5), "anoxic\n(reduced)", size="tiny")

# ---- B: reactive oxygen species -----------------------------------------------------------------------------
bio.panel(ax, "B", (14.0, 9.5))
bio.label(ax, (14.8, 9.25), "Reactive oxygen species and their removal", size="small", bold=True, ha="left")
yb = 6.6
xs = [15.3, 18.6, 21.9, 25.3]
labels = ["$\\mathrm{O_2}$", "$\\mathrm{O_2^{\\bullet-}}$\nsuperoxide", "$\\mathrm{H_2O_2}$\nhydrogen\nperoxide",
          "$\\mathrm{OH^{\\bullet}}$\nhydroxyl\nradical"]
toks = ["neutral", "negative", "highlight", "negative"]
for x, t, tok in zip(xs, labels, toks):
    bio.box(ax, (x, yb), 2.1, 1.35, token=tok, text=t, size="tiny")
for a, b in zip(xs[:-1], xs[1:]):
    bio.arrow(ax, (a + 1.1, yb), (b - 1.1, yb), kind="process", lw=1.2, head=0.18)
    bio.label(ax, ((a + b) / 2, yb + 0.35), "e$^-$", size="tiny")
bio.label(ax, (23.6, yb - 0.4), "Fe$^{2+}$", size="tiny", color=P.muted())
bio.label(ax, (25.3, yb - 1.25), "+ e$^-$ → H$_2$O", size="tiny", color=P.muted())
bio.label(ax, (20.3, yb + 1.25), "each step adds one electron; only water is harmless", size="tiny", color=P.muted())

# enzymes
bio.box(ax, (18.4, 3.6), 3.2, 1.6, token="enzyme",
        text="superoxide dismutase\n$2\\,\\mathrm{O_2^{\\bullet-}} + 2\\,\\mathrm{H^+}$\n$\\to \\mathrm{H_2O_2} + \\mathrm{O_2}$", size="tiny")
bio.box(ax, (18.4, 1.3), 3.2, 1.6, token="enzyme",
        text="superoxide reductase\n$\\mathrm{O_2^{\\bullet-}} + 2\\,\\mathrm{H^+} + \\mathrm{e^-}$\n$\\to \\mathrm{H_2O_2}$ (no $\\mathrm{O_2}$)", size="tiny")
bio.box(ax, (22.0, 3.6), 3.2, 1.6, token="enzyme",
        text="catalase\n$2\\,\\mathrm{H_2O_2} \\to 2\\,\\mathrm{H_2O} + \\mathrm{O_2}$", size="tiny")
bio.box(ax, (22.0, 1.3), 3.2, 1.6, token="enzyme",
        text="peroxidase\n$\\mathrm{H_2O_2} + \\mathrm{NADH} + \\mathrm{H^+}$\n$\\to 2\\,\\mathrm{H_2O} + \\mathrm{NAD^+}$", size="tiny")
bio.arrow(ax, (18.5, yb - 0.7), (18.5, 4.42), kind="link", lw=1.0, color=P.muted())
bio.arrow(ax, (21.95, yb - 0.7), (21.95, 4.42), kind="link", lw=1.0, color=P.muted())
bio.label(ax, (16.4, 4.9), "remove superoxide", size="tiny", color=P.muted(), ha="center")
bio.label(ax, (24.1, 4.9), "remove peroxide", size="tiny", color=P.muted(), ha="center")
bio.label(ax, (25.6, 3.6), "aerobes and\nfacultative anaerobes:\nSOD + catalase", size="tiny", ha="center")
bio.label(ax, (25.6, 1.3), "some strict\nanaerobes:\nSOR instead of SOD", size="tiny", ha="center", color=P.muted())
