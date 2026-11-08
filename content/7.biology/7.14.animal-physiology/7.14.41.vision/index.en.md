---
title: Vision
description: Optics of the eye, accommodation and refractive errors, pupil and intraocular pressure; retina, rods and cones, rhodopsin and the visual cycle, phototransduction and adaptation, color vision; retinal circuits; central visual pathways and cortex; eye movements; evolution and comparison of eyes.
source_hash: ddc5663eed85
---

Of all human senses, vision provides the most information: about a third of the cerebral cortex takes part in visual processing. The eye must do three things: form a sharp image on the retina (optics), convert photons into neural signals (phototransduction), and perform a first round of processing of the image before sending it to the brain (retinal circuits). This chapter treats these three layers in turn, then the central visual pathways and eye movements, and finally compares the diversity of eyes in the animal kingdom. The general principles of sensation (the **labeled line principle**, **receptor potentials**, **adaptation**, **receptive fields**, and **lateral inhibition**) are in Chapter 39 ([7.14.39](/7.14.39)); the physics of photons, pigments, and single-photon detection was discussed in biophysics ([7.6.18](/7.6.18#sec-18.6)), and diffraction and resolving power in optics ([5.4.2](/5.4.2#sec-2.4)); only their conclusions are used here, and the emphasis is on the physiology of organs and circuits.

## 41.1. Optics of the Eye

### 41.1.1. Light, Refraction, and Diopters

The wavelengths of electromagnetic radiation visible to the human eye are about $380$–$760\,\mathrm{nm}$, corresponding to photon energies of about $3.3$–$1.6\,\mathrm{eV}$: enough to isomerize retinal, but not enough to break most chemical bonds ([7.6.18](/7.6.18#sec-18.1.2)). Light travels in a medium at speed $c/n$, where $n$ is the **refractive index** of the medium (1.333 for water). When light strikes obliquely the interface between two media of different refractive index, it changes direction according to **Snell's law** $n_1\sin\theta_1 = n_2\sin\theta_2$; at normal incidence it is not deflected. A convex lens makes parallel light converge at a focal point, a concave lens makes it diverge, and a convex lens forms an inverted real image of a distant object.

**Definition 41.1.1 (Diopter)** The ability of a lens or refracting surface to bend light is measured by the reciprocal of the focal length, called refractive power; the reciprocal of the focal length in meters is called the **diopter**, denoted D:

$$
P = \frac{1}{f}, \qquad 1\,\mathrm{D} = 1\,\mathrm{m^{-1}}.
$$
The power of a converging lens is positive and that of a diverging lens negative; for thin lenses in close contact, the powers add approximately.

For a spherical refracting surface with refractive indices $n_1$ and $n_2$ on its two sides and radius of curvature $r$, the refractive power is $P = (n_2 - n_1)/r$: the greater the difference in refractive index across the surface and the more curved the surface, the greater the power. To calculate imaging with diopters, the object distance $s$ and image distance $s'$ can be written as additive "vergences":

$$
\frac{n'}{s'} = \frac{n}{s} + P, \tag{41.1}
$$
where $n/s$ is the vergence of the light arriving at the refracting surface (negative for divergence), and $n'/s'$ is the vergence leaving it. Light from a distant object is parallel and has zero vergence.

### 41.1.2. The Refractive System of the Eye and the Reduced Eye

The refractive system of the eye consists of the cornea, aqueous humor, lens, and vitreous body, with four refracting surfaces. The refractive indices of the media are similar (cornea about $1.38$, aqueous humor $1.33$, lens about $1.40$ on average, vitreous body $1.34$); only between air and cornea is the difference large, so:

- the anterior surface of the cornea contributes about two thirds of the refractive power (about $40$–$43\,\mathrm{D}$), but its shape is fixed;
- the lens contributes about one third (about $20\,\mathrm{D}$ in the eye), but its refractive power can change, and it is the site of accommodation.

When viewing a distant object, the total refractive power of the eye is about $59$–$60\,\mathrm{D}$. In water, the medium outside the cornea becomes water of refractive index $1.33$ and the cornea almost loses its refractive power, which is exactly why people see blurred under water (Section 41.6 discusses how aquatic animals solve this problem).

In calculations the eye is often simplified to the *reduced eye*: a single refracting surface of radius of curvature about $5.6\,\mathrm{mm}$, internal refractive index $1.336$, with the nodal point about $5.6\,\mathrm{mm}$ behind the refracting surface and about $17\,\mathrm{mm}$ from the retina. Rays through the nodal point are not deflected, so the ratio of image size to object size equals the ratio of their distances from the nodal point:

$$
\frac{\text{image height}}{\text{object height}} = \frac{17\,\mathrm{mm}}{\text{object distance}}. \tag{41.2}
$$

**Example 41.1.1** A person 1.8 m tall at 10 m has a retinal image height of $1.8\,\mathrm{m}\times 17\,\mathrm{mm}/10\,\mathrm{m} \approx 3.1\,\mathrm{mm}$, inverted. Conversely, a visual angle of $1'$ ($2.9\times10^{-4}\,\mathrm{rad}$) corresponds on the retina to $17\,\mathrm{mm}\times2.9\times10^{-4} \approx 5\,\mu\mathrm{m}$, about the spacing of two foveal cones.

The image on the retina is inverted, and the brain does not need to "flip" it: the perception of space is established by the correspondence between retinal position and body movement, and the orientation of the image itself has no meaning.

### 41.1.3. Accommodation and the Near Point

The normal eye, fully relaxed, images distant objects (beyond about 6 m, where rays are approximately parallel) on the retina. When viewing a near object, the light arrives at the eye diverging, and by Eq. (41.1), if the refractive power does not change, the image falls behind the retina; the eye must increase its refractive power.

**Definition 41.1.2 (Accommodation)** The process by which the eye changes its refractive power according to the distance of the object so as to keep the image sharp is called **accommodation**. The farthest point seen clearly without accommodation is called the far point; the nearest point seen clearly with maximal accommodation is called the **near point**. The amplitude of accommodation is the difference between the vergences corresponding to the two:

$$
A = \frac{1}{d_{\text{near}}} - \frac{1}{d_{\text{far}}}\quad(\mathrm{D},\ d\ \text{in meters}). \tag{41.3}
$$

Accommodation is accomplished by changes in the shape of the lens (Helmholtz's theory of accommodation). The lens is an elastic capsule connected at its periphery to the ciliary body by the suspensory ligaments (zonules):

- when viewing far, the ciliary muscle relaxes, the ring formed by the ciliary body has a larger diameter, the zonules are taut, and the lens is pulled flat, with small refractive power;
- when viewing near, the ciliary muscle (mainly the circular fibers) contracts, the ring diameter decreases, the zonules slacken, and the lens becomes more convex by its own elasticity (especially the anterior surface), increasing its refractive power.

The ciliary muscle is innervated mainly by parasympathetic fibers in the oculomotor nerve (through the ciliary ganglion, transmitter acetylcholine acting on M3 receptors); this is the action of the **parasympathetic nervous system**, and the sympathetic contribution is small. In a child the refractive power of the lens can increase from about $20\,\mathrm{D}$ to about $34\,\mathrm{D}$, an amplitude of accommodation of about $14\,\mathrm{D}$ and a near point of only about $7\,\mathrm{cm}$. When viewing a near object, accommodation always occurs together with vergence of the two eyes (convergence, directing the visual axes of both eyes to the near object) and pupillary constriction, called the near triad.

**Definition 41.1.3 (Presbyopia)** With increasing age, the lens continues to grow and thicken and loses elasticity and can no longer become more convex when the zonules slacken; the amplitude of accommodation gradually decreases, the near point recedes, and near vision becomes difficult. This is called **presbyopia**.

The amplitude of accommodation falls steadily from about $14\,\mathrm{D}$ in a child to an average of about $3.5\,\mathrm{D}$ at 50 years (about $2.5$–$5\,\mathrm{D}$ between individuals) and approaches zero in the sixties. Hofstetter's empirical formula gives the average $A \approx 18.5 - 0.3\times\text{age}$ (D) and the minimum about $15 - 0.25\times\text{age}$ (D). A reading distance of about $40\,\mathrm{cm}$ requires $2.5\,\mathrm{D}$ of accommodation; since only about half of the amplitude can be used comfortably for sustained reading, reading glasses with convex lenses are needed once the amplitude drops below about $5\,\mathrm{D}$ (usually in the forties). Because reading glasses focus for only one fixed distance, people who need to see both far and near use bifocal or progressive lenses: the upper part for distance and the lower part for near.

**Remark 41.1.1** Presbyopia and hyperopia are two different things and should not be confused. Hyperopia is insufficient refractive power of the eye relative to axial length (Section 41.1.4), can occur at any age, and requires accommodation even for distant viewing; presbyopia is the loss of accommodative ability with age and occurs in emmetropic, myopic, and hyperopic eyes alike. Both are corrected for near vision with convex lenses, which is why they are often confused; but a presbyopic person can see far without glasses (if originally emmetropic), whereas a hyperopic person also needs correction for distance.

![Refractive errors and presbyopia. A: paraxial ray tracing of a reduced eye (single refracting surface of 60 D, internal refractive index 1.336, axial length of the emmetropic eye 1.336/60 m = 22.3 mm) for a distant object, with the eye relaxed. The image of the myopic eye (axial length 24.0 mm) falls in front of the retina and is corrected with a concave lens of about −4.6 D at 12 mm in front of the cornea; the image of the hyperopic eye (axial length 20.8 mm) falls behind the retina and is corrected with a convex lens of about +4.0 D (lens powers are found by the program so that the image falls exactly on the retina). B: amplitude of accommodation as a function of age, the minimum, mean, and maximum of Hofstetter (1950) (15 − 0.25 × age, 18.5 − 0.3 × age, 25 − 0.4 × age, in D; shading shows the range from minimum to maximum), and the corresponding near point of the emmetropic eye; the dashed line is the 2.5 D needed for reading at 40 cm](./plots/refraction.py)

### 41.1.4. Refractive Errors

When the eye is not accommodating and distant objects are imaged exactly on the retina, the eye is called emmetropic. Otherwise it is said to have a refractive error (ametropia):

| Type | Cause | Far point and near point | Correction |
|---|---|---|---|
| Myopia | Axial length too long (axial, most common) or refractive power too strong | Far point at a finite distance; near point nearer than in emmetropia | Concave lens (negative power) |
| Hyperopia | Axial length too short or refractive power too weak | Accommodation needed even for distance; near point farther than in emmetropia | Convex lens (positive power) |
| Astigmatism | Different curvature in different meridians of the cornea (or lens) | A point is imaged as two mutually perpendicular focal lines | Cylindrical lens or rigid corneal contact lens |

**Example 41.1.2** A myope whose far point is at $0.5\,\mathrm{m}$ has an excess of $1/0.5 = 2\,\mathrm{D}$ of refractive power for distant objects; the spectacles should turn parallel light from afar into diverging light that appears to come from $0.5\,\mathrm{m}$, that is, $-2\,\mathrm{D}$ (neglecting the distance from lens to cornea). If his amplitude of accommodation is $10\,\mathrm{D}$, by Eq. (41.3) the near point is $1/(10 + 2) \approx 8\,\mathrm{cm}$.

Each $1\,\mathrm{mm}$ of axial lengthening is equivalent to about $3\,\mathrm{D}$ of myopia (for a $60\,\mathrm{D}$ eye with image distance $22\,\mathrm{mm}$). The growth of the axial length in development is regulated by visual experience: defocus signals on the retina influence the growth of the sclera, as confirmed in experiments on chicks, tree shrews, and monkeys. The prevalence of myopia among urban adolescents in East Asia has risen sharply in recent decades, and little time spent outdoors is the risk factor with the most consistent evidence.

### 41.1.5. Pupil, Depth of Field, and the Pupillary Light Reflex

The opening at the center of the iris is the pupil, and the diameter of the human pupil can vary between $1.5$ and $8\,\mathrm{mm}$; the amount of light entering the eye is proportional to pupil area, so the pupil can regulate incident light by only about $(8/1.5)^2 \approx 30$-fold. Compared with the range of light intensities to which the eye can adapt ($10^{10}$-fold or more, Section 41.2.5), this is only a small part; the main value of the pupil lies in rapid adjustment and in improving imaging. The iris contains two kinds of smooth muscle: the circular sphincter pupillae is innervated by the **parasympathetic nervous system** and constricts the pupil when it contracts; the radial dilator pupillae is innervated by the **sympathetic nervous system** and dilates the pupil when it contracts. Atropine (an M receptor blocker) dilates the pupil by blocking the parasympathetic innervation of the sphincter.

A small pupil increases the depth of field. When an object point is out of focus, it forms a blur circle on the retina whose angular diameter is approximately the product of the pupil diameter $D$ (m) and the defocus $\Delta P$ (D):

$$
\beta \approx D\,\Delta P\quad(\mathrm{rad}). \tag{41.4}
$$
For a pupil of $3\,\mathrm{mm}$ and defocus of $1\,\mathrm{D}$, $\beta \approx 3\times10^{-3}\,\mathrm{rad} \approx 10'$, about ten times the limit of visual acuity; if the pupil constricts to $1.5\,\mathrm{mm}$, the blur is halved. Squinting when we cannot see clearly is using the eyelids to reduce the effective aperture. The pupil cannot shrink indefinitely either: as the aperture decreases the diffraction limit ($1.22\lambda/D$) worsens, and the combined effect of aberration and diffraction is best near $2$–$3\,\mathrm{mm}$.

The *pupillary light reflex* is the reflex in which the pupils of both eyes constrict when light illuminates one eye, and it is composed of four levels of neurons:

1. Retinal ganglion cells (mainly intrinsically photosensitive ganglion cells, Section 41.3.5) project through the optic nerve and optic tract to the pretectal nucleus of the midbrain;
2. Neurons of the pretectal nucleus project to the Edinger–Westphal nuclei (accessory oculomotor nuclei) on both sides, and the bilateral projection makes both eyes respond at once (consensual light reflex);
3. Preganglionic parasympathetic fibers of the Edinger–Westphal nucleus travel with the oculomotor nerve to the ciliary ganglion;
4. Postganglionic fibers innervate the sphincter pupillae and constrict the pupil.

This **reflex arc** does not pass through the visual cortex, and clinically it is used to judge midbrain function: with injury to one optic nerve, light on the affected side constricts neither pupil, and light on the healthy side constricts both.

### 41.1.6. Aqueous Humor, Intraocular Pressure, and Other Structures of the Eye

The cornea is a transparent avascular epithelial tissue, nourished by aqueous humor and tears; tears are an ultrafiltrate of plasma that moisten the cornea, help $\ce{O2}$ dissolve and enter the cornea, and wash away foreign bodies. The epithelium of the ciliary body continuously secretes aqueous humor (about $2$–$3\,\mu\mathrm{L\,min^{-1}}$), which flows from the posterior chamber through the pupil into the anterior chamber, then through the trabecular meshwork of the anterior chamber angle into the canal of Schlemm and back to the veins. The balance between secretion and outflow maintains the *intraocular pressure*, on average about $15\,\mathrm{mmHg}$ ($2.0\,\mathrm{kPa}$; clinically intraocular pressure is still customarily given in mmHg, $1\,\mathrm{mmHg} = 133.3\,\mathrm{Pa}$), with a normal range of about $10$–$21\,\mathrm{mmHg}$. The intraocular pressure keeps the front of the eyeball in a state of slight pressurization, maintaining the shape and optical stability of the eye. Obstructed outflow raises intraocular pressure and, by long-term compression of the axons of the ganglion cells at the optic disc, causes progressive visual field loss, glaucoma; all treatments aim to lower intraocular pressure (reducing aqueous humor production or promoting outflow).

The lens is made of concentrically arranged fiber cells that have lost their nuclei and organelles, wrapped in a transparent capsule. The fiber cells are filled with a high concentration of crystallin proteins (α, β, γ crystallins), giving the lens a high and uniform refractive index; the refractive index at the center is higher than in the outer layers, and this gradient reduces spherical aberration. Crystallins are not renewed throughout life, and their aggregation makes the lens turbid, which is a cataract. The vitreous body is a transparent gel filling the back of the eyeball.

### 41.1.7. Visual Acuity and Distance Perception

Visual acuity is the ability of the eye to resolve two adjacent object points, expressed as the smallest visual angle just resolvable. In the normal human eye it is about $1'$ (1.0 on the international standard chart, 5.0 on the logarithmic chart); under ideal conditions, two point sources $25''$ apart can be distinguished. Two factors determine visual acuity:

- Optics: the image a point source forms on the retina (the point spread function) has a diameter of about $11\,\mu\mathrm{m}$, determined jointly by diffraction and aberration. By the **Rayleigh criterion**, for a $3\,\mathrm{mm}$ pupil and $550\,\mathrm{nm}$ light, the limit is about $1.22\lambda/D \approx 0.8'$ ([7.6.18](/7.6.18#sec-18.6.6)).
- Sampling: foveal cones have a diameter of about $1.5\,\mu\mathrm{m}$ with a center-to-center spacing of about $2.5\,\mu\mathrm{m}$, so the image of a point source covers about 20 cones. Two points about $2\,\mu\mathrm{m}$ apart on the retina can be resolved as long as one less stimulated cone lies between them; $2\,\mu\mathrm{m}/17\,\mathrm{mm}$ is almost exactly $25''$. The sampling density of the fovea roughly matches the optical limit, neither wasteful nor undersampled.

Visual acuity falls rapidly with eccentricity: at $10^\circ$ from the fovea it is only about one fifth of that at the center, related to cone density and the degree of convergence of ganglion cells (Section 41.3.4). We therefore rely on eye movements (Section 41.5) to bring the object of interest onto the fovea.

There are several kinds of cues for estimating distance: the size of the retinal image of an object of known size; motion parallax (when the head moves, near objects move faster across the retina than far ones); and stereopsis. The two eyes are $I \approx 65\,\mathrm{mm}$ apart, and the position of the same object on the two retinas differs slightly (binocular disparity); the relation between disparity and depth is

$$
\delta \approx \frac{I\,\Delta d}{d^2}, \tag{41.5}
$$
where $d$ is the fixation distance and $\Delta d$ is the depth difference between two objects.

**Example 41.1.3** Human stereoacuity is about $20''$ ($10^{-4}\,\mathrm{rad}$). By Eq. (41.5), at $d = 1\,\mathrm{m}$ the resolvable depth difference is $\Delta d = \delta d^2/I \approx 1.5\,\mathrm{mm}$; at $100\,\mathrm{m}$ it is $15\,\mathrm{m}$. Depth resolution worsens with the square of distance, so stereopsis is most precise within arm's length and in practice ceases to work beyond about $100\,\mathrm{m}$, where we can rely only on monocular cues.

## 41.2. The Retina and Photoreceptors

### 41.2.1. Structure of the Retina

The retina develops from the optic vesicle growing out of the diencephalon in the embryo ([7.5.22](/7.5.22#sec-22.2.2)) and structurally belongs to the central nervous system. From outside (next to the choroid) to inside (next to the vitreous body), it is divided into the pigment epithelium, the photoreceptor layer (outer and inner segments), the outer nuclear layer (photoreceptor cell bodies), the outer plexiform layer (synapses of photoreceptors with bipolar and horizontal cells), the inner nuclear layer (cell bodies of bipolar, horizontal, and amacrine cells), the inner plexiform layer (synapses of bipolar cells, amacrine cells, and ganglion cells), the ganglion cell layer, and the nerve fiber layer.

The vertebrate retina is "inverted": light must first pass through several hundred micrometers of neural layers and blood vessels before reaching the photoreceptors, whereas the signals travel inward from the photoreceptors and are gathered at the ganglion cells into the optic nerve, which passes through the retina to leave the eye. The site where the optic nerve exits (optic disc) has no photoreceptors and forms the blind spot, located about $15^\circ$ nasal to the fovea. The inverted structure places the outer segments of photoreceptors against the pigment epithelium, which has several irreplaceable roles:

- melanin absorbs light that has passed through the photoreceptors, preventing reflection of light within the eye that would reduce image contrast;
- it stores vitamin A and performs the isomerization of retinal needed for regeneration of visual pigment (Section 41.2.3);
- it phagocytoses the tips of photoreceptor outer segments shed each day (rods renew about one tenth of the outer segment each day).

Scattering by the neural layers is compensated in two ways: the inner layers of the retina are transparent, and Müller glial cells guide light to the photoreceptors like optical fibers; in the most demanding central region, the inner layers are pushed aside.

**Definition 41.2.1 (Fovea)** A small pit at the center of the macula at the posterior pole of the retina, about $1.5\,\mathrm{mm}$ in diameter (about $5^\circ$ of visual angle), with inner-layer cells and blood vessels displaced to the periphery to leave a direct light path, is called the **fovea**. The central floor of the pit, about $0.3\,\mathrm{mm}$ in diameter (about $1^\circ$), is called the foveola; it contains only slender, densely packed cones and is the site of highest visual acuity.

### 41.2.2. Rods and Cones

A photoreceptor is divided into outer segment, inner segment, cell body, and synaptic terminal. The outer segment is the photosensitive part: the outer segment of a rod contains about 1000 membrane disks separated from the plasma membrane, and that of a cone is formed by folds of the plasma membrane; the membranes are densely packed with visual pigment. The inner segment is rich in mitochondria and supplies energy for the dark current of the outer segment and for protein synthesis. The synaptic terminal has a ribbon synapse, which can release glutamate continuously and in a graded manner.

The human retina has about $9\times10^7$ rods and $4$–$5\times10^6$ cones (Curcio et al., 1990). The two form two functionally complementary systems:

| Property | Rod system | Cone system |
|---|---|---|
| Visual pigment | Rhodopsin (peak $498\,\mathrm{nm}$) | Three cone pigments (S, M, L) |
| Sensitivity | High, can respond to a single photon | 30–300 times lower |
| Working range | Scotopic vision (starlight, moonlight); saturates in daylight | Photopic vision; hardly saturates |
| Response speed | Slow, long temporal integration (about $0.1\,\mathrm{s}$) | Fast, can resolve higher flicker frequencies |
| Convergence | High, many rods converge onto one ganglion cell | Low, one to one in the fovea |
| Acuity and color vision | Low, no color vision | High, with color vision |
| Distribution | Absent from the foveola; densest about $20^\circ$ from the center | Densest in the fovea, decreasing toward the periphery |

At intermediate luminance between the two (twilight), called mesopic vision, both systems work simultaneously. Looking slightly away from a dim star at night, so that the image falls on the parafoveal region densely packed with rods, makes use of this distribution.

### 41.2.3. Rhodopsin and the Visual Cycle

The visual pigment of rods is **rhodopsin** ([7.1.14](/7.1.14#def-14.4.1)), composed of opsin (a **G protein-coupled receptor**) and the chromophore 11-*cis*-retinal covalently bound within it. After absorbing a photon, 11-*cis*-retinal isomerizes to all-*trans*-retinal within about $200\,\mathrm{fs}$ (quantum yield about $0.67$, [7.6.18](/7.6.18#sec-18.6.1)), and opsin passes through a series of intermediate states to become active metarhodopsin II ($\mathrm{R}^*$), which initiates phototransduction (Section 41.2.4). All-*trans*-retinal is then hydrolyzed off the opsin, and the visual pigment is "bleached".

To restore sensitivity to light, the visual pigment must regenerate, a process called the visual cycle:

1. All-*trans*-retinal is reduced in the rod outer segment to all-*trans*-retinol (vitamin A) and transported to the pigment epithelium;
2. In the pigment epithelium it is esterified, then converted by the isomerohydrolase (RPE65) to 11-*cis*-retinol and oxidized to 11-*cis*-retinal;
3. 11-*cis*-Retinal returns to the outer segment and combines with opsin to form rhodopsin.

In addition to using the pigment epithelium, cones have a faster visual cycle through Müller cells, so cone pigment regenerates much faster (Section 41.2.5). Some retinal is always consumed in the cycle and must be replenished from vitamin A in the blood. Humans cannot synthesize vitamin A, and long-term insufficient intake first impairs scotopic vision, causing night blindness; severe deficiency dries the cornea and ultimately damages photoreceptors, and remains one of the leading causes of childhood blindness in the world.

### 41.2.4. Phototransduction

**Definition 41.2.2 (Phototransduction)** The process by which a photoreceptor converts the absorption of a photon into a change of membrane potential is called **phototransduction**.

In the dark, the cyclic nucleotide-gated channels (CNG channels) in the membrane of the rod outer segment are open because of the high intracellular cGMP concentration, and $\ce{Na+}$ and $\ce{Ca^2+}$ flow in continuously; $\ce{K+}$ channels in the inner segment let $\ce{K+}$ flow out, and the **Na⁺/K⁺-ATPase** of the inner segment pumps $\ce{Na+}$ out. This circulating current is called the dark current (Hagins et al., 1970); it keeps the photoreceptor in a state of **depolarization** in the dark (about $-40\,\mathrm{mV}$) and releasing glutamate continuously. On illumination:

1. $\mathrm{R}^*$ activates the G protein **transducin**;
2. The α subunit of transducin activates the phosphodiesterase PDE6;
3. PDE6 hydrolyzes cGMP, and the cGMP concentration falls;
4. CNG channels close, the dark current decreases, and the membrane undergoes **hyperpolarization** (to at most about $-70\,\mathrm{mV}$);
5. Glutamate release at the synaptic terminal decreases.

Vertebrate photoreceptors are among the few receptors that respond to the **adequate stimulus** by hyperpolarizing: the light signal is "less transmitter released". This cascade has enormous amplification: one $\mathrm{R}^*$ activates tens to over a hundred transducin molecules during its lifetime, each activated PDE6 hydrolyzes over a thousand cGMP per second, and opening of a CNG channel requires **cooperative binding** of about three cGMP (**Hill coefficient** about 3), making the current more sensitive to changes in cGMP. As a result, one photon closes hundreds of channels, blocking the entry of about $10^6$ cations and producing a current of about $1\,\mathrm{pA}$ and a hyperpolarization of about $1\,\mathrm{mV}$ ([7.6.18](/7.6.18#sec-18.6.2)). The response reaches its peak in $0.1$–$0.3\,\mathrm{s}$ and lasts about $1\,\mathrm{s}$; the response of cones is much faster but their sensitivity is 30–300 times lower, still sufficient to work in daylight.

Termination of the cascade is equally fast and reliable: rhodopsin kinase (GRK1) phosphorylates $\mathrm{R}^*$ at several sites and **arrestin** binds to it; the GTPase activity of transducin is accelerated by RGS9; and **guanylyl cyclase** (GC) resynthesizes cGMP.

The peak response $R$ to a flash first rises linearly with flash intensity $I$, then is gradually compressed, and finally saturates (all CNG channels closed). Over about two orders of magnitude in the middle, the response is approximately proportional to $\ln I$, which is the **Weber–Fechner law** at the receptor level (Chapter 39). This light response–intensity curve is often described by the Naka–Rushton function:

$$
\frac{R}{R_{\max}} = \frac{I^n}{I^n + \sigma^n}, \tag{41.6}
$$
where $\sigma$ is the intensity giving half-saturation of the response and $n \approx 1$; for rods, the exponential saturation form $R/R_{\max} = 1 - \mathrm{e}^{-kI}$ fits better (Baylor et al., 1984).

**Negative feedback** by $\ce{Ca^2+}$ extends the dynamic range. By the cascade alone, a rod gives graded responses over only about two orders of magnitude of light intensity. $\ce{Ca^2+}$ enters the outer segment through CNG channels and is extruded by the $\ce{Na+}/\ce{Ca^2+}$–$\ce{K+}$ exchanger; when light closes the channels, entry stops while extrusion continues, and intracellular $\ce{Ca^2+}$ falls from several hundred nM in the dark to a few tens of nM. The fall of $\ce{Ca^2+}$ counteracts the action of light by three routes:

- guanylate cyclase-activating protein (GCAP) relieves its inhibition of GC at low $\ce{Ca^2+}$, accelerating cGMP synthesis (the most important);
- recoverin relieves its inhibition of GRK1 at low $\ce{Ca^2+}$, accelerating inactivation of $\mathrm{R}^*$;
- the inhibition of the CNG channel by $\ce{Ca^2+}$–**calmodulin** is relieved, making the channel more sensitive to cGMP.

This is a system coupling nonlinear amplification with negative feedback: amplification ensures sensitivity to dim light, whereas feedback makes the gain fall automatically as the signal grows, so the response does not easily saturate. A minimal model containing only cGMP and $\ce{Ca^2+}$ illustrates this. Taking dark values as 1,

$$
\frac{\mathrm{d}G}{\mathrm{d}t} = \alpha(c) - \beta_{\mathrm{d}}\Bigl(1 + \frac{I}{I_0}\Bigr)G, \qquad \frac{\mathrm{d}c}{\mathrm{d}t} = \frac{G^3 - c}{\tau_{\mathrm{c}}}, \qquad \alpha(c) = \frac{\alpha_{\max}}{1 + (c/K)^m}, \tag{41.7}
$$
where $G$ is the cGMP concentration, $G^3$ is the dark current, and $c$ is the $\ce{Ca^2+}$ concentration; $\beta_{\mathrm{d}}(1 + I/I_0)$ is the activity of PDE6 ($\beta_{\mathrm{d}}$ is the basal activity in the dark, increased in proportion by the light intensity $I$), $\alpha(c)$ is the GC activity inhibited by $\ce{Ca^2+}$ ($K$ and $m$ describe the $\ce{Ca^2+}$ dependence of GCAP), and $\tau_{\mathrm{c}}$ is the turnover time of $\ce{Ca^2+}$. Without feedback ($\alpha$ constant), the steady-state response rises from 10 % to 90 % over about 1.5 orders of magnitude; with feedback, the range extends to about 2.5 orders of magnitude, and the response to a light step first reaches a peak and then relaxes (figure below). More importantly, the sensitivity to incremental stimuli on a background falls approximately as $1/I$, that is, **Weber's law**: the brighter the background, the less "sensitive" the rod, so that it can report contrast over a wider range. In real photoreceptors, this mechanism is superimposed on pigment bleaching and gain control in retinal circuits, so that the visual system can work over light intensities spanning more than $10^{10}$-fold.

The same design recurs in other senses: in olfactory receptor neurons $\ce{Ca^2+}$–calmodulin lowers the sensitivity of the CNG channel to cAMP ([7.14.43](/7.14.43)), in **hair cells** $\ce{Ca^2+}$ and myosin motors shift the operating point of the transduction channel ([7.14.42](/7.14.42)), and in bacterial chemotaxis there is feedback by methylation ([7.6.35](/7.6.35)). These are all molecular implementations of sensory **adaptation**, analyzed at the systems level in [7.9.16](/7.9.16).

![Ca²⁺ negative feedback extends the working range of the rod (minimal model of Eq. (41.7); β_d = 1 s⁻¹, τ_c = 0.05 s, K = 0.12, m = 2, α_max such that α = β_d in the dark; light intensity in units of I₀, response R = 1 − G³ is the fraction of the dark current suppressed). A: steady-state response as a function of background intensity; without feedback (blue) it rises from 10 % to 90 % over about 1.5 orders of magnitude, with feedback (orange) over about 2.5 orders, saturating only at high intensity. B: responses to a 3 s light step (shading), three intensities; with feedback the response first reaches a peak and then falls to a lower plateau, and recovers quickly after the light is removed; without feedback (dashed) the response rises monotonically and recovers slowly. C: incremental sensitivity dR/dI on a background (relative to the dark, logarithmic axes); with feedback it is close to a slope of −1 over a range (dotted line, Weber's law), and without feedback it falls much faster](./plots/photoresponse.py)

### 41.2.5. Light Adaptation and Dark Adaptation

**Definition 41.2.3 (Dark Adaptation and Light Adaptation)** When going from light to dark, the sensitivity of the eye to light gradually increases over tens of minutes, called **dark adaptation**; when going from dark to light, one is at first dazzled and cannot see clearly, and then recovers within seconds to minutes as the sensitivity of the eye falls to suit the high light intensity, called **light adaptation**.

Light adaptation is fast and relies mainly on the negative feedback by $\ce{Ca^2+}$ within photoreceptors (Section 41.2.4), bleaching of visual pigment, and gain control in retinal circuits. Dark adaptation is slow, lowering the absolute threshold by about $10^4$–$10^6$-fold within 30–40 min, and its time course (the curve of threshold against time) has two phases:

- In the first 5–10 min the threshold falls quickly and then reaches a plateau: this is the adaptation of cones, whose pigment regenerates quickly but whose absolute threshold is higher;
- Afterward comes a break (the rod–cone break), and the threshold falls again until 30–40 min: this is the adaptation of rods, whose rhodopsin regenerates slowly but whose absolute threshold is much lower.

People with only rods (rod monochromats, that is, congenital achromatopsia) lack the first phase, and people without rod function (some forms of congenital stationary night blindness) lack the second, which proves that the two phases belong to the two systems. What determines the speed of adaptation is regeneration of the visual pigment. Dowling and Rushton found that the logarithm of the threshold after bleaching is proportional to the fraction $B$ of visual pigment still in the bleached state:

$$
\log_{10}\frac{T}{T_{\mathrm{abs}}} = kB, \tag{41.8}
$$
with $k$ about 20 for rods: even if only 1 % of rhodopsin has not regenerated, the threshold is about 0.2 log unit higher. The reason is not that there is less pigment to absorb photons (a 1 % reduction hardly affects light absorption) but that bleached opsin and its product with all-*trans*-retinal can weakly activate transducin and reduce sensitivity like an "equivalent background light". Regeneration of visual pigment is limited by the rate of supply of 11-*cis*-retinal (Lamb and Pugh, 2004), so after heavy bleaching $B$ falls approximately linearly and the threshold curve shows a correspondingly approximately straight-line decline.

![Biphasic curve of dark adaptation (schematic model). Regeneration of visual pigment is limited by the supply of 11-cis-retinal: dB/dt = −vB/(K_m + B), K_m = 0.2, rods v = 0.09 min⁻¹, cones v = 0.5 min⁻¹; the threshold rises according to the Dowling–Rushton relation log₁₀(T/T_abs) = kB, rods k = 20, cones k = 3; the absolute threshold of cones is 2.5 log units higher than that of rods; the psychophysical threshold is taken as the lower of the two branches. A: threshold as a function of time in the dark after bleaching of 98 %, 60 %, and 20 % (dots are the rod–cone break; dotted lines are the extensions of the two branches for 98 % bleaching): the less the bleaching, the earlier the break. B: fraction of the two visual pigments still bleached after 98 % bleaching; the decline is approximately linear when B is much larger than K_m](./plots/dark-adaptation.py)

### 41.2.6. Color Vision

Humans have three kinds of cones, each containing one cone pigment, with absorption peaks at about $420\,\mathrm{nm}$ (S, short wavelength), $530\,\mathrm{nm}$ (M, medium wavelength), and $560\,\mathrm{nm}$ (L, long wavelength); their opsins differ and the chromophore is always 11-*cis*-retinal. Each kind of cone is itself "color-blind": by the **principle of univariance** ([7.6.18](/7.6.18#def-18.6.2)), the output of a photoreceptor depends only on the number of photons it absorbs and cannot distinguish a change of wavelength from a change of intensity. Color can come only from the ratios of the outputs of different cones: equal activation of the three kinds of cones produces the sensation of white, and activation of both L and M with little S produces yellow or orange. The spectra of the three cones and a figure of ratio coding are in [7.6.18](/7.6.18#sec-18.6.5).

**Definition 41.2.4 (Trichromacy)** Color vision in which color is determined by the relative activation of three kinds of photoreceptors of different spectral sensitivity, so that any color can be matched by a mixture of three primary lights in suitable proportions, is called **trichromacy**.

The trichromatic theory (Young 1802, Helmholtz) accounts for the receptor level; but the perception of color also has an "opponent" quality: there is no reddish green or yellowish blue, and after gazing at red for a long time one sees a green afterimage. Hering's opponent-process theory accounts for the level after the receptors: ganglion cells and neurons of the lateral geniculate nucleus compute differences of the cone signals, forming two opponent channels, red–green (L − M) and blue–yellow (S − (L + M)) (Section 41.3.5), and a luminance channel. The two theories describe two stages of processing and do not contradict each other.

Color vision deficiencies are mostly hereditary:

- The genes for the L and M opsins are arranged adjacent to each other on the X chromosome with about 96 % sequence similarity and are prone to **unequal crossing over**, producing deleted or hybrid genes. Red–green color vision deficiencies are therefore **X-linked**, occurring in about 5 %–8 % of men and less than 1 % of women: those lacking one kind of cone are called dichromats (protanopes, deuteranopes), and those whose cone pigment spectrum is shifted are called anomalous trichromats (color weakness, the most common).
- Blue color vision deficiency (the S opsin gene is on autosome 7) and total color blindness are both rare.

The Ishihara pseudoisochromatic plates exploit this: the numbers in the plates are composed only of colors that dichromats cannot distinguish, so people with normal vision and color-blind people see different numbers.

## 41.3. Neural Circuits of the Retina

### 41.3.1. Cell Types and Signal Transmission

The retina has five classes of neurons: photoreceptors, horizontal cells, bipolar cells, amacrine cells, and ganglion cells, plus a small number of interplexiform cells. The direct pathway of signals is vertical (photoreceptor → bipolar cell → ganglion cell), and horizontal cells in the outer plexiform layer and amacrine cells in the inner plexiform layer provide lateral connections; interplexiform cells send inhibitory signals backward from the inner plexiform layer to the outer plexiform layer.

Features of signal transmission in the retina:

- Photoreceptors and bipolar cells both use glutamate as transmitter, released continuously and in a graded manner at ribbon synapses; the transmitters of other cells are diverse (GABA, glycine, acetylcholine, dopamine, and so on);
- Only ganglion cells (and some amacrine cells) generate **action potentials**; the other cells transmit signals by graded **electrotonic potentials**. Distances within the retina are only tens to hundreds of micrometers, so graded potentials suffice, and graded signals can carry more information than action potentials; the optic nerve is several centimeters long and must use action potentials;
- Besides **chemical synapses**, the retina has many **electrical synapses** (between rods, between rods and cones, and between AII amacrine cells and ON cone bipolar cells).

### 41.3.2. ON and OFF Bipolar Cells

Photoreceptors release less glutamate in light, and the same signal is received with opposite signs by two classes of bipolar cells:

**Definition 41.3.1 (ON and OFF Bipolar Cells)** A bipolar cell that depolarizes when light illuminates the center of its receptive field is called an **ON bipolar cell**; one that hyperpolarizes in light and depolarizes when light dims is called an **OFF bipolar cell**.

The two differ in glutamate receptors. ON bipolar cells express the **metabotropic receptor** mGluR6, which closes the TRPM1 cation channel through a G protein: in the dark there is much glutamate, the channel is closed, and the cell is hyperpolarized; in light glutamate decreases, the channel opens, and the cell depolarizes (the synapse inverts the sign of the signal). OFF bipolar cells express ionotropic AMPA or kainate receptors, and the signal keeps its sign. The axon terminals of ON and OFF bipolar cells lie in the inner and outer layers of the inner plexiform layer, respectively, and form synapses with the corresponding ON and OFF ganglion cells. Thus, from the first synapse on, the retina separates "brighter" and "darker" into two parallel channels, each reporting by an increase of firing rate, which avoids using a single channel with a low baseline firing rate to report a decrease (firing rates cannot be negative).

### 41.3.3. Center–Surround Receptive Fields

Kuffler (1953), recording from cat ganglion cells, found that their **receptive fields** (Chapter 39) are concentric:

**Definition 41.3.2 (Center–Surround Receptive Field)** The receptive field of a retinal ganglion cell consists of a circular center region and an annular surround region, and the two regions respond oppositely to light: an ON-center cell increases firing when light illuminates the center and decreases firing when light illuminates the surround; an OFF-center cell is the reverse. This structure is called a **center–surround receptive field**.

When the whole receptive field is uniformly illuminated, the actions of center and surround cancel and the cell responds weakly; when a light–dark edge falls on the receptive field the response is strongest. Ganglion cells therefore report local contrast and not absolute luminance: a white sheet of paper differs by a factor of a hundred in luminance between indoor light and sunlight, yet we always see "white". The center comes from the direct pathway through bipolar cells; the surround comes mainly from horizontal cells: horizontal cells are connected by electrical synapses into a wide-ranging network, pool the activity of a large surrounding set of photoreceptors, and feed back onto the synaptic terminals of photoreceptors, subtracting from the center signal. This is **lateral inhibition** in the retina, and its result is contrast enhancement: bright and dark bands (Mach bands) appear visually on the two sides of a light–dark border.

The spatial structure of the receptive field is often described by the difference of two Gaussians (DoG model, Rodieck 1965):

$$
W(r) = \frac{A_{\mathrm{c}}}{2\pi\sigma_{\mathrm{c}}^2}\mathrm{e}^{-r^2/2\sigma_{\mathrm{c}}^2} - \frac{A_{\mathrm{s}}}{2\pi\sigma_{\mathrm{s}}^2}\mathrm{e}^{-r^2/2\sigma_{\mathrm{s}}^2}, \qquad \sigma_{\mathrm{s}} > \sigma_{\mathrm{c}}, \tag{41.9}
$$
and the response of the cell is approximately the convolution of $W$ with the light intensity distribution on the retina. When $A_{\mathrm{c}} \approx A_{\mathrm{s}}$ the cell hardly responds to uniform light; in spatial frequency, $W$ is a band-pass filter that suppresses the low-frequency components carrying most of the energy of natural images and reduces the redundancy between the signals of neighboring ganglion cells ("efficient coding"). Chapter 39 used the same model to discuss two-point discrimination in touch.

### 41.3.4. Rod Pathways and Cone Pathways

The cone pathway is direct: cone → cone bipolar cell (ON or OFF) → ganglion cell, with lateral modulation by horizontal and amacrine cells. Its neurons and fibers are thicker, and signal conduction is 2–5 times faster than in the rod pathway.

Rod signals "borrow" cone pathways, mainly by three routes:

1. The primary pathway (most sensitive): rod → rod bipolar cell (all ON) → AII amacrine cell → through electrical synapses to ON cone bipolar cells and through glycinergic synapses (sign-inverting) to OFF cone bipolar cells → ganglion cell;
2. Electrical synapses between rods and cones: the rod signal enters cones and leaves through the cone pathway (dominant at intermediate luminance);
3. A few OFF cone bipolar cells receive rod input directly.

Thus rod bipolar cells do not connect directly to ganglion cells but are relayed by AII amacrine cells; this roundabout pathway is specific to mammals and may be the result of the rod pathway being "grafted" onto the existing cone circuit in nocturnal mammalian ancestors.

Convergence makes sensitivity and acuity trade off against each other. The signals of about $9\times10^7$ rods and $4.5\times10^6$ cones are gathered into about $1.2$–$1.5\times10^6$ optic nerve fibers. On average about 60 rods or 2 cones correspond to one fiber, but the distribution is very uneven: in the fovea, one cone connects through one midget bipolar cell to one midget ganglion cell (in fact each cone has one ON and one OFF ganglion cell), ensuring the highest acuity; in the periphery, the signals of hundreds to thousands of rods converge on one ganglion cell, which is **convergence** ([7.14.6](/7.14.6)). Convergence makes weak light signals summate in space, raising sensitivity and signal-to-noise ratio, at the cost of spatial resolution: one ganglion cell can report only "there is light somewhere in the receptive field".

There are over 30 kinds of *amacrine cells*, most of them inhibitory, with diverse functions: relay of the rod pathway (AII), transient responses to the onset or end of light, gain control, and direction selectivity. Direction-selective ganglion cells in the rabbit retina respond strongly to motion in one direction and hardly at all to the opposite direction (Barlow and Levick, 1965); the mechanism is that each dendrite of a starburst amacrine cell responds more strongly to motion away from the soma and provides asymmetric inhibition to the ganglion cell. The retina thus accomplishes a good deal of feature extraction before the signal is sent to the brain.

### 41.3.5. Types of Ganglion Cells

The human retina has about 20 kinds of ganglion cells, each tiling the entire retina and reporting one aspect of the image in parallel. The two most numerous classes in primates are:

| Feature | P cells (midget cells) | M cells (parasol cells) |
|---|---|---|
| Proportion | About 70 %–80 % | About 10 % |
| Projection | Parvocellular layers of the lateral geniculate nucleus | Magnocellular layers of the lateral geniculate nucleus |
| Receptive field | Small | Large |
| Conduction velocity | Slower | Faster |
| Response | Sustained | Transient |
| Color | Yes (red–green opponent) | No |
| Fine detail | Sensitive | Insensitive |
| Motion and low contrast | Insensitive | Sensitive |

P and M are a primate classification, and in other animals ganglion cells are classified differently (for example, X, Y, and W cells of the cat). In addition, small bistratified cells (projecting to the koniocellular layers of the lateral geniculate nucleus) convey the blue–yellow (S versus L + M) opponent signal. Ganglion cells process color in three ways: activated in the same direction by all three kinds of cones (reporting luminance); activated in the same direction by two kinds of cones; activated by one kind of cone and inhibited by another (color opponency, ensuring color contrast).

*Intrinsically photosensitive retinal ganglion cells*, abbreviated ipRGCs, make up about 1 %–2 %; they express the opsin-family melanopsin and can respond to light even without rods and cones (Berson et al., 2002). Transduction by melanopsin follows the Gq–**phospholipase C**–TRP channel route, the same as in invertebrate photoreceptors (Section 41.6). ipRGCs respond slowly and in a sustained way, report the overall brightness of the environment, and project to the **suprachiasmatic nucleus** (photic entrainment of circadian rhythms, [7.14.46](/7.14.46)) and the pretectal nucleus (pupillary light reflex). Hence some blind people who have lost all rods and cones still have normal pupillary reflexes and circadian rhythms.

## 41.4. Central Visual Pathways

### 41.4.1. Optic Chiasm and Lateral Geniculate Nucleus

The optic nerves of the two eyes meet at the optic chiasm: fibers from the nasal half of each retina (seeing the temporal visual field) cross to the opposite side, and fibers from the temporal half (seeing the nasal visual field) do not cross. As a result, each optic tract contains all the information about the contralateral visual field: right visual field → left optic tract → left lateral geniculate nucleus → left visual cortex. About 53 % of human optic nerve fibers cross. This arrangement brings the signals from the same point of the visual field in the two eyes to the same side of the brain, a prerequisite of binocular vision. The site of a lesion can be judged from the pattern of visual field loss:

| Site of lesion | Visual field loss |
|---|---|
| One optic nerve | Total blindness of that eye |
| Middle of the optic chiasm (such as compression by a pituitary tumor) | Bitemporal hemianopia |
| One optic tract, lateral geniculate nucleus, or optic radiation | Contralateral homonymous hemianopia |
| One visual cortex | Contralateral homonymous hemianopia, often with macular sparing |

About 90 % of optic tract fibers terminate in the lateral geniculate nucleus of the thalamus, and the rest go to the superior colliculus (orienting and saccades), pretectal nucleus (pupillary reflex), suprachiasmatic nucleus (circadian rhythms), and others. The primate lateral geniculate nucleus has six layers: layers 1, 4, and 6 receive input from the contralateral eye and layers 2, 3, and 5 from the ipsilateral eye; layers 1–2 are the magnocellular layers (M pathway), layers 3–6 are the parvocellular layers (P pathway), and the koniocellular layers between them transmit the blue–yellow signal. Signals from corresponding positions of the two eyes project to vertically aligned neurons in adjacent layers, and this parallel transmission separated by eye and by pathway is maintained up to the visual cortex. The lateral geniculate nucleus is not merely a relay: only about 10 % of the synapses it receives come from the retina, and the rest come from cortical feedback and the brainstem and gate the transmission of visual signals (changing with attention and arousal state). The axons of the lateral geniculate nucleus form the optic radiation, which projects to the occipital lobe.

### 41.4.2. Primary Visual Cortex

The primary visual cortex (V1, striate cortex, Brodmann area 17) lies on the two banks of the calcarine sulcus in the occipital lobe. It preserves the topographic arrangement of the retina (retinotopy), but the representation of the fovea is greatly magnified: the central $10^\circ$ of the visual field occupies about half of V1, corresponding to the high-density sampling of the fovea.

V1 has six layers, and input from the lateral geniculate nucleus terminates mainly in layer 4: the M pathway to sublayer 4Cα, the P pathway to sublayer 4Cβ, and the koniocellular pathway to layers 2/3. In layers 2/3, cytochrome oxidase staining shows regularly arranged patches (blobs), whose neurons are sensitive to color and insensitive to orientation.

Hubel and Wiesel (1959, 1962; Nobel Prize 1981) found that the receptive fields of V1 neurons are no longer circular:

- Simple cells respond most strongly to a light bar or edge of a particular orientation and have receptive fields with adjacent ON and OFF regions, which can be understood as a combination of several center–surround receptive fields arranged in a row;
- Complex cells also have orientation selectivity but are insensitive to the exact position of the light bar in the receptive field, and many also have direction selectivity.

The functional structure of V1 is columnar. Neurons passing through the layers perpendicular to the cortical surface have the same optimal orientation and form orientation columns, with the optimal orientation changing gradually in adjacent columns; inputs from the two eyes are arranged in separate alternating stripes in layer 4, forming ocular dominance columns. About $1\,\mathrm{mm}^2$ of cortex contains a full set of orientation columns and a pair of ocular dominance columns, analyzing all orientations and inputs from both eyes for a small region of the visual field, and is called a hypercolumn. The formation of ocular dominance columns depends on early visual experience: if one eye is covered during the **critical period** of development, the columns of that eye shrink and those of the other eye expand, and the covered eye has permanently poor vision even if optically normal (amblyopia). This is a classic example of activity-dependent **synaptic plasticity**, and is the reason why strabismus and anisometropia in children must be corrected within the critical period.

### 41.4.3. Dorsal and Ventral Pathways

The output of V1 divides through V2 into two major cortical pathways (Ungerleider and Mishkin, 1982):

- The *dorsal stream*: V1 → V2 → middle temporal area (MT, also called V5) → posterior parietal cortex, with input mainly from the M pathway, analyzing motion, spatial position, and depth, and together with somatosensory areas providing spatial information for action (reaching, grasping, eye movements), often summarized as "where" or "how";
- The *ventral stream*: V1 → V2 → V4 → inferior temporal cortex, with input mainly from the P pathway, analyzing shape, color, and texture and recognizing objects and faces, summarized as "what".

Local lesions cause selective deficits: damage to MT makes one unable to see motion (akinetopsia), damage near V4 causes achromatopsia (cerebral color blindness), and damage to the fusiform face area causes prosopagnosia. There are many interconnections between the two pathways, and this distinction is a useful approximation, not two independent systems.

### 41.4.4. The Four-Level Framework of Vision

Chapter 39 analyzed mechanosensation with four levels: "external stimulus, mechanical computation, cellular coding, and central processing" ([7.14.39](/7.14.39#sec-39.5.1)). Vision fits into the same framework, except that level 2 is optical rather than mechanical:

| Level | In vision |
|---|---|
| 1. External stimulus | Photon flux: intensity, wavelength, direction, temporal variation |
| 2. Physical preprocessing | Imaging by the cornea and lens (converting direction into position on the retina); accommodation and pupil control of focus, depth of field, and incident light; pigment epithelium absorbs stray light and macular pigment filters short wavelengths |
| 3. Cellular coding | Photochemistry of visual pigments and the G protein cascade (amplification, gain control by $\ce{Ca^2+}$ feedback), graded **receptor potentials**; retinal circuits accomplish ON/OFF separation, center–surround contrast, color opponency, and direction selectivity; ganglion cells convert to action potentials |
| 4. Central processing | Gating by the lateral geniculate nucleus, orientation and ocular dominance columns of V1, analysis and recognition by dorsal and ventral pathways |

Compared with touch, vision differs in that level 3 is especially thick: the retina itself is part of the central nervous system, and about 20 kinds of ganglion cells decompose the image into 20 parallel "feature maps" before sending them to the brain. Level 2 is equally crucial: the optical quality of the eye (diffraction, aberration, focus) sets the upper limit of resolution that all later levels can reach, and the density of photoreceptors matches it exactly (Section 41.1.7).

## 41.5. Eye Movements

### 41.5.1. The Extraocular Muscles and Their Innervation

Each eye is rotated by six extraocular muscles, forming three pairs:

| Muscle | Main action | Innervation |
|---|---|---|
| Medial rectus / lateral rectus | Adduction / abduction (horizontal movement) | Oculomotor nerve (III) / abducens nerve (VI) |
| Superior rectus / inferior rectus | Elevation / depression (with rotation) | Oculomotor nerve |
| Superior oblique / inferior oblique | Mainly rotation (intorsion / extorsion), and depression / elevation | Trochlear nerve (IV) / oculomotor nerve |

The movements of the two eyes must be precisely coordinated; otherwise the images of the same object fall on noncorresponding points of the two retinas and cause diplopia.

### 41.5.2. Types of Eye Movements

- Fixation: keeping the image on the fovea. During fixation the eye still shows small drifts, tremor, and microsaccades; if the image on the retina is made completely stationary by optical means, the image disappears within a few seconds. This is a manifestation of **adaptation** of receptors and retinal circuits: the visual system reports change, and small eye movements continually refresh the image.
- *Saccade*: a rapid jump of gaze from one point to another, lasting $20$–$80\,\mathrm{ms}$, with peak angular velocity over $500^\circ\,\mathrm{s^{-1}}$, made about 3 times per second. Visual sensitivity is reduced during saccades (saccadic suppression), so we do not see a blurred sweep of the world. Saccades are initiated by the superior colliculus and the frontal eye field, and the brainstem gaze centers (for horizontal movements the paramedian pontine reticular formation, for vertical movements the midbrain) generate the motor commands causing burst contraction of the extraocular muscles.
- *Smooth pursuit*: making gaze follow a moving object smoothly, with a maximum speed of about $30$–$100^\circ\,\mathrm{s^{-1}}$; it requires a moving target, cannot be generated voluntarily against a stationary background, and depends on motion signals from dorsal stream areas such as MT.
- Vergence: rotation of the two eyes in opposite directions to fixate objects at different distances, accompanied by accommodation and pupillary constriction.
- **Vestibulo-ocular reflex**: when the head turns, the eyes rotate at the same speed in the opposite direction, keeping the image on the retina stable; the latency is only about $10\,\mathrm{ms}$, faster than any visual feedback. Its mechanism and adaptation are discussed in the next chapter ([7.14.42](/7.14.42)) and in the cerebellum ([7.14.45](/7.14.45)).
- Optokinetic reflex: when the whole visual field moves continuously (as when looking out of the window of a moving train), the eyes follow the field and then jump back quickly, forming optokinetic **nystagmus**.

## 41.6. Evolution and Comparison

### 41.6.1. Types and Evolution of Eyes

There are at least ten kinds of eyes in the animal kingdom with different optical principles: eyespots that sense only light intensity; cup eyes composed of a pigment cup that can resolve the direction of light; pinhole eyes that form images through a small aperture (*Nautilus*); camera eyes with a lens (vertebrates, cephalopods, some spiders and annelids); compound eyes made of many small eyes (arthropods); and reflecting eyes that form images with a concave mirror (scallops). For the time needed to evolve a camera eye from a patch of photoreceptors, Nilsson and Pelger (1994) made a conservative estimate: with an improvement of only 1 % at each step, it can be accomplished in fewer than half a million generations ([7.10.32](/7.10.32#sec-32.3.2)), so it is not surprising that eyes evolved independently many times in different animal phyla.

At the molecular level, however, the development of eyes has a deep common origin: the transcription factor Pax6 is a key regulator in eye development in *Drosophila*, mouse, and human, and ectopic expression of mouse *Pax6* on the leg or antenna of *Drosophila* can induce compound eyes of *Drosophila* (Halder, Callaerts, and Gehring, 1995). This is a classic example of **deep homology** ([7.5.22](/7.5.22#sec-22.2.5)): different eyes are each built from one ancient shared toolkit.

### 41.6.2. Two Classes of Photoreceptors

Animal photoreceptors fall into two large classes:

| | Ciliary | Rhabdomeric (microvillar) |
|---|---|---|
| Photosensitive membrane | Derived from the cilium (membrane disks or folds) | Rhabdom composed of microvilli |
| Opsin | c-opsin | r-opsin |
| Transduction | Transducin → PDE → cGMP falls, CNG channels close | Gq → phospholipase C → TRP channels open |
| Response | Hyperpolarization | Depolarization |
| After bleaching of pigment | Chromophore leaves, regeneration by visual cycle needed | Absorption of a second photon restores it (bistable) |
| Representative | Rods and cones of vertebrates | Photoreceptors of insects and cephalopods |

The two classes of cells may already have coexisted in early bilaterian animals: the larva of the annelid *Platynereis* has both rhabdomeric eyes and ciliary photoreceptors in the brain, the latter homologous to the rods and cones of vertebrates (Arendt et al., 2004). Vertebrates also retain a rhabdomeric pathway, the intrinsically photosensitive ganglion cells of the previous section, whose melanopsin belongs to the r-opsin class.

### 41.6.3. Cephalopod Camera Eyes and Eyes of Aquatic Animals

The camera eyes of octopus and squid are strikingly similar in shape to the vertebrate eye and are a classic case of **convergent evolution**: the two independently evolved a cornea, iris, spherical lens, and retina. The details are entirely different, however: the cephalopod retina is upright, with the photoreceptors facing the light and the nerve fibers leaving from behind the retina, so there is no blind spot; the photoreceptors are rhabdomeric; and accommodation is achieved by moving the lens forward and backward rather than changing its shape.

In water the cornea loses its refractive power (Section 41.1.2), and all refraction must be done by the lens. The lenses of fish and cephalopods are spherical, with refractive index falling gradually from the center (about $1.52$) to the surface (about $1.38$); this gradient both provides strong refractive power and eliminates the spherical aberration that would otherwise be severe in a spherical lens; the focal length is about 2.5 times the lens radius (Matthiessen's ratio). Accommodation in teleosts is also by moving the lens. Amphibious animals must solve the problem of two media: diving cormorants and diving ducks use powerful iris muscles to squeeze and deform the lens, obtaining tens of diopters of accommodation; in the "four-eyed fish" (*Anableps*) the pupil is divided into upper and lower halves, the upper half seeing in air through the flatter part of the lens and the lower half seeing in water through the more curved part.

### 41.6.4. Compound Eyes

The compound eyes of insects and crustaceans consist of hundreds to tens of thousands of ommatidia (about 800 in *Drosophila*, up to $30\,000$ in dragonflies), each with its own corneal lens and crystalline cone, beneath which is the rhabdom of a small group of photoreceptors. Compound eyes are of two kinds: in apposition eyes each ommatidium is surrounded by pigment and receives light only from its own direction, suiting day-active insects; in superposition eyes the light of many ommatidia is focused onto the same rhabdom, giving much higher sensitivity, as in nocturnal moths and many crustaceans. The spatial resolution of compound eyes is limited by diffraction: the smaller the ommatidia, the denser the sampling, but the greater the diffraction blur of each ommatidium, and the optimal ommatidial diameter grows with the square root of the eye radius; to reach the resolution of the human eye, the radius of a compound eye would need to be tens of meters ([7.6.18](/7.6.18#sec-18.6.6)). The strengths of compound eyes are a wide field of view, compact structure, and high temporal resolution: fast-flying flies can resolve flicker above $200\,\mathrm{Hz}$, whereas humans resolve about $60\,\mathrm{Hz}$.

### 41.6.5. Opsin Diversity and the Evolution of Color Vision

The ancestors of vertebrates had four classes of cone opsins (SWS1 sensitive to ultraviolet or violet, SWS2 to blue, RH2 to green, LWS to red) as well as the rod opsin RH1, and were tetrachromats. Different lineages have added to or lost from this:

- Birds retained four cones, and many species can see ultraviolet light; colored oil droplets containing carotenoids in the inner segments of cones act like filters, making the spectral sensitivity curve of each cone narrower with less overlap and improving color discrimination.
- The ancestors of mammals went through a long period of nocturnal life (the "nocturnal bottleneck"), lost SWS2 and RH2, and most mammals have only the S and L cones and are dichromats; at the same time, rods form the great majority. Many marine mammals (cetaceans, pinnipeds) have further lost SWS1 and have only one kind of cone.
- In Old World primates (including humans), about 30–40 million years ago, the LWS gene on the X chromosome underwent **gene duplication** and the two copies diverged into L and M, regaining trichromacy, perhaps advantageous for finding ripe fruit and young leaves against a background of green foliage. New World monkeys have only one LWS locus on the X chromosome but several alleles, so heterozygous females are trichromats and males are all dichromats; howler monkeys independently underwent gene duplication. The human red–green color blindness discussed above is the instability left behind by this young gene duplication.
- Mantis shrimps have more than 12 types of photoreceptors and can also sense circularly polarized light; but their ability to discriminate close wavelengths is rather poor, and they seem to recognize colors directly from the activation pattern of receptors rather than by comparing the outputs of a few kinds of receptors as we do ([7.6.18](/7.6.18#sec-18.6.5)).
- Deep-sea fish live in an environment with only faint blue light and bioluminescence, and some species have up to several tens of copies of rod opsin genes (Musilova et al., 2019); freshwater fish and some amphibians use 3-dehydroretinal (vitamin A₂) as chromophore, forming porphyropsins whose absorption peak is shifted to longer wavelengths to suit the reddish light in fresh water, and some migratory fish switch between the two chromophores when moving between seawater and fresh water.

### 41.6.6. The Tapetum and Polarization Vision

Many nocturnal mammals (cats, dogs, cattle), crocodilians, and deep-sea fish have a reflective layer, the tapetum lucidum, behind the retina, which reflects light that passed through the photoreceptors without being absorbed back so that it has a second chance of being absorbed; this is why the eyes of nocturnal animals shine when lit. It increases sensitivity at the cost of slight blurring of the image by scattering of the reflected light, another trade-off between sensitivity and acuity.

The microvilli of rhabdomeric photoreceptors are neatly arranged, and the visual pigment molecules are aligned along the long axis of the microvilli, so that the photoreceptor absorbs light of different **polarization** directions differently, and many insects and cephalopods can sense polarized light. A small patch of ommatidia at the dorsal rim of the compound eye in honeybees and desert ants is dedicated to detecting the polarization pattern of the sky, so that the direction of the sun can still be determined when the sun is hidden, as a sky compass for navigation (von Frisch). The membrane disks of vertebrate photoreceptors are perpendicular to the direction of light propagation, and the orientation of the pigment within the disk plane is random, so humans basically have no polarization vision.

## Summary

| Topic | Key points |
|---|---|
| Refraction (Definition 41.1.1) | $P = 1/f$; the eye is about $60\,\mathrm{D}$, cornea about 2/3 (fixed), lens about 1/3 (adjustable); the nodal point of the reduced eye is $17\,\mathrm{mm}$ from the retina, $1'$ is about $5\,\mu\mathrm{m}$ |
| Accommodation (Definition 41.1.2) | Ciliary muscle contracts → zonules slacken → lens becomes more convex; parasympathetic innervation; amplitude of accommodation in children about $14\,\mathrm{D}$; near triad |
| Presbyopia (Definition 41.1.3, Remark 41.1.1) | Amplitude of accommodation falls with age, about $18.5 - 0.3\times\text{age}$ (D); not hyperopia; convex lenses for near vision |
| Refractive errors | Myopia (long axis, concave lens), hyperopia (short axis, convex lens), astigmatism (cylindrical lens); $1\,\mathrm{mm}$ of axial length about $3\,\mathrm{D}$ |
| Pupil and intraocular pressure | $1.5$–$8\,\mathrm{mm}$, light about 30-fold; blur angle $\approx D\,\Delta P$; four levels of neurons in the light reflex; intraocular pressure about $15\,\mathrm{mmHg}$ ($2\,\mathrm{kPa}$), glaucoma |
| Visual acuity and stereopsis | About $1'$, limited jointly by diffraction and cone sampling; disparity $\delta \approx I\,\Delta d/d^2$, depth resolution worsens with $d^2$ |
| Retina (Definition 41.2.1) | Inverted structure, pigment epithelium; fovea about $1.5\,\mathrm{mm}$, its central foveola of about $0.3\,\mathrm{mm}$ cones only |
| Rods and cones | About $9\times10^7$ and $4.5\times10^6$; division of labor between scotopic and photopic vision |
| Phototransduction (Definition 41.2.2) | Dark current; $\mathrm{R}^*$ → transducin → PDE6 → cGMP falls → CNG closes → hyperpolarization → less glutamate; single photon about $1\,\mathrm{mV}$ |
| Dynamic range | Eq. (41.6); $\ce{Ca^2+}$ negative feedback (GCAP, recoverin, CNG) extends the range and produces Weber's law (Eq. (41.7)) |
| Dark adaptation (Definition 41.2.3) | Cone phase and rod phase, rod–cone break; Dowling–Rushton relation Eq. (41.8); visual cycle and vitamin A |
| Color vision (Definition 41.2.4) | Three cones S/M/L; principle of univariance; trichromatic and opponent stages; X-linked red–green color vision deficiency |
| Retinal circuits (Definitions 41.3.1, 41.3.2) | ON (mGluR6–TRPM1) and OFF (AMPA/KA); center–surround, DoG model Eq. (41.9); rods borrow the cone pathway through AII; convergence; direction selectivity |
| Ganglion cells | P (small receptive field, color, detail), M (large receptive field, motion), small bistratified (blue–yellow), ipRGC (melanopsin, pupil and rhythms) |
| Central pathways | Nasal fibers cross; six layers of LGN (1, 4, 6 contralateral; 1–2 magnocellular); orientation columns, ocular dominance columns, and blobs of V1, critical period; dorsal and ventral streams |
| Eye movements | Six extraocular muscles (III, IV, VI); fixation, saccade, smooth pursuit, vergence, vestibulo-ocular reflex, optokinetic reflex |
| Evolution | Eyes evolved independently many times, Pax6 deep homology; ciliary and rhabdomeric photoreceptors; cephalopods have no blind spot; spherical gradient-index lenses of aquatic animals; diffraction limit of compound eyes; loss and regain of opsins (birds tetrachromats, mammals dichromats, Old World primates trichromats); tapetum; polarization vision |

## Questions

1. A 50-year-old person who originally had normal vision (emmetropia) has an amplitude of accommodation of $2\,\mathrm{D}$. Where is his near point? How many diopters of reading glasses does he need to read at $40\,\mathrm{cm}$? With these glasses on, over what range of distances can he see clearly?

   **Answer** The far point of an emmetropic eye is at infinity; by Eq. (41.3), the near point is $1/2\,\mathrm{D} = 50\,\mathrm{cm}$. Reading at $40\,\mathrm{cm}$ needs $2.5\,\mathrm{D}$, so at least $+0.5\,\mathrm{D}$ is required; so as not to use up all the accommodation (long reading would tire), about $+1.0$ to $+1.5\,\mathrm{D}$ is usually prescribed. Taking $+1.5\,\mathrm{D}$ as an example (neglecting the distance from lens to eye): without accommodation, eye plus lens has $1.5\,\mathrm{D}$ of excess and the far point is $1/1.5 \approx 67\,\mathrm{cm}$; at maximal accommodation the total excess is $3.5\,\mathrm{D}$ and the near point is $1/3.5 \approx 29\,\mathrm{cm}$. With the glasses he sees clearly over $29$–$67\,\mathrm{cm}$, and for distance he must take the glasses off or use bifocal lenses.

2. Why do we say that rods "release transmitter continuously" in the dark and the light signal is a decrease of transmitter release? What requirement does this design place on bipolar cells?

   **Answer** In the dark the cGMP concentration is high, CNG channels are open, and the dark current keeps the rod depolarized at about $-40\,\mathrm{mV}$; voltage-gated $\ce{Ca^2+}$ channels at the synaptic terminal are open and the ribbon synapse releases glutamate continuously; light lowers cGMP, closes the channels, hyperpolarizes the membrane, and decreases glutamate release. Thus graded changes of light intensity are converted into graded changes of transmitter release rate, and in the dark the rod sits at the operating point most sensitive to small voltage changes (the steep part of the activation curve of $\ce{Ca^2+}$ channels), so that the change of about $1\,\mathrm{mV}$ caused by a single photon can change release. To read out "brighter" and "darker" from "less transmitter", the downstream circuit must have two classes of bipolar cells: ON cells use mGluR6–TRPM1 to turn a decrease of glutamate into depolarization, and OFF cells use ionotropic receptors to keep the sign, so that an increase of firing in two parallel channels reports brighter and darker, respectively.

3. By the Dowling–Rushton relation, Eq. (41.8) (rods, $k = 20$), after a strong bleach, if 5 % of rhodopsin has still not regenerated, by how much is the rod threshold above the absolute threshold? Can this be explained by "less pigment to absorb photons"?

   **Answer** For $B = 0.05$, $\log_{10}(T/T_{\mathrm{abs}}) = 20\times0.05 = 1$, that is, the threshold is 10 times higher. But then the ability of the rod to absorb photons is only 5 % lower than with full regeneration; if the threshold depended only on absorption, it should rise only by about $1/0.95 \approx 1.05$-fold. So the rise of threshold is not caused by reduced absorption, but because the bleaching products (free opsin and its complex with all-*trans*-retinal) weakly and continuously activate transducin, lowering rod sensitivity through the gain control of Section 41.2.4 like an "equivalent background light". This also explains why the last stage of dark adaptation is so slow: the regeneration of the last few percent of visual pigment determines the last more than one order of magnitude of sensitivity.

4. Why does compression of the middle of the optic chiasm by a pituitary tumor cause bitemporal hemianopia rather than binasal hemianopia?

   **Answer** What crosses in the middle of the optic chiasm are the fibers from the nasal half of the retina of each eye. Because the optics of the eye form an inverted image, the nasal half of the retina receives light from the temporal visual field. When these fibers are compressed and interrupted, both eyes cannot see their temporal visual fields, which is bitemporal hemianopia; the fibers from the temporal half of the retina, which do not cross, run lateral to the chiasm and are unaffected, so the nasal visual fields are preserved.

5. (Open question) The octopus retina has no blind spot, with the photoreceptors facing the light, apparently more sensible than the "inverted" human retina. Why have vertebrates not "corrected" this design? Does the inverted retina have advantages?

   **Answer** Key points: (1) Evolution modifies existing structures. The vertebrate retina forms from the invagination of the optic vesicle of the neural tube, and the orientation of photoreceptors is decided in development; changing it to upright would require reorganizing the whole developmental program, and intermediate states would have no function, so it cannot be reached step by step; this contrasts with the cephalopod eye, formed by invagination of the epidermis with photoreceptors naturally facing outward. (2) The inverted structure has compensations and benefits: the outer segments of photoreceptors lie against the pigment epithelium, and both the vertebrate visual cycle (isomerization of retinal in the pigment epithelium) and the daily renewal of outer segments depend on this contact, while the highly metabolic photoreceptors are also directly adjacent to the rich blood supply of the choroid; Müller cells reduce scattering like optical fibers, the fovea pushes the inner layers aside so that the most critical region is unobstructed, and the blind spots of the two eyes lie at different positions in the visual field and compensate for each other. (3) The visual pigment of cephalopod rhabdomeric photoreceptors is bistable and needs no visual cycle in a pigment epithelium, so the upright structure costs them nothing. The two designs are each matched to their phototransduction mechanism, and one cannot simply say which is more "sensible".
