"""Three modes of transcriptional control by DNA-binding proteins (schematic, E. coli examples).
A: repression of the arg operon: the arginine repressor binds the operator only with its corepressor
   (arginine), so excess arginine switches the biosynthetic genes off.
B: induction of the lac operon: LacI binds the operator unless the inducer (allolactose) is bound to it.
C: positive control of the maltose operon malEFG: the activator MalT binds its activator-binding site
   only with maltose bound and then recruits RNA polymerase to a weak promoter.
Left column: without the small molecule; right column: with it."""

from matplotlib.patches import Circle, Ellipse

import wikibio as bio
from wikibio import genetics as G

P = bio.P
fig, ax = bio.canvas(24.0, 11.0)


def rnap(x, y):
    ax.add_patch(Ellipse((x, y), 1.5, 0.95, facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=1.1, zorder=14))
    bio.label(ax, (x, y), "RNAP", size="tiny", color=P.on_fill(), zorder=15)


def regulator(x, y, token, text, effector=None):
    ax.add_patch(Ellipse((x, y), 1.25, 0.8, facecolor=P.fill(token), edgecolor=P.edge(token), lw=1.1, zorder=14))
    bio.label(ax, (x, y), text, size="tiny", color=P.on_fill(), zorder=15)
    if effector:
        ax.add_patch(Circle((x + 0.55, y + 0.38), 0.2, facecolor=P.fill("metabolite"), edgecolor=P.edge("metabolite"),
                            lw=0.9, zorder=16))


def mrna(x0, x1, y):
    bio.arrow(ax, (x0, y), (x1, y), kind="process", color=P.edge("mrna"), lw=1.6, head=0.25)
    bio.label(ax, (x1 - 0.2, y + 0.32), "mRNA", size="tiny", color=P.edge("mrna"), ha="right")


def blocked(x, y):
    bio.label(ax, (x, y), "no transcription", size="tiny", color=P.edge("negative"))


rows = [
    ("A", "Repression (arg operon)", ["argC", "argB", "argH"], "ArgR", "repressor", "operator", "arginine", False),
    ("B", "Induction (lac operon)", ["lacZ", "lacY", "lacA"], "LacI", "repressor", "operator", "allolactose", True),
    ("C", "Activation (mal operon)", ["malE", "malF", "malG"], "MalT", "activator", "site", "maltose", True),
]
ys = [8.3, 5.1, 1.9]
for (letter, title, genes, reg, role, site, effector, on_with), y in zip(rows, ys):
    bio.panel(ax, letter, (0.2, y + 2.2))
    bio.label(ax, (1.0, y + 1.82), title, size="small", bold=True, ha="left")
    for col, with_eff in enumerate((False, True)):
        x0 = 1.0 + col * 12.0
        bio.label(ax, (x0 + 11.4, y + 1.82), f"+ {effector}" if with_eff else f"no {effector}", size="tiny",
                  color=P.muted(), ha="right")
        if site == "site":
            parts = [{"kind": "operator", "text": None}, {"kind": "promoter"}]
        else:
            parts = [{"kind": "promoter"}, {"kind": "operator", "text": None}]
        parts += [{"kind": "cds", "text": g, "token": "dna", "width": 2.0} for g in genes]
        gl = G.construct(ax, x0 + 0.4, y, parts, unit=0.5, gap=0.1)
        prom = gl[0] if site != "site" else gl[1]
        opr = gl[1] if site != "site" else gl[0]
        bio.label(ax, (opr["centre"], y - 0.45), "O" if site != "site" else "AB", size="tiny", color=P.muted())
        bio.label(ax, (prom["centre"], y - 0.45), "P", size="tiny", color=P.muted())
        on = with_eff == on_with
        tok = "negative" if role == "repressor" else "positive"
        bound = (role == "repressor" and not on) or (role == "activator" and on)
        mid = (gl[2]["x0"] + gl[-1]["x1"]) / 2
        if bound:
            regulator(opr["centre"], y + 0.5, tok, reg, effector=with_eff)
        else:
            regulator(gl[-1]["x1"] + 0.9, y + 0.5, tok, reg, effector=with_eff)
        if on:
            rnap(prom["centre"] + (0.75 if role == "activator" else -0.1), y + (0.55 if role == "activator" else 1.15))
            mrna(gl[2]["x0"], gl[-1]["x1"], y + 0.85)
        else:
            rnap(gl[-1]["x1"] + 0.9, y + 1.5)
            blocked(mid, y + 0.85)

# legend
lx, ly = 1.2, 0.35
ax.add_patch(Circle((lx, ly), 0.2, facecolor=P.fill("metabolite"), edgecolor=P.edge("metabolite"), lw=0.9))
bio.label(ax, (lx + 0.35, ly), "small-molecule effector (corepressor or inducer)", size="tiny", ha="left")
bio.label(ax, (13.0, ly), "O operator   AB activator-binding site   P promoter", size="tiny", ha="left", color=P.muted())
