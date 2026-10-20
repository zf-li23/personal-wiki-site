---
title: Object Lifetime
description: Constructors, member initializer lists, delegating constructors and default member initializers; default constructors, = default and = delete; destructors; lifetimes of local, global, static and dynamic objects and the order of construction and destruction; static and const members; friends; new and delete; RAII; __init__, __del__ and context managers in Python.
source_hash: 0d7df93c61a2
---

An object goes through three phases from birth to death: it acquires storage and is initialized, it is used, and it is cleaned up and its storage is released. In C, both initialization and cleanup depend on the programmer remembering to call the appropriate functions; forgetting initialization reads garbage values, and forgetting cleanup leaks resources. C++ answers as follows: how to initialize and clean up is decided by the designer of the class and written as constructors and destructors; when to initialize and clean up is decided by the compiler, which inserts the calls automatically where objects are created and destroyed. This chapter first covers constructors and destructors, then when different kinds of objects are constructed and destroyed, then static members that belong to the class itself rather than to any object, const members that cannot be modified, friends that can access private members, and `new` and `delete` for creating objects dynamically. Finally it covers RAII, the central idiom of C++ resource management, and compares it with Python's context managers. What happens when objects are copied and moved is the topic of [4.2.6](/4.2.6).

## 4.1. Constructors

### 4.1.1. Defining Constructors

**Definition 4.1.1 (Constructor)** A special member function of a class that has the same name as the class and no return type is called a **constructor**. Whenever an object of the class is created, the compiler automatically calls a constructor to initialize it.

Constructors can be overloaded to support different ways of initialization:

```cpp
class Student {
public:
    Student(int id) : id_(id) {}                                // Student s(20240001);
    Student(int year, int order) : id_(year * 10000 + order) {} // Student t(2024, 2);

private:
    int id_;
};
```

The mission of a constructor is to establish the class **invariant**: once construction is complete, the object must be in a valid state. If the arguments are invalid and the invariant cannot be established, the constructor should throw an exception, so that no "half-initialized" object ever exists.

### 4.1.2. Member Initializer Lists

The `id_(id)` after the colon and before the function body in the constructors above is a member initializer list.

**Definition 4.1.2 (Member Initializer List)** A list written after the parameter list of a constructor, beginning with a colon and of the form "member(initial value)" or "member{initial value}", is called a **member initializer list**; it specifies how each **data member** is initialized.

Assigning to the members in the function body can achieve a similar effect, but there is an essential difference: before the constructor body is entered, all members have already been initialized, and `id_ = id;` in the body is an assignment, not an initialization. For an `int` the difference is small, but the following members can be initialized only in the initializer list:

- `const` data members and reference members: they can only be initialized, not assigned;
- members of class type that have no default constructor: they cannot be constructed unless arguments are given in the initializer list;
- the base-class part ([4.2.7](/4.2.7)).

For members such as `std::string` and `std::vector`, default-constructing first and then assigning also does useless extra work. The rule is therefore simple: whatever can be initialized in the initializer list should be initialized there.

Members are initialized in the order in which they are declared in the class, regardless of the order written in the initializer list. If we write `Owner() : second_(2), first_(1) {}`, `first_` is still constructed first; if the initial value of one member depends on another, we must pay attention to the declaration order. `-Wall` gives a `-Wreorder` warning when the written order differs from the declaration order.

### 4.1.3. Default Member Initializers and Delegating Constructors

Since C++11, an initial value can be given directly where a data member is declared, called a *default member initializer*. If a constructor's initializer list does not mention that member, this value is used:

```cpp
class Config {
public:
    Config() = default;                    // width_ = 80, verbose_ = false
    explicit Config(int width) : width_(width) {}  // verbose_ = false
    Config(int width, bool verbose) : width_(width), verbose_(verbose) {}

private:
    int width_ = 80;
    bool verbose_{false};
};
```

A constructor can also call another constructor of the same class in its initializer list, delegating the work to it; this is called a *delegating constructor*, and it lets the common initialization logic be written only once:

```cpp
class Rational {
public:
    Rational(long num, long den) : num_(num), den_(den) { normalize(); }
    Rational(long n) : Rational(n, 1) {}  // delegate to the two-argument constructor
    Rational() : Rational(0) {}

private:
    void normalize();
    long num_, den_;
};
```

### 4.1.4. Default Constructors

**Definition 4.1.3 (Default Constructor)** A constructor that can be called without arguments, that is, one with no parameters or one whose parameters all have **default arguments**, is called a **default constructor**.

The default constructor is called when an object is defined without arguments. The differences among several ways of writing it:

```cpp
Config a;            // default constructor
Config b{};          // default constructor (value-initialization)
Config c = Config(); // default constructor
Config d();          // NOT an object: declares a function d returning Config
Config e[50];        // 50 objects, each default-constructed
```

`Config d();` is parsed as a function declaration, the famous C++ "most vexing parse". Brace initialization avoids it, and braces also reject **narrowing conversions** (`int x{3.5};` is a compile error), so modern C++ prefers initializing with `{}`.

If a class declares no constructors at all, the compiler implicitly defines a default constructor: for members with default member initializers it uses that value, for members of class type it calls their default constructors, and for members of built-in type it does nothing. The last point means:

```cpp
struct A {
    int a;      // no initializer
    int b = 1;
};

A g;            // global: zero-initialized first, so g.a == 0
int main() {
    A x;        // local: x.a is indeterminate; reading it is an error
    A y{};      // value-initialized: y.a == 0
    static A z; // static local: z.a == 0
}
```

Global and static objects are zero-initialized before any construction, while local objects are not; reading an uninitialized value is **undefined behavior** in C++23 and earlier (C++26 changes it to "erroneous behavior", which is still an error). The best habit is to write a default member initializer for every member of built-in type.

Once any constructor is declared, the compiler no longer generates a default constructor implicitly. When it is still needed, `= default` explicitly asks the compiler to generate it; conversely, `= delete` can forbid a certain way of construction:

```cpp
class Student {
public:
    Student() = default;           // keep the compiler-generated default constructor
    Student(int id) : id_(id) {}
    Student(char) = delete;        // Student s('c') would otherwise convert 'c' to int

private:
    int id_ = 0;
};

Student s1;        // OK
Student s2(42);    // OK
// Student s3('c'); // error: use of deleted function 'Student::Student(char)'
```

A deleted function still takes part in overload resolution and is an error once selected; that is exactly its purpose: `'c'` matches `Student(char)` exactly and is therefore not quietly converted to `int`. A single-argument constructor is also used for **implicit conversions** and should usually be declared `explicit` ([4.2.6](/4.2.6)).

## 4.2. Destructors

**Definition 4.2.1 (Destructor)** A special member function named `~ClassName` with no parameters and no return type is called a **destructor**. When the **lifetime** of an object ends, the compiler calls it automatically to release the resources the object holds or to perform other finishing work.

There is only one way to clean up an object, and it is unconditional, so a destructor has no parameters and a class has only one destructor.

```cpp
class IntArray {
public:
    explicit IntArray(std::size_t n) : size_(n), data_(new int[n]{}) {}
    ~IntArray() { delete[] data_; }  // release what the constructor acquired
    // copying is dealt with in 4.2.6

private:
    std::size_t size_;
    int* data_;
};
```

When no destructor is declared, the compiler implicitly defines one, which destroys the members in turn. Note that "destroying" a pointer member merely makes the pointer itself disappear and does not release the memory it points to: if the `IntArray` above had no destructor, every object would leak a block of memory.

The order of construction and destruction is symmetric: at construction, the members are constructed first (in declaration order) and then the constructor body runs; at destruction, the destructor body runs first and then the members are destroyed in the reverse of the declaration order. This guarantees that all members are still usable in the destructor body.

```cpp
#include <iostream>

class Member {
public:
    explicit Member(int id) : id_(id) { std::cout << "Member(" << id_ << ")\n"; }
    ~Member() { std::cout << "~Member(" << id_ << ")\n"; }

private:
    int id_;
};

class Owner {
public:
    Owner() : first_(1), second_(2) { std::cout << "Owner body\n"; }
    ~Owner() { std::cout << "~Owner body\n"; }

private:
    Member first_;
    Member second_;
};

int main() {
    Owner o;
}
// Member(1)
// Member(2)
// Owner body
// ~Owner body
// ~Member(2)
// ~Member(1)
```

A destructor is `noexcept` by default and should not throw exceptions: destruction often happens while an exception is propagating (§4.7), and throwing another exception at that point terminates the program directly.

## 4.3. Object Lifetime

The lifetime of an object begins when its construction is complete and ends when its destruction begins. In C++ there are four kinds of *storage duration*, which determine when construction and destruction occur:

| Storage duration | Which objects | When constructed | When destroyed |
|---|---|---|---|
| Automatic | Local variables, function parameters | When execution reaches the definition | On leaving the enclosing scope (`{}` block), in reverse order of construction |
| Static | Global objects, objects in namespaces, `static` local objects, static data members | Global objects before `main`; `static` local objects when execution first reaches the definition | After `main` returns, in reverse order of construction |
| Dynamic | Objects created with `new` | When `new` is executed | When `delete` is executed; if `delete` is forgotten, never destroyed (a leak) |
| Thread | `thread_local` objects | When the thread starts or on first use | When the thread ends |

The following program demonstrates these rules:

```cpp
#include <iostream>
#include <string>

class Tracer {
public:
    explicit Tracer(std::string name) : name_(std::move(name)) {
        std::cout << "construct " << name_ << '\n';
    }
    ~Tracer() { std::cout << "destroy   " << name_ << '\n'; }

private:
    std::string name_;
};

Tracer global("global");

void f() {
    static Tracer once("static local");  // initialized on the first call only
    Tracer local("local in f");
}

int main() {
    std::cout << "main starts\n";
    Tracer a("a");
    {
        Tracer b("b");
        Tracer c("c");
    }  // c, then b, are destroyed here
    f();
    f();
    Tracer* p = new Tracer("heap");
    delete p;
    std::cout << "main ends\n";
}  // a is destroyed; after main returns: static local, then global
```

```text
construct global
main starts
construct a
construct b
construct c
destroy   c
destroy   b
construct static local
construct local in f
destroy   local in f
construct local in f
destroy   local in f
construct heap
destroy   heap
main ends
destroy   a
destroy   static local
destroy   global
```

A few remarks:

- Local objects are destroyed in reverse order of construction, which is consistent with the last-in-first-out nature of the stack and also guarantees that an object constructed later can safely depend on one constructed earlier.
- A `static` local object is constructed only when execution first reaches its definition (since C++11 this initialization is thread-safe), is not destroyed on leaving the function, and the same object is used directly in the next call.
- Global objects in the same **translation unit** are constructed in the order of their definitions; the construction order across different translation units is unspecified. If the constructor of a global object uses a global object in another file, the latter may not yet be constructed; this is called the static initialization order problem. One remedy is to turn the global object into a `static` local object inside a function, constructed on first use. A better remedy is to avoid global objects as far as possible: they increase coupling between modules and make programs hard to test, and can usually be replaced by passing arguments.
- The construction and destruction of a constant object (`const`) occur at the same times as for a non-constant object of the same class.
- A temporary object produced in an expression (such as an object returned by a function) is destroyed at the end of the evaluation of the whole expression; if the temporary is bound to a `const` reference, its lifetime is extended to that of the reference ([4.2.6](/4.2.6)).

A function parameter under **pass by value** is also an object: when `void fun(A b)` is called, the parameter `b` is copied from the argument (the copy constructor is called, [4.2.6](/4.2.6)) and destroyed when the function returns. So output such as "constructed once, destroyed twice" is not surprising: two different objects are destroyed; and when the class has a pointer member, the destructors of the two objects release the same block of memory, a problem that [4.2.6](/4.2.6) will solve. With **pass by reference** (`void fun(const A& b)`) no new object is created, and the cost of copying is saved.

## 4.4. Static Members and Const Members

### 4.4.1. Static Data Members

Some data belong to the whole class rather than to any object, for example "how many objects there are now" or "a configuration shared by all objects".

**Definition 4.4.1 (Static Member)** Data members and member functions declared with `static` are called **static members**. A static data member is shared by all objects of the class, exists in a single copy and is stored in the static storage area; a static member function acts on no object and has no `this` pointer.

A static member can be accessed through the class name (`Counter::count`) or through an object (`c.count`); the former is clearer. A static data member has static storage duration: it is initialized before `main`, regardless of whether any object of the class has been created.

```cpp
#include <iostream>

class Counter {
public:
    Counter() { ++alive_; ++created_; }
    ~Counter() { --alive_; }
    static int alive() { return alive_; }      // static member function: no this
    static int created() { return created_; }

    static constexpr int max_alive = 100;     // a constant shared by the class

private:
    static inline int alive_ = 0;    // C++17: defined and initialized in the class
    static inline int created_ = 0;
};

int main() {
    Counter a;
    {
        Counter b, c;
        std::cout << Counter::alive() << '\n';  // 3
    }
    Counter* p = new Counter;
    std::cout << Counter::alive() << ' ' << Counter::created() << '\n';  // 2 4
    delete p;
    std::cout << Counter::alive() << " of at most " << Counter::max_alive << '\n';  // 1 of at most 100
}
```

Before C++17, `static int alive_;` in a class was only a declaration, and a definition `int Counter::alive_ = 0;` had to be written once in exactly one implementation file; if the definition were put in a header, every translation unit including it would define it once, leading to multiple definitions at link time ([4.2.2](/4.2.2)). C++17 `inline` variables solve this problem: a `static inline` member can be initialized directly in the class, for any type. A `static constexpr` data member is implicitly `inline` and is used for class-level compile-time constants. The rule in older textbooks that "only constant static members of integer and enumeration types can be initialized in the class" is out of date.

A static member function has no `this` and therefore cannot access non-static members: non-static members belong to a particular object, and when a static member function is called there may be no object at all. For the same reason a static member function cannot be declared `const`.

### 4.4.2. Const Data Members and Const Member Functions

A `const` data member cannot be modified during the whole lifetime of the object, so its initial value can only be given in the member initializer list or by a default member initializer, not by assignment in the constructor body.

The case of const objects is more interesting. The data of a `const Student` object cannot change, so which member functions can it call? The compiler does not analyze function bodies; it looks at the declaration of the function:

**Definition 4.4.2 (Const Member Function)** A non-static member function marked `const` after its parameter list is called a **const member function**. It promises not to modify the state of the object: in the function body, the type of `this` is a pointer to const, and modifying a data member or calling a non-const member function is a compile error. A const object (and an object accessed through a const reference or a pointer to const) can call only const member functions.

```cpp
#include <iostream>

class Student {
public:
    explicit Student(int id) : id_(id) {}
    int id() const { return id_; }            // const member function
    void rename(int id) { /* id_ = id; */ (void)id; }  // id_ is const: cannot be assigned

    void print() const { std::cout << "const " << id_ << '\n'; }
    void print() { std::cout << "non-const " << id_ << '\n'; }  // overload on const

private:
    const int id_;     // must be set in the member initializer list
};

void show(const Student& s) {  // read-only access through a const reference
    std::cout << s.id() << '\n';
    // s.rename(1);  // error: rename is not a const member function
}

int main() {
    Student a(20240001);
    const Student b(20240002);
    a.print();  // non-const 20240001
    b.print();  // const 20240002
    show(a);    // 20240001
}
```

The `const` and non-`const` versions can form an overload, because their implicit `this` parameters have different types (`Student*` and `const Student*`): a non-const object prefers the non-const version, and a const object can call only the const version. The standard-library containers make heavy use of this; for example, `operator[]` of `std::vector` returns a const reference for a const object and a modifiable reference for a non-const object.

Every member function that does not modify the object should be declared `const`; this is called *const correctness*. Otherwise, once a user passes an object by const reference (the standard way of passing objects), these functions cannot be called. In a few cases, a member does not logically belong to the state of the object (such as a cache or a mutex) and can be declared `mutable`, which allows it to be modified in const member functions.

| Member | Where initialized | Accessible in a static member function | Modifiable in a const member function |
|---|---|---|---|
| Ordinary data member | Initializer list, default member initializer, or assignment in the constructor body | No | No (except `mutable`) |
| `const` data member | Initializer list, default member initializer | No | No |
| `static` data member | Defined outside the class, or `static inline` in the class | Yes | Yes (it does not belong to the object) |
| `static constexpr` data member | In the class | Yes | No |

## 4.5. Friends

**Access control** protects the private members of a class, but sometimes a non-member function is so closely related to the class that it needs direct access to its internals; the most typical case is the output operator `operator<<` ([4.2.5](/4.2.5)): its left operand is a `std::ostream`, so it cannot be written as a member function of our class.

**Definition 4.5.1 (Friend)** A function or class declared in a class with `friend` is called a **friend** of that class, and it can access all members of the class, including private and protected members.

```cpp
#include <iostream>

class Point;

class Inspector {  // all member functions of a friend class may access Point's internals
public:
    static void reset(Point& p);
};

class Point {
public:
    Point(double x, double y) : x_(x), y_(y) {}
    friend double dot(const Point& a, const Point& b);  // friend function
    friend class Inspector;                             // friend class

private:
    double x_, y_;
};

double dot(const Point& a, const Point& b) { return a.x_ * b.x_ + a.y_ * b.y_; }
void Inspector::reset(Point& p) { p.x_ = p.y_ = 0; }

int main() {
    Point a(1, 2), b(3, 4);
    std::cout << dot(a, b) << '\n';  // 11
    Inspector::reset(a);
    std::cout << dot(a, b) << '\n';  // 0
}
```

Properties of friends:

- A friend declaration can appear only inside the class, and it makes no difference whether it is written in a `public` or `private` region; a function declared a friend is not a member function of the class and has no `this`.
- Friendship is one-directional: if `A` declares `B` a friend, `B` can access the private members of `A`, but not conversely.
- Friendship is not transitive (a friend of a friend is not a friend) and not inherited (a derived class of a friend is not a friend, [4.2.7](/4.2.7)).
- A function can be a friend of several classes at once; one can also declare only a particular member function of another class as a friend.

Friends break **encapsulation** to some extent, but friendship is granted by the class itself and remains under the control of the class's author, which is essentially different from making a member `public`. Friends are suited to functions that work closely with the class and logically belong to its interface but cannot be written as members for syntactic reasons, chiefly operator overloading. Adding friends casually to get around **access control** indicates a problem in the design of the class's interface.

## 4.6. new and delete

`new` creates an object on the heap and does two things: it allocates enough memory (by calling `operator new`) and then calls the constructor on that memory. `delete` does the two opposite things: it calls the destructor and then releases the memory (by calling `operator delete`). This is the fundamental difference from C's `malloc`/`free`, which only allocate and release raw memory and do not call constructors and destructors.

```cpp
Tracer* p = new Tracer("one");     // allocate + construct
delete p;                          // destruct + deallocate

Tracer* arr = new Tracer[3]{Tracer("x"), Tracer("y"), Tracer("z")};
delete[] arr;                      // destructs all three elements, in reverse order
```

`new` and `delete`, and `new[]` and `delete[]`, must be used in pairs. Releasing an array obtained with `new[]` using `delete` is **undefined behavior**: common implementations store the number of elements in front of the array, and `delete[]` uses it to call the destructor of each element, whereas `delete` destroys only the first element and hands a wrong address to the memory-release function, which may result in a resource leak or a crash. For a type with no destructor it may "happen to be fine", but that does not change the fact that it is wrong.

Managing `new`/`delete` by hand is error-prone: forgetting `delete` causes leaks, `delete`-ing twice or continuing to use the object afterward causes undefined behavior ([4.1.8](/4.1.8)), and an exception thrown midway skips `delete`. The rule of modern C++ is to write no bare `new` and `delete`: use `std::vector` when a dynamic array is needed, and use `std::make_unique` to create an object managed by a `std::unique_ptr` when a single dynamic object is needed ([4.2.12](/4.2.12)). They are safe because of RAII, the topic of the next section.

## 4.7. RAII

### 4.7.1. Resource Acquisition Is Initialization

The resources a program must manage go far beyond memory: files, network connections, database connections, mutexes, handles of graphical interfaces and so on are all things that "must be returned after being acquired". The difficulty of managing them by hand is that a function may have several exits:

```cpp
void process(const char* path) {
    std::FILE* fp = std::fopen(path, "r");
    if (!fp) return;
    if (!check_header(fp)) return;       // leak: fp is not closed
    parse(fp);                           // may throw: fp is not closed
    std::fclose(fp);
}
```

Each additional `return` or call that may throw gives another chance to forget the release. C++ uses the guarantee that "the destructor of a local object is always called when it leaves scope" to give a systematic solution.

**Definition 4.7.1 (RAII)** Binding the lifetime of a resource to the lifetime of a local object, acquiring the resource in the constructor and releasing it in the destructor, is an idiom called **resource acquisition is initialization** (RAII).

Whether the function returns normally, returns from the middle, or exits because of an exception, local objects are destroyed. As an exception propagates outward along the **call stack**, the local objects already constructed in each **stack frame** along the way are destroyed in reverse order; this is called *stack unwinding*. Therefore a resource held by an RAII object is certain to be released, and cleanup code need not be repeated at every exit.

```cpp
#include <cstdio>
#include <iostream>
#include <stdexcept>
#include <string>

class File {
public:
    File(const char* path, const char* mode) : fp_(std::fopen(path, mode)) {
        if (!fp_) throw std::runtime_error(std::string("cannot open ") + path);
        std::cout << "opened " << path << '\n';
    }
    ~File() {
        std::fclose(fp_);
        std::cout << "closed\n";
    }
    File(const File&) = delete;             // a file handle must not be copied (4.2.6)
    File& operator=(const File&) = delete;

    void write(const std::string& s) {
        if (std::fputs(s.c_str(), fp_) < 0) throw std::runtime_error("write failed");
    }

private:
    std::FILE* fp_;  // invariant: a valid, open file
};

void save(const std::string& text) {
    File f("demo.txt", "w");
    f.write(text);
    if (text.empty()) throw std::invalid_argument("empty text");  // f is still closed
}

int main() {
    save("hello\n");
    try {
        save("");
    } catch (const std::exception& e) {
        std::cout << "error: " << e.what() << '\n';
    }
}
// opened demo.txt
// closed
// opened demo.txt
// closed
// error: empty text
```

Note that in the second call, "closed" is printed before "error": when the exception leaves `save`, `f` has already been destroyed and the file closed, and only then does the `catch` in `main` begin to execute. The constructor throws an exception when the file cannot be opened, so every `File` object holds a valid file; there is no such state as "a `File` that failed to open", and users need not check again.

### 4.7.2. RAII in the Standard Library

RAII is the design foundation of the C++ standard library, and almost every type that manages a resource follows it:

| Resource | RAII type | When released |
|---|---|---|
| Dynamic arrays, strings | `std::vector`, `std::string` | Memory is released on destruction ([4.2.10](/4.2.10)) |
| A single dynamic object | `std::unique_ptr`, `std::shared_ptr` | The object is `delete`d on destruction (when the last owner is destroyed) ([4.2.12](/4.2.12)) |
| Files | `std::ifstream`, `std::ofstream` | The file is closed on destruction ([4.2.11](/4.2.11)) |
| Mutexes | `std::lock_guard`, `std::scoped_lock`, `std::unique_lock` | Unlocked on destruction |
| Threads | `std::jthread` (C++20) | Requests stop and waits for the thread to finish on destruction |

This yields the principle of resource management in modern C++: hand every resource immediately to an object that owns it; prefer these RAII types for the data members of a class, so that the class itself often needs no destructor at all (the rule of zero in [4.2.6](/4.2.6)).

## 4.8. Python Comparison

### 4.8.1. \_\_init\_\_ and \_\_new\_\_

Creating an object `Student(42)` in Python also takes two steps: `__new__` allocates and returns a new object, and `__init__` initializes it. Usually only `__init__` needs to be defined; it corresponds to the constructor, and assigning attributes of `self` in it creates those attributes. Python has no constructor overloading; different ways of construction are implemented with default arguments or class methods, where a class method is a method that acts on the class itself and is often used as "another constructor". Python's class attributes correspond to C++ static data members, and `@staticmethod` corresponds to static member functions.

```python
from datetime import date


class Student:
    count = 0  # class attribute, like a static data member

    def __init__(self, student_id: int) -> None:
        self.student_id = student_id
        Student.count += 1

    @classmethod
    def from_year(cls, year: int, order: int) -> "Student":  # an alternative constructor
        return cls(year * 10000 + order)

    @staticmethod
    def is_valid_year(year: int) -> bool:  # no self, no cls
        return 1911 <= year <= date.today().year


s = Student.from_year(2024, 2)
print(s.student_id, Student.count, Student.is_valid_year(2024))  # 20240002 1 True
```

### 4.8.2. No Deterministic Destruction

Python has a `__del__` method, but it is not a destructor in the C++ sense. CPython manages memory by reference counting: an object is reclaimed immediately when its reference count drops to zero, and `__del__` is called at that point; but if the object is in a reference cycle, it must wait for the **garbage collection** mechanism to discover it, at an indeterminate time; for objects still alive when the interpreter exits, `__del__` is not even guaranteed to be called; and other Python implementations (such as PyPy) do not use reference counting, making the reclamation time even less certain. Therefore we cannot rely on `__del__` to release resources.

### 4.8.3. Context Managers and with

Python manages resources with the `with` statement.

**Definition 4.8.1 (Context Manager)** An object that implements the two methods `__enter__` and `__exit__` is called a **context manager**. The `with` statement calls `__enter__` on entering the block (its return value is bound to the name after `as`), and calls `__exit__` on leaving the block, whether it ends normally or exits because of an exception.

`with` and RAII solve the same problem: binding the release of a resource to the end of a block of code. The difference is that in C++ this binding holds automatically for every local object, whereas in Python `with` must be written explicitly.

```cpp tab
#include <cstdio>
#include <iostream>
#include <stdexcept>
#include <string>

class File {
public:
    File(const char* path, const char* mode) : fp_(std::fopen(path, mode)) {
        if (!fp_) throw std::runtime_error(std::string("cannot open ") + path);
        std::cout << "opened\n";
    }
    ~File() {
        std::fclose(fp_);
        std::cout << "closed\n";
    }
    File(const File&) = delete;
    File& operator=(const File&) = delete;
    void write(const std::string& s) { std::fputs(s.c_str(), fp_); }

private:
    std::FILE* fp_;
};

int main() {
    try {
        File f("demo.txt", "w");  // the scope of f is the "with block"
        f.write("hello\n");
        throw std::runtime_error("something failed");
    } catch (const std::exception& e) {
        std::cout << "error: " << e.what() << '\n';
    }
}
// opened
// closed
// error: something failed
```

```python tab
class File:
    def __init__(self, path: str, mode: str) -> None:
        self._path, self._mode = path, mode

    def __enter__(self) -> "File":
        self._fp = open(self._path, self._mode)
        print("opened")
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        self._fp.close()
        print("closed")
        return False  # False: do not swallow the exception

    def write(self, s: str) -> None:
        self._fp.write(s)


try:
    with File("demo.txt", "w") as f:
        f.write("hello\n")
        raise RuntimeError("something failed")
except RuntimeError as e:
    print("error:", e)
# opened
# closed
# error: something failed
```

The three parameters of `__exit__` describe the exception that occurred in the block (all `None` when there is none), and returning a true value indicates that the exception has been handled and no longer propagates outward. In fact, the file object returned by the built-in `open` is itself a context manager, and we should write `with open(path) as f:` directly; locks in the standard library (`threading.Lock`), temporary directories (`tempfile.TemporaryDirectory`), database connections and so on also support `with`. A simpler way of writing our own context manager is to decorate a generator function with `contextlib.contextmanager`: the code before `yield` corresponds to `__enter__`, and the code after it (placed in `finally`) corresponds to `__exit__`:

```python
from contextlib import contextmanager
import time


@contextmanager
def timer(label: str):
    start = time.perf_counter()
    try:
        yield
    finally:  # runs even if the block raises
        print(f"{label}: {time.perf_counter() - start:.3f} s")


with timer("sum"):
    total = sum(range(1_000_000))
print(total)  # 499999500000
```

## Summary

- A constructor is called automatically when an object is created and is responsible for establishing the invariant; members should be initialized in the initializer list, and the initialization order is the declaration order. When no constructor is declared, the compiler generates a default constructor; `= default` and `= delete` explicitly request or forbid a special member function.
- A destructor is called automatically when an object's lifetime ends; construction does members first and then the body, destruction does the body first and then the members, so the order is symmetric.
- Local objects are destroyed in reverse order on leaving scope; global and static objects are constructed and destroyed before and after `main`, and their initialization order across translation units is unspecified; dynamic objects are created by `new` and destroyed by `delete`, which must be paired.
- Static members belong to the whole class, and static member functions have no `this`; C++17 `static inline` allows defining static data members in the class. Const member functions promise not to modify the object, and const objects can call only them.
- A friend is granted access by the class; it is one-directional, not transitive and not inherited, and is used mainly for operator overloading.
- RAII binds a resource to an object's lifetime so that it is released on every exit path, and is the foundation of C++ resource management; Python achieves the same purpose with context managers and `with`, and one should not rely on `__del__`.
