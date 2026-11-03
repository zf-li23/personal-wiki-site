"""Some major groups of organisms and their relationships (cladogram). Eukaryotes arose from a
partnership between an archaeon related to the Asgard archaea and an alphaproteobacterium that became
the mitochondrion (star); a green-algal ancestor of plants acquired a cyanobacterium that became the
chloroplast (bar). Fungi and animals share an ancestor (opisthokonts); choanoflagellates are the
sister group of animals; birds are the sister group of crocodiles, primates of rodents and their
relatives, whales of hippopotamuses. Topology after Futuyma and Kirkpatrick (2017), Fig. 2.5, with the
origin of eukaryotes within the archaea following current phylogenomic consensus."""
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("((Proteobacteria,Cyanobacteria)Bacteria,(Other_archaea,(Asgard_archaea,"
          "((Brown_algae,(Green_algae,Land_plants)Archaeplastida)Diaphoretickes,"
          "(Amoebozoans,(Fungi,(Choanoflagellates,(Sponges,(Cnidarians,"
          "((Echinoderms,(Ray-finned_fishes,((Birds,Crocodiles)Archosaurs,"
          "((Primates,Rodents)Euarchontoglires,(Hippopotamuses,Whales)Whippomorpha)Mammals)Tetrapods)Vertebrates)"
          "Deuterostomes,(Molluscs,Arthropods)Protostomes)Bilateria)Eumetazoa)Animals)Choanozoa)Opisthokonts)"
          "Amorphea)Eukaryotes)AsgardEuk)Archaea)LUCA;")
ICONS = {
    "Proteobacteria": "phylopic/e-coli", "Cyanobacteria": "phylopic/cyanobacterium",
    "Green algae": "phylopic/chlamydomonas", "Land plants": "phylopic/fern", "Amoebozoans": "phylopic/dictyostelium",
    "Fungi": "phylopic/yeast", "Choanoflagellates": "phylopic/choanoflagellate", "Sponges": "phylopic/sponge",
    "Cnidarians": "phylopic/jellyfish", "Echinoderms": "phylopic/starfish", "Ray-finned fishes": "phylopic/zebrafish",
    "Birds": "phylopic/pigeon", "Crocodiles": "phylopic/crocodile", "Primates": "phylopic/human",
    "Rodents": "phylopic/mouse", "Whales": "phylopic/orca", "Molluscs": "phylopic/snail", "Arthropods": "phylopic/drosophila",
}
fig, ax = bio.canvas(19, 15)
t = phylo.tree(ax, NEWICK, origin=(0.8, 0.8), width=10.5, height=13.4, root_edge=0.4, icons=ICONS, icon_size=0.55,
               icon_width=1.2, label_size="small",
               clades=[dict(node="Bacteria", token="bacterium", style=("branch", "bar"), label="Bacteria"),
                       dict(node="Other archaea", token="rrna", style="branch"),
                       dict(node="Asgard archaea", token="rrna", style="branch"),
                       dict(node="Eukaryotes", token="protein", style="bar", label="Eukaryotes"),
                       dict(node="Animals", token="animal", style="bar", label="Animals")],
               marks=[dict(node="Eukaryotes", kind="star", at=0.5, size=0.28),
                      dict(node="Archaeplastida", kind="trait", at=0.5, token="chloroplast"),
                      dict(node="LUCA", kind="dot", text="LUCA", side=-1)])
phylo.legend(ax, (0.9, 3.2), [("line", "Archaea (a grade: eukaryotes arose within it)", "rrna"),
                               ("star", "mitochondrion from an alphaproteobacterium"),
                               ("trait", "chloroplast from a cyanobacterium", "chloroplast")])
