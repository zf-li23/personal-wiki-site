# Homology of amniote genital ducts: indifferent stage, male, female (vertskel.kidney_series). Not to scale.
import vertskel as vs

titles = ["A  Indifferent stage", "B  Male", "C  Female"]
fig, ax, boxes = vs.panels(3, 6.0, 8.4, titles=titles, ncols=3, legend_rows=2)
specs = [
    dict(stages={"pronephros": "absent", "mesonephros": "functional", "metanephros": "functional"}, gonad=True,
         ducts={"mullerian_duct": "functional"}, rename={"mesonephros": "mesonephros", "gonad": "bipotential gonad"}),
    dict(stages={"pronephros": "absent", "mesonephros": "modified", "metanephros": "functional"}, gonad=True, bladder=True,
         ducts={"mullerian_duct": "embryonic"},
         rename={"mesonephros": "epididymis", "archinephric_duct": "vas deferens", "gonad": "testis",
                 "mullerian_duct": "regressed (appendix testis)"}),
    dict(stages={"pronephros": "absent", "mesonephros": "embryonic", "metanephros": "functional"}, gonad=True, bladder=True,
         ducts={"archinephric_duct": "embryonic", "mullerian_duct": "functional"},
         rename={"mesonephros": "epoophoron (vestige)", "archinephric_duct": "Gartner's duct (vestige)", "gonad": "ovary",
                 "mullerian_duct": "oviduct, uterus, vagina"}),
]
for (x, y, w, h), sp in zip(boxes, specs):
    vs.kidney_series(ax, (x + 0.2, y), w - 1.4, h, **sp)
vs.legend(ax, [("mesonephros", "mesonephros and derivatives"), ("metanephros", "metanephros"),
               ("archinephric_duct", "Wolffian duct"), ("ureter", "ureter"), ("mullerian_duct", "Mullerian duct"),
               ("gonad", "gonad")], at=(0.6, 1.3), width=19, ncols=3)
