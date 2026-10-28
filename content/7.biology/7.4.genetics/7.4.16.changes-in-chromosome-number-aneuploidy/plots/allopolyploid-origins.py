"""Allopolyploidy. A: the origin of bread wheat by two rounds of interspecific hybridization and genome
doubling (approximate dates). B: the triangle of U (1935): three diploid Brassica species and the three
allotetraploids formed from each pair, with their genomes and chromosome numbers."""
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30, 9.2)
bio.panel(ax, "A", (0.2, 8.8))
B = dict(w=4.4, h=1.1)
def node(xy, top, sub, tok):
    bio.box(ax, xy, B["w"], B["h"], token=tok)
    bio.label(ax, (xy[0], xy[1] + 0.2), top, size="small", italic=True, color=P.on_fill(), zorder=12)
    bio.label(ax, (xy[0], xy[1] - 0.25), sub, size="tiny", color=P.on_fill(), zorder=12)
node((2.8, 7.2), "Triticum urartu", "AA, 2n = 14", "plant")
node((8.0, 7.2), "Aegilops speltoides relative", "BB, 2n = 14", "enzyme")
node((5.4, 4.6), "Triticum turgidum", "AABB, 2n = 4x = 28 (emmer, durum)", "highlight")
node((10.6, 4.6), "Aegilops tauschii", "DD, 2n = 14", "dna")
node((8.0, 2.0), "Triticum aestivum", "AABBDD, 2n = 6x = 42 (bread wheat)", "antibody")
for a, b in (((2.8, 6.6), (5.0, 5.2)), ((8.0, 6.6), (5.8, 5.2)), ((5.4, 4.0), (7.6, 2.6)), ((10.6, 4.0), (8.4, 2.6))):
    bio.arrow(ax, a, b, kind="process", head=0.16)
bio.label(ax, (8.6, 5.9), "hybrid, doubling", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (8.6, 5.55), "about 0.5 million years ago", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (10.3, 3.25), "hybrid, doubling", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (10.3, 2.9), "about 10 000 years ago, in cultivation", size="tiny", color=P.muted(), ha="left")
bio.panel(ax, "B", (15.0, 8.8))
cx = {"A": (17.4, 1.3), "B": (27.4, 1.3), "C": (22.4, 7.9)}
dip = {"A": ("Brassica rapa", "AA, 2n = 20", "plant"), "B": ("Brassica nigra", "BB, 2n = 16", "dna"),
       "C": ("Brassica oleracea", "CC, 2n = 18", "receptor")}
for k, (xy) in cx.items():
    nm, sub, tok = dip[k]
    node(xy, nm, sub, tok)
tet = [("A", "B", "Brassica juncea", "AABB, 2n = 36"), ("A", "C", "Brassica napus", "AACC, 2n = 38"),
       ("B", "C", "Brassica carinata", "BBCC, 2n = 34")]
for a, b, nm, sub in tet:
    (x1, y1), (x2, y2) = cx[a], cx[b]
    m = ((x1 + x2) / 2, (y1 + y2) / 2)
    ax.plot([x1, x2], [y1, y2], color=P.muted(), lw=0.9, zorder=2)
    bio.box(ax, m, 4.0, 1.0, token="neutral")
    bio.label(ax, (m[0], m[1] + 0.18), nm, size="small", italic=True, color=P.on_fill(), zorder=12)
    bio.label(ax, (m[0], m[1] - 0.24), sub, size="tiny", color=P.on_fill(), zorder=12)
