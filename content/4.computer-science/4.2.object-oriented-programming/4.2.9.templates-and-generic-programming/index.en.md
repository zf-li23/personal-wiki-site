---
title: Templates and Generic Programming
description: Motivation for generic programming; function templates, class templates and instantiation, the compilation model of templates; non-type template parameters; full and partial specialization, if constexpr; C++20 concepts and constraints; static versus dynamic polymorphism; type hints and generic syntax in Python.
source_hash: a32e35085769
---

The **virtual functions** of Chapter 8 let one piece of code handle **objects** of many types, provided that these types all derive from the same **base class** and that we pay for an indirect call at run time. Often we need a different kind of generality. The same algorithm (finding a maximum, sorting, searching) or the same data structure (a stack, a dynamic array, a map) should work for any type that meets the requirements, including built-in types such as `int` and `double` that have no base class at all, and it should be as fast as a hand-written specialized version. C++ achieves this generality with templates. This chapter covers function templates, class templates, template specialization, and the C++20 concepts that constrain template parameters, and finally compares templates with virtual functions as two forms of polymorphism. The standard library of Chapter 10 is built on templates.

## 9.1. Generic Programming

A function that returns the larger of two numbers could be written separately for `int`, `double` and `std::string`; the bodies are identical and only the types differ. The traditional remedies all have drawbacks.

- The preprocessor macro `#define MAX(a, b) ((a) < (b) ? (b) : (a))` has no type checking, may evaluate an argument twice (`MAX(i++, j)`), and is hard to debug when it goes wrong.
- Representing "any object" by `void*` or a common base class (`qsort` in C, the containers of early Java) loses type information, requires casts, requires built-in types to be wrapped into objects first, and adds the overhead of indirect calls.

**Definition 9.1.1 (Generic Programming)** Writing algorithms and data structures in a form independent of concrete types, with types as parameters to be substituted at the point of use, while retaining type safety and efficiency comparable to specialized code, is called **generic programming**.

Generic programming is concerned with the minimal requirements an algorithm places on types: finding a maximum requires only that the type support `<`, sorting also requires that elements can be swapped, and searching requires only that elements can be compared for equality. When these requirements are distilled and the algorithm depends on nothing else, it can be used with as many types as possible.

## 9.2. Function Templates

### 9.2.1. Definition and Instantiation

**Definition 9.2.1 (Template)** A code skeleton that takes types or constants as parameters and is used to generate functions or classes is called a **template**. Substituting concrete template arguments for the template parameters, so that the compiler generates a concrete function or class, is called *instantiation* of the template.

```cpp
#include <format>
#include <iostream>
#include <string>

template <typename T>                 // T is a template type parameter
T myMax(T a, T b) {
    return a < b ? b : a;             // requires only operator<
}

int main() {
    std::cout << std::format("{}\n", myMax(3, 7));                  // T deduced as int
    std::cout << std::format("{}\n", myMax(2.5, 1.5));              // T deduced as double
    std::cout << std::format("{}\n", myMax<double>(3, 2.5));        // T given explicitly
    std::cout << std::format("{}\n", myMax(std::string("pear"), std::string("apple")));
    // myMax(3, 2.5);                                 // error: T is int or double?
}
```

`typename T` can also be written `class T` with the same meaning. For the call `myMax(3, 7)`, the compiler deduces `T = int` from the argument types (template argument deduction) and generates and compiles the function `int myMax(int, int)`; if a program uses several types, several functions are generated. Deduction requires the types deduced at all places to agree: `myMax(3, 2.5)` deduces the contradictory `int` and `double` and fails to compile, whereas after writing `myMax<double>` explicitly, the arguments are converted by the rules for ordinary functions.

C++20 allows writing a parameter type as `auto` as a shorthand for a function template: `auto twice(auto x) { return x + x; }` is equivalent to a template whose parameter is the type of `x`.

### 9.2.2. The Compilation Model of Templates

A template is not itself a function; code is generated only when it is instantiated. The compiler checks a template in two phases. At definition time it checks the parts that do not depend on the template parameters (syntax, names that do not depend on `T`). At instantiation time it substitutes the arguments and then checks the parts that depend on `T`, for example whether `a < b` is valid for that type. This has several practical consequences.

- The definition of a template is usually placed in a header file. Instantiation happens in the translation unit that uses the template, and the compiler must see the complete definition at that point. If the definition is placed in a separate `.cpp` file, other files see only the declaration; compilation succeeds, but at link time the definition of `myMax<int>` cannot be found ([4.2.2](/4.2.2)). Alternatives are to write an explicit instantiation `template int myMax<int>(int, int);` in the `.cpp` file for a predetermined set of types, or to use C++20 modules.
- Error messages appear at the point of instantiation. Calling `myMax` with a type that does not support `<` produces an error pointing at `a < b` inside the template, and with deep nesting the message is long and hard to read. The concepts of §9.5 were introduced to solve this problem.
- Code bloat and compilation time. One copy of the code is generated for each argument type, enlarging the executable; with many templates in header files, every translation unit must parse and instantiate them again, which slows compilation.

### 9.2.3. Non-Type Template Parameters

A template parameter can also be a compile-time constant, such as an integer, an enumeration or a pointer; since C++20 it can also be a floating-point number or a class type satisfying certain conditions. The standard-library `std::array<T, N>` takes the number of elements `N` as a parameter: the size is fixed at compile time, and the elements are stored directly inside the object, using no heap memory.

```cpp
#include <array>
#include <cstddef>
#include <format>
#include <iostream>

template <typename T, std::size_t N>
T sum(const std::array<T, N>& a) {    // N is deduced from the argument
    T s{};
    for (const T& x : a) s += x;
    return s;
}

int main() {
    std::array<int, 4> a{1, 2, 3, 4};
    std::array<double, 2> b{0.5, 0.25};
    std::cout << std::format("{} {}\n", sum(a), sum(b));
}
```

`std::array<int, 4>` and `std::array<int, 5>` are two distinct types and cannot be assigned to each other.

## 9.3. Class Templates

### 9.3.1. Defining a Class Template

A class template generates classes with types as parameters and is the standard way to write containers. Below is a stack, shown with the C++ and the Python 3.12 generic syntax side by side.

```cpp tab
#include <cstddef>
#include <format>
#include <iostream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

template <typename T>
class Stack {
public:
    void push(const T& x) { items_.push_back(x); }
    T pop();                                      // defined below
    const T& top() const { return items_.back(); }
    bool empty() const { return items_.empty(); }
    std::size_t size() const { return items_.size(); }
private:
    std::vector<T> items_;
};

template <typename T>                             // out-of-class member definition
T Stack<T>::pop() {
    if (items_.empty()) throw std::out_of_range("pop from empty stack");
    T x = std::move(items_.back());
    items_.pop_back();
    return x;
}

int main() {
    Stack<int> a;
    a.push(1);
    a.push(2);
    Stack<std::string> b;
    b.push("hello");
    int x = a.pop();
    std::cout << std::format("{} {} {}\n", x, a.size(), b.top());
}
```

```python tab
class Stack[T]:                                   # PEP 695 generic class (3.12+)
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, x: T) -> None:
        self._items.append(x)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def top(self) -> T:
        return self._items[-1]

    def __len__(self) -> int:
        return len(self._items)


a = Stack[int]()
a.push(1)
a.push(2)
b = Stack[str]()
b.push("hello")
x = a.pop()
print(x, len(a), b.top())
```

`Stack` is a template; `Stack<int>` is a type. Inside a class template, `Stack` can be used as shorthand for `Stack<T>`; when a member function is defined outside the class, the template header `template <typename T>` must be repeated and `Stack<T>::` written. Member functions of a class template are instantiated only when called, so even if some member function of `Stack<T>` requires `T` to support a certain operation, instantiating `Stack` with a type that lacks that operation is fine as long as the function is not called. Since C++17 the compiler can also deduce the arguments of a class template from the arguments of a constructor (CTAD, class template argument deduction); for example, `std::vector v{1, 2, 3};` deduces `std::vector<int>`.

### 9.3.2. Member Function Templates

A member function of a class (whether or not the class is a template) can itself be a template. A common use is to accept "any kind of" iterator or callable object.

```cpp
#include <format>
#include <iostream>
#include <list>
#include <vector>

template <typename T>
class Bag {
public:
    template <typename It>                 // a member template inside a class template
    void addAll(It first, It last) {
        for (; first != last; ++first) items_.push_back(*first);
    }
    std::size_t size() const { return items_.size(); }
private:
    std::vector<T> items_;
};

int main() {
    std::list<int> l{1, 2, 3};
    int raw[]{4, 5};
    Bag<double> bag;
    bag.addAll(l.begin(), l.end());        // It = std::list<int>::iterator
    bag.addAll(raw, raw + 2);              // It = int*
    std::cout << std::format("{}\n", bag.size());
}
```

Here `addAll` requires of `It` only that it support `!=`, `++` and `*`, which both the iterator of a list and an ordinary pointer satisfy. This is exactly the idea of the iterators of Chapter 10.

## 9.4. Template Specialization

### 9.4.1. Full Specialization

A generic template may be incorrect or not efficient enough for certain types; in that case a separate implementation can be provided for those types.

**Definition 9.4.1 (Template Specialization)** A definition given separately for particular template arguments of a template is called a **template specialization**. A specialization that specifies concrete arguments for all template parameters is called an explicit (full) specialization, and one that restricts only some of the parameters, or the form of the parameters, is called a partial specialization. When a template is used, the compiler selects the most specialized version that matches the arguments.

A full specialization begins with `template <>`. For function templates, full specializations do not take part in overload resolution and easily cause surprises, so one usually writes an ordinary overload instead. For example, when comparing C strings `const char*`, the generic `myMax` compares pointer addresses, so a separate `const char* myMax(const char*, const char*)` that compares contents with `std::strcmp` should be written. For class templates, specialization is a common technique. The standard-library `std::vector<bool>` is a specialization of `std::vector` for `bool` (strictly speaking, the allocator parameter is still a template parameter, so it is a partial specialization) that packs each element into one bit. As a result its elements are not real `bool` objects and `operator[]` returns a proxy object, a design often considered a mistake.

### 9.4.2. Partial Specialization

Partial specialization can be used only for class templates (and variable templates). In the following example, `TypeName` handles `int` and `double` by full specialization, and "a pointer to any type" and "a `vector` of any type" by partial specialization, producing the name of a type recursively.

```cpp
#include <format>
#include <iostream>
#include <string>
#include <vector>

template <typename T>                       // primary template
struct TypeName { static std::string get() { return "?"; } };

template <>                                 // explicit (full) specializations
struct TypeName<int> { static std::string get() { return "int"; } };
template <>
struct TypeName<double> { static std::string get() { return "double"; } };

template <typename T>                       // partial specialization: any pointer
struct TypeName<T*> {
    static std::string get() { return TypeName<T>::get() + "*"; }
};

template <typename T>                       // partial specialization: any vector
struct TypeName<std::vector<T>> {
    static std::string get() { return "vector<" + TypeName<T>::get() + ">"; }
};

int main() {
    std::cout << std::format("{}\n", TypeName<std::vector<int*>>::get());
    std::cout << std::format("{}\n", TypeName<double**>::get());
    std::cout << std::format("{}\n", TypeName<char>::get());
}
```

```text
vector<int*>
double**
?
```

A class template that computes a result from types at compile time in this way is called a *type trait*. The standard header `<type_traits>` provides many ready-made traits such as `std::is_pointer_v<T>`, `std::is_integral_v<T>` and `std::remove_const_t<T>`, which are implemented by specialization.

### 9.4.3. Compile-Time Branching

The C++17 `if constexpr` lets a function template choose a branch at compile time according to a condition; branches not chosen are not instantiated. In many situations that formerly required specialization, it is more direct to write.

```cpp
#include <format>
#include <iostream>
#include <string>
#include <type_traits>

template <typename T>
std::string describe(const T& x) {
    if constexpr (std::is_integral_v<T>)
        return std::format("integer {}", x);
    else if constexpr (std::is_floating_point_v<T>)
        return std::format("real {:.3f}", x);
    else
        return "something else";          // x need not be formattable here
}

int main() {
    struct Opaque {};
    std::cout << std::format("{}\n", describe(42));
    std::cout << std::format("{}\n", describe(3.14159));
    std::cout << std::format("{}\n", describe(Opaque{}));
}
```

## 9.5. Concepts

### 9.5.1. Constraining Template Parameters

Before C++20, a template's requirements on types were written only in documentation, and violations were reported inside the template. C++20 introduced concepts, which write the requirements into the declaration of the template.

**Definition 9.5.1 (Concept)** In C++20, a **concept** is a named compile-time predicate on template arguments: it evaluates at compile time to `true` or `false` for a given type (or constant), indicating whether the type satisfies a set of syntactic requirements. When a template parameter is constrained by a concept, an argument that does not satisfy the constraint is rejected at the call site, and the error message points directly at the constraint that failed.

The standard library defines commonly used concepts in `<concepts>`, `<iterator>` and `<ranges>`, such as `std::integral`, `std::floating_point`, `std::totally_ordered`, `std::copyable`, `std::invocable<F, Args...>` and `std::ranges::range`. There are several equivalent ways to write a constraint.

```cpp
#include <concepts>
#include <format>
#include <iostream>

template <std::totally_ordered T>                  // constrained template parameter
const T& myMax(const T& a, const T& b) { return a < b ? b : a; }

template <typename T>
    requires std::integral<T>                       // requires-clause
T gcd(T a, T b) { return b == 0 ? a : gcd(b, a % b); }

auto half(std::floating_point auto x) { return x / 2; }   // abbreviated form

int main() {
    std::cout << std::format("{} {} {}\n", myMax(3, 7), gcd(84, 36), half(5.0));
    // gcd(1.5, 2.5);   // error: constraint std::integral<double> not satisfied
}
```

### 9.5.2. Defining Concepts

A user-defined concept lists the operations a type should support in a `requires` expression; each item is only checked for whether it compiles, and is not executed.

```cpp
#include <concepts>
#include <format>
#include <iostream>

template <typename T>
concept HasArea = requires(const T& t) {
    { t.area() } -> std::convertible_to<double>;    // t.area() must yield a double
};

struct Square { double a; double area() const { return a * a; } };
struct Point { double x, y; };

void report(const HasArea auto& s) { std::cout << std::format("area {:.2f}\n", s.area()); }

void show(std::integral auto) { std::cout << "some integer\n"; }
void show(std::signed_integral auto) { std::cout << "a signed integer\n"; }

int main() {
    report(Square{2.0});
    // report(Point{0, 0});   // error: Point does not satisfy HasArea
    show(-1);                 // the more constrained overload wins
    show(1u);
}
```

```text
area 4.00
a signed integer
some integer
```

`std::signed_integral<T>` is defined in the standard library as `std::integral<T> && std::is_signed_v<T>`, which subsumes `std::integral<T>`; so when both `show` overloads are viable for `int`, the compiler chooses the more constrained one. Selecting overloads by constraints replaces the obscure code that used to be written with SFINAE and similar tricks.

Concepts follow the same idea as the Protocol of Python in Chapter 8: a type is described by "which operations it has", without requiring it to inherit from some base class. The difference is that concepts are checked at compile time, and constraints are a precondition of template instantiation.

## 9.6. Templates and Polymorphism

Templates are also a form of **polymorphism**: the same code acts on different types and produces different behavior according to the type (the parametric polymorphism of Chapter 8). Because the call target is determined at compile time, it is also called static polymorphism; virtual functions are dynamic polymorphism. The following program implements "print the area of any shape" in both ways.

```cpp
#include <concepts>
#include <format>
#include <iostream>
#include <memory>
#include <vector>

// dynamic polymorphism: an explicit base class, dispatch at run time
struct Shape {
    virtual ~Shape() = default;
    virtual double area() const = 0;
};
struct Square : Shape {
    explicit Square(double a) : a_(a) {}
    double area() const override { return a_ * a_; }
    double a_;
};
void reportDynamic(const Shape& s) { std::cout << std::format("{:.2f}\n", s.area()); }

// static polymorphism: any type with area(), resolved at compile time
template <typename T>
concept HasArea = requires(const T& t) { { t.area() } -> std::convertible_to<double>; };
struct Disk { double r; double area() const { return 3.14159 * r * r; } };   // no base class
void reportStatic(const HasArea auto& s) { std::cout << std::format("{:.2f}\n", s.area()); }

int main() {
    std::vector<std::unique_ptr<Shape>> shapes;      // heterogeneous container
    shapes.push_back(std::make_unique<Square>(2.0));
    for (const auto& s : shapes) reportDynamic(*s);
    reportStatic(Square(3.0));
    reportStatic(Disk{1.0});
}
```

| | Virtual functions (dynamic polymorphism) | Templates (static polymorphism) |
|---|---|---|
| Call target determined at | Run time | Compile time |
| Requirement on types | Inherit from a specified base class | Support the required operations (expressible with concepts) |
| Built-in and third-party types | Cannot be used directly | Can be used |
| Heterogeneous containers | Possible (`std::vector<std::unique_ptr<Shape>>`) | Not possible; each instantiation is a different type |
| Run-time overhead | Indirect call, hard to inline | None, can be inlined |
| Compilation and code size | Adding a derived class does not require recompiling callers | Definitions go in headers; code bloat, slow compilation |

The two are often combined. The standard-library `std::function` (Chapter 12) accepts any callable object through a template and uses virtual functions internally to unify the calling interface. This technique is called *type erasure*: only one fixed type is exposed externally, yet it can hold any object that meets the requirements.

## 9.7. Python Comparison

### 9.7.1. Dynamic Typing Is Generic

Python functions do not restrict parameter types to begin with: `def my_max(a, b): return b if a < b else a` works for every object that supports `<`, which is **duck typing** (Chapter 8). Python needs no templates to obtain generality; what it lacks is the ability to find type errors before running. Type hints provide this ability: the annotations themselves have almost no effect at run time, and are read and checked by static type checkers such as mypy and pyright.

### 9.7.2. Generic Functions and Generic Classes

Python 3.12 introduced a generic syntax close to C++ templates (PEP 695): type parameters are written in square brackets after the name of a function or class; `[T: Bound]` gives an upper bound, corresponding to a concept constraint in C++; `[T: (int, str)]` restricts `T` to one of the listed types; and the `type` statement defines generic type aliases. The `Stack[T]` of §9.3.1 is a generic class.

```python
from collections.abc import Sequence
from typing import Protocol, Self


class Comparable(Protocol):                       # plays the role of a C++ concept
    def __lt__(self, other: Self, /) -> bool: ...


def my_max[T: Comparable](a: T, b: T) -> T:       # T is bounded by Comparable
    return b if a < b else a


def first[T](xs: Sequence[T]) -> T:               # an unconstrained type parameter
    return xs[0]


type Pair[T] = tuple[T, T]                        # a generic type alias


def swap[T](p: Pair[T]) -> Pair[T]:
    return p[1], p[0]


print(my_max(3, 7), my_max("pear", "apple"), first([2.5, 1.5]), swap((1, 2)))
```

```text
7 pear 2.5 (2, 1)
```

The fundamental difference from C++ is that Python generics exist only at type-checking time: at run time `Stack[int]` and `Stack[str]` are the same class, no different code is generated, and hence there is no specialization. Special handling for certain types is done at run time with `isinstance`, or with `functools.singledispatch`, which dispatches to different functions by the type of the first argument.

## Summary

- Generic programming writes algorithms and data structures with types as parameters; C++ implements it with templates, and the compiler instantiates concrete code from the arguments.
- Template definitions generally go in header files; errors are checked at instantiation.
- Specialization provides a dedicated implementation for particular arguments: for function templates prefer overloading, while class templates allow full and partial specialization; `if constexpr` selects branches at compile time.
- C++20 concepts write the requirements on types into declarations, report errors early and clearly, and select overloads by the strength of constraints.
- Templates are static polymorphism, with zero run-time overhead but unable to go into heterogeneous containers; virtual functions are dynamic polymorphism; the two can be combined through type erasure.
- Python is generic by nature; the generic syntax of 3.12 and Protocol bounds serve only static type checking.
