---
title: From Procedural to Object-Oriented Programming
description: Programming paradigms; procedural versus object-oriented programming; abstraction, data abstraction and encapsulation; an object's state, behavior and identity; what makes a good program; why we use C++ and Python; everything is an object in Python.
source_hash: b7fb7617a4f1
---

[4.1 Programming Fundamentals](/4.1) is concerned with "how to compute": break a problem into steps and write an algorithm with variables, branches, loops and functions. As programs grow, the difficulty shifts from algorithms to organization: hundreds or thousands of functions share a pile of data that any of them can modify, and a change anywhere may ripple through the whole program. Object-oriented programming is concerned with "how to see the problem": first abstract the things in the problem domain into objects, let each object maintain its own data and provide services, and then let the objects cooperate to accomplish the task. This chapter introduces the course. It presents the notion of a programming paradigm, compares the procedural and object-oriented ways of organizing a program, discusses abstraction and encapsulation, the two ideas that run through the whole course, and finally explains why we study them with C++ and Python. The following chapters unfold in turn: [4.2.2](/4.2.2) covers compiling and building multi-file programs, [4.2.3](/4.2.3)–[4.2.6](/4.2.6) cover the basic mechanisms of classes and objects, [4.2.7](/4.2.7)–[4.2.9](/4.2.9) cover inheritance, polymorphism and generic programming, [4.2.10](/4.2.10)–[4.2.12](/4.2.12) cover the standard library, [4.2.13](/4.2.13) covers design patterns, and [4.2.14](/4.2.14) discusses AI-assisted programming.

## 1.1. Programming Paradigms

### 1.1.1. What Is a Programming Paradigm

The same problem can be organized into a program in very different ways. Take counting how often each word occurs in a text. We can write a loop that reads words one by one, looks each up in a table and adds one; we can regard the text as a sequence of words and write the whole computation in one step as a composition of operations such as "group, then count"; or we can design a "word-frequency table" object that accepts words and answers queries. Behind these three styles are three different mental models.

**Definition 1.1.1 (Programming Paradigm)** The basic style and mental model for organizing computation and data in programming is called a **programming paradigm**. It determines what the basic units of a program are and how the units are combined and communicate.

Common paradigms are listed in the table below. They are not mutually exclusive: most modern mainstream languages are multi-paradigm, and C++ and Python both support procedural and object-oriented programming and, to some extent, functional programming.

| Paradigm | Basic unit | Core idea | Typical languages or settings |
|---|---|---|---|
| Procedural | Procedure (function) | Decompose a task into a sequence of steps, top-down and by stepwise refinement | C, Fortran; the function part of C++ and Python |
| Object-oriented | Object (class) | Bundle data and operations together; objects cooperate with each other | C++, Java, C#, Python |
| Functional | Function (without **side effects**) | Describe computation by composing and transforming functions, avoiding mutable state | Haskell, OCaml; lambdas and ranges in C++, comprehensions in Python |
| Logic | Facts and rules | Describe "what is true" and let an inference engine solve it | Prolog, Datalog |
| Generic | Parameterized types and algorithms | Decouple algorithms from concrete types | C++ templates, Java generics |

Procedural and object-oriented programming are both imperative: a program is a sequence of commands that change state. Functional and logic programming are declarative: a program describes the properties the result should satisfy without prescribing the steps.

### 1.1.2. Procedural versus Object-Oriented

**Definition 1.1.2** Programming that takes procedures (functions) as the basic unit and organizes a program as a set of functions that process data is called **procedural programming**. Programming that takes objects as the basic unit, in which each object bundles data together with the functions that operate on that data and the program accomplishes its task through calls among objects, is called **object-oriented programming**.

The two differ first of all in the relation between data and operations. In a procedural program, data is passive: a structure is merely a container for data, and any function can read and write it. In an object-oriented program, data is active: an object decides for itself what the outside world may do to it, and the outside can only "request" a service from the object (by calling its member functions) rather than modify its interior directly.

| | Procedural | Object-oriented |
|---|---|---|
| Starting point of thinking | What steps are needed to solve the problem | What things are in the problem and what each is responsible for |
| Program structure | Hierarchy of function calls (top-down decomposition) | Objects and their collaborations |
| Data and operations | Separated: data structures plus functions that operate on them | Combined: class = data + operations |
| Effect of a change | If a data structure changes, every function that uses it must be checked | As long as the interface is unchanged, the implementation can change freely |
| Good at | Algorithms, numerical computation, top-level business flow | Large systems and code that must evolve and be reused over a long time |
| Main concern | Computational efficiency: "how to compute" | Developer productivity: "how to see the problem" |

Object orientation does not negate procedural programming: inside each member function of an object there is still a procedure made of sequences, branches and loops; what object orientation changes is the organization above the procedures. The content of this course can be viewed as a staircase in which each step achieves reuse at a higher level:

| Step | What is reused | Chapter |
|---|---|---|
| Procedural C/C++ | Concrete operations (functions) | [4.1](/4.1) |
| Classes and objects | Combinations of data and operations | [4.2.3](/4.2.3)–[4.2.6](/4.2.6) |
| Composition and inheritance | Existing classes | [4.2.7](/4.2.7) |
| Virtual functions and polymorphism | Different implementations behind a uniform interface | [4.2.8](/4.2.8) |
| Templates and generic programming | Type-independent source code | [4.2.9](/4.2.9)–[4.2.12](/4.2.12) |
| Design patterns | Solutions to a class of design problems | [4.2.13](/4.2.13) |

## 1.2. Abstraction

### 1.2.1. The Meaning of Abstraction

People think in language. Mathematics expresses ideas with symbolic systems and logical argument, natural language with vocabulary, grammar and pragmatics, and a programming language offers a third means of expression. A basic belief of the object-oriented method is that the general-purpose ways of thinking that humans have developed in understanding the world should also apply in software development: the structure of a program should be as close as possible to the way people describe a problem, rather than forcing people to think the way a machine does. The most fundamental of these ways of thinking is abstraction.

**Definition 1.2.1 (Abstraction)** The thought process of discarding the individual, nonessential features of many things and extracting their common, essential features is called **abstraction**.

What counts as "essential" depends on the problem to be solved. Consider defining "bird". If we extract "can fly, has wings, has two legs", ostriches and penguins are not birds; the biological definition extracts features such as "warm-blooded, egg-laying, covered with feathers, forelimbs specialized as wings". For a flight-booking system, a "passenger" needs only a name, an ID number and contact information, and height and weight are nonessential; for a medical system the opposite holds. Abstraction is always relative to a purpose: a good abstraction makes details irrelevant to the purpose disappear and makes the relevant properties plain at a glance.

### 1.2.2. Procedural Abstraction and Data Abstraction

**Definition 1.2.2** For any sequence of operations that accomplishes a definite function, its user may care only about what it does and not how it does it, treating it as a whole; this is called **procedural abstraction**. Defining a **data type** by the operations applied to data, and stipulating that the values of the data can be modified and observed only through these operations, is called **data abstraction**.

Procedural abstraction is just the function: whoever calls `std::sort(v.begin(), v.end())` does not need to know which sorting algorithm it uses. Data abstraction understands "data" as "values plus permitted operations". Mathematicians have long viewed data this way: the set of integers $\mathbb{Z}$ together with addition and multiplication forms a ring, rather than being just a heap of numbers. Types in programming languages work the same way:

| Expression | C++ | Python | Remark |
|---|---|---|---|
| `3 / 4` | `0` | `0.75` | Integer division in C++ yields an integer (truncating toward zero); `/` in Python is always true division |
| `3 // 4` | Not an expression (`//` starts a comment) | `0` | Floor division in Python (rounding down) |
| `3.2 / 4.0` | `0.8` | `0.8` | Floating-point division |
| `'a' * 3` | `291` (`char` is first promoted to `int`; the code of `'a'` is 97) | `'aaa'` (string repetition) | The same notation means different things for different types |

We can therefore say: type = storage and representation of data + the operations the data supports. The operations of built-in types are fixed by the language; object-oriented programming lets programmers define new types in the same way, and this is the [class](/4.2.3).

## 1.3. Objects and Encapsulation

### 1.3.1. Objects

**Definition 1.3.1 (Object)** An **object** is an abstract description of a thing in the real world. It may be a tangible entity (a book, a student) or an intangible concept (a loan, a course). An object has:

- state (static features): attributes that can be described by data, such as title, author and whether the book is checked out;
- behavior (dynamic features): the services the object can provide, such as lending, returning and querying;
- identity: the status that distinguishes it from other objects; even if two books have exactly the same attributes, they are two objects.

An object is a combination of attributes and services. A group of objects with the same attributes and services is described by one class, and an object is an instance of its class ([4.2.3](/4.2.3)).

### 1.3.2. Encapsulation and Information Hiding

**Definition 1.3.2 (Encapsulation)** Combining data and the functions that operate on it into a whole, hiding the internal implementation details from the outside and interacting with the outside only through a specified interface, is called **encapsulation**. The aspect of "hiding implementation details from the outside" is called **information hiding**.

Encapsulation brings two benefits. First, an object can maintain its own invariants (*invariant*), that is, conditions that hold throughout the lifetime of the object: for example, an account balance is never negative, and the denominator of a fraction is always positive. As long as all modifications go through the object's own member functions, the check needs to be written in only one place. Second, the implementation can evolve independently: users depend only on the interface, and the author of the class can replace the internal data structure without affecting any caller.

Let us compare two ways of writing a bank account. In the procedural version, the account is a structure that only holds data, and any code can modify the balance directly:

```cpp tab
#include <iostream>

struct Account {
    double balance;
};

bool withdraw(Account& acc, double amount) {
    if (amount <= 0 || amount > acc.balance) return false;
    acc.balance -= amount;
    return true;
}

int main() {
    Account acc{100.0};
    withdraw(acc, 30.0);
    acc.balance = -1e9;  // nothing prevents breaking the rule "balance >= 0"
    std::cout << acc.balance << '\n';
}
```

```python tab
from dataclasses import dataclass


@dataclass
class Account:
    balance: float


def withdraw(acc: Account, amount: float) -> bool:
    if amount <= 0 or amount > acc.balance:
        return False
    acc.balance -= amount
    return True


acc = Account(100.0)
withdraw(acc, 30.0)
acc.balance = -1e9  # nothing prevents breaking the rule "balance >= 0"
print(acc.balance)
```

In the object-oriented version, the balance is private and can be modified only through `deposit` and `withdraw`, so the rule "the balance is nonnegative" is guaranteed by the class itself:

```cpp tab
#include <iostream>
#include <stdexcept>

class Account {
public:
    explicit Account(double initial) : balance_(initial) {
        if (initial < 0) throw std::invalid_argument("negative balance");
    }
    void deposit(double amount) {
        if (amount <= 0) throw std::invalid_argument("non-positive deposit");
        balance_ += amount;
    }
    bool withdraw(double amount) {
        if (amount <= 0 || amount > balance_) return false;
        balance_ -= amount;
        return true;
    }
    double balance() const { return balance_; }

private:
    double balance_;  // invariant: balance_ >= 0
};

int main() {
    Account acc(100.0);
    acc.withdraw(30.0);
    // acc.balance_ = -1e9;  // compile error: balance_ is private
    std::cout << acc.balance() << '\n';  // 70
}
```

```python tab
class Account:
    def __init__(self, initial: float) -> None:
        if initial < 0:
            raise ValueError("negative balance")
        self._balance = initial  # invariant: _balance >= 0

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("non-positive deposit")
        self._balance += amount

    def withdraw(self, amount: float) -> bool:
        if amount <= 0 or amount > self._balance:
            return False
        self._balance -= amount
        return True

    @property
    def balance(self) -> float:
        return self._balance


acc = Account(100.0)
acc.withdraw(30.0)
print(acc.balance)  # 70.0
```

In C++, `private` is enforced by the compiler; Python has no truly private members, and the leading underscore in `_balance` is only a convention meaning "for internal use", while `@property` lets `balance` be read like an attribute but not assigned directly ([4.2.3](/4.2.3)). What the two languages have in common is that the interface (`deposit`, `withdraw`, `balance`) is separated from the implementation (a floating-point number, which could later be replaced by an integer number of cents).

### 1.3.3. The Three Basic Features of Object Orientation

| Feature | Meaning | Where in this course |
|---|---|---|
| Encapsulation | Combine data with operations and hide the implementation | [4.2.3](/4.2.3)–[4.2.6](/4.2.6) |
| Inheritance | Define a new class on the basis of an existing one, reusing and extending its attributes and behavior | [4.2.7](/4.2.7) |
| Polymorphism | The same interface behaves differently on different objects | [4.2.8](/4.2.8), [4.2.9](/4.2.9) |

Note that "object-oriented" does not mean "stuffing all code into classes". A class with only static functions, or a class that exposes all its data members and offers a pile of `get`/`set` functions, gains none of the benefits of encapsulation. To judge whether a design is object-oriented, ask whether responsibilities are assigned to the objects that hold the relevant data, and whether the interface is stable while the implementation is hidden.

## 1.4. Criteria for a Good Program

The goal of this course is to write better software. There are three classical criteria:

- Simplicity: the program is short and easy to manage. Each function and class does one thing; the longer and more complex the code, the harder it is to maintain and debug.
- Clarity: easy to understand, both for people and for machines. For people, naming, structure and comments let readers see the intent of the code at a glance; for machines, the program should not depend on undefined or unspecified behavior.
- Generality: it works correctly in a wide range of situations and is easy to modify for new ones, including boundary cases and erroneous input.

"Clear to the machine" has a concrete meaning. The C++ standard specifies no result for certain constructs, for example modifying the same variable twice in one expression:

```cpp
#include <iostream>

int main() {
    int i = 1;
    // int j = i++ + i++;  // undefined behavior: two unsequenced modifications of i
    int j = i + (i + 1);    // say what you mean instead
    i += 2;
    std::cout << i << ' ' << j << '\n';  // 3 3
}
```

The commented-out line has **undefined behavior**: the standard places no requirement on its result, different compilers and different optimization levels may give different results, and it may even corrupt other parts of the program. A clear program does not contain such code.

## 1.5. Why C++ and Python

### 1.5.1. C++

C++ was developed by Bjarne Stroustrup on the basis of the C language and is still the main language of systems software, game engines, databases, browsers, high-performance computing and the lower layers of deep-learning frameworks. There are several reasons to learn object orientation with it:

- *Zero-overhead abstraction*: abstraction mechanisms such as classes and templates add no extra cost when unused, and when used are no slower than equivalent hand-written code. Abstraction and efficiency can be had together.
- Deterministic object lifetime: when an object is created and when it is destroyed is determined exactly by the structure of the program, and destructors run at well-defined moments. This lets C++ manage memory, files, locks and every other resource with objects ([4.2.4](/4.2.4)), and also forces learners to truly understand the creation, copying and destruction of objects ([4.2.6](/4.2.6)).
- Closeness to the machine: memory and hardware can be manipulated directly, so we can see how each abstraction is implemented underneath (for example the virtual method table, [4.2.8](/4.2.8)).

The price is complexity: the language has many rules, there is no **garbage collection**, and resources must be managed by hand; out-of-bounds accesses, **dangling pointers** and similar errors lead to **undefined behavior**, which is also why the industry has recently stressed "memory safety" and partly turned to languages such as Rust for new projects. The direction of modern C++ is precisely to reduce such errors with safer abstractions: C++11 introduced move semantics, smart pointers, lambdas and `auto`; since then a new standard has appeared every three years, C++20 added concepts, ranges, modules and coroutines, C++23 added `std::print`, `std::expected` and more, and the C++26 draft has added static reflection and contracts. This course follows C++20/23 and advocates using standard-library containers and smart pointers and avoiding bare `new`/`delete`.

### 1.5.2. Python

Python takes a different road: **dynamic typing**, automatic memory management and concise syntax. Its object-oriented mechanisms are more flexible and more "relaxed": there is no enforced access control, attributes can be added to an object at run time, and whether an object can be used depends only on whether it provides the required methods, not on which class it belongs to. Learning the two languages side by side helps separate "the ideas of object orientation" from "the implementation details of a particular language".

| | C++ | Python |
|---|---|---|
| Type checking | Static (compile time) | Dynamic (run time); type annotations are checked only by tools |
| Variable | A block of memory holding a value | A name bound to an object |
| Assignment `b = a` | Copies the value ([4.2.6](/4.2.6)) | Makes `b` refer to the same object |
| Destruction of objects | Deterministic: on leaving scope or on `delete` | When the reference count drops to zero or when garbage-collected |
| Access control | `public`/`protected`/`private`, enforced by the compiler | Naming conventions (`_x`, `__x`) |
| Operator overloading | Member or non-member functions such as `operator+` | Special methods such as `__add__` |
| Polymorphism | Virtual functions, templates | Dynamic dispatch; every method can be overridden |

This course is "light on syntax, heavy on ideas": each concept is first presented with the problem it solves, and then implemented in C++ and in Python; mechanisms that belong to only one language (references, move semantics and RAII in C++; special methods and context managers in Python) are explained separately where they occur.

## 1.6. Everything Is an Object in Python

In Python, integers, strings, functions, classes and modules are all objects: every object has an identity (`id`), a type (`type`) and a value, and can be assigned to a variable, put into a container and passed as an argument. A class is itself an object, and its type is `type`.

```python
def greet(name: str) -> str:
    return f"hello, {name}"


print(type(42), (42).bit_length())  # <class 'int'> 6
print(type(greet), greet.__name__)  # <class 'function'> greet
print(type(int), type(type))        # <class 'type'> <class 'type'>

f = greet                  # a function is a value: bind another name to it
print(f("OOP"))            # hello, OOP
print(isinstance(3, object), isinstance(int, object))  # True True

a = [1, 2]
b = a                      # b names the same list object
print(a is b, id(a) == id(b))  # True True
```

The word "object" has a narrower meaning in C++: the standard defines an object as a region of storage with a type, a size and a lifetime. The `x` in `int x;` is an object, but functions and classes are not objects. The two languages use the same word for different things, a point we will meet again when discussing assignment semantics in [4.2.6](/4.2.6).

## Summary

- A programming paradigm is a mental model for organizing programs. Procedural programming takes functions as its unit and separates data from operations; object-oriented programming takes objects as its unit and encapsulates data and operations together.
- Abstraction discards the nonessential and extracts the essential; procedural abstraction yields functions and data abstraction yields types. Type = representation + operations.
- An object has state, behavior and identity; encapsulation combines data with operations and hides the implementation, so that an object can maintain its own invariants and its implementation can evolve independently.
- C++ offers zero-overhead abstraction and a deterministic object lifetime, and Python offers a dynamic and flexible object model; this course presents the same set of ideas in both languages side by side.
