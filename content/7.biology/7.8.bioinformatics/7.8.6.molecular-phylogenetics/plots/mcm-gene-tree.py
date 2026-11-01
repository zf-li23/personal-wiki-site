# A gene tree of the MCM family. The 15 proteins of 7.8.5 (human MCM2-7, MCM6 of eight further eukaryotes,
# the single MCM of the archaeon Saccharolobus solfataricus) were aligned with FAMSA (1282 columns);
# distances are Kimura's protein distances -ln(1 - p - 0.2 p^2) from the proportion p of differing residues
# (pairwise deletion of gaps), and the tree is the neighbor-joining tree, rooted with the archaeal protein
# as outgroup. Numbers are bootstrap percentages from 1000 resamplings of the alignment columns (computed
# with the same distance and NJ code). Nodes where eukaryotic paralogs separate are gene duplications
# (squares); nodes inside the MCM6 clade are speciations. The MCM6 orthologs form a clade with 100 %
# support, but the order of the duplications that produced MCM2-7 is poorly resolved (31-54 %), and within
# MCM6 the grouping of animals with fungi (opisthokonts), part of the accepted species tree, receives 21 %.
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(MCM_SACS2:0.6102,((MCM2_HUMAN:0.7648,MCM3_HUMAN:0.7052)54:0.06113,(MCM5_HUMAN:0.7393,"
          "(((MCM6_DICDI:0.4746,(MCM6_ARATH:0.164,MCM6_ORYSI:0.1663)100:0.2642)61:0.0405,"
          "(((MCM6_HUMAN:0.01862,MCM6_MOUSE:0.02404)100:0.2005,(MCM6_DROME:0.151,MCM6_ANOGA:0.1162)100:0.1222)100:0.2011,"
          "(MCM6_SCHPO:0.3243,MCM6_YEAST:0.3361)100:0.1385)21:0.002829)100:0.2968,"
          "(MCM4_HUMAN:0.6879,MCM7_HUMAN:0.6999)33:0.03623)31:0.03594)33:0.02509)Dup:0.0);")
text = {"MCM SACS2": "MCM (archaeon)", "MCM2 HUMAN": "MCM2 human", "MCM3 HUMAN": "MCM3 human",
        "MCM4 HUMAN": "MCM4 human", "MCM5 HUMAN": "MCM5 human", "MCM7 HUMAN": "MCM7 human",
        "MCM6 HUMAN": "MCM6 human", "MCM6 MOUSE": "MCM6 mouse", "MCM6 DROME": "MCM6 fruit fly",
        "MCM6 ANOGA": "MCM6 mosquito", "MCM6 ARATH": "MCM6 thale cress", "MCM6 ORYSI": "MCM6 rice",
        "MCM6 DICDI": "MCM6 slime mold", "MCM6 SCHPO": "MCM6 fission yeast", "MCM6 YEAST": "MCM6 budding yeast"}
mcm6 = [k for k in text if k.startswith("MCM6")]
fig, ax = bio.canvas(18.0, 12.0)
t = phylo.tree(ax, NEWICK, origin=(0.8, 0.8), width=11.0, height=10.4, scaled=True, span=0.9, tip_text=text,
               support="label", support_min=0, label_size="small",
               clades=[dict(tips=mcm6, token="dna", style="band", label="MCM6 orthologs")],
               marks=[dict(node=["MCM2 HUMAN", "MCM5 HUMAN"], kind="duplication"),
                      dict(node=["MCM2 HUMAN", "MCM3 HUMAN"], kind="duplication"),
                      dict(node=["MCM5 HUMAN", "MCM6 HUMAN"], kind="duplication"),
                      dict(node=["MCM4 HUMAN", "MCM6 HUMAN"], kind="duplication"),
                      dict(node=["MCM4 HUMAN", "MCM7 HUMAN"], kind="duplication")])
bio.scale_bar(ax, (1.0, 0.3), 11.0 / 0.9 * 0.2, "0.2 substitutions per site", size="tiny")
