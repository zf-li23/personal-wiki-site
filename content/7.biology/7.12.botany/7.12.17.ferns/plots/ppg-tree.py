"""Fern phylogeny after PPG I (2016), simplified cladogram (branch lengths not to scale). Lycophytes are
the outgroup; seed plants are the sister group of ferns. Numbered marks: 1 megaphylls and multiflagellate
sperm (euphyllophytes); 2 leptosporangia; 3 heterospory and sporocarps (Salviniales); 4 vertical annulus
interrupted by the stalk (Polypodiales); 5 Cretaceous and later radiation (eupolypods). Numbers at the tips
are the PPG I species counts."""
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(Lycophytes,(Seed_plants,(Equisetales,((Psilotales,Ophioglossales)Ophioglossidae,(Marattiales,"
          "(Osmundales,((Hymenophyllales,Gleicheniales),(Schizaeales,(Salviniales,(Cyatheales,Polypodiales)Core)Sal)Sch)Rest)"
          "Polypodiidae)MP)Op)Ferns)Euphyllophytes)Vascular;")
COUNTS = {"Lycophytes": "1338 (outgroup)", "Seed plants": "c. 370 000", "Equisetales": "15", "Psilotales": "17",
          "Ophioglossales": "112", "Marattiales": "111", "Osmundales": "18", "Hymenophyllales": "434",
          "Gleicheniales": "172", "Schizaeales": "190", "Salviniales": "82", "Cyatheales": "707", "Polypodiales": "8714"}

fig, ax = bio.canvas(25, 15)
t = phylo.tree(ax, NEWICK, origin=(1.0, 1.0), width=10.5, height=12.6, direction="right", root_edge=0.3,
               label_size="small",
               icons={"Lycophytes": "phylopic/clubmoss", "Equisetales": "phylopic/horsetail", "Psilotales": "phylopic/psilotum",
                      "Polypodiales": "phylopic/fern"},
               icon_size=0.75, icon_color="plant",
               clades=[dict(node="Ferns", token="plant", style="bar", label="Ferns (Polypodiopsida)"),
                       dict(tips=["Equisetales"], token="bract", style="band", label="Equisetidae"),
                       dict(node="Ophioglossidae", token="ovule", style="band", label="Ophioglossidae"),
                       dict(tips=["Marattiales"], token="petal", style="band", label="Marattiidae"),
                       dict(node="Polypodiidae", token="dna", style="band", label="Polypodiidae")],
               marks=[dict(node="Euphyllophytes", kind="trait", text="1", at=0.5, text_size="tiny"),
                      dict(node="Polypodiidae", kind="trait", text="2", at=0.5, text_size="tiny"),
                      dict(node="Salviniales", kind="trait", text="3", at=0.5, text_size="tiny"),
                      dict(node="Polypodiales", kind="trait", text="4", at=0.35, text_size="tiny"),
                      dict(node="Polypodiales", kind="star", text="5", at=0.75, text_size="tiny")])
for tip in t.tips():
    bio.label(ax, (20.0, tip.xy[1]), COUNTS[tip.name], size="small", ha="left", color=P.muted())
bio.label(ax, (20.0, 14.3), "Species", size="small", bold=True, ha="left")
