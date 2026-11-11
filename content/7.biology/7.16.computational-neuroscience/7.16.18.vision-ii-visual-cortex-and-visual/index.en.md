---
title: "Vision II: Visual Cortex and Visual Pathways"
description: "The retinotopic projection, LGN and cortical magnification; simple and complex cells as Gabor filters and energy models; orientation and ocular dominance columns, pinwheels and the ring model of orientation tuning; laminar circuits; dorsal and ventral pathways, MT and motion integration; face patches and the axis model; attention as gain modulation and normalization; MT activity and perceptual decisions."
---

The retina reports local contrast, color and motion through parallel channels ([7.16.17](/7.16.17)). From the lateral geniculate nucleus (LGN) onward, the primate brain devotes about a third of its cortex to vision, organized as a hierarchy of more than thirty areas in which neurons respond to progressively more complex and more invariant features: oriented edges in V1, global motion in MT, curved contours in V4, objects and faces in inferotemporal (IT) cortex. The anatomy of the central pathways (chiasm, LGN layers, V1 and its columns, the two cortical streams) is summarized in animal physiology ([7.14.41](/7.14.41#sec-41.4)). This chapter treats the computations: the receptive field models of V1 neurons built with the tools of [7.16.16](/7.16.16), the recurrent network that sharpens orientation tuning (an application of the rate models of [7.16.15](/7.16.15)), the functional maps whose development is modeled in [7.16.21](/7.16.21) and [7.16.22](/7.16.22), the representation of faces, and the experiments that link the activity of single neurons to perception and decision. Deep networks as models of the whole hierarchy are the subject of the next chapter, [7.16.19](/7.16.19).

## 18.1. From Retina to Cortex

### 18.1.1. The Lateral Geniculate Nucleus

The axons of retinal ganglion cells form a retinotopic projection: neighboring ganglion cells project to neighboring positions in the LGN and the superior colliculus, so that each structure contains a map of the contralateral visual field. Receptive fields of LGN relay neurons are center–surround, much like those of their retinal inputs, and the primate LGN keeps the channels segregated in layers (magnocellular, parvocellular, koniocellular) and the two eyes in alternating layers.

The LGN is nevertheless not a passive relay. Only about $5$–$10\,\%$ of the synapses onto a relay neuron come from the retina; the majority come from layer 6 of the visual cortex, from the thalamic reticular nucleus (inhibitory) and from brainstem modulatory systems. These inputs set the mode of transmission: depolarized relay cells fire tonically and transmit the retinal signal nearly linearly, whereas hyperpolarized cells de-inactivate T-type $\ce{Ca^2+}$ channels and fire in bursts, a mode that prevails in drowsiness and sleep ([7.16.35](/7.16.35)).

### 18.1.2. Cortical Magnification

V1 maps the visual field onto the cortical sheet nonuniformly. The **cortical magnification factor** $M(E)$, the cortical distance in millimeters corresponding to one degree of visual angle at eccentricity $E$, falls steeply away from the fovea.

**Formula 18.1.1 (Cortical Magnification)** In human V1, the linear magnification factor is approximately

$$
M(E) = \frac{M_0}{1 + E/E_2}, \qquad M_0 \approx 23\,\mathrm{mm\,deg^{-1}}, \quad E_2 \approx 0.75^\circ \tag{18.1}
$$
(Horton and Hoyt 1991, $M = 17.3/(E + 0.75)\,\mathrm{mm\,deg^{-1}}$). Integrating, the cortical distance from the foveal representation is $\int_0^E M\,\mathrm{d}E' = M_0E_2\ln(1 + E/E_2)$: for $E \gg E_2$ the map is logarithmic in eccentricity, and in two dimensions it is approximately the complex logarithm $w = \ln(z + a)$ of the position $z$ in the visual field (Schwartz 1977).

The central $10^\circ$ of the visual field, about $3\,\%$ of its area, occupies about half of V1. Magnification follows the density of ganglion cells: each ganglion cell is represented by a roughly constant area of cortex, so that the magnification of the fovea is inherited from the sampling density of the retina rather than added by the cortex. A useful consequence of the logarithmic map is that scaling an image about the fixation point becomes a translation on the cortex.

## 18.2. Simple and Complex Cells

### 18.2.1. Hubel and Wiesel's Classification

Hubel and Wiesel, recording from cat and monkey V1 from 1959 onward, found that cortical neurons respond poorly to spots of light and vigorously to bars or edges of a particular orientation. They classified them by the structure of their receptive fields.

**Definition 18.2.1 (Simple Cell and Complex Cell)** A V1 neuron is a **simple cell** if its receptive field consists of elongated, adjacent ON and OFF subregions, so that its response to a stimulus can be predicted from the map of these subregions by approximately linear summation. A neuron is a **complex cell** if it is selective for orientation (and often spatial frequency and direction) but responds to an optimally oriented bar or edge anywhere within its receptive field, with no separate ON and OFF subregions.

A standard quantitative criterion uses a drifting grating at the preferred orientation: the response of a simple cell is modulated at the temporal frequency of the grating, because the bars alternately cover its ON and OFF subregions, whereas a complex cell responds with an elevated, nearly constant rate. The ratio of the first harmonic to the mean response, $F_1/F_0$, is bimodally distributed across V1, with simple cells above $1$ and complex cells below (Skottun et al. 1991). Simple cells are concentrated in layer 4, the input layer, and complex cells in the layers above and below it.

### 18.2.2. Gabor Receptive Fields

Mapped by reverse correlation with random stimuli ([7.16.16](/7.16.16#sec-16.5)), the spatial receptive field of a simple cell is well fitted by a sinusoid under a Gaussian envelope.

**Definition 18.2.2 (Gabor Filter)** A **Gabor filter** with preferred spatial frequency $k$, phase $\varphi$ and envelope widths $\sigma_x$, $\sigma_y$ is

$$
D_{\mathrm{s}}(x, y) = \frac{1}{2\pi\sigma_x\sigma_y}\exp\Bigl(-\frac{x^2}{2\sigma_x^2} - \frac{y^2}{2\sigma_y^2}\Bigr)\cos(kx - \varphi), \tag{18.2}
$$
in coordinates rotated so that $x$ is perpendicular to the preferred orientation. The phase $\varphi = 0$ gives an even-symmetric field (a central ON stripe flanked by OFF stripes) and $\varphi = \pi/2$ an odd-symmetric field (an edge detector).

The Gabor function is the function that minimizes the product of its spatial extent and its spread in spatial frequency (Gabor 1946, Daugman 1985): it localizes a signal as well as possible in both position and frequency, a compromise that suits a neuron reporting "what pattern, where". In time, the receptive fields of many simple cells are separable, $D(x, y, t) = D_{\mathrm{s}}(x, y)D_{\mathrm{t}}(t)$, and such cells are not direction selective; others have receptive fields whose subregions shift with time, tilted in the $x$–$t$ plane, and these respond selectively to motion perpendicular to their orientation. A space–time inseparable receptive field can be built as the sum of two separable ones in quadrature (spatial phase and temporal phase both shifted by $90^\circ$), the cortical counterpart of the retinal and insect mechanisms of **direction selectivity** ([7.16.17](/7.16.17#sec-17.6)).

### 18.2.3. The Energy Model of Complex Cells

Complex cells cannot be described by a single linear filter followed by rectification: their response is invariant to the spatial phase of a grating, and their **spike-triggered average** is nearly zero ([7.16.16](/7.16.16#sec-16.6)).

**Definition 18.2.3 (Energy Model)** In the **energy model** of a complex cell, the stimulus is filtered by two linear receptive fields with the same position, orientation and frequency but phases differing by $90^\circ$ (a quadrature pair), $L_1 = \int D_{\varphi}s$ and $L_2 = \int D_{\varphi - \pi/2}s$, and the response is the sum of their squares:

$$
r = g\,(L_1^2 + L_2^2). \tag{18.3}
$$

**Theorem 18.2.1 (Phase Invariance of the Energy Model)** For a grating $s(x, y) = c\cos(kx - \psi)$ at the preferred orientation and frequency, with receptive fields large compared with one period, $L_1 \propto c\cos(\psi - \varphi)$ and $L_2 \propto c\sin(\psi - \varphi)$, so the energy-model response $r \propto c^2$ is independent of the spatial phase $\psi$, while a simple cell $r = g[L_1]_+$ varies with $\psi$.

**Proof** The integral of the product of $\cos(kx - \psi)$ with $\mathrm{e}^{-x^2/2\sigma_x^2}\cos(kx - \varphi)$ over $x$ is, using $\cos\alpha\cos\beta = \frac12[\cos(\alpha - \beta) + \cos(\alpha + \beta)]$, the sum of a term $\frac12\cos(\psi - \varphi)\int\mathrm{e}^{-x^2/2\sigma_x^2}\mathrm{d}x$ and a term with $\cos(2kx - \psi - \varphi)$ whose integral is smaller by a factor $\mathrm{e}^{-2k^2\sigma_x^2}$, negligible when $k\sigma_x \gg 1$. The filter with phase $\varphi - \pi/2$ replaces $\cos(\psi - \varphi)$ by $\sin(\psi - \varphi)$. Hence $L_1^2 + L_2^2 \propto c^2[\cos^2 + \sin^2] = c^2$. $\square$

The energy model also describes direction-selective complex cells, when the two filters are space–time inseparable (Adelson and Bergen 1985, "motion energy"), and the response of binocular neurons to disparity (Ohzawa, DeAngelis and Freeman 1990). It is equivalent in its average response to the Reichardt correlation detector of the insect eye ([7.16.17](/7.16.17#sec-17.6.3)). Its structure, linear filtering followed by squaring and pooling, recurs in the convolutional networks of the next chapter, where it is called pooling.

![Simple and complex cells (Definitions 18.2.1–18.2.3; Gabor envelope 0.3° × 0.5°, preferred spatial frequency 1.2 cycles per degree). A: an even-symmetric and an odd-symmetric Gabor receptive field (red: ON, blue: OFF), a quadrature pair. B: responses to a grating drifting at 2 Hz. The simple cell, modeled as the rectified output of the even filter, fires only during half of each cycle ($F_1/F_0 > 1$); the complex cell, modeled as the sum of the squared outputs of the two filters, fires at a constant rate ($F_1/F_0 \approx 0$). C: responses to a stationary grating as a function of its spatial phase; the energy model is phase invariant (Theorem 18.2.1)](./plots/gabor-energy.py)

### 18.2.4. How Are Orientation-Selective Receptive Fields Built?

Hubel and Wiesel proposed in 1962 a feedforward wiring diagram: a simple cell receives input from LGN neurons whose center–surround receptive fields lie in a row along the preferred orientation, and a complex cell pools simple cells of the same orientation but different positions. Several experiments support the first step. Simultaneous recordings from LGN neurons and simple cells in the cat showed that monosynaptically connected pairs have overlapping receptive fields of the same sign (ON center under ON subregion; Reid and Alonso 1995), and when cortical spiking was silenced by cooling or by electrical shocks that activate inhibition, the thalamic input to simple cells, measured intracellularly, remained orientation tuned (Ferster et al. 1996).

The pure feedforward model has difficulties. Orientation tuning width is nearly independent of contrast, whereas a linear sum followed by a threshold would broaden as contrast increases (the "iceberg effect" in reverse); cortical neurons can be suppressed by stimuli orthogonal to their preferred orientation (cross-orientation suppression); and in many cells inhibition is tuned to the same orientation as excitation but has opposite spatial phase ("push–pull"). These properties require cortical circuits in addition to the feedforward input: push–pull inhibition from neighboring simple cells, normalization by a pool of neurons (Section 18.7), and recurrent excitation (Section 18.3.3). In primate V1, a substantial fraction of complex cells receives direct LGN input, so the hierarchy simple → complex is a tendency rather than a strict rule.

## 18.3. Columns and Maps

### 18.3.1. Orientation and Ocular Dominance Columns

Electrode penetrations perpendicular to the cortical surface encounter neurons with the same preferred orientation and the same eye preference through all layers; oblique penetrations encounter orientations that change smoothly, about $10^\circ$ for every $50\,\mu\mathrm{m}$.

**Definition 18.3.1 (Orientation Column and Ocular Dominance Column)** An **orientation column** is a column of cortex, perpendicular to the surface and spanning its layers, in which neurons share a preferred orientation. An **ocular dominance column** is a band of cortex in which neurons respond preferentially to one eye; in layer 4C of the primate the inputs of the two eyes are almost completely segregated into alternating stripes about $0.4$–$0.5\,\mathrm{mm}$ wide.

Ocular dominance columns were visualized by injecting a radioactive tracer into one eye and letting it travel trans-synaptically to layer 4 (Hubel, Wiesel and LeVay), or by staining for the activity marker cytochrome oxidase after closing one eye. Their sensitivity to visual experience during a critical period is the subject of [7.16.21](/7.16.21#sec-21.4).

### 18.3.2. Orientation Maps and Pinwheels

Optical imaging of intrinsic signals (changes in light reflectance due to blood oxygenation in active cortex), with gratings of different orientations, revealed the layout of preferred orientations across the surface of V1 (Bonhoeffer and Grinvald 1991).

**Definition 18.3.2 (Orientation Map and Pinwheel)** The preferred orientation $\theta(\boldsymbol{x})$ as a function of position $\boldsymbol{x}$ on the cortical surface is the **orientation map**. A **pinwheel** is a point of the map around which the preferred orientation changes continuously through all values from $0^\circ$ to $180^\circ$ along any closed path encircling it once.

Because orientation is defined modulo $180^\circ$, the map is conveniently described by the complex field $z(\boldsymbol{x}) = \lvert z\rvert\mathrm{e}^{2\mathrm{i}\theta(\boldsymbol{x})}$, and pinwheels are its zeros, topological point defects of winding number $\pm\frac12$ in $\theta$. Two-photon calcium imaging confirmed with single-cell resolution that orientation changes abruptly but in an orderly way at pinwheel centers in the cat (Ohki et al. 2006), whereas in mice and rats V1 neurons are orientation selective but arranged in a "salt-and-pepper" fashion without maps. Maps are therefore not necessary for orientation selectivity; they may reduce the wiring needed to connect neurons with similar properties.

A striking quantitative regularity holds across species that have maps. If $\Lambda$ is the typical spacing of the orientation map (the period of the dominant Fourier component of $z$), the density of pinwheels per area $\Lambda^2$ is close to $\pi$ in tree shrews, galagos and ferrets, whose last common ancestor lived about 65 million years ago (Kaschube et al. 2010). The value $\pi$ is predicted by a class of models in which the map self-organizes by activity-dependent interactions with long-range suppression ([7.16.22](/7.16.22)), and it is not a property of random maps, which have a different density.

The functional maps are mutually arranged. Orientation contours tend to cross ocular dominance borders at right angles, pinwheels lie preferentially near the centers of ocular dominance bands, and in the primate, color-selective "blobs" rich in cytochrome oxidase sit at the centers of ocular dominance columns. Hubel and Wiesel called a block of cortex about $1\,\mathrm{mm}$ on a side that contains a full set of orientations and both eyes a hypercolumn: a module that analyzes one region of the visual field completely.

### 18.3.3. The Ring Model of Orientation Tuning

How do circuits within a column shape orientation tuning? Consider the neurons of one hypercolumn, indexed by their preferred orientation $\theta \in (-\pi/2, \pi/2]$, with rates $r(\theta, t)$ and recurrent connections that depend only on the difference of preferred orientations.

**Formula 18.3.1 (Ring Model)** In the ring model (Ben-Yishai, Bar-Or and Sompolinsky 1995),

$$
\tau_{\mathrm{r}}\frac{\partial r(\theta)}{\partial t} = -r(\theta) + \Bigl[h(\theta) + \int_{-\pi/2}^{\pi/2}\frac{\mathrm{d}\theta'}{\pi}\bigl(-\lambda_0 + \lambda_1\cos 2(\theta - \theta')\bigr)r(\theta')\Bigr]_+, \tag{18.4}
$$
where $h(\theta) = Ac\,(1 - \varepsilon + \varepsilon\cos 2\theta)$ is a weakly tuned feedforward input from the LGN for a stimulus at $\theta = 0$ and contrast $c$, $\lambda_0 > 0$ is uniform inhibition and $\lambda_1 > 0$ tuned excitation.

The model is a firing-rate network of the type introduced in [7.16.15](/7.16.15). Its behavior is understood from its Fourier modes. Without rectification, the weight kernel acts on the uniform mode with gain $-\lambda_0$ and on the $\cos 2\theta$ mode with gain $\lambda_1/2$ (because $\int\frac{\mathrm{d}\theta'}{\pi}\cos 2(\theta - \theta')\cos 2\theta' = \frac12\cos 2\theta$), so in steady state the tuned component of the input is amplified by $1/(1 - \lambda_1/2)$ and the untuned component suppressed by $1/(1 + \lambda_0)$. As $\lambda_1 \to 2$ the amplification diverges. With rectification and $\lambda_1 > 2$ the network enters a regime in which only neurons within a band of preferred orientations are active; the width of the band is set by $\lambda_1$ alone, and the input determines only where the band sits and, through the contrast, how high it is.

The ring model thus explains contrast-invariant tuning and how a weak feedforward bias can be turned into sharp selectivity. It also makes a prediction that distinguishes it from feedforward models: the network should respond with a tuned bump even to a nearly untuned input, and its response should follow the strongest component of a mixture of orientations. Experiments find intermediate behavior: intracellular recordings show that excitation and inhibition onto V1 neurons are similarly tuned, as both models allow, and optogenetic silencing of cortical excitation in mice reduces responses by a constant factor without changing tuning width (Lien and Scanziani 2013), which suggests that in mouse V1 recurrent circuits amplify rather than sharpen. The same model with $\theta$ standing for a spatial position or a head direction is the continuous attractor of [7.16.44](/7.16.44).

![The ring model of orientation selectivity (Formula 18.3.1, with $A = 40$ Hz, $\varepsilon = 0.1$, $\lambda_0 = 7.3$, $\lambda_1 = 11$, $\tau_{\mathrm{r}} = 10$ ms; 120 neurons; parameters of Dayan and Abbott). A: the feedforward input at four contrasts; it is only 10 % modulated by orientation. B: steady-state responses of the network; recurrent excitation and uniform inhibition turn the weak bias into a sharp tuning curve, active only within about ±28° of the stimulus orientation. C: the responses normalized to their maxima coincide: the tuning width is set by the recurrent weights and is independent of contrast, unlike the broad input (dashed, rescaled)](./plots/ring-model.py)

## 18.4. Laminar Circuits

The six layers of neocortex ([7.14.46](/7.14.46#sec-46.1.2)) organize the flow of information within a column. In V1 the canonical sequence is:

1. Thalamic input arrives mainly in layer 4 (in primates, the magnocellular pathway in 4Cα and the parvocellular in 4Cβ; the koniocellular pathway in layers 2/3).
2. Layer 4 excitatory neurons (spiny stellate cells) project mainly up to layers 2/3.
3. Layer 2/3 pyramidal neurons send outputs to higher cortical areas and project down to layer 5.
4. Layer 5 pyramidal neurons project to subcortical targets (superior colliculus, pulvinar, pons) and layer 6 neurons back to the LGN and to layer 4.

Feedforward projections between cortical areas originate mainly in superficial layers and terminate in layer 4 of the target area; feedback projections originate in deep layers and avoid layer 4. This laminar asymmetry was used by Felleman and Van Essen (1991) to order the areas of the macaque visual cortex into a hierarchy of about ten levels, a hierarchy that is confirmed by the latencies of visual responses and by the growth of receptive field sizes.

Within the column, about $80\,\%$ of the neurons are excitatory, and the inhibitory interneurons fall into three main classes that dominate the circuit at different points: parvalbumin cells (fast, perisomatic inhibition that controls gain and timing), somatostatin cells (dendritic inhibition, surround suppression) and VIP cells, which inhibit somatostatin cells and thereby disinhibit pyramidal neurons, a motif activated by locomotion and attention. Thalamic synapses make up only $5$–$10\,\%$ of the excitatory synapses even onto layer 4 neurons; the rest are cortical, so most of the input to a cortical neuron comes from other cortical neurons, and the recurrent amplification of the ring model is anatomically plausible.

## 18.5. Parallel Pathways and the Visual Hierarchy

### 18.5.1. Two Streams

Beyond V1 and V2 the visual cortex divides into a dorsal stream toward the parietal lobe, concerned with motion, space and the visual guidance of action, and a ventral stream toward the temporal lobe, concerned with the identity of objects (Ungerleider and Mishkin 1982; [7.14.41](/7.14.41#sec-41.4.3)). The evidence is double dissociation: monkeys with temporal lesions fail at object discrimination but not at landmark tasks, and the reverse holds after parietal lesions; patient D. F., with damage to lateral occipital cortex, could not report the orientation of a slot but posted a card into it accurately (Goodale and Milner 1992). Along both streams, receptive fields grow (from about $0.5^\circ$ in foveal V1 to tens of degrees in IT) and selectivity becomes more complex and more invariant to position and size.

### 18.5.2. MT and the Integration of Motion

The middle temporal area (MT, V5) of the macaque is small, and almost all its neurons are direction selective, with receptive fields about ten times wider than in V1 and tuning to speed. It solves a problem that V1 cannot: the aperture problem. A V1 neuron sees a moving edge through a small receptive field and can only measure the component of velocity perpendicular to the edge; a plaid made of two gratings moving in different directions is perceived as a single pattern moving in a third direction. Movshon and colleagues (1985) found that V1 neurons and some MT neurons ("component cells") respond to the directions of the two gratings, while other MT neurons ("pattern cells") respond to the direction of the perceived pattern: they combine the constraints of several component measurements, the intersection of constraints. Area MT is also where the link between single neurons and perception has been made most directly (Section 18.8).

### 18.5.3. V4 and IT

Area V4 lies in the ventral stream after V2. Its neurons respond to color, texture and contour shape; they are tuned to the curvature of a boundary at a particular position relative to the object center, so that a population of V4 cells represents a shape as a set of boundary fragments in an object-centered frame (Pasupathy and Connor 2001). Inferotemporal cortex contains neurons selective for complex shapes and object categories with receptive fields covering much of the visual field. Responses of IT populations support linear readout of object identity and category despite changes in position, size and pose: linear classifiers applied to a few hundred IT neurons, recorded within $100$–$200\,\mathrm{ms}$ of stimulus onset, categorize objects about as well as monkeys do (Hung et al. 2005). How this invariance is achieved by the stages before IT is the question that hierarchical models address ([7.16.19](/7.16.19)).

## 18.6. Face Recognition

### 18.6.1. Face Patches

Faces are the most socially important objects in a primate's visual world, and the brain has a specialized network to process them. In humans, functional imaging revealed a region in the fusiform gyrus that responds more strongly to faces than to other objects (the fusiform face area, Kanwisher et al. 1997), and its damage causes prosopagnosia. In macaques, Tsao, Freiwald, Livingstone and colleagues used functional MRI to locate regions of IT that respond selectively to faces and then recorded from them.

**Definition 18.6.1 (Face Patch)** A **face patch** is a region of a few millimeters in the temporal (or prefrontal) cortex in which almost all neurons respond much more strongly to faces than to other objects. The macaque has six face patches on each side along the temporal lobe, connected with one another into a network.

In the middle face patches, $97\,\%$ of the visually responsive neurons were face selective (Tsao et al. 2006): a direct demonstration that a region identified by imaging is a cortical module of a single function. Microstimulation of one patch activates the others, showing that they form a connected network, and the patches are arranged as a hierarchy: neurons in the posterior patches are tuned to the view of a face (left profile, frontal), neurons in an intermediate patch respond to mirror-symmetric views, and neurons in the most anterior patch respond to the identity of an individual across views (Freiwald and Tsao 2010).

### 18.6.2. The Axis Model

What does a face cell encode? Chang and Tsao (2017) parameterized faces by $50$ dimensions: $25$ for shape (the positions of landmarks) and $25$ for appearance (the texture after shape normalization), obtained by principal component analysis of a large set of face photographs. They presented thousands of faces sampled from this space while recording from two face patches.

**Formula 18.6.1 (Axis Model of Face Cells)** Let $\boldsymbol{x} \in \mathbb{R}^{50}$ be the coordinates of a face relative to the average face. A face cell's firing rate is, to a good approximation, a linear function of the projection of $\boldsymbol{x}$ onto a preferred axis $\boldsymbol{a}$,

$$
r(\boldsymbol{x}) = b + g\,\boldsymbol{a}\cdot\boldsymbol{x}, \tag{18.5}
$$
so that its response increases along the axis and is constant along all directions orthogonal to it.

The axis model contrasts with an exemplar model, in which each cell responds to faces near a preferred face, with a response that falls off in all directions: with axis tuning the iso-response surfaces are parallel planes, with exemplar tuning they are closed shells around the preferred face. The data supported the axis model: responses along the preferred axis were ramp-shaped, often monotonic past the extremes of natural faces, and flat along orthogonal axes. A consequence of Eq. (18.5) is that the population code is linear: if $N$ cells have preferred axes spanning the face space, the face can be recovered from their responses by linear regression. Using about $200$ neurons from the two patches, Chang and Tsao reconstructed faces that the monkeys had seen with remarkable accuracy, and predicted the responses of single cells to new faces. Faces that differ only along directions orthogonal to a cell's axis are, for that cell, indistinguishable, a strong and confirmed prediction.

![The axis model of face cells (Formula 18.6.1), simulated in a 50-dimensional face space with standard normal coordinates; rates are counted in 0.3 s windows with Poisson noise. A: a model cell responds with a ramp to faces placed along its preferred axis and with a flat response (about its baseline of 20 Hz) to faces along an orthogonal axis; means of 8 trials ± SE. B: iso-response contours in the plane of the two axes: straight lines perpendicular to the preferred axis for the axis model (blue) and closed circles around a preferred face for an exemplar model (orange), the distinction tested by Chang and Tsao. C: linear decoding; a linear map from the responses of N model cells to the 50 face coordinates is fitted on 1000 faces and tested on 1000 others; the correlation between true and decoded coordinates rises with N and reaches about 0.9 with 400 cells](./plots/face-axis-model.py)

The axis model also connects face cells with machine learning: the preferred axes of IT face cells are well predicted by the units of the final layers of deep networks trained to recognize objects, and by the latent dimensions of networks trained without labels to generate faces ([7.16.19](/7.16.19), [7.16.48](/7.16.48)).

## 18.7. Attention as Gain Modulation

The responses of visual neurons depend on what the animal attends to. When a monkey attends to a stimulus inside the receptive field of a V4 neuron, rather than to a stimulus elsewhere, the neuron's response increases by about $20$–$30\,\%$ on average, and the increase is multiplicative: the orientation **tuning curve** is scaled without a change of its width or preferred orientation (McAdams and Maunsell 1999). The effect grows along the hierarchy, from a few percent in V1 to large effects in V4 and MT, and is accompanied by a reduction of trial-to-trial variability and of **noise correlations** between neurons (Cohen and Maunsell 2009; Mitchell et al. 2009), which increases the information that the population carries ([7.16.26](/7.16.26)).

When two stimuli are inside a receptive field, the response is typically between the responses to each alone, a weighted average, and attention to one stimulus moves the response toward the response to that stimulus alone (Moran and Desimone 1985; Reynolds, Chelazzi and Desimone 1999), a phenomenon described as biased competition. Both observations are captured by a single formula.

**Formula 18.7.1 (Normalization Model of Attention)** Let $E(\boldsymbol{x}, \theta)$ be the stimulus drive to neurons with receptive field center $\boldsymbol{x}$ and preferred feature $\theta$, and $A(\boldsymbol{x}, \theta) \geq 1$ an attention field. The response is

$$
R(\boldsymbol{x}, \theta) = \frac{A(\boldsymbol{x}, \theta)\,E(\boldsymbol{x}, \theta)}{S(\boldsymbol{x}, \theta) + \sigma}, \qquad S = s * (A\,E), \tag{18.6}
$$
where the suppressive drive $S$ is the attention-weighted drive pooled over neighboring positions and features by a kernel $s$, and $\sigma$ is a semisaturation constant (Reynolds and Heeger 2009).

Depending on the relative sizes of the stimulus and of the attention field, Eq. (18.6) produces either a multiplicative change of response gain or a shift of the contrast-response function along the contrast axis (contrast gain), which reconciles experiments that had appeared contradictory. The source of the attention signal is a network of frontal and parietal areas: microstimulation of the frontal eye field below the threshold for evoking a saccade enhances the responses of V4 neurons whose receptive fields lie at the endpoint of that saccade, as attention does (Moore and Armstrong 2003). **Divisive normalization**, of which Eq. (18.6) is an instance, is a canonical computation found also in the retina, the olfactory system and auditory cortex ([7.16.23](/7.16.23)).

## 18.8. From Perception to Decision

The most direct tests of how visual neurons contribute to perception come from experiments in which a monkey reports what it sees while neurons are recorded or stimulated. Newsome and colleagues trained monkeys to report the direction of motion of a field of random dots, in which a fraction of the dots, the motion coherence, move coherently in one of two opposite directions and the rest move randomly. At $0\,\%$ coherence there is no net signal, and performance improves with coherence along a **psychometric function** with a threshold of a few percent.

Three results linked MT to this behavior.

1. Lesions of MT raise the coherence threshold, and the deficit recovers in weeks as other areas compensate.
2. Neurometric versus psychometric functions: from the spike counts of a single MT neuron in response to its preferred and null directions, an ideal observer that compares the count with that of a hypothetical "antineuron" (using the **ROC curve** of the two count distributions) discriminates direction about as well as the monkey; on average, single neurons and the animal had nearly equal thresholds (Britten et al. 1992). Moreover, trial-to-trial fluctuations of a neuron's response are weakly correlated with the monkey's choices at a fixed stimulus (**choice probability** about $0.55$), which is expected only if the neuron, or its correlated neighbors, contributes to the decision.
3. Microstimulation: weak electrical stimulation of a cluster of MT neurons with a common preferred direction during the stimulus biases the monkey's choices toward that direction, as if coherent motion had been added to the display (Salzman, Britten and Newsome 1990). The activity of this cluster is therefore sufficient to influence perception.

These experiments inaugurated the study of perceptual decision making at the level of neurons. The comparison of neurometric and psychometric functions, the paradox that single neurons are as sensitive as the animal although the animal has thousands of them (resolved by correlated noise, [7.16.26](/7.16.26)), and the accumulation of MT evidence over time by neurons in the lateral intraparietal area ([7.16.47](/7.16.47)) are developed later in the course.

## Summary

| Topic | Key results |
|---|---|
| LGN and magnification | LGN relays retinal signals under strong cortical and modulatory control (tonic versus burst mode); $M(E) = M_0/(1 + E/E_2)$, a logarithmic map, Formula 18.1.1 |
| Simple and complex cells (Definition 18.2.1) | Separate ON/OFF subregions versus phase invariance; $F_1/F_0 > 1$ versus $< 1$ |
| Receptive field models | Gabor filters (Definition 18.2.2) for simple cells; energy model (Definition 18.2.3, Theorem 18.2.1) for complex cells; space–time inseparable fields for direction selectivity |
| Feedforward and recurrent circuits | Aligned LGN inputs give orientation bias (Hubel–Wiesel); contrast invariance, cross-orientation suppression and push–pull require cortical circuits |
| Columns and maps (Definitions 18.3.1, 18.3.2) | Orientation and ocular dominance columns; pinwheels, density $\approx \pi$ per $\Lambda^2$ in species with maps; salt-and-pepper in rodents |
| Ring model (Formula 18.3.1) | Tuned mode amplified by $1/(1 - \lambda_1/2)$; for $\lambda_1 > 2$ with rectification, tuning width set by the recurrent weights, independent of contrast |
| Laminar circuits | L4 → L2/3 → L5/6; feedforward to L4, feedback avoiding L4; PV, SST, VIP interneurons; thalamus supplies 5–10 % of synapses |
| Pathways | Dorsal and ventral streams; MT pattern cells solve the aperture problem; V4 curvature tuning; linear readout of IT populations |
| Faces | Face patches (Definition 18.6.1) form a hierarchical network; axis model (Formula 18.6.1): linear tuning to a projection in face space, linear decoding of faces |
| Attention | Multiplicative gain, reduced variability and correlations; normalization model, Formula 18.7.1 |
| Perception and decision | MT neurometric thresholds match psychometric ones; choice probability; microstimulation biases choices |

## Questions

1. Using Eq. (18.1), estimate the cortical distance between the representations of $1^\circ$ and $2^\circ$ eccentricity, and between $20^\circ$ and $21^\circ$, in human V1. What does the ratio say about acuity?

   **Answer** $M(1.5^\circ) \approx 23/(1 + 1.5/0.75) \approx 7.7\,\mathrm{mm\,deg^{-1}}$, so about $7.6\,\mathrm{mm}$ (the exact integral $M_0E_2\ln\frac{1 + 2/0.75}{1 + 1/0.75} = 17.3\ln(3.67/2.33) \approx 7.8\,\mathrm{mm}$). At $20.5^\circ$, $M \approx 23/(1 + 27.3) \approx 0.81\,\mathrm{mm\,deg^{-1}}$, about $0.8\,\mathrm{mm}$. The ratio is about ten. If each cortical millimeter supports the same spatial resolution, acuity falls about tenfold between these eccentricities, close to the measured decline; the resolution limit is set by the density of retinal ganglion cells, which the cortex inherits.

2. A complex cell is modeled by the energy model, Eq. (18.3). How does its response to a grating depend on contrast, and why might real complex cells show response saturation at high contrast? Which other formula of this chapter could describe the saturation?

   **Answer** By Theorem 18.2.1 the response is proportional to $c^2$: quadratic, and phase invariant. Real neurons saturate at high contrast; their contrast-response functions are well fitted by the Naka–Rushton form $R = R_{\max}c^n/(c^n + c_{50}^n)$ with $n \approx 2$. This is a normalization: divide the squared drive by the pooled drive of neighboring neurons plus a constant, as in Eq. (18.6) with $A = 1$. Normalization produces saturation, contrast-invariant tuning and cross-orientation suppression from the same mechanism.

3. In the linear regime of the ring model, a feedforward input $h(\theta) = h_0 + h_2\cos 2\theta$ produces a steady state $r(\theta) = r_0 + r_2\cos 2\theta$. Derive $r_0$ and $r_2$ and explain why the network becomes unstable when $\lambda_1 > 2$.

   **Answer** In the linear regime the steady state satisfies $r = h + W r$, where $W$ acts on Fourier modes as a multiplication: the uniform mode by $-\lambda_0$ (because $\int\frac{\mathrm{d}\theta'}{\pi}(-\lambda_0) = -\lambda_0$ over an interval of length $\pi$) and the $\cos 2\theta$ mode by $\lambda_1/2$. Hence $r_0 = h_0/(1 + \lambda_0)$ and $r_2 = h_2/(1 - \lambda_1/2)$. The dynamics of the mode amplitude is $\tau_{\mathrm{r}}\dot r_2 = -(1 - \lambda_1/2)r_2 + h_2$, whose eigenvalue $-(1 - \lambda_1/2)/\tau_{\mathrm{r}}$ becomes positive for $\lambda_1 > 2$: any tuned perturbation grows until the rectification limits it, which produces a bump whose width is set by $\lambda_1$.

4. (Open question) The microstimulation experiment of Salzman and Newsome showed that MT activity is sufficient to bias perception. What additional experiment would test whether MT activity is necessary for the judgment on a trial-by-trial basis, and what results would you expect if the decision is read out from a large pool of neurons with correlated noise?

   **Answer** A test of necessity is a reversible, temporally precise inactivation of MT (optogenetic silencing in macaques, or pharmacological inactivation with muscimol) during the motion stimulus, measuring the shift of the psychometric threshold; inactivation of MT with muscimol does raise thresholds strongly. If the decision is read from a large pool with correlated noise, (a) inactivating a small cluster should have little effect, because other neurons with the same preference carry the same information; (b) choice probabilities of single neurons should be modest and similar across neurons; (c) stimulating a cluster should bias choices more than silencing it changes thresholds. These predictions follow because information in a correlated population saturates, so removing a few neurons barely changes it ([7.16.26](/7.16.26)).
