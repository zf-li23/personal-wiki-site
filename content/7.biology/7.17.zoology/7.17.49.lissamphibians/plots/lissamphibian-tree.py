# Relationships of the three orders of living amphibians (Batrachia hypothesis) with key fossils and the
# derived characters of each node; topology after molecular phylogenies (e.g. Jetz & Pyron 2018) and
# fossil analyses (Kligman et al. 2023). Species numbers are rounded counts from AmphibiaWeb (2025).
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(Dissorophoid_temnospondyls,(('Eocaecilia (Jurassic)','Gymnophiona (caecilians)')G,"
          "(('Triassurus (Triassic)','Caudata (salamanders)')C,('Triadobatrachus (Triassic)','Anura (frogs)')A)"
          "Batrachia)Lissamphibia);")
TEXT = {"Dissorophoid temnospondyls": "Dissorophoid temnospondyls (e.g. Gerobatrachus)",
        "Gymnophiona (caecilians)": "Gymnophiona, caecilians (~220)",
        "Caudata (salamanders)": "Caudata, salamanders (~830)",
        "Anura (frogs)": "Anura, frogs and toads (~7 800)"}
ICONS = {"Gymnophiona (caecilians)": "phylopic/caecilian", "Caudata (salamanders)": "phylopic/salamander",
         "Anura (frogs)": "phylopic/frog"}
MARKS = [dict(node="Lissamphibia", kind="trait", text="pedicellate teeth, glandular skin, papilla amphibiorum",
              at=0.5, text_size="tiny", side=1, offset=0.3, va="bottom"),
         dict(node="Gymnophiona (caecilians)", kind="trait", text="limbless, tentacle, annuli", at=0.4,
              text_size="tiny", side=1, offset=0.3, va="bottom"),
         dict(node="Caudata (salamanders)", kind="trait", text="tail, similar fore- and hindlimbs", at=0.4,
              text_size="tiny", side=1, offset=0.3, va="bottom"),
         dict(node="Anura (frogs)", kind="trait", text="urostyle, long hindlimbs, no tail", at=0.4,
              text_size="tiny", side=1, offset=0.3, va="bottom")]
fig, ax = bio.canvas(22, 9)
t = phylo.tree(ax, NEWICK, origin=(0.6, 1.0), width=10.0, height=7.0, root_edge=0.5, icons=ICONS,
               icon_size=0.6, icon_width=1.4, icon_color="animal", label_size="small", tip_text=TEXT,
               italic={"Eocaecilia (Jurassic)", "Triassurus (Triassic)", "Triadobatrachus (Triassic)"},
               clades=[dict(node="Lissamphibia", token="dna", style="band", label="Lissamphibia"),
                       dict(node="Batrachia", token="positive", style="bar", label="Batrachia")],
               marks=MARKS)
bio.label(ax, (0.6, 0.3), "Cladogram; italic: fossil stem members of each order", size="tiny", color=P.muted(),
          ha="left")
