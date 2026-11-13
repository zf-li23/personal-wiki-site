# The compound bones of the mammalian skull and the elements that fuse to form them (vertskel homology colours).
# Each row: one adult mammalian bone; blocks: its components, labelled with the homologous element of reptiles
# or fishes. After Kardong (2019), Novacek (1993) and Yang & Cheng. Schematic.
import wikibio as bio
import vertskel as vs

P = bio.P
rows = [
    ("Temporal", [("squamosal", "squamosal (dermal)"), ("petrosal", "petrosal: prootic + opisthotic"),
                  ("tympanic", "tympanic = angular (dermal)"), ("styloid", "styloid (hyoid arch)")]),
    ("Occipital", [("basioccipital", "basioccipital"), ("exoccipital", "exoccipitals"),
                   ("supraoccipital", "supraoccipital"), ("interparietal", "interparietal = postparietals")]),
    ("Sphenoid", [("basisphenoid", "basisphenoid + presphenoid"), ("orbitosphenoid", "orbitosphenoids"),
                  ("alisphenoid", "alisphenoid = epipterygoid"), ("pterygoid", "pterygoid (dermal)")]),
    ("Ethmoid", [("ethmoid", "mesethmoid, cribriform plate, turbinals")]),
    ("Malleus", [("malleus", "articular"), ("prearticular", "prearticular (anterior process)")]),
    ("Incus", [("incus", "quadrate")]),
    ("Stapes", [("stapes", "hyomandibula")]),
    ("Mandible", [("dentary", "dentary (other jaw bones lost or in the ear)")]),
]
fig, ax = bio.canvas(26, len(rows) * 1.05 + 1.2)
for i, (name, parts) in enumerate(rows):
    y = len(rows) * 1.05 - (i + 1) * 1.05 + 0.4
    bio.label(ax, (0.3, y + 0.4), name, size="small", bold=True, ha="left")
    x = 3.6
    for key, lab in parts:
        w = max(3.2, 0.16 * len(lab) + 0.6)
        vs.bone(ax, key, vs.poly([(x, y + 0.05), (x + w, y + 0.05), (x + w, y + 0.75), (x, y + 0.75)]))
        bio.label(ax, (x + w / 2, y + 0.4), lab, size="tiny", color=P.on_fill())
        x += w + 0.25
