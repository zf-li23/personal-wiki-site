"""vertskel: vertebrate comparative anatomy in one homology colour scheme (see BIO_FIGURES.md §4.1).

Every homologous element has one fixed colour on every page: the quadrate of a lizard and the incus of a
human share the palatoquadrate's gold, the articular and the malleus share Meckel's coral, the hyomandibula,
columella and stapes share the hyoid magenta. Elements of one series (skull-roof bones, circumorbital
bones, palate, pectoral girdle...) are shades of one hue, so a figure can colour either by element or by
series (``level="series"``) or by skull component (``level="component"``: dermatocranium, chondrocranium,
splanchnocranium). Colours are wikibio palette colours and work in both site themes.

Plot scripts import it next to wikibio (render_plot.py puts this folder on the path):

    import wikibio as bio
    import vertskel as vs

    fig, ax, boxes = vs.panels(3, 7, 5, titles=["Shark", "Lizard", "Human"], legend_rows=2)
    x, y, w, h = boxes[0]
    a = vs.draw(ax, [("palatoquadrate", vs.oval((3, 3), 2, 0.5)),
                     ("meckel", vs.rod((1, 2), (5, 2.2), 0.5), {"state": "cartilage"})],
                at=(x, y), scale=1.0)
    vs.callout(ax, a["palatoquadrate"], (x + 6, y + 4), "palatoquadrate")   # text defaults to the name
    vs.legend(ax, ["palatoquadrate", "meckel", "hyomandibula"], at=(0.5, 1.2), width=20)
    vs.aortic_arches(ax, (30, 1), 5, 8, arches={1: "absent", 2: "absent", 4: ("present", "absent")})
    vs.kidney_series(ax, (40, 1), 6, 9, stages={"pronephros": "embryonic", "mesonephros": "embryonic"})

Colours
    vs.color(key, level="element")     fill colour (theme aware); vs.edge(key, level) its outline
    vs.name(key)                       English display name ("Meckel's cartilage")
    vs.series_of(key), vs.component_of(key)
    vs.ELEMENTS                        key -> (name, series, colour); colour is a palette token, a hex value
                                       or another element key (then the two share a colour: "incus" -> "quadrate")
    vs.SERIES                          series -> (name, component, colour)
    vs.keys(series)                    the element keys of one series, in table order
  Keys are lower case with underscores: "premaxilla", "meckel", "arch_3", "aortic_4", "archinephric_duct".
  Common synonyms resolve too (``ALIASES``: "wolffian_duct", "opercle", "columella"...).

Shapes (vertices in the caller's units; pass them to ``bone``/``draw``)
    vs.rod(a, b, w, w2=None)           a bone shaft from a to b, width w (tapering to w2), round ends
    vs.oval(center, rx, ry, angle=0)   an ellipse (angle in degrees)
    vs.smooth(points)                  a smooth closed outline through control points
    vs.poly(points)                    a plain polygon (sharp corners: plates, sutured bones)

Drawing
    vs.bone(ax, key, vertices, state="bone", level="element", text=None)    one element; returns its centroid
        state: "bone" (filled), "cartilage" (pale fill, stippled), "context" (neutral grey: not the subject),
               "lost" (dashed outline only: absent in this taxon, shown for comparison), "highlight" (thick edge)
    vs.draw(ax, parts, at=(0, 0), scale=1.0, flip=False, level="element")   a list of (key, vertices[, opts])
        drawn in order (later parts on top), placed at ``at`` and scaled; ``flip`` mirrors left-right.
        opts: state, text (inside label), z, level. Returns {key: centroid} (and {key#2: ...} for repeats).
    vs.callout(ax, point, text_xy, key_or_text, size="tiny")  leader-line label; a known key prints its name
    vs.panels(n, panel_w, panel_h, titles=None, ncols=None, gap=0.6, legend_rows=0, subtitles=None)
        one canvas with n equal panels (row-major, top row first) and room for a legend strip below;
        returns (fig, ax, boxes) with boxes[i] = (x, y, w, h) of the drawing area of panel i
    vs.legend(ax, entries, at, width, level="element", size="tiny", ncols=None, title=None)
        swatches in rows from ``at`` (top-left); entries are keys, (key, text) or (key, text, state);
        returns the height used
    vs.aortic_arches(ax, at, width, height, arches=None, ...)   pharyngeal arch arteries I-VI (ventral view)
    vs.kidney_series(ax, at, width, height, stages=None, ducts=None, ...)  nephric organs and ducts

Conventions: anterior to the left in lateral views of skulls and skeletons, anterior up in the arch and
kidney diagrams; not to scale between taxa (say so in the caption). Text in figures is English only.
"""

import math

import numpy as np
from matplotlib.patches import PathPatch
from matplotlib.path import Path

import wikibio as bio
from wikibio import palette as P
from wikibio.core import FONT, LINE, smooth_closed

# ----------------------------------------------------------------------------------------------------------
# Homology colour table

COMPONENTS = {
    "dermatocranium": ("dermatocranium", "#7EAEE6"),  # blue: dermal bones
    "chondrocranium": ("chondrocranium", "#D8C7A6"),  # sand: braincase
    "splanchnocranium": ("splanchnocranium", "#F2A86E"),  # warm: pharyngeal arch skeleton
    "postcranial": ("postcranial", "#C9CED6"),
    "soft": ("soft tissue", "#C9CED6"),
}

# series -> (display name, component, series colour)
SERIES = {
    "marginal": ("marginal (tooth-bearing) series", "dermatocranium", "#F29455"),
    "roof": ("skull-roof series", "dermatocranium", "#7EAEE6"),
    "circumorbital": ("circumorbital series", "dermatocranium", "#8FCF86"),
    "temporal": ("temporal series", "dermatocranium", "#B392E8"),
    "palate": ("palatal series", "dermatocranium", "#6CC7BC"),
    "opercular": ("opercular series", "dermatocranium", "#A7B4C8"),
    "mandible": ("dermal bones of the lower jaw", "dermatocranium", "#E3C79B"),
    "braincase": ("chondrocranium and its ossifications", "chondrocranium", "#D8C7A6"),
    "mandibular_arch": ("mandibular arch (arch 1)", "splanchnocranium", "#F5CF5E"),
    "hyoid_arch": ("hyoid arch (arch 2)", "splanchnocranium", "#E58FD0"),
    "branchial": ("branchial arches (arches 3-7)", "splanchnocranium", "#9DB5E3"),
    "vertebra": ("vertebral elements", "postcranial", "#7FB6E8"),
    "pectoral": ("pectoral girdle", "postcranial", "#82B4E0"),
    "pelvic": ("pelvic girdle", "postcranial", "#A893DA"),
    "limb": ("limb skeleton", "postcranial", "#7FB6E8"),
    "fin": ("fin skeleton", "postcranial", "#9CC7EE"),
    "aortic": ("aortic arches", "soft", "#E86A6A"),
    "vessel": ("great vessels", "soft", "#E2B0AE"),
    "kidney": ("nephric organs", "soft", "#C3B6E2"),
    "duct": ("urogenital ducts", "soft", "#7FB6E8"),
}

# key -> (display name, series, colour). Colour: hex, a wikibio palette token, or another key (shared colour).
ELEMENTS = {
    # dermal skull: marginal tooth-bearing bones (orange)
    "premaxilla": ("premaxilla", "marginal", "#F7B27A"),
    "maxilla": ("maxilla", "marginal", "#F29455"),
    "septomaxilla": ("septomaxilla", "marginal", "#F9CBA3"),
    # skull roof, midline (blue)
    "nasal": ("nasal", "roof", "#A9C8EE"),
    "frontal": ("frontal", "roof", "#7EAEE6"),
    "parietal": ("parietal", "roof", "#5E93D6"),
    "postparietal": ("postparietal", "roof", "#9DB0CF"),
    "interparietal": ("interparietal", "roof", "postparietal"),  # the mammalian postparietals
    # circumorbital (green)
    "lacrimal": ("lacrimal", "circumorbital", "#C3E5B0"),
    "prefrontal": ("prefrontal", "circumorbital", "#96D38B"),
    "postfrontal": ("postfrontal", "circumorbital", "#6DBE8F"),
    "postorbital": ("postorbital", "circumorbital", "#4EA98A"),
    "jugal": ("jugal", "circumorbital", "#82C870"),
    # temporal / cheek (violet)
    "squamosal": ("squamosal", "temporal", "#B392E8"),
    "quadratojugal": ("quadratojugal", "temporal", "#DCC8F5"),
    "intertemporal": ("intertemporal", "temporal", "#C7B0EA"),
    "supratemporal": ("supratemporal", "temporal", "#9E86D6"),
    "tabular": ("tabular", "temporal", "#8174C4"),
    # palate (teal)
    "vomer": ("vomer", "palate", "#A6E0D8"),
    "palatine": ("palatine", "palate", "#6CC7BC"),
    "pterygoid": ("pterygoid", "palate", "#3FA9A0"),
    "ectopterygoid": ("ectopterygoid", "palate", "#C4EAE3"),
    "parasphenoid": ("parasphenoid", "palate", "#7DB9C9"),
    # opercular series of bony fishes (slate)
    "operculum": ("opercle", "opercular", "#A7B4C8"),
    "preoperculum": ("preopercle", "opercular", "#C3CCDA"),
    "suboperculum": ("subopercle", "opercular", "#8E9CB4"),
    "interoperculum": ("interopercle", "opercular", "#CDD3DF"),
    "gular": ("gular plate", "opercular", "#B4BCC8"),
    "branchiostegal": ("branchiostegal rays", "opercular", "#BAC3D2"),
    # dermal bones of the lower jaw (tan; the angular keeps its own lime so the tympanic can be tracked)
    "dentary": ("dentary", "mandible", "#E3C79B"),
    "splenial": ("splenial", "mandible", "#EEDCBC"),
    "angular": ("angular", "mandible", "#CBD86A"),
    "tympanic": ("tympanic (ectotympanic)", "mandible", "angular"),
    "surangular": ("surangular", "mandible", "#D6B583"),
    "prearticular": ("prearticular", "mandible", "#E9D3AE"),
    "goniale": ("goniale (anterior process of malleus)", "mandible", "prearticular"),
    "coronoid": ("coronoid", "mandible", "#CFAE80"),
    # chondrocranium and its ossifications (sand)
    "chondrocranium": ("chondrocranium", "braincase", "#D8C7A6"),
    "nasal_capsule": ("nasal capsule", "braincase", "#E4D8C2"),
    "ethmoid": ("ethmoid", "braincase", "nasal_capsule"),
    "optic_capsule": ("optic capsule (sclera)", "braincase", "#DDD3C6"),
    "otic_capsule": ("otic capsule", "braincase", "#CDBB9B"),
    "prootic": ("prootic", "braincase", "#C9B693"),
    "opisthotic": ("opisthotic", "braincase", "#D3C3A4"),
    "petrosal": ("petrosal (periotic)", "braincase", "otic_capsule"),
    "trabecula": ("trabecula", "braincase", "#E9E0CE"),
    "parachordal": ("parachordal", "braincase", "#C2B190"),
    "orbitosphenoid": ("orbitosphenoid", "braincase", "#DCCDB2"),
    "basisphenoid": ("basisphenoid", "braincase", "#C8B48F"),
    "occipital": ("occipital", "braincase", "#BCA986"),
    "basioccipital": ("basioccipital", "braincase", "#B8A381"),
    "exoccipital": ("exoccipital", "braincase", "#C6B391"),
    "supraoccipital": ("supraoccipital", "braincase", "#D2C2A2"),
    # mandibular arch (arch 1): palatoquadrate gold, Meckel's coral
    "palatoquadrate": ("palatoquadrate", "mandibular_arch", "#F5CF5E"),
    "quadrate": ("quadrate", "mandibular_arch", "palatoquadrate"),
    "incus": ("incus", "mandibular_arch", "palatoquadrate"),
    "epipterygoid": ("epipterygoid", "mandibular_arch", "#F8DF9C"),
    "alisphenoid": ("alisphenoid", "mandibular_arch", "epipterygoid"),
    "meckel": ("Meckel's cartilage", "mandibular_arch", "#F08A8A"),
    "articular": ("articular", "mandibular_arch", "meckel"),
    "malleus": ("malleus", "mandibular_arch", "meckel"),
    # hyoid arch (arch 2): magenta
    "hyomandibula": ("hyomandibula", "hyoid_arch", "#E58FD0"),
    "columella": ("columella", "hyoid_arch", "hyomandibula"),
    "stapes": ("stapes", "hyoid_arch", "hyomandibula"),
    "symplectic": ("symplectic", "hyoid_arch", "#EDB6E0"),
    "interhyal": ("interhyal", "hyoid_arch", "#F2C9E7"),
    "epihyal": ("epihyal", "hyoid_arch", "#E9A9D9"),
    "ceratohyal": ("ceratohyal", "hyoid_arch", "#DC9BCB"),
    "hypohyal": ("hypohyal", "hyoid_arch", "#F0BFE2"),
    "basihyal": ("basihyal", "hyoid_arch", "#F4D2EA"),
    "styloid": ("styloid process", "hyoid_arch", "epihyal"),
    "hyoid": ("hyoid (body and lesser horns)", "hyoid_arch", "basihyal"),
    # branchial arches 3-7 (one colour per arch, sky to mauve) and their derivatives
    "arch_3": ("branchial arch 1 (arch 3)", "branchial", "#8EC9E0"),
    "arch_4": ("branchial arch 2 (arch 4)", "branchial", "#9DB5E3"),
    "arch_5": ("branchial arch 3 (arch 5)", "branchial", "#AFA8DB"),
    "arch_6": ("branchial arch 4 (arch 6)", "branchial", "#C1A9CF"),
    "arch_7": ("branchial arch 5 (arch 7)", "branchial", "#CFB2C2"),
    "basibranchial": ("basibranchial", "branchial", "#BFC7DA"),
    "thyrohyal": ("greater horn of hyoid", "branchial", "arch_3"),
    "thyroid_cartilage": ("thyroid cartilage", "branchial", "arch_4"),
    "cricoid": ("cricoid cartilage", "branchial", "arch_6"),
    "arytenoid": ("arytenoid cartilage", "branchial", "arch_6"),
    # vertebrae
    "centrum": ("centrum", "vertebra", "#7FB6E8"),
    "pleurocentrum": ("pleurocentrum", "vertebra", "centrum"),  # forms the amniote centrum
    "intercentrum": ("intercentrum", "vertebra", "#F6B26B"),
    "neural_arch": ("neural arch", "vertebra", "#9FD585"),
    "neural_spine": ("neural spine", "vertebra", "#C6E4AE"),
    "zygapophysis": ("zygapophysis", "vertebra", "#79BC67"),
    "transverse_process": ("transverse process", "vertebra", "#B5D99A"),
    "haemal_arch": ("haemal arch", "vertebra", "#F293B6"),
    "chevron": ("chevron", "vertebra", "haemal_arch"),
    "haemal_spine": ("haemal spine", "vertebra", "#F6B9CF"),
    "rib": ("rib", "vertebra", "#E9C9A8"),
    "notochord": ("notochord", "vertebra", "#F9E29C"),
    # pectoral girdle: endochondral cool, dermal warm
    "scapula": ("scapula", "pectoral", "#82B4E0"),
    "suprascapula": ("suprascapula", "pectoral", "#B8D5F0"),
    "coracoid": ("coracoid", "pectoral", "#5FC3B9"),
    "procoracoid": ("procoracoid", "pectoral", "#A2DDD3"),
    "scapulocoracoid": ("scapulocoracoid", "pectoral", "#8CC6D8"),
    "cleithrum": ("cleithrum", "pectoral", "#F5C242"),
    "clavicle": ("clavicle", "pectoral", "#F79A7B"),
    "interclavicle": ("interclavicle", "pectoral", "#F2A0A0"),
    "supracleithrum": ("supracleithrum", "pectoral", "#F7D08A"),
    "posttemporal": ("posttemporal", "pectoral", "#EAD9BB"),
    "sternum": ("sternum", "pectoral", "#C9C3E6"),
    # pelvic girdle
    "ilium": ("ilium", "pelvic", "#A893DA"),
    "ischium": ("ischium", "pelvic", "#9FD585"),
    "pubis": ("pubis", "pelvic", "#F6B26B"),
    "puboischiadic": ("puboischiadic plate", "pelvic", "#C7DDB0"),
    # limbs (serial homologues share colours; same tokens as wikibio.zoomorph.forelimb and limbdev)
    "stylopod": ("stylopod", "limb", "humerus"),
    "zeugopod": ("zeugopod", "limb", "radius"),
    "autopod": ("autopod", "limb", "phalanges"),
    "humerus": ("humerus", "limb", "humerus"),
    "radius": ("radius", "limb", "radius"),
    "ulna": ("ulna", "limb", "ulna"),
    "carpals": ("carpals", "limb", "carpals"),
    "metacarpals": ("metacarpals", "limb", "metacarpals"),
    "phalanges": ("phalanges", "limb", "phalanges"),
    "femur": ("femur", "limb", "humerus"),
    "tibia": ("tibia", "limb", "radius"),
    "fibula": ("fibula", "limb", "ulna"),
    "tarsals": ("tarsals", "limb", "carpals"),
    "metatarsals": ("metatarsals", "limb", "metacarpals"),
    # fins
    "metapterygium": ("metapterygium", "fin", "#9CC7EE"),
    "mesopterygium": ("mesopterygium", "fin", "#C6DDF3"),
    "propterygium": ("propterygium", "fin", "#B4C3E0"),
    "radials": ("radials", "fin", "#F9DD9A"),
    "fin_rays": ("fin rays (lepidotrichia)", "fin", "#D5DAE1"),
    # pharyngeal arch arteries (aortic arches) I-VI and great vessels
    "aortic_1": ("aortic arch I", "aortic", "#F5C242"),
    "aortic_2": ("aortic arch II", "aortic", "#A9D58C"),
    "aortic_3": ("aortic arch III (carotid)", "aortic", "#5FC3B9"),
    "aortic_4": ("aortic arch IV (systemic)", "aortic", "#E86A6A"),
    "aortic_5": ("aortic arch V", "aortic", "#C9A2FF"),
    "aortic_6": ("aortic arch VI (pulmonary)", "aortic", "#6FA8DC"),
    "carotid": ("carotid arteries", "aortic", "aortic_3"),
    "systemic_arch": ("systemic arch", "aortic", "aortic_4"),
    "pulmonary_artery": ("pulmonary artery", "aortic", "aortic_6"),
    "ductus_arteriosus": ("ductus arteriosus", "aortic", "aortic_6"),
    "dorsal_aorta": ("dorsal aorta", "vessel", "#E2B0AE"),
    "ventral_aorta": ("ventral aorta", "vessel", "#CDBBD8"),
    "heart": ("heart", "vessel", "blood"),
    # nephric organs and ducts (as wikibio.mesoderm where it has them)
    "pronephros": ("pronephros", "kidney", "#F5B07E"),
    "mesonephros": ("mesonephros", "kidney", "metabolite"),
    "opisthonephros": ("opisthonephros", "kidney", "mesonephros"),
    "epididymis": ("epididymis", "kidney", "mesonephros"),
    "metanephros": ("metanephros", "kidney", "carbohydrate"),
    "gonad": ("gonad", "kidney", "rrna"),
    "archinephric_duct": ("archinephric (Wolffian) duct", "duct", "channel"),
    "vas_deferens": ("vas deferens", "duct", "archinephric_duct"),
    "mullerian_duct": ("Mullerian duct", "duct", "receptor"),
    "oviduct": ("oviduct", "duct", "mullerian_duct"),
    "ureter": ("ureter", "duct", "enzyme"),
    "bladder": ("urinary bladder", "duct", "lipid"),
    "cloaca": ("cloaca", "duct", "neutral"),
}

ALIASES = {
    "opercle": "operculum", "preopercle": "preoperculum", "subopercle": "suboperculum", "interopercle": "interoperculum",
    "meckels_cartilage": "meckel", "hyomandibular": "hyomandibula", "ectotympanic": "tympanic",
    "wolffian_duct": "archinephric_duct", "nephric_duct": "archinephric_duct", "muellerian_duct": "mullerian_duct",
    "paramesonephric_duct": "mullerian_duct", "periotic": "petrosal", "branchial_1": "arch_3", "branchial_2": "arch_4",
    "branchial_3": "arch_5", "branchial_4": "arch_6", "branchial_5": "arch_7", "ductus": "ductus_arteriosus",
}

ROMAN = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII"}


def _key(key):
    k = ALIASES.get(key, key)
    if k not in ELEMENTS and k not in SERIES and k not in COMPONENTS:
        raise KeyError(f"unknown vertskel key {key!r}; see vertskel.ELEMENTS")
    return k


def _raw(key, level="element"):
    """The un-themed colour (hex or palette token) of a key at a level."""
    k = _key(key)
    if k in COMPONENTS:
        return COMPONENTS[k][1]
    if k in SERIES:
        return SERIES[k][2] if level != "component" else COMPONENTS[SERIES[k][1]][1]
    if level == "series":
        return SERIES[ELEMENTS[k][1]][2]
    if level == "component":
        return COMPONENTS[SERIES[ELEMENTS[k][1]][1]][1]
    c, seen = ELEMENTS[k][2], {k}
    while c in ELEMENTS and c not in seen:  # follow shared-colour references
        seen.add(c)
        c = ELEMENTS[c][2]
    return c


def color(key, level="element"):
    """Fill colour of an element (or series/component) at ``level``: "element", "series" or "component"."""
    return P.fill(_raw(key, level))


def edge(key, level="element"):
    """Outline colour matching ``color``."""
    return P.edge(_raw(key, level))


def light(key, level="element"):
    """A paler shade (cartilage, transient organs); it moves towards the background in the dark theme."""
    return _fills(key, level, "cartilage")[0]


def name(key):
    """English display name of an element, series or component."""
    k = _key(key)
    if k in ELEMENTS:
        return ELEMENTS[k][0]
    return SERIES[k][0] if k in SERIES else COMPONENTS[k][0]


def series_of(key):
    return ELEMENTS[_key(key)][1]


def component_of(key):
    return SERIES[series_of(key)][1]


def keys(series):
    """Element keys of a series, in table order."""
    return [k for k, v in ELEMENTS.items() if v[1] == series]


# ----------------------------------------------------------------------------------------------------------
# Shapes


def rod(a, b, w, w2=None, n=14):
    """Outline of a bone shaft from a to b: width w at a, w2 at b (default w), rounded ends."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    d = b - a
    L = float(np.hypot(*d)) or 1e-9
    u = d / L
    nrm = np.array([-u[1], u[0]])
    r1, r2 = w / 2, (w if w2 is None else w2) / 2
    ang = math.atan2(u[1], u[0])
    cap_b = [b + r2 * np.array([math.cos(t), math.sin(t)]) for t in np.linspace(ang - math.pi / 2, ang + math.pi / 2, n)]
    cap_a = [a + r1 * np.array([math.cos(t), math.sin(t)]) for t in np.linspace(ang + math.pi / 2, ang + 3 * math.pi / 2, n)]
    return np.array([a - r1 * nrm, b - r2 * nrm, *cap_b, b + r2 * nrm, a + r1 * nrm, *cap_a])


def oval(center, rx, ry, angle=0.0, n=60):
    """Outline of an ellipse; ``angle`` in degrees."""
    t = np.linspace(0, 2 * math.pi, n, endpoint=False)
    c, s = math.cos(math.radians(angle)), math.sin(math.radians(angle))
    x, y = rx * np.cos(t), ry * np.sin(t)
    return np.c_[x * c - y * s, x * s + y * c] + np.asarray(center, float)


def smooth(points, n=160):
    """A smooth closed outline through control points (Catmull-Rom)."""
    return smooth_closed(points, n)[:-1]


def poly(points):
    """A polygon with sharp corners (dermal plates meeting at sutures)."""
    return np.asarray(points, float)


# ----------------------------------------------------------------------------------------------------------
# Drawing elements

STATES = ("bone", "cartilage", "context", "lost", "highlight")


def _centroid(v):
    v = np.asarray(v, float)
    x, y = v[:, 0], v[:, 1]
    xs, ys = np.roll(x, -1), np.roll(y, -1)
    cr = x * ys - xs * y
    A = cr.sum() / 2
    if abs(A) < 1e-9:
        return tuple(v.mean(axis=0))
    return (float(((x + xs) * cr).sum() / (6 * A)), float(((y + ys) * cr).sum() / (6 * A)))


def _stipple(ax, v, color_, z, clip, spacing=None):
    """Dots inside a polygon (clipped to its patch): the textbook convention for cartilage."""
    v = np.asarray(v, float)
    lo, hi = v.min(axis=0), v.max(axis=0)
    s = spacing or max(0.1, min(0.22, float(min(hi - lo)) / 4))
    xs = np.arange(lo[0] + s / 2, hi[0], s)
    pts = []
    for i, y in enumerate(np.arange(lo[1] + s / 2, hi[1], s * 0.87)):
        off = s / 2 if i % 2 else 0
        pts += [(x + off, y) for x in xs]
    if pts:
        pts = np.array(pts)
        dots = ax.scatter(pts[:, 0], pts[:, 1], s=1.4, color=color_, linewidths=0, zorder=z + 0.05)
        dots.set_clip_path(clip)


def _fills(key, level, state):
    """(face, edge) for a drawing state. Pale shades move towards the background in the dark theme, so
    cartilage and context parts recede there too instead of glowing."""
    if state == "context":
        f, e = P.fill("neutral"), P.edge("neutral")
        return (P.mix(f, P.surface(), 0.55), P.mix(e, P.surface(), 0.25)) if P.is_dark() else (f, e)
    f, e = color(key, level), edge(key, level)
    if state == "cartilage":
        # dark theme: a dimmed body with the full colour as outline and stipple
        return (P.mix(f, P.surface(), 0.3), f) if P.is_dark() else (P.mix(f, "#ffffff", 0.5), e)
    return f, e


def bone(ax, key, vertices, state="bone", level="element", text=None, size="tiny", lw=None, z=5):
    """Draw one element (closed outline ``vertices``) coloured by homology. Returns its centroid.

    state: "bone" (homology fill), "cartilage" (pale fill with stipple), "context" (neutral grey, for parts that
    are not the subject), "lost" (dashed outline, no fill: absent in this taxon), "highlight" (thicker edge).
    ``text`` is written inside the element (dark text on the fill).
    """
    if state not in STATES:
        raise ValueError(f"state must be one of {STATES}")
    v = np.asarray(vertices, float)
    path = Path(np.vstack([v, v[:1]]), closed=True)
    lw = LINE * 0.75 if lw is None else lw
    if state == "lost":
        ax.add_patch(PathPatch(path, fill=False, edgecolor=P.muted(), lw=lw * 0.9, linestyle=(0, (2.5, 1.6)), zorder=z,
                               joinstyle="round"))
    else:
        fc, ec = _fills(key, level, state)
        patch = PathPatch(path, facecolor=fc, edgecolor=ec, lw=lw * (1.9 if state == "highlight" else 1.0),
                          zorder=z, joinstyle="round")
        ax.add_patch(patch)
        if state == "cartilage":
            _stipple(ax, v, ec, z, patch)
    c = _centroid(v)
    if text:
        bio.label(ax, c, text, size=size, color=P.on_fill() if state != "lost" else P.muted(), zorder=z + 0.5)
    return c


def _place(v, at, scale, flip):
    v = np.asarray(v, float) * scale
    if flip:
        v = v * np.array([-1.0, 1.0])
    return v + np.asarray(at, float)


def draw(ax, parts, at=(0.0, 0.0), scale=1.0, flip=False, level="element", z=5):
    """Draw a list of parts ``(key, vertices)`` or ``(key, vertices, opts)``, in order (later on top), mapped by
    ``vertices * scale (+ mirror) + at``. opts: state, text, size, z, level. Returns {key: centroid in canvas
    coordinates}; a key drawn twice gets "key#2" for the second one."""
    out = {}
    for i, part in enumerate(parts):
        key, verts = part[0], part[1]
        o = part[2] if len(part) > 2 else {}
        v = _place(verts, at, scale, flip)
        c = bone(ax, key, v, state=o.get("state", "bone"), level=o.get("level", level), text=o.get("text"),
                 size=o.get("size", "tiny"), z=o.get("z", z + i * 0.01))
        k, j = key, 2
        while k in out:
            k, j = f"{key}#{j}", j + 1
        out[k] = c
    return out


def callout(ax, point, text_xy, key_or_text, size="tiny", color_=None):
    """Leader-line label (wikibio.callout); an element key prints its display name."""
    try:
        text = name(key_or_text)
    except KeyError:
        text = key_or_text
    return bio.callout(ax, point, text_xy, text, size=size, color=color_)


# ----------------------------------------------------------------------------------------------------------
# Layout: panel series and legend

TITLE_H = 0.9
LEGEND_ROW = 0.55


def panels(n, panel_w, panel_h, titles=None, ncols=None, gap=0.6, legend_rows=0, subtitles=None, italic=False,
           margin=0.3, scale=0.45):
    """One canvas with ``n`` equal panels (row-major, top row first), each ``panel_w`` x ``panel_h`` units of
    drawing area under a title line, and ``legend_rows`` rows of legend space at the bottom. Titles are bold
    (``italic=True`` for genus names); ``subtitles`` go in small muted text under the titles. Returns
    (fig, ax, boxes) with boxes[i] = (x, y, w, h), the lower-left corner and size of panel i's drawing area.
    The legend strip starts at y = legend_rows * 0.55 + margin (draw it with ``legend(..., at=(margin, that))``).
    """
    ncols = ncols or n
    nrows = math.ceil(n / ncols)
    th = TITLE_H + (0.45 if subtitles else 0) if (titles or subtitles) else 0.2
    leg = legend_rows * LEGEND_ROW + (0.4 if legend_rows else 0)
    W = 2 * margin + ncols * panel_w + (ncols - 1) * gap
    H = 2 * margin + leg + nrows * (panel_h + th) + (nrows - 1) * gap
    fig, ax = bio.canvas(W, H, scale=scale)
    boxes = []
    for i in range(n):
        r, c = divmod(i, ncols)
        x = margin + c * (panel_w + gap)
        ytop = H - margin - r * (panel_h + th + gap)
        y = ytop - th - panel_h
        boxes.append((x, y, panel_w, panel_h))
        if titles and i < len(titles) and titles[i]:
            bio.label(ax, (x + panel_w / 2, ytop - 0.35), titles[i], size="normal", bold=True, italic=italic)
        if subtitles and i < len(subtitles) and subtitles[i]:
            bio.label(ax, (x + panel_w / 2, ytop - 0.95), subtitles[i], size="tiny", color=P.muted())
    return fig, ax, boxes


def _text_w(text, size):
    # rough width of text in canvas units at the default canvas scale (0.45 in per unit)
    return len(text) * FONT.get(size, size) * 0.55 / 72 / 0.45


def legend(ax, entries, at, width, level="element", size="tiny", ncols=None, title=None, swatch=0.36):
    """Colour key: entries are keys, (key, text) or (key, text, state), laid out in rows from ``at`` (the top-left
    corner) within ``width``. A chain of homologues reads best as one entry: ("quadrate", "palatoquadrate /
    quadrate / incus"). Returns the height used."""
    items = []
    for e in entries:
        if isinstance(e, str):
            e = (e,)
        k = e[0]
        items.append((k, e[1] if len(e) > 1 and e[1] else name(k), e[2] if len(e) > 2 else "bone"))
    x0, y = at
    if title:
        bio.label(ax, (x0, y - 0.2), title, size="small", bold=True, ha="left")
        y -= LEGEND_ROW
    cell = max(_text_w(t, size) for _, t, _ in items) + swatch + 0.5
    ncols = ncols or max(1, int(width // cell))
    cw = width / ncols
    for i, (k, t, st) in enumerate(items):
        r, c = divmod(i, ncols)
        x, yy = x0 + c * cw, y - r * LEGEND_ROW - 0.2
        sq = poly([(x, yy - swatch / 2), (x + swatch * 1.4, yy - swatch / 2), (x + swatch * 1.4, yy + swatch / 2),
                   (x, yy + swatch / 2)])
        bone(ax, k, sq, state=st, level=level, lw=LINE * 0.6, z=18)
        bio.label(ax, (x + swatch * 1.4 + 0.18, yy), t, size=size, ha="left")
    rows = math.ceil(len(items) / ncols)
    return (at[1] - y) + rows * LEGEND_ROW


# ----------------------------------------------------------------------------------------------------------
# Vessels: pharyngeal arch arteries


def _vessel(ax, pts, key, state="present", lw=4.2, z=6):
    """A vessel along a polyline: a coloured band with a darker outline; "absent" is a dashed grey trace,
    "reduced" a thin band, "ligament" a thin solid grey cord (a closed fetal shunt)."""
    p = np.asarray(pts, float)
    if state in ("absent", None, False):
        ax.plot(p[:, 0], p[:, 1], color=P.muted(), lw=0.9, linestyle=(0, (2.2, 1.6)), zorder=z - 0.5,
                solid_capstyle="round", dash_capstyle="round")
        return
    if state == "ligament":
        ax.plot(p[:, 0], p[:, 1], color=P.muted(), lw=1.4, zorder=z - 0.5, solid_capstyle="round")
        return
    w = lw * (0.45 if state == "reduced" else 1.0)
    ax.plot(p[:, 0], p[:, 1], color=edge(key), lw=w + 1.6, zorder=z, solid_capstyle="round", solid_joinstyle="round")
    ax.plot(p[:, 0], p[:, 1], color=color(key), lw=w, zorder=z + 0.1, solid_capstyle="round", solid_joinstyle="round")


def _bezier(a, c, b, n=24):
    t = np.linspace(0, 1, n)[:, None]
    a, c, b = (np.asarray(q, float) for q in (a, c, b))
    return (1 - t) ** 2 * a + 2 * (1 - t) * t * c + t ** 2 * b


def _sides(v):
    """(left, right) of the animal from a single value or a pair."""
    return tuple(v) if isinstance(v, (tuple, list)) else (v, v)


def aortic_arches(ax, at, width, height, arches=None, carotid_duct=True, ductus=True, pulmonary=False,
                  roots=True, numerals=True, sides=True, labels=None, lw=4.0, z=6):
    """Pharyngeal arch arteries I-VI between the ventral aorta and the paired dorsal aortae, ventral view
    (anterior up, the heart at the bottom; the animal's left is on the viewer's right, marked L/R).

    at, width, height: lower-left corner and size of the diagram. ``arches`` maps 1..6 to a state, or to a pair
    (left, right) of the animal: "present" (default), "gill" (interrupted by gill capillaries: afferent and
    efferent halves), "reduced" (thin), "absent" (dashed trace). ``carotid_duct`` (dorsal aorta between III and
    IV), ``roots`` (the dorsal aortic roots posterior to arch IV, joining behind the heart) and ``ductus`` (arch
    VI beyond the pulmonary branch) take True/False, a state or a (left, right) pair; ``ductus="ligament"``
    draws the closed ductus as a cord. ``pulmonary=True`` adds a pulmonary artery from each arch VI.
    ``labels``: {arch: text} or {(arch, "L"|"R"): text} written lateral to that arch. Returns anchors:
    {(arch, "L"|"R"): midpoint, "heart", "ventral_aorta", "dorsal_aorta"}.
    """
    x0, y0 = at
    W, H = width, height
    cx = x0 + W / 2
    st = {k: "present" for k in range(1, 7)}
    st.update(arches or {})
    # vertical layout (fractions of height)
    y_arch = {k: y0 + H * (0.86 - (k - 1) * 0.095) for k in range(1, 7)}
    y_top = y0 + H * 0.97
    y_root = y0 + H * 0.30  # where the dorsal aortae turn medially
    y_merge = y0 + H * 0.08
    y_heart = y0 + H * 0.20
    xd = {"L": cx + W * 0.36, "R": cx - W * 0.36}  # ventral view: animal's left on the right
    xv = {"L": cx + W * 0.03, "R": cx - W * 0.03}
    out = {}

    def st_of(v, i):
        v = _sides(v)[i]
        if v is True:
            return "present"
        if v is False:
            return "absent"
        return v

    # ventral aorta (midline) from the heart to arch I, and heart
    _vessel(ax, [(cx, y_heart), (cx, y_arch[1])], "ventral_aorta", lw=lw * 1.2, z=z)
    out["ventral_aorta"] = (cx, (y_heart + y_arch[1]) / 2)
    bio.shape(ax, smooth([(cx - W * 0.11, y_heart + H * 0.02), (cx, y_heart + H * 0.055), (cx + W * 0.11, y_heart + H * 0.02),
                          (cx + W * 0.06, y_heart - H * 0.045), (cx, y_heart - H * 0.06), (cx - W * 0.06, y_heart - H * 0.045)]),
              token="blood", zorder=z + 1, lw=LINE * 0.8)
    out["heart"] = (cx, y_heart)
    # descending dorsal aorta
    _vessel(ax, [(cx, y_merge), (cx, y0)], "dorsal_aorta", lw=lw * 1.2, z=z - 0.2)
    out["dorsal_aorta"] = (cx, (y_merge + y0) / 2)

    for i, sd in enumerate(("L", "R")):
        xs = xd[sd]
        # anterior continuation (internal carotid) and dorsal aorta between arches I and III
        _vessel(ax, [(xs, y_top), (xs, y_arch[3])], "dorsal_aorta", lw=lw, z=z - 0.2)
        _vessel(ax, [(xs, y_arch[3]), (xs, y_arch[4])], "dorsal_aorta", st_of(carotid_duct, i), lw=lw, z=z - 0.2)
        rs = st_of(roots, i)
        _vessel(ax, [(xs, y_arch[4]), (xs, y_root)] + [tuple(q) for q in
                _bezier((xs, y_root), (xs, y_merge + H * 0.04), (cx, y_merge))[1:]], "dorsal_aorta", rs, lw=lw, z=z - 0.2)
        for k in range(1, 7):
            s = st_of(st[k], i)
            a, b = (xv[sd], y_arch[k]), (xs, y_arch[k])
            ctrl = ((a[0] + b[0]) / 2, y_arch[k] + H * 0.035)
            pts = _bezier(a, ctrl, b)
            key = f"aortic_{k}"
            mid = tuple(pts[len(pts) // 2])
            out[(k, sd)] = mid
            if k == 6 and s not in ("absent", None, False):
                # proximal part of VI up to the pulmonary branch, then the ductus
                j = int(len(pts) * 0.55)
                _vessel(ax, pts[: j + 1], key, s, lw=lw, z=z)
                ds = st_of(ductus, i)
                _vessel(ax, pts[j:], key, ds if ds != "present" else s, lw=lw, z=z)
                if pulmonary:
                    p0 = pts[j]
                    _vessel(ax, [p0, (p0[0], p0[1] - H * 0.09), (p0[0] + (xs - cx) * 0.25, p0[1] - H * 0.16)], key, s,
                            lw=lw * 0.8, z=z - 0.1)
                    out[("pulmonary", sd)] = (p0[0] + (xs - cx) * 0.25, p0[1] - H * 0.16)
                continue
            if s == "gill":
                h = len(pts) // 2
                gap = 2
                _vessel(ax, pts[: h - gap + 1], key, "present", lw=lw, z=z)
                _vessel(ax, pts[h + gap:], key, "present", lw=lw, z=z)
                # gill filaments: a comb of capillary loops across the gap
                p, q = pts[h - gap], pts[h + gap]
                for t in np.linspace(0, 1, 5):
                    xm = p[0] + (q[0] - p[0]) * t
                    ym = p[1] + (q[1] - p[1]) * t
                    ax.plot([xm, xm], [ym - H * 0.022, ym + H * 0.022], color=edge(key), lw=0.8, zorder=z + 0.2,
                            solid_capstyle="round")
            else:
                _vessel(ax, pts, key, s, lw=lw, z=z)
        # numerals on the animal's right side (viewer's left), inside the loop
    if numerals:
        for k in range(1, 7):
            bio.label(ax, ((xv["R"] + xd["R"]) / 2, y_arch[k] + H * 0.052), ROMAN[k], size="tiny", color=P.muted(),
                      va="bottom")
    if sides:
        bio.label(ax, (xd["R"], y0 + H * 0.02), "R", size="tiny", color=P.muted(), va="bottom")
        bio.label(ax, (xd["L"], y0 + H * 0.02), "L", size="tiny", color=P.muted(), va="bottom")
    for k, text in (labels or {}).items():
        arch, sd = (k, "L") if isinstance(k, int) else k
        x = xd[sd] + (0.25 if sd == "L" else -0.25)
        bio.label(ax, (x, y_arch[arch]), text, size="tiny", ha="left" if sd == "L" else "right")
    return out


# ----------------------------------------------------------------------------------------------------------
# Kidneys and ducts

KIDNEY_STATES = ("functional", "embryonic", "absent", "modified")


def kidney_series(ax, at, width, height, stages=None, ducts=None, opisthonephros=False, gonad=False, bladder=False,
                  labels=True, rename=None, size="tiny", z=5):
    """The nephric organs of one side (anterior up, lateral to the left of the duct column), in the order
    pronephros, mesonephros, metanephros, with the archinephric (Wolffian) duct, the ureter and the Mullerian
    duct running back to the cloaca.

    ``stages`` maps "pronephros", "mesonephros", "metanephros" to "functional" (default), "embryonic"
    (transient: pale with a dashed outline), "modified" (pale, solid: e.g. the mesonephros as epididymis) or
    "absent" (not drawn). ``ducts`` maps "archinephric_duct", "ureter", "mullerian_duct" the same way (default:
    functional, functional, absent). ``opisthonephros=True`` draws the mesonephric and posterior regions as one
    kidney (anamniotes). ``rename``: {key: text} for the labels ("archinephric_duct": "vas deferens"). Labels sit
    right of the diagram when ``labels`` is True. Returns anchors {key: point}.
    """
    x0, y0 = at
    W, H = width, height
    sg = {"pronephros": "functional", "mesonephros": "functional", "metanephros": "functional"}
    sg.update(stages or {})
    dc = {"archinephric_duct": "functional", "ureter": "functional", "mullerian_duct": "absent"}
    dc.update(ducts or {})
    rename = rename or {}
    out = {}
    xk = x0 + W * 0.22  # kidney column centre
    xa = x0 + W * 0.48  # archinephric duct
    xm = x0 + W * 0.62  # Mullerian duct
    yc = y0 + H * 0.05  # cloaca
    regions = {"pronephros": (0.84, 0.95), "mesonephros": (0.46, 0.80), "metanephros": (0.17, 0.40)}
    if opisthonephros:
        regions = {"pronephros": (0.84, 0.95), "opisthonephros": (0.22, 0.80)}
        sg["opisthonephros"] = sg.get("opisthonephros", sg.get("mesonephros", "functional"))
    tips = {}  # label anchors

    def organ(key, lo, hi, state, tubules):
        if state == "absent":
            return
        yl, yh = y0 + H * lo, y0 + H * hi
        rw = W * (0.13 if key == "pronephros" else 0.17)
        v = smooth([(xk - rw, (yl + yh) / 2), (xk - rw * 0.8, yh), (xk, yh + H * 0.01), (xk + rw * 0.8, yh),
                    (xk + rw, (yl + yh) / 2), (xk + rw * 0.8, yl), (xk, yl - H * 0.01), (xk - rw * 0.8, yl)])
        path = Path(np.vstack([v, v[:1]]), closed=True)
        pale = state in ("embryonic", "modified")
        ax.add_patch(PathPatch(path, facecolor=light(key) if pale else color(key), edgecolor=edge(key), lw=LINE * 0.8,
                               linestyle=(0, (3, 1.8)) if state == "embryonic" else "-", zorder=z, joinstyle="round"))
        # tubules running from the organ to the duct
        if key != "metanephros":
            for y in np.linspace(yl + (yh - yl) * 0.15, yh - (yh - yl) * 0.15, tubules):
                ax.plot([xk + rw * 0.2, xa], [y, y - H * 0.012], color=edge(key), lw=0.9, zorder=z + 0.3,
                        linestyle=(0, (2, 1.4)) if state == "embryonic" else "-", solid_capstyle="round")
        out[key] = (xk, (yl + yh) / 2)
        tips[key] = (xk + rw * 0.55, yh - (yh - yl) * 0.12)  # label anchor: upper right, short leaders

    for key, (lo, hi) in regions.items():
        organ(key, lo, hi, sg[key], 3 if key == "pronephros" else 6 if key == "mesonephros" else 9)

    def duct(key, pts):
        s = dc[key]
        if s == "absent":
            return
        p = np.asarray(pts, float)
        if s == "embryonic":
            ax.plot(p[:, 0], p[:, 1], color=edge(key), lw=2.0, linestyle=(0, (2.4, 1.6)), zorder=z + 0.5,
                    dash_capstyle="round")
        else:
            w = 2.0 if s == "modified" else 3.2
            ax.plot(p[:, 0], p[:, 1], color=edge(key), lw=w + 1.4, zorder=z + 0.5, solid_capstyle="round",
                    solid_joinstyle="round")
            ax.plot(p[:, 0], p[:, 1], color=color(key), lw=w, zorder=z + 0.6, solid_capstyle="round", solid_joinstyle="round")
        out[key] = tuple(p[0] + (p[1] - p[0]) * 0.45)  # on the first (long) segment
        tips[key] = tuple(p[0] + (p[1] - p[0]) * {"archinephric_duct": 0.55, "mullerian_duct": 0.3}.get(key, 0.5))

    top_a = y0 + H * (0.93 if sg["pronephros"] != "absent" else 0.78)
    duct("archinephric_duct", [(xa, top_a), (xa, y0 + H * 0.16), (x0 + W * 0.40, yc + H * 0.02)])
    if "metanephros" in regions and sg["metanephros"] != "absent":
        mt = out["metanephros"]
        duct("ureter", [(mt[0] + W * 0.1, mt[1] - H * 0.02)] + [tuple(q) for q in
             _bezier((mt[0] + W * 0.1, mt[1] - H * 0.02), (x0 + W * 0.36, y0 + H * 0.22), (x0 + W * 0.33, yc + H * 0.02))])
    if dc["mullerian_duct"] != "absent":
        yt = y0 + H * 0.9
        duct("mullerian_duct", [(xm, yt), (xm, y0 + H * 0.16), (x0 + W * 0.47, yc + H * 0.02)])
        # ostium (funnel) at the anterior end
        f = np.array([(xm - W * 0.05, yt + H * 0.04), (xm, yt), (xm + W * 0.05, yt + H * 0.04)])
        ax.plot(f[:, 0], f[:, 1], color=edge("mullerian_duct"), lw=1.6, zorder=z + 0.7, solid_capstyle="round")
    if gonad:
        g = oval((x0 + W * 0.36, y0 + H * 0.62), W * 0.045, H * 0.11)
        bone(ax, "gonad", g, z=z + 0.2, lw=LINE * 0.7)
        out["gonad"] = (x0 + W * 0.36, y0 + H * 0.62)
    # cloaca (and bladder)
    bio.shape(ax, oval((x0 + W * 0.4, yc), W * 0.14, H * 0.035), token=_raw("cloaca"), zorder=z + 1, lw=LINE * 0.7)
    out["cloaca"] = (x0 + W * 0.4, yc)
    if bladder:
        bio.shape(ax, oval((x0 + W * 0.25, yc + H * 0.03), W * 0.06, H * 0.035), token=_raw("bladder"), zorder=z + 1.1,
                  lw=LINE * 0.7)
        out["bladder"] = (x0 + W * 0.25, yc + H * 0.03)
    if labels:
        xl = x0 + W * 0.72
        tips.setdefault("gonad", out.get("gonad"))
        order = ("pronephros", "mesonephros", "opisthonephros", "metanephros", "archinephric_duct", "ureter",
                 "mullerian_duct", "gonad")
        items = [(k, tips.get(k, out[k])) for k in order if k in out]
        # labels at their anchors' heights, pushed apart where they would overlap
        top, bot, sep = y0 + H * 0.97, y0 + H * 0.04, FONT.get(size, 7) * 1.7 / 72 / 0.45
        items.sort(key=lambda kp: -kp[1][1])
        slots, prev = [], top + sep
        for _, pt in items:
            prev = min(pt[1], prev - sep)
            slots.append(prev)
        shift = max(0.0, bot - slots[-1]) if slots else 0.0
        slots = [v + shift for v in slots]
        for (k, p), yl in zip(items, slots):
            text = rename.get(k, name(k).replace(" (Wolffian)", ""))
            callout(ax, p, (xl, yl), text, size=size)
    return out
