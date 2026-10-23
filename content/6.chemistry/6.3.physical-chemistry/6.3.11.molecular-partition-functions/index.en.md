---
title: Molecular Partition Functions and Ideal-Gas Properties
description: Factorization of the molecular partition function into translational, rotational, vibrational, electronic and nuclear parts; thermal wavelength, rotational and vibrational characteristic temperatures, symmetry number and the correction series for the rotational partition function; internal energy, heat capacity and the Einstein function of an ideal gas; the Sackur–Tetrode equation and statistical entropy, comparison with calorimetric entropy, and residual entropy; vapor pressure from statistical entropy; standard equilibrium constants from partition functions (dissociation of I₂, H₂ + D₂ exchange).
source_hash: ff8d20e5cc4f
---

The previous chapter ([6.3.10](/6.3.10)) set up the framework of statistical thermodynamics: once the energy levels of a molecule are known, we can compute the **molecular partition function** $q$, and from the system partition function $Z = q^N/N!$ all the thermodynamic functions of an ideal gas. This chapter carries the program through. The energy of a molecule can be approximately decomposed into translational, rotational, vibrational, electronic and nuclear parts, and $q$ factorizes accordingly into five factors. Each factor can be computed from the mass, moments of inertia, vibrational frequencies and electronic levels of the molecule, all of which come from spectroscopy ([5.5.5](/5.5.5#sec-5.3)). The results explain how heat capacities vary with temperature (when the equipartition theorem holds, and why vibrations are "frozen out" at ordinary temperatures), give statistical entropies that are independent of calorimetry and often more accurate, and reveal the origin of residual entropy. The last section computes standard equilibrium constants directly from partition functions. This connects the $K^\circ$ of [6.3.7](/6.3.7) with molecular structure and is the starting point of transition state theory in [6.3.16](/6.3.16).

The molecular energy levels used here come from quantum physics: the particle in a box and the quantum harmonic oscillator ([5.5.3](/5.5.3)), electron spin and term symbols ([5.5.4](/5.5.4)), and the rotational and vibrational levels of diatomic molecules ([5.5.5](/5.5.5#sec-5.3)). Following the conventions of molecular spectroscopy and chemistry, the rotational quantum number is written $J$, the moment of inertia $I$ and the vibrational quantum number $v$ ([Remark 5.3.1 of 5.5.5](/5.5.5#rem-5.3.1)). The partition function of each mode of motion takes the ground state of that mode as the zero of energy, and the energy $U_0$ at $0\,\mathrm{K}$ is written explicitly where needed ([6.3.10](/6.3.10#sec-10.4.3)). Numerical constants are taken from CODATA 2022, and spectroscopic constants from the literature.

## 11.1. Factorization of the Partition Function

Write the energy of a molecule as the sum of the energies of the various motions, and its degeneracy as the product of the individual degeneracies:

$$
\varepsilon_i = \varepsilon_{\mathrm{t}} + \varepsilon_{\mathrm{r}} + \varepsilon_{\mathrm{v}} + \varepsilon_{\mathrm{e}} + \varepsilon_{\mathrm{n}}, \qquad g_i = g_{\mathrm{t}}\,g_{\mathrm{r}}\,g_{\mathrm{v}}\,g_{\mathrm{e}}\,g_{\mathrm{n}}.
$$
Translation is the motion of the center of mass (external motion); the other four are internal motions. This decomposition is approximate: the Born–Oppenheimer approximation separates electronic and nuclear motion ([5.5.5](/5.5.5#sec-5.3.1)), the rigid-rotor and harmonic-oscillator models neglect the coupling of rotation and vibration and the anharmonicity of vibration, and in homonuclear molecules the nuclear spin is coupled to rotation (Section 11.5). Within these approximations we have

**Theorem 11.1.1** The molecular partition function is the product of the partition functions of the individual motions:

$$
q = q_{\mathrm{t}}\,q_{\mathrm{r}}\,q_{\mathrm{v}}\,q_{\mathrm{e}}\,q_{\mathrm{n}}, \qquad q_{\mathrm{t}} = \sum_{\mathrm{t}} g_{\mathrm{t}}\,\mathrm{e}^{-\varepsilon_{\mathrm{t}}/(k_{\mathrm{B}}T)},\ \dots
\tag{11.1}
$$

**Proof** A level of the molecule is an independent combination of levels $(i_{\mathrm{t}}, i_{\mathrm{r}}, \dots)$ of the individual motions. The exponential turns the sum into a product, and a multiple sum over independent indices is the product of the separate sums:

$$
q = \sum_{i_{\mathrm{t}}}\sum_{i_{\mathrm{r}}}\cdots\ g_{\mathrm{t}}g_{\mathrm{r}}\cdots\ \mathrm{e}^{-(\varepsilon_{\mathrm{t}} + \varepsilon_{\mathrm{r}} + \cdots)/(k_{\mathrm{B}}T)} = \left(\sum_{i_{\mathrm{t}}} g_{\mathrm{t}}\mathrm{e}^{-\varepsilon_{\mathrm{t}}/(k_{\mathrm{B}}T)}\right)\left(\sum_{i_{\mathrm{r}}} g_{\mathrm{r}}\mathrm{e}^{-\varepsilon_{\mathrm{r}}/(k_{\mathrm{B}}T)}\right)\cdots. \qquad \square
$$

Hence $\ln q$ is a sum of terms, and $U$ and $C_V$, obtained from derivatives of $\ln q$, are sums of the contributions of the individual motions. The entropy and the Helmholtz energy contain in addition the term $-k_{\mathrm{B}}\ln N!$, which arises from the indistinguishability of the molecules. Molecules can exchange positions only because of translation, so by convention this term is assigned to the translational part:

$$
\ln\frac{q^N}{N!} = \ln\frac{q_{\mathrm{t}}^N}{N!} + N\ln q_{\mathrm{r}} + N\ln q_{\mathrm{v}} + N\ln q_{\mathrm{e}} + N\ln q_{\mathrm{n}}.
$$

The level spacings of the various motions differ enormously, and this determines how each partition function is evaluated (compared with $k_{\mathrm{B}}T$ at $298\,\mathrm{K}$, taking $\ce{N2}$ as an example):

| Motion | Level spacing / $k_{\mathrm{B}}T$ | Treatment | State at room temperature |
|---|---|---|---|
| Translation ($10\,\mathrm{cm}$ container) | $\sim10^{-19}$ | Replace the sum by an integral | Very many levels populated |
| Rotation | $2\Theta_{\mathrm{r}}/T \approx 0.02$ | Usually an integral is adequate (exceptions such as $\ce{H2}$) | Very many levels populated |
| Vibration | $\Theta_{\mathrm{v}}/T \approx 11$ | The sum must be kept (geometric series) | Almost all in the ground state |
| Electronic | $\gtrsim 10^2$ | Usually the ground state only | Ground state (a few exceptions) |
| Nuclear | $\gg 10^5$ | Ground state only | Ground state |

## 11.2. The Translational Partition Function

The levels of a particle in a one-dimensional box are $\varepsilon_{\mathrm{t}} = \frac{h^2}{8ma^2}n_x^2$, $n_x = 1, 2, \dots$, and none of them is degenerate ([5.5.3](/5.5.3#sec-3.2.2)). Let $\lambda^2 = \frac{h^2}{8mk_{\mathrm{B}}Ta^2}$. For a macroscopic container $\lambda \sim 10^{-10}$, adjacent terms are almost equal, and the sum can be replaced by an integral (starting the integral at $0$ rather than $1$ changes the result only by a relative error of order $\lambda$):

$$
q_{\mathrm{t},x} = \sum_{n_x = 1}^{\infty}\mathrm{e}^{-\lambda^2n_x^2} \approx \int_0^{\infty}\mathrm{e}^{-\lambda^2n_x^2}\,\mathrm{d}n_x = \frac{\sqrt{\pi}}{2\lambda} = \frac{(2\pi mk_{\mathrm{B}}T)^{1/2}}{h}\,a,
$$
where the last step uses the **Gaussian integral** ([2.2.12](/2.2.12#sec-12.2.5)). The three-dimensional translational levels (10.1) are sums over the three directions, so the partition function is the product of three one-dimensional ones (the same argument as in Theorem 11.1.1), and $abc = V$:

**Formula 11.2.1 (Translational Partition Function)**

$$
q_{\mathrm{t}} = \left(\frac{2\pi mk_{\mathrm{B}}T}{h^2}\right)^{3/2}V = \frac{V}{\Lambda^3}.
\tag{11.2}
$$

**Definition 11.2.1** The length

$$
\Lambda = \frac{h}{\sqrt{2\pi mk_{\mathrm{B}}T}}
$$
is called the **thermal wavelength** (thermal de Broglie wavelength) of the molecule.

$\Lambda$ is roughly the de Broglie wavelength of a molecule with thermal kinetic energy, and $q_{\mathrm{t}} = V/\Lambda^3$ can be read as "the number of small cubes of edge $\Lambda$ that fit in the container". The condition $g_i \gg N_i$ of Section 10.2.3 is equivalent to $N/q_{\mathrm{t}} = N\Lambda^3/V \ll 1$: when the mean distance between molecules is much larger than the thermal wavelength, quantum effects can be ignored and Boltzmann statistics applies.

**Example 11.2.1** Compute the translational partition function of $1\,\mathrm{mol}$ of $\ce{N2}$ at $298.15\,\mathrm{K}$ and $p^\circ = 10^5\,\mathrm{Pa}$.

**Solution** $m = 28.013\,\mathrm{u} = 4.652\times10^{-26}\,\mathrm{kg}$, $\Lambda = h/\sqrt{2\pi mk_{\mathrm{B}}T} = 1.91\times10^{-11}\,\mathrm{m} = 19.1\,\mathrm{pm}$, $V = RT/p^\circ = 2.479\times10^{-2}\,\mathrm{m^3}$, so

$$
q_{\mathrm{t}} = \frac{V}{\Lambda^3} = 3.56\times10^{30}, \qquad \frac{q_{\mathrm{t}}}{N_{\mathrm{A}}} = 5.9\times10^6 \gg 1.
$$
(Many textbooks take $V = 0.0245\,\mathrm{m^3}$, which corresponds to the old standard pressure of $101.325\,\mathrm{kPa}$ rather than the current $p^\circ$.) Each molecule has on average about $6\times10^6$ accessible translational quantum states, so Boltzmann statistics applies fully. By contrast, the conduction electrons in a metal have a small mass and a high number density, $N\Lambda^3/V \sim 10^3$, and require Fermi–Dirac statistics ([5.5.6](/5.5.6)).

From $\ln q_{\mathrm{t}} = \frac{3}{2}\ln T + \ln V + \text{const}$, the translational contributions to the internal energy and heat capacity are

$$
U_{\mathrm{t}} = Nk_{\mathrm{B}}T^2\left(\frac{\partial\ln q_{\mathrm{t}}}{\partial T}\right)_V = \frac{3}{2}Nk_{\mathrm{B}}T, \qquad C_{V,\mathrm{t}} = \frac{3}{2}Nk_{\mathrm{B}},
$$
in agreement with the **equipartition theorem** ([5.2.1](/5.2.1)): the translational levels are extremely close together, and translation is completely "classical".

## 11.3. The Rotational Partition Function

### 11.3.1. Heteronuclear Diatomic Molecules

Treat a diatomic molecule as a rigid rotor with moment of inertia $I = \mu r_{\mathrm{e}}^2$ ($\mu$ is the **reduced mass**). The energy levels and degeneracies are ([Formula 5.3.1 of 5.5.5](/5.5.5#fml-5.3.1))

$$
\varepsilon_{\mathrm{r}} = J(J + 1)\frac{h^2}{8\pi^2I}, \qquad g_{\mathrm{r}} = 2J + 1, \qquad J = 0, 1, 2, \dots
$$
The degeneracy comes from the orientation of the angular momentum in space: the quantum number of its $z$ component is $m_J = -J, -J + 1, \dots, J$, a total of $2J + 1$ values.

**Definition 11.3.1** The quantity

$$
\Theta_{\mathrm{r}} = \frac{h^2}{8\pi^2Ik_{\mathrm{B}}} = \frac{hc\tilde B}{k_{\mathrm{B}}}
$$
is called the **characteristic rotational temperature** of the molecule; $\tilde B = h/(8\pi^2cI)$ is the rotational constant expressed as a wavenumber.

Thus $q_{\mathrm{r}} = \sum_{J}(2J + 1)\mathrm{e}^{-J(J + 1)\Theta_{\mathrm{r}}/T}$. Except for very light molecules such as $\ce{H2}$ and $\ce{HD}$, $\Theta_{\mathrm{r}} \ll T$ at ordinary temperatures, and the sum can be replaced by an integral: with $x = J(J + 1)$, $\mathrm{d}x = (2J + 1)\,\mathrm{d}J$,

$$
q_{\mathrm{r}} \approx \int_0^\infty \mathrm{e}^{-x\Theta_{\mathrm{r}}/T}\,\mathrm{d}x = \frac{T}{\Theta_{\mathrm{r}}} = \frac{8\pi^2Ik_{\mathrm{B}}T}{h^2} \qquad (\text{heteronuclear},\ T \gg \Theta_{\mathrm{r}}).
\tag{11.3}
$$

Characteristic temperatures of common diatomic molecules (computed from the ground-state rotational constant $\tilde B_0$ and the fundamental vibrational wavenumber $\tilde\nu$; for $\Theta_{\mathrm{v}}$ see Section 11.4):

| Molecule | $\ce{H2}$ | $\ce{N2}$ | $\ce{O2}$ | $\ce{CO}$ | $\ce{HCl}$ | $\ce{I2}$ |
|---|---|---|---|---|---|---|
| $\tilde B_0/\mathrm{cm^{-1}}$ | 59.32 | 1.990 | 1.438 | 1.923 | 10.44 | 0.0374 |
| $\Theta_{\mathrm{r}}/\mathrm{K}$ | 85.3 | 2.86 | 2.07 | 2.77 | 15.0 | 0.054 |
| $\tilde\nu/\mathrm{cm^{-1}}$ | 4161 | 2330 | 1556 | 2143 | 2886 | 214.5* |
| $\Theta_{\mathrm{v}}/\mathrm{K}$ | 5987 | 3352 | 2239 | 3084 | 4152 | 308 |

(* For $\ce{I2}$ the harmonic constant $\tilde\omega_{\mathrm{e}}$ is used; the fundamental, $213.3\,\mathrm{cm^{-1}}$, gives $307\,\mathrm{K}$.)

### 11.3.2. The Symmetry Number

After a homonuclear diatomic molecule ($\ce{N2}$, $\ce{O2}$) is rotated by $180^\circ$ about an axis perpendicular to the bond, it is indistinguishable from its original configuration. Classically, the integral in Eq. (11.3) counts each distinguishable orientation twice. In quantum mechanics, the exchange symmetry of the nuclei gives the even-$J$ and odd-$J$ levels of $\ce{N2}$ different nuclear-spin weights, and for $T \gg \Theta_{\mathrm{r}}$ the net effect is to halve the sum (Section 11.5). In general,

**Definition 11.3.2** The number of indistinguishable spatial orientations that a molecule can reach by (proper) rotations is called its **symmetry number**, denoted $\sigma$.

$$
q_{\mathrm{r}} = \frac{T}{\sigma\Theta_{\mathrm{r}}} = \frac{8\pi^2Ik_{\mathrm{B}}T}{\sigma h^2} \qquad (\text{linear molecules},\ T \gg \Theta_{\mathrm{r}}).
\tag{11.4}
$$
For heteronuclear diatomic molecules and $\ce{N2O}$ ($\ce{NNO}$), $\sigma = 1$; for homonuclear diatomic molecules and $\ce{CO2}$, $\sigma = 2$. Among nonlinear molecules, $\sigma = 2$ for $\ce{H2O}$ and $\ce{SO2}$, 3 for $\ce{NH3}$, and 12 for $\ce{CH4}$ and $\ce{C6H6}$. The value of $\sigma$ equals the number of pure rotations (including the identity) in the point group of the molecule, and can be found systematically by group theory.

**Example 11.3.1** For $\ce{N2}$, $\Theta_{\mathrm{r}} = 2.86\,\mathrm{K}$ ($I = h^2/(8\pi^2k_{\mathrm{B}}\Theta_{\mathrm{r}}) = 1.41\times10^{-46}\,\mathrm{kg\,m^2}$), and at $298.15\,\mathrm{K}$

$$
q_{\mathrm{r}} = \frac{298.15}{2\times2.86} = 52.1.
$$
The rotational entropy of $\ce{N2}$, $41.18\,\mathrm{J\,mol^{-1}\,K^{-1}}$, in the table of Section 11.6.2 is computed from this value.

### 11.3.3. Sum versus Integral: the Correction Series

When $\Theta_{\mathrm{r}}/T$ is not very small, the integral approximation (11.3) is too low. Treating the sum with the Euler–Maclaurin formula gives the Mulholland expansion

$$
q_{\mathrm{r}} = \frac{T}{\sigma\Theta_{\mathrm{r}}}\left[1 + \frac{1}{3}\frac{\Theta_{\mathrm{r}}}{T} + \frac{1}{15}\left(\frac{\Theta_{\mathrm{r}}}{T}\right)^2 + \frac{4}{315}\left(\frac{\Theta_{\mathrm{r}}}{T}\right)^3 + \cdots\right].
\tag{11.5}
$$
For $\ce{HCl}$ ($\Theta_{\mathrm{r}} = 15.0\,\mathrm{K}$) at $298.15\,\mathrm{K}$, exact summation gives $q_{\mathrm{r}} = 20.19$, the integral approximation gives $19.85$ (low by $1.7\%$, mainly because of the second term, $\frac{1}{3}$), and Eq. (11.5) gives $20.19$. For $T \lesssim \Theta_{\mathrm{r}}$ the series fails and the sum must be done directly; in this temperature range homonuclear molecules also require consideration of nuclear spin (Section 11.5).

![Left: rotational partition function of HCl; ratio of the integral approximation T/Θr and of the Mulholland expansion (four terms) to the exact sum, as a function of T/Θr. Right: rotational level populations of HCl and CO at 298.15 K, with the maximum at J ≈ (T/2Θr)^½ − ½](./plots/rotational-partition-function.py)

By the Boltzmann distribution, the fraction of molecules in rotational level $J$ is $(2J + 1)\mathrm{e}^{-J(J + 1)\Theta_{\mathrm{r}}/T}/q_{\mathrm{r}}$, which is largest at $J_{\max} \approx \sqrt{T/(2\Theta_{\mathrm{r}})} - \frac{1}{2}$: at $298\,\mathrm{K}$ this is $J = 3$ for $\ce{HCl}$ and $J = 7$ for $\ce{CO}$. This is the origin of the intensity distribution of the P and R branches in infrared vibration–rotation spectra ([5.5.5](/5.5.5#sec-5.3.3)).

### 11.3.4. Nonlinear Molecules

A nonlinear molecule rotates about three principal axes, with principal moments of inertia $I_A$, $I_B$, $I_C$ and corresponding characteristic temperatures $\Theta_X = h^2/(8\pi^2I_Xk_{\mathrm{B}})$. At high temperatures

$$
q_{\mathrm{r}} = \frac{\sqrt{\pi}}{\sigma}\left(\frac{T^3}{\Theta_A\Theta_B\Theta_C}\right)^{1/2} = \frac{\sqrt{\pi}}{\sigma}\left(\frac{8\pi^2k_{\mathrm{B}}T}{h^2}\right)^{3/2}\left(I_AI_BI_C\right)^{1/2}.
\tag{11.6}
$$
For example, the rotational constants of $\ce{H2O}$ are $27.88$, $14.51$ and $9.28\,\mathrm{cm^{-1}}$, so $\Theta = 40.1$, $20.9$ and $13.4\,\mathrm{K}$; with $\sigma = 2$, $q_{\mathrm{r}} \approx 43$ at $298.15\,\mathrm{K}$.

Since $q_{\mathrm{r}} \propto T$ (linear) or $T^{3/2}$ (nonlinear), the rotational internal energy at high temperature is $Nk_{\mathrm{B}}T$ or $\frac{3}{2}Nk_{\mathrm{B}}T$, in agreement with the equipartition theorem.

## 11.4. The Vibrational Partition Function

The vibration of a diatomic molecule is treated as harmonic, with the levels of the **quantum harmonic oscillator** ([5.5.3](/5.5.3#sec-3.4.2)), which are nondegenerate:

$$
\varepsilon_{\mathrm{v}} = \left(v + \frac{1}{2}\right)h\nu, \qquad g_{\mathrm{v}} = 1, \qquad v = 0, 1, 2, \dots
$$

**Definition 11.4.1** The quantity $\Theta_{\mathrm{v}} = h\nu/k_{\mathrm{B}} = hc\tilde\nu/k_{\mathrm{B}}$ is called the **characteristic vibrational temperature** of the molecule.

The vibrational levels are equally spaced, and the spacing is large (the table of Section 11.3.1: $\Theta_{\mathrm{v}}$ is several thousand kelvin), so the sum cannot be replaced by an integral, but it is a geometric series. Taking the minimum of the potential-energy curve as the zero, the *vibrational partition function* is

$$
q_{\mathrm{v}} = \sum_{v = 0}^\infty\mathrm{e}^{-(v + 1/2)\Theta_{\mathrm{v}}/T} = \frac{\mathrm{e}^{-\Theta_{\mathrm{v}}/(2T)}}{1 - \mathrm{e}^{-\Theta_{\mathrm{v}}/T}};
$$
taking the vibrational ground state ($v = 0$) as the zero, with the zero-point energy $\frac{1}{2}h\nu$ absorbed into $U_0$,

$$
q_{\mathrm{v}}^{(0)} = \frac{1}{1 - \mathrm{e}^{-\Theta_{\mathrm{v}}/T}}.
\tag{11.7}
$$
The latter is more commonly used.

**Example 11.4.1** The fundamental vibrational wavenumber of $\ce{N2}$ is $\tilde\nu = 2329.9\,\mathrm{cm^{-1}}$, so $\Theta_{\mathrm{v}} = 3352\,\mathrm{K}$. At $298.15\,\mathrm{K}$, $\Theta_{\mathrm{v}}/T = 11.24$ and $q_{\mathrm{v}}^{(0)} = 1.000013$; only a fraction $1.3\times10^{-5}$ of the molecules is in $v = 1$. The vibration of $\ce{N2}$ is almost completely "frozen" at ordinary temperatures.

If the harmonic constant of $\ce{N2}$, $\tilde\omega_{\mathrm{e}} = 2358.6\,\mathrm{cm^{-1}}$, is used instead, $\Theta_{\mathrm{v}} = 3394\,\mathrm{K}$, slightly higher than the value from the fundamental. Both choices appear in the literature, so values of $\Theta_{\mathrm{v}}$ from different sources often differ slightly. When the harmonic-oscillator model is used for a real molecule, taking the measured fundamental (the $v = 0 \to 1$ spacing) makes the most important low-lying spacing correct, and this chapter always uses the fundamental. The two choices differ appreciably only at high temperatures, where anharmonicity itself must also be taken into account.

A polyatomic molecule has several vibrational modes. $n$ atoms have $3n$ degrees of freedom; subtracting 3 translations and 3 rotations (2 for a linear molecule) leaves $3n - 6$ ($3n - 5$ for linear) **normal modes**, each an independent harmonic oscillator:

$$
q_{\mathrm{v}}^{(0)} = \prod_{j = 1}^{3n - 6\ (3n - 5)}\frac{1}{1 - \mathrm{e}^{-\Theta_{\mathrm{v},j}/T}}.
$$
Low-frequency bending vibrations contribute most to thermodynamic properties at room temperature, for example the doubly degenerate bending vibration of $\ce{CO2}$ at $667\,\mathrm{cm^{-1}}$ ($\Theta_{\mathrm{v}} = 960\,\mathrm{K}$).

## 11.5. The Electronic and Nuclear Partition Functions

There is no general formula for electronic levels. For most molecules the first excited state lies several $\mathrm{eV}$ above the ground state, $\Delta\varepsilon/(k_{\mathrm{B}}T) \gtrsim 10^2$. Taking the ground state as the zero,

$$
q_{\mathrm{e}} = g_{\mathrm{e},0} + g_{\mathrm{e},1}\mathrm{e}^{-\Delta\varepsilon_1/(k_{\mathrm{B}}T)} + \cdots \approx g_{\mathrm{e},0}.
$$
The degeneracy of the ground state is determined by the electronic state:

- Atoms: $g_{\mathrm{e},0} = 2J + 1$, where $J$ is the total angular momentum quantum number of the ground-state **term symbol** $^{2S+1}L_J$ ([5.5.4](/5.5.4#sec-4.2.4)). For example, it is 1 for He and Ar ($^1\mathrm{S}_0$), 2 for Na ($^2\mathrm{S}_{1/2}$), 4 for the halogen atoms ($^2\mathrm{P}_{3/2}$) and 5 for the O atom ($^3\mathrm{P}_2$).
- Molecules: for a $\Sigma$ state, in which the component of orbital angular momentum along the bond axis is zero, $g_{\mathrm{e},0} = 2S + 1$ ($S$ is the total spin quantum number). It is 1 for closed-shell molecules, 2 for radicals with one unpaired electron, and 3 for $\ce{O2}$ ($^3\Sigma_{\mathrm{g}}^-$). For $\Pi$, $\Delta$ and similar states there is an additional twofold orbital degeneracy.

The common rule of thumb "$g_{\mathrm{e},0} = n + 1$ ($n$ the number of unpaired electrons)" holds only for $\Sigma$ states ($S = n/2$), and only when the excited states are sufficiently high. $\ce{NO}$ is a counterexample:

**Example 11.5.1** The ground state of $\ce{NO}$ is $^2\Pi_{1/2}$ ($g = 2$), and spin–orbit coupling places $^2\Pi_{3/2}$ ($g = 2$) only $119.8\,\mathrm{cm^{-1}}$ ($172\,\mathrm{K}$) higher. At $298.15\,\mathrm{K}$

$$
q_{\mathrm{e}} = 2 + 2\,\mathrm{e}^{-172/298.15} = 3.12,
$$
not 2. This pair of levels gives the heat capacity of $\ce{NO}$ a Schottky-type peak near $70\,\mathrm{K}$ ([Example 10.3.1 of 6.3.10](/6.3.10#ex-10.3.1)). The $^2\mathrm{P}_{1/2}$ excited state of the halogen atoms (for the iodine atom, $7603\,\mathrm{cm^{-1}}$ higher) contributes less than $10^{-4}$ even at $1000\,\mathrm{K}$ and can be neglected.

Nuclear excitation energies are of the order of $\mathrm{MeV}$, and except in nuclear reactions nuclei are always in their ground states. Taking the ground state as the zero, the nuclear partition function is just the nuclear-spin degeneracy:

$$
q_{\mathrm{n}} = \prod_k(2s_k + 1),
$$
where $s_k$ is the spin quantum number of the $k$th nucleus in the molecule. Nuclei with even numbers of both protons and neutrons have $s = 0$ ($^{12}\mathrm{C}$, $^{16}\mathrm{O}$, $^{32}\mathrm{S}$); when one is odd and the other even, $s$ is a half-integer ($\frac{1}{2}$ for $^1\mathrm{H}$, $^{13}\mathrm{C}$, $^{31}\mathrm{P}$; $\frac{3}{2}$ for $^7\mathrm{Li}$, $^{11}\mathrm{B}$, $^{35}\mathrm{Cl}$); when both are odd, $s$ is an integer (1 for $^2\mathrm{H}$, $^6\mathrm{Li}$, $^{14}\mathrm{N}$). Nuclei with $s \neq 0$ are the subject of nuclear magnetic resonance. Chemical reactions do not change the nuclei, so the product of the $q_{\mathrm{n}}$ is the same before and after reaction and cancels in equilibrium constants and reaction entropies; it is therefore usually omitted.

The exception is homonuclear diatomic molecules at low temperature. The two protons of $\ce{H2}$ are fermions, and the total wave function must be antisymmetric under exchange of the two nuclei. The nuclear-spin triplet (weight 3) can combine only with odd $J$, and this form of $\ce{H2}$ is called *orthohydrogen*; the nuclear-spin singlet (weight 1) can combine only with even $J$, and is called *parahydrogen*. At high temperature the rotational sums over odd and even $J$ are each about half of the total sum, and $q_{\mathrm{r}}q_{\mathrm{n}} \approx (3 + 1)\cdot\frac{1}{2}\cdot\frac{T}{\Theta_{\mathrm{r}}}$, which is exactly the effect of a symmetry number $\sigma = 2$ together with $q_{\mathrm{n}} = 4$. At low temperature the two forms of $\ce{H2}$ must be computed separately. Without a catalyst their interconversion is extremely slow, and ordinary hydrogen gas at low temperature is a metastable $3:1$ mixture of ortho- and parahydrogen, whose heat capacity differs from the value calculated for equilibrium (see the discussion of the heat capacity of $\ce{H2}$ in [5.2.3](/5.2.3)).

## 11.6. Thermodynamic Properties of Ideal Gases

### 11.6.1. Internal Energy and Heat Capacity

From $U = Nk_{\mathrm{B}}T^2(\partial\ln q/\partial T)_V + U_0$ and the individual partition functions, the internal energy of $1\,\mathrm{mol}$ of an ideal gas is

$$
U_{\mathrm{m}} = U_{0,\mathrm{m}} + \frac{3}{2}RT + \underbrace{RT\ \text{or}\ \frac{3}{2}RT}_{\text{rotation, linear or nonlinear}} + \sum_j\frac{R\Theta_{\mathrm{v},j}}{\mathrm{e}^{\Theta_{\mathrm{v},j}/T} - 1} + U_{\mathrm{e},\mathrm{m}},
\tag{11.8}
$$
where the vibrational term comes from differentiating $\ln q_{\mathrm{v}}^{(0)} = -\ln(1 - \mathrm{e}^{-\Theta_{\mathrm{v}}/T})$. Every term depends only on $T$: the $U$ of an ideal gas is a function of temperature alone, while its specific form is determined by the structure of the molecule ($\Theta_{\mathrm{v}}$, etc.). Differentiating with respect to $T$, for a monatomic gas $C_{V,\mathrm{m}} = \frac{3}{2}R$ (valid at any temperature as long as electronic excited states can be neglected); for a diatomic gas

$$
C_{V,\mathrm{m}} = \frac{5}{2}R + R\,\frac{(\Theta_{\mathrm{v}}/T)^2\,\mathrm{e}^{\Theta_{\mathrm{v}}/T}}{\left(\mathrm{e}^{\Theta_{\mathrm{v}}/T} - 1\right)^2} \qquad (T \gg \Theta_{\mathrm{r}}).
\tag{11.9}
$$
The function $E(x) = x^2\mathrm{e}^x/(\mathrm{e}^x - 1)^2$ ($x = \Theta_{\mathrm{v}}/T$) in the vibrational term is called the *Einstein function*; in 1907 Einstein used it to explain the decrease of the heat capacity of solids at low temperature. Its two limits show where the equipartition theorem applies:

- $T \ll \Theta_{\mathrm{v}}$ ($x \gg 1$): $E(x) \approx x^2\mathrm{e}^{-x} \to 0$, vibration is "frozen", and a diatomic gas has $C_{V,\mathrm{m}} = \frac{5}{2}R$. Most diatomic gases are in this regime at ordinary temperatures ([6.3.1](/6.3.1)).
- $T \gg \Theta_{\mathrm{v}}$ ($x \to 0$): $E(x) \to 1$, each vibrational mode contributes $R$ (kinetic and potential energy $\frac{1}{2}R$ each), and $C_{V,\mathrm{m}} \to \frac{7}{2}R$, the result of the equipartition theorem.

The equipartition theorem holds only when the level spacing is much smaller than $k_{\mathrm{B}}T$; this is the most direct manifestation of quantum energy levels in thermodynamics ([5.5.3](/5.5.3#sec-3.4.2), [5.2.3](/5.2.3)). For example, for $\ce{N2}$ at $1000\,\mathrm{K}$, $E(3.35) = 0.42$ and $C_{V,\mathrm{m}} = 24.30\,\mathrm{J\,mol^{-1}\,K^{-1}}$, compared with the measured value ($C_{p,\mathrm{m}} - R$) of $24.39\,\mathrm{J\,mol^{-1}\,K^{-1}}$; the remaining difference comes from anharmonicity and vibration–rotation coupling. For heavy molecules with low $\Theta_{\mathrm{v}}$ ($\ce{I2}$, $\ce{Br2}$), vibration is already considerably excited at room temperature.

![Left: CV,m/R of ideal-gas HCl and its translational, rotational and vibrational contributions (rigid-rotor–harmonic-oscillator model, rotation by exact summation), with dotted lines marking Θr and Θv. Right: vibrational contribution (Einstein function) for I₂, N₂ and HCl; the vertical line is 298.15 K](./plots/heat-capacity-contributions.py)

In the figure the rotational heat capacity is slightly above $R$ near $T \approx 0.8\,\Theta_{\mathrm{r}}$, an effect of the discreteness of the levels. In reality $\ce{HCl}$ has long since condensed at this temperature, and only $\ce{H2}$ and $\ce{D2}$ can be observed in the gas phase to show changes of the rotational heat capacity.

### 11.6.2. Statistical Entropy

**Definition 11.6.1** The entropy computed through partition functions from the spectroscopic data of a molecule (mass, moments of inertia, vibrational frequencies, electronic levels) is called the **statistical entropy** (spectroscopic entropy).

From $S = k_{\mathrm{B}}\ln(q^N/N!) + U/T$, the statistical entropy can be decomposed into translational, rotational, vibrational and electronic contributions (the nuclear-spin contribution is omitted in chemistry, Section 11.5). The translational entropy includes $\ln N!$:

$$
S_{\mathrm{t}} = k_{\mathrm{B}}\ln\frac{q_{\mathrm{t}}^N}{N!} + \frac{U_{\mathrm{t}}}{T} = Nk_{\mathrm{B}}\left(\ln\frac{q_{\mathrm{t}}}{N} + 1\right) + \frac{3}{2}Nk_{\mathrm{B}}.
$$
Using $q_{\mathrm{t}}/N = V/(N\Lambda^3) = k_{\mathrm{B}}T/(p\Lambda^3)$, we obtain

**Theorem 11.6.1 (Sackur–Tetrode Equation)** The molar translational entropy of an ideal gas is

$$
S_{\mathrm{m},\mathrm{t}} = R\left[\ln\left(\frac{(2\pi mk_{\mathrm{B}}T)^{3/2}}{h^3}\cdot\frac{k_{\mathrm{B}}T}{p}\right) + \frac{5}{2}\right].
\tag{11.10}
$$

It applies to both monatomic and polyatomic gases ($m$ is the mass of the molecule); for a monatomic gas the entropy is just this (plus the electronic term $R\ln g_{\mathrm{e},0}$). The equation shows that the translational entropy increases with increasing $T$ and decreasing $p$ (increasing $V$), and also with increasing molecular mass, because the larger the mass, the closer together the translational levels and the more states are accessible. Planck's constant appears in the equation: classical statistics can fix only differences of entropy, and the absolute value of the entropy requires quantum mechanics to supply the "unit of state".

The entropies of the other motions follow from $S = Nk_{\mathrm{B}}\ln q + U/T$ (linear molecules, $x = \Theta_{\mathrm{v}}/T$):

$$
S_{\mathrm{m},\mathrm{r}} = R\left(\ln\frac{T}{\sigma\Theta_{\mathrm{r}}} + 1\right), \qquad S_{\mathrm{m},\mathrm{v}} = R\left[\frac{x}{\mathrm{e}^x - 1} - \ln\left(1 - \mathrm{e}^{-x}\right)\right], \qquad S_{\mathrm{m},\mathrm{e}} = R\ln g_{\mathrm{e},0}.
\tag{11.11}
$$

**Example 11.6.1** Statistical entropies of several gases at $298.15\,\mathrm{K}$ and $p^\circ$ ($\mathrm{J\,mol^{-1}\,K^{-1}}$), compared with $S^\circ_{\mathrm{m}}$ from thermodynamic data tables (CRC):

| Gas | $S_{\mathrm{m},\mathrm{t}}$ | $S_{\mathrm{m},\mathrm{r}}$ | $S_{\mathrm{m},\mathrm{v}}$ | $S_{\mathrm{m},\mathrm{e}}$ | Total | Tabulated $S^\circ_{\mathrm{m}}$ |
|---|---|---|---|---|---|---|
| He | 126.15 | — | — | 0 | 126.15 | 126.15 |
| Ar | 154.85 | — | — | 0 | 154.85 | 154.85 |
| $\ce{N2}$ | 150.42 | 41.18 | 0.001 | 0 | 191.60 | 191.61 |
| $\ce{O2}$ | 152.08 | 43.88 | 0.04 | 9.13 | 205.13 | 205.15 |

For molecules this simple, the statistical entropy agrees with the tabulated value to $0.01$–$0.02\,\mathrm{J\,mol^{-1}\,K^{-1}}$; in fact, the tabulated values for gases are mostly calculated from spectroscopic data. The translational entropy makes up most of the total. The triplet ground state of $\ce{O2}$ contributes $R\ln 3 = 9.13$, and without it the result would be far off. (Computed for the old standard pressure of $101.325\,\mathrm{kPa}$, all values are lower by $R\ln 1.01325 = 0.11$; for He, for example, $126.04$.)

**Example 11.6.2** $\ce{N2}$ and $\ce{CO}$ have almost the same molar mass ($28.01$) and very similar moments of inertia, and neither vibration nor electronic excitation is active at ordinary temperatures. Why is $S^\circ_{\mathrm{m}}(\ce{CO}) = 197.66$ larger than $S^\circ_{\mathrm{m}}(\ce{N2}) = 191.61\,\mathrm{J\,mol^{-1}\,K^{-1}}$ by $6.05$?

**Solution** The main reason is the **symmetry number**: $\sigma = 2$ for $\ce{N2}$ and $\sigma = 1$ for $\ce{CO}$, so the rotational entropies differ by $R\ln 2 = 5.76$. The remaining $0.3$ comes from the small differences in $\Theta_{\mathrm{r}}$ ($2.77$ and $2.86\,\mathrm{K}$) and in the vibrational frequencies.

**Example 11.6.3** $1\,\mathrm{mol}$ of He changes from $(T_1, V_1)$ to $(T_2, V_2)$. Find $\Delta S$.

**Solution** Only the translational entropy changes. From Eq. (11.10) (written in terms of $V$), $S_{\mathrm{m}} = R\ln(T^{3/2}V) + \text{const}$, so

$$
\Delta S_{\mathrm{m}} = \frac{3}{2}R\ln\frac{T_2}{T_1} + R\ln\frac{V_2}{V_1},
$$
the same as the result of classical thermodynamics by constructing a reversible path (heating at constant volume plus isothermal volume change, $C_{V,\mathrm{m}} = \frac{3}{2}R$, [6.3.2](/6.3.2#sec-2.3.2)).

When ideal gases mix at constant temperature and pressure ([Definition 2.3.1 of 6.3.2](/6.3.2#def-2.3.1)), the range available to each kind of molecule expands from $V_{\mathrm{B}}$ to $V$, the translational partition function increases by the factor $V/V_{\mathrm{B}} = 1/x_{\mathrm{B}}$, and the rotational and vibrational parts are unchanged. The **entropy of mixing** therefore comes entirely from the translational entropy: $\Delta_{\mathrm{mix}}S = \sum_{\mathrm{B}} n_{\mathrm{B}}R\ln(V/V_{\mathrm{B}}) = -R\sum_{\mathrm{B}} n_{\mathrm{B}}\ln x_{\mathrm{B}}$. If both sides contain the same gas, the molecules are indistinguishable once the partition is removed, and the $N!$ in $q^N/N!$ makes the entropy change zero (the resolution of the Gibbs paradox).

### 11.6.3. Statistical versus Calorimetric Entropy: Residual Entropy

The **calorimetric entropy** ([6.3.2](/6.3.2#sec-2.4.2)) takes the entropy of a perfect crystal at $0\,\mathrm{K}$ as zero and is obtained by integrating heat capacities and enthalpies of transition; the statistical entropy is computed directly from the energy levels of gas molecules. The two are originally independent, and for most substances they agree within experimental error, which is the strongest evidence for the third law. For some substances, however, the statistical entropy is clearly larger than the calorimetric entropy.

**Definition 11.6.2** The difference $S_{\mathrm{stat}} - S_{\mathrm{cal}}$ between the statistical entropy and the calorimetric entropy of the same substance in the same state is called its **residual entropy**. It is the entropy corresponding to the disorder that remains in the crystal at $0\,\mathrm{K}$, a part that calorimetry cannot detect.

**Example 11.6.4 (CO)** At $298.15\,\mathrm{K}$ and $p^\circ$ the statistical entropy of $\ce{CO}$ is $197.7$ and the calorimetric entropy is about $193.3\,\mathrm{J\,mol^{-1}\,K^{-1}}$, a residual entropy of about $4.4$. The two ends of a $\ce{CO}$ molecule are similar and its dipole moment is very small (about $0.1\,\mathrm{D}$), so the energies of the two orientations, CO and OC, in the crystal are almost equal. On freezing, the orientations are frozen in at random, and at low temperature the molecules lack the energy to flip, so the arrangement no longer tends toward order. If every molecule had two orientations and they were completely random, $\Omega = 2^{N_{\mathrm{A}}}$ and

$$
S_{\mathrm{res,m}} = k_{\mathrm{B}}\ln 2^{N_{\mathrm{A}}} = R\ln 2 = 5.76\,\mathrm{J\,mol^{-1}\,K^{-1}}.
$$
The measured value is slightly smaller, showing that some order was already present at freezing.

Other typical examples:

- $\ce{N2O}$ (two orientations, NNO and ONN): about $4.8$, again close to $R\ln 2$.
- Ice: disorder in the positions of the hydrogen atoms, estimated by Pauling as $R\ln\frac{3}{2} = 3.37$, measured about $3.4$ ([6.3.2](/6.3.2#sec-2.4.2)).
- $\ce{NO}$: the crystal consists of $\ce{(NO)2}$ dimers, each with two orientations, giving about $\frac{1}{2}R\ln 2 = 2.9$ per mole of $\ce{NO}$, measured about $3$.
- $\ce{H2}$: the difference arises because ortho- and parahydrogen cannot reach equilibrium at low temperature (Section 11.5), not from orientational disorder.

In thermodynamic data tables the $S^\circ_{\mathrm{m}}$ of these substances is the statistical entropy: on this point statistical thermodynamics is more reliable than calorimetry.

### 11.6.4. Example: Vapor Pressure from Statistical Entropy

**Example 11.6.5** At $84\,\mathrm{K}$ the molar entropy of solid Ar is $38.3\,\mathrm{J\,mol^{-1}\,K^{-1}}$ and its molar enthalpy of sublimation is $7940\,\mathrm{J\,mol^{-1}}$. Assuming Ar vapor to be an ideal gas, find the equilibrium vapor pressure $p$ of solid Ar at $84\,\mathrm{K}$.

**Solution** At solid–gas equilibrium $\Delta_{\mathrm{sub}}G_{\mathrm{m}} = 0$ and $\Delta_{\mathrm{sub}}S_{\mathrm{m}} = \Delta_{\mathrm{sub}}H_{\mathrm{m}}/T$, so the molar entropy of the vapor at the equilibrium pressure $p$ is (the effect of pressure on the entropy of the solid is negligible)

$$
S_{\mathrm{m}}(\mathrm{g}, p) = S_{\mathrm{m}}(\mathrm{s}) + \frac{\Delta_{\mathrm{sub}}H_{\mathrm{m}}}{T} = 38.3 + \frac{7940}{84} = 132.8\,\mathrm{J\,mol^{-1}\,K^{-1}}.
$$
On the other hand, from the Sackur–Tetrode equation (11.10), $S_{\mathrm{m}}(\mathrm{g}, p^\circ) = 128.5\,\mathrm{J\,mol^{-1}\,K^{-1}}$ at $84\,\mathrm{K}$ and $p^\circ$, and $S_{\mathrm{m}}(\mathrm{g}, p) = S_{\mathrm{m}}(\mathrm{g}, p^\circ) - R\ln(p/p^\circ)$. Hence

$$
\ln\frac{p}{p^\circ} = \frac{128.5 - 132.8}{8.314} = -0.52, \qquad p \approx 0.60\,p^\circ = 60\,\mathrm{kPa}.
$$
The triple point of Ar is $83.81\,\mathrm{K}$ and $68.9\,\mathrm{kPa}$, so the computed value is about $14\%$ low. An error of $0.14$ in $\ln p$ corresponds to an entropy error of only $0.14R = 1.2\,\mathrm{J\,mol^{-1}\,K^{-1}}$, within the precision of the data given: the vapor pressure obtained from entropies is very sensitive to the data. The point of the example is that, using only calorimetric data for the condensed phase and the mass of the gas molecule, one obtains the correct order of magnitude of the vapor pressure from "first principles".

## 11.7. Equilibrium Constants from Partition Functions

### 11.7.1. The Standard Chemical Potential of an Ideal Gas

By Eq. (10.15), the chemical potential of molecule B in an ideal gas is $\mu_{\mathrm{B}} = -k_{\mathrm{B}}T\ln(q_{\mathrm{B}}/N_{\mathrm{B}})$, where the energies in $q_{\mathrm{B}}$ must be measured from a zero common to all species. Let the ground-state energy of molecule B be $\varepsilon_{0,\mathrm{B}}$ and the partition function with the ground state as zero be $q_{\mathrm{B}}^{(0)}$; then $q_{\mathrm{B}} = q_{\mathrm{B}}^{(0)}\mathrm{e}^{-\varepsilon_{0,\mathrm{B}}/(k_{\mathrm{B}}T)}$. Multiplying by $N_{\mathrm{A}}$ to obtain molar quantities ($U_{0,\mathrm{m}}(\mathrm{B}) = N_{\mathrm{A}}\varepsilon_{0,\mathrm{B}}$):

$$
\mu_{\mathrm{B}} = U_{0,\mathrm{m}}(\mathrm{B}) - RT\ln\frac{q_{\mathrm{B}}^{(0)}}{N_{\mathrm{B}}}.
$$
$q_{\mathrm{B}}^{(0)}$ is proportional to $V$ only through its translational factor, and in an ideal-gas mixture $N_{\mathrm{B}}/V = p_{\mathrm{B}}/(k_{\mathrm{B}}T)$, so

$$
\frac{q_{\mathrm{B}}^{(0)}}{N_{\mathrm{B}}} = \frac{q_{\mathrm{B}}^{(0)}}{V}\cdot\frac{k_{\mathrm{B}}T}{p_{\mathrm{B}}} = \frac{q_{\mathrm{B}}^\circ}{N_{\mathrm{A}}}\cdot\frac{p^\circ}{p_{\mathrm{B}}}, \qquad q_{\mathrm{B}}^\circ = q_{\mathrm{B}}^{(0)}\Big|_{V = V^\circ_{\mathrm{m}} = RT/p^\circ},
$$
where $q_{\mathrm{B}}^\circ$ is the molecular partition function of B in the standard molar volume. Substituting and comparing with $\mu_{\mathrm{B}} = \mu_{\mathrm{B}}^\circ + RT\ln(p_{\mathrm{B}}/p^\circ)$ ([6.3.4](/6.3.4#sec-4.4.2)),

$$
\mu_{\mathrm{B}}^\circ(T) = U_{0,\mathrm{m}}(\mathrm{B}) - RT\ln\frac{q_{\mathrm{B}}^\circ}{N_{\mathrm{A}}}.
\tag{11.12}
$$
The standard chemical potential depends only on temperature; $q_{\mathrm{B}}^\circ/N_{\mathrm{A}}$ is the number of quantum states accessible to each molecule in the standard state (for $\ce{N2}$ at $298\,\mathrm{K}$, about $6\times10^6\times52\approx3\times10^8$). The "Gibbs energy function" $[G^\circ_{\mathrm{m}}(T) - H^\circ_{\mathrm{m}}(0\,\mathrm{K})]/T = -R\ln(q^\circ/N_{\mathrm{A}})$ in thermodynamic data tables is computed from spectroscopic data in exactly this way.

### 11.7.2. The Standard Equilibrium Constant

**Theorem 11.7.1** The **standard equilibrium constant** of an ideal-gas reaction $0 = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mathrm{B}$ is

$$
K^\circ = \prod_{\mathrm{B}}\left(\frac{q_{\mathrm{B}}^\circ}{N_{\mathrm{A}}}\right)^{\nu_{\mathrm{B}}}\exp\left(-\frac{\Delta_{\mathrm{r}}U_0}{RT}\right), \qquad \Delta_{\mathrm{r}}U_0 = \sum_{\mathrm{B}}\nu_{\mathrm{B}}U_{0,\mathrm{m}}(\mathrm{B}).
\tag{11.13}
$$

**Proof** By the definition of the **standard reaction Gibbs energy** and Eq. (11.12), $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu^\circ_{\mathrm{B}} = \Delta_{\mathrm{r}}U_0 - RT\sum_{\mathrm{B}}\nu_{\mathrm{B}}\ln(q^\circ_{\mathrm{B}}/N_{\mathrm{A}})$; then use $K^\circ = \exp(-\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}/(RT))$ ([Definition 7.2.2 of 6.3.7](/6.3.7#def-7.2.2)). $\square$

$\Delta_{\mathrm{r}}U_0$ is the energy change of the reaction at $0\,\mathrm{K}$, that is, the difference between the vibrational ground-state energies of products and reactants, and can be obtained from spectroscopy or quantum-chemical calculation. For the dissociation of a diatomic molecule $\ce{A2 -> 2A}$, $\Delta_{\mathrm{r}}U_0 = N_{\mathrm{A}}D_0$, where $D_0$ is the dissociation energy measured from the vibrational ground state (less than the well depth $D_{\mathrm{e}}$ of the potential-energy curve by the zero-point energy $\frac{1}{2}h\nu$).

Eq. (11.13) displays clearly the two factors that determine equilibrium: the exponential factor is the energy, favoring the lower-energy side; the ratio of partition functions counts accessible states, favoring the side with more states (entropy). As the temperature rises, the role of the energy factor weakens and the equilibrium shifts toward the side with the larger partition functions, for example a molecule dissociating into atoms (atoms have large translational partition functions). It is also the starting point of transition state theory in [6.3.16](/6.3.16): the activated complex is treated as a species in quasi-equilibrium with the reactants, and this "equilibrium constant" is written with Eq. (11.13), except that the vibration along the reaction coordinate must be treated separately.

### 11.7.3. Worked Examples

**Example 11.7.1 (Dissociation of Iodine)** Compute $K^\circ$ for $\ce{I2(g) <=> 2I(g)}$ at $1000\,\mathrm{K}$. Given for $\ce{I2}$: $\tilde B = 0.03737\,\mathrm{cm^{-1}}$ ($\Theta_{\mathrm{r}} = 0.0538\,\mathrm{K}$), $\tilde\omega_{\mathrm{e}} = 214.5\,\mathrm{cm^{-1}}$ ($\Theta_{\mathrm{v}} = 308.6\,\mathrm{K}$), nondegenerate ground state, $D_0 = 12441\,\mathrm{cm^{-1}}$ ($148.8\,\mathrm{kJ\,mol^{-1}}$); the I atom has ground state $^2\mathrm{P}_{3/2}$ ($g = 4$).

**Solution** Term by term ($T = 1000\,\mathrm{K}$, $p^\circ = 10^5\,\mathrm{Pa}$):

| Quantity | I | $\ce{I2}$ |
|---|---|---|
| $q_{\mathrm{t}}^\circ/N_{\mathrm{A}} = k_{\mathrm{B}}T/(p^\circ\Lambda^3)$ | $1.173\times10^9$ | $3.318\times10^9$ |
| $q_{\mathrm{r}} = T/(2\Theta_{\mathrm{r}})$ | — | $9299$ |
| $q_{\mathrm{v}}^{(0)} = 1/(1 - \mathrm{e}^{-\Theta_{\mathrm{v}}/T})$ | — | $3.766$ |
| $q_{\mathrm{e}}$ | $4$ | $1$ |

$$
K^\circ = \frac{(1.173\times10^9\times4)^2}{3.318\times10^9\times9299\times3.766}\,\exp\left(-\frac{hcD_0}{k_{\mathrm{B}}T}\right) = 1.89\times10^5\times\mathrm{e}^{-17.90} = 3.19\times10^{-3}.
$$
As a check, correcting the CRC thermodynamic data at $298.15\,\mathrm{K}$ ($\Delta_{\mathrm{f}}H^\circ$, $S^\circ_{\mathrm{m}}$, $C_{p,\mathrm{m}}$) to $1000\,\mathrm{K}$ by **Kirchhoff's law** gives $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = 47.8\,\mathrm{kJ\,mol^{-1}}$ and $K^\circ = 3.2\times10^{-3}$, in agreement. At a total pressure of $p^\circ$ the degree of dissociation is $\alpha = \sqrt{K^\circ/(K^\circ + 4)} = 0.028$. The ratio of partition functions is about $2\times10^5$, arising almost entirely from the translation of the two I atoms (each atom has $10^9$ states in the standard volume) compared with the translation, rotation and vibration of $\ce{I2}$; it competes with the very small energy factor $\mathrm{e}^{-17.9}$, and this competition makes the dissociation significant only at high temperatures.

```python
import numpy as np

h, kB, NA, c = 6.62607015e-34, 1.380649e-23, 6.02214076e23, 299792458.0
c2 = h * c * 100 / kB                      # hc/kB in cm K
T, p0 = 1000.0, 1e5


def qt_per_molecule(M):                    # q_t / N_A at the standard molar volume
    m = M * 1e-3 / NA
    return (2 * np.pi * m * kB * T / h**2) ** 1.5 * kB * T / p0


q_I = qt_per_molecule(126.904) * 4                                   # 2P3/2 ground level
q_I2 = (qt_per_molecule(253.809) * T / (2 * c2 * 0.03737)
        / (1 - np.exp(-c2 * 214.5 / T)))                             # rotation, vibration
K = q_I**2 / q_I2 * np.exp(-c2 * 12440.9 / T)
print(f"K = {K:.3g}")                                                # K = 0.00319
```

![I₂(g) ⇌ 2I(g). Left: lg K° versus 1000 K/T, computed from partition functions (solid line) and extrapolated from 298.15 K thermodynamic data with constant ΔrCp (dashed) or ΔrCp = 0 (dotted). Right: degree of dissociation at a total pressure of p°](./plots/iodine-dissociation.py)

**Example 11.7.2 (Isotope Exchange)** For $\ce{H2 + D2 <=> 2HD}$, $\Delta\nu = 0$, and the $V$ and $T$ factors in the partition functions largely cancel. At high temperature all partition functions take their classical forms, and the factors of mass and moment of inertia cancel completely, leaving only the symmetry numbers:

$$
K^\circ \to \frac{\sigma(\ce{H2})\,\sigma(\ce{D2})}{\sigma(\ce{HD})^2} = 4.
$$
This is the ratio of the numbers of combinations for random pairing of H and D atoms ($\ce{HD}$ has two "ways of arrangement"). Computing term by term from the spectroscopic constants and zero-point energies of $\ce{H2}$, $\ce{D2}$ and $\ce{HD}$, one obtains $K^\circ = 3.26$ at $298\,\mathrm{K}$ and $3.90$ at $1000\,\mathrm{K}$, in agreement with experiment. The deviation from 4 at low temperature arises because the zero-point energies of the three molecules differ ($\Delta_{\mathrm{r}}U_0 > 0$): this quantum effect is the root of isotope fractionation and of kinetic isotope effects.

## Summary

| Motion | Partition function (ground state as zero) | Contribution to $U_{\mathrm{m}}$ (high-temperature limit) | Contribution to $S_{\mathrm{m}}$ |
|---|---|---|---|
| Translation | $V/\Lambda^3$, $\Lambda = h/\sqrt{2\pi mk_{\mathrm{B}}T}$ | $\frac{3}{2}RT$ | Sackur–Tetrode equation (11.10) |
| Rotation (linear) | $T/(\sigma\Theta_{\mathrm{r}})$; corrections in (11.5) | $RT$ | $R[\ln(T/\sigma\Theta_{\mathrm{r}}) + 1]$ |
| Rotation (nonlinear) | Eq. (11.6) | $\frac{3}{2}RT$ | $R[\ln q_{\mathrm{r}} + \frac{3}{2}]$ |
| Vibration (each mode) | $1/(1 - \mathrm{e}^{-\Theta_{\mathrm{v}}/T})$ | $R\Theta_{\mathrm{v}}/(\mathrm{e}^{\Theta_{\mathrm{v}}/T} - 1) \to RT$ | Eq. (11.11) |
| Electronic | $g_{\mathrm{e},0}$ (add terms if excited states are low) | 0 | $R\ln g_{\mathrm{e},0}$ |
| Nuclear | $\prod(2s_k + 1)$, omitted in chemistry | 0 | Omitted |

- The equipartition theorem holds only for motions whose level spacing is $\ll k_{\mathrm{B}}T$: at ordinary temperatures translation and rotation are classical, vibration is mostly frozen, and electrons and nuclei are only in their ground states.
- Statistical and calorimetric entropies generally agree; the residual entropy comes from disorder frozen in at $0\,\mathrm{K}$ ($\ce{CO}$ is close to $R\ln 2$).
- $K^\circ = \prod_{\mathrm{B}}(q^\circ_{\mathrm{B}}/N_{\mathrm{A}})^{\nu_{\mathrm{B}}}\mathrm{e}^{-\Delta_{\mathrm{r}}U_0/(RT)}$: equilibrium is decided by the competition between energy and the number of accessible states.

## Questions

1. Can the Sackur–Tetrode equation for a monatomic ideal gas be used to compute the translational entropy of a diatomic gas? On what factors does the molar translational entropy at the standard pressure depend?

   **Answer** Yes. Translation involves only the motion of the center of mass, so one simply takes $m$ to be the mass of the molecule. For a given $p = p^\circ$, $S^\circ_{\mathrm{m},\mathrm{t}}$ depends only on $T$ and the molecular mass $m$; the volume is already fixed by $V^\circ_{\mathrm{m}} = RT/p^\circ$ and is not an independent factor.

2. Why is it unwise to compute the rotational partition function of $\ce{H2}$ as $T/(\sigma\Theta_{\mathrm{r}})$ even at ordinary temperatures?

   **Answer** $\Theta_{\mathrm{r}} = 85.3\,\mathrm{K}$, so at $298\,\mathrm{K}$ $\Theta_{\mathrm{r}}/T \approx 0.29$ and the integral approximation is in error by about $10\%$; one must use the correction series (11.5) or sum directly. At lower temperatures ortho- and parahydrogen must in addition be treated separately.

3. Does the choice of the zero of energy affect the $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ of a reaction computed from partition functions?

   **Answer** Not as long as the energies of all species are measured from the same zero. If each species' $q^{(0)}$ is computed with its own ground state as the zero, the term $\Delta_{\mathrm{r}}U_0$ must be added, otherwise the result is meaningless.

4. Using the data of Example 11.7.1, explain why both raising the temperature and lowering the pressure favor the dissociation of $\ce{I2}$.

   **Answer** $\Delta_{\mathrm{r}}U_0 > 0$, and a higher temperature increases $\mathrm{e}^{-\Delta_{\mathrm{r}}U_0/(RT)}$ (an endothermic reaction, van 't Hoff equation). $\Delta\nu_{\mathrm{g}} = 1$, and lowering the pressure amounts to increasing the number of translational states accessible to each molecule, which favors the side with more molecules.
