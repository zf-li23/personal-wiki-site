# A time-calibrated tree of jawed vertebrates (a chronogram) on the ICS geological time scale.
# Divergence times are approximate median estimates (TimeTree 5, Kumar et al. 2022), in Myr.
import wikibio as bio
from wikibio import phylo


def clade(age, *children):
    """Newick for a node of the given age (Ma); children are (newick, age) pairs."""
    parts = [f"{nw}:{age - a:g}" for nw, a in children]
    return "(" + ",".join(parts) + ")", age


def tip(name):
    return name.replace(" ", "_"), 0.0


primates = clade(28.8, clade(6.4, tip("Homo sapiens"), tip("Pan troglodytes")), tip("Macaca mulatta"))
boreo = clade(94, clade(87, primates, tip("Mus musculus")), clade(76, tip("Canis lupus"), tip("Bos taurus")))
theria = clade(160, clade(99, boreo, tip("Loxodonta africana")),
               clade(80, tip("Didelphis virginiana"), tip("Macropus giganteus")))
mammals = clade(180, theria, tip("Ornithorhynchus anatinus"))
sauropsids = clade(280, tip("Anolis carolinensis"),
                   clade(255, tip("Chelonia mydas"), clade(247, tip("Crocodylus niloticus"), tip("Gallus gallus"))))
tetrapods = clade(352, clade(319, mammals, sauropsids), tip("Xenopus laevis"))
root = clade(465, clade(429, tetrapods, tip("Danio rerio")), tip("Carcharodon carcharias"))
NEWICK = root[0] + ";"

ICONS = {
    "Homo sapiens": "phylopic/human", "Pan troglodytes": "phylopic/chimpanzee", "Macaca mulatta": "phylopic/macaque",
    "Mus musculus": "phylopic/mouse", "Canis lupus": "phylopic/wolf", "Bos taurus": "phylopic/cattle",
    "Loxodonta africana": "phylopic/african-elephant", "Didelphis virginiana": "phylopic/opossum",
    "Macropus giganteus": "phylopic/kangaroo", "Ornithorhynchus anatinus": "phylopic/platypus",
    "Anolis carolinensis": "phylopic/anole", "Chelonia mydas": "phylopic/green-turtle",
    "Crocodylus niloticus": ("phylopic/nile-crocodile", {"rotate": -90}), "Gallus gallus": "phylopic/chicken",
    "Xenopus laevis": "phylopic/xenopus", "Danio rerio": "phylopic/zebrafish",
    "Carcharodon carcharias": "phylopic/great-white-shark",
}

fig, ax = bio.canvas(22, 12.6)
t = phylo.tree(ax, NEWICK, origin=(0.6, 2.2), width=14.2, height=9.6, scaled=True, span=500, italic=True,
               icons=ICONS, icon_size=0.5, icon_width=1.25,
               clades=[dict(tips=["Homo sapiens", "Ornithorhynchus anatinus"], token="animal", style=("branch", "bar"),
                            label="Mammals"),
                       dict(tips=["Anolis carolinensis", "Gallus gallus"], token="dna", style=("branch", "bar"),
                            label="Reptiles\n(incl. birds)")],
               marks=[dict(node=["Homo sapiens", "Gallus gallus"], kind="dot", text="Amniota 319 Ma", side=-1),
                      dict(node=["Homo sapiens", "Danio rerio"], kind="dot", text="Osteichthyes 429 Ma", side=-1)])
t.time_lines(ax, [251.902, 66.0], ["End-Permian", "K–Pg"], y0=1.25, y1=t.frame[1] + t.frame[3] + 0.25)
y = t.time_axis(ax, ticks=[500, 400, 300, 200, 100, 0], minor=list(range(450, 0, -100)), y=1.95)
t.geo_scale(ax, y=1.25, ranks=("era", "period"), height=0.42)
