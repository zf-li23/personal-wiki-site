# Ten insect orders and their diagnostic characters, each insect generated from body-plan rules
# (wikibio.zoomorph) and drawn as a set specimen, next to a cladogram of the orders after current
# phylogenomic consensus (Misof et al. 2014, Science 346:763; Wipfler et al. 2019, PNAS 116:3024):
# Polyneoptera (here Orthoptera, Blattodea incl. termites), Hemiptera (Acercaria) and Holometabola,
# within which Hymenoptera are sister to all others and Neuropterida + Coleoptera are sister to
# Lepidoptera + Diptera (Mecopterida). The relationship of mayflies, dragonflies and Neoptera is
# unresolved (Palaeoptera, marked "?"). Wing types are colour coded (key below), mouthparts are shown in
# lateral head insets coloured by homology (labrum, mandible, maxilla, labium). Bars on the tree mark
# key innovations. Hemelytra are diagnostic of Heteroptera, not of all Hemiptera; termites (former
# Isoptera) are nested within Blattodea.
import wikibio as bio
from wikibio import phylo
from wikibio import zoomorph as zm

P = bio.P
NEWICK = ("(((Ephemeroptera,Odonata)Palaeoptera,((Orthoptera,Blattodea)Polyneoptera,(Hemiptera,"
          "(Hymenoptera,((Neuroptera,Coleoptera)Neuropteroidea,(Lepidoptera,Diptera)Mecopterida)Aparaglossata)"
          "Holometabola)Eumetabola)Neoptera)Pterygota);")
ORDER = ["Ephemeroptera", "Odonata", "Orthoptera", "Blattodea", "Hemiptera", "Hymenoptera", "Neuroptera", "Coleoptera",
         "Lepidoptera", "Diptera"]
STEP, TOP = 3.42, 36.5
Y = {o: TOP - i * STEP for i, o in enumerate(ORDER)}
XI = 12.4  # insect column
XC = 15.9  # callout text column
XH = 24.6  # head insets

fig, ax = bio.canvas(31.5, 40.8)
INNOV = [("Pterygota", "Wings"), ("Neoptera", "Wings fold back over the abdomen"),
         ("Holometabola", "Complete metamorphosis (larva, pupa)")]
MARKS = [dict(node=n, kind="trait", text=str(k + 1), at=0.5, text_size="tiny", side=-1, offset=0.28, va="bottom")
         for k, (n, _) in enumerate(INNOV)]
t = phylo.tree(ax, NEWICK, origin=(0.7, Y["Diptera"]), width=4.6, height=Y["Ephemeroptera"] - Y["Diptera"], root_edge=0.4,
               tip_labels=False, marks=MARKS,
               clades=[dict(node="Holometabola", token="positive", style="branch"),
                       dict(node="Polyneoptera", token="antibody", style="branch")])
pal = t.node("Palaeoptera")
bio.label(ax, (pal.xy[0] - 0.12, pal.xy[1] + 0.12), "?", size="normal", bold=True, color=P.muted(), ha="right", va="bottom")
for name in ("Palaeoptera", "Polyneoptera", "Holometabola"):
    nd = t.node(name)
    bio.label(ax, (nd.xy[0] - 0.08, nd.xy[1] - 0.25), name, size="tiny", ha="right", va="top", color=P.muted())

SIZE = {"Ephemeroptera": 2.35, "Odonata": 2.75, "Orthoptera": 2.75, "Blattodea": 2.5, "Hemiptera": 2.6, "Neuroptera": 2.4,
        "Coleoptera": 2.45, "Hymenoptera": 2.6, "Lepidoptera": 2.2, "Diptera": 2.3}
SHIFT = {"Ephemeroptera": 0.35, "Odonata": 0.25, "Coleoptera": 0.0, "Orthoptera": 0.2}
OVER = {"Ephemeroptera": dict(cerci=0.45)}
MOUTH = {"Ephemeroptera": ("vestigial", "Vestigial (adults do not feed)"), "Odonata": ("chewing", "Chewing"),
         "Orthoptera": ("chewing", "Chewing"), "Blattodea": ("chewing", "Chewing"),
         "Hemiptera": ("piercing-sucking", "Piercing-sucking beak"), "Neuroptera": ("chewing", "Chewing"),
         "Coleoptera": ("chewing", "Chewing"), "Hymenoptera": ("chewing", "Chewing (chewing-lapping in bees)"),
         "Lepidoptera": ("siphoning", "Siphoning proboscis"), "Diptera": ("sponging", "Sponging (piercing in mosquitoes)")}
# (anchor, text) callouts per order
CALL = {
    "Ephemeroptera": [("hindwing", "Hind wings much reduced"), ("caudal_filament", "2-3 long caudal filaments")],
    "Odonata": [("nodus", "Nodus; dense venation"), ("pterostigma", "Pterostigma"), ("hindwing", "Two similar pairs")],
    "Orthoptera": [("forewing", "Tegmina (leathery forewings)"), ("hindwing", "Fan-folded hind wings"),
                   ("hind_femur", "Saltatorial hind legs")],
    "Blattodea": [("pronotum", "Shield-like pronotum over head"), ("forewing", "Tegmina"), ("cerci", "Cerci")],
    "Hemiptera": [("corium", "Hemelytron: corium"), ("membrane", "... and membrane"), ("scutellum", "Scutellum")],
    "Neuroptera": [("forewing", "Net-veined wings, many crossveins"), ("hindwing", "Hind wings similar")],
    "Coleoptera": [("elytron", "Elytra meet in a straight line"), ("hindwing", "Membranous hind wing, folded at rest")],
    "Hymenoptera": [("hind_hamuli", "Hamuli couple the smaller hind wing"), ("petiole", "Wasp waist (petiole)"),
                    ("antenna", "Elbowed antennae")],
    "Lepidoptera": [("forewing", "Wings covered in scales"), ("antenna_club", "Clubbed antennae (butterflies)")],
    "Diptera": [("forewing", "One pair of wings"), ("haltere", "Halteres (reduced hind wings)")],
}
COMMON = {o: zm.ORDERS[o]["common"] for o in ORDER}

for o in ORDER:
    y = Y[o]
    bio.label(ax, (5.75, y + 0.2), o, size="normal", bold=True, ha="left")
    bio.label(ax, (5.75, y - 0.25), COMMON[o], size="tiny", ha="left", color=P.muted())
    a = zm.insect(ax, (XI, y + SHIFT.get(o, 0.15)), SIZE[o], o, **OVER.get(o, {}))
    a["hind_femur"] = a["legs"]["hind"]["femur"]
    calls = CALL[o]
    n = len(calls)
    for k, (key, text) in enumerate(calls):
        ty = y + 0.6 - k * (1.2 / max(1, n - 1)) if n > 1 else y
        bio.callout(ax, a[key], (XC, ty), text, size="tiny")
    m, mtext = MOUTH[o]
    h = zm.head(ax, (XH, y + 0.45), 0.5, m, facing="left", antenna_kind=False)
    bio.label(ax, (XH + 0.95, y + 0.15), mtext, size="tiny", ha="left")

# column headers
for x, text, ha in ((5.75, "Order", "left"), (XI, "Wings and body (dorsal)", "center"), (XC, "Diagnostic characters", "left"),
                    (XH, "Mouthparts", "center")):
    bio.label(ax, (x, TOP + 2.55), text, size="small", bold=True, ha=ha)
bio.label(ax, (0.7, TOP + 2.55), "Phylogeny", size="small", bold=True, ha="left")

# keys
yk = 1.5
bio.label(ax, (0.7, yk + 0.55), "Innovations", size="small", bold=True, ha="left")
for k, (_, text) in enumerate(INNOV):
    phylo.marker(ax, (0.85, yk - k * 0.42), "trait", size=0.13)
    bio.label(ax, (1.05, yk - k * 0.42), f"{k + 1}  {text}", size="tiny", ha="left")
bio.label(ax, (9.6, yk + 0.55), "Wing types", size="small", bold=True, ha="left")
WK = [("membrane", "Membranous"), ("tegmen", "Tegmen / corium"), ("elytron", "Elytron"), ("scales", "Scaled"),
      ("haltere", "Haltere")]
for k, (role, text) in enumerate(WK):
    x = 9.7 + (k % 3) * 3.3
    yy = yk - (k // 3) * 0.5
    tok = zm.WING[role]
    bio.shape(ax, [(x - 0.15, yy - 0.15), (x + 0.15, yy - 0.15), (x + 0.15, yy + 0.15), (x - 0.15, yy + 0.15)], tok, lw=0.8, zorder=20)
    bio.label(ax, (x + 0.3, yy), text, size="tiny", ha="left")
bio.label(ax, (20.6, yk + 0.55), "Mouthpart homology", size="small", bold=True, ha="left")
for k, part in enumerate(("labrum", "mandible", "maxilla", "labium")):
    x = 20.7 + (k % 2) * 3.4
    yy = yk - (k // 2) * 0.5
    tok = zm.MOUTH[part]
    bio.shape(ax, [(x - 0.15, yy - 0.15), (x + 0.15, yy - 0.15), (x + 0.15, yy + 0.15), (x - 0.15, yy + 0.15)], tok, lw=0.8, zorder=20)
    bio.label(ax, (x + 0.3, yy), part.capitalize(), size="tiny", ha="left")
