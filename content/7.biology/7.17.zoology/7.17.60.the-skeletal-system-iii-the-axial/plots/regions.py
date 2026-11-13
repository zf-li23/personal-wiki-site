# Regions of the vertebral column in six tetrapods, one block per vertebra, anterior to the left, coloured by region;
# fused groups outlined together. Counts: frog 1 cervical, 7 trunk, 1 sacral, urostyle; lizard (lacertid) 8 C,
# 18 dorsal, 2 S, ~40 caudal; crocodile 9 C, 10 T, 5 L, 2 S, ~35 Cd; chicken 14 C, 7 T, ~14 in synsacrum, 6 Cd +
# pygostyle; rabbit 7 C, 12 T, 7 L, 4 S, 16 Cd; human 7 C, 12 T, 5 L, 5 S, 4 Cd (Kardong 2019; veterinary anatomy).
import wikibio as bio

P = bio.P
REG = {"C": ("cervical", "dna"), "T": ("thoracic / dorsal", "mrna"), "L": ("lumbar", "positive"),
       "S": ("sacral, synsacrum", "highlight"), "Cd": ("caudal", "neutral"), "F": ("fused tail (urostyle, pygostyle, coccyx)", "protein")}
animals = [
    ("Frog", [("C", 1), ("T", 7), ("S", 1), ("F", 1)]),
    ("Lizard", [("C", 8), ("T", 18), ("S", 2), ("Cd", 40)]),
    ("Crocodile", [("C", 9), ("T", 10), ("L", 5), ("S", 2), ("Cd", 35)]),
    ("Chicken", [("C", 14), ("T", 7), ("S", 14), ("Cd", 6), ("F", 1)]),
    ("Rabbit", [("C", 7), ("T", 12), ("L", 7), ("S", 4), ("Cd", 16)]),
    ("Human", [("C", 7), ("T", 12), ("L", 5), ("S", 5), ("F", 1)]),
]
bw = 0.3
fig, ax = bio.canvas(30, len(animals) * 1.1 + 2.0)
for i, (name, regs) in enumerate(animals):
    y = len(animals) * 1.1 - i * 1.1 + 0.6
    bio.label(ax, (0.2, y + 0.3), name, size="small", bold=True, ha="left")
    x = 3.0
    for r, n in regs:
        tok = REG[r][1]
        fused = r in ("S", "F") and (n > 1 or r == "F") and not (name in ("Frog",) and r == "S")
        w = bw * (n if r != "F" else 3)
        if fused:
            bio.shape(ax, [(x, y), (x + w - 0.04, y), (x + w - 0.04, y + 0.6), (x, y + 0.6)], token=tok, lw=1.2)
        else:
            for k in range(n):
                xx = x + k * bw
                bio.shape(ax, [(xx, y), (xx + bw - 0.04, y), (xx + bw - 0.04, y + 0.6), (xx, y + 0.6)], token=tok, lw=0.5)
        if r in ("C", "T", "L", "S") or (r == "Cd" and n < 10):
            bio.label(ax, (x + w / 2, y - 0.2), str(n), size="tiny", color=P.muted())
        x += w + 0.05
for j, (k, (lab, tok)) in enumerate(REG.items()):
    xx = 3.0 + j * 4.5
    bio.shape(ax, [(xx, 0.2), (xx + 0.4, 0.2), (xx + 0.4, 0.55), (xx, 0.55)], token=tok, lw=0.5)
    bio.label(ax, (xx + 0.55, 0.37), lab, size="tiny", ha="left")
