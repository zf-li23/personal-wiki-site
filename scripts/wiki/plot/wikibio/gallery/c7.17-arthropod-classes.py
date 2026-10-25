# The four living arthropod lineages compared by their diagnostic characters. Arthropods share a
# segmented body with a jointed chitinous exoskeleton moulted during growth, jointed appendages and an
# open circulatory system (haemocoel); the lineages differ in how segments are grouped into tagmata and in
# their appendages. Insects: head, thorax (three pairs of legs, usually two pairs of wings), abdomen; one
# pair of antennae; mandibles; tracheae. Arachnids (a spider, internal anatomy): prosoma (cephalothorax)
# and opisthosoma (abdomen) joined by the pedicel; no antennae; chelicerae and pedipalps; four pairs of
# legs; book lungs and/or tracheae. Crustaceans (an amphipod): cephalon, pereon (thorax) and pleon
# (abdomen) with many, often biramous appendages; two pairs of antennae; gills. Myriapods (a centipede):
# head and a long trunk with one leg pair per segment (two per diplosegment in millipedes); one pair of
# antennae; tracheae. Crustaceans are paraphyletic: insects arose within them (Pancrustacea).
import wikibio as bio
from wikibio import animalmorph as AM

P = bio.P
fig, ax = bio.canvas(28, 16.4)
H, T, A, C = AM.TAGMA["head"], AM.TAGMA["thorax"], AM.TAGMA["abdomen"], AM.TAGMA["cephalothorax"]
YD = 12.6  # drawings
YB = 10.0  # tagma bars

titles = [("Insecta", "grasshopper"), ("Arachnida", "spider (internal anatomy)"), ("Crustacea", "amphipod"),
          ("Myriapoda", "centipede")]
X = [3.6, 10.6, 17.6, 24.4]
for (t, sub), x in zip(titles, X):
    bio.label(ax, (x, 16.0), t, size="title", bold=True)
    bio.label(ax, (x, 15.5), sub, size="small", color=P.muted())

# insect
g = AM.Specimen("wikimedia/grasshopper", at=(X[0], YD), width=6.0)
g.draw(ax, parts={"head": H, "mouthparts": H, "antenna": H, "compound-eye": H, "pronotum": T, "pterothorax": T,
                  "forewing": T, "foreleg": T, "midleg": T, "hind-femur": T, "hind-tibia": T, "hind-tarsus": T,
                  "abdomen": A}, mute="neutral")
x0 = g.point("antenna", where="left")[0]
xh = g.point("pronotum", where="left")[0]
xt = g.point("pterothorax", where="right")[0]
x1 = g.point("abdomen", where="right")[0]
for a, b, tok, name in ((x0 + 0.6, xh, H, "Head"), (xh, xt, T, "Thorax"), (xt, x1, A, "Abdomen")):
    AM.bracket(ax, (a + 0.03, YB), (b - 0.03, YB), name, token=tok, side=-1, depth=0.24)

# arachnid
s = AM.Specimen("wikimedia/spider-internal", at=(X[1], YD), width=6.2)
s.draw(ax, parts={"heart": "blood", "digestive-tubules": "golgi", "silk-gland": "positive", "book-lung": "channel",
                  "venom-gland": "drug", "nervous-system": "neuron"}, mute="neutral")
sx, sy, sw, sh = s.box
for a, b, tok, name in ((0.06, 0.43, C, "Prosoma"), (0.47, 0.99, A, "Opisthosoma")):
    AM.bracket(ax, (sx + a * sw, YB), (sx + b * sw, YB), name, token=tok, side=-1, depth=0.24)
AM.callouts(ax, [(s.point("silk-gland"), "Silk glands", "right"),
                 (s.point("venom-gland"), "Venom gland", "left")], left=sx - 0.1, right=sx + sw + 0.1, gap=0.5,
            bottom=YB + 0.6)

# crustacean
c = AM.Specimen("wikimedia/amphipod", at=(X[2], YD), width=5.6)
c.draw(ax, parts={"cephalon": H, "eye": H, "pereon": T, "pleon": A, "urosome": A, "telson": A}, mute="neutral")
c1 = c.point("pereon", where="left")[0]
c2 = c.point("pereon", where="right")[0]
c3 = c.point("telson", where="right")[0]
for a, b, tok, name in ((c.point("eye")[0] - 0.45, c1, H, "Cephalon"), (c1, c2, T, "Pereon"), (c2, c3, A, "Pleon")):
    AM.bracket(ax, (a + 0.03, YB), (b - 0.03, YB), name, token=tok, side=-1, depth=0.24)

# myriapod (dorsal view, head to the left)
m = AM.Specimen("wikimedia/centipede", at=(X[3], YD), height=5.6, rotate=90)
m.draw(ax)
mx, my, mw, mh = m.box
for a, b, tok, name in ((0.0, 0.1, H, "Head"), (0.1, 1.0, A, "Trunk")):
    AM.bracket(ax, (mx + a * mw + 0.03, YB), (mx + b * mw - 0.03, YB), name, token=tok, side=-1, depth=0.24)

# character table
rows = [["", "Insecta", "Arachnida", "Crustacea", "Myriapoda"],
        ["Tagmata", "head, thorax, abdomen", "prosoma, opisthosoma", "cephalon, pereon, pleon", "head, trunk"],
        ["Antennae", "1 pair", "none", "2 pairs", "1 pair"],
        ["Feeding appendages", "mandibles, maxillae", "chelicerae, pedipalps", "mandibles, 2 pairs of maxillae",
         "mandibles, maxillae"],
        ["Walking legs", "3 pairs (thorax)", "4 pairs (prosoma)", "many, often biramous", "1 or 2 pairs per segment"],
        ["Wings", "usually 2 pairs", "none", "none", "none"],
        ["Respiration", "tracheae", "book lungs, tracheae", "gills", "tracheae"],
        ["Excretion", "Malpighian tubules", "Malpighian tubules, coxal glands", "antennal (green) glands",
         "Malpighian tubules"]]
AM.table(ax, (0.4, 8.6), col_w=[3.8, 5.95, 5.95, 5.95, 5.95], row_h=[0.75] + [0.95] * 7, cells=rows)
