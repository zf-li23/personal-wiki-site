# Relationships of the eleven holometabolous orders, following phylogenomic studies (Misof et al. 2014;
# Peters et al. 2014; McKenna et al. 2019), with fleas shown in their usual placement as sister to
# Mecoptera (some analyses nest them within Mecoptera, near Nannochoristidae). Approximate species numbers.
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(24, 11.5)
nwk = ("(Hymenoptera_115000,(((Raphidioptera_260,(Megaloptera_380,Neuroptera_6000))Neuropterida,"
       "(Coleoptera_390000,Strepsiptera_600)Coleopterida)Neuropteroidea,"
       "(((Mecoptera_700,Siphonaptera_2600),Diptera_160000)Antliophora,"
       "(Trichoptera_16000,Lepidoptera_160000)Amphiesmenoptera)Mecopterida)Aparaglossata)Holometabola;")
nwk = nwk.replace("_", " ")
t = phylo.tree(ax, nwk, origin=(0.6, 0.8), width=14.5, height=9.8, label_size="normal", root_edge=1.0,
               clades=[dict(node="Neuropterida", token="enzyme", style="bar", label="Neuropterida"),
                       dict(node="Coleopterida", token="protein", style="bar", label="Coleopterida"),
                       dict(node="Antliophora", token="channel", style="bar", label="Antliophora"),
                       dict(node="Amphiesmenoptera", token="positive", style="bar", label="Amphiesmenoptera")],
               marks=[dict(node="Holometabola", kind="trait", text="pupa; larval wing\nbuds internal", at=0.5,
                           token="positive"),
                      dict(node="Coleopterida", kind="trait", text="hind wings drive flight", at=0.55, token="positive"),
                      dict(node="Antliophora", kind="trait", text="male sperm pump", at=0.5, token="positive"),
                      dict(node="Amphiesmenoptera", kind="trait", text="hairy wings; ZW females;\nlarval silk from labium",
                           at=0.5, token="positive")])
bio.label(ax, (23.6, 11.1), "Cladogram; approximate species numbers", size="tiny", color=P.muted(), ha="right")
