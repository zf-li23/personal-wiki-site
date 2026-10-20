---
title: Classes and Encapsulation
description: Function overloading and overload resolution, default arguments, nullptr; type deduction with auto and decltype; classes, data members and member functions; separating interface from implementation; public, private and access control; the this pointer; inline functions and macros; classes, naming conventions, property and class attributes in Python.
source_hash: 69b8c9caef65
---

[4.2.1](/4.2.1) explained why we need **encapsulation**; this chapter covers the mechanism C++ uses to achieve it: the class. A class is a user-defined type that combines data members and member functions and uses access control to separate the interface from the implementation. Before turning to classes, we first add a few language mechanisms that make functions and variables more flexible to write: function overloading lets operations that have "the same name and different meanings" share one name, which is also the basis of [operator overloading](/4.2.5) and constructor overloading later on; `auto` and `decltype` let the compiler deduce types. Finally we introduce the `this` pointer implicit in member functions and inline functions, and compare with Python classes, whose encapsulation relies on convention rather than on the compiler. How objects are created and destroyed is the topic of the [next chapter](/4.2.4).

## 3.1. Function Overloading and Default Arguments

### 3.1.1. Function Overloading

The same task often needs to accept inputs of different types: computing the sum of two `int`s and the sum of two `double`s, or writing a message to the screen, to a file or to the network. If every case needs a name of its own (`sum_int`, `sum_double`), users have to remember a pile of names even though conceptually they are the same thing.

**Definition 3.1.1 (Function Overloading)** Declaring in the same scope several functions with the same name but different parameter lists (in the number or types of parameters) is called **function overloading**. At a call, the compiler selects the most suitable one according to the types of the arguments; this process is called overload resolution.

```cpp
#include <iostream>
#include <string>

void print(int score)              { std::cout << "score = " << score << '\n'; }
void print(const std::string& msg) { std::cout << "message: " << msg << '\n'; }
void print(double x, int digits)   { std::cout.precision(digits); std::cout << x << '\n'; }

int main() {
    print(94);                     // print(int)
    print(std::string("Hello"));   // print(const std::string&)
    print(3.14159, 3);             // print(double, int): 3.14
}
```

Overloaded functions must differ in their parameter lists; differing only in return type does not constitute overloading. The reason is simple: at a call `f(3)` only the arguments are visible, and if `int f(int)` and `double f(int)` coexisted, the compiler would have no way to choose. Differing only in parameter names does not constitute overloading either.

Overload resolution compares each candidate function roughly in the following order of preference: an exact match (including trivial conversions such as array-to-pointer and adding `const`) beats a promotion (such as `char` or `short` to `int`, and `float` to `double`), a promotion beats other standard conversions (such as between `int` and `double`, and `double` to `float`), and a standard conversion beats a user-defined conversion ([4.2.6](/4.2.6)). If the best candidate is not unique, the call is ambiguous and compilation fails:

```cpp
void print(int x);
void print(float x);

print(1.0f);  // float: exact match -> print(float)
print(1);     // int: exact match -> print(int)
print(1.7);   // double: converting to int and to float are both standard conversions
              // -> error: call of overloaded 'print(double)' is ambiguous
```

If only `print(int)` existed, `print(1.7)` would convert 1.7 to `int`, that is, truncate toward zero to get 1, and `print(-3.9)` would give -3. This implicit **narrowing conversion** silently loses information, and the `-Wconversion` option warns about it.

### 3.1.2. The Null Pointer nullptr

Before C++11, the null pointer was written as `0` or the macro `NULL`. `NULL` is an integer constant (in GCC it is the special `__null`), which causes problems with overloading:

```cpp
void f(int);
void f(int* p);

f(0);        // calls f(int), although 0 was meant as a null pointer
f(NULL);     // f(int) or ambiguous, depending on the compiler; never f(int*)
f(nullptr);  // calls f(int*)
```

The type of `nullptr` is `std::nullptr_t`; it can be converted to any pointer type but not to an integer, so it always matches pointer parameters. In modern C++, always use `nullptr` for the null pointer.

### 3.1.3. Default Arguments

**Definition 3.1.2 (Default Argument)** A value specified for a parameter in a function declaration is called a **default argument**; if the corresponding argument is omitted in a call, the compiler fills in that value automatically.

```cpp
void print(const std::string& name, int score = 0, const std::string& msg = "pass");

print("Alice");             // print("Alice", 0, "pass")
print("Bob", 95);           // print("Bob", 95, "pass")
print("Carol", 59, "fail");
```

The rules: parameters with default values must be at the end of the parameter list, because at a call the arguments correspond to the parameters from left to right and only a number of trailing ones can be omitted; the default value is given in only one declaration, usually the one in the **header file**, and is not repeated in the definition in the implementation file. Combining default arguments with overloading may produce ambiguity:

```cpp
void fun(int a, int b = 1);
void fun(int a);

fun(1, 2);  // OK: only fun(int, int) accepts two arguments
fun(2);     // error: both candidates accept one argument
```

### 3.1.4. Python Comparison

Python does not support overloading by parameter type: a later function of the same name in the same scope overrides the earlier one. It satisfies the same needs with other mechanisms: default and keyword arguments, variadic parameters `*args` and `**kwargs`, type checks inside the function, and the standard library's `functools.singledispatch` (dispatching on the type of the first argument).

```python
from functools import singledispatch


@singledispatch
def describe(x) -> str:
    return f"object {x!r}"


@describe.register
def _(x: int) -> str:
    return f"int {x}"


@describe.register
def _(x: str) -> str:
    return f"str of length {len(x)}"


print(describe(42), describe("hello"), describe(3.5), sep="; ")
# int 42; str of length 5; object 3.5


def append_to(item, target=None):  # never write target=[]: the default is created once
    if target is None:
        target = []
    target.append(item)
    return target


print(append_to(1), append_to(2))  # [1] [2]
```

Python's default values are evaluated once, at function definition time, and shared by all calls; if the default is a mutable object such as a list, a modification made in one call persists into the next. The idiom is to use `None` as the default and create a new object inside the function body.

## 3.2. Type Deduction: auto and decltype

### 3.2.1. auto

When a variable is declared with `auto`, the compiler deduces its type from the initializing expression. Its main use is to avoid long and obvious type names, such as the iterator type of a container, `std::map<std::string, int>::const_iterator`.

```cpp
#include <iostream>
#include <map>
#include <string>
#include <type_traits>

auto sum(auto a, auto b) { return a + b; }  // C++20 abbreviated function template

int main() {
    int i = 1;
    const int& r = i;
    auto a = r;            // int: auto drops the reference and top-level const
    auto& b = r;           // const int&
    decltype(r) c = i;     // const int&: decltype keeps the declared type
    decltype((i)) d = i;   // int&: a parenthesized lvalue expression
    static_assert(std::is_same_v<decltype(a), int>);
    static_assert(std::is_same_v<decltype(b), const int&>);
    static_assert(std::is_same_v<decltype(c), const int&>);
    static_assert(std::is_same_v<decltype(d), int&>);
    auto s = "abc";        // const char*, not std::string
    static_assert(std::is_same_v<decltype(s), const char*>);

    std::map<std::string, int> freq{{"oop", 2}, {"cpp", 1}};
    for (const auto& [word, count] : freq)   // structured binding (C++17)
        std::cout << word << ": " << count << '\n';
    std::cout << sum(1, 2) << ' ' << sum(1, 2.5) << '\n';  // 3 3.5
    std::cout << a + b + c + d << ' ' << s << '\n';         // 4 abc
}
```

Key points about `auto`:

- An `auto` variable must be initialized, and its type is determined at compile time and does not change afterward; it is not "**dynamic typing**".
- Deduction drops references and top-level `const`: `auto a = r;` yields a copy. When a reference is wanted, write `auto&` or `const auto&`; this matters especially in range-based `for` loops: `for (auto x : v)` copies every element, `for (const auto& x : v)` reads without copying, and `for (auto& x : v)` can modify the elements.
- A string literal is deduced as `const char*`, not `std::string`; when `std::string` is needed, write `std::string s = "abc";` or use the literal suffix `"abc"s`.
- The return type of a function can be written `auto` and is deduced from the `return` statements (C++14).
- Since C++20, function parameters can also be written `auto`; such a function is an abbreviated function template ([4.2.9](/4.2.9)): `sum(1, 2)` and `sum(1, 2.5)` instantiate two different functions. Before C++20 a parameter could not be declared `auto`.

### 3.2.2. decltype

`decltype(e)` gives the type of the expression `e` without evaluating it. For a variable name it gives the declared type of that variable (keeping references and `const`); for a parenthesized lvalue expression `(i)` it gives the reference type `int&`. `decltype` is mainly used in generic code to express "the same type as some expression", for example in a trailing return type:

```cpp
template <typename T, typename U>
auto multiply(T x, U y) -> decltype(x * y) {  // C++11 style; since C++14 "auto" alone suffices
    return x * y;
}
```

`auto f(...) -> R` is the syntax of a trailing return type: the return type is written after the parameter list and can therefore refer to the parameters.

## 3.3. Classes and Objects

### 3.3.1. Defining a Class

**Definition 3.3.1 (Class)** A **class** is a user-defined type that combines the data describing an object's state with the functions that operate on that data. The data in a class are called **data members** (member variables), and the functions in a class are called **member functions**. A variable defined with a class is called an object, or instance, of that class.

Class = attributes (data) + services (functions). The following stack ([4.3.4](/4.3.4)) uses a `std::vector<int>` as internal storage and offers only stack operations to the outside:

```cpp
#include <iostream>
#include <stdexcept>
#include <vector>

class Stack {
public:
    void push(int x) { data_.push_back(x); }  // member function defined inside the class
    int pop();                                // declared here, defined below
    int top() const;
    bool empty() const { return data_.empty(); }
    std::size_t size() const { return data_.size(); }

private:
    std::vector<int> data_;  // data member: the representation is hidden
};

int Stack::pop() {  // "Stack::" says that pop is a member of Stack
    int x = top();
    data_.pop_back();
    return x;
}

int Stack::top() const {
    if (data_.empty()) throw std::out_of_range("top of empty stack");
    return data_.back();
}

int main() {
    Stack s;            // an object of type Stack
    s.push(1);
    s.push(2);
    s.push(3);
    std::cout << s.pop() << ' ' << s.top() << ' ' << s.size() << '\n';  // 3 2 2
    Stack* p = &s;
    p->push(4);         // through a pointer: "->"
    std::cout << p->top() << '\n';  // 4
}
```

We access a member of an object with "object name `.` member name", and through a pointer with "pointer `->` member name". A member function must be declared inside the class; its definition may be written inside or outside the class; when written outside, it must be qualified with `ClassName::` to say which class it belongs to. A `const` after the parameter list of a member function means the function does not modify the object; it is a const member function ([4.2.4](/4.2.4)).

Both `struct` and `class` can define a class; the only difference is the default access: members of a `struct` are `public` by default, and those of a `class` are `private` by default. By convention, `struct` is used for a type that merely packs several data together and has no **invariants** to maintain (such as `struct Point { double x, y; };`), and `class` is used when encapsulation is needed.

### 3.3.2. Separating Interface from Implementation

In a multi-file program ([4.2.2](/4.2.2)), the class definition (including the declarations of member functions) goes in a **header file** and the definitions of member functions go in an implementation file, generally one pair of files per class:

```cpp
// stack.h: the interface, included by every user of Stack
#pragma once
#include <cstddef>
#include <vector>

class Stack {
public:
    void push(int x);
    int pop();
    int top() const;
    bool empty() const;
    std::size_t size() const;

private:
    std::vector<int> data_;
};
```

```cpp
// stack.cpp: the implementation, compiled once
#include "stack.h"
#include <stdexcept>

void Stack::push(int x) { data_.push_back(x); }
int Stack::top() const {
    if (data_.empty()) throw std::out_of_range("top of empty stack");
    return data_.back();
}
// ... the other member functions
```

A user needs to read only the `public` part in the header to know what the class can do. However, a C++ header does not hide the implementation completely: the private data members are also written in the header, because the compiler needs to know the size of an object in order to create objects in the user's code. Modifying a private member still forces every source file that includes the header to be recompiled; for complete isolation we can use the Pimpl idiom (the header keeps only a pointer to an implementation class, [4.2.12](/4.2.12)).

## 3.4. Access Control

### 3.4.1. public and private

**Definition 3.4.1 (Access Control)** The mechanism that divides the members of a class into groups according to where they may be accessed is called **access control**. C++ has three access specifiers:

- `public`: public members, accessible by any code; they constitute the interface of the class;
- `private`: private members, accessible only by member functions and friends ([4.2.4](/4.2.4)) of the class; they are the implementation of the class;
- `protected`: protected members, which in addition to the class itself can be accessed by derived classes ([4.2.7](/4.2.7)).

```cpp
Stack s;
s.push(1);           // OK: push is public
s.data_.clear();     // error: 'std::vector<int> Stack::data_' is private within this context
```

Access control is checked per class, not per object: a member function can access the private members of other objects of the same class.

```cpp
class Stack {
public:
    bool same_as(const Stack& other) const { return data_ == other.data_; }  // OK
    // ...
private:
    std::vector<int> data_;
};
```

Access control is checked at compile time and incurs no run-time cost; what it prevents is accidental misuse, not malicious sabotage (forcibly overwriting an object's memory through a pointer is still possible). It is independent of overload resolution: the compiler first performs overload resolution to select a function, and then checks whether it can be accessed. Consequently, a private overload still takes part in the competition and may make a call from outside the class ambiguous, or, once selected, cause an error because access is denied.

### 3.4.2. Designing the Interface

Making data members `private` and accessing them through member functions is the basic practice of encapsulation. But this does not mean writing a `get`/`set` pair for every data member: that merely makes the data public by a detour, and the class cannot maintain any invariant. A good interface is designed around the operations users need, not around the internal data. Compare:

| Designed around data | Designed around operations |
|---|---|
| `set_balance(double)`, `get_balance()` | `deposit(double)`, `withdraw(double)`, `balance()` |
| Users check for themselves whether the balance suffices | The rule is written inside `withdraw`, only once |
| If the storage changes to an integer number of cents, every caller must change | The internal representation can be replaced freely |

A practical test: if every data member of a class can be assigned arbitrarily without breaking any rule, then the class may not need encapsulation at all, and a `struct` suffices.

## 3.5. The this Pointer

An important difference between member functions and ordinary functions is that a member function always acts on some object. When we call `s.push(1)`, how does `push` know that it is the `data_` of `s` that should be modified? The answer is that every non-static member function has an implicit parameter `this`, a pointer to the object on which the function was called. `s.push(1)` is roughly equivalent to `Stack::push(&s, 1)`, and `data_` in the function body is shorthand for `this->data_`. In a const member function, the type of `this` is `const Stack*`, so members cannot be modified through it.

Common occasions for using `this` explicitly: to distinguish a parameter from a member of the same name; to pass the current object as an argument to another function; and to return `*this` to support chained calls.

```cpp
#include <iostream>
#include <string>

class Message {
public:
    Message& append(const std::string& text) {
        this->text += text;  // this->text is the member, text is the parameter
        return *this;        // return the object itself to allow chaining
    }
    const std::string& str() const { return text; }

private:
    std::string text;
};

int main() {
    Message m;
    m.append("Hello").append(", ").append("OOP");
    std::cout << m.str() << '\n';  // Hello, OOP
}
```

Python writes this implicit parameter out: the first parameter of a method (conventionally named `self`) is the object on which it was called, and `a.f(x)` is equivalent to `A.f(a, x)`. C++23 also allows writing this parameter explicitly, called an explicit object parameter ("deducing this"): `void f(this Stack& self)`; it is mainly used to simplify template code.

## 3.6. Inline Functions

A function call has a fixed overhead: passing arguments, jumping, setting up a **stack frame**, and returning. For a one-line function such as `max` or `top()`, the call overhead may exceed the function body itself. Inlining is an optimization: the compiler expands the function body directly at the call site, eliminating the call and creating opportunities for further optimization.

**Definition 3.6.1 (Inline Function)** A function declared with `inline`, or defined inside a class definition, is called an **inline function**. An inline function may be defined once in each of several **translation units** (all the definitions must be identical), so its definition can be placed in a header file.

```cpp
inline int max(int a, int b) { return a > b ? a : b; }

class Stack {
public:
    bool empty() const { return data_.empty(); }  // defined in the class: implicitly inline
    // ...
};
```

A common misunderstanding about `inline` needs clarifying. Whether a call is actually expanded is entirely up to the compiler: it refuses to expand functions that are too large or recursive, and it also expands small functions not marked `inline` on its own initiative (especially under `-O2`). In modern C++ the real effect of the `inline` keyword is to relax the **one definition rule** ([4.2.2](/4.2.2)) and allow the definition to appear in a header file; and for the compiler to be able to expand a function, its definition must be visible at the call site. Therefore short, frequently called functions (such as simple accessors) are usually defined directly inside the class, and larger functions are defined in the implementation file. Overusing inlining copies the function body into every call site and bloats the code.

Inline functions are the type-safe replacement for parameterized **macros** ([4.2.2](/4.2.2)):

| | Macro `#define MAX(a, b) ((a) > (b) ? (a) : (b))` | Inline function `inline int max(int a, int b)` |
|---|---|---|
| Stage of processing | Preprocessing, text replacement | Compilation; a real function |
| Type checking | None | Yes |
| Argument evaluation | In `MAX(a++, b)`, `a++` may be evaluated twice | Each argument is evaluated exactly once |
| Scope and access control | None; cannot be a class member | Obeys scope, can be a member function, can access private members |
| Debugging | The debugger cannot see macros | Unoptimized, it can be stepped through like an ordinary function |

When generality over several types is needed, use a function template ([4.2.9](/4.2.9)) instead of the `MAX` macro; the standard library already provides `std::max`.

## 3.7. Python Comparison: Classes and Encapsulation

### 3.7.1. Defining Classes and Naming Conventions

Python's `class` statement also defines a new type, but the data attributes of an instance need not be declared in advance; assigning them in `__init__` creates them (for the role of `__init__` see [4.2.4](/4.2.4)). Python has no access specifiers, and encapsulation relies on naming conventions:

| Form | Meaning |
|---|---|
| `name` | Public attribute |
| `_name` | Internal by convention; outside code can access it but should not depend on it |
| `__name` | Name mangling: inside a class `A` it is rewritten to `_A__name`, mainly to avoid name clashes with attributes of subclasses; it is not truly private |
| `__name__` | A special name defined by the language (such as `__init__`, `__len__`, [4.2.5](/4.2.5)); do not invent your own |

The attitude of the Python community is "we are all consenting adults": a convention is enough to show intent, and the language does not stop users from deliberately circumventing it.

```cpp tab
#include <iostream>
#include <stdexcept>
#include <vector>

class Stack {
public:
    void push(int x) { items_.push_back(x); }
    int pop() {
        int x = top();
        items_.pop_back();
        return x;
    }
    int top() const {
        if (items_.empty()) throw std::out_of_range("top of empty stack");
        return items_.back();
    }
    std::size_t size() const { return items_.size(); }

private:
    std::vector<int> items_;  // private: enforced by the compiler
};

int main() {
    Stack s;
    for (int x : {1, 2, 3}) s.push(x);
    int popped = s.pop();
    std::cout << popped << ' ' << s.top() << ' ' << s.size() << '\n';  // 3 2 2
}
```

```python tab
class Stack:
    def __init__(self) -> None:
        self._items: list[int] = []  # internal by convention

    def push(self, x: int) -> None:
        self._items.append(x)

    def pop(self) -> int:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def top(self) -> int:
        if not self._items:
            raise IndexError("top of empty stack")
        return self._items[-1]

    def __len__(self) -> int:  # enables len(s)
        return len(self._items)


s = Stack()
for x in (1, 2, 3):
    s.push(x)
print(s.pop(), s.top(), len(s))  # 3 2 2
```

### 3.7.2. property

Java-style `get_x()`/`set_x()` is uncommon in Python. The idiom is to expose the attribute directly first; if reads and writes later need to compute or check something, use `@property` to turn it into a method, and the users' code `obj.x`, `obj.x = v` needs no change. C++ has no such mechanism, so in C++ data must be accessed through member functions from the start.

```cpp tab
#include <iostream>
#include <stdexcept>

class Temperature {
public:
    explicit Temperature(double celsius) { set_celsius(celsius); }
    double celsius() const { return celsius_; }
    void set_celsius(double value) {
        if (value < -273.15) throw std::invalid_argument("below absolute zero");
        celsius_ = value;
    }
    double fahrenheit() const { return celsius_ * 9 / 5 + 32; }  // computed

private:
    double celsius_;
};

int main() {
    Temperature t(25);
    t.set_celsius(100);
    std::cout << t.celsius() << ' ' << t.fahrenheit() << '\n';  // 100 212
    try {
        t.set_celsius(-300);
    } catch (const std::invalid_argument& e) {
        std::cout << "error: " << e.what() << '\n';  // error: below absolute zero
    }
}
```

```python tab
class Temperature:
    def __init__(self, celsius: float) -> None:
        self.celsius = celsius  # goes through the setter below

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:  # computed, read-only
        return self._celsius * 9 / 5 + 32


t = Temperature(25)
t.celsius = 100
print(t.celsius, t.fahrenheit)  # 100 212.0
try:
    t.celsius = -300
except ValueError as e:
    print("error:", e)          # error: below absolute zero
```

### 3.7.3. Class Attributes and Instance Attributes

Names assigned directly in the body of a `class` statement are class attributes, shared by the class and all its instances, corresponding to static data members in C++ ([4.2.4](/4.2.4)); names assigned through `self.x = ...` are instance attributes, with one copy per object. Reading `obj.x` looks in the instance first and then in the class; but assigning through an instance always creates or modifies an instance attribute, which then shadows a class attribute of the same name:

```python
class A:
    count = 0  # class attribute, shared


a1, a2 = A(), A()
A.count = 2
print(a1.count, a2.count)  # 2 2: both read the class attribute
a1.count = 3               # creates an instance attribute on a1 only
print(A.count, a1.count, a2.count)  # 2 3 2
print(vars(a1), vars(a2))  # {'count': 3} {}
```

A simple class that merely stores data can use the standard library's `dataclasses.dataclass` to generate `__init__`, `__repr__` and `__eq__` automatically, which corresponds to a `struct` in C++:

```python
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


p = Point(1.0, 2.0)
print(p, p == Point(1.0, 2.0))  # Point(x=1.0, y=2.0) True
```

## Summary

- Function overloading lets one name denote a group of functions with different parameters, selected by overload resolution in the order exact match, promotion, conversion; the return type plays no part in distinguishing them. Default arguments can only be at the end and are given only once, in the declaration. Use `nullptr` for the null pointer.
- `auto` deduces types at compile time, dropping references and top-level `const`; when a reference is wanted, write `auto&` or `const auto&`. Since C++20, parameters can also be written `auto`.
- Class = data members + member functions; `public` members constitute the interface and `private` members are the implementation; access control is checked per class and enforced at compile time. The interface should be designed around operations, not around data.
- A non-static member function acts on an object through the implicit `this` pointer; Python writes it explicitly as `self`.
- The real effect of `inline` is to allow a function to be defined in a header file, and whether it is expanded is up to the compiler; inline functions and templates replace function-like macros.
- Python replaces access control with naming conventions, and uses `@property` to add checks and computation without changing the interface.
