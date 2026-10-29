"""The gene regulatory network of the neural crest (SBGN activity flow, simplified after Simões-Costa and Bronner
2015). Signals at the neural plate border (intermediate BMP, Wnt, FGF, Notch) induce the neural plate border
specifiers; these activate the neural crest specifiers, which in turn control the effector genes of
delamination and migration (Snai2 represses E-cadherin, the cadherin switch to cadherin-6B and -7, RhoB, matrix
metalloproteases) and maintain multipotency. Differentiation genes downstream of Sox10 and other specifiers then
select particular fates. Arrows: activation; bars: repression."""
import wikibio as bio
from wikibio import network

fig, ax = bio.canvas(23, 11.6)
P = bio.P
d = network.Diagram(ax, size="small")
tiers = [
    ("Signals", 10.4, [("bmp", "BMP (intermediate)"), ("wnt", "Wnt"), ("fgf", "FGF"), ("notch", "Notch")], "neutral", False),
    ("Border specifiers", 8.2, [("pax", "Pax3/7"), ("msx", "Msx1"), ("zic", "Zic1"), ("tfap", "Tfap2a"), ("gbx", "Gbx2"), ("dlx", "Dlx5")], "protein", True),
    ("Crest specifiers", 6.0, [("snai", "Snai2"), ("foxd", "FoxD3"), ("sox9", "Sox9"), ("sox10", "Sox10"), ("ets", "Ets1"), ("twist", "Twist1")], "cl", True),
    ("Effectors", 3.8, [("ecad", "E-cadherin"), ("cad6", "Cad6B, Cad7"), ("rhob", "RhoB"), ("mmp", "MMPs")], "receptor", True),
    ("Fates", 1.4, [("mitf", "Mitf: melanocyte"), ("phox", "Phox2b: autonomic neuron"), ("erbb", "ErbB3: glia"), ("runx", "Runx2: bone")], "antibody", False),
]
for name, y, nodes, tok, ital in tiers:
    bio.label(ax, (0.3, y), name, size="small", bold=True, ha="left")
    n = len(nodes)
    for k, (nid, text) in enumerate(nodes):
        x = 6.4 + k * (14.4 / (n - 1)) if n > 1 else 14.0
        d.activity(nid, (x, y), text, token=tok, italic=ital and ":" not in text)
for a, b in (("bmp", "pax"), ("wnt", "zic"), ("wnt", "msx"), ("fgf", "pax"), ("notch", "dlx"), ("bmp", "tfap"), ("wnt", "gbx")):
    d.connect(a, b, kind="positive")
for a, b in (("pax", "snai"), ("zic", "foxd"), ("msx", "sox9"), ("tfap", "sox10"), ("pax", "sox10"), ("gbx", "ets"), ("dlx", "twist"),
             ("tfap", "sox9")):
    d.connect(a, b, kind="positive")
d.connect("snai", "ecad", kind="negative")
for a, b in (("sox9", "cad6"), ("foxd", "cad6"), ("snai", "rhob"), ("ets", "mmp")):
    d.connect(a, b, kind="positive")
for a, b in (("sox10", "mitf"), ("sox10", "phox"), ("sox10", "erbb"), ("twist", "runx"), ("sox9", "runx")):
    d.connect(a, b, kind="positive", bend=0.05)
