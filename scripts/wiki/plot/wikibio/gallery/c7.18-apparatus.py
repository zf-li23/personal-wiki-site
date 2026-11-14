# wikibehav sample (7.18): apparatus. Rendered with render_plot.py like any plot script.
import wikibio as bio
import wikibehav as wb

P = bio.P
fig, ax = bio.canvas(34, 18)
bio.panel(ax, "A", (0.2, 17.8)); bio.label(ax, (1.2, 17.5), "T-maze", size="small", bold=True, ha="left")
m = wb.t_maze(ax, (4.5, 15.0), arm=2.6, stem=4.0, width=0.8, reward="right")
bio.panel(ax, "B", (9.0, 17.8)); bio.label(ax, (10.0, 17.5), "Y-maze", size="small", bold=True, ha="left")
wb.y_maze(ax, (12.8, 13.4), arm=2.8, width=0.8, reward="left")
bio.panel(ax, "C", (17.5, 17.8)); bio.label(ax, (18.5, 17.5), "Radial-arm maze", size="small", bold=True, ha="left")
r = wb.radial_maze(ax, (21.8, 12.6), arm=2.6, n=8, width=0.6, baited=(0, 2, 5, 7), visited=(2, 5))
bio.panel(ax, "D", (26.5, 17.8)); bio.label(ax, (27.5, 17.5), "Elevated plus maze", size="small", bold=True, ha="left")
wb.plus_maze(ax, (30.2, 12.8), arm=2.6, width=0.7)
bio.panel(ax, "E", (0.2, 8.6)); bio.label(ax, (1.2, 8.3), "Morris water maze", size="small", bold=True, ha="left")
for k, (kind, x) in enumerate((("search", 5.2), ("direct", 13.6))):
    path = wb.swim_path((45, 0.5), start=200, kind=kind, seed=k + 2)
    w = wb.water_maze(ax, (x, 4.0), 3.2, platform=(45, 0.5), path=path, cues=k == 0)
    bio.label(ax, (x, 0.3), "trial 1" if k == 0 else "trial 10", size="tiny", color=P.muted())
bio.panel(ax, "F", (19.0, 8.6)); bio.label(ax, (20.0, 8.3), "Operant chamber", size="small", bold=True, ha="left")
b = wb.operant_box(ax, (24.5, 4.0), w=7.5, h=5.0, key=True, speaker=True)
bio.icon(ax, "phylopic/rat", at=b["inside"], height=1.3, anchor="bottom", color="animal")
for k, (txt, xy) in enumerate((("cue light", (27.0, 7.4)), ("lever", (24.4, 4.9)), ("food magazine", (23.6, 0.6)),
                                ("pellet dispenser", (31.0, 7.6)), ("key", (24.4, 6.2)), ("grid floor", (21.0, 0.6)))):
    key = ["light", "lever", "magazine", "dispenser", "key", "floor"][k]
    bio.callout(ax, b[key], xy, txt, size="tiny")
