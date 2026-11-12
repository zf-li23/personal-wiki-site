# Body of a monogonont rotifer (Brachionus-like), ventral view, schematic, with an inset of malleate trophi.
import numpy as np
import wikibio as bio
from matplotlib.patches import Circle, Ellipse, Polygon

P = bio.P
fig, ax = bio.canvas(24, 14.6)
cx = 7.6
# lorica (trunk) with anterior spines
lor = [(cx - 2.6, 9.6), (cx - 2.2, 10.9), (cx - 1.7, 9.9), (cx - 0.6, 10.3), (cx, 9.9), (cx + 0.6, 10.3), (cx + 1.7, 9.9),
       (cx + 2.2, 10.9), (cx + 2.6, 9.6), (cx + 2.8, 6.5), (cx + 2.0, 4.0), (cx + 0.7, 3.4), (cx - 0.7, 3.4), (cx - 2.0, 4.0),
       (cx - 2.8, 6.5)]
ax.add_patch(Polygon(lor, closed=True, facecolor=P.mix(P.fill("animal"), P.surface(), 0.55), edgecolor=P.edge("animal"), lw=1.2, zorder=3))
# head and corona
ax.add_patch(Ellipse((cx, 10.6), 3.4, 1.6, facecolor=P.mix(P.fill("animal"), P.surface(), 0.4), edgecolor=P.edge("animal"), lw=1.0, zorder=2))
th = np.linspace(np.pi * 0.05, np.pi * 0.95, 34)
for t in th:
    x, y = cx + 1.7 * np.cos(t), 10.6 + 0.8 * np.sin(t)
    ax.plot([x, x + 0.35 * np.cos(t)], [y, y + 0.35 * np.sin(t)], color=P.edge("animal"), lw=0.8, zorder=2)
# foot and toes
for k, y in enumerate([3.2, 2.6, 2.0, 1.45]):
    ax.add_patch(Ellipse((cx, y), 0.9 - 0.08 * k, 0.6, facecolor=P.mix(P.fill("animal"), P.surface(), 0.4), edgecolor=P.edge("animal"), lw=0.8, zorder=2))
for sx in (-1, 1):
    ax.add_patch(Polygon([(cx + sx * 0.12, 1.25), (cx + sx * 0.38, 1.2), (cx + sx * 0.2, 0.45)], facecolor=P.mix(P.fill("animal"), P.surface(), 0.3),
                         edgecolor=P.edge("animal"), lw=0.8, zorder=2))
ax.add_patch(Ellipse((cx, 2.3), 0.3, 0.9, facecolor=P.fill("vesicle"), edgecolor=P.edge("vesicle"), lw=0.7, zorder=4))  # pedal gland
# brain, eyespot, mouth, mastax
ax.add_patch(Ellipse((cx, 10.05), 1.2, 0.5, facecolor=P.fill("neuron"), edgecolor=P.edge("neuron"), lw=0.8, zorder=6))
ax.add_patch(Circle((cx, 10.1), 0.12, facecolor=P.negative() if hasattr(P, "negative") else P.edge("negative"), edgecolor="none", zorder=7))
ax.add_patch(Ellipse((cx, 9.1), 1.5, 1.1, facecolor=P.fill("muscle"), edgecolor=P.edge("muscle"), lw=0.9, zorder=6))
for sx in (-1, 1):
    ax.plot([cx, cx + sx * 0.45, cx + sx * 0.3], [8.75, 9.2, 9.5], color=P.ink(), lw=1.2, zorder=7)
ax.plot([cx, cx], [8.65, 8.95], color=P.ink(), lw=1.4, zorder=7)
# oesophagus, stomach, gastric glands, intestine, cloaca
ax.plot([cx, cx], [8.5, 7.9], color=P.edge("endoderm"), lw=3, zorder=5)
ax.add_patch(Ellipse((cx, 6.7), 2.0, 2.6, facecolor=P.fill("endoderm"), edgecolor=P.edge("endoderm"), lw=0.9, zorder=5))
for sx in (-1, 1):
    ax.add_patch(Ellipse((cx + sx * 1.05, 7.95), 0.7, 0.5, facecolor=P.fill("lysosome"), edgecolor=P.edge("lysosome"), lw=0.7, zorder=6))
ax.add_patch(Ellipse((cx, 4.9), 1.1, 1.0, facecolor=P.fill("endoderm"), edgecolor=P.edge("endoderm"), lw=0.9, zorder=5))
ax.add_patch(Ellipse((cx + 0.15, 4.05), 0.55, 0.45, facecolor=P.mix(P.fill("endoderm"), P.surface(), 0.4), edgecolor=P.edge("endoderm"), lw=0.8, zorder=6))
# germovitellarium, bladder, protonephridia, egg
ax.add_patch(Ellipse((cx - 1.6, 5.8), 0.9, 2.0, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=6))
ax.add_patch(Ellipse((cx + 1.3, 4.5), 0.7, 0.6, facecolor=P.mix(P.fill("vesicle"), P.surface(), 0.4), edgecolor=P.edge("vesicle"), lw=0.9, zorder=6))
xs = np.array([cx + 2.2, cx + 2.35, cx + 2.2, cx + 1.6])
ys = np.array([9.0, 7.0, 5.4, 4.6])
ax.plot(xs, ys, color=P.edge("vesicle"), lw=1.0, zorder=6)
for y in (8.6, 7.4, 6.2):
    x = np.interp(-y, -ys, xs)
    ax.add_patch(Polygon([(x, y), (x - 0.3, y + 0.14), (x - 0.3, y - 0.14)], facecolor=P.fill("vesicle"), edgecolor=P.edge("vesicle"), lw=0.6, zorder=7))
ax.add_patch(Ellipse((cx - 2.3, 3.2), 1.3, 1.0, angle=30, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.9, zorder=4))
CL = [((cx - 1.0, 11.15), (1.0, 13.2), "Corona"), ((cx, 10.1), (1.0, 11.8), "Brain and eyespot"),
      ((cx - 0.4, 9.0), (1.0, 10.4), "Mastax with trophi"), ((cx - 1.6, 6.3), (1.0, 7.2), "Germovitellarium"),
      ((cx - 2.3, 3.2), (1.0, 3.6), "Egg (carried)"), ((cx - 2.45, 8.6), (1.0, 8.8), "Lorica"),
      ((cx + 1.05, 7.95), (13.0, 11.0), "Gastric gland"), ((cx + 0.6, 6.4), (13.0, 9.6), "Stomach"),
      ((cx + 2.25, 7.4), (13.0, 8.2), "Protonephridium, flame bulb"), ((cx + 0.4, 4.9), (13.0, 6.2), "Intestine"),
      ((cx + 1.3, 4.5), (13.0, 5.0), "Bladder"), ((cx + 0.35, 4.0), (13.0, 3.8), "Cloaca"),
      ((cx + 0.1, 2.3), (13.0, 2.4), "Foot with pedal gland"), ((cx + 0.3, 0.8), (13.0, 1.0), "Toes")]
for p, q, t in CL:
    bio.callout(ax, p, q, t, size="small")

# inset: malleate trophi
ix, iy = 20.4, 8.6
ax.add_patch(Circle((ix, iy), 2.7, facecolor=P.surface(), edgecolor=P.muted(), lw=0.8, zorder=8))
J = P.edge("animal")
ax.plot([ix, ix], [iy - 1.9, iy - 0.4], color=J, lw=3, zorder=9)                        # fulcrum
for sx in (-1, 1):
    ram = [(ix, iy - 0.4), (ix + sx * 0.9, iy - 0.1), (ix + sx * 0.8, iy + 0.7), (ix + sx * 0.1, iy + 0.5)]
    ax.add_patch(Polygon(ram, facecolor=P.fill("animal"), edgecolor=J, lw=1.2, zorder=9))       # ramus
    for k in range(4):
        ax.plot([ix + sx * (0.25 + 0.15 * k), ix + sx * (0.45 + 0.15 * k)], [iy + 0.9 - 0.05 * k, iy + 0.6 - 0.05 * k], color=J, lw=1.4, zorder=10)
    ax.plot([ix + sx * 0.85, ix + sx * 1.7, ix + sx * 1.8], [iy + 0.75, iy + 0.9, iy - 1.3], color=J, lw=2.2, zorder=9)  # uncus + manubrium
bio.label(ax, (ix, iy - 2.1), "Fulcrum", size="tiny")
bio.label(ax, (ix - 1.2, iy - 0.45), "Ramus", size="tiny")
bio.label(ax, (ix + 0.2, iy + 1.35), "Unci", size="tiny")
bio.label(ax, (ix + 2.0, iy - 1.6), "Manubrium", size="tiny", ha="left")
bio.label(ax, (ix, iy + 3.0), "Malleate trophi", size="small", bold=True)
