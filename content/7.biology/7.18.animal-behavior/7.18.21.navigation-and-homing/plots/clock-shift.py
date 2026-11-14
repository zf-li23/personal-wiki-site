"""Model: clock-shift experiments with homing pigeons (simulated vanishing bearings, after Schmidt-Koenig 1958 and
Wiltschko and Wiltschko). Pigeons are released at a site from which home lies due north (0 deg), around noon in
summer at mid latitude. Controls vanish homeward. Birds whose clock was advanced by 6 h (kept on a light-dark cycle
starting 6 h early for a week) think it is evening: they expect the sun in the west and, keeping the angle they
would use at that time, deviate counterclockwise by about 90 deg; birds delayed by 6 h deviate clockwise. Observed
deflections are often smaller than predicted because the birds also use a magnetic compass."""
import wikibio as bio
import wikibehav as wb

P = bio.P
fig, ax = bio.canvas(25, 9.4)
sets = [("Control", 5, "neutral", 0, None), ("Clock advanced 6 h", 275, "dna", 270, "predicted (-90°)"),
        ("Clock delayed 6 h", 80, "rna", 90, "predicted (+90°)")]
for k, (title, mean, tok, exp, et) in enumerate(sets):
    x = 4.3 + k * 8.2
    bio.panel(ax, "ABC"[k], (x - 4.0, 9.1))
    bio.label(ax, (x - 3.0, 8.8), title, size="small", bold=True, ha="left")
    wb.circular_plot(ax, (x, 4.6), 2.8, wb.vonmises(mean, 3.0, 16, seed=10 + k), token=tok, expected=0,
                     expected_text="home direction" if et is None else None)
