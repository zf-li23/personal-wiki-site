# Transverse sections through the trunk at the level of the shoulder girdle (schematic, after Kardong 2019,
# Nagashima et al. 2009 and Lyson et al. 2013). In a lizard (left) the ribs encircle the trunk and the
# scapula lies outside them, embedded in the body-wall muscles. In a turtle (right) the ribs grow laterally
# into the dermis of the back, guided by the carapacial ridge, and fuse with dermal costal plates to form
# the carapace; the neural plates fuse with the neural spines. The scapula and coracoid therefore come to
# lie inside the rib cage. The plastron is formed by dermal bones: anteriorly the clavicles (epiplastra) and
# interclavicle (entoplastron), posteriorly bones derived from gastralia. Keratinous scutes cover the shell.
# Bones are coloured in the course-wide homology scheme; dermal shell plates without a homologue in the
# lizard are grey. Not to scale.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax, boxes = vs.panels(2, 11.0, 8.0, titles=["Lizard", "Turtle"],
                           subtitles=["scapula outside the ribs", "scapula inside the ribs"], legend_rows=2,
                           gap=1.2)


def arc(cx, cy, rx, ry, a0, a1, n=40):
    a = np.radians(np.linspace(a0, a1, n))
    return np.c_[cx + rx * np.cos(a), cy + ry * np.sin(a)]


def band(path, w):
    path = np.asarray(path)
    d = np.gradient(path, axis=0)
    nrm = np.c_[-d[:, 1], d[:, 0]]
    nrm /= np.linalg.norm(nrm, axis=1)[:, None]
    return np.r_[path + nrm * w / 2, (path - nrm * w / 2)[::-1]].tolist()


# --- lizard
x, y, w, h = boxes[0]
cx, cy = x + 5.5, y + 3.6
body = arc(cx, cy, 4.6, 3.2, 0, 360)
bio.shape(ax, body.tolist(), token="animal", lw=0.8, zorder=2, alpha=0.35)
parts = [("centrum", vs.oval((0, 2.2), 0.6, 0.5)), ("neural_arch", vs.poly([(-0.5, 2.6), (0.5, 2.6), (0.3, 3.3), (-0.3, 3.3)])),
         ("neural_spine", vs.rod((0, 3.2), (0, 3.9), 0.25))]
for sgn in (-1, 1):
    r = arc(0, 0.2, 3.4, 2.0, 90 - sgn * 22, 90 - sgn * 165)
    r[:, 0] *= 1
    parts.append(("rib", band(r, 0.22)))
    parts.append(("scapula", vs.rod((sgn * 3.9, 1.9), (sgn * 4.2, 0.0), 0.35)))
    parts.append(("coracoid", vs.rod((sgn * 4.2, -0.1), (sgn * 2.0, -2.2), 0.35)))
    parts.append(("humerus", vs.rod((sgn * 4.3, -0.2), (sgn * 5.4, -1.4), 0.4)))
parts.append(("interclavicle", vs.oval((0, -2.55), 0.9, 0.18)))
a = vs.draw(ax, parts, at=(cx, cy))
vs.callout(ax, (cx - 3.95, cy + 1.2), (x + 0.2, y + 6.4), "scapula (outside)")
vs.callout(ax, (cx - 3.4, cy + 0.2), (x + 0.2, y + 7.3), "rib")
vs.callout(ax, (cx + 0.5, cy + 2.2), (x + 8.6, y + 5.6), "vertebra (centrum)")

# --- turtle
x, y, w, h = boxes[1]
cx, cy = x + 5.5, y + 3.0
bio.shape(ax, arc(cx, cy + 0.3, 4.9, 3.6, 0, 180).tolist() + [(cx - 4.9, cy - 2.2), (cx + 4.9, cy - 2.2)],
          token="animal", lw=0.8, zorder=2, alpha=0.35)
shell = band(arc(0, 0.3, 5.0, 3.7, 4, 176), 0.42)
parts = [("chondrocranium", shell, {"state": "context"}),
         ("centrum", vs.oval((0, 2.95), 0.55, 0.45)),
         ("neural_spine", vs.rod((0, 3.3), (0, 3.95), 0.4))]
for sgn in (-1, 1):
    r = arc(0, 0.3, 4.75, 3.45, 90 - sgn * 8, 90 - sgn * 80)
    parts.append(("rib", band(r, 0.2)))
    parts.append(("scapula", vs.rod((sgn * 1.3, 2.4), (sgn * 1.9, -0.6), 0.35)))
    parts.append(("coracoid", vs.rod((sgn * 1.9, -0.7), (sgn * 3.4, -1.7), 0.35)))
    parts.append(("humerus", vs.rod((sgn * 2.0, -0.8), (sgn * 3.9, 0.3), 0.4)))
    parts.append(("clavicle", vs.poly([(sgn * 1.0, -2.25), (sgn * 4.8, -2.25), (sgn * 4.8, -2.7), (sgn * 1.0, -2.7)])))
    parts.append(("chondrocranium", vs.rod((sgn * 4.9, -2.45), (sgn * 4.95, 0.2), 0.3), {"state": "context"}))
parts.append(("interclavicle", vs.poly([(-1.0, -2.25), (1.0, -2.25), (1.0, -2.7), (-1.0, -2.7)])))
a = vs.draw(ax, parts, at=(cx, cy))
# scutes: thin keratin line over the carapace
sc = arc(cx, cy + 0.3, 5.25, 3.95, 4, 176)
ax.plot(sc[:, 0], sc[:, 1], color=P.edge("bone"), lw=1.6, zorder=8)
vs.callout(ax, a["scapula"], (x + 10.8, y + 7.4), "scapula (inside)")
vs.callout(ax, (cx - 3.6, cy + 2.9), (x + 0.2, y + 7.6), "carapace: costal plates fused with ribs")
vs.callout(ax, (cx - 4.0, cy + 3.05), (x + 0.2, y + 6.6), "keratin scutes")
vs.callout(ax, a["interclavicle"], (x + 5.5, y - 0.1), "plastron: entoplastron (interclavicle)")
vs.callout(ax, (cx + 3.5, cy - 2.45), (x + 10.8, y + 0.4), "epiplastron (clavicle)")
vs.callout(ax, (cx + 4.9, cy - 1.0), (x + 10.9, y + 2.0), "bridge")
vs.legend(ax, ["centrum", "neural_spine", "rib", "scapula", "coracoid", "humerus", "clavicle", "interclavicle",
               ("chondrocranium", "dermal shell plates", "context")],
          at=(0.4, 2 * 0.55 + 0.25), width=23.0, ncols=5)
