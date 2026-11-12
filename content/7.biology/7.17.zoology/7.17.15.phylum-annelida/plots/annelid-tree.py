# Phylogeny of the Annelida (simplified; after Weigert et al. 2014, Struck et al. 2015, Helm et al. 2018 and
# Brusca et al. 2023). Numbered bars mark gains, crossed bars losses; grey dots mark nodes whose position
# differs among phylogenomic analyses. Approximate numbers of described species in parentheses.
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("((Oweniidae,Magelonidae)Oweniida,(Chaetopteridae,((Amphinomida,Sipuncula)AmSi,"
          "((Phyllodocida,Eunicida)Errantia,((Sabellida,Siboglinidae)SabSib,(Terebelliformia,"
          "((Capitellidae,Thalassematidae)CapTh,(Oligochaetes,Hirudinea)Clitellata)CC)TCC)Sedentaria)"
          "Pleistoannelida)P2)P1)Annelida;")
TEXT = {"Oweniidae": "Oweniidae (~50)", "Magelonidae": "Magelonidae (~70)", "Chaetopteridae": "Chaetopteridae (~70)",
        "Amphinomida": "Amphinomida: fireworms (~200)", "Sipuncula": "Sipuncula: peanut worms (~150)",
        "Phyllodocida": "Phyllodocida: ragworms, scale worms (~4,500)", "Eunicida": "Eunicida: bobbit and palolo worms (~1,000)",
        "Sabellida": "Sabellida: fan worms, serpulids (~1,300)",
        "Siboglinidae": "Siboglinidae: beard and vent tube worms (~200)",
        "Terebelliformia": "Terebelliformia: spaghetti worms (~1,000)",
        "Capitellidae": "Capitellidae (~200)", "Thalassematidae": "Thalassematidae: spoon worms (~160)",
        "Oligochaetes": "'Oligochaetes': earthworms and kin (~5,000)", "Hirudinea": "Hirudinea: leeches (~900)"}
ICONS = {"Phyllodocida": "phylopic/ragworm", "Sipuncula": "phylopic/peanut-worm", "Siboglinidae": "phylopic/tubeworm",
         "Thalassematidae": "phylopic/spoon-worm", "Oligochaetes": "phylopic/earthworm", "Hirudinea": "phylopic/leech"}
GAINS = [("Annelida", "Segments added from a posterior growth zone; chaetae; head of prostomium and peristomium"),
         ("Errantia", "Well-developed parapodia with aciculae; jaws in many"),
         ("Clitellata", "Clitellum and cocoon; hermaphroditism; direct development; parapodia lost"),
         ("Hirudinea", "Fixed number of segments (about 32-34); suckers; coelom reduced to channels; chaetae lost (most)")]
LOSSES = [("Sipuncula", "Segmentation and chaetae lost in the adult"),
          ("Thalassematidae", "Segmentation lost in the adult"),
          ("Siboglinidae", "Gut lost in the adult (chemosymbiotic trophosome)")]
MARKS = [dict(node=n, kind="trait", text=str(k + 1), at=0.5, text_size="tiny", side=-1, offset=0.3, va="bottom")
         for k, (n, _) in enumerate(GAINS)]
MARKS += [dict(node=n, kind="loss", text=chr(97 + k), at=0.5, text_size="tiny", side=-1, offset=0.3, va="bottom")
          for k, (n, _) in enumerate(LOSSES)]
MARKS += [dict(node=n, kind="dot", token="neutral", at=1.0, size=0.3) for n in ("AmSi", "SabSib", "TCC", "CC")]

fig, ax = bio.canvas(23.0, 16.0)
phylo.tree(ax, NEWICK, origin=(0.8, 6.0), width=9.0, height=9.4, root_edge=0.8, tip_text=TEXT, icons=ICONS,
           icon_size=0.7, icon_width=1.2, label_size="small",
           clades=[dict(node="Errantia", token="dna", style="bar", label="Errantia"),
                   dict(node="Sedentaria", token="bone", style="bar", label="Sedentaria"),
                   dict(node="Clitellata", token="positive", style="bar", label="Clitellata")],
           marks=MARKS)
y = 5.0
for k, (_, txt) in enumerate(GAINS):
    phylo.marker(ax, (1.0, y), "trait", direction=(1, 0))
    bio.label(ax, (1.4, y), f"{k + 1}  {txt}", size="small", ha="left")
    y -= 0.6
for k, (_, txt) in enumerate(LOSSES):
    phylo.marker(ax, (1.0, y), "loss", direction=(1, 0))
    bio.label(ax, (1.4, y), f"{chr(97 + k)}  {txt}", size="small", ha="left")
    y -= 0.6
phylo.marker(ax, (1.0, y), "dot", token="neutral", size=0.3)
bio.label(ax, (1.4, y), "Position differs among phylogenomic analyses", size="small", ha="left")
