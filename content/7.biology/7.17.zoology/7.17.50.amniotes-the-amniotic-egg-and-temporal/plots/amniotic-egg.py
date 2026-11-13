# The amniotic egg of a bird (chicken, about day 5-6 of incubation) in section, and the germ layers of the
# four extraembryonic membranes (after Gilbert, Pough et al. 2023 and Kardong 2019). The amnion and chorion
# form from the somatopleure (ectoderm + somatic mesoderm), the yolk sac and allantois from the splanchnopleure
# (endoderm + splanchnic mesoderm); the allantois later fuses with the chorion as the chorioallantoic
# membrane, the respiratory surface under the shell. Schematic, not to scale.
import wikibio as bio
from wikibio import embryology as E
from wikibio import animalmorph as AM

P = bio.P
fig, ax = bio.canvas(27.5, 11)
a = E.amniote_egg(ax, (6.6, 5.6), r=3.6)
bio.callout(ax, a["shell"], (0.4, 9.4), "Shell (calcite, with pores)")
bio.callout(ax, a["chorion"], (12.6, 10.4), "Chorion")
bio.callout(ax, a["amnion"], (0.4, 7.8), "Amnion")
bio.callout(ax, a["amniotic_cavity"], (3.0, 10.4), "Amniotic cavity")
bio.callout(ax, a["embryo"], (8.6, 10.4), "Embryo")
bio.callout(ax, a["allantois"], (12.9, 7.2), "Allantois")
bio.callout(ax, a["yolk_sac"], (0.4, 5.6), "Yolk sac")
bio.callout(ax, a["yolk"], (6.6, 0.4), "Yolk")
bio.callout(ax, a["albumen"], (0.4, 2.2), "Albumen")

rows = [["Membrane", "Germ layers", "Origin", "Function"],
        ["Amnion", "ectoderm + mesoderm", "somatopleure fold", "fluid cushion around embryo"],
        ["Chorion", "ectoderm + mesoderm", "somatopleure fold", "outer envelope; forms chorioallantois"],
        ["Allantois", "endoderm + mesoderm", "hindgut outgrowth", "stores uric acid; vascularizes chorion"],
        ["Yolk sac", "endoderm + mesoderm", "midgut wall", "absorbs and transports yolk"]]
AM.table(ax, (14.4, 9.4), col_w=[2.0, 3.1, 2.7, 6.4], row_h=[0.8] + [1.1] * 4, cells=rows, size="tiny")
bio.label(ax, (20.5, 3.0), "Gas exchange: O2 in, CO2 and water vapour out through ~10 000 shell pores",
          size="tiny", color=P.muted())
