# Relationships of the main groups of synapsids (cladogram, simplified after Kemp 2005, Benson 2012, Luo
# 2007 and Pough et al. 2023), with the stepwise acquisition of mammalian characters (bars). "Pelycosaurs"
# (caseasaurs, ophiacodontids, edaphosaurids, sphenacodontids) form a paraphyletic grade at the base;
# therapsids, cynodonts and mammaliaforms are successively more exclusive clades. Daggers mark extinct groups.
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(Caseasauria,(Ophiacodontidae,(Edaphosauridae,(Sphenacodontidae,(Biarmosuchia,(Dinocephalia,"
          "(Anomodontia,(Gorgonopsia,(Therocephalia,(Thrinaxodon,(Cynognathia,(Tritylodontidae,"
          "(Morganucodon,(Docodonta,(Hadrocodium,Mammalia)))Mammaliaformes)Probainognathia)Eucynodontia)"
          "Cynodontia)Eutheriodontia)Theriodontia)Neotherapsida)Eutherapsida)Therapsida)Sphenacodontia)"
          "Sphenacomorpha)Eupelycosauria)Synapsida;")
TEXT = {k: "†" + k for k in ["Caseasauria", "Ophiacodontidae", "Edaphosauridae", "Sphenacodontidae",
                                     "Biarmosuchia", "Dinocephalia", "Anomodontia", "Gorgonopsia",
                                     "Therocephalia", "Thrinaxodon", "Cynognathia", "Tritylodontidae",
                                     "Morganucodon", "Docodonta", "Hadrocodium"]}
TEXT.update({"Sphenacodontidae": "†Sphenacodontidae (Dimetrodon)",
             "Anomodontia": "†Anomodontia (dicynodonts, Lystrosaurus)",
             "Mammalia": "Mammalia (crown)"})
ICONS = {"Sphenacodontidae": "phylopic/dimetrodon", "Anomodontia": "phylopic/dicynodont",
         "Gorgonopsia": "phylopic/gorgonopsian", "Thrinaxodon": "phylopic/thrinaxodon",
         "Morganucodon": "phylopic/morganucodon", "Mammalia": "phylopic/opossum"}
MARKS = [dict(node="Synapsida", kind="trait", text="lower temporal fenestra", at=0.5),
         dict(node="Sphenacodontia", kind="trait", text="canine-like teeth, reflected lamina", at=0.5),
         dict(node="Therapsida", kind="trait", text="larger fenestra, erect hindlimb", at=0.5),
         dict(node="Cynodontia", kind="trait", text="secondary palate, enlarged dentary, turbinate ridges", at=0.5),
         dict(node="Probainognathia", kind="trait", text="double occipital condyle, no lumbar ribs", at=0.5),
         dict(node="Mammaliaformes", kind="trait", text="dentary-squamosal joint, diphyodonty", at=0.5),
         dict(node="Mammalia", kind="trait", text="definitive middle ear (in stages)", at=0.5)]
KEY = []
for i, m in enumerate(MARKS, 1):
    KEY.append(f"{i}  {m['text']}")
    m.update(text=str(i), text_size="tiny", side=1, offset=0.25, va="top")
fig, ax = bio.canvas(24, 13)
phylo.tree(ax, NEWICK, origin=(3.0, 0.9), width=9.5, height=11.4, root_edge=0.4, icons=ICONS, icon_size=0.55,
           icon_width=1.3, icon_color="animal", label_size="small", tip_text=TEXT, layout="slanted",
           marks=MARKS)
for i, t in enumerate(KEY):
    bio.label(ax, (0.6, 12.3 - 0.5 * i), t, size="tiny", ha="left")
bio.label(ax, (0.6, 0.3), "Cladogram; \u2020 extinct; numbered bars mark the characters listed", size="tiny",
          color=P.muted(), ha="left")
