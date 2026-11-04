"""A: what the colonic community does with dietary fiber and host mucus, and how the products act on the
host (SBGN-style). B: colonization resistance and its loss after an antibiotic course: a two-species model
in which a resident population R and an invader I compete for one resource, the antibiotic removing most of
R for a short period (illustrative parameters; the invader grows only when R is low)."""
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(26, 10.4)

# ---------------- A
bio.panel(ax, "A", (0.2, 10.2))
bio.box(ax, (2.6, 8.8), 4.0, 1.0, "carbohydrate", "dietary fiber", size="small")
bio.box(ax, (2.6, 6.6), 4.0, 1.0, "golgi", "host mucus glycans", size="small")
bio.box(ax, (8.2, 7.7), 4.2, 1.4, "bacterium", "colonic community\n(polysaccharide\nutilization loci)", size="small")
bio.arrow(ax, (4.7, 8.8), (6.1, 8.0), head=0.18)
bio.arrow(ax, (4.7, 6.6), (6.1, 7.4), head=0.18, dashed=True)
bio.box(ax, (8.2, 4.8), 4.2, 1.0, "lipid", "acetate, propionate,\nbutyrate", size="small")
bio.arrow(ax, (8.2, 7.0), (8.2, 5.3), head=0.18)
bio.box(ax, (13.6, 8.6), 3.8, 1.0, "h", "H₂, CO₂ → CH₄,\nacetate, H₂S", size="tiny")
bio.arrow(ax, (10.4, 7.9), (11.7, 8.5), head=0.16)
bio.box(ax, (13.6, 6.6), 3.8, 1.0, "metabolite", "vitamins K, B;\nsecondary bile acids", size="tiny")
bio.arrow(ax, (10.4, 7.4), (11.7, 6.8), head=0.16)

targets = [(5.2, 3.0, "colonocytes: fuel,\nO₂ consumption → anoxic lumen", "blood"),
           (10.4, 3.0, "liver: gluconeogenesis\nfrom propionate", "lysosome"),
           (15.8, 3.0, "immune cells: regulatory\nT cells (HDAC inhibition)", "antibody")]
for x, y, text, tok in targets:
    bio.box(ax, (x, y), 4.6, 1.2, tok, text, size="tiny")
    bio.arrow(ax, (8.2, 4.3), (x, y + 0.65), kind="activation", head=0.18, bg=P.surface())
bio.box(ax, (21.0, 7.0), 4.0, 1.4, "positive", "colonization\nresistance", size="small")
bio.arrow(ax, (15.5, 6.1), (19.2, 6.5), kind="activation", head=0.18, bg=P.surface())
bio.arrow(ax, (10.4, 5.1), (19.0, 6.4), kind="activation", head=0.18, bg=P.surface())
bio.label(ax, (21.0, 5.9), "low pH, inhibitory substances,\nnutrient competition, anoxia", size="tiny", color=P.muted())

# ---------------- B: model
bio.panel(ax, "B", (18.4, 4.4))
t = np.linspace(0, 40, 4001)
dt = t[1] - t[0]
rR, rI, K = 0.9, 1.3, 1.0
R, I = np.empty_like(t), np.empty_like(t)
r_, i_ = 1.0, 0.0
for k, tk in enumerate(t):
    kill = 2.2 if 10 <= tk < 13 else 0.0        # antibiotic: kills the resident
    inoc = 0.004 if 12 <= tk < 14 else 0.0      # spores ingested
    if k > 0:
        dr = rR * r_ * (1 - (r_ + i_) / K) - kill * r_
        di = rI * i_ * (1 - (r_ + i_) / K) + inoc
        r_ = max(r_ + dr * dt, 1e-6)
        i_ = max(i_ + di * dt, 0.0)
    R[k], I[k] = r_, i_
q = quant.Plot(ax, (20.0, 1.3, 5.2, 2.6), xlim=(0, 40), ylim=(0, 1.05), xlabel="time / days",
               ylabel="rel. abundance", xticks=[0, 10, 20, 30, 40], yticks=[0, 0.5, 1], size="tiny")
q.span(10, 13, "negative", strength=0.5)
q.line(t, R, token="bacterium")
q.line(t, I, token="negative")
q.text(38, 0.33, "resident", token="bacterium", ha="right")
q.text(38, 0.86, "invader", token="negative", ha="right")
bio.label(ax, (22.6, 4.15), "antibiotic (band) opens the niche", size="tiny", color=P.muted())
