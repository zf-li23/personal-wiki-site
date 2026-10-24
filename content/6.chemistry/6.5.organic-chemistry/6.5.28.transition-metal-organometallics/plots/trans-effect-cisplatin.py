"""Synthesis of the two isomers of [PtCl2(NH3)2] controlled by the trans effect (Cl- > NH3).
Top: from [PtCl4]2-, the first NH3 replaces any chloride; the second replaces a chloride trans to
chloride (the ligand trans to NH3 is held more firmly), so the two NH3 end up cis: cisplatin.
Bottom: from [Pt(NH3)4]2+, the first Cl- replaces any NH3; the second enters trans to that chloride,
giving the trans isomer, which has no anticancer activity. The ligand labelled with an asterisk is
the one replaced in the next step."""

exec(open("helpers.txt").read())

s = Scheme()


def sq(x, y, l, r, u, d, charge):
    complex_at(s, "Pt", [(180, l), (0, r), (90, u), (270, d)], at=(x, y))
    if charge:
        s.text((x + 1.7, y + 1.4), charge, size=12)


sq(0, 0, "Cl", "Cl", "Cl", "Cl*", "2$-$")
s.arrow((2.4, 0), (3.8, 0), above="NH$_3$", below="$-$Cl$^-$")
sq(6.4, 0, "Cl", "Cl*", "Cl", "NH$_3$", "$-$")
s.text((6.4, -2.2), "Cl trans to Cl is labile", size=11)
s.arrow((8.9, 0), (10.3, 0), above="NH$_3$", below="$-$Cl$^-$")
sq(12.9, 0, "Cl", "H$_3$N", "Cl", "NH$_3$", None)
s.text((12.9, -2.2), "cis (cisplatin)", size=12)

y = -5.2
sq(0, y, "H$_3$N", "NH$_3$", "NH$_3$", "NH$_3$*", "2+")
s.arrow((2.6, y), (4.0, y), above="Cl$^-$", below="$-$NH$_3$")
sq(6.6, y, "H$_3$N", "NH$_3$", "NH$_3$*", "Cl", "+")
s.text((6.6, y - 2.2), "NH$_3$ trans to Cl is labile", size=11)
s.arrow((9.2, y), (10.6, y), above="Cl$^-$", below="$-$NH$_3$")
sq(13.2, y, "H$_3$N", "NH$_3$", "Cl", "Cl", None)
s.text((13.2, y - 2.2), "trans", size=12)
s.draw()
