---
title: "Hierarchical Models of Vision: From Hubel–Wiesel to Deep Networks"
description: The selectivity–invariance problem and object manifolds; the Neocognitron and HMAX as alternating simple and complex stages; task-optimized convolutional networks as models of the ventral stream, regression mapping and representational similarity analysis; adversarial examples, texture bias and the role of recurrence; self-supervised models; models of the dorsal stream.
---

The previous chapter followed visual signals from V1 to IT and found neurons of increasing selectivity and invariance ([7.16.18](/7.16.18)). This chapter asks whether a single computational principle, repeated at every stage, can explain the whole hierarchy. Hubel and Wiesel's proposal that complex cells pool simple cells led to a family of hierarchical models, from Fukushima's Neocognitron (1980) to the **convolutional neural networks** of modern machine learning, which in turn became the best available models of the ventral stream. The architecture, training and optimization of convolutional networks are covered in [4.7.3](/4.7.3) and [4.7.4](/4.7.4) and are not repeated here; this chapter treats them as hypotheses about the brain: how they are compared with neural data, where they agree, and where they fail.

## 19.1. The Selectivity–Invariance Problem

Object recognition must reconcile two opposite demands. A representation must be selective: it must distinguish a face from a similar face, a "7" from a "1". And it must be invariant: the same object seen at a different position, size, pose, illumination or partially occluded must give the same result. In pixel space these demands conflict. The images of one object under all its transformations form a curved, low-dimensional manifold in the space of pixel intensities, and the manifolds of different objects are tangled: two images of different faces at the same position can be closer in pixel space than two images of the same face at different positions.

DiCarlo and Cox (2007) proposed that the ventral stream works by untangling these manifolds, so that at the level of IT the manifolds of different objects become linearly separable: a downstream neuron can then read out the identity of an object by a weighted sum of IT responses followed by a threshold, as the linear decoding of IT populations suggests ([7.16.18](/7.16.18#sec-18.5.3)). Each stage must make a representation that is both somewhat more selective (by combining features of the previous stage, an AND-like operation) and somewhat more invariant (by pooling features over positions or scales, an OR-like operation). Hubel and Wiesel's simple and complex cells are the first instance of these two operations.

## 19.2. Neocognitron and HMAX

### 19.2.1. Alternating S and C Layers

**Definition 19.2.1 (Simple–Complex Hierarchy)** A simple–complex hierarchy alternates two kinds of layers. A unit in an S layer ("simple") computes a tuned function of the activities $\boldsymbol{x}$ of a local patch of units in the layer below, maximal when $\boldsymbol{x}$ matches a stored template $\boldsymbol{w}$; the same template is replicated at all positions. A unit in a C layer ("complex") pools S units with the same template at neighboring positions or scales, by a sum, a sum of squares or a maximum.

In the Neocognitron (Fukushima 1980) the S units are thresholded linear filters learned by an unsupervised competitive rule, and the C units are local averages; the network recognized handwritten digits despite shifts and distortions. HMAX (Riesenhuber and Poggio 1999) made the pooling operation explicit:

$$
r_{\mathrm{S}} = \exp\Bigl(-\frac{\|\boldsymbol{x} - \boldsymbol{w}\|^2}{2\sigma^2}\Bigr), \qquad r_{\mathrm{C}} = \max_{j \in \text{pool}} r_{\mathrm{S},j}. \tag{19.1}
$$

The first S layer of HMAX consists of Gabor filters (V1 simple cells), the first C layer of their local maxima (complex cells), and higher S layers combine C1 outputs into templates of intermediate complexity learned from natural images (V4), whose maxima over the whole visual field give position-invariant units (posterior IT). The maximum, rather than the sum, preserves selectivity when the receptive field contains clutter: the response to a preferred stimulus is not diluted by other stimuli. Consistent with this, about half of the complex cells in cat V1 respond to two bars in their receptive field approximately as to the stronger one alone (Lampl et al. 2004). The energy model of [7.16.18](/7.16.18#sec-18.2.3) is the C operation with a sum of squares over a quadrature pair.

### 19.2.2. Growth of Receptive Fields

Repeated local operations make receptive fields grow along the hierarchy. For a stack of layers with kernel sizes $K_l$ and strides $s_l$ (a pooling layer is a layer with stride larger than one), the receptive field $r_l$ of a unit in layer $l$, measured in input pixels, satisfies

$$
r_l = r_{l-1} + (K_l - 1)\,j_{l-1}, \qquad j_l = j_{l-1}s_l, \qquad r_0 = j_0 = 1, \tag{19.2}
$$
where $j_l$ is the distance in the input between neighboring units of layer $l$. With unit strides the receptive field grows only linearly, $r_L = 1 + L(K - 1)$; with pooling, $j_l$ grows geometrically and so does $r_l$. In the macaque ventral stream, receptive field diameters at a few degrees of eccentricity grow from below $1^\circ$ in V1 through a few degrees in V4 to more than $10^\circ$ in IT, an increase that requires subsampling, in the brain as in networks.

![Receptive field growth in hierarchical networks, Eq. (19.2). A: receptive field size against layer for 3 × 3 convolutions with stride 1 (linear growth, $1 + 2L$), the same with 2 × 2 pooling after every convolution pair (geometric growth), and an AlexNet-like stack whose first layer has an 11-pixel kernel with stride 4. B: the dependency of one unit in layer 3 of a network of 3-wide kernels on the units below it: its receptive field spans $1 + 3(3 - 1) = 7$ input units](./plots/receptive-field-growth.py)

## 19.3. Convolutional Networks as Models of the Ventral Stream

### 19.3.1. Task-Optimized Models

HMAX had fixed, hand-designed early stages and could not match the performance of primates on difficult recognition tasks. From 2012, convolutional networks trained by **backpropagation** on millions of labeled photographs reached human-level accuracy on such tasks ([4.7.3](/4.7.3)). They are simple–complex hierarchies in which the templates of every layer are learned to optimize a task, and their first-layer filters, without any instruction to do so, resemble Gabor functions and color-opponent blobs.

Yamins, DiCarlo and colleagues (2014) asked whether such networks also explain neural responses. They presented the same set of several thousand object images to monkeys, recording from V4 and IT with multielectrode arrays, and to many network variants. The responses of each recorded neuron were predicted by a cross-validated linear regression from the units of a network layer (the regression mapping). Three results stood out:

1. The better a network performed at object categorization, the more of the variance of IT responses its top layer explained, although no network had been trained on neural data.
2. The best network explained about half of the explainable variance of IT sites, roughly twice as much as previous models.
3. The top layer best predicted IT, and an intermediate layer best predicted V4: the hierarchy of the network aligned with the hierarchy of the cortex.

The approach is called goal-driven or task-optimized modeling. It replaces the fitting of a model to neurons by the optimization of a model for a behavior, and then tests the internal representations against the brain. The same strategy produced models of auditory cortex (networks trained to recognize words and music genres, Kell et al. 2018), of the dorsal stream (Section 19.6) and of the motor system ([7.16.32](/7.16.32)). Networks fitted to V4 have also been used for control: images synthesized to maximize the predicted response of a V4 site drove the real neuron beyond its responses to any natural image (Bashivan, Kar and DiCarlo 2019), a strong test that a model captures what a neuron computes.

### 19.3.2. Representational Similarity Analysis

Regression maps one unit to one neuron and requires many stimuli. A second method compares representations without fitting any mapping.

**Definition 19.3.1 (Representational Similarity Analysis)** Let $\boldsymbol{r}_i$ be the response pattern of a system (a brain region measured by recording or fMRI, or a model layer) to stimulus $i$, $i = 1, \dots, n$. The representational dissimilarity matrix (RDM) of the system is the $n\times n$ matrix with entries

$$
D_{ij} = 1 - \operatorname{Corr}(\boldsymbol{r}_i, \boldsymbol{r}_j),
$$
or another distance between response patterns. **Representational similarity analysis** (RSA) compares two systems by the rank correlation between the upper triangles of their RDMs (Kriegeskorte, Mur and Bandettini 2008).

The RDM abstracts from the identities and the number of units: a population of $100$ neurons in monkey IT, a voxel pattern in human fMRI and a layer of $4096$ network units can all be compared on the same footing, as can different species. Human and monkey IT have strikingly similar RDMs for the same images, with a major division between animate and inanimate objects and a subdivision of faces and bodies (Kriegeskorte et al. 2008), and the RDMs of deep network layers come closer to those of IT the more the networks are trained for categorization (Khaligh-Razavi and Kriegeskorte 2014). Statistical inference compares the observed correlation with the noise ceiling, the correlation expected between the true RDM and one estimated from noisy data, which bounds how well any model can do.

![Representational similarity analysis with a small convolutional hierarchy (Definition 19.3.1). Stimuli are 48 synthetic images in four categories (horizontal, vertical and diagonal bars, crosses; H, V, D, X), each exemplar at a random position within ±8 pixels, with random contrast and noise. Layer 1 is the energy of four oriented Gabor filters at every position, layer 2 the maximum over 4 × 4 blocks, layer 3 the maximum over the whole image. A synthetic "IT" population of 60 rectified units mixes the layer-3 features with noise. A: RDMs of the pixels, of layer 3 and of the synthetic IT (dark: similar). In pixel space, images of the same category at different positions are as dissimilar as images of different categories; in layer 3, which is invariant to position, the four categories form blocks. B: Spearman correlation of each stage's RDM with the IT RDM; it increases along the hierarchy as invariance is built](./plots/rsa-demo.py)

### 19.3.3. What the Comparison Shows and What It Does Not

The success of task-optimized networks is often misunderstood. It does not show that the brain uses backpropagation (the learning algorithm is a separate question, [7.16.50](/7.16.50)), nor that individual network units correspond to neurons. It shows that the constraints of the task, together with a hierarchical, convolutional architecture, determine to a large extent the representations at each stage. The networks are also only partially predictive: a substantial part of explainable IT variance remains unexplained, and networks with very different architectures but similar performance can be equally predictive, so that the method discriminates poorly among them.

## 19.4. Differences Between Networks and Brains

### 19.4.1. Adversarial Examples

A network that classifies an image correctly can be made to misclassify it with high confidence by adding a perturbation that is invisible to a human (Szegedy et al. 2014). Goodfellow, Shlens and Szegedy (2015) argued that such adversarial examples are a consequence of approximate linearity in high dimensions, not of overfitting.

**Theorem 19.4.1 (Linear Vulnerability in High Dimensions)** Let a unit compute $z = \boldsymbol{w}\cdot\boldsymbol{x}$ with $\boldsymbol{w} \in \mathbb{R}^n$, and let the perturbation $\boldsymbol{\eta}$ be bounded in each component, $\|\boldsymbol{\eta}\|_\infty \leq \varepsilon$. The largest achievable change of $z$ is $\varepsilon\|\boldsymbol{w}\|_1$, attained by $\boldsymbol{\eta} = \varepsilon\operatorname{sgn}(\boldsymbol{w})$. If the components of $\boldsymbol{w}$ are of comparable size, with $\|\boldsymbol{w}\|_2 = 1$, then $\|\boldsymbol{w}\|_1 \approx \sqrt{2n/\pi}$ for Gaussian weights, whereas a perturbation with random signs changes $z$ by only about $\varepsilon\|\boldsymbol{w}\|_2 = \varepsilon$.

**Proof** $\lvert\boldsymbol{w}\cdot\boldsymbol{\eta}\rvert \leq \sum_i \lvert w_i\rvert\lvert\eta_i\rvert \leq \varepsilon\|\boldsymbol{w}\|_1$, with equality for $\eta_i = \varepsilon\operatorname{sgn}(w_i)$. For $w_i$ independent normal with variance $1/n$, $\mathbb{E}\lvert w_i\rvert = \sqrt{2/(\pi n)}$, so $\|\boldsymbol{w}\|_1 \approx n\sqrt{2/(\pi n)} = \sqrt{2n/\pi}$. For random signs $\varepsilon_i = \pm 1$, $\boldsymbol{w}\cdot\boldsymbol{\eta} = \varepsilon\sum_i \varepsilon_i w_i$ has mean zero and variance $\varepsilon^2\sum_i w_i^2 = \varepsilon^2$. $\square$

A per-pixel change far below the visibility threshold therefore adds up, over hundreds of thousands of pixels, to a change of a unit's input large enough to cross a decision boundary, provided it is aligned with the gradient. The fast gradient sign method, $\boldsymbol{x}' = \boldsymbol{x} + \varepsilon\operatorname{sgn}\nabla_{\boldsymbol{x}}L$, exploits exactly this.

![Linear vulnerability in high dimensions (Theorem 19.4.1). A: the per-component perturbation budget $\varepsilon$ needed to change the input of a linear unit with $\|\boldsymbol{w}\|_2 = 1$ by one unit, against the input dimension $n$. A perturbation aligned with the sign of the weights needs $\varepsilon = 1/\|\boldsymbol{w}\|_1 \approx \sqrt{\pi/2n}$ (dotted), which falls below 0.01 for $n > 10^4$; a perturbation with random signs needs $\varepsilon \approx 1$ regardless of $n$. B: for $n = 784$ (a 28 × 28 image) and $\varepsilon = 0.05$ per pixel, the changes produced by 5000 random-sign perturbations (histogram, standard deviation 0.05) against the change produced by the adversarial perturbation (line, about −1.1)](./plots/adversarial-linear.py)

Humans are not entirely immune: perturbations designed against an ensemble of networks, and shown briefly, bias human judgments slightly (Elsayed et al. 2018). But the gap is large, and it points to properties that brains have and standard networks lack: noise and stochasticity in early processing, divisive normalization, the low-pass filtering and foveation of the retina, and recurrent processing. Networks whose first stage is a model of V1 with Gabor filters, normalization and noise (VOneNet) are markedly more robust (Dapello et al. 2020).

### 19.4.2. Texture Versus Shape

Networks trained on ImageNet classify an image with the shape of a cat and the texture of elephant skin as an elephant, whereas humans call it a cat (Geirhos et al. 2019). Standard networks rely on local texture statistics, which suffice for the training set; training on images whose textures have been randomized by style transfer increases the shape bias and also the robustness to distortions. The difference shows that a network can match a task without matching the strategy of the visual system, and that the choice of training data and objective shapes the representation as much as the architecture.

### 19.4.3. Recurrence and Feedback

The ventral stream is not a feedforward pipeline. Each feedforward projection is matched by a feedback projection, and within every area recurrent connections outnumber the feedforward inputs ([7.16.18](/7.16.18#sec-18.4)). Core object recognition, recognizing an object in a brief glance, is fast (monkeys categorize in about $200$–$250\,\mathrm{ms}$ and IT responses carry category information about $100\,\mathrm{ms}$ after stimulus onset), which made a feedforward account plausible.

But for images that feedforward networks fail on and monkeys solve, the object identity emerges in IT about $30\,\mathrm{ms}$ later than for easy images, and adding recurrent connections to the network model captures this late information (Kar et al. 2019); inactivating prefrontal cortex, a source of feedback, reduces it. Recurrence also completes occluded objects and implements attention ([7.16.18](/7.16.18#sec-18.7)), and recurrent networks with fewer layers can match deep feedforward networks by unrolling in time. Feedback is also the substrate of predictive coding theories, in which higher areas send predictions and lower areas send prediction errors ([7.16.48](/7.16.48)).

## 19.5. Self-Supervised Models

Supervised training with millions of labeled images is not how a primate learns to see: infants receive few labels. **Self-supervised learning** ([4.6.1](/4.6.1); its methods in [4.7.7](/4.7.7)) learns representations from unlabeled data by solving a pretext task, for example making the representations of two augmented views of the same image similar and those of different images dissimilar (contrastive learning). Networks trained in this way predict the responses of the ventral stream about as well as supervised networks: Zhuang et al. (2021) found that contrastive embedding objectives produced the best models of V4 and IT among unsupervised methods, matching supervised ones, even when trained on head-camera videos recorded from a child (the SAYCam data set). The result weakens the objection from labels: the task that shapes the ventral stream could be the prediction or the consistency of the visual input itself. The relation between self-supervised objectives, generative models and theories of perception as inference is developed in [7.16.48](/7.16.48).

## 19.6. Models of the Dorsal Stream

The same strategy applies to motion. A classic mechanistic model of MT pools V1 motion-energy units ([7.16.18](/7.16.18#sec-18.2.3)) whose spatiotemporal frequency tuning lies on the plane in frequency space that corresponds to a given velocity, and normalizes them divisively; it reproduces the pattern-direction selectivity of MT cells and their speed tuning (Simoncelli and Heeger 1998). Networks trained to estimate optic flow or self-motion from video develop units with MT-like and MST-like tuning, and networks with separate streams for appearance and motion recognize actions better than single-stream networks, a computational argument for the division of labor between the two cortical streams. The dorsal stream also serves action, and its models are taken up with sensorimotor control in [7.16.29](/7.16.29).

| Model family | Mechanism | Strength | Main limitation |
|---|---|---|---|
| Neocognitron, HMAX | Hand-designed S and C stages, max pooling | Explicit link to simple and complex cells; invariance by design | Weak performance on natural images |
| Supervised CNN | Learned S stages, pooling, trained for categorization | Best prediction of V4/IT responses; layer–area correspondence | Adversarial vulnerability, texture bias, needs labels, feedforward |
| Recurrent CNN | Adds lateral and feedback connections | Captures late-emerging information for hard images | More parameters, less interpretable |
| Self-supervised CNN | Learned without labels from consistency or prediction | Equally predictive; plausible training signal | Same architectural limitations |

## Summary

- Object recognition requires both selectivity and invariance; the ventral stream can be viewed as untangling object manifolds until identity is linearly decodable in IT (Section 19.1).
- Simple–complex hierarchies (Definition 19.2.1) alternate template matching and pooling; HMAX uses a maximum, Eq. (19.1), which preserves selectivity in clutter. Receptive fields grow by Eq. (19.2), linearly without subsampling and geometrically with it.
- Task-optimized convolutional networks predict V4 and IT responses in proportion to their performance, with a layer–area correspondence (Section 19.3.1); representational similarity analysis (Definition 19.3.1) compares systems through their dissimilarity matrices, independently of units.
- Networks differ from brains in adversarial vulnerability, explained by linearity in high dimensions (Theorem 19.4.1), in texture bias, and in the lack of recurrence, which carries the information for hard images (Section 19.4).
- Self-supervised networks predict the ventral stream as well as supervised ones (Section 19.5); motion-energy and task-optimized models account for MT (Section 19.6).

## Questions

1. Using Eq. (19.2), compute the receptive field of a unit after five layers of $5\times5$ convolutions, each followed by $2\times2$ pooling with stride $2$. Compare with five layers of $5\times5$ convolutions without pooling.

   **Answer** Treat each convolution ($K = 5$, $s = 1$) and pooling ($K = 2$, $s = 2$) as layers. Start with $r = j = 1$. Conv 1: $r = 5$, $j = 1$; pool: $r = 6$, $j = 2$. Conv 2: $r = 6 + 4\cdot2 = 14$; pool: $r = 16$, $j = 4$. Conv 3: $r = 32$; pool: $r = 36$, $j = 8$. Conv 4: $r = 68$; pool: $r = 76$, $j = 16$. Conv 5: $r = 140$; pool: $r = 156$, $j = 32$. Without pooling, $r = 1 + 5\cdot4 = 21$. Pooling makes the receptive field about seven times larger and reduces the number of units by a factor of $4^5 \approx 1000$.

2. Why does an RDM-based comparison not depend on which network unit corresponds to which neuron? Give an example of two representations with identical RDMs but different single-unit tuning.

   **Answer** The RDM depends only on the correlations (or distances) between response patterns to pairs of stimuli. Any transformation that preserves these, such as a permutation of units, or, for Euclidean distances, an orthogonal rotation of the response space, leaves the RDM unchanged. Example: a population of neurons each tuned to one feature dimension and a population whose units are random orthonormal mixtures of these dimensions have the same Euclidean RDM, although the single units of the second population have mixed, uninterpretable tuning. RSA therefore tests the geometry of a representation, not the tuning of its elements.

3. Show that adversarial vulnerability of the kind in Theorem 19.4.1 does not depend on the nonlinearity of a network but can be reduced by it. What property of neural responses in V1 would limit it?

   **Answer** The theorem uses only the linear part of a unit; a deep network whose units operate mostly in their linear range (ReLUs are piecewise linear) inherits it, because the gradient with respect to the input is then a fixed vector over a neighborhood, and a perturbation along its sign accumulates. Nonlinearities that saturate or normalize (divisive normalization, which divides each response by the pooled activity of its neighbors) reduce the effective gain for perturbations that are spread over many inputs, and noise in early stages makes the gradient direction unreliable. V1 responses saturate with contrast, are normalized, and are noisy; these properties bound $\|\nabla_{\boldsymbol{x}}r\|_1$ and are among the features that make V1-inspired front ends more robust.

4. (Open question) Task-optimized networks with very different architectures explain IT responses about equally well. Propose an experiment or analysis that could discriminate between two such models.

   **Answer** Possible approaches: (a) model-driven stimulus synthesis, generating images on which the two models make maximally different predictions (controversial stimuli) and recording the neurons' responses to them; (b) comparing behavior image by image (the pattern of errors across images, not only the accuracy), which separates models that agree on average; (c) causal tests: inactivating a region and comparing the change in behavior with the effect of removing the corresponding layer in each model; (d) temporal dynamics: comparing the time course of neural responses with recurrent versions of the models. Each goes beyond average predictive accuracy on natural images, which is where current models converge.
