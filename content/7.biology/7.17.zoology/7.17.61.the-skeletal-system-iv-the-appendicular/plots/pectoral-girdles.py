# The pectoral girdle from fish to mammal, schematic left lateral views (anterior to the left), vertskel colours:
# endochondral elements (scapulocoracoid, scapula, coracoid, procoracoid) cool, dermal elements (posttemporal,
# supracleithrum, cleithrum, clavicle, interclavicle) warm. After Romer & Parsons, Kardong (2019), Jenkins (1993).
import wikibio as bio
import vertskel as vs

P = bio.P
titles = ["Osteolepiform fish", "Early tetrapod", "Lizard", "Bird", "Therian mammal"]
subs = ["attached to the skull", "free from the skull", "clavicle and interclavicle", "furcula, strut coracoid",
        "scapula and clavicle"]
fig, ax, boxes = vs.panels(5, 5.4, 6.4, titles=titles, subtitles=subs, ncols=5, legend_rows=2, gap=0.5)
G = []
x, y, w, h = boxes[0]
G.append([("posttemporal", vs.poly([(0.6, 5.6), (2.0, 5.8), (2.2, 5.3), (0.8, 5.1)])),
          ("supracleithrum", vs.poly([(1.8, 5.3), (2.4, 5.4), (2.6, 4.2), (2.0, 4.1)])),
          ("cleithrum", vs.smooth([(2.0, 4.2), (2.6, 4.3), (2.4, 2.2), (1.6, 0.8), (1.1, 1.0), (1.9, 2.4)])),
          ("clavicle", vs.smooth([(1.6, 0.8), (1.1, 1.0), (0.2, 0.7), (0.4, 0.4)])),
          ("scapulocoracoid", vs.oval((2.4, 2.0), 0.45, 0.6), {"z": 7})])
G.append([("scapulocoracoid", vs.smooth([(2.0, 4.2), (3.2, 4.2), (3.4, 1.4), (2.0, 0.9), (1.8, 2.0)])),
          ("cleithrum", vs.rod((3.3, 5.0), (3.1, 1.6), 0.3)),
          ("clavicle", vs.smooth([(2.0, 1.0), (2.2, 0.6), (0.6, 0.4), (0.5, 0.8)])),
          ("interclavicle", vs.smooth([(0.2, 0.5), (0.8, 0.8), (1.0, 0.2), (0.3, 0.0)]))])
G.append([("suprascapula", vs.poly([(2.2, 5.2), (3.6, 5.2), (3.4, 4.2), (2.4, 4.2)]), {"state": "cartilage"}),
          ("scapula", vs.poly([(2.4, 4.2), (3.4, 4.2), (3.2, 2.4), (2.6, 2.4)])),
          ("coracoid", vs.smooth([(2.4, 2.5), (3.4, 2.4), (3.0, 0.9), (1.6, 0.9), (1.8, 1.8)])),
          ("clavicle", vs.rod((2.5, 2.6), (0.8, 0.9), 0.22)),
          ("interclavicle", vs.poly([(0.4, 1.0), (1.2, 1.0), (1.0, 0.3), (0.6, 0.3)])),
          ("sternum", vs.poly([(1.2, 0.7), (3.4, 0.7), (3.4, 0.3), (1.2, 0.3)]), {"state": "cartilage"})])
G.append([("scapula", vs.rod((2.4, 3.6), (4.8, 4.6), 0.3)),
          ("coracoid", vs.rod((2.4, 3.5), (2.8, 0.9), 0.4)),
          ("clavicle", vs.smooth([(2.3, 3.7), (2.5, 3.4), (1.3, 1.0), (1.0, 1.3)]), {"text": None}),
          ("sternum", vs.smooth([(1.8, 0.9), (4.8, 0.9), (4.6, 0.3), (2.0, 0.3)])),
          ("sternum", vs.poly([(2.4, 0.3), (4.4, 0.3), (3.4, -0.6)]))])
G.append([("scapula", vs.smooth([(1.8, 5.4), (4.2, 5.4), (3.2, 2.6), (2.4, 2.4)])),
          ("coracoid", vs.oval((2.2, 2.4), 0.3, 0.2)),
          ("clavicle", vs.rod((2.5, 2.6), (0.6, 1.2), 0.2)),
          ("sternum", vs.poly([(0.3, 1.4), (0.9, 1.4), (0.9, 0.2), (0.3, 0.2)]))])
labs = [("posttemporal", "cleithrum", "scapulocoracoid"), ("cleithrum", "interclavicle"), ("clavicle", "coracoid"),
        ("clavicle", "coracoid"), ("clavicle", "scapula")]
for i, (x, y, w, h) in enumerate(boxes):
    a = vs.draw(ax, G[i], at=(x + 0.2, y + 0.8))
    if i == 3:
        vs.callout(ax, a["clavicle"], (x + 0.4, y + 5.6), "furcula (clavicles)")
    if i == 4:
        vs.callout(ax, a["coracoid"], (x + 4.0, y + 1.0), "coracoid process")
vs.legend(ax, ["scapulocoracoid", "scapula", "suprascapula", "coracoid", "posttemporal", "supracleithrum",
               "cleithrum", "clavicle", "interclavicle", "sternum"], at=(0.4, 1.3), width=28.0, ncols=5)
