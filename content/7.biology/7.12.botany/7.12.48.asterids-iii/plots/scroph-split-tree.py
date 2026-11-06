# The break-up of Scrophulariaceae s.l. Family-level tree of Lamiales (APG IV; Refulio-Rodriguez & Olmstead
# 2014, simplified; unresolved parts drawn as polytomies). Families that received genera of the traditional
# Scrophulariaceae are coloured, and example genera are listed after the family name; they are scattered
# over several branches of the order.
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(Plocospermataceae,((Carlemanniaceae,Oleaceae),(Tetrachondraceae,((Calceolariaceae,Gesneriaceae),"
          "(Plantaginaceae,(Scrophulariaceae,(Stilbaceae,Linderniaceae,Byblidaceae,"
          "(Acanthaceae,Martyniaceae,Pedaliaceae),Bignoniaceae,Lentibulariaceae,Verbenaceae,"
          "(Lamiaceae,(Mazaceae,(Phrymaceae,(Paulowniaceae,Orobanchaceae)))))HCL))))))Lamiales;")
EX = {"Calceolariaceae": r"Calceolariaceae: $\it{Calceolaria}$",
      "Plantaginaceae": r"Plantaginaceae: $\it{Veronica}$, $\it{Digitalis}$, $\it{Antirrhinum}$, $\it{Linaria}$",
      "Scrophulariaceae": r"Scrophulariaceae s.s.: $\it{Scrophularia}$, $\it{Verbascum}$ (+ $\it{Buddleja}$)",
      "Linderniaceae": r"Linderniaceae: $\it{Lindernia}$, $\it{Torenia}$",
      "Mazaceae": r"Mazaceae: $\it{Mazus}$",
      "Phrymaceae": r"Phrymaceae: $\it{Mimulus}$ (+ $\it{Phryma}$)",
      "Paulowniaceae": r"Paulowniaceae: $\it{Paulownia}$",
      "Orobanchaceae": r"Orobanchaceae: $\it{Rehmannia}$, $\it{Pedicularis}$, $\it{Siphonostegia}$"}
fig, ax = bio.canvas(34, 16)
phylo.tree(ax, NEWICK, origin=(1.0, 0.6), width=10.5, height=14.8, label_size="small", root_edge=0.4,
           tip_text=EX,
           clades=[dict(tips=[k], token="rna", style=("branch",), label="") for k in EX] +
                  [dict(node="HCL", token="plant", style=("bar",), label="higher core Lamiales")])
bio.label(ax, (27.5, 2.2), "Coloured: families that received genera\nof traditional Scrophulariaceae", size="small", ha="left")
