# Asterids at order level (APG IV; Soltis et al. 2018); unresolved parts as polytomies. Numbered marks:
# 1 asterids (unitegmic tenuinucellate ovules, iridoids); 2 Ericales (stamens often twice the petals,
# reversal to bitegmic ovules in many); 3 euasterids (sympetaly, epipetalous stamens as many as the
# corolla lobes, two carpels); 4 lamiids; 5 campanulids. Chapters of the course on the right.
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(Cornales,(Ericales,(((Icacinales,(Metteniusales,(Garryales,(Boraginales,Gentianales,Vahliales,"
          "Solanales,Lamiales)))))Lamiids,(Aquifoliales,(Asterales,(Escalloniales,Bruniales,Paracryphiales,"
          "(Dipsacales,Apiales))))Campanulids)Euasterids)E)Asterids;")
fig, ax = bio.canvas(30, 16)
t = phylo.tree(ax, NEWICK, origin=(1.0, 0.8), width=12.0, height=14.0, label_size="small", root_edge=0.4,
               clades=[dict(tips=["Cornales"], token="plant", style=("bar",), label="7.12.46"),
                       dict(tips=["Ericales"], token="petal", style=("bar",), label="7.12.46"),
                       dict(node="Lamiids", token="dna", style=("bar", "branch"), label="Lamiids: 7.12.47, 7.12.48"),
                       dict(node="Campanulids", token="rna", style=("bar", "branch"), label="Campanulids: 7.12.49")],
               marks=[dict(node="Asterids", kind="star", at=0.5, token="highlight", text="1"),
                      dict(node="Ericales", kind="trait", at=0.5, token="petal", text="2"),
                      dict(node="Euasterids", kind="trait", at=0.5, token="highlight", text="3"),
                      dict(node="Lamiids", kind="trait", at=0.5, token="dna", text="4"),
                      dict(node="Campanulids", kind="trait", at=0.5, token="rna", text="5")])
KEY = ["1  Asterids: unitegmic, tenuinucellate ovules; iridoids",
       "2  Ericales: stamens often 2x petals; mostly bitegmic (reversal)",
       "3  Euasterids: sympetalous; stamens epipetalous, = corolla lobes",
       "4  Lamiids: leaves opposite, entire; early sympetaly; ovary superior",
       "5  Campanulids: leaves alternate, toothed; late sympetaly; ovary inferior"]
for i, k in enumerate(KEY):
    bio.label(ax, (19.0, 8.6 - i * 0.85), k, size="small", ha="left")
