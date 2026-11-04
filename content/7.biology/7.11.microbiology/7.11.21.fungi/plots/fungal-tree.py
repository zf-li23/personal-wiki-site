"""The main lineages of fungi with a representative genus each (cladogram after the phylum-level
classifications of Spatafora et al. 2016 and James et al. 2020; the position of the Opisthosporidia, here
Cryptomycota and Microsporidia, is still debated), animals as the outgroup, and four characters: a flagellated
stage, the vegetative body, the dikaryon and the sexual spore."""
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(25, 12.5)
NW = ("(Homo,((Rozella,Encephalitozoon)Opisthosporidia,(Batrachochytrium,(Allomyces,(Entomophthora,"
      "((Rhizopus,Rhizophagus)Mucoromycota,((Saccharomyces,(Aspergillus,Neurospora))Ascomycota,"
      "(Agaricus,Puccinia)Basidiomycota)Dikarya))))));")
icons = {"Homo": "phylopic/human", "Encephalitozoon": "phylopic/microsporidian", "Allomyces": "phylopic/allomyces",
         "Rhizopus": "phylopic/rhizopus", "Rhizophagus": "phylopic/rhizophagus", "Saccharomyces": "phylopic/yeast",
         "Aspergillus": "phylopic/aspergillus", "Neurospora": "phylopic/neurospora", "Agaricus": "phylopic/agaricus",
         "Puccinia": "phylopic/rust"}
phyla = {"Homo": "(animals)", "Rozella": "Cryptomycota", "Encephalitozoon": "Microsporidia",
         "Batrachochytrium": "Chytridiomycota", "Allomyces": "Blastocladiomycota", "Entomophthora": "Zoopagomycota",
         "Rhizopus": "Mucoromycota", "Rhizophagus": "Mucoromycota (Glomeromycotina)", "Saccharomyces": "Ascomycota",
         "Aspergillus": "Ascomycota", "Neurospora": "Ascomycota", "Agaricus": "Basidiomycota", "Puccinia": "Basidiomycota"}
t = phylo.tree(ax, NW, origin=(0.6, 1.2), width=5.6, height=10.0, label_size="small", italic=True,
               icons=icons, icon_size=0.6, icon_color="neutral",
               clades=[dict(node="Dikarya", token="rna", style="branch"),
                       dict(node="Mucoromycota", token="positive", style="branch"),
                       dict(node="Opisthosporidia", token="neutral", style="branch")],
               marks=[dict(node="Dikarya", kind="trait", text="dikaryon, septate hyphae", at=0.5)])
cols = [14.2, 16.8, 19.6, 22.6]
heads = ["phylum", "flagellum", "vegetative body", "sexual spore"]
bio.label(ax, (cols[0] - 2.0, 11.9), heads[0], size="small", bold=True, ha="left")
for c, h in zip(cols[1:], heads[1:]):
    bio.label(ax, (c, 11.9), h, size="small", bold=True)
flag = {"Homo": "sperm", "Rozella": "zoospore", "Batrachochytrium": "zoospore", "Allomyces": "zoospore"}
body = {"Homo": "", "Rozella": "intracellular", "Encephalitozoon": "intracellular", "Batrachochytrium": "thallus, rhizoids",
        "Allomyces": "branched thallus", "Entomophthora": "hyphae", "Rhizopus": "coenocytic hyphae",
        "Rhizophagus": "coenocytic hyphae", "Saccharomyces": "yeast", "Aspergillus": "septate hyphae",
        "Neurospora": "septate hyphae", "Agaricus": "septate hyphae", "Puccinia": "septate hyphae"}
spore = {"Rhizopus": "zygospore", "Entomophthora": "zygospore", "Rhizophagus": "(none known)",
         "Saccharomyces": "ascospore", "Aspergillus": "ascospore", "Neurospora": "ascospore",
         "Agaricus": "basidiospore", "Puccinia": "basidiospore", "Allomyces": "(zygote)", "Batrachochytrium": "(not observed)"}
for tip in t.root.leaves():
    y = tip.xy[1]
    bio.label(ax, (cols[0] - 2.0, y), phyla[tip.name], size="tiny", ha="left")
    if tip.name in flag:
        ax.plot([cols[1]], [y], "o", ms=8, color=P.edge("highlight"), zorder=12)
        bio.label(ax, (cols[1] + 0.3, y), flag[tip.name], size="tiny", ha="left")
    else:
        ax.plot([cols[1]], [y], "o", ms=8, color=P.edge("highlight"), markerfacecolor="none", mew=1.3, zorder=12)
    bio.label(ax, (cols[2], y), body.get(tip.name, ""), size="tiny")
    s = spore.get(tip.name, "")
    bio.label(ax, (cols[3], y), s, size="tiny", color=P.muted() if s.startswith("(") else P.ink())
bio.label(ax, (0.6, 0.4), "Opisthosporidia: Cryptomycota and Microsporidia (with Aphelida, not shown); position debated",
          size="tiny", ha="left", color=P.muted())
