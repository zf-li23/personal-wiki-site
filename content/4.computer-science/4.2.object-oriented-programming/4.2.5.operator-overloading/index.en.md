---
title: Operator Overloading
description: Motivation and rules of operator overloading; choosing between member and non-member forms; implementing arithmetic, compound assignment and comparison operators with a fraction class; the C++20 three-way comparison <=> and defaulted comparisons; prefix and postfix increment; the subscript and function call operators; stream operators; special methods and NotImplemented in Python.
source_hash: 3cca4d7c20c8
---

Built-in types have a natural notation: `a + b`, `a < b`, `v[i]`, `std::cout << x`. If user-defined types could only be written as `add(a, b)`, `less(a, b)`, `at(v, i)`, they would sit awkwardly beside the built-in types: users would have to remember another set of names, and generic code ([4.2.9](/4.2.9)) could not treat the two kinds of types alike. Operator overloading lets the designer of a class define the meaning of operators for their own types, so that fractions, complex numbers, matrices, big integers, strings and iterators can be used like built-in types. This is a natural extension of **data abstraction** ([4.2.1](/4.2.1)): type = representation + operations, and operators are the most commonly used operations. This chapter first covers the rules of operator overloading and the choice between the member and non-member forms, then implements arithmetic, comparison and output operators with a fraction class, and then covers increment, subscript and function call, the operators whose forms are special. Type conversion operators and assignment operators are closely tied to **implicit conversions** and to copying objects respectively, and are covered in [4.2.6](/4.2.6). At the end we compare with Python's special methods.

## 5.1. Rules of Operator Overloading

### 5.1.1. Operator Functions

**Definition 5.1.1 (Operator Overloading)** Defining the meaning of an operator for a user-defined type is called **operator overloading**. The overload of an operator `@` is a function named `operator@`, and the compiler rewrites the expression `a @ b` into a call of that function: the member form `a.operator@(b)`, or the non-member form `operator@(a, b)`.

An operator function is just an ordinary function with a special name and a special way of being called. It therefore obeys the rules of **function overloading** ([4.2.3](/4.2.3)) and can be called directly with function-call syntax: `a + b` and `operator+(a, b)` are exactly equivalent.

### 5.1.2. What Can and Cannot Be Overloaded

Almost all operators can be overloaded:

| Category | Operators |
|---|---|
| Arithmetic | `+` `-` `*` `/` `%`, unary `+` `-` |
| Comparison | `==` `!=` `<` `>` `<=` `>=` `<=>` |
| Logical | `!` `&&` `\|\|` |
| Bitwise | `&` `\|` `^` `~` `<<` `>>` |
| Assignment | `=` `+=` `-=` `*=` `/=` `%=` `&=` `\|=` `^=` `<<=` `>>=` |
| Increment and decrement | `++` `--` (prefix and postfix) |
| Other | `()` function call, `[]` subscript, `->` member access, `,` comma, unary `*` and `&` |
| Memory | `new` `new[]` `delete` `delete[]` |

Those that cannot be overloaded are member access `.`, pointer-to-member access `.*`, scope resolution `::`, the conditional operator `?:`, and `sizeof`, `typeid`, `alignof` and the like. In addition:

- new operators cannot be created (such as `**`), and the precedence, associativity and number of operands of an operator cannot be changed;
- at least one operand must be of a user-defined type: the meaning of `int + int` cannot be changed;
- `=`, `[]`, `()` and `->` can be overloaded only as member functions (`=` must be a member so that the compiler can decide whether an assignment operator needs to be generated automatically, [4.2.6](/4.2.6));
- overloaded `&&` and `||` lose **short-circuit evaluation** and both operands are evaluated, so they and the comma operator are almost never overloaded.

The most important rule is not in the syntax: an overloaded operator should meet people's expectations of it. `+` should have no **side effects** and should satisfy the familiar algebraic properties; `==` should be an equivalence relation; `a += b` and `a = a + b` should give the same result. A counterintuitive overload (such as using `+` to mean deletion) makes the code harder to read than an ordinary function name would.

### 5.1.3. Member or Non-Member

The same operator can be written as a member function or a non-member function, but for the same operand types only one of the two may be chosen, otherwise calls are ambiguous. The basis for the choice:

| Operator | Recommended form | Reason |
|---|---|---|
| `=`, `[]`, `()`, `->` | Member | Required by the language |
| Compound assignment `+=` etc., `++`, `--` | Member | Modify the left operand and return a reference to it |
| Unary `-`, `!`, `~` | Member | Act only on the object itself |
| Symmetric binary operations `+`, `*`, `==`, `<` etc. | Non-member | Both operands can undergo implicit conversion |
| Stream operators `<<`, `>>` | Non-member (usually a **friend**) | The left operand is a stream, not our class |

Why should symmetric binary operations be written as non-members? Suppose the fraction class `Fraction` can be implicitly constructed from integers. If `operator*` is a member, `f * 2` compiles (`f.operator*(Fraction(2))`) but `2 * f` does not: the compiler will not convert the left operand `2` in order to call a member function. Written as a non-member `operator*(const Fraction&, const Fraction&)`, the two operands have equal status and both can be converted, so both `2 * f` and `f * 2` work, in keeping with the intuition of the commutativity of multiplication.

If a non-member operator needs access to private members, it can be declared a **friend** ([4.2.4](/4.2.4)); a better approach is to implement it with the public compound assignment operator, so that it needs no access to private members at all.

## 5.2. A Complete Example: A Fraction Class

The `Fraction` class below represents rational numbers and always keeps its internal form in lowest terms with a positive denominator (this is its invariant). It shows the standard way of writing arithmetic operators: compound assignments are written as member functions that modify `*this` and return a reference; symmetric binary operations are written as non-member functions and implemented with the compound assignments.

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

A few details:

- Return types. `+=` returns `Fraction&`, which, as with built-in types, allows `(a += b) += c` and also avoids copying. `+` returns a new object (by value), because the result is neither `a` nor `b`; it must never return a reference to a local variable ([4.2.6](/4.2.6)).
- Parameters. Parameters that are not modified are passed as `const Fraction&` to avoid copying. The first parameter of `operator+` deliberately uses **pass by value**: since a copy has to be made in order to modify it anyway, it is better to let the compiler copy when passing the argument, which can also make use of moves ([4.2.6](/4.2.6)).
- Unary and binary. Unary `-` is a member function without parameters (the operand is `*this`); binary `-` is a non-member function with two parameters.
- Implicit conversion. The **constructor** `Fraction(long num = 0, long den = 1)` is not declared `explicit`, so integers can be implicitly converted to fractions, which is what makes `2 * a` and `a + 1` work. For a type such as a fraction, of which "integers are a special case", this conversion is reasonable; for most classes a single-argument constructor should be `explicit` ([4.2.6](/4.2.6)).

## 5.3. Comparison Operators

### 5.3.1. Equality and Three-Way Comparison

Before C++20, making a class support all six comparison operators required writing six functions, and their consistency was guaranteed entirely by hand. C++20 introduced the *three-way comparison operator* `<=>`, popularly called the "spaceship operator": `a <=> b` compares once and gives one of the three results "less, equal, greater", and the type of the result states the nature of the comparison:

| Result type | Meaning | Examples |
|---|---|---|
| `std::strong_ordering` | Total order; equal values are interchangeable | Integers, fractions, strings |
| `std::weak_ordering` | Total order, but "equivalent" values are not necessarily identical | Case-insensitive string comparison |
| `std::partial_ordering` | Partial order; some values may be incomparable | Floating-point numbers (`NaN` is incomparable with every number) |

As soon as `==` and `<=>` are defined, the compiler rewrites `a != b` as `!(a == b)` and `a < b` as `(a <=> b) < 0`, and likewise for `a > b`, `a <= b` and `a >= b`, and it also considers swapping the order of the operands automatically. `Fraction` wrote only two functions and obtained all six comparison operators.

### 5.3.2. Defaulted Comparisons

If the meaning of the comparison is simply "compare the data members one after another", the compiler can generate it:

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

The defaulted `<=>` performs a **lexicographic order** comparison in the declaration order of the members: first compare `major`, and if equal compare `minor`, and so on, which is exactly the rule for comparing version numbers. The `==` of `Fraction` also uses the defaulted implementation: because the internal form is always in lowest terms, two fractions are equal if and only if their numerators and denominators are equal respectively. But its `<=>` cannot use the defaulted implementation: comparing member by member would conclude that $\frac{1}{2} < \frac{1}{3}$ (compare the numerators first, 1 equals 1; then the denominators, 2 is less than 3), so we compare by cross-multiplication ourselves.

## 5.4. Increment and Decrement

`++` and `--` each have a prefix form and a postfix form with different semantics: `++a` adds one first, and the value of the expression is the incremented object itself; `a++` also adds one, but the value of the expression is the old value before the increment. Both are named `operator++`, and C++ distinguishes them with an unused `int` parameter: the version with this dummy parameter is the postfix one.

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

The prefix version returns a reference; the postfix version must first save the old value and then return a copy of it, so it makes one more copy than the prefix version. This is why, for class types such as iterators, the idiom in C++ is `++it` rather than `it++`: when the old value is not needed, the prefix version is no slower and may be faster. The postfix version is implemented with the prefix version, which guarantees that the two behave consistently. They can also be written as non-member functions: `Counter& operator++(Counter&)` and `Counter operator++(Counter&, int)`.

## 5.5. Subscript and Function Call

### 5.5.1. The Subscript Operator

`operator[]` lets an object be accessed by subscript like an array. It is usually provided in pairs: the non-const version returns a reference, so that `obj[i] = value` can appear on the left of an assignment; the const version returns a const reference (or a value) for reading by const objects (the const overloading in [4.2.4](/4.2.4)). The subscript need not be an integer: the subscript of `std::map<std::string, int>` is a string.

Since C++23, `operator[]` can take several arguments, so a matrix can be written `m[i, j]`. Before that, the idiomatic approach was to overload the function call operator `m(i, j)`.

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

If `operator[]` returned a `double` by value, `m[0, 0] = 1` would assign to a temporary copy and would not compile. When returning a reference, we must ensure that the referenced element continues to exist while the caller uses it; here the element belongs to `data_` and is valid as long as the matrix object exists.

### 5.5.2. The Function Call Operator

An object that overloads `operator()` can be called like a function: `obj(args)` is equivalent to `obj.operator()(args)`. Compared with ordinary functions, such an object can carry state (the interval endpoints in the example below) and is therefore often passed to standard-library algorithms; such objects are called function objects, and [4.2.12](/4.2.12) discusses them and lambda expressions systematically.

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

Note the distinction between `InRange five_to_eight(5, 8);` (calling the constructor to create an object) and `five_to_eight(6)` (calling the `operator()` of an existing object).

## 5.6. Stream Operators

To let objects support `std::cout << obj` and `std::cin >> obj`, we need to overload `operator<<` and `operator>>`. Their left operand is a stream object, and `std::ostream` and `std::istream` are classes of the standard library to which we cannot add member functions, so they can only be written as non-member functions; when access to private members is needed they are declared friends.

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

Every reference in the signatures has a reason:

- The stream parameter and the return value are both references. A stream object cannot be copied (its copy constructor is deleted; a stream corresponds to an external device, and copying it makes no sense), and returning a reference to the same stream makes chained calls possible: `std::cout << a << b` is `operator<<(operator<<(std::cout, a), b)`.
- The object being output is passed by `const` reference: output does not modify the object, and copying is avoided; the object being input is passed by non-const reference because it will be modified.
- An input operator should leave the object unchanged when reading fails and leave the stream in a failed state (which `is >> x` sets automatically on failure), to be checked by the caller.

C++20's `std::format` and C++23's `std::print` use another mechanism: after specializing the `std::formatter` template for a type, we can write `std::format("{}", p)`. This will be introduced in [4.2.11](/4.2.11).

## 5.7. Python Comparison: Special Methods

### 5.7.1. Special Methods

Python's operators are likewise translated into method calls, and the names of these methods have two underscores before and after.

**Definition 5.7.1 (Special Method)** A method whose name has the form `__xxx__` and which the interpreter calls implicitly when executing an operator, a built-in function or a particular syntax is called a **special method** (popularly a magic method or dunder method). For example, `a + b` calls `a.__add__(b)` and `len(x)` calls `x.__len__()`.

| Syntax | Special method | Corresponding C++ |
|---|---|---|
| `a + b`, `a - b`, `a * b`, `a / b`, `a // b`, `a % b`, `a ** b` | `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__` | `operator+` etc. |
| `b + a` when `b` does not support it | `__radd__` etc. (reflected versions) | Non-member operators |
| `a += b` | `__iadd__` etc.; when not defined, falls back to `a = a + b` | `operator+=` |
| `-a`, `abs(a)` | `__neg__`, `__abs__` | Unary `operator-` |
| `a == b`, `a < b` etc. | `__eq__`, `__lt__`, `__le__`, `__gt__`, `__ge__`, `__ne__` | `operator==`, `operator<=>` |
| `hash(a)` | `__hash__` | Specialization of `std::hash` |
| `a[k]`, `a[k] = v`, `del a[k]` | `__getitem__`, `__setitem__`, `__delitem__` | `operator[]` |
| `a(...)` | `__call__` | `operator()` |
| `len(a)`, `bool(a)` | `__len__`, `__bool__` | `size()`, `explicit operator bool` |
| `str(a)`, `print(a)` / `repr(a)` | `__str__` / `__repr__` | `operator<<` |
| `for x in a` | `__iter__`, `__next__` | `begin()`, `end()` and iterators ([4.2.10](/4.2.10)) |
| `with a:` | `__enter__`, `__exit__` | Construction and destruction (**resource acquisition is initialization**, [4.2.4](/4.2.4)) |

### 5.7.2. NotImplemented and Reflected Operations

How does Python handle a case such as `2 * f`, where the left operand is of a built-in type? When evaluating `x * y`, the interpreter first calls `x.__mul__(y)`; if it returns the special value `NotImplemented` (meaning "I do not know how to operate with this type"), it then tries `y.__rmul__(x)`; only if neither supports it is a `TypeError` raised. A special method that meets an operand type it does not recognize should therefore return `NotImplemented` rather than raise an exception, which leaves the other operand a chance. This solves the same problem as "write symmetric operators as non-members" in C++. Here is the Python implementation corresponding to the C++ version of §5.2:

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

A few points where Python differs from C++:

- `__repr__` gives an unambiguous, developer-oriented representation (ideally one from which the object can be rebuilt), and `__str__` gives a user-oriented representation; when only `__repr__` is defined, `str()` uses it too.
- For a class that defines `__eq__`, Python automatically sets `__hash__` to `None`, making the objects unhashable (they cannot be put in a `set` or used as `dict` keys), unless a `__hash__` consistent with equality is defined at the same time: equal objects must have the same hash value. Only immutable objects should be hashable.
- `functools.total_ordering` supplies the remaining comparison methods from `__eq__` and one ordering method, with an effect similar to the rewrite rules for `<=>` in C++20.
- For the immutable `Fraction`, `a += b` falls back to `a = a + b`, making the name `a` refer to a new object; for a mutable object such as a list, `__iadd__` modifies the object in place. This distinction matters when several names refer to the same object ([4.2.6](/4.2.6)).

In practice, rational numbers can simply use the standard library's `fractions.Fraction`, and big integers and rational numbers in C++ can use libraries such as GMP. The value of implementing one ourselves lies in understanding the design considerations of operator overloading.

### 5.7.3. Subscript and Call

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

Python splits "reading a subscript" and "writing a subscript" into the two methods `__getitem__` and `__setitem__`, whereas C++ has a single `operator[]` that supports both reading and writing by returning a reference. `m[i, j]` has always been legal in Python: the subscript is the tuple `(i, j)`, and this is exactly how NumPy arrays implement multidimensional subscripts ([4.4.2](/4.4.2)).

## Summary

- Operator overloading gives operators a meaning for user-defined types, and `a @ b` is rewritten as a call of `operator@`; new operators cannot be created and precedence cannot be changed, and an overload should meet people's expectations of the operator.
- `=`, `[]`, `()` and `->` must be members; compound assignment, increment and unary operations are written as members returning references; symmetric binary operations are written as non-members and implemented with compound assignment, so that both operands can be implicitly converted.
- In C++20 it suffices to define `==` and `<=>`, and the compiler rewrites the other comparison operators; when comparing member by member one can write `= default`.
- Prefix `++` returns a reference and postfix `++(int)` returns a copy of the old value; `operator[]` returns a reference to support assignment and provides a const overload; since C++23 `operator[]` can take several subscripts.
- Stream operators are non-members (often friends), and both the stream parameter and the return value are references to support chaining.
- Python implements operators with special methods, which return `NotImplemented` for unsupported operands so that the interpreter tries the reflected version; defining `__eq__` calls for defining `__hash__` accordingly.
