---
title: Hemodynamics, Arteries and Veins
description: Functions and classification of the vascular system; cross-sectional area and flow velocity; laminar flow, turbulent flow and the Reynolds number; driving pressure, hydrostatic pressure and transmural pressure; the Ohm's law of blood flow, the PRU and the Poiseuille law; viscosity, hematocrit and the Fåhræus–Lindqvist effect; series and parallel; Laplace's law, compliance and delayed compliance; systolic pressure, diastolic pressure, pulse pressure, mean arterial pressure and the Windkessel model; the Moens–Korteweg equation for pulse wave velocity; central venous pressure, gravity, venous valves and the muscle pump, blood reservoirs; the giraffe, snakes and Murray's law.
source_hash: e24c4ca13158
---

Chapters 12 and 13 treated the heart as a pump that ejects about $70\,\mathrm{mL}$ of blood per beat and about $5\,\mathrm{L}$ per minute ([7.14.12](/7.14.12)). This chapter follows that blood out of the heart and asks how the vascular system turns an intermittent, high-pressure output into continuous, steady flow distributed on demand throughout the body. The physics used is elementary fluid mechanics: continuity, pressure and resistance, the **Hagen–Poiseuille law** of viscous flow, and the mechanics of elastic vessel walls (derivations in biophysics, [7.6.22](/7.6.22)). This physics determines several basic facts of the circulation: why blood pressure falls fastest in the arterioles, why arterial pressure is pulsatile while flow in the capillaries is continuous, why the arterial pressure in the feet approaches $190\,\mathrm{mmHg}$ on standing, and why most of the blood is stored in the veins. The next chapter takes up exchange between the capillaries and the interstitial fluid ([7.14.15](/7.14.15)), and Chapter 16 discusses how nerves and humoral factors regulate these quantities ([7.14.16](/7.14.16)).

## 14.1. Functions and Classification of the Vascular System

### 14.1.1. Three Features of the Vascular System

The vascular system is the logistics infrastructure of the body and has three features.

1. Transport: it delivers $\ce{O2}$ and nutrients to the tissues, carries away $\ce{CO2}$ and metabolic wastes, and is also the channel for humoral regulatory signals such as hormones.
2. Flow is set by demand: the blood flow of each organ is regulated first by local needs (local feedback within a single organ, Chapter 15), and for the body as a whole it is ensured by the output of the heart and by integrated control of the nervous and endocrine systems (Chapter 16).
3. Exchange with body fluids: in the microcirculation it exchanges substances with the interstitial fluid; some special organs (liver, kidney) maintain the composition of the blood itself; others (brain, heart) have special circulations and protective mechanisms (Chapter 16).

### 14.1.2. Functional Classification of Vessels and Distribution of Blood Volume

By function in the circulation, vessels fall into six classes:

| Type | Vessels | Structural features | Function |
|---|---|---|---|
| Elastic reservoir vessels | Aorta, main pulmonary artery and their large branches | Thick walls rich in elastic fibers | Distend in systole to store blood and energy, recoil in diastole to propel blood (Section 14.5.2) |
| Distribution vessels | Medium-sized arteries | Relatively more smooth muscle | Deliver blood to the organs |
| Resistance vessels | Small arteries and arterioles (precapillary resistance vessels); venules (postcapillary resistance vessels) | Small caliber, relatively thick smooth muscle layer, controlled by nerves and local factors | Form the main peripheral resistance and distribute the blood flow of the organs |
| Exchange vessels | True capillaries | Only a single endothelial layer and basement membrane | Exchange of substances between blood and interstitial fluid (Chapter 15) |
| Capacitance vessels | The venous system | Thin walls, large lumen, easily distended | Store blood (Section 14.6.4) |
| Shunt vessels | Arteriovenous anastomoses | Found mainly in the skin of fingers, toes and the ear | Regulate skin blood flow and heat loss (Chapter 16) |

The blood volume of an adult is about 7% of body weight (about $5\,\mathrm{L}$). About 84% of it is in the *systemic circulation*: veins about 64%, arteries about 13%, arterioles and capillaries about 7%; the heart holds about 7% and the *pulmonary circulation* about 9%. The veins hold about two thirds of the blood, a fact that comes from their high compliance (Section 14.4.2) and also makes the veins a blood reservoir that can be mobilized.

### 14.1.3. Structure of the Vessel Wall

Except for capillaries, vessel walls consist of three layers: the intima (endothelial cells and the connective tissue beneath them), the media (smooth muscle with elastic and collagen fibers) and the adventitia (loose connective tissue containing vasa vasorum and nerves). The proportions of the three components determine the mechanical properties of the vessel: elastic fibers provide elasticity at low strain, collagen provides stiffness and tensile strength at high strain, and smooth muscle provides actively adjustable tension ([7.14.10](/7.14.10)). Large arteries are mainly elastic fibers, small arteries mainly smooth muscle, and veins have thin walls in all three layers with little smooth muscle. Except for capillaries, the smooth muscle of nearly all vessels is innervated by vasoconstrictor fibers of the **sympathetic nervous system** (Chapter 16), and the endothelium regulates smooth muscle by releasing factors such as NO (Chapter 15).

## 14.2. Blood Flow, Velocity and Cross-Sectional Area

### 14.2.1. Blood Flow and Continuity

**Definition 14.2.1 (Blood Flow)** The volume of blood flowing through a cross section of a vessel per unit time is called the **blood flow**, denoted $F$ (often also $Q$), in units of $\mathrm{mL\,s^{-1}}$ or $\mathrm{L\,min^{-1}}$.

Blood is almost incompressible and the circulation is closed, so in the steady state the volume of blood passing per minute through any "whole cross section" of the systemic circulation (for example the total cross section of all the capillaries) equals the **cardiac output**, about $5\,\mathrm{L\,min^{-1}} \approx 83\,\mathrm{mL\,s^{-1}}$. If the total cross-sectional area of the vessels there is $A$ and the mean velocity is $v$, then

$$
F = vA, \qquad v = \frac{F}{A}. \tag{14.1}
$$

Vessels branch level by level and each becomes narrower, but their number increases faster, so the total cross-sectional area increases from about $2.5\,\mathrm{cm^2}$ in the aorta to about $2500\,\mathrm{cm^2}$ in the capillaries, and then decreases again as the vessels merge in the veins. The velocity falls accordingly from about $33\,\mathrm{cm\,s^{-1}}$ in the aorta to about $0.03\,\mathrm{cm\,s^{-1}}$ ($0.3\,\mathrm{mm\,s^{-1}}$) in the capillaries. The total cross-sectional area of the veins is larger than that of the corresponding arteries (about 4-fold), which is the other side of venous storage of blood.

![Total cross-sectional area, mean velocity and blood pressure at each level of the systemic circulation. A: total cross-sectional area (log scale); the capillary bed is about 1000 times the aorta; the cross-sectional area of the veins is larger than that of arteries of the same level. B: mean velocity from continuity v = F/A; F = 83 mL/s is the same at every level, about 33 cm/s in the aorta and about 0.03 cm/s in the capillaries. C: blood pressure (schematic): the pulsation in the aorta (shading shows the range between systolic and diastolic pressure) is gradually smoothed out in the small arteries and arterioles; the mean pressure falls fastest in the small arteries and arterioles, which is where most of the resistance lies (Section 14.3.6)](./plots/circulation-profile.py)

**Example 14.2.1 (Residence Time in a Capillary)** A capillary is about $1\,\mathrm{mm}$ long and blood flows through it at $0.3$–$1\,\mathrm{mm\,s^{-1}}$, a residence time of about $1$–$3\,\mathrm{s}$. In this time substances must diffuse from the blood to the surrounding tissue cells. The distance between capillaries is usually no more than a few tens of micrometers; a protein molecule in water has a diffusion coefficient of about $D = 6\times10^{-6}\,\mathrm{cm^2\,s^{-1}}$, and the time to diffuse $50\,\mu\mathrm{m}$ is about $x^2/2D = (5\times10^{-3})^2/(1.2\times10^{-5})\,\mathrm{s} \approx 2\,\mathrm{s}$, comparable to the residence time; small molecules such as $\ce{O2}$ and glucose have diffusion coefficients an order of magnitude larger and take less time. Slow flow, thin walls and low pressure are exactly the conditions needed for exchange (Chapter 15).

### 14.2.2. Laminar and Turbulent Flow

**Definition 14.2.2 (Laminar and Turbulent Flow)** Flow in which the fluid moves in layers, each layer moving parallel to the tube axis without mixing, is called **laminar flow**; flow in which fluid elements move irregularly and the layers mix continuously is called **turbulent flow**.

Laminar flow in a vessel has a parabolic velocity profile: fastest at the center, with the layer next to the wall stationary because of the no-slip condition ([7.6.22](/7.6.22#sec-22.2.1)). Whether turbulence occurs depends on the ratio of inertial to viscous forces, the **Reynolds number**

$$
\operatorname{Re} = \frac{\rho v d}{\eta}, \tag{14.2}
$$

where $\rho$ is the density of blood (about $1050\,\mathrm{kg\,m^{-3}}$), $v$ is the mean velocity, $d$ is the vessel diameter and $\eta$ is the viscosity of blood (about $3$–$4\,\mathrm{mPa\,s}$). Steady flow in a straight tube becomes turbulent when $\operatorname{Re}$ exceeds about 2000; but at branches, stenoses and bends of vessels, pulsatile flow can show local turbulence at $\operatorname{Re}$ of only 200–400.

Equation (14.2) answers three questions.

1. Flow in capillaries is laminar: with $d = 6\,\mu\mathrm{m}$ and $v = 0.5\,\mathrm{mm\,s^{-1}}$, $\operatorname{Re} \approx 10^{-3}$, and inertia is entirely negligible. In the aorta $d \approx 2.5\,\mathrm{cm}$ and the peak systolic velocity can reach $1\,\mathrm{m\,s^{-1}}$, so $\operatorname{Re}$ reaches several thousand, and disturbed flow appears briefly in the ascending aorta in systole.
2. Turbulence appears readily when $v$ increases, $\eta$ decreases or the lumen narrows locally: anemia ($\eta$ reduced, cardiac output increased), the high cardiac output of fever and exercise, valve stenosis or incompetence, and stenosis caused by atherosclerotic plaque.
3. Turbulence has functional and diagnostic significance: the resistance of turbulent flow is greater than that of laminar flow (the pressure drop is approximately proportional to $F^2$ rather than $F$), so the heart does more work; turbulence produces vibration that can be heard with a stethoscope, which is the cardiac murmur and vascular bruit. In measuring blood pressure, the cuff compresses the brachial artery so that blood jets at high velocity through the partly open artery, forming turbulence and producing the Korotkoff sounds (Section 14.5.3). On the other hand, laminar flow subjects the vessel wall to a steady, unidirectional shear stress, on the basis of which endothelial cells maintain a quiescent anti-inflammatory and anticoagulant phenotype (Chapter 15); disturbed flow and oscillatory shear stress at branch points are one reason why atherosclerosis occurs preferentially at these sites.

## 14.3. Pressure and Resistance

### 14.3.1. Three Kinds of Pressure in the Circulation

Blood pressure is the force exerted by blood on a unit area of vessel wall. Physiology and clinical practice customarily use millimeters of mercury ($1\,\mathrm{mmHg} = 133.3\,\mathrm{Pa} = 0.1333\,\mathrm{kPa}$) with atmospheric pressure as zero; we follow this convention and give kPa where needed. Blood pressure has two sources: the pressure produced by the heartbeat, and gravity (which depends on body position). By direction of action and meaning, three kinds of pressure must be distinguished:

**Definition 14.3.1 (Driving, Hydrostatic and Transmural Pressure)** The pressure difference between two points along the long axis of a vessel is called the driving pressure and drives blood flow; the pressure $\rho g h$ produced by the weight of a column of fluid is called the hydrostatic pressure and changes with body position; the pressure difference between the inside and outside of a vessel is called the **transmural pressure**, which determines the degree of distension of the vessel and fluid exchange across the vessel wall.

Gravity changes only the hydrostatic pressure and not the driving pressure: on standing, both the arterial and the venous pressure in the foot increase by about $90\,\mathrm{mmHg}$, and the difference between them (the local driving pressure) is unchanged, so gravity by itself neither makes it "hard for blood to reach the feet" nor "hard for it to return to the heart." The problem caused by gravity lies in the transmural pressure: in the foot the intravascular pressure rises while the external pressure is unchanged, the transmural pressure increases, the compliant veins are distended and hold more blood (Section 14.6), and capillary filtration increases (Chapter 15).

The relation between transmural pressure and intravascular volume depends on the compliance of the wall. In an ideal rigid tube a change of pressure does not change the volume, and flow is proportional to the pressure difference; an ideal infinitely soft tube cannot support any transmural pressure; real vessels lie between the two, and their volume, caliber and hence resistance all vary with transmural pressure (Section 14.4).

### 14.3.2. Blood Pressure at Each Site of the Circulation

The blood pressures at various sites of the circulation in a person lying supine are roughly as follows (mmHg; kPa in parentheses):

| Site | Pressure | Notes |
|---|---|---|
| Left ventricle | About 120 in systole, near 0 in diastole | |
| Aorta and large arteries | Systolic 120 (16), diastolic 80 (10.7), mean about 93 | Pulsatile |
| Arterioles | Fall from about 85 to about 35 | Where the fall is steepest |
| Capillaries | About 35 at the arterial end, about 10 at the venous end, functional mean about 17 (2.3) | Flows, but without too much leakage |
| Veins | Below 10, gradually decreasing | |
| Right atrium | About 0 | Central venous pressure (Section 14.6.1) |
| Right ventricle | About 25 in systole, 0–1 in diastole | |
| Pulmonary artery | Systolic 25, diastolic 8, mean about 16 | Low pressure |
| Pulmonary capillaries | Mean about 7 | Lower than plasma colloid osmotic pressure, so the alveoli stay dry ([7.14.18](/7.14.18)) |
| Pulmonary veins and left atrium | About 2–5 | |

The systemic circulation is a high-pressure, high-resistance system and the pulmonary circulation a low-pressure, low-resistance one: with the same flow, the driving pressure of the pulmonary circulation is only about one seventh that of the systemic circulation. The capillary pressure of about $17\,\mathrm{mmHg}$ is a compromise: enough to drive blood through at low velocity, without letting too much plasma escape (Starling forces, Chapter 15).

### 14.3.3. Ohm's Law of Blood Flow

The relation among blood flow, driving pressure and resistance is formally the same as **Ohm's law** of electric circuits:

**Definition 14.3.2 (Vascular Resistance and Conductance)** The ratio of the pressure difference $\Delta P$ across a segment of vessel to the blood flow $F$ through it,

$$
R = \frac{\Delta P}{F}, \qquad F = \frac{\Delta P}{R}, \tag{14.3}
$$
is called the **vascular resistance** of that segment; its reciprocal $G = 1/R$ is called the conductance of the vessel. The resistance of the whole systemic circulation (the difference between mean aortic pressure and right atrial pressure divided by the cardiac output) is called the **total peripheral resistance**.

The unit of resistance commonly used in physiology is the peripheral resistance unit (PRU): $1\,\mathrm{PRU} = 1\,\mathrm{mmHg\,s\,mL^{-1}}$, the resistance when a pressure difference of $1\,\mathrm{mmHg}$ drives a flow of $1\,\mathrm{mL\,s^{-1}}$.

**Example 14.3.1 (Resistance of the Systemic and Pulmonary Circulations)** The systemic flow is about $100\,\mathrm{mL\,s^{-1}}$ and the difference between mean aortic pressure and right atrial pressure is about $100\,\mathrm{mmHg}$, so the total peripheral resistance is about $1\,\mathrm{PRU}$. With intense vasoconstriction throughout the body it can rise to about $4\,\mathrm{PRU}$, and with extreme vasodilation fall to about $0.2\,\mathrm{PRU}$. The pulmonary circulation has the same flow, the difference between mean pulmonary arterial pressure and left atrial pressure is about $14\,\mathrm{mmHg}$, and the pulmonary vascular resistance is about $0.14\,\mathrm{PRU}$. In SI, $1\,\mathrm{PRU} = 133.3\,\mathrm{Pa}/(10^{-6}\,\mathrm{m^3\,s^{-1}}) \approx 1.3\times10^{8}\,\mathrm{Pa\,s\,m^{-3}}$.

Equation (14.3) is the basis of quantitative reasoning in circulatory physiology: cardiac output = arterial pressure / total peripheral resistance, and the blood flow of each organ = arterial pressure / resistance of that organ. The discussion of "controlling pressure or controlling flow" in Chapter 16 rests on it.

### 14.3.4. The Poiseuille Law

What determines resistance? For steady laminar flow of a **Newtonian fluid** in a rigid circular tube of length $l$ and radius $r$, the **Hagen–Poiseuille law** gives (derivation in [7.6.22](/7.6.22#sec-22.2.1), where it is written with diameter $d = 2r$)

$$
F = \frac{\pi r^4}{8\eta l}\,\Delta P, \qquad R = \frac{8\eta l}{\pi r^4}. \tag{14.4}
$$

Resistance is proportional to viscosity and length and inversely proportional to the fourth power of the radius. The fourth power makes the radius the most effective variable for regulating blood flow: a 19% increase of radius doubles the conductance ($1.19^4 \approx 2.0$); doubling the radius increases the conductance 16-fold. Therefore:

- About two thirds of systemic resistance lies in the small arteries and arterioles. A single capillary is narrower still, but capillaries are extremely numerous and arranged in parallel with one another (Section 14.3.6), and are also very short, so their total resistance is actually smaller than that of the arterioles.
- By changing their caliber by a few tens of percent, the smooth muscle of the small arteries can change organ blood flow several- to tens-fold. Neural signals (sympathetic vasoconstrictor fibers) and chemical signals (local metabolites, hormones) both act through them (Chapters 15 and 16), so the small arteries are the "valves" for distributing blood flow.

Conductance and resistance reflect the properties of the blood (viscosity) and the dimensions of the vessels, and have no direct relation to the properties of the wall material. But Eq. (14.4) has three premises: a rigid tube, a Newtonian fluid and steady laminar flow. Real vessels are distensible (caliber changes with transmural pressure, Section 14.4.3), blood is not a Newtonian fluid in narrow tubes (Section 14.3.5), and flow in arteries is pulsatile (Section 14.5). In physiology the Poiseuille law is therefore used mainly to show qualitatively the dominance of radius and to compare different states, not to calculate resistance precisely from anatomical dimensions.

### 14.3.5. Viscosity, Hematocrit and the Fåhræus–Lindqvist Effect

**Viscosity** characterizes the internal friction between adjacent layers of flow: the force $F$ required for a layer of fluid of area $A$ to move at velocity difference $\Delta v$ relative to another layer a distance $\Delta x$ away satisfies

$$
\tau = \frac{F}{A} = \eta\,\frac{\Delta v}{\Delta x}, \tag{14.5}
$$

that is, viscosity is the shear stress needed to reach unit velocity gradient (shear rate) in a laminar liquid. The viscosity of plasma is about 1.6–2.4 times that of water and that of whole blood 3–4 times (the viscosity of water at body temperature is about $0.7\,\mathrm{mPa\,s}$), and depends mainly on the **hematocrit** (about 42% in men and 38% in women). A raised hematocrit (polycythemia, dehydration) increases viscosity and resistance, slows blood flow and raises the risk of thrombosis; a lowered one (anemia) reduces oxygen-carrying capacity. The trade-off between oxygen carriage and viscosity and its optimum are in [7.14.11](/7.14.11#sec-11.2.5).

Whole blood is not a Newtonian fluid: at low shear rates the erythrocytes aggregate into stacks (rouleaux) and the apparent viscosity rises markedly, so slow-flowing blood in the veins is "thicker" than blood in the arteries. In narrow tubes there are two further effects that depend on tube diameter.

**Definition 14.3.3 (Fåhræus Effect and Fåhræus–Lindqvist Effect)** In tubes with a diameter smaller than about $0.3\,\mathrm{mm}$, erythrocytes concentrate toward the tube axis, leaving a cell-free plasma layer a few micrometers thick at the wall. As a result the hematocrit of the blood in the tube is lower than that of the blood flowing in (Fåhræus effect), and the apparent viscosity falls as the tube diameter decreases, reaching a minimum at a diameter of about $7\,\mu\mathrm{m}$ (the **Fåhræus–Lindqvist effect**).

The cause is that the erythrocytes experience a lift force directed toward the tube axis in flow (migration of deformable particles in shear flow), while the low-viscosity plasma layer at the wall acts as a lubricant; the erythrocytes at the axis move faster than the mean velocity, so they spend less time in the tube and occupy a smaller volume fraction. In capillaries narrower than an erythrocyte, the cells must deform into bullet shapes and squeeze through in single file, and the apparent viscosity rises sharply again. In vivo, the glycocalyx about $0.5\,\mu\mathrm{m}$ thick on the endothelial surface further increases the effective resistance to flow, making the resistance of microvessels in the body higher than the values measured in glass tubes.

### 14.3.6. Series and Parallel

The resistance of a network of vessels combines according to the rules of electric circuits:

$$
R_{\text{series}} = R_1 + R_2 + \cdots + R_n, \qquad \frac{1}{R_{\text{parallel}}} = \frac{1}{R_1} + \frac{1}{R_2} + \cdots + \frac{1}{R_n}. \tag{14.6}
$$

The systemic circulation as a whole is in series: arteries, arterioles, capillaries, venules and veins join one after another, the total resistance is the sum of the segments, and the pressure falls most across the segment of greatest resistance (in panel C the steepest fall of pressure is in the arterioles). Locally it is in parallel: the circulations of the brain, coronary arteries, kidney, liver and gut, skeletal muscle, skin and other organs branch from the aorta, are independent of one another, and each regulates its own resistance according to local conditions. Two consequences of parallel arrangement:

1. The total resistance of a parallel arrangement is smaller than that of any one branch. A single capillary among $10^{10}$ has an extremely high resistance, yet the total resistance after parallel combination is not large.
2. A change of resistance in any one organ changes the total resistance and so affects the whole body. Amputating a limb or resecting an organ removes one parallel branch and increases the total peripheral resistance; if arterial pressure is unchanged, total blood flow (cardiac output) falls. Conversely, in strenuous exercise the resistance of skeletal muscle falls greatly and the total peripheral resistance falls with it; if cardiac output cannot increase correspondingly, arterial pressure falls and the perfusion of other organs falls with it (Chapter 16).

**Example 14.3.2 (Adding or Removing Parallel Branches)** Let the difference between arterial pressure and right atrial pressure be held at $100\,\mathrm{mmHg}$, and let the systemic circulation consist of two groups of organs in parallel with resistances $R_1 = 2\,\mathrm{PRU}$ and $R_2 = 2\,\mathrm{PRU}$, so that the total resistance is $1\,\mathrm{PRU}$ and the total flow $100\,\mathrm{mL\,s^{-1}}$. After resecting half of the second group (its resistance becomes $4\,\mathrm{PRU}$), the total resistance is $1/(1/2 + 1/4) = 1.33\,\mathrm{PRU}$, the total flow falls to $75\,\mathrm{mL\,s^{-1}}$, and the flow of the first group is still $50\,\mathrm{mL\,s^{-1}}$. If instead cardiac output is held constant and arterial pressure varies, the conclusion is the opposite: the same resection raises arterial pressure to $133\,\mathrm{mmHg}$ and the flow of the first group increases to $67\,\mathrm{mL\,s^{-1}}$. Which of these quantities the body actually regulates is the question to be answered at the start of Chapter 16.

## 14.4. Mechanics of the Vessel Wall

### 14.4.1. Laplace's Law

The pressure in a vessel pushes the wall outward, and the wall must resist with tension. For a thin-walled cylindrical tube of radius $r$, the circumferential tension $T$ per unit length of wall along the tube axis and the transmural pressure $P$ satisfy (taking half of the wall in force balance: the pressure force $P \cdot 2r$ is balanced by the tension $2T$ at the two cut edges)

**Definition 14.4.1 (Laplace's Law)** The relation of wall tension in a thin-walled elastic tube or sac to the transmural pressure and radius,

$$
T = P\,r \quad (\text{cylinder}), \qquad T = \frac{P\,r}{2} \quad (\text{sphere}), \tag{14.7}
$$
is called **Laplace's law**. When the wall thickness is $h$, the circumferential stress in the wall is $\sigma = T/h = Pr/h$.

It is the same force balance as the Laplace formula for surface tension (excess pressure $2\gamma/R$, [5.1.2](/5.1.2)), written for a different material.

**Example 14.4.1 (Wall Tension in the Aorta and a Capillary)** In the aorta $P \approx 100\,\mathrm{mmHg} = 13.3\,\mathrm{kPa}$ and $r \approx 1.2\,\mathrm{cm}$, so $T \approx 1.3\times10^4 \times 0.012\,\mathrm{N\,m^{-1}} \approx 160\,\mathrm{N\,m^{-1}}$. In a capillary $P \approx 25\,\mathrm{mmHg} = 3.3\,\mathrm{kPa}$ and $r \approx 4\,\mu\mathrm{m}$, so $T \approx 0.013\,\mathrm{N\,m^{-1}}$, about $10^4$ times smaller than in the aorta. A capillary with only one endothelial layer (about $0.5\,\mu\mathrm{m}$ thick) can therefore withstand a pressure similar to that of the small arteries without bursting, whereas the aorta needs thick elastic fibers and collagen; the wall stress $\sigma = Pr/h$ is fairly similar in arteries of different size, and wall thickness is roughly proportional to radius.

Laplace's law also explains the danger of an aneurysm. When a local part of the wall weakens and bulges, $r$ increases, the tension needed at the same blood pressure increases, the wall is stretched further, and $r$ continues to increase: this is a positive feedback that can end in rupture. The same relation appears in a dilated ventricle: when the ventricular radius increases, a greater wall tension is needed to produce the same intracavitary pressure ([7.14.12](/7.14.12)), and in the alveolus it appears as the relation between surface tension and alveolar size ([7.14.18](/7.14.18)).

### 14.4.2. Compliance and Distensibility

**Definition 14.4.2 (Compliance and Distensibility)** The ability of vessel volume to change with transmural pressure. The change of volume per unit change of pressure,

$$
C = \frac{\Delta V}{\Delta P} \tag{14.8}
$$
is called the **compliance** (also called capacitance); the fractional change of volume relative to the original volume,

$$
D = \frac{\Delta V}{V_0\,\Delta P} = \frac{C}{V_0} \tag{14.9}
$$
is called the **distensibility**.

The two differ: distensibility is a property of the wall material and structure, whereas compliance also includes the volume of the vessel. The distensibility of the systemic veins is about 8 times that of the corresponding arteries and their volume about 3 times, so the compliance is about $8\times3 = 24$ times. This means that for the same increase of $1\,\mathrm{mmHg}$ in pressure, the veins hold 24 times as much additional blood as the arteries. The pulmonary vessels also have high compliance, and the distensibility of the pulmonary arteries is about 6 times that of the systemic arteries.

The pressure–volume curves of vessels reveal the division of labor between arteries and veins. When the volume of the systemic arteries is about $700\,\mathrm{mL}$ the mean pressure is about $100\,\mathrm{mmHg}$, and when the volume falls to about $400\,\mathrm{mL}$ the pressure falls to zero: in the arteries a small change in blood volume gives a large change in pressure, so the arteries are a store of pressure. When the volume of the veins increases from about $2000$ to $3500\,\mathrm{mL}$ the pressure rises by only a few mmHg, so the veins are a store of volume. This answers a practical question: transfusions and infusions usually use veins not only because venous pressure is low and the procedure is safe but also because veins can accept a large amount of fluid with a very small change in pressure; infusing the same volume into an artery would cause much larger pressure swings.

Sympathetic excitation contracts vascular smooth muscle and the volume at a given pressure decreases (the curve moves down); inhibition does the opposite. Venous contraction is especially important: it squeezes stored blood toward the heart and in hemorrhage can compensate for a considerable part of the blood loss with very little fall in blood pressure (Chapter 16).

### 14.4.3. Nonlinearity of the Pressure–Flow Relation

In a rigid tube, flow is proportional to the driving pressure (Eq. (14.3)). In a distensible vessel, when the driving pressure rises the intraluminal pressure rises, the transmural pressure increases, the caliber increases, the resistance falls as $r^4$, and flow therefore increases faster than pressure, so the pressure–flow curve bends upward. At very low pressure the tension of vascular smooth muscle can close small vessels completely and the flow is zero; this pressure is called the critical closing pressure (usually about $20\,\mathrm{mmHg}$). Sympathetic excitation shifts the curve to the right and flattens it: flow is lower at the same pressure; sympathetic inhibition shifts the curve left and makes it steeper. On the other hand, many organs (brain, kidney, heart, skeletal muscle) maintain constant flow over a certain range of pressure, that is, autoregulation of blood flow; this is an active process in which the response of smooth muscle is superimposed on the passive elastic curve (Chapter 15).

### 14.4.4. Delayed Compliance

**Definition 14.4.3 (Delayed Compliance)** When the volume of a vessel is suddenly increased, the pressure first rises sharply and then falls gradually over minutes to hours, as if the vessel "gave up" space; this is called **delayed compliance** (also stress relaxation); when the volume is suddenly decreased, the pressure first falls and then gradually rises, called reverse stress relaxation.

Its basis is stress relaxation of vascular smooth muscle: after the smooth muscle is stretched, the contractile apparatus rearranges at the new length and the tension gradually returns to near its original level ([7.14.10](/7.14.10#sec-10.5.3)). Mechanically, it can be described by a **viscoelastic** model: the stress of a **Maxwell viscoelastic liquid**, a spring and dashpot in series, decays at fixed strain as $\sigma(t) = \sigma_0\,\mathrm{e}^{-t/\tau}$, where $\tau = \eta/E$ is the relaxation time ([7.6.22](/7.6.22#sec-22.7.1)); the stress of a real vessel does not decay to zero, and it is closer to a standard linear solid, a spring in parallel with a Maxwell element. The physiological significance of delayed compliance is that after infusion of a large volume of fluid the venous pressure gradually recovers and the circulatory system can accommodate the extra blood within minutes; after blood loss, vascular tension gradually adjusts so that the remaining blood fills the vascular system again, which is one of the mechanisms for the partial recovery of blood pressure within tens of minutes after hemorrhage (Chapter 16).

## 14.5. Arterial Blood Pressure

### 14.5.1. Systolic, Diastolic, Pulse and Mean Arterial Pressure

**Definition 14.5.1 (Systolic, Diastolic, Pulse and Mean Arterial Pressure)** The highest value of arterial blood pressure in a cardiac cycle is called the **systolic pressure**, the lowest the **diastolic pressure**, and the difference between them the **pulse pressure**; the time average of arterial blood pressure over a cardiac cycle is called the **mean arterial pressure**.

In healthy young people the systolic pressure is about $120\,\mathrm{mmHg}$ ($16\,\mathrm{kPa}$), the diastolic pressure about $80\,\mathrm{mmHg}$ ($10.7\,\mathrm{kPa}$) and the pulse pressure about $40\,\mathrm{mmHg}$. Because diastole is longer than systole, the mean arterial pressure is closer to the diastolic pressure, and the usual estimate is

$$
\bar P_{\mathrm{a}} \approx P_{\mathrm{d}} + \frac{P_{\mathrm{s}} - P_{\mathrm{d}}}{3}, \tag{14.10}
$$

that is, about $93\,\mathrm{mmHg}$. The factor 1/3 increases to nearly 1/2 when heart rate rises and diastole shortens.

The formation of arterial blood pressure requires three conditions: sufficient filling of the vascular system with blood (the mean circulatory filling pressure is about $7\,\mathrm{mmHg}$, the pressure in the vessels of the whole body after the heart has stopped, Chapter 16); ejection by the heart; and peripheral resistance, which prevents the blood ejected into the arteries from running off at once. The elastic reservoir action of the aorta turns the intermittent ejection into continuous flow and buffers the fluctuation of pressure. The effects of the various factors on blood pressure can be summarized as follows:

| Change | Systolic pressure | Diastolic pressure | Pulse pressure | Reason |
|---|---|---|---|---|
| Increased stroke volume | Markedly raised | Raised little | Increased | More blood is ejected into the arteries in systole; it also runs off faster in diastole |
| Faster heart rate | Raised little | Markedly raised | Decreased | Diastole is shortened, and more blood remains in the arteries at end-diastole |
| Increased peripheral resistance | Raised little | Markedly raised | Decreased | Outflow of blood slowed in diastole |
| Decreased aortic compliance (old age) | Raised | Lowered | Increased | Elastic reservoir action weakened |
| Circulating volume reduced relative to vascular capacity | Falls | Falls | | Blood loss below about 20% can be compensated by reflex vasoconstriction |

### 14.5.2. The Windkessel Model

The rules in the table above can be derived quantitatively from a model with only two parameters. Otto Frank (1899) compared the aorta and large arteries to the air chamber of a fire engine (German *Windkessel*), which turns intermittent pumping of water into continuous spraying.

**Definition 14.5.2 (Windkessel Model)** Regard the arterial system as an elastic chamber of compliance $C$ that drains through the total peripheral resistance $R$ to veins at approximately zero pressure. With ventricular inflow $Q_{\mathrm{in}}(t)$, the arterial pressure $P(t)$ satisfies

$$
C\,\frac{\mathrm{d}P}{\mathrm{d}t} = Q_{\mathrm{in}}(t) - \frac{P}{R}, \tag{14.11}
$$
called the (two-element) **Windkessel model**.

It is exactly the same as the RC circuit in which a capacitor discharges through a resistor ([5.3](/5.3)). Three conclusions can be read from Eq. (14.11):

1. The mean arterial pressure is determined only by the mean flow and the resistance: integrating over one cycle, in the steady state $P$ is the same at the beginning and end, the left side is zero, and $\bar P = \bar Q R$, independent of $C$. This is Eq. (14.3).
2. In diastole $Q_{\mathrm{in}} = 0$ and the arterial pressure decays exponentially as $P(t) = P_{\mathrm{es}}\,\mathrm{e}^{-t/\tau}$ with time constant $\tau = RC$. Taking $R = 1\,\mathrm{PRU}$ and $C = 1.5\,\mathrm{mL\,mmHg^{-1}}$, $\tau = 1.5\,\mathrm{s}$, which is longer than diastole (about $0.5\,\mathrm{s}$), so the arterial pressure falls only partway during diastole and blood continues to flow to the periphery throughout diastole.
3. When ejection is much faster than $\tau$, almost all of the ejected stroke volume is first stored in the elastic chamber, and the pulse pressure is about $\mathrm{SV}/C$: halving the compliance doubles the pulse pressure.

![Two-element Windkessel model (Eq. (14.11)). Each stroke is ejected as a half sine lasting 0.3 s, heart rate 75 beats/min, stroke volume 70 mL, total peripheral resistance R = 1 mmHg·s/mL. A: aortic pressure in the steady state with compliance C of 1.5 (young, compliant aorta), 0.75 and 0.4 mL/mmHg (stiff aorta); the gray trace is the ejection inflow. The mean pressure is the same in all three (dotted line, Q̄R); the smaller the compliance, the higher the systolic and the lower the diastolic pressure. B: systolic pressure, diastolic pressure and pulse pressure as functions of C; the dashed line is the estimate SV/C for very fast ejection](./plots/windkessel.py)

The model explains the isolated systolic hypertension common in the elderly: the elastic fibers in the aorta fragment with age and are replaced by collagen, compliance falls, and the mean pressure need not rise but the pulse pressure increases, with a raised systolic and lowered diastolic pressure. The raised systolic pressure increases the afterload of the heart, and the lowered diastolic pressure reduces coronary perfusion, which takes place mainly in diastole (Chapter 16). The two-element model ignores the inertia of blood and the propagation and reflection of pressure waves in the arteries; adding the characteristic impedance of the aorta (the three-element model) or treating the arterial tree as a transmission line fits the systolic waveform better, but the rules above for mean pressure and pulse pressure are unchanged.

### 14.5.3. Propagation and Attenuation of the Pressure Pulse

Ejection suddenly distends the wall at the root of the aorta, and this distension propagates as a wave along the arteries to the periphery; what can be felt at the body surface is the arterial pulse. The speed of propagation of the pressure wave is far greater than the speed of blood flow, and what is transmitted is pressure rather than a large volume of blood. For a fluid in an elastic thin-walled tube, the wave speed is determined by the stiffness of the wall:

**Formula 14.5.1 (Moens–Korteweg Equation)** Let the **Young's modulus** of the wall be $E$, its thickness $h$, the internal diameter of the tube $d$ and the density of blood $\rho$; then the propagation speed of the pressure wave is

$$
c = \sqrt{\frac{E\,h}{\rho\,d}}. \tag{14.12}
$$

The equivalent Bramwell–Hill form is written using distensibility: $c = 1/\sqrt{\rho D_A}$, where $D_A = \mathrm{d}A/(A\,\mathrm{d}P)$ is the distensibility of the cross-sectional area. The stiffer and thicker the wall, or the narrower the tube, the faster the wave travels. Taking the aorta with $E \approx 0.4\,\mathrm{MPa}$ and $h/d \approx 0.08$ gives $c \approx \sqrt{0.4\times10^6\times0.08/1050}\,\mathrm{m\,s^{-1}} \approx 5.5\,\mathrm{m\,s^{-1}}$. The measured pulse wave velocity is about $3$–$5\,\mathrm{m\,s^{-1}}$ in the aorta, about $7$–$10\,\mathrm{m\,s^{-1}}$ in the branches of large arteries and about $15$–$35\,\mathrm{m\,s^{-1}}$ in small arteries. Because $E$ in Eq. (14.12) increases with age and arteriosclerosis, measuring the pulse wave velocity between the carotid and femoral arteries has become a standard clinical index of arteriosclerosis: about $6\,\mathrm{m\,s^{-1}}$ in young people and often more than $10\,\mathrm{m\,s^{-1}}$ in the elderly.

The pressure pulse undergoes two kinds of change as it travels to the periphery. On the one hand, impedance mismatch at arterial branches and resistance vessels reflects part of the pressure wave back, where it adds to the forward wave; in large and medium arteries this makes the systolic pressure in peripheral arteries (such as the dorsalis pedis) actually higher than in the aorta and the waveform sharper (pulse amplification). When the arteries are stiff the wave speed is fast, the reflected wave returns to the aorta within systole and is superimposed on the systolic peak, raising systolic pressure further. On the other hand, in the small arteries and arterioles resistance and compliance together attenuate the pulsation: each segment of vessel acts like an RC low-pass filter, and by the capillaries the pulsation has essentially disappeared and blood flows smoothly and continuously in them (panel C of the figure).

The auscultatory method of indirect blood pressure measurement makes use of all this: when the cuff pressure is above the systolic pressure the brachial artery is completely closed and there is no sound; when the cuff pressure falls below the systolic pressure, blood jets from the flattened artery in each systole, forming turbulence and giving the first Korotkoff sound; when the cuff pressure falls to near the diastolic pressure, the artery is open throughout the cycle, the turbulence disappears, and the sound changes in tone and then vanishes.

## 14.6. Venous Pressure and Venous Return

### 14.6.1. Central and Peripheral Venous Pressure

**Definition 14.6.1 (Central Venous Pressure)** The blood pressure in the right atrium and the large intrathoracic veins is called the **central venous pressure**, normally about $0\,\mathrm{mmHg}$ (fluctuating between $-3$ and $+5\,\mathrm{mmHg}$); the blood pressure in the veins of the organs is called the peripheral venous pressure.

The central venous pressure is a balance between two actions: the ability of the right heart to pump blood out of the right atrium, and the tendency of the peripheral veins to return blood to the right atrium. When right heart contraction is weakened (right heart failure), blood accumulates in the right atrium and the central venous pressure rises; it also rises when transfusion, infusion or venoconstriction increases return, and falls in hemorrhage. Measuring central venous pressure therefore allows assessment of the pumping capacity of the heart and the circulating volume and guides fluid therapy. It is also the "downstream pressure" of venous return and plays a central role in the Guyton analysis of Chapter 16.

Peripheral venous pressure is $4$–$6\,\mathrm{mmHg}$ higher than central venous pressure because the large veins are compressed by surrounding tissues on their way into the thorax: the veins of the arm are compressed as they cross the first rib, the neck veins partly collapse under atmospheric pressure, the veins at the axilla are angulated, and the veins in the abdomen are compressed by intra-abdominal pressure (normally about $6\,\mathrm{mmHg}$, reaching $15$–$30\,\mathrm{mmHg}$ in pregnancy or ascites). These "collapse points" of the veins act like a pressure-limiting valve: peripheral venous pressure does not generally fall further when central venous pressure falls below zero, and the large veins only become flatter.

### 14.6.2. The Influence of Gravity

On standing, the column of fluid in the vessels produces a hydrostatic pressure $\Delta P = \rho g h$. For blood $\rho g \approx 1050 \times 9.8\,\mathrm{Pa\,m^{-1}} = 10.3\,\mathrm{kPa\,m^{-1}}$, or about $0.77\,\mathrm{mmHg}$ per centimeter. Taking the tricuspid valve as the reference point (where pressure is least affected by posture):

- The foot is about $1.2\,\mathrm{m}$ below the heart; in quiet standing its venous pressure is about $+90\,\mathrm{mmHg}$ and its arterial pressure about $100 + 90 = 190\,\mathrm{mmHg}$. The difference between the two, the driving pressure for flow to the foot, is the same as when supine.
- The neck veins above the heart collapse under the external atmospheric pressure, and the pressure in them stays near zero. The dural venous sinuses in the skull have rigid walls and cannot collapse, and the pressure in them becomes negative with height: about $-10\,\mathrm{mmHg}$ in the superior sagittal sinus. This is why air can be sucked in and cause air embolism when the sagittal sinus is opened in neurosurgery.
- The arterial pressure in the head is about $40\,\mathrm{mmHg}$ lower than at heart level, that is, about $60\,\mathrm{mmHg}$; a "blood pressure of 100 mmHg" therefore refers to the pressure at heart level.

![Blood pressure along body height (ρg taken as 0.77 mmHg per centimeter of blood, with heart level as zero). A: arterial pressure in a standing adult varies linearly with height, about 190 mmHg at the foot; supine it is about 100 mmHg everywhere (red dotted line). In quiet standing there is a continuous column of fluid in the veins below the heart, about 90 mmHg at the foot; above the heart the jugular veins collapse and the pressure is near zero, while the rigid-walled sagittal sinus is at negative pressure (about −10 mmHg). In walking, the muscle pump and venous valves break the column and the venous pressure at the foot stays below 20 mmHg (dashed line, schematic). B: the giraffe (head about 1.5 m above the heart) has a mean arterial pressure at heart level of about 200 mmHg, falling to about 85 mmHg at the head, comparable to the perfusion pressure of the human brain; at the foot it is as high as about 340 mmHg (values approximate)](./plots/posture-pressure.py)

### 14.6.3. Venous Valves and the Muscle Pump

Without venous valves, the venous pressure at the foot of a standing adult would remain $+90\,\mathrm{mmHg}$. The veins of the limbs contain many valves opening toward the heart; each contraction of the leg muscles compresses the veins within and between them and pushes blood toward the heart; when the muscle relaxes, the lower valves open to let the blood refill, and the upper valves close to prevent backflow.

**Definition 14.6.2 (Muscle Pump)** The alternate compression of veins by contraction and relaxation of skeletal muscle which, together with venous valves, drives venous blood toward the heart and lowers peripheral venous pressure is called the **muscle pump** (also the venous pump).

The efficiency of the muscle pump is sufficient to keep the venous pressure at the foot of a walking adult below $+20\,\mathrm{mmHg}$. In prolonged quiet standing the muscle pump does not work, venous pressure at the foot rises to about $90\,\mathrm{mmHg}$, capillary pressure rises with it, fluid leaks out, and edema of the feet results (Chapter 15); the veins dilate and within 15–30 seconds can hold more than $500\,\mathrm{mL}$ of blood, venous return falls, cardiac output and arterial pressure fall, and in severe cases cerebral perfusion is inadequate and fainting results (as with soldiers standing at attention for a long time). Occasional contraction of the leg muscles or slight bending of the knees avoids this. Prolonged venous hypertension (as in occupations requiring long standing, or pregnancy) overdistends the veins, the valve leaflets can no longer close, the muscle pump fails, and the veins dilate further, forming varicose veins: again a positive feedback.

Respiratory movement constitutes another pump: on inspiration the intrapleural pressure becomes more negative and the large intrathoracic veins dilate, while the descent of the diaphragm raises intra-abdominal pressure and compresses the abdominal veins, both promoting return of blood to the right atrium ([7.14.17](/7.14.17)).

### 14.6.4. Blood Storage by the Veins

The venous system holds more than about 60% of the blood of the whole body, and some sites are especially large or especially compliant and are called blood reservoirs:

| Reservoir | Volume that can be mobilized | Mechanism |
|---|---|---|
| Spleen | About $100\,\mathrm{mL}$ | The venous sinuses of the spleen store whole blood; the splenic pulp also stores concentrated erythrocytes, which are released when smooth muscle of the capsule contracts on sympathetic excitation |
| Liver | Several hundred milliliters (about $500\,\mathrm{mL}$) | Hepatic sinusoids |
| Large abdominal veins | About $300\,\mathrm{mL}$ | |
| Subcutaneous venous plexus | Several hundred milliliters | High distensibility |
| Heart | $50$–$100\,\mathrm{mL}$ | Reduced in size on sympathetic excitation |
| Lungs | $100$–$200\,\mathrm{mL}$ | When pulmonary vascular pressure is lowered |

In hemorrhage, exercise or standing, the sympathetic nerves constrict these veins and send the stored blood back into effective circulation; this action is as important as arterial constriction (Chapter 16).

## 14.7. Evolution and Comparative Biology

### 14.7.1. The Giraffe: Hypertension under Gravity

The head of a standing giraffe is about $1.5$–$2\,\mathrm{m}$ above the heart and its feet are about $2\,\mathrm{m}$ below the heart. To deliver blood to the head and maintain cerebral perfusion, the mean arterial pressure at heart level is about $200\,\mathrm{mmHg}$ (about $27\,\mathrm{kPa}$), twice that of humans and the highest among mammals; by $\rho g h$ a $1.5\,\mathrm{m}$ column of fluid consumes about $115\,\mathrm{mmHg}$, so that only about $85$–$100\,\mathrm{mmHg}$, comparable to humans, remains on reaching the head. The high blood pressure of the giraffe is caused by gravity and not by a high peripheral resistance: its heart has not become proportionally larger (about 0.5% of body weight, the same as other mammals) but has a thicker left ventricular wall and relatively small cavity, working at high pressure in the manner stated by Laplace's law (small $r$, large $h$).

The price of hypertension is paid in the legs: arterial pressure at the foot can exceed $300\,\mathrm{mmHg}$, and the transmural pressure of the capillaries should drive out large amounts of fluid. The adaptations of the giraffe's legs act like an "anti-gravity suit": the skin and deep fascia of the lower leg are tight and inelastic, and the pressure of the interstitial fluid is high, offsetting the high pressure in the capillaries; the walls of the leg arteries are extremely thick and the lumen narrow, taking up part of the pressure drop proximally; the capillaries of the leg have low permeability and lymphatic return is well developed. When the giraffe lowers its head to drink, the head suddenly drops about $2\,\mathrm{m}$ below the heart; valves in the jugular veins prevent backflow of blood, and resistive regulation of the cerebral arteries together with pressure balance inside and outside the skull prevents excessive engorgement of the brain. These mechanisms are partly still under study, but all are solutions of one physical problem: keeping transmural pressure and driving pressure each in a suitable range in a body where $\rho g h$ is large.

### 14.7.2. Snakes: Heart Position and Way of Life

The snake body is long and slender and has no limbs, so when inclined or vertical the whole body is a long column of fluid, a natural experiment for studying gravity and circulation. Lillywhite and colleagues compared snakes of different ways of life:

- Arboreal snakes often climb vertically, and the heart lies closer to the head (about 15%–25% of body length from it), shortening the column of fluid from heart to brain; they have higher blood pressure, a slender body and tight skin, and arterial pressure stays stable when they are tilted vertically.
- Sea snakes live in water, where the hydrostatic pressure of the surrounding water cancels the hydrostatic pressure in the vessels (water and blood having similar densities), so gravity has almost no effect on them; the heart lies near the middle of the body (about 25%–45% of body length) and blood pressure is low. When a sea snake is held vertically in air, blood pools in the lower body and blood pressure falls quickly.
- Terrestrial snakes lie between the two.

The cost of a heart near the head is a greater distance to the tail, while a heart in the middle makes perfusion of the whole body most uniform. The convergent change of heart position with way of life is a clear example of gravity as a selective pressure shaping the circulatory system.

### 14.7.3. Scaling of Vascular Networks: Murray's Law

How should vessels branch to be "economical"? Murray (1926) proposed an optimization argument: maintaining a segment of vessel has two costs, one the power needed to drive blood against viscous resistance, $F^2 R = 8\eta l F^2/(\pi r^4)$ (Eq. (14.4)), and the other the metabolic cost of maintaining the blood and the wall itself, approximately proportional to the vessel volume $b\,\pi r^2 l$. A small caliber makes the cost of pumping large, and a large caliber makes the cost of maintenance large. Minimizing the total cost over $r$:

$$
\frac{\partial}{\partial r}\left(\frac{8\eta l F^2}{\pi r^4} + b\pi r^2 l\right) = 0 \quad\Longrightarrow\quad F = \sqrt{\frac{\pi^2 b}{16\eta}}\;r^3 \propto r^3. \tag{14.13}
$$

Flow is proportional to the cube of the radius, and flow is conserved at a bifurcation, so $r_0^3 = r_1^3 + r_2^3$; this is **Murray's law**, and for a symmetric bifurcation the radius ratio of daughter to parent branch is $2^{-1/3} \approx 0.79$. By Eq. (14.5), the wall shear stress $\tau = 4\eta F/(\pi r^3)$ is the same everywhere in a network satisfying $F \propto r^3$. This suggests an achievable mechanism: endothelial cells sense shear stress (Chapter 15), and if vessels dilate and remodel when the shear stress is above a set value and constrict and atrophy when it is below, they will naturally grow into a network satisfying Murray's law.

Measured medium and small arteries roughly conform to an exponent of 3 (most measurements lie between 2.5 and 3); the aorta and large arteries deviate more and are closer to the exponent of 2 for conservation of cross-sectional area, because flow there is pulsatile and inertia cannot be ignored, and the objective of optimization must also include impedance matching of pressure waves (Section 14.5.3). A branching law of the same form, $d_0^p = d_1^p + d_2^p$, also appears in the dendrites of neurons, where electrical impedance matching gives **Rall's 3/2 power rule** ($p = 3/2$) ([7.14.5](/7.14.5)). Combining the optimization of branching networks with the conditions that "the size of terminal capillaries is invariant and the network fills the space," West, Brown and Enquist (1997) derived the $3/4$-power **allometry** of metabolic rate with body mass; the assumptions and range of validity of this derivation are still debated, and metabolic scaling is in Chapter 30.

## Summary

- Continuity: $F = vA$; the total cross-sectional area increases from $2.5\,\mathrm{cm^2}$ in the aorta to about $2500\,\mathrm{cm^2}$ in the capillaries, the velocity falls from $33$ to $0.03\,\mathrm{cm\,s^{-1}}$, and blood stays in a capillary for $1$–$3\,\mathrm{s}$. $\operatorname{Re} = \rho vd/\eta$ determines laminar versus turbulent flow; turbulence increases resistance and produces murmurs and Korotkoff sounds.
- Three kinds of pressure: driving pressure drives blood flow; hydrostatic pressure $\rho g h$ ($0.77\,\mathrm{mmHg}$ per centimeter of blood) changes with posture without changing the driving pressure; transmural pressure determines the distension of vessels and fluid exchange (Definition 14.3.1).
- The Ohm's law of blood flow $F = \Delta P/R$ (Definition 14.3.2); systemic resistance about $1\,\mathrm{PRU}$, pulmonary about $0.14\,\mathrm{PRU}$. The Poiseuille law $R = 8\eta l/(\pi r^4)$ makes the small arteries the main resistance (about 2/3) and the valves for distributing blood flow; it assumes a rigid tube, a Newtonian fluid and steady laminar flow. Viscosity rises with hematocrit; the Fåhræus–Lindqvist effect in narrow tubes (Definition 14.3.3) lowers the apparent viscosity. Series overall, parallel locally: a change of resistance in any organ changes the total resistance.
- Wall mechanics: Laplace's law $T = Pr$ (Definition 14.4.1); compliance $C = \Delta V/\Delta P$ and distensibility $C/V_0$ (Definition 14.4.2), the compliance of veins being about $8\times3 = 24$ times that of arteries: arteries store pressure and veins store volume; delayed compliance comes from stress relaxation of smooth muscle (Definition 14.4.3).
- Arterial blood pressure: systolic, diastolic, pulse and mean arterial pressure $\approx P_{\mathrm{d}} + (P_{\mathrm{s}} - P_{\mathrm{d}})/3$ (Definition 14.5.1). Windkessel model $C\dot P = Q_{\mathrm{in}} - P/R$ (Definition 14.5.2): mean pressure $= \bar QR$, decay in diastole with $\tau = RC$, pulse pressure $\approx \mathrm{SV}/C$. Pulse wave velocity $c = \sqrt{Eh/(\rho d)}$ (Formula 14.5.1) is an index of arterial stiffness; pulsation is attenuated in the arterioles.
- Veins: central venous pressure about $0\,\mathrm{mmHg}$ (Definition 14.6.1) reflects the balance between cardiac pumping and venous return; on standing the venous pressure at the foot is about $90$ and the arterial pressure about $190\,\mathrm{mmHg}$, and the sagittal sinus is at negative pressure; the muscle pump and venous valves (Definition 14.6.2) keep the venous pressure at the foot below $20\,\mathrm{mmHg}$ in walking. The spleen, liver, abdominal veins and subcutaneous venous plexus are mobilizable blood reservoirs.
- Evolution: the giraffe opposes the column of fluid in the neck with a blood pressure of about $200\,\mathrm{mmHg}$ and opposes high transmural pressure in the legs with tight skin and fascia; the heart of arboreal snakes is near the head and sea snakes in water are unaffected by gravity; Murray's law $r_0^3 = r_1^3 + r_2^3$ minimizes the total cost of transport and maintenance and makes the shear stress the same everywhere.

## Questions

1. A person's cardiac output is $6\,\mathrm{L\,min^{-1}}$, mean arterial pressure $96\,\mathrm{mmHg}$ and right atrial pressure $0$. Find the total peripheral resistance (PRU). If in exercise cardiac output increases to $18\,\mathrm{L\,min^{-1}}$ while mean arterial pressure rises only to $110\,\mathrm{mmHg}$, what is the total peripheral resistance? What does this show?

   **Answer** At rest: $F = 100\,\mathrm{mL\,s^{-1}}$, $R = 96/100 = 0.96\,\mathrm{PRU}$. In exercise: $F = 300\,\mathrm{mL\,s^{-1}}$, $R = 110/300 \approx 0.37\,\mathrm{PRU}$, a fall to about 38%. Cardiac output increases to 3 times while blood pressure rises only about 15% because total peripheral resistance falls greatly: the small arteries of skeletal muscle dilate strongly under the action of metabolites (Chapter 15), and the fall of resistance of this parallel branch lowers the total resistance; at the same time neural regulation increases cardiac output, and arterial pressure is maintained (Chapter 16).

2. The radius of a small artery is reduced by 20% by smooth muscle contraction. What fraction of its original blood flow remains at unchanged driving pressure? By what factor must the driving pressure increase to maintain the original flow?

   **Answer** From Eq. (14.4), $F \propto r^4$, $0.8^4 = 0.41$, so flow falls to about 41% of the original. To maintain flow the driving pressure must increase to $1/0.41 \approx 2.4$ times.

3. Use Laplace's law to explain: (a) why the ventricle in dilated cardiomyopathy has difficulty producing sufficient intracavitary pressure even if the contractile force of the myocytes themselves is unchanged; (b) why an aneurysm tends to grow larger.

   **Answer** (a) The ventricle is approximately spherical, $T = Pr/2$. After the ventricle dilates, $r$ increases, and to produce the same intracavitary pressure $P$ the wall tension $T$ must increase in proportion; if the wall is thinned ($h$ reduced), the stress per unit cross-sectional area of myocardium, $\sigma = Pr/(2h)$, increases even more, the myocytes can hardly generate it, ejection pressure and stroke volume fall, and oxygen consumption increases. (b) At an aneurysm $r$ is increased, and at the same blood pressure the wall tension $T = Pr$ increases, the weak wall is stretched further and $r$ increases again: a positive feedback until rupture. The emphasis of treatment is therefore to control blood pressure and to operate when the diameter exceeds a certain value.

4. Use the Windkessel model to explain: (a) why diastolic pressure rises and pulse pressure falls when heart rate increases; (b) why aortic stiffening raises systolic pressure and lowers diastolic pressure. Taking $R = 1\,\mathrm{PRU}$ and $C = 1.5\,\mathrm{mL\,mmHg^{-1}}$, estimate the fraction by which arterial pressure falls during a diastole of $0.5\,\mathrm{s}$.

   **Answer** (a) In diastole the arterial pressure decays as $\mathrm{e}^{-t/RC}$. When heart rate rises, diastole is shortened, there is less time for decay, and the end-diastolic pressure is higher; the mean pressure $\bar QR$ rises slightly because flow per minute increases, but the stroke volume is unchanged or reduced, so the pulse pressure does not increase and may decrease. (b) When $C$ decreases, the ejected SV raises the pressure by $\approx \mathrm{SV}/C$, which is more (high systolic pressure); at the same time $\tau = RC$ becomes smaller, the decay in diastole is faster, and the diastolic pressure is low; the mean pressure $\bar QR$ is unchanged. Estimate: $\tau = 1.5\,\mathrm{s}$, $\mathrm{e}^{-0.5/1.5} = 0.72$, so the pressure falls about 28% in diastole, for example from about $105$ at end-systole to about $75\,\mathrm{mmHg}$.

5. A person lying supine has a dorsalis pedis venous pressure of $8\,\mathrm{mmHg}$. He stands quietly, with the foot $125\,\mathrm{cm}$ below the tricuspid valve. Estimate the dorsalis pedis venous pressure and the arterial pressure at the foot (mean arterial pressure at heart level $95\,\mathrm{mmHg}$). Why does the blood flow to the foot not change much as a result? Why does prolonged standing cause edema of the feet?

   **Answer** Hydrostatic pressure $0.77\times125 \approx 96\,\mathrm{mmHg}$. The venous pressure is about $96$–$100\,\mathrm{mmHg}$ (in quiet standing the fluid column is continuous, and the hydrostatic pressure is far greater than the few mmHg of driving pressure difference when supine), and the arterial pressure about $95 + 96 = 191\,\mathrm{mmHg}$. Arterial and venous pressure increase together, the driving pressure is unchanged, so blood flow is determined mainly by local resistance and does not fall greatly because of gravity (in fact the local myogenic response also constricts the small arteries and reduces flow slightly). But the capillary pressure rises by about $90\,\mathrm{mmHg}$ with them, the increased transmural pressure makes filtration exceed the capacity for reabsorption and lymphatic return, and interstitial fluid accumulates as edema; the muscle pump in walking can lower venous and capillary pressure, so walking is better than standing.

6. The distensibility of the systemic veins is 8 times and their volume 3 times that of the arteries. If $100\,\mathrm{mL}$ of fluid is injected into each of the arterial and venous systems, what is the ratio of the pressure rises? Use this to explain why venoconstriction is the first compensation in hemorrhage.

   **Answer** The compliance ratio is $C_{\mathrm{v}}/C_{\mathrm{a}} = 8\times3 = 24$, so the ratio of $\Delta P = \Delta V/C$ for the same $\Delta V$ is $1/24$: the rise of arterial pressure is 24 times that of venous pressure. Conversely, the large amount of blood stored in the veins can be mobilized with a very small change of pressure: sympathetic contraction of venous smooth muscle (compliance reduced, volume at a given pressure smaller) can squeeze several hundred milliliters of blood back to the heart and maintain ventricular filling and cardiac output, whereas the arteries hold little blood to begin with, and arterial constriction mainly increases resistance to maintain blood pressure.

7. (Open question) Using the reasoning of Murray's law, explain why arteries dilate (caliber increases) under long-term high blood flow and become narrower when blood flow is reduced (for example the arteries of a stump after amputation). Design a measurement to test whether a vascular network satisfies Murray's law.

   **Answer** In a Murray network the shear stress $\tau = 4\eta F/(\pi r^3)$ is the same everywhere. A long-term increase of blood flow raises $\tau$; endothelial cells sense a shear stress above the set value, release factors such as NO and initiate remodeling, and the caliber increases until $\tau$ returns to the set value ($r \propto F^{1/3}$); a decrease of flow does the opposite and the caliber decreases. Test: using vascular casts, micro-CT or intravital imaging, measure the radii of the parent branch and two daughter branches at many bifurcations in a vascular tree and fit the exponent $p$ in $r_0^p = r_1^p + r_2^p$ to see whether it is close to 3; one can also measure the flow in each branch at the same time (for example by Doppler or particle tracking) to test directly whether $F \propto r^3$ and whether shear stress is approximately constant. Large arteries (pulsatile, inertial, where deviation is expected) should be distinguished from small arteries.
