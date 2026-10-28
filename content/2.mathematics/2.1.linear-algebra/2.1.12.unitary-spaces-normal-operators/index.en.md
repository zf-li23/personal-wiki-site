---
title: Unitary Spaces and Normal Operators
source_hash: 717ee5d4a2c6
---

[Chapter 4](/2.1.4) used the **inner product** on $\mathbb{R}^n$ to define length, angle and orthogonality, and from them obtained Gram–Schmidt orthogonalization, the **QR decomposition**, **orthogonal projection** and least squares. Those results use only three properties of the inner product: symmetry, bilinearity and positive definiteness. This chapter takes these three properties as axioms and generalizes in two directions: first, inner products are placed on arbitrary vector spaces, so that function spaces and matrix spaces also acquire lengths and angles; second, the real numbers are replaced by the complex numbers, and symmetry is replaced accordingly by conjugate symmetry. Wherever a proof is the same as in the case of $\mathbb{R}^n$, we only sketch it.

The central question of the chapter is: under what conditions does a **linear transformation** admit an orthonormal basis in which its matrix is diagonal? On $\mathbb{R}^n$, [Chapter 7](/2.1.7) proved that real symmetric matrices can be orthogonally diagonalized (Theorem 7.1.1). Over the complex numbers the answer is the spectral theorem: exactly the normal operators ($TT^* = T^*T$). The **spectral decomposition** of real symmetric matrices will be recovered as a corollary of the spectral theorem. The proof follows a standard breakdown: the Schur triangularization of [Chapter 10](/2.1.10) combined with the QR decomposition gives unitary triangularization, and normality then forces the triangular matrix to be diagonal. Computationally, unitary diagonalization amounts to finding the eigenvalues and applying Gram–Schmidt orthogonalization within each **eigenspace**.

## 12.1. Inner Product Spaces

First recall the dot product $\boldsymbol{u} \cdot \boldsymbol{v} = \boldsymbol{u}^{\mathsf T}\boldsymbol{v}$ on $\mathbb{R}^3$. Let $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2, \boldsymbol{\alpha}_3$ be a basis of $\mathbb{R}^3$, $\boldsymbol{\alpha} = \sum x_i\boldsymbol{\alpha}_i$ and $\boldsymbol{\beta} = \sum y_j\boldsymbol{\alpha}_j$. Then

$$
\boldsymbol{\alpha} \cdot \boldsymbol{\beta} = \sum_{i,j}x_iy_j(\boldsymbol{\alpha}_i \cdot \boldsymbol{\alpha}_j) = \boldsymbol{x}^{\mathsf T}G\boldsymbol{y}, \qquad G = (\boldsymbol{\alpha}_i \cdot \boldsymbol{\alpha}_j)_{3 \times 3},
$$

and $G$ is called the **Gram matrix** (or metric matrix) of the dot product with respect to this basis; it is a real symmetric positive definite matrix, and $G = I$ when the basis is orthonormal. Conversely, any real symmetric positive definite matrix $G$ makes $\boldsymbol{x}^{\mathsf T}G\boldsymbol{y}$ a "metric" on $\mathbb{R}^3$. This suggests keeping only the algebraic properties of the dot product.

**Definition 12.1.1 (Inner Product Space)** Let $\mathbb{F} = \mathbb{R}$ or $\mathbb{C}$ and let $V$ be a vector space over $\mathbb{F}$. A map $\langle \cdot, \cdot \rangle\colon V \times V \to \mathbb{F}$ is called an inner product on $V$ if for all $\alpha, \beta, \gamma \in V$ and $c_1, c_2 \in \mathbb{F}$ it satisfies the following three conditions; $(V, \langle \cdot, \cdot \rangle)$ is then called an **inner product space**. For $\mathbb{F} = \mathbb{R}$ and $\dim V < \infty$ it is called a **Euclidean space**, and for $\mathbb{F} = \mathbb{C}$ and $\dim V < \infty$ a **unitary space**:

1. conjugate symmetry: $\langle \alpha, \beta \rangle = \overline{\langle \beta, \alpha \rangle}$;
2. linearity in the first argument: $\langle c_1\alpha + c_2\beta, \gamma \rangle = c_1\langle \alpha, \gamma \rangle + c_2\langle \beta, \gamma \rangle$;
3. positive definiteness: $\langle \alpha, \alpha \rangle \ge 0$, and $\langle \alpha, \alpha \rangle = 0 \Leftrightarrow \alpha = 0$.

For $\mathbb{F} = \mathbb{R}$ conjugate symmetry is just symmetry, and the inner product is bilinear. For $\mathbb{F} = \mathbb{C}$, conditions 1 and 2 imply that the inner product is conjugate linear in the second argument: $\langle \alpha, c\beta \rangle = \bar c\langle \alpha, \beta \rangle$. This course (like most textbooks) takes inner products to be linear in the first argument; the physics literature (for example Dirac notation in quantum mechanics) usually takes them to be linear in the second argument, and the conjugates in formulas move accordingly.

**Example 12.1.1** The inner products $\langle \boldsymbol{\alpha}, \boldsymbol{\beta} \rangle = \boldsymbol{\alpha}^{\mathsf T}\boldsymbol{\beta}$ on $\mathbb{R}^n$ and

$$
\langle \boldsymbol{\alpha}, \boldsymbol{\beta} \rangle = \boldsymbol{\alpha}^{\mathsf T}\bar{\boldsymbol{\beta}} = \boldsymbol{\beta}^{\mathsf H}\boldsymbol{\alpha} = x_1\bar y_1 + \cdots + x_n\bar y_n
$$

on $\mathbb{C}^n$ are both called standard inner products. In the complex case the conjugate is essential: with $\langle \alpha, \beta \rangle = \alpha\beta$ on $\mathbb{C}$ we would get $\langle \mathrm{i}, \mathrm{i} \rangle = -1 < 0$, violating positive definiteness, whereas $\mathrm{i} \cdot \bar{\mathrm{i}} = 1$. For example, for $\boldsymbol{\alpha} = (1, \mathrm{i})^{\mathsf T}$ and $\boldsymbol{\beta} = (1 + \mathrm{i}, 2\mathrm{i})^{\mathsf T}$,

$$
\langle \boldsymbol{\alpha}, \boldsymbol{\beta} \rangle = 1 \cdot (1 - \mathrm{i}) + \mathrm{i} \cdot (-2\mathrm{i}) = 3 - \mathrm{i}, \qquad \langle \boldsymbol{\alpha}, \boldsymbol{\alpha} \rangle = 2, \qquad \langle \boldsymbol{\beta}, \boldsymbol{\beta} \rangle = 6.
$$

**Example 12.1.2** Let $A \in \mathbb{R}^{n\times n}$. Then $\langle \boldsymbol{\alpha}, \boldsymbol{\beta} \rangle = \boldsymbol{\alpha}^{\mathsf T}A\boldsymbol{\beta}$ is an inner product on $\mathbb{R}^n$ $\Leftrightarrow$ $A$ is a real symmetric **positive definite matrix**: symmetry $\Leftrightarrow$ $\boldsymbol{\alpha}^{\mathsf T}A\boldsymbol{\beta} = \boldsymbol{\beta}^{\mathsf T}A\boldsymbol{\alpha}$ for all $\boldsymbol{\alpha}, \boldsymbol{\beta}$ $\Leftrightarrow$ $A = A^{\mathsf T}$; linearity holds automatically; positive definiteness $\Leftrightarrow$ $\boldsymbol{\alpha}^{\mathsf T}A\boldsymbol{\alpha} > 0$ ($\boldsymbol{\alpha} \ne \boldsymbol{0}$). For the corresponding complex result (positive definite Hermitian matrices), see [Chapter 13](/2.1.13).

**Example 12.1.3** On $C[a, b]$ (the real continuous functions on $[a, b]$), $\langle f, g \rangle = \int_a^b f(t)g(t)\,\mathrm{d}t$ is an inner product. It is the continuous version of the dot product on $\mathbb{R}^n$: $\int_a^b fg\,\mathrm{d}t = \lim_{n \to \infty}\frac{b - a}{n}\sum_i f(t_i)g(t_i)$. Positive definiteness holds because the integral of a nonnegative continuous function vanishes if and only if the function vanishes identically. Since $C[a, b]$ is infinite-dimensional, it is an inner product space but not a Euclidean space.

**Example 12.1.4** On $\mathbb{R}^{n\times n}$, $\langle A, B \rangle = \operatorname{tr}(AB^{\mathsf T}) = \sum_{i,j}a_{ij}b_{ij}$, and on $\mathbb{C}^{n\times n}$, $\langle A, B \rangle = \operatorname{tr}(AB^{\mathsf H})$; this is called the *Frobenius inner product*. It is the standard inner product obtained by regarding a matrix as a vector with $n^2$ entries; the property $\operatorname{tr}(AB^{\mathsf T}) = \operatorname{tr}(BA^{\mathsf T})$ of the **trace** gives symmetry, and $\operatorname{tr}(AA^{\mathsf T}) = \sum a_{ij}^2$ gives positive definiteness.

In general, let $\alpha_1, \dots, \alpha_n$ be a basis of an inner product space $V$. The matrix $G = (\langle \alpha_i, \alpha_j \rangle)_{n \times n}$ is called the metric matrix of the inner product with respect to this basis; it is the **Gram matrix** of these vectors (Definition 11.2.2 of [Chapter 11](/2.1.11) is the special case of the integral inner product on a function space). If $\alpha = \sum x_i\alpha_i$ and $\beta = \sum y_j\alpha_j$, then

$$
\langle \alpha, \beta \rangle = \sum_{i,j}x_i\bar y_j\langle \alpha_i, \alpha_j \rangle = \boldsymbol{x}^{\mathsf T}G\bar{\boldsymbol{y}}.
$$

Conjugate symmetry gives $G^{\mathsf H} = G$, and positive definiteness makes $G$ positive definite. So once a basis is fixed, inner products on an $n$-dimensional Euclidean (unitary) space correspond one-to-one to positive definite real symmetric (Hermitian) matrices of order $n$; the basis is orthonormal if and only if $G = I$.

## 12.2. Length, Angle and Orthogonality

**Definition 12.2.1** Let $V$ be an inner product space and $\alpha, \beta \in V$. The number $\|\alpha\| = \sqrt{\langle \alpha, \alpha \rangle}$ is called the length of $\alpha$; if $\|\alpha\| = 1$, $\alpha$ is called a unit vector, and for $\alpha \ne 0$ the vector $\alpha / \|\alpha\|$ is a unit vector (normalization). If $\langle \alpha, \beta \rangle = 0$, then $\alpha$ and $\beta$ are called orthogonal, written $\alpha \perp \beta$. For nonzero $\alpha, \beta$ the angle $\theta$ is defined by

- in a real inner product space: $\cos\theta = \dfrac{\langle \alpha, \beta \rangle}{\|\alpha\|\,\|\beta\|}$, $0 \le \theta \le \pi$;
- in a complex inner product space: $\cos\theta = \dfrac{|\langle \alpha, \beta \rangle|}{\|\alpha\|\,\|\beta\|}$, $0 \le \theta \le \dfrac{\pi}{2}$.

In the complex case $\langle \alpha, \beta \rangle$ is a complex number, so only its modulus can be used, and the angle therefore lies in $[0, \pi/2]$, with $\theta = \pi/2$ exactly when $\alpha \perp \beta$. The definition of the angle requires $|\cos\theta| \le 1$, which is precisely the Cauchy–Schwarz inequality.

**Property 12.2.1** Let $V$ be an inner product space, $\alpha, \beta \in V$ and $c \in \mathbb{F}$.

1. $\|\alpha\| = 0 \Leftrightarrow \alpha = 0$; $\|c\alpha\| = |c|\,\|\alpha\|$.
2. (Pythagorean theorem) If $\alpha \perp \beta$, then $\|\alpha \pm \beta\|^2 = \|\alpha\|^2 + \|\beta\|^2$.
3. (**Cauchy–Schwarz inequality**) $|\langle \alpha, \beta \rangle| \le \|\alpha\|\,\|\beta\|$, with equality if and only if $\alpha, \beta$ are linearly dependent.
4. (**Triangle inequality**) $\|\alpha + \beta\| \le \|\alpha\| + \|\beta\|$.

**Proof** 2: $\|\alpha - \beta\|^2 = \langle \alpha, \alpha \rangle - \langle \alpha, \beta \rangle - \langle \beta, \alpha \rangle + \langle \beta, \beta \rangle$, and the two middle terms vanish.

3: The case $\beta = 0$ is trivial. Let $\beta \ne 0$ and let $\alpha_p = t\beta$ be the projection of $\alpha$ onto $\beta$, that is, require $\langle \alpha - t\beta, \beta \rangle = 0$, which gives $t = \dfrac{\langle \alpha, \beta \rangle}{\langle \beta, \beta \rangle}$. By the Pythagorean theorem, $\|\alpha\|^2 = \|\alpha - \alpha_p\|^2 + \|\alpha_p\|^2 \ge \|\alpha_p\|^2 = \dfrac{|\langle \alpha, \beta \rangle|^2}{\|\beta\|^2}$. Equality holds $\Leftrightarrow$ $\alpha = \alpha_p$ $\Leftrightarrow$ $\alpha, \beta$ are linearly dependent.

4: $\|\alpha + \beta\|^2 = \|\alpha\|^2 + 2\operatorname{Re}\langle \alpha, \beta \rangle + \|\beta\|^2 \le \|\alpha\|^2 + 2\|\alpha\|\,\|\beta\| + \|\beta\|^2$, using $\operatorname{Re}\langle \alpha, \beta \rangle \le |\langle \alpha, \beta \rangle|$ and 3. $\square$

In the complex case the converse of the Pythagorean theorem fails: $\|\alpha + \beta\|^2 = \|\alpha\|^2 + \|\beta\|^2$ only says that $\operatorname{Re}\langle \alpha, \beta \rangle = 0$. For example, in $\mathbb{C}$ we have $\|1 + \mathrm{i}\|^2 = 2 = \|1\|^2 + \|\mathrm{i}\|^2$, but $\langle 1, \mathrm{i} \rangle = \bar{\mathrm{i}} = -\mathrm{i} \ne 0$.

## 12.3. Orthonormal Bases and Unitary Matrices

**Definition 12.3.1** Vectors $u_1, \dots, u_k$ in an inner product space $V$ with $\langle u_i, u_j \rangle = \delta_{ij}$ are called an orthonormal set; if $V$ is finite-dimensional and $k = \dim V$, then $u_1, \dots, u_k$ is called an orthonormal basis of $V$.

**Property 12.3.1** Let $u_1, \dots, u_k$ be an orthonormal set.

1. $u_1, \dots, u_k$ are linearly independent: if $\sum c_ju_j = 0$, taking the inner product with $u_i$ gives $c_i = 0$;
2. if $v = x_1u_1 + \cdots + x_ku_k$, then $x_i = \langle v, u_i \rangle$;
3. if $v = \sum x_iu_i$ and $w = \sum y_iu_i$, then $\langle v, w \rangle = \sum_i x_i\bar y_i = \boldsymbol{x}^{\mathsf T}\bar{\boldsymbol{y}}$ and $\|v\|^2 = \sum|x_i|^2$.

Thus in an **orthonormal basis**, coordinates are obtained by taking inner products, and inner products are obtained by taking the standard inner product of coordinates: computationally, an abstract unitary space is no different from $\mathbb{C}^n$.

**Example 12.3.1** Let $\omega = \mathrm{e}^{2\pi \mathrm{i}/3}$ and give $\mathbb{C}^3$ the standard inner product. The vectors

$$
\boldsymbol{v}_1 = \tfrac{1}{\sqrt3}(1, 1, 1)^{\mathsf T}, \qquad \boldsymbol{v}_2 = \tfrac{1}{\sqrt3}(1, \omega, \omega^2)^{\mathsf T}, \qquad \boldsymbol{v}_3 = \tfrac{1}{\sqrt3}(1, \omega^2, \omega^4)^{\mathsf T}
$$

form an orthonormal basis. For example, $\langle \boldsymbol{v}_2, \boldsymbol{v}_1 \rangle = \frac13(1 + \omega + \omega^2) = 0$, $\langle \boldsymbol{v}_3, \boldsymbol{v}_2 \rangle = \frac13(1 + \omega^2\bar\omega + \omega^4\bar\omega^2) = \frac13(1 + \omega + \omega^2) = 0$ (since $\bar\omega = \omega^2$ and $\omega^3 = 1$), and $\langle \boldsymbol{v}_2, \boldsymbol{v}_2 \rangle = \frac13(1 + 1 + 1) = 1$.

**Example 12.3.2** On $C[-\pi, \pi]$ with the integral inner product, the functions

$$
\frac{1}{\sqrt{2\pi}}, \quad \frac{\cos x}{\sqrt\pi}, \quad \frac{\sin x}{\sqrt\pi}, \quad \frac{\cos 2x}{\sqrt\pi}, \quad \frac{\sin 2x}{\sqrt\pi}, \quad \dots
$$

form an orthonormal set (for example, $\int_{-\pi}^\pi \sin x\cos x\,\mathrm{d}x = \frac12\int_{-\pi}^\pi \sin 2x\,\mathrm{d}x = 0$). The coordinates given by part 2 of Property 12.3.1 are the Fourier coefficients.

In $\mathbb{C}^n$, let $A = (\boldsymbol{u}_1, \dots, \boldsymbol{u}_n)$. Then $\boldsymbol{u}_1, \dots, \boldsymbol{u}_n$ is an orthonormal basis $\Leftrightarrow$ $\boldsymbol{u}_j^{\mathsf H}\boldsymbol{u}_i = \delta_{ij}$ $\Leftrightarrow$ $A^{\mathsf H}A = I_n$. In the real case this is an **orthogonal matrix**.

**Definition 12.3.2 (Unitary Matrix)** A complex square matrix $A$ with $A^{\mathsf H}A = AA^{\mathsf H} = I_n$ (that is, $A^{-1} = A^{\mathsf H}$) is called a **unitary matrix**.

**Property 12.3.2** Let $A, B$ be unitary matrices of order $n$.

1. The columns (rows) of $A$ form an orthonormal basis of $\mathbb{C}^n$;
2. $AB$ and $A^{-1} = A^{\mathsf H}$ are also unitary, and the unitary matrices of order $n$ form the group $U(n)$ ([1.3.5](/1.3.5));
3. $\langle A\boldsymbol{x}, A\boldsymbol{y} \rangle = \langle \boldsymbol{x}, \boldsymbol{y} \rangle$ and $\|A\boldsymbol{x}\| = \|\boldsymbol{x}\|$;
4. the eigenvalues of $A$ have modulus $1$, and $|\det A| = 1$.

**Proof** 3: $\langle A\boldsymbol{x}, A\boldsymbol{y} \rangle = \boldsymbol{y}^{\mathsf H}A^{\mathsf H}A\boldsymbol{x} = \boldsymbol{y}^{\mathsf H}\boldsymbol{x}$. 4: Let $A\boldsymbol{x} = \lambda \boldsymbol{x}$ with $\boldsymbol{x} \ne \boldsymbol{0}$. By 3, $\|\boldsymbol{x}\| = \|A\boldsymbol{x}\| = |\lambda|\,\|\boldsymbol{x}\|$, so $|\lambda| = 1$; $|\det A|$ is the product of the moduli of the eigenvalues. $\square$

**Example 12.3.3**

1. If $Q$ is a real orthogonal matrix and $|z| = 1$, then $zQ$ is unitary: $(zQ)^{\mathsf H}(zQ) = \bar zzQ^{\mathsf T}Q = I$.
2. If $A^{\mathsf H} = A$, then $\mathrm{e}^{\mathrm{i}A}$ is unitary: by the power series definition $(\mathrm{e}^{\mathrm{i}A})^{\mathsf H} = \mathrm{e}^{(\mathrm{i}A)^{\mathsf H}} = \mathrm{e}^{-\mathrm{i}A}$, and since $\mathrm{i}A$ and $-\mathrm{i}A$ commute, $\mathrm{e}^{-\mathrm{i}A}\mathrm{e}^{\mathrm{i}A} = \mathrm{e}^O = I$ (Theorem 11.8.1 of [Chapter 11](/2.1.11)). This is the matrix version of $|\mathrm{e}^{\mathrm{i}\theta}| = 1$ for real $\theta$.
3. Taking the three vectors of Example 12.3.1 as columns gives the unitary matrix $F_3 = \frac{1}{\sqrt3}(\omega^{jk})_{j,k=0,1,2}$. In general, $F_n = \frac{1}{\sqrt n}(\omega_n^{jk})$ ($\omega_n = \mathrm{e}^{2\pi \mathrm{i}/n}$) is the matrix of the discrete Fourier transform. Computing $F_n\boldsymbol{x}$ directly takes $n^2$ multiplications; the fast Fourier transform exploits the block structure of $F_n$ to reduce the cost to $O(n\log n)$.

![Four columns of the unitary matrix F_16: the real and imaginary parts of column k are the cosine and sine of frequency k sampled at 16 equally spaced points (thin lines show the corresponding continuous functions); these columns form an orthonormal basis of C^16](./plots/dft-basis.py)

## 12.4. Gram–Schmidt Orthogonalization

**Algorithm 12.4.1 (Gram–Schmidt Process)** Input: linearly independent vectors $v_1, \dots, v_k$ in an inner product space $V$.

1. $w_1 = v_1$, $q_1 = w_1 / \|w_1\|$;
2. for $j = 2, \dots, k$: $w_j = v_j - \sum_{i=1}^{j-1}\langle v_j, q_i \rangle q_i$ (subtract the projection of $v_j$ onto $\operatorname{span}\{q_1, \dots, q_{j-1}\}$), $q_j = w_j / \|w_j\|$.

The output is an orthonormal set $q_1, \dots, q_k$ with $\operatorname{span}\{q_1, \dots, q_l\} = \operatorname{span}\{v_1, \dots, v_l\}$ for every $l \le k$.

The proof of correctness is the same as in [Chapter 4](/2.1.4): $\langle w_j, q_l \rangle = \langle v_j, q_l \rangle - \langle v_j, q_l \rangle = 0$ ($l < j$), and $w_j \ne 0$ because $v_j \notin \operatorname{span}\{v_1, \dots, v_{j-1}\}$. In the complex case, note that the coefficient is $\langle v_j, q_i \rangle$ and not $\langle q_i, v_j \rangle$; the two are complex conjugates of each other. We obtain:

**Theorem 12.4.1** Every finite-dimensional inner product space has an orthonormal basis, and every orthonormal set can be extended to an orthonormal basis. In matrix language, a matrix $A = (\boldsymbol{v}_1, \dots, \boldsymbol{v}_k) \in \mathbb{C}^{n \times k}$ of full column rank can be factored as $A = QR$ with $Q^{\mathsf H}Q = I_k$ and $R$ upper triangular with positive diagonal entries, where $r_{ij} = \langle \boldsymbol{v}_j, \boldsymbol{q}_i \rangle = \boldsymbol{q}_i^{\mathsf H}\boldsymbol{v}_j$ ($i < j$) and $r_{jj} = \|w_j\|$.

**Example 12.4.1** Give $\mathbb{C}^3$ the standard inner product and let $\boldsymbol{v}_1 = (1, 0, \mathrm{i})^{\mathsf T}$, $\boldsymbol{v}_2 = (-1, \mathrm{i}, 1)^{\mathsf T}$, $\boldsymbol{v}_3 = (1, -1, 1)^{\mathsf T}$.

1. $\|\boldsymbol{v}_1\|^2 = 1 + 0 + |\mathrm{i}|^2 = 2$, $\boldsymbol{q}_1 = \frac{1}{\sqrt2}(1, 0, \mathrm{i})^{\mathsf T}$.
2. $\langle \boldsymbol{v}_2, \boldsymbol{q}_1 \rangle = \frac{1}{\sqrt2}(-1 \cdot 1 + 1 \cdot \bar{\mathrm{i}}) = \frac{-1 - \mathrm{i}}{\sqrt2}$, $\boldsymbol{w}_2 = \boldsymbol{v}_2 - \langle \boldsymbol{v}_2, \boldsymbol{q}_1 \rangle \boldsymbol{q}_1 = \left(\frac{-1 + \mathrm{i}}{2}, \mathrm{i}, \frac{1 + \mathrm{i}}{2}\right)^{\mathsf T}$, $\|\boldsymbol{w}_2\|^2 = 2$, $\boldsymbol{q}_2 = \boldsymbol{w}_2 / \sqrt2$.
3. $\boldsymbol{w}_3 = \boldsymbol{v}_3 - \langle \boldsymbol{v}_3, \boldsymbol{q}_1 \rangle \boldsymbol{q}_1 - \langle \boldsymbol{v}_3, \boldsymbol{q}_2 \rangle \boldsymbol{q}_2 = \left(\frac{1 + \mathrm{i}}{2}, -1, \frac{1 - \mathrm{i}}{2}\right)^{\mathsf T}$, $\|\boldsymbol{w}_3\|^2 = 2$, $\boldsymbol{q}_3 = \boldsymbol{w}_3 / \sqrt2$.

One can check that $\langle \boldsymbol{w}_3, \boldsymbol{q}_1 \rangle = \frac{1}{\sqrt2}\left(\frac{1 + \mathrm{i}}{2} + \frac{1 - \mathrm{i}}{2}\cdot(-\mathrm{i})\right) = 0$. The third component of $\boldsymbol{w}_3$ must be $\frac{1 - \mathrm{i}}{2}$: the value $\frac{-1 - \mathrm{i}}{2}$ would give $\langle \boldsymbol{w}_3, \boldsymbol{v}_1 \rangle = \mathrm{i} \ne 0$.

**Example 12.4.2** On $\mathcal{P}_2(\mathbb{R}) = \{a_0 + a_1x + a_2x^2\}$ with $\langle f, g \rangle = \int_{-1}^1 f(x)g(x)\,\mathrm{d}x$, orthogonalize $1, x, x^2$:

1. $\|1\|^2 = 2$, $q_1 = \frac{1}{\sqrt2}$;
2. $\langle x, q_1 \rangle = 0$, $w_2 = x$, $\|x\|^2 = \frac23$, $q_2 = \sqrt{\frac32}\,x$;
3. $\langle x^2, q_1 \rangle = \frac{\sqrt2}{3}$, $\langle x^2, q_2 \rangle = 0$, $w_3 = x^2 - \frac13$, $\|w_3\|^2 = \int_{-1}^1(x^2 - \frac13)^2\,\mathrm{d}x = \frac{8}{45}$, $q_3 = \sqrt{\frac{45}{8}}\left(x^2 - \frac13\right)$.

$q_1, q_2, q_3$ are the normalized *Legendre polynomials* $1, x, \frac12(3x^2 - 1)$. Continuing the orthogonalization with $x^3, x^4, \dots$ produces all Legendre polynomials, which appear again and again in approximation theory and partial differential equations.

In numerical computation, classical Gram–Schmidt gradually loses orthogonality because of rounding errors; in practice the QR decomposition is computed by modified Gram–Schmidt or by **Householder reflections** ([Chapter 4](/2.1.4)).

## 12.5. Orthogonal Complements and Orthogonal Projections

**Definition 12.5.1 (Orthogonal Complement)** Let $V$ be an inner product space and $W$ a subspace. The set $W^\perp = \{v \in V \mid \langle v, w \rangle = 0, \forall w \in W\}$ is called the **orthogonal complement** of $W$; it is a subspace of $V$.

**Example 12.5.1** In $\mathbb{R}^n$ (with the standard inner product), $\mathcal{R}(A)^\perp = \mathcal{N}(A^{\mathsf T})$ and $\mathcal{R}(A^{\mathsf T})^\perp = \mathcal{N}(A)$. In $\mathbb{C}^n$ the transpose must be replaced by the conjugate transpose:

$$
\boldsymbol{v} \in \mathcal{R}(A)^\perp \Leftrightarrow \langle A\boldsymbol{u}, \boldsymbol{v} \rangle = \boldsymbol{v}^{\mathsf H}A\boldsymbol{u} = (A^{\mathsf H}\boldsymbol{v})^{\mathsf H}\boldsymbol{u} = 0, \ \forall \boldsymbol{u} \Leftrightarrow A^{\mathsf H}\boldsymbol{v} = \boldsymbol{0},
$$

so $\mathcal{R}(A)^\perp = \mathcal{N}(A^{\mathsf H})$ and $\mathcal{R}(A^{\mathsf H})^\perp = \mathcal{N}(A)$. This explains the phenomenon in Example 10.1.2 of [Chapter 10](/2.1.10): for a complex matrix, $\mathcal{N}(A^{\mathsf T})$ need not be complementary to $\mathcal{R}(A)$.

**Definition 12.5.2 (Orthogonal Projection)** Let $W$ be a subspace of an inner product space $V$ and $v \in V$. If $v_p \in W$ and $v - v_p \in W^\perp$, then $v_p$ is called the **orthogonal projection** of $v$ onto $W$.

**Theorem 12.5.1** Let $V$ be an inner product space, $W$ a finite-dimensional subspace, and $e_1, \dots, e_k$ an orthonormal basis of $W$.

1. Every $v \in V$ has a unique orthogonal projection onto $W$, namely $v_p = \langle v, e_1 \rangle e_1 + \cdots + \langle v, e_k \rangle e_k$;
2. (best approximation) $\|v - w\| \ge \|v - v_p\|$ for all $w \in W$, with equality only for $w = v_p$;
3. $W \cap W^\perp = \{0\}$ and $V = W \oplus W^\perp$; if $V$ is finite-dimensional, then $(W^\perp)^\perp = W$.

**Proof** 1: $\langle v - v_p, e_i \rangle = \langle v, e_i \rangle - \langle v, e_i \rangle = 0$, so $v - v_p \in W^\perp$. Uniqueness: the difference of two projections lies in both $W$ and $W^\perp$, hence is orthogonal to itself and therefore zero. 2: $v - w = (v - v_p) + (v_p - w)$ with the two terms in $W^\perp$ and $W$ respectively, so by the Pythagorean theorem $\|v - w\|^2 = \|v - v_p\|^2 + \|v_p - w\|^2$. 3: If $w \in W \cap W^\perp$, then $\langle w, w \rangle = 0$; by 1, $v = v_p + (v - v_p) \in W + W^\perp$. In finite dimensions $\dim W^\perp = \dim V - \dim W$, hence $\dim(W^\perp)^\perp = \dim W$; since clearly $W \subseteq (W^\perp)^\perp$, the two are equal (left as an exercise). $\square$

The method of **least squares** is a special case of orthogonal projection: $\min_x\|\boldsymbol{b} - A\boldsymbol{x}\|$ is attained when $A\boldsymbol{x}$ is the projection of $\boldsymbol{b}$ onto $\mathcal{R}(A)$, and the condition $\boldsymbol{b} - A\boldsymbol{x} \in \mathcal{R}(A)^\perp = \mathcal{N}(A^{\mathsf H})$ is the complex form of the **normal equations** $A^{\mathsf H}A\boldsymbol{x} = A^{\mathsf H}\boldsymbol{b}$. If an orthonormal basis of $\mathcal{R}(A)$ is available (for example the columns of $Q$ in $A = QR$), the projection requires only inner products, $\boldsymbol{b}_p = QQ^{\mathsf H}\boldsymbol{b}$, and no system needs to be solved.

## 12.6. The Riesz Representation Theorem and Adjoint Operators

[Chapter 8](/2.1.8) showed that every **linear functional** on $\mathbb{R}^n$ can be written as the inner product with a fixed vector. This holds in every finite-dimensional inner product space.

**Theorem 12.6.1 (Riesz Representation Theorem)** Let $V$ be a finite-dimensional inner product space ($\mathbb{F} = \mathbb{R}$ or $\mathbb{C}$) and $f\colon V \to \mathbb{F}$ a linear functional. Then there is a unique $u \in V$ such that $f(v) = \langle v, u \rangle$ for all $v \in V$. If $e_1, \dots, e_n$ is an orthonormal basis, then $u = \overline{f(e_1)}e_1 + \cdots + \overline{f(e_n)}e_n$.

**Proof** For $v = \sum_i\langle v, e_i \rangle e_i$ we have $f(v) = \sum_i\langle v, e_i \rangle f(e_i) = \left\langle v, \sum_i\overline{f(e_i)}e_i \right\rangle$ (the inner product is conjugate linear in the second argument). Uniqueness: if $\langle v, u_1 - u_2 \rangle = 0$ for all $v$, take $v = u_1 - u_2$. $\square$

Writing $u$ as $\sum f(e_i)e_i$ is correct only in the real case; in the complex case the coefficients must be conjugated. For the same reason, the map $u \mapsto \langle \cdot, u \rangle$ from $V$ to the **dual space** $V^*$ is a bijection that is a linear isomorphism in the real case but conjugate linear in the complex case ($cu \mapsto \bar c\langle \cdot, u \rangle$).

**Example 12.6.1** In the space $\mathcal{P}_2(\mathbb{R})$ of Example 12.4.2, find $u(x)$ such that $\langle p, u \rangle = \int_{-1}^1 p(t)\cos(\pi t)\,\mathrm{d}t$ for all $p \in \mathcal{P}_2(\mathbb{R})$. The right-hand side is a linear functional $f$. Using the orthonormal basis $q_1, q_2, q_3$ of Example 12.4.2: $f(q_1) = \frac{1}{\sqrt2}\int_{-1}^1\cos\pi t\,\mathrm{d}t = 0$, $f(q_2) = 0$ (an odd function), and since $\int_{-1}^1 t^2\cos\pi t\,\mathrm{d}t = -\frac{4}{\pi^2}$, $f(q_3) = -\sqrt{\frac{45}{8}}\cdot\frac{4}{\pi^2}$. Therefore

$$
u(x) = f(q_3)q_3 = -\frac{45}{2\pi^2}\left(x^2 - \frac13\right).
$$

Geometrically, $u$ is the orthogonal projection of $\cos\pi x$ (in the larger space of continuous functions) onto $\mathcal{P}_2(\mathbb{R})$, that is, the best quadratic least squares approximation of $\cos\pi x$ on $[-1, 1]$: for $p \in \mathcal{P}_2$, $\langle p, \cos\pi x \rangle = \langle p, u \rangle$.

**Definition 12.6.1 (Adjoint Operator)** Let $V$ be an inner product space and $T\colon V \to V$ a linear transformation. If a linear transformation $T^*\colon V \to V$ satisfies $\langle T\alpha, \beta \rangle = \langle \alpha, T^*\beta \rangle$ for all $\alpha, \beta \in V$, then $T^*$ is called the **adjoint operator** of $T$ (also called the adjoint transformation).

The adjoint operator has nothing to do with the **adjugate matrix** ($\operatorname{adj}A$) of the chapter on determinants; its relation to the **dual map** $T^{\mathsf t}\colon V^* \to V^*$ of Chapter 8 is explained in [Chapter 13](/2.1.13).

**Theorem 12.6.2** Let $V$ be a finite-dimensional inner product space and $T\colon V \to V$ a linear transformation. Then $T^*$ exists and is unique. If $T$ has matrix $A$ with respect to an orthonormal basis $e_1, \dots, e_n$, then $T^*$ has matrix $A^{\mathsf H}$ with respect to the same basis ($A^{\mathsf T}$ in the real case).

**Proof** Fix $\beta$. The map $\alpha \mapsto \langle T\alpha, \beta \rangle$ is a linear functional, so by the Riesz representation theorem there is a unique vector, denoted $T^*\beta$, with $\langle T\alpha, \beta \rangle = \langle \alpha, T^*\beta \rangle$. Uniqueness implies that $T^*$ is linear. Matrix: the $i$-th coordinate of $T^*e_j$ is $\langle T^*e_j, e_i \rangle = \overline{\langle e_i, T^*e_j \rangle} = \overline{\langle Te_i, e_j \rangle} = \bar a_{ji}$. $\square$

Only with respect to an orthonormal basis is the matrix of the adjoint equal to $A^{\mathsf H}$. With respect to a general basis with metric matrix $G$, the identity $\langle T\alpha, \beta \rangle = \boldsymbol{x}^{\mathsf T}A^{\mathsf T}G\bar{\boldsymbol{y}}$ shows that the matrix of $T^*$ is $\bar G^{-1}A^{\mathsf H}\bar G$.

**Example 12.6.2** Give $\mathbb{C}^3$ the standard inner product and let $T(x_1, x_2, x_3)^{\mathsf T} = (x_1 - \mathrm{i}x_2, x_2 + \mathrm{i}x_3, x_3 + \mathrm{i}x_1)^{\mathsf T}$, with matrix $A = \begin{bmatrix} 1 & -\mathrm{i} & 0 \\ 0 & 1 & \mathrm{i} \\ \mathrm{i} & 0 & 1 \end{bmatrix}$. Then $T^*\boldsymbol{y} = A^{\mathsf H}\boldsymbol{y} = (y_1 - \mathrm{i}y_3, \mathrm{i}y_1 + y_2, -\mathrm{i}y_2 + y_3)^{\mathsf T}$.

**Property 12.6.1** Let $V$ be a finite-dimensional inner product space, $T, T_1, T_2$ linear transformations of $V$ and $c \in \mathbb{F}$.

1. $(T^*)^* = T$, $(T_1 + T_2)^* = T_1^* + T_2^*$, $(cT)^* = \bar cT^*$, $(T_1T_2)^* = T_2^*T_1^*$;
2. if $T$ is invertible, then $T^*$ is invertible and $(T^*)^{-1} = (T^{-1})^*$;
3. if $W$ is a $T$-**invariant subspace**, then $W^\perp$ is a $T^*$-invariant subspace;
4. if $\lambda$ is an eigenvalue of $T$, then $\bar\lambda$ is an eigenvalue of $T^*$.

**Proof** The first identity of 1: $\langle T^*\alpha, \beta \rangle = \overline{\langle \beta, T^*\alpha \rangle} = \overline{\langle T\beta, \alpha \rangle} = \langle \alpha, T\beta \rangle$. The rest follows directly from the definition. 3: Let $u \in W^\perp$. For every $w \in W$, $\langle w, T^*u \rangle = \langle Tw, u \rangle = 0$ because $Tw \in W$. 4: $\det(\bar\lambda I - A^{\mathsf H}) = \overline{\det(\lambda I - A)} = 0$. $\square$

**Example 12.6.3** Let $V = W \oplus W^\perp$ and let $P$ be the orthogonal projection onto $W$. Take an orthonormal basis $e_1, \dots, e_k$ of $W$ and extend it to an orthonormal basis of $V$; the matrix of $P$ is then $\operatorname{diag}(I_k, O)$, which equals its conjugate transpose, so $P^* = P$.

## 12.7. Isometries

**Definition 12.7.1 (Isometry)** Let $V$ be an inner product space. A linear transformation $T\colon V \to V$ with $\langle T\alpha, T\beta \rangle = \langle \alpha, \beta \rangle$ for all $\alpha, \beta$ is called an **isometry**. An isometry of a Euclidean space is called an **orthogonal transformation**, and an isometry of a unitary space is called a **unitary transformation**.

Isometries preserve lengths, angles and orthogonality. The linearity requirement can in fact be dropped: if a map $T$ preserves inner products, expanding $\|T(\alpha + \beta) - T\alpha - T\beta\|^2$ in terms of inner products of images and then replacing them by inner products of the original vectors gives $\|(\alpha + \beta) - \alpha - \beta\|^2 = 0$; scalar multiplication is handled in the same way.

**Example 12.7.1**

1. The rotation $\boldsymbol{x} \mapsto \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}\boldsymbol{x}$ of $\mathbb{R}^2$: $\langle A\boldsymbol{x}, A\boldsymbol{y} \rangle = \boldsymbol{x}^{\mathsf T}A^{\mathsf T}A\boldsymbol{y} = \boldsymbol{x}^{\mathsf T}\boldsymbol{y}$.
2. $\boldsymbol{\alpha} \mapsto U\boldsymbol{\alpha}$ on $\mathbb{C}^n$, where $U$ is a unitary matrix (Property 12.3.2).
3. $\mathbb{C}^{n\times n}$ with the Frobenius inner product, a fixed unitary matrix $U$, and $T(A) = UA$: $\langle UA, UB \rangle = \operatorname{tr}(UAB^{\mathsf H}U^{\mathsf H}) = \operatorname{tr}(AB^{\mathsf H}U^{\mathsf H}U) = \langle A, B \rangle$.

**Theorem 12.7.1** An isometry of a finite-dimensional inner product space is a linear isomorphism.

**Proof** If $T\alpha = 0$, then $\langle \alpha, \alpha \rangle = \langle T\alpha, T\alpha \rangle = 0$, so $\alpha = 0$ and $\mathcal{N}(T) = \{0\}$; by the **rank–nullity theorem**, $T$ is also surjective. $\square$

**Lemma 12.7.1** Let $\alpha_1, \dots, \alpha_n$ be an orthonormal basis of an $n$-dimensional inner product space $V$ and $(\beta_1, \dots, \beta_n) = (\alpha_1, \dots, \alpha_n)P$. Then $\beta_1, \dots, \beta_n$ is an orthonormal basis $\Leftrightarrow$ the **change-of-basis matrix** $P$ is unitary (orthogonal in the real case).

**Proof** $\beta_j = \sum_k p_{kj}\alpha_k$, so by part 3 of Property 12.3.1, $\langle \beta_i, \beta_j \rangle = \sum_k p_{ki}\bar p_{kj}$, the standard inner product in $\mathbb{C}^n$ of the $i$-th and $j$-th columns of $P$. Hence $\langle \beta_i, \beta_j \rangle = \delta_{ij}$ $\Leftrightarrow$ the columns of $P$ form an orthonormal basis $\Leftrightarrow$ $P$ is unitary. $\square$

For example, in $\mathbb{C}^n$, if $A = (\boldsymbol{\alpha}_1, \dots, \boldsymbol{\alpha}_n)$ and $B = (\boldsymbol{\beta}_1, \dots, \boldsymbol{\beta}_n)$ are both unitary, then the change-of-basis matrix $P = A^{-1}B = A^{\mathsf H}B$ from $\{\boldsymbol{\alpha}_i\}$ to $\{\boldsymbol{\beta}_i\}$ is unitary.

**Theorem 12.7.2** Let $V$ be a finite-dimensional inner product space and $T\colon V \to V$ a linear transformation. The following are equivalent:

1. $T$ is an isometry;
2. $TT^* = T^*T = \mathrm{id}_V$, that is, $T^* = T^{-1}$;
3. $T$ preserves lengths: $\|T\alpha\| = \|\alpha\|$ for all $\alpha$;
4. $T$ maps some (and hence every) orthonormal basis to an orthonormal basis;
5. the matrix of $T$ with respect to some orthonormal basis is unitary (orthogonal in the real case).

**Proof** 1 $\Leftrightarrow$ 2: $\langle T\alpha, T\beta \rangle = \langle \alpha, T^*T\beta \rangle$, which equals $\langle \alpha, \beta \rangle$ for all $\alpha$ if and only if $T^*T\beta = \beta$; in finite dimensions $T^*T = \mathrm{id}$ implies $TT^* = \mathrm{id}$. 1 $\Rightarrow$ 3 is clear. 3 $\Rightarrow$ 1 uses the polarization identities, which express the inner product in terms of lengths:

$$
\langle \alpha, \beta \rangle = \frac14\left(\|\alpha + \beta\|^2 - \|\alpha - \beta\|^2\right) \ (\text{real}), \qquad \langle \alpha, \beta \rangle = \frac14\sum_{k=0}^3 \mathrm{i}^k\|\alpha + \mathrm{i}^k\beta\|^2 \ (\text{complex}).
$$

1 $\Rightarrow$ 4: $\langle Te_i, Te_j \rangle = \langle e_i, e_j \rangle = \delta_{ij}$. 4 $\Rightarrow$ 1: let $Te_1, \dots, Te_n$ be orthonormal, $\alpha = \sum x_ie_i$ and $\beta = \sum y_ie_i$. The coordinates of $T\alpha, T\beta$ with respect to the basis $Te_i$ are again $\boldsymbol{x}, \boldsymbol{y}$, so by part 3 of Property 12.3.1, $\langle T\alpha, T\beta \rangle = \boldsymbol{x}^{\mathsf T}\bar{\boldsymbol{y}} = \langle \alpha, \beta \rangle$. 4 $\Leftrightarrow$ 5: $(Te_1, \dots, Te_n) = (e_1, \dots, e_n)A$; apply Lemma 12.7.1. $\square$

**Example 12.7.2** Let $V$ be an $n$-dimensional Euclidean space, $u \in V$ with $\|u\| = 1$, and $T\alpha = \alpha - 2\langle \alpha, u \rangle u$. Direct verification gives

$$
\langle T\alpha, T\beta \rangle = \langle \alpha, \beta \rangle - 2\langle \alpha, u \rangle\langle u, \beta \rangle - 2\langle \beta, u \rangle\langle \alpha, u \rangle + 4\langle \alpha, u \rangle\langle \beta, u \rangle = \langle \alpha, \beta \rangle.
$$

Alternatively, use Theorem 12.7.2: extend $u$ to an orthonormal basis $e_1 = u, e_2, \dots, e_n$; then $Te_1 = -e_1$ and $Te_j = e_j$ ($j \ge 2$), and the matrix $\operatorname{diag}(-1, 1, \dots, 1)$ is orthogonal. $T$ is the reflection in the hyperplane $u^\perp$; in $\mathbb{R}^n$ it is the Householder reflection $I - 2\boldsymbol{u}\boldsymbol{u}^{\mathsf T}$.

Let $T$ be an orthogonal transformation of a Euclidean space; its matrix $A$ with respect to an orthonormal basis is orthogonal, so $\det A = \pm 1$. If $\det A = 1$, $T$ is called a proper orthogonal transformation (a rotation), and if $\det A = -1$, an improper one. For example, on $\mathbb{R}^2$, $\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$ is proper and $\begin{bmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{bmatrix}$ (the reflection in the line through the origin at angle $\theta/2$) is improper. The orthogonal transformations form a group, and the proper ones form a subgroup; these are the groups $O(n)$ and $\operatorname{SO}(n)$ of [1.3.5](/1.3.5). [Chapter 13](/2.1.13) revisits these groups from the point of view of bilinear forms.

## 12.8. Orthogonal and Unitary Similarity

How are the matrices of a linear transformation $T$ with respect to different orthonormal bases related? Let $v_1, \dots, v_n$ and $w_1, \dots, w_n$ be two orthonormal bases, $(w_1, \dots, w_n) = (v_1, \dots, v_n)P$, and let $A$ and $B$ be the matrices of $T$ with respect to the two bases. By Lemma 12.7.1, $P$ is unitary, so

$$
B = P^{-1}AP = P^{\mathsf H}AP.
$$

**Definition 12.8.1** Let $A, B \in \mathbb{C}^{n\times n}$. If there is a unitary matrix $P$ with $P^{\mathsf H}AP = B$, then $A$ and $B$ are called **unitarily similar**. **Orthogonal similarity** of real square matrices ($P$ orthogonal, $P^{\mathsf T}AP = B$) is its real version ([Chapter 7](/2.1.7)).

**Theorem 12.8.1** The matrices of a linear transformation of a finite-dimensional inner product space with respect to different orthonormal bases are orthogonally similar (Euclidean space) or unitarily similar (unitary space). Conversely, every matrix unitarily similar to $A$ is the matrix of $T$ with respect to some orthonormal basis.

The central question of the chapter now takes a matrix form: when does $\{P^{\mathsf H}AP \mid P \text{ unitary}\}$ contain a diagonal matrix? Unitary similarity is more restrictive than ordinary **matrix similarity**, but it has two advantages: $P^{-1} = P^{\mathsf H}$ needs no inversion, and unitary matrices preserve lengths, so errors are not amplified in numerical computation.

## 12.9. Normal Operators

If the matrix of $T$ with respect to an orthonormal basis is a diagonal matrix $\Lambda$, then the matrix of $T^*$ is $\bar\Lambda$; two diagonal matrices commute, so $TT^* = T^*T$. This necessary condition turns out to be sufficient as well.

**Definition 12.9.1** Let $V$ be a unitary space. A linear transformation $T$ with $TT^* = T^*T$ is called a **normal operator**; a complex square matrix $A$ with $AA^{\mathsf H} = A^{\mathsf H}A$ is called a **normal matrix**.

$T$ is a normal operator if and only if its matrix with respect to an orthonormal basis is a normal matrix. Unitary matrices ($A^{\mathsf H}A = I = AA^{\mathsf H}$), Hermitian matrices ($A^{\mathsf H} = A$), skew-Hermitian matrices ($A^{\mathsf H} = -A$) and diagonal matrices are all normal; thus unitary transformations are special normal operators, and they form a proper subclass. The matrix $\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ is not normal.

**Property 12.9.1** Let $T$ be a normal operator.

1. If $T\alpha = \lambda\alpha$, then $T^*\alpha = \bar\lambda\alpha$: $T$ and $T^*$ have the same eigenvectors, with complex conjugate eigenvalues;
2. eigenvectors belonging to distinct eigenvalues are orthogonal.

**Proof** 1: $S = T - \lambda\,\mathrm{id}$ is also normal ($S^* = T^* - \bar\lambda\,\mathrm{id}$), and for a normal operator $\|S\alpha\|^2 = \langle \alpha, S^*S\alpha \rangle = \langle \alpha, SS^*\alpha \rangle = \|S^*\alpha\|^2$. Hence $S\alpha = 0 \Leftrightarrow S^*\alpha = 0$. 2: Let $T\alpha = \lambda\alpha$ and $T\beta = \mu\beta$ with $\lambda \ne \mu$. By 1, $\lambda\langle \alpha, \beta \rangle = \langle T\alpha, \beta \rangle = \langle \alpha, T^*\beta \rangle = \langle \alpha, \bar\mu\beta \rangle = \mu\langle \alpha, \beta \rangle$, so $\langle \alpha, \beta \rangle = 0$. $\square$

To prove that normal operators can be unitarily diagonalized, we first strengthen Schur's theorem to unitary triangularization.

**Theorem 12.9.1 (Unitary Schur Triangularization)** Let $T$ be a linear transformation of an $n$-dimensional unitary space. Then there is an orthonormal basis with respect to which the matrix of $T$ is upper triangular. In matrix form: every $A \in \mathbb{C}^{n\times n}$ is unitarily similar to an upper triangular matrix, $U^{\mathsf H}AU = R'$, whose diagonal entries are the eigenvalues of $A$.

**Proof** By Schur's theorem (Theorem 10.3.1) there is an invertible $M$ such that $N = M^{-1}AM$ is upper triangular. Take the QR decomposition of $M$ (Theorem 12.4.1): $M = UR$ with $U$ unitary and $R$ an invertible upper triangular matrix. Then

$$
U^{\mathsf H}AU = U^{-1}AU = R\left(M^{-1}AM\right)R^{-1} = RNR^{-1},
$$

and products and inverses of upper triangular matrices are upper triangular. $\square$

The proof combines "Schur's theorem + QR decomposition": Schur's theorem provides a basis $\boldsymbol{m}_1, \dots, \boldsymbol{m}_n$ in which $A$ is upper triangular, which is equivalent to all the subspaces $\operatorname{span}\{\boldsymbol{m}_1\} \subseteq \operatorname{span}\{\boldsymbol{m}_1, \boldsymbol{m}_2\} \subseteq \cdots \subseteq \mathbb{C}^n$ being $A$-invariant; Gram–Schmidt orthogonalization does not change this chain of subspaces, so the orthogonalized basis still makes the matrix upper triangular. The QR algorithm for computing eigenvalues in numerical linear algebra aims precisely at this unitary triangularization.

## 12.10. The Spectral Theorem

**Theorem 12.10.1 (Spectral Theorem)** Let $T$ be a linear transformation of a unitary space $V$. The following are equivalent:

1. $T$ is a normal operator;
2. there is an orthonormal basis of $V$ with respect to which the matrix of $T$ is diagonal;
3. (matrix form) the matrix $A$ of $T$ with respect to an orthonormal basis is unitarily similar to a diagonal matrix: there is a unitary $U$ with $U^{\mathsf H}AU = \Lambda = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$.

**Proof** 2 $\Leftrightarrow$ 3 is Theorem 12.8.1. 3 $\Rightarrow$ 1: $A = U\Lambda U^{\mathsf H}$, so $AA^{\mathsf H} = U\Lambda\bar\Lambda U^{\mathsf H} = U\bar\Lambda\Lambda U^{\mathsf H} = A^{\mathsf H}A$.

1 $\Rightarrow$ 3: By Theorem 12.9.1, $U^{\mathsf H}AU = B$ is upper triangular, and $BB^{\mathsf H} = U^{\mathsf H}AA^{\mathsf H}U = U^{\mathsf H}A^{\mathsf H}AU = B^{\mathsf H}B$, so $B$ is also normal. Comparing the $(1, 1)$ entries of $BB^{\mathsf H}$ and $B^{\mathsf H}B$:

$$
|b_{11}|^2 + |b_{12}|^2 + \cdots + |b_{1n}|^2 = |b_{11}|^2,
$$

so $b_{12} = \cdots = b_{1n} = 0$. Comparing the $(2, 2)$ entries next: $|b_{22}|^2 + \cdots + |b_{2n}|^2 = |b_{12}|^2 + |b_{22}|^2 = |b_{22}|^2$, which gives $b_{23} = \cdots = b_{2n} = 0$. Continuing in this way, $B$ is diagonal. $\square$

In outer product form, $A = \sum_i\lambda_i\boldsymbol{u}_i\boldsymbol{u}_i^{\mathsf H}$, where the $\boldsymbol{u}_i$ are the columns of $U$; grouping the terms with the same eigenvalue gives $A = \sum_j\mu_jP_j$, where $P_j$ is the orthogonal projection onto the eigenspace $V_{\mu_j}$ (Example 12.6.3), $\sum_j P_j = I$ and $P_jP_k = O$ ($j \ne k$). This is the spectral decomposition of a normal matrix.

**Corollary 12.10.1** Unitary matrices can be unitarily diagonalized with diagonal entries of modulus $1$; Hermitian matrices can be unitarily diagonalized with real diagonal entries; skew-Hermitian matrices can be unitarily diagonalized with purely imaginary diagonal entries.

**Proof** All of them are normal. By part 1 of Property 12.9.1, the eigenvalues satisfy $\bar\lambda = \lambda^{-1}$ for unitary matrices, $\bar\lambda = \lambda$ for Hermitian matrices, and $\bar\lambda = -\lambda$ for skew-Hermitian matrices. $\square$

**Corollary 12.10.2** A real symmetric matrix $A$ is orthogonally similar to a real diagonal matrix: there is a real orthogonal matrix $Q$ such that $Q^{\mathsf T}AQ$ is real diagonal.

**Proof** $A$ is Hermitian, so by Corollary 12.10.1 its eigenvalues are real. For each real eigenvalue $\mu$, $A - \mu I$ is a real matrix, so $\mathcal{N}(A - \mu I)$ has a real basis, and Gram–Schmidt orthogonalization in $\mathbb{R}^n$ yields a real orthonormal basis of it. Different eigenspaces are mutually orthogonal (part 2 of Property 12.9.1), and their dimensions add up to $n$ ($A$ is unitarily diagonalizable, so geometric multiplicities equal algebraic multiplicities). Together these vectors form an orthonormal basis of $\mathbb{R}^n$, and taking them as columns gives $Q$. $\square$

This is the spectral decomposition of real symmetric matrices in Theorem 7.1.1 of [Chapter 7](/2.1.7), derived here from the complex spectral theorem; the step "the eigenvalues are real" in the proof is exactly where the complex field helps.

**Corollary 12.10.3** A matrix that is both normal and nilpotent is the zero matrix: it is unitarily similar to a diagonal matrix whose diagonal entries (the eigenvalues) are all zero.

**Example 12.10.1** Real normal matrices of order 2. Let $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \in \mathbb{R}^{2\times 2}$. Comparing $AA^{\mathsf T}$ and $A^{\mathsf T}A$ gives $b^2 = c^2$ and $(c - b)(a - d) = 0$, so $A$ is normal if and only if $A$ is symmetric ($b = c$) or $A = \begin{bmatrix} a & b \\ -b & a \end{bmatrix}$ ($b \ne 0$). The latter is the matrix representation of the complex number $a - b\mathrm{i}$ ([Chapter 9](/2.1.9)); its eigenvalues are $a \pm b\mathrm{i}$, the corresponding eigenvectors $\frac{1}{\sqrt2}(1, \pm \mathrm{i})^{\mathsf T}$ are orthogonal, $U = \frac{1}{\sqrt2}\begin{bmatrix} 1 & 1 \\ \mathrm{i} & -\mathrm{i} \end{bmatrix}$ is unitary, and $U^{\mathsf H}AU = \operatorname{diag}(a + b\mathrm{i}, a - b\mathrm{i})$. It has no real eigenvectors in $\mathbb{R}^2$ and cannot be orthogonally diagonalized, but it can be unitarily diagonalized.

The difference between normal and non-normal matrices can also be seen in the *numerical range* $W(A) = \{\boldsymbol{x}^{\mathsf H}A\boldsymbol{x} \mid \|\boldsymbol{x}\| = 1\}$. It always contains all the eigenvalues (take $\boldsymbol{x}$ to be a unit eigenvector), and it is convex (the Toeplitz–Hausdorff theorem). If $A = U\Lambda U^{\mathsf H}$ is normal, put $\boldsymbol{y} = U^{\mathsf H}\boldsymbol{x}$; then $\boldsymbol{x}^{\mathsf H}A\boldsymbol{x} = \sum_i \lambda_i|y_i|^2$ with $\sum_i |y_i|^2 = 1$, so $W(A)$ is exactly the convex hull of the eigenvalues. The numerical range of a non-normal matrix can be much larger. The powers of the non-normal matrix in [Chapter 11](/2.1.11), which first grow and then decay, are a manifestation of the same phenomenon.

![Numerical ranges of two 3 x 3 matrices with the same eigenvalues (1, -0.5+i, -0.8-0.6i). Left: a normal matrix, whose numerical range is the triangle spanned by the eigenvalues. Right: a non-normal upper triangular matrix, whose numerical range is much larger than the triangle. The scattered points are values x^H A x for random unit vectors x](./plots/numerical-range.py)

Unitary diagonalization of a normal matrix combines two standard problems:

**Algorithm 12.10.1 (Unitary Diagonalization of a Normal Matrix)** Input: a normal matrix $A \in \mathbb{C}^{n\times n}$.

1. Find the eigenvalues $\mu_1, \dots, \mu_s$ and their algebraic multiplicities.
2. For each $\mu_j$, solve $(A - \mu_jI)\boldsymbol{x} = \boldsymbol{0}$ to obtain a basis of the eigenspace, and apply Gram–Schmidt orthogonalization to it to obtain an orthonormal basis.
3. Arrange all these vectors into $U$. Different eigenspaces are automatically orthogonal (Property 12.9.1), so $U$ is unitary and $U^{\mathsf H}AU = \Lambda$.

**Example 12.10.2** Let $A = \begin{bmatrix} 0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & \mathrm{i} \end{bmatrix}$. Then $A^{\mathsf H} = \begin{bmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & -\mathrm{i} \end{bmatrix}$ and $A^{\mathsf H}A = I = AA^{\mathsf H}$, so $A$ is unitary and hence normal. $\det(\lambda I - A) = (\lambda^2 + 1)(\lambda - \mathrm{i})$, with eigenvalues $\mathrm{i}$ (double) and $-\mathrm{i}$.

1. $\lambda = \mathrm{i}$: a basis of the solutions of $(A - \mathrm{i}I)\boldsymbol{x} = \boldsymbol{0}$ is $(-\mathrm{i}, 1, 0)^{\mathsf T}$, $(0, 0, 1)^{\mathsf T}$; these are already orthogonal, and normalizing gives $\boldsymbol{u}_1 = \frac{1}{\sqrt2}(-\mathrm{i}, 1, 0)^{\mathsf T}$ and $\boldsymbol{u}_2 = (0, 0, 1)^{\mathsf T}$. Had we chosen a non-orthogonal basis (for example $(-\mathrm{i}, 1, 1)^{\mathsf T}$ and $(0, 0, 1)^{\mathsf T}$), Gram–Schmidt would be needed first.
2. $\lambda = -\mathrm{i}$: a basis is $(\mathrm{i}, 1, 0)^{\mathsf T}$, giving $\boldsymbol{u}_3 = \frac{1}{\sqrt2}(\mathrm{i}, 1, 0)^{\mathsf T}$, which is automatically orthogonal to $\boldsymbol{u}_1, \boldsymbol{u}_2$.
3. $U = (\boldsymbol{u}_1, \boldsymbol{u}_2, \boldsymbol{u}_3)$ and $U^{\mathsf H}AU = \operatorname{diag}(\mathrm{i}, \mathrm{i}, -\mathrm{i})$.

Numerical software does not follow Algorithm 12.10.1 (the eigenspace of a multiple eigenvalue is hard to compute accurately in floating-point arithmetic); instead it computes the unitary triangularization of Theorem 12.9.1 directly, and for a normal matrix the resulting triangular matrix is diagonal.

```python
import numpy as np
from scipy.linalg import schur

A = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1j]])
print(np.allclose(A @ A.conj().T, A.conj().T @ A))   # True: A is normal
T, U = schur(A, output='complex')                    # A = U T U^H, U unitary
print(np.round(T, 12))                               # T is diagonal
print(np.allclose(U @ T @ U.conj().T, A))            # True
```

## Summary

| | $\mathbb{R}^n$ (Chapters 4, 7) | Euclidean space | Unitary space |
|---|---|---|---|
| Inner product | $\boldsymbol{\alpha}^{\mathsf T}\boldsymbol{\beta}$ | Symmetric, bilinear, positive definite | Conjugate symmetric, linear in the first argument, positive definite |
| Representation in a basis | — | $\boldsymbol{x}^{\mathsf T}G\boldsymbol{y}$, $G$ real symmetric positive definite | $\boldsymbol{x}^{\mathsf T}G\bar{\boldsymbol{y}}$, $G$ positive definite Hermitian |
| Matrices preserving the inner product | Orthogonal matrices | Orthogonal matrices (in an orthonormal basis) | Unitary matrices $A^{\mathsf H}A = I$ |
| Matrix of the adjoint | $A^{\mathsf T}$ | $A^{\mathsf T}$ | $A^{\mathsf H}$ |
| Orthogonally (unitarily) diagonalizable | Real symmetric matrices | Symmetric transformations | Normal operators |

| Result | Content |
|---|---|
| Cauchy–Schwarz and triangle inequalities | Property 12.2.1, proof by projection |
| Gram–Schmidt | Algorithm 12.4.1; finite-dimensional inner product spaces have orthonormal bases; $A = QR$ (Theorem 12.4.1) |
| Orthogonal complements and projections | $V = W \oplus W^\perp$, $v_p = \sum\langle v, e_i \rangle e_i$, best approximation (Theorem 12.5.1); $\mathcal{R}(A)^\perp = \mathcal{N}(A^{\mathsf H})$ |
| Riesz representation | $f = \langle \cdot, u \rangle$, $u = \sum\overline{f(e_i)}e_i$ (Theorem 12.6.1) |
| Adjoint | Exists and is unique; its matrix in an orthonormal basis is $A^{\mathsf H}$ (Theorem 12.6.2) |
| Isometries | Five equivalent conditions (Theorem 12.7.2); the change-of-basis matrix between orthonormal bases is unitary |
| Unitary Schur triangularization | Every complex square matrix is unitarily similar to an upper triangular matrix = Schur's theorem + QR (Theorem 12.9.1) |
| Spectral theorem | Unitarily diagonalizable $\Leftrightarrow$ normal (Theorem 12.10.1); the spectral decomposition of real symmetric matrices is a corollary |
| Unitary diagonalization | Algorithm 12.10.1: find the eigenvalues, apply Gram–Schmidt in each eigenspace |

With an orthonormal basis, coordinates, projections and adjoints require only inner products or conjugate transposes, never solving systems or inverting matrices; this is why orthogonal (unitary) methods are favored in numerical computation. The [next chapter](/2.1.13) studies the class of normal operators with real eigenvalues (Hermitian operators) and revisits quadratic forms and the singular value decomposition over the complex numbers.
