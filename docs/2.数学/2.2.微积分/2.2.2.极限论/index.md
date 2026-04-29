**2.1 数列极限的概念和性质**

-   **数列极限的定义**：\( \{a_n\} \) 收敛于 \( A \)，即 \( \forall \varepsilon > 0, \exists N \in \mathbb{Z}^{+}, \forall n > N, |a_n - A| < \varepsilon \)。
-   **基本数列极限**：\( \lim_{n\to\infty} q^n = 0 \ (|q|<1) \)，\( \lim_{n\to\infty} a^{1/n} = 1 \ (a>0) \)，\( \lim_{n\to\infty} \sqrt[n]{n} = 1 \)，\( \lim_{n\to\infty} \frac{n}{a^n} = 0 \ (a>1) \)。
-   **数列极限的性质**：唯一性、有界性、保号性、保序性等。
-   **子列**：\( \lim_{n\to\infty} a_n = A \Leftrightarrow \) 所有子列收敛于 \( A \)。常用于判定极限不存在。
-   **无穷小量与无穷大量**：若 \( a_n \neq 0 \)，\( \{a_n\} \) 无穷大 \( \Leftrightarrow \{1/a_n\} \) 无穷小。

**2.2 数列极限的运算法则和存在的充分条件**

-   **运算法则**：四则运算、乘方、开方。
-   **夹逼原理**：若 \( a_n \leq b_n \leq c_n \) 且 \( a_n, c_n \to A \)，则 \( b_n \to A \)。
-   **单调收敛原理**：单调有界数列必有极限。重要极限：\( \lim_{n\to\infty} (1+\frac{1}{n})^n = e \)。
-   **柯西收敛准则**：\( \{a_n\} \) 收敛 \( \Leftrightarrow \forall \varepsilon > 0, \exists N, \forall n,m > N, |a_n - a_m| < \varepsilon \)。该准则基于实数完备性（区间套定理、列紧性定理）。

**2.3 函数极限的概念和性质**

-   **六种极限形式**：\( x \to x_0,\ x \to x_0^+,\ x \to x_0^-,\ x \to \infty,\ x \to +\infty,\ x \to -\infty \)。
-   **定义**：例如 \( \lim_{x\to x_0} f(x) = A \) 定义为 \( \forall \varepsilon > 0, \exists \delta > 0, 0 < |x-x_0| < \delta \Rightarrow |f(x)-A| < \varepsilon \)。
-   **性质**：唯一性、局部有界性、局部保号性。
-   **函数极限与数列极限的关系**：\( \lim_{x\to x_0} f(x) = A \Leftrightarrow \) 对任意以 \( x_0 \) 为极限的点列 \( \{x_n\} \)，有 \( f(x_n) \to A \)。

**2.4 函数极限运算法则和存在的充分条件**

-   **运算法则**：四则运算、复合运算。
-   **夹逼定理**：\( \lim_{x\to 0} \frac{\sin x}{x} = 1 \) 的重要证明。
-   **单调收敛原理**：单调有界函数在每一点的左右极限存在。
-   **复合运算**：\( \lim_{t\to t_0} g(t) = x_0, \lim_{x\to x_0} f(x) = A \)，满足一定条件时，\( \lim_{t\to t_0} f(g(t)) = A \)。

**2.5 无穷小量与阶的比较**

-   **无穷小量**：极限为零的量。有限个无穷小的和、积仍为无穷小；有界量与无穷小之积为无穷小；无穷小的倒数为无穷大。
-   **阶的比较**：
    -   等价无穷小：\( f(x) \sim g(x) \) 若 \( \lim \frac{f(x)}{g(x)} = 1 \)。
    -   常用等价无穷小 (\( x \to 0 \))：\( x \sim \sin x \sim \tan x \sim \arcsin x \sim \arctan x \sim \ln(1+x) \sim e^x - 1 \)；\( 1-\cos x \sim \frac{1}{2}x^2 \)；\( (1+x)^k - 1 \sim kx \)。

