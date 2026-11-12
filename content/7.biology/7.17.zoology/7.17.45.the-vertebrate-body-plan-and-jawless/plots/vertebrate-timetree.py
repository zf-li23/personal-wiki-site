# Time tree of the jawless vertebrates and the gnathostome stem (topology after Pough et al., Vertebrate
# Life, 11th ed., Fig. 3.4). Extinct lineages end at their last occurrence; node ages are approximate
# (rounded to 5-10 Myr) and the order of the stem lineages above conodonts is debated.
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("((Hagfishes:470,Lampreys:470)Cyclostomata:65,"
          "(Conodonts:324,(Pteraspidomorphs:141,(Anaspids:108,(Thelodonts:98,(Galeaspids:88,"
          "(Osteostracans:78,Gnathostomes:450)X:10)G:10)T:10)A:20)B:25)Bone:10)Vertebrata;")
ICONS = {"Hagfishes": ("phylopic/hagfish", {"rotate": 90}), "Lampreys": "phylopic/lamprey",
         "Osteostracans": "phylopic/osteostracan", "Gnathostomes": "phylopic/great-white-shark"}
TEXT = {"Pteraspidomorphs": "Pteraspidomorphs (arandaspids, heterostracans)", "Gnathostomes": "Gnathostomata (jawed vertebrates)"}

fig, ax = bio.canvas(24, 13)
t = phylo.tree(ax, NEWICK, origin=(0.6, 2.4), width=14.5, height=9.6, scaled=True, span=545, root_edge=10,
               icons=ICONS, icon_size=0.6, icon_width=1.4, icon_color="animal", label_size="small", tip_text=TEXT,
               clades=[dict(node="Cyclostomata", token="dna", style="band", label="Cyclostomata")],
               marks=[dict(node="B", kind="trait", text="dermal bone", token="positive", at=0.5),
                      dict(node="X", kind="trait", text="paired fins, cellular bone", token="positive",
                           at=0.5, text_size="tiny", side=1, offset=0.5, va="bottom", ha="left")])
t.time_lines(ax, [443.8, 372.2, 201.4], ["End-Ordovician", "Late Devonian", "End-Triassic"], y0=1.3,
             y1=t.frame[1] + t.frame[3] + 0.25)
t.time_axis(ax, ticks=[500, 400, 300, 200, 100, 0], minor=list(range(450, 0, -100)), y=2.0)
t.geo_scale(ax, y=1.3, ranks=("era", "period"), height=0.42)
bio.label(ax, (23.6, 0.35), "Ages approximate; extinct lineages end at their last occurrence", size="tiny",
          color=P.muted(), ha="right")
