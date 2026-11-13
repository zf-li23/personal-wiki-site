# Relationships of the orders of living mammals (cladogram), simplified after Meredith et al. 2011,
# Upham et al. 2019 and Foley et al. 2023. Placental mammals form four superorders; the position of the
# placental root (Atlantogenata versus Boreoeutheria) is supported by most genomic analyses but debated.
# Numbers are approximate counts of living species (Mammal Diversity Database 2024).
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(Monotremata,((Didelphimorphia,(Paucituberculata,(Microbiotheria,(Dasyuromorphia,"
          "(Peramelemorphia,Diprotodontia)))))Marsupialia,"
          "((((Proboscidea,Sirenia),Hyracoidea),(Tubulidentata,(Macroscelidea,Afrosoricida)))Afrotheria,"
          "(Cingulata,Pilosa)Xenarthra)Atlantogenata_xx,"
          "((((Rodentia,Lagomorpha)Glires,(Scandentia,(Dermoptera,Primates))Euarchonta)Euarchontoglires,"
          "(Eulipotyphla,(Chiroptera,((Pholidota,Carnivora),(Perissodactyla,Cetartiodactyla))))Laurasiatheria)"
          "Boreoeutheria)Placentalia)Theria)Mammalia;").replace("Atlantogenata_xx", "Atlantogenata")
N = {"Monotremata": "platypus, echidnas (5)", "Didelphimorphia": "opossums (~120)",
     "Paucituberculata": "shrew opossums (7)", "Microbiotheria": "monito del monte (3)",
     "Dasyuromorphia": "quolls, numbat, devil (~80)", "Peramelemorphia": "bandicoots (~25)",
     "Diprotodontia": "kangaroos, koala, wombats (~155)", "Proboscidea": "elephants (3)",
     "Sirenia": "dugong, manatees (4)", "Hyracoidea": "hyraxes (5)", "Tubulidentata": "aardvark (1)",
     "Macroscelidea": "elephant shrews (~20)", "Afrosoricida": "tenrecs, golden moles (~55)",
     "Cingulata": "armadillos (~22)", "Pilosa": "sloths, anteaters (~10)", "Rodentia": "rodents (~2 600)",
     "Lagomorpha": "rabbits, pikas (~100)", "Scandentia": "treeshrews (~23)", "Dermoptera": "colugos (2)",
     "Primates": "primates (~520)", "Eulipotyphla": "hedgehogs, shrews, moles (~550)",
     "Chiroptera": "bats (~1 480)", "Pholidota": "pangolins (8)", "Carnivora": "carnivorans (~300)",
     "Perissodactyla": "horses, rhinos, tapirs (~17)", "Cetartiodactyla": "even-toed ungulates, whales (~350)"}
TEXT = {k: f"{k}: {v}" for k, v in N.items()}
ICONS = {"Monotremata": "phylopic/platypus", "Didelphimorphia": "phylopic/opossum",
         "Dasyuromorphia": "phylopic/numbat", "Diprotodontia": "phylopic/kangaroo",
         "Proboscidea": "phylopic/african-elephant", "Sirenia": "phylopic/manatee", "Hyracoidea": "phylopic/hyrax",
         "Tubulidentata": "phylopic/aardvark", "Macroscelidea": "phylopic/elephant-shrew",
         "Afrosoricida": "phylopic/tenrec", "Cingulata": "phylopic/armadillo", "Pilosa": "phylopic/sloth",
         "Rodentia": "phylopic/mouse", "Lagomorpha": "phylopic/rabbit", "Scandentia": "phylopic/tree-shrew",
         "Dermoptera": "phylopic/colugo", "Primates": "phylopic/macaque", "Eulipotyphla": "phylopic/hedgehog",
         "Chiroptera": "phylopic/bat", "Pholidota": "phylopic/pangolin", "Carnivora": "phylopic/tiger",
         "Perissodactyla": "phylopic/horse", "Cetartiodactyla": "phylopic/deer"}
fig, ax = bio.canvas(21, 15.5)
phylo.tree(ax, NEWICK, origin=(0.6, 0.9), width=8.0, height=13.8, root_edge=0.4, icons=ICONS, icon_size=0.5,
           icon_width=1.2, icon_color="animal", label_size="tiny", tip_text=TEXT,
           clades=[dict(node="Marsupialia", token="mrna", style="bar", label="Marsupialia"),
                   dict(node="Afrotheria", token="highlight", style="bar", label="Afrotheria"),
                   dict(node="Xenarthra", token="neutral", style="bar", label="Xenarthra"),
                   dict(node="Euarchontoglires", token="dna", style="bar", label="Euarchontoglires"),
                   dict(node="Laurasiatheria", token="positive", style="bar", label="Laurasiatheria")])
bio.label(ax, (0.6, 0.3), "Cladogram; approximate numbers of living species", size="tiny", color=P.muted(),
          ha="left")
