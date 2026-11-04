# Sensing of viral nucleic acid, induction of interferon, and the antiviral state in the neighbour cell.
# Red bars mark documented viral antagonists.
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(19.0, 10.4)
RED = P.edge("negative")

bio.label(ax, (9.5, 10.15), "Detection of viral nucleic acid, interferon and the antiviral state",
          size="title", bold=True)

# ---------------------------------------------------------------- the infected cell
bio.box(ax, (5.4, 5.1), 10.2, 8.8, token="cytoplasm", radius=0.6)
bio.label(ax, (1.1, 9.15), "Infected cell", size="small", bold=True, ha="left")


def unit(center, w, h, token, title, sub=None, size="small"):
    bio.box(ax, center, w, h, token=token, radius=0.18)
    bio.label(ax, (center[0], center[1] + (0.30 if sub else 0)), title, size=size, bold=True,
              color=P.on_fill())
    if sub:
        bio.label(ax, (center[0], center[1] - 0.30), sub, size="tiny", color=P.on_fill())


unit((2.1, 8.1), 3.3, 1.3, "lysosome", "TLR3, TLR7/8, TLR9", "endosome:\ndsRNA, ssRNA, CpG DNA")
unit((5.7, 8.1), 3.1, 1.3, "enzyme", "RIG-I, MDA5", "cytoplasm:\ndsRNA, 5′-PPP RNA")
unit((8.9, 8.1), 2.4, 1.3, "receptor", "cGAS", "cytoplasm:\ndsDNA")

unit((2.1, 6.4), 3.1, 0.8, "protein", "MyD88 / TRIF")
unit((5.6, 6.4), 3.0, 0.8, "mitochondrion", "MAVS filament")
unit((8.9, 6.4), 2.4, 0.8, "er", "STING (ER)")
bio.label(ax, (8.2, 7.15), "2′3′-cGAMP", size="tiny", color=P.muted())

unit((5.4, 4.8), 4.0, 0.8, "protein", "TBK1 and IKK kinases")
unit((3.6, 3.4), 2.6, 0.8, "dna2", "IRF3")
unit((7.2, 3.4), 2.6, 0.8, "dna2", "NF-κB")

bio.box(ax, (5.1, 1.75), 4.4, 1.05, token="nucleus", radius=0.2)
bio.label(ax, (5.1, 1.95), "Nucleus", size="small", bold=True)
bio.label(ax, (5.1, 1.52), "IFN-β and IFN-λ genes transcribed", size="tiny", color=P.muted())

for a, b in (((2.1, 7.45), (2.1, 6.8)), ((5.7, 7.45), (5.7, 6.8)), ((8.9, 7.45), (8.9, 6.8)),
             ((2.1, 6.0), (4.4, 5.2)), ((5.7, 6.0), (5.5, 5.2)), ((8.9, 6.0), (6.6, 5.2)),
             ((4.8, 4.4), (3.9, 3.8)), ((6.0, 4.4), (6.9, 3.8)),
             ((3.8, 3.0), (4.3, 2.4)), ((7.0, 3.0), (6.5, 2.4))):
    bio.arrow(ax, a, b, kind="process")

# viral antagonists
for (x, y), text in (((7.15, 8.1), "influenza NS1\nsequesters dsRNA"),
                     ((10.2, 6.4), "Zika NS2B3\ncleaves STING"),
                     ((2.3, 3.4), "many viruses\ndegrade IRF3")):
    bio.label(ax, (x + (0.0 if x < 9 else 0.0), y + 0.95), text, size="tiny", color=RED)
bio.arrow(ax, (7.15, 8.75), (6.6, 8.35), kind="inhibition", color=RED)
bio.arrow(ax, (10.2, 7.1), (9.6, 6.6), kind="inhibition", color=RED)
bio.arrow(ax, (2.3, 4.1), (3.0, 3.6), kind="inhibition", color=RED)

# ---------------------------------------------------------------- interferon
bio.molecule(ax, (11.0, 2.6), token="metabolite", text="IFN", r=0.34, size="tiny")
bio.molecule(ax, (11.6, 3.5), token="metabolite", text="IFN", r=0.28, size="tiny")
bio.arrow(ax, (7.4, 1.75), (10.5, 2.3), kind="process", bend=-0.10)
bio.label(ax, (9.4, 0.95), "type I (IFN-α/β) and type III (IFN-λ)\nsecreted", size="tiny", color=P.muted())

# ---------------------------------------------------------------- the neighbouring cell
bio.box(ax, (15.4, 5.1), 6.6, 8.8, token="cytoplasm", radius=0.6)
bio.label(ax, (12.4, 9.15), "Neighbouring cell", size="small", bold=True, ha="left")
bio.receptor(ax, 15.3, 8.2, kind="rtk", token="receptor", text=None)
bio.label(ax, (16.9, 8.2), "IFNAR / IFNLR", size="small", bold=True)
unit((15.3, 6.3), 4.6, 0.8, "enzyme", "JAK1, TYK2 → STAT1/2, IRF9")
unit((15.3, 4.9), 4.6, 0.8, "dna2", "ISGs transcribed")
bio.box(ax, (15.3, 2.75), 5.6, 2.0, token="positive", radius=0.18)
bio.label(ax, (15.3, 3.45), "The antiviral state", size="small", bold=True, color=P.on_fill())
bio.label(ax, (15.3, 2.95), "PKR → eIF2α: translation off", size="tiny", color=P.on_fill())
bio.label(ax, (15.3, 2.55), "OAS → RNase L: RNA degraded", size="tiny", color=P.on_fill())
bio.label(ax, (15.3, 2.15), "restriction factors, more sensors", size="tiny", color=P.on_fill())
bio.arrow(ax, (15.3, 7.5), (15.3, 6.8), kind="process")
bio.arrow(ax, (15.3, 5.9), (15.3, 5.4), kind="process")
bio.arrow(ax, (15.3, 4.5), (15.3, 3.85), kind="process")
bio.arrow(ax, (11.9, 3.9), (14.4, 8.0), kind="process", bend=0.16)

bio.label(ax, (18.0, 7.3), "blocked by decoy\nreceptors and by\nblocks on STAT\nimport", size="tiny", color=RED)
bio.arrow(ax, (18.0, 6.6), (17.7, 6.3), kind="inhibition", color=RED)

bio.label(ax, (9.5, 0.35), "the infected cell both defends itself and warns its neighbours; every vertebrate virus "
                           "antagonizes some step of this pathway", size="tiny", color=P.muted())
