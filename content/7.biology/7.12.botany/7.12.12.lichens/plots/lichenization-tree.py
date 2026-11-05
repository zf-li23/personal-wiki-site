"""Lichenization across the Ascomycota and Basidiomycota (cladogram; branch lengths have no meaning).
Class relationships simplified after Schoch et al. (2009); lichenized lineages after Lucking et al.
(2017). Star: (almost) all members lichenized; dot: a few lichenized lineages."""
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(17, 12)
nw = ("((Taphrinomycotina,Saccharomycotina,(Pezizomycetes,Orbiliomycetes,"
      "((Dothideomycetes,Arthoniomycetes)dm,(Sordariomycetes,Leotiomycetes)sm,Lecanoromycetes,"
      "Eurotiomycetes,Lichinomycetes)leo)pez)asc,(Pucciniomycotina,Ustilaginomycotina,Agaricomycetes)bas)r;")
text = {"Taphrinomycotina": "Taphrinomycotina", "Saccharomycotina": "Saccharomycotina (yeasts)",
        "Pezizomycetes": "Pezizomycetes (morels, truffles)", "Orbiliomycetes": "Orbiliomycetes",
        "Dothideomycetes": "Dothideomycetes", "Arthoniomycetes": "Arthoniomycetes",
        "Sordariomycetes": "Sordariomycetes", "Leotiomycetes": "Leotiomycetes",
        "Lecanoromycetes": "Lecanoromycetes (most lichens)", "Eurotiomycetes": "Eurotiomycetes (Verrucariales)",
        "Lichinomycetes": "Lichinomycetes", "Pucciniomycotina": "Pucciniomycotina (rusts)",
        "Ustilaginomycotina": "Ustilaginomycotina (smuts)", "Agaricomycetes": "Agaricomycetes (mushrooms and allies)"}
marks = ([dict(node=[n], kind="star", token="positive", at=0.6) for n in ["Lecanoromycetes", "Arthoniomycetes", "Lichinomycetes"]]
         + [dict(node=[n], kind="dot", token="positive", at=0.6) for n in ["Eurotiomycetes", "Dothideomycetes", "Agaricomycetes"]])
phylo.tree(ax, nw, origin=(0.8, 1.0), width=6.5, height=10.4, root_edge=0.3, tip_text=text, label_size="small",
           clades=[dict(node="asc", token="highlight", style="bar", label="Ascomycota"),
                   dict(node="bas", token="animal", style="bar", label="Basidiomycota")],
           marks=marks)
bio.label(ax, (0.8, 0.35), "star: (almost) all lichenized    dot: some lichenized lineages", size="tiny", ha="left",
          color=P.muted())
