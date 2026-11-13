# Fate of the pharyngeal arch skeleton, element by element, in six vertebrates (shark, teleost, frog, lizard,
# bird, mammal). Each cell is coloured with the course-wide vertskel homology colour of its element; grey cells:
# element absent or lost. Summarized from Kardong (2019), Goodrich (1930), de Beer (1937) and Yang & Cheng; the laryngeal
# rows (arches 4-6) are uncertain homologies.
import wikibio as bio
import vertskel as vs

P = bio.P
rows = [
    ("1 palatoquadrate, front", "epipterygoid", ["palatoquadrate", "autopalatine", "cartilage", "epipterygoid", None, "alisphenoid"]),
    ("1 palatoquadrate, back", "quadrate", ["palatoquadrate", "quadrate", "quadrate", "quadrate", "quadrate", "incus"]),
    ("1 Meckel's, back", "articular", ["Meckel's cartilage", "articular", "articular (cart.)", "articular", "articular", "malleus"]),
    ("1 Meckel's, front", "meckel", ["Meckel's cartilage", "jaw core", "mentomeckelian", "jaw core", None, "ligament"]),
    ("2 hyomandibula", "hyomandibula", ["hyomandibula", "hyomandibula", "stapes", "columella", "columella", "stapes"]),
    ("2 symplectic, interhyal", "symplectic", [None, "symplectic", None, "extracolumella", "extracolumella", None]),
    ("2 ceratohyal", "ceratohyal", ["ceratohyal", "ceratohyal", "hyoid horn", "hyoid horn", None, "styloid, lesser horn"]),
    ("2 basihyal", "basihyal", ["basihyal", "basihyal", "hyoid body", "hyoid body", "entoglossum", "hyoid body"]),
    ("3", "arch_3", ["gill arch", "gill arch", "hyoid process", "hyoid horn", "long hyoid horn", "greater horn"]),
    ("4", "arch_4", ["gill arch", "gill arch", "larynx", "larynx", "larynx", "thyroid cartilage"]),
    ("5", "arch_5", ["gill arch", "gill arch", None, None, None, None]),
    ("6", "arch_6", ["gill arch", "gill arch", "larynx", "larynx", "larynx", "cricoid, arytenoid"]),
    ("7", "arch_7", ["gill arch", "pharyngeal jaw", None, None, None, None]),
]
taxa = ["Shark", "Teleost", "Frog", "Lizard", "Bird", "Mammal"]
cw, ch, x0 = 3.6, 0.82, 5.6
H = len(rows) * ch + 2.0
fig, ax = bio.canvas(x0 + cw * len(taxa) + 0.4, H + 0.4)
top = H - 0.9
for j, t in enumerate(taxa):
    bio.label(ax, (x0 + cw * (j + 0.5), top + 0.45), t, size="small", bold=True)
for i, (rl, key, cells) in enumerate(rows):
    y = top - (i + 1) * ch
    bio.label(ax, (0.2, y + ch / 2), rl, size="tiny", ha="left")
    for j, c in enumerate(cells):
        x = x0 + cw * j
        pts = vs.poly([(x + 0.06, y + 0.06), (x + cw - 0.06, y + 0.06), (x + cw - 0.06, y + ch - 0.06), (x + 0.06, y + ch - 0.06)])
        if c is None:
            vs.bone(ax, key, pts, state="context")
            bio.label(ax, (x + cw / 2, y + ch / 2), "absent", size="tiny", color=P.muted())
        else:
            vs.bone(ax, key, pts)
            bio.label(ax, (x + cw / 2, y + ch / 2), c, size="tiny", color=P.on_fill())
for yy, lab in ((top - 4 * ch, ""), (top - 8 * ch, "")):
    ax.plot([0.2, x0 + cw * len(taxa)], [yy, yy], color=P.muted(), lw=0.8)
bio.label(ax, (0.2, top + 0.45), "arch and element", size="tiny", bold=True, ha="left")
