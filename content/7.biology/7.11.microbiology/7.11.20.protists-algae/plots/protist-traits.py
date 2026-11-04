"""Representative genera of microbial eukaryotes on a cladogram of the supergroups (topology after the
phylogenomic consensus of Burki et al. 2020; unresolved relationships drawn as polytomies, root not resolved),
with four traits: plastid origin, mitochondrion type, mineral skeleton and disease of humans."""
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(25, 17)
NW = ("((((Homo,Monosiga)Holozoa,Saccharomyces)Opisthokonta,(Amoeba,(Entamoeba,(Dictyostelium,Physarum))))Amorphea,"
      "((Porphyra,Chlamydomonas)Archaeplastida,Guillardia,"
      "((Phytophthora,(Thalassiosira,Macrocystis))Stramenopiles,(Paramecium,(Alexandrium,Plasmodium))Alveolata,"
      "((Globigerina,Acantharia),Bigelowiella)Rhizaria)SAR,Emiliania)Diaphoretickes,"
      "((Euglena,Trypanosoma),Naegleria)Discoba,(Giardia,Trichomonas)Metamonada)Eukaryotes;")
icons = {"Homo": "phylopic/human", "Monosiga": "phylopic/choanoflagellate", "Saccharomyces": "phylopic/yeast",
         "Amoeba": "phylopic/amoeba", "Dictyostelium": "phylopic/dictyostelium", "Physarum": "phylopic/physarum",
         "Porphyra": "phylopic/porphyra", "Chlamydomonas": "phylopic/chlamydomonas", "Guillardia": "phylopic/cryptophyte",
         "Phytophthora": "phylopic/phytophthora", "Thalassiosira": "phylopic/diatom", "Macrocystis": "phylopic/kelp",
         "Paramecium": "phylopic/paramecium", "Alexandrium": "phylopic/dinoflagellate", "Plasmodium": "phylopic/plasmodium",
         "Globigerina": "phylopic/foraminiferan", "Acantharia": "phylopic/radiolarian", "Emiliania": "phylopic/coccolithophore",
         "Euglena": "phylopic/euglena", "Trypanosoma": "phylopic/trypanosoma", "Naegleria": "phylopic/naegleria",
         "Giardia": "phylopic/giardia"}
group = {"Discoba": "rna", "Metamonada": "negative", "Amorphea": "animal", "Archaeplastida": "plant",
         "Stramenopiles": "golgi", "Alveolata": "dna", "Rhizaria": "highlight"}
t = phylo.tree(ax, NW, origin=(0.6, 0.9), width=6.2, height=14.6, label_size="small", italic=True,
               tip_text={"Acantharia": "radiolarian"}, icons=icons, icon_size=0.62, icon_color="neutral",
               clades=[dict(node=k, token=v, style="branch") for k, v in group.items()])
for k, lab in [("Discoba", "Discoba"), ("Metamonada", "Metamonada"), ("Amorphea", "Amorphea"),
               ("Archaeplastida", "Archaeplastida"), ("Stramenopiles", "Stramenopiles"), ("Alveolata", "Alveolata"),
               ("Rhizaria", "Rhizaria")]:
    x, y = t.node(k).xy
    bio.label(ax, (x - 0.12, y + 0.22), lab, size="tiny", ha="right", color=P.edge(group[k]))

# trait columns
cols = [11.6, 14.4, 17.4, 21.0]
heads = ["plastid", "mitochondrion", "mineral\nskeleton", "disease of humans"]
for c, h in zip(cols, heads):
    bio.label(ax, (c, 16.35), h, size="small", bold=True)
plastid = {"Porphyra": "1", "Chlamydomonas": "1", "Guillardia": "2r", "Thalassiosira": "2r", "Macrocystis": "2r",
           "Alexandrium": "2r", "Plasmodium": "relict", "Bigelowiella": "2g", "Emiliania": "2r", "Euglena": "2g"}
mito = {"Entamoeba": "mitosome", "Giardia": "mitosome", "Trichomonas": "hydrogenosome"}
skel = {"Thalassiosira": "silica", "Globigerina": "CaCO3", "Acantharia": "silica or SrSO4", "Emiliania": "CaCO3"}
disease = {"Entamoeba": "amoebic dysentery", "Plasmodium": "malaria", "Trypanosoma": "sleeping sickness, Chagas",
           "Naegleria": "meningoencephalitis (rare)", "Giardia": "giardiasis", "Trichomonas": "trichomoniasis",
           "Phytophthora": "(potato late blight)", "Alexandrium": "(shellfish poisoning)"}
for tip in t.root.leaves():
    y = tip.xy[1]
    p = plastid.get(tip.name)
    if p == "1":
        ax.plot([cols[0]], [y], marker="*", ms=13, color=P.edge("positive"), zorder=12)
    elif p in ("2r", "2g"):
        tok = "negative" if p == "2r" else "positive"
        ax.plot([cols[0]], [y], marker="^", ms=8, color=P.edge(tok), zorder=12)
    elif p == "relict":
        ax.plot([cols[0]], [y], marker="^", ms=8, color=P.edge("negative"), markerfacecolor="none", mew=1.4, zorder=12)
    m = mito.get(tip.name)
    if m:
        ax.plot([cols[1]], [y], "o", ms=8, color=P.edge("mitochondrion"), markerfacecolor="none", mew=1.4, zorder=12)
        bio.label(ax, (cols[1] + 0.3, y), m, size="tiny", ha="left")
    else:
        ax.plot([cols[1]], [y], "o", ms=8, color=P.edge("mitochondrion"), zorder=12)
    if tip.name in skel:
        s = {"CaCO3": "CaCO$_3$", "silica or SrSO4": "silica or SrSO$_4$"}.get(skel[tip.name], skel[tip.name])
        bio.label(ax, (cols[2], y), s, size="small")
    if tip.name in disease:
        bio.label(ax, (cols[3] - 1.6, y), disease[tip.name], size="tiny", ha="left",
                  color=P.muted() if disease[tip.name].startswith("(") else P.ink())
# legend
lx, ly = 0.8, 0.35
ax.plot([lx], [ly], marker="*", ms=12, color=P.edge("positive")); bio.label(ax, (lx + 0.3, ly), "primary plastid", size="tiny", ha="left")
ax.plot([lx + 4.2], [ly], marker="^", ms=8, color=P.edge("positive")); bio.label(ax, (lx + 4.5, ly), "secondary, green", size="tiny", ha="left")
ax.plot([lx + 8.6], [ly], marker="^", ms=8, color=P.edge("negative")); bio.label(ax, (lx + 8.9, ly), "secondary or tertiary, red", size="tiny", ha="left")
ax.plot([lx + 14.4], [ly], marker="^", ms=8, color=P.edge("negative"), markerfacecolor="none", mew=1.4)
bio.label(ax, (lx + 14.7, ly), "nonphotosynthetic relict", size="tiny", ha="left")
ax.plot([lx + 19.6], [ly], "o", ms=8, color=P.edge("mitochondrion")); bio.label(ax, (lx + 19.9, ly), "aerobic mitochondrion", size="tiny", ha="left")
