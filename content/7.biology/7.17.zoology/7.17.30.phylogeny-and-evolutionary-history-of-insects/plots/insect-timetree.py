# Dated tree of the major insect lineages (chronogram). Node ages are approximate and rounded to 5 Myr,
# combining Misof et al. 2014 (Insecta ~480 Ma, Pterygota ~405 Ma, Holometabola ~345 Ma) and later studies;
# many nodes are uncertain by 20-40 Myr. Polyneoptera collapsed to one tip; the split among Ephemeroptera,
# Odonata and Neoptera is drawn as a polytomy (unresolved). Fleas are included in Mecoptera.
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(Archaeognatha:480,(Zygentoma:450,(Ephemeroptera:405,Odonata:405,"
          "(Polyneoptera:390,((Psocodea:360,(Thysanoptera:350,Hemiptera:350)Condylognatha:10)Paraneoptera:15,"
          "(Hymenoptera:345,((Neuropterida:315,(Coleoptera:300,Strepsiptera:300)Coleopterida:15)Neuropteroidea:15,"
          "((Diptera:280,'Mecoptera (incl. fleas)':280)Antliophora:35,(Trichoptera:290,Lepidoptera:290)Amphiesmenoptera:25)"
          "Mecopterida:15)Aparaglossata:15)Holometabola:30)Eumetabola:15)Neoptera:15)Pterygota:45)Dicondylia:30)Insecta;")
ICONS = {"Archaeognatha": "phylopic/bristletail", "Zygentoma": "phylopic/silverfish",
         "Ephemeroptera": "phylopic/mayfly", "Odonata": "phylopic/dragonfly", "Polyneoptera": "phylopic/grasshopper",
         "Psocodea": "phylopic/barklouse", "Thysanoptera": "phylopic/thrips", "Hemiptera": "phylopic/cicada",
         "Hymenoptera": "phylopic/wasp", "Neuropterida": "phylopic/lacewing", "Coleoptera": "phylopic/beetle",
         "Strepsiptera": "phylopic/strepsipteran", "Diptera": "phylopic/housefly",
         "Mecoptera (incl. fleas)": "phylopic/scorpionfly", "Trichoptera": "phylopic/caddisfly",
         "Lepidoptera": "phylopic/moth"}

fig, ax = bio.canvas(24, 14)
t = phylo.tree(ax, NEWICK, origin=(0.6, 2.4), width=15.5, height=11.0, scaled=True, span=500, root_edge=20,
               icons=ICONS, icon_size=0.55, icon_width=1.2, icon_color="animal", label_size="small",
               clades=[dict(node="Holometabola", token="enzyme", style="band", label="Holometabola"),
                       dict(node="Paraneoptera", token="protein", style="band", label="Paraneoptera"),
                       dict(tips=["Polyneoptera"], token="positive", style="band", label="Polyneoptera")],
               marks=[dict(node="Pterygota", kind="trait", text="wings", token="positive", at=0.5),
                      dict(node="Neoptera", kind="trait", text="wing folding", token="positive", at=0.5),
                      dict(node="Holometabola", kind="trait", text="pupa", token="positive", at=0.5)])
t.time_lines(ax, [251.902, 66.0], ["End-Permian", "K–Pg"], y0=1.3, y1=t.frame[1] + t.frame[3] + 0.25)
t.time_axis(ax, ticks=[500, 400, 300, 200, 100, 0], minor=list(range(450, 0, -100)), y=2.0)
t.geo_scale(ax, y=1.3, ranks=("era", "period"), height=0.42)
bio.label(ax, (23.6, 0.35), "Ages approximate (after Misof et al. 2014 and later studies)", size="tiny",
          color=P.muted(), ha="right")
