# Panarthropod relationships with Cambrian stem groups (dagger: extinct). Tardigrades are the sister group
# of onychophorans plus arthropods. The lobopodians form a grade along the stems: Hallucigenia is a stem
# onychophoran, the gilled lobopodians (Kerygmachela, Pambdelurion), Opabinia and the radiodonts
# (Anomalocaris) are successive stem arthropods. Hard, jointed trunk limbs and segmental sclerites appear
# only in the upper stem (Fuxianhuia) and the crown (Euarthropoda). Trilobites belong to the crown group
# (Artiopoda), close either to the chelicerates or to the mandibulates.
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(21, 12)
nwk = ("(Tardigrada,(('Hallucigenia †',Onychophora)Onychophora_total,('Kerygmachela †',('Pambdelurion †',"
       "('Opabinia †',('Anomalocaris †',('Fuxianhuia †',('Trilobita †',Chelicerata,(Myriapoda,Pancrustacea)Mandibulata)"
       "Arthropoda_crown)Euarthropoda)Radiodonta_up)Op_up)Pamb_up)Arthropoda_total)Lobopodia_up)Panarthropoda;")
t = phylo.tree(ax, nwk, origin=(0.8, 1.0), width=11.0, height=10.0, root_edge=0.5, label_size="small",
               icons={"Tardigrada": "phylopic/tardigrade", "Onychophora": "phylopic/velvet-worm",
                      "Hallucigenia †": "phylopic/hallucigenia", "Trilobita †": "phylopic/trilobite",
                      "Chelicerata": "phylopic/scorpion", "Myriapoda": "phylopic/centipede",
                      "Pancrustacea": "phylopic/crayfish"},
               icon_size=0.7, icon_color="animal",
               italic={"Hallucigenia †", "Kerygmachela †", "Pambdelurion †", "Opabinia †", "Anomalocaris †", "Fuxianhuia †"},
               clades=[dict(node="Arthropoda crown", token="dna", style="bar", label="Crown Arthropoda"),
                       dict(node="Arthropoda total", token="plant", style="band", label="")],
               marks=[dict(node="Panarthropoda", kind="trait", text="paired clawed limbs", at=0.5),
                      dict(node="Radiodonta up", kind="trait", text="compound eyes", at=0.5),
                      dict(node="Euarthropoda", kind="trait", text="jointed limbs, sclerites", at=0.5),
                      dict(node="Mandibulata", kind="trait", text="mandibles", at=0.5)])
bio.label(ax, (14.3, 0.4), "Green band: total-group Arthropoda", size="tiny", color=P.muted())
