---
title: Hearing and Vestibular Sensation
description: Sound pressure and the decibel; impedance matching by the middle ear; the cochlea, endocochlear potential, traveling wave and place principle; hair cell transduction, adaptation and the cochlear amplifier; central auditory pathways and sound localization; vestibular organs, semicircular canals, otolith organs and the vestibulo-ocular reflex; evolution and comparison of hearing.
source_hash: b906820a0232
---

Hearing and the vestibular sense use the same receptor cell, the hair cell of the inner ear, to convert extremely small mechanical movements into electrical signals; the differences between the two senses arise almost entirely from the accessory structures surrounding the hair cells. The cochlea decomposes sound by frequency along the basilar membrane and raises sensitivity more than a thousandfold with an amplifier powered by cells; the vestibular organs convert angular and linear acceleration of the head into deflection of hair bundles. This chapter first covers the physics of sound and impedance matching by the outer and middle ear, then the mechanics of the cochlea, transduction and amplification by hair cells, central pathways and sound localization, then the vestibular system, and finally compares the diversity of hearing organs in the animal kingdom. The general principles of sensation are in Chapter 39 ([7.14.39](/7.14.39)); the physics of the gating spring and active amplification of hair cells was discussed in biophysics ([7.6.25](/7.6.25#sec-25.6.3), [7.6.31](/7.6.31#sec-31.5)), and the physics of sound waves is in wave motion in 5.1 Mechanics.

## 42.1. Sound and the Range of Hearing

### 42.1.1. Sound Pressure, Intensity, and the Decibel

Sound is a small oscillation of pressure and density propagating in a medium. In a plane sound wave, the relation between the rms **sound pressure** $p$ and the sound intensity $I$ is

$$
I = \frac{p^2}{Z}, \qquad Z = \rho c, \tag{42.1}
$$
where $Z$ is the **characteristic impedance** of the medium: about $415\,\mathrm{Pa\,s\,m^{-1}}$ for air and about $1.5\times10^6\,\mathrm{Pa\,s\,m^{-1}}$ for water. The sound pressures the human ear can sense span about $10^6$-fold (intensity $10^{12}$-fold), and are therefore expressed by the sound pressure level on a logarithmic scale:

$$
L_p = 20\log_{10}\frac{p}{p_0}\ \mathrm{dB}, \qquad p_0 = 20\,\mu\mathrm{Pa}, \tag{42.2}
$$
where $p_0$ is about the human hearing threshold at $1\,\mathrm{kHz}$, corresponding to an intensity of $10^{-12}\,\mathrm{W\,m^{-2}}$; in air it is numerically the same as the **sound intensity level** $10\log_{10}(I/I_0)$. Normal conversation is about $60\,\mathrm{dB}$, prolonged exposure above $85\,\mathrm{dB}$ causes hearing damage, and about $120$–$130\,\mathrm{dB}$ causes pain.

**Example 42.1.1** At the hearing threshold ($p = 20\,\mu\mathrm{Pa}$, $1\,\mathrm{kHz}$) the displacement amplitude of air particles is $\xi = \sqrt2\,p/(Z\omega) = \sqrt2\times2\times10^{-5}/(415\times2\pi\times10^3) \approx 1.1\times10^{-11}\,\mathrm{m}$, about one tenth of the diameter of a hydrogen atom. The vibration amplitudes of the eardrum, ossicles, and basilar membrane at the hearing threshold are all subnanometer; the ear is one of the most sensitive mechanical detectors known, and it achieves this through the impedance matching, active amplification, and direct gating of hair cells discussed in this chapter.

### 42.1.2. Hearing Threshold and Hearing Range

The frequency range audible to the human ear is about $20\,\mathrm{Hz}$–$20\,\mathrm{kHz}$, and the most sensitive range is $1$–$4\,\mathrm{kHz}$. When the hearing threshold at each frequency and the maximum sound pressure causing pain are plotted on one graph, the region between them is called the hearing range. The threshold curve rises at both low and high frequencies, for reasons including the transmission characteristics of the middle ear (stiffness limiting low frequencies and mass limiting high frequencies) and the resonance of the ear canal (Section 42.2.1).

Subjective loudness is not proportional to sound pressure: by **Stevens' power law**, loudness is approximately proportional to the $0.3$ power of intensity, and each increase of $10\,\mathrm{dB}$ in sound pressure level roughly doubles loudness. High-frequency hearing declines gradually with age (presbycusis), first affecting the base of the cochlea, the region sensitive to high frequencies (Section 42.3.2); noise-induced hearing loss often shows a "notch" at about $4\,\mathrm{kHz}$.

## 42.2. The Outer Ear and Middle Ear

### 42.2.1. The Outer Ear

The pinna collects sound, and its folds cause different spectral filtering for sounds from different directions (a notch at high frequencies that moves with the elevation of the source), providing cues for judging the elevation and front–back position of a source (Section 42.4.3). The external auditory canal is about $2.5\,\mathrm{cm}$ long, open at one end and closed by the eardrum at the other, and acts as a quarter-wavelength resonant tube with a resonant frequency of about

$$
f \approx \frac{c}{4\ell} = \frac{343\,\mathrm{m\,s^{-1}}}{4\times0.025\,\mathrm{m}} \approx 3.4\,\mathrm{kHz},
$$
raising the sound pressure at the eardrum by about $10$–$15\,\mathrm{dB}$ within $2$–$5\,\mathrm{kHz}$, which is one reason the threshold curve is lowest in this band.

### 42.2.2. Impedance Matching by the Middle Ear

The inner ear is filled with fluid. If sound passes directly from air onto the surface of a liquid, because the characteristic impedances differ by about a factor of 3600, the fraction of intensity transmitted is only

$$
T = \frac{4Z_1Z_2}{(Z_1 + Z_2)^2} \approx \frac{4Z_{\text{air}}}{Z_{\text{water}}} \approx 1.1\times10^{-3}, \tag{42.3}
$$
that is, a loss of about $30\,\mathrm{dB}$: 99.9 % of the energy is reflected back. The role of the middle ear is to reduce this loss.

**Definition 42.2.1 (Impedance Matching)** The action of the eardrum and ossicular chain of the middle ear in converting the low-pressure, large-displacement vibration acting on the large-area eardrum into a high-pressure, small-displacement vibration acting on the small-area oval window, so that sound energy passes efficiently from low-impedance air into the high-impedance perilymph of the inner ear, is called **impedance matching** of the middle ear.

The pressure gain comes from two parts:

- Area ratio: the effective vibrating area of the eardrum is about $55\,\mathrm{mm}^2$ and the footplate of the stapes about $3.2\,\mathrm{mm}^2$, a ratio of about 17; the same force acting on the smaller area raises the pressure 17-fold;
- Lever: the handle of the malleus is longer than the long process of the incus, and the ossicular chain acts as a lever that reduces the displacement of the stapes and increases the force about 1.3-fold.

The total pressure gain is about $17\times1.3 \approx 22$-fold (about $27\,\mathrm{dB}$), compensating most of the loss in Eq. (42.3). Note that the ossicular lever by itself amplifies the force only about 1.3-fold; the roughly 20-fold pressure amplification comes mainly from the area ratio, not the lever.

**Example 42.2.1** A sound of $60\,\mathrm{dB}$ at the eardrum has an rms sound pressure of $20\,\mathrm{mPa}$. Amplified 22-fold by the middle ear, the sound pressure acting on the oval window is about $0.44\,\mathrm{Pa}$, equivalent to "seeing" a sound of about $87\,\mathrm{dB}$ on the fluid side. Without the middle ear (for example, with the ossicular chain fixed by otosclerosis), sound can reach the inner ear only through the round window and the skull, and the hearing threshold rises by about $30$–$60\,\mathrm{dB}$, which is conductive hearing loss.

The inner ear is a closed fluid chamber and the fluid is almost incompressible: when the stapes pushes the oval window inward, the round window membrane must bulge outward for the fluid to move. The eustachian tube connects the tympanic cavity with the nasopharynx, equalizing air pressure on the two sides of the eardrum. Sound can also vibrate the skull and reach the inner ear directly (bone conduction), with efficiency far lower than air conduction; clinically, comparing air- and bone-conduction thresholds distinguishes conductive hearing loss from sensorineural hearing loss.

### 42.2.3. The Acoustic Reflex

Loud sound (above about $70$–$90\,\mathrm{dB}$) causes, through a brainstem **reflex arc**, contraction of two muscles of the middle ear: the stapedius (innervated by the facial nerve) and the tensor tympani (innervated by the trigeminal nerve). They increase the stiffness of the ossicular chain and reduce its amplitude, mainly attenuating low-frequency sounds below $1\,\mathrm{kHz}$, with attenuation up to $30$–$40\,\mathrm{dB}$. This *acoustic reflex* has three functions:

1. It protects the cochlea from damage by sustained loud sound;
2. It lowers low-frequency background noise so that mid- and high-frequency speech is more easily heard (reducing masking);
3. It contracts before and during one's own speech, lowering sensitivity to one's own voice.

The latency of the acoustic reflex is $40$–$80\,\mathrm{ms}$, so it cannot protect against sudden impulsive sounds such as gunshots and explosions.

## 42.3. The Cochlea

### 42.3.1. Structure of the Cochlea and the Endolymph

The cochlea is a bony tube winding about $2.5$–$2.75$ turns around the modiolus, about $35\,\mathrm{mm}$ long when unrolled. Reissner's membrane (vestibular membrane) and the basilar membrane divide it into three scalae: the upper scala vestibuli and lower scala tympani are filled with perilymph and communicate at the helicotrema at the apex, connecting with the middle ear through the oval window and round window, respectively; the middle scala media (cochlear duct) is filled with endolymph and is a closed compartment.

The composition of endolymph is very special: $\ce{K+}$ about $150\,\mathrm{mmol\,L^{-1}}$, $\ce{Na+}$ only about $1\,\mathrm{mmol\,L^{-1}}$, and $\ce{Ca^2+}$ about $20\,\mu\mathrm{mol\,L^{-1}}$, like **intracellular fluid** rather than **extracellular fluid**; perilymph is similar to cerebrospinal fluid.

**Definition 42.3.1 (Endocochlear Potential)** With the perilymph of the scala tympani taken as zero potential, the potential of the endolymph of the scala media is about $+80\,\mathrm{mV}$, called the **endocochlear potential**. It is produced and maintained by active transport of $\ce{K+}$ by cells of the stria vascularis in the lateral wall of the cochlear duct (sodium–potassium pump and $\ce{Na+}$–$\ce{K+}$–$2\ce{Cl-}$ cotransporter).

The apical surface of hair cells is bathed in endolymph and the basolateral side in perilymph, and the intracellular potential is about $-60$ to $-70\,\mathrm{mV}$. The potential difference driving $\ce{K+}$ from the apical transduction channels into the hair cell is thus about $80 - (-65) \approx 145\,\mathrm{mV}$, while $\ce{K+}$ can leave the cell down its concentration gradient from the basolateral side into the perilymph. This ingenious arrangement lets hair cells use $\ce{K+}$ (rather than $\ce{Na+}$) as the carrier of the transduction current, so the hair cell itself pays almost no ion-pump cost for the transduction current: the energy is paid centrally by the stria vascularis. $\ce{K+}$ entering the perilymph is recycled to the stria vascularis through a network of **gap junctions** made of connexin 26 between supporting cells. Mutations of the *GJB2* gene encoding connexin 26 are the most common cause of hereditary deafness.

The organ of Corti sits on the basilar membrane and is the receptor organ of hearing; it includes:

- A row of inner hair cells (about 3500), the receptor cells that truly send auditory information to the brain; about 95 % of afferent fibers of the auditory nerve (type I spiral ganglion neurons, about $30\,000$ in all) come from inner hair cells, each inner hair cell connecting to 10–20 fibers;
- Three rows of outer hair cells (about $12\,000$), whose main role is to amplify the vibration of the basilar membrane (Section 42.3.4); they receive only a few type II afferent fibers and receive efferent fibers from the superior olivary complex;
- Supporting cells such as pillar cells, and the tectorial membrane covering the hair cells. The stereocilia of the tallest row of outer hair cells are embedded in the tectorial membrane.

**Definition 42.3.2 (Hair Cell)** An epithelial receptor cell with a bundle of stereocilia arranged in graded heights at its apex (vestibular hair cells also have one kinocilium), in which deflection of the bundle opens mechanically gated channels and produces a receptor potential, is called a **hair cell**. It has no axon and releases glutamate to afferent neurons through ribbon synapses at its base. Hair cells are found in the cochlea, vestibular organs, and lateral line of vertebrates (Section 42.6).

### 42.3.2. Traveling Wave and the Place Principle

Vibration of the stapes pushes the perilymph of the scala vestibuli, creating a pressure difference between scala vestibuli and scala tympani that makes the basilar membrane move up and down. Békésy (Nobel Prize 1961) observed in cadaver cochleae that the vibration of the basilar membrane propagates from base to apex as a **traveling wave**: the amplitude of the wave gradually increases, reaches a maximum at a certain position, and then decays rapidly; the wavelength shortens and the speed slows at the same time. The position of maximum amplitude varies with frequency: high frequencies at the base and low frequencies at the apex.

The reason is that the mechanical properties of the basilar membrane vary continuously along its length: at the base the basilar fibers are short (about $0.1\,\mathrm{mm}$ wide) and stiff; toward the apex the basilar membrane gradually widens (about $0.5\,\mathrm{mm}$) and softens, with stiffness falling by about two orders of magnitude. Each small segment of basilar membrane acts as a local harmonic oscillator, whose resonant frequency $f = \frac{1}{2\pi}\sqrt{s/m}$ ($s$ the stiffness, $m$ the effective mass per unit area) decreases from base to apex.

**Definition 42.3.3 (Place Principle)** Sounds of different frequency make different parts of the basilar membrane vibrate maximally, thereby exciting hair cells and auditory nerve fibers at different positions, and the central nervous system judges pitch from the position excited; this principle of frequency analysis is called the **place principle**. This spatial arrangement of the cochlea by frequency is called tonotopy.

**Formula 42.3.1 (Greenwood Function)** The relative position $y$ along the human basilar membrane from the apex ($0$ at the apex, $1$ at the base) and the characteristic frequency at that point approximately satisfy

$$
f(y) = 165.4\,(10^{2.1y} - 0.88)\ \mathrm{Hz}. \tag{42.4}
$$

By Eq. (42.4), the apex is $20\,\mathrm{Hz}$ and the base about $20.7\,\mathrm{kHz}$. In the mid- and high-frequency range, $f$ is approximately an exponential function of position, and each octave occupies the same length of basilar membrane: $\log_{10}2/2.1 \approx 0.14$, about $5\,\mathrm{mm}$. This logarithmic arrangement is consistent with our perception of pitch (octaves equally spaced).

The formation of the traveling wave can be explained with a one-dimensional "long-wave" cochlear model: treat the two scalae as fluid ducts of cross-sectional height $H$, with the pressure difference $p(x)$ driving a basilar membrane of impedance $Z(x) = r + \mathrm{i}\omega m + s(x)/(\mathrm{i}\omega)$; mass conservation and the equation of motion of the fluid give

$$
\frac{\mathrm{d}^2p}{\mathrm{d}x^2} = \frac{2\rho\,\mathrm{i}\omega}{H\,Z(x)}\,p, \tag{42.5}
$$
and the velocity of the basilar membrane is $v = p/Z$. Near the base the basilar membrane is very stiff ($Z$ dominated by stiffness), and the wave travels fast with long wavelength; approaching the resonant place, the imaginary part of $Z$ tends to zero, the wave slows, energy piles up, and the amplitude grows; beyond the resonance point the basilar membrane is mass-dominated and the wave decays rapidly. Setting $s(x)$ with the Greenwood function and solving Eq. (42.5) numerically gives the frequency-ordered traveling wave envelopes in the figure below.

![Traveling waves and the Greenwood map in a passive one-dimensional cochlea (Eq. (42.5); height of the two scalae H = 1 mm, fluid density 1000 kg m⁻³, basilar membrane length 35 mm; effective mass m = 0.5 kg m⁻², stiffness s(x) such that the local resonant frequency follows Eq. (42.4), damping corresponding to quality factor Q = 6; pressure gradient prescribed at the stapes, pressure zero at the helicotrema). A: basilar membrane velocity envelopes for pure tones of 0.5, 1, 2, 4, and 8 kHz (each normalized to its peak), and the instantaneous waveform of the 1 kHz traveling wave at two times (thin lines): the wave slows and its wavelength shortens as it travels toward the apex, reaches a maximum before the characteristic place, and then vanishes rapidly. B: Greenwood function and the positions of the model envelope peaks; the peaks of the passive model are slightly shifted toward the base and are far less sharp than in the living cochlea](./plots/traveling-wave.py)

The passive traveling wave observed by Békésy has very broad tuning and cannot explain how humans can distinguish frequency differences of about 0.2 %. The tuning of the basilar membrane measured in living animals is much sharper, especially for low-intensity sounds, and this sharp tuning disappears immediately after the animal dies (Rhode, 1971): the cochlea contains an amplifier powered by living cells (Section 42.3.4).

For sounds below about $4$–$5\,\mathrm{kHz}$, the action potentials of auditory nerve fibers also fire locked to a particular phase of the sound wave (phase locking). A single fiber need not fire every cycle, and many fibers together can have a spike in every cycle (volley principle, Wever). The pitch of low-frequency sound is therefore coded both by place and by the temporal structure of firing, and the latter is also the basis of the interaural time difference (Section 42.4.3).

### 42.3.3. Mechanoelectrical Transduction in Hair Cells

When the basilar membrane moves upward, shear motion arises between it and the tectorial membrane, deflecting the hair bundles of hair cells back and forth. The tip of each stereocilium is connected to the side of its taller neighbor by a tip link (composed of cadherin-23 and protocadherin-15):

1. When the bundle is deflected toward the tallest row, the tip links are stretched and open **mechanosensitive channels** at their lower end (pore subunits TMC1/TMC2);
2. $\ce{K+}$ and a little $\ce{Ca^2+}$ from the endolymph enter under a driving force of about $145\,\mathrm{mV}$, the hair cell undergoes **depolarization**, and a **receptor potential** is produced;
3. Voltage-gated $\ce{Ca^2+}$ channels (CaV1.3) at the base open, ribbon synapses release glutamate, and afferent fibers are excited;
4. When the bundle is deflected in the opposite direction, the channels close, **hyperpolarization** of the hair cell follows, and transmitter release decreases.

At rest about 10 %–20 % of channels are open, so the hair cell can report deflection in both directions. The channels are opened directly by force, and opening takes only a few microseconds, which is the prerequisite for hearing to follow vibrations of several kilohertz; the transduction threshold is a bundle deflection of about $0.3$–$1\,\mathrm{nm}$, and saturation occurs at about $100\,\mathrm{nm}$.

The tip links and their anchoring structures act as the **gating spring** ([7.6.31](/7.6.31#def-31.5.1)): the movement of the gate when the channel opens relaxes the spring, and the open probability is a Boltzmann function of the work done by the spring,

$$
P_{\mathrm{o}}(X) = \frac{1}{1 + \exp\!\bigl[-z(X - X_{\mathrm{a}} - X_0)/k_{\mathrm{B}}T\bigr]}, \tag{42.6}
$$
where $X$ is the deflection of the hair bundle, $z$ is the "gating force", the change of tension in the gating spring on opening of one channel referred to the tip of the hair bundle (about $0.5$–$1\,\mathrm{pN}$), $X_0$ determines the fraction open at rest, and $X_{\mathrm{a}}$ is the shift caused by adaptation. The open probability curve and the negative stiffness of the hair bundle due to gating are in [7.6.31](/7.6.31#sec-31.5.1).

When the hair bundle is held deflected, the transduction current decreases within a few to tens of milliseconds: this is the **adaptation** of the hair cell. It has two components:

- Fast adaptation (submillisecond to a few milliseconds): entering $\ce{Ca^2+}$ acts on the channel or its vicinity and closes the channel;
- Slow adaptation (tens of milliseconds): myosin-1c motors at the upper end of the tip link slide down the actin when $\ce{Ca^2+}$ rises, relaxing the tension of the tip link; after the channel closes they climb up again and restore tension.

Both shift $X_{\mathrm{a}}$ in Eq. (42.6) in the direction of the present deflection, pulling the operating point back to the steep part of the curve and ensuring that the hair cell always remains sensitive to new small changes. This is the same design as the $\ce{Ca^2+}$ **negative feedback** of the rod ([7.14.41](/7.14.41#sec-41.2.4)): high-gain transduction plus negative feedback that strengthens as the signal grows extends the usable working range.

![Adaptation of hair cell transduction (schematic model, Eq. (42.6); z = 0.7 pN, k_BT = 4.1 pN nm, X₀ = 12.9 nm so that the open probability at rest is 0.1; the amount of adaptation X_a consists of a fast component (τ = 0.5 ms) and a slow component (τ = 20 ms), each tending to 0.4X, with 80 % total adaptation). A: open probability curve at rest, and curves after adaptation to sustained deflections of +20 nm, +50 nm, and −20 nm: the curve shifts along the displacement axis and the operating point (dot) returns to near the steep part. B: time course of open probability after step deflections of +10, +20, +40 nm and −15 nm applied at t = 0: first a rapid rise (or fall), then relaxation with fast and slow time constants, but not completely back to the resting value](./plots/hair-cell-adaptation.py)

### 42.3.4. Outer Hair Cells and the Cochlear Amplifier

Outer hair cells have a unique ability: when the membrane potential changes, the cell itself lengthens or shortens, shortening on depolarization and lengthening on hyperpolarization (Brownell et al., 1985). This electromotility is carried out by the **motor protein** prestin (SLC26A5), densely packed in the lateral membrane of the outer hair cell (Zheng et al., 2000); it is driven directly by membrane potential, consumes no ATP, and can follow voltage changes of tens of kilohertz.

**Definition 42.3.4 (Cochlear Amplifier)** The mechanism, powered actively by cells, in which outer hair cells convert the receptor potential caused by basilar membrane vibration into changes of their own length, applying force to the basilar membrane in each cycle and amplifying vibration near the characteristic frequency, is called the **cochlear amplifier**.

The cochlear amplifier has three features:

- It amplifies low-intensity sounds by about $40$–$60\,\mathrm{dB}$ (100–1000-fold) and hardly amplifies loud sounds, so that vibration of the basilar membrane grows compressively with sound pressure: at the characteristic frequency, a $10\,\mathrm{dB}$ increase in sound pressure increases vibration by only about $2$–$3\,\mathrm{dB}$; this compresses a sound pressure range of about $120\,\mathrm{dB}$ into the range hair cells can handle;
- Amplification occurs only near the characteristic frequency, sharpening the tuning curve;
- In mice with prestin knocked out, the hearing threshold rises by about $40$–$60\,\mathrm{dB}$ and frequency selectivity is lost (Liberman et al., 2002).

An active oscillator close to a **Hopf bifurcation** has exactly these properties: large gain for weak signals, response compressed as the $1/3$ power of force, and strong frequency selectivity ([7.6.31](/7.6.31#sec-31.5.2)). The amplifier occasionally "overshoots": the cochlea can emit sound by itself.

**Definition 42.3.5 (Otoacoustic Emission)** Sound produced by active processes within the cochlea, transmitted backward through the middle ear, and recordable in the external auditory canal with a sensitive microphone is called an **otoacoustic emission**. It can be spontaneous or evoked by a click or pure tone (Kemp, 1978).

The existence of otoacoustic emissions proves that there are indeed active mechanical processes in the cochlea. Their measurement is fast and noninvasive and is the routine method for newborn hearing screening: when outer hair cells are damaged (common sensorineural hearing loss, such as that caused by noise and ototoxic drugs), evoked otoacoustic emissions disappear. Efferent fibers from the medial part of the superior olivary complex (medial olivocochlear bundle) release acetylcholine to inhibit outer hair cells, lowering the gain of the amplifier, improving discrimination of signals in noise, and giving some protection against loud sound.

### 42.3.5. Coding of Loudness

The louder the sound, the stronger the signal entering the central nervous system, accomplished jointly by three mechanisms:

1. The amplitude of basilar membrane vibration increases, the **receptor potential** of each excited hair cell increases, and the firing rate of afferent fibers increases;
2. The extent of vibration widens, and more hair cells and fibers near the characteristic frequency are excited (spatial recruitment);
3. Fibers of different thresholds are recruited successively: the 10–20 fibers connected to one inner hair cell differ in threshold and dynamic range; fibers with high spontaneous rates have low thresholds and saturate within about $20$–$30\,\mathrm{dB}$, whereas fibers with low spontaneous rates have high thresholds and wide dynamic ranges (Liberman, 1978).

The dynamic range of a single fiber is only about $30$–$40\,\mathrm{dB}$, whereas the dynamic range of hearing as a whole reaches $120\,\mathrm{dB}$; the grading of fiber thresholds together with the compression of the cochlear amplifier bridges this gap. Earlier textbooks attributed the third mechanism to "outer hair cells being excited only for loud sounds and informing the central nervous system", a statement that has been refuted: the role of outer hair cells is amplification, and they send almost no information to the central nervous system.

## 42.4. Central Auditory Pathways and Sound Localization

### 42.4.1. The Ascending Pathway

The central pathway of hearing has more levels than other senses and is bilateral from the second level on:

1. Bipolar neurons of the spiral ganglion enter the medulla through the auditory nerve (VIII), and all fibers synapse in the ipsilateral cochlear nuclei (dorsal and ventral nuclei);
2. Fibers of the ventral cochlear nucleus project through the trapezoid body to the superior olivary complexes on both sides, where the signals from the two ears first meet (Section 42.4.3);
3. Fibers ascend through the lateral lemniscus, some synapsing in the nuclei of the lateral lemniscus and most going to the inferior colliculus of the midbrain;
4. Fibers of the inferior colliculus go to the medial geniculate nucleus of the thalamus, where all fibers synapse, and then project through the auditory radiation to the primary auditory cortex of the temporal lobe (transverse temporal gyrus, Brodmann area 41).

Information from the two sides crosses repeatedly among the trapezoid body, nuclei of the lateral lemniscus, and inferior colliculus, so that each auditory cortex receives input from both ears, predominantly from the contralateral one. Damage to one auditory cortex therefore does not cause deafness in one ear, but affects only localization of sources in contralateral space. The tonotopic spatial arrangement is maintained from the cochlea to the cortex. Loud sound also causes, through the brainstem reticular formation, a whole-body startle reflex and arousal, and through the superior colliculus, turning of the head and eyes toward the source.

### 42.4.2. The Auditory Cortex

The primary auditory cortex is arranged tonotopically and sharpens frequency tuning through **lateral inhibition**. The belt and parabelt areas around it process increasingly complex sound features: pitch, timbre, temporal patterns of sound and the direction of the source, and integration with other senses; the posterior part of the left superior temporal gyrus (Wernicke's area) takes part in language comprehension ([7.14.46](/7.14.46)). The auditory cortex contains several tonotopic maps, each arranged by frequency, processing different features of sound.

### 42.4.3. Sound Localization

Humans judge the horizontal direction of a source mainly with two binaural cues (Rayleigh's duplex theory, 1907):

**Definition 42.4.1 (Interaural Time Difference and Interaural Level Difference)** A source off the midline reaches the two ears at different times, and the difference is called the **interaural time difference** (ITD); the shadowing of sound waves by the head weakens the sound at the far ear, and the difference in sound pressure level between the two ears is called the **interaural level difference** (ILD).

For a spherical head of radius $a$, at high frequencies (wavelength smaller than the head), the interaural time difference for sound from azimuth $\theta$ ($0$ straight ahead) is approximately (Woodworth's formula)

$$
\mathrm{ITD}(\theta) = \frac{a}{c}\,(\theta + \sin\theta), \tag{42.7}
$$
and at low frequencies, because of diffraction, the ITD is about $3(a/c)\sin\theta$. Taking $a = 8.75\,\mathrm{cm}$, the maximum ITD (source directly to the side) is about $0.66\,\mathrm{ms}$.

**Example 42.4.1** Humans can resolve an ITD of about $10\,\mu\mathrm{s}$ near straight ahead. By Eq. (42.7), for small $\theta$, $\mathrm{ITD} \approx 2a\theta/c$, so $\Delta\theta \approx c\,\Delta\mathrm{ITD}/2a = 343\times10^{-5}/0.175 \approx 0.02\,\mathrm{rad} \approx 1^\circ$. $10\,\mu\mathrm{s}$ is only about one hundredth of the width of an action potential, and the auditory system relies on precisely phase-locked firing and specialized synapses to compare such small time differences.

The two cues each cover a range of frequencies. ITD relies on phase locking to compare the phase of the sound wave at the two ears. The maximum ITD is about $0.66\,\mathrm{ms}$; once the period is shorter than twice this value (frequencies above about $0.76\,\mathrm{kHz}$), the same phase difference corresponds to two possible azimuths, and by about $1.5\,\mathrm{kHz}$ the period (about $0.67\,\mathrm{ms}$) is comparable to the maximum ITD itself, so the ambiguity is severe and the cue is essentially lost; at high frequency, however, head shadowing is pronounced and the ILD can reach $10$–$20\,\mathrm{dB}$. Low-frequency sounds are therefore localized by ITD and high-frequency sounds by ILD. Neither cue can distinguish front from back (the same ITD corresponds to a "cone of confusion"); distinguishing front from back and up from down relies on the spectral cues of the pinna and on head turning.

The two cues are computed separately in the superior olivary complex:

- The medial superior olive computes ITD: its neurons receive excitatory input from both ears and fire only when the inputs from the two sides arrive simultaneously, so they are coincidence detectors. Jeffress (1948) proposed that if the axons of the two sides' inputs have different lengths, forming a set of "delay lines", each detector is most sensitive to one particular ITD, and the position of the activated detector represents the azimuth of the source (place code). The circuit in birds (nucleus laminaris of the barn owl) basically fits this model; mammals depend more on precisely timed glycinergic inhibition to tune the optimal ITD, and the difference of population firing rates of the medial superior olives on the two sides codes azimuth (Brand et al., 2002).
- The lateral superior olive computes ILD: it receives excitatory input from the ipsilateral ear and inhibitory input from the contralateral ear converted through the medial nucleus of the trapezoid body (the synapse is the giant calyx of Held), and its firing rate reflects the difference of intensity between the two ears.

![Interaural time difference and an array of coincidence detectors. A: ITD of a spherical head of radius 8.75 cm (speed of sound 343 m/s) as a function of azimuth: Woodworth's formula at high frequency (Eq. (42.7)) and 3(a/c) sin θ at low frequency (diffraction); the dotted line is the 10 μs resolution threshold, corresponding to about 1° near straight ahead. B, C: Jeffress-type detector array, responses of seven detectors with internal delays −0.6 to +0.6 ms to phase-locked input, model exp(κ(cos 2πf(ITD − d) − 1)), κ = 2; shading is the physiological ITD range (±0.66 ms). At 500 Hz each detector has only one peak within the physiological range; at 1.5 kHz the period (0.67 ms) is comparable to the maximum ITD, peaks recur within the range, and the code becomes ambiguous](./plots/itd.py)

## 42.5. The Vestibular System

### 42.5.1. The Vestibular Organs

The vestibular part of the inner ear (vestibular labyrinth) includes three semicircular canals and two otolith organs (utricle and saccule), all filled with endolymph, with hair cells as the receptor cells. In addition to stereocilia, vestibular hair cells have one kinocilium at the tallest side (mature cochlear hair cells have lost the kinocilium), and so have a definite polarity:

- When the bundle is deflected toward the kinocilium, transduction channels open, the hair cell depolarizes, and the firing of the afferent fiber increases;
- When it is deflected the opposite way, the hair cell hyperpolarizes and firing decreases.

Vestibular afferent fibers have a high spontaneous rate at rest (about $100$ spikes per second in primates), so the firing rate can change in two directions and report movement in two directions. Vestibular hair cells are of two types: type I are completely enclosed by the calyx of an afferent ending, and type II contact ordinary bouton endings. The cell bodies of afferent neurons are in the vestibular ganglion (Scarpa's ganglion), and the central processes form the vestibular nerve.

### 42.5.2. Semicircular Canals and Angular Acceleration

**Definition 42.5.1 (Semicircular Canal)** The three mutually approximately perpendicular, endolymph-filled ring-shaped ducts of the inner ear, each of which is enlarged at one end into an ampulla, with hair cells on the crista ampullaris in the ampulla whose hair bundles extend into the gelatinous cupula that spans the ampulla, sensing rotation of the head in each plane, are called the **semicircular canals**.

The three semicircular canals are the horizontal (lateral), anterior (superior), and posterior canals. When the head begins to rotate, the semicircular canal turns with the head, whereas the endolymph in the canal lags because of inertia and flows in the opposite direction relative to the canal wall, pushing the cupula and deflecting it. The coplanar canals of the two sides work in pairs: when the head turns left, endolymph in the left horizontal canal flows toward the ampulla and the hair cells are excited, whereas on the right they are inhibited, and the central nervous system compares the difference between the two sides (push–pull).

The movement of the cupula and endolymph can be described by an overdamped torsion pendulum (Steinhausen model). Let $\xi$ be the angular displacement of the endolymph relative to the canal wall (proportional to the deflection of the cupula) and $\Omega$ the angular velocity of the head:

$$
J\ddot\xi + B\dot\xi + K\xi = -J\dot\Omega, \tag{42.8}
$$
where $J$ is the moment of inertia of the endolymph, $B$ is the coefficient of viscous resistance in the thin duct, and $K$ is the elastic restoring coefficient of the cupula. The duct is very thin, viscous forces are far larger than inertial and elastic forces, and the two time constants differ greatly: the long time constant $\tau_1 = B/K \approx 5\,\mathrm{s}$ and the short time constant $\tau_2 = J/B \approx 3$–$5\,\mathrm{ms}$. The transfer function is

$$
\frac{\xi(s)}{\Omega(s)} = -\frac{J}{K}\,\frac{s}{(1 + \tau_1 s)(1 + \tau_2 s)}. \tag{42.9}
$$
Between $1/(2\pi\tau_1) \approx 0.03\,\mathrm{Hz}$ and $1/(2\pi\tau_2) \approx 40\,\mathrm{Hz}$, $\xi \approx -(J/K)\Omega/\tau_1 = -(J/B)\Omega$: the deflection of the cupula is proportional to the angular velocity of the head. Although the **adequate stimulus** of the semicircular canal is angular acceleration, within the frequency band of natural head movements (about $0.5$–$20\,\mathrm{Hz}$) the viscous endolymph integrates acceleration once, and the canal actually reports angular velocity.

Sustained constant-velocity rotation is a stimulus below $0.03\,\mathrm{Hz}$: the cupula returns to its original position with $\tau_1$, the afferent signal vanishes, and the person feels that the rotation has stopped; on sudden stopping, the endolymph continues to flow, the cupula deflects in the opposite direction, and the person feels rotation in the opposite direction. The central "velocity storage" mechanism extends the decay time constant of the vestibulo-ocular reflex to about $15\,\mathrm{s}$.

![Torsion pendulum model of the semicircular canal (Eq. (42.9), τ₁ = 5 s, τ₂ = 4 ms). A: gain and phase of cupula deflection relative to head angular velocity; between about 0.03 and 40 Hz the gain is flat and the phase near zero, so the canal is an angular velocity sensor; shading is the frequency band of natural head movements. B: constant-velocity rotation at 60°/s for 45 s, then stopping: the cupula (afferent) signal decays to zero with τ₁ = 5 s and reappears with the opposite sign at stopping (post-rotatory sensation in the opposite direction); the slow-phase velocity of the vestibulo-ocular reflex is extended to about 15 s by central velocity storage (illustrated here by a first-order process with time constant 15 s)](./plots/canal-model.py)

### 42.5.3. Otolith Organs and Linear Acceleration

The receptor apparatus of the utricle and saccule is the macula: the hair bundles of hair cells are inserted into the overlying gelatinous otolithic membrane, in which are embedded otoconia consisting of calcium carbonate (calcite) crystals, with a density of about $2.7\,\mathrm{g\,cm^{-3}}$, much greater than that of endolymph. When the head undergoes linear acceleration or tilts relative to gravity, the otolithic membrane slides relative to the macula because of inertia and gravity, deflecting the hair bundles. In the upright human, the macula of the utricle is approximately horizontal and senses mainly horizontal acceleration; the macula of the saccule is approximately vertical and senses mainly vertical acceleration and gravity. The polarity of hair cells on each macula is arranged by direction and reverses on the two sides of the central striola, so linear acceleration in any direction excites some hair cells and inhibits others.

Because of the **equivalence principle**, the otolith organs alone cannot distinguish tilt of the head from linear acceleration: both appear as shear of the otolithic membrane. The central nervous system combines the rotation signals reported by the semicircular canals to distinguish them (tilt is accompanied by rotation, translation is not). This mechanism can fail during acceleration at takeoff in aircraft, and pilots may mistakenly believe the nose is pitching up (somatogravic illusion). When otoconia become dislodged and enter the posterior semicircular canal, changes of head position make them roll in the canal and push the cupula, causing brief, intense vertigo; this is the most common vertigo, benign paroxysmal positional vertigo, treated with positional maneuvers that roll the otoconia back into the utricle.

### 42.5.4. Vestibular Reflexes and Central Connections

Fibers of the vestibular nerve reach the vestibular nuclei of the brainstem (superior, medial, lateral, and inferior nuclei) and the flocculonodular lobe of the cerebellum. Vestibular signals are used for three classes of reflexes:

- The *vestibulo-ocular reflex*: when the head turns, the eyes rotate at the same speed in the opposite direction, keeping the image on the retina stable. It passes through only three levels of neurons (vestibular ganglion → vestibular nucleus → oculomotor, trochlear, or abducens nucleus), has a latency of about $10\,\mathrm{ms}$, and a gain (ratio of eye velocity to head velocity) close to 1. The gain is plastic: after days of wearing glasses that magnify or reverse the visual field, the gain changes accordingly, and this motor learning depends on the cerebellum ([7.14.45](/7.14.45)).
- Vestibulospinal and vestibulocollic reflexes: the lateral vestibulospinal tract excites antigravity extensor muscles and maintains posture and balance, and is a component of **postural reflexes**; in the **decerebrate rigidity** of decerebrate animals, the excitation of extensors by the vestibular nuclei loses inhibition from higher centers ([7.14.44](/7.14.44)).
- Vestibular autonomic responses: when the vestibular organs are stimulated too strongly or for too long, nausea, vomiting, sweating, pallor, and changes in heart rate and blood pressure appear; motion sickness is thought to originate from conflict between vestibular and visual signals.

**Definition 42.5.2 (Nystagmus)** The involuntary back-and-forth eye movement caused by sustained vestibular stimulation (or sustained motion of the visual field), consisting of alternating slow and fast phases in opposite directions, is called **nystagmus**. The slow phase is the compensatory movement of the vestibulo-ocular reflex, and the fast phase is a resetting saccade that returns the eye to the center of the orbit; the direction of nystagmus is named for the fast phase.

For example, when a person begins to rotate to the left, the left horizontal canal is excited, and the eyes first move slowly to the right (slow phase), then at the edge of the orbit jump quickly back to the left (fast phase), over and over; after constant-velocity rotation has continued for some time the nystagmus disappears, and when rotation stops suddenly, nystagmus in the opposite direction appears. Irrigating the external auditory canal with warm or cold water can create convection in the endolymph and stimulate the horizontal canal of one side alone, causing nystagmus (caloric test, Bárány, Nobel Prize 1914), used to assess vestibular function on one side.

Vestibular signals reach several cortical areas of the parietal lobe and insula through the thalamus, where they are integrated with vision and **proprioception** to form the perception of self-motion and spatial orientation. The vestibular system has no separate "vestibular cortex", and vestibular sensation is usually not noticed unless something goes wrong.

### 42.5.5. The Four-Level Framework of Hearing and Vestibular Sensation

Comparing hearing and the vestibular sense with the four-level framework of Chapter 39 ([7.14.39](/7.14.39#sec-39.5.1)), we see that, like touch, their differences are concentrated at the level of "mechanical computation":

| Level | Hearing | Vestibular sense |
|---|---|---|
| 1. External stimulus | Pressure oscillation in air (frequency, intensity, arrival time) | Angular acceleration, linear acceleration, and gravity of the head |
| 2. Mechanical computation | Resonance of the ear canal and spectral filtering by the pinna; impedance matching of the middle ear; traveling wave of the basilar membrane spreading frequency into position; active amplification and compression by outer hair cells | Endolymph–cupula torsion pendulum integrating angular acceleration into angular velocity; mass of otoconia converting linear acceleration into shear |
| 3. Cellular coding | Direct gating of the gating spring and TMC channels, fast and slow adaptation; ribbon synapses; phase locking, threshold-graded fibers | The same transduction channels; high spontaneous firing, bidirectional coding |
| 4. Central processing | Binaural comparison in the superior olive, tonotopic maps of the inferior colliculus and auditory cortex | Push–pull comparison in the vestibular nuclei, vestibulo-ocular reflex, gain calibration by the cerebellum, integration with vision and proprioception |

The cochlear amplifier blurs the boundary between levels 2 and 3: it is a mechanical computation element powered by cells (outer hair cells), using electrical signals in turn to change the movement of the mechanical structure. This shows that the four-level framework is a tool of analysis and not a strict partition of biological structure.

## 42.6. Evolution and Comparison

### 42.6.1. Hair Cells and the Lateral Line

Hair cells are a cell type specific to vertebrates, but their mode of operation (hair bundle, graded arrangement, direct gating) is highly conserved in all vertebrates, from lampreys to humans. The oldest site of use may be the lateral line.

**Definition 42.6.1 (Lateral Line)** The mechanosensory system of fish and aquatic amphibians, distributed along the two sides of the body and on the head and composed of many neuromasts, in each of which the hair bundles of hair cells extend into a gelatinous cupula and sense the movement of the surrounding water, is called the **lateral line**.

Superficial neuromasts are directly exposed to the water and are deflected by the flow, reporting flow velocity; canal neuromasts are buried in fluid-filled canals under the skin and are sensitive to the acceleration of the water (the pressure gradient along the canal) (Chapter 39, [7.14.39](/7.14.39#sec-39.8)). The lateral line is used in schooling, orienting against a current, avoiding predators, and capturing prey, and blind cave fish rely mainly on it to detect obstacles around them. Both the inner ear and the lateral line develop from ectodermal **placodes** of the head ([7.5.22](/7.5.22#sec-22.1)), and the development of hair cells is controlled by the same transcription factors (such as Atoh1).

### 42.6.2. Hearing in Fish

Sound in water contains two components: pressure waves, and the back-and-forth movement of water particles. The density of a fish's body is close to that of water, so it moves along with the water, whereas otoliths are dense and their movement lags behind the body, deflecting hair cells. All fish can therefore sense the particle motion of sound with the otolith organs, like an inertial accelerometer, but are sensitive only to low-frequency (below a few hundred hertz), nearby sounds.

Sensing pressure requires a compressible structure: the gas in the swim bladder expands and contracts under sound pressure, converting pressure into displacement. Otophysans (carp, catfish, and others, making up about two thirds of freshwater fish species) use a chain of small bones derived from the first few vertebrae (the Weberian apparatus) to transmit the vibration of the swim bladder to the inner ear, which greatly lowers the hearing threshold and extends the audible frequency to $3$–$4\,\mathrm{kHz}$. This is a convergence on the same principle as impedance matching in the mammalian middle ear. Certain clupeid fish (American shad) can even hear ultrasound of $180\,\mathrm{kHz}$, possibly to avoid dolphin echolocation (Mann et al., 1997).

### 42.6.3. Multiple Origins of the Tympanic Ear and the Mammalian Middle Ear

Land vertebrates face the impedance mismatch between air and the inner-ear fluid. The tympanic ear, which solves this problem with an eardrum and ossicles, arose independently at least five times in the Triassic in frogs, turtles, lepidosaurs (lizards and snakes), archosaurs (crocodilians and birds), and mammals (Clack). Nonmammalian tetrapods have only one ossicle (the columella, **homologous** to the mammalian stapes), whereas mammals have three, malleus, incus, and stapes.

The two extra ossicles of mammals come from the jaw joint of reptilian ancestors: the malleus from the articular bone of the lower jaw and the incus from the quadrate bone of the upper jaw (Reichert–Gaupp theory). In embryology both bones develop from the cartilage of the first **pharyngeal arch** ([7.5.30](/7.5.30)), and the fossil record (such as *Yanoconodon* and *Liaoconodon* from Liaoning, China, Meng et al., 2011) shows intermediate stages in which the middle ear bones gradually detach from the jaw ([7.10.32](/7.10.32#sec-32.1.2)). The lever system of three ossicles, the long coiled cochlea, and outer hair cells with prestin motors enable mammals to hear sounds above $10\,\mathrm{kHz}$, which is unique to mammals; many small mammals reach an upper limit of $50$–$100\,\mathrm{kHz}$, possibly so that animals with very small heads can still use ILD for localization (Heffner). The upper limit of hearing in birds and reptiles generally does not exceed $10\,\mathrm{kHz}$.

Nonmammals have no prestin-type outer hair cells, and part of their frequency selectivity comes from electrical tuning of the hair cells themselves: in the turtle cochlea, the voltage-gated $\ce{Ca^2+}$ channels and $\ce{Ca^2+}$-activated $\ce{K+}$ channels (BK channels) of each hair cell form an electrical resonance circuit, whose resonant frequency varies from the low-frequency end to the high-frequency end with the number and kinetics of BK channels in the hair cell, reaching several hundred hertz (Crawford and Fettiplace, 1981). Active movement of the hair bundle itself also provides amplification.

### 42.6.4. Insect Ears

Insect tympanal organs arose independently about 20 times in at least seven orders and are located on almost any part of the body: on the foreleg tibia in crickets and katydids, on the first abdominal segment in locusts and many moths, on the ventral thorax in mantids, and on the wing veins in lacewings. All evolved from a chordotonal organ (a stretch receptor) together with a thin cuticular tympanum and an air sac behind it. The ear of a noctuid moth has only two receptor cells, yet can hear the ultrasound of bats tens of meters away and trigger evasive flight (Roeder); the Johnston's organ in the antenna of mosquitoes (about $15\,000$ receptor cells) is used to hear the wingbeat of a mate.

The ear of the parasitoid fly *Ormia ochracea* is a brilliant mechanical design. The female finds hosts to parasitize by listening to the calling song of male crickets (about $5\,\mathrm{kHz}$), but its two tympana are only about $0.5\,\mathrm{mm}$ apart, so the binaural cues it can use are astonishingly small.

**Example 42.6.1** With the ears $0.5\,\mathrm{mm}$ apart, the maximum ITD for a source directly to the side is only $0.5\times10^{-3}/343 \approx 1.5\,\mu\mathrm{s}$, and the wavelength of a $5\,\mathrm{kHz}$ sound wave ($7\,\mathrm{cm}$) is much larger than the body, so there is almost no ILD. The two tympana of *Ormia* are joined by a cuticular "seesaw", forming a coupled oscillator with two vibration modes, rocking and bending; after the two modes are superposed, the time difference between the vibrations of the two tympana is amplified to about $50\,\mu\mathrm{s}$ and the level difference to a few decibels (Miles, Robert, and Hoy, 1995). The fly can localize a source to about $2^\circ$ (Mason et al., 2001), comparable to humans, and this principle has been used in designing miniature directional microphones.

### 42.6.5. Echolocation

**Definition 42.6.2 (Echolocation)** The behavior in which an animal actively emits sound and receives and analyzes the echoes reflected from objects to determine their distance, direction, size, texture, and motion is called **echolocation**.

Echolocation evolved independently many times in bats (confirmed by Griffin in the 1940s), toothed whales, a few cave-dwelling birds (oilbirds, swiftlets), and in shrews and tenrecs. Distance is given by the echo delay $\tau = 2d/c$: in air about $5.8\,\mathrm{ms}$ per meter.

- Frequency-modulated (FM) bats (such as the big brown bat) emit short calls sweeping from about $100\,\mathrm{kHz}$ to $20\,\mathrm{kHz}$ within a few milliseconds; the broad bandwidth makes measurement of delay (and thus distance) very precise; the auditory centers contain neurons sensitive to particular delays, forming a "range map". In the final phase of pursuit, the call rate increases to about 200 per second (terminal buzz).
- Constant-frequency–frequency-modulated (CF–FM) bats (such as horseshoe bats, CF about $83\,\mathrm{kHz}$) emit calls dominated by a long constant-frequency tone and use the **Doppler effect** to detect motion and the fluttering of insect wings. When a bat flies toward an object at speed $v$, the echo frequency rises by about $f(1 + 2v/c)$; at $v = 5\,\mathrm{m\,s^{-1}}$ it rises about 3 % (about $2.4\,\mathrm{kHz}$ at $83\,\mathrm{kHz}$). Horseshoe bats lower their emission frequency so that the echo always falls on one very narrow reference frequency (Doppler compensation, Schnitzler, 1968); in their cochlea this frequency occupies an unusually long stretch with extremely sharp tuning, called an "acoustic fovea".

The bat's call can exceed $120\,\mathrm{dB}$ at $10\,\mathrm{cm}$ in front of the mouth, and the middle ear muscles contract in synchrony with emission, protecting the cochlea and restoring sensitivity before the echo arrives. Toothed whales (dolphins) produce brief clicks of $40$–$150\,\mathrm{kHz}$ with "phonic lips" in the nasal passages, focused into a beam by the fat-filled melon of the head like a lens, and echoes reach the middle ear through fat channels in the lower jaw. The prestin genes of bats and toothed whales have undergone parallel amino acid substitutions (Liu et al., 2010; Li et al., 2010), an example of molecular **convergent evolution**. Some blind people have also learned to echolocate with tongue clicks.

### 42.6.6. Sound Localization in the Barn Owl, and Infrasound

The barn owl can catch mice in complete darkness by sound alone, with a localization accuracy of about $1^\circ$–$2^\circ$. Its auditory nerve fibers can phase-lock to about $9\,\mathrm{kHz}$, far higher than in mammals; in the nucleus laminaris of the brainstem, axons from the two ears form delay lines, exactly the biological implementation of the Jeffress model (Carr and Konishi, 1990). The openings of the owl's two ears are one high and one low, and the feathers of the facial ruff gather sound toward the ear openings like reflectors, so ILD varies mainly with elevation and ITD with azimuth; in the external nucleus of the inferior colliculus in the midbrain, the two cues are combined into an "auditory space map" in which neurons are arranged by spatial position (Knudsen and Konishi, 1978).

Low-frequency sound is little absorbed and diffracts strongly, suiting long-distance communication. Elephants emit low rumbles of $14$–$35\,\mathrm{Hz}$ (fundamentals below the human hearing threshold) that can travel several kilometers in air and also through the ground, to be sensed by the elephant's feet; the $10$–$40\,\mathrm{Hz}$ calls of baleen whales (blue whale, fin whale) can travel hundreds of kilometers in the ocean sound channel. Pigeons are sensitive to infrasound as low as about $0.05\,\mathrm{Hz}$ (Kreithen and Quine, 1979). The wavelength of infrasound is tens of meters to kilometers, and for small animals the ITD is extremely small and localization is difficult, which is one reason low-frequency hearing is found mostly in large animals or used for long-range detection.

## Summary

| Topic | Key points |
|---|---|
| Sound (Example 42.1.1) | $I = p^2/Z$; sound pressure level $20\log_{10}(p/20\,\mu\mathrm{Pa})$; air displacement at threshold about $10^{-11}\,\mathrm{m}$; $20\,\mathrm{Hz}$–$20\,\mathrm{kHz}$, loudness about $\propto I^{0.3}$ |
| Outer ear | Spectral cues of the pinna; resonance of the ear canal at $c/4\ell \approx 3.4\,\mathrm{kHz}$ |
| Impedance matching (Definition 42.2.1) | Direct air–water transmission is only about 0.1 % (Eq. (42.3)); area ratio 17 × lever 1.3 ≈ 22-fold (about $27\,\mathrm{dB}$); the lever amplifies force only 1.3-fold |
| Acoustic reflex | Stapedius and tensor tympani; latency $40$–$80\,\mathrm{ms}$; attenuates low frequencies by $30$–$40\,\mathrm{dB}$ |
| Cochlea (Definitions 42.3.1, 42.3.2) | Three scalae; endolymph high in $\ce{K+}$, endocochlear potential $+80\,\mathrm{mV}$, transduction current carried by $\ce{K+}$; inner hair cells transmit information, outer hair cells amplify |
| Place principle (Definition 42.3.3, Formula 42.3.1) | Traveling wave; basilar membrane from stiff to soft; Greenwood $f = 165.4(10^{2.1y} - 0.88)$, about $5\,\mathrm{mm}$ per octave; phase locking at low frequency |
| Transduction | Tip links, TMC channels, microsecond direct gating; Boltzmann curve of the gating spring (Eq. (42.6)); fast and slow adaptation shift the operating point |
| Cochlear amplifier (Definitions 42.3.4, 42.3.5) | Prestin electromotility; amplification of $40$–$60\,\mathrm{dB}$, compression, sharp tuning; otoacoustic emissions and newborn screening |
| Loudness | Firing rate, spatial recruitment, threshold-graded fibers |
| Central pathway | Cochlear nucleus → superior olive → lateral lemniscus → inferior colliculus → medial geniculate → transverse temporal gyrus; bilateral, tonotopic |
| Localization (Definition 42.4.1) | ITD (Eq. (42.7), maximum about $0.66\,\mathrm{ms}$, low frequency, medial superior olive, Jeffress); ILD (high frequency, lateral superior olive) |
| Semicircular canals (Definition 42.5.1) | Torsion pendulum model (Eqs. (42.8)–(42.9)), $\tau_1 \approx 5\,\mathrm{s}$, $\tau_2 \approx 4\,\mathrm{ms}$, reporting angular velocity in the natural frequency band |
| Otolith organs | Utricle and saccule; linear acceleration and gravity; tilt–translation ambiguity; benign positional vertigo |
| Vestibular reflexes (Definition 42.5.2) | Vestibulo-ocular reflex (three levels of neurons, about $10\,\mathrm{ms}$, plastic gain), vestibulospinal reflex, nystagmus, caloric test |
| Evolution | Lateral line (Definition 42.6.1); fish otoliths and Weberian apparatus; tympanic ear arose at least five times, mammalian three ossicles from the jaw joint; electrical tuning of hair cells; insect tympanal organs and *Ormia* (Example 42.6.1); echolocation (Definition 42.6.2) and Doppler compensation; barn owl; infrasound |

## Questions

1. A person's ossicular chain is fixed by otosclerosis (the stapes cannot move). By roughly how much will his hearing threshold for a $1\,\mathrm{kHz}$ sound rise? Why is the bone-conduction threshold essentially unchanged?

   **Answer** Impedance matching by the middle ear provides a gain of about $27\,\mathrm{dB}$; with the ossicular chain fixed, sound can act only through the air in the tympanic cavity directly on the oval and round windows, whose pressures are nearly equal and cancel each other, and with the impedance mismatch between air and liquid (Eq. (42.3), about $30\,\mathrm{dB}$), the threshold typically rises by $30$–$60\,\mathrm{dB}$. In bone conduction, sound vibrates the skull and inner ear as a whole, bypassing the middle ear, and the cochlea and auditory nerve are normal, so the bone-conduction threshold is normal: poor air conduction with normal bone conduction is the hallmark of conductive hearing loss.

2. Use the Greenwood function (Eq. (42.4)) to calculate the distance in millimeters between the characteristic places of $1\,\mathrm{kHz}$ and $2\,\mathrm{kHz}$ (basilar membrane length $35\,\mathrm{mm}$). Why does an octave occupy about the same length of basilar membrane in the high-frequency range but a shorter length in the low-frequency range?

   **Answer** From $10^{2.1y} = f/165.4 + 0.88$: for $f = 1000$, $10^{2.1y} = 6.926$ and $y = 0.400$; for $f = 2000$, $10^{2.1y} = 12.97$ and $y = 0.530$. The separation is $0.130\times35 \approx 4.6\,\mathrm{mm}$. When $f \gg 165.4\times0.88 \approx 146\,\mathrm{Hz}$, the constant $0.88$ can be neglected, $f \propto 10^{2.1y}$, and a fixed frequency ratio (one octave) corresponds to a fixed difference in $y$ of $\log_{10}2/2.1 = 0.143$, about $5\,\mathrm{mm}$; in the low-frequency range the constant term cannot be neglected, $f$ varies approximately linearly with $y$, the increment of $y$ needed to double the frequency becomes smaller, and so low-frequency octaves are compressed near the apex.

3. The long time constant of the semicircular canal is $\tau_1 \approx 5\,\mathrm{s}$. If a person sitting on a rotating chair has been turning at constant angular velocity for $30\,\mathrm{s}$, does he still feel he is rotating at $30\,\mathrm{s}$? What happens after a sudden stop? If $\tau_1$ were only $0.5\,\mathrm{s}$, what would be the effect on everyday head movements?

   **Answer** Constant-velocity rotation is equivalent to a step in angular velocity at $t = 0$; by Eq. (42.9), the cupula deflection decays as $\mathrm{e}^{-t/\tau_1}$; after $30\,\mathrm{s}$ it is $\mathrm{e}^{-6} \approx 0.25\,\%$, the afferent signal has essentially returned to the resting level (with the central velocity storage time constant of about $15\,\mathrm{s}$, only about $\mathrm{e}^{-2} \approx 14\,\%$ remains), and he feels that rotation has almost stopped. On a sudden stop, a reverse step of angular velocity appears, the cupula deflects in the opposite direction, producing the sensation of rotating in the opposite direction and nystagmus in the opposite direction, which fade with the same time constant. If $\tau_1 = 0.5\,\mathrm{s}$, the low-frequency cutoff of the canal as an angular velocity sensor would rise to $1/(2\pi\times0.5) \approx 0.3\,\mathrm{Hz}$, close to the frequencies of slow head turning and body sway in walking; the angular velocities of these movements would be underestimated and phase-advanced, the vestibulo-ocular reflex could not compensate accurately, and the image on the retina would slip, causing blurred vision and oscillopsia.

4. Why does the upper limit of phase locking in human hearing (about $4$–$5\,\mathrm{kHz}$) differ from the upper limit of effective ITD cues (about $1.5\,\mathrm{kHz}$)? Barn owls can phase-lock up to $9\,\mathrm{kHz}$; what is the use of this?

   **Answer** The upper limit of phase locking is set by the temporal precision of hair cell synapses and afferent fiber firing, whereas the upper limit of effective ITD is set by geometry: when the period of the sound wave is shorter than twice the maximum ITD ($2\times0.66 = 1.3\,\mathrm{ms}$, that is, above about $0.76\,\mathrm{kHz}$), the same phase difference corresponds to several possible azimuths and comparing phase becomes ambiguous; by about $1.5\,\mathrm{kHz}$ the period is comparable to the maximum ITD and the ambiguity is so severe that the cue is essentially lost (see panel C of the figure). The human head is large, so the ambiguity of ITD appears before the upper limit of phase locking, and high frequencies must rely on ILD. The owl's head is small (ears about $5\,\mathrm{cm}$ apart, maximum ITD about $0.17\,\mathrm{ms}$), and ambiguity does not appear until about $3$–$6\,\mathrm{kHz}$; the rustling of mice is mainly at $3$–$9\,\mathrm{kHz}$, and phase locking to $9\,\mathrm{kHz}$ lets it use ITD directly in this band, then combine information across several frequency channels centrally to remove residual ambiguity, while using the asymmetric ear openings to leave ILD for elevation.

5. (Open question) Amplification by outer hair cells raises the sensitivity of the cochlea about 1000-fold, but it also brings problems. Discuss the costs of this design in terms of energy, noise, and damage.

   **Answer** Key points: (1) Energy: prestin of outer hair cells itself consumes no ATP, but it depends on the transduction current driven by the endocochlear potential, which is maintained by ion pumps of the stria vascularis; the cochlea is a tissue of very high metabolic rate, and with ischemia or hypoxia the endocochlear potential falls rapidly and the amplifier fails first. (2) Noise and stability: an active amplifier works at the edge of oscillation (near a Hopf bifurcation), amplifying noise as well as signal and occasionally self-oscillating, forming spontaneous otoacoustic emissions, which may be the source of some tinnitus; the central nervous system adjusts gain through the medial olivocochlear bundle, reducing amplification in noise to improve signal-to-noise ratio. (3) Damage: outer hair cells are especially sensitive to loud noise, ototoxic drugs (**aminoglycosides**, cisplatin), and aging, and mammalian hair cells cannot regenerate (those of birds and fish can); after loss of outer hair cells the amplifier is permanently lost, the threshold rises by $40$–$60\,\mathrm{dB}$ and frequency selectivity is lost, the most common sensorineural hearing loss; hearing aids can only amplify sound and cannot restore the sharpness of tuning, so understanding speech in noise remains difficult.
