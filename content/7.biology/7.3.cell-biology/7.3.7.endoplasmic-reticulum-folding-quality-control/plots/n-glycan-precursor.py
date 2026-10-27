# The N-glycan precursor and its trimming in the ER (SNFG symbols, reducing end on the right).
# A: Glc3Man9GlcNAc2 on dolichol pyrophosphate, as transferred en bloc by oligosaccharyltransferase;
# callouts give the enzymes that remove the residues in the ER. B: the trimming intermediates and the
# lectins that read them: Glc1Man9 (calnexin/calreticulin), Man9 (folded or refolding; UGGT re-adds Glc),
# Man8B (ER mannosidase I), and Man7 with the C-arm alpha1-6 mannose exposed (signal for ERAD lectins).
import wikibio as bio
from wikibio import glycan as G

fig, ax = bio.canvas(22, 11.2)
P = bio.P

bio.panel(ax, "A", (0.2, 11.0))
bio.label(ax, (1.0, 10.7), "Precursor transferred by OST: Glc3Man9GlcNAc2", bold=True, ha="left")
PRE = ("Man(a1-2)Man(a1-6)[Man(a1-2)Man(a1-3)]Man(a1-6)"
       "[Glc(a1-2)Glc(a1-3)Glc(a1-3)Man(a1-2)Man(a1-2)Man(a1-3)]Man(b1-4)GlcNAc(b1-4)GlcNAc(a1-")
g = G.draw(ax, PRE, at=(13.2, 8.0), step=1.15, row=1.05, size=0.48, labels="short", aglycone="PP-Dol")
glc = [g.find("Glc", k) for k in range(3)]
bio.callout(ax, glc[0] + (0, 0.25), (2.3, 9.9), "Glucosidase I")
bio.callout(ax, glc[1] + (0, -0.25), (2.6, 6.2), "Glucosidase II (Glc 2 and 3)")
bio.callout(ax, glc[2] + (0.05, -0.25), (2.6, 6.2), "")
man = [g.find("Man", k) for k in range(9)]
# written order: Man0 (C-arm a1-2), Man1, Man2 (B-arm a1-2), Man3, Man4, Man5.. A-arm
bio.callout(ax, man[2] + (0.0, 0.25), (8.6, 10.1), "ER mannosidase I (Man8B)")
bio.callout(ax, man[0] + (0.0, 0.25), (6.3, 10.1), "EDEMs: ERAD timer")
bio.label(ax, (13.9, 7.3), "OST transfers the whole glycan\nto Asn in Asn–X–Ser/Thr", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (12.6, 9.6), "Arms: C (top), B, A (bottom)", size="tiny", color=P.muted())
G.legend(ax, (18.3, 10.2), ["Glc", "Man", "GlcNAc"], dy=0.7, size=0.42)

bio.panel(ax, "B", (0.2, 5.0))
bio.label(ax, (1.0, 4.7), "Trimming intermediates and their readers", bold=True, ha="left")
STEPS = [
    ("Glc1Man9", "Man(a1-2)Man(a1-6)[Man(a1-2)Man(a1-3)]Man(a1-6)[Glc(a1-3)Man(a1-2)Man(a1-2)Man(a1-3)]Man(b1-4)GlcNAc(b1-4)GlcNAc(b1-",
     "Calnexin / calreticulin\n(folding intermediate)"),
    ("Man9", "Man(a1-2)Man(a1-6)[Man(a1-2)Man(a1-3)]Man(a1-6)[Man(a1-2)Man(a1-2)Man(a1-3)]Man(b1-4)GlcNAc(b1-4)GlcNAc(b1-",
     "Released; UGGT re-adds\nGlc if still unfolded"),
    ("Man8B", "Man(a1-2)Man(a1-6)[Man(a1-3)]Man(a1-6)[Man(a1-2)Man(a1-2)Man(a1-3)]Man(b1-4)GlcNAc(b1-4)GlcNAc(b1-",
     "Exit-competent\n(cargo receptors)"),
    ("Man7", "Man(a1-6)[Man(a1-3)]Man(a1-6)[Man(a1-2)Man(a1-2)Man(a1-3)]Man(b1-4)GlcNAc(b1-4)GlcNAc(b1-",
     "Exposed α1-6 Man:\nOS-9 / XTP3-B → ERAD"),
]
x = 5.2
prev = None
for k, (name, s, reader) in enumerate(STEPS):
    gg = G.draw(ax, s, at=(x, 2.4), step=0.62, row=0.62, size=0.3, labels=None, aglycone="Asn", stub=0.4)
    x0, y0, x1, y1 = gg.bounds()
    bio.label(ax, ((x0 + x1) / 2, 4.15), name, size="small", bold=True)
    bio.label(ax, ((x0 + x1) / 2, 0.55), reader, size="tiny", color=P.muted())
    if prev is not None:
        bio.arrow(ax, (prev, 2.4), (x0 - 0.35, 2.4), kind="process")
    prev = x + 1.3
    x += 5.4
