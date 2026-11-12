"""Two hypotheses for the root of the animal tree and what each implies for the evolution of neurons and
muscle cells (cladograms of the five non-bilaterian lineages plus Bilateria).

A, ctenophores first (Ctenophora-sister): supported by many phylogenomic analyses and, decisively for many
authors, by the pattern of chromosome-scale gene linkage (synteny) shared by sponges, cnidarians, placozoans
and bilaterians but not by ctenophores and choanoflagellates (Schultz et al. 2023). Either nervous systems
and muscles evolved twice (in ctenophores and in ParaHoxozoa; bars) or they evolved once and were lost
in sponges and placozoans (crosses). B, sponges first (Porifera-sister): favored by analyses with
site-heterogeneous models and amino-acid recoding (e.g. Pisani et al. 2015; Simion et al. 2017); a single
origin of neurons and muscles in the common ancestor of ctenophores and ParaHoxozoa (Eumetazoa) and one
loss in placozoans suffice.
"""

import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(22.0, 9.4)
A = "((Ctenophora,(Porifera,(Placozoa,(Cnidaria,Bilateria)Planulozoa)ParaHoxozoa)Myriazoa)Metazoa,Choanoflagellata);"
B = "((Porifera,(Ctenophora,(Placozoa,(Cnidaria,Bilateria)Planulozoa)ParaHoxozoa)Eumetazoa)Metazoa,Choanoflagellata);"
ICON = {"Ctenophora": "phylopic/comb-jelly", "Porifera": "phylopic/sponge", "Placozoa": "phylopic/placozoan",
        "Cnidaria": "phylopic/jellyfish", "Bilateria": "phylopic/drosophila", "Choanoflagellata": "phylopic/choanoflagellate"}
TEXT = {"Choanoflagellata": "Choanoflagellates"}
ma = [dict(node="Ctenophora", kind="trait", text="neurons, muscles", at=0.5, text_size="tiny", side=1, offset=0.25),
      dict(node="ParaHoxozoa", kind="trait", text="neurons, muscles", at=0.5, text_size="tiny", side=1, offset=0.25)]
mb = [dict(node="Eumetazoa", kind="trait", text="neurons, muscles", at=0.5, text_size="tiny", side=1, offset=0.25),
      dict(node="Placozoa", kind="loss", text="lost", at=0.5, text_size="tiny", side=1, offset=0.25)]
ta = phylo.tree(ax, A, origin=(0.8, 1.6), width=5.6, height=5.8, tip_text=TEXT, icons=ICON, icon_size=0.55,
                icon_width=0.9, marks=ma, label_size="small")
tb = phylo.tree(ax, B, origin=(12.0, 1.6), width=5.6, height=5.8, tip_text=TEXT, icons=ICON, icon_size=0.55,
                icon_width=0.9, marks=mb, label_size="small")
for nd, tree in (("Porifera", ta), ("Placozoa", ta)):
    phylo.marker(ax, (tree.node(nd).xy[0] - 0.9, tree.node(nd).xy[1]), "loss", size=0.16)
bio.panel(ax, "A", (0.3, 8.9))
bio.label(ax, (5.2, 8.9), "Ctenophores first", size="small", bold=True)
bio.label(ax, (5.2, 0.7), "two gains (bars), or one gain and two losses (crosses)", size="tiny", color=P.muted())
bio.panel(ax, "B", (11.5, 8.9))
bio.label(ax, (16.4, 8.9), "Sponges first", size="small", bold=True)
bio.label(ax, (16.4, 0.7), "one gain, one loss (placozoans)", size="tiny", color=P.muted())
