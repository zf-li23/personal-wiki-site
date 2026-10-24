"""The transmetalation step of three cross-couplings that share the Suzuki cycle (L = PPh3, Ar from
the aryl halide, R from the organometallic reagent). In each row the R-M electrons move to
palladium while the Pd-X electrons move toward the main-group metal, through a four-centre
bridged transition state, and R is transferred with retention of configuration (the trans
product isomerizes to cis before reductive elimination).
Kumada (M = MgBr) is the fastest but the Grignard reagent attacks carbonyl groups and nitriles;
Negishi (ZnCl) is slower and tolerates esters, nitriles and ketones; Stille (SnBu3) is neutral and
slowest, can pass through an open (associative) transition state in polar solvents, and moves the
groups on tin in the order alkynyl > alkenyl > aryl > alkyl, so only R is transferred."""

exec(open("cycle.txt").read())

s = Scheme()
rows = [("MgBr", "Mg", "Br", "Kumada: most reactive, no C=O, CN"),
        ("ZnCl", "Zn", "Cl", "Negishi: tolerates esters, nitriles, ketones"),
        ("SnBu$_3$", "Sn", "Bu$_3$", "Stille: neutral, slowest;\nalkynyl > alkenyl > aryl > alkyl")]
for k, (mlab, metal, rest, note) in enumerate(rows):
    y = -3.6 * k
    pd = complex_at(s, "Pd", [(90, "L"), (270, "L"), (180, "Ar"), (0, "X")], (0, y))
    rm = s.molecule(f"*[{metal}]*", coords=[(1.4, 1.2), (2.6, 1.2), (3.6, 1.2)],
                    at=(0, y), labels={0: "R", 1: metal, 2: rest})
    s.curly(rm.bond(0, 1), pd.atom(0), bend=0.5)
    s.curly(pd.bond(0, 4), rm.atom(1), bend=0.6)
    s.arrow((4.4, y), (5.8, y))
    x = 8.2
    complex_at(s, "Pd", [(90, "L"), (270, "L"), (180, "Ar"), (0, "R")], (x, y))
    s.plus((x + 1.9, y))
    s.text((x + 3.0, y), f"X$-${mlab}", size=13)
    s.text((x + 9.2, y), note, size=11)
s.draw()
