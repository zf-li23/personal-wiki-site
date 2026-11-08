---
title: "Course Summary: Integrative Animal Physiology"
description: "The knowledge of the individual systems reorganized by five principles that run through the whole course: the distance limit of diffusion and bulk flow, gradients and pumps, hierarchies of feedback and set points, countercurrent exchange, and scaling laws; two integrative settings: the coordination of all systems in exercise, and a comparison across groups of diving and high altitude; a table of key numerical values for each system; connections with other courses."
source_hash: b160c759164b
---

The first 46 chapters presented animal physiology system by system: cell motility and membranes (Chapters 1–4), neurons and circuits (Chapters 5–7), muscle (Chapters 8–10), then blood and circulation (Chapters 11–16), respiration (Chapters 17–20), body fluids and the kidney (Chapters 21–25), digestion and metabolism (Chapters 26–31), endocrinology and reproduction (Chapters 32–38), and finally sensation, movement, and the brain (Chapters 39–46). Going system by system makes it easy to master how each organ works, but it can make us overlook that different systems are often solving the same physical problem with the same few solutions. This chapter introduces no new material but rereads the whole course from a different direction: first five principles that run through all the systems reorganize the knowledge (Sections 47.1–47.5), then two situations that require the coordination of all systems test them (Section 47.6), and finally we give key numerical values for each system and the connections of this course to other courses (Sections 47.7 and 47.8). The numbered objects in each section link to the chapters where they first appeared.

## 47.1. The Distance Limit of Diffusion and Bulk Flow

### 47.1.1. Diffusion Works Only over Short Distances

The time needed for diffusion grows as the square of the distance (Eq. (2.1)): a small molecule needs only about $0.5\,\mathrm{ms}$ to diffuse $1\,\mu\mathrm{m}$, about $5\,\mathrm{s}$ to diffuse $100\,\mu\mathrm{m}$, and about $5\times10^4\,\mathrm{s}$ (about 14 h) to diffuse $1\,\mathrm{cm}$ (Example 12.1.1). This one fact determines almost the entire construction of the animal body:

| Scale | Is diffusion sufficient? | Example |
|---|---|---|
| Synaptic cleft ($20$–$50\,\mathrm{nm}$) | entirely sufficient, microseconds | diffusion of the transmitter is not the bottleneck of neuromuscular transmission (Example 8.4.1) |
| Cell ($10\,\mu\mathrm{m}$) | sufficient | but in skeletal muscle fibers about $100\,\mu\mathrm{m}$ in diameter $\ce{Ca^2+}$ must be released nearby from the **triads**, since diffusion from the surface membrane alone would be too slow (Example 8.5.1) |
| Tissue ($100\,\mu\mathrm{m}$) | marginal | the distance between capillaries; $P_{\ce{O2}}$ at the farthest point of tissue in the Krogh cylinder model (Definition 15.2.1) |
| Whole animal ($> 1\,\mathrm{mm}$) | insufficient | the radius of an animal supplied with oxygen by diffusion alone cannot exceed about $1\,\mathrm{mm}$ (Formula 17.2.2, Example 17.2.2) |

The design of large animals is therefore a "relay of bulk flow and diffusion": bulk flow (convection) transports quickly over long distances, and diffusion is responsible only for the last tens of micrometers. The price of bulk flow is a pump: the heart, respiratory muscles, cilia, and intestinal smooth muscle are all pumps that drive bulk flow; the price of diffusion is area: the exchange area must be large and the distance short (Fick's law, Eq. (17.2)).

### 47.1.2. The Same Solution in Each System

| System | Bulk flow part | Diffusion part | Area and distance |
|---|---|---|---|
| Circulation (Chapters 12–15) | blood flow pumped by the heart, Poiseuille's law $R \propto r^{-4}$ (Eq. (14.4)) | capillary wall and interstitial space | total capillary area about $500$–$1000\,\mathrm{m^2}$, wall thickness about $0.5\,\mu\mathrm{m}$ |
| Respiration (Chapters 17–19) | ventilation (alveolar ventilation, Eq. (17.5)) and pulmonary blood flow | respiratory membrane (Definition 19.1.1) | alveolar area about $70\,\mathrm{m^2}$, barrier about $0.2$–$0.6\,\mu\mathrm{m}$ |
| Digestion (Chapters 26–28) | peristalsis (Definition 26.5.1) and segmentation (Definition 26.8.1) propel and mix the chyme | unstirred layer at the mucosal surface and the epithelium | folds, villi, and microvilli make the area more than two orders of magnitude larger than that of a smooth tube (classical estimate about 600-fold; Example 28.1.1) |
| Kidney (Chapters 22–24) | renal blood flow and flow of tubular fluid | filtration barrier and tubular epithelium | about $180\,\mathrm{L}$ filtered per day |
| Cell motility (Chapter 2) | flow driven by cilia and flagella (Definition 2.4.1), mucociliary clearance (Definition 2.4.2) | diffusion gradients of chemical signals (Formula 2.5.1) | low Reynolds number (Eq. (2.2)) |

Another recurring problem is the diffusion of signals: hormones reach the whole body by the bulk flow of blood and then diffuse from capillaries to the target cells (Chapter 33); nerve signals instead bypass diffusion with action potentials that conduct along axons at $0.5$–$120\,\mathrm{m\,s^{-1}}$ (Definition 4.7.2). The division of labor between nerves and hormones (Examples 33.1.1 and 33.1.2) is essentially a division between "dedicated line" and "broadcast."

## 47.2. Gradients and Pumps

### 47.2.1. One Primary Pump Drives Many Secondary Flows

Substances on the two sides of the cell membrane are not in equilibrium, and what drives them across the membrane is the **electrochemical potential** difference (Eq. (3.5)): the concentration difference and the membrane potential together determine the direction. The pattern that maintains these gradients is almost the same in all systems: an ATP-consuming **primary active transport** (Definition 3.4.1) establishes an ion gradient, and a great many secondary transports (symport, antiport, ion channels) use this gradient to do work.

| System | Primary pump | Flows driven |
|---|---|---|
| All cells | $\ce{Na+}$/$\ce{K+}$-ATPase | resting potential (Eqs. (4.2), (4.4)), cell volume, $\ce{Na+}$–glucose symport (Example 3.4.2), $\ce{Na+}$–$\ce{Ca^2+}$ exchange (Example 3.4.3) |
| Nerve and muscle | $\ce{Na+}$/$\ce{K+}$-ATPase; SERCA (Example 8.6.1) | the action potential (Definition 4.6.1) uses the $\ce{Na+}$ and $\ce{K+}$ gradients; the $\ce{Ca^2+}$ gradient of the sarcoplasmic reticulum drives contraction |
| Renal tubule (Chapter 23) | basolateral $\ce{Na+}$/$\ce{K+}$-ATPase | secondary reabsorption of glucose, amino acids, and phosphate, secretion of $\ce{H+}$, water following; countercurrent multiplication in the ascending limb of the loop of Henle (Definition 24.3.1) |
| Stomach (Chapter 27) | $\ce{H+}$/$\ce{K+}$-ATPase of parietal cells | concentrates $\ce{H+}$ about $4\times10^6$-fold (a pH difference of 6.6, Example 27.3.1) while producing an alkaline tide on the blood side (Definition 27.3.1) |
| Small intestine (Chapter 28) | basolateral $\ce{Na+}$/$\ce{K+}$-ATPase | absorption of sugars and amino acids, water following the osmotic gradient |
| Thyroid (Chapter 34) | basolateral $\ce{Na+}$/$\ce{K+}$-ATPase | the sodium–iodide symporter concentrates iodide tens of fold (Definition 34.5.2, Example 34.5.1) |

The benefit of this design is economy: one pump and one energy currency can accomplish transport of all kinds through different secondary transporters; the cost is that the $\ce{Na+}$/$\ce{K+}$-ATPase consumes a large part of resting metabolism (most in the brain, Example 46.7.1).

### 47.2.2. Gases and Water Move Down Gradients

Gases and water do not depend on pumps but move passively down gradients, and physiological regulation acts on the gradients themselves:

- Gases diffuse down partial pressure gradients (Eq. (17.2)). The alveolar gas equation (Formula 17.6.1) links alveolar $P_{\ce{O2}}$ to ventilation, and the sigmoid shape of the oxygen dissociation curve (Definition 19.3.2) makes hemoglobin nearly saturated in the lung and unload a great deal in the tissues; the swim bladder uses the Root effect (Definition 19.6.1) and countercurrent exchange to "pump" $\ce{O2}$ to extremely high partial pressure, an exception in which a chemical reaction builds the gas gradient.
- Water moves down osmotic gradients (Eq. (3.8)). The hypertonic interstitium that the renal medulla builds by countercurrent multiplication lets the degree of opening of the water channels, determined by antidiuretic hormone (Definition 24.4.1), control the concentration of urine; the Starling forces in capillaries (Definition 15.2.3) balance hydrostatic against **colloid osmotic pressure** and determine filtration and reabsorption.

## 47.3. Hierarchies of Feedback and Set Points

### 47.3.1. The Common Structure of Negative Feedback

Homeostasis (Definition 1.4.1) is maintained by negative feedback (Definition 1.6.1): a sensor measures the controlled variable, compares it with the set point, and the error drives an effector to correct the deviation. Proportional feedback can only reduce a disturbance to $1/(1 + \lvert G\rvert)$ (Eq. (1.1), Definition 1.6.2), and only **integral feedback** can eliminate the steady-state error. Almost every system fits into this framework:

| Controlled variable | Sensor | Center | Effector | Gain and character |
|---|---|---|---|---|
| Arterial pressure (short-term) | baroreceptors of the carotid sinus and aortic arch | medullary cardiovascular center (Definition 16.3.1) | heart rate, myocardial contractility, vascular resistance | about $-2$ (Example 1.6.1); the baroreceptor reflex (Definition 16.3.2) resets after days |
| Arterial pressure (long-term) | the kidney itself | none | excretion of sodium and water (pressure diuresis, Definition 24.6.4) | "infinite gain" integral control (Section 16.5) |
| Core body temperature | temperature sensors of the skin and hypothalamus | hypothalamus | **shivering thermogenesis**, **nonshivering thermogenesis**, sweating, skin blood vessels, behavior | about $-33$ (Example 1.6.1); the set point (Definition 31.4.1) is raised in fever |
| Arterial $P_{\ce{CO2}}$ and pH | peripheral and central chemoreceptors (Definitions 20.4.1, 20.4.2) | medullary respiratory center | ventilation | Formula 20.4.1 |
| Plasma osmolality | hypothalamic osmoreceptors (Definition 24.4.2) | hypothalamus | antidiuretic hormone and thirst | sensitive: a change of about 1% evokes a response |
| Blood glucose | pancreatic β and α cells | none (the gland itself) | actions of insulin and glucagon on liver, muscle, and fat | Examples 35.9.1, 35.9.2 |
| Plasma $\ce{Ca^2+}$ | calcium-sensing receptor of the parathyroid (Definition 36.5.2) | none | parathyroid hormone (Definition 36.5.1) acting on bone, kidney, and gut | two time scales (Example 36.8.1) |
| Thyroid hormone, cortisol, sex hormones | hypothalamus and pituitary | hypothalamus–pituitary | tropic hormones of the anterior pituitary | long, short, and ultrashort feedback (Definition 32.7.1); HPT axis (Definition 34.6.1), HPA axis (Definition 35.3.1), HPG axis (Definition 37.2.1) |
| Muscle length and tension | muscle spindle (Definition 44.2.1), tendon organ (Definition 44.2.3) | spinal cord | $\alpha$ motor neurons | stretch reflex (Definition 44.3.1), with delay (Formula 44.3.1) |

### 47.3.2. Hierarchies Nested by Time Scale

The same controlled variable is often regulated by several feedback loops together, fast loops being responsible for immediate correction and slow loops determining the long-term level (figure). Arterial pressure is the clearest example: the **baroreceptor reflex** corrects fluctuations within seconds but resets to a new level after a few days, and the long-term blood pressure is determined by **pressure diuresis** in the kidney. Acid–base balance has three lines of defense: chemical buffering within a second, respiration within minutes, and the kidney within days (Chapter 25). Blood glucose is regulated by insulin and glucagon over minutes to hours, and cortisol and growth hormone change the responsiveness of the liver and peripheral tissues over hours to days.

![Time scales of physiological regulatory loops (orders of magnitude of the typical response times given in the chapters). Neural reflexes (blue) from milliseconds to about an hour, chemical buffering and local regulation (teal) from milliseconds to minutes, hormones (red) from seconds to weeks, renal regulation (green) from half a day to two weeks, and cell production (purple, such as regulation of red cell number by erythropoietin) from days to two months. The same controlled variable is often regulated by a fast loop and a slow loop at once: arterial pressure by the baroreceptor reflex (seconds) and pressure diuresis (days), pH by buffering, respiratory compensation, and renal acid excretion, and oxygen transport by ventilation (minutes) and red cell number (weeks).](./plots/timescales.py)

This nesting explains why the "gain" cannot be raised without limit: it takes time for the signal to travel around the loop, and the longer the delay, the more easily a high gain causes oscillation ([7.14.1](/7.14.1#sec-1.6.1)). The tremor and clonus of the stretch reflex (Formula 44.3.1), periodic breathing ([7.14.20](/7.14.20#sec-20.6.2)), and the pulsatility of hormones (Chapter 33) are all related to this; and the predictive control of the cerebellum ([7.14.45](/7.14.45#sec-45.3.4)) and the central commands to the cardiovascular and respiratory systems in exercise (the feedforward control of Definition 1.6.3) are ways of bypassing the delay.

### 47.3.3. Positive Feedback and Bistability

Positive feedback (Definition 1.6.1) makes a deviation grow ever larger, is used only when a rapid, complete "all-or-none" event is needed, and always has a mechanism that terminates it:

- The action potential: depolarization opens $\ce{Na+}$ channels and depolarizes further (Definition 4.6.1), terminated by inactivation of $\ce{Na+}$ channels and opening of $\ce{K+}$ channels.
- Blood coagulation: thrombin activates upstream clotting factors (Definition 11.4.1), and it is confined to the site of injury by the anticoagulant system and fibrinolysis (Definition 11.5.1).
- The LH surge: sustained high estradiol switches from negative to positive feedback (Definition 37.4.2) and causes ovulation.
- Parturition: uterine contraction stretches the cervix and reflexly increases the release of **oxytocin** (the Ferguson reflex, Definition 38.5.1; the bistable model of Example 38.5.1).
- The switch between sleep and wakefulness: two mutually inhibiting groups of neurons form a flip-flop ([7.14.46](/7.14.46#sec-46.4.3)).

## 47.4. Countercurrent Exchange

When two fluids flow in opposite directions and exchange some quantity between them, the efficiency of exchange is far higher than for flow in the same direction: in cocurrent flow the two fluids can reach at most the mean of the two values, whereas in countercurrent flow the outlet of the receiving stream can almost reach the inlet value of the supplying stream (Definition 17.3.1, Formula 17.3.1). This one geometrical arrangement has been used independently many times in animals:

| Location | Quantity exchanged | Result | Section |
|---|---|---|---|
| Gill lamellae of fishes | $\ce{O2}$ | arterial $P_{\ce{O2}}$ can exceed $P_{\ce{O2}}$ of the expired water, with uptake of 50%–80% | Definition 17.3.1 |
| Parabronchi of the bird lung | $\ce{O2}$, $\ce{CO2}$ | crosscurrent, with efficiency between cocurrent and countercurrent | Definition 17.7.1 |
| Loop of Henle in the renal medulla | solute (countercurrent multiplication) and water | a small single effect is amplified into a gradient of $300 \to 1200\,\mathrm{mOsm\,L^{-1}}$ from cortex to papilla | Definitions 24.3.1, 24.7.1 |
| Vasa recta | solute and water (countercurrent exchange) | supplies the medulla with blood without washing out the gradient | Chapter 24 |
| Arteries and veins of limbs, fins, and gills | heat | flippers of whales and legs of wading birds conserve core heat; tunas and mackerel sharks keep their muscles warm | Definition 31.6.5 |
| **Rete mirabile** of the swim bladder | $\ce{O2}$ | together with the Root effect, raises the $\ce{O2}$ partial pressure in the swim bladder to tens or even a hundred atmospheres | Definition 19.6.1 |
| Vessels of intestinal villi | $\ce{O2}$ and absorbed substances | the villus tip is relatively hypoxic (a cost) | Chapter 28 |
| Placenta | $\ce{O2}$ and nutrients | the labyrinthine placenta of the rabbit is countercurrent, the human is pool-type, and the sheep is close to cocurrent and crosscurrent | Chapter 38 |

The common rule is that, for countercurrent exchange to work, the contact between the two streams must be long enough, the exchange fast enough, and the flow slow enough; for what is conserved for some purpose (heat, a solute gradient), the countercurrent structure at the same time hinders its rapid change, and so it is often accompanied by bypasses (arteriovenous anastomoses, regulation of medullary blood flow).

## 47.5. Scaling Laws

### 47.5.1. Volume as $M$, Rate as $M^{-1/4}$

When mammals of different sizes are compared, many physiological quantities vary as power laws of body mass $M$ (**allometry**):

- Volumes and organ sizes are roughly proportional to $M$: blood volume (about 7% of body mass), heart mass (about 0.6%), lung volume;
- Metabolic rate grows as $M^{3/4}$ (**Kleiber's law**, Definition 30.3.2), so the metabolic rate per unit body mass falls as $M^{-1/4}$: a mouse consumes about 20 times as much oxygen per gram of tissue as an elephant;
- Then all rates "supplied in proportion to the metabolic rate per unit body mass" also vary as $M^{-1/4}$: heart rate (about $600\,\mathrm{min^{-1}}$ in a mouse, about $30\,\mathrm{min^{-1}}$ in an elephant), respiratory frequency, and circulation time of the blood;
- Lifespan grows about as $M^{1/4}$ (measured about $M^{0.2}$).

Multiplying the two, the number of heartbeats in a lifetime is about $10^9$, almost independent of body size (figure). Heart mass and blood volume are both proportional to $M$ and **stroke volume** is also proportional to $M$, so **cardiac output** grows like metabolic rate as $M^{3/4}$, which is achieved through the $M^{-1/4}$ of the heart rate.

![Allometric scaling of mammalian physiological quantities ($Y = aM^b$, coefficients from classical compilations, Schmidt-Nielsen 1984; Calder 1984). A: each quantity divided by its value for a $1\,\mathrm{kg}$ animal, as straight lines on logarithmic axes: lung volume, blood volume, and heart mass are about proportional to $M$, basal metabolic rate and brain mass about $M^{3/4}$, lifespan $M^{0.2}$, and metabolic rate per unit body mass, heart rate, and respiratory frequency $M^{-1/4}$. B: number of heartbeats in a lifetime ($241\,M^{-0.25}\,\mathrm{min^{-1}}$ times the maximum lifespan $11.8\,M^{0.20}$ years) is about $10^9$, and the number of breaths in a lifetime about $2$–$5\times10^8$; over the range from mouse to elephant they differ by only about a factor of 2.](./plots/scaling.py)

### 47.5.2. Scaling in the Chapters

| Quantity | Scaling | Consequence | Section |
|---|---|---|---|
| Diffusion time | $\propto L^2$ | animals larger than about $1\,\mathrm{mm}$ need circulatory and respiratory organs | Eq. (2.1), Formula 17.2.2 |
| Reynolds number of swimming | $\propto vL$ | cells and sperm move in a world dominated by viscosity, and fish in a world dominated by inertia | Eq. (2.2) |
| Muscle force and body weight | force $\propto L^2$, weight $\propto L^3$ | specific muscle force is conserved; geometrically similar animals jump equally high, but small animals need elastic energy storage (Example 9.11.1) | Definition 9.10.2, Section 9.11 |
| Metabolic rate | $\propto M^{3/4}$ | small animals need more food and higher heart rate and ventilation; the extreme metabolism of hummingbirds (Example 30.6.1) | Definition 30.3.2 |
| Heat loss | surface area $\propto M^{2/3}$ | Bergmann's rule and Allen's rule (Definition 31.6.7); small **endotherms** need torpor (Definition 31.6.6) | Chapter 31 |
| Oxygen dissociation curve | higher $P_{50}$ in small animals | oxygen is unloaded more readily in the tissues, adapted to the high oxygen consumption per unit body mass | Chapter 19 |
| Relative medullary thickness | greatest in small desert rodents | more concentrated urine, adapted to water scarcity (Definition 24.7.1) | Chapter 24 |
| Brain mass | about $\propto M^{0.7}$ within mammals | the encephalization quotient compares the deviation from this line (Definition 46.8.2) | Chapter 46 |

Scaling laws are not "laws": the exponents are statistical fits across species (regression as in [3.3](/3.3)), and the residuals contain information about ecology and phylogeny (such as the brains of dolphins, the longevity of bats). But they give the null hypothesis of comparative physiology: to ask whether some quantity of a species is special, one must first see whether it deviates from the value expected for its body size.

## 47.6. Two Integrative Settings

### 47.6.1. Exercise

From rest to vigorous exercise, the oxygen consumption of skeletal muscle can increase more than 50-fold, and that of the whole body from about $0.25$ to $3$–$4\,\mathrm{L\,min^{-1}}$ (up to $5$–$6\,\mathrm{L\,min^{-1}}$ in endurance athletes). Every step of oxygen from air to mitochondria must increase at the same time to meet the demand (Fick principle, Definition 15.2.2):

1. Muscle: **motor units** are recruited in order by the size principle (Definition 9.8.2); energy comes first from ATP and phosphocreatine, after a few seconds from anaerobic glycolysis, and in sustained exercise from oxidative phosphorylation (Chapter 9).
2. Ventilation: central commands and afferents from muscle make ventilation increase abruptly at the onset of exercise (feedforward), after which chemoreceptors fine-tune it so that arterial $P_{\ce{O2}}$, $P_{\ce{CO2}}$, and pH hardly change ([7.14.20](/7.14.20#sec-20.6.1)); above the ventilatory threshold, buffering of lactate makes ventilation increase more than oxygen consumption.
3. Gas exchange: recruitment of pulmonary capillaries increases the diffusing capacity of the lung about 3-fold (Definition 19.1.2), the transit time of blood in the lung shortens, but $\ce{O2}$ still reaches equilibrium before the end of the transit (Definition 19.2.1).
4. Circulation: cardiac output rises from about $5$ to $20$–$25\,\mathrm{L\,min^{-1}}$, through an increase of heart rate (sympathetic activation, vagal withdrawal) and of stroke volume (increased **venous return**, the Frank–Starling mechanism, Definition 12.6.1); the resistance of the working muscle falls greatly through metabolic vasodilation, the vessels of the viscera and kidney constrict, and blood flow is redistributed to muscle ([7.14.16](/7.14.16#sec-16.7.1)).
5. Oxygen unloading: the rise of $P_{\ce{CO2}}$, $\ce{H+}$, and temperature in muscle shifts the oxygen dissociation curve to the right (**Bohr effect**), and the oxygen extraction of muscle (Definition 15.2.2) rises from about 25% to over 80%.
6. Metabolic fuels: the **sympathoadrenal system** and glucagon mobilize liver glycogen and fat, insulin falls, and glucose uptake by muscle increases because of contraction itself (independent of insulin); blood glucose stays essentially unchanged (Chapters 29, 35).
7. Body temperature: the efficiency of exercise is about 20%–25%, and the remaining 75% or more becomes heat, so heat production can increase more than 10-fold. Skin vasodilation and sweating dissipate the heat (Eq. (31.1)), which in turn competes with muscle for cardiac output and loses water and salt through sweating (Chapter 31).
8. Body fluids and kidney: renal blood flow and **glomerular filtration rate** fall, and antidiuretic hormone and **aldosterone** increase, conserving water and sodium (Chapter 24).

Which step limits maximal oxygen consumption? For whole-body exercise in healthy people, the main limit is cardiac output (the delivery of the circulation), not diffusion in the lung or the capacity of muscle mitochondria; but at high altitude, in lung disease, or in anemia, other steps become the bottleneck. This is a general property of a cascade: every step must increase at the same time, and the step that is hardest to increase determines the upper limit.

### 47.6.2. Diving and High Altitude

Diving and high altitude are both settings of insufficient oxygen supply, but the time scales and solutions differ, and comparing them ties together the knowledge of circulation, respiration, and blood.

| | Diving (breath-hold) | High altitude (hypoxic environment) |
|---|---|---|
| Problem | no new $\ce{O2}$ enters, limited stores; $\ce{CO2}$ accumulates | inspired $P_{\ce{O2}}$ falls (Chapter 17), arterial $P_{\ce{O2}}$ falls |
| Time scale | minutes to an hour or two | hours (acute) to generations (genetic adaptation) |
| Circulation | the diving reflex (Definition 16.8.1): bradycardia, peripheral vessels closed, blood flow preserved only to brain and heart; total peripheral resistance rises and cardiac output falls, so arterial pressure is maintained (the logic of pressure control, Example 16.1.1) | acutely heart rate and cardiac output increase; hypoxic pulmonary vasoconstriction (Definition 18.4.2) raises pulmonary arterial pressure and can cause high-altitude pulmonary edema |
| Respiration | breathing suppressed, low sensitivity to $\ce{CO2}$; seals exhale before diving, avoiding decompression sickness ([7.14.20](/7.14.20#sec-20.7.4)) | hypoxic ventilatory response, limited by **respiratory alkalosis**; after days the kidney excretes $\ce{HCO3-}$ and ventilatory acclimatization follows ([7.14.20](/7.14.20#sec-20.6.3)) |
| Blood and stores | large blood volume, high **hematocrit**, much myoglobin, spleen contraction releases red cells; oxygen is stored mainly in blood and muscle | erythropoietin (Definition 11.2.3) raises hemoglobin within weeks; 2,3-BPG increases |
| Metabolism | within the aerobic dive limit mainly aerobic metabolism; beyond it, tissues with blood flow shut off use anaerobic metabolism, and lactate enters the blood only after surfacing | changes of tissue capillary density and mitochondrial efficiency |
| Comparison across groups | Weddell seals, whales, penguins; the human diving reflex is weak | the *EPAS1* allele of Tibetans suppresses excessive erythrocytosis, relying on more blood flow and NO; Andeans rely mainly on high hemoglobin; the hemoglobins of the bar-headed goose, Andean goose, and llama have high oxygen affinity (Chapter 19); yaks and pikas have very weak hypoxic pulmonary vasoconstriction |

Both settings show the same principle: when oxygen is insufficient, the organism first secures the brain and heart, second trades time for space (temporarily tolerating a local oxygen debt in diving), and only last, on longer time scales, changes the oxygen transport capacity (red cells, the affinity of hemoglobin, genes).

## 47.7. Key Numerical Values of Each System

The following are typical resting values for an adult (body mass about $70\,\mathrm{kg}$), for use in estimates; the specific ranges and sources are in the chapters. Blood pressure and gas partial pressures are written in mmHg by clinical convention ($1\,\mathrm{mmHg} \approx 0.133\,\mathrm{kPa}$).

| System | Quantity | Typical value |
|---|---|---|
| Body fluids (Chapter 21) | total body water, intracellular fluid, extracellular fluid | about 60%, 40%, 20% of body mass (about $42$, $28$, $14\,\mathrm{L}$) |
| | plasma osmolality | about $290\,\mathrm{mOsm\,kg^{-1}}$ |
| | plasma $\ce{Na+}$, $\ce{K+}$, $\ce{Ca^2+}$ (total) | $140$, $4$, $2.4\,\mathrm{mmol\,L^{-1}}$ |
| Membrane and nerve (Chapters 4–5) | resting potential | about $-70\,\mathrm{mV}$ in nerve, about $-90\,\mathrm{mV}$ in skeletal muscle |
| | action potential duration, conduction velocity | about $1\,\mathrm{ms}$; $0.5$–$120\,\mathrm{m\,s^{-1}}$ |
| | synaptic delay | about $0.5\,\mathrm{ms}$ |
| Blood (Chapter 11) | blood volume, hematocrit | about $5\,\mathrm{L}$ (7% of body mass); about 0.45 in men, about 0.40 in women |
| | hemoglobin, red cell lifespan | about $150\,\mathrm{g\,L^{-1}}$; about 120 days |
| Circulation (Chapters 12–16) | heart rate, stroke volume, cardiac output | about $70\,\mathrm{min^{-1}}$, $70\,\mathrm{mL}$, $5\,\mathrm{L\,min^{-1}}$ |
| | arterial pressure, mean arterial pressure | about $120/80\,\mathrm{mmHg}$ ($16/10.7\,\mathrm{kPa}$), about $93\,\mathrm{mmHg}$ |
| | central venous pressure | about $0\,\mathrm{mmHg}$ ($-3$ to $+5\,\mathrm{mmHg}$) |
| Respiration (Chapters 17–20) | tidal volume, respiratory frequency, alveolar ventilation | about $500\,\mathrm{mL}$, $12\,\mathrm{min^{-1}}$, $4.2\,\mathrm{L\,min^{-1}}$ |
| | oxygen consumption, $\ce{CO2}$ production | about $250$, $200\,\mathrm{mL\,min^{-1}}$ |
| | arterial $P_{\ce{O2}}$, $P_{\ce{CO2}}$ | about $100$, $40\,\mathrm{mmHg}$ ($13.3$, $5.3\,\mathrm{kPa}$) |
| Kidney (Chapters 22–24) | renal blood flow, glomerular filtration rate, filtration fraction | about $1.1\,\mathrm{L\,min^{-1}}$, $125\,\mathrm{mL\,min^{-1}}$ ($180\,\mathrm{L\,d^{-1}}$), about 0.2 |
| | urine volume, urine osmolality | about $1.5\,\mathrm{L\,d^{-1}}$; $50$–$1200\,\mathrm{mOsm\,L^{-1}}$ |
| Acid–base (Chapter 25) | arterial pH, $\ce{HCO3-}$ | $7.40$ ($7.35$–$7.45$), $24\,\mathrm{mmol\,L^{-1}}$ |
| | daily fixed acid | about $1\,\mathrm{mmol\,kg^{-1}\,d^{-1}}$ |
| Digestion (Chapters 26–28) | fluid entering the small intestine daily, fecal water | about $8$–$9\,\mathrm{L}$, about $0.1\,\mathrm{L}$ |
| Metabolism and temperature (Chapters 29–31) | basal metabolism | about $1700\,\mathrm{kcal\,d^{-1}}$ (about $80\,\mathrm{W}$) |
| | fasting blood glucose | about $4$–$6\,\mathrm{mmol\,L^{-1}}$ |
| | core temperature | about $37\,{}^\circ\mathrm{C}$, with a daily fluctuation of about $0.5\,{}^\circ\mathrm{C}$ |
| Brain (Chapter 46) | mass, blood flow, oxygen consumption, power | about $1.4\,\mathrm{kg}$; about $0.7\,\mathrm{L\,min^{-1}}$; 20% of resting oxygen consumption; about $16$–$20\,\mathrm{W}$ |
| | number of neurons | about $8.6\times10^{10}$ in the whole brain, of which the cerebellum has about 80% and the cerebral cortex about 19% |

## 47.8. Connections with Other Courses

Animal physiology lies between courses at the cellular level and courses at the level of individuals and populations: it borrows mechanisms from the former and provides functional explanations for the latter.

| Course | What this course uses or provides |
|---|---|
| Mathematics (2.x) and statistics (3.x) | ordinary differential equations describe feedback and dynamics ([2.4](/2.4): one- and two-compartment models of hormones, **rate models**, the **two-process model**); partial differential equations describe diffusion, cables, and countercurrent flow ([2.5](/2.5)); the Poisson distribution describes **quantal release** ([3.1](/3.1)); regression fits allometric scaling ([3.3](/3.3)) |
| Physics (5.x) | fluid mechanics (Poiseuille, Reynolds number, **Laplace's law**), thermal physics (the four routes of heat exchange), electricity (the RC circuit of the membrane), optics (image formation in the eye), acoustics (**impedance matching**) ([5](/5)) |
| Chemistry (6.x) | thermodynamics (electrochemical potential, osmotic pressure, free energy of ATP), acids, bases, and buffers ([6](/6)) |
| Biochemistry ([7.1](/7.1)) | metabolic pathways, oxygen binding of hemoglobin and the Hill equation, signal transduction and second messengers; this course treats only flows and feedback between organs |
| Cell biology ([7.3](/7.3)) | membrane transport, cytoskeleton and molecular motors, cell junctions; this course treats their combination in tissues and organs |
| Developmental biology ([7.5](/7.5)) | development of the organs, gametogenesis and fertilization, sex determination |
| Biophysics ([7.6](/7.6)) | Nernst–Planck, GHK, the cable equation and the Hodgkin–Huxley model, cross-bridges and the force–velocity curve, physical limits of sensation |
| Systems biology ([7.9](/7.9)) | general theory of feedback, bistability, and oscillation (the LH surge, the sleep switch, the molecular clock, CPGs) |
| Evolutionary biology ([7.10](/7.10)) | convergence and homology in the "Evolution and Comparative Aspects" of the chapters (origin of **endothermy**, genes of high-altitude adaptation, vocal learning) |
| Immunology ([7.15](/7.15)) | the physiology of leukocytes, inflammation, and the lymphatic system is in this course, the mechanisms of immune recognition in immunology |
| Computational neuroscience ([7.16](/7.16)) | this course gives the physiological facts and phenomenological models of the action potential, synapse, circuits, sensory coding, the cerebellum, and basal ganglia, and the computational theory is in computational neuroscience |
| Zoology ([7.17](/7.17)), ethology ([7.18](/7.18)), ecology ([7.19](/7.19)) | comparison of the circulation, respiration, excretion, and nervous systems of the groups; behavior of sensation, feeding, reproduction, and sleep; the ecological significance of metabolic scaling, thermal ecology, and **osmoregulation** |

## Summary

| Principle | Core claim | Representative numbered objects |
|---|---|---|
| Diffusion and bulk flow | diffusion time $\propto L^2$, beyond about $1\,\mathrm{mm}$ bulk flow must relay; exchange needs large area and short distance | Eq. (2.1), Formula 17.2.2, Definition 15.2.1, Eq. (14.4) |
| Gradients and pumps | one primary pump ($\ce{Na+}$/$\ce{K+}$-ATPase, $\ce{H+}$-ATPase) establishes a gradient that many secondary transports use; gases and water move passively down gradients | Definition 3.4.1, Example 3.4.2, Example 27.3.1, Definition 24.3.1 |
| Feedback | residual error of negative feedback $\Delta_0/(1 + \lvert G\rvert)$; fast loops correct, slow loops set the level; delay limits gain; positive feedback for all-or-none events | Definition 1.6.1, Definition 1.6.2, Eq. (1.1), Definition 16.3.2, Definition 24.6.4, Formula 44.3.1, Definition 37.4.2 |
| Countercurrent | opposed flow makes exchange far more efficient than cocurrent flow, arising independently in gills, kidney, heat exchange, swim bladder, and placenta | Definition 17.3.1, Formula 17.3.1, Definition 24.3.1, Definition 31.6.5 |
| Scaling | volume $\propto M$, metabolism $\propto M^{3/4}$, rates $\propto M^{-1/4}$; about $10^9$ heartbeats in a lifetime | Definition 30.3.2, Definition 9.10.2, Definition 46.8.2 |
| Exercise | every step from air to mitochondria increases at the same time, and cardiac output is usually the limit of maximal oxygen consumption | Definition 15.2.2, Definition 12.6.1, Definition 9.8.2 |
| Diving and high altitude | first protect brain and heart, then trade time for space, and finally change transport capacity on long time scales | Definition 16.8.1, Definition 18.4.2, Definition 11.2.3 |

## Questions

1. Use at least three of the five principles of this chapter to explain why insects do not grow as large as dogs.

   **Answer** Key points: (1) Diffusion and bulk flow: the tracheal system of insects (Definition 17.7.2) delivers air directly to the tissues, with the last stretch by diffusion; the length of the tracheae increases with body length and the diffusion time is $\propto L^2$, so large insects need active ventilation, and the fraction of volume occupied by tracheae increases rapidly with body size, crowding out the space of tissue. The giant dragonfly-like Meganeura with a wingspan of about $70\,\mathrm{cm}$ appeared in the Carboniferous when the atmospheric $\ce{O2}$ content was higher, consistent with this limit. (2) Scaling: the force of the exoskeleton and muscles is $\propto L^2$ and body weight is $\propto L^3$, so as body size increases the exoskeleton must be thicker to support the weight, and the soft period at molting is also more dangerous. (3) Circulation: insects have an open circulatory system (Definition 12.1.1) in which hemolymph pressure is low and flow slow, and the hemolymph does not carry oxygen, so it can hardly support tissues of large size and high metabolic rate. The limits thus come mainly from oxygen delivery and mechanics, not from a single factor.

2. A person runs at sea level at $80\%$ of maximal oxygen consumption. Point out, among the steps of oxygen from air to muscle mitochondria, which have had their "gain" raised, which feedback keeps the arterial blood gases unchanged, and why he cannot maintain the same speed on a plateau at 4000 m.

   **Answer** The steps that are raised: ventilation (feedforward central command plus fine tuning by chemoreflexes), diffusing capacity of the lung (recruitment of capillaries), cardiac output (heart rate and stroke volume), blood flow of muscle (metabolic vasodilation and redistribution of flow), and oxygen extraction of muscle (Bohr effect and lowered tissue $P_{\ce{O2}}$). Arterial $P_{\ce{O2}}$ and $P_{\ce{CO2}}$ are kept nearly constant by the feedback of the **chemoreceptor reflex** on the residual error (Formula 20.4.1). At 4000 m, the inspired $P_{\ce{O2}}$ is only about 60% of that at sea level, alveolar and arterial $P_{\ce{O2}}$ fall onto the steep part of the oxygen dissociation curve, and arterial oxygen content falls; the transit time of blood in the lung shortens during exercise, and the exchange of $\ce{O2}$ changes from perfusion-limited to diffusion-limited (Definition 19.2.1), lowering arterial oxygen further. The upper limit of cardiac output is unchanged, so the maximal oxygen delivery given by the Fick principle (Definition 15.2.2) falls, maximal oxygen consumption falls with it, and the former 80% speed now exceeds the new maximum.

3. Arterial pressure is regulated both by the baroreceptor reflex and by pressure diuresis in the kidney. If a person's renal sodium excretion is impaired (less sodium is excreted at any pressure), what will happen to his blood pressure over minutes, days, and weeks? Can the baroreceptor reflex correct it?

   **Answer** Over minutes there is no obvious change, because a change in sodium excretion affects blood volume only slowly. Over days sodium and water are retained in the body, blood volume and venous return increase, and cardiac output and arterial pressure rise; the baroreceptor reflex opposes this rise (gain about $-2$, which can only reduce the deviation to about one third) but resets to the new level within days. After weeks, because pressure diuresis in the kidney is integral control ("infinite gain"), arterial pressure keeps rising until, at the new, higher pressure, sodium excretion again equals intake, and the long-term blood pressure is set at this higher level; the baroreceptor reflex cannot correct the long-term blood pressure and is responsible only for short-term fluctuations. This is why many forms of hypertension are thought to originate in the kidney (Section 16.5, Definition 24.6.4).

4. Use scaling laws to estimate the ratio of the heart rates of a $25\,\mathrm{g}$ mouse and a $70\,\mathrm{kg}$ human, and the ratio of their **basal metabolic rates** per unit body mass. Why is the $P_{50}$ of the oxygen dissociation curve of the mouse higher?

   **Answer** Heart rate $\propto M^{-1/4}$: $(0.025/70)^{-1/4} = (2800)^{1/4} \approx 7.3$, so with about $70\,\mathrm{min^{-1}}$ in a human the mouse has about $500\,\mathrm{min^{-1}}$ (measured about $500$–$600$). The metabolic rate per unit body mass also goes as $M^{-1/4}$, and the ratio is likewise about 7. The tissue of the mouse consumes about 7 times as much oxygen per gram as that of a human and needs to unload a great deal at a higher tissue $P_{\ce{O2}}$ to maintain the diffusion gradient from capillary to mitochondria; a higher $P_{50}$ (lower oxygen affinity) lets hemoglobin release $\ce{O2}$ more readily in the tissues, while the mouse lives in sea-level air and its hemoglobin can still become nearly saturated in the lung.

5. (Open question) Choose from the whole course the example that you think best shows that "physiology is a quantitative discipline," and explain how a quantitative argument led to a conclusion that qualitative description alone could not give.

   **Answer** Suggested approach: many examples are possible, and the key is to show that a quantitative estimate overturned or established some qualitative view. For example, Harvey's argument (Example 1.2.1): estimating from stroke volume and heart rate, the heart pumps in an hour a volume of blood far exceeding the body weight, so blood cannot be continually produced from food and must circulate; this conclusion came from an order of magnitude and did not depend on any observation of the vessels. Or the square law of diffusion (Eq. (2.1)): a simple order-of-magnitude estimate explains why all animals larger than about $1\,\mathrm{mm}$ have a circulatory system and why capillary spacing is within about $100\,\mu\mathrm{m}$; the estimate of the energy cost and volume of replacing hormones with nerves (Examples 33.1.1 and 33.1.2) shows the economy of hormonal broadcast; and the two-process model (Eq. (46.1)) explains quantitatively why a night of sleep deprivation needs only an hour or two of extra sleep to recover. The answer should give the key numerical values of the estimate and say to which assumptions the conclusion is sensitive.
