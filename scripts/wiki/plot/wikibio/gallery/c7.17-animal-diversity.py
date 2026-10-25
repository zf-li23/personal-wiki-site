# Animal diversity: ten major phyla and the characters traditionally used to classify them. Symmetry:
# none (sponges), radial (cnidarians), biradial (ctenophores), bilateral (most phyla), pentaradial in adult
# echinoderms (their larvae are bilateral). Germ layers: sponges lack true tissues; cnidarians and
# ctenophores are diploblastic; bilaterians are triploblastic (ectoderm blue, mesoderm red, endoderm yellow).
# Body cavity: none in flatworms (acoelomate), a pseudocoel in nematodes, a coelom in annelids, molluscs
# (reduced to the pericardium and gonad cavities), arthropods (reduced; the body cavity is a haemocoel),
# echinoderms and chordates. Segmentation: metameric in annelids, fused into tagmata in arthropods, in the
# muscle blocks (myomeres) and vertebrae of chordates. Skeleton and the major clade of Bilateria close
# the table. Body cavities and segmentation are grades, gained and lost repeatedly; the clades in the last
# column (from molecular phylogenies; see the animal phylogeny) are the natural groups.
import wikibio as bio
from wikibio import animalmorph as AM
from wikibio import zoology as zoo

P = bio.P
fig, ax = bio.canvas(27.5, 25.1)

ROWS = [
    ("Porifera", "sponges", "none", 0, None, False, "spicules, spongin", "-"),
    ("Cnidaria", "jellyfish, corals", "radial", 2, "diploblast", False, "hydrostatic; CaCO$_3$ in corals", "-"),
    ("Ctenophora", "comb jellies", "biradial", 2, "diploblast", False, "hydrostatic", "-"),
    ("Platyhelminthes", "flatworms", "bilateral", 3, "acoelomate", False, "hydrostatic (parenchyma)", "Spiralia"),
    ("Nematoda", "roundworms", "bilateral", 3, "pseudocoelomate", False, "hydrostatic, cuticle", "Ecdysozoa"),
    ("Annelida", "segmented worms", "bilateral", 3, "coelomate", True, "hydrostatic (coelom)", "Spiralia"),
    ("Mollusca", "snails, clams, squid", "bilateral", 3, "coelomate", False, "shell (CaCO$_3$)", "Spiralia"),
    ("Arthropoda", "insects, crustaceans", "bilateral", 3, "coelomate", "tagmata", "chitin exoskeleton", "Ecdysozoa"),
    ("Echinodermata", "sea stars, urchins", "pentaradial", 3, "coelomate", False, "CaCO$_3$ ossicles", "Deuterostomia"),
    ("Chordata", "lancelets, vertebrates", "bilateral", 3, "coelomate", True, "notochord; bone, cartilage", "Deuterostomia"),
]
NOTES = {"Mollusca": "reduced", "Arthropoda": "reduced", "Echinodermata": "larva bilateral", "Chordata": "myomeres"}
DRAW = [
    lambda c: bio.icon(ax, "wikimedia/sponge-syconoid", at=c, height=1.75),
    lambda c: bio.icon(ax, "phylopic/jellyfish", at=c, height=1.5, color="animal"),
    lambda c: bio.icon(ax, "wikimedia/ctenophore", at=c, height=1.5),
    lambda c: bio.icon(ax, "wikimedia/planarian", at=c, width=2.4),
    lambda c: bio.icon(ax, "wikimedia/nematode-male", at=c, height=2.6, rotate=90),
    lambda c: bio.icon(ax, "wikimedia/polychaete-segments", at=c, width=2.5),
    lambda c: bio.icon(ax, "wikimedia/snail-anatomy", at=c, width=2.7),
    lambda c: bio.icon(ax, "wikimedia/grasshopper", at=c, width=2.8),
    lambda c: bio.icon(ax, "wikimedia/sea-urchin-section", at=c, width=2.6),
    lambda c: bio.icon(ax, "wikimedia/lancelet", at=c, width=2.9),
]


def cell_center(b):
    return (b[0] + b[2] / 2, b[1] + b[3] / 2)


def name_cell(name, common):
    def f(ax_, b):
        bio.label(ax_, (b[0] + 0.15, b[1] + b[3] * 0.62), name, size="normal", bold=True, ha="left")
        bio.label(ax_, (b[0] + 0.15, b[1] + b[3] * 0.32), common, size="tiny", color=P.muted(), ha="left")
    return f


def glyph(fn, *args, note=None, **kw):
    def f(ax_, b):
        c = cell_center(b)
        fn(ax_, (c[0], c[1] + (0.18 if note else 0)), *args, **kw)
        if note:
            bio.label(ax_, (c[0], b[1] + 0.25), note, size="tiny", color=P.muted())
    return f


def cavity(kind, note=None):
    def f(ax_, b):
        c = cell_center(b)
        if kind is None:
            bio.label(ax_, c, "none", size="small", color=P.muted())
            return
        zoo.body_plan(ax_, (c[0], c[1] + (0.15 if note else 0)), 0.62, kind, zorder=8)
        if note:
            bio.label(ax_, (c[0], b[1] + 0.2), note, size="tiny", color=P.muted())
    return f


def drawing(k):
    def f(ax_, b):
        DRAW[k](cell_center(b))
    return f


def text(t, size="small", bold=False):
    def f(ax_, b):
        bio.label(ax_, cell_center(b), t, size=size, bold=bold)
    return f


header = ["Phylum", "", "Symmetry", "Germ layers", "Body cavity", "Segmentation", "Skeleton", "Clade"]
cells = [header]
for k, (name, common, sym, germ, cav, seg, skel, clade) in enumerate(ROWS):
    cav_note = {"diploblast": "gut only", "acoelomate": "acoelomate", "pseudocoelomate": "pseudocoel"}.get(cav)
    if cav == "coelomate":
        cav_note = "coelom" + (", " + NOTES[name] if name in ("Mollusca", "Arthropoda") else "")
    cells.append([name_cell(name, common), drawing(k),
                  glyph(AM.symmetry, sym, note=NOTES.get(name) if name == "Echinodermata" else None),
                  glyph(AM.germ_layers, germ, note={0: "none", 2: "two", 3: "three"}[germ]),
                  cavity(cav, cav_note),
                  glyph(AM.segmentation, seg, note={True: NOTES.get(name, "metameric") if name == "Chordata" else "metameric",
                                                    "tagmata": "tagmata", False: "none"}[seg]),
                  text(skel), text(clade, bold=clade != "-")])
AM.table(ax, (0.3, 24.8), col_w=[4.2, 3.4, 2.4, 2.4, 2.6, 2.8, 5.4, 3.9], row_h=[0.8] + [2.3] * len(ROWS), cells=cells,
         align={0: "left"})
zoo.germ_layer_legend(ax, (0.6, 0.45), items=("ectoderm", "mesoderm", "endoderm", "mesoglea"),
                      cavities=("pseudocoel", "coelom"), step=3.3)
