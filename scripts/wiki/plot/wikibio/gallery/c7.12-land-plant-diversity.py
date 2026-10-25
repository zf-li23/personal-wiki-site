# Diversity of land plants shown through their diagnostic characters. Left: a cladogram of the major
# lineages (charophyte green algae as the outgroup; bryophytes monophyletic, hornworts sister to mosses +
# liverworts; lycophytes sister to euphyllophytes; horsetails within the ferns; gnetophytes nested among
# the conifers, close to the pine family, simplified here as sister to the other conifers; magnoliids,
# monocots and eudicots in the core angiosperms after the ANA grade of Amborella and water lilies).
# Numbered bars mark the origin of key characters (key at the bottom). Right: a drawing of each group and
# its character states: embryo protected by the parent plant, lignified vascular tissue (xylem and phloem),
# seeds, flowers with carpels (fruits), and the dominant, long-lived generation of the life cycle.
# Filled circle: present; open circle: absent.
import wikibio as bio
from wikibio import phylo
from wikibio import plantmorph as PM

P = bio.P
NEWICK = ("(Charophyte_algae,(((Liverworts,Mosses)Setaphyta,Hornworts)Bryophytes,(Lycophytes,((Horsetails,Ferns)Monilophytes,"
          "(((Cycads,Ginkgo),(Gnetophytes,Conifers))Gymnosperms,(Amborella,(Water_lilies,(Magnoliids,(Monocots,Eudicots))))Angiosperms)"
          "Seed_plants)Euphyllophytes)Vascular_plants)Land_plants);")
ROWS = {  # tip: (embryo, vascular, seeds, flowers, dominant generation)
    "Charophyte algae": (False, False, False, False, "haploid only"),
    "Liverworts": (True, False, False, False, "gametophyte"),
    "Mosses": (True, False, False, False, "gametophyte"),
    "Hornworts": (True, False, False, False, "gametophyte"),
    "Lycophytes": (True, True, False, False, "sporophyte"),
    "Horsetails": (True, True, False, False, "sporophyte"),
    "Ferns": (True, True, False, False, "sporophyte"),
    "Cycads": (True, True, True, False, "sporophyte"),
    "Ginkgo": (True, True, True, False, "sporophyte"),
    "Gnetophytes": (True, True, True, False, "sporophyte"),
    "Conifers": (True, True, True, False, "sporophyte"),
    "Amborella": (True, True, True, True, "sporophyte"),
    "Water lilies": (True, True, True, True, "sporophyte"),
    "Magnoliids": (True, True, True, True, "sporophyte"),
    "Monocots": (True, True, True, True, "sporophyte"),
    "Eudicots": (True, True, True, True, "sporophyte"),
}
INNOVATIONS = [
    ("Land plants", "Embryo retained on the parent; cuticle; sporopollenin-walled spores; multicellular gametangia"),
    ("Vascular plants", "Lignified xylem and phloem; branched, dominant sporophyte"),
    ("Euphyllophytes", "Megaphylls (leaves with branched veins)"),
    ("Seed plants", "Seeds; pollen grains (reduced male gametophytes)"),
    ("Angiosperms", "Flowers, carpels (fruit), double fertilization, endosperm"),
]

fig, ax = bio.canvas(30.0, 21.4)
TOP, BOT = 19.6, 3.6
t = phylo.tree(ax, NEWICK, origin=(0.6, BOT), width=6.2, height=TOP - BOT, direction="right", root_edge=0.4,
               label_size="small", clades=[
                   dict(node="Bryophytes", token="plant", style="bar", label="Bryophytes"),
                   dict(node="Gymnosperms", token="bract", style="bar", label="Gymnosperms"),
                   dict(node="Angiosperms", token="petal", style="bar", label="Angiosperms"),
               ], marks=[dict(node=n, kind="trait", text=str(k + 1), at=0.5, text_size="tiny", side=-1, offset=0.25, va="bottom")
                         for k, (n, _) in enumerate(INNOVATIONS)])
ys = {tip.name: tip.xy[1] for tip in t.tips()}

XD, XC = 13.2, [15.6, 17.6, 19.6, 21.6]  # drawing column, character columns
XG = 24.6
head = TOP + 1.0
for x, text in zip(XC, ("Embryo", "Vascular\ntissue", "Seeds", "Flowers,\nfruit")):
    bio.label(ax, (x, head), text, size="small", bold=True, va="center")
bio.label(ax, (XG, head), "Dominant\ngeneration", size="small", bold=True)
ax.plot([10.6, 26.6], [TOP + 0.45] * 2, color=P.muted(), lw=0.8)

H = 1.2  # drawing height per row
for tip, (emb, vas, sds, flw, gen) in ROWS.items():
    y = ys[tip]
    for x, st in zip(XC, (emb, vas, sds, flw)):
        PM.presence(ax, (x, y), st)
    bio.label(ax, (XG, y), gen.capitalize(), size="small", color=P.edge("dna") if gen == "sporophyte" else P.edge("rna")
              if gen == "gametophyte" else P.muted())
# drawings (literal icon ids for the build)
bio.icon(ax, "phylopic/chara", at=(XD, ys["Charophyte algae"]), height=H, color="plant")
bio.icon(ax, "phylopic/liverwort", at=(XD, ys["Liverworts"]), height=H * 0.85, color="plant")
bio.icon(ax, "wikimedia/moss-gametophyte-sporophyte", at=(XD, ys["Mosses"]), height=H * 1.05)
bio.icon(ax, "phylopic/hornwort", at=(XD, ys["Hornworts"]), height=H * 0.85, color="plant")
bio.icon(ax, "phylopic/clubmoss", at=(XD, ys["Lycophytes"]), height=H * 0.9, color="plant")
bio.icon(ax, "phylopic/horsetail", at=(XD, ys["Horsetails"]), height=H, color="plant")
bio.icon(ax, "wikimedia/fern-sporophyte", at=(XD, ys["Ferns"]), height=H)
bio.icon(ax, "phylopic/cycad", at=(XD, ys["Cycads"]), height=H, color="plant")
bio.icon(ax, "phylopic/ginkgo", at=(XD, ys["Ginkgo"]), height=H * 0.85, color="plant")
bio.icon(ax, "phylopic/welwitschia", at=(XD, ys["Gnetophytes"]), height=H * 0.7, color="plant")
bio.icon(ax, "wikimedia/pine-branch-cone", at=(XD, ys["Conifers"]), height=H)
bio.icon(ax, "phylopic/amborella", at=(XD, ys["Amborella"]), height=H * 0.8, color="plant")
bio.icon(ax, "phylopic/water-lily", at=(XD, ys["Water lilies"]), height=H * 0.7, color="plant")
bio.icon(ax, "phylopic/magnolia", at=(XD, ys["Magnoliids"]), height=H * 0.85, color="plant")
bio.icon(ax, "phylopic/orchid", at=(XD, ys["Monocots"]), height=H, color="plant")
bio.icon(ax, "phylopic/arabidopsis", at=(XD, ys["Eudicots"]), height=H, color="plant")

# key of innovations
x0, y0 = 0.8, 2.5
bio.label(ax, (x0, y0 + 0.4), "Key innovations", size="small", bold=True, ha="left")
for k, (_, text) in enumerate(INNOVATIONS):
    yy = y0 - 0.38 * (k + 0.5)
    phylo.marker(ax, (x0 + 0.12, yy), "trait", size=0.14, direction=(1, 0))
    bio.label(ax, (x0 + 0.35, yy), f"{k + 1}  {text}", size="tiny", ha="left")
for k, (st, text) in enumerate(((True, "present"), (False, "absent"))):
    PM.presence(ax, (16.0 + 2.6 * k, 2.1), st, size=0.15)
    bio.label(ax, (16.3 + 2.6 * k, 2.1), text, size="small", ha="left")
