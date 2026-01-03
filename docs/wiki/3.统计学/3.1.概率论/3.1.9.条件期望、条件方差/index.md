## 9.1 条件概率回顾

### 9.1.1 条件概率定义

- 事件条件概率：
  $$
  \mathbb{P}(A|B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}
  $$
  
- 随机变量条件概率：
  - 离散型：
  $$
    \mathbb{P}(X = x_i | A) = \frac{\mathbb{P}((X = x_i) \cap A)}{\mathbb{P}(A)}
  $$
  - 连续型：
    $$
    f_{X|A}(x) = \frac{f_X(x) \cdot I_A(x)}{\mathbb{P}(A)}
    $$
  
- 条件分布 $\mathbb{P}(X|Y)$：
  - 离散型：
  $$
  \mathbb{P}(X = x_i | Y = y_j) = \frac{\mathbb{P}(X = x_i, Y = y_j)}{\mathbb{P}(Y = y_j)}
  $$
  - 连续型：
    $$
    f_{X|Y}(x|y) = \frac{f_{X,Y}(x,y)}{f_Y(y)}
    $$

### 9.1.2 乘法法则

- 事件：
  $$
  \mathbb{P}(A \cap B) = \mathbb{P}(A|B)\mathbb{P}(B)
  $$
  
- 随机变量：
  - 离散：
  $$
  \mathbb{P}(X = x_i, Y = y_j) = \mathbb{P}(X = x_i | Y = y_j)\mathbb{P}(Y = y_j)
  $$
  - 连续：
    $$
    f_{X,Y}(x,y) = f_{X|Y}(x|y)f_Y(y)
    $$

### 9.1.3 全概率公式

- 事件：
  $$
  \mathbb{P}(B) = \sum_i \mathbb{P}(B|A_i)\mathbb{P}(A_i)
  $$
  
- 随机变量：
  - 离散：
  $$
  p_X(x) = \sum_i p_{X|A_i}(x)\mathbb{P}(A_i)
  $$
  - 连续：
    $$
    f_X(x) = \int f_{X|Y}(x|y)f_Y(y)dy
    $$

### 9.1.4 贝叶斯准则

- 事件：
  $$
  \mathbb{P}(A_i|B) = \frac{\mathbb{P}(A_i)\mathbb{P}(B|A_i)}{\sum_j \mathbb{P}(A_j)\mathbb{P}(B|A_j)}
  $$
  
- 随机变量：
  - 离散：
  $$
  P_{X|Y}(x|y) = \frac{P_X(x)P_{Y|X}(y|x)}{P_Y(y)}
  $$
  - 连续：
    $$
    f_{X|Y}(x|y) = \frac{f_X(x)f_{Y|X}(y|x)}{f_Y(y)}
    $$

## 9.2 条件期望 $E(X|A)$

### 9.2.1 定义

- 离散型：
  $$
  E(X|A) = \sum_i x_i \mathbb{P}(X = x_i | A)
  $$
  
- 连续型：
  $$
  E(X|A) = \int_{-\infty}^{\infty} x f_{X|A}(x) dx
  $$

### 9.2.2 由无条件期望计算 $E(X|A)$

- 定理：
  $$
  E(X|A) = \frac{E(X \cdot I_A)}{\mathbb{P}(A)}
  $$
  
- 例子：若 $X \sim \mathcal{E}(\lambda)$，则
  $$
  E(X|X > a) = a + \frac{1}{\lambda}
  $$

### 9.2.3 全期望定理

- 若 $A_1, \dots, A_n$ 是 $\Omega$ 的分割，则：
  $$
  E(X) = \sum_{i=1}^n \mathbb{P}(A_i)E(X|A_i)
  $$
  
- 例子：几何分布 $X \sim G(p)$，可得
  $$
  E(X) = \frac{1}{p}
  $$

## 9.3 条件期望 $E(X|Y)$

### 9.3.1 定义

- 离散型：
  $$
  E(X|Y = y) = \sum_i x_i \mathbb{P}(X = x_i | Y = y)
  $$
  
- 连续型：
  $$
  E(X|Y = y) = \int_{-\infty}^{\infty} x f_{X|Y}(x|y) dx
  $$
  
- 条件期望作为随机变量：
  $$
  E(X|Y) = m(Y)
  $$

### 9.3.2 重期望法则

- 定理：
  $$
  E[E(X|Y)] = E(X)
  $$

### 9.3.3 性质

1. 线性性：
   $$
   E(c + \sum c_i X_i | Y) = c + \sum c_i E(X_i|Y)
   $$
   
2. 独立性：
   $$
   E(g(X)|Y) = E(g(X)) \quad \text{若 } X \perp Y
   $$
   
3. 最佳预测性：
   $$
   E[(X - E(X|Y))h(Y)] = 0
   $$
   
4. 最小均方误差：
   $$
   E[(X - m(Y))^2] \leq E[(X - g(Y))^2]
   $$

## 9.4 条件方差

### 9.4.1 定义

- 条件方差：
  $$
  var(X|Y) = E[(X - E(X|Y))^2 | Y]
  $$

### 9.4.2 全方差法则

- 定理：
  $$
  var(X) = E[var(X|Y)] + var(E[X|Y])
  $$

## 小结

### 核心知识点

- 理解 $E(X|A)$ 和 $E(X|Y)$ 的定义与意义
- 掌握由无条件期望计算条件期望的方法
- 熟练运用全期望定理和全方差法则
- 理解 $E(X|Y)$ 是最佳预测

### 关键公式

- 条件期望：
  $$E(X|A) = \frac{E(XI_A)}{\mathbb{P}(A)}$$
  $$E(X) = \sum \mathbb{P}(A_i)E(X|A_i)$$
  $$E[E(X|Y)] = E(X)$$

- 条件方差：
  $$var(X|Y) = E[(X - E(X|Y))^2 | Y]$$
  $$var(X) = E[var(X|Y)] + var(E[X|Y])$$

### 应用技巧

- 计算 $E(X|Y)$ 时，先固定 $Y = y$，再将 $y$ 替换为 $Y$
- 利用对称性、换序求和/积分简化计算
- 在二次型中加减 $E(X|Y)$ 以构造零均值项
