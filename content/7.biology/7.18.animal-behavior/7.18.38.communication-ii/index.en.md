---
title: "Communication II: Signal Production, Transmission and Sensory Drive"
description: "The physics of signals in each channel: producing sound (stridulation, tymbals, vocal folds and the syrinx, swim bladders, percussion), the source–filter principle and the efficiency of small radiators; sound propagation (spreading, absorption, scattering, reverberation, the deep sound channel), noise and masking, urban noise and the acoustic adaptation hypothesis; pigmentary, structural and bioluminescent color, color change, measuring color through the receiver's eyes and the light environments of forests and water; chemical signals, volatility and active space; touch, vibration, hydrodynamic and electric signals; sensory drive in sticklebacks, cichlids and guppies; a comparison of channels and multimodal signals."
---

The previous chapter treated a receiver as a decision maker that uses signals to estimate conditions it cannot observe. Whether a signal reaches the receiver at all, and how clearly, depends on physics: on how efficiently the sender can produce energy in a given modality, on what the medium does to the signal on its way, and on the background against which the receiver must detect it. These constraints concern the *efficacy* of signals ([7.18.37](/7.18.37#sec-37.2)), and they explain a large part of signal diversity: why insects stridulate at high frequencies and whales moan at low ones, why forest birds whistle and grassland birds trill, why tropical forest birds display in particular patches of light, and why ants use different compounds for alarm and for trails.

This chapter follows each sensory channel from the sender to the receiver. Reception was treated in the chapters on sensory worlds, which this one complements: chemical senses in [7.18.9](/7.18.9), vision in [7.18.10](/7.18.10), mechanoreception and hearing in [7.18.11](/7.18.11) and electroreception in [7.18.15](/7.18.15). The physics of waves is in the physics courses (sound waves, [5.1.7](/5.1.7)); the production of sound and light by insects and the Bossert–Wilson model of pheromone diffusion are described in [7.17.27](/7.17.27). The chapter ends with *sensory drive*, the coevolution of signals, sense organs and habitats, which links the physics of communication to the origin of species, and with the use of several channels at once.

## 38.1. Design for Detection

Whatever the modality, a signal must stand out against noise at the position of the receiver. Its detectability depends on four factors: the energy emitted by the sender, the attenuation and distortion during propagation, the noise in the environment, and the sensitivity and filtering of the receiver's sense organs. A receiver can detect a signal only where the signal-to-noise ratio in the frequency band, wavelength range or chemical channel to which it is tuned exceeds some threshold. Senders can improve detection in several ways, each with costs:

- *Increasing power*: a louder call, a brighter patch, a larger amount of pheromone. Power is costly and limited by the size of the sender.
- *Matching the channel*: concentrating energy in the frequencies, wavelengths or compounds that propagate best and that the receiver's sense organs are most sensitive to.
- *Contrast with the background*: choosing frequencies where noise is low, colors that contrast with the background, compounds that are rare in the environment.
- *Redundancy*: repeating the signal, making it stereotyped and predictable, which allows the receiver to integrate over time and to use templates (a *matched filter* in the language of signal processing).
- *Alerting components*: a conspicuous introductory element that draws the receiver's attention before the information-bearing part of the signal.

The relative importance of these strategies differs among channels because the physics of each medium differs. The following sections take the channels in turn.

## 38.2. Sound

### 38.2.1. Producing Sound

Sound is a pressure wave produced by a vibrating object that moves the surrounding medium. Animals make sound in five main ways.

- *Stridulation*: a toothed file is drawn across a scraper, and each tooth impact excites a vibration. Crickets and katydids stridulate with their forewings, grasshoppers with a hind leg against the wing, many beetles and ants with body segments ([7.17.27](/7.17.27#sec-27.6.1)). In crickets the impacts drive a resonant wing area, the harp, so that the song is a nearly pure tone at the harp's resonant frequency ([7.18.16](/7.18.16#sec-16.1.2)).
- *Tymbals*: cicadas buckle a ribbed membrane on the abdomen with a fast muscle; each buckling produces a click, and an air sac in the abdomen acts as a resonator ([7.17.27](/7.17.27#sec-27.6.2)).
- *Airflow*: in mammals and frogs, air forced from the lungs sets the vocal folds of the larynx into self-sustained oscillation; in birds, the source is the **syrinx** at the junction of the bronchi, which has two independently controlled sides and can produce two unrelated sounds at once ([7.18.17](/7.18.17#sec-17.3.1)). Some insects, such as the hissing cockroaches of Madagascar, expel air through spiracles.
- *Swim bladder drumming*: many fishes vibrate the **swim bladder** with sonic muscles attached to it. The sonic muscles of toadfishes contract at about 200 Hz and are among the fastest vertebrate muscles known (Rome and colleagues 1996).
- *Percussion*: striking the substrate or a body part: woodpeckers drumming on resonant branches, kangaroo rats drumming with their feet, termite soldiers banging their heads on the walls of galleries.

In almost all of these mechanisms the sound produced by the source is modified by structures that act as filters or resonators, a principle formalized for the human voice as the *source–filter theory*. The vibrating vocal folds produce a periodic source whose spectrum contains the fundamental frequency $F_0$ and its harmonics; the vocal tract above the larynx acts as a filter whose **resonances**, the *formants*, emphasize some harmonics and suppress others. For a tube of length $L$ closed at one end, the formants lie at $F_i = (2i - 1)c/(4L)$, where $c$ is the speed of sound, so that their spacing, the *formant dispersion* $\Delta F = c/(2L)$, depends only on the length of the tract. Because the length of the vocal tract is constrained by body size, formant dispersion is a reliable indicator of size, which red deer and other mammals exploit and fake within limits ([7.18.39](/7.18.39)). In birds, the vocal tract can be tuned dynamically: songbirds widen the beak and expand the oropharyngeal cavity to track the frequency of a whistle, which suppresses harmonics and produces pure tones.

### 38.2.2. Size, Frequency and Efficiency

The frequencies that an animal can produce efficiently are limited by its size. A sound source radiates efficiently only if it is not small compared with the wavelength $\lambda = c/f$ it produces. For a small pulsating sphere of radius $a$ the fraction of the mechanical power that is radiated as sound rather than lost in moving the surrounding medium back and forth grows as $(ka)^2$, where $k = 2\pi/\lambda$, until $ka \approx 1$; above that, radiation is efficient. In air at 2 kHz, $\lambda \approx 17\,\mathrm{cm}$, and an insect whose radiating surface is a few millimeters across has $ka \approx 0.1$ and radiates only about 1% of the power that a large source would. Small animals therefore produce high frequencies: crickets of 2–3 cm call at 3–5 kHz, many katydids at 10–40 kHz and beyond, whereas large frogs, crocodiles and elephants use frequencies of tens to hundreds of hertz. Across species of frogs and of birds, the dominant frequency of calls decreases with body mass, approximately as a power of mass with an exponent around $-0.3$ to $-0.4$ (for birds, Ryan and Brenowitz 1985), close to what is expected if the dimensions of the sound-producing structures scale with linear body size.

The problem is worse for sources that vibrate like a plate open on both sides, such as a cricket's wing: the two faces move air in opposite phases, and around the edge of a small plate the pressure waves from front and back cancel, an *acoustic short circuit*. Some insects solve the problem with devices that would delight an acoustic engineer. Mole crickets (*Gryllotalpa*) sing from the mouth of a burrow that is shaped as a double horn; the horn matches the impedance of the small source to the air and increases the radiated power several times (Bennet-Clark 1987). Tree crickets (*Oecanthus*) chew a hole in the middle of a leaf and sing with their wings in the hole, using the leaf as a baffle that separates front and back; the gain depends on the size of the leaf and of the hole, and males make holes that give close to the maximal gain for the leaf they use (Mhatre and colleagues 2017).

![Why small animals call at high frequencies. A: radiation efficiency of a small spherical source, (ka)²/(1 + (ka)²), against frequency in air for source radii of 2 mm (a small insect), 1 cm (a cricket's wing or a small frog's vocal sac), 5 cm (a bird or large frog) and 20 cm (a large mammal); dashed lines mark ka = 1, above which radiation is efficient. B: the same scaling expressed as the frequency at which ka = 1 against source size, with typical call frequencies of some groups (horizontal bars) for comparison: small animals that call at low frequencies would waste most of their effort](./plots/radiation-efficiency.py)

### 38.2.3. Propagation

A sound weakens and changes shape on its way to the receiver.

- *Spreading*: in open space, the intensity of sound from a point source falls with the square of the distance, so the **sound intensity level** ([5.1.7](/5.1.7#def-7.8.2)) falls by 6 dB for each doubling of distance whatever the frequency.
- *Absorption*: air absorbs sound by molecular relaxation, with losses that increase roughly with the square of the frequency: about 0.005 dB per meter at 1 kHz and around 0.1 dB per meter at 10 kHz, depending on temperature and humidity. Ultrasound is therefore useful only at short range, a constraint that also limits the range of bat echolocation ([7.18.12](/7.18.12)).
- *Scattering and excess attenuation*: leaves, trunks and the ground scatter and absorb sound beyond spreading and atmospheric absorption. Scattering increases steeply with frequency once the wavelength becomes comparable with the size of the obstacles, so high frequencies are attenuated more in vegetation. Near the ground, interference between the direct sound and its reflection from the ground causes additional losses at low frequencies.
- *Reverberation*: in forests, echoes from trunks and leaves arrive after the direct sound and smear rapid amplitude and frequency modulations; trills and closely spaced notes lose their structure, whereas long, slowly modulated tones survive.
- *Amplitude fluctuations*: in open habitats, wind and the temperature gradients above sunlit ground refract sound and cause irregular fluctuations of amplitude over periods of tens of milliseconds to seconds, which mask slow amplitude modulations but not rapid ones.

The combined effect of spreading and excess attenuation can be written

$$
L(r) = L(r_0) - 20 \log_{10}\frac{r}{r_0} - \alpha(f)\,(r - r_0),
$$
where $L$ is the level in decibels at distance $r$, $r_0$ is a reference distance (usually 1 m) and $\alpha(f)$ is the excess attenuation coefficient in decibels per meter, which depends on frequency and habitat.

The distance at which a signal can be detected is the distance at which $L(r)$ falls to the level of the background noise in the receiver's frequency band, plus the margin needed for detection (the *critical ratio*). In a forest, where $\alpha$ rises steeply with frequency and low frequencies are masked by noise and ground effects, the range of detection is greatest in an intermediate band. Eugene Morton (1975) measured transmission in Panama and found a "sound window" around 1.5–2.5 kHz in which tones carried farthest in forest, and that forest birds sang lower and more tonal songs than birds of grassland and edge.

Water is a better medium for sound than air: sound travels at about $1500\,\mathrm{m\,s^{-1}}$, absorption at low frequencies is very small, and because the speed of sound in the ocean has a minimum at a depth of about 1 km, sound emitted near this depth is trapped in a *deep sound channel* (the SOFAR channel) and spreads in two dimensions rather than three. Fin whales (*Balaenoptera physalus*) and blue whales (*B. musculus*) produce intense calls of 15–20 Hz; Payne and Webb (1971) calculated that before the noise of ship engines filled the oceans such calls could have been heard over hundreds of kilometers, perhaps across ocean basins.

![Habitat, frequency and the range of a call (illustrative parameters). A: received level against distance for a call of 90 dB at 1 m in forest, at 2, 4 and 8 kHz, with spherical spreading and frequency-dependent excess attenuation; dotted lines mark the background noise plus the detection margin at each frequency, and the dashed line spreading alone. B: detection distance (where the received level falls to the noise level plus a critical ratio) against frequency in forest and in open grassland, and in grassland with low-frequency urban noise added. Forest favors an intermediate frequency band; low-frequency noise shifts the best frequency upward and shortens the range of low-pitched calls](./plots/sound-propagation.py)

### 38.2.4. Noise and Masking

Natural environments are noisy. Wind, rain, running water and surf produce broadband noise concentrated at low frequencies; insects and frogs produce choruses in particular frequency bands; and the songs of other birds compete for the same airspace. A receiver's ear acts as a bank of filters, and a signal is masked mainly by noise within the same filter band. Senders can therefore escape masking by shifting the frequency of the signal, by raising its amplitude, by changing its timing or by increasing its redundancy.

Human noise has turned these adjustments into a natural experiment. Traffic and industry produce noise concentrated below 2–3 kHz. Great tits (*Parus major*) in the city of Leiden sang songs whose lowest frequency was higher in noisier territories (Slabbekoorn and Peet 2003), and across ten European cities urban great tits sang shorter and faster songs with higher minimum frequencies than forest populations (Slabbekoorn and den Boer-Visser 2006). Birds also sing louder in noise, an adjustment known in humans as the *Lombard effect*: male nightingales (*Luscinia megarhynchos*) in Berlin increased the amplitude of their songs with the level of traffic noise (Brumm 2004). European robins (*Erithacus rubecula*) sing at night more often where daytime noise is high (Fuller, Warren and Gaston 2007). In the sea, North Atlantic right whales (*Eubalaena glacialis*) have shifted their contact calls to higher frequencies over decades of increasing shipping noise (Parks, Clark and Tyack 2007).

These changes show that individuals adjust their signals to noise, but they raise further questions. Are the adjustments learned or flexible responses of individuals, or genetic changes in urban populations? Great tits adjust song frequency within minutes when noise changes, so much of the change is plastic. And do the adjustments have costs? Lower-frequency songs are more attractive or more threatening in some species, so the shift may trade audibility against signal value: in great tits, females respond more strongly to the low-frequency songs of their mates, but in traffic noise these songs lose their effect (Halfwerk and colleagues 2011).

### 38.2.5. The Acoustic Adaptation Hypothesis

Morton's results suggested a general hypothesis.

**Definition 38.2.1 (Acoustic Adaptation Hypothesis)** The **acoustic adaptation hypothesis** states that the acoustic structure of long-range signals evolves to maximize their transmission in the habitat in which they are used: lower frequencies, narrower bandwidths and slower, tonal modulation in dense vegetation, and higher frequencies and rapid amplitude modulation (trills) in open habitats.

The hypothesis has found support within species, where populations in different habitats differ in song in the predicted ways: great tits in dense forests sing lower and purer songs than those in open woodlands (Hunter and Krebs 1979), and white-crowned sparrows and rufous-collared sparrows show habitat-related variation of song ([7.18.17](/7.18.17#sec-17.5.2)). Comparative tests across species are less consistent. A meta-analysis of studies on birds found that species of closed habitats tend to have lower frequencies, as predicted, but the effects on other song parameters were weak and inconsistent (Boncoraglio and Saino 2007). Song is shaped by many other factors (body size and beak shape constrain frequency and trill rate; sexual selection favors particular features; songs are learned and drift culturally), and habitat is only one of them. The acoustic adaptation hypothesis is therefore best regarded as one component of the more general framework of sensory drive (Section 38.6).

## 38.3. Light

### 38.3.1. Producing Color

Most visual signals reflect ambient light rather than producing it, and their color depends on which wavelengths are absorbed and which reflected. Animals produce color in three ways.

- *Pigments* absorb particular wavelengths. Carotenoids (yellow, orange, red) cannot be synthesized by animals and must be obtained from the diet; they are used for signals in birds, fishes and insects, and because their acquisition and deposition depend on foraging success and health, carotenoid colors are often condition dependent, as in the house finch ([7.18.2](/7.18.2)). Melanins (black, brown, rufous) are synthesized from tyrosine and are less tightly tied to diet. Other classes include the pterins of the yellow and white wings of pierid butterflies and of wasps, the psittacofulvins of parrots, and the porphyrins that give some eggshells and feathers their color.
- *Structural colors* arise from the interference, diffraction or scattering of light by nanostructures with dimensions comparable to the wavelength. Thin films and stacks of alternating layers, as in the scales of *Morpho* butterflies and the throat feathers of hummingbirds, reflect wavelengths that depend on the layer spacing and on the angle of view, producing iridescence. The noniridescent blue of bluebirds and kingfishers arises from coherent scattering by spongy keratin with air spaces of a characteristic size (Prum 2006). White is produced by incoherent scattering from disordered structures, as in the scales of white beetles.
- **Bioluminescence** is the emission of light by a chemical reaction, the oxidation of a luciferin catalyzed by an enzyme, luciferase ([6.4.10](/6.4.10)). It is used for signaling by fireflies, whose species-specific flash patterns attract mates and are exploited by predatory fireflies ([7.18.39](/7.18.39)), by many deep-sea fishes and crustaceans, and for counterillumination by squids that match the downwelling light with their photophores.

Colors can change on three time scales. Seasonal changes of plumage occur by molt, as in the breeding plumage of many birds. Hormonal changes over hours to days alter the dispersion of pigment in **chromatophores**, as in the nuptial colors of many fishes. Fastest are the neurally controlled chromatophores of cephalopods, which are expanded by radial muscles and can change the pattern of the skin within a fraction of a second for camouflage ([7.18.24](/7.18.24#sec-24.2.2)) or signaling: a male of the mourning cuttlefish (*Sepia plangon*) courting a female beside a rival can show courtship patterns on the side facing the female and female-like patterns on the side facing the rival (Brown, Garwood and Williamson 2012).

### 38.3.2. Measuring Color Through the Receiver's Eyes

Because animals see color differently from us ([7.18.10](/7.18.10#sec-10.4)), the color of a signal must be measured physically and then interpreted through a model of the receiver's visual system. A spectrophotometer measures the reflectance spectrum $R(\lambda)$ of the signal and of its background over the full range of wavelengths the receiver can see, including the ultraviolet. The light captured by photoreceptor class $i$ is

$$
Q_i = \int I(\lambda)\, R(\lambda)\, S_i(\lambda)\, \mathrm{d}\lambda,
$$
where $I(\lambda)$ is the spectrum of the ambient light and $S_i(\lambda)$ the spectral sensitivity of the photoreceptor, including the absorption of its **opsin** and of any filtering oil droplets. The difference between the catches for the signal and the background, scaled by the noise in each photoreceptor class, gives a distance in units of just-noticeable differences (the receptor-noise-limited model of Vorobyev and Osorio 1998): two colors more than about one unit apart can be discriminated under ideal conditions.

Such measurements have revealed signals invisible to humans. Blue tits (*Cyanistes caeruleus*), which look alike to us, are sexually dichromatic in the ultraviolet: the crown of males reflects more ultraviolet than that of females, and females prefer males with more ultraviolet-reflective crowns (Hunt and colleagues 1998; [7.18.10](/7.18.10#sec-10.4.2)). Damselfishes of the genus *Pomacentrus* recognize conspecifics by ultraviolet facial patterns that predators cannot see (Siebeck and colleagues 2010).

### 38.3.3. Light Environments

The ambient light against which a visual signal is seen varies among habitats and times of day. In forests, John Endler (1993) distinguished four main light environments: *forest shade*, where light is filtered by leaves and is rich in yellow-green; *woodland shade*, under small canopy openings, lit by blue sky and therefore bluish; *small gaps*, where direct sunlight passes through holes in the canopy and is rich in long wavelengths; and *large gaps*, lit by the full spectrum of daylight. Dawn and dusk add a purplish light.

A color patch is most conspicuous where its reflectance is high in the wavelengths that are abundant in the ambient light and where it contrasts with the background. Forest-dwelling birds of Central and South America display in particular light environments that enhance their colors: male white-throated manakins (*Corapipo gutturalis*), golden-headed manakins (*Ceratopipra erythrocephala*) and Guianan cocks-of-the-rock (*Rupicola rupicola*) display at lek sites and times at which the contrast between their plumage and the background is high (Endler and Théry 1996). Animals can also manipulate light: male guppies (*Poecilia reticulata*) in Trinidad court mostly at dawn and dusk, when the purplish light makes their orange and blue spots conspicuous to females but the low light makes them harder for predators to see (Endler 1987).

In water, light is absorbed and scattered more strongly than in air. In clear oceanic water, red light is absorbed within a few meters and the light at depth is blue; in lakes and coastal waters rich in dissolved organic matter and phytoplankton, blue and ultraviolet light is absorbed and the light at depth is shifted toward yellow, orange and red. Turbidity also reduces contrast with distance by scattering. Visual communication underwater is therefore short range and closely tuned to the local water color, which makes it a prime arena for sensory drive (Section 38.6).

## 38.4. Chemical Signals

### 38.4.1. Producing Chemical Signals

Chemical signals, the **pheromones** of animals ([7.14.43](/7.14.43#def-43.3.1), [7.18.9](/7.18.9#sec-9.5)), are the oldest form of communication and the only one that can persist after the sender has left. Their design is governed by a trade-off between volatility and persistence. Airborne signals that must travel far, such as the sex pheromones of moths, are compounds of intermediate size (typically with 10–20 carbon atoms and molecular masses of about 200–300 Da): large enough for specificity and to be detected at very low concentrations, small enough to evaporate. Alarm pheromones, which should spread quickly and fade soon after the danger is past, are often smaller and more volatile molecules, such as the short-chain ketones and aldehydes of ant alarm pheromones. Territorial marks, which should persist for days or weeks, are larger, less volatile molecules, often bound to proteins, such as the major urinary proteins of mice, which release their ligands slowly and themselves encode individual identity ([7.18.9](/7.18.9#sec-9.5.2)).

Specificity is achieved by molecular structure and, more often, by blends: two or more compounds in a characteristic ratio, such as the blends of moth pheromones whose ratio carries species identity ([7.18.9](/7.18.9#sec-9.5.1)). Many mammalian chemical signals are complex and variable mixtures of dozens of compounds that identify individuals, colonies or kin rather than species; Tristram Wyatt (2014) called these variable mixtures *signature mixtures*, to distinguish them from pheromones proper, which are the same in all members of a species or sex.

### 38.4.2. Active Space

The range of a chemical signal depends on how much is released, how sensitive the receiver is and how the medium moves.

**Definition 38.4.1 (Active Space)** The **active space** of a signal is the region around the sender within which the signal is above the receiver's threshold of response; for a chemical signal, the region in which the concentration exceeds the behavioral threshold $K$ of the receiver.

Bossert and Wilson (1963) calculated active spaces by solving the diffusion equation ([2.5.1](/2.5.1)) for instantaneous and continuous releases in still air and in wind ([7.17.27](/7.17.27#sec-27.4.4)). Two results are general. First, because concentration falls with distance in three dimensions, the radius of the active space grows only with the cube root of the ratio $Q/K$ of the amount released to the threshold: a thousandfold increase in emission enlarges the signal only tenfold. This explains why alarm pheromones with a small ratio $Q/K$ are local and short lived, while the sex attractant of a moth, released continuously and detected at extremely low thresholds, can attract males from tens to hundreds of meters downwind. Second, in moving air the active space of a continuous source becomes an elongated plume downwind, whose length depends on the wind speed and whose width on turbulence.

Real plumes are not smooth gradients but filamentous: turbulence breaks the odor into patches separated by clean air, and a male moth follows a plume by surging upwind when he encounters a filament and casting across the wind when he loses it ([7.18.9](/7.18.9#sec-9.4.4)). The intermittent structure is information: the frequency of encounters with filaments, rather than their concentration, tells the moth that it is in the plume.

### 38.4.3. Persistence, Trails and Marks

Because chemical signals persist, they can mark places and paths. Ants and termites lay trail pheromones from food sources to the nest; the trail evaporates within minutes unless reinforced, so that trails to rich food sources, which recruit more workers who reinforce them, persist, and trails to exhausted sources fade, a self-organizing system of foraging allocation ([7.18.40](/7.18.40)). Mammals deposit scent marks with urine, feces and glandular secretions along the boundaries of territories ([7.18.26](/7.18.26#sec-26.2.2)), where the marks advertise ownership in the owner's absence. The persistence that makes marks useful also limits them: a chemical signal cannot be switched off and cannot change rapidly with the sender's state, so chemical signals rarely carry information about momentary motivation.

## 38.5. Close-Range Channels

### 38.5.1. Touch and Substrate Vibration

Touch requires contact, so it is the channel of intimate interactions: allogrooming in primates, antennation in ants, the courtship tapping of many insects, and the communication of honey bees in the dark hive, where followers of a waggle dance obtain information by touching the dancer with their antennae ([7.18.40](/7.18.40)).

Substrate vibration extends touch to distances of centimeters to meters. Many insects, spiders and other arthropods communicate by vibrating plant stems, leaves, webs or the ground; an estimated 200,000 species of insects use vibrational signals (Cocroft and Rodríguez 2005), most of them small sap-sucking bugs such as treehoppers and leafhoppers whose signals are inaudible to us. Plant stems transmit bending waves, whose speed depends on frequency, so that signals are dispersed during propagation; the signals of treehoppers (*Enchenopa*) are pure tones well suited to this medium, and males and females duet to find each other along the plant. Male wolf spiders, fiddler crabs and many frogs combine vibrational signals with visual and acoustic ones, and elephants can detect the ground-borne components of low-frequency rumbles through their feet (O'Connell-Rodwell 2007). Vibration receptors are described in [7.18.11](/7.18.11#sec-11.2.2).

### 38.5.2. Hydrodynamic and Electric Signals

In water, a moving animal displaces the surrounding water, and fishes detect these near-field displacements with the **lateral line** ([7.18.11](/7.18.11#sec-11.2.3)). Courting male fishes quiver their bodies close to females, and schooling fish use the flow fields of neighbors to keep position. Hydrodynamic signals are limited to about one or two body lengths, because near-field displacements decline steeply with distance.

Weakly electric fishes communicate with the discharges of their **electric organs**, varying the frequency and waveform of the discharge and producing chirps and interruptions during courtship and aggression ([7.18.15](/7.18.15#sec-15.6)). Electric fields are quasi-static and decline steeply with distance, so electric communication works over at most a meter or so; it functions in darkness and in turbid water, and it is private except to predators, such as electric eels and catfishes, that have evolved to detect it.

## 38.6. Sensory Drive

The preceding sections treated the environment as a filter for signals. John Endler (1992) proposed a broader framework in which the environment shapes all components of communication together.

**Definition 38.6.1 (Sensory Drive)** **Sensory drive** is the coevolution of signals, sensory systems and signaling behavior under the influence of the environment: environmental conditions determine which signals transmit well and contrast with the background, and they also shape the receiver's sense organs through selection in other contexts such as foraging and predator avoidance; signals then evolve to match the sensory systems and the environment, and divergence in any component between habitats can lead to divergence in mate choice and to reproductive isolation.

The framework connects the physical constraints of this chapter with **sensory bias** ([7.10.13](/7.10.13)): a receiver's sense organs are tuned by the environment for other tasks, and signals evolve to exploit the resulting biases. Three systems illustrate it.

*Threespine sticklebacks.* Males of most populations of *Gasterosteus aculeatus* have a red throat and belly during the breeding season ([7.18.3](/7.18.3)). In some lakes of British Columbia whose water is stained red by dissolved organic matter, males are much less red, and in some populations black. Janette Boughman (2001) found that in such lakes females were less sensitive to red light, and that the redness of males and the strength of female preference for red varied among lakes with water color; the divergence of the signal contributed to reproductive isolation between the benthic and limnetic species that coexist in some lakes.

*Cichlids of Lake Victoria.* The hundreds of species of cichlid fishes in Lake Victoria are among the fastest radiations known, and closely related species often differ mainly in male nuptial coloration. In species pairs of *Pundamilia*, males of one species are blue and live in shallower water, where the light is broad-spectrum, and males of the other are red and live deeper, where the light is shifted toward longer wavelengths because the water is turbid. Seehausen and colleagues (2008) found that the two species differ in the long-wavelength-sensitive opsin gene *LWS*, whose alleles differ in their absorption maximum; the frequency of the allele with longer-wavelength sensitivity increased with depth along the light gradient at each of several islands, and so did the frequency of red males. Where the light gradient was steep, the species were distinct; where it was shallow (in clear water), they had merged into one variable population. The same study links the loss of cichlid diversity in the eutrophic lake to turbidity: when the water becomes turbid, the color differences on which mate choice depends can no longer be seen, and species hybridize (Seehausen, van Alphen and Witte 1997).

*Guppies.* Female guppies prefer males with more and brighter orange spots, an orange that depends on dietary carotenoids. Across populations in Trinidad, the strength of the female preference for orange was correlated with the females' attraction to orange objects in a foraging context, and both sexes peck at orange objects, which resemble fallen fruit that guppies eat (Rodd and colleagues 2002). A sensitivity that evolved for finding food may thus have set the stage for orange as a sexual signal.

![Sensory drive in Lake Victoria cichlids (schematic, after Seehausen and colleagues 2008). A: spectrum of downwelling light at increasing depth in turbid water, where short wavelengths are absorbed most strongly, so the light at depth is shifted toward red. B: absorbance spectra of two long-wavelength-sensitive opsin variants with absorption maxima 12 nm apart (opsin templates), and reflectance spectra of a blue and a red male. C: the brightness of the red male relative to the blue male, as perceived by each opsin variant, against depth: the advantage of red increases with depth, and more so for the long-shifted opsin, so that light environment, opsin allele and male color covary along the depth gradient](./plots/sensory-drive.py)

## 38.7. Choosing a Channel

### 38.7.1. A Comparison of Channels

Each channel has a characteristic profile of advantages and disadvantages (compare the comparison of insect channels in [7.17.27](/7.17.27#sec-27.8)).

| Property | Sound | Light | Chemicals | Touch and vibration | Electric |
|---|---|---|---|---|---|
| Range | Long (km in water) | Medium (needs line of sight) | Long downwind, short otherwise | Contact to a few meters | About 1 m |
| Speed of transmission | Fast | Instantaneous | Slow | Fast | Instantaneous |
| Speed of change | Fast | Fast (displays) or slow (plumage) | Slow | Fast | Fast |
| Around obstacles | Yes | No | Yes | Along the substrate | Yes |
| In darkness | Yes | Only bioluminescence | Yes | Yes | Yes |
| Localization by receiver | Good (needs two ears) | Very good | Poor, needs search | Moderate | Good at close range |
| Persistence | None | Momentary or static | Long | None | None |
| Energy cost | High | Low (reflected light) | Low to moderate | Low | Moderate |
| Eavesdropping risk | High | High (predators see) | Moderate | Low | Low, except specialists |

Sound is the channel of choice for long-range signals in dense habitats and at night; light for fast, localizable signals in open habitats by day; chemicals for persistent marks and signals that must work in the sender's absence; vibration and touch for private, close-range exchanges; electric signals for darkness and turbid water.

### 38.7.2. Multimodal Signals

Many signals combine several channels. A courting male túngara frog inflates a vocal sac as he calls; male wolf spiders of the genus *Schizocosa* wave ornamented forelegs while drumming on leaf litter; male peacock spiders (*Maratus*) combine colorful abdominal flaps with substrate vibrations.

**Definition 38.7.1 (Multimodal Signal)** A **multimodal signal** is a signal whose components are received through two or more sensory modalities.

Two kinds of hypothesis explain why multimodal signals evolve (Partan and Marler 1999; Hebets and Papaj 2005). *Efficacy hypotheses* hold that the components back each other up in variable environments (one channel works when the other fails: visual signals in daylight, vibrational signals in darkness or dense litter) or that one component alerts the receiver to the other. *Content hypotheses* hold that each component carries different information ("multiple messages"), or that the components are redundant indicators that together give a more reliable estimate of the same quality. Partan and Marler classified multimodal signals by the receiver's response to the components alone and together: equivalence (each alone elicits the same response as the combination), enhancement (the combination elicits a stronger response), dominance (one component determines the response), modulation (one component changes the response to the other) and emergence (the combination elicits a response different from either).

Experiments with robotic and video stimuli have separated the components. Female túngara frogs approached a call presented with a robotic frog whose vocal sac inflated in synchrony more readily than the call alone, an enhancement (Taylor and colleagues 2008); the visual component also helped females locate the caller in a noisy chorus. In *Schizocosa* wolf spiders, females responded to video playback of courting males and to the vibrations alone, and responded most strongly to the combination; in species with more ornamented males, the visual component mattered more (Hebets and Uetz 1999). Multimodal signals also have costs: each component can attract its own eavesdroppers, as when fringe-lipped bats are drawn more strongly to túngara frogs whose vocal sac inflates and whose call creates ripples on the water (Halfwerk and colleagues 2014).

## Summary

- Detection depends on emitted power, propagation, noise and the receiver's tuning; senders increase power, match the channel, contrast with the background, add redundancy and alerting components.
- Sound is produced by stridulation, tymbals, airflow through the larynx or **syrinx**, swim bladder drumming and percussion, and is shaped by resonators (source–filter theory; formant dispersion $\Delta F = c/(2L)$ indicates size).
- Small sources radiate low frequencies inefficiently (efficiency ∝ $(ka)^2$ for $ka < 1$), so call frequency falls with body size; baffles and horns (tree crickets, mole crickets) help.
- Propagation: spherical spreading (−6 dB per doubling of distance), absorption rising with frequency, scattering and ground effects, reverberation in forest and amplitude fluctuations in the open; the deep sound channel carries whale calls far.
- Noise masks signals in the same frequency band; urban birds raise song frequency (great tits), amplitude (nightingales) and change timing (robins). The **acoustic adaptation hypothesis** (Definition 38.2.1) is supported within species but only weakly across species.
- Color comes from pigments (carotenoids, melanins, pterins), structures (multilayers, spongy keratin) and **bioluminescence**; it changes by molt, hormones or neurally controlled **chromatophores**. Color must be measured through the receiver's photoreceptors; ultraviolet signals are common. Light environments differ among forest patches, times of day and water types.
- Chemical signals trade volatility against persistence; their **active space** (Definition 38.4.1) grows only as $(Q/K)^{1/3}$; plumes are filamentous; trails and marks persist.
- Close-range channels (touch, vibration, hydrodynamic, electric) are private and work in darkness.
- **Sensory drive** (Definition 38.6.1) links habitat, sense organs and signals: sticklebacks in red-stained lakes, *Pundamilia* cichlids and *LWS* alleles along depth gradients, guppies and orange.
- **Multimodal signals** (Definition 38.7.1) serve efficacy (backup, alerting) and content (multiple or redundant messages); components may interact by equivalence, enhancement, dominance, modulation or emergence.

## Questions

1. A frog's call has a level of 90 dB at 1 m. Ignoring excess attenuation, at what distance does it fall to 30 dB? How does the answer change if the excess attenuation in its habitat is 0.05 dB per meter?

   **Answer** With spreading alone, $90 - 20\log_{10} r = 30$ gives $\log_{10} r = 3$, $r = 1000\,\mathrm{m}$. With excess attenuation, $20\log_{10} r + 0.05(r - 1) = 60$. Trying values: at $r = 300$, $49.5 + 15.0 = 64.5$; at $r = 250$, $48.0 + 12.5 = 60.5$; at $r = 245$, $47.8 + 12.2 = 60.0$. So $r \approx 245\,\mathrm{m}$: the excess attenuation, small per meter, reduces the range fourfold, because it grows linearly with distance whereas spreading losses grow only logarithmically.
2. Why can a small insect not produce an efficient low-frequency sound, and how have tree crickets and mole crickets overcome this limitation?

   **Answer** A source radiates efficiently only if its size is comparable with the wavelength ($ka \gtrsim 1$); for a small source, the medium near it moves back and forth without being compressed, and the radiated fraction of the power falls as $(ka)^2$. A vibrating wing radiates from both faces in opposite phase, and around the edges the front and back pressure waves cancel (acoustic short circuit). Tree crickets sing through a hole in a leaf, which acts as a baffle and separates the two faces, effectively enlarging the source; mole crickets sing from a horn-shaped burrow that couples the small source to the air (impedance matching), increasing the radiated power several times.
3. Great tits in noisy urban territories sing songs with higher minimum frequencies. List three alternative explanations of this observation and an experiment that would distinguish them.

   **Answer** (1) Individual birds adjust song frequency flexibly to current noise (plasticity); (2) birds learn songs from tutors in noisy places, so that the local song tradition shifts (cultural evolution); (3) urban populations have diverged genetically, or birds with high-pitched songs preferentially settle in noisy places. Tests: experimentally raise noise in territories with loudspeakers and record whether the same individuals shift frequency within minutes or days (Slabbekoorn and colleagues found rapid adjustments, supporting plasticity); hand-raise nestlings from urban and forest populations with the same tutors (genetic differences); follow marked birds as they settle (habitat choice).
4. Explain why alarm pheromones are usually more volatile and produced in smaller amounts than sex attractants, using the concept of active space.

   **Answer** The active space radius grows only as $(Q/K)^{1/3}$, and with a volatile compound the signal rises and fades quickly. An alarm signal should reach only nearby colony members and should switch off soon after the danger has passed, so that the colony is not alarmed unnecessarily; a small $Q/K$ and high volatility produce a small, short-lived active space. A sex attractant must reach mates far away and over a long time, so it is emitted continuously, the threshold of the receiver is extremely low (very large $Q/K$), and the molecule is less volatile; wind extends its active space into a long plume.
5. How does sensory drive differ from the simple idea that signals are adapted to transmit well in their habitat? Why can sensory drive lead to speciation?

   **Answer** The simple idea (as in the acoustic adaptation hypothesis) considers only the transmission of the signal. Sensory drive adds that the environment also shapes the receiver's sense organs, through selection in other tasks such as foraging, and that signals evolve to match both the transmission properties and the receiver's biases, with mate preferences evolving in turn. If populations live in different environments (shallow and deep water, clear and stained lakes), their sense organs, signals and preferences diverge together; because mate choice depends on them, females prefer local males, which reduces gene flow and can lead to reproductive isolation, as in *Pundamilia* cichlids and sticklebacks.
6. (Open question) A male wolf spider courts with both visual leg-waving and substrate vibrations. Design an experiment that distinguishes the backup hypothesis from the multiple-messages hypothesis.

   **Answer** Present females with video playback of the visual display, with playback of the vibrations through the substrate, and with both, synchronized, in light and in darkness and on substrates that transmit vibrations well or poorly. The backup hypothesis predicts that each component alone elicits receptivity (equivalence) and that the visual component is effective in light but not darkness, the vibrational one on good substrates; the combination should be most effective where either component alone is unreliable. The multiple-messages hypothesis predicts that the components affect different decisions or are correlated with different male traits: manipulate one component (for example, the vibration rate, which may reflect condition) independently of the other (for example, leg-tuft size, which may reflect age or species) and test whether each affects female preference independently, and whether each is correlated with a different male attribute.
