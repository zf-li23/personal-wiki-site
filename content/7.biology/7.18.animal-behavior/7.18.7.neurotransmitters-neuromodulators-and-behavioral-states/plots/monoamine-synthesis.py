"""Synthesis of the monoamines: catecholamines, serotonin and melatonin, tyramine and octopamine."""
import wikibio as bio
from wikibio import metabolism

P = bio.P
fig, ax = bio.canvas(22, 13)
pw = metabolism.Pathway(ax, size="small")
cols = {"cat": 3.5, "ser": 11.0, "oct": 18.5}
ys = [11.5, 8.8, 6.1, 3.4, 0.9]
for key, names in [("cat", ["Tyrosine", "L-DOPA", "Dopamine", "Norepinephrine", "Epinephrine"]),
                   ("ser", ["Tryptophan", "5-Hydroxytryptophan", "Serotonin (5-HT)", "N-Acetylserotonin", "Melatonin"]),
                   ("oct", ["Tyrosine", "Tyramine", "Octopamine"])]:
    for i, n in enumerate(names):
        pw.node(f"{key}{i}", (cols[key], ys[i]), n, token="metabolite" if i else "neutral")
enz = {"cat": ["TH", "AADC", "DBH", "PNMT"], "ser": ["TPH", "AADC", "AANAT", "ASMT"], "oct": ["TDC", "TβH"]}
for key, es in enz.items():
    for i, e in enumerate(es):
        pw.step(f"{key}{i}", f"{key}{i + 1}", enzyme=e)
bio.label(ax, (cols["cat"], 12.6), "Catecholamines (vertebrates and invertebrates)", size="small", bold=True)
bio.label(ax, (cols["ser"], 12.6), "Indolamines", size="small", bold=True)
bio.label(ax, (cols["oct"], 12.6), "Phenolamines (invertebrates)", size="small", bold=True)
bio.label(ax, (cols["ser"] + 2.2, 2.15), "pineal gland", size="tiny", color=P.muted())
bio.label(ax, (cols["cat"] + 2.4, 2.15), "adrenal medulla", size="tiny", color=P.muted())
