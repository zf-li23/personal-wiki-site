# Anatomy of a conjugative R plasmid (schematic, modelled on the IncF resistance plasmids such as R1 and R100;
# positions are illustrative, not those of a particular plasmid). The backbone carries the functions of the
# plasmid itself: replication (oriV, rep) with copy-number control, partition (par), a toxin-antitoxin
# module, and the tra region with the origin of transfer oriT. The accessory genes sit in mobile elements
# inserted into the backbone: a composite transposon Tn10 (tetracycline resistance between two IS10), a
# Tn3-family transposon carrying bla (ampicillin resistance), and a Tn21-like transposon that carries mercury
# resistance (mer) and a class 1 integron with resistance gene cassettes (aadA, streptomycin/spectinomycin)
# followed by sul1 (sulfonamides).
import wikibio as bio
from wikibio import genetics as G

P = bio.P
fig, ax = bio.canvas(22.0, 11.0)
SIZE = 94000
backbone = "dna"
acc = "receptor"
G.plasmid(ax, (7.0, 5.5), 3.4, SIZE, name="R plasmid", ring=0.34, label_gap=0.7, features=[
    {"name": "Tn3: bla (AmpR)", "start": 2000, "end": 6900, "strand": 1, "token": acc, "inside": False},
    {"name": "IS10", "start": 12000, "end": 13300, "strand": 1, "token": "highlight", "label": False},
    {"name": "tet (TetR)", "start": 14600, "end": 17600, "strand": -1, "token": acc, "italic": True, "inside": False},
    {"name": "IS10 ", "start": 19700, "end": 21000, "strand": -1, "token": "highlight", "label": False},
    {"name": "Tn10", "start": 12000, "end": 21000, "strand": 0, "token": "highlight", "track": 1, "inside": False},
    {"name": "tra region: pilus, T4SS, relaxase", "start": 27000, "end": 61000, "strand": -1, "token": backbone, "inside": False},
    {"name": "oriT", "start": 61800, "end": 62600, "strand": 0, "token": "highlight", "bold": True, "inside": False},
    {"name": "mer (Hg resistance)", "start": 69000, "end": 73500, "strand": 1, "token": acc, "inside": False},
    {"name": "intI1", "start": 75000, "end": 76000, "strand": -1, "token": "enzyme", "italic": True, "inside": False},
    {"name": "aadA cassette", "start": 76300, "end": 77200, "strand": 1, "token": acc, "inside": False},
    {"name": "sul1", "start": 77600, "end": 78500, "strand": 1, "token": acc, "italic": True, "inside": False},
    {"name": "Tn21-like transposon", "start": 68000, "end": 81000, "strand": 0, "token": "highlight", "track": 1,
     "inside": False},
    {"name": "oriV, rep (copy-number control)", "start": 84500, "end": 88500, "strand": 1, "token": backbone,
     "inside": False},
    {"name": "par (partition)", "start": 89000, "end": 91200, "strand": 1, "token": backbone, "inside": False},
    {"name": "toxin-antitoxin", "start": 91800, "end": 92800, "strand": 1, "token": "enzyme", "inside": False},
])

# key
x0, y = 14.6, 9.6
bio.label(ax, (x0, y), "Modules", size="normal", bold=True, ha="left")
rows = [
    (backbone, "Backbone: replication, partition, transfer"),
    ("enzyme", "Maintenance and recombination enzymes"),
    (acc, "Accessory genes: resistance"),
    ("highlight", "Mobile elements: IS, transposons; oriT"),
]
for k, (tok, text) in enumerate(rows):
    yy = y - 0.8 - 0.7 * k
    bio.box(ax, (x0 + 0.3, yy), 0.45, 0.32, token=tok, radius=0.05)
    bio.label(ax, (x0 + 0.75, yy), text, size="small", ha="left")
notes = [
    "Resistance genes travel in nested units:",
    "a gene cassette in an integron, the integron in a",
    "transposon, the transposon in a conjugative plasmid.",
    "One conjugation event can transfer resistance",
    "to several unrelated drugs at once.",
]
for k, line in enumerate(notes):
    bio.label(ax, (x0, 5.2 - 0.48 * k), line, size="small", ha="left", color=P.muted())
