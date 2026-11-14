---
title: "Neuroethology: Principles, Model Systems and the Cellular Basis of Behavior"
description: "What neuroethology studies and how: natural behavior as the object, neural mechanism as the goal, quantitative behavior and neurophysiology as the foundation; Krogh's principle and the choice of model systems; identified neurons and levels of simplicity; the neuron doctrine, chemical and electrical synapses and the ionic basis of the action potential seen as design solutions for behavior; conduction speed and escape; neurotoxins as chemical weapons aimed at channels and the evolution of target-site resistance; a survey of methods."
---

The chapters so far have asked what animals do, why the four kinds of explanation of **Tinbergen's four questions** are needed, how behavior is studied and how genes and development build it ([7.18.1](/7.18.1)–[7.18.5](/7.18.5)). This chapter begins the part of the course on mechanism: how a nervous system turns stimuli into behavior. The cellular machinery itself, ion channels, action potentials and synapses, is treated in animal physiology ([7.14.4](/7.14.4), [7.14.5](/7.14.5)) and computational neuroscience ([7.16.4](/7.16.4), [7.16.5](/7.16.5), [7.16.9](/7.16.9), [7.16.10](/7.16.10)); we do not derive it again. Instead we ask what the study of mechanism looks like when it starts from natural behavior, why a few animals have taught us most of what we know, and which properties of neurons matter most for behavior: speed, the choice between electrical and chemical transmission, and the vulnerability of channels that animals exploit with toxins. The next two chapters add the chemical messengers that set behavioral states ([7.18.7](/7.18.7)) and the brain systems for homeostasis, emotion and planning ([7.18.8](/7.18.8)); [7.18.9](/7.18.9)–[7.18.16](/7.18.16) then treat the classic neuroethological systems one by one.

## 6.1. What Neuroethology Studies

### 6.1.1. Object, Goal and Foundations

The study of animal behavior grew from two traditions ([7.18.1](/7.18.1)). **Ethology** was evolutionary in outlook, worked mainly in the field and compared many species; comparative psychology was mechanistic and developmental, worked in the laboratory and concentrated on a few mammals. Neurobiology, for its part, traditionally worked on anesthetized animals, isolated tissues or single cells, and chose its species for technical convenience, such as the size of the neurons. Neuroethology is the synthesis of ethology and neurobiology.

**Definition 6.1.1 (Neuroethology)** **Neuroethology** is the study of the neural mechanisms of natural behavior: behavior that an animal performs in its own environment and that has been shaped by natural selection; it combines the quantitative analysis of behavior under natural or seminatural conditions with neurophysiological, neuroanatomical and neurogenetic analysis of the circuits that produce it.

The definition has three parts, which together distinguish neuroethology from other ways of studying brain and behavior:

| | Neuroethology | What it excludes or adds |
|---|---|---|
| Object | Natural behavior: prey capture, escape, courtship song, navigation, communication | Not arbitrary laboratory tasks chosen for convenience, although laboratory tasks may model natural ones |
| Goal | Neural mechanism: which neurons, circuits and molecules produce the behavior, and how | Not behavior alone (ethology) and not neurons alone (cellular neurobiology) |
| Foundation | Quantitative analysis of behavior, combined with neurophysiology and neurogenetics | The behavior must be measured as precisely as the neurons, preferably with stimuli that mimic natural ones |

Neuroethology is one level of analysis within the proximate half of **Tinbergen's four questions**, but its practitioners also ask why the mechanism has the design it has, which links it to function and evolution. A recurring theme of the following chapters is that the mechanism makes sense only in the light of the behavior it serves: the sensitivity of a moth's ear is matched to the calls of bats ([7.18.12](/7.18.12)), and the feature detectors of a toad's retina and tectum to the shapes of prey and predators ([7.18.13](/7.18.13)). Paraphrasing Dobzhansky's dictum about evolution, neuroethologists like to say that nothing in neuroscience makes sense except in the light of behavior. The opposite approach, which starts from the neurons and adds behavior later, has been criticized for a "reductionist bias": recording from ever more neurons cannot reveal how a circuit produces a behavior unless the behavior has first been described carefully enough to say what the circuit must compute (Krakauer et al., 2017).

### 6.1.2. Quantifying Behavior

A neural analysis requires a behavior that can be measured. Any behavior can be divided into components of decreasing complexity. The aggressive display of a cichlid fish, for example, consists of lateral display, tail beating, circling and mouth fighting; lateral display in turn consists of erecting the fins, spreading the gill covers and intensifying the coloration; each of these is a pattern of contraction of particular muscles, and each contraction is controlled by particular motor units. This hierarchy of levels of integration, emphasized by Tinbergen, tells the neuroethologist where to look: the lowest levels are closest to identifiable neurons, the highest to the function of the behavior.

At any level, a behavior can be quantified by three measures:

- *rate of occurrence*: how often the pattern is performed per unit time;
- *duration*: how long each performance lasts;
- *intensity*: how strongly it is performed (the angle of a fin, the amplitude of a call).

A behavior suited to neural analysis has well-defined beginnings and ends, so that rate and duration can be measured, and an intensity that varies along a single dimension. Compound displays, whose elements are not performed together, are hard to quantify; their elements are easier. The methods of observation and sampling are treated in [7.18.2](/7.18.2). In the last decade, machine vision has transformed the measurement of behavior: deep networks track body parts in video without markers (pose estimation; Mathis et al., 2018), and unsupervised methods split continuous movement into recurring motifs lasting a fraction of a second (Wiltschko et al., 2015), so that a behavior can be described at a resolution comparable to that of neural recordings ([7.16.3](/7.16.3#sec-3.7)).

### 6.1.3. The Three Roles of the Nervous System

The nervous system serves behavior in three ways:

1. it relays information about the environment and the body: *sensation*;
2. it processes that information, comparing it with internal state and past experience, and selects an action: *integration* or brain function;
3. it relays instructions to the muscles and glands: *movement* and other output.

The division is a simplification (sensory neurons already filter information, and motor circuits generate patterns without instructions for each contraction), but it organizes the following chapters: the sensory worlds of animals and the classic sensory systems ([7.18.9](/7.18.9)–[7.18.12](/7.18.12)), feature detection and stimulus filtering ([7.18.13](/7.18.13)), motor patterns ([7.18.14](/7.18.14)) and systems that span all three, such as the jamming avoidance response of electric fish ([7.18.15](/7.18.15)) and acoustic communication ([7.18.16](/7.18.16)).

![The three roles of the nervous system in behavior. Top row: a stimulus from the environment is transduced by receptors (sensation), integrated by central circuits under the influence of internal state, hormones and modulators, and translated into commands for muscles (movement); the behavior changes the animal's relation to the environment and so its next input. Bottom row: the same stages in the escape of a noctuid moth from a bat: the ultrasonic call is detected by the two receptor cells (A1, A2) of the tympanal organ, interneurons in the thoracic ganglia compare the two sides, and flight motor neurons steer the moth away or into a dive. The chapters of this course that treat each stage are marked.](./plots/three-roles.py)

## 6.2. Choosing the Right Animal

### 6.2.1. Krogh's Principle

In 1929 the Danish physiologist August Krogh, discussing the progress of physiology, wrote that "for such a large number of problems there will be some animal of choice, or a few such animals, on which it can be most conveniently studied." Hans Krebs (1975) named the idea after him.

**Definition 6.2.1 (Krogh's Principle)** **Krogh's principle** is the methodological rule that for many biological problems there exists an animal species, or a few species, in which the problem can be studied most conveniently, because the relevant structure or behavior is unusually large, accessible, simple or exaggerated in it; the investigator should seek out that species rather than study the problem in whichever animal is at hand.

The principle works because the number of solutions to a given problem is limited. Keeping the body oriented requires a reference such as the direction of light or of gravity; detecting the direction of a sound requires comparing two ears. Many solutions were found early in evolution and are homologous in different groups, and others have been reached repeatedly by **convergent evolution**. The mechanisms of learning in the sea slug *Aplysia* (cAMP, CREB, synaptic facilitation) turned out to be those of mammals ([7.16.38](/7.16.38)), and the ionic mechanism of the action potential found in the squid giant axon is that of every animal with $\ce{Na+}$ action potentials. A model system is therefore studied not mainly to understand that species but to extract principles.

A good neuroethological model system combines two sets of properties:

- the *behavior* is simple, robust, readily elicited in the laboratory, quantifiable and ethologically relevant (it matters to the animal in nature);
- the *animal* is inexpensive, easy to keep and preferably to breed, and its nervous system is accessible to recording and manipulation.

These requirements are rarely met together. The electric organ discharge of weakly electric fish is a model case: each discharge is a brief electrical pulse or wave, extremely constant in form, which can be recorded by electrodes in the water without touching the fish; its rate and regularity change during aggressive and courtship interactions, and the fish can be stimulated with playback of artificial discharges ([7.18.15](/7.18.15)).

Two kinds of species have dominated the field. *Specialists* (sometimes called champion species) perform a task exceptionally well: the barn owl localizes sound in darkness, echolocating bats hunt with sound, electric fish sense their surroundings with their own electric field. Their exaggerated abilities make the relevant circuits large and their computations visible. *Genetic model organisms* (the nematode *Caenorhabditis elegans*, the fruit fly *Drosophila melanogaster*, the zebrafish, the mouse) were chosen for genetics and development; they offer genetic access to identified cell types, but their behavior was initially less well known. The distinction is fading: genome editing and viral vectors now make it possible to manipulate genes in ants, mosquitoes, butterflies and cichlid fishes, and ever more natural behavior (courtship song, aggression, foraging, navigation) is studied in the genetic models.

| System | Behavior | Why it is suitable | Chapter |
|---|---|---|---|
| Squid giant axon | Jet-propelled escape | Axon up to $1\,\mathrm{mm}$ wide | [7.14.4](/7.14.4#sec-4.7.2) |
| Sea slug *Aplysia* | Gill and siphon withdrawal, inking, egg laying | Few, large, identified neurons | [7.18.41](/7.18.41), [7.16.38](/7.16.38) |
| Crab and lobster stomatogastric ganglion | Rhythmic chewing and filtering of food | About 30 identified neurons that keep working in a dish | [7.18.7](/7.18.7) |
| Crayfish lateral giant, fish Mauthner cell, fly giant fiber | Escape | Single identified command-like neurons | [7.18.14](/7.18.14) |
| Locust LGMD–DCMD | Avoiding approaching objects | One identified pathway for looming | [7.18.13](/7.18.13) |
| Toad | Prey catching and predator avoidance | Behavior elicited by simple dummies | [7.18.13](/7.18.13) |
| Noctuid moth and bat | Echolocation and its evasion | Two receptor cells per ear; prey and predator both accessible | [7.18.12](/7.18.12) |
| Barn owl | Sound localization in darkness | Precise behavior, maps of auditory space | [7.18.11](/7.18.11) |
| Weakly electric fish *Eigenmannia* | Jamming avoidance response | Behavior measured electrically, circuit known from receptors to pacemaker | [7.18.15](/7.18.15) |
| Field cricket and frogs | Phonotaxis to calling songs | Songs synthesized and played back | [7.18.16](/7.18.16) |
| Zebra finch and canary | Song learning | Learned vocal behavior with a dedicated set of nuclei | [7.18.17](/7.18.17) |
| Honey bee, desert ant | Navigation, dance communication | Precise homing behavior in the field | [7.18.21](/7.18.21) |
| *C. elegans*, *Drosophila*, zebrafish, mouse | Chemotaxis, courtship, aggression, foraging, prey capture | Genetic access to cell types, complete or partial connectomes | throughout |

### 6.2.2. Identified Neurons and Levels of Simplicity

Many invertebrate nervous systems, and some parts of vertebrate ones, contain neurons that can be found again in every individual.

**Definition 6.2.2 (Identified Neuron)** An **identified neuron** is a neuron that can be recognized individually in every member of a species by its position, size, shape, projections, transmitter and physiological properties, so that results obtained from it in different animals can be combined.

Examples are the Mauthner cells of fishes and amphibians, the lateral and medial giant interneurons of crayfish, the giant fibers of flies, the LGMD and DCMD neurons of locusts, the neuron R2 and the bag cells of *Aplysia*, and the neurons of the stomatogastric ganglion. Identified neurons allow the experimenter to record the same cell in many animals, to establish its connections one by one and to ask whether its activity is necessary and sufficient for a behavior ([7.18.14](/7.18.14)). In *C. elegans* every one of the 302 neurons of the hermaphrodite is identified, and in *Drosophila* genetic driver lines give reproducible access to most cell types.

Neuroethology deliberately studies simple behaviors. To ethologists this restriction is sometimes disappointing, but it is both unavoidable and productive. The situation resembles that of mechanics in the seventeenth century: by first analyzing idealized motions (falling bodies without air resistance), physics discovered principles such as Newton's laws, which an early attempt to analyze realistic, complicated motions would have obscured. Choosing the right level of simplicity means choosing a behavior simple enough that the neurons producing it can be found, yet natural enough that the answer matters.

![Numbers of neurons in nervous systems used in neuroethology (approximate published counts, logarithmic scale): the crab stomatogastric ganglion (about 30), the hermaphrodite of *Caenorhabditis elegans* (302), the central nervous system of *Aplysia* (about 2 × 10⁴), the brain of a larval zebrafish (about 10⁵), the adult *Drosophila* central brain (about 1.4 × 10⁵), the honey bee brain (about 10⁶), the mouse brain (about 7 × 10⁷), the octopus (about 5 × 10⁸, two thirds of them in the arms), the common raven (about 2 × 10⁹), the rhesus macaque (about 6 × 10⁹) and the human (about 8.6 × 10¹⁰). Filled bars: complete synaptic wiring diagram (connectome) published for the whole nervous system or brain. Eight orders of magnitude separate the smallest systems, in which every neuron is identified, from the largest.](./plots/neuron-counts.py)

## 6.3. Three Foundations, Seen from Behavior

The nineteenth century produced more knowledge of the brain than all earlier centuries together. Purkinje described the large neurons of the cerebellum (1837), Helmholtz measured the speed of the nerve impulse (1850), and even the young Sigmund Freud, before he turned to psychology, studied the nerve cells of the crayfish and the lamprey. Three theories, completed in the twentieth century, form the cellular foundation of neuroethology: the neuron doctrine, synaptic transmission and the ionic basis of the action potential. Their full treatment is in [7.14.4](/7.14.4), [7.14.5](/7.14.5) and [7.16.4](/7.16.4)–[7.16.10](/7.16.10); here we recall them briefly and stress the features that matter for behavior.

### 6.3.1. The Neuron Doctrine and Its Exceptions

Golgi's silver chromate stain (1873) revealed whole single nerve cells for the first time, and Cajal used it to argue that nerve cells are separate units that touch but do not fuse, against Golgi's own reticular theory of a continuous network; the two shared the Nobel Prize of 1906. The **neuron doctrine** ([7.14.5](/7.14.5#sec-5.1.1)) was finally confirmed when electron microscopy in the 1950s showed a cleft between pre- and postsynaptic membranes.

Was Golgi entirely wrong? A volume electron microscopy reconstruction of the subepithelial **nerve net** of a juvenile comb jelly, *Mnemiopsis leidyi*, showed that its neurons are fused into a single syncytium by continuous plasma membrane, without chemical synapses between them (Burkhardt et al., 2023). Ctenophores may be the sister group of all other animals, and whether their neurons are homologous to those of other animals is disputed ([7.14.5](/7.14.5#sec-5.6), [7.16.53](/7.16.53#sec-53.1)). What the syncytial net contributes to the comb jelly's behavior (the coordination of its swimming comb rows and of prey capture with its tentacles) is not yet known, and the animal also has neurons with ordinary chemical synapses elsewhere. The finding shows that a continuous network can exist, but also why discrete neurons prevail: cells with polarized connections allow specific signals to be routed along specific paths, the basis of the circuits in the following chapters.

### 6.3.2. Synaptic Transmission: Chemical and Electrical

Sherrington named the junction between neurons the synapse (1897) and in *The Integrative Action of the Nervous System* (1906) inferred its properties from the behavior of reflexes: delay, summation, inhibition and fatigue. He shared the Nobel Prize of 1932 with Edgar Adrian, who showed that nerve fibers signal stimulus strength by the frequency of all-or-none impulses. Transmission is discontinuous, and it occurs in two forms ([7.14.5](/7.14.5#sec-5.4.1), [7.16.10](/7.16.10#sec-10.5)).

At a **chemical synapse**, the presynaptic action potential opens voltage-gated $\ce{Ca^2+}$ channels, and $\ce{Ca^2+}$ triggers the fusion of vesicles that release a **neurotransmitter** in packets of nearly fixed size (**quantal release**, [7.14.8](/7.14.8#sec-8.3), [7.16.9](/7.16.9#sec-9.2)). At an **electrical synapse**, **gap junctions** connect the cytoplasm of the two cells, and current flows directly. The two forms are design alternatives with different strengths:

| Property | Chemical synapse | Electrical synapse |
|---|---|---|
| Delay | About $0.3$–$1\,\mathrm{ms}$ (release machinery) | Virtually none (below $0.1\,\mathrm{ms}$) |
| Sign | Excitatory or inhibitory, depending on the receptor | Follows the presynaptic voltage (sign-preserving) |
| Gain | Can amplify: a small terminal can drive a large cell | No amplification; a small cell cannot drive a large one |
| Direction | One way | Often two way; some junctions rectify |
| Plasticity and modulation | Extensive: short- and long-term plasticity, many modulators | More limited, although coupling can be modulated |
| Typical behavioral use | Almost all computation | Speed and synchrony |

The table explains where electrical synapses are found in behavior. The first is speed. The first electrical synapse to be demonstrated, by Furshpan and Potter (1959), connects the lateral giant interneuron of the crayfish to the giant motor neuron of the tail flexor muscles; it rectifies, passing current only forward, so that the escape command reaches the muscles with no synaptic delay ([7.18.14](/7.18.14)). The Mauthner cell of fishes receives mixed electrical and chemical input from the auditory nerve, and the giant fiber of *Drosophila* drives the motor neuron of the jump muscle through a mixed synapse whose electrical component depends on the innexin *shaking-B*.

The second use is synchrony: cells that are electrically coupled fire together, so that their output adds up in time. In *Aplysia*, the motor neurons of the ink gland are coupled, so that a strong noxious stimulus releases the whole ink cloud at once; the neuroendocrine bag cells, also coupled, fire together for about half an hour and release the egg-laying hormone that triggers the long sequence of egg-laying behavior. In weakly electric fish, the neurons of the medullary pacemaker nucleus are electrically coupled, which keeps the electric organ discharge regular to within microseconds ([7.18.15](/7.18.15)). Synchrony is also the reason electrical coupling is common in developing circuits and in networks that generate rhythms.

### 6.3.3. The Ionic Basis of the Action Potential

Galvani's *Commentary on the Effect of Electricity on Muscular Motion* (1791) began the study of animal electricity; the controversy with Volta, and the work of du Bois-Reymond, Helmholtz and Bernstein that followed, are told in [7.14.4](/7.14.4#sec-4.1). The decisive experiments were made possible by an animal chosen exactly as Krogh's principle recommends. J. Z. Young (1936) drew attention to the giant axon of the squid, up to about $1\,\mathrm{mm}$ in diameter, into which a wire electrode could be inserted lengthwise. With it, Hodgkin and Huxley recorded the overshoot of the **action potential** (1939) and, using the **voltage clamp**, separated the $\ce{Na+}$ and $\ce{K+}$ currents and built the quantitative model of 1952 ([7.14.4](/7.14.4#sec-4.7.2), [7.16.5](/7.16.5)).

The giant axon was convenient for the experimenters, but it exists because of behavior: it is the final common path of the squid's escape jet. Giant axons in the stellar nerves activate the circular muscles of the mantle, which contract and expel water through the funnel; axons to the far end of the mantle are thicker and therefore faster, so that all parts of the mantle contract nearly at once ([7.14.4](/7.14.4#sec-4.10.1)). The technical gift to physiology is a by-product of selection for speed.

In vertebrates the same speed is achieved by **myelin** and **saltatory conduction**: the action potential is regenerated only at the **nodes of Ranvier**, the myelinated internodes between them being charged quickly by passive current. Myelin increases conduction velocity, reduces the energy cost of each impulse and, because the node just excited is refractory, helps keep propagation one-way ([7.14.4](/7.14.4#sec-4.9)).

The action potential is produced by a few kinds of voltage-gated channels, but the genome encodes many. In humans, the superfamily of voltage-gated-like **ion channels** comprises about 140 genes ($\mathrm{Na_V}$, $\mathrm{Ca_V}$, $\mathrm{K_V}$, $\ce{Ca^2+}$-activated $\ce{K+}$ channels, inward rectifiers, HCN, cyclic nucleotide-gated and TRP channels and others; Yu and Catterall, 2004). This diversity gives different neurons their firing patterns ([7.16.5](/7.16.5#sec-5.4)), and it gives receptors their sensitivities: TRP channels sense temperature and chemical irritants, mechanically gated channels touch and sound ([7.18.9](/7.18.9)). Two techniques made channels visible as molecules. The **patch clamp** of Neher and Sakmann (1976; Nobel Prize 1991) recorded the current through a single channel, a step of a few picoamperes, and the crystal structure of the bacterial $\ce{K+}$ channel KcsA solved by MacKinnon's group (Doyle et al., 1998; Nobel Prize in Chemistry 2003) showed how a channel selects $\ce{K+}$ over $\ce{Na+}$ ([7.16.4](/7.16.4#sec-4.1)).

### 6.3.4. Speed as a Design Problem

Escape is a race. The prey must start moving before the predator's strike arrives, and the time between detection and movement, the escape latency, is the sum of delays at each stage: sensory transduction, conduction to the central nervous system, synaptic delays in the circuit, conduction to the muscles and the latency of muscle contraction. Conduction time is the part most sensitive to body size, because it is the length of the path divided by the conduction velocity.

The velocity of an unmyelinated axon grows only with the square root of its diameter $d$, whereas that of a myelinated fiber grows in proportion to $d$ ([7.14.4](/7.14.4#sec-4.9.3)). Taking the squid giant axon ($d \approx 500\,\mu\mathrm{m}$, $v \approx 25\,\mathrm{m\,s^{-1}}$) to calibrate the first relation and Hursh's rule (about $6\,\mathrm{m\,s^{-1}}$ per micrometer of fiber diameter in mammals) for the second,

$$
v_{\mathrm{u}} \approx 1.1\,\mathrm{m\,s^{-1}}\sqrt{d/\mu\mathrm{m}}, \qquad v_{\mathrm{m}} \approx 6\,\mathrm{m\,s^{-1}}\;(d/\mu\mathrm{m}).
$$

**Example 6.3.1 (Conduction Time and Escape)** A squid's mantle is about $0.2\,\mathrm{m}$ long. How long does an impulse take to travel this distance in its giant axon, in an unmyelinated axon of $10\,\mu\mathrm{m}$ and in a myelinated fiber of $10\,\mu\mathrm{m}$? What diameter would an unmyelinated axon need to cover $0.2\,\mathrm{m}$ in $2\,\mathrm{ms}$?

In the giant axon, $t = 0.2/25 = 8\,\mathrm{ms}$. An unmyelinated $10\,\mu\mathrm{m}$ axon conducts at $1.1\sqrt{10} \approx 3.5\,\mathrm{m\,s^{-1}}$ and needs $57\,\mathrm{ms}$, far too slow for an escape from a fish strike lasting a few tens of milliseconds. A myelinated $10\,\mu\mathrm{m}$ fiber conducts at about $60\,\mathrm{m\,s^{-1}}$ and needs $3.3\,\mathrm{ms}$. To cover $0.2\,\mathrm{m}$ in $2\,\mathrm{ms}$ requires $v = 100\,\mathrm{m\,s^{-1}}$; an unmyelinated axon would need $d = (100/1.1)^2\,\mu\mathrm{m} \approx 8\,\mathrm{mm}$, wider than the nerve cord of most animals, whereas a myelinated fiber of about $17\,\mu\mathrm{m}$ suffices. The cross-sectional area of the unmyelinated axon would be about $2\times10^5$ times larger.

:::

The calculation explains three facts of comparative neurobiology. Giant axons are found in invertebrates whose escape requires speed but whose bodies are short (squid, crayfish, earthworms, cockroaches); a few giant axons can be afforded, many cannot. Vertebrates, with long bodies and thousands of fast pathways, rely on myelin. And the invertebrates that need high speed in many fibers, such as copepods that jump away from predators within a few milliseconds and penaeid shrimps, evolved myelin-like sheaths of their own ([7.14.4](/7.14.4#sec-4.10.2)). Conduction is only part of the latency: synaptic delays add about $0.5$–$1\,\mathrm{ms}$ per chemical synapse, which is why escape circuits have few synapses and use electrical ones where possible. In the fastest escapes, the C-start of fishes triggered by the Mauthner cell, movement begins about $5$–$10\,\mathrm{ms}$ after an abrupt sound ([7.18.14](/7.18.14)).

![Conduction speed as a constraint on escape. A: time to conduct over the $0.2\,\mathrm{m}$ length of a squid's mantle as a function of fiber diameter, for unmyelinated axons ($v \approx 1.1\sqrt{d}$, calibrated by the squid giant axon, square) and myelinated fibers ($v \approx 6d$, Hursh's rule for mammalian fibers at $37\,^\circ\mathrm{C}$). The shaded band marks the few milliseconds available in a fast escape. B: diameter needed to cover distances from $1\,\mathrm{cm}$ to $1\,\mathrm{m}$ within a $2\,\mathrm{ms}$ budget. Unmyelinated diameters (and their cross-sectional areas, which grow with the fourth power of the distance) become impossible for large animals, whereas myelinated diameters remain within the range of ordinary fibers.](./plots/escape-latency.py)

## 6.4. Neurotoxins: Chemical Weapons Aimed at Channels

### 6.4.1. Why Channels Are Targets

The features that make channels and receptors good for behavior, speed and the dependence of every movement on a few kinds of molecules, also make them the Achilles heel of animals. A molecule that blocks the $\ce{Na+}$ channels of nerve and muscle stops all movement, including breathing, within minutes. It is no surprise that many organisms have evolved toxins aimed at channels, to defend themselves against predators (poisons, often in the skin or tissues) or to subdue prey (venoms, injected by a bite or sting); the distinction and the behavioral ecology of chemical defense are treated in [7.18.24](/7.18.24).

**Definition 6.4.1 (Neurotoxin)** A **neurotoxin** is a substance produced by an organism that disrupts the function of nervous tissue at low concentration, usually by binding with high affinity and specificity to an ion channel, a receptor, a transporter or the release machinery.

Neurotoxins have been as useful to neuroscience as giant axons. Tetrodotoxin (TTX) blocks voltage-gated $\ce{Na+}$ channels and so separates $\ce{Na+}$ currents from others; α-bungarotoxin, from the venom of the many-banded krait (*Bungarus multicinctus*), binds the **nicotinic acetylcholine receptor** of muscle almost irreversibly and was used to count, locate and purify it; ω-conotoxins identified the N-type $\ce{Ca^2+}$ channels of nerve terminals. Toxins are grouped by chemistry:

| Toxin | Producer (and carrier) | Target and action | Poisoning |
|---|---|---|---|
| Tetrodotoxin (TTX) | Bacteria (in pufferfish, newts, blue-ringed octopus, some frogs and flatworms) | Blocks the pore of $\mathrm{Na_V}$ channels | Pufferfish poisoning |
| Saxitoxin | Dinoflagellates and cyanobacteria (accumulated by shellfish) | Blocks the pore of $\mathrm{Na_V}$ channels | Paralytic shellfish poisoning |
| Brevetoxin, ciguatoxin | Dinoflagellates (*Karenia*, *Gambierdiscus*) | Shift $\mathrm{Na_V}$ activation, causing repetitive firing | Neurotoxic shellfish poisoning, ciguatera |
| Batrachotoxin | Poison frogs (*Phyllobates*) and birds (*Pitohui*), probably from melyrid beetles in the diet | Holds $\mathrm{Na_V}$ channels open | — |
| Grayanotoxin | Rhododendrons and other heaths (also in their honey) | Holds $\mathrm{Na_V}$ channels open | "Mad honey" poisoning |
| Domoic acid | Diatoms (*Pseudo-nitzschia*) and red algae | Agonist of kainate- and AMPA-type glutamate receptors; excitotoxic | Amnesic shellfish poisoning |
| Palytoxin | Zoanthid corals (*Palythoa*), dinoflagellates (*Ostreopsis*) | Converts the $\ce{Na+}/\ce{K+}$-ATPase into an open channel | — |
| Maitotoxin | Dinoflagellates (*Gambierdiscus*) | Massive $\ce{Ca^2+}$ entry through a target still debated | Ciguatera |
| Scorpion α- and β-toxins | Scorpions (peptides) | Slow $\mathrm{Na_V}$ inactivation (α) or shift its activation (β) | Scorpion sting |
| Charybdotoxin, iberiotoxin | Scorpions (peptides) | Block $\ce{Ca^2+}$-activated $\ce{K+}$ channels (BK) and some $\mathrm{K_V}$ | — |
| Apamin | Honey bee venom (peptide) | Blocks small-conductance $\ce{Ca^2+}$-activated $\ce{K+}$ channels (SK) | — |
| Hanatoxin | Tarantula venom (peptide) | Modifies the gating of $\mathrm{K_V}2$ and $\mathrm{K_V}4$ channels | — |
| ShK | Sea anemone (*Stichodactyla helianthus*) | Blocks $\mathrm{K_V}1.3$ | — |
| Conotoxins (α, δ, κ, μ, ω) | Cone snails (peptides) | Block muscle nicotinic receptors (α), delay $\mathrm{Na_V}$ inactivation (δ), block $\mathrm{K_V}$ (κ), block muscle $\mathrm{Na_V}1.4$ (μ), block N-type $\mathrm{Ca_V}2.2$ (ω) | Cone snail sting |
| α-Bungarotoxin, α-cobratoxin | Elapid snakes (kraits, cobras; peptides) | Antagonists of muscle nicotinic receptors | Snakebite paralysis |

Two features of the table are worth noting. Many toxins are not made by the animals that carry them: TTX in pufferfish is made by bacteria and accumulated through the food chain, and the batrachotoxins of poison frogs and pitohuis come from their insect diet. And unrelated toxins converge on the same few targets: at least six classes of molecule act on $\mathrm{Na_V}$ channels, at different binding sites, because no other target stops nerve and muscle as quickly. Domoic acid, in contrast, acts on glutamate receptors of the brain and causes seizures and loss of memory; after an outbreak from mussels in Canada in 1987, the same toxin was found to cause seizures and stranding in California sea lions that eat contaminated anchovies.

![Targets of neurotoxins, drawn on one schematic membrane (outside above) although the targets lie in different places: $\mathrm{Na_V}$ and $\mathrm{K_V}$ channels in axons, $\ce{Ca^2+}$-activated $\ce{K+}$ channels and N-type $\ce{Ca^2+}$ channels in nerve terminals, nicotinic receptors at the neuromuscular junction, kainate and AMPA receptors in the brain, and the $\ce{Na+}/\ce{K+}$-ATPase in all cells. Blockers are marked with inhibition bars and activators (toxins that open channels, prolong their opening or, for palytoxin, turn the pump into an open channel) with open arrows. Voltage-gated $\ce{Na+}$ channels are the target of the largest number of unrelated toxins.](./plots/toxin-targets.py)

### 6.4.2. Venoms as Behavioral Tools

A venom is not a single toxin but a cocktail, deployed by behavior. Cone snails (*Conus*, about 900 species) each inject a mixture of 100 or more peptides through a harpoon-like radular tooth. Fish-hunting species combine toxins into functional groups that Baldomero Olivera called cabals. The "lightning-strike cabal" (δ- and κ-conotoxins) causes immediate, massive excitation and tetanic paralysis around the injection site, so that a speared fish cannot swim away; the "motor cabal" (α-, μ- and ω-conotoxins) blocks neuromuscular transmission more slowly and completely. Some net-hunting species release into the water a "nirvana cabal" that sedates a school of fish, including a specialized fish-like insulin that causes hypoglycemic shock (Safavi-Hemami et al., 2015), before engulfing them with the expanded mouth. The geography cone (*Conus geographus*) produces separate venoms for predation and for defense, the defensive one rich in toxins that paralyze vertebrate muscle, and switches between them according to whether it is hunting or threatened (Dutertre et al., 2014). The composition of the venom is thus part of the behavioral strategy.

### 6.4.3. The Evolution of Resistance

Toxins select for resistance in the animals that carry them, the predators that eat them and the prey that are attacked by them. The most common mechanism is a change in the target itself.

**Definition 6.4.2 (Target-Site Insensitivity)** **Target-site insensitivity** is resistance to a toxin conferred by amino acid substitutions in the toxin's molecular target (a channel, receptor or enzyme) that reduce its affinity for the toxin while preserving the target's normal function.

Pufferfish are resistant to their own TTX because their $\mathrm{Na_V}$ channels carry substitutions in the pore loops that bind the toxin (Venkatesh et al., 2005; Jost et al., 2008). The best-studied case of resistance in a predator involves the common garter snake (*Thamnophis sirtalis*) and the rough-skinned newt (*Taricha granulosa*) of western North America, studied by Edmund Brodie Jr., Edmund Brodie III and colleagues. The newt's skin contains enough TTX to kill several humans, yet some garter snake populations eat newts. Resistance was measured with a behavioral assay: snakes are timed crawling along a racetrack before and after an injection of TTX, and resistance is the dose that reduces crawl speed by half. Snakes from populations sympatric with toxic newts tolerate doses hundreds of times higher than snakes from populations without them, and the resistance maps to a few substitutions in the domain IV pore loop of the skeletal muscle channel $\mathrm{Na_V}1.4$ (Geffeney et al., 2002, 2005). The same or equivalent substitutions arose independently in other snake lineages that eat toxic amphibians (Feldman et al., 2012), a case of **convergent evolution** at the molecular level, and newt toxicity tracks snake resistance across populations, as expected of an **evolutionary arms race** with a geographic mosaic of hot and cold spots ([7.10.17](/7.10.17), [7.18.24](/7.18.24)).

Resistance has costs. The most resistant snakes crawl more slowly even without toxin (Brodie and Brodie, 1999), probably because the substitutions also change the channel's kinetics, and a snake that has eaten a newt may be immobilized for hours, exposed to its own predators. Resistance can also be turned into an advantage: the southern grasshopper mouse (*Onychomys torridus*) preys on bark scorpions (*Centruroides*), whose venom activates the $\mathrm{Na_V}1.7$ channels of pain-sensing neurons. In the mouse, amino acid variants of $\mathrm{Na_V}1.8$, the channel that carries the action potential of these neurons, are inhibited by a venom component, so that the venom blocks the very pain it should cause (Rowe et al., 2013). The monarch butterfly, which stores cardenolides from milkweeds, carries substitutions in the $\ce{Na+}/\ce{K+}$-ATPase that make it insensitive to them; introducing the same three substitutions into *Drosophila* by genome editing made flies resistant, and able to store the toxins, as monarchs do (Karageorgi et al., 2019).

![Target-site insensitivity to tetrodotoxin (illustrative values). A: fraction of the $\ce{Na+}$ current remaining as a function of TTX concentration, $I/I_0 = 1/(1 + [\mathrm{TTX}]/K_{\mathrm{d}})$, for a sensitive channel ($K_{\mathrm{d}} = 10\,\mathrm{nM}$, typical of nerve and muscle $\mathrm{Na_V}$ channels), a moderately resistant channel ($K_{\mathrm{d}} = 300\,\mathrm{nM}$) and a highly resistant channel ($K_{\mathrm{d}} = 10\,\mu\mathrm{M}$), as found in pufferfish and in garter snakes from populations that eat toxic newts. B: the corresponding whole-animal assay: crawl speed of snakes on a racetrack after injection of TTX, relative to their speed before, for a population without and a population with toxic newts. The dose that halves speed (dashed line) is the measure of resistance; the resistant population is slower before injection, a cost of resistance (the lower starting point of its curve).](./plots/ttx-resistance.py)

## 6.5. Methods of Neuroethology

The methods of neurobiology are described in [7.16.3](/7.16.3); here we list them by the question each answers about behavior.

| Method | What it shows | Example in this course |
|---|---|---|
| Lesion and electrical stimulation | Whether a region is necessary for, or can evoke, a behavior | Hypothalamic feeding and attack ([7.18.8](/7.18.8)); songbird nuclei ([7.18.17](/7.18.17)) |
| Tract tracing (horseradish peroxidase, dyes, viruses) | Which neurons project where | The input to the pacemaker nucleus of electric fish ([7.18.15](/7.18.15)) |
| Extracellular and intracellular recording, in restrained or freely moving animals | What neurons signal and when, relative to stimulus and behavior | Moth auditory receptors ([7.18.12](/7.18.12)); place cells in flying bats ([7.18.21](/7.18.21)) |
| **Patch clamp** | Currents and channels of single neurons | Channel properties of escape neurons |
| **Calcium imaging** | Activity of hundreds to thousands of identified neurons at once | Whole-brain imaging in larval zebrafish during prey capture |
| Genetic access (Gal4–UAS, Cre lines, genome editing) | Which cell type matters; manipulation of single genes | *Drosophila* courtship and aggression ([7.18.7](/7.18.7), [7.18.19](/7.18.19)) |
| **Optogenetics** and chemogenetics | Whether activity of a cell type is necessary or sufficient, with millisecond timing | Fear and feeding circuits ([7.18.8](/7.18.8)) |
| **Connectome** reconstruction by electron microscopy | The complete wiring of a circuit | *C. elegans*, *Drosophila* larva and adult brain |
| Quantitative behavior (high-speed video, pose estimation, playback, virtual reality) | What the animal does and which stimuli control it | Fly escape takeoffs ([7.18.14](/7.18.14)); phonotaxis treadmills ([7.18.16](/7.18.16)) |

The methods give three kinds of evidence about a link between neurons and behavior, and a convincing case usually needs all three:

1. *correlation*: the activity of the neuron changes with the stimulus or precedes the behavior;
2. *necessity*: removing or silencing the neuron abolishes or impairs the behavior;
3. *sufficiency*: activating the neuron, in the absence of the natural stimulus, produces the behavior.

The logic is that of the command neuron concept ([7.18.14](/7.18.14)). Each kind of evidence has its pitfalls: a correlated neuron may be a bystander; silencing one region may disrupt others that depend on it, or the circuit may compensate during a chronic lesion; and artificial activation may produce a behavior through a route never used naturally. Modern work therefore records activity during natural behavior, silences or activates genetically defined cell types acutely and with the timing of the behavior, and checks the results against the animal's behavior in its own environment, where possible with telemetry in the field.

## Summary

- **Neuroethology** (Definition 6.1.1) studies the neural mechanisms of natural behavior; its object is natural behavior, its goal the neural mechanism, its foundation quantitative behavior combined with neurophysiology and neurogenetics.
- Behavior is analyzed as a hierarchy of levels of integration and quantified by rate, duration and intensity. The nervous system serves behavior by sensation, integration and movement.
- Krogh's principle (Definition 6.2.1): for many problems there is an animal in which they are best studied. Specialist species exaggerate a function; genetic model organisms give access to cell types. Identified neurons (Definition 6.2.2) allow results from many individuals to be combined.
- The three foundations, the **neuron doctrine**, synaptic transmission and the ionic basis of the **action potential**, were established in part with animals chosen for convenience (the squid giant axon), whose features exist because of behavior (the escape jet).
- **Chemical synapses** compute (sign, gain, plasticity, modulation); **electrical synapses** provide speed and synchrony (crayfish escape, *Aplysia* inking and egg laying, the electric fish pacemaker).
- Conduction velocity grows with $\sqrt d$ in unmyelinated and with $d$ in myelinated fibers (Example 6.3.1): giant axons serve short invertebrates, myelin long-bodied vertebrates and fast-jumping crustaceans.
- Neurotoxins (Definition 6.4.1) converge on a few targets, above all $\mathrm{Na_V}$ channels; venoms are cocktails deployed by behavior (cone snail cabals). Toxins select for target-site insensitivity (Definition 6.4.2): pufferfish, garter snakes, grasshopper mice and monarch butterflies, with costs and a geographic mosaic of the arms race.
- Links between neurons and behavior require correlation, necessity and sufficiency, ideally tested during natural behavior.

## Questions

1. A colleague says: "Nothing in neuroscience makes sense except in the light of behavior." Do you agree? Give one example where knowledge of the behavior was needed to understand a neural mechanism, and one where a neural finding changed how a behavior was understood.

   **Answer** Behavior first: the tuning of moth auditory receptors and the toad's prey-selective neurons can only be interpreted once the natural stimuli (bat calls, the shapes of worms and of predators) and the behavioral responses are known; without them, the response properties would be arbitrary numbers ([7.18.12](/7.18.12), [7.18.13](/7.18.13)). Neural finding first: the discovery that the dopamine response of midbrain neurons behaves like a reward prediction error reinterpreted reward-driven behavior, such as blocking in conditioning, in terms of a teaching signal ([7.16.37](/7.16.37)). The statement is a useful corrective to purely reductionist programs, but it is not literally true: properties of channels and synapses, such as their biophysics, can be understood without reference to behavior, and they constrain which behaviors are possible.

2. What are the limits of the research paradigm of modern neuroscience, based on genetic model organisms, restrained animals and laboratory tasks, for understanding behavior?

   **Answer** Points to discuss: (a) laboratory tasks may engage circuits differently from natural behavior, and the variety of natural behavior (social interactions, navigation over kilometers, seasonal changes) is hard to reproduce; (b) a few species represent a tiny and biased sample of animal diversity, so that specializations (echolocation, electroreception, magnetoreception) and convergent solutions are missed, whereas comparisons across species are the basis of evolutionary explanations; (c) restraint, head fixation and anesthesia change the state of the brain; (d) necessity and sufficiency tests in a circuit that compensates or that has many parallel paths can mislead. Remedies include wireless recording in freely moving animals (bats, birds), field studies, new genetic tools for non-model species, and behavioral analysis with machine vision.

3. Why do escape circuits so often use giant axons and electrical synapses, whereas most circuits in the brain use thin axons and chemical synapses?

   **Answer** Escape is a race in which a millisecond can decide survival, and the latency of the response is dominated by conduction time and synaptic delays. Giant axons raise conduction velocity (as $\sqrt d$), and electrical synapses eliminate the $0.5$–$1\,\mathrm{ms}$ delay of chemical release. Both have costs that are acceptable for one or a few pathways but not for the whole brain: giant axons occupy volume, and electrical synapses cannot invert signs, amplify, or support the plasticity and modulation that most computations need. Escape circuits also have few stages and a simple decision, so they need little computation.

4. Using Example 6.3.1, estimate the conduction time from the head to the tail of a $1\,\mathrm{m}$ fish along a myelinated fiber of $15\,\mu\mathrm{m}$ diameter, and the diameter of an unmyelinated axon that would conduct equally fast. Assume the vertebrate fiber at the fish's body temperature conducts at half the mammalian rate.

   **Answer** At $37\,^\circ\mathrm{C}$ the fiber would conduct at $6 \times 15 = 90\,\mathrm{m\,s^{-1}}$; at half this rate, $45\,\mathrm{m\,s^{-1}}$, and the conduction time is $1/45\,\mathrm{s} \approx 22\,\mathrm{ms}$. An unmyelinated axon with $v = 45\,\mathrm{m\,s^{-1}}$ would need $d = (45/1.1)^2 \approx 1700\,\mu\mathrm{m}$, about $1.7\,\mathrm{mm}$. Such a diameter is impossible for the thousands of fast fibers of a vertebrate, which is why the axons of the reticulospinal neurons that trigger escape, including the Mauthner axon that runs the length of the spinal cord, are myelinated.

5. Garter snakes resistant to TTX crawl more slowly than non-resistant snakes. What does this cost imply about the distribution of resistance among populations, and what observations would test the explanation?

   **Answer** If resistance carries a cost, selection should favor it only where toxic newts are common and toxic enough for the benefit (access to a food that other predators cannot use, survival after eating toxic prey) to exceed the cost (slower locomotion, perhaps higher predation). Resistance should then vary among populations with the toxicity of local newts, high in hot spots of the arms race and low where newts are absent or weakly toxic, and resistance alleles should be rare or absent where newts are absent. Tests: measure newt TTX and snake resistance across many localities (they covary in nature); genotype the $\mathrm{Na_V}1.4$ alleles across this range; measure crawl speed and survival of snakes with different alleles in the field; and measure the functional properties of resistant channels to identify the mechanism of the cost.

6. A neuron in a moth's thoracic ganglion fires just before the moth dives in response to bat calls. What experiments would establish that the neuron is part of the circuit that causes the dive?

   **Answer** Three kinds of evidence are needed. Correlation: record the neuron in freely flying or tethered moths and show that its activity reliably precedes and predicts dives, with appropriate latency, and is driven by the ultrasonic receptors. Necessity: silence or ablate the neuron (or its genetic equivalent, if accessible) and show that dives are reduced or abolished while other flight behavior remains normal. Sufficiency: stimulate the neuron in the absence of ultrasound and show that it evokes a dive or its motor pattern. Each test has pitfalls (bystander neurons, compensation, unnatural activation), so the experiments should be acute and repeated with natural stimuli.
