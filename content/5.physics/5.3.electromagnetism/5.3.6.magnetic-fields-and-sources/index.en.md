---
title: Magnetic Fields and Their Sources
description: The connection between magnetic phenomena and moving charges, the Lorentz force and the magnetic flux density, magnetic field lines, magnetic flux and Gauss's law for magnetism, the Biot–Savart law and its applications (straight wires, current loops and magnetic dipoles, Helmholtz coils, solenoids, moving charges), Ampère's circuital law and its applications, polar and axial vectors, displacement current and the Ampère–Maxwell law.
source_hash: bf15ff1a9a4e
---

The previous five chapters studied the electric fields of static charges and **steady currents**. This chapter turns to another effect of electric current, the magnetic field. In 1820 Ørsted discovered that an electric current deflects a compass needle, and within half a year it was recognized that all magnetic phenomena originate in the motion of electric charges: a magnetic field is produced by moving charges (currents) and exerts forces only on moving charges. The basic quantity describing a magnetic field is the magnetic flux density $\boldsymbol{B}$, which is defined through the Lorentz force on a moving charge; the law by which currents produce magnetic fields is the Biot–Savart law. From it follow the two fundamental theorems of the magnetic field, which are exactly "complementary" to the two fundamental theorems of the electrostatic field ([5.3.1](/5.3.1), [5.3.2](/5.3.2)):

| | Electrostatic field $\boldsymbol{E}$ | Steady magnetic field $\boldsymbol{B}$ |
|---|---|---|
| Flux | $\oint\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S} = q_{\mathrm{enc}}/\varepsilon_0$, has sources | $\oint\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S} = 0$, no sources |
| Circulation | $\oint\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l} = 0$, no curl | $\oint\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = \mu_0I_{\mathrm{enc}}$, has curl |

In the language of field theory, the electrostatic field is an **irrotational vector field** and the steady magnetic field is a **solenoidal vector field** ([2.2.14](/2.2.14)). The last section explains that Ampère's circuital law holds only for steady currents, and that Maxwell generalized it by introducing the displacement current: a changing electric field also produces a magnetic field. This is the key step toward Maxwell's equations ([5.3.10](/5.3.10)). The next chapter, [5.3.7](/5.3.7), studies the action of the magnetic field on moving charges and currents.

## 6.1. Magnetic Force and the Motion of Charges

### 6.1.1. Early Magnetic Phenomena

That a lodestone attracts iron has been known since antiquity; the *Guanzi* already records that "where there is lodestone above, there is copper and gold below", and the compass is an important ancient Chinese invention. The basic magnetic phenomena are these: a magnet attracts iron, cobalt, nickel and similar substances; a magnet has N and S poles, with like poles repelling and unlike poles attracting; and if a magnet is cut in two, each piece still has its own N and S poles, so an isolated pole has never been obtained.

Connections between electricity and magnetism were also observed sporadically: lightning magnetized steel knives and forks (1731), and the discharge of a Leyden jar magnetized sewing needles (Franklin, 1751). Yet until the early nineteenth century, Coulomb, Ampère and others still regarded electricity and magnetism as two unrelated kinds of phenomena, and the two subjects developed independently.

### 6.1.2. Ørsted's Experiment

In 1820 the Danish physicist Ørsted discovered that a compass needle near a current-carrying wire is deflected, revealing the magnetic effect of electric current; placing glass, metal, wood or water between the needle and the wire did not weaken the deflection. This discovery opened a new era of electromagnetism. Within the same year Ampère studied the action of a circular current on a magnetic needle and the interaction between two parallel straight wires, and found that a current-carrying solenoid is equivalent to a bar magnet; Arago found that steel is magnetized by an electric current; and Biot and Savart measured the action of a long straight wire on a magnetic needle. Only half a year passed from Ørsted's discovery to a fairly systematic understanding of magnetic phenomena.

Experiments show the following kinds of magnetic interaction: a current-carrying wire acting on a magnetic needle, a magnet acting on a current-carrying wire, current-carrying wires acting on each other, and a magnet acting on moving electrons (such as cathode rays). What they have in common is that at least one party involves the motion of charge.

### 6.1.3. The Magnetic Charge Hypothesis and Ampère's Molecular Currents

One explanation introduces, by analogy with electric charge, a "magnetic charge" $Q_{\mathrm{m}}$, and assumes an inverse-square force between magnetic charges, $\boldsymbol{F}_{21} = k\dfrac{Q_{\mathrm{m}1}Q_{\mathrm{m}2}}{r^2}\boldsymbol{e}_{r}$. In 1931 Dirac argued from quantum mechanics that if *magnetic monopoles*, that is, isolated magnetic charges, exist, then electric charge must be quantized. To this day, however, there is no conclusive experimental evidence for the existence of magnetic monopoles. Some condensed-matter systems (such as spin ice) host quasiparticle excitations that behave like magnetic monopoles, but they are not elementary particles.

Another explanation is Ampère's hypothesis of molecular currents: inside the molecules of a magnet there are circulating currents (molecular currents), and each molecule acts as a tiny magnet. In a nonmagnetic material the orientations of the molecular currents are random and their magnetic fields cancel; in a magnetic material the molecular currents are roughly aligned, and magnetic poles appear at the two ends. The molecular-current hypothesis naturally explains the similarity between a bar magnet and a current-carrying solenoid, and also why isolated poles cannot be cut out. On this view all magnetic interactions reduce to interactions between currents (moving charges): the motion of charge is the origin of all magnetic phenomena. Hence, as in electrostatics, it suffices to find the law by which currents produce magnetic fields and the law of the force of a magnetic field on currents in order to solve problems of magnetic interaction. The microscopic nature of molecular currents (the orbital motion and spin of electrons) can be explained only in quantum mechanics ([5.3.8](/5.3.8), [5.5.4](/5.5.4)).

## 6.2. The Magnetic Field and the Magnetic Flux Density

### 6.2.1. The Magnetic Field

Just as charges interact through the electric field, the magnetic interaction between currents is transmitted by the magnetic field: a current (moving charge) produces a magnetic field in the surrounding space, and the magnetic field exerts a force on other currents (moving charges) in it. Like the electric field, the magnetic field is a form of existence of matter and carries energy and momentum: it exerts forces on moving charges, and when a current-carrying wire is moved in a magnetic field, the magnetic force does work on the wire. Around a moving charge there is both an electric field and a magnetic field.

### 6.2.2. The Magnetic Flux Density

The physical quantity describing the magnetic field is defined through the force on a moving charge. Experiments show that when a charge $q$ passes a point in a magnetic field with velocity $\boldsymbol{v}$:

- the magnetic force on it is always perpendicular to $\boldsymbol{v}$, and its magnitude is proportional to $q$ and $v$;
- the magnitude of the magnetic force depends on the direction of $\boldsymbol{v}$: it vanishes for motion along one particular direction and is largest for motion perpendicular to that direction.

**Definition 6.2.1 (Magnetic Flux Density)** The direction along which a moving charge experiences no magnetic force is the direction of the **magnetic flux density** $\boldsymbol{B}$ at that point (the sense is fixed by the formula below); if $F_{\max}$ is the maximum magnetic force on a charge moving perpendicular to this direction, the magnitude of $\boldsymbol{B}$ is

$$
B = \frac{F_{\max}}{qv} .
$$
The unit of magnetic flux density is the tesla, $1\,\mathrm{T} = 1\,\mathrm{N\,A^{-1}\,m^{-1}}$.

These experimental facts combine into a single formula:

**Definition 6.2.2 (Lorentz Force)** The magnetic force on a charge $q$ moving with velocity $\boldsymbol{v}$ in a magnetic field of flux density $\boldsymbol{B}$,

$$
\boldsymbol{F} = q\boldsymbol{v}\times\boldsymbol{B}
$$
is called the **Lorentz force**. When an electric field is also present, the electromagnetic force on the charge is $\boldsymbol{F} = q(\boldsymbol{E} + \boldsymbol{v}\times\boldsymbol{B})$.

Since $\boldsymbol{v}\times\boldsymbol{B}$ is a **cross product**, the Lorentz force is always perpendicular to the velocity and does no work on the charge. The CGS unit often seen in the literature, the gauss, is related to the tesla by $1\,\mathrm{T} = 10^4\,\mathrm{G}$; this course uses SI units throughout. Some typical magnetic flux densities:

| Situation | $B/\mathrm{T}$ |
|---|---|
| Earth's field at the surface | $(3$–$6)\times10^{-5}$ |
| Refrigerator magnet | about $5\times10^{-3}$ |
| Clinical magnetic resonance imaging | $1.5$–$3$ (research systems reach $7$ and above) |
| Strongest steady field in a laboratory | about $45$ |
| Surface of a neutron star | $10^{6}$–$10^{9}$, up to $10^{11}$ for a magnetar |

**Property 6.2.1 (Superposition Principle for Magnetic Fields)** When several sources are present, the magnetic flux density at a field point is the vector sum of the flux densities that each source would produce there alone: $\boldsymbol{B} = \sum_i\boldsymbol{B}_i$, or $\boldsymbol{B} = \int\mathrm{d}\boldsymbol{B}$.

### 6.2.3. Magnetic Field Lines and Magnetic Flux

**Definition 6.2.3 (Magnetic Field Lines)** Draw in a magnetic field a family of curves such that the tangent at every point is along $\boldsymbol{B}$ at that point, and such that the number of curves crossing a unit area perpendicular to $\boldsymbol{B}$ equals the magnitude $B$ there. These curves are called **magnetic field lines**.

The field lines of a straight current, a circular current, a straight solenoid and a toroidal solenoid show that no two field lines intersect; that field lines are related to the current by the right-hand rule; and that field lines are closed curves with neither beginning nor end, circling the current (Section 6.3 plots the field lines of a circular current).

**Definition 6.2.4 (Magnetic Flux)** The flux of the magnetic flux density through a surface $S$,

$$
\Phi = \int_S\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S}
$$
is called the **magnetic flux** through $S$. Its unit is the weber, $1\,\mathrm{Wb} = 1\,\mathrm{T\,m^2}$. It equals the number of field lines passing through $S$.

### 6.2.4. Gauss's Law for Magnetism

The Biot–Savart law in the next section shows that the field lines of each current element are concentric circles centered on the axis of the element; they are closed curves, so the magnetic flux of the field of one current element through any closed surface is zero. By the superposition principle, for the magnetic field of any current:

**Theorem 6.2.1 (Gauss's Law for Magnetism)** The magnetic flux through any closed surface is identically zero:

$$
\oint_S\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S} = 0,\qquad \nabla\cdot\boldsymbol{B} = 0 .
$$
The differential form follows from the **divergence theorem**.

The magnetic field is a **solenoidal vector field**: it has no "sources" from which field lines emerge or into which they disappear, in agreement with the fact that no magnetic monopole has been found. If magnetic monopoles are discovered in the future, a magnetic-charge term must be added on the right. Since $\nabla\cdot\boldsymbol{B} = 0$, $\boldsymbol{B}$ can always be written as the **curl** of another vector field, $\boldsymbol{B} = \nabla\times\boldsymbol{A}$, where $\boldsymbol{A}$ is called the vector potential (the field-line plot of the circular current in Section 6.3 is drawn using the vector potential).

## 6.3. The Biot–Savart Law

Regard a current as made up of current elements $I\,\mathrm{d}\boldsymbol{l}$ ($\mathrm{d}\boldsymbol{l}$ along the direction of the current); first find the field produced by each element, then find the total field by the superposition principle. The experiments of Biot and Savart, analyzed mathematically by Laplace, give the magnetic field of a current element:

**Theorem 6.3.1 (Biot–Savart Law)** The magnetic flux density produced by a current element $I\,\mathrm{d}\boldsymbol{l}$ at the position $\boldsymbol{r}$ (pointing from the element to the field point) is

$$
\mathrm{d}\boldsymbol{B} = \frac{\mu_0}{4\pi}\frac{I\,\mathrm{d}\boldsymbol{l}\times\boldsymbol{e}_r}{r^2},
$$
where $\boldsymbol{e}_r = \boldsymbol{r}/r$ and $\mu_0$ is called the *vacuum permeability*.

The field lines of a current element lie in planes perpendicular to the element and are concentric circles centered on its axis, with the sense related to the current by the right-hand rule. $\mathrm{d}B$ is inversely proportional to $r^2$ and proportional to $\sin\theta$ ($\theta$ being the angle between $\mathrm{d}\boldsymbol{l}$ and $\boldsymbol{r}$); along the extension of the element, $\mathrm{d}\boldsymbol{B} = \boldsymbol{0}$. In principle, the Biot–Savart law together with the superposition principle gives the magnetic field of any current distribution:

$$
\boldsymbol{B} = \frac{\mu_0}{4\pi}\int_L\frac{I\,\mathrm{d}\boldsymbol{l}\times\boldsymbol{e}_r}{r^2} .
$$

**Remark** Before the 2019 revision of the SI, the ampere was defined through the force between parallel wires, and $\mu_0 = 4\pi\times10^{-7}\,\mathrm{N\,A^{-2}}$ was exact. After the revision the **elementary charge** $e$ is fixed instead and $\mu_0$ becomes an experimentally determined quantity, $\mu_0 = 1.256\,637\,061\,27(20)\times10^{-6}\,\mathrm{N\,A^{-2}}$, which differs from $4\pi\times10^{-7}$ only in the tenth significant digit, so $4\pi\times10^{-7}\,\mathrm{N\,A^{-2}}$ may still be used in calculations. The relation $\varepsilon_0\mu_0 = 1/c^2$ still holds exactly.

### 6.3.1. Ampère's Law and Newton's Third Law

Combining the Biot–Savart law with the Lorentz force (for a current element, $\mathrm{d}\boldsymbol{F} = I\,\mathrm{d}\boldsymbol{l}\times\boldsymbol{B}$, [5.3.7](/5.3.7)) gives the force between two isolated current elements (Ampère's law):

$$
\mathrm{d}\boldsymbol{F}_{12} = I_2\,\mathrm{d}\boldsymbol{l}_2\times\Big(\frac{\mu_0}{4\pi}\frac{I_1\,\mathrm{d}\boldsymbol{l}_1\times\boldsymbol{e}_{12}}{r_{12}^2}\Big),
$$
where $\mathrm{d}\boldsymbol{F}_{12}$ is the force of element 1 on element 2 and $\boldsymbol{e}_{12}$ points from 1 to 2. Ampère's law has the same standing as the Biot–Savart law.

In general $\mathrm{d}\boldsymbol{F}_{12} \ne -\mathrm{d}\boldsymbol{F}_{21}$. For example, if the two elements are perpendicular to each other and $I_1\,\mathrm{d}\boldsymbol{l}_1$ lies along the line joining them, then $\mathrm{d}\boldsymbol{B}_1$ vanishes at element 2, so $\mathrm{d}\boldsymbol{F}_{12} = \boldsymbol{0}$ while $\mathrm{d}\boldsymbol{F}_{21} \ne \boldsymbol{0}$: the forces between two current elements do not obey **Newton's third law**. This does not contradict the **law of conservation of momentum**. The interaction between charges and currents is transmitted by the electromagnetic field rather than acting at a distance, and the field itself carries momentum ([5.3.10](/5.3.10)); it can be shown that the momentum of the sources plus the momentum of the field is conserved. The law of conservation of momentum is therefore more general, and Newton's third law is only its form within mechanics ([5.1.3](/5.1.3)). For two closed steady current loops, the mutual force still obeys Newton's third law.

The Biot–Savart law and Ampère's law summarize experiments but cannot be verified directly, because an isolated steady current element does not exist (a steady current must close on itself, [5.3.5](/5.3.5)). What can be verified directly is only their integrals over closed loops.

### 6.3.2. Applications

**Example 6.3.1 (Magnetic Field of a Straight Current-Carrying Wire)** Find the magnetic flux density produced by a straight wire segment $A_1A_2$ carrying current $I$ at a point $P$ at distance $r_0$ from the wire.

**Solution** The $\mathrm{d}\boldsymbol{B}$ produced at $P$ by all current elements have the same direction (perpendicular to the plane containing the wire and $P$, related to the current by the right-hand rule), so only the magnitudes need to be added. Let $\theta$ be the angle between the line from the element $I\,\mathrm{d}l$ to $P$ and the direction of the current, and take the foot $O$ of the perpendicular from $P$ to the wire as origin; then $l = -r_0\cot\theta$, $\mathrm{d}l = \dfrac{r_0\,\mathrm{d}\theta}{\sin^2\theta}$, $r = \dfrac{r_0}{\sin\theta}$, and

$$
B = \int\frac{\mu_0}{4\pi}\frac{I\,\mathrm{d}l\sin\theta}{r^2} = \frac{\mu_0I}{4\pi r_0}\int_{\theta_1}^{\theta_2}\sin\theta\,\mathrm{d}\theta = \frac{\mu_0I}{4\pi r_0}(\cos\theta_1 - \cos\theta_2),
$$
where $\theta_1$ and $\theta_2$ are the values of $\theta$ at the start $A_1$ and end $A_2$ of the wire. For an infinitely long wire, $\theta_1 = 0$ and $\theta_2 = \pi$; for a semi-infinite wire with $P$ on the perpendicular through the end point, $\theta_1 = \pi/2$ and $\theta_2 = \pi$:

$$
B_\infty = \frac{\mu_0I}{2\pi r_0},\qquad B_{\text{semi}} = \frac{\mu_0I}{4\pi r_0} .
$$

**Example 6.3.2 (Field on the Axis of a Circular Current)** A circular current $I$ of radius $R$; find the magnetic flux density on its axis at distance $x$ from the center.

**Solution** Every current element $I\,\mathrm{d}l$ on the ring is perpendicular to the line from it to the field point, so $\mathrm{d}B = \dfrac{\mu_0I\,\mathrm{d}l}{4\pi r^2}$ with $r^2 = R^2 + x^2$. By axial symmetry the components of $\mathrm{d}\boldsymbol{B}$ perpendicular to the axis cancel, leaving only the component along the axis, $\mathrm{d}B_\parallel = \mathrm{d}B\cdot\dfrac Rr$:

$$
B = \oint\frac{\mu_0I}{4\pi r^2}\frac Rr\,\mathrm{d}l = \frac{\mu_0IR}{4\pi r^3}\cdot2\pi R = \frac{\mu_0IR^2}{2(R^2 + x^2)^{3/2}},
$$
directed along the axis and related to the current by the right-hand rule. At the center, $B = \dfrac{\mu_0I}{2R}$.

Far away ($x \gg R$), $B \approx \dfrac{\mu_0IR^2}{2x^3}$, which has the same form as the **electric field strength** $E = \dfrac{p}{2\pi\varepsilon_0x^3}$ on the axis of an **electric dipole**. Introduce the vector $\boldsymbol{m} = IS\boldsymbol{e}_{\mathrm{n}}$ ($S = \pi R^2$ is the area enclosed by the current and $\boldsymbol{e}_{\mathrm{n}}$ is the unit normal related to the current by the right-hand rule), called the magnetic moment of the coil; then $\boldsymbol{B} = \dfrac{\mu_0\boldsymbol{m}}{2\pi x^3}$.

**Definition 6.3.1 (Magnetic Dipole)** A current-carrying coil whose size is much smaller than the distance from it to the field point is called a **magnetic dipole**; its magnetic properties are completely described by the magnetic moment $\boldsymbol{m} = IS\boldsymbol{e}_{\mathrm{n}}$ ([5.3.7](/5.3.7)). Far away, its magnetic field has the same form as the electric field of an electric dipole:

$$
\boldsymbol{B} = \frac{\mu_0}{4\pi}\Big(\frac{3(\boldsymbol{m}\cdot\boldsymbol{r})\boldsymbol{r}}{r^5} - \frac{\boldsymbol{m}}{r^3}\Big),\qquad
\boldsymbol{E} = \frac{1}{4\pi\varepsilon_0}\Big(\frac{3(\boldsymbol{p}\cdot\boldsymbol{r})\boldsymbol{r}}{r^5} - \frac{\boldsymbol{p}}{r^3}\Big) .
$$

Near the coil the two are entirely different: the **electric field lines** of an electric dipole start on the positive charge and end on the negative charge, whereas the magnetic field lines of a circular current pass through the coil and close on themselves. The figure below computes the field lines of a circular current exactly with elliptic integrals; far away they have the same shape as the electric field lines of an electric dipole.

![Magnetic field lines of a circular current (radius $a$) in a plane containing the axis: the field lines pass through the loop and have neither beginning nor end, and far away they approach the field of a magnetic dipole; the two symbols on the left and right indicate current flowing out of and into the page](./plots/current-loop-field-lines.py)

**Example 6.3.3 (Helmholtz Coils)** Two coaxial circular coils of radius $R$ with $N$ turns each carry the same current $I$ in the same sense, and their separation equals the radius $R$. Find the magnetic flux density at the center of each coil and at the midpoint between the coils.

**Solution** On the axis the fields of the two coils point the same way. By Example 6.3.2, the field at the center of one coil is its own $\frac{\mu_0NI}{2R}$ plus the field of the other coil at distance $R$:

$$
B_0 = \frac{\mu_0NI}{2R} + \frac{\mu_0NIR^2}{2(R^2 + R^2)^{3/2}} = \frac{\mu_0NI}{2R}\Big(1 + \frac{1}{2\sqrt2}\Big) \approx 0.677\frac{\mu_0NI}{R} .
$$
The midpoint $P$ is at distance $R/2$ from both coils:

$$
B_P = 2\cdot\frac{\mu_0NIR^2}{2\big(R^2 + (R/2)^2\big)^{3/2}} = \frac{8\mu_0NI}{5\sqrt5R} \approx 0.716\frac{\mu_0NI}{R} .
$$

**Definition 6.3.2 (Helmholtz Coils)** A pair of identical coaxial current-carrying coils whose separation equals their radius is called a **Helmholtz coil**.

The separation $d = R$ is chosen to make the field most uniform near the midpoint: by symmetry the first derivative of $B(x)$ vanishes at the midpoint, and a calculation shows that for $d = R$ the second derivative vanishes too (the third vanishes by symmetry), so that $B(x) = B_P + O(x^4)$. Laboratories often use it to produce a moderate uniform field, for example to cancel the Earth's field or to measure the charge-to-mass ratio of the electron.

**Example 6.3.4 (Field on the Axis of a Straight Solenoid)** A solenoid of radius $R$ and length $L$ has $n$ turns per unit length and carries current $I$. Find the field distribution on the axis.

**Solution** Regard the solenoid as many circular currents. Near the axial point $P$, a segment of length $\mathrm{d}l$ at distance $l$ from $P$ is equivalent to a circular current $nI\,\mathrm{d}l$, which by Example 6.3.2 produces at $P$ the field

$$
\mathrm{d}B = \frac{\mu_0nIR^2\,\mathrm{d}l}{2(R^2 + l^2)^{3/2}} .
$$
Let $\beta$ be the angle between the line from this segment to $P$ and the axis; then $l = R\cot\beta$, $\mathrm{d}l = -\dfrac{R\,\mathrm{d}\beta}{\sin^2\beta}$, $R^2 + l^2 = \dfrac{R^2}{\sin^2\beta}$, and hence $\mathrm{d}B = -\dfrac{\mu_0nI}{2}\sin\beta\,\mathrm{d}\beta$. The fields of all segments at $P$ point the same way, so

$$
B = -\frac{\mu_0nI}{2}\int_{\beta_1}^{\beta_2}\sin\beta\,\mathrm{d}\beta = \frac{\mu_0nI}{2}(\cos\beta_2 - \cos\beta_1),
$$
where $\beta_1$ and $\beta_2$ are the angles between the axis and the lines from $P$ to the two ends of the solenoid ($\beta_1 > \beta_2$). For an infinitely long solenoid, $\beta_1 = \pi$, $\beta_2 = 0$, and $B = \mu_0nI$; at the center of the end face of a semi-infinite solenoid, $B = \frac12\mu_0nI$.

For a solenoid of length $L = 10R$, $B \approx 0.98\mu_0nI$ at the center and about $0.50\mu_0nI$ at the center of an end face, and it has already dropped to about $0.05\mu_0nI$ outside the tube at a distance $2R$ from the end face. Inside the tube the field is fairly uniform near the center and decreases monotonically from the center toward the ends.

![Left: the field on the axis of solenoids of different lengths; right: the field on the axis of two coaxial coils, which is flattest near the midpoint when the separation equals the radius (Helmholtz coils)](./plots/solenoid-helmholtz-axis.py)

**Example 6.3.5 (Magnetic Field of a Uniformly Moving Point Charge)** Find the magnetic field produced by a charge $q$ moving with velocity $\boldsymbol{v}$ ($v \ll c$).

**Solution** Let the cross-sectional area of a current element be $S$, the number density of charge carriers be $n$, and each carrier have charge $q$ and **drift velocity** $\boldsymbol{v}$; then $I = nqSv$ and $I\,\mathrm{d}\boldsymbol{l} = nqS\,\mathrm{d}l\,\boldsymbol{v}$. The element contains $nS\,\mathrm{d}l$ carriers, so the field produced by each carrier is

$$
\boldsymbol{B} = \frac{\mathrm{d}\boldsymbol{B}}{nS\,\mathrm{d}l} = \frac{\mu_0}{4\pi}\frac{q\boldsymbol{v}\times\boldsymbol{e}_r}{r^2} .
$$
Comparing with the electric field of a **point charge**, $\boldsymbol{E} = \dfrac{q}{4\pi\varepsilon_0r^2}\boldsymbol{e}_r$, and using $\varepsilon_0\mu_0 = 1/c^2$,

$$
\boldsymbol{B} = \frac{1}{c^2}\boldsymbol{v}\times\boldsymbol{E} .
$$
This relation holds exactly for a uniformly moving point charge at any speed ($\boldsymbol{E}$ must then be taken from the relativistic result). It shows that the magnetic and electric fields are different manifestations of one electromagnetic field in different reference frames: in the frame in which the charge is at rest there is only an electric field, while in a frame in which the charge moves there are both electric and magnetic fields ([5.1.8](/5.1.8), [5.3.7](/5.3.7)). The ratio of the fields is $B/E \sim v/c^2$, so the ratio of the magnetic to the electric force between moving charges is $\sim v^2/c^2$, which is small at low speeds; the magnetic force in a wire is significant only because the wire as a whole is electrically neutral, so that the electric forces cancel.

**Example 6.3.6 (Finding a Field by Superposition)** Two arbitrary points $A$ and $B$ of a uniform copper ring are connected by two long straight wires, directed along radii, to a **source of electromotive force** very far away; the current $I$ enters at $A$ and leaves at $B$. Find the magnetic flux density at the center $O$ of the ring.

**Solution** The current system consists of five parts: the two straight wires, the distant wires connecting the source, and the two arcs into which $A$ and $B$ divide the ring (lengths $L_1$, $L_2$, currents $I_1$, $I_2$). $O$ lies on the extensions of the two straight wires, which therefore produce no field at $O$; the field of the distant wires can be neglected. The fields of the two arcs at $O$ point in opposite directions, with magnitudes

$$
B_1 = \int_0^{L_1}\frac{\mu_0I_1\,\mathrm{d}l}{4\pi R^2} = \frac{\mu_0I_1L_1}{4\pi R^2},\qquad B_2 = \frac{\mu_0I_2L_2}{4\pi R^2} .
$$
The two arcs are in parallel, so the voltage across them is the same, $I_1R_1 = I_2R_2$; the ring is uniform, so the **electrical resistance** is proportional to the length, $R_1/R_2 = L_1/L_2$, hence $I_1L_1 = I_2L_2$ and $B = B_1 - B_2 = 0$.

## 6.4. Ampère's Circuital Law

### 6.4.1. Statement of the Theorem

**Theorem 6.4.1 (Ampère's Circuital Law)** In the magnetic field of steady currents, the line integral of the magnetic flux density around any closed path $L$ (its **circulation**) equals $\mu_0$ times the algebraic sum of the currents enclosed by $L$ (linked with $L$):

$$
\oint_L\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = \mu_0\sum_iI_{i,\mathrm{enc}} .
$$
The sense of traversal of $L$ is chosen arbitrarily; currents related to it by the right-hand rule are counted positive, the others negative.

Note that $\boldsymbol{B}$ is produced jointly by all currents in space, but the loop integral depends only on the currents linked with $L$; currents not linked with $L$ contribute nothing to the circulation, though they do contribute to $\boldsymbol{B}$ at the points of $L$. A vanishing loop integral does not mean that $\boldsymbol{B} = \boldsymbol{0}$ at every point of the loop, nor that no current passes through the loop (positive and negative currents may cancel).

### 6.4.2. Proof of the Theorem

We prove it first for an infinitely long straight current $I$ and then generalize.

1. A circular loop in a plane perpendicular to the current, centered on the current: $B = \dfrac{\mu_0I}{2\pi r}$, tangent to the loop, and $\oint\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = \dfrac{\mu_0I}{2\pi r}\cdot2\pi r = \mu_0I$.
2. An arbitrary loop in a plane perpendicular to the current, enclosing the current: $\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = B\,r\,\mathrm{d}\phi$, where $\mathrm{d}\phi$ is the angle subtended by $\mathrm{d}\boldsymbol{l}$ at the current, and $\oint\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = \oint\dfrac{\mu_0I}{2\pi r}r\,\mathrm{d}\phi = \dfrac{\mu_0I}{2\pi}\cdot2\pi = \mu_0I$.
3. A planar loop not enclosing the current: draw two tangent lines from the location of the current, dividing the loop into two parts $L_1$ and $L_2$; the angles they subtend at the current are equal in magnitude and opposite in sign, so $\oint\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = \dfrac{\mu_0I}{2\pi}\big[\phi + (-\phi)\big] = 0$.
4. A nonplanar closed path: decompose each line element into a component $\mathrm{d}\boldsymbol{l}_\parallel$ in a plane perpendicular to the current and a component $\mathrm{d}\boldsymbol{l}_\perp$ along the current. Since $\boldsymbol{B}$ is perpendicular to the current, $\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l}_\perp = 0$, and only the projection of the loop onto the perpendicular plane remains, which reduces to cases 2 and 3.
5. Several current-carrying wires: by the superposition principle, the circulation is the sum of the individual contributions.

A closed steady current of arbitrary shape can be regarded as a loop made of current elements, and the Biot–Savart law can be used to prove the theorem in general; we omit this here.

### 6.4.3. Differential Form and Conditions of Validity

Let $S$ be any surface bounded by $L$; the current enclosed by $L$ is $I_{\mathrm{enc}} = \int_S\boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S}$. By **Stokes' theorem**, $\oint_L\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = \int_S(\nabla\times\boldsymbol{B})\cdot\mathrm{d}\boldsymbol{S}$, which holds for arbitrary $S$, so

$$
\nabla\times\boldsymbol{B} = \mu_0\boldsymbol{J} .
$$

- The curl is nonzero and so is the circulation: the steady magnetic field is nonconservative (a vortex field), and in general a scalar potential cannot be defined for it as in electrostatics. Only in a simply connected region without currents, where $\nabla\times\boldsymbol{B} = \boldsymbol{0}$, can a magnetic scalar potential be defined.
- The theorem holds only for steady currents: the current must close on itself or extend to infinity. Taking the **divergence** of both sides of $\nabla\times\boldsymbol{B} = \mu_0\boldsymbol{J}$, the left side is identically zero, so $\nabla\cdot\boldsymbol{J} = 0$ is required, which is exactly the steady-state condition ([5.3.5](/5.3.5)). The nonsteady case is treated in Section 6.6.

## 6.5. Finding Magnetic Fields with Ampère's Circuital Law

For current distributions with some symmetry, Ampère's circuital law finds the magnetic field more easily than the Biot–Savart law. The procedure is to analyze the symmetry of the current distribution and thereby determine the symmetry of the field (under which transformations the direction and magnitude of the field are invariant), and then to choose a loop on which the magnitude of $\boldsymbol{B}$ is constant and its direction is tangent or perpendicular to the loop, so that $B$ can be taken out of the integral.

### 6.5.1. Polar Vectors and Axial Vectors

In analyzing the symmetry of the magnetic field, note that $\boldsymbol{B}$ and $\boldsymbol{E}$ transform differently under mirror reflection.

**Definition 6.5.1 (Polar Vectors and Axial Vectors)** Under mirror reflection (for example reflection in the $xy$ plane, $z \to -z$), a vector whose components parallel to the mirror are unchanged and whose component perpendicular to the mirror reverses is called a **polar vector**, such as $\mathrm{d}\boldsymbol{r}$, $\boldsymbol{v}$, $\boldsymbol{a}$, $\boldsymbol{p}$, $\boldsymbol{F}$, $\boldsymbol{E}$; a vector whose components parallel to the mirror reverse and whose component perpendicular to the mirror is unchanged is called an **axial vector** (pseudovector), such as the angular velocity $\boldsymbol{\omega}$, the **angular momentum** $\boldsymbol{L}$, the **torque** $\boldsymbol{M}$, and $\boldsymbol{B}$.

The cross product of two polar vectors is an axial vector (for example $\boldsymbol{L} = \boldsymbol{r}\times\boldsymbol{p}$), and the cross product of an axial vector and a polar vector is a polar vector (for example $\boldsymbol{F} = q\boldsymbol{v}\times\boldsymbol{B}$). Defining the cross product requires the right-hand rule, and a mirror reflection turns a right hand into a left hand, which is why axial vectors acquire an extra minus sign. By the Biot–Savart law, $\mathrm{d}\boldsymbol{B} \propto \mathrm{d}\boldsymbol{l}\times\boldsymbol{e}_r$, so $\boldsymbol{B}$ is an axial vector.

For example, an infinitely long straight current is mirror-symmetric with respect to any plane containing the wire. If $\boldsymbol{B}$ had a component parallel to such a plane (a radial or axial component), that component would reverse under reflection while the current distribution is unchanged, a contradiction; so $\boldsymbol{B}$ can only be perpendicular to the plane containing the wire, that is, tangent to the circle around the wire.

### 6.5.2. Applications

**Example 6.5.1 (Field of an Infinitely Long Cylindrical Current)** A current $I$ flows uniformly through an infinitely long cylindrical **conductor** of radius $R$; find the field inside and outside the conductor.

**Solution** By mirror symmetry, $\boldsymbol{B}$ is tangent to circles centered on the axis; by axial and translational symmetry, $B$ depends only on the distance $r$ from the axis. Take a coaxial circular loop of radius $r$:

$$
\oint_L\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = 2\pi rB = \mu_0I_{\mathrm{enc}},\qquad
B = \begin{cases}\dfrac{\mu_0Ir}{2\pi R^2}, & r < R,\\[2ex] \dfrac{\mu_0I}{2\pi r}, & r > R .\end{cases}
$$
Outside the conductor the field is the same as when the current is concentrated on the axis, in agreement with Example 6.3.1.

**Example 6.5.2 (Field of an Infinitely Long Straight Solenoid)** An infinitely long, tightly wound straight solenoid has $n$ turns per unit length and carries current $I$. Find the field inside and outside.

**Solution** A tightly wound solenoid can be regarded as an array of circular currents (neglecting the pitch). In cylindrical coordinates write $\boldsymbol{B} = B_r\boldsymbol{e}_r + B_\phi\boldsymbol{e}_\phi + B_z\boldsymbol{e}_z$; by the infinite length and axial symmetry, each component depends only on $r$.

- Construct a closed cylindrical surface of radius $r$ and length $l$ about the axis. The fluxes through the two bases cancel, so by Gauss's law for magnetism, $2\pi rl\,B_r = 0$, hence $B_r = 0$.
- Construct a circular loop of radius $r$ centered on the axis. It is not linked with any current (neglecting the pitch, the current flows only in the circumferential direction), so by Ampère's circuital law $2\pi rB_\phi = 0$ and $B_\phi = 0$.
- Hence $\boldsymbol{B} = B_z(r)\boldsymbol{e}_z$. Inside the tube, take a rectangular loop with one side on the axis and one side at radius $r$ (the sides parallel to the axis having length $l$); it is not linked with any current, so $[B_z(0) - B_z(r)]l = 0$ and the field inside is uniform. A similar rectangular loop outside shows that the field outside is also uniform, and since it vanishes at infinity, $B = 0$ outside.
- Finally take a rectangular loop with one side inside and one side outside the tube; it is linked with the current $nlI$, so $B_{\mathrm{in}}l = \mu_0nlI$.

$$
\boldsymbol{B}_{\mathrm{in}} = \mu_0nI\boldsymbol{e}_z,\qquad \boldsymbol{B}_{\mathrm{out}} = \boldsymbol{0},
$$
where $\boldsymbol{e}_z$ is related to the sense of the current by the right-hand rule. This agrees with the limit $L \to \infty$ in Example 6.3.4. The conclusion is the same for a tightly wound long straight solenoid of noncircular cross section.

**Example 6.5.3 (Field of a Toroidal Solenoid)** A toroidal solenoid (toroid) with $N$ turns carries current $I$. Find the field inside and outside the ring.

**Solution** By symmetry the field lines are circles coaxial with the ring. Take a coaxial circular loop of radius $r$: inside the ring the loop is linked with the current $NI$, so $2\pi rB = \mu_0NI$; outside the ring ($r$ smaller than the inner radius or larger than the outer radius), the algebraic sum of the linked currents is zero, so $B = 0$.

$$
B_{\mathrm{in}} = \frac{\mu_0NI}{2\pi r} .
$$
When the cross section of the ring is small, $n = N/(2\pi r)$ is approximately constant and $B \approx \mu_0nI$, the same as for an infinitely long solenoid.

**Example 6.5.4 (Field of an Infinite Plane Current)** A uniformly distributed current flows in an infinite thin conducting sheet; the current per unit length perpendicular to the current direction is $K$ (the surface **current density**, in $\mathrm{A\,m^{-1}}$). Find the field outside the sheet.

**Solution** By symmetry, the fields on the two sides of the sheet have equal magnitude and opposite directions, both parallel to the sheet and perpendicular to the current. Take a rectangular loop straddling the sheet, with two sides of length $l$ parallel to the sheet, one on each side; it is linked with the current $Kl$:

$$
2Bl = \mu_0Kl,\qquad B = \frac{\mu_0K}{2},
$$
independent of the distance from the sheet, so the field is uniform. This corresponds to the electric field $E = \sigma/(2\varepsilon_0)$ of an infinite uniformly charged plane.

## 6.6. Magnetic Fields Associated with Changing Electric Fields

### 6.6.1. A Difficulty with Ampère's Circuital Law

In Ampère's circuital law, $I_{\mathrm{enc}}$ is the current through a surface $S$ bounded by $L$. For steady currents $\nabla\cdot\boldsymbol{J} = 0$, so the currents through any two surfaces bounded by the same $L$ are equal, and $I_{\mathrm{enc}}$ has a definite meaning. For nonsteady currents a contradiction arises.

Consider a circuit that charges a **capacitor**. Take a circular loop $L$ around the wire and two surfaces bounded by it: a plane $S_1$ that cuts the wire, and a surface $S_2$ that passes between the two plates of the capacitor and does not meet the wire. For $S_1$, $\oint_L\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = \mu_0I$; for $S_2$, no conduction current passes through it, and $\oint_L\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = 0$. The same circulation receives two different values.

### 6.6.2. Displacement Current

In 1861–1862 Maxwell noted that when a capacitor is being charged, the charge on the plates is changing, and so is the electric field between them. By the **charge continuity equation** and **Gauss's law** for $\boldsymbol{D}$ ([5.3.4](/5.3.4), Theorem 4.3.1), for any closed surface $S$,

$$
\oint_S\boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S} = -\frac{\mathrm{d}q_{\mathrm{enc}}}{\mathrm{d}t},\qquad
\frac{\mathrm{d}q_{\mathrm{enc}}}{\mathrm{d}t} = \frac{\mathrm{d}}{\mathrm{d}t}\oint_S\boldsymbol{D}\cdot\mathrm{d}\boldsymbol{S} = \oint_S\frac{\partial\boldsymbol{D}}{\partial t}\cdot\mathrm{d}\boldsymbol{S},
$$
and therefore

$$
\oint_S\Big(\boldsymbol{J} + \frac{\partial\boldsymbol{D}}{\partial t}\Big)\cdot\mathrm{d}\boldsymbol{S} = 0 .
$$
In the nonsteady case the conduction current $\boldsymbol{J}$ is not continuous, but $\boldsymbol{J} + \partial\boldsymbol{D}/\partial t$ always is: $S_1$ and $S_2$ together form a closed surface, so the fluxes of $\boldsymbol{J} + \partial\boldsymbol{D}/\partial t$ through $S_1$ and $S_2$ are equal.

**Definition 6.6.1 (Displacement Current)** The rate of change with time of the electric displacement flux $\Phi_D = \int_S\boldsymbol{D}\cdot\mathrm{d}\boldsymbol{S}$,

$$
I_{\mathrm{d}} = \frac{\mathrm{d}\Phi_D}{\mathrm{d}t} = \int_S\frac{\partial\boldsymbol{D}}{\partial t}\cdot\mathrm{d}\boldsymbol{S}
$$
is called the **displacement current** through $S$, and $\boldsymbol{J}_{\mathrm{d}} = \partial\boldsymbol{D}/\partial t$ is called the displacement current density. The sum of the conduction current and the displacement current, $I = I_{\mathrm{c}} + I_{\mathrm{d}}$, is called the **total current**.

In vacuum $\boldsymbol{J}_{\mathrm{d}} = \varepsilon_0\partial\boldsymbol{E}/\partial t$; it is not a motion of charge but a changing electric field. In a medium $\partial\boldsymbol{D}/\partial t = \varepsilon_0\partial\boldsymbol{E}/\partial t + \partial\boldsymbol{P}/\partial t$, and the last term is the motion of **bound charge** (the polarization current). The total current is always continuous. Maxwell postulated that the displacement current excites a magnetic field just as the conduction current does; in essence, a changing electric field excites a magnetic field. Ampère's circuital law is thereby generalized to:

**Theorem 6.6.1 (Ampère–Maxwell Law)**

$$
\oint_L\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = \mu_0(I_{\mathrm{c}} + I_{\mathrm{d}}) = \mu_0\int_S\Big(\boldsymbol{J} + \frac{\partial\boldsymbol{D}}{\partial t}\Big)\cdot\mathrm{d}\boldsymbol{S},\qquad
\nabla\times\boldsymbol{B} = \mu_0\Big(\boldsymbol{J} + \frac{\partial\boldsymbol{D}}{\partial t}\Big),
$$
where $\boldsymbol{J}$ is the conduction current density of free charge, and the sources of $\boldsymbol{B}$ also include the magnetization currents of the medium ([5.3.8](/5.3.8)).

Taking the divergence of the differential form, the left side vanishes and the right side is $\nabla\cdot\boldsymbol{J} + \partial(\nabla\cdot\boldsymbol{D})/\partial t = \nabla\cdot\boldsymbol{J} + \partial\rho_0/\partial t = 0$, which is exactly the charge continuity equation: with the displacement current included, Ampère's circuital law is compatible with the **law of conservation of charge**. The hypothesis of the displacement current was confirmed by the existence of electromagnetic waves (Hertz, 1888) ([5.3.10](/5.3.10)).

**Example 6.6.1 (Displacement Current in a Conductor)** A conductor of cross-sectional area $S$ carries a sinusoidal current $I = I_0\cos\omega t$ distributed uniformly over the cross section. Find the ratio of the amplitudes of the displacement current and the conduction current.

**Solution** By **Ohm's law**, in the conductor $E = \rho J = \rho I/S$ ($\rho$ is the **electrical resistivity**), so

$$
I_{\mathrm{d}} = \varepsilon_0\varepsilon_{\mathrm{r}}\frac{\mathrm{d}E}{\mathrm{d}t}S = \varepsilon_0\varepsilon_{\mathrm{r}}\rho\frac{\mathrm{d}I}{\mathrm{d}t} = \varepsilon_0\varepsilon_{\mathrm{r}}\rho\omega I_0\cos\Big(\omega t + \frac\pi2\Big),\qquad
\frac{I_{\mathrm{d},0}}{I_0} = \varepsilon_0\varepsilon_{\mathrm{r}}\rho\omega .
$$
For a good conductor, $\rho \sim 10^{-8}\,\Omega\,\mathrm{m}$; taking $\varepsilon_{\mathrm{r}} \approx 1$, the ratio is about $9\times10^{-12}\times10^{-8}\times2\pi\nu \approx 6\times10^{-19}\nu/\mathrm{Hz}$. Even in the microwave band at $\nu = 10^9\,\mathrm{Hz}$ it is only of order $10^{-9}$, so the displacement current in a good conductor can be neglected entirely. For seawater ($\rho \approx 0.2\,\Omega\,\mathrm{m}$, $\varepsilon_{\mathrm{r}} \approx 80$) the two are comparable at $\nu \sim 10^9\,\mathrm{Hz}$. In insulators and in vacuum there is only displacement current.

**Example 6.6.2 (Magnetic Field of a Charging Parallel-Plate Capacitor)** A circular parallel-plate capacitor with plates of radius $R$ (vacuum between the plates) is charged by a conduction current $I_{\mathrm{c}}$. Find the magnetic field between the plates at distance $r$ from the axis (neglecting edge effects).

**Solution** The field between the plates is $E = \dfrac{q}{\varepsilon_0\pi R^2}$, so $\dfrac{\mathrm{d}E}{\mathrm{d}t} = \dfrac{I_{\mathrm{c}}}{\varepsilon_0\pi R^2}$; the displacement current is uniformly distributed between the plates, with a total equal to $I_{\mathrm{c}}$. By axial symmetry the field lines are circles concentric with the axis. Take a coaxial circular loop of radius $r$:

$$
2\pi rB = \mu_0\varepsilon_0\frac{\mathrm{d}}{\mathrm{d}t}\int_S\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S} =
\begin{cases}\mu_0I_{\mathrm{c}}\dfrac{r^2}{R^2}, & r < R,\\[2ex] \mu_0I_{\mathrm{c}}, & r > R,\end{cases}
\qquad
B = \begin{cases}\dfrac{\mu_0I_{\mathrm{c}}r}{2\pi R^2}, & r < R,\\[2ex] \dfrac{\mu_0I_{\mathrm{c}}}{2\pi r}, & r > R .\end{cases}
$$
The field between the plates is exactly the same as when the current $I_{\mathrm{c}}$ flows uniformly through a cylindrical conductor of radius $R$ (Example 6.5.1): in producing a magnetic field, the displacement current is equivalent to the conduction current.

## Summary

| Law | Integral form | Differential form |
|---|---|---|
| Lorentz force | $\boldsymbol{F} = q\boldsymbol{v}\times\boldsymbol{B}$ | |
| Biot–Savart law | $\mathrm{d}\boldsymbol{B} = \dfrac{\mu_0}{4\pi}\dfrac{I\,\mathrm{d}\boldsymbol{l}\times\boldsymbol{e}_r}{r^2}$ | |
| Gauss's law for magnetism | $\oint_S\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S} = 0$ | $\nabla\cdot\boldsymbol{B} = 0$ |
| Ampère's circuital law (steady currents) | $\oint_L\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = \mu_0I_{\mathrm{enc}}$ | $\nabla\times\boldsymbol{B} = \mu_0\boldsymbol{J}$ |
| Ampère–Maxwell law | $\oint_L\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = \mu_0(I_{\mathrm{c}} + I_{\mathrm{d}})$ | $\nabla\times\boldsymbol{B} = \mu_0(\boldsymbol{J} + \partial_t\boldsymbol{D})$ |

| Current distribution | Magnetic flux density |
|---|---|
| Straight wire segment | $\dfrac{\mu_0I}{4\pi r_0}(\cos\theta_1 - \cos\theta_2)$; infinitely long: $\dfrac{\mu_0I}{2\pi r_0}$ |
| Axis of a circular current | $\dfrac{\mu_0IR^2}{2(R^2 + x^2)^{3/2}}$; at the center: $\dfrac{\mu_0I}{2R}$ |
| Axis of a solenoid | $\dfrac{\mu_0nI}{2}(\cos\beta_2 - \cos\beta_1)$; infinitely long: $\mu_0nI$ inside, $0$ outside |
| Toroidal solenoid | inside the ring $\dfrac{\mu_0NI}{2\pi r}$, outside $0$ |
| Infinite plane current | $\dfrac{\mu_0K}{2}$ |
| Moving point charge | $\dfrac{\mu_0}{4\pi}\dfrac{q\boldsymbol{v}\times\boldsymbol{e}_r}{r^2} = \dfrac{\boldsymbol{v}\times\boldsymbol{E}}{c^2}$ |

## Questions

1. A closed surface encloses only one pole of a bar magnet. What is the magnetic flux through it?

   **Answer** Zero. The field lines are closed curves that run inside the magnet from the S pole to the N pole, so as many field lines leave the surface as enter it. This is exactly Gauss's law for magnetism, and it also shows that isolated magnetic poles do not exist.

2. In a region without currents, if the field lines are parallel straight lines, must the magnetic field be uniform?

   **Answer** Yes. Let the field lines run along the $z$ direction. From $\nabla\cdot\boldsymbol{B} = 0$ we get $\partial B_z/\partial z = 0$, so $B$ is constant along a field line; from $\nabla\times\boldsymbol{B} = \boldsymbol{0}$ we get $\partial B_z/\partial x = \partial B_z/\partial y = 0$, so $B$ is also constant in the perpendicular directions (this can also be shown with the circulation around a rectangular loop).

3. Can the magnetic field between magnetic poles drop abruptly to zero at the edge of the poles?

   **Answer** No. Take a rectangular loop with one side between the poles, parallel to the field, and the other side outside, where the field is zero. The loop is linked with no current, yet the circulation is nonzero, contradicting Ampère's circuital law. There must be a fringing field that weakens gradually at the edge, similar to the fringing field of a parallel-plate capacitor ([5.3.4](/5.3.4)).

4. Why does Ampère's circuital law fail for nonsteady currents?

   **Answer** In the nonsteady case $\nabla\cdot\boldsymbol{J} \ne 0$, and the conduction currents through different surfaces bounded by the same loop differ, so "the current enclosed by the loop" has no definite meaning. Mathematically, taking the divergence of both sides of $\nabla\times\boldsymbol{B} = \mu_0\boldsymbol{J}$ gives $\nabla\cdot\boldsymbol{J} = 0$, which contradicts the conservation of charge. The contradiction disappears once the displacement current is added.
