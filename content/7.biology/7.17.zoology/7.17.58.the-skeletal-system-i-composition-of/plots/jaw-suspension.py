# Types of jaw suspension, schematic left lateral views (anterior to the left), after Kardong (2019) and
# Grogan & Lund: braincase (chondrocranium, context), palatoquadrate/quadrate (gold), Meckel's cartilage /
# articular (coral), hyomandibula/stapes (magenta), dentary and squamosal (dermal). Ligaments dashed. Not to scale.
import wikibio as bio
import vertskel as vs

P = bio.P
titles = ["Paleostyly", "Euautostyly", "Amphistyly", "Hyostyly", "Metautostyly", "Craniostyly"]
subs = ["cyclostomes", "placoderms, acanthodians", "early sharks, hexanchids", "most sharks, teleosts",
        "amphibians, reptiles, birds", "mammals"]
fig, ax, boxes = vs.panels(6, 8.0, 5.0, titles=titles, subtitles=subs, ncols=3, legend_rows=2, gap=0.8)
CASE = [("chondrocranium", vs.smooth([(0.6, 3.4), (2.5, 4.4), (6.5, 4.5), (7.6, 3.8), (7.4, 2.9), (4.0, 2.9), (1.0, 2.9)]))]


def lig(a, b, at):
    ax.plot([at[0] + a[0], at[0] + b[0]], [at[1] + a[1], at[1] + b[1]], color=P.ink(), lw=1.0, ls="--", zorder=9)


for i, (x, y, w, h) in enumerate(boxes):
    at = (x, y)
    vs.draw(ax, CASE, at=at)
    if i == 0:
        for k in range(4):
            vs.draw(ax, [("arch_%d" % (k + 3), vs.rod((2.2 + 1.3 * k, 2.6), (2.6 + 1.3 * k, 0.6), 0.25))], at=at)
        vs.draw(ax, [("epipterygoid", vs.rod((1.0, 2.6), (1.3, 1.2), 0.25), {"state": "cartilage"})], at=at)
        bio.label(ax, (x + 4.0, y + 0.1), "arches not attached; no jaws", size="tiny", color=P.muted())
        continue
    if i in (1, 2, 3):
        pq = vs.smooth([(1.2, 2.3), (3.0, 2.75), (5.6, 2.6), (5.9, 2.0), (3.5, 1.9), (1.3, 1.9)])
        mk = vs.smooth([(1.2, 1.75), (5.9, 1.85), (6.1, 1.4), (3.5, 1.05), (1.2, 1.4)])
        a = vs.draw(ax, [("palatoquadrate", pq), ("meckel", mk)], at=at)
        if i == 1:
            vs.draw(ax, [("palatoquadrate", vs.rod((4.8, 2.5), (5.2, 2.95), 0.35))], at=at)
            vs.draw(ax, [("hyomandibula", vs.rod((6.7, 2.8), (6.8, 1.0), 0.28))], at=at)
        if i == 2:
            lig((1.8, 2.5), (1.8, 2.95), at)
            vs.draw(ax, [("hyomandibula", vs.rod((6.8, 2.95), (6.0, 1.8), 0.32))], at=at)
        if i == 3:
            lig((2.0, 2.45), (2.3, 2.95), at)
            vs.draw(ax, [("hyomandibula", vs.rod((7.0, 2.95), (6.2, 1.6), 0.38))], at=at)
        continue
    if i == 4:
        a = vs.draw(ax, [("dentary", vs.smooth([(0.8, 1.7), (5.8, 1.9), (6.2, 1.3), (3.0, 1.0), (0.8, 1.3)])),
                         ("quadrate", vs.rod((6.4, 2.95), (6.3, 1.7), 0.45)),
                         ("articular", vs.oval((6.25, 1.5), 0.35, 0.25)),
                         ("stapes", vs.rod((6.8, 2.6), (7.6, 2.0), 0.12))], at=at)
        vs.callout(ax, a["stapes"], (x + 7.6, y + 0.6), "stapes")
        vs.callout(ax, a["quadrate"], (x + 4.6, y + 0.3), "quadrate")
    if i == 5:
        a = vs.draw(ax, [("squamosal", vs.smooth([(5.0, 2.9), (7.0, 2.95), (7.0, 2.4), (5.4, 2.5)])),
                         ("dentary", vs.smooth([(0.8, 1.7), (5.0, 1.9), (5.8, 2.6), (6.1, 2.4), (5.6, 1.4), (3.0, 1.0), (0.8, 1.3)])),
                         ("incus", vs.oval((6.9, 2.1), 0.2, 0.15)), ("malleus", vs.oval((6.55, 2.0), 0.2, 0.14)),
                         ("stapes", vs.rod((7.1, 2.1), (7.5, 2.15), 0.08))], at=at)
        vs.callout(ax, (x + 5.95, y + 2.55), (x + 3.4, y + 3.9), "dentary-squamosal joint")
        vs.callout(ax, a["incus"], (x + 7.6, y + 0.6), "incus, malleus")
vs.legend(ax, ["chondrocranium", ("quadrate", "palatoquadrate / quadrate / incus"),
               ("articular", "Meckel's cartilage / articular / malleus"),
               ("hyomandibula", "hyomandibula / stapes"), "dentary", "squamosal"], at=(0.4, 1.2), width=24.0, ncols=3)
