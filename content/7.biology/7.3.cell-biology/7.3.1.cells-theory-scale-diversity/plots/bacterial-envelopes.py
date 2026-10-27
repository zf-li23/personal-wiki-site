# Bacterial cell envelopes and cell shapes (7.3.1). A: the Gram-positive envelope: cytoplasmic membrane with
# integral proteins and a thick (20-80 nm) multilayer peptidoglycan wall threaded by wall teichoic acids
# (linked to peptidoglycan) and lipoteichoic acids (anchored in the membrane). B: the Gram-negative
# envelope: inner membrane, periplasm with a thin (2-7 nm) peptidoglycan layer tied to the outer membrane
# by Braun's lipoprotein, and the asymmetric outer membrane (phospholipid inner leaflet, lipopolysaccharide
# outer leaflet: lipid A, core oligosaccharide, O-antigen of variable length) with porin channels. Glycan
# strands alternate NAG and NAM residues and are cross-linked by peptides. The thick wall retains the
# crystal violet-iodine complex (purple); the thin wall does not, and the cell takes up the safranin
# counterstain (pink). C: cell shapes, arrangements and flagellation, coloured by Gram reaction.
import numpy as np

import wikibio as bio
from wikibio import microbio as M
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(25.0, 14.6)
Y, TOP = 6.6, 12.4

# ---- headers -----------------------------------------------------------------------------------
for x0, k, title, gram, note in ((0.9, "A", "Gram-positive", "+", "stains purple: crystal violet retained"),
                                 (13.4, "B", "Gram-negative", "-", "stains pink: safranin counterstain")):
    bio.panel(ax, k, (x0 - 0.8, 14.45))
    M.coccus(ax, (x0 + 0.3, 13.55), 0.3, gram=gram)
    bio.label(ax, (x0 + 0.85, 13.75), title, size="normal", bold=True, ha="left")
    bio.label(ax, (x0 + 0.85, 13.25), note, size="tiny", ha="left", color=P.muted())

# ---- A: Gram-positive ------------------------------------------------------------------------------
ax0, ax1 = 0.9, 7.9
A = M.envelope(ax, ax0, ax1, Y, kind="gram+", top=TOP, seed=4)
cx = ax1 + 0.55
bio.label(ax, (ax1 - 0.1, TOP - 0.25), "Outside", size="small", ha="right", va="top", color=P.muted())
bio.label(ax, (ax1 - 0.1, A["bottom"] + 0.2), "Cytoplasm", size="small", ha="right", va="bottom", color=P.muted())
w_x, w_tip = A["wta"][-1]
bio.callout(ax, w_tip, (cx, TOP - 0.7), "Wall teichoic acid")
l_x, l_tip = A["lta"][-1]
bio.callout(ax, (l_x, (A["pg_lo"] + A["pg_hi"]) / 2 + 0.18), (cx, (A["pg_lo"] + A["pg_hi"]) / 2 + 0.55), "Lipoteichoic acid")
bio.callout(ax, (ax1 - 0.35, A["pg_lo"] + 0.36 * 2), (cx, A["pg_lo"] + 0.3), "Peptidoglycan")
bio.callout(ax, (ax1 - 0.3, A["im_hi"] - 0.1), (cx, A["im"] + 0.05), "Cytoplasmic\nmembrane")
t = A["transporters"][1]
bio.callout(ax, (t + 0.2, A["im_lo"] - 0.15), (cx, A["im_lo"] - 0.75), "Membrane protein")
quant.bracket(ax, (ax0 - 0.2, A["pg_lo"]), (ax0 - 0.2, A["pg_hi"]), side=-1, tick=0.12, text="20–80 nm", size="tiny")

# ---- B: Gram-negative ------------------------------------------------------------------------------
bx0, bx1 = 13.4, 20.4
B = M.envelope(ax, bx0, bx1, Y, kind="gram-", top=TOP, seed=5)
cx = bx1 + 0.55
bio.label(ax, (bx1 - 0.1, TOP - 0.25), "Outside", size="small", ha="right", va="top", color=P.muted())
bio.label(ax, (bx1 - 0.1, B["bottom"] + 0.2), "Cytoplasm", size="small", ha="right", va="bottom", color=P.muted())
bio.label(ax, (bx0 + 0.15, (B["im_hi"] + B["pg_lo"]) / 2 - 0.05), "Periplasm", size="small", ha="left", color=P.muted())
# LPS parts: pick the tallest chain right of the second porin
xs, tips = B["lps_x"], B["lps_tips"]
k = int(np.argmax([tp[1] for tp in tips]))
tip = tips[k]
bio.callout(ax, (tip[0] + 0.05, tip[1] - 0.25), (cx, 11.7), "O-antigen")
xr = max(x for x in xs if x < bx1 - 0.25)
bio.callout(ax, (xr + 0.07, B["om_hi"] + 0.35), (cx, 10.8), "Core oligosaccharide")
bio.callout(ax, (xr + 0.1, B["om_hi"] - 0.08), (cx, 10.1), "Lipid A")
bio.callout(ax, (xr, B["om_lo"] + 0.08), (cx, 8.85), "Outer membrane")
p = B["porins"][1]
bio.callout(ax, (p + 0.4, B["om"] + 0.05), (cx, 9.45), "Porin")
lp = B["lipoproteins"][1]
bio.callout(ax, (lp + 0.06, (B["pg_hi"] + B["om_lo"]) / 2), (cx, 8.25), "Braun's lipoprotein")
bio.callout(ax, (bx1 - 2.3, B["pg_lo"] + 0.08), (cx, 7.65), "Peptidoglycan")
bio.callout(ax, (bx1 - 0.3, B["im_hi"] - 0.1), (cx, 6.95), "Inner membrane")
t = B["transporters"][1]
bio.callout(ax, (t + 0.2, B["im_lo"] - 0.15), (cx, 5.85), "Membrane protein")
quant.bracket(ax, (bx0 - 0.2, B["om"]), (bx0 - 0.2, TOP - 0.45), side=-1, tick=0.12, text="LPS", size="small")
quant.bracket(ax, (bx0 - 0.2, B["pg_lo"]), (bx0 - 0.2, B["pg_hi"]), side=-1, tick=0.08, text="2–7 nm", size="tiny")

# ---- C: shapes and flagella ----------------------------------------------------------------------
bio.panel(ax, "C", (0.1, 4.05))
bio.label(ax, (0.9, 3.75), "Cell shapes, arrangements and flagella", size="normal", bold=True, ha="left")
yc, yl = 2.0, 0.55
items = []
M.coccus(ax, (1.3, yc), 0.35, gram="+")
items.append((1.3, "coccus", "Micrococcus"))
M.diplococcus(ax, (3.1, yc), 0.3, gram="-")
items.append((3.1, "diplococci", "Neisseria"))
M.chain(ax, (4.75, yc + 0.35), 6, 0.22, angle=-0.25, gram="+", seed=4)
items.append((5.9, "chain", "Streptococcus"))
M.cluster(ax, (8.45, yc), 0.22, n=11, gram="+")
items.append((8.6, "cluster", "Staphylococcus"))
M.bacillus(ax, (11.3, yc), 1.5, 0.55, gram="-", flagella="peritrichous", flagellum_length=0.75)
items.append((11.3, "bacillus, peritrichous", "Escherichia coli"))
M.bacillus(ax, (14.4, yc), 1.3, 0.5, gram="-", flagella="lophotrichous", flagellum_length=1.0, angle=180)
items.append((14.75, "bacillus, lophotrichous", "Pseudomonas"))
M.vibrio(ax, (17.15, yc), 1.15, 0.42, angle=0, flagella="monotrichous", flagellum_length=1.1)
items.append((17.6, "vibrio, monotrichous", "Vibrio cholerae"))
M.spirillum(ax, (19.6, yc - 0.05), (21.5, yc - 0.05), width=0.22, turns=2.0, amplitude=0.28, flagellum_length=0.6)
items.append((20.55, "spirillum, amphitrichous", "Spirillum"))
M.spirochete(ax, (22.4, yc), (24.6, yc), width=0.11, turns=7, amplitude=0.12)
items.append((23.5, "spirochete", "Treponema"))
for x, kind, genus in items:
    bio.label(ax, (x, yl + 0.35), kind, size="tiny")
    bio.label(ax, (x, yl), genus, size="tiny", italic=True, color=P.muted())
