# Subfamilies of Rosaceae (after Potter et al. 2007 and Xiang et al. 2017, simplified to tribes) and the four
# traditional subfamilies. Rosoideae diverge first; Dryadoideae and Amygdaloideae are sisters. Branch colours
# mark the traditional groups: Spiraeoideae (paraphyletic, several tribes of Amygdaloideae), Rosoideae
# (Kerria moved to Amygdaloideae), Maloideae (= tribe Maleae) and Prunoideae (= tribe Amygdaleae).
import wikibio as bio
from wikibio import phylo

NEWICK = ("((Rubeae,(Roseae,(Potentilleae,(Sanguisorbeae,Geeae))))Rosoideae,"
          "(Dryadoideae,(Lyonothamneae,((Neillieae,(Amygdaleae,Kerrieae)),((Exochordeae,Sorbarieae),"
          "(Spiraeeae,Maleae)))))Amygdaloideae)Rosaceae;")
fig, ax = bio.canvas(30, 14)
tips = {"Rubeae": r"Rubeae ($\it{Rubus}$)", "Roseae": r"Roseae ($\it{Rosa}$)", "Potentilleae": r"Potentilleae ($\it{Potentilla}$, $\it{Fragaria}$)",
        "Sanguisorbeae": r"Sanguisorbeae ($\it{Sanguisorba}$)", "Geeae": r"Colurieae ($\it{Geum}$)",
        "Dryadoideae": r"Dryadoideae ($\it{Dryas}$)", "Lyonothamneae": r"Lyonothamneae",
        "Neillieae": r"Neillieae ($\it{Neillia}$, $\it{Stephanandra}$)", "Amygdaleae": r"Amygdaleae ($\it{Prunus}$)",
        "Kerrieae": r"Kerrieae ($\it{Kerria}$)", "Exochordeae": r"Exochordeae ($\it{Exochorda}$)",
        "Sorbarieae": r"Sorbarieae ($\it{Sorbaria}$)", "Spiraeeae": r"Spiraeeae ($\it{Spiraea}$)",
        "Maleae": r"Maleae ($\it{Malus}$, $\it{Pyrus}$, $\it{Crataegus}$)"}
SPIR = ["Neillieae", "Exochordeae", "Sorbarieae", "Spiraeeae", "Lyonothamneae"]
t = phylo.tree(ax, NEWICK, origin=(0.8, 0.6), width=9.5, height=12.4, label_size="small", root_edge=0.4,
               tip_text=tips,
               clades=[dict(node="Rosoideae", token="plant", style="bar", label="Rosoideae"),
                       dict(tips=["Dryadoideae"], token="neutral", style="bar", label="Dryadoideae"),
                       dict(node="Amygdaloideae", token="petal", style="bar", label="Amygdaloideae"),
                       dict(node="Rosoideae", token="plant", style="branch"),
                       dict(tips=["Kerrieae"], token="plant", style="branch"),
                       dict(tips=["Dryadoideae"], token="plant", style="branch"),
                       dict(tips=["Maleae"], token="dna", style="branch"),
                       dict(tips=["Amygdaleae"], token="rna", style="branch")]
               + [dict(tips=[s], token="anther", style="branch") for s in SPIR])
LEG = [("plant", "Traditional Rosoideae"), ("anther", "Traditional Spiraeoideae"),
       ("dna", "Traditional Maloideae"), ("rna", "Traditional Prunoideae")]
for i, (tok, txt) in enumerate(LEG):
    phylo.marker(ax, (22.5, 4.0 - i * 0.8), "line", tok)
    bio.label(ax, (23.1, 4.0 - i * 0.8), txt, size="small", ha="left")
bio.icon(ax, "phylopic/rosaceae", at=(26.5, 11.5), height=3.0, color="petal")
