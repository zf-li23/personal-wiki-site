"""Phylogeny of the fungi and the fungus-like organisms of traditional botany (cladogram; branch lengths
have no meaning). Fungal phyla after Spatafora et al. (2016) and James et al. (2020); eukaryote
supergroups after Adl et al. (2019). Square brackets: the group in the Ainsworth (1973) system."""
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(23, 15.5)
nw = ("(((Oomycota,Plasmodiophorids)sar,"
      "((Myxogastria,Dictyostelia)amoeb,"
      "((Animals,Choanoflagellates)hol,"
      "((Cryptomycota,Microsporidia)opi,(Chytridiomycota,(Blastocladiomycota,"
      "((Zoopagomycota,Mucoromycota)zm,(Ascomycota,Basidiomycota)dik)ter)b)c)fun)op)amor)euk)r;")
text = {
    "Oomycota": "Oomycota: water molds, Phytophthora   [Mastigomycotina]",
    "Plasmodiophorids": "Plasmodiophorids: clubroot   [Myxomycota]",
    "Myxogastria": "Myxogastria: plasmodial slime molds   [Myxomycota]",
    "Dictyostelia": "Dictyostelia: cellular slime molds   [Myxomycota]",
    "Animals": "Animals",
    "Choanoflagellates": "Choanoflagellates",
    "Cryptomycota": "Cryptomycota (Rozella)   [Mastigomycotina]",
    "Microsporidia": "Microsporidia   [Protozoa]",
    "Chytridiomycota": "Chytridiomycota: chytrids   [Mastigomycotina]",
    "Blastocladiomycota": "Blastocladiomycota: Allomyces   [Mastigomycotina]",
    "Zoopagomycota": "Zoopagomycota: Entomophthora   [Zygomycotina]",
    "Mucoromycota": "Mucoromycota: Rhizopus, Glomeromycotina   [Zygomycotina]",
    "Ascomycota": "Ascomycota   [Ascomycotina; most Deuteromycotina]",
    "Basidiomycota": "Basidiomycota   [Basidiomycotina; some Deuteromycotina]",
}
icons = {
    "Oomycota": "phylopic/phytophthora",
    "Myxogastria": "phylopic/physarum",
    "Dictyostelia": "phylopic/dictyostelium",
    "Animals": "phylopic/drosophila",
    "Choanoflagellates": "phylopic/choanoflagellate",
    "Microsporidia": "phylopic/microsporidian",
    "Blastocladiomycota": "phylopic/allomyces",
    "Mucoromycota": "phylopic/rhizopus",
    "Ascomycota": "phylopic/penicillium",
    "Basidiomycota": "phylopic/agaricus",
}
t = phylo.tree(ax, nw, origin=(1.0, 0.7), width=7.0, height=13.4, root_edge=0.4, tip_text=text,
               label_size="small", icons=icons, icon_size=0.6, icon_color="animal",
               clades=[dict(node="sar", token="plant", style="bar", label="SAR"),
                       dict(node="amoeb", token="animal", style="bar", label="Amoebozoa"),
                       dict(node="fun", token="highlight", style=["branch", "bar"], label="Fungi"),
                       dict(node="dik", token="positive", style="bar", label="Dikarya")])
bio.label(ax, (1.0, 0.2), "[ ]: position in the Ainsworth (1973) system", size="tiny", ha="left",
          color=P.muted())
