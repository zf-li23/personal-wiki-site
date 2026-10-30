"""Induction of cardiogenic mesoderm and the core cardiac gene regulatory network (SBGN activity flow,
simplified). A: in the anterior lateral plate mesoderm, BMP2 from the endoderm (and lateral mesoderm) and FGF8
from the endoderm promote heart fates; Wnt3a and Wnt8 from the neural tube and posterior tissues inhibit heart and
favour blood, and the anterior endoderm relieves this inhibition by secreting the Wnt antagonists Dkk1, Cerberus
and Crescent; Noggin and Chordin from the notochord block BMP near the midline. Heart forms where BMP is present
and Wnt is absent. B: Mesp1 marks the earliest cardiovascular progenitors; BMP and the absence of Wnt then
activate Nkx2-5, Gata4 and Tbx5 (first heart field) or Isl1 with Fgf8 and Tbx1 (second heart field), which
cross-activate one another and the genes of cardiomyocyte differentiation; Tbx5 and Tbx20 together with Hand1
and Hand2 subdivide the chambers."""
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(25, 10)
bio.panel(ax, "A", (0.2, 9.8))
bio.box(ax, (4.2, 8.4), 4.0, 1.0, "protein", "Neural tube: Wnt3a, Wnt8", size="small")
bio.box(ax, (9.6, 8.4), 3.8, 1.0, "drug", "Notochord: Noggin, Chordin", size="tiny")
bio.box(ax, (2.6, 4.2), 4.6, 1.2, "muscle", "Cardiogenic mesoderm", size="small")
bio.box(ax, (9.6, 4.2), 3.4, 1.2, "blood", "Blood, vessels", size="small")
bio.box(ax, (2.6, 1.4), 4.6, 1.3, "highlight", "Anterior endoderm:\nBMP2, FGF8; Dkk1,\nCerberus, Crescent", size="tiny")
bio.box(ax, (9.6, 1.4), 3.4, 1.0, "highlight", "Posterior endoderm", size="tiny")
bio.arrow(ax, (3.2, 7.9), (2.4, 4.85), kind="inhibition")
bio.arrow(ax, (5.4, 7.9), (9.0, 4.85), kind="activation")
bio.arrow(ax, (9.0, 7.9), (4.4, 4.85), kind="inhibition", dashed=True)
bio.arrow(ax, (2.0, 2.05), (2.0, 3.55), kind="activation")
bio.arrow(ax, (4.0, 2.05), (4.0, 7.85), kind="inhibition", bend=-0.12)
bio.label(ax, (6.2, 2.7), "Dkk1, Cer\nblock Wnt", size="tiny", color=P.muted())
bio.label(ax, (8.0, 6.3), "blocks BMP\nnear midline", size="tiny", color=P.muted())

bio.panel(ax, "B", (12.8, 9.8))
nodes = {"BMP": (14.4, 8.6), "Wnt": (17.0, 8.6), "Mesp1": (15.6, 7.0), "Nkx2-5": (14.2, 5.2), "Gata4": (16.8, 5.2), "Tbx5": (19.6, 6.8),
         "Isl1": (22.6, 6.8), "Tbx20": (19.6, 3.6), "Hand1/2": (22.6, 3.6), "Mef2c": (15.6, 3.2), "Myh6, Nppa,\nTnnt2": (15.6, 1.2),
         "Fgf8, Tbx1": (22.6, 8.6)}
gene = {"Mesp1", "Nkx2-5", "Gata4", "Tbx5", "Isl1", "Tbx20", "Hand1/2", "Mef2c", "Myh6, Nppa,\nTnnt2", "Fgf8, Tbx1"}
for k, xy in nodes.items():
    tk = "neutral" if k in ("BMP", "Wnt") else ("receptor" if k in ("Isl1", "Fgf8, Tbx1") else ("muscle" if k == "Tbx5" else "enzyme"))
    bio.box(ax, xy, 2.3 if "\n" in k or "," in k else 1.8, 0.9 if "\n" in k else 0.7, tk, k, size="tiny", italic=k in gene)
E = [("BMP", "Mesp1", "activation"), ("Wnt", "Mesp1", "inhibition"), ("Mesp1", "Nkx2-5", "activation"), ("Mesp1", "Gata4", "activation"),
     ("Mesp1", "Tbx5", "activation"), ("Mesp1", "Isl1", "activation"), ("BMP", "Nkx2-5", "activation"), ("Isl1", "Fgf8, Tbx1", "activation"),
     ("Tbx5", "Tbx20", "inhibition"), ("Isl1", "Hand1/2", "activation"), ("Nkx2-5", "Mef2c", "activation"), ("Gata4", "Mef2c", "activation"),
     ("Mef2c", "Myh6, Nppa,\nTnnt2", "activation"), ("Tbx5", "Gata4", "activation")]
for a, b, k in E:
    bio.arrow(ax, nodes[a], nodes[b], kind=k, shrink=0.55, bend=0.1 if (a, b) == ("Mesp1", "Isl1") else 0.0)
ax.plot(*zip((14.95, 5.2), (16.25, 5.2)), color=P.ink(), lw=1.2, zorder=14)
bio.label(ax, (15.5, 5.55), "mutual", size="tiny", color=P.muted())
bio.label(ax, (19.6, 7.75), "first field, LV", size="tiny", color=P.muted())
bio.label(ax, (22.6, 7.75), "second field", size="tiny", color=P.muted())
