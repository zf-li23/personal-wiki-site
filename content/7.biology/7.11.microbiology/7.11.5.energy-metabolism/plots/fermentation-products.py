"""Fermentation products from pyruvate (and PEP), colored by the organisms that make them.
Lactic acid bacteria: pyruvate -> lactate (lactate dehydrogenase, NADH). Yeasts and Zymomonas:
pyruvate -> acetaldehyde + CO2 (pyruvate decarboxylase) -> ethanol (NADH). Enteric bacteria:
pyruvate -> acetyl-CoA + formate (pyruvate formate-lyase); formate -> H2 + CO2 (formate
hydrogenlyase); acetyl-CoA -> acetate (ATP via acetyl-P) or -> ethanol (2 NADH); PEP -> oxaloacetate
-> succinate (2 NADH); 2 pyruvate -> alpha-acetolactate -> acetoin -> 2,3-butanediol (Klebsiella,
Enterobacter). Clostridia: pyruvate -> acetyl-CoA + CO2 + H2 (pyruvate:ferredoxin oxidoreductase and
hydrogenase); 2 acetyl-CoA -> acetoacetyl-CoA -> butyryl-CoA -> butyrate (ATP) or butanol;
acetoacetate -> acetone + CO2. Propionibacteria: pyruvate -> propionate (methylmalonyl-CoA pathway)."""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27.0, 15.0)
G = {"lab": "enzyme", "yeast": "highlight", "ent": "drug", "clo": "protein", "prop": "carbohydrate", "core": "neutral"}
N = {}


def node(id, xy, text, grp, w=None):
    w = w or max(2.2, 0.21 * max(len(t) for t in text.split("\n")) + 0.8)
    h = 0.8 if "\n" not in text else 1.25
    bio.box(ax, xy, w, h, G[grp], text, size="small")
    N[id] = (xy, w, h)


def edge(a, b, grp, text=None, at=0.5, off=(0.0, 0.25), dashed=False, ha="center"):
    (xa, ya), wa, ha_ = N[a]
    (xb, yb), wb, hb = N[b]
    import math
    dx, dy = xb - xa, yb - ya
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L

    def trim(w, h):  # distance from centre to box edge along (ux, uy)
        tx = (w / 2) / abs(ux) if abs(ux) > 1e-9 else 1e9
        ty = (h / 2) / abs(uy) if abs(uy) > 1e-9 else 1e9
        return min(tx, ty) + 0.1
    p = (xa + ux * trim(wa, ha_), ya + uy * trim(wa, ha_))
    q = (xb - ux * trim(wb, hb), yb - uy * trim(wb, hb))
    bio.arrow(ax, p, q, kind="process", color=P.edge(G[grp]), lw=1.5, head=0.18, dashed=dashed)
    if text:
        m = (p[0] + (q[0] - p[0]) * at + off[0], p[1] + (q[1] - p[1]) * at + off[1])
        bio.label(ax, m, text, size="tiny", color=P.ink(), ha=ha)


node("glc", (12.5, 14.1), "Glucose", "core")
node("pep", (12.5, 12.2), "PEP", "core")
node("pyr", (12.5, 9.6), "Pyruvate", "core")
edge("glc", "pep", "core", "glycolysis", off=(1.2, 0.0))
edge("pep", "pyr", "core", "ATP", off=(0.6, 0.0))

node("lac", (3.2, 9.6), "Lactate", "lab")
edge("pyr", "lac", "lab", "LDH, NADH", off=(0.0, 0.3))
node("oaa", (3.6, 12.2), "Oxaloacetate", "ent")
node("suc", (3.6, 13.9), "Succinate", "ent")
edge("pep", "oaa", "ent", "+CO₂", off=(0.0, 0.3))
edge("oaa", "suc", "ent", "2 NADH", off=(1.1, 0.0))
node("prop", (3.2, 6.6), "Propionate", "prop")
edge("pyr", "prop", "prop", "methylmalonyl-CoA\npathway", at=0.55, off=(0.0, 0.55), dashed=True)

node("ald", (7.6, 6.6), "Acetaldehyde\n+ CO₂", "yeast")
node("eth", (7.6, 3.4), "Ethanol", "yeast")
edge("pyr", "ald", "yeast", "PDC", off=(-0.4, 0.15), ha="right")
edge("ald", "eth", "yeast", "NADH", off=(0.75, 0.0))

node("acoa", (12.5, 6.2), "Acetyl-CoA", "core")
edge("pyr", "acoa", "core", "PFL: + formate (enterics)\nPFOR: + CO₂ + H₂ (clostridia)", off=(3.0, 0.0))
node("for", (18.4, 7.8), "Formate", "ent")
node("h2", (22.8, 7.8), "H₂ + CO₂", "ent")
edge("acoa", "for", "ent")
edge("for", "h2", "ent", "FHL", off=(0.0, 0.3))
node("ace", (11.0, 3.4), "Acetate", "ent")
edge("acoa", "ace", "ent", "ATP", off=(-0.55, 0.0))
edge("acoa", "eth", "ent", "2 NADH", off=(-0.6, -0.35))

node("alac", (17.6, 11.6), "α-Acetolactate", "ent")
node("acetoin", (22.8, 11.6), "Acetoin", "ent")
node("bdo", (22.8, 9.7), "2,3-Butanediol", "ent")
edge("pyr", "alac", "ent", "2 pyruvate, −CO₂", off=(0.0, 0.35))
edge("alac", "acetoin", "ent", "−CO₂", off=(0.0, 0.3))
edge("acetoin", "bdo", "ent", "NADH", off=(0.75, 0.0))

node("aaco", (17.2, 4.2), "Acetoacetyl-CoA", "clo")
node("bcoa", (17.2, 2.0), "Butyryl-CoA", "clo")
node("but", (13.8, 0.7), "Butyrate", "clo")
node("buoh", (21.0, 0.7), "Butanol", "clo")
node("acn", (22.6, 4.2), "Acetone + CO₂", "clo")
edge("acoa", "aaco", "clo", "2 acetyl-CoA", off=(0.9, 0.3))
edge("aaco", "bcoa", "clo", "2 NADH", off=(0.75, 0.0))
edge("bcoa", "but", "clo", "ATP", off=(-0.2, 0.3))
edge("bcoa", "buoh", "clo", "2 NADH", off=(0.4, 0.3))
edge("aaco", "acn", "clo", "via acetoacetate", off=(0.0, 0.55))

leg = [("lactic acid bacteria", "lab"), ("yeasts, Zymomonas", "yeast"), ("enteric bacteria", "ent"),
       ("clostridia", "clo"), ("propionibacteria", "prop")]
for k, (t, g) in enumerate(leg):
    y = 2.6 - 0.55 * k
    bio.box(ax, (0.8, y), 0.5, 0.35, G[g])
    bio.label(ax, (1.25, y), t, size="tiny", ha="left")
