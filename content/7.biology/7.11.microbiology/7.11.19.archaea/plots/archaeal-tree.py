"""Major lineages of Archaea (cladogram, schematic; branch lengths have no meaning, the position of the
root is debated and unresolved relationships are drawn as polytomies). Root drawn between the DPANN
archaea and all others. The former Euryarchaeota comprise the GTDB phyla Methanobacteriota, Halobacteriota
and Thermoplasmatota and smaller lineages; the TACK superphylum is the GTDB phylum Thermoproteota, which
includes the former Crenarchaeota, Thaumarchaeota (Nitrososphaerota), Korarchaeota and Bathyarchaeia;
eukaryotes branch within or beside the Asgard archaea."""
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(20, 11)
nw = ("(DPANN,((Methanobacteriota,Halobacteriota,Thermoplasmatota)eury,"
      "((Crenarchaea,Nitrososphaeria,Korarchaeia,Bathyarchaeia)tack,(Asgard,Eukaryotes)asg)ta)na)r;")
text = {
    "DPANN": "DPANN (Nanoarchaeota and others; small symbionts)",
    "Methanobacteriota": "Methanobacteriota (methanogens, Thermococci)",
    "Halobacteriota": "Halobacteriota (haloarchaea, methanogens, Archaeoglobi, ANME)",
    "Thermoplasmatota": "Thermoplasmatota (Thermoplasma, marine group II)",
    "Crenarchaea": "Thermoprotei (Sulfolobus, Pyrodictium)",
    "Nitrososphaeria": "Nitrososphaeria (ammonia oxidizers)",
    "Korarchaeia": "Korarchaeia",
    "Bathyarchaeia": "Bathyarchaeia",
    "Asgard": "Asgard archaea",
    "Eukaryotes": "eukaryotes",
}
t = phylo.tree(ax, nw, origin=(1.4, 0.8), width=5.4, height=9.4, root_edge=0.4, tip_text=text, label_size="small",
               clades=[dict(tips=["DPANN"], token="highlight", style="branch"),
                       dict(node="eury", token="rna", style="branch"),
                       dict(node="tack", token="enzyme", style="branch"),
                       dict(tips=["Asgard"], token="protein", style="branch"),
                       dict(tips=["Eukaryotes"], token="dna", style="branch")])
for node, lab, tok in [("eury", "former Euryarchaeota", "rna"), ("tack", "TACK (Thermoproteota)", "enzyme")]:
    x, y = t.node(node).xy
    bio.label(ax, (x - 0.2, y + 0.42), lab, size="tiny", ha="right", color=P.edge(tok), bold=True)
bio.label(ax, (1.0, 10.6), "root position debated", size="tiny", ha="left", color=P.muted())
