# The two suborders of Orthoptera compared in lateral view (schematic, drawn with wikibio.zoomorph):
# Caelifera (grasshoppers, locusts) with short antennae, tympanal organs on the first abdominal segment,
# femoro-tegminal stridulation and a short digging ovipositor of hooked valves; Ensifera (katydids,
# crickets) with antennae longer than the body, tympanal organs on the fore tibiae, tegmino-tegminal
# stridulation (file on one forewing, scraper on the other) and a long blade- or needle-shaped ovipositor.
import numpy as np
from matplotlib.patches import Ellipse, Polygon
import wikibio as bio
from wikibio import zoomorph as zm

P = bio.P
fig, ax = bio.canvas(29, 10.5)
L = 10.0
specs = [("Caelifera", "grasshoppers, locusts", 1.2, ("filiform", 0.24)),
         ("Ensifera", "katydids, crickets", 17.0, ("filiform", 0.24))]
for k, (name, common, x0, ant) in enumerate(specs):
    bio.label(ax, (x0 + 5.4, 10.0), name, size="title", bold=True)
    bio.label(ax, (x0 + 5.4, 9.4), common, size="small", color=P.muted())
    a = zm.insect(ax, (x0 + 5.2, 4.6), L, order="Orthoptera", view="lateral", colored=False,
                  antenna=ant if k == 0 else ("filiform", 0.0001), highlight=("hind",))
    head = np.array(a["head"]); tip = np.array(a["cerci"])
    sock = head + np.array([0.25, 0.35])
    if k == 1:
        zm.antenna(ax, tuple(sock), 112, 11.5, "setaceous", colored=False, curve=0.5, segments=40, thickness=0.12)
    fore = a["legs"]["fore"]
    # tympanal organs
    if k == 0:
        t = np.array(a["thorax"]) + np.array([-1.5, 0.3])
        ax.add_patch(Ellipse(t, 0.6, 0.42, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.9, zorder=30))
        bio.callout(ax, tuple(t), (t[0] - 0.5, 1.2), "Tympanum on abdominal segment 1", size="small")
        # stridulatory pegs on inner hind femur against a forewing vein
        fem = np.array(a["legs"]["hind"]["femur"])
        bio.callout(ax, tuple(fem), (x0 + 0.2, 7.8), "Pegs on hind femur rub\na forewing vein", size="small")
        # short ovipositor valves
        for dy, s in ((0.18, 1), (-0.18, -1)):
            ax.add_patch(Polygon([tip + [0.1, dy * 0.4], tip + [-0.55, dy * 1.6], tip + [-0.75, dy * 1.1 + s * 0.15],
                                  tip + [-0.2, dy * 0.2]], closed=True, facecolor=P.fill("enzyme"),
                                 edgecolor=P.edge("enzyme"), lw=0.8, zorder=30))
        bio.callout(ax, tuple(tip + [-0.5, -0.3]), (x0 + 0.3, 2.2), "Short, hooked valves\n(dig into soil)", size="small")
        bio.callout(ax, tuple(sock + [0.55, 0.9]), (x0 + 9.6, 8.6), "Antenna shorter than body\n(<30 segments)", size="small")
    else:
        tib = np.array(fore["tibia"])
        ax.add_patch(Ellipse(tib, 0.22, 0.5, angle=-20, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"),
                             lw=0.9, zorder=30))
        bio.callout(ax, tuple(tib), (tib[0] + 1.0, 1.2), "Tympana on fore tibiae", size="small")
        w = np.array(a["forewing"]) + np.array([3.0, 0.1])
        bio.callout(ax, tuple(w), (x0 + 6.4, 8.3), "File and scraper on\nthe two forewings", size="small")
        blade = [tip + [0.2, 0.05], tip + [-1.2, 0.45], tip + [-2.5, 1.1], tip + [-2.6, 0.95], tip + [-1.3, 0.25],
                 tip + [0.15, -0.15]]
        ax.add_patch(Polygon(blade, closed=True, facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.8, zorder=30))
        bio.callout(ax, tuple(tip + [-1.9, 0.75]), (x0 - 1.6, 7.6), "Blade-like ovipositor\n(into plant tissue)", size="small")
        bio.callout(ax, (sock[0] - 1.0, sock[1] + 4.1), (x0 + 11.6, 8.6), "Antenna longer than body\n(>30 segments)", size="small")
ax.plot([14.2, 14.2], [0.6, 10.2], color=P.muted(), lw=0.4, alpha=0.5)
bio.label(ax, (28.7, 0.3), "Schematic, not to scale", size="tiny", color=P.muted(), ha="right")
