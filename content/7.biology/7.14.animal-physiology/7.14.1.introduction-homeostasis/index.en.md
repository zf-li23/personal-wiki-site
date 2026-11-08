---
title: "Introduction: The Internal Environment, Homeostasis and Physiological Control"
description: What physiology studies; from Hippocrates and Galen to Harvey's quantitative argument and on to Bernard's internal environment and Cannon's homeostasis; the fluid compartments and the composition of the internal environment; neural, humoral and autoregulation; negative feedback and feedback gain, integral control and delay, positive feedback and vicious cycles, feedforward control; the cell cycle as a complex control system; conformers and regulators, and the evolution of animals from open body fluids to a barrier-protected internal environment.
source_hash: d337f5ae1e57
---

Physiology asks how living organisms work: how the heart can beat continuously for several billion cycles, how the kidney processes $180\,\mathrm{L}$ of filtrate into $1.5\,\mathrm{L}$ of urine in a day, how a nerve fiber generates and transmits an electrical signal within a millisecond. These functions belong to different systems, yet they serve a single goal: to keep every cell of the body immersed in a liquid environment whose composition, temperature and pressure are almost constant. This chapter introduces three concepts that run through the whole course: the internal environment (the extracellular fluid in which cells live), homeostasis (the relative constancy of the physical and chemical properties of the internal environment), and the physiological regulation that maintains it (neural, humoral and autoregulation, and the control modes of negative feedback, positive feedback and feedforward).

The remaining chapters proceed system by system. Cells and membranes (Chapters 2–4) underlie every function; nerve and muscle (Chapters 5–10) supply fast information transfer and mechanical power; circulation, respiration, the urinary system, digestion and metabolism (Chapters 11–31) are responsible for transport, gas exchange, body fluids and acid–base balance, and nutrition and energy; the endocrine and reproductive systems (Chapters 32–38) provide slow, widespread regulation; sensation, movement and the higher functions of the brain (Chapters 39–46) connect the organism to the outside world. The mathematics of control (feedback, bistability and oscillation) is treated systematically in systems biology ([7.9.16](/7.9.16)); this chapter covers only its physiological meaning. For the basics of ordinary differential equations, see [2.4](/2.4).

## 1.1. What Physiology Studies

**Definition 1.1.1 (Physiology)** **Physiology** is the science that studies how organisms and their parts (organs, tissues, cells and molecules) carry out the chemical and physical functions that sustain life, and how these functions are regulated and coordinated with one another.

Physiological questions operate at four levels: function (what is done), principle (which physical and chemical laws apply), mechanism (which structures and molecules implement it) and regulation (how it changes with demand). The subject spans every level from molecules to the whole organism, and what is characteristic of physiology is that it links them: the gating properties of a channel protein determine the shape of an **action potential**, the conduction velocity of the action potential determines the latency of a reflex, and the reflex determines whether an animal escapes a predator. "Form fits function" is the thread that runs through the whole subject: the wall of the **alveolus** is only $0.6\,\mu\mathrm{m}$ thick to favor diffusion, and the brush border of renal tubule cells enlarges the absorptive area several tens of times; both can be understood quantitatively from the functional requirement.

Medical physiology, with the human body as its principal subject, is the main thread of this course. But since Aristotle, comparing different animals has been a basic method for understanding function: the same problem (obtaining oxygen, excreting nitrogenous waste, maintaining body temperature) has different solutions in different groups, and comparing these solutions reveals which constraints are physical and which are historical. For this reason the last section of every chapter is "Evolution and Comparison".

By subject, physiological experiments are divided into in vitro experiments (organs, tissues or cells are removed from the body and studied under controlled conditions, as in the isolated frog heart, brain slices or **patch clamp**) and in vivo experiments (performed on intact animals, closer to the physiological state but harder to control). In vivo experiments are further divided into acute experiments (the effect of one treatment is observed under anesthesia) and chronic experiments (the animal recovers after surgery and is observed over a long period, as with Pavlov's dogs with gastric fistulas). Modern physiology also makes extensive use of molecular tools such as gene knockout and optogenetics, and of mathematical models: a model can test whether a proposed mechanism is quantitatively sufficient to explain the observed function.

## 1.2. A Brief History of Physiology

### 1.2.1. Observation and Speculation

The school of Hippocrates (c. 460–c. 370 BCE) in ancient Greece regarded disease as a natural process rather than divine will, proposed the "four humors" of blood, phlegm, yellow bile and black bile, held that health is a balance of the humors, and emphasized the influence of lifestyle on health. Aristotle (384–322 BCE) dissected and compared a great many animals, understood organs teleologically (structure exists for the sake of function), and held the heart to be the source of body heat and the center of life. In Roman times Galen (129–c. 216) performed many animal experiments: ligating the ureter showed that urine is produced by the kidney, and cutting the recurrent laryngeal nerve silenced the animal. His doctrine of three "spirits" (the natural spirit of the liver governing nutrition and growth, the vital spirit of the heart governing vitality and body heat, the animal spirit of the brain governing sensation and movement) dominated Western medicine for more than a thousand years.

Traditional Chinese medicine (the *Huangdi Neijing*, the *Nanjing*, the *Shanghan Zabing Lun*, the *Shennong Bencao Jing*, and Bian Que's four diagnostic methods of looking, listening, asking and feeling the pulse) built a systematic and workable theory of bodily function without anatomy or experiment, and is good at describing integrated regulation and functional imbalance. It did not develop into physiology in the modern sense, because of the limits of its methodology: the theory lacked experimental intervention and falsifiability, so it could hardly be systematically revised or discarded; concepts such as "qi" and "meridians" resist quantification and so could not enter a cumulative quantitative science; and it was better at describing states than explaining causes.

Early physiology relied mainly on direct observation and speculative reasoning, and a considerable part of its knowledge was mixed with subjective judgment and lacked empirical data from precise measurement. This began to change with the refinement of anatomy (Vesalius's *De humani corporis fabrica* of 1543 corrected many errors that Galen had drawn from animal dissection) and the emergence of quantitative argument.

### 1.2.2. The Birth of Experimental Physiology

William Harvey's (1578–1657) *De motu cordis* of 1628 marks the point at which physiology became an experimental science. His key argument was quantitative.

**Example 1.2.1 (Harvey's Argument for the Circulation of the Blood)** Galen's doctrine held that blood is continually made from food in the liver and flows through the veins to be consumed throughout the body. Harvey took a conservative estimate: each beat of the ventricle ejects about half an ounce (about $14\,\mathrm{g}$) of blood, and the heart beats more than a thousand times in half an hour, so more than $14\,\mathrm{kg}$ of blood passes out of the heart in half an hour, more than the total amount of blood in the body and far more than the food eaten in that time. Blood cannot be made and consumed so fast; it must be the same blood circulating again and again. With modern numbers, a **stroke volume** of about $70\,\mathrm{mL}$ and a heart rate of about 70 beats per minute give a **cardiac output** of about $5\,\mathrm{L\,min^{-1}}$, or about $7000\,\mathrm{L}$ per day, more than a thousand times the blood volume (about $5\,\mathrm{L}$).

:::

Harvey also used ligation experiments to show that the venous valves allow blood to flow only toward the heart. He could not see the connections between arteries and veins; in 1661 Marcello Malpighi saw capillaries in the frog lung with a microscope, supplying the last link of the circulation. The microscope also revealed the fine structure of a great many organs, the first typical example of instruments driving physiology forward.

Seventeenth-century Europe was a time of flowering: Descartes explained reflexes mechanistically, Borelli analyzed muscles and movement with mechanics (*De motu animalium*, 1680), Steno studied the anatomy of muscles and glands, Glisson proposed the "irritability" of tissues, and Swammerdam studied muscle contraction in isolated nerve–muscle preparations of insects and frogs. Newton's mechanics supplied a theoretical paradigm for the idea that living processes obey the same laws as inanimate matter.

### 1.2.3. Mechanism, Chemistry and the Cell

In the eighteenth century La Mettrie argued that "man is a machine", in conflict with religion and traditional philosophy; the debate between mechanism and vitalism ran through the eighteenth and nineteenth centuries. In chemistry, Sylvius explained digestion by acid–base fermentation, while Stahl insisted that life has an immaterial force; Priestley and Scheele discovered oxygen, and Lavoisier and Laplace used an ice calorimeter to measure the heat production and $\ce{CO2}$ output of guinea pigs, showing that respiration is a slow combustion (about 1780). In 1828 Wöhler synthesized urea from inorganic substances, shaking the belief that organic substances can be produced only by a vital force.

Nineteenth-century physiology rested on two "basic units". Bichat (1771–1802) proposed that organs are composed of several kinds of tissue, a tissue being a collection of cells of similar structure and function; Schleiden (1838, plants) and Schwann (1839, animals) established the **cell theory**. Physical methods entered physiology: du Bois-Reymond recorded the electrical activity of nerves, and Helmholtz in 1850 measured the conduction velocity of the frog nerve at about $27\,\mathrm{m\,s^{-1}}$, showing that the nerve signal is not an instantaneous "spirit" but a measurable physical process (Chapter 4).

### 1.2.4. The Internal Environment and Homeostasis

Claude Bernard (1813–1878) proposed that the cells of higher animals do not live in the external environment but in the organism's own fluid environment, the "milieu intérieur", and wrote that "the constancy of the internal environment is the condition for a free and independent life". Walter B. Cannon (1871–1945) coined the term "homeostasis" in 1926 and in *The Wisdom of the Body* (1932) gave a systematic account of the regulatory mechanisms that maintain it, especially the role of the sympathetic–adrenal system in stress.

Twentieth-century physiology developed in two directions. One went down to the molecular level: Bayliss and Starling discovered secretin (1902), establishing the concept of the hormone; Hodgkin and Huxley explained the action potential with the **voltage clamp** (1952); molecular genetics (Morgan) and the DNA double helix (Watson and Crick) then made it possible to trace physiological function to genes and proteins, and cell biology, developmental biology, biophysics and synthetic biology all branched off from this. The other went up toward integration: Pavlov's work on conditioned reflexes studied the neural regulation of digestion and behavior, Wiener's cybernetics (1948) brought feedback from engineering into biology, and Guyton used computer models to study the long-term regulation of blood pressure. Modern Chinese physiology began in the 1920s: the Chinese Physiological Society was founded in Beijing in 1926, and the work of Robert K. S. Lim (Lin Kesheng), Tsai Chiao (Cai Qiao), Feng Tehchuan (Feng Depei) and others reached international standing in digestion, the neuromuscular junction and other fields.

This history shows the main line of physiology: from speculation to experiment, from qualitative to quantitative, from organs to cells and molecules, and finally back to the whole organism, to homeostasis and regulation.

## 1.3. Body Fluids and the Internal Environment

### 1.3.1. Fluid Compartments

About $60\%$ of the body weight of an adult is water, called the body fluid. The cell membrane divides it into two compartments.

**Definition 1.3.1 (Intracellular and Extracellular Fluid)** The part of the body fluid inside cells is called the **intracellular fluid**, about $2/3$ of the body fluid; the part outside cells is called the **extracellular fluid**, about $1/3$. The extracellular fluid includes the plasma in the blood vessels (about $1/4$ of the extracellular fluid), the **interstitial fluid** between cells (about $3/4$), and small amounts of lymph and transcellular fluid (cerebrospinal fluid, synovial fluid, aqueous humor, the endolymph of the inner ear, and so on).

For a $70\,\mathrm{kg}$ man the body fluid is about $42\,\mathrm{L}$: about $28\,\mathrm{L}$ of intracellular fluid and about $14\,\mathrm{L}$ of extracellular fluid, of which plasma is about $3\,\mathrm{L}$ and interstitial fluid about $11\,\mathrm{L}$ (the "60–40–20 rule": body fluid, intracellular fluid and extracellular fluid make up about $60\%$, $40\%$ and $20\%$ of body weight, respectively). Women and obese people have a higher fat fraction and so a lower water fraction; in newborns the water fraction is about $75\%$. Methods for measuring the compartments, and water balance, are covered in Chapter 21.

**Definition 1.3.2 (Internal Environment)** The cells of a multicellular animal live directly in the extracellular fluid, exchanging $\ce{O2}$, nutrients and metabolic products with it. The extracellular fluid forms the environment in which cells live and is called the **internal environment** of the body, to distinguish it from the external environment in which the organism lives.

In the internal environment, the interstitial fluid bathes the cells directly; the **blood plasma** flows throughout the body through the circulation and exchanges water and small molecules rapidly with the interstitial fluid across the capillary wall (the amount exchanged per minute is far greater than the cardiac output). Plasma is therefore the most active part of the internal environment and the easiest to measure, and clinical tests of the composition of the blood represent the state of the internal environment.

### 1.3.2. Composition of the Internal Environment

The composition of intracellular fluid and extracellular fluid is very different. This difference is maintained by transport proteins in the cell membrane (chiefly the **Na⁺/K⁺-ATPase**) and underlies the membrane potential and many transport processes (Chapters 3 and 4).

| Component | Extracellular fluid (plasma) | Intracellular fluid (skeletal muscle) | Normal range and remarks |
|---|---|---|---|
| $\ce{Na+}$ | $142\,\mathrm{mmol\,L^{-1}}$ | $12$ | $135$–$145$ |
| $\ce{K+}$ | $4.2$ | $140$–$155$ | $3.5$–$5.0$; large deviations affect cardiac rhythm |
| $\ce{Ca^2+}$ (free) | $1.2$ | $10^{-4}$ | Total plasma calcium about $2.4$, about half free and about $40\%$ bound to protein |
| $\ce{Mg^2+}$ (free) | $0.6$ | $0.5$–$1$ | |
| $\ce{Cl-}$ | $106$ | $4$–$10$ | |
| $\ce{HCO3-}$ | $24$ | $10$–$12$ | $22$–$28$ |
| Glucose | $5$ | Very low | Fasting $3.9$–$6.1$ |
| Protein | $70\,\mathrm{g\,L^{-1}}$ | Very high | Little in interstitial fluid |
| pH | $7.40$ | About $7.1$–$7.2$ | Arterial blood $7.35$–$7.45$ |
| Osmolality | $290\,\mathrm{mOsm\,kg^{-1}}$ | Same | $285$–$295$ |
| Temperature | $37\,{}^\circ\mathrm{C}$ | | Core temperature, daily fluctuation about $0.5\,{}^\circ\mathrm{C}$ |

The extracellular fluid is rich in $\ce{Na+}$, $\ce{Cl-}$, $\ce{HCO3-}$, $\ce{O2}$, glucose and amino acids; the intracellular fluid is rich in $\ce{K+}$, $\ce{Mg^2+}$, phosphate and protein anions. The **osmolarity** is the same on both sides because water passes freely through the cell membrane (Chapter 3).

The factors that shape the internal environment can be understood in terms of inputs and outputs: cellular metabolism continually consumes $\ce{O2}$ and nutrients and produces $\ce{CO2}$, $\ce{H+}$, nitrogenous waste and heat; the circulation mixes the extracellular fluid throughout the body; the lungs exchange $\ce{O2}$ and $\ce{CO2}$, the digestive tract absorbs nutrients and water, the liver processes metabolites, the kidney regulates water, electrolytes and acid–base balance and excretes waste, and the skin dissipates heat; the nervous and endocrine systems regulate the activity of these organs so that inputs and outputs match.

## 1.4. Homeostasis

**Definition 1.4.1 (Homeostasis)** The relatively constant state in which the physical and chemical properties of the internal environment (composition, temperature, pH, osmotic pressure and so on) are kept within a narrow range despite perturbations from changes in the external environment and from the activity of the organism is called **homeostasis**; the process that maintains it is also called homeostasis.

The parameters of the internal environment are controlled very precisely. The $[\ce{H+}]$ of arterial blood is about $40 \pm 5\,\mathrm{nmol\,L^{-1}}$ (pH $7.35$–$7.45$), only about one 3.5-millionth of the intracellular $\ce{K+}$ concentration, yet it is held within $\pm 12\%$; the plasma $[\ce{Na+}]$ is about $140 \pm 3\,\mathrm{mmol\,L^{-1}}$, fluctuating by only about $2\%$, even though the $\ce{Na+}$ taken in through the digestive tract and excreted by the kidney varies from a few grams to several tens of grams per day.

Homeostasis is neither stillness nor chemical equilibrium. The constancy of the internal environment is the result of a large number of substances continuously flowing in and out in balance, an energy-consuming **dynamic steady state**: once the energy supply stops (for example, when the **Na⁺/K⁺-ATPase** stops after death) the distribution of ions inside and outside cells moves toward **chemical equilibrium**, and equilibrium means precisely the end of life. The "steady state" of physics and chemistry requires only that variables not change with time, not that there be regulation; the homeostasis of physiology stresses that when a perturbation displaces a variable, specific mechanisms pull it back.

The concept of homeostasis extends inside the cell (cytosolic $[\ce{Ca^2+}]$ of about $100\,\mathrm{nmol\,L^{-1}}$ and cytosolic pH of about $7.2$ are both precisely regulated) and to the level of organs and the whole organism (blood pressure, body temperature, blood glucose). The regulated value is not fixed once and for all: in **fever** the **set point** of body temperature moves upward, **circadian rhythms** make body temperature and **cortisol** vary regularly through the day, and in exercise respiration and circulation change greatly so that arterial blood gases remain essentially unchanged.

Disease can often be seen as a breakdown of homeostasis. For example, impaired renal function reduces the ability to excrete sodium, and blood pressure rises as a result; the raised pressure helps the kidney excrete sodium and water in the short term (**pressure natriuresis**, Chapter 24), but in the long term hypertension damages the glomeruli and vessels and lowers renal function further, forming a vicious cycle. Understanding a disease often means finding which regulatory link has failed and which compensatory link is being overused.

## 1.5. Modes of Physiological Regulation

### 1.5.1. Neural Regulation, Humoral Regulation and Autoregulation

**Definition 1.5.1 (Neural Regulation)** Regulation carried out through the nervous system is called **neural regulation**. Its basic mode is the reflex: a regular response of the organism to stimuli from the internal or external environment, mediated by the central nervous system. The structural basis of a reflex is the reflex arc, which consists of five parts: receptor, afferent nerve, nerve center, efferent nerve and effector.

Reflexes are divided into unconditioned reflexes, which are innate and have a fixed reflex arc (such as the knee-jerk and sucking reflexes), and conditioned reflexes, which are established during the life of the individual (Pavlov's salivation to a bell). Neural regulation is fast (milliseconds to seconds), precise, localized and brief.

**Definition 1.5.2 (Humoral Regulation)** The influence of chemical substances produced by certain cells of the body on the activity of other cells, tissues or organs through the body fluids is called **humoral regulation**. The most important form is **endocrine** action, in which **hormones** are carried by the blood to distant target cells; chemical substances may also diffuse through the interstitial fluid to act on neighboring cells (**paracrine**) or on the secreting cell itself (**autocrine**); the hormones synthesized by some neurons are released from axon terminals into the blood, which is called neurosecretion.

Humoral regulation is slow (seconds to hours), widespread and long-lasting; only cells with the corresponding receptors respond, so it is at once a "broadcast" and "addressed". Besides hormones, local metabolites ($\ce{CO2}$, $\ce{H+}$, adenosine, lactate) and cytokines also take part in humoral regulation. Many endocrine glands are controlled directly or indirectly by the nervous system; humoral regulation then becomes an extension of the efferent limb of the **reflex arc**, called neurohumoral regulation, for example the secretion of **epinephrine** by the adrenal medulla when the **sympathetic nervous system** is activated.

**Definition 1.5.3 (Autoregulation)** The adaptive response of a tissue or cell to changes in the internal or external environment, arising from its own properties and independent of neural and humoral factors, is called **autoregulation**.

For example, when arterial pressure varies between about $80$ and $180\,\mathrm{mmHg}$ ($10.7$–$24\,\mathrm{kPa}$; in physiology and clinical practice blood pressure and gas partial pressures are customarily given in millimeters of mercury, $1\,\mathrm{mmHg} = 133.3\,\mathrm{Pa}$), renal blood flow and **glomerular filtration rate** remain essentially unchanged (Chapter 22), because the smooth muscle of the afferent arteriole contracts when stretched (the myogenic response); cardiac muscle contracts more forcefully when stretched (the **Frank–Starling mechanism**, Chapter 12). Autoregulation has a small range and a small magnitude, but is important for keeping the function of certain organs stable.

| Mode | Signal and carrier | Onset | Range of action | Duration |
|---|---|---|---|---|
| Neural regulation | **Action potentials**, **neurotransmitters**; reflex arc | Milliseconds–seconds | Localized, precise | Short |
| Humoral regulation | Hormones, local factors; blood and interstitial fluid | Seconds–hours | Widespread (cells with receptors) | Long |
| Autoregulation | Mechanical and metabolic properties of the tissue itself | Seconds–minutes | Local | As long as the stimulus persists |

## 1.6. Principles of Control Systems

Whether neural, humoral or autoregulatory, the logic of regulation can be described in a unified way in the language of control theory: a controlled variable (blood pressure, body temperature, blood glucose), a sensor that measures it, a controller that compares the measured value with a reference value (the **set point**), and an effector that changes the controlled variable. The way signals flow among these elements determines the behavior of the system.

### 1.6.1. Negative Feedback and Feedback Gain

**Definition 1.6.1 (Negative and Positive Feedback)** The return of information about the output of the controlled part to the controlling part, influencing its activity, is called feedback. If the feedback makes the controlled variable change in the direction opposite to the original perturbation, reducing the deviation, it is called **negative feedback**; if it makes the controlled variable change further in the direction of the original perturbation, amplifying the deviation, it is called **positive feedback**.

Negative feedback is the main way homeostasis is maintained. Take body temperature as an example: strenuous exercise increases heat production and body temperature rises; temperature-sensitive neurons in the hypothalamus detect the deviation, and the thermoregulatory center dilates skin vessels, increases sweating and reduces heat production, so body temperature falls back; when body temperature is below the set point the reverse occurs (Chapter 31).

Negative feedback cannot eliminate the effect of a perturbation completely: a deviation must exist before a correction can be produced. The quantity that measures how effective negative feedback is, is the gain.

**Definition 1.6.2 (Feedback Gain)** For a given perturbation, let the deviation of the controlled variable without feedback be $\Delta_0$ and with feedback the residual error be $e$; then the correction produced by feedback is $e - \Delta_0$. The **feedback gain** of the control system is defined as
$$
G = \frac{\text{correction}}{\text{error}} = \frac{e - \Delta_0}{e}.
$$
For negative feedback $G < 0$.

**Formula 1.6.1 (Residual Error of Proportional Control)** Solving Definition 1.6.2 gives
$$
e = \frac{\Delta_0}{1 - G} = \frac{\Delta_0}{1 + \lvert G\rvert}. \tag{1.1}
$$
The larger the absolute value of the gain, the smaller the residual error.

**Example 1.6.1 (Gain of the Baroreceptor Reflex and of Thermoregulation)** When a large volume of blood is infused into a person whose **baroreceptor reflex** has been abolished, arterial pressure rises from $100\,\mathrm{mmHg}$ to $175\,\mathrm{mmHg}$ ($\Delta_0 = +75\,\mathrm{mmHg}$); with the reflex intact, the same infusion raises pressure by only $25\,\mathrm{mmHg}$. The correction is $-50\,\mathrm{mmHg}$ and the error is $+25\,\mathrm{mmHg}$, so the gain is $G = -50/25 = -2$: any perturbation that changes blood pressure has only one third of its effect without feedback, consistent with the $1/(1+2)$ of Eq. (1.1). The system that maintains core temperature in moderate cold has a gain of about $-33$, reducing perturbations to about $1/34$.

:::

Eq. (1.1) describes proportional control: the correction is proportional to the current error. If the controller accumulates the integral of the error over time, the correction keeps growing as long as the error is nonzero, until the error is zero; this is **integral feedback**. The mechanism by which the kidney regulates blood volume and long-term arterial pressure by excreting sodium and water has this property: as long as arterial pressure is above the kidney's set point, sodium and water excretion exceed intake and blood volume keeps falling, until pressure returns to the set point (Chapters 16 and 24). It is therefore called "infinite gain" feedback and is the final determinant of the long-term level of arterial pressure.

High gain is not always advantageous. Signals take time to travel around a feedback loop (nerve conduction, hormone secretion and clearance, the response of the effector), so the correction always lags behind the deviation; the higher the gain, the more serious the overcorrection caused by the delay, and the system oscillates or even becomes unstable (Panel B below). This is the origin of many oscillations in physiological systems (Cheyne–Stokes breathing, pulses of some hormones); the general theory of oscillation from delayed negative feedback is in [7.9.16](/7.9.16).

![Gain and delay in negative feedback (dimensionless model τ dx/dt = −x + D + u). A: a unit step perturbation is applied at t = 1; without feedback the deviation is 1, and proportional feedback u = Gx reduces the steady-state deviation to 1/(1 − G): 1/3 for G = −2 (baroreceptor reflex) and about 1/34 for G = −33 (body temperature); integral control (dashed) finally brings the error to zero. B: with a delay of 0.4 τ added to the same loop, G = −2 converges smoothly, G = −3.5 gives damped oscillations, and the oscillations for G = −5 grow](./plots/feedback-gain.py)

### 1.6.2. Levels of Negative Feedback

Negative feedback appears on different spatial and temporal scales and with different substances as carriers, but the principle is the same.

- Biochemical level: the product of a metabolic pathway inhibits a key enzyme of the pathway, which is **feedback inhibition**. For example, ATP inhibits phosphofructokinase-1, matching the rate of **glycolysis** to the cell's energy demand ([7.1](/7.1)). The time scale is milliseconds to seconds.
- Mechanical level: the tip links of the stereocilia bundle of inner-ear hair cells pull open **mechanosensitive channels**; the entering $\ce{Ca^2+}$ makes the myosin "adaptation motor" attached to the upper end of the tip link slide, relaxing the tension on the gating spring and returning the open probability of the channel to the resting level of about $15\%$. The response to a sustained deflection thus decays, and the bundle always operates in its most sensitive range (Chapter 42).
- Whole-body level: a rise in the partial pressure of blood $\ce{CO2}$ stimulates central and peripheral chemoreceptors, and the respiratory center increases ventilation, exhaling more $\ce{CO2}$ and bringing its partial pressure back down (Chapter 20). This loop spans the blood, brainstem, respiratory muscles and lungs, with a time scale of seconds to minutes.

### 1.6.3. Positive Feedback

Positive feedback makes a process faster and faster until it reaches an extreme or is completed. It has three kinds of use in physiology:

- Generating fast all-or-none events: membrane depolarization opens voltage-gated $\ce{Na+}$ channels, and the influx of $\ce{Na+}$ depolarizes further, producing an action potential (Chapter 4); in cardiac muscle cells, the small amount of $\ce{Ca^2+}$ entering through L-type $\ce{Ca^2+}$ channels opens the ryanodine receptors of the **sarcoplasmic reticulum**, releasing a large amount of $\ce{Ca^2+}$ (**calcium-induced calcium release**, Chapter 10).
- Completing a process that must be "done all at once": in **blood coagulation**, activated clotting factors activate more clotting factors, so that a clot forms within minutes (Chapter 11); in childbirth, stretching of the cervix by the fetal head reflexively promotes **oxytocin** secretion and uterine contraction (Chapter 38); in micturition, urine flowing through the urethra further strengthens bladder contraction until it is emptied (Chapter 22).
- Producing a switch: in the middle of the **menstrual cycle**, once estrogen exceeds a threshold, negative feedback turns into positive feedback, causing the luteinizing hormone surge and ovulation (Chapter 37).

Positive feedback is intrinsically unstable. Physiology terminates it in three ways: exhaustion or inactivation of resources or channels ($\ce{Na+}$ channels inactivate about $1\,\mathrm{ms}$ after opening); disappearance of the stimulus once the process is complete (delivery of the fetus); and coupling to negative feedback, which confines the positive feedback locally. Blood coagulation is the classic example of the last: thrombin amplifies its own production at the site of injury, but also activates protein C and is inactivated by antithrombin, so that the clot does not spread through the whole body. At the level of the whole organism, the positive-feedback process of coagulation is part of the negative feedback that maintains blood volume; the positive feedback of the action potential likewise serves thousands of neural negative-feedback regulations.

When a perturbation exceeds the capacity of negative feedback, a loop that was formerly under control may turn into a vicious cycle. In severe hemorrhage, the fall in arterial pressure reduces coronary perfusion, myocardial ischemia lowers pumping capacity, and arterial pressure falls further. A healthy person can recover from the loss of about $1\,\mathrm{L}$ of blood, but the loss of about $2\,\mathrm{L}$ is often fatal.

**Example 1.6.2 (The Threshold after Hemorrhage)** Let the arterial pressure $P$ (normally 1) be determined jointly by the effective blood volume $V$ (normally 1) and the pumping capacity of the heart $h(P)$, which in turn depends on coronary perfusion, that is, on $P$:
$$
\tau\frac{\mathrm{d}P}{\mathrm{d}t} = Vh(P) - P, \qquad h(P) = \frac{aP^2}{P^2 + K^2}.
$$
Apart from $P = 0$, the fixed points satisfy $P^2 - aVP + K^2 = 0$, which has solutions only for $V \ge 2K/a$. Taking $a = 1.12$ and $K = 0.35$ (so that $h(1) = 1$), the critical blood volume is $0.625$: after a $20\%$ loss ($V = 0.8$) the system has a stable low-pressure state and an unstable threshold, so that pressure falls, stabilizes, and is then restored by other negative feedback; after a $40\%$ loss ($V = 0.6$) there is no positive fixed point and the pressure keeps falling to collapse. This model illustrates only the structure (positive feedback gives the system a threshold and **bistability**); the parameters are schematic. For the real mechanisms of circulatory regulation, see Chapter 16.

![Positive feedback after hemorrhage (the model of Example 1.6.2, schematic parameters). A: the curve of τ dP/dt against P; intersections with the horizontal axis are fixed points, filled for stable and open for the unstable threshold. At V = 1 the stable point is at normal pressure; at V = 0.8 the stable point moves down and a threshold appears; at V = 0.6 only the collapsed state P = 0 remains. B: blood pressure after sudden loss of 20% (about 1 L) and 40% (about 2 L) of blood: the former settles at a lower level, the latter enters a vicious cycle](./plots/hemorrhage.py)

### 1.6.4. Feedforward

**Definition 1.6.3 (Feedforward Control)** The detection of a perturbation by the controlling part directly, through a separate pathway, before or at the same time as the perturbation acts on the controlled variable, and the adjustment of effector activity in advance, is called **feedforward control**.

Take the cruise control of a car as an analogy: feedback control increases the throttle only after climbing a hill has slowed the car, pulling the speed back to the set value; feedforward control measures the slope of the road and increases the throttle in advance as the hill begins, so that the speed can hardly fall. But feedforward does not compare output with the set value: if the estimates of slope and load are inaccurate, the speed will still deviate, and feedforward itself cannot detect this error. Feedforward and feedback are therefore not mutually exclusive, and the best control combines the two: feedforward quickly cancels most of the perturbation and feedback removes the remaining error.

Physiology has many examples of feedforward. At the sight or smell of food, gastric juice, pancreatic juice and insulin already begin to be secreted (the cephalic phase of digestion, Chapter 27; the cephalic phase of insulin secretion, Chapter 35), so the body is prepared before nutrients are absorbed; at the onset of exercise, ventilation and heart rate are increased by central command before blood gases change (Chapter 20); cold receptors in the skin trigger heat production and skin vasoconstriction before the **core temperature** falls (Chapter 31); before reaching out to lift an object, postural muscles contract in advance to offset the coming shift of the center of gravity. The cerebellum continually corrects feedforward commands by comparing expected and actual movement outcomes, a form of adaptive control (Chapter 45).

![Feedback and feedforward in cruise control (dimensionless model dv/dt = F − v − s, with load s = 0.5 on the uphill segment 5 ≤ t < 25). Without control the speed falls to 0.5; with feedback only (proportional plus integral) the speed first falls and is then pulled back to the set value, with a brief overshoot on leaving the slope; with feedforward only, the controller increases power in advance according to the estimated load (underestimated by 20%), so the speed falls only slightly, but this error persists; with both combined the deviation is smallest and ends at zero](./plots/feedforward.py)

### 1.6.5. Complex Control: The Cell Cycle

A physiological process often requires a combination of several control modes. The **cell cycle** is an example ([7.3.20](/7.3.20)): it must proceed in one direction (G1–S–G2–M cannot go backward), it must be extremely robust to stress and molecular fluctuations, division must be matched to the doubling of cell mass, and it is not a simple timer, because each step must check whether the previous step has been completed. These properties arise from a combination of several control motifs: positive feedback in Cdk activity produces an irreversible switch (each transition is a bistable jump), negative feedback (such as degradation of cyclins by the APC/C) resets the system and produces oscillation, and checkpoints make downstream events depend on completion signals from upstream events. Describing these interactions with ordinary differential equations reproduces the timing of the cycle and its response to perturbation quantitatively. The same combinatorial principle also appears at the organ level: pacemaking in the heart, the menstrual cycle and the sleep–wake cycle are all oscillators built from positive-feedback switches and delayed negative feedback.

## 1.7. Evolution and Comparison

### 1.7.1. Conformers and Regulators

Faced with environmental change, animals have two basic strategies. A *conformer* lets some internal variable change along with the environment, whereas a *regulator* expends energy to hold it at a constant value. The same animal may adopt different strategies for different variables, and may regulate the same variable only within a certain range.

| Variable | Conformers | Regulators | Chapter in this course |
|---|---|---|---|
| Osmolarity | Most marine invertebrates, whose body fluids are isosmotic with seawater | Teleost fishes, most crustaceans (within a certain range), terrestrial animals | Chapter 21 |
| Body temperature | **Ectotherms** (fishes, amphibians, reptiles, most invertebrates) | **Endotherms** (birds, mammals), and local regions of some insects and fishes | Chapter 31 |
| $\ce{O2}$ consumption | In many invertebrates the rate of oxygen consumption falls with ambient oxygen partial pressure | Most vertebrates keep the rate of oxygen consumption constant within a certain range | Chapter 19 |
| Ionic composition | A few | Almost all animals regulate extracellular $\ce{K+}$, $\ce{Ca^2+}$ and pH | Chapters 21 and 25 |

Each strategy has its costs. Regulation consumes energy continuously (a large part of the resting metabolism of mammals goes to maintaining body temperature and ion gradients) and is effective only within a certain range, beyond which regulation fails; conforming consumes no energy but requires the cells themselves to function under changing conditions (for example, enzymes that remain sufficiently active at different temperatures, and cells that can tolerate changes in the osmolarity of the body fluids). Bernard's "free and independent life" is precisely the benefit of regulation: endotherms can forage on a cold night, and teleosts can move from the ocean into rivers.

![Conformers and regulators (schematic). A: body-fluid osmolarity in relation to the environment. An osmoconformer (such as the marine mussel) has body fluids that follow the environment (the dotted line is where the two are equal); a hyperosmotic-regulating shore crab keeps its body fluids above the environment in diluted seawater and conforms in seawater and at higher concentrations; a teleost keeps its body fluids at about 300–400 mOsm/kg over a very wide range. B: body temperature in relation to ambient temperature. An ectotherm without behavioral regulation has a body temperature that follows the environment; an endotherm keeps about 37 °C within its regulatory range and becomes hypothermic or hyperthermic beyond it](./plots/conformer-regulator.py)

### 1.7.2. From Open Body Fluids to a Barrier-Protected Internal Environment

The internal environment was not there from the beginning. Sponges have no true tissue barrier; water flows through the canal system and most cells exchange directly with seawater. In cnidarians only the mesoglea lies between the two cell layers, and the fluid in the gastrovascular cavity is continuous with the outside; flatworms and placozoans have no circulatory system and move substances between cells mainly by diffusion, so the body must be flat or small (the limit that diffusion distance sets is discussed in Chapter 2). A true internal environment requires three conditions: (1) an epithelium sealed by **tight junctions** or **septate junctions**, separating the extracellular fluid from the outside; (2) a circulatory system, which mixes the extracellular fluid throughout the body and connects it with the exchange organs; and (3) organs and control systems that regulate these exchanges.

In animals that originated in the sea, the earliest extracellular fluid was enclosed seawater, and the hemolymph of many marine invertebrates is still isosmotic with seawater and similar in ionic composition. The extracellular fluid of vertebrates has an osmolality only about one third that of seawater (about $300$ versus $1000\,\mathrm{mOsm\,kg^{-1}}$), which was once explained by the idea that the vertebrate ancestors passed through a freshwater stage (Homer Smith), a hypothesis that is still disputed. Cartilaginous fishes took another route: the plasma retains about $350\,\mathrm{mmol\,L^{-1}}$ of urea and trimethylamine oxide, giving an osmolality slightly above that of seawater, while $\ce{Na+}$ and $\ce{Cl-}$ remain far below their seawater levels (Chapter 21).

The modes of regulation themselves also have an evolutionary order. Unicellular organisms and animals without a nervous system have only regulation mediated by chemical signals; once a nervous system appeared, fast neural regulation gradually became dominant, and the endocrine system also grew more complex and came largely under nervous control. Comparing the regulatory capacity of different animals also reveals a pattern in individual development: newborns cannot concentrate urine effectively, and the elderly adapt less well to exercise and changes in air temperature, so the capacity to maintain homeostasis also has its "life cycle".

## Summary

| Concept | Key points |
|---|---|
| Physiology (Definition 1.1.1) | Function, principle, mechanism, regulation; from molecules to the whole organism; form fits function; comparison is a basic method |
| History | Speculation and experiment of Hippocrates and Galen → Harvey's quantitative argument (Example 1.2.1) → mechanism and chemistry → tissues and cells → Bernard's internal environment and Cannon's homeostasis → molecules and cybernetics |
| Body fluids (Definition 1.3.1) | $60\%$ of body weight; intracellular fluid $2/3$, extracellular fluid $1/3$ (plasma $1/4$, interstitial fluid $3/4$) |
| Internal environment (Definition 1.3.2) | Extracellular fluid; high $\ce{Na+}$ and $\ce{Cl-}$, low $\ce{K+}$; equal osmolarity on both sides |
| Homeostasis (Definition 1.4.1) | Dynamic constancy maintained by energy expenditure; $[\ce{H+}] = 40 \pm 5\,\mathrm{nmol\,L^{-1}}$, $[\ce{Na+}] = 140 \pm 3\,\mathrm{mmol\,L^{-1}}$; disease is a breakdown of homeostasis |
| Modes of regulation (Definitions 1.5.1–1.5.3) | Neural (fast, precise, short), humoral (slow, widespread, long), autoregulation (local); neurohumoral regulation |
| Negative feedback (Definition 1.6.1) | Reduces deviation; gain $G = $ correction/error, residual error $\Delta_0/(1 - G)$ (Eq. 1.1); baroreceptor reflex $-2$, body temperature $-33$; integral control gives zero error; delay plus high gain causes oscillation |
| Positive feedback | Amplifies deviation; produces all-or-none events, completes processes, makes switches; terminated by inactivation, completion or coupling to negative feedback; beyond the capacity of negative feedback it forms vicious cycles and thresholds (Example 1.6.2) |
| Feedforward (Definition 1.6.3) | Cancels perturbations in advance; fast but cannot correct its own errors; best combined with feedback |
| Evolution | Conformers and regulators; an internal environment requires a sealed epithelium, circulation and regulatory organs; humoral regulation preceded neural regulation |

## Questions

1. Why is homeostasis said to be dynamic? Use the distribution of $\ce{Na+}$ and $\ce{K+}$ inside and outside cells to explain the difference between "homeostasis" and "equilibrium".

   **Answer** The ion concentration differences across the cell membrane do not change with time, but this is the result of $\ce{Na+}$ continually leaking in and $\ce{K+}$ continually leaking out through channels, balanced by the Na⁺/K⁺-ATPase continually pumping them back at the expense of ATP: the variable is constant, but the fluxes are not zero. If the pump is blocked with ouabain, or the cell is deprived of oxygen, the gradients gradually disappear within tens of minutes, the ions approach electrochemical equilibrium, and the cell swells, loses excitability and eventually dies. Equilibrium requires no energy and has zero net flux; homeostasis requires a continuous energy supply and has mechanisms that restore the original value after a perturbation.

2. A person's thermoregulatory gain in the cold is $-33$. If, without regulation, an exposure to cold would lower core temperature by $6.8\,{}^\circ\mathrm{C}$, by how much does it fall with regulation? Why can a physiological system not raise its gain indefinitely?

   **Answer** From Eq. (1.1), $e = 6.8/(1 + 33) = 0.2\,{}^\circ\mathrm{C}$. Gain cannot be raised indefinitely: first, the capacity of the effectors is limited (heat production and vasoconstriction both have upper limits, beyond which the effective gain actually falls); second, there are delays in the feedback loop, and high gain combined with delay causes overcorrection, oscillation and even instability (Panel B); third, high gain often means a continuous high energy cost. Physiological systems use integral control (such as the kidney's long-term regulation of blood pressure) to eliminate error without increasing the instantaneous gain.

3. Using the model of Example 1.6.2, explain why hemorrhage beyond a certain degree suddenly changes from "recoverable" to "irreversible". How should this vicious cycle be interrupted clinically?

   **Answer** Positive feedback gives $Vh(P) = P$ two positive roots: a higher stable point and a lower unstable threshold. As blood volume falls the two roots approach each other, merge at $V = 2K/a$ and disappear (a **saddle-node bifurcation**), after which the system can only go to $P = 0$. A small additional loss can therefore change the outcome qualitatively. The vicious cycle can be interrupted at any link in the loop: rapidly replacing blood volume (bringing $V$ back above the critical value), maintaining coronary perfusion with vasopressors, and stopping the bleeding to prevent $V$ from falling further; the earlier the intervention, the smaller the correction needed.

4. Give two examples of feedforward control in physiology and explain why they still need feedback.

   **Answer** The cephalic phase of digestion: before eating, gastric acid and insulin have begun to be secreted, reducing the fluctuations of gastric pH and blood glucose once food arrives; but the amount secreted in advance is an estimate, and actual meals differ, so in the end gastric acid is corrected by **negative feedback** from gastric pH (low pH inhibits gastrin) and blood glucose by the **insulin**–**glucagon** negative feedback. Central command in exercise: at the onset of exercise ventilation and cardiac output increase immediately, but matching their magnitude to the actual metabolic demand relies on feedback adjustment by arterial $\ce{CO2}$, $\ce{H+}$ and muscle metabolic receptors. Feedforward does not measure the output and so cannot detect errors in its own estimates.

5. (Open question) Most marine invertebrates are osmoconformers, whereas teleost fishes are osmoregulators. Discuss the advantages and limitations of the two strategies from an energetic and ecological standpoint.

   **Answer** Key points: **osmoconformers** need no energy to maintain an osmotic gradient, but their cells must tolerate changes in body fluids (cell volume is regulated with organic osmolytes such as free amino acids), and they can live only in environments of stable salinity, with a limited ability to enter estuaries or fresh water; **osmoregulators** can occupy habitats of different or even changing salinity (migratory fishes move between ocean and rivers) and their cells work in a constant environment, but they bear the energy cost of ion transport (ion transport by the gills and kidney can account for several percent of resting metabolism, and more at extreme salinities) and need specialized organs (the salt-secreting cells of the gill, the kidney). Some crustaceans adopt an intermediate strategy: hyperosmotic regulation in dilute environments and conforming in seawater.
