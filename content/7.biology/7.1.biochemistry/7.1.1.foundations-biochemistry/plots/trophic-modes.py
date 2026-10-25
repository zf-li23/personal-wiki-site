# Classification of organisms by their source of energy (light or chemical fuels) and, for the
# carbon used to build cell material, by whether it comes from CO2 (autotrophs) or from organic
# compounds (heterotrophs); chemotrophs are further split by the kind of fuel they oxidize.
import wikibio as bio

fig, ax = bio.canvas(17, 8.2)
W, H = 3.6, 0.95


def node(xy, text, token, w=W, h=H, size="small"):
    bio.box(ax, xy, w, h, token, text=text, size=size)


def link(a, b):
    bio.arrow(ax, (a[0], a[1] - H / 2), (b[0], b[1] + H / 2), kind="process", shrink=0.05)


root = (8.5, 7.3)
photo, chemo = (4.4, 5.5), (12.6, 5.5)
leaves = [(2.3, 3.5), (6.5, 3.5), (10.5, 3.5), (14.7, 3.5)]
node(root, "All organisms", "neutral", w=4.2)
node(photo, "Phototrophs", "chloroplast")
node(chemo, "Chemotrophs", "mitochondrion")
link(root, photo)
link(root, chemo)
bio.label(ax, (6.2, 6.62), "energy from light", size="tiny", color=bio.P.muted(), ha="right")
bio.label(ax, (10.8, 6.62), "energy from chemical fuels", size="tiny", color=bio.P.muted(), ha="left")

names = ["Autotrophs", "Heterotrophs", "Lithotrophs", "Organotrophs"]
tokens = ["plant", "bacterium", "metabolite", "animal"]
notes = ["carbon from CO$_2$", "carbon from organic\ncompounds", "inorganic fuels\n(H$_2$, H$_2$S, NH$_4^+$, Fe$^{2+}$)",
         "organic fuels"]
examples = [
    "plants, algae,\ncyanobacteria,\npurple and green\nsulfur bacteria",
    "purple non-sulfur\nbacteria,\nheliobacteria",
    "hydrogen, sulfur,\nnitrifying and iron\nbacteria; many archaea\n(mostly autotrophic)",
    "animals, fungi,\nmost protists,\nmost bacteria",
]
for i, (xy, name, tok, note, ex) in enumerate(zip(leaves, names, tokens, notes, examples)):
    parent = photo if i < 2 else chemo
    link(parent, xy)
    node(xy, name, tok)
    bio.label(ax, (xy[0], xy[1] - 0.95), note, size="tiny", color=bio.P.muted(), va="top")
    bio.label(ax, (xy[0], xy[1] - 1.85), ex, size="tiny", va="top")
