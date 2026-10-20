---
title: 运算符重载
description: 运算符重载的动机与规则；成员与非成员形式的选择；以分数类为例实现算术、复合赋值与比较运算符；C++20 的三路比较 <=> 与默认比较；前缀与后缀自增；下标与函数调用运算符；流运算符；Python 的特殊方法与 NotImplemented。
---

内置类型有一套自然的写法：`a + b`、`a < b`、`v[i]`、`std::cout << x`。用户定义的类型如果只能写成 `add(a, b)`、`less(a, b)`、`at(v, i)`，就和内置类型格格不入：使用者要记住另一套名字，泛型代码（[4.2.9](/4.2.9)）也无法对两类类型一视同仁。运算符重载让类的设计者为自己的类型定义运算符的含义，使分数、复数、矩阵、大整数、字符串、迭代器用起来像内置类型一样。这是**数据抽象**（[4.2.1](/4.2.1)）的自然延伸：类型 = 表示 + 操作，运算符就是最常用的操作。本章先讲运算符重载的规则与成员、非成员两种形式的选择，再以分数类为例实现算术、比较和输出运算符，然后讲自增、下标、函数调用这几个形式特殊的运算符。类型转换运算符与赋值运算符分别和**隐式转换**、对象复制密切相关，放在 [4.2.6](/4.2.6) 讲。章末对照 Python 的特殊方法。

## 5.1. 运算符重载的规则

### 5.1.1. 运算符函数

**定义 5.1.1（运算符重载）** 为用户定义的类型定义运算符的含义，称为**运算符重载**。运算符 `@` 的重载是一个名为 `operator@` 的函数，表达式 `a @ b` 被编译器改写为对该函数的调用：成员形式 `a.operator@(b)`，或非成员形式 `operator@(a, b)`。

运算符函数就是普通的函数，只是名字特殊、调用方式特殊。因此它遵循**函数重载**的规则（[4.2.3](/4.2.3)），可以直接用函数调用的语法调用：`a + b` 与 `operator+(a, b)` 完全等价。

### 5.1.2. 可以与不可以

几乎所有运算符都可以重载：

| 类别 | 运算符 |
|---|---|
| 算术 | `+` `-` `*` `/` `%`，一元 `+` `-` |
| 比较 | `==` `!=` `<` `>` `<=` `>=` `<=>` |
| 逻辑 | `!` `&&` `\|\|` |
| 位运算 | `&` `\|` `^` `~` `<<` `>>` |
| 赋值 | `=` `+=` `-=` `*=` `/=` `%=` `&=` `\|=` `^=` `<<=` `>>=` |
| 自增自减 | `++` `--`（前缀与后缀） |
| 其他 | `()` 函数调用、`[]` 下标、`->` 成员访问、`,` 逗号、一元 `*` 与 `&` |
| 内存 | `new` `new[]` `delete` `delete[]` |

不能重载的有：成员访问 `.`、成员指针访问 `.*`、作用域解析 `::`、条件运算符 `?:`，以及 `sizeof`、`typeid`、`alignof` 等。此外：

- 不能创造新的运算符（如 `**`），也不能改变运算符的优先级、结合性和操作数个数；
- 至少有一个操作数是用户定义的类型：不能改变 `int + int` 的含义；
- `=`、`[]`、`()`、`->` 只能作为成员函数重载（`=` 必须是成员，这样编译器才能确定是否需要自动生成赋值运算符，[4.2.6](/4.2.6)）；
- 重载的 `&&`、`||` 失去**短路求值**的特性，两个操作数都会被求值，因此几乎从不重载它们和逗号运算符。

最重要的规则不在语法里：重载的运算符应当符合人们对它的预期。`+` 应当没有**副作用**、满足人们熟悉的代数性质；`==` 应当是等价关系；`a += b` 与 `a = a + b` 的结果应当相同。违反直觉的重载（比如用 `+` 表示删除）会让代码比用普通函数名更难读。

### 5.1.3. 成员还是非成员

同一个运算符可以写成成员函数，也可以写成非成员函数，但对同一组操作数类型只能二选一，否则调用二义。选择的依据：

| 运算符 | 推荐形式 | 原因 |
|---|---|---|
| `=`、`[]`、`()`、`->` | 成员 | 语言规定 |
| 复合赋值 `+=` 等、`++`、`--` | 成员 | 修改左操作数，返回它的引用 |
| 一元 `-`、`!`、`~` | 成员 | 只作用于对象自身 |
| 对称的二元运算 `+`、`*`、`==`、`<` 等 | 非成员 | 左右操作数都可以发生隐式转换 |
| 流运算符 `<<`、`>>` | 非成员（通常是**友元**） | 左操作数是流，不是我们的类 |

对称的二元运算为什么要写成非成员？假设分数类 `Fraction` 可以由整数隐式构造。若 `operator*` 是成员，`f * 2` 可以编译（`f.operator*(Fraction(2))`），而 `2 * f` 不行：编译器不会为了调用成员函数而转换左操作数 `2`。写成非成员 `operator*(const Fraction&, const Fraction&)` 后，两个操作数地位平等，都可以转换，`2 * f` 与 `f * 2` 都能工作，这符合乘法交换律的直觉。

非成员运算符如果需要访问私有成员，可以声明为**友元**（[4.2.4](/4.2.4)）；更好的做法是用公有的复合赋值运算符实现它，这样它根本不需要访问私有成员。

## 5.2. 一个完整的例子：分数类

下面的 `Fraction` 类表示有理数，内部始终保持既约形式、分母为正（这是它的不变式）。它展示了算术运算符的标准写法：复合赋值写成成员函数，修改 `*this` 并返回引用；对称的二元运算写成非成员函数，用复合赋值实现。

```cpp
#include <compare>
#include <iostream>
#include <numeric>
#include <stdexcept>

class Fraction {
public:
    Fraction(long num = 0, long den = 1) : num_(num), den_(den) {  // implicit from long: 2 * f works
        if (den_ == 0) throw std::invalid_argument("zero denominator");
        normalize();
    }
    long num() const { return num_; }
    long den() const { return den_; }

    // compound assignment: members that modify *this and return it by reference
    Fraction& operator+=(const Fraction& r) {
        num_ = num_ * r.den_ + r.num_ * den_;
        den_ *= r.den_;
        normalize();
        return *this;
    }
    Fraction& operator*=(const Fraction& r) {
        num_ *= r.num_;
        den_ *= r.den_;
        normalize();
        return *this;
    }
    Fraction operator-() const { return Fraction(-num_, den_); }  // unary minus

    // comparison (C++20): == and <=> generate all six relational operators
    friend bool operator==(const Fraction&, const Fraction&) = default;
    friend std::strong_ordering operator<=>(const Fraction& a, const Fraction& b) {
        return a.num_ * b.den_ <=> b.num_ * a.den_;  // denominators are positive
    }

    friend std::ostream& operator<<(std::ostream& os, const Fraction& f) {
        os << f.num_;
        if (f.den_ != 1) os << '/' << f.den_;
        return os;
    }

private:
    void normalize() {
        if (den_ < 0) { num_ = -num_; den_ = -den_; }
        long g = std::gcd(num_, den_);
        if (g > 1) { num_ /= g; den_ /= g; }
    }
    long num_, den_;  // invariant: den_ > 0 and gcd(num_, den_) == 1
};

// symmetric binary operators: non-members, implemented with the compound ones
Fraction operator+(Fraction a, const Fraction& b) { return a += b; }
Fraction operator*(Fraction a, const Fraction& b) { return a *= b; }
Fraction operator-(const Fraction& a, const Fraction& b) { return a + (-b); }

int main() {
    Fraction a(1, 2), b(1, 3);
    std::cout << a + b << ' ' << a - b << ' ' << a * b << '\n';  // 5/6 1/6 1/6
    std::cout << 2 * a << ' ' << a + 1 << '\n';                  // 1 3/2
    std::cout << (a > b) << ' ' << (a == Fraction(2, 4)) << '\n'; // 1 1
    a += b;
    std::cout << a << ' ' << -a << '\n';                         // 5/6 -5/6
}
```

几个细节：

- 返回类型。`+=` 返回 `Fraction&`，与内置类型一样允许 `(a += b) += c`，也避免复制。`+` 返回新的对象（按值），因为结果既不是 `a` 也不是 `b`；它绝不能返回局部变量的引用（[4.2.6](/4.2.6)）。
- 参数。不修改的参数用 `const Fraction&` 传递，避免复制。`operator+` 的第一个参数故意按**值传递**：反正要复制一份来修改，不如让编译器在传参时复制，这样还能利用移动（[4.2.6](/4.2.6)）。
- 一元与二元。一元 `-` 是没有参数的成员函数（操作数是 `*this`）；二元 `-` 是两个参数的非成员函数。
- 隐式转换。**构造函数** `Fraction(long num = 0, long den = 1)` 没有声明为 `explicit`，所以整数可以隐式转换为分数，`2 * a`、`a + 1` 才能工作。对分数这样"整数是它的特例"的类型，这种转换是合理的；对大多数类，单参数构造函数应当是 `explicit` 的（[4.2.6](/4.2.6)）。

## 5.3. 比较运算符

### 5.3.1. 相等与三路比较

C++20 之前，要让一个类支持全部六个比较运算符，需要写六个函数，而且它们之间的一致性全靠手工保证。C++20 引入了三路比较运算符（three-way comparison operator）`<=>`，俗称"太空船运算符"：`a <=> b` 一次比较给出"小于、等于、大于"三种结果之一，结果的类型说明了比较的性质：

| 结果类型 | 含义 | 例子 |
|---|---|---|
| `std::strong_ordering` | 全序，相等即可互换 | 整数、分数、字符串 |
| `std::weak_ordering` | 全序，但"等价"的值未必相同 | 不区分大小写的字符串比较 |
| `std::partial_ordering` | 偏序，可能有不可比较的值 | 浮点数（`NaN` 与任何数都不可比较） |

只要定义了 `==` 和 `<=>`，编译器就会把 `a != b` 改写为 `!(a == b)`，把 `a < b` 改写为 `(a <=> b) < 0`，`a > b`、`a <= b`、`a >= b` 同理，还会自动考虑交换操作数的顺序。`Fraction` 只写了两个函数，就得到了全部六个比较运算符。

### 5.3.2. 默认比较

如果比较的含义就是"依次比较各个数据成员"，可以让编译器生成：

```cpp
#include <compare>
#include <iostream>
#include <string>

struct Version {
    int major, minor, patch;
    auto operator<=>(const Version&) const = default;  // also declares a defaulted ==
};

struct Student {
    std::string name;
    int id;
    bool operator==(const Student&) const = default;   // memberwise equality
};

int main() {
    Version a{1, 4, 2}, b{1, 10, 0};
    std::cout << (a < b) << ' ' << (a == Version{1, 4, 2}) << '\n';  // 1 1
    std::cout << (Student{"Li", 1} != Student{"Li", 2}) << '\n';      // 1
}
```

默认的 `<=>` 按成员的声明顺序做**字典序**比较：先比较 `major`，相同再比较 `minor`，以此类推，这正是版本号的比较规则。`Fraction` 的 `==` 也用了默认实现：因为内部总是既约形式，两个分数相等当且仅当分子分母分别相等。但它的 `<=>` 不能用默认实现：按成员比较会认为 $\frac{1}{2} < \frac{1}{3}$（先比分子，1 等于 1；再比分母，2 小于 3），所以要交叉相乘自己比较。

## 5.4. 自增与自减

`++` 和 `--` 各有前缀和后缀两种形式，语义不同：`++a` 先加一，表达式的值是加一之后的对象本身；`a++` 也加一，但表达式的值是加一之前的旧值。两者的名字都是 `operator++`，C++ 用一个不使用的 `int` 参数区分：带这个哑参数的是后缀版本。

```cpp
#include <iostream>

class Counter {
public:
    explicit Counter(int v = 0) : value_(v) {}
    Counter& operator++() {      // prefix: ++c
        ++value_;
        return *this;            // the incremented object itself
    }
    Counter operator++(int) {    // postfix: c++ (the int parameter is only a tag)
        Counter old = *this;
        ++*this;                 // reuse the prefix version
        return old;              // a copy of the old value
    }
    int value() const { return value_; }

private:
    int value_;
};

int main() {
    Counter c(1);
    std::cout << (++c).value() << '\n';  // 2
    std::cout << (c++).value() << '\n';  // 2
    std::cout << c.value() << '\n';      // 3
    ++++c;                               // fine: prefix returns a reference
    std::cout << c.value() << '\n';      // 5
}
```

前缀版本返回引用；后缀版本必须先保存旧值、再返回它的拷贝，所以比前缀版本多一次复制。这就是为什么在 C++ 中对迭代器这样的类类型，惯用写法是 `++it` 而不是 `it++`：不需要旧值时，前缀版本不会更慢，可能更快。后缀版本用前缀版本实现，保证二者的行为一致。它们也可以写成非成员函数：`Counter& operator++(Counter&)` 与 `Counter operator++(Counter&, int)`。

## 5.5. 下标与函数调用

### 5.5.1. 下标运算符

`operator[]` 让对象可以像数组一样用下标访问。它通常成对提供：非常量版本返回引用，使 `obj[i] = value` 可以出现在赋值号左边；常量版本返回常量引用（或值），供常量对象读取（[4.2.4](/4.2.4) 中的 const 重载）。下标不必是整数：`std::map<std::string, int>` 的下标就是字符串。

C++23 起，`operator[]` 可以接受多个参数，于是矩阵可以写成 `m[i, j]`。在此之前，惯用的做法是重载函数调用运算符 `m(i, j)`。

```cpp
// compile with -std=c++23 (multidimensional operator[])
#include <cstddef>
#include <iostream>
#include <stdexcept>
#include <vector>

class Matrix {
public:
    Matrix(std::size_t rows, std::size_t cols) : rows_(rows), cols_(cols), data_(rows * cols) {}

    // C++23: operator[] may take several indices
    double& operator[](std::size_t i, std::size_t j) { return data_[i * cols_ + j]; }
    const double& operator[](std::size_t i, std::size_t j) const { return data_[i * cols_ + j]; }

    // before C++23 the usual choice was operator(), here with bounds checking
    double& operator()(std::size_t i, std::size_t j) {
        if (i >= rows_ || j >= cols_) throw std::out_of_range("Matrix index");
        return data_[i * cols_ + j];
    }

    std::size_t rows() const { return rows_; }
    std::size_t cols() const { return cols_; }

private:
    std::size_t rows_, cols_;
    std::vector<double> data_;  // row-major storage
};

double trace(const Matrix& m) {
    double t = 0;
    for (std::size_t i = 0; i < m.rows() && i < m.cols(); ++i) t += m[i, i];  // const version
    return t;
}

int main() {
    Matrix m(2, 2);
    m[0, 0] = 1;   // a reference is returned, so the call can be assigned to
    m(1, 1) = 4;
    std::cout << trace(m) << '\n';  // 5
    try {
        m(2, 0) = 7;
    } catch (const std::out_of_range& e) {
        std::cout << "error: " << e.what() << '\n';  // error: Matrix index
    }
}
```

如果 `operator[]` 按值返回 `double`，`m[0, 0] = 1` 就是在给一个临时的副本赋值，无法编译。返回引用时要保证被引用的元素在调用者使用期间一直存在；这里元素属于 `data_`，只要矩阵对象存在就有效。

### 5.5.2. 函数调用运算符

重载了 `operator()` 的对象可以像函数一样被调用：`obj(args)` 等价于 `obj.operator()(args)`。与普通函数相比，这样的对象可以携带状态（下例中的区间端点），因此常作为参数传给标准库算法，这样的对象称为函数对象，[4.2.12](/4.2.12) 将系统讨论它和 lambda 表达式。

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

class InRange {  // an object that can be called like a function
public:
    InRange(int lo, int hi) : lo_(lo), hi_(hi) {}
    bool operator()(int x) const { return lo_ <= x && x <= hi_; }

private:
    int lo_, hi_;
};

int main() {
    std::vector<int> v{3, 8, 1, 9, 5, 7};
    InRange five_to_eight(5, 8);
    std::cout << five_to_eight(6) << ' '
              << std::count_if(v.begin(), v.end(), five_to_eight) << '\n';  // 1 3
}
```

注意区分 `InRange five_to_eight(5, 8);`（调用构造函数，创建对象）与 `five_to_eight(6)`（调用已有对象的 `operator()`）。

## 5.6. 流运算符

让对象支持 `std::cout << obj` 和 `std::cin >> obj`，需要重载 `operator<<` 和 `operator>>`。它们的左操作数是流对象，而 `std::ostream`、`std::istream` 是标准库的类，我们不能给它们添加成员函数，所以只能写成非成员函数；需要访问私有成员时声明为友元。

```cpp
#include <iostream>
#include <sstream>

class Point {
public:
    Point(double x = 0, double y = 0) : x_(x), y_(y) {}
    friend std::ostream& operator<<(std::ostream& os, const Point& p) {
        return os << '(' << p.x_ << ", " << p.y_ << ')';
    }
    friend std::istream& operator>>(std::istream& is, Point& p) {
        double x, y;
        if (is >> x >> y) p = Point(x, y);  // modify p only if reading succeeded
        return is;
    }

private:
    double x_, y_;
};

int main() {
    std::istringstream in("1.5 2  3 4");
    Point p, q;
    in >> p >> q;                                   // operator>>(operator>>(in, p), q)
    std::cout << p << " and " << q << '\n';         // (1.5, 2) and (3, 4)
}
```

签名中的每个引用都有理由：

- 流参数和返回值都是引用。流对象不能复制（它的拷贝构造函数是被删除的，一个流对应一个外部设备，复制它没有意义），而返回同一个流的引用使链式调用成为可能：`std::cout << a << b` 就是 `operator<<(operator<<(std::cout, a), b)`。
- 输出的对象用 `const` 引用传递：输出不修改对象，也避免复制；输入的对象用非常量引用，因为要修改它。
- 输入运算符应当在读取失败时保持对象不变，并让流处于失败状态（`is >> x` 失败时会自动设置），由调用者检查。

C++20 的 `std::format` 和 C++23 的 `std::print` 使用另一套机制：为类型特化 `std::formatter` 模板后，就可以写 `std::format("{}", p)`。这将在 [4.2.11](/4.2.11) 中介绍。

## 5.7. Python 对照：特殊方法

### 5.7.1. 特殊方法

Python 的运算符同样被翻译成方法调用，这些方法的名字前后各有两个下划线。

**定义 5.7.1（特殊方法）** 名字形如 `__xxx__`、由解释器在执行运算符、内置函数或特定语法时隐式调用的方法，称为**特殊方法**（俗称魔术方法、dunder 方法）。例如 `a + b` 调用 `a.__add__(b)`，`len(x)` 调用 `x.__len__()`。

| 语法 | 特殊方法 | 对应的 C++ |
|---|---|---|
| `a + b`、`a - b`、`a * b`、`a / b`、`a // b`、`a % b`、`a ** b` | `__add__`、`__sub__`、`__mul__`、`__truediv__`、`__floordiv__`、`__mod__`、`__pow__` | `operator+` 等 |
| `b + a` 中 `b` 不支持时 | `__radd__` 等（反射版本） | 非成员运算符 |
| `a += b` | `__iadd__` 等，没有定义时退化为 `a = a + b` | `operator+=` |
| `-a`、`abs(a)` | `__neg__`、`__abs__` | 一元 `operator-` |
| `a == b`、`a < b` 等 | `__eq__`、`__lt__`、`__le__`、`__gt__`、`__ge__`、`__ne__` | `operator==`、`operator<=>` |
| `hash(a)` | `__hash__` | `std::hash` 的特化 |
| `a[k]`、`a[k] = v`、`del a[k]` | `__getitem__`、`__setitem__`、`__delitem__` | `operator[]` |
| `a(...)` | `__call__` | `operator()` |
| `len(a)`、`bool(a)` | `__len__`、`__bool__` | `size()`、`explicit operator bool` |
| `str(a)`、`print(a)` / `repr(a)` | `__str__` / `__repr__` | `operator<<` |
| `for x in a` | `__iter__`、`__next__` | `begin()`、`end()` 与迭代器（[4.2.10](/4.2.10)） |
| `with a:` | `__enter__`、`__exit__` | 构造与析构（**RAII**，[4.2.4](/4.2.4)） |

### 5.7.2. NotImplemented 与反射运算

Python 怎样处理 `2 * f` 这样左操作数是内置类型的情形？求值 `x * y` 时，解释器先调用 `x.__mul__(y)`；如果它返回特殊值 `NotImplemented`（表示"我不知道怎样与这种类型运算"），再尝试 `y.__rmul__(x)`；两者都不支持才抛出 `TypeError`。所以特殊方法遇到不认识的操作数类型时应当返回 `NotImplemented`，而不是抛出异常，这样才给另一个操作数留出机会。这与 C++ 中"对称运算符写成非成员"解决的是同一个问题。下面是与 §5.2 的 C++ 版本对应的 Python 实现：

```python
from __future__ import annotations

from functools import total_ordering
from math import gcd


@total_ordering  # derives <=, >, >= from __eq__ and __lt__
class Fraction:
    def __init__(self, num: int = 0, den: int = 1) -> None:
        if den == 0:
            raise ZeroDivisionError("zero denominator")
        if den < 0:
            num, den = -num, -den
        g = gcd(num, den)
        self._num, self._den = num // g, den // g

    @staticmethod
    def _coerce(x) -> Fraction | None:
        if isinstance(x, Fraction):
            return x
        if isinstance(x, int):
            return Fraction(x)
        return None

    def __add__(self, other):
        o = Fraction._coerce(other)
        if o is None:
            return NotImplemented  # let Python try other.__radd__
        return Fraction(self._num * o._den + o._num * self._den, self._den * o._den)

    __radd__ = __add__  # 1 + f calls f.__radd__(1)

    def __mul__(self, other):
        o = Fraction._coerce(other)
        if o is None:
            return NotImplemented
        return Fraction(self._num * o._num, self._den * o._den)

    __rmul__ = __mul__

    def __neg__(self) -> Fraction:
        return Fraction(-self._num, self._den)

    def __sub__(self, other):
        o = Fraction._coerce(other)
        return NotImplemented if o is None else self + (-o)

    def __eq__(self, other) -> bool:
        o = Fraction._coerce(other)
        return NotImplemented if o is None else (self._num, self._den) == (o._num, o._den)

    def __lt__(self, other) -> bool:
        o = Fraction._coerce(other)
        return NotImplemented if o is None else self._num * o._den < o._num * self._den

    def __hash__(self) -> int:  # equal objects must have equal hashes
        return hash((self._num, self._den))

    def __repr__(self) -> str:
        return f"Fraction({self._num}, {self._den})"

    def __str__(self) -> str:
        return str(self._num) if self._den == 1 else f"{self._num}/{self._den}"


a, b = Fraction(1, 2), Fraction(1, 3)
print(a + b, a - b, a * b)          # 5/6 1/6 1/6
print(2 * a, a + 1)                 # 1 3/2
print(a > b, a == Fraction(2, 4))   # True True
a += b                              # no __iadd__: falls back to a = a + b
print(a, -a, repr(a))               # 5/6 -5/6 Fraction(5, 6)
```

几点与 C++ 不同的地方：

- `__repr__` 给出无歧义的、面向开发者的表示（最好能用它重建对象），`__str__` 给出面向用户的表示；只定义 `__repr__` 时 `str()` 也会用它。
- 定义了 `__eq__` 的类，Python 会自动把 `__hash__` 设为 `None`，使对象不可哈希（不能放进 `set` 或作 `dict` 的键），除非同时定义一个与相等一致的 `__hash__`：相等的对象必须有相同的哈希值。只有不可变的对象才应该可哈希。
- `functools.total_ordering` 根据 `__eq__` 和一个排序方法补齐其余比较方法，作用类似 C++20 的 `<=>` 改写规则。
- `a += b` 对不可变的 `Fraction` 退化为 `a = a + b`，让名字 `a` 指向一个新对象；对列表这样的可变对象，`__iadd__` 原地修改对象。这一区别在多个名字指向同一对象时很重要（[4.2.6](/4.2.6)）。

实际使用中，有理数可以直接用标准库的 `fractions.Fraction`，C++ 中的大整数、有理数可以用 GMP 等库。自己实现一遍的价值在于理解运算符重载的设计考虑。

### 5.7.3. 下标与调用

```cpp tab
#include <iostream>
#include <map>
#include <string>

class Temperatures {
public:
    double& operator[](const std::string& day) { return by_day_[day]; }  // creates if missing
    double operator()(double celsius) const { return celsius * 9 / 5 + 32; }  // to Fahrenheit

private:
    std::map<std::string, double> by_day_;
};

int main() {
    Temperatures beijing;
    beijing["mon"] = -3;
    beijing["tue"] = -1;
    std::cout << beijing["mon"] << ' ' << beijing(beijing["tue"]) << '\n';  // -3 30.2
}
```

```python tab
class Temperatures:
    def __init__(self) -> None:
        self._by_day: dict[str, float] = {}

    def __getitem__(self, day: str) -> float:
        return self._by_day[day]  # KeyError if missing

    def __setitem__(self, day: str, value: float) -> None:
        self._by_day[day] = value

    def __call__(self, celsius: float) -> float:  # to Fahrenheit
        return celsius * 9 / 5 + 32


beijing = Temperatures()
beijing["mon"] = -3
beijing["tue"] = -1
print(beijing["mon"], beijing(beijing["tue"]))  # -3 30.2
```

Python 把"读下标"和"写下标"分成 `__getitem__` 与 `__setitem__` 两个方法，而 C++ 只有一个 `operator[]`，靠返回引用同时支持读和写。`m[i, j]` 在 Python 中一直是合法的：下标是元组 `(i, j)`，NumPy 的数组正是这样实现多维下标的（[4.4.2](/4.4.2)）。

## 小结

- 运算符重载为用户定义的类型赋予运算符含义，`a @ b` 被改写为 `operator@` 的调用；不能创造新运算符或改变优先级，重载应符合人们对运算符的预期。
- `=`、`[]`、`()`、`->` 必须是成员；复合赋值、自增和一元运算写成成员并返回引用；对称的二元运算写成非成员，用复合赋值实现，使两个操作数都能隐式转换。
- C++20 中只需定义 `==` 和 `<=>`，其余比较运算符由编译器改写得到；按成员比较时可以 `= default`。
- 前缀 `++` 返回引用，后缀 `++(int)` 返回旧值的拷贝；`operator[]` 返回引用以支持赋值，并提供 const 重载；C++23 起 `operator[]` 可接受多个下标。
- 流运算符是非成员（常为友元），流参数和返回值都是引用，以支持链式调用。
- Python 用特殊方法实现运算符，遇到不支持的操作数时返回 `NotImplemented`，让解释器尝试反射版本；定义 `__eq__` 时要相应地定义 `__hash__`。
