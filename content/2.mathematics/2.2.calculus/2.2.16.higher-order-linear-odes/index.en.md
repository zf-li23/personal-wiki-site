---
title: Higher-Order Linear Differential Equations and Linear Systems
source_hash: 44d7c6b9eb4d
---

The first-order linear equations of the [previous chapter](/2.2.15) have two features: the solution set has the structure "one particular solution plus the general solution of the homogeneous equation", and the solutions of the homogeneous equation form a one-dimensional vector space. This chapter extends both features to $n$th-order linear equations and to linear systems: the solution set of the homogeneous equation is an $n$-dimensional **vector space**, finding the general solution means finding a **basis** of it, and deciding whether $n$ solutions form a basis requires the Wronskian. The language of linear algebra ([2.1](/2.1)) here is not a metaphor but literal: differentiation is a linear map, a linear differential equation is an equation for a linear map, and the superposition principle, the structure of solutions, bases and dimension are all concrete instances of the results of [2.1.3](/2.1.3) and [2.1.8](/2.1.8).

Equations with variable coefficients generally cannot be solved in closed form; for them this chapter discusses only reduction of order and variation of parameters when some solutions are already known. Equations with constant coefficients, by contrast, can be solved completely: writing differentiation as the operator $\mathrm{D}$, the equation becomes $P(\mathrm{D})y=f$; finding a basis for the homogeneous equation reduces to finding the roots of the polynomial $P$ (the characteristic equation), and particular solutions of the nonhomogeneous equation are found by the method of undetermined coefficients and the operator method. Vibration problems in physics are the most important application of second-order equations with constant coefficients. The last section treats first-order linear systems $\boldsymbol{x}'=A(t)\boldsymbol{x}+\boldsymbol{f}(t)$, which can be converted to and from $n$th-order equations; the solutions of a system with constant coefficients are given by the **eigenvalues** and **eigenvectors** of $A$, and the general case, with $\mathrm{e}^{tA}$ and the Jordan form, is treated in [2.1.11](/2.1.11#sec-11.9). A more systematic theory is given in ordinary differential equations ([2.4](/2.4)), and applications of planar systems in biology appear in [Systems Biology](/7.9) and [Ecology](/7.19).

## 16.1. Structure of Solutions of Linear Differential Equations

### 16.1.1. $n$th-Order Linear Equations

The general form of an $n$th-order linear equation is

$$
y^{(n)}+a_1(x)y^{(n-1)}+\cdots+a_{n-1}(x)y'+a_n(x)y=f(x),\tag{16.1}
$$
and when $f\equiv0$,

$$
y^{(n)}+a_1(x)y^{(n-1)}+\cdots+a_{n-1}(x)y'+a_n(x)y=0\tag{16.2}
$$
is called the homogeneous equation associated with Eq. (16.1). Writing $L(y)=y^{(n)}+a_1y^{(n-1)}+\cdots+a_ny$, Eqs. (16.1) and (16.2) become $L(y)=f$ and $L(y)=0$.

**Theorem 16.1.1** Suppose $a_1(x),\dots,a_n(x),f(x)$ are continuous on an interval $I$. Then for any $x_0\in I$ and any real numbers $\eta_0,\eta_1,\dots,\eta_{n-1}$, the solution of Eq. (16.1) satisfying $y^{(k)}(x_0)=\eta_k$ ($k=0,1,\dots,n-1$) exists and is unique on the whole of $I$.

This strengthens the general existence and uniqueness theorem (the higher-dimensional form of Theorem 15.1.1, [2.4](/2.4)) in the linear case: solutions of a linear equation do not "blow up" inside $I$, so the interval of existence is all of $I$. From now on the coefficients are always assumed continuous on $I$.

**Theorem 16.1.2 (Superposition Principle)** 

1. $L$ is linear: $L(c_1y_1+c_2y_2)=c_1L(y_1)+c_2L(y_2)$. In particular, linear combinations of solutions of the homogeneous equation (16.2) are again solutions;
2. If $L(y_1)=f_1$ and $L(y_2)=f_2$, then $L(y_1+y_2)=f_1+f_2$;
3. The difference of two solutions of the nonhomogeneous equation (16.1) is a solution of the homogeneous equation (16.2). Hence, if $y^*$ is one solution of Eq. (16.1), every solution of Eq. (16.1) can be written as $y=y^*+Y$, where $Y$ is a solution of Eq. (16.2).

**Proof** Differentiation is a linear operation, and so is multiplication by a function $a_k(x)$; hence $L$ is linear. Statements 2 and 3 follow directly from linearity. $\square$

In the language of linear algebra, $L$ is a linear map from $C^n(I)$ to $C(I)$; the solution set of the homogeneous equation is its kernel, and the solution set of the nonhomogeneous equation is a coset $y^*+\ker L$ of the kernel. Statement 2 means that we may split the right-hand side into pieces, find a particular solution for each, and add them.

### 16.1.2. Linear Dependence of Functions and the Wronskian

**Definition 16.1.1** Let the functions $\varphi_1,\dots,\varphi_m$ be defined on an interval $I$. If there are constants $c_1,\dots,c_m$, not all zero, such that $c_1\varphi_1(x)+\cdots+c_m\varphi_m(x)=0$ for all $x\in I$, the functions are said to be **linearly dependent** on $I$; otherwise they are **linearly independent**.

This is the definition of linear dependence from [2.1.3](/2.1.3), with a function space as the vector space. For example, $x^2+1$, $2x^2$, $1$ are linearly dependent ($2(x^2+1)-2x^2-2\cdot1=0$), while $\cos x,\sin x$ are linearly independent on every interval.

**Example 16.1.1** If $\lambda_1,\dots,\lambda_m$ are distinct, then $\mathrm{e}^{\lambda_1x},\dots,\mathrm{e}^{\lambda_mx}$ are linearly independent on every interval. Suppose $\sum c_k\mathrm{e}^{\lambda_kx}=0$. Differentiating $0,1,\dots,m-1$ times and setting $x=x_0$ gives a homogeneous linear system for the numbers $c_k\mathrm{e}^{\lambda_kx_0}$ whose coefficient matrix is the **Vandermonde matrix** $(\lambda_k^{j})$, with determinant $\prod_{j<k}(\lambda_k-\lambda_j)\ne0$; hence $c_k=0$.

The method of this example is general: a linear relation that holds for all $x$ still holds after differentiation, which yields a linear system with numerical coefficients.

**Definition 16.1.2** Suppose $\varphi_1,\dots,\varphi_m$ have derivatives of order $m-1$ on $I$. The determinant

$$
W(x)=W[\varphi_1,\dots,\varphi_m](x)=\begin{vmatrix}\varphi_1(x)&\varphi_2(x)&\cdots&\varphi_m(x)\\ \varphi_1'(x)&\varphi_2'(x)&\cdots&\varphi_m'(x)\\ \vdots&\vdots&&\vdots\\ \varphi_1^{(m-1)}(x)&\varphi_2^{(m-1)}(x)&\cdots&\varphi_m^{(m-1)}(x)\end{vmatrix}
$$
is called the **Wronskian** of the functions $\varphi_1,\dots,\varphi_m$.

It is the determinant of the **Wronskian matrix** of [2.1.11](/2.1.11) (with $n=1$, that is, for scalar functions), except that here the functions are arranged in columns and the derivatives in rows.

**Proposition 16.1.1** If $\varphi_1,\dots,\varphi_m$ are linearly dependent on $I$, then $W(x)\equiv0$. Equivalently, if $W(x_0)\ne0$ for some $x_0\in I$, then they are linearly independent.

**Proof** Suppose $\sum c_k\varphi_k\equiv0$ with $c_k$ not all zero. Differentiating gives $\sum c_k\varphi_k^{(i)}(x)=0$ ($i=0,\dots,m-1$). For each $x$, the homogeneous linear system whose coefficient matrix is the matrix of $W(x)$ has the nonzero solution $(c_1,\dots,c_m)^{\mathsf T}$, so $W(x)=0$. $\square$

The converse is false. Let $\varphi_1(x)=x^3$ for $x\ge0$ and $0$ for $x<0$, and $\varphi_2(x)=0$ for $x\ge0$ and $x^3$ for $x<0$. Both have continuous derivatives and $W(x)=\varphi_1\varphi_2'-\varphi_1'\varphi_2\equiv0$ (at each point at least one of the functions vanishes together with its derivative), but they are linearly independent on $\mathbb{R}$: $c_1\varphi_1+c_2\varphi_2=0$ at $x=1$ and $x=-1$ gives $c_1=0$ and $c_2=0$, respectively. For solutions of a homogeneous linear equation, however, the converse does hold:

**Theorem 16.1.3** Let $y_1,\dots,y_n$ be $n$ solutions of the homogeneous equation (16.2) on $I$. The following conditions are equivalent:

1. $y_1,\dots,y_n$ are linearly dependent on $I$;
2. $W(x)\equiv0$ for $x\in I$;
3. $W(x_0)=0$ for some $x_0\in I$.

Hence the Wronskian of $n$ solutions either vanishes identically or vanishes nowhere.

**Proof** 1 ⇒ 2 is Proposition 16.1.1, and 2 ⇒ 3 is obvious. 3 ⇒ 1: since $W(x_0)=0$, the numerical system $\sum_kc_ky_k^{(i)}(x_0)=0$ ($i=0,\dots,n-1$) has a nonzero solution $(c_1,\dots,c_n)$. Let $y=\sum c_ky_k$. By the superposition principle, $y$ is a solution of Eq. (16.2), and $y(x_0)=y'(x_0)=\cdots=y^{(n-1)}(x_0)=0$. Since $y\equiv0$ satisfies the same initial conditions, the uniqueness in Theorem 16.1.1 gives $\sum c_ky_k\equiv0$. $\square$

For two solutions we can compute more concretely: $W=y_1y_2'-y_1'y_2$ satisfies $W'=y_1y_2''-y_1''y_2=-a_1(x)W$ (substituting $y''=-a_1y'-a_2y$ from the equation), so

$$
W(x)=W(x_0)\,\mathrm{e}^{-\int_{x_0}^xa_1(t)\,\mathrm{d}t}.
$$
This is called *Liouville's formula* (it holds for $n$th-order equations as well), and it shows directly that $W$ is either identically zero or nowhere zero. For the case of systems, see Theorem 16.6.2.

### 16.1.3. The Solution Space and the General Solution

**Theorem 16.1.4** The solutions of the homogeneous equation (16.2) form an $n$-dimensional linear subspace of $C^n(I)$.

**Proof** By the superposition principle, the solution set is a subspace. Fix $x_0\in I$ and let $y_k$ be the solution satisfying the initial conditions $(y_k(x_0),y_k'(x_0),\dots,y_k^{(n-1)}(x_0))=\boldsymbol{e}_k^{\mathsf T}$, where $\boldsymbol{e}_k$ is the standard basis of $\mathbb{R}^n$ (the existence of these solutions is guaranteed by Theorem 16.1.1). Then $W(x_0)=\det I_n=1$, so $y_1,\dots,y_n$ are linearly independent. For any solution $y$, let $\eta_i=y^{(i)}(x_0)$; then $\tilde y=\sum_{k=1}^n\eta_{k-1}y_k$ is a solution satisfying the same initial conditions, so $y=\tilde y$ by uniqueness. Therefore $y_1,\dots,y_n$ form a basis of the solution space. $\square$

From another point of view: the map $y\mapsto(y(x_0),\dots,y^{(n-1)}(x_0))^{\mathsf T}$ is a linear map from the solution space to $\mathbb{R}^n$; existence shows that it is surjective and uniqueness shows that it is injective, so it is an **isomorphism**, and the solution space has **dimension** $n$.

**Definition 16.1.3** A set of $n$ linearly independent solutions of the homogeneous equation (16.2) is called a **fundamental set of solutions** of it.

**Theorem 16.1.5** Let $y_1,\dots,y_n$ be a fundamental set of solutions of Eq. (16.2) and $y^*$ a particular solution of Eq. (16.1). Then the general solution of Eq. (16.1) is

$$
y=y^*+C_1y_1+C_2y_2+\cdots+C_ny_n,
$$
and it includes all solutions of Eq. (16.1).

This differs from the situation for general first-order equations: the general solution of a linear equation consists of all its solutions (compare Example 15.2.1). Solving a linear equation therefore splits into two tasks: finding $n$ linearly independent solutions of the homogeneous equation, and finding one particular solution of the nonhomogeneous equation.

**Example 16.1.2** Solve the following equations. (1) $y''+y=0$ has the solutions $\cos x$ and $\sin x$, with $W=\begin{vmatrix}\cos x&\sin x\\-\sin x&\cos x\end{vmatrix}=1\ne0$, so the general solution is $y=C_1\cos x+C_2\sin x$.

(2) $(x-1)y''-xy'+y=0$: the coefficients sum to zero, so $y=\mathrm{e}^x$ is a solution ($y=y'=y''$); $y=x$ is also a solution ($y''=0$, $-x\cdot1+x=0$). Since $W=\begin{vmatrix}x&\mathrm{e}^x\\1&\mathrm{e}^x\end{vmatrix}=(x-1)\mathrm{e}^x$ does not vanish on $x>1$ or on $x<1$, the general solution is $y=C_1x+C_2\mathrm{e}^x$.

## 16.2. Second-Order Linear Equations with Variable Coefficients

This section considers $y''+a_1(x)y'+a_2(x)y=f(x)$. There is no general method for equations with variable coefficients, but once one solution of the homogeneous equation is known, all solutions can be found; variation of parameters is the key.

### 16.2.1. Reduction of Order When One Solution Is Known

Let $y_1$ be a nonzero solution of the homogeneous equation $y''+a_1y'+a_2y=0$. Put $y_2=C(x)y_1$ and substitute into the homogeneous equation; the terms containing $C$ itself cancel because $y_1$ is a solution, leaving

$$
C''y_1+C'(2y_1'+a_1y_1)=0,
$$
a first-order linear (indeed separable) equation for $C'$: $\dfrac{\mathrm{d}C'}{C'}=-\Big(\dfrac{2y_1'}{y_1}+a_1\Big)\mathrm{d}x$. Taking a nonzero solution,

$$
C'(x)=\frac{1}{y_1^2}\mathrm{e}^{-\int a_1(x)\,\mathrm{d}x},\qquad y_2=y_1\int\frac{1}{y_1^2}\mathrm{e}^{-\int a_1(x)\,\mathrm{d}x}\,\mathrm{d}x.
$$
Since $C'\ne0$, $C$ is not constant, so $y_2$ and $y_1$ are linearly independent (this can also be seen from $W[y_1,y_2]=y_1^2C'=\mathrm{e}^{-\int a_1\mathrm{d}x}\ne0$, in agreement with Liouville's formula).

**Example 16.2.1** Given the solution $y_1=x$ of $(x-1)y''-xy'+y=0$, find another linearly independent solution. Put $y_2=C(x)x$; substitution gives $x(x-1)C''+(2x-2-x^2)C'=0$,

$$
\frac{\mathrm{d}C'}{C'}=\frac{x^2-2x+2}{x(x-1)}\,\mathrm{d}x=\Big(1+\frac{1}{x-1}-\frac2x\Big)\mathrm{d}x,\qquad C'=\frac{x-1}{x^2}\mathrm{e}^x=\Big(\frac1x-\frac1{x^2}\Big)\mathrm{e}^x.
$$
Hence $C=\dfrac{\mathrm{e}^x}{x}$ and $y_2=\mathrm{e}^x$, in agreement with Example 16.1.2 (2).

**Example 16.2.2** Solve $x^2y''-2y=0$. By inspection, $y_1=x^2$ is a solution ($2x^2-2x^2=0$). Put $y_2=C(x)x^2$; substitution gives $x^4C''+4x^3C'=0$, so $C'=\dfrac1{x^4}$ and $C=-\dfrac1{3x^3}$; we take $y_2=\dfrac1x$ (constant factors may be dropped). The general solution is $y=C_1x^2+\dfrac{C_2}x$.

### 16.2.2. Variation of Parameters

Suppose a fundamental set of solutions $y_1,y_2$ of the homogeneous equation is known, and we want a particular solution of the nonhomogeneous equation $y''+a_1y'+a_2y=f$. Following the first-order case, we replace the constants in the general solution $C_1y_1+C_2y_2$ by functions: $Y=C_1(x)y_1+C_2(x)y_2$. Two unknown functions need satisfy only one equation, so we may impose one more condition; we choose

$$
C_1'y_1+C_2'y_2=0,
$$
so that no $C_i'$ appears in $Y'=C_1y_1'+C_2y_2'$. Differentiating once more, substituting into the equation and using the fact that $y_1,y_2$ are homogeneous solutions, we obtain $C_1'y_1'+C_2'y_2'=f$.

**Algorithm 16.2.1 (Variation of Parameters for Second-Order Equations)** Let $y_1,y_2$ be a fundamental set of solutions of $y''+a_1y'+a_2y=0$.

1. Solve the linear system
   $$
   \begin{cases}C_1'y_1+C_2'y_2=0,\\ C_1'y_1'+C_2'y_2'=f(x),\end{cases}
   $$
   whose coefficient determinant is $W=W[y_1,y_2]\ne0$; by Cramer's rule, $C_1'=-\dfrac{y_2f}{W}$ and $C_2'=\dfrac{y_1f}{W}$;
2. Integrate to obtain $C_1,C_2$ (one antiderivative each); a particular solution is $Y=C_1y_1+C_2y_2$. If the constants of integration are kept, the result is the general solution.

Note that the equation must first be put in standard form, with coefficient 1 for $y''$, and $f$ denotes the right-hand side of the standard form. This is the same method as **variation of parameters** for systems in [2.1.11](/2.1.11#sec-11.9) (see 16.6.3).

**Example 16.2.3** Solve $y''+y=\sec x$ ($\lvert x\rvert<\frac\pi2$). Here $y_1=\cos x$, $y_2=\sin x$ and $W=1$.

$$
\begin{cases}C_1'\cos x+C_2'\sin x=0,\\ -C_1'\sin x+C_2'\cos x=\sec x,\end{cases}\qquad C_1'=-\tan x,\quad C_2'=1.
$$
Hence $C_1=\ln\cos x$ and $C_2=x$, and the general solution is

$$
y=C_1\cos x+C_2\sin x+\cos x\ln\cos x+x\sin x.
$$
Similarly, a particular solution of $y''+y=\tan x$ is $-\cos x\ln(\sec x+\tan x)$.

We could also use just one homogeneous solution $y_1=\cos x$: substituting $y=C(x)\cos x$ gives $C''\cos x-2C'\sin x=\sec x$, that is, the first-order linear equation $(C')'-2\tan x\,C'=\sec^2x$ for $C'$, whose solution is $C'=\dfrac{x+C_1}{\cos^2x}$; one more integration gives the same general solution. This shows that when only one homogeneous solution is known, applying the method of 16.2.1 directly to the nonhomogeneous equation also yields the general solution.

**Example 16.2.4** Given that the general solution of $(x-1)y''-xy'+y=0$ is $C_1x+C_2\mathrm{e}^x$, find the general solution of $(x-1)y''-xy'+y=(x-1)^2$. The right-hand side of the standard form is $f=x-1$, and $W=(x-1)\mathrm{e}^x$.

$$
\begin{cases}C_1'x+C_2'\mathrm{e}^x=0,\\ C_1'+C_2'\mathrm{e}^x=x-1,\end{cases}\qquad C_1'=-1,\quad C_2'=x\mathrm{e}^{-x}.
$$
Then $C_1=-x$ and $C_2=-(x+1)\mathrm{e}^{-x}$, a particular solution is $Y=-x^2-(x+1)=-(x^2+x+1)$, and the general solution is $y=C_1x+C_2\mathrm{e}^x-(x^2+x+1)$.

## 16.3. Homogeneous Linear Equations with Constant Coefficients

### 16.3.1. Differential Operators and the Characteristic Equation

Write $\mathrm{D}=\dfrac{\mathrm{d}}{\mathrm{d}x}$ and $\mathrm{D}^ky=y^{(k)}$. For a polynomial $P(\lambda)=\lambda^n+a_1\lambda^{n-1}+\cdots+a_n$ (with constant $a_k$), define $P(\mathrm{D})=\mathrm{D}^n+a_1\mathrm{D}^{n-1}+\cdots+a_n$. A linear equation with constant coefficients then reads

$$
P(\mathrm{D})y=y^{(n)}+a_1y^{(n-1)}+\cdots+a_{n-1}y'+a_ny=f(x).\tag{16.3}
$$
Operators with constant coefficients compose like polynomials: $P(\mathrm{D})Q(\mathrm{D})=(PQ)(\mathrm{D})$, and they commute. So a factorization of $P$ corresponds to a factorization of the operator, for example $\mathrm{D}^2-3\mathrm{D}+2=(\mathrm{D}-1)(\mathrm{D}-2)$.

Exponential functions are "eigenvectors" of $\mathrm{D}$: $\mathrm{D}\mathrm{e}^{\lambda x}=\lambda\mathrm{e}^{\lambda x}$, so $P(\mathrm{D})\mathrm{e}^{\lambda x}=P(\lambda)\mathrm{e}^{\lambda x}$. Hence $\mathrm{e}^{\lambda x}$ is a solution of the homogeneous equation if and only if $P(\lambda)=0$.

**Definition 16.3.1** The algebraic equation $P(\lambda)=\lambda^n+a_1\lambda^{n-1}+\cdots+a_n=0$ is called the **characteristic equation** of the homogeneous equation with constant coefficients $P(\mathrm{D})y=0$, and its roots are called the **characteristic roots** of the equation.

The characteristic equation says exactly that the **characteristic polynomial** of the coefficient matrix (a **companion matrix**, [2.1.6](/2.1.6)) obtained by converting the equation into a system in 16.6.5 equals zero, and the characteristic roots are the eigenvalues of this matrix.

When $\lambda$ is a root of multiplicity $k$, we obtain only one solution $\mathrm{e}^{\lambda x}$ and are still $k-1$ solutions short. The following lemma is the basic tool for handling repeated roots and nonhomogeneous equations.

**Lemma 16.3.1 (Shift Formula)** Let $u(x)$ have derivatives of order $n$ and let $\lambda$ be a complex number. Then

$$
P(\mathrm{D})\big(\mathrm{e}^{\lambda x}u\big)=\mathrm{e}^{\lambda x}P(\mathrm{D}+\lambda)u.
$$

**Proof** We have $\mathrm{D}(\mathrm{e}^{\lambda x}u)=\mathrm{e}^{\lambda x}(u'+\lambda u)=\mathrm{e}^{\lambda x}(\mathrm{D}+\lambda)u$; repeated application gives $\mathrm{D}^m(\mathrm{e}^{\lambda x}u)=\mathrm{e}^{\lambda x}(\mathrm{D}+\lambda)^mu$ (this also follows from the **general Leibniz rule** and the binomial theorem), and we then take linear combinations. $\square$

Here $\lambda$ may be complex: for $\lambda=\alpha+\mathrm{i}\beta$, **Euler's formula** defines $\mathrm{e}^{\lambda x}=\mathrm{e}^{\alpha x}(\cos\beta x+\mathrm{i}\sin\beta x)$ (obtained from power series in [2.2.9](/2.2.9)). Complex-valued functions are differentiated by differentiating their real and imaginary parts, and a direct check shows that $(\mathrm{e}^{\lambda x})'=\lambda\mathrm{e}^{\lambda x}$ still holds. Since the coefficients of $P(\mathrm{D})$ are real, a complex-valued function $z=u+\mathrm{i}v$ satisfies $P(\mathrm{D})z=g+\mathrm{i}h$ if and only if $P(\mathrm{D})u=g$ and $P(\mathrm{D})v=h$: taking real and imaginary parts gives solutions of real equations.

### 16.3.2. Fundamental Sets of Solutions

**Theorem 16.3.1** Let the distinct real roots of the characteristic equation $P(\lambda)=0$ be $\lambda_1,\dots,\lambda_r$, with multiplicities $m_1,\dots,m_r$, and let the distinct pairs of complex conjugate roots be $\alpha_j\pm\mathrm{i}\beta_j$ ($\beta_j>0$), with multiplicities $l_j$ ($j=1,\dots,s$), so that $\sum m_i+2\sum l_j=n$. Then the following $n$ functions form a fundamental set of solutions of $P(\mathrm{D})y=0$:

1. Each real root $\lambda$ of multiplicity $m$ contributes $\mathrm{e}^{\lambda x},\ x\mathrm{e}^{\lambda x},\ \dots,\ x^{m-1}\mathrm{e}^{\lambda x}$;
2. Each pair of complex conjugate roots $\alpha\pm\mathrm{i}\beta$ of multiplicity $l$ contributes
   $$
   \mathrm{e}^{\alpha x}\cos\beta x,\ x\mathrm{e}^{\alpha x}\cos\beta x,\ \dots,\ x^{l-1}\mathrm{e}^{\alpha x}\cos\beta x;\qquad\mathrm{e}^{\alpha x}\sin\beta x,\ \dots,\ x^{l-1}\mathrm{e}^{\alpha x}\sin\beta x.
   $$

**Proof** They are solutions: let $\lambda$ (real or complex) be a root of multiplicity $m$, so that $P(\mu)=(\mu-\lambda)^mR(\mu)$ and $P(\mathrm{D}+\lambda)=\mathrm{D}^mR(\mathrm{D}+\lambda)$. By Lemma 16.3.1, for $k<m$,

$$
P(\mathrm{D})(x^k\mathrm{e}^{\lambda x})=\mathrm{e}^{\lambda x}R(\mathrm{D}+\lambda)\mathrm{D}^mx^k=0.
$$
For a complex root $\alpha+\mathrm{i}\beta$, $x^k\mathrm{e}^{(\alpha+\mathrm{i}\beta)x}$ is a complex-valued solution, and its real part $x^k\mathrm{e}^{\alpha x}\cos\beta x$ and imaginary part $x^k\mathrm{e}^{\alpha x}\sin\beta x$ are both real solutions.

Linear independence: it suffices to show that for distinct complex numbers $\mu_1,\dots,\mu_q$ and polynomials $p_1,\dots,p_q$, $\sum_{j}p_j(x)\mathrm{e}^{\mu_jx}\equiv0$ implies $p_j\equiv0$ for all $j$ (the real functions are linear combinations of the $\mathrm{e}^{\mu x}$, $\mathrm{e}^{\bar\mu x}$ terms and this representation is invertible, so complex linear independence implies real linear independence). We use induction on $q$. The case $q=1$ is obvious. Let $q\ge2$ and multiply both sides by $\mathrm{e}^{-\mu_qx}$: $\sum_{j<q}p_j\mathrm{e}^{(\mu_j-\mu_q)x}+p_q\equiv0$. Applying $\mathrm{D}^{d+1}$ ($d=\deg p_q$) annihilates $p_q$; by Lemma 16.3.1, $\mathrm{D}^{d+1}(p_j\mathrm{e}^{\nu x})=\mathrm{e}^{\nu x}(\mathrm{D}+\nu)^{d+1}p_j$, and when $\nu=\mu_j-\mu_q\ne0$ the polynomial $(\mathrm{D}+\nu)^{d+1}p_j$ has the same degree as $p_j$ (its leading term is multiplied by $\nu^{d+1}$). By the induction hypothesis these polynomials all vanish, so $p_j\equiv0$ ($j<q$), and therefore $p_q\equiv0$. $\square$

**Algorithm 16.3.1 (Homogeneous Linear Equations with Constant Coefficients)** To solve $y^{(n)}+a_1y^{(n-1)}+\cdots+a_ny=0$:

1. Write down the characteristic equation $\lambda^n+a_1\lambda^{n-1}+\cdots+a_n=0$ and find all characteristic roots and their multiplicities;
2. Write down $n$ linearly independent solutions according to Theorem 16.3.1; the general solution is an arbitrary linear combination of them.

The three cases for the second-order equation $y''+py'+qy=0$:

| Discriminant $p^2-4q$ | Characteristic roots | General solution |
|---|---|---|
| $>0$ | Two distinct real roots $\lambda_1,\lambda_2$ | $C_1\mathrm{e}^{\lambda_1x}+C_2\mathrm{e}^{\lambda_2x}$ |
| $=0$ | A double real root $\lambda=-\frac p2$ | $(C_1+C_2x)\mathrm{e}^{\lambda x}$ |
| $<0$ | Complex conjugate roots $\alpha\pm\mathrm{i}\beta$ | $\mathrm{e}^{\alpha x}(C_1\cos\beta x+C_2\sin\beta x)$ |

**Example 16.3.1** Solve the following equations. (1) $y^{(4)}-y=0$: $\lambda^4-1=0$ has roots $\pm1$, $\pm\mathrm{i}$, so the general solution is $C_1\mathrm{e}^x+C_2\mathrm{e}^{-x}+C_3\cos x+C_4\sin x$.

(2) $y'''-3y''+3y'-y=0$: $(\lambda-1)^3=0$ has the triple root $1$, so the general solution is $(C_1+C_2x+C_3x^2)\mathrm{e}^x$.

(3) $y^{(4)}+y''+y=0$: $\lambda^4+\lambda^2+1=(\lambda^2+1)^2-\lambda^2=(\lambda^2+\lambda+1)(\lambda^2-\lambda+1)$ has roots $\dfrac{-1\pm\sqrt3\,\mathrm{i}}{2}$ and $\dfrac{1\pm\sqrt3\,\mathrm{i}}{2}$, so the general solution is

$$
y=\mathrm{e}^{-x/2}\Big(C_1\cos\frac{\sqrt3}2x+C_2\sin\frac{\sqrt3}2x\Big)+\mathrm{e}^{x/2}\Big(C_3\cos\frac{\sqrt3}2x+C_4\sin\frac{\sqrt3}2x\Big).
$$

(4) $y^{(4)}-2y'''+5y''=0$: $\lambda^2(\lambda^2-2\lambda+5)=0$ has roots $0$ (double) and $1\pm2\mathrm{i}$, so the general solution is $C_1+C_2x+\mathrm{e}^x(C_3\cos2x+C_4\sin2x)$.

**Example 16.3.2** Find a third-order homogeneous equation with constant coefficients having the solutions $\mathrm{e}^{-x}$, $2x\mathrm{e}^{-x}$, $3\mathrm{e}^x$. By Theorem 16.3.1, $-1$ is a root of multiplicity at least two and $1$ is a root, so the characteristic equation of a third-order equation must be $(\lambda+1)^2(\lambda-1)=\lambda^3+\lambda^2-\lambda-1=0$, and the required equation is $y'''+y''-y'-y=0$.

## 16.4. Nonhomogeneous Equations with Constant Coefficients

### 16.4.1. The Method of Undetermined Coefficients

When the right-hand side $f$ is a polynomial, an exponential, a sine or cosine, or a product of these, a particular solution has the same form as $f$; we can posit a particular solution with undetermined coefficients and substitute it into the equation. Below, $Q_m(x)$ denotes a polynomial of degree $m$.

**Theorem 16.4.1** Let $\lambda$ be a root of $P(\lambda)=0$ of multiplicity $k$ ($k=0$ if $\lambda$ is not a root), and let $Q_m$ be a polynomial of degree $m$. Then $P(\mathrm{D})y=Q_m(x)\mathrm{e}^{\lambda x}$ has a particular solution of the form

$$
y^*=x^kS_m(x)\mathrm{e}^{\lambda x},
$$
where $S_m$ is a polynomial of degree $m$ to be determined.

**Proof** Write $P(\mu)=(\mu-\lambda)^kR(\mu)$ with $R(\lambda)\ne0$. By Lemma 16.3.1, $P(\mathrm{D})(x^kS\mathrm{e}^{\lambda x})=\mathrm{e}^{\lambda x}R(\mathrm{D}+\lambda)\mathrm{D}^k(x^kS)$. The operator $\mathrm{D}^k$ maps the polynomial $x^kS$ of degree $m+k$ to a polynomial of degree $m$, and $x^kS\mapsto\mathrm{D}^k(x^kS)$ is a bijection on the space of polynomials of degree at most $m$ (compare leading terms and determine the coefficients one by one); $R(\mathrm{D}+\lambda)$ has constant term $R(\lambda)\ne0$ and is likewise invertible on polynomials (comparing coefficients, we can solve for them one by one from the highest degree down). Hence the equation $R(\mathrm{D}+\lambda)\mathrm{D}^k(x^kS)=Q_m$ has a unique polynomial solution $S$ of degree $m$. $\square$

When the right-hand side is $Q_m(x)\mathrm{e}^{\alpha x}\cos\beta x$ or $Q_m(x)\mathrm{e}^{\alpha x}\sin\beta x$, it is the real or imaginary part of $Q_m(x)\mathrm{e}^{(\alpha+\mathrm{i}\beta)x}$. We find a particular solution of the complex equation by Theorem 16.4.1 and take its real or imaginary part; alternatively, we can posit a particular solution in real form directly.

**Algorithm 16.4.1 (Method of Undetermined Coefficients)** To find a particular solution of $P(\mathrm{D})y=f(x)$, posit a particular solution according to the table below, substitute it into the equation and compare coefficients; when $f$ is a sum of several terms, solve for each term separately and add the results, by the superposition principle.

| Right-hand side $f(x)$ | Form of particular solution | Choice of $k$ |
|---|---|---|
| $Q_m(x)$ | $x^kS_m(x)$ | Multiplicity of $0$ as a characteristic root |
| $Q_m(x)\mathrm{e}^{\lambda x}$ | $x^kS_m(x)\mathrm{e}^{\lambda x}$ | Multiplicity of $\lambda$ as a characteristic root |
| $\mathrm{e}^{\alpha x}\big(Q_m(x)\cos\beta x+\tilde Q_l(x)\sin\beta x\big)$ | $x^k\mathrm{e}^{\alpha x}\big(S_M(x)\cos\beta x+T_M(x)\sin\beta x\big)$, $M=\max\{m,l\}$ | Multiplicity of $\alpha+\mathrm{i}\beta$ as a characteristic root |
| Same as above (complex exponential method) | Find the particular solution $x^kS_m(x)\mathrm{e}^{(\alpha+\mathrm{i}\beta)x}$ of $P(\mathrm{D})z=Q_m(x)\mathrm{e}^{(\alpha+\mathrm{i}\beta)x}$ and take its real part (for $\cos$) or imaginary part (for $\sin$) | Same as above |

In the third row, even if $f$ contains only $\cos\beta x$, the particular solution must include both a $\cos\beta x$ term and a $\sin\beta x$ term.

**Example 16.4.1** Solve $y''-y=2x\mathrm{e}^x$. The characteristic roots are $\pm1$, and $1$ is a simple root, so we posit $y^*=x(ax+b)\mathrm{e}^x$. By Lemma 16.3.1,

$$
(\mathrm{D}^2-1)\big((ax^2+bx)\mathrm{e}^x\big)=\mathrm{e}^x\big((\mathrm{D}+1)^2-1\big)(ax^2+bx)=\mathrm{e}^x(\mathrm{D}^2+2\mathrm{D})(ax^2+bx)=\mathrm{e}^x(4ax+2a+2b),
$$
and comparing coefficients, $4a=2$ and $2a+2b=0$, so $a=\frac12$ and $b=-\frac12$. The general solution is $y=C_1\mathrm{e}^x+C_2\mathrm{e}^{-x}+\dfrac{x^2-x}2\mathrm{e}^x$.

(The shift formula turns "substitute and differentiate twice" into an operation on polynomials, which is simpler than direct substitution.)

**Example 16.4.2** Solve $y''-2y'+y=4x\mathrm{e}^x$. Since $1$ is a double characteristic root, we posit $y^*=x^2(ax+b)\mathrm{e}^x$; then $(\mathrm{D}-1)^2(x^2(ax+b)\mathrm{e}^x)=\mathrm{e}^x\mathrm{D}^2(ax^3+bx^2)=\mathrm{e}^x(6ax+2b)$, which gives $a=\frac23$ and $b=0$. The general solution is $y=(C_1+C_2x)\mathrm{e}^x+\dfrac23x^3\mathrm{e}^x$.

**Example 16.4.3** Solve $y''-2y'+4y=\cos x+\mathrm{e}^x\sin x$. The characteristic roots are $1\pm\sqrt3\,\mathrm{i}$.

- For $\cos x$: $\mathrm{i}$ is not a characteristic root, and a particular solution of $P(\mathrm{D})z=\mathrm{e}^{\mathrm{i}x}$ is $z=\dfrac{\mathrm{e}^{\mathrm{i}x}}{P(\mathrm{i})}=\dfrac{\mathrm{e}^{\mathrm{i}x}}{3-2\mathrm{i}}=\dfrac{(3+2\mathrm{i})(\cos x+\mathrm{i}\sin x)}{13}$; its real part $\dfrac{3\cos x-2\sin x}{13}$ is a particular solution of $P(\mathrm{D})y=\cos x$;
- For $\mathrm{e}^x\sin x$: $1+\mathrm{i}$ is not a characteristic root, $P(1+\mathrm{i})=(1+\mathrm{i})^2-2(1+\mathrm{i})+4=2$, and $z=\dfrac12\mathrm{e}^{(1+\mathrm{i})x}$, whose imaginary part is $\dfrac12\mathrm{e}^x\sin x$.

The general solution is $y=\mathrm{e}^x(C_1\cos\sqrt3x+C_2\sin\sqrt3x)+\dfrac{3\cos x-2\sin x}{13}+\dfrac12\mathrm{e}^x\sin x$.

**Example 16.4.4** Solve $y''+9y=18\cos3x+30\sin3x$. Since $3\mathrm{i}$ is a simple characteristic root, we seek a particular solution $z=Ax\mathrm{e}^{3\mathrm{i}x}$ of $(\mathrm{D}^2+9)z=\mathrm{e}^{3\mathrm{i}x}$. By Lemma 16.3.1, $(\mathrm{D}^2+9)(Ax\mathrm{e}^{3\mathrm{i}x})=\mathrm{e}^{3\mathrm{i}x}\big((\mathrm{D}+3\mathrm{i})^2+9\big)(Ax)=\mathrm{e}^{3\mathrm{i}x}(\mathrm{D}^2+6\mathrm{i}\mathrm{D})(Ax)=6\mathrm{i}A\mathrm{e}^{3\mathrm{i}x}$, so $A=\dfrac{1}{6\mathrm{i}}=-\dfrac{\mathrm{i}}{6}$ and

$$
z=-\frac{\mathrm{i}}{6}x(\cos3x+\mathrm{i}\sin3x)=\frac x6(\sin3x-\mathrm{i}\cos3x).
$$
The term $\cos3x$ corresponds to the real part $\frac x6\sin3x$, and $\sin3x$ to the imaginary part $-\frac x6\cos3x$. The general solution is

$$
y=C_1\cos3x+C_2\sin3x+x(3\sin3x-5\cos3x).
$$

**Example 16.4.5** Solve $y''+y=x\cos2x$. Since $2\mathrm{i}$ is not a characteristic root, we posit $y^*=(a_1x+b_1)\cos2x+(a_2x+b_2)\sin2x$; substitution gives

$$
(-3a_1x-3b_1+4a_2)\cos2x+(-3a_2x-3b_2-4a_1)\sin2x=x\cos2x,
$$
and comparing coefficients, $a_1=-\frac13$, $a_2=0$, $b_1=0$ and $b_2=\frac49$. The general solution is $y=C_1\cos x+C_2\sin x-\dfrac13x\cos2x+\dfrac49\sin2x$.

**Example 16.4.6** Write down the form of a particular solution of $y''+2y'-3y=3\mathrm{e}^x+\sin2x+\mathrm{e}^x\cos2x$. The characteristic roots are $1,-3$. The three terms correspond to $\lambda=1$ (a simple root, $k=1$), $2\mathrm{i}$ ($k=0$) and $1+2\mathrm{i}$ ($k=0$), so the particular solution has the form

$$
y^*=Ax\mathrm{e}^x+(B\cos2x+C\sin2x)+\mathrm{e}^x(D\cos2x+E\sin2x).
$$

### 16.4.2. The Operator Method

Factoring and "inverting" $P(\mathrm{D})$ as if it were a polynomial gives another set of techniques for finding particular solutions, called the *operator method*.

Method (1): successive reduction of order ("peeling off" factors). A polynomial $P$ with real coefficients factors into real linear and quadratic factors. If $P(\mathrm{D})=(\mathrm{D}-\lambda_1)R(\mathrm{D})$, let $z=R(\mathrm{D})y$; first solve the first-order linear equation $z'-\lambda_1z=f$ (Eq. (15.3)), then solve the equation $R(\mathrm{D})y=z$ of one lower order. A quadratic factor $\mathrm{D}^2+s\mathrm{D}+t$ is handled in the same way, using variation of parameters for second-order equations. Each step uses only methods for first- and second-order equations, so in principle every nonhomogeneous equation with constant coefficients can be solved this way. The method places no restriction on the right-hand side.

**Example 16.4.7** Solve the following equations. (1) $y''-y=2x\mathrm{e}^x$: write it as $(\mathrm{D}-1)(\mathrm{D}+1)y=2x\mathrm{e}^x$. Let $z=(\mathrm{D}+1)y$; then $z'-z=2x\mathrm{e}^x$ and $z=\mathrm{e}^x\int2x\,\mathrm{d}x=x^2\mathrm{e}^x$ (taking one particular solution). Next solve $y'+y=x^2\mathrm{e}^x$: $y=\mathrm{e}^{-x}\int x^2\mathrm{e}^{2x}\,\mathrm{d}x=\Big(\dfrac{x^2}2-\dfrac x2+\dfrac14\Big)\mathrm{e}^x$. The term $\frac14\mathrm{e}^x$ is a homogeneous solution and can be dropped, in agreement with Example 16.4.1.

(2) $y'''+y'=\sec x$: let $z=y'$; then $z''+z=\sec x$, and by Example 16.2.3, $z=\cos x\ln\cos x+x\sin x$. Integrating gives the particular solution

$$
y=\int(\cos x\ln\cos x+x\sin x)\,\mathrm{d}x=\sin x\ln\cos x-x\cos x+\ln(\sec x+\tan x),
$$
where $\int\cos x\ln\cos x\,\mathrm{d}x=\sin x\ln\cos x+\int\frac{\sin^2x}{\cos x}\,\mathrm{d}x=\sin x\ln\cos x-\sin x+\ln(\sec x+\tan x)$ and $\int x\sin x\,\mathrm{d}x=-x\cos x+\sin x$. The general solution is $y=C_1+C_2\cos x+C_3\sin x+\sin x\ln\cos x-x\cos x+\ln(\sec x+\tan x)$.

Method (2): exponential right-hand sides. From $P(\mathrm{D})\mathrm{e}^{\lambda x}=P(\lambda)\mathrm{e}^{\lambda x}$ and Lemma 16.3.1:

**Proposition 16.4.1** If $P(\lambda)\ne0$, then $\dfrac{\mathrm{e}^{\lambda x}}{P(\lambda)}$ is a particular solution of $P(\mathrm{D})y=\mathrm{e}^{\lambda x}$. If $\lambda$ is a root of multiplicity $k$ and $P(\mu)=(\mu-\lambda)^kR(\mu)$, then $\dfrac{x^k\mathrm{e}^{\lambda x}}{k!\,R(\lambda)}$ is a particular solution.

**Proof** The first statement is checked directly. For the second, $P(\mathrm{D})\big(x^k\mathrm{e}^{\lambda x}\big)=\mathrm{e}^{\lambda x}R(\mathrm{D}+\lambda)\mathrm{D}^kx^k=k!\,R(\lambda)\mathrm{e}^{\lambda x}$, because $\mathrm{D}^kx^k=k!$ is a constant and $R(\mathrm{D}+\lambda)$ acting on a constant leaves only its constant term $R(\lambda)$. $\square$

**Example 16.4.8** Solve the following equations. (1) $y'''-2y''-5y'+6y=\mathrm{e}^{4x}$: $P(\lambda)=(\lambda-1)(\lambda-3)(\lambda+2)$ and $P(4)=18$, so a particular solution is $\dfrac{\mathrm{e}^{4x}}{18}$ and the general solution is $C_1\mathrm{e}^x+C_2\mathrm{e}^{3x}+C_3\mathrm{e}^{-2x}+\dfrac{\mathrm{e}^{4x}}{18}$.

(2) With the same operator, $y'''-2y''-5y'+6y=(\mathrm{e}^{2x}+3)^2=\mathrm{e}^{4x}+6\mathrm{e}^{2x}+9$: $P(2)=-4$ and $P(0)=6$, so a particular solution is $\dfrac{\mathrm{e}^{4x}}{18}-\dfrac32\mathrm{e}^{2x}+\dfrac32$.

(3) $y^{(4)}-y=\mathrm{e}^x$: $1$ is a simple root, $P(\mu)=(\mu-1)(\mu+1)(\mu^2+1)$ and $R(1)=4$, so a particular solution is $\dfrac{x\mathrm{e}^x}4$ and the general solution is $C_1\mathrm{e}^x+C_2\mathrm{e}^{-x}+C_3\cos x+C_4\sin x+\dfrac{x\mathrm{e}^x}{4}$.

(4) $y''+y'-2y=2\sin x$: $P(\mathrm{i})=-3+\mathrm{i}$ and $\dfrac{2\mathrm{e}^{\mathrm{i}x}}{-3+\mathrm{i}}=-\dfrac{(3+\mathrm{i})(\cos x+\mathrm{i}\sin x)}{5}$; taking the imaginary part gives the particular solution $-\dfrac{\cos x+3\sin x}5$.

Method (3): polynomial right-hand sides. If $f$ is a polynomial of degree $m$ and $P(0)\ne0$, expand $\dfrac1{P(\lambda)}$ in a power series $b_0+b_1\lambda+b_2\lambda^2+\cdots$ about $\lambda=0$ (by long division in ascending powers). Then

$$
y^*=\big(b_0+b_1\mathrm{D}+\cdots+b_m\mathrm{D}^m\big)f
$$
is a particular solution of $P(\mathrm{D})y=f$, because $P(\lambda)(b_0+\cdots+b_m\lambda^m)=1+O(\lambda^{m+1})$ and $\mathrm{D}^{m+1}f=0$. If $0$ is a root of multiplicity $k$, write $P(\mathrm{D})=\mathrm{D}^kR(\mathrm{D})$; first find in this way a polynomial solution $u$ of $R(\mathrm{D})u=f$, then integrate $k$ times.

**Example 16.4.9** Solve $2y''+2y'+3y=x^2+2x-1$. Since $\dfrac{1}{3+2\lambda+2\lambda^2}=\dfrac13-\dfrac29\lambda-\dfrac2{27}\lambda^2+\cdots$,

$$
y^*=\Big(\frac13-\frac29\mathrm{D}-\frac2{27}\mathrm{D}^2\Big)(x^2+2x-1)=\frac{x^2+2x-1}3-\frac29(2x+2)-\frac4{27}=\frac13x^2+\frac29x-\frac{25}{27}.
$$
The characteristic roots are $\dfrac{-1\pm\sqrt5\,\mathrm{i}}{2}$, so the general solution is $y=\mathrm{e}^{-x/2}\Big(C_1\cos\dfrac{\sqrt5}2x+C_2\sin\dfrac{\sqrt5}2x\Big)+\dfrac13x^2+\dfrac29x-\dfrac{25}{27}$.

### 16.4.3. Cauchy–Euler Equations

**Definition 16.4.1** An equation of the form

$$
x^ny^{(n)}+a_1x^{n-1}y^{(n-1)}+\cdots+a_{n-1}xy'+a_ny=f(x)\qquad(a_k\text{ constants})
$$
is called a **Cauchy–Euler equation**.

It has variable coefficients, but each term $x^ky^{(k)}$ is invariant under the scaling $x\mapsto cx$, and the substitution $x=\mathrm{e}^t$ transforms it into an equation with constant coefficients.

**Proposition 16.4.2** Let $x>0$, put $x=\mathrm{e}^t$ and write $\mathrm{D}=\dfrac{\mathrm{d}}{\mathrm{d}t}$. Then

$$
x^k\frac{\mathrm{d}^ky}{\mathrm{d}x^k}=\mathrm{D}(\mathrm{D}-1)\cdots(\mathrm{D}-k+1)y.
$$

**Proof** We have $\dfrac{\mathrm{d}y}{\mathrm{d}x}=\dfrac{\mathrm{d}y}{\mathrm{d}t}\cdot\dfrac{\mathrm{d}t}{\mathrm{d}x}=\dfrac1x\mathrm{D}y$, so the case $k=1$ holds. Suppose the formula holds for $k$, that is, $x^ky^{(k)}=Q_k(\mathrm{D})y$ with $Q_k(\mathrm{D})=\mathrm{D}(\mathrm{D}-1)\cdots(\mathrm{D}-k+1)$. Differentiate both sides with respect to $x$ and multiply by $x$: the left-hand side becomes $kx^ky^{(k)}+x^{k+1}y^{(k+1)}$ and the right-hand side becomes $x\cdot\dfrac1x\mathrm{D}Q_k(\mathrm{D})y$. Hence $x^{k+1}y^{(k+1)}=(\mathrm{D}-k)Q_k(\mathrm{D})y=Q_{k+1}(\mathrm{D})y$. $\square$

For $x<0$, putting $x=-\mathrm{e}^t$ gives the same result, so $\ln x$ in the final answer may be written as $\ln\lvert x\rvert$.

**Algorithm 16.4.2 (Cauchy–Euler Equations)** Put $x=\mathrm{e}^t$ and replace $x^ky^{(k)}$ by $\mathrm{D}(\mathrm{D}-1)\cdots(\mathrm{D}-k+1)y$ to obtain an equation with constant coefficients $P(\mathrm{D})y=f(\mathrm{e}^t)$; solve it by the methods of 16.3 and 16.4 and substitute back $t=\ln x$. A homogeneous solution $t^j\mathrm{e}^{\lambda t}$ becomes $x^\lambda\ln^jx$, so one can also substitute $y=x^\lambda$ directly into the homogeneous equation and solve for $\lambda$.

**Example 16.4.10** Solve the following equations. (1) Solve $x^3y'''+3x^2y''-2xy'+2y=0$. We get $[\mathrm{D}(\mathrm{D}-1)(\mathrm{D}-2)+3\mathrm{D}(\mathrm{D}-1)-2\mathrm{D}+2]y=(\mathrm{D}^3-3\mathrm{D}+2)y=(\mathrm{D}-1)^2(\mathrm{D}+2)y=0$, so $y=C_1\mathrm{e}^t+C_2t\mathrm{e}^t+C_3\mathrm{e}^{-2t}=C_1x+C_2x\ln x+\dfrac{C_3}{x^2}$.

(2) Solve $x^2y''-xy'+4y=\cos\ln x+x\sin\ln x$. The equation becomes $(\mathrm{D}^2-2\mathrm{D}+4)y=\cos t+\mathrm{e}^t\sin t$, which is the equation of Example 16.4.3 (with independent variable $t$), so

$$
y=x\big(C_1\cos(\sqrt3\ln x)+C_2\sin(\sqrt3\ln x)\big)+\frac{3\cos\ln x-2\sin\ln x}{13}+\frac x2\sin\ln x.
$$

(3) Solve $x^2y''+3xy'-8y=25x\ln x$. The equation becomes $(\mathrm{D}^2+2\mathrm{D}-8)y=25t\mathrm{e}^t$, with characteristic roots $2,-4$. Since $1$ is not a root, we posit $y^*=(at+b)\mathrm{e}^t$; by Lemma 16.3.1, $(\mathrm{D}^2+2\mathrm{D}-8)\big((at+b)\mathrm{e}^t\big)=\mathrm{e}^t(\mathrm{D}^2+4\mathrm{D}-5)(at+b)=\mathrm{e}^t(-5at+4a-5b)$, which gives $a=-5$ and $b=-4$. Hence

$$
y=C_1x^2+\frac{C_2}{x^4}-x(5\ln x+4).
$$

## 16.5. Vibration Problems

A body of mass $m$ attached to a spring moves along a straight line in a resisting medium. Let $x(t)$ be its displacement from the equilibrium position. The elastic restoring force is $-hx$ (Hooke's law), the resistance $-cx'$ is proportional to the velocity, and the external force is $F(t)$. By Newton's second law, $mx''=-hx-cx'+F(t)$; writing $\omega^2=h/m$, $2k=c/m$ and $f=F/m$,

$$
x''+2kx'+\omega^2x=f(t),\qquad\omega>0,\ k\ge0.\tag{16.4}
$$
The charge in a series RLC circuit satisfies the same equation.

### 16.5.1. Free Vibrations

This is the case $f=0$. The characteristic equation is $\lambda^2+2k\lambda+\omega^2=0$, with $\lambda=-k\pm\sqrt{k^2-\omega^2}$.

- Undamped ($k=0$): $x=C_1\cos\omega t+C_2\sin\omega t=A\sin(\omega t+\theta)$, where the amplitude is $A=\sqrt{C_1^2+C_2^2}$ and the initial phase $\theta$ satisfies $\sin\theta=C_1/A$, $\cos\theta=C_2/A$. This is simple harmonic motion with period $2\pi/\omega$, and $\omega$ is called the natural frequency.
- Underdamped ($0<k<\omega$, weak damping): $x=A\mathrm{e}^{-kt}\sin\big(\sqrt{\omega^2-k^2}\,t+\theta\big)$; the amplitude of the oscillation decays exponentially, and the frequency becomes $\sqrt{\omega^2-k^2}<\omega$.
- Critically damped ($k=\omega$): $x=(C_1+C_2t)\mathrm{e}^{-\omega t}$; the motion no longer oscillates and returns to equilibrium fastest.
- Overdamped ($k>\omega$, strong damping): $x=C_1\mathrm{e}^{(-k+\sqrt{k^2-\omega^2})t}+C_2\mathrm{e}^{(-k-\sqrt{k^2-\omega^2})t}$; both exponents are negative, and the body returns slowly and monotonically to equilibrium (crossing it at most once).

![The three damping regimes of x'' + 2k x' + x = 0 with initial values x(0) = 1, x'(0) = 0: underdamped, k = 0.15, the amplitude decays like e^{-kt} (dashed envelope); critically damped, k = 1, the fastest return to equilibrium; overdamped, k = 2.5, a slow return to equilibrium](./plots/damped-oscillation.py)

### 16.5.2. Forced Vibrations and Resonance

Suppose the external force is the periodic force $f(t)=H\sin pt$.

The undamped case ($k=0$). The equation is $x''+\omega^2x=H\sin pt$.

- $p\ne\omega$: $\mathrm{i}p$ is not a characteristic root; by Proposition 16.4.1, the imaginary part of $\dfrac{\mathrm{e}^{\mathrm{i}pt}}{\omega^2-p^2}$ gives a particular solution, and the general solution is
  $$
  x=A\sin(\omega t+\theta)+\frac{H}{\omega^2-p^2}\sin pt,
  $$
  a superposition of the natural vibration and the forced vibration. The closer $p$ is to $\omega$, the larger the amplitude of the forced vibration.
- $p=\omega$: $\mathrm{i}\omega$ is a simple root; by Proposition 16.4.1, the imaginary part $-\dfrac{t\cos\omega t}{2\omega}$ of $\dfrac{t\mathrm{e}^{\mathrm{i}\omega t}}{2\mathrm{i}\omega}$ gives a particular solution, and the general solution is
  $$
  x=A\sin(\omega t+\theta)-\frac{H}{2\omega}t\cos\omega t.
  $$
  The amplitude grows linearly in time without bound. The phenomenon in which the amplitude grows without bound when the frequency of the external force equals the natural frequency is called *resonance*.

The damped case ($0<k<\omega$). Here $\mathrm{i}p$ is not a characteristic root, and $P(\mathrm{i}p)=\omega^2-p^2+2kp\,\mathrm{i}$, so

$$
\frac{\mathrm{e}^{\mathrm{i}pt}}{\omega^2-p^2+2kp\,\mathrm{i}}=\frac{\big((\omega^2-p^2)-2kp\,\mathrm{i}\big)(\cos pt+\mathrm{i}\sin pt)}{(\omega^2-p^2)^2+4k^2p^2}.
$$
Taking the imaginary part, the general solution is

$$
x=A\mathrm{e}^{-kt}\sin\big(\sqrt{\omega^2-k^2}\,t+\theta\big)+H\frac{(\omega^2-p^2)\sin pt-2kp\cos pt}{(\omega^2-p^2)^2+4k^2p^2}
=A\mathrm{e}^{-kt}\sin\big(\sqrt{\omega^2-k^2}\,t+\theta\big)+\frac{H}{\sqrt{(\omega^2-p^2)^2+4k^2p^2}}\sin(pt-\varphi),
$$
where $\tan\varphi=\dfrac{2kp}{\omega^2-p^2}$. The first term decays in time (the transient), and the second is a steady-state oscillation with the same frequency as the external force and bounded amplitude: with damping, the amplitude never grows without bound. The steady-state amplitude

$$
A(p)=\frac{H}{\sqrt{(\omega^2-p^2)^2+4k^2p^2}},
$$
as a function of $p$, attains its maximum $\dfrac{H}{2k\sqrt{\omega^2-k^2}}$ at $p=\sqrt{\omega^2-2k^2}$ when $k<\omega/\sqrt2$ (minimize $(\omega^2-p^2)^2+4k^2p^2$ as a function of $p^2$). The smaller the damping, the higher and sharper the peak and the closer its location to $\omega$; as $k\to0$ we recover undamped resonance.

![Left: the steady-state amplitude A(p) as a function of the driving frequency p (H = 1, ω = 1); the smaller the damping, the higher the resonance peak and the closer it is to p = ω. Right: the particular solution -(t cos t)/2 of the undamped resonant equation x'' + x = sin t, whose amplitude grows linearly](./plots/resonance.py)

## 16.6. Systems of Linear Differential Equations

### 16.6.1. General Concepts

Let $A(t)=(a_{ij}(t))$ be an $n\times n$ matrix of functions, $\boldsymbol{f}(t)=(f_1(t),\dots,f_n(t))^{\mathsf T}$, and let $\boldsymbol{x}(t)=(x_1(t),\dots,x_n(t))^{\mathsf T}$ be the vector of unknown functions. Continuity, derivatives and integrals of matrices of functions are all defined entrywise ([2.1.11](/2.1.11#sec-11.1)).

**Definition 16.6.1** The system

$$
\begin{cases}x_1'=a_{11}(t)x_1+\cdots+a_{1n}(t)x_n+f_1(t),\\ \quad\vdots\\ x_n'=a_{n1}(t)x_1+\cdots+a_{nn}(t)x_n+f_n(t)\end{cases}
\qquad\text{i.e.}\qquad\boldsymbol{x}'=A(t)\boldsymbol{x}+\boldsymbol{f}(t)\tag{16.5}
$$
is called a (first-order) **system of linear differential equations**; when $\boldsymbol{f}\equiv\boldsymbol{0}$,

$$
\boldsymbol{x}'=A(t)\boldsymbol{x}\tag{16.6}
$$
is called a homogeneous system. When $A$ is a constant matrix, the system is called a linear system with constant coefficients.

**Theorem 16.6.1** If $A(t)$ and $\boldsymbol{f}(t)$ are continuous on an interval $I$, then for any $t_0\in I$ and $\boldsymbol{\eta}\in\mathbb{R}^n$, the initial value problem $\boldsymbol{x}'=A(t)\boldsymbol{x}+\boldsymbol{f}(t)$, $\boldsymbol{x}(t_0)=\boldsymbol{\eta}$ has a unique solution on the whole of $I$.

Differentiation of matrices of functions obeys the product rule $(AB)'=A'B+AB'$, but the derivative of a determinant is not the determinant of the derivatives: $\dfrac{\mathrm{d}}{\mathrm{d}t}\det A(t)$ equals the sum of the $n$ determinants obtained by replacing the $i$th row of $\det A(t)$ by the derivative of that row ($i=1,\dots,n$), which follows from the linearity of the determinant in each row and the product rule. We use this below to compute the derivative of the Wronskian.

### 16.6.2. Structure of Solutions

This is entirely parallel to Section 16.1. Linear dependence and independence of a set of vector functions $\boldsymbol{\varphi}_1(t),\dots,\boldsymbol{\varphi}_n(t)$ are defined as in [Definition 11.2.1 of 2.1.11](/2.1.11#def-11.2.1) (with constant coefficients), and

$$
W(t)=\det\big(\boldsymbol{\varphi}_1(t),\dots,\boldsymbol{\varphi}_n(t)\big)
$$
is called their **Wronskian**. If they are linearly dependent, then $W\equiv0$.

**Theorem 16.6.2** Let $\boldsymbol{\varphi}_1,\dots,\boldsymbol{\varphi}_n$ be solutions of the homogeneous system (16.6) on $I$.

1. If $W(t_0)=0$ for some $t_0\in I$, then $\boldsymbol{\varphi}_1,\dots,\boldsymbol{\varphi}_n$ are linearly dependent, and hence $W\equiv0$; thus $W$ is either identically zero or nowhere zero;
2. (Liouville's formula) $W(t)=W(t_0)\,\mathrm{e}^{\int_{t_0}^t\operatorname{tr}(A(s))\,\mathrm{d}s}$.

**Proof** (1) Since $W(t_0)=0$, there are $c_1,\dots,c_n$, not all zero, with $\sum c_k\boldsymbol{\varphi}_k(t_0)=\boldsymbol{0}$. Both $\sum c_k\boldsymbol{\varphi}_k(t)$ and $\boldsymbol{0}$ are solutions of (16.6) satisfying $\boldsymbol{x}(t_0)=\boldsymbol{0}$, so $\sum c_k\boldsymbol{\varphi}_k\equiv\boldsymbol{0}$ by uniqueness. (2) Let $\Phi=(\boldsymbol{\varphi}_1,\dots,\boldsymbol{\varphi}_n)$. By the rule for differentiating determinants above, the derivative of row $i$ is $\sum_ja_{ij}(\text{row }j)$; after substituting it and subtracting multiples of the rows $j\ne i$, only $a_{ii}\det\Phi$ remains. Hence $W'=\operatorname{tr}(A)W$, and solving this first-order linear equation gives the formula. $\square$

**Theorem 16.6.3** The solution set of the homogeneous system (16.6) is an $n$-dimensional vector space.

**Proof** Let $\boldsymbol{\varphi}_k$ be the solution with $\boldsymbol{\varphi}_k(t_0)=\boldsymbol{e}_k$. Then $W(t_0)=1$, so they are linearly independent; any solution $\boldsymbol{\varphi}$ and $\sum_k\eta_k\boldsymbol{\varphi}_k$ (with $\boldsymbol{\eta}=\boldsymbol{\varphi}(t_0)$) satisfy the same initial condition, so they are equal by uniqueness. $\square$

**Definition 16.6.2** A set of $n$ linearly independent solutions of the system (16.6) is called a **fundamental set of solutions** of it; the matrix $\Phi(t)=(\boldsymbol{\varphi}_1(t),\dots,\boldsymbol{\varphi}_n(t))$ whose columns form a fundamental set of solutions is called a **fundamental matrix**.

A matrix $\Phi$ is a fundamental matrix if and only if $\Phi'=A\Phi$ and $\det\Phi(t)\ne0$. The general solution of the homogeneous system is $\boldsymbol{x}=\Phi(t)\boldsymbol{c}$ with $\boldsymbol{c}$ an arbitrary constant vector, and the solution satisfying $\boldsymbol{x}(t_0)=\boldsymbol{x}_0$ is

$$
\boldsymbol{x}(t)=\Phi(t)\Phi^{-1}(t_0)\boldsymbol{x}_0,
$$
because $\boldsymbol{c}$ is uniquely determined by $\Phi(t_0)\boldsymbol{c}=\boldsymbol{x}_0$. With constant coefficients, $\mathrm{e}^{tA}$ is the fundamental matrix satisfying $\Phi(0)=I$ ([Theorem 11.9.1 of 2.1.11](/2.1.11#thm-11.9.1)); every fundamental matrix satisfies $\Phi(t)\Phi^{-1}(0)=\mathrm{e}^{tA}$, and Liouville's formula becomes $\det\mathrm{e}^{tA}=\mathrm{e}^{t\operatorname{tr}(A)}$.

**Example 16.6.1** Solve the following problems. (1) Solve $\boldsymbol{x}'=\begin{bmatrix}1&1\\0&1\end{bmatrix}\boldsymbol{x}$. The second equation $x_2'=x_2$ gives $x_2=C_2\mathrm{e}^t$; substituting into the first equation gives $x_1'-x_1=C_2\mathrm{e}^t$, and Eq. (15.3) gives $x_1=\mathrm{e}^t(C_2t+C_1)$. Hence

$$
\boldsymbol{x}=C_1\begin{bmatrix}\mathrm{e}^t\\0\end{bmatrix}+C_2\begin{bmatrix}t\mathrm{e}^t\\ \mathrm{e}^t\end{bmatrix},\qquad\Phi(t)=\begin{bmatrix}\mathrm{e}^t&t\mathrm{e}^t\\0&\mathrm{e}^t\end{bmatrix},\quad\det\Phi=\mathrm{e}^{2t}=\mathrm{e}^{t\operatorname{tr}(A)}.
$$

(2) Find the solution with $\boldsymbol{x}(0)=(3,2)^{\mathsf T}$. Since $\Phi(0)=I$, $\boldsymbol{x}=\Phi(t)\boldsymbol{x}(0)=\big((3+2t)\mathrm{e}^t,\ 2\mathrm{e}^t\big)^{\mathsf T}$. Here $\Phi(t)=\mathrm{e}^{tA}$, $A$ is a Jordan block, and the term $t\mathrm{e}^t$ comes from a Jordan chain ([Corollary 11.9.1 of 2.1.11](/2.1.11#cor-11.9.1)).

### 16.6.3. Nonhomogeneous Systems and Variation of Parameters

By the superposition principle, the general solution of the nonhomogeneous system (16.5) equals one particular solution of it plus the general solution of the homogeneous system. A particular solution is again found by variation of parameters:

**Theorem 16.6.4** Let $\Phi(t)$ be a fundamental matrix of (16.6). Then the general solution of (16.5) is

$$
\boldsymbol{x}(t)=\Phi(t)\boldsymbol{c}+\Phi(t)\int_{t_0}^t\Phi^{-1}(s)\boldsymbol{f}(s)\,\mathrm{d}s.\tag{16.7}
$$

**Proof** Let $\boldsymbol{x}=\Phi(t)\boldsymbol{c}(t)$. Then $\boldsymbol{x}'=\Phi'\boldsymbol{c}+\Phi\boldsymbol{c}'=A\Phi\boldsymbol{c}+\Phi\boldsymbol{c}'$. Substituting into (16.5) gives $\Phi\boldsymbol{c}'=\boldsymbol{f}$, so $\boldsymbol{c}'=\Phi^{-1}\boldsymbol{f}$, and integration gives the result. $\square$

When $\Phi=\mathrm{e}^{tA}$, we have $\Phi(t)\Phi^{-1}(s)=\mathrm{e}^{(t-s)A}$, and Eq. (16.7) is the **variation of constants formula** of [2.1.11](/2.1.11#sec-11.9). For the second-order equation $y''+a_1y'+a_2y=f$ with $\boldsymbol{x}=(y,y')^{\mathsf T}$, the vector $\Phi^{-1}\boldsymbol{f}$ in Eq. (16.7) is exactly the vector $(C_1',C_2')^{\mathsf T}$ obtained by Cramer's rule in Algorithm 16.2.1.

**Example 16.6.2** Solve $\boldsymbol{x}'=\begin{bmatrix}1&1\\0&1\end{bmatrix}\boldsymbol{x}+\begin{bmatrix}\mathrm{e}^{-t}\\0\end{bmatrix}$, $\boldsymbol{x}(0)=\begin{bmatrix}-1\\1\end{bmatrix}$. By Example 16.6.1, $\Phi(t)=\begin{bmatrix}\mathrm{e}^t&t\mathrm{e}^t\\0&\mathrm{e}^t\end{bmatrix}$ and $\Phi^{-1}(s)=\begin{bmatrix}\mathrm{e}^{-s}&-s\mathrm{e}^{-s}\\0&\mathrm{e}^{-s}\end{bmatrix}$, so

$$
\int_0^t\Phi^{-1}(s)\boldsymbol{f}(s)\,\mathrm{d}s=\int_0^t\begin{bmatrix}\mathrm{e}^{-2s}\\0\end{bmatrix}\mathrm{d}s=\begin{bmatrix}\frac{1-\mathrm{e}^{-2t}}{2}\\0\end{bmatrix}.
$$
From $\boldsymbol{x}(0)=\Phi(0)\boldsymbol{c}=\boldsymbol{c}$ we get $\boldsymbol{c}=(-1,1)^{\mathsf T}$, so

$$
\boldsymbol{x}(t)=\Phi(t)\begin{bmatrix}-\frac12-\frac12\mathrm{e}^{-2t}\\1\end{bmatrix}=\begin{bmatrix}t\mathrm{e}^t-\frac{\mathrm{e}^t+\mathrm{e}^{-t}}{2}\\ \mathrm{e}^t\end{bmatrix}.
$$

### 16.6.4. Homogeneous Systems with Constant Coefficients

For a system with constant coefficients $\boldsymbol{x}'=A\boldsymbol{x}$, we try, as for $n$th-order equations, $\boldsymbol{x}=\mathrm{e}^{\lambda t}\boldsymbol{r}$ with $\boldsymbol{r}\ne\boldsymbol{0}$ a constant vector. Substitution gives $\lambda\mathrm{e}^{\lambda t}\boldsymbol{r}=\mathrm{e}^{\lambda t}A\boldsymbol{r}$, that is, $A\boldsymbol{r}=\lambda\boldsymbol{r}$: $\mathrm{e}^{\lambda t}\boldsymbol{r}$ is a solution if and only if $(\lambda,\boldsymbol{r})$ is an eigenvalue–eigenvector pair of $A$. The numbers $\lambda$ are the roots of the **characteristic polynomial** $\det(\lambda I-A)$.

**Theorem 16.6.5** If $A$ has $n$ linearly independent eigenvectors $\boldsymbol{r}_1,\dots,\boldsymbol{r}_n$ (that is, $A$ is a **diagonalizable matrix**) with corresponding eigenvalues $\lambda_1,\dots,\lambda_n$, then $\mathrm{e}^{\lambda_1t}\boldsymbol{r}_1,\dots,\mathrm{e}^{\lambda_nt}\boldsymbol{r}_n$ form a fundamental set of solutions of $\boldsymbol{x}'=A\boldsymbol{x}$.

**Proof** Each is a solution (see above); the Wronskian at $t=0$ is $\det(\boldsymbol{r}_1,\dots,\boldsymbol{r}_n)\ne0$, so by Theorem 16.6.2 they are linearly independent. $\square$

When $A$ is a real matrix, $\lambda=\alpha+\mathrm{i}\beta$ ($\beta\ne0$) is a complex eigenvalue and $\boldsymbol{r}=\boldsymbol{a}+\mathrm{i}\boldsymbol{b}$ is a corresponding eigenvector, $\mathrm{e}^{\lambda t}\boldsymbol{r}$ is a complex-valued solution, and its real and imaginary parts

$$
\mathrm{e}^{\alpha t}\big(\boldsymbol{a}\cos\beta t-\boldsymbol{b}\sin\beta t\big),\qquad\mathrm{e}^{\alpha t}\big(\boldsymbol{a}\sin\beta t+\boldsymbol{b}\cos\beta t\big)
$$
are two linearly independent real solutions, which replace the two complex solutions corresponding to the conjugate eigenvalues $\alpha\pm\mathrm{i}\beta$.

**Algorithm 16.6.1 (Homogeneous Systems with Constant Coefficients, $A$ Diagonalizable)**

1. Find the roots $\lambda_1,\dots,\lambda_n$ of the characteristic polynomial $\det(\lambda I-A)$;
2. For each eigenvalue find eigenvectors (for a repeated eigenvalue, a basis of its eigenspace); for a pair of complex conjugate eigenvalues it suffices to find an eigenvector for one of them and take the real and imaginary parts of $\mathrm{e}^{\lambda t}\boldsymbol{r}$;
3. The general solution is $\boldsymbol{x}=\sum C_k\mathrm{e}^{\lambda_kt}\boldsymbol{r}_k$.

If $A$ is not diagonalizable (it has a **defective eigenvalue**), there are fewer than $n$ independent eigenvectors, and solutions of the form $\mathrm{e}^{\lambda t}(t\boldsymbol{p}_1+\boldsymbol{p}_2)$ are also needed, where $\boldsymbol{p}_1,\boldsymbol{p}_2,\dots$ form a **Jordan chain**; in general the fundamental matrix is $\mathrm{e}^{tA}=P\mathrm{e}^{tJ}P^{-1}$, see [Corollary 11.9.1 of 2.1.11](/2.1.11#cor-11.9.1) and [Example 11.9.1](/2.1.11#ex-11.9.1). Example 16.6.1 is the simplest case of this kind.

**Example 16.6.3** Solve $\begin{cases}x_1'=x_2-x_3,\\x_2'=x_3,\\x_3'=x_2.\end{cases}$ We have $\det(\lambda I-A)=\begin{vmatrix}\lambda&-1&1\\0&\lambda&-1\\0&-1&\lambda\end{vmatrix}=\lambda(\lambda-1)(\lambda+1)$, with eigenvalues $0,1,-1$ and eigenvectors $\boldsymbol{r}_1=(1,0,0)^{\mathsf T}$, $\boldsymbol{r}_2=(0,1,1)^{\mathsf T}$, $\boldsymbol{r}_3=(2,-1,1)^{\mathsf T}$. The general solution is

$$
\boldsymbol{x}=\begin{bmatrix}1&0&2\mathrm{e}^{-t}\\0&\mathrm{e}^t&-\mathrm{e}^{-t}\\0&\mathrm{e}^t&\mathrm{e}^{-t}\end{bmatrix}\begin{bmatrix}C_1\\C_2\\C_3\end{bmatrix}.
$$

**Example 16.6.4** Solve $\begin{cases}x_1'=3x_1+5x_2,\\x_2'=-5x_1+3x_2.\end{cases}$ We have $\det(\lambda I-A)=(\lambda-3)^2+25$, with eigenvalues $3\pm5\mathrm{i}$. For $\lambda=3+5\mathrm{i}$, $(A-\lambda I)\boldsymbol{r}=\boldsymbol{0}$ reads $-5\mathrm{i}r_1+5r_2=0$; take $\boldsymbol{r}=(1,\mathrm{i})^{\mathsf T}=\boldsymbol{a}+\mathrm{i}\boldsymbol{b}$ with $\boldsymbol{a}=(1,0)^{\mathsf T}$ and $\boldsymbol{b}=(0,1)^{\mathsf T}$. The real and imaginary parts give

$$
\boldsymbol{x}=\mathrm{e}^{3t}\begin{bmatrix}\cos5t&\sin5t\\-\sin5t&\cos5t\end{bmatrix}\begin{bmatrix}C_1\\C_2\end{bmatrix}.
$$
The trajectories are spirals that rotate clockwise with angular velocity $5$ while moving away from the origin like $\mathrm{e}^{3t}$ (an unstable focus). The various phase portraits of planar systems with constant coefficients are shown in [2.1.11](/2.1.11#sec-11.9).

### 16.6.5. Converting Between Systems and Higher-Order Equations

An $n$th-order equation can be converted into a first-order system: for $y^{(n)}+a_1y^{(n-1)}+\cdots+a_ny=f$, let $x_1=y$, $x_2=y'$, …, $x_n=y^{(n-1)}$; then

$$
\boldsymbol{x}'=\begin{bmatrix}0&1&&\\&\ddots&\ddots&\\&&0&1\\-a_n&-a_{n-1}&\cdots&-a_1\end{bmatrix}\boldsymbol{x}+\begin{bmatrix}0\\ \vdots\\0\\f\end{bmatrix}.
$$
The coefficient matrix is a **companion matrix**, whose characteristic polynomial is exactly $\lambda^n+a_1\lambda^{n-1}+\cdots+a_n$ ([2.1.6](/2.1.6)), that is, the characteristic equation of Section 16.3; the $n$ solutions $y_1,\dots,y_n$ of the equation correspond to the solutions $(y_k,y_k',\dots,y_k^{(n-1)})^{\mathsf T}$ of the system, and the two Wronskians coincide. All results of Section 16.1 are therefore special cases of this section. Conversely, a system can be reduced by elimination to a single higher-order equation.

**Example 16.6.5** Solve $\begin{cases}x_1'=3x_1-x_2,\\x_2'=x_1+x_2.\end{cases}$ From the first equation $x_2=3x_1-x_1'$; substituting into the second gives $3x_1'-x_1''=x_1+3x_1-x_1'$, that is, $x_1''-4x_1'+4x_1=0$, so $x_1=\mathrm{e}^{2t}(C_1+C_2t)$. Then $x_2=3x_1-x_1'=\mathrm{e}^{2t}(C_1-C_2+C_2t)$. Here $A=\begin{bmatrix}3&-1\\1&1\end{bmatrix}$ has the double eigenvalue $2$ but only one eigenvector direction, so it is not diagonalizable, and $t\mathrm{e}^{2t}$ appears in the solution.

**Example 16.6.6** Solve $x'''-3x''+2x'=0$. Letting $y=x'$ and $z=x''$ gives the system $x'=y$, $y'=z$, $z'=-2y+3z$. The characteristic polynomial is $\lambda(\lambda^2-3\lambda+2)$, with eigenvalues $0,1,2$ and eigenvectors $(1,0,0)^{\mathsf T}$, $(1,1,1)^{\mathsf T}$, $(1,2,4)^{\mathsf T}$ (an eigenvector of a companion matrix for $\lambda$ is always $(1,\lambda,\lambda^2)^{\mathsf T}$). Taking the first component, $x=C_1+C_2\mathrm{e}^t+C_3\mathrm{e}^{2t}$, in agreement with the result obtained directly from the characteristic equation $\lambda^3-3\lambda^2+2\lambda=0$.

After the second-order equation (16.4) is converted into the system $x'=v$, $v'=-\omega^2x-2kv$, the differences among the three damping regimes can be seen in the $(x,v)$ phase plane: underdamped trajectories are spirals around the origin, while critically damped and overdamped trajectories enter the origin directly without winding around it.

![Phase-plane trajectories of the damped oscillator x'' + 2k x' + x = 0 written as the system x' = v, v' = -x - 2k v (initial values x = 1, v = 0 and others): underdamped, k = 0.15, spirals; critically damped, k = 1, and overdamped, k = 2.5, trajectories enter the origin along the eigenvector directions (dashed lines)](./plots/oscillator-phase-plane.py)

## Summary

| Equation | Structure or method | Key points |
|---|---|---|
| $n$th-order linear equation $L(y)=f$ | General solution = particular solution + linear combination of a fundamental set | The solution space has dimension $n$ (Theorem 16.1.4); $n$ solutions are independent $\Leftrightarrow$ $W$ is nonzero at one point (Theorem 16.1.3) |
| Second order, variable coefficients, $y_1$ known | Reduce the order with $y=C(x)y_1$ | $y_2=y_1\int y_1^{-2}\mathrm{e}^{-\int a_1\mathrm{d}x}\,\mathrm{d}x$ |
| Second order, variable coefficients, $y_1,y_2$ known | Variation of parameters (Algorithm 16.2.1) | $C_1'y_1+C_2'y_2=0$, $C_1'y_1'+C_2'y_2'=f$ |
| Constant coefficients, homogeneous, $P(\mathrm{D})y=0$ | Characteristic equation (Algorithm 16.3.1) | Root $\lambda$ of multiplicity $k$: $x^j\mathrm{e}^{\lambda x}$; for complex roots take real and imaginary parts |
| Constant coefficients, nonhomogeneous, $P(\mathrm{D})y=f$ | Undetermined coefficients (Algorithm 16.4.1) | Particular solution $x^kS_m\mathrm{e}^{\lambda x}$, $k$ the multiplicity of $\lambda$; complex exponentials for trigonometric terms |
| Same as above | Operator method | Successive reduction by factorization; $\frac{\mathrm{e}^{\lambda x}}{P(\lambda)}$; expand $\frac1{P(\mathrm{D})}$ for polynomial right-hand sides |
| Cauchy–Euler equation | $x=\mathrm{e}^t$ (Algorithm 16.4.2) | $x^ky^{(k)}=\mathrm{D}(\mathrm{D}-1)\cdots(\mathrm{D}-k+1)y$ |
| Vibration $x''+2kx'+\omega^2x=H\sin pt$ | Characteristic roots $-k\pm\sqrt{k^2-\omega^2}$ | Underdamped, critically damped, overdamped; resonance when $k=0$, $p=\omega$ |
| System $\boldsymbol{x}'=A(t)\boldsymbol{x}+\boldsymbol{f}$ | Fundamental matrix $\Phi$; variation of parameters (16.7) | $\boldsymbol{x}=\Phi\Phi^{-1}(t_0)\boldsymbol{x}_0$; $\det\Phi$ satisfies Liouville's formula |
| Constant-coefficient homogeneous system $\boldsymbol{x}'=A\boldsymbol{x}$ | Eigenvalues and eigenvectors (Algorithm 16.6.1) | Diagonalizable: $\mathrm{e}^{\lambda_kt}\boldsymbol{r}_k$; otherwise Jordan chains and $\mathrm{e}^{tA}$ ([2.1.11](/2.1.11)) |

The theory of linear equations corresponds point by point to linear algebra:

| Linear algebra | Linear differential equations |
|---|---|
| Linear map $A$, equation $A\boldsymbol{x}=\boldsymbol{b}$ | Differential operator $L$, equation $L(y)=f$ |
| Solution set = particular solution + $\mathcal{N}(A)$ | General solution = particular solution + $\ker L$ |
| $\dim\mathcal{N}(A)=n-\operatorname{rank}(A)$ | $\dim\ker L=n$ (the order) |
| Vectors linearly independent $\Leftrightarrow$ determinant nonzero | $n$ solutions linearly independent $\Leftrightarrow$ Wronskian nonzero |
| Eigenvalues and eigenvectors, $A\boldsymbol{r}=\lambda\boldsymbol{r}$ | Exponential solutions, $\mathrm{D}\mathrm{e}^{\lambda x}=\lambda\mathrm{e}^{\lambda x}$, $\boldsymbol{x}=\mathrm{e}^{\lambda t}\boldsymbol{r}$ |
| Jordan chains | $x^j\mathrm{e}^{\lambda x}$ for repeated roots and $\mathrm{e}^{\lambda t}(t\boldsymbol{p}_1+\boldsymbol{p}_2)$ |
