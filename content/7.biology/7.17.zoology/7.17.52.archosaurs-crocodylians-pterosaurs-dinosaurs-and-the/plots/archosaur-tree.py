# Time-scaled tree of the archosaurs (simplified after Nesbitt 2011, Ezcurra et al. 2020, Langer et al.
# 2017 and Pough et al. 2023). Branch tips end at the last occurrence of each group (extinct groups end in
# the past); node ages are approximate first appearances or molecular estimates, in Ma. The crocodile line
# (Pseudosuchia) and the bird line (Avemetatarsalia) diverged in the Early Triassic. Only two archosaur
# lineages survive: crown crocodylians and birds.
import wikibio as bio
from wikibio import phylo

P = bio.P
# (name, age of the node) and children; tips are (name, last occurrence)
TREE = ("Archosauria", 250, [
    ("Pseudosuchia", 248, [
        ("Aetosauria", 201),
        ("Poposauroidea", 201),
        ("Crocodylomorpha", 235, [
            ("Thalattosuchia", 125),
            ("Notosuchia", 11),
            ("Crocodylia", 0)])]),
    ("Avemetatarsalia", 247, [
        ("Pterosauria", 66),
        ("Dinosauriformes", 242, [
            ("Silesauridae", 205),
            ("Dinosauria", 233, [
                ("Ornithischia", 66),
                ("Saurischia", 231, [
                    ("Sauropodomorpha", 66),
                    ("Theropoda", 230, [
                        ("non-avian theropods", 66),
                        ("Paraves", 168, [
                            ("deinonychosaurs", 66),
                            ("Aves", 0)])])])])])])])


def newick(node, parent_age=None):
    name, age = node[0], node[1]
    label = name.replace(" ", "_")
    ln = "" if parent_age is None else f":{parent_age - age}"
    if len(node) == 2:
        return f"{label}{ln}"
    return "(" + ",".join(newick(c, age) for c in node[2]) + f"){label}{ln}"


NEWICK = newick(TREE) + ";"
ICONS = {"Aetosauria": "phylopic/aetosaur", "Poposauroidea": "phylopic/postosuchus",
         "Crocodylia": "phylopic/crocodile", "Pterosauria": "phylopic/pterosaur",
         "Ornithischia": "phylopic/stegosaur", "Sauropodomorpha": "phylopic/sauropod",
         "non-avian theropods": "phylopic/tyrannosaurus", "deinonychosaurs": "phylopic/velociraptor", "Aves": "phylopic/pigeon"}
TEXT = {"Aetosauria": "†Aetosauria", "Poposauroidea": "†Poposauroidea, 'rauisuchians'",
        "Thalattosuchia": "†Thalattosuchia (marine)", "Notosuchia": "†Notosuchia (terrestrial)",
        "Crocodylia": "Crocodylia (crown)", "Pterosauria": "†Pterosauria", "Silesauridae": "†Silesauridae",
        "Ornithischia": "†Ornithischia", "Sauropodomorpha": "†Sauropodomorpha",
        "non-avian theropods": "†non-avian theropods", "Aves": "Aves (birds)",
        "deinonychosaurs": "\u2020deinonychosaurs"}
fig, ax = bio.canvas(27, 12.5)
t = phylo.tree(ax, NEWICK, origin=(0.8, 2.4), width=14.5, height=9.4, scaled=True, root_edge=3.0, icons=ICONS,
               icon_size=0.55, icon_width=1.4, icon_color="animal", label_size="small", tip_text=TEXT,
               clades=[dict(node="Pseudosuchia", token="dna", style="branch", label="crocodile line"),
                       dict(node="Avemetatarsalia", token="mrna", style="branch", label="bird line")],
               marks=[dict(node="Dinosauria", kind="trait", text="perforate acetabulum", at=0.5, text_size="tiny",
                           side=-1, offset=0.3, va="bottom"),
                      dict(node="Paraves", kind="trait", text="pennaceous wings", at=0.5, text_size="tiny",
                           side=-1, offset=0.3, va="bottom")])
t.time_axis(ax, ticks=[250, 200, 150, 100, 50, 0], y=1.9)
t.geo_scale(ax, y=1.3, ranks=("period",), age_range=(253, 0))
for age, txt in ((201.4, "end-Triassic extinction"), (66.0, "K-Pg extinction")):
    x = t.x_of_age(age)
    ax.plot([x, x], [2.3, 11.9], color=P.muted(), lw=0.8, ls=(0, (3, 3)), zorder=3)
    bio.label(ax, (x, 12.2), txt, size="tiny", color=P.muted())
bio.label(ax, (0.8, 0.25), "Ma; † extinct; tips end at the last known occurrence", size="tiny",
          color=P.muted(), ha="left")
