"""Catalytic cycle of the Tsuji-Trost allylic alkylation with a soft nucleophile (L = PPh3, Nu- =
dimethyl malonate anion). Pd(0)L2 binds the alkene of the allylic acetate; oxidative addition
with loss of acetate occurs from the face opposite the leaving group (first inversion), giving the
cationic eta3-allyl complex; the soft nucleophile attacks a terminal allyl carbon from the face
opposite palladium (second inversion), giving the eta2 complex of the product, which is released.
Two inversions give overall retention; hard nucleophiles instead attack palladium first and are
delivered from the metal side (overall inversion)."""

exec(open("cycle.txt").read())

s = Scheme()
R = 5.6
complex_at(s, "Pd", [(180, "L"), (0, "L")], polar(R, 90), ox="0")
pa = complex_at(s, "Pd", [(180, "L"), (90, "L")], polar(R, 0) + np.array([-1.2, 0]), ox="0", ox_angle=225)
alkene(s, pa, 0, subst="CH$_2$OAc")
complex_at(s, "Pd", [(180, "L"), (0, "L"), (270, "$\\eta^3$-allyl", 0.1)], polar(R, -90) + np.array([0, 0.4]), ox="II")
s.text(polar(R, -90) + np.array([1.4, 1.3]), "+", size=13)
pn = complex_at(s, "Pd", [(0, "L"), (90, "L")], polar(R, 180) + np.array([1.2, 0]), ox="0", ox_angle=315)
alkene(s, pn, 180, subst="CH$_2$Nu")
cycle_arc(s, R, 76, 30, step="alkene\nbinding", enter="allyl acetate", leave="L")
cycle_arc(s, R, -24, -66, step="oxidative addition\n(inversion)", leave="AcO$^-$", step_r=R - 1.7)
cycle_arc(s, R, -114, -150, step="Nu$^-$ anti to Pd\n(inversion)", enter="Nu$^-$", step_r=R - 1.7)
cycle_arc(s, R, 154, 104, step="release", enter="L", leave="allyl$-$Nu", enter_at=0.25, leave_at=0.7)
s.text((0, 0), "Tsuji$-$Trost\n\nnet retention", size=13)
s.draw()
