# Where the molecular parts of the nervous system arose on the tree of life (cladogram).
# Topology: ctenophores as sister to all other animals (Schultz et al. 2023); placozoans sister to
# cnidarians + bilaterians. Gains follow comparative genomics (Liebeskind, Hillis and Zakon 2011;
# Srivastava et al. 2010; Moran et al. 2015); a crossed bar is a loss.
# Stars mark neurons: either one origin before the ctenophore split with losses in sponges and
# placozoans, or two independent origins (ctenophores and cnidarians + bilaterians).
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(Bacteria,(Fungi,(Choanoflagellata,(Ctenophora,(Porifera,(Placozoa,(Cnidaria,"
          "((Nematoda,Arthropoda)Protostomia,Vertebrata)Bilateria)Planulozoa)ParaHoxozoa)Myriazoa)Metazoa)"
          "Choanozoa)Eukaryota)Root;")

TEXT = {"Bacteria": "Bacteria", "Fungi": "Fungi (yeast)", "Choanoflagellata": "Choanoflagellates",
        "Ctenophora": "Ctenophores", "Porifera": "Sponges", "Placozoa": "Placozoans", "Cnidaria": "Cnidarians",
        "Nematoda": "Nematodes", "Arthropoda": "Arthropods", "Vertebrata": "Vertebrates"}

ICONS = {
    "Bacteria": "phylopic/e-coli", "Fungi": "phylopic/yeast", "Choanoflagellata": "phylopic/choanoflagellate",
    "Ctenophora": "phylopic/comb-jelly", "Porifera": "phylopic/sponge", "Placozoa": "phylopic/placozoan",
    "Cnidaria": "phylopic/jellyfish", "Nematoda": ("phylopic/c-elegans", {"rotate": 90}),
    "Arthropoda": "phylopic/drosophila", "Vertebrata": "phylopic/zebrafish",
}

GAINS = [
    ("Root", "trait", "K+ channels (2TM and voltage-gated 6TM)"),
    ("Eukaryota", "trait", "24TM CaV channels, GPCRs, SNAREs, calmodulin"),
    ("Choanozoa", "trait", "NaV-like channel (Na+/Ca2+), PSD-95, Homer, Shank, cadherins"),
    ("Metazoa", "trait", "Ancestral iGluR; mGluR; most postsynaptic scaffolds"),
    ("Planulozoa", "trait", "Neurexin-neuroligin, ephrin-Eph pair, AMPA/NMDA-type iGluRs"),
    ("Cnidaria", "trait", "Na+-selective NaV (independent origin)"),
    ("Bilateria", "trait", "Na+-selective NaV (DEKA filter); centralized CNS (?)"),
    ("Vertebrata", "trait", "Connexins, myelin (jawed), four cone opsin classes"),
    ("Nematoda", "loss", "Loss of NaV channels (nematodes)"),
]
MARKS = [dict(node=n, kind=k, text=str(i + 1), at=0.5, text_size="tiny", side=-1, offset=0.3, va="bottom")
         for i, (n, k, _) in enumerate(GAINS)]
MARKS += [dict(node=n, kind="star", at=0.82, size=0.24) for n in ("Ctenophora", "Planulozoa")]

fig, ax = bio.canvas(17.0, 9.0)
t = phylo.tree(ax, NEWICK, origin=(0.8, 2.6), width=10.0, height=6.2, direction="right", root_edge=0.4,
               tip_text=TEXT, icons=ICONS, icon_size=0.55, icon_width=1.0, label_size="small",
               clades=[dict(node="Metazoa", token="neuron", style="band", label="Animals")],
               marks=MARKS)

for name, text in (("Eukaryota", "Eukaryotes"), ("Choanozoa", "Choanozoa"), ("Metazoa", "Metazoa"),
                   ("Planulozoa", "Planulozoa"), ("Bilateria", "Bilateria")):
    nd = t.node(name)
    bio.label(ax, (nd.xy[0] - 0.06, nd.xy[1] - 0.3), text, size="tiny", bold=True, ha="right", va="top",
              color=P.muted())

x0, y0 = 0.8, 1.9
bio.label(ax, (x0, y0 + 0.4), "Gains (bars) and losses (crossed bar)", size="small", bold=True, ha="left")
for k, (_, kind, text) in enumerate(GAINS):
    col, row = divmod(k, 5)
    xx, yy = x0 + col * 8.2, y0 - row * 0.42
    phylo.marker(ax, (xx + 0.12, yy), kind, size=0.14, direction=(1, 0))
    bio.label(ax, (xx + 0.35, yy), f"{k + 1}  {text}", size="tiny", ha="left")
xx, yy = x0 + 8.2, y0 - 4 * 0.42
phylo.marker(ax, (xx + 0.12, yy), "star", size=0.18, direction=(1, 0))
bio.label(ax, (xx + 0.35, yy), "Neurons: one origin with losses, or two origins?", size="tiny", ha="left")
