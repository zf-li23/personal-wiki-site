# Peptidoglycan biosynthesis in three compartments (schematic, E. coli-type, with meso-diaminopimelic acid).
# Cytoplasm: UDP-GlcNAc -> UDP-MurNAc (MurA, MurB) -> UDP-MurNAc-pentapeptide (MurC-F; the last step adds the
# dipeptide D-Ala-D-Ala made by alanine racemase and D-Ala-D-Ala ligase), the "Park nucleotide".
# Membrane: MraY transfers phospho-MurNAc-pentapeptide to the lipid carrier undecaprenyl phosphate
# (bactoprenol phosphate), giving lipid I; MurG adds GlcNAc, giving lipid II, which is flipped to the outer
# face of the membrane (MurJ).
# Outside the membrane: glycosyltransferases (class A penicillin-binding proteins and the SEDS proteins RodA
# and FtsW) add the disaccharide-pentapeptide to a growing glycan strand, releasing undecaprenyl
# pyrophosphate, which is dephosphorylated and returned; transpeptidases (PBPs) cross-link the peptides,
# releasing the terminal D-Ala. Autolysins open the existing wall so that new strands can be inserted.
# Drug targets (bars, SBGN inhibition): fosfomycin (MurA), D-cycloserine (Ala racemase and ligase),
# bacitracin (binds undecaprenyl pyrophosphate), vancomycin (binds D-Ala-D-Ala of lipid II and nascent wall),
# beta-lactams (acylate the PBP transpeptidases).
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26, 11.5)

# compartments
ax.add_patch(Rectangle((0, 0), 26, 4.6, facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=0))
ax.add_patch(Rectangle((0, 6.0), 26, 5.5, facecolor=P.fill("extracellular"), edgecolor="none", zorder=0))
MEM = P.mix(P.fill("lipid_tail"), P.surface(), 0.7 if P.is_dark() else 0.2)
ax.add_patch(Rectangle((0, 4.6), 26, 1.4, facecolor=MEM, edgecolor="none", zorder=0))
ax.plot([0, 26], [4.6, 4.6], color=P.edge("lipid_head"), lw=2.2, zorder=1)
ax.plot([0, 26], [6.0, 6.0], color=P.edge("lipid_head"), lw=2.2, zorder=1)
bio.label(ax, (0.3, 0.4), "Cytoplasm", size="small", bold=True, ha="left")
bio.label(ax, (0.3, 5.3), "Cytoplasmic membrane", size="small", bold=True, ha="left")
bio.label(ax, (0.3, 11.1), "Outside the membrane (periplasm or wall)", size="small", bold=True, ha="left")

C = P.fill("cytoplasm")
E = P.fill("extracellular")


def node(xy, text, w=3.0, h=0.9, token="carbohydrate"):
    bio.box(ax, xy, w, h, token=token, text=text, size="tiny")


def enz(xy, text, ha="center"):
    bio.label(ax, xy, text, size="tiny", italic=False, color=P.ink(), ha=ha, bold=True)


def drug(target, at, text):
    bio.arrow(ax, at, target, kind="inhibition", color=P.edge("drug"), lw=1.3)
    bio.label(ax, (at[0], at[1] + (0.28 if at[1] > target[1] else -0.28)), text, size="tiny", color=P.edge("drug"),
              italic=False)


# ---- cytoplasm -----------------------------------------------------------------------------------------
y = 2.6
node((2.2, y), "UDP-GlcNAc", w=2.6, token="dna")
node((7.4, y), "UDP-MurNAc", w=2.6, token="protein")
node((13.6, y), "UDP-MurNAc-\npentapeptide", w=3.2, h=1.1, token="peptide")
bio.arrow(ax, (3.55, y), (6.05, y), kind="process", bg=C)
enz((4.8, y + 0.35), "MurA, MurB")
bio.arrow(ax, (8.75, y), (11.95, y), kind="process", bg=C)
enz((10.35, y + 0.35), "MurC, D, E, F")
bio.label(ax, (9.9, y - 0.4), "+ L-Ala, D-Glu, $m$-DAP", size="tiny", color=P.muted())
node((10.35, 0.9), "D-Ala-D-Ala", w=2.4, token="peptide")
bio.arrow(ax, (10.35, 1.4), (11.6, y - 0.25), kind="process", bend=-0.2, bg=C)
bio.label(ax, (11.75, 0.9), "from 2 L-Ala\n(Alr, Ddl)", size="tiny", color=P.muted(), ha="left")
drug((4.8, y - 0.1), (4.8, 1.0), "fosfomycin")
drug((9.1, 0.8), (6.3, 0.35), "")
bio.label(ax, (5.2, 0.35), "D-cycloserine", size="tiny", color=P.edge("drug"))
bio.label(ax, (13.6, 3.45), "Park nucleotide", size="tiny", color=P.muted())

# ---- membrane ------------------------------------------------------------------------------------------
ym = 5.3
node((14.0, ym), "bactoprenol-P", w=2.6, h=0.8, token="lipid")
node((17.6, ym), "lipid I", w=1.9, h=0.8, token="lipid")
node((21.4, ym), "lipid II", w=1.9, h=0.8, token="lipid")
bio.arrow(ax, (15.2, y + 0.3), (17.0, ym - 0.4), kind="process", bend=0.2, bg=C)
enz((15.3, 3.9), "MraY", ha="right")
bio.arrow(ax, (15.3, ym), (16.65, ym), kind="process", bg=MEM)
bio.arrow(ax, (18.55, ym), (20.45, ym), kind="process", bg=MEM)
enz((19.5, 5.8), "MurG (+ GlcNAc)")
bio.arrow(ax, (22.35, ym + 0.2), (23.0, 6.9), kind="process", bend=0.25, bg=MEM)
enz((23.9, 5.3), "flippase (MurJ)", ha="left")

# ---- outside -------------------------------------------------------------------------------------------
node((23.4, 7.3), "lipid II (outer face)", w=3.6, h=0.75, token="lipid")
node((17.6, 7.3), "undecaprenyl-PP", w=2.9, h=0.75, token="lipid")
bio.arrow(ax, (21.55, 7.3), (19.1, 7.3), kind="process", bg=E)
bio.arrow(ax, (16.1, 7.2), (14.6, ym + 0.45), kind="process", bend=0.25, bg=E)
bio.label(ax, (13.6, 7.15), "–P$_i$: carrier\nreturns", size="tiny", color=P.muted(), ha="right")
drug((17.6, 7.7), (17.6, 8.6), "bacitracin")
drug((23.9, 7.7), (24.9, 8.9), "vancomycin")

GN, MN = "dna", "protein"
yw = 10.0


def sugar(x, yy, k):
    tok = GN if k % 2 == 0 else MN
    ax.add_patch(plt.Circle((x, yy), 0.22, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=8))


for k in range(11):
    sugar(1.6 + k * 1.2, yw - 1.0, k)
for k in range(7):
    sugar(1.6 + k * 1.2, yw, k)
for k in (1, 3, 5):
    ax.plot([1.6 + k * 1.2] * 2, [yw - 0.22, yw - 0.78], color=P.edge("peptide"), lw=1.6, zorder=7)
ax.plot([1.2, 13.6], [yw - 1.0, yw - 1.0], color=P.muted(), lw=0.8, zorder=7)
ax.plot([1.2, 8.8], [yw, yw], color=P.muted(), lw=0.8, zorder=7)
ax.plot([10.0, 13.6], [yw, yw], color=P.muted(), lw=0.8, zorder=7)
for k in (7, 8, 9):  # new strand
    sugar(1.6 + k * 1.2 + 0.4, yw, k)
bio.label(ax, (5.2, yw + 0.6), "existing peptidoglycan", size="tiny", color=P.muted())
bio.label(ax, (11.6, yw + 0.6), "new strand", size="tiny", color=P.muted())
bio.label(ax, (5.2, 7.9), "autolysins open the existing wall\nat insertion sites", size="tiny", color=P.muted())
bio.arrow(ax, (21.9, 7.7), (13.4, yw + 0.15), kind="process", bend=0.12, bg=E)
enz((18.6, 10.0), "transglycosylation: class A PBPs, RodA, FtsW")
xt = 1.6 + 8 * 1.2 + 0.4
bio.arrow(ax, (xt, yw - 0.25), (xt, yw - 0.75), kind="process", bg=E, head=0.14)
enz((xt, 8.15), "transpeptidation: PBPs\n(releases D-Ala)")
drug((xt + 0.15, yw - 0.5), (14.6, 8.4), "")
bio.label(ax, (14.75, 8.4), "β-lactams", size="tiny", color=P.edge("drug"), ha="left")

# legend
sugar(20.6, 0.9, 0)
bio.label(ax, (20.95, 0.9), "GlcNAc", size="tiny", ha="left")
sugar(22.8, 0.9, 1)
bio.label(ax, (23.15, 0.9), "MurNAc", size="tiny", ha="left")
ax.plot([20.4, 20.8], [1.6, 1.6], color=P.edge("peptide"), lw=1.6)
bio.label(ax, (20.95, 1.6), "peptide cross-link", size="tiny", ha="left")
ax.plot([20.4, 20.8], [2.3, 2.3], color=P.edge("drug"), lw=1.3)
ax.plot([20.8, 20.8], [2.15, 2.45], color=P.edge("drug"), lw=1.3)
bio.label(ax, (20.95, 2.3), "inhibited by a drug", size="tiny", ha="left")
