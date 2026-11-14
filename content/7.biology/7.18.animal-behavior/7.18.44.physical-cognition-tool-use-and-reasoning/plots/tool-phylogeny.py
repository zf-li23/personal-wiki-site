# Tool use has evolved many times. Cladogram (topology only) of a selection of tool-using animals with
# their best-documented tool behavior; bars mark tool use and stars tool manufacture (modifying an object
# before use). Sources: Goodall 1964, Boesch and Boesch 1990 (chimpanzees); Fragaszy et al. 2004
# (bearded capuchins); Gumert et al. 2009 (long-tailed macaques); Hall and Schaller 1964 (sea otters);
# Kruetzen et al. 2005 (dolphin sponging); Hart et al. 2001 (elephants modifying branches as fly
# switches); Hunt 1996 (New Caledonian crows); Tebbich et al. 2001 (woodpecker finch); Auersperg et al.
# 2012 (Goffin's cockatoo); van Lawick-Goodall 1968 (Egyptian vultures); Finn et al. 2009 (veined
# octopus); Maak et al. 2017 (Aphaenogaster ants); Peckham and Peckham 1898 (Ammophila wasps).
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(((Ant,Wasp)Insects,Octopus)Protostomes,((((NC_crow,Finch)Passerines,Cockatoo)Psittacopasserae,"
          "Vulture)Birds,(((Chimpanzee,Macaque)Catarrhines,Capuchin)Primates,(Otter,Dolphin)Laurasiatheria,"
          "Elephant)Mammals)Amniotes)Bilateria;")
TEXT = {
    "Ant": "Funnel ants: debris as sponges for liquid food",
    "Wasp": "Thread-waisted wasps: pebble to tamp the burrow",
    "Octopus": "Veined octopus: carries coconut shells as shelter",
    "NC crow": "New Caledonian crow: hooked twig and leaf tools",
    "Finch": "Woodpecker finch: cactus spines as probes",
    "Cockatoo": "Goffin's cockatoo: cuts stick tools (captivity)",
    "Vulture": "Egyptian vulture: throws stones at ostrich eggs",
    "Chimpanzee": "Chimpanzee: termite probes, stone hammers, tool sets",
    "Macaque": "Long-tailed macaque: stones to open shellfish",
    "Capuchin": "Bearded capuchin: stone hammers and anvils",
    "Otter": "Sea otter: stone anvil carried on the chest",
    "Dolphin": "Bottlenose dolphin: marine sponge over the rostrum",
    "Elephant": "Elephants: trimmed branches as fly switches",
}
ICONS = {"Ant": "phylopic/ant", "Wasp": "phylopic/wasp", "Octopus": "phylopic/octopus",
         "Finch": "phylopic/darwin-finch", "Cockatoo": "phylopic/parrot", "Chimpanzee": "phylopic/chimpanzee",
         "Macaque": "phylopic/macaque", "Dolphin": "phylopic/dolphin", "Elephant": "phylopic/african-elephant"}
MAKERS = ["NC crow", "Finch", "Cockatoo", "Chimpanzee", "Elephant"]
USERS = ["Ant", "Wasp", "Octopus", "Vulture", "Macaque", "Capuchin", "Otter", "Dolphin"]
MARKS = [dict(node=t, kind="trait", at=0.55, token="highlight") for t in USERS]
MARKS += [dict(node=t, kind="star", at=0.55, token="rna", size=0.22) for t in MAKERS]

fig, ax = bio.canvas(22, 12.2)
phylo.tree(ax, NEWICK, origin=(0.8, 1.5), width=7.2, height=9.8, direction="right", root_edge=0.3,
           tip_text=TEXT, icons=ICONS, icon_size=0.55, icon_width=0.95, label_size="small", marks=MARKS,
           clades=[dict(node="Birds", token="dna", style="band", label="Birds"),
                   dict(node="Mammals", token="animal", style="band", label="Mammals"),
                   dict(node="Protostomes", token="plant", style="band", label="Invertebrates")])
phylo.legend(ax, (1.2, 0.75), [("trait", "tool use", "highlight")], size="small")
phylo.legend(ax, (5.0, 0.75), [("star", "tool manufacture", "rna")], size="small")
bio.label(ax, (9.0, 0.75), "Topology only; tool use arose independently in these lineages.", size="tiny",
          color=P.muted(), ha="left")
