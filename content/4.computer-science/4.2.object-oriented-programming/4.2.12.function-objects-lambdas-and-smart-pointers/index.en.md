---
title: Function Objects, Lambdas and Smart Pointers
description: Function pointers and function objects; lambda expressions, captures and closures, generic lambdas; std::function and callbacks; the problems of raw pointers and ownership; unique_ptr, shared_ptr and reference counting, weak_ptr and reference cycles; Python's first-class functions, closures, reference counting and garbage collection.
source_hash: 81189651566a
---

This chapter discusses two topics that seem unrelated but are both about "wrapping behavior and resources into objects". The first half shows how to pass functions around as values: function pointers, function objects that can carry state, lambda expressions that define a function in place, and `std::function`, which can hold all of them. They let the algorithms of Chapter 10 accept user-defined comparisons and predicates, and they are a lightweight way to write the strategy pattern of Chapter 13. The second half covers smart pointers: class templates that write "who is responsible for releasing this memory" into the type, so that dynamically allocated objects are released automatically like local objects. They are a direct application of **resource acquisition is initialization** ([4.2.4](/4.2.4)) and **move semantics** ([4.2.6](/4.2.6)) to memory management, and modern C++ code almost never needs a hand-written `delete`.

## 12.1. Functions as Values

### 12.1.1. Function Pointers

A function also has an address in memory, which can be stored in a function pointer and passed as an argument. The type of a function pointer is determined by the return type and the parameter types, for example `bool (*)(const Student&, const Student&)`; giving it an alias with `using` is more readable. C's `qsort` and many callback interfaces take function pointers as parameters, through which the caller leaves "how to compare" or "what to do when an event occurs" to the function being called.

The limitation of a function pointer is that it can point only to one fixed function and cannot carry extra data: for a predicate "score at least some threshold", the threshold can only be placed in a global variable.

### 12.1.2. Function Objects

**Definition 12.1.1 (Function Object)** An object of a class that overloads the function-call operator `operator()` and can therefore be called like a function is called a **function object** (also known as a functor).

A function object is an ordinary object and can keep state (such as a threshold) in data members, set by the constructor. It also has a performance advantage: each function-object class is a distinct type, so when an algorithm template is instantiated with it as the template argument, the compiler knows exactly which `operator()` is called and can inline it, whereas a call through a function pointer usually cannot be inlined. The standard library provides ready-made function objects such as `std::less`, `std::greater` and `std::plus` in `<functional>`.

```cpp tab
#include <algorithm>
#include <format>
#include <iostream>
#include <string>
#include <vector>

struct Student {
    std::string name;
    int score;
};

bool byName(const Student& a, const Student& b) { return a.name < b.name; }

struct ByScoreDesc {                              // a stateless function object
    bool operator()(const Student& a, const Student& b) const { return a.score > b.score; }
};

class AtLeast {                                   // a function object with state
public:
    explicit AtLeast(int limit) : limit_(limit) {}
    bool operator()(const Student& s) const { return s.score >= limit_; }
private:
    int limit_;
};

int main() {
    std::vector<Student> v{{"Carol", 88}, {"Alice", 95}, {"Bob", 88}};

    bool (*cmp)(const Student&, const Student&) = byName;   // a function pointer
    std::ranges::sort(v, cmp);
    std::ranges::stable_sort(v, ByScoreDesc{});             // ties keep name order
    for (const auto& s : v) std::cout << std::format("{}:{} ", s.name, s.score);
    std::cout << '\n';
    std::cout << std::format("{} student(s) >= 90\n", std::ranges::count_if(v, AtLeast(90)));
}
```

```python tab
from dataclasses import dataclass
from operator import attrgetter


@dataclass
class Student:
    name: str
    score: int


class AtLeast:                                    # a callable object with state
    def __init__(self, limit: int) -> None:
        self.limit = limit

    def __call__(self, s: Student) -> bool:
        return s.score >= self.limit


v = [Student("Carol", 88), Student("Alice", 95), Student("Bob", 88)]
v.sort(key=attrgetter("name"))                    # key functions instead of comparators
v.sort(key=lambda s: s.score, reverse=True)       # sort is stable
print(*(f"{s.name}:{s.score}" for s in v))
print(f"{sum(map(AtLeast(90), v))} student(s) >= 90")
```

```text
Alice:95 Bob:88 Carol:88
1 student(s) >= 90
```

## 12.2. Lambda Expressions

### 12.2.1. Syntax

Writing a whole class just to pass `count_if` a predicate "score at least 90" is cumbersome. The lambda expressions of C++11 let us write the function object right at the point of use.

**Definition 12.2.1 (Lambda Expression)** An expression of the form `[capture list](parameter list) -> return type { body }` is called a **lambda expression**; it defines an anonymous function object. The compiler generates for each lambda expression a unique, unnamed class (the closure type) whose `operator()` has the body of the lambda; evaluating the lambda expression yields an object of this class (the closure object).

The return type can be omitted when it can be deduced from the `return` statements, and the parameter list `()` can be omitted when there are no parameters. The `AtLeast(90)` of the previous section can be written as `[](const Student& s) { return s.score >= 90; }`. The type of a lambda has no name; to store one, use `auto`.

### 12.2.2. Captures and Closures

The body of a lambda can directly use only its parameters, global variables and static variables; to use a local variable of the enclosing function, it must be listed in the capture list:

| Capture | Meaning |
|---|---|
| `[x]` | Capture `x` by value: a copy is made when the closure is created, and later changes of the outer `x` do not affect it |
| `[&x]` | Capture `x` by reference: the closure uses the outer `x` itself |
| `[=]`, `[&]` | Implicitly capture, by value or by reference, all local variables used in the body |
| `[this]`, `[*this]` | Capture the pointer to the current object, or a copy of the current object |
| `[y = expr]` | Init-capture (C++14): initialize a new member with an expression, for example `[p = std::move(p)]` moves in a move-only object |

A variable captured by value is `const` in the closure by default; to modify its copy, declare the lambda `mutable`.

**Definition 12.2.2 (Closure)** The entity formed by a function together with the variables in the enclosing scope that it refers to (its environment) is called a **closure**. In C++, the closure object obtained by evaluating a lambda expression is a closure: the captured variables become data members of that object.

```cpp
#include <algorithm>
#include <format>
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v{1, 2, 3, 4};
    int base = 10;
    auto addBase = [base](int x) { return x + base; };   // copies base now
    base = 100;
    std::cout << std::format("{}\n", addBase(1));                       // 11, not 101

    int total = 0;
    std::ranges::for_each(v, [&total](int x) { total += x; });   // by reference
    std::cout << std::format("{}\n", total);

    auto counter = [n = 0]() mutable { return ++n; };     // init-capture, own state
    counter();
    std::cout << std::format("{}\n", counter());

    int limit = 3;
    std::cout << std::format("{}\n", std::ranges::count_if(v, [limit](int x) { return x >= limit; }));
}
```

```text
11
10
2
2
```

The greatest danger of capturing by reference is dangling: when a closure outlives the local variable it captured (for example when the closure is returned, stored in a container, or handed to another thread), the variable it refers to has already been destroyed. For example, the closure returned by `int n = 0; return [&n] { return ++n; };` in a function refers to the destroyed local variable `n`, and calling it is undefined behavior. The rule is that a closure captures by reference only when it is used synchronously within the current scope (such as when passed to `std::sort`); a closure to be stored or returned captures by value. In a member function, the implicit `[=]` captures only the `this` pointer and not copies of the members, which can dangle as well; since C++20 implicitly capturing `this` via `[=]` is deprecated, and one should write `[this]` or `[*this]` explicitly.

### 12.2.3. Generic Lambdas

A lambda whose parameter types are written as `auto` (C++14) is called a generic lambda; its `operator()` is a member function template (Chapter 9) and can accept arguments of different types. For example, `[](const auto& a, const auto& b) { return a.size() < b.size(); }` can compare any objects that have `size()`. C++20 also allows writing template parameters with constraints: `[]<std::integral T>(T x) { return x * 2; }`.

## 12.3. std::function and Callbacks

Function pointers, function objects and lambdas are all callable objects, but their types differ: the type of each lambda does not even have a name. To store them in the same container, to use them as data members of a class, or to pass them as parameters of non-template functions, we need a type that can hold "any callable object with the same signature", and this is `std::function<R(Args...)>`.

Below is a simple calculator: reading, computing and output each have several implementations, and the function `process` accepts any combination through `std::function`. It solves the same problem as the inheritance-based template method pattern of Chapter 13, but without defining any base class.

```cpp tab
#include <format>
#include <functional>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using ReadFunc = std::function<std::string()>;
using CalcFunc = std::function<std::string(const std::string&)>;
using WriteFunc = std::function<void(const std::string&)>;

void process(const ReadFunc& read, const CalcFunc& calc, const WriteFunc& write) {
    write(calc(read()));
}

std::string readFixed() { return "3 4 5"; }               // a plain function

struct Sum {                                              // a function object
    std::string operator()(const std::string& in) const {
        std::istringstream ss(in);
        int s = 0, x;
        while (ss >> x) s += x;
        return std::to_string(s);
    }
};

int main() {
    process(readFixed, Sum{}, [](const std::string& out) { std::cout << std::format("result: {}\n", out); });

    std::vector<std::string> log;
    process([] { return std::string("2 3 7"); },
            [](const std::string& in) {                   // a lambda computing a product
                std::istringstream ss(in);
                long p = 1, x;
                while (ss >> x) p *= x;
                return std::to_string(p);
            },
            [&log](const std::string& out) { log.push_back(out); });
    std::cout << std::format("logged: {}\n", log.front());
}
```

```python tab
import math
from collections.abc import Callable


def process(read: Callable[[], str], calc: Callable[[str], str],
            write: Callable[[str], None]) -> None:
    write(calc(read()))


def read_fixed() -> str:                                  # a plain function
    return "3 4 5"


class Sum:                                                # a callable object
    def __call__(self, text: str) -> str:
        return str(sum(map(int, text.split())))


process(read_fixed, Sum(), lambda out: print("result:", out))

log: list[str] = []
process(lambda: "2 3 7",
        lambda text: str(math.prod(map(int, text.split()))),
        log.append)                                       # a bound method is callable too
print("logged:", log[0])
```

```text
result: 12
logged: 42
```

`std::function` is implemented internally with **type erasure** (Chapter 9): it stores a copy of the callable object and forwards calls through one indirect call, and larger callable objects also require heap allocation. The three ways of passing callable objects therefore each have their own uses:

| Way | Accepts | Cost | Suited to |
|---|---|---|---|
| Function pointer | Ordinary functions, non-capturing lambdas | Indirect call | Interaction with C interfaces |
| Template parameter `template <typename F>` (can be constrained with `std::invocable`) | Any callable object | None, can be inlined | Algorithms, functions that return right after the call |
| `std::function` | Any callable object with a matching signature | Indirect call, possible heap allocation | Callbacks that must be stored: event handlers, class members, container elements |

C++23 adds `std::move_only_function`, which can hold move-only callable objects (for example, a lambda that captures a `unique_ptr`).

## 12.4. Smart Pointers

### 12.4.1. Ownership and the Problems of Raw Pointers

An object created with `new` must be `delete`d exactly once. With raw pointers, this responsibility rests entirely on the programmer's memory, and common mistakes include forgetting to `delete` (a **memory leak**), deleting twice, continuing to use the object after `delete` (a **dangling pointer**), and an exception or early `return` between `new` and `delete` that skips the `delete`. The fundamental difficulty is that the type of a raw pointer `T*` says nothing about ownership: given a pointer, there is no way to know whether one is supposed to release it.

**Definition 12.4.1 (Smart Pointer)** An object of a class template that owns a dynamically allocated object, automatically releases it on its own destruction according to ownership rules, and overloads `*` and `->` so that it is used like a pointer, is called a **smart pointer**.

Smart pointers are an application of RAII: the release is written in the destructor, so the object is released whether execution ends normally, returns early or throws an exception. The C++ standard library provides three smart pointers in `<memory>`, expressing three ownership relations.

### 12.4.2. unique_ptr: Exclusive Ownership

`std::unique_ptr<T>` owns the object it points to exclusively: at any time only one `unique_ptr` owns the object, and it releases the object when destroyed. It cannot be copied (its **copy constructor** is deleted) and can only be moved; after a move the original `unique_ptr` becomes empty, so a transfer of ownership is evident in the code. With the default deleter it takes no more space than a raw pointer and has no run-time overhead, and it is the default choice for dynamically allocated objects.

```cpp
#include <format>
#include <iostream>
#include <memory>
#include <string>
#include <utility>

struct Resource {
    explicit Resource(std::string n) : name(std::move(n)) { std::cout << std::format("acquire {}\n", name); }
    ~Resource() { std::cout << std::format("release {}\n", name); }
    std::string name;
};

std::unique_ptr<Resource> make(std::string name) {        // a factory hands over ownership
    return std::make_unique<Resource>(std::move(name));
}

int main() {
    auto a = make("A");
    auto b = std::move(a);              // ownership moves; a becomes empty
    // auto c = b;                      // error: unique_ptr cannot be copied
    std::cout << std::format("a is empty: {}, b owns {}\n", a == nullptr, b->name);
    {
        auto t = make("T");
    }                                   // T is released at the end of the block
    b.reset();                          // release A now
    std::cout << "end of main\n";
}
```

```text
acquire A
a is empty: true, b owns A
acquire T
release T
release A
end of main
```

Create objects with `std::make_unique<T>(args...)` rather than writing `std::unique_ptr<T>(new T(args...))`: the former contains no raw `new` and is also more concise. A `unique_ptr` can be put into a container, and the `std::vector<std::unique_ptr<Shape>>` of Chapter 8 uses it to hold polymorphic objects; `std::unique_ptr<T[]>` manages dynamic arrays (a `vector` is generally better); and a custom deleter can be specified to manage non-memory resources such as file handles.

### 12.4.3. shared_ptr and Reference Counting

Sometimes an object is indeed owned jointly by several places and there is no telling who uses it last, for example a document shared by several windows, or data in a cache.

**Definition 12.4.2 (Reference Counting)** Maintaining for each shared object a counter that records how many owners currently refer to it, adding one when an owner is added, subtracting one when an owner gives up, and releasing the object when the count drops to zero, is a memory-management method called **reference counting**.

`std::shared_ptr<T>` implements shared ownership with reference counting: copying a `shared_ptr` increments the count, destroying or reassigning one decrements it, and the object is released when the last `shared_ptr` disappears. The counter lives in a separately allocated control block shared by all `shared_ptr`s that point to the same object; `std::make_shared` places the object and the control block in a single allocation and should be preferred. The increments and decrements of the count are atomic operations, so it is safe for several threads to copy different `shared_ptr`s simultaneously, but this also makes copying a `shared_ptr` much slower than copying a raw pointer. A function that merely uses an object read-only should therefore accept `T&` or `const T&` rather than a `shared_ptr` by value.

The principle of reference counting can be illustrated in a few dozen lines of code. The following is a minimal `SharedPtr` that only demonstrates maintaining the count (no thread safety, move operations or `weak_ptr` support); for the writing of copy control see [4.2.6](/4.2.6):

```cpp
#include <format>
#include <iostream>
#include <string>
#include <utility>

template <typename T>
class SharedPtr {
public:
    explicit SharedPtr(T* p = nullptr) : ptr_(p), count_(p ? new long(1) : nullptr) {}
    SharedPtr(const SharedPtr& other) : ptr_(other.ptr_), count_(other.count_) {
        if (count_) ++*count_;                    // one more owner
    }
    SharedPtr& operator=(SharedPtr other) {       // copy-and-swap
        swap(other);
        return *this;                             // the old value is released with other
    }
    ~SharedPtr() {
        if (count_ && --*count_ == 0) {           // the last owner frees the object
            delete ptr_;
            delete count_;
        }
    }
    void swap(SharedPtr& other) noexcept {
        std::swap(ptr_, other.ptr_);
        std::swap(count_, other.count_);
    }
    T& operator*() const { return *ptr_; }
    T* operator->() const { return ptr_; }
    long useCount() const { return count_ ? *count_ : 0; }
private:
    T* ptr_;
    long* count_;
};

int main() {
    SharedPtr<std::string> a(new std::string("shared"));
    std::cout << std::format("{}\n", a.useCount());             // 1
    {
        SharedPtr<std::string> b = a;
        SharedPtr<std::string> c;
        c = b;
        std::cout << std::format("{} {}\n", a.useCount(), *c);  // 3 shared
    }
    std::cout << std::format("{}\n", a.useCount());             // 1
}
```

When using `shared_ptr`, avoid constructing two `shared_ptr`s from the same raw pointer: each would create its own control block, and the object would be released twice. When a member function of a class needs a `shared_ptr` to the object itself, let the class inherit from `std::enable_shared_from_this<T>` and call `shared_from_this()`.

### 12.4.4. weak_ptr and Reference Cycles

Reference counting has an inherent defect: if the `shared_ptr`s among objects form a cycle, for example when the nodes of a doubly linked list own each other, then even when no external pointer points to them any more, the count of every object in the cycle is at least 1 and they are never released.

`std::weak_ptr<T>` points to an object managed by `shared_ptr` but takes no part in ownership and does not increment the count. The object may already have been released, so it cannot be accessed directly through a `weak_ptr`; one first calls `lock()`, which yields a valid `shared_ptr` if the object is still alive (guaranteeing that it stays alive during the access) and an empty pointer if it has been released. Turning the "backward" edge of the cycle into a `weak_ptr` breaks the cycle:

```cpp
#include <format>
#include <iostream>
#include <memory>
#include <string>
#include <utility>

struct Node {
    explicit Node(std::string n) : name(std::move(n)) {}
    ~Node() { std::cout << std::format("~Node {}\n", name); }
    std::string name;
    std::shared_ptr<Node> next;        // owning, forward
    std::weak_ptr<Node> prev;          // non-owning, backward: breaks the cycle
};

int main() {
    auto a = std::make_shared<Node>("a");
    auto b = std::make_shared<Node>("b");
    a->next = b;
    b->prev = a;
    if (auto p = b->prev.lock()) std::cout << std::format("b.prev = {}\n", p->name);
    std::cout << std::format("use counts: a {}, b {}\n", a.use_count(), b.use_count());
}
```

```text
b.prev = a
use counts: a 1, b 2
~Node a
~Node b
```

If `prev` were also written as a `shared_ptr`, the count of `a` would be 2, and after `main` ends the counts of both nodes would stay at 1 and no destructor would run. Pointers from child nodes to parent nodes in a tree, observer lists and caches are typical uses of `weak_ptr`.

### 12.4.5. Guidelines

| Situation | What to use |
|---|---|
| A dynamically allocated object with a unique owner (the default) | `std::unique_ptr`, created with `std::make_unique` |
| Several owners indeed exist and there is no telling who uses it last | `std::shared_ptr`, created with `std::make_shared` |
| Need to refer to a shared object without owning it (back pointers, observers, caches) | `std::weak_ptr` |
| A function merely uses the object, with no ownership involved | `T&`, `const T&`; `T*` when it may be null |
| A function takes over ownership | Accept `std::unique_ptr<T>` by value |

Under these conventions, a raw pointer in the code only means "does not own", and `new` and `delete` appear only in the implementation of low-level data structures.

## 12.5. Python Comparison

### 12.5.1. First-Class Functions

Python functions are first-class objects: they can be assigned to variables, stored in containers, passed as arguments and returned as values. Python therefore needs no function pointers and seldom needs a wrapper like `std::function`: `sorted(v, key=len)` and `map(str.upper, words)` simply take the function. `lambda` defines an anonymous function, but its body can only be a single expression, and complex logic should be written as a named `def`. An instance of a class that defines `__call__` can be called like a function, corresponding to a C++ function object. The `operator` module of the standard library (`attrgetter`, `itemgetter`, `add`) corresponds to the ready-made function objects in `<functional>`, and `functools.partial` fixes some arguments of a function, equivalent to a lambda that captures arguments.

### 12.5.2. Closures and nonlocal

A nested function can use the local variables of the enclosing function; these variables still exist after the enclosing function returns, and the inner function together with them forms a closure. Unlike C++'s capture by value, a Python closure captures the variable itself (equivalent to capture by reference, except that the lifetime of the variable is extended and nothing dangles), and reads the current value of the variable at call time. For an inner function to rebind an outer variable, it must declare it `nonlocal`.

```cpp tab
#include <format>
#include <functional>
#include <iostream>
#include <vector>

auto makeCounter() {
    return [n = 0]() mutable { return ++n; };      // the closure owns its copy of n
}

int main() {
    auto c = makeCounter();
    c();
    std::cout << std::format("{}\n", c());

    std::vector<std::function<int()>> fs;
    for (int i = 0; i < 3; ++i) fs.push_back([i] { return i; });   // i copied each time
    for (const auto& f : fs) std::cout << std::format("{} ", f());
    std::cout << '\n';
}
```

```python tab
def make_counter():
    n = 0

    def inc() -> int:
        nonlocal n                                 # rebind the enclosing variable
        n += 1
        return n

    return inc


c = make_counter()
c()
print(c())

fs = [lambda: i for i in range(3)]                 # all three share the same i
print(*(f() for f in fs))
fs = [lambda i=i: i for i in range(3)]             # a default argument freezes the value
print(*(f() for f in fs))
```

```text
2
0 1 2
```

(The Python version prints `2 2 2` on the second line and `0 1 2` on the third.) The Python closures created in a loop all refer to the same loop variable, which has already reached its last value when they are called, the most common closure pitfall in Python; evaluating it at creation time with a default argument fixes this. A Python decorator is a function that takes a function as its argument and returns a closure; Chapter 13 compares it with the decorator pattern.

### 12.5.3. Reference Counting and Garbage Collection

Python programmers do not write `delete`, but the way objects are released is akin to `shared_ptr`: in CPython every object carries a reference count, which is incremented for each additional name, container element or attribute that refers to it, and the object is released immediately when the count drops to zero. This makes the timing of release largely predictable, but reference counting likewise cannot handle reference cycles, so CPython also has a **garbage collection** mechanism: a generational collector (the `gc` module) that periodically finds unreachable reference cycles and reclaims them. The standard library `weakref` provides weak references that do not increment the count, corresponding to `weak_ptr`:

```python
import gc
import sys
import weakref


class Node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.other: "Node | None" = None

    def __del__(self) -> None:
        print("free", self.name)


a = Node("a")
print(sys.getrefcount(a))         # the name a plus the temporary argument reference
r = weakref.ref(a)                # does not increase the count
print(r() is a)
del a                             # count drops to zero: freed immediately
print(r())

x, y = Node("x"), Node("y")
x.other, y.other = y, x           # a reference cycle
del x, y                          # counts stay at 1: nothing is freed yet
print("before collect")
gc.collect()                      # the cycle collector finds and frees them
print("after collect")
```

```text
2
True
free a
None
before collect
free x
free y
after collect
```

(The exact value from `sys.getrefcount` depends on the implementation and version of the interpreter.) Compared with C++, the price Python pays is that every object must maintain a count and the program must occasionally stop to detect cycles; the gain is that the programmer hardly has to think about ownership. Understanding reference counting is still useful: a large object often fails to be released because some container, cache or closure still refers to it.

## Summary

- A function pointer can point only to a fixed function; a function object can carry state and is easy for the compiler to inline.
- A lambda expression defines a function object in place, and the capture list decides how the closure stores outer variables; a closure to be stored or returned captures by value to avoid dangling.
- `std::function` holds any callable object with a matching signature by type erasure and suits callbacks that must be stored; algorithm-like functions accept callable objects through template parameters.
- Smart pointers write ownership into the type: `unique_ptr` is exclusive and zero-overhead, and is the default choice; `shared_ptr` shares ownership by reference counting; `weak_ptr` does not own the object and is used to break reference cycles.
- Python functions are first-class objects, and closures capture the variable itself; CPython manages memory with reference counting plus cycle detection, and `weakref` corresponds to `weak_ptr`.
