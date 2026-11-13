# Horns and antlers of mammals in schematic longitudinal section (skull surface at the bottom), after
# Kardong (2019) and Davis et al. (2011): bovid horn, pronghorn, antler (in velvet and hard), rhinoceros horn,
# giraffe ossicone. Bone in one colour, keratin in another, skin in a third. Not to scale.
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30, 10)
titles = ["Bovid horn", "Pronghorn", "Antler", "Rhinoceros horn", "Ossicone"]
subs = ["permanent sheath", "sheath shed yearly", "bone shed yearly", "keratin only", "skin-covered"]
xs = [3.0, 9.0, 15.0, 21.0, 27.0]


def skull(x):
    bio.shape(ax, [(x - 2.6, 1.0), (x + 2.6, 1.0), (x + 2.6, 2.0), (x - 2.6, 2.0)], token="bone", lw=0.8)
    bio.label(ax, (x, 1.5), "skull", size="tiny", color=P.on_fill())


for x, t, s in zip(xs, titles, subs):
    bio.label(ax, (x, 9.4), t, size="small", bold=True)
    bio.label(ax, (x, 8.8), s, size="tiny", color=P.muted())
    skull(x)

x = xs[0]
bio.shape(ax, bio.smooth_closed([(x - 1.3, 2.0), (x + 1.3, 2.0), (x + 0.9, 5.0), (x + 0.2, 8.0), (x - 0.4, 5.5)]), token="metabolite")
bio.shape(ax, bio.smooth_closed([(x - 0.8, 2.0), (x + 0.8, 2.0), (x + 0.5, 4.6), (x + 0.1, 6.4), (x - 0.3, 4.8)]), token="bone", zorder=6)
bio.callout(ax, (x, 3.6), (x + 1.9, 4.6), "bony core", size="tiny")
bio.callout(ax, (x + 0.5, 6.4), (x + 1.9, 7.4), "keratin sheath", size="tiny")

x = xs[1]
bio.shape(ax, bio.smooth_closed([(x - 0.9, 2.0), (x + 0.9, 2.0), (x + 0.4, 4.4), (x, 5.2), (x - 0.4, 4.2)]), token="bone", zorder=6)
sheath = bio.smooth_closed([(x - 1.3, 2.0), (x + 1.3, 2.0), (x + 1.0, 4.2), (x + 2.0, 5.2), (x + 0.9, 5.0),
                            (x + 0.5, 7.6), (x - 0.2, 8.1), (x - 0.6, 5.6)])
bio.shape(ax, sheath, token="metabolite")
bio.callout(ax, (x + 1.7, 5.05), (x + 2.2, 6.4), "prong", size="tiny")

x = xs[2]
bio.shape(ax, [(x - 0.5, 2.0), (x + 0.5, 2.0), (x + 0.5, 3.0), (x - 0.5, 3.0)], token="bone", zorder=6)
bio.shape(ax, [(x - 0.75, 3.0), (x + 0.75, 3.0), (x + 0.75, 3.3), (x - 0.75, 3.3)], token="bone", zorder=7, lw=1.4)
for (a, b, c, d) in (((x, 3.3), (x - 0.3, 8.0), 0.3, 0.22), ((x - 0.1, 5.0), (x - 1.8, 6.6), 0.22, 0.15),
                     ((x - 0.2, 6.6), (x + 1.6, 8.0), 0.2, 0.14), ((x, 4.0), (x + 1.7, 5.0), 0.2, 0.14)):
    v = np.array(b) - np.array(a)
    n = np.array([-v[1], v[0]]) / np.hypot(*v)
    pts = [tuple(np.array(a) + n * c), tuple(np.array(b) + n * d), tuple(np.array(b) - n * d), tuple(np.array(a) - n * c)]
    bio.shape(ax, pts, token="bone", zorder=6)
bio.callout(ax, (x, 2.5), (x + 1.9, 2.6), "pedicle", size="tiny")
bio.callout(ax, (x + 0.7, 3.15), (x + 2.0, 3.6), "burr: shed here", size="tiny")
bio.label(ax, (x - 1.6, 4.0), "velvet (skin)\nwhile growing", size="tiny", color=P.muted())

x = xs[3]
bio.shape(ax, [(x - 1.2, 2.0), (x + 1.2, 2.0), (x + 1.0, 2.35), (x - 1.0, 2.35)], token="bone", zorder=6, lw=1.4)
horn = bio.smooth_closed([(x - 1.6, 2.35), (x + 1.6, 2.35), (x + 0.8, 4.5), (x - 0.2, 7.8), (x - 0.6, 4.6)])
bio.shape(ax, horn, token="metabolite")
for k in range(5):
    ax.plot([x - 1.0 + 0.5 * k, x - 0.5 + 0.2 * k], [2.5, 6.0 - abs(k - 2) * 0.6], color=P.edge("metabolite"), lw=0.6, zorder=7)
bio.callout(ax, (x + 1.0, 2.2), (x + 2.0, 3.2), "nasal boss", size="tiny")
bio.callout(ax, (x - 0.1, 5.5), (x + 1.8, 6.5), "keratin tubules", size="tiny")

x = xs[4]
bio.shape(ax, bio.smooth_closed([(x - 1.1, 2.0), (x + 1.1, 2.0), (x + 0.9, 4.8), (x + 0.7, 5.9), (x - 0.7, 5.9), (x - 0.9, 4.8)]), token="animal")
bio.shape(ax, bio.smooth_closed([(x - 0.7, 2.0), (x + 0.7, 2.0), (x + 0.6, 4.6), (x + 0.4, 5.5), (x - 0.4, 5.5), (x - 0.6, 4.6)]), token="bone", zorder=6)
bio.callout(ax, (x, 4.0), (x + 1.8, 7.0), "ossified dermal cartilage", size="tiny")
bio.callout(ax, (x - 0.9, 5.0), (x - 1.5, 7.4), "skin with hair", size="tiny")

for i, (tok, t) in enumerate((("bone", "bone"), ("metabolite", "keratin"), ("animal", "skin"))):
    xx = 8 + i * 6
    bio.shape(ax, [(xx, 0.2), (xx + 0.5, 0.2), (xx + 0.5, 0.6), (xx, 0.6)], token=tok, lw=0.6)
    bio.label(ax, (xx + 0.7, 0.4), t, size="tiny", ha="left")
