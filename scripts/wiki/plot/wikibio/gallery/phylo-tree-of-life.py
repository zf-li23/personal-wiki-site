# The tree of life as a circular cladogram: two domains, with eukaryotes branching from within the
# Asgard archaea (Eme et al. 2023, Nature 618:992). Bacterial and eukaryotic supergroups follow
# Coleman et al. 2021 (Science 372:eabe0511) and Burki et al. 2020 (Trends Ecol. Evol. 35:43).
import wikibio as bio
from wikibio import phylo

BACTERIA = ("(((Bacillus_subtilis,Staphylococcus_aureus),(Streptomyces_coelicolor,Synechocystis_sp.)),"
            "((Escherichia_coli,Vibrio_cholerae),(Bacteroides_fragilis,Chlamydia_trachomatis)))")
ARCHAEA = ("(Nanoarchaeum_equitans,(((Methanocaldococcus_jannaschii,Pyrococcus_furiosus),Halobacterium_salinarum),"
           "((Sulfolobus_acidocaldarius,Nitrosopumilus_maritimus),"
           "(Lokiarchaeia,(Heimdallarchaeia,EUK)))))")
EUKARYA = ("((Giardia_intestinalis,Trypanosoma_brucei),((Arabidopsis_thaliana,Chlamydomonas_reinhardtii),"
           "(Plasmodium_falciparum,Phytophthora_infestans)),(Dictyostelium_discoideum,(Saccharomyces_cerevisiae,Homo_sapiens)))")
NEWICK = "(" + BACTERIA + "," + ARCHAEA.replace("EUK", EUKARYA) + ");"
GROUPS = {"Lokiarchaeia", "Heimdallarchaeia"}

fig, ax = bio.canvas(19, 17)
t = phylo.tree(ax, NEWICK, layout="circular", center=(9.5, 8.6), radius=4.3, start=90, arc=360, 
               italic=lambda name: name not in GROUPS, label_size="tiny",
               clades=[dict(tips=["Bacillus subtilis", "Chlamydia trachomatis"], token="bacterium", style=("band", "branch"),
                            label="Bacteria"),
                       dict(node="Nanoarchaeum equitans", token="rrna", style=("band", "branch"), label="DPANN"),
                       dict(tips=["Methanocaldococcus jannaschii", "Halobacterium salinarum"], token="rna",
                            style=("band", "branch"), label="Euryarchaeota"),
                       dict(tips=["Sulfolobus acidocaldarius", "Nitrosopumilus maritimus"], token="atp", style=("band", "branch"),
                            label="TACK"),
                       dict(node="Lokiarchaeia", token="channel", style="branch"),  # Asgard archaea: a grade that
                       dict(node="Heimdallarchaeia", token="channel", style="branch"),  # includes the eukaryotes
                       dict(tips=["Giardia intestinalis", "Homo sapiens"], token="protein", style=("band", "branch"),
                            label="Eukarya")],
               marks=[dict(node=["Giardia intestinalis", "Homo sapiens"], kind="star", at=0.5, size=0.26),
                      dict(node=["Arabidopsis thaliana", "Chlamydomonas reinhardtii"], kind="trait", at=0.5,
                           token="chloroplast")])
phylo.legend(ax, (0.8, 1.4), [("line", "Asgard archaea (a grade including Eukarya)", "channel"), ("star", "Mitochondrial endosymbiosis"),
                              ("trait", "Primary plastid endosymbiosis", "chloroplast")])
