# Relationships of the main orders of living birds (cladogram), simplified after Prum et al. 2015, Kuhl et
# al. 2021 and Stiller et al. 2024. Palaeognathae and Neognathae split first; Neognathae comprise
# Galloanserae and Neoaves. The branching order of the major clades at the base of Neoaves (shown as a
# polytomy) is still uncertain because they diverged rapidly just after the K-Pg extinction. Numbers are
# approximate counts of living species (IOC World Bird List 2024).
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("((Struthioniformes,(Rheiformes,(Tinamiformes,(Apterygiformes,Casuariiformes))))Palaeognathae,"
          "((Galliformes,Anseriformes)Galloanserae,"
          "((Phoenicopteriformes,Podicipediformes)Mirandornithes,(Caprimulgiformes,Apodiformes)Strisores,"
          "((Otidiformes,Cuculiformes),Columbiformes)Columbaves,(Gruiformes,Charadriiformes),"
          "((Gaviiformes,((Sphenisciformes,Procellariiformes),(Ciconiiformes,(Suliformes,Pelecaniformes))))"
          "Aequornithes,(Accipitriformes,(Strigiformes,((Bucerotiformes,(Coraciiformes,Piciformes)),"
          "(Falconiformes,(Psittaciformes,Passeriformes)))))Telluraves))Neoaves)Neognathae);")
N = {"Struthioniformes": "ostriches (2)", "Rheiformes": "rheas (2)", "Tinamiformes": "tinamous (47)",
     "Apterygiformes": "kiwis (5)", "Casuariiformes": "cassowaries, emu (4)",
     "Galliformes": "pheasants, chickens (~300)", "Anseriformes": "ducks, geese (~180)",
     "Phoenicopteriformes": "flamingos (6)", "Podicipediformes": "grebes (~20)",
     "Caprimulgiformes": "nightjars (~100)", "Apodiformes": "swifts, hummingbirds (~470)",
     "Otidiformes": "bustards (~26)", "Cuculiformes": "cuckoos (~150)", "Columbiformes": "pigeons (~350)",
     "Gruiformes": "cranes, rails (~190)", "Charadriiformes": "shorebirds, gulls, auks (~390)",
     "Gaviiformes": "loons (5)", "Sphenisciformes": "penguins (18)",
     "Procellariiformes": "albatrosses, petrels (~150)", "Ciconiiformes": "storks (~20)",
     "Suliformes": "cormorants, boobies (~60)", "Pelecaniformes": "pelicans, herons, ibises (~120)",
     "Accipitriformes": "hawks, eagles, vultures (~260)", "Strigiformes": "owls (~250)",
     "Bucerotiformes": "hornbills, hoopoes (~75)", "Coraciiformes": "kingfishers, rollers (~180)",
     "Piciformes": "woodpeckers, barbets (~480)", "Falconiformes": "falcons (~65)",
     "Psittaciformes": "parrots (~400)", "Passeriformes": "passerines (~6 600)"}
TEXT = {k: f"{k}: {v}" for k, v in N.items()}
ICONS = {"Struthioniformes": "phylopic/ostrich", "Rheiformes": "phylopic/rhea", "Tinamiformes": "phylopic/tinamou",
         "Apterygiformes": "phylopic/kiwi", "Casuariiformes": "phylopic/cassowary",
         "Galliformes": "phylopic/chicken", "Anseriformes": "phylopic/duck",
         "Phoenicopteriformes": "phylopic/flamingo", "Podicipediformes": "phylopic/grebe",
         "Caprimulgiformes": "phylopic/nightjar", "Apodiformes": "phylopic/hummingbird",
         "Cuculiformes": "phylopic/cuckoo", "Columbiformes": "phylopic/pigeon", "Gruiformes": "phylopic/crane",
         "Charadriiformes": "phylopic/gull", "Gaviiformes": "phylopic/loon", "Sphenisciformes": "phylopic/penguin",
         "Procellariiformes": "phylopic/albatross", "Ciconiiformes": "phylopic/stork",
         "Suliformes": "phylopic/cormorant", "Pelecaniformes": "phylopic/heron",
         "Accipitriformes": "phylopic/eagle", "Strigiformes": "phylopic/owl", "Bucerotiformes": "phylopic/hornbill",
         "Coraciiformes": "phylopic/kingfisher", "Piciformes": "phylopic/woodpecker",
         "Falconiformes": "phylopic/falcon", "Psittaciformes": "phylopic/parrot", "Passeriformes": "phylopic/sparrow"}
fig, ax = bio.canvas(19.5, 17)
phylo.tree(ax, NEWICK, origin=(0.6, 0.9), width=8.5, height=15.4, root_edge=0.4, icons=ICONS, icon_size=0.45,
           icon_width=1.1, icon_color="animal", label_size="tiny", tip_text=TEXT,
           clades=[dict(node="Palaeognathae", token="dna", style="bar", label="Palaeognathae"),
                   dict(node="Galloanserae", token="mrna", style="bar", label="Galloanserae"),
                   dict(node="Neoaves", token="positive", style="bar", label="Neoaves")])
bio.label(ax, (0.6, 0.3), "Cladogram; basal Neoaves shown as a polytomy; approximate numbers of living species",
          size="tiny", color=P.muted(), ha="left")
