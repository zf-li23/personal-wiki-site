"""Maternal-effect inheritance of shell coiling in the pond snail Lymnaea (dextral allele D dominant to sinistral d).
Each shell is drawn by Raup's coiling model, dextral (aperture on the right, apex up) or sinistral (mirror image, aperture on the left).
The coiling of every snail is set by the genotype of its mother: P dd female x DD male; F1 all Dd but sinistral;
F2 (self-fertilized F1) 1 DD : 2 Dd : 1 dd, all dextral; F3 broods of the F2 snails: three dextral broods to one
sinistral brood (from the dd F2 snails)."""

import wikibio as bio
from wikibio import zoomorph as zm

P = bio.P

fig, ax = bio.canvas(20.0, 9.0)


def shell(x, y, dextral, geno, size=1.5):
    zm.raup_shell(ax, (x, y), size, W=2.2, D=0.1, T=2.4, elev=12, hand=-1 if dextral else 1, azim=-25 if dextral else 205, n_theta=140, n_phi=18)
    bio.label(ax, (x, y - size * 0.72), geno, size="small", italic=True)


cols = [1.6, 5.4, 10.2, 16.2]
for x, t in zip(cols, ["P", "F1", "F2 (F1 selfed)", "F3 broods (F2 selfed)"]):
    bio.label(ax, (x, 8.4), t, size="normal", bold=True)

# P generation
shell(0.7, 6.0, False, "dd female")
shell(2.8, 6.0, True, "DD male")
bio.label(ax, (1.75, 6.0), "x", size="normal")
bio.label(ax, (1.6, 4.4), "sinistral x dextral", size="tiny", color=P.muted())
# F1
shell(5.4, 6.0, False, "Dd")
bio.label(ax, (5.4, 4.4), "sinistral: mother dd", size="tiny", color=P.muted())
bio.arrow(ax, (3.5, 6.0), (4.5, 6.0))
# F2
bio.arrow(ax, (6.3, 6.0), (7.7, 6.0))
for x, g in zip((8.4, 9.7, 11.0, 12.3), ("DD", "Dd", "Dd", "dd")):
    shell(x, 6.0, True, g, size=1.2)
bio.label(ax, (10.35, 4.4), "all dextral: mother Dd", size="tiny", color=P.muted())
# F3: one brood per F2 snail
bio.arrow(ax, (13.1, 6.0), (14.1, 6.0))
for i, (g, dex) in enumerate((("DD", True), ("Dd", True), ("Dd", True), ("dd", False))):
    y = 7.2 - i * 1.55
    bio.label(ax, (14.6, y), f"{g} mother:", size="tiny", ha="left")
    for k in range(3):
        zm.raup_shell(ax, (16.6 + k * 0.85, y), 0.75, W=2.2, D=0.1, T=2.4, elev=12, hand=-1 if dex else 1, azim=-25 if dex else 205,
                      n_theta=100, n_phi=14)
    bio.label(ax, (19.1, y), "dextral" if dex else "sinistral", size="tiny")
bio.label(ax, (17.0, 0.6), "3 dextral : 1 sinistral broods", size="small")
bio.label(ax, (6.5, 1.6), "Each snail's coiling = phenotype dictated by its mother's genotype "
          "(maternal-effect gene, D dominant)", size="small")
