# Relationships within Dictyoptera, simplified from phylogenomic studies (Inward, Beccaloni & Eggleton
# 2007; Evangelista et al. 2019; Bourguignon et al. 2015): termites (former order Isoptera) are the
# sister group of the wood-eating cockroach Cryptocercus and nested within the cockroaches, so that
# "cockroaches" without termites are paraphyletic. Marks give the characters gained along the branches.
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(24, 11.5)
nwk = ("(Mantodea,((Corydiidae,(Ectobiidae,Blaberidae)),(Blattidae,(Cryptocercidae,(Mastotermitidae,"
       "(Kalotermitidae,(Rhinotermitidae,Termitidae)))Termitoidae)Tutricablattae)Blattoidea)Blattodea)Dictyoptera;")
t = phylo.tree(ax, nwk, origin=(0.6, 0.8), width=15.5, height=9.8, label_size="normal", root_edge=1.2,
               clades=[dict(node="Termitoidae", token="enzyme", style=["band", "branch"], label="Termites"),
                       dict(node="Blattodea", token="positive", style="bar", label="Blattodea")],
               marks=[dict(node="Dictyoptera", kind="trait", text="ootheca; perforated\ntentorium", at=0.5, token="positive"),
                      dict(node="Mantodea", kind="trait", text="raptorial forelegs", token="positive", at=0.5),
                      dict(node="Tutricablattae", kind="trait", text="wood diet; gut flagellates;\nbiparental family groups",
                           token="positive", at=0.5),
                      dict(node="Termitoidae", kind="trait", text="eusociality; castes;\ndeciduous wings", token="highlight", at=0.5),
                      dict(node="Termitidae", kind="trait", text="loss of flagellates", token="negative", at=0.5)])
bio.label(ax, (23.6, 11.1), "Cladogram; branch lengths not to scale", size="tiny", color=P.muted(), ha="right")
