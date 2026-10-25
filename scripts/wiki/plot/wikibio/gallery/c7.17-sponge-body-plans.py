# Sponges (Porifera): body plans and cells. A: the three grades of canal system, in longitudinal
# section. Water enters through many small pores (ostia), is driven by the beating flagella of the
# choanocytes (red) and leaves through one large osculum. Asconoid: choanocytes line the central cavity
# (spongocoel) directly. Syconoid: the wall is folded into radial canals lined by choanocytes. Leuconoid:
# choanocytes sit in small chambers within a thick mesohyl, fed and drained by branching canals; most
# sponges, including all large ones, are leuconoid, which maximises the filtering surface. Pinacocytes
# (yellow) cover the outside. B: cells of the wall (inside on the left): choanocytes, the mesohyl with
# amoebocytes (totipotent, transport food and become other cell types), scleroblasts secreting spicules
# and an oocyte, porocytes forming the ostia, and the outer pinacoderm. C: a choanocyte: a collar of
# microvilli around a single flagellum; bacteria trapped on the collar are phagocytosed. Choanocytes
# closely resemble choanoflagellates, the sister group of animals.
import wikibio as bio
from wikibio import animalmorph as AM

P = bio.P
fig, ax = bio.canvas(32.6, 12.6)
SP = {"choanocytes": "negative", "pinacoderm": "highlight", "mesohyl": "neutral"}

bio.panel(ax, "A", (0.2, 12.4))
items = [dict(icon="wikimedia/sponge-asconoid", title="Asconoid"), dict(icon="wikimedia/sponge-syconoid", title="Syconoid"),
         dict(icon="wikimedia/sponge-leuconoid", title="Leuconoid")]
xs = [2.6, 7.0, 12.0]
row = AM.homology_row(ax, items, SP, y=1.5, height=7.6, x=xs, mute=None)
for s in row:
    x, y, w, h = s.box
    top = (x + w / 2, y + h)
    bio.arrow(ax, (top[0], top[1] - 1.4), (top[0], top[1] + 0.9), kind="process", color=P.edge("channel"), lw=1.6, head=0.25)
x, y, w, h = row[0].box
for yy in (0.62, 0.45, 0.28):
    bio.arrow(ax, (x - 0.75, y + yy * h), (x + 0.15 * w, y + yy * h), kind="process", color=P.edge("channel"), lw=1.1, head=0.18)
bio.label(ax, (x - 0.2, y + 0.73 * h), "Ostia", size="small", ha="center")
t = row[0].box
bio.label(ax, (t[0] + t[2] / 2 + 0.25, t[1] + t[3] + 0.55), "Osculum", size="small", ha="left")
bio.label(ax, (t[0] + t[2] / 2, t[1] + 0.55 * t[3]), "Spongo-\ncoel", size="tiny", color=P.muted())
AM.part_legend(ax, (1.0, 0.35), {"choanocytes": "negative", "pinacoderm": "highlight", "mesohyl": "neutral"},
               names={"choanocytes": "Choanocytes", "pinacoderm": "Pinacoderm", "mesohyl": "Mesohyl"})

bio.panel(ax, "B", (15.0, 12.4))
wall = AM.Specimen("wikimedia/sponge-wall-cells", at=(19.1, 6.6), height=10.0)
wall.draw(ax)
F = wall.frac
AM.callouts(ax, [(F(0.065, 0.94), "Flagellum", "left"), (F(0.54, 0.93), "Choanocyte", "left"), (F(0.6, 0.47), "Porocyte", "left")],
            left=15.4, gap=0.8)
AM.callouts(ax, [(F(0.84, 0.85), "Spicule", "right"), (F(0.8, 0.76), "Scleroblast", "right"), (F(0.93, 0.66), "Pinacocyte", "right"),
                 (F(0.76, 0.58), "Amoebocyte", "right"), (F(0.66, 0.535), "Mesohyl", "right"), (F(0.74, 0.19), "Oocyte", "right")],
            right=22.3, gap=0.7)
bx = wall.box
bio.label(ax, (bx[0] + 0.25 * bx[2], bx[1] + bx[3] + 0.35), "Inside", size="small", color=P.muted())
bio.label(ax, (bx[0] + 0.85 * bx[2], bx[1] + bx[3] + 0.35), "Outside", size="small", color=P.muted())

bio.panel(ax, "C", (24.4, 12.4))
ch = AM.Specimen("wikimedia/choanocyte", at=(27.0, 6.4), height=10.0)
ch.draw(ax)
cb = ch.box
AM.callouts(ax, [(ch.point("flagellum", where="top"), "Flagellum", "right"),
                 (ch.frac(0.62, 0.62), "Collar (microvilli)", "right"),
                 (ch.point("nucleus"), "Nucleus", "right"),
                 (ch.point("mitochondrion"), "Mitochondrion", "right")], left=cb[0] - 0.1, right=cb[0] + cb[2] + 0.1, gap=0.6)
