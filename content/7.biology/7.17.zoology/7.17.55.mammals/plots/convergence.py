# Convergent evolution of marsupials (Australia) and placental mammals (other continents): pairs of species
# with similar body forms and ways of life that evolved independently (silhouettes from PhyloPic, not to
# scale). Thylacine (Thylacinus cynocephalus, extinct 1936) and grey wolf: cursorial carnivores. Sugar glider
# (Petaurus breviceps) and flying squirrel (Pteromys): gliders with a patagium between fore- and hindlimbs.
# Marsupial mole (Notoryctes) and mole (Talpidae): burrowers with reduced eyes and digging forelimbs.
# Numbat (Myrmecobius) and giant anteater (Myrmecophaga): termite and ant eaters with a long tongue.
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24, 9)
bio.label(ax, (0.4, 8.3), "Marsupials", size="normal", bold=True, ha="left", color=P.edge("mrna"))
bio.label(ax, (0.4, 4.4), "Placentals", size="normal", bold=True, ha="left", color=P.edge("dna"))
pairs = [("phylopic/thylacine", "phylopic/wolf", "cursorial carnivore", "thylacine", "grey wolf"),
         ("phylopic/sugar-glider", "phylopic/flying-squirrel", "glider", "sugar glider", "flying squirrel"),
         ("phylopic/marsupial-mole", "phylopic/mole", "burrower", "marsupial mole", "mole"),
         ("phylopic/numbat", "phylopic/anteater", "ant and termite eater", "numbat", "giant anteater")]
for i, (_m, _p, role, mn, pn) in enumerate(pairs):
    x = 5.0 + 5.2 * i
    bio.label(ax, (x, 0.5), role, size="small", bold=True)
    bio.label(ax, (x, 5.0), mn, size="tiny", italic=False)
    bio.label(ax, (x, 1.1), pn, size="tiny")
    bio.arrow(ax, (x, 4.6), (x, 3.6), kind="link", dashed=True)

bio.icon(ax, "phylopic/thylacine", at=(5.0, 6.4), height=1.5, color="mrna")
bio.icon(ax, "phylopic/sugar-glider", at=(10.2, 6.4), height=1.6, color="mrna")
bio.icon(ax, "phylopic/marsupial-mole", at=(15.4, 6.4), height=0.9, color="mrna")
bio.icon(ax, "phylopic/numbat", at=(20.6, 6.4), height=1.2, color="mrna")
bio.icon(ax, "phylopic/wolf", at=(5.0, 2.4), height=1.6, color="dna")
bio.icon(ax, "phylopic/flying-squirrel", at=(10.2, 2.4), height=1.5, color="dna")
bio.icon(ax, "phylopic/mole", at=(15.4, 2.4), height=3.2, rotate=90, color="dna")
bio.icon(ax, "phylopic/anteater", at=(20.6, 2.4), height=1.3, color="dna")
