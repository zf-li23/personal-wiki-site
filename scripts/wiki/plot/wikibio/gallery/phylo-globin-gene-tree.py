# A gene tree of vertebrate globins (a phylogram): two gene duplications (squares) give myoglobin and the
# alpha and beta haemoglobin families; speciation nodes (circles) repeat the species tree in each family.
# Topology follows Hoffmann et al. 2012 (Mol. Biol. Evol. 29:303); branch lengths and bootstrap values
# are illustrative.
import wikibio as bio
from wikibio import phylo

NEWICK = ("(((MB_human:0.12,MB_mouse:0.14)98:0.08,MB_chicken:0.24)99:0.40,"
          "((((HBA_human:0.08,HBA_mouse:0.10)100:0.09,HBA_chicken:0.20)97:0.10,HBA_zebrafish:0.36)88:0.30,"
          "(((HBB_human:0.07,HBB_mouse:0.12)100:0.10,HBB_chicken:0.19)95:0.12,HBB_zebrafish:0.40)91:0.28)82:0.15);")

TEXT = {}
for gene, name in (("MB", "Myoglobin"), ("HBA", "Hemoglobin α"), ("HBB", "Hemoglobin β")):
    for sp in ("human", "mouse", "chicken", "zebrafish"):
        TEXT[f"{gene} {sp}"] = f"{name}, {sp}"

fig, ax = bio.canvas(16, 9.4)
t = phylo.tree(ax, NEWICK, origin=(0.8, 1.4), width=8.6, height=7.2, scaled=True, root_edge=0.06, tip_text=TEXT,
               support="label", support_min=70, align=True,
               clades=[dict(tips=["MB human", "MB chicken"], token="enzyme", style=("branch", "bar"), label="Myoglobin"),
                       dict(tips=["HBA human", "HBA zebrafish"], token="blood", style=("branch", "bar"), label="α-globins"),
                       dict(tips=["HBB human", "HBB zebrafish"], token="dna", style=("branch", "bar"), label="β-globins")],
               marks=[dict(node=["MB human", "HBB human"], kind="duplication"),
                      dict(node=["HBA human", "HBB human"], kind="duplication", text="α/β duplication", ha="right", shift=(-0.05, 0.12)),
                      dict(node=["MB human", "MB chicken"], kind="speciation"),
                      dict(node=["MB human", "MB mouse"], kind="speciation"),
                      dict(node=["HBA human", "HBA mouse"], kind="speciation"),
                      dict(node=["HBB human", "HBB mouse"], kind="speciation"),
                      dict(node=["HBA human", "HBA zebrafish"], kind="speciation"),
                      dict(node=["HBB human", "HBB zebrafish"], kind="speciation"),
                      dict(node=["HBA human", "HBA chicken"], kind="speciation"),
                      dict(node=["HBB human", "HBB chicken"], kind="speciation")])
t.scale_bar(ax, 0.1, at=(1.6, 0.8))
phylo.legend(ax, (6.2, 0.75), [("duplication", "Gene duplication"), ("speciation", "Speciation")])
