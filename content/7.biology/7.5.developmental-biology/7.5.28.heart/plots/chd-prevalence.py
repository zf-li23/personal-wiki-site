"""Birth prevalence of the common congenital heart defects (per 1000 live births; approximate pooled estimates
after van der Linde et al. 2011, total about 9 per 1000), coloured by the developmental process most often at
fault: septation and the endocardial cushions, the outflow tract (second heart field and cardiac neural crest),
the valves, the ductus arteriosus (failure to close after birth) and left-heart growth, which depends on flow."""
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
data = [("VSD", 2.62, "sept"), ("ASD", 1.64, "sept"), ("PDA", 0.87, "duct"), ("Pulmonary stenosis", 0.50, "valve"),
        ("Tetralogy of Fallot", 0.34, "oft"), ("AVSD", 0.34, "sept"), ("Coarctation", 0.34, "flow"), ("TGA", 0.31, "oft"),
        ("HLHS", 0.23, "flow"), ("Aortic stenosis", 0.22, "valve")]
col = {"sept": ("lipid", "septation, cushions"), "oft": ("drug", "outflow tract (SHF, crest)"), "valve": ("enzyme", "valves"),
       "duct": ("dna", "ductus arteriosus"), "flow": ("muscle", "left heart, flow")}
fig, ax = plt.subplots(figsize=(7.4, 3.8))
fig.subplots_adjust(left=0.27, right=0.97, bottom=0.14, top=0.9)
names = [d[0] for d in data][::-1]
vals = [d[1] for d in data][::-1]
cs = [charts.line(col[d[2]][0]) for d in data][::-1]
ax.barh(names, vals, color=cs)
for k, v in enumerate(vals):
    ax.text(v + 0.04, k, f"{v:.2f}", va="center", fontsize=FT["tiny"], color=P_.ink())
for key, (tk, txt) in col.items():
    ax.barh([0], [0], color=charts.line(tk), label=txt)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="lower right")
ax.tick_params(axis="y", labelsize=FT["small"])
charts.style_axes(ax, "birth prevalence per 1000 live births", None)
charts.title(ax, "Congenital heart defects (total about 9 per 1000)")
