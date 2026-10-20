---
title: 对象的创建与销毁
description: 构造函数、成员初始化列表、委托构造与默认成员初始化；默认构造函数、= default 与 = delete；析构函数；局部、全局、静态与动态对象的生存期及构造析构顺序；静态成员与常量成员；友元；new 与 delete；RAII；Python 的 __init__、__del__ 与上下文管理器。
---

一个对象从诞生到消亡要经历三个阶段：获得存储空间并被初始化，被使用，被清理并释放存储空间。在 C 语言中，初始化和清理都靠程序员记得调用相应的函数，忘记初始化会读到垃圾值，忘记清理会泄漏资源。C++ 的回答是：如何初始化和清理由类的设计者决定，写成构造函数和析构函数；何时初始化和清理由编译器决定，在对象创建和销毁的位置自动插入调用。本章先讲构造函数与析构函数，再讲不同种类的对象在什么时刻被构造和析构，然后讲属于类本身而不属于某个对象的静态成员、不可修改的常量成员、可以访问私有成员的友元，以及动态创建对象的 `new` 与 `delete`。最后讲 C++ 资源管理的核心惯用法 RAII，并与 Python 的上下文管理器对照。对象被复制和移动时发生什么，是 [4.2.6](/4.2.6) 的主题。

## 4.1. 构造函数

### 4.1.1. 构造函数的定义

**定义 4.1.1（构造函数）** 类中与类同名、没有返回类型的特殊成员函数称为**构造函数**。每当创建该类的对象时，编译器自动调用一个构造函数来初始化它。

构造函数可以重载，以支持不同的初始化方式：

```cpp
class Student {
public:
    Student(int id) : id_(id) {}                                // Student s(20240001);
    Student(int year, int order) : id_(year * 10000 + order) {} // Student t(2024, 2);

private:
    int id_;
};
```

构造函数的使命是建立类的**不变式**：构造完成后，对象必须处于合法的状态。如果参数不合法、无法建立不变式，构造函数应当抛出异常，这样就不会存在"半初始化"的对象。

### 4.1.2. 成员初始化列表

上面构造函数中冒号之后、函数体之前的 `id_(id)` 是成员初始化列表。

**定义 4.1.2（成员初始化列表）** 写在构造函数参数列表之后、以冒号开头、形如"成员(初值)"或"成员{初值}"的列表称为**成员初始化列表**，它指定各**数据成员**的初始化方式。

在函数体中给成员赋值也能达到类似效果，但两者有本质区别：进入构造函数体之前，所有成员都已经初始化完毕，函数体里的 `id_ = id;` 是赋值而不是初始化。对 `int` 而言区别不大，但以下成员只能在初始化列表中初始化：

- `const` 数据成员和引用成员：它们只能初始化，不能赋值；
- 没有默认构造函数的类类型成员：不在初始化列表中指定参数就无法构造；
- 基类部分（[4.2.7](/4.2.7)）。

对 `std::string`、`std::vector` 这样的成员，先默认构造再赋值也会多做一次无用功。所以规则很简单：能在初始化列表中初始化的，就在初始化列表中初始化。

成员按照它们在类中声明的顺序初始化，与初始化列表中的书写顺序无关。若写成 `Owner() : second_(2), first_(1) {}`，仍然先构造 `first_`；如果某个成员的初值依赖另一个成员，就必须注意声明顺序。`-Wall` 会对书写顺序与声明顺序不一致的情况给出 `-Wreorder` 警告。

### 4.1.3. 默认成员初始化与委托构造

C++11 起，可以在声明数据成员时直接给出初值，称为默认成员初始化（default member initializer）。若某个构造函数的初始化列表中没有提到该成员，就使用这个初值：

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

一个构造函数还可以在初始化列表中调用同类的另一个构造函数，把工作委托给它，称为委托构造函数（delegating constructor），这样公共的初始化逻辑只写一次：

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

### 4.1.4. 默认构造函数

**定义 4.1.3（默认构造函数）** 不需要实参就能调用的构造函数，即没有参数、或者所有参数都有**默认实参**的构造函数，称为**默认构造函数**。

定义对象而不提供参数时调用默认构造函数。几种写法的区别：

```cpp
Config a;            // default constructor
Config b{};          // default constructor (value-initialization)
Config c = Config(); // default constructor
Config d();          // NOT an object: declares a function d returning Config
Config e[50];        // 50 objects, each default-constructed
```

`Config d();` 被解析为函数声明，这是 C++ 著名的"最令人烦恼的解析"。用花括号初始化可以避免它，花括号还会拒绝**窄化转换**（`int x{3.5};` 是编译错误），因此现代 C++ 倾向于用 `{}` 初始化。

如果类没有声明任何构造函数，编译器会隐式定义一个默认构造函数：它对有默认成员初始化的成员使用该初值，对类类型的成员调用它们的默认构造函数，对内置类型的成员什么都不做。最后一点意味着：

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

全局对象和静态对象在任何构造之前先被零初始化，局部对象则不会；读取未初始化的值在 C++23 及以前是**未定义行为**（C++26 改为"错误行为"，但仍然是错误）。最好的习惯是给每个内置类型的成员都写上默认成员初始化。

一旦声明了任何构造函数，编译器就不再隐式生成默认构造函数。还需要它时，用 `= default` 显式要求编译器生成；反过来，用 `= delete` 可以禁止某种构造方式：

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

被删除的函数仍然参与重载决议，一旦被选中就报错；这正是它的用途：`'c'` 与 `Student(char)` 精确匹配，因而不会悄悄地转换为 `int`。单参数构造函数还会被用于**隐式类型转换**，通常应当声明为 `explicit`（[4.2.6](/4.2.6)）。

## 4.2. 析构函数

**定义 4.2.1（析构函数）** 名为 `~类名`、没有参数也没有返回类型的特殊成员函数称为**析构函数**。对象的**生存期**结束时，编译器自动调用它，以释放对象占有的资源或完成其他收尾工作。

清理一个对象的方式是唯一的、无条件的，所以析构函数没有参数，一个类只有一个析构函数。

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

没有声明析构函数时，编译器隐式定义一个，它依次销毁各个成员。注意"销毁"一个指针成员只是让指针本身消失，不会释放它指向的内存：如果上面的 `IntArray` 不写析构函数，每个对象都会泄漏一块内存。

构造与析构的顺序是对称的：构造时先构造各个成员（按声明顺序），再执行构造函数体；析构时先执行析构函数体，再按与声明相反的顺序销毁各个成员。这保证了析构函数体中所有成员仍然可用。

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

析构函数默认是 `noexcept` 的，不应抛出异常：析构常常发生在异常传播的过程中（§4.7），此时再抛出一个异常会直接终止程序。

## 4.3. 对象的生存期

对象的生存期从构造完成开始，到析构开始时结束。C++ 中对象的存储期（storage duration）有四种，它们决定了构造和析构的时机：

| 存储期 | 哪些对象 | 何时构造 | 何时析构 |
|---|---|---|---|
| 自动 | 局部变量、函数参数 | 执行到定义处 | 离开所在的作用域（`{}` 块）时，按构造的逆序 |
| 静态 | 全局对象、命名空间中的对象、`static` 局部对象、静态数据成员 | 全局对象在 `main` 之前；`static` 局部对象在第一次执行到定义处时 | `main` 返回之后，按构造的逆序 |
| 动态 | 用 `new` 创建的对象 | 执行 `new` 时 | 执行 `delete` 时；忘记 `delete` 就永不析构（泄漏） |
| 线程 | `thread_local` 对象 | 线程开始时或首次使用时 | 线程结束时 |

下面的程序展示了这些规则：

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

几点说明：

- 局部对象按构造的逆序析构，这与栈"后进先出"的性质一致，也保证了后构造的对象可以放心地依赖先构造的对象。
- `static` 局部对象只在第一次执行到定义处时构造（C++11 起这一初始化是线程安全的），离开函数时不析构，下次调用直接使用同一个对象。
- 同一**编译单元**中的全局对象按定义的顺序构造；不同编译单元之间的构造顺序是不确定的。如果一个全局对象的构造函数使用了另一个文件中的全局对象，后者可能尚未构造，这称为静态初始化顺序问题。解决办法之一是把全局对象改成函数中的 `static` 局部对象，在第一次使用时才构造。更好的办法是尽量不用全局对象：它们增加了模块间的耦合，使程序难以测试，通常可以改为通过参数传递。
- 常量对象（`const`）的构造与析构时机与同类的非常量对象相同。
- 表达式中产生的临时对象（如函数返回的对象）在整个表达式求值结束时析构；如果临时对象被绑定到 `const` 引用上，它的生存期延长到与该引用相同（[4.2.6](/4.2.6)）。

按**值传递**的函数参数也是对象：调用 `void fun(A b)` 时，形参 `b` 由实参复制而来（调用拷贝构造函数，[4.2.6](/4.2.6)），函数返回时被析构。于是"构造一次、析构两次"这样的输出并不奇怪，被析构的是两个不同的对象；而当类含有指针成员时，两个对象的析构函数会释放同一块内存，这是 [4.2.6](/4.2.6) 要解决的问题。按**引用传递**（`void fun(const A& b)`）则不创建新对象，也省去了复制的开销。

## 4.4. 静态成员与常量成员

### 4.4.1. 静态数据成员

有些数据属于整个类，而不属于某个对象，例如"当前共有多少个对象""所有对象共用的配置"。

**定义 4.4.1（静态成员）** 用 `static` 声明的数据成员和成员函数称为**静态成员**。静态数据成员由该类的所有对象共享，只有一份，存放在静态存储区；静态成员函数不作用于任何对象，没有 `this` 指针。

静态成员既可以通过类名访问（`Counter::count`），也可以通过对象访问（`c.count`），前者更清楚。静态数据成员具有静态存储期：在 `main` 之前初始化，与是否创建了该类的对象无关。

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

C++17 之前，类内的 `static int alive_;` 只是声明，必须在恰好一个实现文件中写一次定义 `int Counter::alive_ = 0;`；若把定义写进头文件，每个包含它的编译单元都会定义一次，导致链接时重复定义（[4.2.2](/4.2.2)）。C++17 的 `inline` 变量解决了这个问题，`static inline` 成员可以在类内直接初始化，任何类型都可以。`static constexpr` 数据成员隐含 `inline`，用于类级别的编译期常量。旧教材中"只有 `int` 和枚举类型的常量静态成员可以在类内初始化"的规则已经过时。

静态成员函数没有 `this`，因此不能访问非静态成员：非静态成员属于某个具体的对象，而调用静态成员函数时可能根本没有对象。出于同样的原因，静态成员函数不能声明为 `const`。

### 4.4.2. 常量数据成员与常量成员函数

`const` 数据成员在对象的整个生存期中不能修改，因此只能在成员初始化列表或默认成员初始化中赋予初值，不能在构造函数体中赋值。

常量对象的情况更有意思。一个 `const Student` 对象的数据不能改变，那么它能调用哪些成员函数？编译器不分析函数体，而是看函数的声明：

**定义 4.4.2（常量成员函数）** 参数列表之后标有 `const` 的非静态成员函数称为**常量成员函数**。它承诺不修改对象的状态：在函数体中，`this` 的类型是指向常量的指针，修改数据成员或调用非常量成员函数都是编译错误。常量对象（以及通过常量引用、指向常量的指针访问的对象）只能调用常量成员函数。

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

`const` 与非 `const` 版本可以构成重载，因为它们隐含的 `this` 参数类型不同（`Student*` 与 `const Student*`）：非常量对象优先调用非常量版本，常量对象只能调用常量版本。标准库容器大量使用这一点，例如 `std::vector` 的 `operator[]` 对常量对象返回常量引用，对非常量对象返回可修改的引用。

凡是不修改对象的成员函数都应该声明为 `const`，这叫 const 正确性（const correctness）。否则使用者一旦以常量引用传递对象（这是传递对象的标准方式），就无法调用这些函数。少数情况下，某个成员在逻辑上不属于对象的状态（如缓存、互斥锁），可以声明为 `mutable`，允许在常量成员函数中修改。

| 成员 | 在哪里初始化 | 静态成员函数中可访问 | 常量成员函数中可修改 |
|---|---|---|---|
| 普通数据成员 | 初始化列表、默认成员初始化，或在构造函数体中赋值 | 否 | 否（`mutable` 除外） |
| `const` 数据成员 | 初始化列表、默认成员初始化 | 否 | 否 |
| `static` 数据成员 | 类外定义，或类内 `static inline` | 是 | 是（它不属于对象） |
| `static constexpr` 数据成员 | 类内 | 是 | 否 |

## 4.5. 友元

**访问控制**把类的私有成员保护起来，但有时一个非成员函数与类的关系非常紧密，需要直接访问其内部，最典型的是输出运算符 `operator<<`（[4.2.5](/4.2.5)）：它的左操作数是 `std::ostream`，不能写成我们的类的成员函数。

**定义 4.5.1（友元）** 在类中用 `friend` 声明的函数或类称为该类的**友元**，它可以访问该类的所有成员，包括私有成员和受保护成员。

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

友元的性质：

- 友元声明只能出现在类内部，写在 `public` 还是 `private` 区域没有区别；被声明为友元的函数不是该类的成员函数，没有 `this`。
- 友元关系是单向的：`A` 声明 `B` 为友元，`B` 能访问 `A` 的私有成员，反之不行。
- 友元关系不传递（朋友的朋友不是朋友），也不继承（朋友的派生类不是朋友，[4.2.7](/4.2.7)）。
- 一个函数可以同时是多个类的友元；也可以只把另一个类的某个成员函数声明为友元。

友元在一定程度上打破了**封装**，但它是由类自己授予的，仍在类的作者的控制之下，与把成员设为 `public` 有本质区别。它适用于与类紧密配合、逻辑上属于类的接口、却因语法原因不能写成成员的函数，主要就是运算符重载。为了绕过**访问控制**而随意添加友元，说明类的接口设计有问题。

## 4.6. new 与 delete

`new` 在堆上创建对象，它做两件事：分配足够的内存（调用 `operator new`），然后在这块内存上调用构造函数。`delete` 做相反的两件事：调用析构函数，然后释放内存（调用 `operator delete`）。这是它们与 C 的 `malloc`/`free` 的根本区别，后者只分配和释放原始内存，不调用构造函数和析构函数。

```cpp
Tracer* p = new Tracer("one");     // allocate + construct
delete p;                          // destruct + deallocate

Tracer* arr = new Tracer[3]{Tracer("x"), Tracer("y"), Tracer("z")};
delete[] arr;                      // destructs all three elements, in reverse order
```

`new` 与 `delete`、`new[]` 与 `delete[]` 必须配对使用。用 `delete` 释放 `new[]` 得到的数组是**未定义行为**：常见的实现会在数组前额外存放元素个数，`delete[]` 据此对每个元素调用析构函数，而 `delete` 只析构第一个元素，并把错误的地址交给内存释放函数，结果可能是资源泄漏，也可能是程序崩溃。对没有析构函数的类型也许"碰巧没事"，但这不改变它是错误的。

手工管理 `new`/`delete` 很容易出错：忘记 `delete` 导致泄漏，`delete` 两次或之后继续使用导致未定义行为（[4.1.8](/4.1.8)），中途抛出异常时跳过了 `delete`。现代 C++ 的准则是不写裸露的 `new` 和 `delete`：需要动态数组时用 `std::vector`，需要单个动态对象时用 `std::make_unique` 创建由 `std::unique_ptr` 管理的对象（[4.2.12](/4.2.12)）。它们之所以安全，原因就是下一节的 RAII。

## 4.7. RAII

### 4.7.1. 资源获取即初始化

程序要管理的资源远不止内存：文件、网络连接、数据库连接、互斥锁、图形界面的句柄等，都是"获取之后必须归还"的东西。手工管理它们的困难在于，一个函数可能有多个出口：

```cpp
void process(const char* path) {
    std::FILE* fp = std::fopen(path, "r");
    if (!fp) return;
    if (!check_header(fp)) return;       // leak: fp is not closed
    parse(fp);                           // may throw: fp is not closed
    std::fclose(fp);
}
```

每多一个 `return` 或可能抛出异常的调用，就多一个忘记释放的机会。C++ 利用"局部对象离开作用域时析构函数一定会被调用"这一保证，给出了系统的解法。

**定义 4.7.1（RAII）** 把资源的生存期与一个局部对象的生存期绑定：在构造函数中获取资源，在析构函数中释放资源。这一惯用法称为 **RAII**（resource acquisition is initialization，资源获取即初始化）。

无论函数是正常返回、从中途 `return`，还是因异常而退出，局部对象都会被析构。异常沿**调用栈**向外传播时，沿途每个**栈帧**中已构造的局部对象都按逆序析构，这称为栈展开（stack unwinding）。因此，用 RAII 对象持有的资源一定会被释放，不需要在每个出口重复清理代码。

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

注意第二次调用中，"closed" 在 "error" 之前输出：异常离开 `save` 时，`f` 已经被析构，文件已经关闭，然后 `main` 中的 `catch` 才开始执行。构造函数在无法打开文件时抛出异常，于是任何 `File` 对象都持有一个有效的文件，不存在"打开失败的 `File`"这种状态，使用者无需再检查。

### 4.7.2. 标准库中的 RAII

RAII 是 C++ 标准库的设计基础，几乎所有管理资源的类型都遵循它：

| 资源 | RAII 类型 | 释放时机 |
|---|---|---|
| 动态数组、字符串 | `std::vector`、`std::string` | 析构时释放内存（[4.2.10](/4.2.10)） |
| 单个动态对象 | `std::unique_ptr`、`std::shared_ptr` | 析构时（最后一个所有者析构时）`delete` 对象（[4.2.12](/4.2.12)） |
| 文件 | `std::ifstream`、`std::ofstream` | 析构时关闭文件（[4.2.11](/4.2.11)） |
| 互斥锁 | `std::lock_guard`、`std::scoped_lock`、`std::unique_lock` | 析构时解锁 |
| 线程 | `std::jthread`（C++20） | 析构时请求停止并等待线程结束 |

由此得到现代 C++ 资源管理的原则：每个资源都立即交给一个拥有它的对象管理；类的数据成员优先使用这些 RAII 类型，这样类本身往往根本不需要写析构函数（[4.2.6](/4.2.6) 的零法则）。

## 4.8. Python 对照

### 4.8.1. \_\_init\_\_ 与 \_\_new\_\_

Python 中创建对象 `Student(42)` 也分两步：`__new__` 分配并返回一个新对象，`__init__` 初始化它。通常只需要定义 `__init__`，它相当于构造函数，在其中给 `self` 的属性赋值即创建了这些属性。Python 没有构造函数重载，不同的构造方式用默认参数或类方法实现；类方法是作用于类本身的方法，常用作"另一种构造函数"。Python 的类属性对应 C++ 的静态数据成员，`@staticmethod` 对应静态成员函数。

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

### 4.8.2. 没有确定的析构

Python 有 `__del__` 方法，但它不是 C++ 意义上的析构函数。CPython 用引用计数管理内存：对象的引用计数降为零时立即回收，此时会调用 `__del__`；但如果对象处在循环引用中，要等**垃圾回收**器发现它们，时间不确定；解释器退出时仍存活的对象，`__del__` 甚至不保证被调用；其他 Python 实现（如 PyPy）不使用引用计数，回收时间更不确定。因此不能依靠 `__del__` 释放资源。

### 4.8.3. 上下文管理器与 with

Python 管理资源的方式是 `with` 语句。

**定义 4.8.1（上下文管理器）** 实现了 `__enter__` 和 `__exit__` 两个方法的对象称为**上下文管理器**。`with` 语句进入代码块时调用 `__enter__`（其返回值绑定到 `as` 后的名字），离开代码块时无论是正常结束还是因异常退出，都调用 `__exit__`。

`with` 与 RAII 解决的是同一个问题：把资源的释放与一个代码块的结束绑定在一起。区别在于，C++ 中这种绑定对每个局部对象都自动成立，Python 中需要显式写出 `with`。

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

`__exit__` 的三个参数描述了代码块中发生的异常（没有异常时都是 `None`），返回真值表示异常已被处理、不再向外传播。实际上，内置的 `open` 返回的文件对象本身就是上下文管理器，应当直接写 `with open(path) as f:`；标准库中的锁（`threading.Lock`）、临时目录（`tempfile.TemporaryDirectory`）、数据库连接等也都支持 `with`。自己写上下文管理器时，更简便的方法是用 `contextlib.contextmanager` 装饰一个生成器函数，`yield` 之前的代码相当于 `__enter__`，之后的代码（放在 `finally` 中）相当于 `__exit__`：

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

## 小结

- 构造函数在对象创建时自动调用，负责建立不变式；成员应在初始化列表中初始化，初始化顺序是声明顺序。没有声明任何构造函数时编译器生成默认构造函数；`= default` 与 `= delete` 显式要求或禁止某个特殊成员函数。
- 析构函数在对象生存期结束时自动调用；构造先成员后函数体，析构先函数体后成员，顺序对称。
- 局部对象离开作用域时按逆序析构；全局与静态对象在 `main` 前后构造与析构，跨编译单元的初始化顺序不确定；动态对象由 `new` 创建、`delete` 销毁，二者必须配对。
- 静态成员属于整个类，静态成员函数没有 `this`；C++17 的 `static inline` 允许在类内定义静态数据成员。常量成员函数承诺不修改对象，常量对象只能调用它们。
- 友元由类授予访问权，单向、不传递、不继承，主要用于运算符重载。
- RAII 把资源绑定到对象的生存期，在任何退出路径上都能释放资源，是 C++ 资源管理的基础；Python 用上下文管理器和 `with` 达到同样的目的，不应依赖 `__del__`。
