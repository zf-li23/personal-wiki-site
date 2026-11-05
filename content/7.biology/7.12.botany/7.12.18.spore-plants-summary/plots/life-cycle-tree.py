"""Modes of sexual reproduction and life-cycle types mapped on a simplified phylogeny of algae and land
plants. Brown algae (an independent plastid lineage among the stramenopiles) are shown outside as a
comparison. Marks: O oogamy (several independent origins); S sporic meiosis with alternation of
generations (independent origins in Ulva, red algae, brown algae and, by interpolation of a multicellular
sporophyte, land plants); E embryo and multicellular jacketed gametangia; D sporophyte dominance
(vascular plants); H heterospory (several origins); Sd seeds. Columns: gametes, meiosis, dominant
generation."""
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(Brown_algae,(Red_algae,(((Chlamydomonas,Volvox)Volvocales,Ulva)Chlorophyta,(Chara,(Zygnema,"
          "((Liverworts,Mosses,Hornworts)Bryophytes,(Lycophytes,(Ferns,Seed_plants)Euph)Vascular)Land)Z)Strept)Green)Arch)Root;")
ROWS = {
    "Brown algae": ("iso- to oogamy", "sporic or gametic", "sporophyte (kelps) / diploid (fucoids)"),
    "Red algae": ("oogamy, non-flagellate", "sporic, triphasic", "gametophyte and tetrasporophyte"),
    "Chlamydomonas": ("isogamy", "zygotic", "haploid"),
    "Volvox": ("oogamy", "zygotic", "haploid"),
    "Ulva": ("isogamy", "sporic, isomorphic", "both alike"),
    "Chara": ("oogamy", "zygotic", "haploid"),
    "Zygnema": ("conjugation", "zygotic", "haploid"),
    "Liverworts": ("oogamy", "sporic", "gametophyte"),
    "Mosses": ("oogamy", "sporic", "gametophyte"),
    "Hornworts": ("oogamy", "sporic", "gametophyte"),
    "Lycophytes": ("oogamy", "sporic", "sporophyte"),
    "Ferns": ("oogamy", "sporic", "sporophyte"),
    "Seed plants": ("oogamy, pollen tube", "sporic", "sporophyte"),
}
fig, ax = bio.canvas(30, 15)
TOP, BOT = 13.0, 1.0
t = phylo.tree(ax, NEWICK, origin=(0.6, BOT), width=9.6, height=TOP - BOT, direction="right", root_edge=0.3,
               label_size="small", italic={"Chlamydomonas", "Volvox", "Ulva", "Chara", "Zygnema"},
               clades=[dict(node="Land", token="plant", style="bar", label="Land plants")],
               marks=[dict(node="Volvox", kind="trait", text="O", at=0.5, text_size="tiny"),
                      dict(node="Chara", kind="trait", text="O", at=0.5, text_size="tiny"),
                      dict(node="Red algae", kind="trait", text="S", at=0.5, text_size="tiny"),
                      dict(node="Brown algae", kind="trait", text="S", at=0.5, text_size="tiny"),
                      dict(node="Ulva", kind="trait", text="S", at=0.5, text_size="tiny"),
                      dict(node="Land", kind="trait", text="E, S", at=0.5, text_size="tiny"),
                      dict(node="Vascular", kind="trait", text="D", at=0.5, text_size="tiny"),
                      dict(node="Lycophytes", kind="star", text="H", at=0.6, text_size="tiny"),
                      dict(node="Ferns", kind="star", text="H", at=0.6, text_size="tiny"),
                      dict(node="Seed plants", kind="trait", text="Sd", at=0.6, text_size="tiny")])
XC = [16.4, 21.0, 25.4]
for x, h in zip(XC, ("Gametes", "Meiosis", "Dominant generation")):
    bio.label(ax, (x, TOP + 1.0), h, size="small", bold=True, ha="left")
for tip in t.tips():
    for x, v in zip(XC, ROWS[tip.name]):
        bio.label(ax, (x, tip.xy[1]), v, size="small", ha="left", color=P.ink())
