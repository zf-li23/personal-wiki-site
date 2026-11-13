# Tooth attachment (schematic transverse sections of a lower jaw, labial side to the left) and tooth
# replacement over time. Not to scale.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax = bio.canvas(24, 10.4)

ENAMEL, DENTINE, PULP = "lipid_tail", "bone", "blood"


def tooth(cx, base, h, w, tilt=0.0, z=6, small=False):
    """A conical tooth standing on y=base: dentine with a pulp cavity and an enamel cap."""
    s = 0.6 if small else 1.0
    h, w = h * s, w * s
    outer = vs.smooth([(cx - w / 2, base), (cx - w * 0.45, base + h * 0.55), (cx - w * 0.2 + tilt, base + h * 0.92),
                       (cx + tilt, base + h), (cx + w * 0.2 + tilt, base + h * 0.92), (cx + w * 0.45, base + h * 0.55),
                       (cx + w / 2, base)])
    bio.shape(ax, outer, token=DENTINE, zorder=z, lw=0.8)
    cap = vs.smooth([(cx - w * 0.4, base + h * 0.62), (cx - w * 0.2 + tilt, base + h * 0.93), (cx + tilt, base + h * 1.01),
                     (cx + w * 0.2 + tilt, base + h * 0.93), (cx + w * 0.4, base + h * 0.62), (cx + tilt * 0.5, base + h * 0.7)])
    bio.shape(ax, cap, token=ENAMEL, zorder=z + 0.5, lw=0.7)
    pulp = vs.smooth([(cx - w * 0.15, base), (cx - w * 0.08, base + h * 0.5), (cx + tilt * 0.5, base + h * 0.6),
                      (cx + w * 0.08, base + h * 0.5), (cx + w * 0.15, base)])
    bio.shape(ax, pulp, token=PULP, zorder=z + 0.4, lw=0.5)


def title(x, y, s):
    bio.label(ax, (x, y), s, size="small", ha="left")


# A shark: cartilage jaw with connective tissue and tooth rows
x0, y0 = 0.8, 5.6
title(x0, 9.9, "A  Shark")
bio.shape(ax, vs.smooth([(x0 + 0.3, y0), (x0 + 0.2, y0 + 1.6), (x0 + 1.4, y0 + 2.1), (x0 + 2.8, y0 + 1.6), (x0 + 2.6, y0)]),
          token="extracellular", zorder=3)
ax.fill([x0 + 0.5, x0 + 2.4, x0 + 2.3, x0 + 0.6], [y0 + 0.2, y0 + 0.2, y0 + 1.4, y0 + 1.4], color=vs.light("chondrocranium"),
        ec=vs.edge("chondrocranium"), lw=0.8, zorder=4)
tooth(x0 + 0.9, y0 + 2.0, 1.3, 0.8)
tooth(x0 + 1.7, y0 + 1.6, 1.0, 0.7, tilt=0.3, small=True)
tooth(x0 + 2.4, y0 + 1.0, 1.0, 0.7, tilt=0.5, small=True)
bio.callout(ax, (x0 + 1.4, y0 + 0.8), (x0 + 1.2, y0 - 0.5), "jaw cartilage", size="tiny")
bio.callout(ax, (x0 + 2.4, y0 + 1.2), (x0 + 3.3, y0 + 3.6), "replacement rows in connective tissue", size="tiny")


def jaw(x0, y0, kind):
    if kind == "acrodont":
        bone = vs.smooth([(x0 + 0.3, y0), (x0 + 0.2, y0 + 1.6), (x0 + 1.4, y0 + 2.05), (x0 + 2.6, y0 + 1.6), (x0 + 2.5, y0)])
        bio.shape(ax, bone, token="neutral", zorder=4)
        tooth(x0 + 1.4, y0 + 1.95, 1.4, 0.9)
    elif kind == "pleurodont":
        bone = np.array([(x0 + 0.3, y0), (x0 + 0.3, y0 + 2.6), (x0 + 0.9, y0 + 2.6), (x0 + 1.0, y0 + 1.2), (x0 + 2.5, y0 + 1.2),
                         (x0 + 2.5, y0)])
        bio.shape(ax, vs.smooth(bone) if False else bone, token="neutral", zorder=4)
        tooth(x0 + 1.4, y0 + 1.15, 2.1, 0.8)
        tooth(x0 + 2.1, y0 + 1.2, 0.8, 0.5, small=True)
    else:
        bone = np.array([(x0 + 0.3, y0), (x0 + 0.3, y0 + 2.2), (x0 + 0.85, y0 + 2.2), (x0 + 0.95, y0 + 0.9), (x0 + 1.85, y0 + 0.9),
                         (x0 + 1.95, y0 + 2.2), (x0 + 2.5, y0 + 2.2), (x0 + 2.5, y0)])
        bio.shape(ax, bone, token="neutral", zorder=4)
        lig = np.array([(x0 + 0.88, y0 + 2.15), (x0 + 0.98, y0 + 0.85), (x0 + 1.82, y0 + 0.85), (x0 + 1.92, y0 + 2.15),
                        (x0 + 1.8, y0 + 2.15), (x0 + 1.72, y0 + 0.97), (x0 + 1.08, y0 + 0.97), (x0 + 1.0, y0 + 2.15)])
        bio.shape(ax, lig, token="muscle", zorder=5, lw=0.5)
        tooth(x0 + 1.4, y0 + 0.97, 2.6, 0.75)


for i, (k, lab) in enumerate((("acrodont", "B  Acrodont"), ("pleurodont", "C  Pleurodont"), ("thecodont", "D  Thecodont"))):
    xx = 6.6 + 5.6 * i
    title(xx, 9.9, lab)
    jaw(xx, y0, k)
bio.callout(ax, (6.6 + 1.4, y0 + 1.95), (6.6 + 3.0, y0 - 0.5), "fused to the crest", size="tiny")
bio.callout(ax, (12.2 + 0.6, y0 + 2.2), (12.2 - 0.2, y0 + 3.6), "labial wall", size="tiny")
bio.callout(ax, (12.2 + 2.1, y0 + 1.5), (12.2 + 3.2, y0 + 3.6), "replacement tooth (lingual)", size="tiny")
bio.callout(ax, (17.8 + 1.77, y0 + 1.5), (17.8 + 3.3, y0 + 3.6), "periodontal ligament", size="tiny")
bio.callout(ax, (17.8 + 0.5, y0 + 1.0), (17.8 + 3.3, y0 - 0.5), "socket in jaw bone", size="tiny")
lx = 1.0
for tok, txt in ((ENAMEL, "enamel / enameloid"), (DENTINE, "dentine"), (PULP, "pulp"), ("neutral", "bone"),
                 ("extracellular", "connective tissue")):
    bio.shape(ax, np.array([(lx, 4.4), (lx + 0.4, 4.4), (lx + 0.4, 4.7), (lx, 4.7)]), token=tok, lw=0.6)
    bio.label(ax, (lx + 0.55, 4.55), txt, size="tiny", ha="left")
    lx += 3.6

# E replacement over time
title(0.8, 3.7, "E  Replacement at five tooth positions over life (bars: one tooth generation)")
rows = [("polyphyodont", [(p, s, 2.2) for p in range(5) for s in np.arange(0.0 + (p % 2) * 1.1, 11, 2.2)]),
        ("diphyodont", [(p, 0.3, 3.0) for p in range(3)] + [(p, 3.3, 7.7) for p in range(3)] + [(p, 2.0, 9.0) for p in (3, 4)]),
        ("monophyodont", [(p, 0.3, 10.7) for p in range(5)])]
for r, (name, bars) in enumerate(rows):
    yb = 2.6 - r * 1.05
    bio.label(ax, (3.6, yb + 0.35), name, size="tiny", ha="right")
    for p, s, d in bars:
        s0, s1 = max(s, 0.0), min(s + d, 11.0)
        if s1 <= s0:
            continue
        tok = "dna" if (name != "diphyodont" or p > 2 or s > 1) else "rrna"
        X0, X1 = 4.0 + s0 * 1.7, 4.0 + s1 * 1.7 - 0.06
        yy = yb + p * 0.15
        ax.fill([X0, X1, X1, X0], [yy, yy, yy + 0.12, yy + 0.12], color=P.fill(tok), ec=P.edge(tok), lw=0.4, zorder=5)
ax.annotate("", (23.2, 0.1), (4.0, 0.1), arrowprops=dict(arrowstyle="-|>", color=P.muted(), lw=0.9))
bio.label(ax, (23.2, -0.2), "age", size="tiny", ha="right", color=P.muted())
bio.label(ax, (3.6, 1.25), "(red: milk teeth)", size="tiny", ha="right", color=P.muted())
