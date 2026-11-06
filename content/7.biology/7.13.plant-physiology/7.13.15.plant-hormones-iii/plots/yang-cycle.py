# Ethylene biosynthesis and the Yang (methionine) cycle.
# Met + ATP -> SAM (SAM synthetase); SAM -> ACC + MTA (ACC synthase, PLP; rate-limiting);
# ACC + 1/2 O2 -> C2H4 + CO2 + HCN (ACC oxidase); MTA -> MTR -> MTR-1-P -> KMB -> Met (recycles CH3S).
import wikibio as bio
from wikibio import metabolism as M

fig, ax = bio.canvas(22, 12)
P = bio.P
pw = M.Pathway(ax, size="small")
ctr, r = (7.0, 6.2), 4.0
pos = M.ring(ctr, r, 6, start=90, clockwise=True)
names = [("met", "Methionine"), ("sam", "S-Adenosyl-\nmethionine (SAM)"), ("mta", "5′-Methylthio-\nadenosine (MTA)"),
         ("mtr", "5-Methylthioribose\n(MTR)"), ("mtrp", "MTR-1-phosphate"), ("kmb", "2-Keto-4-methyl-\nthiobutyrate (KMB)")]
for (id, text), p in zip(names, pos):
    pw.node(id, p, text, bold=id in ("met", "sam"), h=0.75 if "\n" in text else None)
order = [n for n, _ in names] + ["met"]
enz = ["SAM synthetase", "ACC synthase", "nucleosidase", "MTR kinase", "several steps", "transaminase"]
sides = [("ATP", "PPi + Pi"), None, (None, "adenine"), ("ATP", "ADP"), (None, "formate"), ("amino acid", "2-oxo acid")]
for k in range(6):
    a, b = order[k], order[k + 1]
    if k == 1:
        continue
    pw.step(a, b, enzyme=enz[k], side=sides[k], enzyme_size="tiny", side_size="tiny",
            bend=M.cycle_bend(pos[k], pos[(k + 1) % 6], ctr))
bio.label(ax, ctr, "YANG\nCYCLE", size="normal", bold=True, color=P.muted())

# branch: SAM -> ACC (+MTA) -> ethylene
pw.node("acc", (14.4, 6.2), "ACC", bold=True)
pw.node("eth", (19.4, 6.2), "Ethylene", bold=True, token="positive")
pw.node("macc", (14.4, 2.4), "N-Malonyl-ACC (MACC)", token="neutral")
pw.step("sam", "acc", enzyme="ACC synthase (ACS)\nPLP; rate-limiting", enzyme_size="tiny", bend=-0.12)
pw.step("acc", "mta", bend=0.12, dashed=True)
bio.label(ax, (13.1, 5.0), "MTA released", size="tiny", color=P.muted())
pw.step("acc", "eth", enzyme="ACC oxidase (ACO)\nFe²⁺, ascorbate", side=("½ O₂", "CO₂ + HCN"), enzyme_size="tiny",
        side_size="tiny")
pw.step("acc", "macc", enzyme="malonyl transferase", enzyme_size="tiny", enzyme_flip=True)


def factors(x, y, title, items, tok):
    bio.label(ax, (x, y), title, size="small", bold=True, ha="left", color=P.edge(tok))
    for i, t in enumerate(items):
        bio.label(ax, (x, y - 0.5 * (i + 1)), "• " + t, size="tiny", ha="left")


factors(16.4, 11.4, "Promote ACS / ACO", ["ripening (system 2)", "senescence, pollination", "high auxin",
                                          "wounding, pathogens", "flooding, chilling, drought"], "positive")
factors(16.4, 3.6, "Inhibit", ["AVG, AOA (ACS, PLP enzymes)", "Co²⁺, anaerobiosis (ACO)",
                               "temperature > 35 °C", "ethylene in vegetative tissue (system 1)"], "negative")
