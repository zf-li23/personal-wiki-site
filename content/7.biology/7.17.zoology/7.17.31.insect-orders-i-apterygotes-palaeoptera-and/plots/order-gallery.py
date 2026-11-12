# Representatives of the apterygote, palaeopteran and polyneopteran orders (PhyloPic silhouettes, not to
# scale), coloured by lineage as in the order-diversity figure of 7.17.22, each with the characters that
# identify the order in the field. Species numbers are approximate recent counts.
import wikibio as bio
from wikibio.icons import size as icon_size

P = bio.P
CELLS = [
    ("Archaeognatha", "jumping bristletails", "~500", "bone", "phylopic/bristletail",
     "humped thorax; eyes meet;\n3 tails; monocondylic mandible"),
    ("Zygentoma", "silverfish", "~550", "bone", "phylopic/silverfish",
     "flattened, scaly; eyes small;\n3 tails of equal length"),
    ("Ephemeroptera", "mayflies", "~3,500", "channel", "phylopic/mayfly2",
     "wings upright; hind wing small;\n2-3 tails; subimago"),
    ("Odonata", "dragonflies, damselflies", "~6,400", "channel", "phylopic/dragonfly-libellulid",
     "huge eyes; nodus, pterostigma;\nlabial mask in nymph"),
    ("Plecoptera", "stoneflies", "~3,800", "positive", "phylopic/stonefly",
     "wings flat, hind anal lobe;\nlong cerci; aquatic nymph"),
    ("Dermaptera", "earwigs", "~2,000", "positive", "phylopic/earwig",
     "short tegmina; cerci\nform forceps"),
    ("Zoraptera", "angel insects", "~50", "positive", "phylopic/zorapteran",
     "minute; 9-segmented beaded\nantennae; tarsi 2"),
    ("Orthoptera", "grasshoppers, crickets", "~29,000", "positive", "phylopic/grasshopper",
     "jumping hind legs; saddle\npronotum; tympana"),
    ("Phasmatodea", "stick and leaf insects", "~3,500", "positive", "phylopic/stick-insect",
     "twig- or leaf-like; long\nmeso- and metathorax"),
    ("Embioptera", "webspinners", "~400", "positive", "phylopic/webspinner",
     "swollen fore basitarsus\nspins silk"),
    ("Grylloblattodea", "ice crawlers", "~35", "positive", "phylopic/ice-crawler",
     "wingless, pale; long cerci;\nsword ovipositor"),
    ("Mantophasmatodea", "heel-walkers", "~20", "positive", "phylopic/heelwalker",
     "wingless; walks with tarsal\ntips raised"),
    ("Mantodea", "mantises", "~2,500", "positive", "phylopic/mantis",
     "raptorial forelegs; long\nprothorax; mobile head"),
    ("Blattodea", "cockroaches", "~4,500", "positive", "phylopic/cockroach",
     "flat; shield pronotum;\nootheca"),
    ("Blattodea", "termites (soldier)", "~3,000", "positive", "phylopic/termite",
     "social castes; beaded antennae;\nequal, deciduous wings"),
]
NC, CW, CH = 5, 5.6, 5.4
NR = (len(CELLS) + NC - 1) // NC
W, H = NC * CW, NR * CH + 1.6
fig, ax = bio.canvas(W, H)
for i, (order, common, n, tok, icon, chars) in enumerate(CELLS):
    c, r = i % NC, i // NC
    x0, y0 = c * CW, H - 1.6 - (r + 1) * CH
    bio.label(ax, (x0 + CW / 2, y0 + CH - 0.35), order, size="normal", bold=True)
    bio.label(ax, (x0 + CW / 2, y0 + CH - 0.85), f"{common} ({n} spp.)", size="tiny", color=P.muted())
    iw, ih = icon_size(icon)
    w = min(CW - 1.2, 2.6 * iw / ih)
    bio.icon(ax, icon, at=(x0 + CW / 2, y0 + 2.75), width=w, color=tok)
    bio.label(ax, (x0 + CW / 2, y0 + 0.75), chars, size="tiny")
for k, (name, tok) in enumerate([("Apterygote insects", "bone"), ("Palaeoptera", "channel"), ("Polyneoptera", "positive")]):
    x = 1.0 + k * 7.5
    bio.box(ax, (x + 0.3, H - 0.8), 0.5, 0.5, token=tok)
    bio.label(ax, (x + 0.8, H - 0.8), name, size="small", ha="left")
bio.label(ax, (W - 0.3, H - 0.8), "Silhouettes not to scale", size="tiny", color=P.muted(), ha="right")
