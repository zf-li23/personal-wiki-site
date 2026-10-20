---
title: Design Patterns
description: The concept and classification of design patterns; the template method, strategy, adapter and decorator patterns through the example of a load monitor; design principles such as the open–closed principle, the single-responsibility principle and SOLID; the corresponding idioms in Python using first-class functions, duck typing and decorator syntax.
source_hash: e23c7e845eeb
---

The preceding chapters covered the mechanisms of object-oriented programming: **encapsulation**, **composition** and **inheritance**, **virtual functions** and **polymorphism**, **templates**, **function objects**. The mechanisms alone do not guarantee a well-structured program: the same requirements can be written as code in which every change ripples everywhere, or as code in which adding a feature only means adding a new class. Design patterns are mature solutions to recurring design problems, distilled by developers from long practice, and they show how to combine these mechanisms to cope with changing requirements. This chapter takes a load monitor as a running example, treats four patterns in turn (template method, strategy, adapter and decorator), distills from them design principles such as the open–closed principle and the single-responsibility principle, and explains why, in a language like Python with first-class functions and duck typing, many patterns can be written much more lightly. Other aspects of software design (requirements, architecture, testing and maintenance) are covered in [4.14 Software Engineering](/4.14).

## 13.1. Design Patterns

**Definition 13.1.1 (Design Pattern)** A description of a proven, reusable solution to a problem that recurs in a particular context of software design is called a **design pattern**. A pattern usually comprises a name, the problem it solves, the structure of the solution (the participating classes and objects and how they collaborate), and the consequences of using it (benefits and costs).

The concept became widely known through the 1994 book *Design Patterns: Elements of Reusable Object-Oriented Software* by Gamma, Helm, Johnson and Vlissides (often called the Gang of Four, GoF). The book collects 23 patterns in three categories:

| Category | Concern | Examples |
|---|---|---|
| Creational | How to create objects, separating creation from use | Factory method, abstract factory, builder, singleton |
| Structural | How to compose classes and objects into larger structures | Adapter, decorator, composite, proxy, facade |
| Behavioral | How responsibilities are distributed among objects and how they collaborate | Template method, strategy, observer, iterator, command |

Two principles run through the book: program to an interface, not to an implementation (Chapter 8); and favor composition over inheritance (Chapter 7). As we shall see, the four patterns below are concrete embodiments of these two principles. Design patterns are also valuable as a shared vocabulary: saying "use the strategy pattern here" lets a colleague understand the whole structure.

## 13.2. Example: A Load Monitor

Suppose we are to write a program that monitors the load of a compute node: every second it reads the CPU load, the total memory, the used memory and the network latency, and then displays them. The difficulty is that how to read this information differs between environments: on Linux one reads files under `/proc`, on Windows one calls a system API, and in a cluster one may also fetch it from a monitoring system such as Ganglia.

The most direct way is to enumerate all the environments and branch on the environment in every function:

```cpp
enum class Platform { Linux, Windows, Ganglia };

class Monitor {
public:
    explicit Monitor(Platform p) : platform_(p) {}
    double getLoad() const {
        switch (platform_) {
            case Platform::Linux:   return 0.42;   // read /proc/loadavg
            case Platform::Windows: return 0.35;   // call the Windows API
            case Platform::Ganglia: return 0.77;   // query the Ganglia daemon
        }
        return 0.0;
    }
    // getTotalMemory(), getUsedMemory(), getNetworkLatency(): the same switch again
private:
    Platform platform_;
};
```

The problem with this is that every new environment requires modifying the enumeration and the `switch` in every function; the code for one environment is scattered across functions, while the code for different environments is crowded into the same function, so a change in one place easily breaks another. The ideal is that adding an environment only requires adding new code, without modifying code that has already been written and tested.

**Definition 13.2.1 (Open–Closed Principle)** Software entities (classes, modules, functions) should be open for extension and closed for modification: when requirements change, their behavior should be extended by adding new code rather than modifying existing code. This design principle is called the **open–closed principle**.

The means of realizing the open–closed principle are the **abstraction** and **polymorphism** of Chapter 8: hide what may change behind a stable interface, and add each change as a new implementation class.

## 13.3. The Template Method Pattern

**Definition 13.3.1 (Template Method Pattern)** Defining the skeleton of an algorithm in a method of a base class, declaring some of its steps as virtual functions to be implemented by derived classes, so that derived classes can redefine these steps without changing the structure of the algorithm, is a design pattern called the **template method pattern**. The method that defines the skeleton is called the template method.

(Here "template" refers to the framework of an algorithm and has nothing to do with the C++ **templates** of Chapter 9.) The procedure of the monitor, "read the indicators, then display them", is fixed, and only the way of reading varies; so we write the procedure in the base class and leave the individual reading steps to the derived classes:

```cpp tab
#include <format>
#include <iostream>
#include <memory>
#include <string>
#include <vector>

class Monitor {
public:
    virtual ~Monitor() = default;
    void report() const {                       // the template method: a fixed skeleton
        std::cout << std::format("[{}] load {:.2f}, memory {}/{} MB\n",
                     source(), getLoad(), getUsedMemory(), getTotalMemory());
    }
private:                                        // the steps, overridden by subclasses
    virtual std::string source() const = 0;
    virtual double getLoad() const = 0;
    virtual long getTotalMemory() const = 0;
    virtual long getUsedMemory() const = 0;
};

class LinuxMonitor : public Monitor {
    std::string source() const override { return "linux"; }
    double getLoad() const override { return 0.42; }          // read /proc/loadavg
    long getTotalMemory() const override { return 16384; }    // read /proc/meminfo
    long getUsedMemory() const override { return 5120; }
};

class WindowsMonitor : public Monitor {
    std::string source() const override { return "windows"; }
    double getLoad() const override { return 0.35; }          // call the Windows API
    long getTotalMemory() const override { return 8192; }
    long getUsedMemory() const override { return 2048; }
};

int main() {
    std::vector<std::unique_ptr<Monitor>> monitors;
    monitors.push_back(std::make_unique<LinuxMonitor>());
    monitors.push_back(std::make_unique<WindowsMonitor>());
    for (const auto& m : monitors) m->report();
}
```

```python tab
from abc import ABC, abstractmethod


class Monitor(ABC):
    def report(self) -> None:                   # the template method: a fixed skeleton
        print(f"[{self.source()}] load {self.get_load():.2f}, "
              f"memory {self.get_used_memory()}/{self.get_total_memory()} MB")

    @abstractmethod
    def source(self) -> str: ...
    @abstractmethod
    def get_load(self) -> float: ...
    @abstractmethod
    def get_total_memory(self) -> int: ...
    @abstractmethod
    def get_used_memory(self) -> int: ...


class LinuxMonitor(Monitor):
    def source(self) -> str: return "linux"
    def get_load(self) -> float: return 0.42
    def get_total_memory(self) -> int: return 16384
    def get_used_memory(self) -> int: return 5120


class WindowsMonitor(Monitor):
    def source(self) -> str: return "windows"
    def get_load(self) -> float: return 0.35
    def get_total_memory(self) -> int: return 8192
    def get_used_memory(self) -> int: return 2048


for m in [LinuxMonitor(), WindowsMonitor()]:
    m.report()
```

```text
[linux] load 0.42, memory 5120/16384 MB
[windows] load 0.35, memory 2048/8192 MB
```

Adding an environment only requires writing another derived class; neither `Monitor` nor the existing derived classes need to change, which conforms to the open–closed principle. In C++, writing the template method as a public non-virtual function and the steps as private virtual functions is called the *non-virtual interface* idiom, NVI for short: derived classes can override the private virtual functions but cannot bypass the skeleton to call them directly, so the base class can uniformly add checks, logging and similar logic in the skeleton.

The limitation of the template method is that each derived class must decide the implementation of all steps at once. If there are $n$ ways to read the load, $k$ for memory and $m$ for network latency, and they can be combined freely (for example, on Linux reading the load with Ganglia and the memory from `/proc`), then up to $n \cdot k \cdot m$ derived classes are needed, with a great deal of duplicated code.

## 13.4. The Strategy Pattern

### 13.4.1. Composition Instead of Inheritance

**Definition 13.4.1 (Strategy Pattern)** Encapsulating each of a family of interchangeable algorithms in a separate class implementing the same interface, with the object that uses the algorithm (the context) holding a strategy object by composition and delegating the corresponding work to it, is a design pattern called the **strategy pattern**.

We abstract each kind of variation of the monitor into a strategy interface, and the monitor is composed of several strategy objects:

```cpp tab
#include <format>
#include <iostream>
#include <memory>
#include <utility>

class LoadStrategy {                                  // one interface per kind of variation
public:
    virtual ~LoadStrategy() = default;
    virtual double load() const = 0;
};
class ProcLoad : public LoadStrategy {
    double load() const override { return 0.42; }     // read /proc/loadavg
};
class GangliaLoad : public LoadStrategy {
    double load() const override { return 0.77; }     // query the Ganglia daemon
};

class MemoryStrategy {
public:
    virtual ~MemoryStrategy() = default;
    virtual long total() const = 0;
    virtual long used() const = 0;
};
class ProcMemory : public MemoryStrategy {
    long total() const override { return 16384; }
    long used() const override { return 5120; }
};

class Monitor {  // the context: a composition of strategies
public:
    Monitor(std::unique_ptr<LoadStrategy> load, std::unique_ptr<MemoryStrategy> memory)
        : load_(std::move(load)), memory_(std::move(memory)) {}
    void setLoadStrategy(std::unique_ptr<LoadStrategy> s) { load_ = std::move(s); }
    void report() const {
        std::cout << std::format("load {:.2f}, memory {}/{} MB\n", load_->load(), memory_->used(), memory_->total());
    }
private:
    std::unique_ptr<LoadStrategy> load_;
    std::unique_ptr<MemoryStrategy> memory_;
};

int main() {
    Monitor m(std::make_unique<ProcLoad>(), std::make_unique<ProcMemory>());
    m.report();
    m.setLoadStrategy(std::make_unique<GangliaLoad>());   // switch at run time
    m.report();
}
```

```python tab
from collections.abc import Callable
from dataclasses import dataclass


def proc_load() -> float:                  # strategies are just functions
    return 0.42


def ganglia_load() -> float:
    return 0.77


@dataclass
class ProcMemory:                          # a strategy with two operations stays an object
    def total(self) -> int: return 16384
    def used(self) -> int: return 5120


@dataclass
class Monitor:
    load: Callable[[], float]
    memory: ProcMemory

    def report(self) -> None:
        print(f"load {self.load():.2f}, memory {self.memory.used()}/{self.memory.total()} MB")


m = Monitor(proc_load, ProcMemory())
m.report()
m.load = ganglia_load                      # switch at run time
m.report()
```

```text
load 0.42, memory 5120/16384 MB
load 0.77, memory 5120/16384 MB
```

Now $n$ ways of reading the load, $k$ ways of reading memory and $m$ ways of reading latency need only $n + k + m$ strategy classes, plus 3 strategy interfaces and 1 monitor class, instead of $n \cdot k \cdot m$ derived classes; any combination is made at run time and can even be changed while running. Each strategy class does only one thing and can be tested and reused individually.

### 13.4.2. The Single-Responsibility Principle

**Definition 13.4.2 (Single-Responsibility Principle)** A class (or module) should be responsible for a single duty, that is, have only one reason to change. This design principle is called the **single-responsibility principle**.

The `LinuxMonitor` of the template method version is responsible for reading the load, the memory and the latency at once: a change in any one of these ways of reading requires modifying it. The strategy pattern assigns each duty to a strategy class, decoupling the duties so that a change in one does not affect the others. A class with too many duties is often hard to understand and test, and modifying one place is more likely to disturb other functionality.

### 13.4.3. Template Method Versus Strategy

The two patterns solve the same problem: the impact of the diversity of algorithms on code structure. When the business logic is simple, the two are almost equivalent.

| | Template method | Strategy |
|---|---|---|
| Mechanism | Inheritance: derived classes override steps | Composition: the context class holds strategy objects |
| Granularity of variation | Some steps within a stable procedure | The whole algorithm |
| When determined | Compile time (which derived class is chosen) | Run time, can be changed |
| Several dimensions of variation | Number of derived classes grows as a product | Grows as a sum |
| Suited to | Complex, stable procedures with only local steps varying | Algorithms that vary a lot and must be combined freely |

In C++, a strategy with only one operation can also be represented by the `std::function<double()>` of Chapter 12, which dispenses with the strategy interface and strategy classes and directly takes a **lambda expression**; in Python this is the preferred way to write it, as with `load` in the example above.

## 13.5. The Adapter Pattern

**Definition 13.5.1 (Adapter Pattern)** Converting the interface of a class into another interface that clients expect, so that classes that could not work together because of incompatible interfaces can work together, is a design pattern called the **adapter pattern**. The interface that clients expect is called the target, and the existing class to be converted is called the adaptee.

It is like a power adapter: a phone charger can only plug into a USB port, while the wall has only 220 V sockets, and the adapter converts one kind of interface into the other. In the monitor, suppose there is already a ready-made Windows monitor class that cannot be modified (for example, from a third-party library); its functionality meets our needs, but its interface differs from ours:

```cpp
#include <format>
#include <iostream>

class Probe {                                  // the target interface our code expects
public:
    virtual ~Probe() = default;
    virtual double load() const = 0;
    virtual long usedMemory() const = 0;
    virtual long totalMemory() const = 0;
};

void report(const Probe& p) {
    std::cout << std::format("load {:.2f}, memory {}/{} MB\n", p.load(), p.usedMemory(), p.totalMemory());
}

class Win32Monitor {                           // the adaptee: existing code we cannot change
public:
    float getLoading() const { return 0.35f; }
    long get_using_memory() const { return 2048; }
    long get_total_memory() const { return 8192; }
};

class Win32Adapter : public Probe {            // object adapter: composition
public:
    double load() const override { return legacy_.getLoading(); }
    long usedMemory() const override { return legacy_.get_using_memory(); }
    long totalMemory() const override { return legacy_.get_total_memory(); }
private:
    Win32Monitor legacy_;
};

class Win32ClassAdapter : public Probe, private Win32Monitor {   // class adapter: inheritance
public:
    double load() const override { return getLoading(); }
    long usedMemory() const override { return get_using_memory(); }
    long totalMemory() const override { return get_total_memory(); }
};

int main() {
    report(Win32Adapter{});
    report(Win32ClassAdapter{});
}
```

```text
load 0.35, memory 2048/8192 MB
load 0.35, memory 2048/8192 MB
```

There are two ways to implement an adapter:

- Object adapter: the adapter implements the target interface and holds an adaptee object by composition, forwarding calls to it. It can also adapt derived classes of the adaptee (when holding a pointer) and is the more commonly used form.
- Class adapter: the adapter inherits publicly from the target interface and privately from the adaptee ("implemented in terms of" in [4.2.7](/4.2.7)) and calls the inherited functions directly. Private inheritance ensures that the outside world sees only the target interface.

An adapter lets existing classes be reused without modification (conforming to the open–closed principle) and isolates clients from the interface of third-party components: when the component is replaced in the future, only the adapter needs rewriting. The `std::stack` and `std::queue` of the standard library are called container adapters (Chapter 10); they adapt the interface of `deque` to the interfaces of a stack and a queue.

In Python, thanks to **duck typing**, an adapter need not inherit from any interface and only has to provide the methods the client needs; for a simple adaptation that merely renames something, one can even assign the bound method of the adaptee directly to a new attribute name.

## 13.6. The Decorator Pattern

### 13.6.1. Adding Functionality to Objects Dynamically

Now we want to show the monitoring result in a window, with the option of adding a border, a horizontal scroll bar and a vertical scroll bar in any combination. With inheritance, every combination needs a derived class, and $k$ features give $2^k$ combinations; with the strategy pattern, the base class must reserve slots for a "border strategy" and a "scroll bar strategy" in advance, and adding a new feature requires modifying the base class.

**Definition 13.6.1 (Decorator Pattern)** Defining a decorator class that implements the same interface as the decorated object, holds a decorated object, and adds extra behavior before and after forwarding requests to it, is a design pattern called the **decorator pattern**. Since a decorated object still satisfies the same interface, it can be decorated again, so that several features are stacked layer by layer onto one object at run time.

```cpp tab
#include <format>
#include <iostream>
#include <memory>
#include <string>
#include <utility>

class View {                                       // the common interface
public:
    virtual ~View() = default;
    virtual std::string show() const = 0;
};

class MonitorView : public View {                  // the basic component
public:
    std::string show() const override { return "load 0.42"; }
};

class Decorator : public View {                    // wraps another View
public:
    explicit Decorator(std::unique_ptr<View> inner) : inner_(std::move(inner)) {}
protected:
    std::string inner() const { return inner_->show(); }
private:
    std::unique_ptr<View> inner_;
};

class Border : public Decorator {
public:
    using Decorator::Decorator;
    std::string show() const override { return "[" + inner() + "]"; }
};

class VScroll : public Decorator {
public:
    using Decorator::Decorator;
    std::string show() const override { return inner() + " |v"; }
};

class HScroll : public Decorator {
public:
    using Decorator::Decorator;
    std::string show() const override { return inner() + " <h>"; }
};

int main() {
    std::unique_ptr<View> v = std::make_unique<MonitorView>();
    v = std::make_unique<VScroll>(std::move(v));   // add features one layer at a time
    v = std::make_unique<HScroll>(std::move(v));
    v = std::make_unique<Border>(std::move(v));
    std::cout << std::format("{}\n", v->show());
    std::cout << std::format("{}\n", Border(std::make_unique<MonitorView>()).show());
}
```

```python tab
from typing import Protocol


class View(Protocol):
    def show(self) -> str: ...


class MonitorView:
    def show(self) -> str:
        return "load 0.42"


class Border:                                      # no common base class needed
    def __init__(self, inner: View) -> None:
        self.inner = inner

    def show(self) -> str:
        return "[" + self.inner.show() + "]"


class VScroll:
    def __init__(self, inner: View) -> None:
        self.inner = inner

    def show(self) -> str:
        return self.inner.show() + " |v"


class HScroll:
    def __init__(self, inner: View) -> None:
        self.inner = inner

    def show(self) -> str:
        return self.inner.show() + " <h>"


v: View = Border(HScroll(VScroll(MonitorView())))
print(v.show())
print(Border(MonitorView()).show())
```

```text
[load 0.42 |v <h>]
[load 0.42]
```

When `show` is called, the request travels along the chain of wrappers from the outside in: `Border` calls `HScroll`, `HScroll` calls `VScroll`, and finally `MonitorView` is reached, with each layer adding its own functionality to the result. Each decorator only knows that the object it directly wraps satisfies the `View` interface and need not know the whole chain. There are as many layers as there are features, and both the kinds and the order of the features are decided at run time; adding a new feature only requires writing a new decorator class. A typical example in other languages is Java's I/O streams (a buffered stream wraps a file stream); Python's `io.BufferedReader` wrapping a raw file object has the same structure.

### 13.6.2. Python's Decorator Syntax

Python's `@decorator` syntax shares its name and its idea with the decorator pattern, but acts on functions (or classes) rather than objects: a decorator is a function that takes a function as its argument and returns a new function, which is usually a **closure** (Chapter 12) wrapping the original function and adds logging, timing, caching, permission checks and the like before and after the call. Writing `@d` above `def f` is equivalent to executing `f = d(f)` after the definition; with several decorators, they wrap layer by layer from bottom to top.

```python
import functools


def logged(func):
    @functools.wraps(func)                # keep the name and docstring of func
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}{args}")
        return func(*args, **kwargs)
    return wrapper


@functools.cache                          # a standard decorator: memoization
def fib(n: int) -> int:
    return n if n < 2 else fib(n - 1) + fib(n - 2)


@logged
def add(a: int, b: int) -> int:           # equivalent to add = logged(add)
    return a + b


print(add(2, 3))
print(fib(80))
```

```text
calling add(2, 3)
5
23416728348467685
```

## 13.7. Design Principles

Design patterns are concrete solutions, while design principles are the general guidelines hidden behind them. The most frequently mentioned in object-oriented design are the five principles summarized by Robert C. Martin, which together form the acronym SOLID from their initials:

- S: the single-responsibility principle (Definition 13.4.2).
- O: the open–closed principle (Definition 13.2.1).
- L: the Liskov substitution principle, see Definition 13.7.1 below.
- I: the *interface segregation principle*. Clients should not be forced to depend on methods they do not use: rather than designing one all-encompassing large interface, split it into several small, focused interfaces, several of which a class may implement (the interfaces of multiple inheritance in Chapter 7).
- D: the *dependency inversion principle*. High-level modules should not depend on low-level modules; both should depend on abstractions: in the strategy pattern, `Monitor` depends on the `LoadStrategy` interface and not on a concrete way of reading, and the concrete strategy objects are created externally and passed in (dependency injection).

**Definition 13.7.1 (Liskov Substitution Principle)** If a type $S$ is a subtype of a type $T$, then wherever a program uses an object of type $T$, an object of type $S$ can be substituted without changing the correctness of the program. That is, a derived class must honor the contract of the base-class interface: not strengthen preconditions, not weaken postconditions, and preserve the invariants of the base class. This design principle is called the **Liskov substitution principle** and was proposed by Barbara Liskov in 1987.

The example of "a square is not a rectangle" in Chapter 7 violates exactly this principle: `Square` cannot honor the contract of `Rectangle` that "setting the width does not change the height". The Liskov substitution principle is the criterion for whether public inheritance may be used: is-a must hold in behavior and not only conceptually.

Two further principles are often listed alongside SOLID: the *composite reuse principle*, which prefers composition over inheritance for code reuse (the strategy, adapter and decorator patterns are all examples), and the *law of Demeter*, also known as the principle of least knowledge, according to which an object interacts only with its direct collaborators and does not reach into the internals of other objects through a chain such as `a.b().c().d()`.

The common goal of these principles is to reduce coupling and increase cohesion: to separate what may change from what is stable, and to confine changes to as small a scope as possible. They are guidelines for weighing trade-offs rather than rules that must be obeyed. Introducing abstractions in advance for changes that do not yet exist makes simple programs complicated; the common advice is to write the simplest workable code first and to refactor toward a suitable pattern once a change really appears, and appears more than once.

## 13.8. Patterns and Languages

The GoF patterns were distilled for languages such as C++ and Smalltalk, and quite a few of them compensate for features these languages lack. In languages with first-class functions, closures and duck typing, many patterns become very light, or even vanish into everyday idioms:

| Pattern | Typical C++ idiom | Corresponding idiom in Python |
|---|---|---|
| Strategy | Strategy interface plus strategy classes; or `std::function`, lambda | Pass a function directly |
| Template method | A non-virtual function of the base class calling private virtual functions | Inheritance as well, or pass the steps as function arguments |
| Command | Command interface plus `execute` | A function or `functools.partial` |
| Observer | Observer interface; a callback list `std::vector<std::function<…>>`, with `weak_ptr` to avoid dangling | A list of callback functions, `weakref` |
| Iterator | Iterator classes (Chapter 10) | The iterator protocol and generators |
| Adapter | A wrapper class implementing the target interface | A wrapper class under duck typing, or directly assigning a bound method |
| Decorator | A wrapper class implementing the same interface | A wrapper class; `@decorator` for functions |
| Singleton | A static local variable in a function (called the Meyers singleton) | A module-level object (a module is imported only once) |
| Factory | A function returning `std::unique_ptr<Base>` | A class is itself a callable factory; pass classes as arguments |

The problems behind the patterns (how to isolate change, how to make objects collaborate) exist in every language; only the way of expressing them changes. The point of studying design patterns is therefore not to memorize class diagrams but to recognize problems, understand the cost of each solution, and choose the most concise expression in the language at hand.

## Summary

- Design patterns are mature solutions to recurring design problems, divided into creational, structural and behavioral; the two basic principles of the GoF are to program to an interface and to favor composition.
- The template method fixes the procedure and opens the steps through inheritance; the strategy encapsulates interchangeable algorithms through composition, and with several dimensions of variation the number of classes grows as a sum rather than a product.
- An adapter converts interfaces so that incompatible existing classes can be reused without modification; a decorator implements the same interface and wraps an object, stacking features layer by layer at run time.
- The open–closed, single-responsibility, Liskov substitution, interface segregation and dependency inversion principles (SOLID) are the design guidelines behind these patterns; they should be weighed as needed, without over-designing for imagined changes.
- Python's first-class functions, duck typing and `@decorator` syntax make many patterns very light: a strategy is just a function, and an adapter need not inherit an interface.
