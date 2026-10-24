# Two signalling cascades drawn by network.cascade: a receptor tyrosine kinase pathway (EGF -> ERK -> ELK1)
# and a G-protein-coupled receptor pathway (glucagon -> cAMP -> PKA -> CREB) in a hepatocyte.
import wikibio as bio
from wikibio import network

fig, ax = bio.canvas(19, 15.5, scale=0.42)

bio.panel(ax, "A", (0.0, 15.5))
network.cascade(ax, (0.4, 0.2, 9.2, 15.0), ligand="EGF", receptor="EGFR", chain=("GRB2", "SOS", "RAS", "RAF", "MEK", "ERK"),
                tf="ELK1", gene="FOS", phenotype="Proliferation",
                states={"RAS": ["GTP"], "RAF": ["P"], "MEK": ["P", "P"], "ERK": ["P", "P"]})

bio.panel(ax, "B", (9.6, 15.5))
network.cascade(ax, (10.0, 0.2, 18.8, 15.0), ligand="Glucagon", receptor="GCGR", receptor_dimer=False,
                chain=("Gαs", "AC", {"text": "cAMP", "kind": "chemical", "token": "atp"}, "PKA"),
                tf="CREB", gene="PCK1", phenotype="Gluconeogenesis",
                states={"GCGR": [], "Gαs": ["GTP"], "CREB": ["P"]})
