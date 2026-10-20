---
title: 函数对象、lambda 与智能指针
description: 函数指针与函数对象；lambda 表达式、捕获与闭包、泛型 lambda；std::function 与回调；裸指针的问题与所有权；unique_ptr、shared_ptr 与引用计数、weak_ptr 与循环引用；Python 的一等函数、闭包、引用计数与垃圾回收。
---

本章讨论两个看似无关、实则都关于"把行为和资源包装成对象"的主题。前半章讲怎样把函数当作值来传递：函数指针、可以携带状态的函数对象、就地定义函数的 lambda 表达式，以及能装下这一切的 `std::function`。它们让第 10 章的算法可以接受自定义的比较与谓词，也是第 13 章策略模式的轻量写法。后半章讲智能指针：用类模板把"谁负责释放这块内存"写进类型里，让动态分配的对象像局部对象一样自动释放。它是 **RAII**（[4.2.4](/4.2.4)）与**移动语义**（[4.2.6](/4.2.6)）在内存管理上的直接应用，现代 C++ 代码中几乎不再需要手写 `delete`。

## 12.1. 函数作为值

### 12.1.1. 函数指针

函数在内存中也有地址，可以保存在函数指针中、作为参数传递。函数指针的类型由返回类型和参数类型决定，例如 `bool (*)(const Student&, const Student&)`；用 `using` 起别名更易读。C 的 `qsort` 和许多回调接口都以函数指针为参数，调用者借此把"怎样比较""事件发生时做什么"交给被调用的函数决定。

函数指针的局限是它只能指向一个固定的函数，不能携带额外的数据：想要"分数不低于某个阈值"的谓词，阈值只能放在全局变量里。

### 12.1.2. 函数对象

**定义 12.1.1（函数对象）** 重载了函数调用运算符 `operator()` 的类的对象，可以像函数一样被调用，称为**函数对象**（function object，又称仿函数 functor）。

函数对象是普通的对象，可以用数据成员保存状态（如阈值），由构造函数设置。它还有性能上的好处：每个函数对象类是一个不同的类型，算法模板以它为模板实参实例化时，编译器知道确切调用的是哪个 `operator()`，可以内联；而通过函数指针调用通常无法内联。标准库在 `<functional>` 中提供了 `std::less`、`std::greater`、`std::plus` 等现成的函数对象。

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

## 12.2. lambda 表达式

### 12.2.1. 语法

为了传给 `count_if` 一个"分数不低于 90"的谓词而专门写一个类，显得繁琐。C++11 的 lambda 表达式让我们在使用处直接写出函数对象。

**定义 12.2.1（lambda 表达式）** 形如 `[捕获列表](参数列表) -> 返回类型 { 函数体 }` 的表达式称为 **lambda 表达式**，它定义一个匿名的函数对象。编译器为每个 lambda 表达式生成一个唯一的、没有名字的类（闭包类型），其 `operator()` 的函数体就是 lambda 的函数体；求值 lambda 表达式得到这个类的一个对象（闭包对象）。

返回类型能由 `return` 语句推导时可以省略，没有参数时参数列表 `()` 也可以省略。上一节的 `AtLeast(90)` 可以写成 `[](const Student& s) { return s.score >= 90; }`。lambda 的类型没有名字，要保存它时用 `auto`。

### 12.2.2. 捕获与闭包

lambda 的函数体只能直接使用它的参数、全局变量和静态变量；要用外层函数中的局部变量，必须在捕获列表中写明：

| 捕获 | 含义 |
|---|---|
| `[x]` | 按值捕获 `x`：创建闭包时复制一份，此后外部的 `x` 变化不影响它 |
| `[&x]` | 按引用捕获 `x`：闭包中使用的就是外部的 `x` |
| `[=]`、`[&]` | 按值、按引用隐式捕获函数体中用到的所有局部变量 |
| `[this]`、`[*this]` | 捕获当前对象的指针、当前对象的副本 |
| `[y = expr]` | 初始化捕获（C++14）：用表达式初始化一个新的成员，例如 `[p = std::move(p)]` 移入只能移动的对象 |

按值捕获的变量在闭包中默认是 `const` 的，要修改它的副本须把 lambda 声明为 `mutable`。

**定义 12.2.2（闭包）** 一个函数连同它所引用的外层作用域中的变量（它的环境）一起构成的实体，称为**闭包**（closure）。C++ 中求值 lambda 表达式得到的闭包对象就是闭包：被捕获的变量成为该对象的数据成员。

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

按引用捕获最大的危险是悬垂：闭包比被捕获的局部变量活得更久时（例如把闭包作为返回值、保存到容器中、交给另一个线程），它引用的变量已经销毁。例如函数中 `int n = 0; return [&n] { return ++n; };` 返回的闭包引用了已销毁的局部变量 `n`，调用它是未定义行为。规则是：闭包只在当前作用域内同步使用时（如传给 `std::sort`）才按引用捕获；要保存或返回的闭包按值捕获。隐式的 `[=]` 在成员函数中只捕获了 `this` 指针而不是成员的副本，同样可能悬垂，C++20 起弃用了经由 `[=]` 隐式捕获 `this` 的写法，应当显式写出 `[this]` 或 `[*this]`。

### 12.2.3. 泛型 lambda

参数类型写成 `auto` 的 lambda（C++14）称为泛型 lambda，它的 `operator()` 是一个成员函数模板（第 9 章），可以接受不同类型的实参，例如 `[](const auto& a, const auto& b) { return a.size() < b.size(); }` 可以比较任何有 `size()` 的对象。C++20 还允许写出模板参数并加约束：`[]<std::integral T>(T x) { return x * 2; }`。

## 12.3. std::function 与回调

函数指针、函数对象、lambda 都是可调用对象，但类型各不相同：每个 lambda 的类型甚至没有名字。要把它们存进同一个容器、作为类的数据成员，或者作为非模板函数的参数，需要一个能装下"任何签名相同的可调用对象"的类型，这就是 `std::function<R(Args...)>`。

下面是一个简单计算器：读入、计算、输出三个步骤各有多种实现，`process` 函数用 `std::function` 接受任意组合。它与第 13 章基于继承的模板方法模式解决的是同一个问题，但不需要定义任何基类。

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

`std::function` 内部用**类型擦除**（第 9 章）实现：它保存可调用对象的一份副本，通过一次间接调用转发，较大的可调用对象还需要堆分配。因此三种传递可调用对象的方式各有适用场合：

| 方式 | 能接受 | 开销 | 适用 |
|---|---|---|---|
| 函数指针 | 普通函数、不捕获的 lambda | 间接调用 | 与 C 接口交互 |
| 模板参数 `template <typename F>`（可用 `std::invocable` 约束） | 任何可调用对象 | 无，可内联 | 算法、调用后立即返回的函数 |
| `std::function` | 任何签名相符的可调用对象 | 间接调用，可能堆分配 | 需要保存的回调：事件处理器、类的成员、容器元素 |

C++23 增加了 `std::move_only_function`，可以保存只能移动的可调用对象（例如捕获了 `unique_ptr` 的 lambda）。

## 12.4. 智能指针

### 12.4.1. 所有权与裸指针的问题

`new` 出来的对象必须恰好 `delete` 一次。用裸指针管理时，这一责任完全靠程序员记住，常见的错误有：忘记 `delete`（**内存泄漏**）；`delete` 两次；`delete` 之后继续使用（**悬垂指针**）；在 `new` 与 `delete` 之间抛出异常或提前 `return`，`delete` 被跳过。根本的困难在于裸指针 `T*` 的类型没有说明所有权：拿到一个指针，无从得知自己是否应当释放它。

**定义 12.4.1（智能指针）** 拥有一个动态分配的对象、在自身析构时按所有权规则自动释放该对象，并重载 `*`、`->` 使其用法与指针相同的类模板对象，称为**智能指针**（smart pointer）。

智能指针是 RAII 的应用：把释放写进析构函数，无论正常结束、提前返回还是异常，对象都会被释放。C++ 标准库在 `<memory>` 中提供三种智能指针，分别表达三种所有权关系。

### 12.4.2. unique_ptr：独占所有权

`std::unique_ptr<T>` 独占它所指的对象：同一时刻只有一个 `unique_ptr` 拥有该对象，它析构时释放对象。它不能复制（**拷贝构造函数**被删除），只能移动，移动后原来的 `unique_ptr` 变为空，所有权的转移在代码中一目了然。使用默认删除器时，它不比裸指针多占空间，也没有运行时开销，是动态分配对象的默认选择。

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

用 `std::make_unique<T>(args...)` 创建对象，而不要写 `std::unique_ptr<T>(new T(args...))`：前者不会出现裸 `new`，也更简洁。`unique_ptr` 可以放进容器，第 8 章的 `std::vector<std::unique_ptr<Shape>>` 就用它保存多态对象；`std::unique_ptr<T[]>` 管理动态数组（一般用 `vector` 更好）；还可以指定自定义的删除器，用来管理文件句柄等非内存资源。

### 12.4.3. shared_ptr 与引用计数

有时一个对象确实被多处共同拥有，无法确定谁最后使用它，例如被多个窗口共享的文档、缓存中的数据。

**定义 12.4.2（引用计数）** 为每个被共享的对象维护一个计数器，记录当前有多少个所有者引用它：新增一个所有者时加一，一个所有者放弃时减一，计数降为零时释放对象。这种内存管理方式称为**引用计数**（reference counting）。

`std::shared_ptr<T>` 用引用计数实现共享所有权：复制 `shared_ptr` 使计数加一，析构或重新赋值使计数减一，最后一个 `shared_ptr` 消失时对象被释放。计数器存放在单独分配的控制块中，所有指向同一对象的 `shared_ptr` 共享这个控制块；`std::make_shared` 把对象与控制块放在一次分配中，应当优先使用。计数的增减是原子操作，多个线程同时复制不同的 `shared_ptr` 是安全的，但这也使复制 `shared_ptr` 比复制裸指针慢得多，所以只读地使用对象的函数应当接受 `T&` 或 `const T&`，而不是按值接受 `shared_ptr`。

引用计数的原理可以用几十行代码说明。下面是一个极简的 `SharedPtr`，只演示计数的维护（没有线程安全、移动操作与 `weak_ptr` 支持），复制控制的写法见 [4.2.6](/4.2.6)：

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

使用 `shared_ptr` 时要避免从同一个裸指针构造两个 `shared_ptr`：它们会各建一个控制块，对象被释放两次。类的成员函数需要得到指向自身的 `shared_ptr` 时，让类继承 `std::enable_shared_from_this<T>` 并调用 `shared_from_this()`。

### 12.4.4. weak_ptr 与循环引用

引用计数有一个固有的缺陷：如果对象之间的 `shared_ptr` 形成环，例如双向链表中前后结点互相拥有，那么即使外部已经没有任何指针指向它们，环中每个对象的计数也至少是 1，永远不会被释放。

`std::weak_ptr<T>` 指向由 `shared_ptr` 管理的对象，但不参与所有权、不增加计数。对象可能已被释放，因此不能直接通过 `weak_ptr` 访问，要先调用 `lock()`：对象还在时得到一个有效的 `shared_ptr`（访问期间保证对象存活），已释放时得到空指针。把环中"反向"的那条边改成 `weak_ptr`，环就被打破了：

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

如果把 `prev` 也写成 `shared_ptr`，`a` 的计数就是 2，`main` 结束后两个结点的计数都停在 1，析构函数一个也不会运行。树中子结点指向父结点的指针、观察者列表、缓存都是 `weak_ptr` 的典型用途。

### 12.4.5. 使用原则

| 情形 | 用什么 |
|---|---|
| 动态分配的对象，所有者唯一（默认） | `std::unique_ptr`，用 `std::make_unique` 创建 |
| 确实有多个所有者、无法确定谁最后使用 | `std::shared_ptr`，用 `std::make_shared` 创建 |
| 需要引用一个共享对象但不拥有它（反向指针、观察者、缓存） | `std::weak_ptr` |
| 函数只是使用对象，不涉及所有权 | `T&`、`const T&`，可以为空时用 `T*` |
| 函数要接管所有权 | 按值接受 `std::unique_ptr<T>` |

在这套约定下，代码中出现的裸指针只表示"不拥有"，`new` 与 `delete` 只出现在底层的数据结构实现中。

## 12.5. Python 对照

### 12.5.1. 一等函数

Python 的函数是一等对象：可以赋给变量、存进容器、作为参数传递、作为返回值。因此 Python 不需要函数指针，也很少需要 `std::function` 这样的包装：`sorted(v, key=len)`、`map(str.upper, words)` 直接传入函数即可。`lambda` 定义匿名函数，但函数体只能是一个表达式，复杂的逻辑应当写成有名字的 `def`。定义了 `__call__` 的类的实例可以像函数一样调用，相当于 C++ 的函数对象。标准库的 `operator` 模块（`attrgetter`、`itemgetter`、`add`）对应 `<functional>` 中的现成函数对象，`functools.partial` 固定函数的部分参数，相当于一个捕获了参数的 lambda。

### 12.5.2. 闭包与 nonlocal

嵌套函数可以使用外层函数的局部变量，外层函数返回后这些变量依然存在，内层函数连同它们构成闭包。与 C++ 的按值捕获不同，Python 闭包捕获的是变量本身（相当于按引用捕获，但变量的生存期被延长，不会悬垂），读取的是调用时变量的当前值。内层函数要给外层变量重新赋值，须声明 `nonlocal`。

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

（Python 版第二行输出 `2 2 2`，第三行输出 `0 1 2`。）循环中创建的 Python 闭包都引用同一个循环变量，调用时它已经是最后的值，这是 Python 中最常见的闭包陷阱；用默认参数在创建时求值即可修正。Python 的装饰器就是以函数为参数、返回闭包的函数，第 13 章会把它与装饰器模式对照。

### 12.5.3. 引用计数与垃圾回收

Python 程序员不写 `delete`，但对象的释放机制与 `shared_ptr` 一脉相承：CPython 中每个对象都带有引用计数，每多一个名字、容器元素或属性引用它就加一，计数降为零时立即释放。这使得对象的释放时机大体可以预期，但同样无法处理循环引用，所以 CPython 另有**垃圾回收**机制：一个分代的回收器（`gc` 模块），定期找出不可达的引用环并回收。标准库 `weakref` 提供不增加计数的弱引用，对应 `weak_ptr`：

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

（`sys.getrefcount` 的具体数值依赖解释器的实现与版本。）与 C++ 相比，Python 的代价是每个对象都要维护计数、程序要偶尔停下来做环检测；收益是程序员几乎不必考虑所有权。理解引用计数仍然有用：大对象之所以没有被释放，往往是因为某个容器、缓存或闭包还引用着它。

## 小结

- 函数指针只能指向固定的函数；函数对象可以携带状态，并且便于编译器内联。
- lambda 表达式就地定义函数对象，捕获列表决定闭包怎样保存外层变量；要保存或返回的闭包按值捕获，以免悬垂。
- `std::function` 用类型擦除装下任意签名相符的可调用对象，适合需要保存的回调；算法类函数用模板参数接受可调用对象。
- 智能指针把所有权写进类型：`unique_ptr` 独占、零开销，是默认选择；`shared_ptr` 用引用计数共享所有权；`weak_ptr` 不拥有对象，用来打破循环引用。
- Python 的函数是一等对象，闭包捕获变量本身；CPython 用引用计数加环检测管理内存，`weakref` 对应 `weak_ptr`。
