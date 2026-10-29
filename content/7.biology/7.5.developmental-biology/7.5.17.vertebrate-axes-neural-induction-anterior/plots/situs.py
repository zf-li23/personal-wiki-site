# Human visceral situs (schematic; heart, lungs, liver, stomach and spleen in frontal view, the patient's right on the
# viewer's left). Situs solitus: heart apex and stomach on the left, the larger part of the liver on the right, the right
# lung with three lobes and the left with two, one spleen on the left. Situs inversus totalis: a mirror image.
# Right isomerism (asplenia): both sides right-like, a symmetric midline liver, two trilobed lungs, no spleen. Left
# isomerism (polysplenia): both sides left-like, two bilobed lungs, several small spleens. Isomerism (heterotaxy) is
# usually accompanied by complex congenital heart disease.
import wikibio as bio

fig, ax = bio.canvas(24.0, 9.8)
P = bio.P
cols = [("Situs solitus", 3.0), ("Situs inversus", 9.0), ("Right isomerism", 15.0), ("Left isomerism", 21.0)]
for k, (title, cx) in enumerate(cols):
    ax.add_patch(bio.core.FancyBboxPatch((cx - 2.6, 0.9), 5.2, 7.6, boxstyle="round,pad=0,rounding_size=1.2",
                                         facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cytoplasm"), lw=1.0, zorder=1))
    bio.label(ax, (cx, 9.1), title, size="normal", bold=True)
    bio.label(ax, (cx - 2.3, 8.1), "R", size="tiny", color=P.muted())
    bio.label(ax, (cx + 2.3, 8.1), "L", size="tiny", color=P.muted())
    inv = k == 1
    s = -1 if inv else 1
    lobes_r = 3 if k in (0, 2) or (k == 1) else 2
    lobes_l = 2 if k in (0, 3) or (k == 1) else 3
    if k == 1:
        lobes_r, lobes_l = 2, 3
    for side, lobes in ((-1, lobes_r), (1, lobes_l)):
        x0 = cx + side * 1.25
        for j in range(lobes):
            h = 2.6 / lobes
            ax.add_patch(bio.core.FancyBboxPatch((x0 - 0.65, 6.0 - (j + 1) * h + 0.05 + 1.5), 1.3, h - 0.1,
                                                 boxstyle="round,pad=0,rounding_size=0.25", facecolor=P.fill("receptor"),
                                                 edgecolor=P.edge("receptor"), lw=0.7, zorder=3))
    bio.icon(ax, "servier/heart", at=(cx + s * 0.35, 5.6), height=1.4, flip=inv, zorder=5)
    if k == 2:
        bio.icon(ax, "servier/liver", at=(cx, 3.6), height=1.2, zorder=4)
    else:
        bio.icon(ax, "servier/liver", at=(cx - s * 0.7, 3.6), height=1.2, flip=inv, zorder=4)
    if k in (0, 1):
        bio.icon(ax, "servier/stomach", at=(cx + s * 1.3, 3.2), height=1.1, flip=inv, zorder=5)
        bio.icon(ax, "servier/spleen", at=(cx + s * 1.95, 2.2), height=0.6, flip=inv, zorder=5)
    elif k == 2:
        bio.icon(ax, "servier/stomach", at=(cx + 0.2, 2.1), height=0.9, zorder=5)
        bio.label(ax, (cx, 1.3), "no spleen", size="tiny", color=P.muted())
    else:
        bio.icon(ax, "servier/stomach", at=(cx - 0.3, 2.2), height=1.0, zorder=5)
        for j in range(4):
            bio.icon(ax, "servier/spleen", at=(cx + 1.2 + 0.35 * (j % 2), 1.7 + 0.35 * j), height=0.3, zorder=5)
        bio.label(ax, (cx, 1.2), "several spleens", size="tiny", color=P.muted())
bio.label(ax, (12.0, 0.35), "lung lobes drawn as segments: three on the right side, two on the left side in situs solitus", size="tiny",
          color=P.muted())
