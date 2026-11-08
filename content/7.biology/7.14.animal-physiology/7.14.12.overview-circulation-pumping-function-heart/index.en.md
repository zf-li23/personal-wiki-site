---
title: Overview of Circulation and the Pumping Function of the Heart
description: "Why circulation is needed (diffusion time x² = 2Dt); the four elements of bulk flow and the diversity of pumps; open and closed circulatory systems; the systemic and pulmonary circulations; the time allocation of the cardiac cycle, pressures and volumes in each phase, pressure gating of the valves, heart sounds and atrial pressure waves; the pressure–volume loop, external work of about 1 J against a total energy cost of about 6 J, and the heart as maintainer of a pressure field; stroke volume, ejection fraction, cardiac output and cardiac index; preload, afterload and contractility; the sarcomere basis of the Frank–Starling mechanism; effects of the autonomic nerves, ions and temperature; evolution and comparative biology: diversity and convergence of circulatory systems across animal phyla, separation of the vertebrate heart and pulmonary circulation, and the early heartbeat of the zebrafish embryo."
source_hash: fc52b53bce16
---

Cells exchange materials with their environment by diffusion, which is fast on the micrometer scale but far too slow on the centimeter scale to sustain life. Large animals therefore need a system that drives bulk flow of fluid by pressure, carrying materials rapidly to the neighborhood of every cell and leaving only the last few tens of micrometers to diffusion. This is the circulatory system. This chapter begins by explaining physically why a circulatory system is necessary, what elements it consists of, and the two designs found in the animal kingdom, open and closed (Section 12.1). It then describes the overall structure of the human circulation (Section 12.2). Next comes the core of the chapter, the heart as a pump: how pressure and volume change during one cardiac cycle (Section 12.3), how much work the heart does and how much energy it consumes (Section 12.4), how pumping function is measured by stroke volume and cardiac output (Section 12.5), how the heart automatically adjusts its output to the volume of returning blood (the Frank–Starling mechanism, Section 12.6), and how it is regulated by nerves and ions (Section 12.7). The structure of cardiac muscle cells and excitation–contraction coupling are in Chapter 10, the electrical activity and rhythm of the heart in the next chapter, the mechanics of blood flow in vessels in Chapter 14, and the integrated regulation of the circulation in Chapter 16. Blood itself is in Chapter 11, and the development of the heart in [7.5.28](/7.5.28).

## 12.1. Why a Circulatory System Is Needed

### 12.1.1. The Distance Limit of Diffusion

From the statistics of the **random walk** ([7.6.5](/7.6.5)), the **mean squared displacement** of a molecule diffusing along one direction in time $t$ is

$$
\langle x^2\rangle = 2Dt,
$$

so the time required for diffusion is proportional to the square of the distance. This is the fundamental reason for the existence of circulatory systems.

**Example 12.1.1 (Time Required for Diffusion)** The **diffusion coefficient** of small molecules such as glucose in water is about $D = 10^{-9}\,\mathrm{m^2\,s^{-1}}$. Diffusing $100\,\mathrm{\mu m}$ (the size of a fairly large cell) takes $t = x^2/2D = (10^{-4})^2/(2 \times 10^{-9}) = 5\,\mathrm{s}$; diffusing $10\,\mathrm{\mu m}$ takes only $0.05\,\mathrm{s}$; diffusing $1\,\mathrm{mm}$ takes $500\,\mathrm{s}$ (about 8 min); diffusing $1\,\mathrm{m}$ takes $5 \times 10^8\,\mathrm{s}$, about 16 years. The diffusion coefficient of $\ce{O2}$ in tissue is about $2 \times 10^{-9}\,\mathrm{m^2\,s^{-1}}$, of the same order of magnitude.

:::

If a substance moves with the fluid as a whole at velocity $v$ (convection, bulk flow), the time required, $t = x/v$, is proportional only to the distance. The blood of a person takes about 1 min to go from the heart to the foot and back, shortening the diffusion time for $1\,\mathrm{m}$ by about $10^7$-fold. Which of the two transport processes is faster is judged by the **Péclet number** $\mathrm{Pe} = vL/D$: convection dominates when $\mathrm{Pe} \gg 1$. In the aorta $v \approx 0.3\,\mathrm{m\,s^{-1}}$ and $L \approx 1\,\mathrm{m}$, so $\mathrm{Pe} \sim 10^8$; in capillaries $v \approx 0.3\,\mathrm{mm\,s^{-1}}$, but the distance perpendicular to the wall is only a few micrometers, and diffusion takes over here.

Besides distance, the rate of oxygen consumption also determines whether diffusion is sufficient. The oxygen consumption of a spherical organism is proportional to its volume ($\propto r^3$), while the oxygen entering by diffusion through the body surface is proportional to the surface area ($\propto r^2$), so the ratio falls as body size increases. A simple estimate (a spherical organism with surface $\ce{O2}$ concentration at the atmospheric equilibrium value and uniform oxygen consumption) shows that at the typical oxygen consumption rate of animal tissue, an organism supplied with oxygen by diffusion alone cannot have a radius greater than about $1\,\mathrm{mm}$. Large body size, complex structure (interior cells far from the body surface) and a high metabolic rate are the three conditions that make a circulatory system necessary in animals. The human body still contains cells that exchange gas with the outside directly by diffusion, such as alveolar epithelial cells and the outer cells of the epidermis, but they all lie on surfaces only a few tens of micrometers from the environment.

### 12.1.2. The Four Elements of Bulk Flow

Any system that transports materials by bulk flow needs four elements:

| Element | Role | In the human body |
|---|---|---|
| Pressure difference | Drives the fluid | The heart, and compression of veins by skeletal muscle |
| One-way valves | Make the flow go in one direction only | Heart valves, venous valves, lymphatic valves |
| Tubes or chambers | Guide the fluid and define the route of flow | Blood vessels, lymphatic vessels, cardiac chambers |
| Medium | Carries the transported substances | Blood, lymph |

The "pump" that generates the pressure difference takes three basic forms in animals:

- Chambered heart (vertebrates and many invertebrates): when a chamber with muscular walls contracts, the pressure of the fluid in it rises, and with one-way valves at the inlet and outlet (opened and closed by the pressure difference) the fluid is driven in one direction.
- **Skeletal muscle pump** (vertebrates and invertebrates): when skeletal muscle contracts it compresses the veins or lymphatic vessels between its fibers, and together with the one-way valves in the vessels it drives fluid toward the heart (Chapter 14).
- Contractile vessel (invertebrates, such as the dorsal vessel of annelids and of insects): a peristaltic wave of the wall muscle propagates along the tube and pushes the fluid in the direction of the wave; the direction is determined by the direction of peristalsis, and valves are not necessarily needed.

### 12.1.3. Open and Closed Circulation

**Definition 12.1.1 (Open and Closed Circulatory Systems)** A circulatory system in which the circulating fluid always flows in vessels (tubes whose walls have a specialized lining that separates the circulating fluid from the tissues) and in which substances must cross the vessel wall to enter the tissues is called a **closed circulatory system**. A circulatory system in which the circulating fluid leaves the vessels at least at one point and enters sinuses in the body cavity (collectively called the **hemocoel**), where it contacts the tissues directly and mixes with the extracellular fluid, is called an **open circulatory system**.

The circulating fluid in an open circulatory system is the hemolymph mentioned in Chapter 11. The general features of the two systems are compared below:

| Property | Closed circulation | Open circulation |
|---|---|---|
| Fate of the circulating fluid | Always within vessels | Flows freely in the hemocoel, mixing with **interstitial fluid** |
| Pressure and flow rate | High, fast flow, can be distributed to organs as needed | Low, slow flow, distribution depends mainly on body movement |
| Volume of circulating fluid | Small (human blood volume is about 7% of body weight) | Large (up to 20%–40% of body weight) |
| Suited to | Large animals with high metabolic rates (vertebrates, cephalopods, annelids) | Animals of smaller size or lower metabolic rate, or with another route of oxygen supply (most arthropods and mollusks) |
| Energy cost | High | Low |
| Structure | Complex (heart, multilevel vessels, capillaries) | Simple |
| Effect of injury | Blood loss is dangerous | Easier to repair |

This comparison is only a generalization. Open and closed are not mutually exclusive classes: many so-called open animals have well-developed vessels and the hemolymph leaves the vessels only locally (the vessels of crustaceans, for example, can branch very finely and open into sinuses at only a few sites), and the closed vertebrates also have "open" parts, such as the sinusoids of the liver, spleen and bone marrow, where the endothelium is discontinuous and blood contacts parenchymal cells directly. The open circulation of insects is inefficient, but this does not limit their metabolism: the oxygen of insects is delivered in the gas phase directly to the cells by the **tracheal system** (Chapter 17), and the hemolymph takes practically no part in oxygen transport.

## 12.2. Structure of the Human Circulatory System

### 12.2.1. Systemic and Pulmonary Circulations

The heart of mammals (and birds) is completely divided into left and right halves, forming two circulations in series:

- *Systemic circulation*: left ventricle → aorta → arteries of all levels → arterioles → capillaries throughout the body → veins → superior and inferior venae cavae → right atrium.
- *Pulmonary circulation*: right ventricle → pulmonary artery → pulmonary capillaries → pulmonary veins → left atrium.

The two circulations are in series, so in the steady state the volumes of blood ejected per minute by the left and right ventricles must be equal (Section 12.6.3). The distribution of blood volume among the parts is very uneven: the systemic circulation holds about 84% (veins about 64%, arteries about 13%, arterioles and capillaries about 7%), the pulmonary circulation about 9% and the heart about 7%. The veins are therefore a "reservoir" of blood (capacitance vessels), which is important in circulatory regulation (Chapters 14 and 16).

By pressure, the circulation is divided into a high-pressure part (the left ventricle in systole and the systemic arteries, with a mean of about $90$–$100\,\mathrm{mmHg}$, $1\,\mathrm{mmHg} = 0.1333\,\mathrm{kPa}$, that is, about $13\,\mathrm{kPa}$) and a low-pressure part (systemic capillaries and veins, the right heart, the pulmonary circulation and the left atrium, mostly below $25\,\mathrm{mmHg}$). The high-pressure part distributes blood to the organs, and the low-pressure part holds most of the blood. Capillaries are the site of exchange: their walls are thin and they are enormously numerous, forming meshlike capillary beds (Chapter 15).

### 12.2.2. The Heart and Cardiac Muscle

The human heart has four chambers: right atrium, right ventricle, left atrium and left ventricle. Between atria and ventricles are the atrioventricular valves (the tricuspid on the right and the mitral on the left), and between the ventricles and the arteries are the semilunar valves (pulmonary and aortic, each with three semilunar cusps). The free edges of the atrioventricular valves are attached by chordae tendineae to the papillary muscles of the ventricular wall; when the ventricle contracts the papillary muscles contract at the same time and pull on the chordae, preventing the cusps from everting into the atrium.

Cardiac muscle is striated muscle with the same contractile mechanism as skeletal muscle (the actin–myosin cross-bridge cycle), but cardiac cells are connected to one another through **intercalated discs**. The **gap junctions** in the discs let excitation pass directly from one cell to the next, and **desmosomes** and **adherens junctions** bind the cells mechanically into one whole, so that atrial muscle and ventricular muscle are each a "functional syncytium": once excitation arises it spreads to the whole atrium or ventricle, and all parts contract almost simultaneously (all or none). Cardiac muscle also has stretch-sensitive ion channels, so that its electrical activity is influenced by its mechanical state (mechano-electrical feedback). Atrial and ventricular muscle are separated by a nonconducting fibrous ring, and excitation can pass from atria to ventricles only through the atrioventricular node and the atrioventricular bundle. Besides the contracting working cells, the heart contains specialized autorhythmic cells (the **sinoatrial node**) and conducting cells (the atrioventricular node, the bundle of His and Purkinje fibers), described in Chapter 13; the structure of cardiac muscle cells and **excitation–contraction coupling** are in Chapter 10.

## 12.3. The Cardiac Cycle

### 12.3.1. Time Allocation

**Definition 12.3.1 (Cardiac Cycle)** The cycle of mechanical activity formed by one contraction and one relaxation of the heart is called the **cardiac cycle**. The atria and ventricles each have their own systole and diastole; what are usually called systole and diastole refer to those of the ventricles.

Each cardiac cycle begins with a spontaneous **action potential** of the sinoatrial node (Chapter 13). At a heart rate of 75 beats per minute the cardiac cycle lasts $60/75 = 0.8\,\mathrm{s}$: the atria contract first, for about $0.1\,\mathrm{s}$, and then relax for about $0.7\,\mathrm{s}$; when atrial contraction ends the ventricles begin to contract, for about $0.3\,\mathrm{s}$, and then relax for about $0.5\,\mathrm{s}$. During the first $0.4\,\mathrm{s}$ of ventricular diastole the atria are also in diastole, a period called the joint diastole. Systole occupies about 40% of the cycle and diastole about 60%.

When the heart rate increases the cardiac cycle shortens, but systole and diastole shorten to different degrees: when the heart rate increases from 75 to 200 beats/min the cycle shortens from 0.8 s to 0.3 s, systole shortens only to about 0.16–0.2 s, while diastole shortens to 0.1–0.14 s, and its share falls from 60% to less than half. Ventricular filling and the blood supply of the myocardium itself (the coronary arteries are perfused mainly in diastole) both take place in diastole, so an excessively fast heart rate causes insufficient filling and myocardial ischemia, which is why there is an upper limit to the increase of cardiac output by heart rate (Section 12.7.3).

### 12.3.2. Pressures and Volumes in Each Phase

Taking the left heart as an example, the cardiac cycle is divided into the following phases by the opening and closing of the valves (durations for a heart rate of 75 beats/min):

| Phase | Duration | Valves | Pressure relations | Ventricular volume | ECG and heart sounds |
|---|---|---|---|---|---|
| Atrial systole | 0.1 s | AV valve open, semilunar valve closed | Atrial pressure slightly above ventricular pressure | Increases by a further 20% or so, reaching the end-diastolic volume (about 120–130 mL) | After the P wave |
| Isovolumetric contraction | 0.05 s | Both closed | Ventricular pressure rises sharply from about $8\,\mathrm{mmHg}$ to the aortic diastolic pressure (about $80\,\mathrm{mmHg}$) | Unchanged | Right after the QRS complex; first heart sound |
| Rapid ejection | 0.1 s | Semilunar valve open | Ventricular pressure above aortic pressure, reaching its peak (about $120\,\mathrm{mmHg}$) | Falls rapidly, ejecting about two thirds of the stroke volume | ST segment |
| Reduced ejection | 0.15 s | Semilunar valve open | Ventricular pressure slightly below aortic pressure; blood continues to flow out by inertia | Continues to fall to the end-systolic volume (about 50–60 mL) | T wave |
| Isovolumetric relaxation | 0.06–0.08 s | Both closed | Ventricular pressure falls sharply to below atrial pressure | Unchanged | Second heart sound |
| Rapid filling | 0.11 s | AV valve open | Ventricular pressure below atrial pressure (ventricular relaxation produces suction) | Increases rapidly | (Third heart sound) |
| Reduced filling | 0.22 s | AV valve open | Pressure difference decreases | Increases slowly | — |

In the rapid and reduced filling phases, about 80% of ventricular filling is accomplished by blood flowing passively from the veins through the atrium into the ventricle; atrial contraction pushes in only a further 20% (at rest). The atrium is thus more like a "booster pump": in atrial fibrillation the atria lose effective contraction, and at rest patients often have no obvious symptoms, while on exercise (diastole shortened, passive filling reduced) cardiac output becomes clearly inadequate.

Plotting pressure, volume, the ECG and the heart sounds on the same time axis gives the Wiggers diagram. The figure below is generated from a lumped-parameter model of the left heart. Ventricular and atrial contraction are represented by a time-varying elastance (ventricular pressure $P = E(t)(V - V_0)$, with the elastance $E$ increasing in systole and decreasing in diastole), the valves are diodes allowing one-way flow only, and the aorta is a three-element Windkessel (Chapter 14); the shapes agree with real measurements.

![The cardiac cycle (time-varying elastance model of the left heart, heart rate 75 beats/min). A: Wiggers diagram; from top to bottom, the pressures of the left ventricle, aorta and left atrium, the left ventricular volume, and the ECG and heart sounds. The dashed lines mark four moments, mitral valve (MV) closure, aortic valve (AV) opening, aortic valve closure and mitral valve opening, which divide the cycle into five phases: atrial systole, isovolumetric contraction (IVC), ejection, isovolumetric relaxation (IVR) and filling. The first heart sound (S1) coincides with closure of the atrioventricular valve and the second (S2) with closure of the semilunar valve. B: the pressure–volume loop of the same beat, with the end-systolic (ESPVR) and end-diastolic (EDPVR) pressure–volume relations](./plots/wiggers.py)

The cycle of the right heart is synchronous with that of the left heart and has the same shape, but the pressures are much lower: right ventricular systolic pressure is about $25\,\mathrm{mmHg}$, end-diastolic pressure about $4\,\mathrm{mmHg}$, and pulmonary artery pressure about $25/8\,\mathrm{mmHg}$.

### 12.3.3. Pressure Gating of the Valves

The valves of the heart are all passive: they have no muscle and open and close only according to the pressure difference across them. Taking the mitral valve as an example, let the left atrial pressure be $P_1$ and the left ventricular pressure $P_2$: when $P_1 > P_2$ the valve is pushed open and blood flows into the ventricle; when $P_1 < P_2$ the valve is pushed shut, and the chordae tendineae prevent it from everting into the atrium. The aortic valve is the same, with the direction reversed. Each reversal of the pressure relation during the cardiac cycle corresponds to the opening or closing of a valve, and as ventricular contraction and relaxation change the pressure in the ventricle, they automatically determine the direction of blood flow. This "pressure gating" makes the heart a simple and reliable pump: it needs no signal to control the valves. When a valve is stenotic (opens incompletely), a larger pressure difference is needed to maintain flow and the ventricular load increases; when a valve is incompetent, part of the blood regurgitates, and a part of the stroke volume merely shuttles back and forth between the ventricle and the atrium (or aorta).

### 12.3.4. Heart Sounds and Atrial Pressure Waves

The vibrations caused during the cardiac cycle by valve closure and by acceleration and deceleration of blood flow are transmitted to the chest wall and can be heard with a stethoscope as heart sounds:

| Heart sound | Timing | Cause | Features |
|---|---|---|---|
| First heart sound (S1) | Onset of ventricular systole | Closure of the atrioventricular valves, blood striking the valves and ventricular wall | Lower pitch, longer duration (about 0.1–0.12 s); marks the onset of ventricular systole, heard best at the apex |
| Second heart sound (S2) | Onset of ventricular diastole | Closure of the semilunar valves, blood decelerating at the roots of the aorta and pulmonary artery | Higher pitch, shorter duration (about 0.08 s); marks the onset of ventricular diastole, heard best at the base; on inspiration closure of the pulmonary valve is delayed and the sound can split into two components |
| Third heart sound (S3) | End of rapid filling | Sudden deceleration of the filling flow, vibration of the ventricular wall and papillary muscles | Low frequency, faint; audible in some healthy children and young adults; in adults it often suggests raised ventricular filling pressure |
| Fourth heart sound (S4) | Atrial systole | Atrial contraction pushes blood into a ventricle with reduced compliance (stiff) | Normally inaudible; its presence is mostly pathological |

The pressure in the atrium (and in the jugular vein) shows three positive waves in a cycle: the a wave is caused by atrial contraction; the c wave by the atrioventricular valve bulging into the atrium during isovolumetric ventricular contraction; and the v wave is formed as venous blood continues to flow into the atrium while the atrioventricular valve is closed, so that atrial pressure gradually rises, and it falls rapidly when the atrioventricular valve opens.

## 12.4. Work and Energy of the Heart

### 12.4.1. The Pressure–Volume Loop

If left ventricular pressure is plotted against volume, one cardiac cycle traces a closed curve.

**Definition 12.4.1 (Pressure–Volume Loop)** The closed curve traced by ventricular pressure against ventricular volume during one cardiac cycle is called the **pressure–volume loop** (P–V loop) of the ventricle. In the counterclockwise direction it consists of four segments in order: filling (A→B, volume increases, pressure rises slightly), isovolumetric contraction (B→C, volume constant, pressure rises sharply), ejection (C→D, volume decreases) and isovolumetric relaxation (D→A, volume constant, pressure falls sharply).

The four corners of the loop correspond to four valve events: point B, mitral valve closure (end of diastole); point C, aortic valve opening; point D, aortic valve closure (end of systole); point A, mitral valve opening. The width of the loop is the stroke volume. The lower edge of the loop lies on the end-diastolic pressure–volume relation (EDPVR), which reflects the passive elasticity of the relaxed ventricle and becomes steep at large volumes; the upper left corner lies on the end-systolic pressure–volume relation (ESPVR), which is approximately a straight line whose slope (the end-systolic elastance $E_{\mathrm{es}}$) measures the contractility of the myocardium and over a considerable range does not change with filling and arterial pressure. In every cycle the ventricle operates between these two boundaries; greater contraction (smaller end-systolic volume) or more filling (larger end-diastolic volume) makes the loop larger, and this is the dynamic range of the work done by the heart.

That ventricular pressure first rises and then falls during ejection (the C→D segment in the figure first rises and then falls) is because at the beginning of ejection the myocardium is still increasing its contraction (the time-varying elastance is still increasing) while ejection reduces the volume.

### 12.4.2. External Work and Total Energy Expenditure

The external work done by the ventricle per beat is the area of the pressure–volume loop:

$$
W = \oint P\,\mathrm{d}V,
$$

that is, the pressure–volume work done by the ventricle in pushing blood from the low-pressure atrium to the high-pressure artery; in addition there is the kinetic energy $\tfrac12 \rho v^2 V$ imparted to the blood.

**Example 12.4.1 (The Energy Account of the Heart)** The stroke volume of the left ventricle is $70\,\mathrm{mL}$ and the mean pressure during ejection is about $100\,\mathrm{mmHg} = 13.3\,\mathrm{kPa}$, so the pressure–volume work is about $70 \times 10^{-6}\,\mathrm{m^3} \times 1.33 \times 10^4\,\mathrm{Pa} \approx 0.93\,\mathrm{J}$, that is, about $1\,\mathrm{J}$ per beat. The mean velocity of blood in the aorta during ejection is about $0.5\,\mathrm{m\,s^{-1}}$, giving a kinetic energy of about $\tfrac12 \times 1060\,\mathrm{kg\,m^{-3}} \times 0.25\,\mathrm{m^2\,s^{-2}} \times 70 \times 10^{-6}\,\mathrm{m^3} \approx 0.01\,\mathrm{J}$, only about 1% of the pressure work (in strenuous exercise the velocity doubles and the kinetic energy is still only a few percent; it can increase markedly in aortic stenosis). The pressure of the right ventricle is about 1/6 that of the left ventricle, and its external work is also about 1/6 that of the left. At a heart rate of 75 beats/min, the mechanical power of the left heart is about $1.2\,\mathrm{W}$.

The total energy consumed by the heart is much greater. Myocardial oxygen consumption at rest is about $8$–$10\,\mathrm{mL\,min^{-1}}$ per $100\,\mathrm{g}$, so a heart of 300 g consumes about $30\,\mathrm{mL\,min^{-1}}$; oxidizing substrate releases about $20\,\mathrm{J}$ per milliliter of $\ce{O2}$, giving a total power of about $10\,\mathrm{W}$ and about $6$–$8\,\mathrm{J}$ per beat. That is, the external work of the two ventricles together is about $1.1\,\mathrm{J}$ and total energy expenditure about $6$–$8\,\mathrm{J}$, so the efficiency of the heart as a mechanical pump is only about 15% (usually 10%–20% at rest, rising to about 25% in exercise), similar to that of skeletal muscle.

:::

Most of the total energy expenditure (the "internal work") does not appear in the pressure–volume loop: pumps that maintain ion gradients ($\ce{Na+}$/$\ce{K+}$-ATPase, the sarcoplasmic reticulum $\ce{Ca^2+}$-ATPase SERCA, and sodium–calcium exchange), cross-bridge cycling that generates tension during isovolumetric contraction without doing external work, and basal metabolism. Internal work cannot be measured directly and can only be inferred from the difference between oxygen consumption and external work. The oxygen consumption of the ventricle is linearly related to the "pressure–volume area" (the area of the P–V loop plus the triangular region between the loop and the ESPVR and EDPVR, the latter representing potential energy stored in the myocardium at end-systole without doing external work), an empirical law of cardiac energetics (Suga). It follows that for the same external work, doing it at high pressure and small volume (high afterload) consumes more oxygen than at low pressure and large volume; this is one reason why hypertension increases myocardial oxygen consumption and causes myocardial hypertrophy.

### 12.4.3. The Heart Maintains a Pressure Field

The energy account above answers a question: is the role of the heart to "squirt" blood into the vessels? Kinetic energy accounts for only 1% of the external work, which shows that the heart hardly drives the circulation by giving the blood velocity. The role of the heart is to establish and maintain, by periodic work, a pressure distribution (a pressure field) in the circulatory system: a mean pressure of about $100\,\mathrm{mmHg}$ is maintained in the arteries and only a few $\mathrm{mmHg}$ in the veins, and blood flows down this pressure gradient through the resistance vessels of the organs. The blood flow of each organ is determined by its local resistance, and the elasticity of the vessels (the Windkessel effect of Chapter 14) smooths the intermittent ejection of the heart into a continuous pressure.

This view also determines where circulatory control is exerted: the body regulates first of all arterial blood pressure (the **baroreceptor reflex**, Chapter 16), not the blood flow at any one place; each organ then draws flow as needed from the common pressure source by changing its own resistance.

From the molecular point of view, the energy invested by the heart can be divided by function into four classes:

| Function | Molecular system | Core process | Role of the energy |
|---|---|---|---|
| State | SERCA, sodium–calcium exchanger, $\ce{Na+}$/$\ce{K+}$-ATPase | Maintaining ion gradients | Establishes a nonequilibrium state so that the cell can be excited (excitability) |
| Tension | Myosin, actin, troponin | Cross-bridge cycle | Generates tension (sustained force) |
| Control | $\beta_1$ adrenergic receptor, PKA, L-type calcium channel | Phosphorylation | Changes the parameters of the system (regulability) |
| Stabilization | Titin, connexin, cytoskeleton | Viscoelasticity and coupling | Provides damping and restoring force so that each contraction is reproducible |

## 12.5. Cardiac Output and Its Assessment

### 12.5.1. Stroke Volume, Ejection Fraction and Cardiac Output

**Definition 12.5.1 (Stroke Volume, Ejection Fraction, Cardiac Output)** The volume of blood ejected by one ventricle in each contraction is called the **stroke volume** (SV), equal to the difference between the end-diastolic volume (EDV) and the end-systolic volume (ESV). The stroke volume as a percentage of the end-diastolic volume is called the **ejection fraction** (EF). The volume of blood ejected by one ventricle per minute is called the **cardiac output** (CO):

$$
\mathrm{SV} = \mathrm{EDV} - \mathrm{ESV}, \qquad \mathrm{EF} = \frac{\mathrm{SV}}{\mathrm{EDV}}, \qquad \mathrm{CO} = \mathrm{SV} \times \mathrm{HR}.
$$

In a resting healthy adult the EDV is about 120–130 mL, the ESV about 50–60 mL, the SV about 70 mL and the EF 55%–65%; at a heart rate of 70–75 beats/min the CO is about $5\,\mathrm{L\,min^{-1}}$ (10%–20% lower in women than in men). Cardiac output is related to body size, and different individuals are compared using the cardiac index:

**Definition 12.5.2 (Cardiac Index)** The cardiac output per square meter of body surface area is called the **cardiac index**. At rest in adults it is about $3.0$–$3.5\,\mathrm{L\,min^{-1}\,m^{-2}}$ (the body surface area of an adult of average build is about $1.6$–$1.7\,\mathrm{m^2}$); it is highest at about 10 years of age (more than $4\,\mathrm{L\,min^{-1}\,m^{-2}}$) and declines with age.

Normalizing by body surface area rather than body weight is done because resting metabolic rate is more nearly proportional to body surface area than to body weight (metabolic scaling in Chapter 30). The ejection fraction is the most commonly used index of ventricular systolic function: when the ventricle is dilated and contraction is weakened, SV may still be normal (compensated by an increased EDV), but EF falls. The ability of cardiac output to increase with the metabolic needs of the body is called cardiac reserve: in strenuous exercise the cardiac output of a healthy adult can reach 4–5 times the resting value ($25$–$30\,\mathrm{L\,min^{-1}}$), and in elite endurance athletes more than $35\,\mathrm{L\,min^{-1}}$, mainly from heart rate reserve (which can increase 2–2.5-fold) and systolic reserve (reduced ESV).

### 12.5.2. Preload, Afterload and Contractility

The factors that affect stroke volume can be grouped into three classes, whose effects on the pressure–volume loop are quite different.

**Definition 12.5.3 (Preload and Afterload)** The load borne by the myocardium before it contracts is called the **preload**; it determines the initial length of the muscle and, for the ventricle, is expressed by the end-diastolic volume (or end-diastolic pressure, or atrial pressure). The load encountered only after the muscle begins to contract is called the **afterload**; for the ventricle it is mainly the arterial pressure that must be overcome during ejection.

The third factor is the contractility of the myocardium: the ability of the muscle itself to generate force and shorten, independent of preload and afterload, determined by the amount of $\ce{Ca^2+}$ in excitation–contraction coupling and the sensitivity of the myofilaments to $\ce{Ca^2+}$, and expressed on the pressure–volume loop as the slope of the ESPVR.

![Effects of preload, afterload and contractility on the pressure–volume loop (time-varying elastance ventricle model, heart rate 75 beats/min; dotted line, ESPVR; dashed line, EDPVR). A: when filling pressure (preload) increases, the end-diastolic volume increases, the loop expands to the right, and stroke volume and external work both increase. B: when peripheral resistance (afterload) increases, the aortic valve opens later and the ejection pressure is higher, the end-systolic point moves up along the ESPVR, and stroke volume decreases. C: when contractility (ESPVR slope Emax) increases, the end-systolic volume decreases at the same filling and stroke volume increases. D: the curve of stroke volume against filling pressure (Starling's ventricular function curve); sympathetic stimulation raises contractility and shifts the curve upward](./plots/pv-loops.py)

Three rules can be read from the figure:

1. When preload increases, stroke volume increases: this is the Frank–Starling mechanism of the next section.
2. When afterload increases (arterial pressure rises), isovolumetric contraction is prolonged and ejection shortened, and stroke volume decreases transiently; but incomplete ejection increases the end-systolic volume, and if venous return is unchanged the next end-diastolic volume increases accordingly, so that through the Frank–Starling mechanism stroke volume is largely restored within a few beats, at the cost of the ventricle working at a larger volume and higher pressure. Long-term increase of afterload (hypertension, aortic stenosis) causes concentric myocardial hypertrophy.
3. When contractility increases, the ESPVR steepens and ejection is more complete at the same preload and afterload, so the ejection fraction rises. Sympathetic nerves and epinephrine, digitalis drugs and raised extracellular $\ce{Ca^2+}$ increase contractility; hypoxia, acidosis and heart failure reduce it.

## 12.6. Autoregulation of Cardiac Pumping: The Frank–Starling Mechanism

### 12.6.1. The Starling Curve

Otto Frank (1895) found in the isolated frog heart that the more the ventricle is filled at end-diastole, the greater the pressure produced in the subsequent isovolumetric contraction. Ernest Starling and his colleagues (1914), keeping arterial pressure and heart rate constant in the dog heart–lung preparation and varying venous return, found that cardiac output increases with venous return over a wide range: the heart ejects the volume of blood it receives, within certain limits. This conclusion has been summarized as the "law of the heart."

**Definition 12.6.1 (Frank–Starling Mechanism)** Within a certain range, the greater the ventricular end-diastolic volume (the initial length of the myocardium), the stronger the contraction of the myocardium and the greater the stroke volume. This regulation of contractile force, independent of nerves and humoral factors and caused by a change in the initial length of the myocardium, is called the **Frank–Starling mechanism** (heterometric autoregulation).

The curve plotted with stroke volume (or stroke work) as ordinate and filling pressure (left atrial pressure or end-diastolic pressure) as abscissa is called the ventricular function curve (Starling curve). The curve is steep at low filling pressure and flattens gradually as filling pressure rises: stroke work increases rapidly as left atrial pressure increases from $0$ to about $12\,\mathrm{mmHg}$ and hardly increases further above $15$–$20\,\mathrm{mmHg}$. The normal ventricle works on the rising part of the curve and has a large reserve of initial length.

### 12.6.2. The Sarcomere Basis

The Frank–Starling mechanism rests on the **length–tension relationship** of cardiac muscle, but cardiac muscle differs from skeletal muscle in two respects.

Passive tension: for the same change in length, the passive tension of cardiac muscle is much greater than that of skeletal muscle and rises much faster. The passive elastic elements in cardiac muscle are hard to stretch: cardiac muscle mainly expresses the short, stiff N2B isoform of titin (the titin molecule of skeletal muscle is longer and more extensible), and the extracellular collagen network is also denser. Within the physiological range, therefore, cardiac sarcomeres are rarely stretched beyond $2.3$–$2.4\,\mathrm{\mu m}$; even when end-diastolic pressure rises to $50\,\mathrm{mmHg}$, sarcomere length hardly exceeds $2.6\,\mathrm{\mu m}$, and the heart does not fall onto the descending limb of the length–tension relationship through overfilling. This is exactly why the ventricular function curve flattens, rather than falls, at high filling pressure.

Active tension: over the sarcomere length range $1.8$–$2.4\,\mathrm{\mu m}$, the active tension of frog skeletal muscle changes little (near the plateau of the length–tension curve of [Chapter 9](/7.14.9)), whereas the active tension of cardiac muscle increases steeply with sarcomere length, much more steeply than expected from the degree of overlap of thick and thin filaments alone. Beyond a sarcomere length of about $2.4\,\mathrm{\mu m}$ active tension declines, and the resistance of the passive elements opposes further development of active tension. Replacing sarcomere length by ventricular end-diastolic volume and active tension by ventricular pressure turns the length–tension relationship of cardiac muscle into the pressure–volume relationship of the ventricle:

| Sarcomere level | Ventricular level |
|---|---|
| Sarcomere length (initial length) | End-diastolic volume |
| Active tension | Ventricular pressure in isovolumetric contraction, the ESPVR |
| Passive tension | Ventricular pressure in diastole, the EDPVR |

Why does active tension change so steeply with length in cardiac muscle? Filament overlap explains only a small part (below $1.8\,\mathrm{\mu m}$ the thin filaments overlap one another and the thick filaments butt against the Z lines, which does reduce tension). The main cause is *length-dependent activation*: when the sarcomere is stretched, the same $\ce{Ca^2+}$ concentration produces greater tension, that is, the sensitivity of the myofilaments to $\ce{Ca^2+}$ is increased. Possible mechanisms include the following: the volume of the sarcomere is essentially constant on stretch, so the lattice spacing between thick and thin filaments decreases and the myosin heads more readily contact actin; stretched titin transmits tension to the thick filament, converting myosin heads that were held "off" against the thick filament backbone into an "on" state able to bind; and the affinity of troponin C for $\ce{Ca^2+}$ rises with tension. In addition, stretch increases the intracellular $\ce{Ca^2+}$ transient within minutes (the "slow response," part of the Anrep effect). Skeletal muscle works in the body at lengths near the plateau and grades its force mainly by recruiting **motor units** and changing stimulation frequency (Chapter 9); cardiac muscle is an all-or-none syncytium that can neither recruit nor tetanize, and changing the initial length becomes its intrinsic means of regulating the force of each contraction.

### 12.6.3. Physiological Significance

The most important role of the Frank–Starling mechanism is to match the outputs of the left and right ventricles precisely. The two ventricles are in series; if the output of the left ventricle were persistently 1% less than that of the right (0.7 mL per beat), about $50\,\mathrm{mL}$ of blood would be retained in the pulmonary circulation each minute, the pulmonary blood volume would increase by about $1.5\,\mathrm{L}$ after half an hour, and **pulmonary edema** would result. In fact, the extra blood ejected by the right ventricle slightly increases pulmonary venous return and the left ventricular end-diastolic volume, the stroke volume of the left ventricle increases accordingly, and within a few beats the two sides are back in balance, without any neural signal. Likewise, when changes of posture or respiration transiently alter venous return, the heart adjusts its output beat by beat by this mechanism. The denervated transplanted heart can still increase its cardiac output markedly with exercise, in part by the Frank–Starling mechanism.

## 12.7. Neural and Humoral Regulation of Cardiac Pumping

### 12.7.1. Autonomic Nerves

The heart is innervated by both sympathetic and parasympathetic (vagus) nerves, whose actions are opposite:

| | Parasympathetic (vagus) | Sympathetic |
|---|---|---|
| Main action | Slows the heart rate | Speeds the heart rate, strengthens contraction |
| Sites innervated | Sinoatrial node, atrial muscle, atrioventricular node (vagal innervation of ventricular muscle is sparse) | Sinoatrial node, atrioventricular node, atrial and ventricular muscle, Purkinje fibers |
| Transmitter and receptor | Acetylcholine, $\mathrm{M}_2$ muscarinic receptor | Norepinephrine, $\beta_1$ adrenergic receptor |
| Effect on cardiac output | Strong stimulation can stop the heart for a few seconds, after which the ventricle "escapes" with its own rhythm of 20–40 beats/min | Maximal stimulation can raise the heart rate to 180–200 beats/min (up to 250 beats/min in young people), doubles the force of contraction, and raises cardiac output at the same filling pressure to more than about twice |

At rest the vagal influence predominates: after all the nerves to the heart are cut, the heart rate rises from about 70 beats/min to the intrinsic frequency of the sinoatrial node (about 100 beats/min). On the other hand, the heart also receives a continuous low level of sympathetic impulses: blocking the sympathetic action reduces the pumping capacity of the heart (the cardiac output curve) by about 20%–30%. Neural regulation appears on the Starling curve as a shift of the whole curve: sympathetic stimulation shifts the curve upward (panel D), and vagal stimulation or sympathetic inhibition shifts it downward. Sympathetic nerves also speed relaxation of the myocardium (phosphorylating phospholamban and accelerating SERCA uptake of $\ce{Ca^2+}$), which ensures filling when the heart rate rises and diastole is shortened. How the transmitters change the ionic currents of pacemaking and conduction is in Chapter 13, the organization of the **autonomic nervous system** in Chapter 7, and how the baroreceptor reflex regulates blood pressure through them in Chapter 16. Epinephrine secreted by the adrenal medulla acts through the blood on the same $\beta_1$ receptors, with effects identical to those of the sympathetic nerves.

### 12.7.2. Ions and Temperature

| Factor | Action | Result |
|---|---|---|
| High $\ce{K+}$ (extracellular fluid $8$–$12\,\mathrm{mmol\,L^{-1}}$, 2–3 times normal) | Cardiac cells undergo partial **depolarization**, the **resting potential** is reduced, sodium channels are partly inactivated, action potential amplitude is reduced and conduction slowed | Dilated heart, weak contraction, conduction block, possibly ventricular fibrillation or cardiac arrest; intravenous potassium replacement must be slow |
| High $\ce{Ca^2+}$ | More $\ce{Ca^2+}$ enters the cell, contractile activity is strengthened but unstable | Sustained contraction of the myocardium, unstable rhythm (an isolated heart can stop in contraction) |
| Low $\ce{Ca^2+}$ | Weak contraction | Reduced cardiac function (an isolated heart stops in calcium-free solution; see Chapter 10) |
| Cooling | Ionic currents of the sinoatrial node slow, heart rate falls | Reduced cardiac function; the heart can stop in deep hypothermia, which hypothermic surgery makes use of |
| Warming (**fever**, exercise) | Ionic currents and metabolism speed up, heart rate increases (about 10 beats/min for each 1 °C rise in body temperature) | Raises cardiac function in the short term; prolonged high temperature causes metabolic disturbance and myocardial failure |

### 12.7.3. Interaction of Heart Rate and Stroke Volume

The two factors in $\mathrm{CO} = \mathrm{SV} \times \mathrm{HR}$ are not independent. When heart rate increases, diastole shortens (Section 12.3.1), filling decreases if **venous return** is limited, and stroke volume falls; at the same time a faster heart rate itself slightly strengthens contraction through the "staircase phenomenon" (the Bowditch effect: the higher the frequency, the more $\ce{Ca^2+}$ enters the cell with each beat and is not extruded in time). Within a certain range, a faster heart rate increases cardiac output; but in healthy adults, above a heart rate of about $170$–$180$ beats/min the filling time becomes too short and stroke volume falls sharply, so cardiac output actually decreases; at too slow a rate (below about 40 beats/min), even though stroke volume increases because of the long filling time, it cannot compensate for the reduction in heart rate. The increase of cardiac output in exercise does not rely on heart rate alone: sympathetic nerves simultaneously strengthen contraction and speed relaxation, and the **skeletal muscle pump** and respiration increase venous return; all four act in concert to raise cardiac output 4–5-fold.

## 12.8. Evolution and Comparative Biology

### 12.8.1. Diversity of Animal Circulatory Systems

Animals without a circulatory system: sponges, cnidarians (jellyfish, corals, hydras) and flatworms have no circulatory system, but all have structures that move fluid so that every cell is close to water. Sponges use the beating of choanocyte flagella to draw water in through the ostia and out through the central cavity; the digestive cavity (gastrovascular cavity) of cnidarians and flatworms branches throughout the body, and muscular contraction stirs the fluid in it. Flatworms are flat, and no cell is more than about $1\,\mathrm{mm}$ from the surface (the diffusion limit of Section 12.1.1). Nematodes transport materials by the flow of pseudocoelomic fluid during body movements.

Arthropods: all arthropods have open circulation. Insects have a tubular heart (dorsal vessel) running along the back, with ostia on both sides in each segment; the valves of the ostia allow hemolymph to flow only into the heart. When the heart relaxes, hemolymph enters through the ostia; when it contracts, hemolymph is pumped forward, flows into the hemocoel at the head, and returns to the abdomen among the organs. The return of hemolymph depends on pressure created by body movements and movements of the diaphragm. Many insects also have auxiliary pulsatile organs (accessory hearts) at the bases of the wings, antennae and legs. The crustacean heart is a compact muscular sac in the pericardial sinus; arteries deliver hemolymph to sinuses throughout the body, it returns through the gills to the pericardial sinus and then enters the heart through ostia, and the vascular system is quite well developed.

Annelids and mollusks: earthworms have closed circulation. The dorsal vessel contracts peristaltically from back to front, and in the anterior part of the body five pairs of contractile aortic arches ("hearts") send blood into the ventral vessel, which then branches into capillary networks in each segment. Most mollusks have open circulation, but cephalopods (squid, octopus) have a high-pressure closed circulation: a systemic heart sends blood to the whole body, and two branchial hearts pump the returning venous blood through the gills on each side, which compensates for the pressure drop as blood flows through the gill capillaries. Cephalopods are among the fastest-swimming invertebrates, and a high-pressure closed circulation suits their high metabolic rates (Chapter 15).

*Convergent evolution*: on the phylogenetic tree of animals, hearts and closed circulatory systems have arisen independently in several groups (vertebrates, cephalopods, annelids, nemerteans and others), and open circulation has also arisen several times. The phylogenetic distribution shows that the type of circulatory system is determined mainly by body size, metabolic rate and mode of oxygen supply rather than by ancestry; nevertheless, the development of cardiac muscle in different groups uses a conserved set of regulatory genes (such as $\textit{tinman}/\textit{Nkx2.5}$), and the origin of the heart may be traceable to a contractile vessel in the bilaterian ancestor ([7.5.28](/7.5.28#sec-28.7)).

### 12.8.2. The Vertebrate Heart and Pulmonary Circulation

The basic plan of the circulatory system is the same in vertebrates: one heart, arteries, capillaries and veins, but the degree of division of the heart and separation of the pulmonary circulation differ:

| Group | Heart | Circulation |
|---|---|---|
| Fishes | Sinus venosus, atrium, ventricle, and conus arteriosus (cartilaginous fishes) or bulbus arteriosus (bony fishes) in series; only one atrium and one ventricle | Single circulation: heart → gills → body → heart; blood pressure falls after blood passes through the gill capillaries, and the blood then supplies the body |
| Amphibians | Two atria and one ventricle, with a spiral valve in the conus arteriosus | Incomplete double circulation: pulmocutaneous and systemic arteries are separate; there is some mixing in the ventricle, but the spongy trabeculae of the ventricular wall and the spiral valve roughly separate oxygenated and deoxygenated blood |
| Non-crocodilian reptiles | Two atria; the ventricle has an incomplete septum (divided into several interconnected chambers) | Double circulation, with shunting between systemic and pulmonary circulations that can be regulated |
| Crocodilians | Four-chambered heart, but the two systemic aortic arches arise from the left and right ventricles, connected to each other through the foramen of Panizza | Blood of the right ventricle can bypass the lungs and enter the systemic circulation (right-to-left shunt) |
| Birds and mammals | Four-chambered heart, completely divided (arose independently in the two groups; birds retain the right aortic arch, mammals the left) | Complete double circulation |

The advantage of complete separation of the systemic and pulmonary circulations is that pulmonary pressure can be kept very low independently of the systemic circulation, the pulmonary capillary wall can be very thin without causing edema, which favors gas exchange, and systemic pressure can be very high, to meet the large flow and long-distance distribution of blood at high metabolic rates. Birds and mammals are both **endotherms**, with metabolic rates about 5–10 times those of **ectotherms** of the same size, consistent with their independent evolution of completely divided hearts.

Incomplete separation also has advantages: blood can be flexibly distributed between the systemic and pulmonary circulations according to environmental and metabolic needs. When turtles and water snakes dive, the lungs are not ventilated; pulmonary vasoconstriction makes the blood of the right ventricle bypass the lungs, through communication within the ventricle or through the systemic arches, into the systemic circulation (right-to-left shunt), avoiding repeated passage of blood through idle lungs and saving cardiac work; crocodilians when diving can also achieve this shunt through the foramen of Panizza and a toothlike valve beneath the pulmonary valve that can be closed actively. Amphibians compensate for the loss from blood mixing by skin respiration. The reptilian heart should therefore not be seen as an "incompletely evolved" transitional form but as another solution adapted to intermittent breathing.

### 12.8.3. The Heart Beats Before It Is Needed

The heart is one of the earliest organs to form and function in the vertebrate embryo. The zebrafish heart begins to beat rhythmically about one day after fertilization, but the embryo is then only a millimeter or two in size, and by the estimate of Section 12.1.1 diffusion alone is sufficient to supply oxygen; experiments also show that early zebrafish embryos without circulation (such as mutants whose hearts do not beat) obtain oxygen by diffusion normally and survive for days. If it is not for transporting oxygen, why does the heart begin to beat so early?

Studies in developmental physiology give a partial answer: the blood flow produced by the heartbeat is itself a developmental signal. When a tiny bead is implanted at the inflow or outflow tract of the zebrafish embryonic heart to reduce blood flow, heart development is disturbed: the chambers do not form normally or are misaligned, and the heart valves do not develop at all. The force of blood flow on the ends of developing vessels promotes vessel growth and sprouting and helps form the circulatory network. Endothelial cells sense the shear stress of flow through cilia and mechanosensitive channels and thereby regulate gene expression ([7.5.29](/7.5.29#sec-29.5)). These processes continue in adult animals (exercise training remodels vessels and increases capillaries, Chapter 15), showing that the circulatory system is not a set of passive pipes but a dynamic physiological system that adjusts its own structure and function to the changing needs of the tissues.

## Summary

| Topic | Key points |
|---|---|
| Why circulation is needed | Diffusion time $t = x^2/2D$: 100 µm about 5 s, 1 m about 16 years (Example 12.1.1); an organism relying on diffusion alone has a radius of no more than about 1 mm |
| Four elements of bulk flow | Pressure difference (pump), one-way valves, tubes, medium; three kinds of pump: chambered heart, skeletal muscle pump, contractile vessel |
| Open and closed | Definition 12.1.1; closed is high pressure, fast and distributable, open is low pressure and low energy cost, and the two are not mutually exclusive |
| Human circulation | Systemic and pulmonary circulations in series; 84% of blood volume in the systemic circulation (64% in veins); the high-pressure part distributes blood and the low-pressure part stores it |
| Cardiac cycle | 75 beats/min → 0.8 s; ventricular systole 0.3 s, diastole 0.5 s; a faster heart rate mainly shortens diastole (Definition 12.3.1); passive filling 80%, atrial systole 20%; valves are pressure-gated; S1 AV valve closure, S2 semilunar valve closure |
| Work | The area of the P–V loop is the external work (Definition 12.4.1); external work about 1 J per beat, kinetic energy about 1%, total energy expenditure about 6–8 J per beat, efficiency about 15% (Example 12.4.1); the heart maintains a pressure field |
| Assessment of output | $\mathrm{SV} = \mathrm{EDV} - \mathrm{ESV}$, $\mathrm{EF} = \mathrm{SV}/\mathrm{EDV}$, $\mathrm{CO} = \mathrm{SV} \times \mathrm{HR}$ about 5 L/min, cardiac index 3.0–3.5 L min⁻¹ m⁻² (Definitions 12.5.1, 12.5.2) |
| Three classes of factor | Preload (EDV), afterload (arterial pressure), contractility (ESPVR slope) (Definition 12.5.3) |
| Frank–Starling | The greater the initial length the stronger the contraction (Definition 12.6.1); titin makes passive tension high so that cardiac muscle does not reach the descending limb; length-dependent activation makes active tension rise steeply over 1.8–2.4 µm; matches left and right ventricular output |
| Nerves and ions | Vagus slows heart rate; sympathetic speeds heart rate and strengthens contraction, shifting the curve up about 2-fold; high K⁺ and low Ca²⁺ depress, high Ca²⁺ destabilizes; CO falls when heart rate exceeds about 180 beats/min |
| Evolution | Closed circulation and hearts arising independently several times; open circulation and ostia of arthropods; systemic and branchial hearts of cephalopods; vertebrates from single circulation to complete double circulation, with incomplete separation allowing shunting in diving; blood flow shapes the heart and vessels in the zebrafish embryo |

## Questions

1. An earthworm is about 5 mm in diameter, and the body wall of a hydra is only two cell layers thick. Using the diffusion time estimate, explain why the former needs a circulatory system and the latter does not.

   **Answer** From $t = x^2/2D$, with $D \approx 2 \times 10^{-9}\,\mathrm{m^2\,s^{-1}}$ for $\ce{O2}$. Every cell in the hydra body wall is only a few tens of micrometers from the water outside or in the digestive cavity; diffusing $50\,\mathrm{\mu m}$ takes about $0.6\,\mathrm{s}$, which is entirely sufficient. In the earthworm the distance from the body surface to the body axis is about $2.5\,\mathrm{mm}$, and diffusion would take about $1.6 \times 10^3\,\mathrm{s}$ (about 26 min), during which the oxygen would be used up long before it arrived; moreover, since oxygen consumption goes with volume and oxygen entry with area, a radius of 2.5 mm already exceeds the limit of about 1 mm for oxygen supply by diffusion alone. The earthworm therefore needs vessels to carry oxygen by convection to the neighborhood of the tissues of each segment, leaving only a few tens of micrometers to diffusion.

2. A person's heart rate rises from 70 beats/min to 140 beats/min. If systole shortens from 0.3 s to 0.2 s, from what to what does diastole shorten? Describe the effect on ventricular filling and coronary blood flow.

   **Answer** At 70 beats/min the cycle is $0.857\,\mathrm{s}$ and diastole about $0.557\,\mathrm{s}$; at 140 beats/min the cycle is $0.429\,\mathrm{s}$ and diastole about $0.229\,\mathrm{s}$, shortened to about 41% of the original, while systole shortens to only 67%. Passive ventricular filling takes place mainly in the rapid filling phase of early diastole, so a moderate increase of heart rate reduces filling little; when diastole shortens further the rapid filling phase is also compressed and stroke volume falls. Coronary flow to the left ventricular myocardium is perfused mainly in diastole, so shortening of diastole reduces the time available for myocardial perfusion, while the faster rate also increases myocardial oxygen consumption; patients with coronary stenosis are therefore prone to myocardial ischemia in tachycardia.

3. Using the data of Example 12.4.1, estimate the total external work done by the left ventricle in a lifetime (80 years). Approximately how heavy an object could this energy lift by 1 m?

   **Answer** About 1 J per beat, about $10^5$ beats per day, about $3 \times 10^9$ beats in a lifetime, giving a total of about $3 \times 10^9\,\mathrm{J}$. Lifting by 1 m requires $mg \times 1\,\mathrm{m}$, so $m = 3 \times 10^9/9.8 \approx 3 \times 10^8\,\mathrm{kg}$, about 300,000 tonnes. The energy actually consumed by the heart is about 6 times greater still.

4. In a patient with aortic stenosis the left ventricular systolic pressure can reach 200 mmHg while aortic pressure is normal. Draw (or describe) this change on the pressure–volume loop, and explain why the patient's myocardial oxygen consumption increases and the myocardium gradually hypertrophies.

   **Answer** The stenotic orifice needs a large pressure difference to maintain ejection, and the ejection pressure of the left ventricle is far above aortic pressure, equivalent to an increased afterload: the upper edge of the loop rises to about 200 mmHg and the end-systolic point moves up along the ESPVR; if contractility is unchanged, stroke volume decreases and the end-systolic volume increases; through the Frank–Starling mechanism (and long-term compensation) the end-diastolic volume increases to maintain stroke volume. The area of the loop (external work) increases, the triangle of the P–V area representing end-systolic potential energy also increases, and myocardial oxygen consumption rises. By **Laplace's law** the wall stress is $\propto Pr/h$; raised pressure raises the stress, and the myocytes restore wall stress to normal by adding sarcomeres in parallel (concentric hypertrophy, increased $h$), at the cost of a stiffer ventricle, impaired diastolic filling and relatively inadequate myocardial blood supply.

5. A patient who has had a heart transplant has a donor heart without nerve supply. About what is the resting heart rate? Can cardiac output still increase during exercise, and by what mechanism?

   **Answer** The denervated heart beats at the intrinsic frequency of the sinoatrial node, with a resting heart rate of about 90–110 beats/min (higher than the normal 70 beats/min because the vagal tone that predominates at rest is lost). Cardiac output can still increase during exercise, but the response is slower and smaller. At the start of exercise the skeletal muscle pump and respiration increase venous return, the end-diastolic volume increases, and the Frank–Starling mechanism increases stroke volume; after a few minutes epinephrine secreted by the adrenal medulla acts through the blood on the $\beta_1$ receptors of the heart, increasing heart rate and contractility. (After some years the hearts of some patients undergo partial sympathetic reinnervation.)

6. (Open question) Insects have open circulation yet are among the animals with the highest metabolic rates (the oxygen consumption of flight muscle can be 100 times the resting value). Does this contradict the statement that "open circulation is suitable only for low-metabolism animals"?

   **Answer** There is no contradiction; the key is the mode of oxygen transport. Insect $\ce{O2}$ is delivered in the gas phase through the tracheal system directly to the neighborhood of every cell; the diffusion coefficient of oxygen in the gas phase is about $10^4$ times that in water, so the circulatory system takes essentially no part in oxygen transport and carries only nutrients, hormones and metabolites, whose requirements are at much lower rates and are met by open circulation. The tracheal system itself also limits insect body size (limits on gas-phase diffusion distance and tube volume; giant insects appeared in the high-oxygen Paleozoic). The statement that "open circulation suits only low metabolism" therefore holds only for animals that use the circulatory system to carry oxygen; open-circulation mollusks (such as snails) have low metabolic rates, while the oxygen-transporting cephalopods evolved closed circulation.
