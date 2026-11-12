# Phylogeny of the living molluscan classes (simplified; after Kocot et al. 2011, 2020; Giribet and
# Edgecombe 2020), with selected synapomorphies as numbered bars and approximate numbers of living species.
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(((Solenogastres,Caudofoveata)Aplacophora,Polyplacophora)Aculifera,"
          "((Monoplacophora,Cephalopoda)MonCeph,(Scaphopoda,(Gastropoda,Bivalvia))GSB)Conchifera)Mollusca;")
TEXT = {"Solenogastres": "Solenogastres (~300)", "Caudofoveata": "Caudofoveata (~150)",
        "Polyplacophora": "Polyplacophora (~1,000)", "Monoplacophora": "Monoplacophora (~35)",
        "Cephalopoda": "Cephalopoda (~800)", "Scaphopoda": "Scaphopoda (~600)",
        "Gastropoda": "Gastropoda (~55,000)", "Bivalvia": "Bivalvia (~9,000)"}
ICONS = {"Solenogastres": "phylopic/solenogaster", "Caudofoveata": "phylopic/caudofoveate",
         "Polyplacophora": "phylopic/chiton2", "Monoplacophora": "phylopic/monoplacophoran",
         "Cephalopoda": "phylopic/nautilus", "Scaphopoda": "phylopic/tusk-shell",
         "Gastropoda": "phylopic/snail", "Bivalvia": "phylopic/bivalve"}
CHARS = [("Mollusca", "Mantle, radula, foot, ctenidia; coelom reduced"),
         ("Aculifera", "Calcareous sclerites in the mantle cuticle"),
         ("Aplacophora", "Worm-like body; foot reduced or lost"),
         ("Polyplacophora", "Eight shell plates; girdle; aesthetes"),
         ("Conchifera", "Single shell gland; larval shell; 3-layered shell; statocysts"),
         ("Cephalopoda", "Chambered shell; closed circulation; arms and funnel"),
         ("Monoplacophora", "Serially repeated gills, nephridia, muscles"),
         ("Gastropoda", "Torsion; operculum"),
         ("Bivalvia", "Two valves; adductors; radula lost"),
         ("Scaphopoda", "Tubular shell open at both ends; captacula")]
MARKS = [dict(node=n, kind="trait", text=str(k + 1), at=0.5, text_size="tiny", side=-1, offset=0.3, va="bottom")
         for k, (n, _) in enumerate(CHARS)]
MARKS += [dict(node=n, kind="dot", token="neutral", at=1.0, size=0.3) for n in ("MonCeph", "GSB")]

fig, ax = bio.canvas(21.0, 13.2)
phylo.tree(ax, NEWICK, origin=(0.8, 5.2), width=9.0, height=7.4, root_edge=0.8, tip_text=TEXT, icons=ICONS,
           icon_size=0.7, icon_width=1.2, label_size="small",
           clades=[dict(node="Aculifera", token="dna", style="bar", label="Aculifera"),
                   dict(node="Conchifera", token="bone", style="bar", label="Conchifera")],
           marks=MARKS)
y = 4.4
for k, (_, txt) in enumerate(CHARS):
    col, row = divmod(k, 5)
    x0, yy = 1.0 + col * 10.0, y - row * 0.62
    phylo.marker(ax, (x0, yy), "trait", direction=(1, 0))
    bio.label(ax, (x0 + 0.35, yy), f"{k + 1}  {txt}", size="small", ha="left")
phylo.marker(ax, (1.0, 0.9), "dot", token="neutral", size=0.3)
bio.label(ax, (1.4, 0.9), "Node supported by some phylogenomic analyses but not all", size="small", ha="left")
