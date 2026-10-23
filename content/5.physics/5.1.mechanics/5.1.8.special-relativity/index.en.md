---
title: Foundations of Special Relativity
source_hash: dfaa164cb731
---

By the end of the 19th century, Newtonian mechanics, heat and the kinetic theory of molecules, wave optics and Maxwell's electromagnetic theory had all been enormously successful: Newtonian mechanics had predicted Neptune from the perturbations of the orbit of Uranus, and Maxwell's equations had predicted electromagnetic waves. In a 1900 lecture Kelvin said that only "two clouds" floated in the clear sky of physics: the null result of the ether-drift experiments and the difficulty of equipartition of energy in blackbody radiation. The first led to special relativity (1905) and the second to the quantum theory ([5.5.1](/5.5.1)); together with general relativity (1916), which revealed the relation between spacetime and gravitation, and quantum mechanics (1925), these conceptual revolutions of the early 20th century completely changed our understanding of time, space and matter.

This is the last chapter on mechanics. The previous seven chapters were all built on the Galilean transformation and the absolute conception of space and time (relative motion in [5.1.1](/5.1.1), **inertial frames** in [5.1.2](/5.1.2)). Starting from Einstein's two fundamental principles, this chapter derives the **Lorentz transformation**, from which we obtain the relativity of simultaneity, time dilation, length contraction and the transformation of **velocity** (the **kinematics**). Requiring that conservation of **momentum** and of energy hold in all inertial frames then gives relativistic momentum, energy and the mass–energy relation (the **dynamics**). Mathematically, the Lorentz transformations are the linear transformations that preserve an indefinite quadratic form in Minkowski spacetime, and they form the **Lorentz group** ([2.1.13](/2.1.13#ex-13.7.1)). The results of this chapter are needed in electromagnetism ([5.3](/5.3), transformation of the electromagnetic field) and in quantum physics ([5.5](/5.5), photons, Compton scattering, matter waves); the derivation of the **Doppler effect** of light from the previous chapter ([5.1.7](/5.1.7#sec-7.9.2)) is also given here ([Section 8.5.7](#sec-8.5.7)).

## 8.1. Newton's Principle of Relativity and the Galilean Transformation

### 8.1.1. Events and Spacetime Coordinates

**Definition 8.1.1** A physical occurrence with a definite time and place is called an **event**, and the time and place $(x,y,z,t)$ of an event in some **reference frame** are called its **spacetime coordinates** in that frame. The relation between the spacetime coordinates of the same event in two inertial frames is called a spacetime transformation.

For example, "a particle appears at a certain position at a certain time" is an event. When discussing the properties of spacetime we care only about the spacetime coordinates of events, not about their specific physical content. Different spacetime transformations represent different ways of measuring time and space and reflect different conceptions of spacetime:

- Absolute conception of space and time: time and space are independent of each other, an absolute "stage" independent of the motion of matter; the measurement of time intervals and spatial intervals does not depend on the reference frame. This agrees with everyday experience.
- Relativistic conception of space and time: time and space form a unified whole inseparable from the motion of matter; the measurement of spacetime depends on the reference frame.

### 8.1.2. The Galilean Transformation

**Property 8.1.1 (Newton's Principle of Relativity)** All laws of mechanics have the same form in all inertial frames.

Let the inertial frame S′ move with velocity $\boldsymbol{v}=v\boldsymbol{e}_x$ relative to the inertial frame S, with the coordinate axes of the two frames parallel and the origins $O$ and $O'$ coinciding at $t=t'=0$ (called the standard configuration below). Because the measurement of time intervals and spatial intervals is absolute, the spacetime coordinates of the same event satisfy the *Galilean transformation*

$$
x'=x-vt,\qquad y'=y,\qquad z'=z,\qquad t'=t.\tag{8.1}
$$
Differentiating with respect to time gives the **Galilean velocity transformation** $u_x'=u_x-v$, $u_y'=u_y$, $u_z'=u_z$ ([5.1.1](/5.1.1)), and differentiating again gives $\boldsymbol{a}'=\boldsymbol{a}$. Force and mass do not depend on the reference frame, so **Newton's second law** $\boldsymbol{F}=m\boldsymbol{a}$ is invariant in form under the Galilean transformation: the Galilean transformation is consistent with the mechanical principle of relativity, and no mechanical experiment can tell whether an inertial frame is at rest or in uniform rectilinear motion.

### 8.1.3. Difficulties of the Absolute Conception of Space and Time

Newtonian mechanics satisfies the Galilean transformation, but Maxwell's electromagnetic theory does not.

- Electromagnetic theory gives the speed of light in vacuum, $c=1/\sqrt{\varepsilon_0\mu_0}$, as a constant independent of the motion of the source and the observer; according to the Galilean velocity transformation, the speed of light should vary with the reference frame.
- Maxwell's equations change their form under the Galilean transformation. Could the laws of electromagnetism be different in different inertial frames?

Historically some compromise theories were proposed, still aiming to keep the Galilean transformation, but all were refuted by experiment.

The emission theory holds that the speed of light adds to the velocity of the source. According to this theory, light emitted by the star of a binary moving toward the Earth (speed $c+v_1$) and light emitted by the star moving away (speed $c-v_2$) would reach the Earth at different times, and the apparent motion of the binary should show pronounced distortion, which has never been observed (de Sitter, 1913). In a 1964 experiment at CERN, $\pi^0$ mesons moving at $0.99975c$ decayed by $\pi^0\to2\gamma$, and the speed of the $\gamma$ photons measured along the direction of motion agreed with the speed of light from a source at rest to a precision of $10^{-4}$. A large body of experiments shows that the speed of light is independent of the motion of the source.

The ether theory holds that the propagation of light waves in vacuum needs an absolutely stationary medium, the "ether"; the laws of electromagnetism hold only in the "absolute reference frame" at rest relative to the ether, and the speed of light $c$ is isotropic only in this frame. Since the Earth moves relative to the ether, an "ether wind" should be observed on the Earth. The 1887 Michelson–Morley experiment used an **interference** apparatus to compare two mutually perpendicular light paths, each of length $l$. Let the apparatus move with velocity $v$ relative to the ether; by Galilean velocity addition, the round-trip time along the direction of motion is $t_\parallel=\frac{l}{c-v}+\frac{l}{c+v}=\frac{2l/c}{1-\beta^2}$ and that in the perpendicular direction is $t_\perp=\frac{2l/c}{\sqrt{1-\beta^2}}$ ($\beta=v/c$), which differ by $\Delta t\approx\frac{l}{c}\beta^2$. When the apparatus is rotated through $90^\circ$ the two paths are exchanged, and the interference fringes should shift by

$$
\Delta N=\frac{2c\Delta t}{\lambda}\approx\frac{2l\beta^2}{\lambda}.
$$
Taking the orbital speed of the Earth $v\approx3\times10^4\,\mathrm{m\,s^{-1}}$ ($\beta\approx10^{-4}$), an effective arm length $l\approx11\,\mathrm{m}$ and $\lambda\approx500\,\mathrm{nm}$, one expects $\Delta N\approx0.4$ fringe; the observed shift was less than $0.02$ fringe, and likewise when repeated in different seasons and at different times. This "null result" refuted the existence of an "ether wind".

The question thus became acute: which is more fundamental, the Galilean transformation (the absolute conception of space and time) or the invariance of physical laws in all inertial frames? Einstein chose the latter: Maxwell's equations should hold in all inertial frames, and the speed of light is the isotropic $c$ in any inertial frame, so that the null result of the Michelson–Morley experiment is natural; what has to be modified is the spacetime transformation.

## 8.2. Einstein's Principle of Relativity and the Constancy of the Speed of Light

In his 1905 paper "On the Electrodynamics of Moving Bodies", Einstein put forward two fundamental principles, which are the starting point of special relativity.

**Property 8.2.1 (Einstein's Principle of Relativity)** All inertial frames are equivalent: the laws of physics (including those of mechanics and of electromagnetism) have the same form in all inertial frames.

**Property 8.2.2 (Constancy of the Speed of Light)** In any inertial frame, the speed of light in vacuum is $c$, independent of the motion of the inertial frame and also independent of the motion of the source or the observer.

Since 1983 the SI has defined the speed of light in vacuum to be the exact value $c=299\,792\,458\,\mathrm{m\,s^{-1}}$, and the meter is defined by the distance light travels in $1/299\,792\,458\,\mathrm{s}$, which writes the constancy of the speed of light into the system of units.

To understand the constancy of the speed of light through a specific event: in the standard configuration, a flash is emitted from the coincident points at the moment when $O$ and $O'$ coincide ($t=t'=0$). In S, since the speed of light is independent of the motion of the source, the **wavefront** of the flash is a sphere centered at $O$ with radius $ct$; in S′ the wavefront is likewise a sphere centered at $O'$ with radius $ct'$:

$$
x^2+y^2+z^2=c^2t^2,\qquad x'^2+y'^2+z'^2=c^2t'^2.\tag{8.2}
$$
The two centers do not coincide for $t>0$, yet the same wavefront is a sphere centered at the origin of its own frame in both frames. This is possible only if $t'\ne t$: time too must be transformed from one reference frame to another.

## 8.3. Relativity of Simultaneity

To compare the times of events occurring at different places, we must first say how to synchronize clocks placed at different places.

**Definition 8.3.1 (Einstein Synchronization)** In an inertial frame, a light signal is emitted from the midpoint M of the line joining clocks A and B at rest. By the constancy of the speed of light, the signal reaches A and B simultaneously; if both clocks are set to the same reading at the moment of arrival, the two clocks are synchronized.

Place at every position in the inertial frame a clock at rest relative to the frame, and synchronize all the clocks in this way; these synchronized clocks together with the inertial coordinate system form the measuring system of that inertial frame. The time $t$ of an event $(x,y,z,t)$ is read from the clock of the frame placed at the location $(x,y,z)$ of the event.

Now imagine a train (frame S′) moving to the right with velocity $v$ relative to a platform (frame S), and a flash emitted from the midpoint M of the carriage. On the train, the flash reaches the front and the rear simultaneously. On the platform, the speed of light is still $c$, while the rear moves toward the light and the front moves away from it, so the light reaches the rear first and the front later. Hence:

**Property 8.3.1 (Relativity of Simultaneity)** Two events that occur simultaneously at different places in one inertial frame do not necessarily occur simultaneously in another inertial frame moving relative to it.

The relativity of simultaneity is a direct consequence of the constancy of the speed of light. As a result, each inertial frame considers its own clocks to be synchronized and the clocks of other inertial frames not to be; the readings of two clocks belonging to two inertial frames can be compared directly only when they meet. Quantitatively ([Section 8.5.1](#sec-8.5.1)): seen from S, in a row of clocks of S′ arranged along the direction of motion, the farther forward a clock is, the smaller (the "later") its reading.

## 8.4. The Lorentz Transformation

### 8.4.1. Derivation

The conception of space and time implied by the constancy of the speed of light and Einstein's principle of relativity should be expressed by a new spacetime transformation. As early as 1899–1904, Lorentz obtained this transformation in order to explain the null result of the ether-drift experiments, but he presupposed the existence of the ether and held that only $t$ was the true time, with $t'$ merely an auxiliary quantity ("local time"). In 1905 Einstein rederived it from an entirely new physical basis.

In the standard configuration, we look for the transformation between the coordinates $(x,y,z,t)$ and $(x',y',z',t')$ of the same event.

1. The transformation must be linear: spacetime is homogeneous, uniform rectilinear motion must be uniform rectilinear motion in both inertial frames, and events at equal intervals in one inertial frame must also be at equal intervals in the other.
2. The measurement of lengths perpendicular to the direction of motion is independent of the reference frame: $y'=y$, $z'=z$. Otherwise, imagine two rods along the $y$ direction with the same rest length moving relative to each other; the result of comparing them when they meet would distinguish the two reference frames, violating the principle of relativity.
3. The motion of $O'$ ($x'=0$) in S is $x=vt$, so $x'$ must be proportional to $x-vt$: $x'=\gamma(x-vt)$ with $\gamma$ to be determined. By the principle of relativity, S moves with $-v$ in S′, and the two frames are symmetric (isotropy of space ensures the same coefficient of proportionality): $x=\gamma(x'+vt')$.
4. Determine $\gamma$ from the constancy of the speed of light: take a light signal emitted from the origin along the $x$ direction at $t=t'=0$; it satisfies $x=ct$ in S and $x'=ct'$ in S′. Substituting into the two relations above gives $ct'=\gamma(c-v)t$ and $ct=\gamma(c+v)t'$; multiplying them to eliminate $tt'$ gives $c^2=\gamma^2(c^2-v^2)$.

**Definition 8.4.1 (Lorentz Factor)** With $\beta=v/c$, the quantity

$$
\gamma=\frac{1}{\sqrt{1-\beta^2}}=\frac{1}{\sqrt{1-v^2/c^2}}\ge1
$$
is called the **Lorentz factor**.

Finally, eliminating $x'$ from $x=\gamma(x'+vt')$ and $x'=\gamma(x-vt)$ and using $1-\gamma^2=-\gamma^2\beta^2$ gives $t'=\gamma\big(t-\frac{v}{c^2}x\big)$. One can check that the transformation so obtained makes the two wavefront equations in Eq. (8.2) equivalent.

### 8.4.2. The Lorentz Transformation and Its Properties

**Theorem 8.4.1 (Lorentz Transformation)** In the standard configuration, the spacetime coordinates of the same event in the inertial frames S and S′ satisfy

$$
x'=\gamma(x-vt),\quad y'=y,\quad z'=z,\quad t'=\gamma\Big(t-\frac{v}{c^2}x\Big);\tag{8.3}
$$
the inverse transformation is obtained by replacing $v$ by $-v$:

$$
x=\gamma(x'+vt'),\quad y=y',\quad z=z',\quad t=\gamma\Big(t'+\frac{v}{c^2}x'\Big).
$$
The spatial and time intervals between two events satisfy the same relations:

$$
\Delta x'=\gamma(\Delta x-v\Delta t),\qquad \Delta t'=\gamma\Big(\Delta t-\frac{v}{c^2}\Delta x\Big).\tag{8.4}
$$

Remarks:

1. For $v\ll c$, $\gamma\approx1$ and $\frac{v}{c^2}x\approx0$, and the Lorentz transformation goes over into the Galilean transformation (8.1). Newtonian mechanics is the low-velocity limit of relativity.
2. For $v\ge c$, $\gamma$ is imaginary or infinite and the transformation loses its meaning: the speed of light $c$ in vacuum is the limiting **speed** of any body that can serve as a reference frame, and the **relative velocity** of two bodies can only be less than $c$.
3. The measurements of time and space are coupled: $t'$ depends on $x$ and $x'$ depends on $t$. Using $ct$ in place of $t$, the transformation reads $ct'=\gamma(ct-\beta x)$, $x'=\gamma(x-\beta ct)$, in which $ct$ and $x$ play completely symmetric roles; it is a "hyperbolic rotation" in Minkowski spacetime $(ct,x,y,z)$: letting $\beta=\tanh\phi$, we have $\gamma=\cosh\phi$ and $\gamma\beta=\sinh\phi$.

**Example 8.4.1 (Einstein's Train)** A train (frame S′) moves with $v=0.6c$ relative to the ground (frame S). A light-signal generator M on the train and a receiver A behind it are a distance $l=3\times10^6\,\mathrm{m}$ apart. Find the time taken by the light signal to travel from M to A as measured on the ground.

**Solution** Event 1: M emits light; event 2: the light reaches A. In the train frame, $\Delta t'=l/c=0.01\,\mathrm{s}$ and $\Delta x'=-l$. By the inverse transformation,

$$
\Delta t=\gamma\Big(\Delta t'+\frac{v}{c^2}\Delta x'\Big)=\gamma\frac{l}{c}(1-\beta)=\sqrt{\frac{1-\beta}{1+\beta}}\,\frac lc=\frac12\times0.01\,\mathrm{s}=0.005\,\mathrm{s}.
$$
Seen from the ground, A moves toward the light, so the light travels a shorter distance than $l$ and takes a shorter time. [Section 8.5.3](#sec-8.5.3) recomputes this problem using length contraction.

## 8.5. The Relativistic Conception of Space and Time

In this section we start from the Lorentz transformation and discuss several important conclusions that embody the relativistic conception of space and time.

![Minkowski spacetime diagram (c = 1). Frame S' moves at v = 0.5c: its time axis ct' and space axis x' close in toward the light cone (dashed); the dashed line parallel to the x' axis is a line of simultaneity of S', and events P1 and P2 that are simultaneous in S' are not simultaneous in S](./plots/minkowski-diagram.py)

### 8.5.1. Relativity of Simultaneity

Let two events $P_1$ and $P_2$ occur simultaneously in S′ ($\Delta t'=0$) at different places ($\Delta x'=x_2'-x_1'\ne0$). By the inverse transformation (8.4),

$$
\Delta t=t_2-t_1=\gamma\frac{v}{c^2}\Delta x'.
$$
For $\Delta x'>0$, $\Delta t>0$: seen from S, the event $P_1$ at the rear (with respect to the motion) occurs first. For $v\ll c$ or $\Delta x'=0$, $\Delta t=0$: events occurring simultaneously at the same place are simultaneous in every inertial frame. On a Minkowski diagram, the lines of simultaneity of S′ are slanted lines parallel to the $x'$ axis, not the horizontal lines of S.

### 8.5.2. Time Dilation

**Definition 8.5.1 (Proper Time)** The time interval between two events occurring successively at the same place in some inertial frame, measured by a single clock at that place, is called the **proper time** of the two events, denoted $\tau$. In another inertial frame the two events occur at different places, and their time interval must be measured by two (synchronized) clocks.

Let the two events occur at the same place in S′ ($\Delta x'=0$), so that the proper time is $\tau=\Delta t'$. By the inverse transformation $\Delta t=\gamma(\Delta t'+\frac{v}{c^2}\Delta x')$,

$$
\Delta t=\gamma\tau=\frac{\tau}{\sqrt{1-v^2/c^2}}>\tau.\tag{8.5}
$$

**Property 8.5.1 (Time Dilation)** Observed from one inertial frame, the time interval between two events occurring at the same place in another inertial frame moving relative to it is longer than the proper time (the proper time is the shortest). This is called *time dilation*.

Any process consists of a series of successive events, so observed from one inertial frame, any process (physical, chemical or biological) occurring at one place in the moving frame proceeds more slowly: "moving clocks run slow". Compared with the "1 second" of a series of synchronized clocks at rest in S, the "1 second" of the moving clock is longer. Note:

- Moving clocks running slow does not mean that the structure of the clock has changed; an observer moving with the clock does not feel the clock slow down.
- Time dilation is reciprocal: S considers clocks at rest relative to S′ to run slow, and S′ also considers clocks at rest relative to S to run slow. There is no contradiction, because the two judgments compare different pairs of events and require different notions of "simultaneous".
- For $v\ll c$, $\Delta t\approx\tau$, which returns to absolute time.

**Example 8.5.1 (Lifetime of the $\pi$ Meson)** A charged $\pi$ meson decays into a $\mu$ lepton and a neutrino, $\pi^+\to\mu^++\nu_\mu$, with mean lifetime at rest $\tau\approx2.6\times10^{-8}\,\mathrm{s}$. If a beam of $\pi$ mesons moves at $v=0.99c$ and the measured mean flight distance is $l\approx53\,\mathrm{m}$, the mean lifetime in the laboratory is $\Delta t=l/v\approx1.8\times10^{-7}\,\mathrm{s}$, and $\tau/\Delta t\approx0.15$; the theoretical value is $\sqrt{1-\beta^2}=\sqrt{1-0.99^2}\approx0.14$, and the two agree within experimental error. Without time dilation the mean flight distance would be only $v\tau\approx7.7\,\mathrm{m}$. That $\mu$ leptons produced by cosmic rays at high altitude arrive at the ground in large numbers is also a result of time dilation.

### 8.5.3. Length Contraction

**Definition 8.5.2 (Proper Length)** The length of an object measured in the inertial frame in which the object is at rest is called its **proper length**, denoted $l_0$. Measuring the proper length requires measuring the coordinates of the two ends of the object, and the order of measurement does not matter. Measuring the length in a frame in which the object moves requires measuring the coordinates of the two ends simultaneously.

Let a rod lie at rest along the $x'$ axis in S′ with proper length $l_0=x_2'-x_1'$. In S the coordinates $x_1$, $x_2$ of the two ends are measured simultaneously ($\Delta t=0$); by (8.4), $\Delta x'=\gamma(\Delta x-v\Delta t)=\gamma\Delta x$, so

$$
l=x_2-x_1=\frac{l_0}{\gamma}=l_0\sqrt{1-\frac{v^2}{c^2}}<l_0.\tag{8.6}
$$

**Property 8.5.2 (Length Contraction)** In an inertial frame in which the object moves, the length of the object measured along the direction of motion is shorter than the proper length (the proper length is the longest). This is called *length contraction*.

Length contraction occurs only along the direction of motion; lengths perpendicular to the direction of motion are unchanged. Like time dilation, it does not mean that the structure of the rod has changed, and it is also reciprocal; an observer moving with the rod does not feel the rod shorten.

**Example 8.5.2** Solve Example 8.4.1 using length contraction. In the ground frame, the length of the carriage AM contracts to $l\sqrt{1-\beta^2}$. After being emitted from M, the light reaches A after a time $\Delta t$, during which A moves forward by $v\Delta t$, so $c\Delta t+v\Delta t=l\sqrt{1-\beta^2}$ and

$$
\Delta t=\frac{l\sqrt{1-\beta^2}}{c+v}=\sqrt{\frac{1-\beta}{1+\beta}}\,\frac lc=0.005\,\mathrm{s},
$$
the same as in Example 8.4.1.

**Example 8.5.3 (The Rod and the Doorway)** A thin rod whose proper length equals the width $l_0$ of a doorway in a wall translates at high speed along the wall and passes the doorway (neglect the thickness of the doorway). Can the rod be "pushed" entirely into the doorway at some instant? In the frame of the wall, the length of the rod contracts to $l_0\sqrt{1-\beta^2}<l_0$, and for some time the rod lies entirely between the two sides of the doorway, so it seems possible. In the frame of the rod, the doorway contracts while the rod has length $l_0$, so it seems impossible for the rod to lie entirely inside the doorway. The root of the contradiction is simultaneity: in the wall frame, "the front of the rod has not yet reached the far edge of the doorway" and "the rear of the rod has already passed the near edge of the doorway" are two simultaneous events, which are not simultaneous in the rod frame. In the rod frame, the front of the rod passes the far edge of the doorway first, and the rear passes the near edge only afterward; the rod is never entirely inside the doorway. If the points of the rod are pushed simultaneously in the wall frame, they are not pushed simultaneously in the rod frame, and the rod bends; so the two descriptions are not contradictory.

### 8.5.4. Absoluteness of Causality

Could the Lorentz transformation reverse the order of two events? Let the time interval and spatial interval between events $P_1$ and $P_2$ in S be $\Delta t=t_2-t_1$ and $\Delta x=x_2-x_1$, and write $v_{\mathrm{s}}=\Delta x/\Delta t$. By (8.4),

$$
\Delta t'=\gamma\Delta t\Big(1-\frac{v}{c^2}v_{\mathrm{s}}\Big).
$$
If $P_1$ is the cause of $P_2$, the influence (signal) emitted at $P_1$ must travel to $P_2$ with speed $v_{\mathrm{s}}$, and the speed of any signal does not exceed $c$, so $\lvert v_{\mathrm{s}}\rvert\le c$. Since also $\lvert v\rvert<c$, $1-\frac{v v_{\mathrm{s}}}{c^2}>0$ and $\Delta t'$ has the same sign as $\Delta t$:

**Property 8.5.3 (Absoluteness of Causality)** The temporal order of two events that are causally connected is the same in all inertial frames.

If $P_1$ and $P_2$ are independent of each other, $v_{\mathrm{s}}$ can exceed $c$, and an inertial frame with $v>c^2/v_{\mathrm{s}}$ reverses their temporal order (relativity of temporal order); this does not violate causality. Conversely, if there were signals faster than light, an effect could precede its cause in some inertial frame; causality requires that signal speeds do not exceed $c$.

### 8.5.5. Invariance of the Spacetime Interval

**Definition 8.5.3 (Spacetime Interval)** The spacetime interval $\Delta s$ between two events $P_1$ and $P_2$ is defined by

$$
(\Delta s)^2=c^2(\Delta t)^2-\big[(\Delta x)^2+(\Delta y)^2+(\Delta z)^2\big]=c^2(\Delta t)^2-(\Delta l)^2,
$$
where $\Delta t$ and $\Delta l$ are the time interval and spatial distance between the two events in the same inertial frame.

**Theorem 8.5.1 (Invariance of the Interval)** The spacetime interval is a Lorentz invariant: $(\Delta s')^2=(\Delta s)^2$.

**Proof** Direct computation from (8.4) gives $c^2(\Delta t')^2-(\Delta x')^2=\gamma^2\big[(c\Delta t-\beta\Delta x)^2-(\Delta x-\beta c\Delta t)^2\big]=\gamma^2(1-\beta^2)\big[c^2(\Delta t)^2-(\Delta x)^2\big]=c^2(\Delta t)^2-(\Delta x)^2$, while $\Delta y'=\Delta y$ and $\Delta z'=\Delta z$. $\square$

In the language of linear algebra, $(\Delta s)^2$ is a Lorentz form on $\mathbb{R}^4$ (an indefinite quadratic form of signature $(1,3)$), and the linear transformations that preserve it are the Lorentz transformations ([2.1.13](/2.1.13#ex-13.7.1), where the same computation is given). According to the sign of the interval, the relation between two events falls into three classes:

| Interval | Type | Physical meaning |
|---|---|---|
| $(\Delta s)^2>0$ | Timelike | May be causally connected; there is an inertial frame in which the two events occur at the same place, and the temporal order is the same in all inertial frames |
| $(\Delta s)^2=0$ | Lightlike | May be connected by a light signal, $\Delta l=c\Delta t$ |
| $(\Delta s)^2<0$ | Spacelike | Cannot be causally connected; there is an inertial frame in which the two events are simultaneous, and the temporal order can be reversed |

For two events at the same place, $\Delta l=0$ and $\Delta s=c\tau$, so the proper time $\tau=\Delta s/c$ is also a Lorentz invariant: different inertial frames agree on "the time elapsed on the same clock". The time dilation formula (8.5) is precisely a consequence of this invariance: $c^2\tau^2=c^2(\Delta t)^2-v^2(\Delta t)^2$.

**Example 8.5.4** The time interval between two events occurring at the same place in S′ is $4\,\mathrm{s}$, and in S it is $5\,\mathrm{s}$. Find the spatial distance between the two events in S.

**Solution** By the invariance of the interval, $c^2(5\,\mathrm{s})^2-(\Delta l)^2=c^2(4\,\mathrm{s})^2$, so $\Delta l=c\times3\,\mathrm{s}\approx9.0\times10^8\,\mathrm{m}$. From this the relative velocity of the two frames is also found, $v=\Delta l/\Delta t=0.6c$.

### 8.5.6. The Twin Problem

Of a pair of twins, the elder brother travels at high speed by spaceship to a distant star and back, while the younger stays on the Earth. By time dilation, the younger brother considers the elder brother's clock to run slow, and the elder brother considers the younger brother's clock to run slow; which of them is younger when they meet again? This is the twin paradox.

The resolution of the paradox is that the roles of the two are not symmetric: the Earth is (approximately) always an inertial frame, whereas the spaceship must turn around, undergoes **acceleration** at the turnaround and is not always in the same inertial frame. The problem can be solved entirely within special relativity, without general relativity: in the Earth's inertial frame, the proper time of the traveler accumulates along his worldline,

$$
\tau=\int\sqrt{1-\frac{v(t)^2}{c^2}}\,\mathrm{d}t,
$$
and is always less than the time $\int\mathrm{d}t$ on the Earth, independently of the details of the acceleration (the acceleration phases can be arbitrarily short). For example, if the spaceship travels at $0.8c$ to a star $4$ light-years away and back, when $10$ years have elapsed on the Earth the elder brother has aged only $10\times0.6=6$ years: on reunion the elder brother is younger. This is called the twin effect. From the elder brother's point of view, at the turnaround he changes from one inertial frame to another, and the Earth time he regards as "simultaneous" with his own jumps, making up the difference.

Effects of this kind have been verified directly by experiment. In 1971 Hafele and Keating flew cesium atomic clocks around the world on commercial airliners, eastward and westward, and compared them with the atomic clocks of the US Naval Observatory: the eastward-flown clocks lost $(59\pm10)\,\mathrm{ns}$ (predicted $(40\pm23)\,\mathrm{ns}$) and the westward-flown clocks gained $(273\pm7)\,\mathrm{ns}$ (predicted $(275\pm21)\,\mathrm{ns}$), in agreement between experiment and theory. The predictions include both the special-relativistic effect due to motion and the gravitational (general-relativistic) effect due to altitude. Today the clocks of GPS satellites must be corrected for both effects for positioning to work.

### 8.5.7. The Doppler Effect of Light

[5.1.7](/5.1.7#sec-7.9.2) gave the Doppler formula for electromagnetic waves; we now derive it using time dilation. In the inertial frame of the receiver R, let the source S move with velocity $v$ at angle $\theta$ to the direction from S to R, with R very far from S. The period $T_0=1/\nu_{\mathrm{S}}$ of the source in its own frame is a proper time (two successive crests are emitted at the same place at the source), so in the frame of R the two emissions are separated by $\gamma T_0$. During this time the source approaches R by $v\gamma T_0\cos\theta$, the later crest travels this much less distance, and the time interval between arrivals at R is

$$
T_{\mathrm{R}}=\gamma T_0-\frac{v\gamma T_0\cos\theta}{c}=\gamma T_0(1-\beta\cos\theta).
$$
Hence

$$
\nu_{\mathrm{R}}=\frac{\nu_{\mathrm{S}}}{\gamma(1-\beta\cos\theta)}=\frac{\sqrt{1-\beta^2}}{1-\beta\cos\theta}\,\nu_{\mathrm{S}}.\tag{8.7}
$$
Compared with the formula for **mechanical waves** [5.1.7](/5.1.7#fml-7.9.1), the factor $1-\beta\cos\theta$ in the denominator is the classical factor by which the motion of the source compresses the **wavelength**, and the factor $\sqrt{1-\beta^2}$ in the numerator is the time dilation of the source. $\theta=0$ and $\theta=\pi$ give the longitudinal Doppler effect $\nu_{\mathrm{R}}=\sqrt{\frac{1\pm\beta}{1\mp\beta}}\nu_{\mathrm{S}}$; for $\theta=\pi/2$ there is still $\nu_{\mathrm{R}}=\nu_{\mathrm{S}}/\gamma$, a purely relativistic effect (the transverse Doppler effect), first confirmed in 1938 by Ives and Stilwell using the spectrum of a beam of fast hydrogen ions. The longitudinal formula depends only on the relative velocity: computing the case of the receiver moving toward the source in the frame of the source gives the same result, as the principle of relativity requires. Note that the $\theta$ in Eq. (8.7) is measured in the frame of the receiver; the angle measured in the frame of the source is different (aberration of light).

## 8.6. Relativistic Velocity Transformation

Let the velocities of the same **particle** in S and S′ be $\boldsymbol{u}=(u_x,u_y,u_z)$ and $\boldsymbol{u}'$ respectively (in this section $u$ denotes the velocity of the particle, to distinguish it from the relative velocity $v$ of the two reference frames). Taking differentials of the Lorentz transformation (8.3):

$$
\mathrm{d}x'=\gamma(\mathrm{d}x-v\,\mathrm{d}t),\qquad \mathrm{d}t'=\gamma\Big(\mathrm{d}t-\frac{v}{c^2}\mathrm{d}x\Big)=\gamma\,\mathrm{d}t\Big(1-\frac{vu_x}{c^2}\Big),\qquad \mathrm{d}y'=\mathrm{d}y,\qquad \mathrm{d}z'=\mathrm{d}z,
$$
and dividing them in pairs gives:

**Theorem 8.6.1 (Relativistic Velocity Transformation)**

$$
u_x'=\frac{u_x-v}{1-\dfrac{vu_x}{c^2}},\qquad u_y'=\frac{u_y}{\gamma\Big(1-\dfrac{vu_x}{c^2}\Big)},\qquad u_z'=\frac{u_z}{\gamma\Big(1-\dfrac{vu_x}{c^2}\Big)};\tag{8.8}
$$
the inverse transformation is obtained by exchanging primed and unprimed quantities and replacing $v$ by $-v$: $u_x=\frac{u_x'+v}{1+vu_x'/c^2}$, $u_y=\frac{u_y'}{\gamma(1+vu_x'/c^2)}$, $u_z=\frac{u_z'}{\gamma(1+vu_x'/c^2)}$.

Remarks:

1. For $v\ll c$, $u\ll c$ it goes over into the Galilean velocity transformation $\boldsymbol{u}'=\boldsymbol{u}-\boldsymbol{v}$.
2. Unlike **displacement**, the velocity components perpendicular to the direction of relative motion also transform, because the time interval has changed.
3. A speed exceeding the speed of light cannot be obtained by a change of reference frame (see the identity below).

From (8.8) one can verify the identity

$$
1-\frac{u'^2}{c^2}=\frac{\big(1-\frac{v^2}{c^2}\big)\big(1-\frac{u^2}{c^2}\big)}{\big(1-\frac{vu_x}{c^2}\big)^2},
$$
so $u<c$ implies $u'<c$ and $u=c$ implies $u'=c$: the speed of light is the same in all inertial frames, which is precisely the constancy of the speed of light.

**Example 8.6.1** A spaceship flies at $0.80c$ relative to the ground and throws an object from the ship along the direction of flight, with velocity $0.90c$ relative to the ship. Find the velocity of the object measured on the ground.

**Solution** Take the ground as S and the spaceship as S′, $v=0.80c$, $u_x'=0.90c$. By the inverse transformation,

$$
u_x=\frac{0.90c+0.80c}{1+0.80\times0.90}=\frac{1.70}{1.72}c\approx0.99c,
$$
instead of the $1.70c$ given by the Galilean transformation.

**Example 8.6.2** In S′ a beam of light propagates along the $y'$ axis, and S′ moves relative to S with $0.8c$ along the $x$ direction. Find the speed of light in S.

**Solution** $v=0.8c$, $u_x'=0$, $u_y'=c$, $u_z'=0$. By the inverse transformation, $u_x=v=0.8c$, $u_y=\frac{c}{\gamma}=c\sqrt{1-0.64}=0.6c$ and $u_z=0$, so $u=\sqrt{u_x^2+u_y^2}=c$. The constancy of the speed of light means that the speed of propagation of light is the same in different reference frames, not that its direction of propagation is the same: in S the light propagates at an angle $\arctan(0.6/0.8)\approx37^\circ$ to the $x$ axis (aberration of light).

## 8.7. Relativistic Momentum

From this section on, $\boldsymbol{v}$ denotes the velocity of a particle relative to some inertial frame, and $\gamma=1/\sqrt{1-v^2/c^2}$ is the Lorentz factor of the particle.

Relativistic dynamics is built by retaining the basic conservation laws of momentum, energy and so on. The basic requirements are: by the principle of relativity, the basic laws (conservation laws, dynamical equations) are invariant in form under the Lorentz transformation; and for $v\ll c$ they go over into Newtonian mechanics.

The Newtonian momentum $m\boldsymbol{v}$ does not satisfy the first requirement: one can verify that if a collision conserves $\sum m_i\boldsymbol{v}_i$ in S, the quantity is in general no longer conserved after transforming to S′ with the relativistic velocity transformation (8.8). The problem lies in time: the $\mathrm{d}t$ in $\mathrm{d}\boldsymbol{r}/\mathrm{d}t$ depends on the reference frame, whereas the proper time $\mathrm{d}\tau=\mathrm{d}t/\gamma$ is invariant ([Section 8.5.5](#sec-8.5.5)). Using it in place of $\mathrm{d}t$ gives:

**Definition 8.7.1 (Relativistic Momentum)** The **relativistic momentum** of a particle of mass $m$ and velocity $\boldsymbol{v}$ is

$$
\boldsymbol{p}=m\frac{\mathrm{d}\boldsymbol{r}}{\mathrm{d}\tau}=\gamma m\boldsymbol{v}=\frac{m\boldsymbol{v}}{\sqrt{1-v^2/c^2}}.\tag{8.9}
$$
Here $m$ is the mass of the particle (the invariant mass), independent of the reference frame and of the velocity.

Experiments (for example the deflection of charged particles in a magnetic field, [Section 8.8](#sec-8.8)) confirm that the momentum defined by (8.9) is conserved in an isolated system, and conserved in all inertial frames. For $v\ll c$, $\boldsymbol{p}\approx m\boldsymbol{v}$, returning to Newtonian mechanics; for $v\to c$, $p\to\infty$, so a body with mass cannot be accelerated to the speed of light.

**Example 8.7.1** A particle at rest (mass $M$) splits into two pieces A and B, each of mass $m$; in the frame S′ in which the particle was originally at rest, the two pieces move along the $x$ direction with $-v$ and $+v$ respectively. Analyze the process in the frame S moving with A.

**Solution** S′ moves with $v$ relative to S. By the velocity transformation, A is at rest in S, B has velocity $v_B=\frac{2v}{1+\beta^2}$, and the particle before the split moves with $v$. One finds $1-v_B^2/c^2=\big(\frac{1-\beta^2}{1+\beta^2}\big)^2$, that is, $\gamma_B=\frac{1+\beta^2}{1-\beta^2}=2\gamma^2-1$. In S, conservation of momentum requires

$$
\gamma Mv=0+\gamma_Bmv_B=\frac{2mv}{1-\beta^2}=2\gamma^2mv,
$$
so $M=2\gamma m>2m$: the mass of the particle before the split exceeds the sum of the masses of the two pieces afterward; in relativity mass is not additive. In S′ we verify conservation of energy ([Section 8.9](#sec-8.9)): $Mc^2=2\gamma mc^2$, which likewise holds. The role of $\gamma_B m$ can also be read off from the momentum conservation equation: if $m_B=\gamma_Bm$ is called the "mass" of B, the momentum can still be written as "mass times velocity".

**Remark 8.7.1 (Relativistic Mass)** Many older textbooks (including the textbook used in this course) call $m(v)=\gamma m_0$ the "relativistic mass" or "moving mass" and $m_0$ the "rest mass", so that $\boldsymbol{p}=m(v)\boldsymbol{v}$ and $E=m(v)c^2$. This notation is numerically equivalent to that of this chapter, but modern physics literature (including the Particle Data Group) uses only the invariant mass $m$, which does not change with velocity: $m(v)$ is merely another name for the total energy $E/c^2$, it does not satisfy $\boldsymbol{F}=m(v)\boldsymbol{a}$ ([Section 8.8](#sec-8.8)), and it can mislead one into thinking that the "inertia" or gravitational mass of a fast-moving body has "increased". This wiki uses $\boldsymbol{p}=\gamma m\boldsymbol{v}$ and $E=\gamma mc^2$ throughout, with $m$ the mass of the particle.

| Total energy of an electron $E/\mathrm{MeV}$ | $\gamma=E/(mc^2)$ | $v/c$ |
|---|---|---|
| $5$ | $9.78$ | $0.9948$ |
| $25$ | $48.9$ | $0.99979$ |
| $2.8\times10^3$ | $5.48\times10^3$ | $0.999\,999\,983$ |

(The rest energy of the electron is $mc^2=0.511\,\mathrm{MeV}$. When the energy increases by a factor of 560, the speed increases only from $0.995c$ to $0.999\,999\,98c$.)

## 8.8. The Relativistic Equation of Motion

Retain the definition of force as "the rate of change of momentum":

$$
\boldsymbol{F}=\frac{\mathrm{d}\boldsymbol{p}}{\mathrm{d}t}=\frac{\mathrm{d}}{\mathrm{d}t}(\gamma m\boldsymbol{v})=\gamma m\boldsymbol{a}+m\frac{\mathrm{d}\gamma}{\mathrm{d}t}\boldsymbol{v}.\tag{8.10}
$$
From $\frac{\mathrm{d}\gamma}{\mathrm{d}t}=\gamma^3\frac{v}{c^2}\frac{\mathrm{d}v}{\mathrm{d}t}=\gamma^3\frac{\boldsymbol{v}\cdot\boldsymbol{a}}{c^2}$, decomposing the acceleration into the tangential component $a_{\mathrm{t}}=\mathrm{d}v/\mathrm{d}t$ (along $\boldsymbol{v}$) and the normal component $a_{\mathrm{n}}=v^2/\rho$ (the **intrinsic coordinates** of [5.1.1](/5.1.1)), we get

$$
F_{\mathrm{t}}=\gamma ma_{\mathrm{t}}+m\gamma^3\frac{v^2}{c^2}a_{\mathrm{t}}=\gamma^3ma_{\mathrm{t}},\qquad F_{\mathrm{n}}=\gamma ma_{\mathrm{n}}.
$$

Therefore:

- Force and acceleration are in general not parallel ($\boldsymbol{F}=m\boldsymbol{a}$ does not hold, whatever "mass" is used);
- The greater the speed, the harder it is to accelerate;
- Accelerating along the velocity (coefficient $\gamma^3m$) is harder than changing the direction of the velocity (coefficient $\gamma m$).

For $v\ll c$, $\gamma\approx1$, which returns to $\boldsymbol{F}=m\boldsymbol{a}$. When $\boldsymbol{F}\perp\boldsymbol{v}$ the speed is constant and $\boldsymbol{F}=\gamma m\boldsymbol{a}$. For example, an electron of charge $-e$ moving in a circle perpendicular to a uniform magnetic field $\boldsymbol{B}$ has the Lorentz force $evB$ providing the centripetal force ([5.3.7](/5.3.7)):

$$
evB=\gamma m\frac{v^2}{R},\qquad R=\frac{\gamma mv}{eB}=\frac{p}{eB}.
$$
Measuring the radius of the orbit gives the momentum. Measurements of the deflection of fast electrons in electromagnetic fields by Kaufmann, Bucherer and others in the early 20th century were the first to verify the relativistic expression for momentum.

## 8.9. Relativistic Energy

### 8.9.1. Relativistic Kinetic Energy

Retain the **work–energy theorem** ([5.1.4](/5.1.4)): the **work** done by the net force equals the increase of the **kinetic energy**, $\mathrm{d}E_{\mathrm{k}}=\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{r}=\frac{\mathrm{d}\boldsymbol{p}}{\mathrm{d}t}\cdot\boldsymbol{v}\,\mathrm{d}t=\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{p}$. From $\boldsymbol{p}=\gamma m\boldsymbol{v}$,

$$
\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{p}=m\big(\gamma v\,\mathrm{d}v+v^2\,\mathrm{d}\gamma\big)=m\big(\gamma+\gamma^3\beta^2\big)v\,\mathrm{d}v=m\gamma^3v\,\mathrm{d}v=mc^2\,\mathrm{d}\gamma,
$$
where we used $\mathrm{d}\gamma=\gamma^3v\,\mathrm{d}v/c^2$ and $\gamma(1+\gamma^2\beta^2)=\gamma^3$. Integrating from rest ($\gamma=1$) to velocity $v$:

**Formula 8.9.1 (Relativistic Kinetic Energy)**

$$
E_{\mathrm{k}}=(\gamma-1)mc^2=\frac{mc^2}{\sqrt{1-v^2/c^2}}-mc^2.\tag{8.11}
$$

For $v\ll c$, $\gamma=1+\frac12\beta^2+\frac38\beta^4+\cdots$ and $E_{\mathrm{k}}\approx\frac12mv^2+\frac38\frac{mv^4}{c^2}$; the leading term is the kinetic energy of Newtonian mechanics. Note that $\boldsymbol{p}=\gamma m\boldsymbol{v}$ is the relativistic momentum, but $\frac12\gamma mv^2$ is not the relativistic kinetic energy. For $v\to c$, $E_{\mathrm{k}}\to\infty$: accelerating a body with mass to the speed of light requires infinite energy.

![Left: the Lorentz factor gamma as a function of beta = v/c; right: comparison of the relativistic kinetic energy (gamma - 1) m c^2 with the Newtonian kinetic energy m v^2 / 2, which nearly coincide for beta below about 0.3](./plots/lorentz-factor-energy.py)

### 8.9.2. Rest Energy and the Mass–Energy Relation

In Eq. (8.11), $\gamma mc^2$ and $mc^2$ each have a physical meaning.

**Definition 8.9.1** $E_0=mc^2$ is called the **rest energy** of the particle, and $E=\gamma mc^2=E_{\mathrm{k}}+mc^2$ is called the total energy (relativistic energy) of the particle.

A body at rest also has energy $E_0=mc^2$, which includes the kinetic energies of all the particles inside the body, their interaction **potential energy** (for example, the binding energy of an atomic nucleus), and so on. The *mass–energy relation* proposed by Einstein,

$$
E_0=mc^2,\qquad E=\gamma mc^2\tag{8.12}
$$
says that mass is a measure of the rest energy contained in a body: when the rest energy of a system changes by $\Delta E_0$, its mass changes correspondingly by $\Delta m=\Delta E_0/c^2$. In relativity, conservation of energy and of momentum still hold, while the independent law of conservation of mass of Newtonian mechanics is absorbed into conservation of energy: the total energy $\sum\gamma_im_ic^2$ of an isolated system is conserved, while the sum of the masses of the particles is not necessarily conserved.

For an isolated system of several particles, the total energy is conserved before and after a reaction, $\Delta E_{\mathrm{k}}+\Delta\big(\sum m_ic^2\big)=0$, so

$$
\Delta E_{\mathrm{k}}=\Big(\sum m_{i,\mathrm{initial}}-\sum m_{i,\mathrm{final}}\Big)c^2=\Delta m\,c^2.
$$
The decrease $\Delta m$ of the sum of the particle masses before and after the reaction is called the *mass defect*; the rest energy corresponding to the mass defect is converted into kinetic energy of the reaction products (energy is released).

**Example 8.9.1 (D–T Fusion)** In the thermonuclear reaction $\ce{^2_1H + ^3_1H -> ^4_2He + ^1_0n}$, the atomic masses ($m_{\mathrm{D}}=2.014\,10\,\mathrm{u}$, $m_{\mathrm{T}}=3.016\,05\,\mathrm{u}$, $m_{\mathrm{He}}=4.002\,60\,\mathrm{u}$, $m_{\mathrm{n}}=1.008\,66\,\mathrm{u}$) give the mass defect

$$
\Delta m=(m_{\mathrm{D}}+m_{\mathrm{T}})-(m_{\mathrm{He}}+m_{\mathrm{n}})=0.018\,88\,\mathrm{u}\approx3.136\times10^{-29}\,\mathrm{kg},
$$
and the energy released is $\Delta E=\Delta m\,c^2\approx2.818\times10^{-12}\,\mathrm{J}\approx17.6\,\mathrm{MeV}$ ($1\,\mathrm{u}\cdot c^2=931.494\,\mathrm{MeV}$). Each kilogram of D–T fuel releases about $3.4\times10^{14}\,\mathrm{J}$, about ten million times the heat of combustion of $1\,\mathrm{kg}$ of good coal (about $2.9\times10^7\,\mathrm{J}$). The mass–energy relation ushered in the atomic age.

**Example 8.9.2** Two identical particles of mass $m$ move toward each other with the same speed $v$ and combine into a composite particle after the collision. Find the velocity and mass of the composite particle.

**Solution** Let the composite particle have mass $M$ and velocity $V$. Conservation of momentum: $\gamma mv-\gamma mv=\gamma_VMV$, so $V=0$. Conservation of energy: $2\gamma mc^2=Mc^2$, so

$$
M=2\gamma m=\frac{2m}{\sqrt{1-v^2/c^2}}>2m.
$$
The kinetic energy lost in the collision, $2(\gamma-1)mc^2$, is entirely converted into the rest energy of the composite particle, whose mass is therefore greater than $2m$. In Newtonian mechanics this kinetic energy "turns into heat"; in relativity, the energy of thermal motion is already counted in the rest energy of the body.

### 8.9.3. The Energy–Momentum Relation

From $E=\gamma mc^2$ and $p=\gamma mv$, $E^2-p^2c^2=\gamma^2m^2c^4(1-\beta^2)=m^2c^4$, that is,

**Formula 8.9.2 (Energy–Momentum Relation)**

$$
E^2=p^2c^2+m^2c^4.\tag{8.13}
$$

$E$, $pc$ and $mc^2$ form the hypotenuse and the two legs of a right triangle. The quantity $E^2-p^2c^2=m^2c^4$ is independent of the reference frame ([Section 8.10](#sec-8.10)), so the mass $m$ is a Lorentz invariant. From $E=E_{\mathrm{k}}+mc^2$ we also obtain the kinetic energy–momentum relation

$$
E_{\mathrm{k}}^2+2E_{\mathrm{k}}mc^2=p^2c^2.
$$
For $v\ll c$, $E_{\mathrm{k}}\ll mc^2$ and dropping $E_{\mathrm{k}}^2$ gives $E_{\mathrm{k}}\approx\frac{p^2}{2m}$, the kinetic energy–momentum relation of Newtonian mechanics; in the extreme relativistic case $E_{\mathrm{k}}\gg mc^2$, $E\approx pc$. From (8.13) and $E=\gamma mc^2$ there is also a commonly used relation $\boldsymbol{v}=\frac{\boldsymbol{p}c^2}{E}$.

### 8.9.4. The Photon

For a particle of zero mass, (8.13) gives $E=pc$, and from $\boldsymbol{v}=\boldsymbol{p}c^2/E$ its speed is always $c$. Conversely, a particle moving at the speed of light must have zero mass (otherwise $\gamma\to\infty$ and the energy would be infinite). The photon is such a particle ([5.5.1](/5.5.1)): in Einstein's photon theory, the energy and momentum of a photon of frequency $\nu$ are

$$
E=h\nu,\qquad p=\frac{E}{c}=\frac{h\nu}{c}=\frac{h}{\lambda}.
$$
The mass of the photon is zero, and all its energy is kinetic energy. Older textbooks call $h\nu/c^2$ the "moving mass" of the photon; in the current notation this is merely $E/c^2$, not the mass of the photon (Remark 8.7.1). The momentum of the photon shows up directly in radiation pressure and in Compton scattering.

## 8.10. Transformation of Momentum and Energy

From $\boldsymbol{p}=\gamma m\boldsymbol{v}$, $E=\gamma mc^2$ and the velocity transformation (8.8), we can find the transformation of the momentum and energy of the same particle between S and S′ ($v$ is the relative velocity of the two frames and $\gamma$ the Lorentz factor between them):

**Theorem 8.10.1 (Momentum–Energy Transformation)**

$$
p_x'=\gamma\Big(p_x-\frac{v}{c^2}E\Big),\qquad p_y'=p_y,\qquad p_z'=p_z,\qquad E'=\gamma(E-vp_x).\tag{8.14}
$$

Comparing with the Lorentz transformation (8.3), $p_x\leftrightarrow x$, $p_y\leftrightarrow y$, $p_z\leftrightarrow z$ and $E/c^2\leftrightarrow t$: $(E/c,\boldsymbol{p})$ and $(ct,\boldsymbol{r})$ transform in the same way. $(E/c,p_x,p_y,p_z)$ is called the *four-momentum*, and $(ct,x,y,z)$ the four-dimensional **position vector**; their "squared lengths" $E^2/c^2-p^2=m^2c^2$ and $c^2t^2-r^2$ are both unchanged under the action of the **Lorentz group** ([2.1.13](/2.1.13#ex-13.7.1)). This shows that in relativity, energy and momentum are components of one four-vector, just as time and space are coordinates of one spacetime.

## 8.11. Transformation of Force

From $\boldsymbol{F}=\mathrm{d}\boldsymbol{p}/\mathrm{d}t$, the momentum–energy transformation (8.14) and $\mathrm{d}E/\mathrm{d}t=\boldsymbol{F}\cdot\boldsymbol{u}$, we can find the transformation of the force on a particle between two inertial frames. Let the velocity of the particle in S′ be $\boldsymbol{u}'$; the result is

$$
F_x=\frac{F_x'+\dfrac{v}{c^2}\boldsymbol{F}'\cdot\boldsymbol{u}'}{1+\dfrac{vu_x'}{c^2}},\qquad F_y=\frac{F_y'}{\gamma\Big(1+\dfrac{vu_x'}{c^2}\Big)},\qquad F_z=\frac{F_z'}{\gamma\Big(1+\dfrac{vu_x'}{c^2}\Big)}.
$$
In particular, if the particle is instantaneously at rest in S′ ($\boldsymbol{u}'=\boldsymbol{0}$, moving with $v$ in S), then

$$
F_x=F_x',\qquad F_y=\frac{F_y'}{\gamma},\qquad F_z=\frac{F_z'}{\gamma}:
$$
the component of force along the direction of motion is unchanged, and the perpendicular components become $1/\gamma$ of their values. This result is used in electromagnetism: a charge at rest is acted on only by the electric force in its rest frame, and on transforming to a moving frame, the transformation of force requires a velocity-dependent magnetic force to appear, from which the transformation of the electric and magnetic fields can be derived from Coulomb's law and relativity ([5.3](/5.3)).

## Summary

| Topic | Key points |
|---|---|
| Fundamental principles | Einstein's principle of relativity; constancy of the speed of light |
| Lorentz transformation | $x'=\gamma(x-vt)$, $t'=\gamma(t-vx/c^2)$, $\gamma=1/\sqrt{1-v^2/c^2}$; returns to the Galilean transformation for $v\ll c$ |
| Simultaneity | Events simultaneous at different places in S′ have $\Delta t=\gamma v\Delta x'/c^2$ in S; the one at the rear occurs first |
| Time dilation | $\Delta t=\gamma\tau$; the proper time is the shortest |
| Length contraction | $l=l_0/\gamma$; the proper length is the longest; only along the direction of motion |
| Interval | $(\Delta s)^2=c^2(\Delta t)^2-(\Delta l)^2$ is invariant; the temporal order of causally connected events is invariant |
| Velocity transformation | $u_x'=\frac{u_x-v}{1-vu_x/c^2}$, $u_y'=\frac{u_y}{\gamma(1-vu_x/c^2)}$; speeds above that of light are impossible |
| Momentum and force | $\boldsymbol{p}=\gamma m\boldsymbol{v}$, $\boldsymbol{F}=\mathrm{d}\boldsymbol{p}/\mathrm{d}t$; $F_{\mathrm{t}}=\gamma^3ma_{\mathrm{t}}$, $F_{\mathrm{n}}=\gamma ma_{\mathrm{n}}$ |
| Energy | $E=\gamma mc^2$, $E_0=mc^2$, $E_{\mathrm{k}}=(\gamma-1)mc^2$, $E^2=p^2c^2+m^2c^4$; photon $E=pc=h\nu$ |
| Four-momentum | $(E/c,\boldsymbol{p})$ transforms like $(ct,\boldsymbol{r})$ |

## Questions

1. Time dilation says "moving clocks run slow", and S and S′ each consider the other's clocks to be slow. Is this self-contradictory?

   **Answer** the two judgments compare different pairs of events; each reference frame uses its own row of synchronized clocks, and the other frame considers this row not to be synchronized ([Section 8.3](#sec-8.3)).

2. Can the mass of a particle be changed by accelerating it? What is wrong with the statement that "the mass of a moving body increases"?

   **Answer** the mass $m$ is a Lorentz invariant ($E^2-p^2c^2=m^2c^4$); what increases is the energy $\gamma mc^2$ and the momentum (Remark 8.7.1).

3. Does the mass of a box change when the gas in it is heated?

   **Answer** yes, $\Delta m=\Delta E_0/c^2$, but for everyday amounts of heat $\Delta m$ is too small to measure ($1\,\mathrm{J}$ corresponds to $1.1\times10^{-17}\,\mathrm{kg}$).

4. The spot of a searchlight sweeping across distant clouds can move faster than $c$. Does this violate relativity?

   **Answer** the illumination of different positions on the spot consists of different events with no causal connection; no signal or energy is transmitted, and $c$ imposes no limit.
