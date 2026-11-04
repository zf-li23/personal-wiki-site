"""Major lineages of Bacteria (cladogram, schematic; branch lengths have no meaning, and relationships
that are not well resolved are drawn as polytomies). Genome trees group most phyla into two large clades,
the Terrabacteria (mostly monoderm, gram-positive or wall-less, and the cyanobacteria) and the
Gracilicutes (diderm, gram-negative), which contain the FCB group (Fibrobacterota, Chlorobiota,
Bacteroidota) and the PVC group (Planctomycetota, Verrucomicrobiota, Chlamydiota). The candidate phyla
radiation (Patescibacteria) is placed with the Terrabacteria in recent rooted analyses. The positions of
Aquificota, Thermotogota and Fusobacteriota, once thought to branch first, are uncertain."""
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(19, 13)
nw = ("(((Bacillota,Actinomycetota,Cyanobacteriota,Chloroflexota,Deinococcota,Patescibacteria)terra,"
      "((Bacteroidota,Chlorobiota,Fibrobacterota)fcb,(Planctomycetota,Verrucomicrobiota,Chlamydiota)pvc,"
      "Pseudomonadota,Delta,Campylobacterota,Spirochaetota,Acidobacteriota,Nitrospirota)grac)tg,"
      "Aquificota,Thermotogota,Fusobacteriota)r;")
text = {
    "Bacillota": "Bacillota (low G+C gram-positive; incl. mycoplasmas)",
    "Actinomycetota": "Actinomycetota (high G+C gram-positive)",
    "Cyanobacteriota": "Cyanobacteriota (oxygenic phototrophs)",
    "Chloroflexota": "Chloroflexota",
    "Deinococcota": "Deinococcota (Deinococcus, Thermus)",
    "Patescibacteria": "Patescibacteria (candidate phyla radiation)",
    "Bacteroidota": "Bacteroidota",
    "Chlorobiota": "Chlorobiota (green sulfur bacteria)",
    "Fibrobacterota": "Fibrobacterota",
    "Planctomycetota": "Planctomycetota",
    "Verrucomicrobiota": "Verrucomicrobiota",
    "Chlamydiota": "Chlamydiota",
    "Pseudomonadota": "Pseudomonadota",
    "Delta": "Thermodesulfobacteriota, Myxococcota, Bdellovibrionota",
    "Campylobacterota": "Campylobacterota",
    "Spirochaetota": "Spirochaetota",
    "Acidobacteriota": "Acidobacteriota",
    "Nitrospirota": "Nitrospirota",
    "Aquificota": "Aquificota",
    "Thermotogota": "Thermotogota",
    "Fusobacteriota": "Fusobacteriota",
}
t = phylo.tree(ax, nw, origin=(1.2, 0.7), width=6.4, height=11.6, root_edge=0.4, tip_text=text,
               label_size="small",
               clades=[dict(node="terra", token="gram_pos", style="branch"),
                       dict(node="grac", token="gram_neg", style="branch"),
                       dict(tips=["Patescibacteria"], token="highlight", style="branch")])
for node, lab, tok, dy in [("terra", "Terrabacteria", "gram_pos", 0.45), ("grac", "Gracilicutes", "gram_neg", 0.45),
                           ("fcb", "FCB", "gram_neg", 0.4), ("pvc", "PVC", "gram_neg", 0.4)]:
    x, y = t.node(node).xy
    bio.label(ax, (x - 0.1, y + dy), lab, size="tiny", ha="right", color=P.edge(tok), bold=True)
bio.label(ax, (10.3, 1.9), "polytomies: branching order unresolved", size="tiny",
          ha="left", color=P.muted())
