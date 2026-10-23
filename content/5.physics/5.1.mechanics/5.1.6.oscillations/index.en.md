---
title: Oscillations
description: Definition, criteria, characteristic quantities and phasor representation of simple harmonic motion; small oscillations near a stable equilibrium; superposition of simple harmonic motions (beats, Lissajous figures, normal modes of coupled oscillators); harmonic analysis and spectra; damped oscillation and the quality factor; forced oscillation and resonance.
source_hash: "443e75311359"
---

A process in which a physical quantity varies back and forth about some value is called an oscillation. Oscillations are not confined to mechanical motion: the current in an alternating-current circuit, the electric field in an electromagnetic wave and the positions of atoms in a molecule all oscillate, and they satisfy equations of the same form. According to the forces involved, oscillations are classified as undamped free oscillation, damped free oscillation and forced oscillation. The simplest and most fundamental case is simple harmonic motion in undamped free oscillation, which is the focus of this chapter: on the one hand, many small oscillations in practice can be treated as simple harmonic; on the other hand, any complicated oscillation can be decomposed into a superposition of simple harmonic motions.

Mathematically, the equations of this chapter are all second-order **linear differential equations** with constant coefficients. Their solution was treated in the section on oscillation problems in [2.2.16](/2.2.16#sec-16.5) and in [2.4.9](/2.4.9) and is not repeated here; instead we stress the physical picture: representing oscillations with **complex numbers** and phasors, judging the nature of an oscillation from its energy, and understanding resonance through the frequency response. The normal modes of coupled oscillations are a direct application of the **eigenvalue** problem of linear algebra, and harmonic analysis is the **Fourier series**. The **potential energy curve** of the previous chapter ([5.1.4](/5.1.4)) explains why oscillation occurs near a stable equilibrium; the next chapter, [5.1.7](/5.1.7), studies the propagation of oscillations through space, that is, waves.

## 6.1. Simple Harmonic Motion

### 6.1.1. Definition of Simple Harmonic Motion

**Definition 6.1.1 (Simple Harmonic Motion)** A process in which a physical quantity $x$ varies with time according to a cosine (or sine) law,

$$
x=A\cos(\omega t+\varphi_0)
$$
is called **simple harmonic motion**, where $A>0$ is the **amplitude**, $\omega$ is the **angular frequency**, $\omega t+\varphi_0$ is the **phase**, and $\varphi_0$ is the **initial phase**.

The quantity $x$ may be a **displacement** or an angle, or a current, an electric field strength, a temperature, and so on. Simple harmonic motion is an idealized model and the basis for studying complicated oscillations.

### 6.1.2. Criteria for Simple Harmonic Motion

For a mechanical oscillation, any one of the following three conditions suffices to establish simple harmonic motion:

1. Force law: the net force on the **particle** is proportional to the displacement from the equilibrium position and opposite in direction,
   $$
   F=-kx,
   $$
   Such a force is called a linear restoring force (elastic or quasi-elastic force), and $k$ is the force constant (stiffness).
2. Equation of motion:
   $$
   \frac{\mathrm{d}^2x}{\mathrm{d}t^2}+\omega^2x=0,
   $$
   whose general solution is exactly $x=A\cos(\omega t+\varphi_0)$.
3. Energy: the restoring force is a **conservative force**; taking the **potential energy** to be zero at the equilibrium position, $E_{\mathrm{p}}=\frac12kx^2$ and the **mechanical energy** of the system is conserved,
   $$
   E=\frac12mv^2+\frac12kx^2=\frac12kA^2=\text{const}.
   $$
   The **kinetic energy** and the potential energy continually convert into each other, and their averages over a period are equal: $\bar E_{\mathrm{k}}=\bar E_{\mathrm{p}}=\frac14kA^2$.

From 1 and **Newton's second law** we obtain 2 ($\omega^2=k/m$); differentiating 3 gives $mv\dot v+kxv=0$, that is, $m\ddot x+kx=0$, which also gives 2.

### 6.1.3. Characteristic Quantities of Simple Harmonic Motion

1. The angular frequency $\omega=\sqrt{k/m}$ is determined by the system alone and is also called the natural angular frequency. The frequency is $\nu=\dfrac{\omega}{2\pi}$ and the period is $T=\dfrac1\nu=\dfrac{2\pi}{\omega}$, with units $\mathrm{rad\,s^{-1}}$, $\mathrm{Hz}$ and $\mathrm{s}$ respectively.
2. The amplitude $A$ is determined by the initial conditions $x_0$, $v_0$ and the system:
   $$
   A=\sqrt{x_0^2+\frac{v_0^2}{\omega^2}}=\sqrt{\frac{2E}{k}} .
   $$
3. The initial phase $\varphi_0$ is also determined by the initial conditions and the system: from $x_0=A\cos\varphi_0$ and $v_0=-A\omega\sin\varphi_0$,
   $$
   \tan\varphi_0=-\frac{v_0}{\omega x_0},
   $$
   and the signs of $x_0$ and $v_0$ determine the quadrant of $\varphi_0$ (usually a value in $(-\pi,\pi]$ is taken).

### 6.1.4. Representations of Simple Harmonic Motion

Given the amplitude $A$, the angular frequency $\omega$ and the initial phase $\varphi_0$, a simple harmonic motion is determined.

In terms of the oscillation function, the displacement, **velocity** and **acceleration** are

$$
x=A\cos(\omega t+\varphi_0),\quad
v=\frac{\mathrm{d}x}{\mathrm{d}t}=\omega A\cos\Big(\omega t+\varphi_0+\frac\pi2\Big),\quad
a=\frac{\mathrm{d}^2x}{\mathrm{d}t^2}=\omega^2A\cos(\omega t+\varphi_0+\pi),
$$
The phase of the velocity leads that of the displacement by $\pi/2$, and the acceleration is in antiphase with the displacement, $a=-\omega^2x$.

The oscillation curve, drawn with $t$ as abscissa and $x$ as ordinate, is a cosine curve of period $T$ whose value at $t=0$ is $A\cos\varphi_0$.

A more intuitive representation is the rotating vector (phasor) representation. In the plane of the $x$ axis, draw from the origin a vector $\boldsymbol{A}$ of length $A$ and let it rotate counterclockwise uniformly with **angular velocity** $\omega$, making an angle $\varphi_0$ with the $x$ axis at $t=0$. The projection of the tip of the vector on the $x$ axis is $x=A\cos(\omega t+\varphi_0)$, and the circle traced by the tip is called the reference circle. This rotating vector (*phasor*) is the picture in the complex plane of the complex number $\tilde x=A\mathrm{e}^{\mathrm{i}(\omega t+\varphi_0)}$, with $x=\operatorname{Re}\tilde x$: by [Euler's formula](/2.1.9), the amplitude and initial phase combine into a complex amplitude $A\mathrm{e}^{\mathrm{i}\varphi_0}$ (the **polar form** of a complex number), and differentiation amounts to multiplication by $\mathrm{i}\omega$, that is, the phasor turns counterclockwise by $\pi/2$ and is stretched by a factor $\omega$. The rotating vector is convenient for determining the initial phase and for studying the superposition of oscillations.

**Example 6.1.1** Given $x_0=A/2$, find the initial phase for $v_0<0$ and for $v_0>0$.

**Solution** $\cos\varphi_0=\frac12$, so $\varphi_0=\pm\frac\pi3$. On the reference circle, at $t=0$ the projection of the tip of the rotating vector is at $A/2$; when the tip is on the upper half of the circle its projection moves to the left, $v_0<0$. Hence $\varphi_0=\frac\pi3$ for $v_0<0$ and $\varphi_0=-\frac\pi3$ for $v_0>0$.

**Example 6.1.2** A liquid of mass $m$ and density $\rho$ fills a U-tube of cross-sectional area $S$. Initially the liquid levels in the two arms differ in height. Neglecting friction between the tube wall and the liquid, determine the nature of the oscillation of the liquid column.

**Solution** Method 1 (forces): suppose the level on one side rises by $y$ relative to the equilibrium position and that on the other side drops by $y$. The weight of the liquid column corresponding to the level difference $2y$ is the restoring force,
$$
F=-2\rho gSy=-ky,\qquad k=2\rho gS=\text{const},
$$
so the motion is simple harmonic, with $\omega=\sqrt{k/m}=\sqrt{2\rho gS/m}$.

Method 2 (energy): relative to the equilibrium position, this is equivalent to moving a segment of liquid of height $y$ and mass $\rho Sy$ from one side to the other and raising it by $y$, so $E_{\mathrm{p}}=\rho gSy\cdot y=\frac12ky^2$ with $k=2\rho gS$; with no losses the mechanical energy is conserved, so the motion is simple harmonic with the same angular frequency. If the total length of the liquid column is $l$, then $m=\rho Sl$ and $\omega=\sqrt{2g/l}$, independent of the density of the liquid and the thickness of the tube.

### 6.1.5. Small Oscillations Near a Stable Equilibrium

**Example 6.1.3** Show that small oscillations near a stable equilibrium position are simple harmonic.

**Proof** Let the stable equilibrium position of a one-dimensional conservative system be $x=0$, so that $E_{\mathrm{p}}'(0)=0$ and $E_{\mathrm{p}}''(0)>0$. Expand the potential energy about $x=0$ as a **Taylor series**, keeping terms only up to $x^2$ for small oscillations and taking $E_{\mathrm{p}}(0)=0$:

$$
E_{\mathrm{p}}(x)\approx\frac12E_{\mathrm{p}}''(0)\,x^2=\frac12kx^2,\qquad k=E_{\mathrm{p}}''(0)>0,
$$
so $f=-\dfrac{\mathrm{d}E_{\mathrm{p}}}{\mathrm{d}x}=-kx$, a linear restoring force. $\square$

This is the linearization of the equation at an **equilibrium point** ([2.4.11](/2.4.11)). Vibrations of atoms and molecules (the potential energy curve of [Example 4.6.2](/5.1.4#ex-4.6.2) is approximately parabolic near its minimum) and lattice vibrations in solids are small oscillations of exactly this kind.

**Remark 6.1.1 (Large-Amplitude Oscillation of a Pendulum)** The equation of the simple pendulum, $\ddot\theta+\frac gl\sin\theta=0$, is nonlinear, and the motion is simple harmonic only when $\sin\theta\approx\theta$, with period $T_0=2\pi\sqrt{l/g}$. For a swing of amplitude $\theta_0$, conservation of energy gives the exact period

$$
T=4\sqrt{\frac lg}\,K\Big(\sin\frac{\theta_0}{2}\Big)\approx T_0\Big(1+\frac{\theta_0^2}{16}\Big),
$$
where $K(k)=\int_0^{\pi/2}\frac{\mathrm{d}\phi}{\sqrt{1-k^2\sin^2\phi}}$ is the complete elliptic integral of the first kind. For $\theta_0=10^\circ$, $T/T_0=1.0019$; for $30^\circ$, $1.0174$; for $90^\circ$, $1.1803$. For small angles the period is almost independent of the amplitude (isochronism), while for larger amplitudes the period becomes longer. This result can also be checked by solving the equation numerically with `solve_ivp`, as in [4.4.4](/4.4.4#sec-4.3.2):

```python
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import ellipk

theta0 = np.radians(90)


def crossing(t, y):  # pendulum passes theta = 0 after a quarter period
    return y[0]


crossing.terminal, crossing.direction = True, -1
sol = solve_ivp(lambda t, y: [y[1], -np.sin(y[0])], (0, 50), [theta0, 0],
                events=crossing, rtol=1e-10, atol=1e-12)  # g / l = 1
print(4 * sol.t_events[0][0] / (2 * np.pi))          # T / T0 from the ODE
print(2 / np.pi * ellipk(np.sin(theta0 / 2) ** 2))  # SciPy uses the parameter k^2
```

```text
1.18034059902613
1.1803405990160962
```

## 6.2. Superposition of Simple Harmonic Motions

### 6.2.1. Superposition of Collinear Motions of the Same Frequency

Let $x_1=A_1\cos(\omega t+\varphi_1)$ and $x_2=A_2\cos(\omega t+\varphi_2)$. The two rotating vectors rotate with the same angular velocity and keep a fixed angle between them, so their vector sum also rotates with $\omega$. Hence the resultant oscillation $x=x_1+x_2=A\cos(\omega t+\varphi)$ is again simple harmonic with the same frequency, and by the parallelogram rule (or by adding the complex amplitudes, $A\mathrm{e}^{\mathrm{i}\varphi}=A_1\mathrm{e}^{\mathrm{i}\varphi_1}+A_2\mathrm{e}^{\mathrm{i}\varphi_2}$),

$$
A=\sqrt{A_1^2+A_2^2+2A_1A_2\cos(\varphi_2-\varphi_1)},\qquad
\tan\varphi=\frac{A_1\sin\varphi_1+A_2\sin\varphi_2}{A_1\cos\varphi_1+A_2\cos\varphi_2}.
$$
Important special cases:

- In phase, $\varphi_2-\varphi_1=2k\pi$ ($k\in\mathbb{Z}$): $A=A_1+A_2$, the resultant amplitude is a maximum;
- In antiphase, $\varphi_2-\varphi_1=(2k+1)\pi$: $A=\lvert A_1-A_2\rvert$, the resultant amplitude is a minimum.

Now consider the superposition of $n$ simple harmonic motions of equal amplitude whose initial phases differ successively by $\delta$. Let $x_j=a\cos\big(\omega t+(j-1)\delta\big)$, $j=1,\dots,n$. The sum of the complex amplitudes is a geometric series,

$$
a\sum_{j=0}^{n-1}\mathrm{e}^{\mathrm{i}j\delta}=a\frac{\mathrm{e}^{\mathrm{i}n\delta}-1}{\mathrm{e}^{\mathrm{i}\delta}-1}=a\frac{\sin(n\delta/2)}{\sin(\delta/2)}\mathrm{e}^{\mathrm{i}(n-1)\delta/2},
$$
so the resultant oscillation is $x=A\cos(\omega t+\varphi)$ with

$$
A=a\frac{\sin(n\delta/2)}{\sin(\delta/2)},\qquad \varphi=\frac{n-1}{2}\delta .
$$
Geometrically, the $n$ rotating vectors joined head to tail form part of a regular polygon.

- $\delta=2k\pi$ ($k\in\mathbb{Z}$): all component oscillations are in phase, $A=na$, a maximum;
- $\delta=2k\pi/n$ with $k$ not an integer multiple of $n$: $A=0$, and the component amplitude vectors form a closed polygon. For $n=4$, for example, $\delta=\pm\frac\pi2,\pm\pi,\pm\frac{3\pi}2,\dots$ all make the resultant amplitude zero.

This result underlies the intensity distribution of multiple-slit interference in grating diffraction ([5.4.2](/5.4.2)).

### 6.2.2. Superposition of Collinear Motions of Different Frequencies; Beats

For simplicity, let the two oscillations have the same amplitude and the same initial phase: $x_1=A\cos(\omega_1t+\varphi_0)$ and $x_2=A\cos(\omega_2t+\varphi_0)$. By the sum-to-product identity,

$$
x=x_1+x_2=2A\cos\Big(\frac{\omega_2-\omega_1}{2}t\Big)\cos\Big(\frac{\omega_2+\omega_1}{2}t+\varphi_0\Big),
$$
and the resultant oscillation is no longer simple harmonic. If $\omega_1$ and $\omega_2$ are both large and their difference is small, the first factor varies slowly and the second varies rapidly, so the resultant oscillation can be regarded as an oscillation of angular frequency $\frac{\omega_1+\omega_2}{2}$ whose amplitude $\big\lvert2A\cos\frac{\omega_2-\omega_1}{2}t\big\rvert$ varies slowly: the resultant oscillation alternately strengthens and weakens. This phenomenon is called a *beat*.

In the rotating-vector picture, the angle between the two rotating vectors changes slowly at angular velocity $\lvert\omega_1-\omega_2\rvert$: when they coincide in direction, $A_{\max}=A_1+A_2$, and when they point in opposite directions, $A_{\min}=\lvert A_1-A_2\rvert$. The frequency with which the resultant amplitude varies is called the beat frequency,

$$
\nu_{\mathrm{beat}}=\lvert\nu_1-\nu_2\rvert .
$$
When two tuning forks of nearby frequencies sound together, one hears a beat tone whose loudness rises and falls periodically. Beats can be used to measure frequencies (for example, in tuning one makes the beats disappear), and a low-frequency oscillation can be obtained from two high-frequency ones.

![Beats: two oscillations of equal amplitude with nearby frequencies nu1 = 10 Hz and nu2 = 11 Hz (top) and their sum (bottom), whose amplitude 2A|cos((omega2 - omega1) t / 2)| (dashed envelope) varies with the beat frequency |nu1 - nu2| = 1 Hz](./plots/beats.py)

**Example 6.2.1 (Coupled Pendulums and Normal Modes)** Two identical simple pendulums (mass $m$, length $l$, $\omega_0^2=g/l$) are connected by a light spring of force constant $k$. For small oscillations, the horizontal displacements $x_1$, $x_2$ of the two pendulums satisfy

$$
\ddot x_1=-\omega_0^2x_1-\kappa(x_1-x_2),\qquad \ddot x_2=-\omega_0^2x_2-\kappa(x_2-x_1),\qquad \kappa=\frac km,
$$
that is, $\ddot{\boldsymbol{x}}=-K\boldsymbol{x}$ with $K=\begin{bmatrix}\omega_0^2+\kappa&-\kappa\\-\kappa&\omega_0^2+\kappa\end{bmatrix}$. The matrix $K$ is a real **symmetric matrix**, and its **eigenvalues** and eigenvectors are

$$
\omega_1^2=\omega_0^2,\ \ \boldsymbol{u}_1=\begin{bmatrix}1\\1\end{bmatrix};\qquad
\omega_2^2=\omega_0^2+2\kappa,\ \ \boldsymbol{u}_2=\begin{bmatrix}1\\-1\end{bmatrix}.
$$
In the coordinates along the eigenvectors, $q_1=\frac12(x_1+x_2)$ and $q_2=\frac12(x_1-x_2)$, the equations decouple into two independent simple harmonic oscillations: when the two pendulums swing in phase the spring is neither stretched nor compressed and the frequency is $\omega_1$; when they swing in antiphase the spring is stretched and compressed and the frequency is $\omega_2$. These two patterns, in which every part oscillates at the same frequency, are called *normal modes*, and the general motion is a superposition of them. If initially only the first pendulum is displaced ($x_1=A$, $x_2=0$, both at rest), then

$$
x_1=A\cos\frac{\omega_2-\omega_1}{2}t\,\cos\frac{\omega_2+\omega_1}{2}t,\qquad
x_2=A\sin\frac{\omega_2-\omega_1}{2}t\,\sin\frac{\omega_2+\omega_1}{2}t .
$$
For weak coupling ($\kappa\ll\omega_0^2$) each pendulum exhibits beats, and the energy is transferred back and forth between the two pendulums, completely transferred once every $\pi/(\omega_2-\omega_1)$: the "resonantly coupled pendulums" of lecture demonstrations show exactly this phenomenon. A system of $n$ coupled oscillators has $n$ normal modes, and the normal modes of a continuous medium (a string, an air column) are standing waves ([5.1.7](/5.1.7)).

### 6.2.3. Superposition of Perpendicular Motions of the Same Frequency

A particle takes part simultaneously in the two oscillations $x=A_x\cos(\omega t+\varphi_x)$ and $y=A_y\cos(\omega t+\varphi_y)$. Eliminating $t$ gives the equation of the trajectory

$$
\frac{x^2}{A_x^2}+\frac{y^2}{A_y^2}-\frac{2xy}{A_xA_y}\cos(\varphi_y-\varphi_x)=\sin^2(\varphi_y-\varphi_x).
$$
Write $\Delta\varphi=\varphi_y-\varphi_x$:

- $\Delta\varphi=0$ or $\pi$: the trajectory is a line segment through the origin, and the resultant oscillation is linear;
- $\Delta\varphi=\pm\frac\pi2$: the trajectory is an upright ellipse whose principal axes are the coordinate axes, and a circle when $A_x=A_y$;
- In general the trajectory is an oblique ellipse.

The sense of rotation is determined by $\Delta\varphi$ (taking $\Delta\varphi\in(-\pi,\pi]$): for $0<\Delta\varphi<\pi$ the phase of $y$ leads and the particle moves clockwise (right-handed); for $-\pi<\Delta\varphi<0$ the phase of $x$ leads and the particle moves counterclockwise (left-handed). For example, for $\Delta\varphi=\frac\pi2$, $x=A\cos\omega t$ and $y=-A\sin\omega t$; at $t=0$ the particle is at $(A,0)$ and moves in the $-y$ direction, which is clockwise. Conversely, any circular or elliptical motion can be decomposed into two perpendicular simple harmonic oscillations of the same frequency; this is exactly how linear, circular and elliptical polarization are described in the polarization of light ([5.4.3](/5.4.3)).

### 6.2.4. Superposition of Perpendicular Motions of Different Frequencies

If the ratio of the two frequencies is a simple ratio of integers, $\omega_x:\omega_y=m:n$, the resultant trajectory is a stable closed curve called a *Lissajous figure*. Over one full period of the figure, the ratio of the number of times $x$ reaches its maximum to the number of times $y$ reaches its maximum equals the frequency ratio: if the figure touches the line $x=A_x$ at $N_x$ points and the line $y=A_y$ at $N_y$ points, then

$$
\frac{\omega_x}{\omega_y}=\frac{N_x}{N_y}.
$$
By observing on an oscilloscope the Lissajous figure formed by combining a known frequency with an unknown one, the unknown frequency can be determined. The shape of the figure also depends on the initial phase difference.

If the frequency ratio is irrational, the trajectory is not closed and after a long enough time almost fills the whole rectangle $\lvert x\rvert\le A_x$, $\lvert y\rvert\le A_y$.

If two originally independent oscillations of nearby frequencies are weakly coupled physically, their frequency ratio may be "pulled" to a nearby simple integer ratio and remain locked there, a phenomenon called *frequency locking*, also known as synchronization. In 1665 Huygens observed that two pendulum clocks hung on the same beam gradually synchronize; the entrainment of biological clocks to the 24-hour day by circadian rhythms is another example of frequency locking.

![Lissajous figures x = cos(m t), y = cos(n t + phi) for frequency ratios 1:1, 1:2 and 2:3 (rows) and phase differences 0, pi/4 and pi/2 (columns)](./plots/lissajous.py)

| Direction of oscillations | Same frequency | Different frequencies |
|---|---|---|
| Same | Vector addition: the frequency is unchanged, the amplitude and phase change | Beats when the frequencies are close |
| Perpendicular | Line, circle or ellipse | Lissajous figure for an integer ratio; a trajectory that is not closed for an irrational ratio |

## 6.3. Harmonic Analysis

Simple harmonic motions can be combined into complicated oscillations; conversely, a complicated oscillation can be decomposed into a superposition of a series of simple harmonic motions, which is called *harmonic analysis* (Fourier analysis). An oscillation $x(t)$ of period $T$ (satisfying the Dirichlet conditions, [Theorem 9.3.1](/2.2.9#thm-9.3.1)) can be expanded as a **Fourier series**

$$
x(t)=\frac{a_0}{2}+\sum_{k=1}^{\infty}A_k\cos(k\omega t+\varphi_k),\qquad \omega=\frac{2\pi}{T}.
$$

- The component with $k=1$ is called the fundamental (fundamental tone); its frequency $\nu=1/T$ equals that of the original oscillation and determines the pitch;
- The components with $k=2,3,\dots$ are called the second, third, ... harmonics (overtones), and the relative strengths of the harmonics determine the timbre.

Plotting $A_k$ against $k\omega$ gives the spectrum of the oscillation. The spectrum of a periodic oscillation is discrete. For example, a symmetric square wave (equal to $+1$ for half of each period and $-1$ for the other half) contains only odd harmonics,

$$
x(t)=\frac4\pi\Big(\cos\omega t-\frac13\cos3\omega t+\frac15\cos5\omega t-\cdots\Big),
$$
with $A_{2n}=0$; partial sums of the first few terms approximate the square wave, with an overshoot of about $9\%$ that always remains near the discontinuities (the **Gibbs phenomenon**).

![Fourier synthesis of a square wave: partial sums with the first one, two, three and twenty odd harmonics (left) and its discrete amplitude spectrum A_k = 4/(pi k) for odd k (right)](./plots/square-wave-fourier.py)

A non-periodic oscillation (such as the sound of a single knock) can be regarded as the limit of an infinite period; its spectrum becomes continuous and is given by the **Fourier transform** ([2.5.6](/2.5.6)). The spectrum of a discrete signal measured in practice is computed with the **fast Fourier transform** ([4.4.4](/4.4.4#sec-4.7)). When a singer is praised for a "resonant voice, wide range and sweet timbre", these correspond respectively to a large amplitude (sound intensity), a wide range of variation of the fundamental frequency and pleasant harmonic content.

## 6.4. Damped Oscillation

A real oscillating system always does **work** against resistance, so its energy gradually decreases and the amplitude gradually decays; such an oscillation is called *damped oscillation*. At moderate speeds the resistance of the medium is proportional to the velocity, $f=-\gamma\dot x$, and the equation is

$$
m\frac{\mathrm{d}^2x}{\mathrm{d}t^2}=-kx-\gamma\frac{\mathrm{d}x}{\mathrm{d}t},
$$
that is,

$$
\ddot x+2\beta\dot x+\omega_0^2x=0,\qquad \omega_0=\sqrt{\frac km},\quad \beta=\frac{\gamma}{2m},
$$
where $\omega_0$ is the natural angular frequency and $\beta$ is called the damping coefficient. This is the equation $x''+2kx'+\omega^2x=0$ of [2.2.16](/2.2.16#sec-16.5.1) (the $k$ and $\omega$ there correspond to $\beta$ and $\omega_0$ here); the solutions and graphs for the three cases are given in that section:

1. Underdamping ($\beta<\omega_0$):
   $$
   x=A_0\mathrm{e}^{-\beta t}\cos(\omega_{\mathrm{d}}t+\varphi_0),\qquad \omega_{\mathrm{d}}=\sqrt{\omega_0^2-\beta^2},
   $$
   where $\mathrm{e}^{-\beta t}$ is the decay factor. This is a quasi-periodic motion whose amplitude decays exponentially, with period $T_{\mathrm{d}}=2\pi/\omega_{\mathrm{d}}$ longer than the natural period of the system: the resistance makes the particle slightly slower each time it returns to the equilibrium position.
2. Overdamping ($\beta>\omega_0$): a non-periodic motion in which the particle returns slowly to the equilibrium position.
3. Critical damping ($\beta=\omega_0$): the boundary at which oscillation just ceases, and among non-periodic motions the one in which the particle returns to equilibrium in the shortest time. Electric meter needles, balances and automobile shock absorbers are designed near critical damping so that the needle or the body comes quickly to rest without swinging back and forth.

For weak damping ($\beta\ll\omega_0$), the amplitude is $A=A_0\mathrm{e}^{-\beta t}$ and the energy $E\propto A^2$ is

$$
E=E_0\mathrm{e}^{-2\beta t}.
$$
The time $\tau=\dfrac1{2\beta}$ taken for the energy to fall to $1/\mathrm{e}$ of its initial value is called the ring-down time. The more oscillations occur within $\tau$, the better the "quality" of the oscillation.

**Definition 6.4.1 (Quality Factor)** The **quality factor** of a weakly damped oscillation is

$$
Q=2\pi\frac{\tau}{T}=\omega_0\tau=\frac{\omega_0}{2\beta},
$$
where $T$ and $\omega_0$ are the natural period and natural angular frequency of the system. Equivalently, $Q$ equals $2\pi$ times the ratio of the energy stored in the system to the energy lost per period.

The quality factor $Q$ is dimensionless. Typical values: $Q\sim10^2$ for a radio $LC$ oscillating circuit, $Q\sim10^3$ for tuning forks and piano strings, $Q\sim10^5$ for quartz crystal oscillators, and up to $10^7$ and beyond for the optical resonator of a laser.

## 6.5. Forced Oscillation

### 6.5.1. Equation of Motion and the Steady-State Solution

The oscillation of a system under a periodic external force (driving force) $F_0\cos\omega t$ is called *forced oscillation*. The equation is

$$
m\frac{\mathrm{d}^2x}{\mathrm{d}t^2}=-kx-\gamma\frac{\mathrm{d}x}{\mathrm{d}t}+F_0\cos\omega t,\qquad \ddot x+2\beta\dot x+\omega_0^2x=\frac{F_0}{m}\cos\omega t .
$$
Its general solution is the sum of the general solution of the homogeneous equation (damped oscillation) and a particular solution ([2.2.16](/2.2.16#sec-16.5.2)). The damped part decays with time and is the transient solution; after a sufficiently long time only the steady-state solution remains,

$$
x=A\cos(\omega t+\varphi_0),\qquad
A=\frac{F_0/m}{\sqrt{(\omega_0^2-\omega^2)^2+4\beta^2\omega^2}},\qquad
\tan\varphi_0=-\frac{2\beta\omega}{\omega_0^2-\omega^2},\quad -\pi<\varphi_0<0 .
$$
The particular solution is easiest to find with complex numbers: let $\tilde x=\tilde A\mathrm{e}^{\mathrm{i}\omega t}$ satisfy $\ddot{\tilde x}+2\beta\dot{\tilde x}+\omega_0^2\tilde x=\frac{F_0}m\mathrm{e}^{\mathrm{i}\omega t}$; then $\tilde A=\dfrac{F_0/m}{\omega_0^2-\omega^2+2\mathrm{i}\beta\omega}$, $A=\lvert\tilde A\rvert$ and $\varphi_0=\arg\tilde A$.

The steady-state solution resembles simple harmonic motion in form, but it is not the same thing:

- The system oscillates at the frequency $\omega$ of the driving force, not at the natural frequency $\omega_0$;
- $A$ and $\varphi_0$ are functions of $F_0/m$, $\omega$, $\omega_0$ and $\beta$ and are independent of the initial state $x_0$, $v_0$;
- $\varphi_0$ is the phase by which the displacement lags the driving force: for $\omega\ll\omega_0$, $\varphi_0\approx0$ and the displacement is in phase with the driving force; for $\omega=\omega_0$, $\varphi_0=-\frac\pi2$; for $\omega\gg\omega_0$, $\varphi_0\to-\pi$ and the displacement is in antiphase with the driving force.

### 6.5.2. Resonance

When the frequency of the driving force is close to the natural frequency of the system, the amplitude of the forced oscillation increases sharply; this phenomenon is called **resonance**.

- Displacement resonance: $A(\omega)$ attains its maximum at $\omega_{\mathrm{r}}=\sqrt{\omega_0^2-2\beta^2}$ (when $\beta<\omega_0/\sqrt2$), with value $A_{\mathrm{r}}=\dfrac{F_0}{2m\beta\sqrt{\omega_0^2-\beta^2}}$. The smaller the damping, the higher and sharper the resonance peak and the closer $\omega_{\mathrm{r}}$ is to $\omega_0$.
- Velocity resonance: the velocity amplitude $v_{\mathrm{m}}=\omega A=\dfrac{F_0/m}{\sqrt{(\omega_0^2-\omega^2)^2/\omega^2+4\beta^2}}$ attains its maximum $\dfrac{F_0}{2m\beta}$ exactly at $\omega=\omega_0$, independently of the damping.

At $\omega=\omega_0$, $\varphi_0=-\frac\pi2$ and

$$
v=\frac{\mathrm{d}x}{\mathrm{d}t}=\omega A\cos\Big(\omega t+\varphi_0+\frac\pi2\Big)=\omega A\cos\omega t,
$$
so the velocity is in phase with the driving force, the driving force always does positive work, and the system absorbs the maximum energy from its surroundings. In general, the average **power** of the driving force, $\bar P=\frac12F_0v_{\mathrm{m}}\cos(\varphi_0+\frac\pi2)$, is largest at $\omega_0$; for weak damping the difference between the two frequencies at which $\bar P$ drops to half its peak (the width of the resonance peak) is $\Delta\omega=2\beta$, so

$$
Q=\frac{\omega_0}{\Delta\omega},
$$
and the higher the quality factor, the narrower the resonance peak and the better the frequency selectivity of the system. For weak damping $\omega_{\mathrm{r}}\approx\omega_0$, the two kinds of resonance occur at almost the same frequency, and the peak amplitude is $A_{\mathrm{r}}\approx Q\cdot\dfrac{F_0}{k}$, that is, $Q$ times the displacement produced by a static force of the same magnitude.

![Steady-state response of a driven damped oscillator for quality factors Q = 0.5, 1, 2, 5 and 10: amplitude A k / F0 (left) and phase phi0 of the displacement relative to the driving force (right) versus omega / omega0; all phase curves pass through -pi/2 at omega = omega0](./plots/forced-response.py)

Both the use and the avoidance of resonance are important. A radio selects a station by the electrical resonance of an $LC$ circuit (the equation of a series $RLC$ circuit has the same form as that of forced oscillation; see [5.3.9](/5.3.9)); nuclear magnetic resonance and the sound boxes of musical instruments also rely on resonance. On the other hand, machines, buildings and bridges must avoid having natural frequencies close to frequently occurring driving frequencies. Resonance was understood in ancient China: according to the *Tianzhong Ji*, a man of Shu owned a bronze basin that sounded by itself morning and evening; Zhang Hua explained that it resonated with the bells of the palace and that changing the thickness of the basin would remove the effect. A wine glass can be shattered by sustained excitation with sound at its natural frequency.

The collapse of the Tacoma Narrows Bridge in the United States in 1940, after violent torsional oscillation in a strong wind, is often cited as an example of resonance, but this is inaccurate: the wind speed was roughly steady, and there was no periodic driving force at the natural frequency of the bridge. The torsional oscillation of the bridge made the force exerted on the deck by the surrounding airflow synchronous with the oscillation, which acts as negative damping, so that the amplitude grew by self-excitation. This is aeroelastic flutter (self-excited oscillation), whose mechanism differs from that of forced resonance.

**Example 6.5.1 (Atomic Force Microscope)** The probe of an atomic force microscope (AFM) is mounted at the end of a microcantilever; in dynamic mode a piezoelectric element drives it at a frequency close to the natural frequency of the cantilever. As the probe approaches the sample surface, the gradient of the interatomic force effectively changes the stiffness of the cantilever and shifts its resonance frequency, so that at a fixed driving frequency the amplitude and phase change. This change is measured with a laser (beam deflection or interferometry), the height of the probe is adjusted by feedback control, and scanning yields the topography of the surface. The higher the $Q$ of the cantilever, the steeper the resonance curve and the more sensitive the measurement.

## Summary

| Oscillation | Equation | Solution and features |
|---|---|---|
| Simple harmonic motion | $\ddot x+\omega_0^2x=0$ | $x=A\cos(\omega_0t+\varphi_0)$; $\omega_0$ is determined by the system, $A$ and $\varphi_0$ by the initial conditions; $E=\frac12kA^2$ |
| Damped oscillation | $\ddot x+2\beta\dot x+\omega_0^2x=0$ | Underdamped $A_0\mathrm{e}^{-\beta t}\cos(\omega_{\mathrm{d}}t+\varphi_0)$, critically damped, overdamped; $Q=\omega_0/(2\beta)$ |
| Forced oscillation | $\ddot x+2\beta\dot x+\omega_0^2x=\frac{F_0}m\cos\omega t$ | Steady state $A\cos(\omega t+\varphi_0)$ at the driving frequency, with $A$ and $\varphi_0$ independent of the initial conditions; resonance at $\omega\approx\omega_0$ |

Superposition of simple harmonic motions: collinear motions of the same frequency add as rotating vectors; collinear motions of different frequencies produce beats with beat frequency $\lvert\nu_1-\nu_2\rvert$; perpendicular oscillations combine into a line, an ellipse or a Lissajous figure. Any periodic oscillation can be decomposed into a superposition of the fundamental and its harmonics (Fourier series).

## Questions

1. Why is the period of a damped oscillation longer than that of the undamped one?

   **Answer** $\omega_{\mathrm{d}}=\sqrt{\omega_0^2-\beta^2}<\omega_0$; physically, resistance always slows the motion of the particle.

2. When a spring oscillator hangs vertically, does gravity change the period of oscillation?

   **Answer** No. Taking the new equilibrium position (where the spring is already stretched by $mg/k$) as origin, the restoring force is still $-kx$ and $\omega=\sqrt{k/m}$ is unchanged; only the equilibrium position moves down.

3. After a forced oscillation has reached the steady state, where does the work done by the driving force over one period go?

   **Answer** It is entirely dissipated by the resistance (converted into heat), and the average mechanical energy of the system stays constant.
