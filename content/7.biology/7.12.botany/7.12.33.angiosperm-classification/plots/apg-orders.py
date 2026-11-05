# The 64 orders of APG IV (2016, Bot. J. Linn. Soc. 181: 1-20, fig. 1) as a circular cladogram. Relationships
# that APG IV leaves unresolved are drawn as polytomies: the five lineages of Mesangiospermae (magnoliids,
# Chloranthales, monocots, Ceratophyllales, eudicots) and the orders of the lamiid crown. Coloured bands
# mark the major clades; the label of each band gives the chapters of this course (7.12.34-49) that treat it.
import wikibio as bio
from wikibio import phylo

ANA = "Amborellales,(Nymphaeales,(Austrobaileyales,MESANGIO))"
MAGNOLIIDS = "((Canellales,Piperales),(Magnoliales,Laurales))Magnoliids"
MONOCOTS = ("(Acorales,(Alismatales,(Petrosaviales,((Dioscoreales,Pandanales),(Liliales,(Asparagales,"
            "(Arecales,(Poales,(Commelinales,Zingiberales)))Commelinids))))))Monocots")
FABIDS = ("(Zygophyllales,((Celastrales,(Oxalidales,Malpighiales))COM,"
          "(Fabales,(Rosales,(Fagales,Cucurbitales)))))Fabids")
MALVIDS = ("(Geraniales,(Myrtales,(Crossosomatales,(Picramniales,(Sapindales,(Huerteales,"
           "(Malvales,Brassicales)))))))Malvids")
ROSIDS = "(Saxifragales,(Vitales,(" + FABIDS + "," + MALVIDS + "))Rosids)Superrosids"
LAMIIDS = "(Icacinales,(Metteniusales,(Garryales,(Boraginales,Gentianales,Vahliales,Solanales,Lamiales))))Lamiids"
CAMPANULIDS = ("(Aquifoliales,(Asterales,(Escalloniales,((Bruniales,Apiales),(Paracryphiales,Dipsacales)))))"
               "Campanulids")
ASTERIDS = "(Cornales,(Ericales,(" + LAMIIDS + "," + CAMPANULIDS + ")))Asterids"
SUPERASTERIDS = "(Berberidopsidales,(Santalales,(Caryophyllales," + ASTERIDS + ")))Superasterids"
EUDICOTS = ("(Ranunculales,(Proteales,(Trochodendrales,(Buxales,(Gunnerales,(Dilleniales," + ROSIDS + ","
            + SUPERASTERIDS + ")Pentapetalae)Gunneridae))))Eudicots")
MESANGIO = "(" + MAGNOLIIDS + ",Chloranthales," + MONOCOTS + ",(Ceratophyllales," + EUDICOTS + "))Mesangiospermae"
NEWICK = "(" + ANA.replace("MESANGIO", MESANGIO) + ")Angiosperms;"


def group(members, token, text, at=None):
    """Bands for a grade or a run of sister lineages: one band per member, the label on member ``at``."""
    at = len(members) // 2 if at is None else at
    return [dict(tips=m if isinstance(m, list) else [m], token=token, style=("band", "branch"),
                 label=text if i == at else None) for i, m in enumerate(members)]


CLADES = (group(["Amborellales", "Nymphaeales", "Austrobaileyales"], "neutral", "ANA grade (34)")
          + [dict(node="Magnoliids", token="petal", style=("band", "branch"), label="Magnoliids (35)"),
             dict(tips=["Chloranthales"], token="anther", style=("band", "branch"), label="Chloranthales (35)")]
          + group(["Acorales", "Alismatales", "Petrosaviales", ["Dioscoreales", "Pandanales"], "Liliales"], "rna",
                  "Monocots (36)", at=2)
          + [dict(tips=["Asparagales"], token="mrna", style=("band", "branch"), label="37"),
             dict(node="Commelinids", token="rrna", style=("band", "branch"), label="Commelinids (38, 39)"),
             dict(tips=["Ceratophyllales"], token="neutral", style=("band", "branch"), label="34")]
          + group(["Ranunculales", "Proteales", "Trochodendrales", "Buxales", "Gunnerales", "Dilleniales"], "atp",
                  "Early eudicots (40)")
          + group(["Saxifragales", "Vitales"], "enzyme", "41", at=0)
          + [dict(node="Fabids", token="plant", style=("band", "branch"), label="Fabids (42, 43)"),
             dict(node="Malvids", token="chloroplast", style=("band", "branch"), label="Malvids (44)")]
          + group(["Berberidopsidales", "Santalales", "Caryophyllales"], "channel", "45")
          + group(["Cornales", "Ericales"], "receptor", "46", at=0)
          + [dict(node="Lamiids", token="dna", style=("band", "branch"), label="Lamiids (47, 48)"),
             dict(node="Campanulids", token="protein", style=("band", "branch"), label="Campanulids (49)")])

fig, ax = bio.canvas(24, 24)
t = phylo.tree(ax, NEWICK, layout="circular", center=(12, 12), radius=6.6, start=90, arc=355, label_size="tiny",
               clades=CLADES,
               marks=[dict(node="Mesangiospermae", kind="dot", text="Mesangiospermae", text_size="tiny"),
                      dict(node="Eudicots", kind="trait", text="Tricolpate pollen", text_size="tiny"),
                      dict(node="Monocots", kind="trait", text="One cotyledon", text_size="tiny")])
bio.label(ax, (12, 23.3), "APG IV: 64 orders of flowering plants", size="title")
