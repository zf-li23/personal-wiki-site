# The kidney series (vertskel.kidney_series): one side, anterior up. Not to scale.
import vertskel as vs

titles = ["A  Holonephros (hypothetical)", "B  Anamniote larva", "C  Anamniote adult male", "D  Amniote embryo",
          "E  Amniote adult male"]
fig, ax, boxes = vs.panels(5, 4.6, 8.0, titles=titles, ncols=5, legend_rows=2)
specs = [
    dict(stages={"pronephros": "functional", "mesonephros": "functional"}, opisthonephros=True,
         ducts={"ureter": "absent"}, rename={"pronephros": "segmental nephrons", "opisthonephros": "holonephros"}),
    dict(stages={"pronephros": "functional", "mesonephros": "embryonic"}, opisthonephros=True, ducts={"ureter": "absent"}),
    dict(stages={"pronephros": "absent", "mesonephros": "functional"}, opisthonephros=True, gonad=True,
         ducts={"ureter": "absent"}, rename={"archinephric_duct": "duct: urine, sperm"}),
    dict(stages={"pronephros": "embryonic", "mesonephros": "functional", "metanephros": "functional"},
         ducts={"mullerian_duct": "embryonic"}),
    dict(stages={"pronephros": "absent", "mesonephros": "modified", "metanephros": "functional"}, gonad=True, bladder=True,
         rename={"mesonephros": "epididymis", "archinephric_duct": "vas deferens"}),
]
for (x, y, w, h), sp in zip(boxes, specs):
    vs.kidney_series(ax, (x + 0.2, y), w - 0.6, h, **sp)
vs.legend(ax, [("pronephros", "pronephros"), ("mesonephros", "mesonephros / opisthonephros / epididymis"),
               ("metanephros", "metanephros"), ("archinephric_duct", "archinephric (Wolffian) duct / vas deferens"),
               ("ureter", "ureter"), ("mullerian_duct", "Mullerian duct"), ("gonad", "gonad"), ("cloaca", "cloaca")],
          at=(0.6, 1.3), width=24, ncols=4)
