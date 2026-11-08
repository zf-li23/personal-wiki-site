---
title: Spinal and Brainstem Control of Movement
description: The hierarchy of motor control, the final common path, and the two destinations of sensory input; α and γ motor neurons and interneurons; the muscle spindle (intrafusal fibers, nuclear bag and nuclear chain fibers, the dynamic and static responses of Ia primary endings, II secondary endings), a phenomenological model, unloading and α–γ coactivation, the gamma loop; the Golgi tendon organ (Ib, in series with extrafusal fibers, autogenic inhibition); the stretch reflex and muscle tone, a latency estimate, a closed-loop model as negative feedback with delay, tremor and clonus; the flexor reflex (reciprocal inhibition, afterdischarge, local sign) and the crossed extensor reflex; spinal shock; spinal central pattern generators for locomotion, the spinal cat, the mesencephalic locomotor region and a hierarchical model of gait; reticulospinal and vestibulospinal tracts of the brainstem, decerebrate rigidity (γ and α rigidity), postural reflexes; the phase lag of segmental CPGs in the lamprey, gait transitions in quadrupeds and the Froude number, decentralized coordination in stick insects, undulatory locomotion of fishes and snakes.
source_hash: 2d13613c1959
---

A movement such as reaching for a glass of water appears to be initiated by will, but most of its details are worked out in the spinal cord and brainstem: maintaining posture and balance, adjusting the force of each muscle to the load, correcting quickly when something unexpected happens, and, when necessary, coordinating the limbs of the other side. The spinal cord is not just a cable that passes commands from the brain to the muscles; it contains reflex circuits and circuits that generate rhythmic movements, and above it the brainstem maintains posture and antigravity muscle tone. This chapter proceeds from the bottom up: motor neurons and interneurons, the two kinds of receptors in muscle, spinal reflexes and their nature as feedback control, spinal motor rhythms, and finally the role of the brainstem. The cortex, cerebellum, and basal ganglia are discussed in the next chapter ([7.14.45](/7.14.45)). Motor units and the size principle are in [7.14.9](/7.14.9#sec-9.8.2), the basic units of neural circuits (reciprocal inhibition, afterdischarge, central pattern generators) in [7.14.6](/7.14.6), the anatomy of the spinal cord in [7.14.7](/7.14.7#sec-7.2.7), and the general principles of proprioception and mechanoreceptors in [7.14.39](/7.14.39). The models in this chapter are phenomenological and serve to illustrate physiological mechanisms; computational theories of motor control belong to computational neuroscience ([7.16](/7.16)).

## 44.1. The Hierarchy of Motor Control

### 44.1.1. Hierarchical Control

Motor control has a hierarchical structure ([7.14.7](/7.14.7#sec-7.1.2)): the spinal cord executes specific movement patterns (reflexes, rhythmic alternation of the limbs), the brainstem handles posture, balance, and the initiation of movement, the cortex formulates strategies and initiates voluntary movement, and the cerebellum and **basal ganglia** act as side loops that correct and select motor programs. Each level can produce some movements independently, and each is modulated by the level above.

Sensory signals entering the spinal cord have two destinations: one is the neurons of the spinal gray matter, which elicit local reflexes at the same or neighboring segments; the other is the ascending route along the spinal cord to the brainstem, cerebellum, and cortex, where they take part in higher-level sensory and motor control. Branches of the same Ia fiber do both at once.

**Definition 44.1.1 (Final Common Path)** The motor neurons in the ventral horn of the spinal cord and in the motor nuclei of the brainstem are the sole exit through which all motor commands from reflexes, rhythm-generating circuits, and descending pathways reach the muscles; they are called the **final common path** (Sherrington).

### 44.1.2. Motor Neurons and Interneurons

The ventral horn contains two kinds of motor neurons:

- α motor neurons: large cell bodies that give rise to thick Aα fibers ($70$–$120\,\mathrm{m\,s^{-1}}$); their branches innervate many extrafusal muscle fibers and constitute a **motor unit**, and they are recruited in order according to the **size principle**.
- γ motor neurons: smaller cell bodies that give rise to thinner Aγ fibers; they innervate only the intrafusal fibers within the muscle spindle and make up about one third of the motor fibers of the ventral root. A few β motor neurons innervate extrafusal and intrafusal fibers at the same time.

Motor neurons are arranged in the ventral horn by muscle: those innervating trunk and proximal muscles lie medially, those innervating distal limb muscles (fingers) lie laterally, and those of flexors lie dorsal to those of extensors.

Interneurons outnumber motor neurons about 30-fold. They are small and highly excitable, often spontaneously active, and form circuits of **divergence**, **convergence**, **reciprocal inhibition**, oscillation, and so on with one another ([7.14.6](/7.14.6)). Most signals from the cortex, brainstem, and sensory afferents act first on interneurons and reach the motor neurons only after preprocessing by them; only a few (such as Ia fibers and some corticospinal fibers) synapse directly on motor neurons. Renshaw cells are a special class of inhibitory interneurons: axon collaterals of motor neurons excite them, and they in turn use glycine to inhibit the same group of motor neurons and neighboring ones, forming recurrent inhibition ([7.14.6](/7.14.6#sec-6.1.3)). In addition, many propriospinal neurons pass signals up and down between segments and coordinate the movements of the upper and lower limbs.

## 44.2. Muscle Spindles and Tendon Organs

Muscles contain two kinds of specialized proprioceptors: muscle spindles sense muscle length and its rate of change, and tendon organs sense muscle tension. They are not only the receptors of spinal reflexes but also report continuously to the cerebellum (error correction), the brainstem (posture and balance), and the cortex (motor planning and position sense), and so constitute the feedback sensors of the entire motor system.

### 44.2.1. Structure of the Muscle Spindle

**Definition 44.2.1 (Muscle Spindle)** The receptor in skeletal muscle that consists of several specialized intrafusal fibers enclosed in a connective tissue capsule, the sensory nerve endings wound around their middle portions, and the γ motor fibers innervating their two ends, that lies in parallel with the extrafusal fibers, and that senses muscle length and its changes is called a **muscle spindle**.

A muscle spindle is about $4$–$10\,\mathrm{mm}$ long and contains $3$–$12$ intrafusal fibers (usually fewer than about $10$), whose two ends attach to the endomysium of extrafusal fibers or to the tendon. The middle portion of an intrafusal fiber has little or no actin–myosin apparatus and cannot contract, and serves as the receptor; the two ends are striated and can contract under the control of γ motor neurons. There are two kinds of intrafusal fibers:

- Nuclear bag fibers ($1$–$3$ per spindle): the nuclei are concentrated in the swollen middle portion; they are divided into dynamic nuclear bag fibers (bag$_1$) and static nuclear bag fibers (bag$_2$).
- Nuclear chain fibers ($3$–$9$): thinner and shorter, with the nuclei lined up in a row in the middle.

There are two kinds of sensory endings:

- Primary endings: Ia fibers (thick, about $17\,\mu\mathrm{m}$, conduction velocity about $70$–$120\,\mathrm{m\,s^{-1}}$) wind spirally around the middle portions of all the intrafusal fibers, one per spindle.
- Secondary endings: class II fibers (about $8\,\mu\mathrm{m}$) lie on one or both sides of the primary ending, mainly on the nuclear chain fibers and static nuclear bag fibers.

The density of spindles differs greatly among muscles: the small hand muscles that control fine movements and the neck muscles have dozens to over a hundred spindles per gram of muscle, whereas large limb muscles have far fewer.

### 44.2.2. Dynamic and Static Responses

When the middle portion of an intrafusal fiber is stretched slowly, the firing frequencies of both primary and secondary endings increase approximately in proportion to length and continue while the length is held; this is the static response. When the spindle is stretched rapidly, the primary ending fires extra strongly during the stretch, with a frequency related to the rate of stretch, and falls quickly back to the static level when the stretch stops; when the spindle shortens, firing falls below the static level and may even stop. This is the dynamic response, which occurs almost only in primary endings.

**Formula 44.2.1 (Phenomenological Model of Spindle Afferent Firing)** Let the muscle length change be $L(t)$ and the rate be $v = \mathrm{d}L/\mathrm{d}t$. The firing frequency of the afferent fiber can then be written approximately as

$$
r(t) = \max\Bigl(0,\; r_0 + k_{\mathrm{s}}L + k_{\mathrm{d}}\,\operatorname{sgn}(v)\,\lvert v\rvert^{1/2}\Bigr), \tag{44.1}
$$

where $r_0$ is the resting firing rate, $k_{\mathrm{s}}$ is the length sensitivity, and $k_{\mathrm{d}}$ is the velocity sensitivity; the square-root dependence on velocity reflects the power-law velocity sensitivity of the primary ending (Matthews and Stein, 1969; exponent about $0.3$–$0.5$). $k_{\mathrm{d}}$ is large for Ia fibers and very small for class II fibers.

γ motor neurons adjust these two sensitivities. Dynamic γ fibers innervate dynamic nuclear bag fibers and enhance the dynamic response of the primary ending (increasing $k_{\mathrm{d}}$); static γ fibers innervate static nuclear bag fibers and nuclear chain fibers and enhance the static responses of the primary and secondary endings (increasing $k_{\mathrm{s}}$ and $r_0$) while reducing the dynamic response. The center can thus change the operating mode of the spindle according to the task: dynamic γ output is strengthened in unstable tasks that require rapid responses to unexpected perturbations, and static γ output in slow postural maintenance.

![Firing of spindle afferents during ramp-and-hold stretch (the phenomenological model of Formula 44.2.1). A: the muscle is stretched by 6 mm in 0.25 s, held for 1 s, and returned to its original length in 0.25 s. B: primary ending (Ia), r₀ = 20 per s, k_s = 4 (per s)/mm, k_d = 9; dynamic γ drive doubles k_d (r₀ = 30), static γ drive gives k_s = 8, k_d = 5, r₀ = 40. The extra firing during the stretch is the dynamic response and the plateau during the hold is the static response; Ia firing stops during shortening. C: secondary ending (class II), r₀ = 15, k_s = 5, k_d = 1, reporting almost only length. Firing rates are smoothed by a 20 ms low-pass filter.](./plots/spindle.py)

### 44.2.3. Unloading, α–γ Coactivation, and the Gamma Loop

The muscle spindle lies in parallel with the extrafusal fibers. When the extrafusal fibers contract and the muscle shortens, the spindle goes slack, and if the intrafusal fibers do not contract at the same time its firing stops (unloading), so the center loses information about length during muscle contraction. In reality, when the brain issues a motor command it almost always excites α and γ motor neurons together (α–γ coactivation); the two ends of the intrafusal fibers contract together with the extrafusal fibers and keep the middle portion taut, so the spindle remains sensitive throughout the contraction. If the actual shortening is less than intended (for example, because the load is heavier than expected), the intrafusal fibers are stretched relatively, Ia firing increases, and the output of the α motor neurons is reflexively strengthened to compensate for the load.

**Definition 44.2.2 (Gamma Loop)** The pathway by which excitation of γ motor neurons makes intrafusal fibers contract and excites the sensory endings of the spindle, and the Ia afferents then excite the α motor neurons of the same muscle so that the extrafusal fibers contract, thereby causing muscle contraction indirectly, is called the **gamma loop**.

Merton (1953) proposed that voluntary movement is initiated through the gamma loop: the α motor neurons "servo" to follow the length set by the intrafusal fibers. Later recordings found that in human voluntary movement α and γ motor neurons are activated almost simultaneously, with γ not preceding α, so the gamma loop is not the main route for initiating movement but a mechanism that maintains spindle sensitivity during movement and assists load compensation. The facilitatory and inhibitory systems of the brainstem regulate muscle tone mainly by changing the activity of γ motor neurons (Section 44.5).

### 44.2.4. The Tendon Organ

**Definition 44.2.3 (Golgi Tendon Organ)** The receptor at the junction of muscle and tendon that consists of bundles of collagen fibers enclosed in a connective tissue capsule and the Ib sensory endings wound among them, that lies in series with the extrafusal fibers, and that senses muscle tension is called a **Golgi tendon organ**.

Each tendon organ is connected to $10$–$15$ extrafusal fibers. When the muscle contracts, the tension tightens the collagen fibers and compresses the endings among them, and Ib firing increases with tension; during passive stretch, because the muscle fibers in series with it are much more compliant than the tendon, the tension on the tendon organ is small, so the tendon organ is most sensitive to tension from active contraction and can even report the contraction of a single **motor unit**. It also has a dynamic response (more firing when the tension rises rapidly) and a static response.

| | Muscle spindle | Tendon organ |
|---|---|---|
| Relation to extrafusal fibers | in parallel | in series |
| Quantity sensed | length and rate of change of length | tension |
| Afferent fibers | Ia, II | Ib |
| Efferent innervation | yes (γ) | none |
| During active contraction | unloaded (stops firing without γ) | firing increases |
| Reflex action on the homonymous muscle | monosynaptic excitation | inhibition via inhibitory interneurons |

In the spinal cord, Ib fibers inhibit the α motor neurons of the same muscle through inhibitory interneurons (autogenic inhibition) and at the same time excite the antagonist. The classical explanation is protection: when tension is excessive, the tendon organ makes the muscle relax suddenly and so prevents the tendon from being torn (the "clasp-knife" relaxation). It is now thought that its more important role is as **negative feedback** on force, which tends to equalize the load among the motor units of a muscle and regulates the magnitude of force during movement. In the stance phase of walking, Ib feedback from extensors even changes from inhibition to excitation and helps to maintain support; and the removal of load (a fall in Ib firing) is one of the signals for the start of the swing phase (Section 44.4).

## 44.3. Spinal Reflexes

### 44.3.1. The Stretch Reflex

**Definition 44.3.1 (Stretch Reflex)** The reflex contraction of an innervated skeletal muscle in response to being stretched is called the **stretch reflex**. The brief, synchronous contraction caused by rapid stretch (such as the tendon reflex elicited by tapping a tendon) is called the phasic stretch reflex; the contraction that maintains a certain tension and is caused by sustained slow stretch is called the tonic stretch reflex, which is the basis of **muscle tone**.

The basic pathway of the stretch reflex is monosynaptic: after entering the spinal cord, Ia fibers form excitatory synapses directly on the α motor neurons that innervate the same muscle (the homonymous muscle) and synergists. Collaterals of Ia fibers at the same time excite Ia inhibitory interneurons, which inhibit the motor neurons of the antagonist; this is **reciprocal inhibition** ([7.14.6](/7.14.6#sec-6.1.3)). Class II fibers end mainly on interneurons and act on motor neurons through polysynaptic pathways; their transmission is slower, and they take part in the tonic stretch reflex and in more complex regulation.

The phasic tendon reflex is caused mainly by the dynamic response of Ia fibers; the tonic stretch reflex is maintained by the static responses of the primary and secondary endings together. In standing, gravity flexes the knee and ankle and stretches the quadriceps and the triceps surae, and the stretch reflex keeps these antigravity muscles moderately contracted; this is the basic mechanism of posture maintenance.

**Example 44.3.1 (Latency of the Knee-Jerk Reflex)** Tapping the patellar tendon briefly stretches the muscle spindles of the quadriceps. The Ia fibers run from the spindles in the middle of the thigh to the $\mathrm{L_3}$–$\mathrm{L_4}$ segments, a path of about $0.5\,\mathrm{m}$; the return path of the motor fibers is similar. Taking the conduction velocities of Ia and α fibers both as about $80\,\mathrm{m\,s^{-1}}$, the round trip of $1.0\,\mathrm{m}$ takes about $12.5\,\mathrm{ms}$; adding a central synaptic delay of about $0.5$–$1\,\mathrm{ms}$, receptor transduction and transmission at the **neuromuscular junction** of about $1$–$2\,\mathrm{ms}$, and the slowing in the thinner terminal fibers, the latency of the electromyogram is about $15$–$20\,\mathrm{ms}$, in agreement with measurements. The central delay is enough for only one synapse, which is the evidence that the stretch reflex is monosynaptic ([7.14.5](/7.14.5)). The H reflex, recorded in the soleus muscle on electrical stimulation of the tibial nerve in the popliteal fossa, has a longer path and a latency of about $30\,\mathrm{ms}$. Muscles of the distal limb also show a second reflex component about $50$–$100\,\mathrm{ms}$ after stretch (the long-latency stretch reflex), whose pathway passes through motor cortex and whose gain can be adjusted with the task.

### 44.3.2. The Stretch Reflex as Negative Feedback with Delay

The stretch reflex is a **negative feedback**: muscle stretched → spindle firing increases → muscle contracts and restores its length. It keeps the limb in position when it is perturbed and acts as damping. But every negative feedback has a delay, and delayed negative feedback oscillates when the gain is large enough ([7.9.16](/7.9.16)).

**Formula 44.3.1 (Closed-Loop Model of the Stretch Reflex)** Simplify a joint as a second-order system with moment of inertia $J$, damping $b$, and stiffness $k$, with the reflex torque proportional to the length and velocity at a time $T$ earlier:

$$
J\ddot x + b\dot x + kx = -G\bigl[x(t - T) + \tau_{\mathrm{v}}\dot x(t - T)\bigr] + d(t), \tag{44.2}
$$

where $x$ is the deviation of the joint angle from the set position, $G$ is the reflex gain, $\tau_{\mathrm{v}}$ represents the velocity sensitivity of the spindle, and $d$ is an applied perturbation. Taking $x \propto \mathrm{e}^{\mathrm{i}\omega t}$, the boundary at which oscillation appears is given by the real solutions $(\omega, G)$ of the characteristic equation

$$
-J\omega^2 + \mathrm{i}b\omega + k + G(1 + \mathrm{i}\omega\tau_{\mathrm{v}})\,\mathrm{e}^{-\mathrm{i}\omega T} = 0 \tag{44.3}
$$

When $G$ exceeds the critical gain $G_{\mathrm{crit}}$, the system oscillates spontaneously at frequency $\omega/2\pi$.

The longer the delay, the lower the critical gain and the slower the oscillation (panel B). This explains two phenomena. Physiological tremor (about $8$–$12\,\mathrm{Hz}$) comes in part from resonance of short reflex loops (such as those of the fingers and wrist); here the reflex gain is below the critical value, and the system merely responds to perturbations with underdamped oscillation. Clonus is pathological: after damage to descending pathways (such as spinal cord injury or stroke), the activity of γ motor neurons and the **excitability** of motor neurons increase, the gain of the stretch reflex rises, and tendon reflexes become hyperactive; a rapid dorsiflexion of the ankle can cause rhythmic sustained contraction of the triceps surae at about $5$–$8\,\mathrm{Hz}$, ankle clonus; the reflex loop of the ankle is longer than that of the wrist, and the oscillation frequency is lower.

![Negative feedback with delay and oscillation of the stretch reflex (Formula 44.3.1; natural frequency of the joint 2 Hz, damping ratio 0.4, J = 1, τ_v = 0.05 s; a brief perturbation is applied at t = 0.1 s). A: response of the joint angle for a delay T = 40 ms and gains of 0.5, 0.95, and 1.1 times the critical gain: at low gain the perturbation decays quickly, near the critical gain a long-lasting oscillation appears, and above the critical gain the oscillation grows (clonus), with a frequency of about 5 Hz. B: critical gain (relative to the passive stiffness k, solid line, logarithmic scale) and oscillation frequency at the boundary (dashed line, right axis) as functions of the loop delay, obtained numerically from the characteristic equation (44.3): the longer the delay, the lower the gain at which oscillation occurs, and the slower the oscillation.](./plots/stretch-loop.py)

### 44.3.3. The Flexor Reflex and the Crossed Extensor Reflex

**Definition 44.3.2 (Flexor Reflex)** The reflex in which noxious stimulation (or strong tactile stimulation) of the skin of a limb makes the flexors of that limb contract and the extensors relax, so that the limb is rapidly withdrawn from the stimulus, is called the **flexor reflex**, also called the withdrawal reflex.

Pulling the hand back at once on touching a hot stove is a flexor reflex. It is a polysynaptic reflex whose pathway passes through several interneurons: afferent signals excite flexor motor neurons through excitatory interneurons and inhibit extensor motor neurons through inhibitory interneurons (**reciprocal inhibition**). The flexor reflex has three features:

1. Fast onset: the flexors begin to be excited within a few milliseconds of the stimulus.
2. Afterdischarge: after the stimulus stops, flexor contraction continues for tens to hundreds of milliseconds, and the stronger the stimulus, the longer the **afterdischarge** ([7.14.6](/7.14.6#sec-6.2.1)). Short afterdischarges come from repetitive firing of interneurons and long ones from reverberating circuits, which keep the limb away from the stimulus for some time after it has gone.
3. Local sign: the direction of withdrawal depends on the site stimulated; for example, when the inner thigh is stimulated, the leg is abducted; the reflex circuit "knows" how to move so as to get away from the stimulus, which is called local sign.

**Definition 44.3.3 (Crossed Extensor Reflex)** The reflex in which, when a flexor reflex occurs in one limb, the extensors of the opposite limb contract and the flexors relax so that it extends, is called the **crossed extensor reflex**.

When one foot steps on a nail and is lifted, the other leg must straighten to support the weight of the whole body. Afferent signals cross to interneurons on the opposite side, which excite the contralateral extensors and inhibit the contralateral flexors. The crossed extensor reflex appears only about $0.2$–$0.5\,\mathrm{s}$ after the flexor reflex begins, because it passes through more interneurons; its **afterdischarge** is also longer. The flexor reflex and crossed extensor reflex together are already a rudiment of the alternation of the two legs in walking.

### 44.3.4. Spinal Shock

After sudden complete transection of the spinal cord, all spinal reflexes below the transection disappear at once, blood pressure falls (loss of tone in the **sympathetic nervous system**), and the micturition and defecation reflexes also disappear; this is called spinal shock. After days to weeks, reflexes gradually recover and often become hyperactive: tendon reflexes are enhanced, clonus appears, the flexor reflex is elicited by weak stimuli, and spasms alternating between flexors and extensors may occur. Spinal shock shows that the excitability of spinal neurons normally depends on continuous facilitation by descending pathways (especially the reticulospinal and vestibulospinal tracts); the recovery and hyperactivity of reflexes are related to supersensitivity of motor neurons, new synaptic collaterals, and loss of descending inhibition. The Babinski sign that appears when the **corticospinal tract** is damaged (dorsiflexion of the great toe on stroking the sole, in contrast to plantar flexion in normal adults) is a clinical test of corticospinal function ([7.14.45](/7.14.45)).

## 44.4. Spinal Motor Rhythms

### 44.4.1. Central Pattern Generators in the Spinal Cord

The rhythmic alternation of the limbs in walking, running, and swimming is generated by **central pattern generators** in the spinal cord ([7.14.6](/7.14.6#sec-6.4.2)). The evidence comes from a series of classical experiments:

- Graham Brown (1911): in cats in which the dorsal roots were cut and all rhythmic sensory input removed, the spinal cord could still produce a walking rhythm with alternating flexors and extensors; he proposed the model of the **half-center oscillator** ([7.14.6](/7.14.6#sec-6.4.3)).
- The spinal cat: cats with the thoracic spinal cord transected (especially when transected young; Forssberg et al., 1980) can step with the hindlimbs on a treadmill and change their step frequency with the belt speed, even changing from walking to trotting; this shows that rhythm, left–right alternation, and adaptation to speed can all be accomplished within the spinal cord.
- The mesencephalic locomotor region: when a region of the midbrain of a decerebrate cat (Section 44.5.2) is stimulated electrically and continuously, the animal begins to walk on the treadmill; the stronger the stimulus, the faster the stepping, and the animal changes in turn to trotting and galloping (Shik, Severin, and Orlovsky, 1966). The descending command need provide only an intensity signal for "how fast"; the specific rhythm and the coordination between limbs are generated by the spinal cord.
- Fictive locomotion: in isolated spinal cords of newborn rats, adding NMDA and serotonin produces alternating rhythmic discharges that can be recorded from left and right and flexor and extensor ventral roots.

The spinal locomotor CPG is usually described as having two layers: a rhythm-generating layer determines "when" (period and phase), and a pattern-forming layer determines "which muscles" are active in what order (McCrea and Rybak, 2008). Mouse genetics has identified several groups of interneurons defined by developmental origin: V0 interneurons cross the midline and mediate left–right alternation, and mice lacking them hop with both legs in synchrony at all speeds; V1 and V2b inhibitory interneurons mediate flexor–extensor alternation; V2a interneurons take part in rhythm generation and left–right coordination; V3 interneurons balance the output of the two sides (Kiehn, 2016).

Sensory feedback does not generate the rhythm but adjusts its phase and amplitude: extension of the hip and removal of extensor load (a fall in tendon organ Ib firing) trigger the transition from the stance phase to the swing phase, and when the dorsum of the foot hits an obstacle during the swing, the flexor reflex is strengthened in the swing phase and lifts the leg higher (phase-dependent reflex reversal). The human spinal CPG depends more on descending input than that of cats and rodents, and patients with complete transection usually cannot walk spontaneously; but epidural electrical stimulation of the lumbar spinal cord combined with training can restore standing and stepping in some patients (Wagner et al., 2018).

## 44.5. Brainstem Control of Movement

### 44.5.1. Reticular and Vestibular Nuclei

The brainstem is both an extension of the spinal cord, providing for the head and face the same motor and sensory functions that the spinal cord provides for the body below the neck, and an independent control center that controls respiration ([7.14.20](/7.14.20)), cardiovascular activity ([7.14.16](/7.14.16)), some gastrointestinal activity, eye movements, balance, and the movements of many body parts. In somatic movement the most important role of the brainstem is to maintain posture against gravity, which is done by two groups of nuclei.

- Pontine reticular nuclei: through the pontine reticulospinal tract (medial reticulospinal tract) they excite the motor neurons that innervate the extensors of the trunk and proximal limbs (axial muscles). They are themselves highly excitable and receive strong excitatory input from the vestibular nuclei and deep cerebellar nuclei, and are a continuous source of facilitation.
- Medullary reticular nuclei: through the medullary reticulospinal tract (lateral reticulospinal tract) they inhibit the motor neurons of the same group of antigravity muscles. They have no strong spontaneous activity themselves, and their activity depends on input from the **corticospinal tract**, the rubrospinal tract, and other motor pathways.

Normally the inhibition of the medullary reticular system is balanced by the excitation from the pontine reticular system, which keeps the muscles at a moderate tension; when standing is required, higher centers reduce their drive to the medullary inhibitory system, and the pontine facilitatory system makes the antigravity muscles contract.

- Vestibular nuclei: the lateral vestibular nucleus excites antigravity muscles through the lateral vestibulospinal tract, in cooperation with the pontine reticular nuclei. Without the support of the vestibular nuclei, the excitatory effect of the pontine reticular system on axial antigravity muscles is greatly weakened. The vestibular nuclei selectively adjust the excitation of different antigravity muscles according to the signals of the vestibular apparatus ([7.14.42](/7.14.42)) to maintain balance: when the body tilts to one side, the extensors of that side are strengthened.

These descending pathways (the reticulospinal, vestibulospinal, and tectospinal tracts) lie in the ventromedial spinal cord and mainly innervate axial and proximal muscles, and are collectively called the **medial motor system**; the corticospinal and rubrospinal tracts lie laterally and mainly control fine movements of the distal limbs, and are collectively called the **lateral motor system** ([7.14.45](/7.14.45)).

### 44.5.2. Decerebrate Rigidity

**Definition 44.5.1 (Decerebrate Rigidity)** In an animal whose brainstem is transected between the superior and inferior colliculi, the tone of the extensor (antigravity) muscles of the whole body is at once markedly increased: the limbs are extended, the head and tail are raised, and the spine is arched backward. This is called **decerebrate rigidity**.

The transection cuts the drive from higher structures such as the cerebral cortex, basal ganglia, and red nucleus to the medullary inhibitory system, so the medullary reticular inhibitory system is ineffective, while the facilitation from the pontine reticular system and vestibular nuclei is preserved (their input comes from the vestibular apparatus and cerebellum below the transection); the stretch reflex of antigravity muscles is therefore excessive.

Decerebrate rigidity has two mechanistic components:

- γ rigidity: the brainstem facilitatory system mainly excites γ motor neurons, which increase spindle afferent input through the gamma loop and thereby excite α motor neurons reflexively. Cutting the corresponding dorsal roots (removing spindle afferents) or injecting a local anesthetic into the muscle abolishes the rigidity. Classical decerebrate rigidity is mainly of this kind, which shows that it is an excessive stretch reflex.
- α rigidity: if the anterior lobe of the cerebellum is then removed, the rigidity is instead worsened and is no longer abolished by cutting the dorsal roots, because the anterior lobe of the cerebellum normally inhibits α motor neurons through the vestibular nuclei, and after its removal the vestibulospinal tract excites α motor neurons directly.

Destroying the vestibular nuclei weakens the rigidity at once; further destroying the reticular formation of the midbrain and pons abolishes it completely. In humans, lesions of the midbrain or upper pons (such as brain herniation) cause a similar "decerebrate posture": the limbs are extended and the arms internally rotated, a sign of severe brainstem damage; when the lesion is above the midbrain (such as extensive cortical or internal capsule damage), the "decorticate posture" appears, with flexed arms and extended legs.

### 44.5.3. Postural Reflexes

**Definition 44.5.2 (Postural Reflex)** The reflex activity by which the central nervous system, according to the positions of the body and head, reflexively adjusts the tone and movement of the skeletal muscles of the whole body to maintain or restore normal posture is called a **postural reflex**.

A change of posture is in effect a redistribution of muscle tone among the muscles. Besides the stretch reflex and crossed extensor reflex of the spinal cord, postural reflexes involving the whole body are mainly accomplished by the brainstem (Magnus and de Kleijn):

- Labyrinthine tonic reflex: when the position of the head in space changes, the otolith organs of the utricle and saccule change their input to the vestibular nuclei and cause changes in the tone of the limb extensors. In a decerebrate animal the extensor tone is highest in the supine position and lowest in the prone position.
- Tonic neck reflex: when the head is turned relative to the trunk, proprioceptors in the joints and muscles of the neck change the muscle tone of the limbs. When the head is turned to one side, the extensor tone of the ipsilateral (the side the chin points to) upper and lower limbs increases and the contralateral flexors are strengthened; when the head is tilted back the forelimbs extend and the hindlimbs flex, and the opposite occurs when the head is flexed forward. These reflexes are inhibited by higher centers in normal adults and can be observed in infants and in patients with brain damage.
- Righting reflex: a supine animal that is released quickly turns over into the normal posture; a cat dropped from an upside-down position turns its head first and then its trunk in the air and lands on its feet. Righting is led by the head: vestibular and visual signals first return the head to its normal position, and the twisting of the neck then causes the trunk to turn through the neck proprioceptors. Animals with an intact midbrain have the righting reflex and decerebrate animals do not, which shows that its center is in the midbrain.

## 44.6. Evolution and Comparative Aspects

### 44.6.1. Segmental CPGs in the Lamprey

Swimming in the lamprey is the most thoroughly studied system of the vertebrate locomotor CPG (Grillner et al.). Its spinal cord has about 100 segments, and each segment, or even an isolated piece of only one or two segments, can produce a left–right alternating rhythm under the action of excitatory substances such as NMDA; the left–right alternation depends on glycinergic **reciprocal inhibition** across the midline ([7.14.6](/7.14.6#sec-6.5)). The rhythm of the whole cord propagates from head to tail, with a phase lag between neighboring segments of about $1\,\%$ of the period; over the whole swimming frequency range of $0.3$–$8\,\mathrm{Hz}$ this fraction hardly changes, so a wavelength of about one body length is always maintained on the body. If coordination between segments depended only on a fixed conduction delay, the phase lag would increase linearly with frequency, but this is not the case.

Cohen, Holmes, and Rand (1982) regarded each segment as a phase oscillator, with coupling between neighboring oscillators that locks them at a phase difference independent of frequency (a coupled-oscillator model of the same kind as the **Kuramoto model**). This model explains the constancy of the phase lag and also predicts how changing the excitability of the head or tail segments changes the direction of the wave: increasing the excitability of the tail end can make the wave propagate in the reverse direction, and the lamprey then swims backward, which has been verified in isolated spinal cords.

![Traveling wave generated by a chain of coupled segmental oscillators (phase oscillator model: N = 100 segments, dθ_i/dt = 2πf_i + a sin(θ_{i+1} − θ_i + φ) + a sin(θ_{i−1} − θ_i − φ), preferred phase φ = 2π/N, a = 200 s⁻¹, natural frequencies of the segments scattered by 2 % about f; starting from a nearly synchronous state, the state after 20 s is shown). A: bursts of the segments at f = 2 Hz (cos θ > 0.7): bursts propagate from head to tail. B: phase lag between neighboring segments (fraction of the period per segment) as a function of swimming frequency: about 1 % for the coupled-oscillator chain, independent of frequency; as a control, if the segments were coordinated only by a fixed conduction delay of 5 ms per segment, the lag would increase linearly with frequency (dashed line). C: left–right activity sin θ along the body at one instant: about one wavelength over the whole body.](./plots/segmental-cpg.py)

### 44.6.2. Gait Transitions in Quadrupeds

Quadrupeds such as horses and dogs adopt, with increasing speed, the gaits of walking, trotting, and galloping (running, bounding gallop), in each of which the four legs have a different phase relationship; these are the same as the gaits that appear when the CPG is driven by the mesencephalic locomotor region with different intensities (Section 44.4.1). Why change gait? Hoyt and Taylor (1981) trained horses to walk, trot, and gallop at various speeds on a treadmill and measured oxygen consumption: in each gait the energy cost of covering a unit distance is lowest at some intermediate speed, the speeds freely chosen by the horses fall near the minimum of each gait, and gait transitions occur where the energy cost curves of two gaits cross. Later studies found that the trot–gallop transition is also related to the forces on the leg bones and muscles reaching a threshold (Farley and Taylor, 1991); energy cost and mechanical load may jointly determine the transition point.

Walking is like an inverted pendulum: the body vaults over the stance leg, with kinetic and gravitational potential energy converted into each other. With leg length $l$ and gravitational acceleration $g$, define the dimensionless Froude number $Fr = v^2/(gl)$. The inverted pendulum model gives an upper limit of walking of $Fr = 1$ (the leg would leave the ground when the centripetal acceleration $v^2/l$ reaches $g$); in reality the transition from walking to running occurs near $Fr \approx 0.5$, almost independent of body size from humans to horses to birds (Alexander). With a human leg length of $0.9\,\mathrm{m}$, $v = \sqrt{0.5 \times 9.8 \times 0.9} \approx 2.1\,\mathrm{m\,s^{-1}}$, in agreement with the measured walk–run transition speed of about $2\,\mathrm{m\,s^{-1}}$. At the same Froude number, animals of different sizes move in mechanically similar ways, and this is a commonly used scale for comparing animal locomotion.

### 44.6.3. Decentralized Coordination in Insects

Insects have six legs, and the rhythm of each leg is generated mainly by local circuits in the thoracic ganglia and by the leg's own sensory feedback, with no single central rhythm for all legs. Cruse and colleagues' studies of the stick insect (*Carausius morosus*) summarized several local rules between legs, for example: when a leg is in the swing phase, it inhibits the leg in front of it from starting to swing; when a leg touches down and starts to support, it promotes the start of the swing of the leg in front of it; and a swinging leg aims its placement at the position of the neighboring leg in front. With only these local rules between neighboring legs (and no central command), the gait can pass with increasing speed from the slow "wave gait" (legs swing in sequence from the rear to the front) to the fast "tripod gait" (the front and hind legs of one side swing together with the middle leg of the other side) and adapts automatically when a leg is obstructed or missing (Cruse, 1990). A model built on these rules (Walknet) can control a six-legged robot to walk. A cockroach running fast depends more on a central rhythm and on the mechanical stability of the body, with feedback playing a relatively small role, which shows that "central rhythm" and "feedback coordination" form a continuous spectrum, and different animals at different speeds lie at different positions on it.

### 44.6.4. Undulatory Locomotion of Fishes and Snakes

Fishes swim by lateral undulation of the body: in anguilliform swimming the whole body takes part in the undulation, with a wavelength of about one body length; in carangiform swimming (such as mackerel and tuna) the undulation is concentrated in the posterior third of the body and the tail fin, and the front part hardly moves, which is better for high-speed cruising. The speed at which the body wave travels backward is always greater than the speed at which the fish advances, and the ratio of the two reflects the efficiency of propulsion. The serpentine movement of snakes on land is also a body wave traveling backward, but the snake needs to push sideways against projections on the ground to advance; on smooth surfaces, snakes use sideways sidewinding (the sidewinder rattlesnake, *Crotalus cerastes*, of North American deserts), concertina movement like an accordion, or rectilinear movement with the ventral scales. The walking of tetrapods (such as salamanders) retains the trunk undulation of fishes: salamanders swim with traveling waves in water and walk on land with standing-wave-like bending of the trunk together with the limbs, with the same spinal circuits switching between the two modes (Ijspeert et al., 2007, reproduced this transition with a salamander robot). From the swimming of the lamprey to the walking of tetrapods, the vertebrate locomotor CPG preserves its segmental structure and its core of **reciprocal inhibition**, and the limb CPGs evolved on this basis.

## Summary

| Topic | Key points |
|---|---|
| Hierarchy | spinal cord executes, brainstem maintains posture, cortex plans, cerebellum and basal ganglia correct; motor neurons are the final common path (Definition 44.1.1) |
| Motor neurons | α (Aα, motor unit, size principle), γ (Aγ, intrafusal), β; interneurons about 30-fold more numerous; recurrent inhibition by Renshaw cells |
| Muscle spindle (Definition 44.2.1) | in parallel with extrafusal fibers; nuclear bag (dynamic, static) and nuclear chain fibers; Ia primary endings report length and rate, II secondary endings mainly report length (Formula 44.2.1) |
| γ regulation (Definition 44.2.2) | dynamic γ enhances velocity sensitivity, static γ enhances length sensitivity; α–γ coactivation prevents unloading; gamma loop |
| Tendon organ (Definition 44.2.3) | in series with extrafusal fibers, Ib, senses active tension; autogenic inhibition, negative feedback on force, may become excitatory in walking |
| Stretch reflex (Definition 44.3.1) | monosynaptic, reciprocal inhibition of antagonists; tendon reflex and muscle tone; knee-jerk latency $15$–$20\,\mathrm{ms}$ (Example 44.3.1) |
| Closed loop (Formula 44.3.1) | negative feedback with delay, oscillates when the gain exceeds the critical value; the longer the delay, the lower the critical gain and the slower the oscillation; clonus about $5$–$8\,\mathrm{Hz}$ |
| Flexor and crossed extensor reflexes (Definitions 44.3.2, 44.3.3) | polysynaptic, reciprocal inhibition, afterdischarge increasing with stimulus strength, local sign; the crossed extensor reflex is $0.2$–$0.5\,\mathrm{s}$ later with longer afterdischarge |
| Spinal shock | reflexes vanish after transection, recover and become hyperactive after weeks |
| Spinal CPG | deafferented cat, spinal cat, intensity coding in the mesencephalic locomotor region, fictive locomotion; rhythm-generating and pattern-forming layers; V0 and other interneurons; sensory feedback adjusts phase |
| Brainstem | pontine reticulospinal tract excites, medullary reticulospinal tract inhibits, vestibulospinal tract excites antigravity muscles |
| Decerebrate rigidity (Definition 44.5.1) | transection between the colliculi; γ rigidity (abolished by dorsal root section) and α rigidity (cerebellar anterior lobe removed) |
| Postural reflexes (Definition 44.5.2) | labyrinthine tonic reflex, tonic neck reflex, righting reflex (midbrain) |
| Evolution | lamprey segmental lag about 1 % independent of frequency (coupled oscillators); gait transitions at energy minima, $Fr \approx 0.5$; local rules of the stick insect; body waves of fishes and snakes, the salamander transition |

## Questions

1. A person holds an empty box on the palm, and someone suddenly puts a book into the box. Describe what happens in turn in the muscle spindles, tendon organs, and spinal reflexes of the biceps brachii during the next $100\,\mathrm{ms}$.

   **Answer** The weight of the book makes the forearm sink and suddenly stretches the biceps, and the firing of the spindles (especially the dynamic response of the Ia primary endings) jumps; the Ia signals excite the α motor neurons of the biceps monosynaptically (a short-latency reflex electromyogram appears about $20$–$30\,\mathrm{ms}$ later) and at the same time inhibit the antagonist triceps through Ia inhibitory interneurons (reciprocal inhibition). Then, about $50$–$100\,\mathrm{ms}$ later, a long-latency reflex through the cortex appears and strengthens the contraction further. As the biceps contracts and its tension rises, Ib firing of the tendon organs increases and limits excessive rise of tension through autogenic inhibition, so that force rises smoothly to the level needed to support the book. At the same time α–γ coactivation keeps the spindles from being unloaded when the muscle shortens again, so that they continue to report length.

2. In Formula 44.3.1, why does increasing the reflex gain resist perturbations more effectively but also bring oscillation? By what means can the nervous system strike a balance between the two?

   **Answer** The larger the gain $G$, the larger the restoring torque for the same deviation, the smaller the steady-state error, and the more effective the resistance to perturbations. But the reflex signal acts only after the loop delay $T$, and an oscillation of frequency $\omega$ is delayed in phase by $\omega T$ around the loop; when the total phase lag reaches $180^\circ$, the "negative" feedback becomes **positive feedback**, and if the loop gain is then greater than 1 the oscillation grows. Possible means: using velocity feedback (the dynamic response of Ia, equivalent to phase lead, the $\tau_{\mathrm{v}}$ term in the equation) to compensate part of the delay; adjusting the gain with the task (the output of γ motor neurons, presynaptic inhibition, and the gain of the long-latency reflex change with the task); using the **viscoelasticity** of the muscle itself and cocontraction to increase passive stiffness and damping (unaffected by neural delay); and having the cerebellum provide feedforward prediction based on internal models instead of relying only on delayed feedback ([7.14.45](/7.14.45)).

3. The extensor rigidity of a decerebrate cat disappears after the dorsal roots of the hindlimb are cut. What would be the result if the anterior lobe of the cerebellum were removed first and the dorsal roots cut afterward? What does this show?

   **Answer** After removal of the anterior lobe of the cerebellum the rigidity is worsened and is no longer abolished by cutting the dorsal roots. The reason is that the anterior lobe normally inhibits α motor neurons through the vestibular nuclei and other routes; after its removal the vestibulospinal tract excites α motor neurons directly, forming an α rigidity that does not depend on spindle afferents. This shows that classical decerebrate rigidity is mainly γ rigidity: descending facilitation acts on γ motor neurons and makes the stretch reflex excessive through the gamma loop; what appears after cerebellar damage is a different mechanism.

4. Estimate the speed at which a horse with a leg length of $1.5\,\mathrm{m}$ and a dog with a leg length of $0.15\,\mathrm{m}$ change from walking to running. Why is it reasonable to compare animals of different sizes using the Froude number?

   **Answer** From $Fr = v^2/(gl) \approx 0.5$, the horse has $v \approx \sqrt{0.5 \times 9.8 \times 1.5} \approx 2.7\,\mathrm{m\,s^{-1}}$ and the small dog $v \approx \sqrt{0.5 \times 9.8 \times 0.15} \approx 0.86\,\mathrm{m\,s^{-1}}$. The mechanics of walking is determined by the ratio of the inertial force (the centripetal acceleration related to $v^2/l$) to gravity $g$; two movements with the same Froude number have the same relative importance of inertia and gravity, so in geometrically similar bodies the form of movement (ratio of stride length to leg length, phase relationships, the way energy is exchanged) is also similar, that is, dynamically similar. This is the same as using the **Reynolds number** to compare swimmers of different sizes ([7.6.22](/7.6.22)).

5. (Open question) The lamprey uses a central chain of segmental oscillators to generate the traveling wave of swimming, and the stick insect coordinates walking with local feedback rules between legs. Compare the advantages and disadvantages of the two strategies and explain why a fast-running cockroach resembles the former more.

   **Answer** Key points: the rhythm generated by a central oscillator chain is robust, does not depend on the delay of sensory feedback, and can maintain fixed coordination (constant phase lag) over a wide range of frequencies, which suits strongly periodic movements in a not very variable environment (swimming in water); the disadvantage is that adaptation to terrain and unexpected perturbations requires additional feedback regulation. Local feedback rules distribute coordination among the legs and are naturally adaptive to irregular terrain and to obstructed or missing legs, with no need for a central model; the disadvantage is the dependence on sensory information, which has a delay, so the faster the movement, the less time the feedback has. When a cockroach runs at a dozen or so steps per second, each step lasts only a few tens of milliseconds, and the delay of neural feedback already takes up a considerable part of it, so it depends more on a central feedforward rhythm and on the mechanical stability of the body itself (the elasticity of the legs makes the body self-stabilizing against perturbations), and leaves feedback for slow adjustments. This agrees with the analysis of the stretch reflex in this chapter: delay limits what feedback can do.
