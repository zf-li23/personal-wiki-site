"""The former Proteobacteria in the current classification (cladogram, schematic; branch lengths
carry no meaning, and unresolved relationships are drawn as a polytomy).
The phylum Pseudomonadota now contains the Alphaproteobacteria and the Gammaproteobacteria; in the
Genome Taxonomy Database the former Betaproteobacteria are the order Burkholderiales within the
Gammaproteobacteria. The former Deltaproteobacteria were divided among several phyla (the largest are
the Thermodesulfobacteriota, GTDB name Desulfobacterota, the Myxococcota and the Bdellovibrionota) and the
former Epsilonproteobacteria became the Campylobacterota. Their positions relative to each other and to
the other phyla are not well resolved."""
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(22, 10.5)
nw = ("((Alphaproteobacteria,(Gammaproteobacteria,Burkholderiales)gam)pse,"
      "Thermodesulfobacteriota,Myxococcota,Bdellovibrionota,Campylobacterota,Other_bacterial_phyla)r;")
text = {
    "Alphaproteobacteria": "Alphaproteobacteria",
    "Gammaproteobacteria": "Gammaproteobacteria",
    "Burkholderiales": "Burkholderiales",
    "Thermodesulfobacteriota": "Thermodesulfobacteriota (Desulfobacterota)",
    "Myxococcota": "Myxococcota",
    "Bdellovibrionota": "Bdellovibrionota",
    "Campylobacterota": "Campylobacterota",
    "Other_bacterial_phyla": "other bacterial phyla",
}
t = phylo.tree(ax, nw, origin=(1.0, 0.9), width=5.2, height=8.6, root_edge=0.4, tip_text=text,
               label_size="normal",
               clades=[dict(node="pse", token="positive", style="branch"),
                       dict(tips=["Thermodesulfobacteriota"], token="rna", style="branch"),
                       dict(tips=["Myxococcota"], token="rna", style="branch"),
                       dict(tips=["Bdellovibrionota"], token="rna", style="branch"),
                       dict(tips=["Campylobacterota"], token="dna", style="branch")])
former = {
    "Alphaproteobacteria": ("class Alphaproteobacteria", "positive"),
    "Gammaproteobacteria": ("class Gammaproteobacteria", "positive"),
    "Burkholderiales": ("class Betaproteobacteria", "positive"),
    "Thermodesulfobacteriota": ("class Deltaproteobacteria", "rna"),
    "Myxococcota": ("class Deltaproteobacteria", "rna"),
    "Bdellovibrionota": ("class Deltaproteobacteria", "rna"),
    "Campylobacterota": ("class Epsilonproteobacteria", "dna"),
}
xcol = 14.6
bio.label(ax, (xcol, 10.15), "before 2017-2020: phylum Proteobacteria", size="small", ha="left", color=P.muted())
for name, (old, tok) in former.items():
    x, y = t.node(name).xy
    bio.box(ax, (xcol + 3.2, y), 6.2, 0.62, token=tok, text=old, size="small")
    ax.plot([x + (7.6 if name == "Thermodesulfobacteriota" else 5.0), xcol - 0.15], [y, y], color=P.muted(), lw=0.6, ls=(0, (1.5, 2.5)), zorder=3)
xp, yp = t.node("pse").xy
bio.label(ax, (xp - 0.15, yp + 0.45), "Pseudomonadota", size="small", ha="right", color=P.edge("positive"), bold=True)
xb, yb = t.node("Burkholderiales").xy
bio.label(ax, (xb + 0.25, yb - 0.5), "(in GTDB an order of the Gammaproteobacteria)", size="tiny", ha="left",
          color=P.muted())
