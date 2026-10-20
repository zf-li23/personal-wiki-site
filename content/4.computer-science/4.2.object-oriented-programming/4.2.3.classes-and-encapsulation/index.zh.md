---
title: 类与封装
description: 函数重载与重载决议、默认实参、nullptr；auto 与 decltype 类型推导；类、数据成员与成员函数；接口与实现的分离；public、private 与访问控制；this 指针；内联函数与宏；Python 的类、命名约定、property 与类属性。
---

[4.2.1](/4.2.1) 说明了为什么需要**封装**，本章讲 C++ 用什么机制实现**封装**：类。类是用户定义的类型，它把数据成员和成员函数组合在一起，用访问控制把接口与实现分开。在进入类之前，先补充几项让函数和变量的写法更灵活的语言机制：函数重载让"名字相同、含义不同"的操作共用一个名字，这也是后面[运算符重载](/4.2.5)和构造函数重载的基础；`auto` 与 `decltype` 让编译器推导类型。最后介绍成员函数中隐含的 `this` 指针和内联函数，并对照 Python 的类：它的封装依靠约定而不是编译器。对象怎样被创建和销毁，是[下一章](/4.2.4)的主题。

## 3.1. 函数重载与默认实参

### 3.1.1. 函数重载

同一个任务常常需要接受不同类型的输入：求两个 `int` 的和与求两个 `double` 的和；把一条消息输出到屏幕、文件或网络。如果每种情形都要另起一个名字（`sum_int`、`sum_double`），使用者就得记住一堆名字，而它们在概念上是同一件事。

**定义 3.1.1（函数重载）** 在同一作用域中声明多个名字相同而参数列表（参数的个数或类型）不同的函数，称为**函数重载**。调用时，编译器根据实参的类型从中选出最合适的一个，这一过程称为重载决议。

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

重载的函数必须在参数列表上有所区别；只有返回类型不同不构成重载。原因很简单：调用 `f(3)` 时只看得到实参，如果 `int f(int)` 与 `double f(int)` 同时存在，编译器无从选择。参数名不同也不构成重载。

重载决议大致按以下优先次序比较每个候选函数：精确匹配（包括数组到指针等平凡转换、添加 `const`）优于类型提升（如 `char`、`short` 到 `int`，`float` 到 `double`），类型提升优于其他标准转换（如 `int` 与 `double` 互转、`double` 到 `float`），标准转换优于用户定义的转换（[4.2.6](/4.2.6)）。若最好的候选不唯一，调用就是二义的，编译失败：

```cpp
void print(int x);
void print(float x);

print(1.0f);  // float: exact match -> print(float)
print(1);     // int: exact match -> print(int)
print(1.7);   // double: converting to int and to float are both standard conversions
              // -> error: call of overloaded 'print(double)' is ambiguous
```

如果只有 `print(int)`，`print(1.7)` 会把 1.7 转换为 `int`，即向零取整得 1，`print(-3.9)` 得 -3。这种隐式的**窄化转换**会悄悄丢失信息，`-Wconversion` 选项会对它发出警告。

### 3.1.2. 空指针 nullptr

C++11 之前，空指针写作 `0` 或宏 `NULL`。`NULL` 是一个整数常量（在 GCC 中是特殊的 `__null`），这在重载时会出问题：

```cpp
void f(int);
void f(int* p);

f(0);        // calls f(int), although 0 was meant as a null pointer
f(NULL);     // f(int) or ambiguous, depending on the compiler; never f(int*)
f(nullptr);  // calls f(int*)
```

`nullptr` 的类型是 `std::nullptr_t`，它可以转换为任何指针类型，但不能转换为整数，因此总是匹配指针参数。现代 C++ 中一律用 `nullptr` 表示空指针。

### 3.1.3. 默认实参

**定义 3.1.2（默认实参）** 函数声明中为参数指定的值称为**默认实参**（也称缺省参数）；调用时若省略了对应的实参，编译器自动用该值补上。

```cpp
void print(const std::string& name, int score = 0, const std::string& msg = "pass");

print("Alice");             // print("Alice", 0, "pass")
print("Bob", 95);           // print("Bob", 95, "pass")
print("Carol", 59, "fail");
```

规则：带默认值的参数必须位于参数列表的末尾，因为调用时实参从左到右依次对应形参，只能省略尾部的若干个；默认值只在一处声明中给出，通常是**头文件**中的声明，实现文件中的定义不再重复。默认实参与重载结合时可能产生二义：

```cpp
void fun(int a, int b = 1);
void fun(int a);

fun(1, 2);  // OK: only fun(int, int) accepts two arguments
fun(2);     // error: both candidates accept one argument
```

### 3.1.4. Python 对照

Python 不支持按参数类型重载：同一作用域中后定义的同名函数会覆盖先定义的。它用另外几种机制满足同样的需求：默认参数与关键字参数、可变参数 `*args` 与 `**kwargs`、在函数内部检查类型，以及标准库的 `functools.singledispatch`（按第一个参数的类型分派）。

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

Python 的默认值在函数定义时求值一次，并被所有调用共享；如果默认值是列表这样的可变对象，一次调用对它的修改会延续到下一次调用。惯用写法是用 `None` 作默认值，在函数体内再创建新对象。

## 3.2. 类型推导：auto 与 decltype

### 3.2.1. auto

用 `auto` 声明变量时，编译器根据初始化表达式推导变量的类型。它的主要用途是省去冗长而又显然的类型名，例如容器的迭代器类型 `std::map<std::string, int>::const_iterator`。

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

`auto` 的要点：

- `auto` 变量必须初始化，类型在编译期确定，此后不再改变；它不是"**动态类型**"。
- 推导时去掉引用和顶层 `const`：`auto a = r;` 得到一份拷贝。需要引用时写 `auto&` 或 `const auto&`，这在范围 `for` 循环中尤其重要：`for (auto x : v)` 复制每个元素，`for (const auto& x : v)` 只读而不复制，`for (auto& x : v)` 可以修改元素。
- 字符串字面量推导为 `const char*`，不是 `std::string`；需要 `std::string` 时写 `std::string s = "abc";` 或使用字面量后缀 `"abc"s`。
- 函数的返回类型可以写 `auto`，由 `return` 语句推导（C++14）。
- 从 C++20 起，函数参数也可以写 `auto`，这样的函数是简写的函数模板（[4.2.9](/4.2.9)）：`sum(1, 2)` 与 `sum(1, 2.5)` 实例化出两个不同的函数。在 C++20 之前参数不能声明为 `auto`。

### 3.2.2. decltype

`decltype(e)` 给出表达式 `e` 的类型而不求值。对一个变量名，它给出该变量的声明类型（保留引用和 `const`）；对加了括号的左值表达式 `(i)`，它给出引用类型 `int&`。`decltype` 主要用于泛型代码中表达"与某个表达式相同的类型"，例如尾置返回类型：

```cpp
template <typename T, typename U>
auto multiply(T x, U y) -> decltype(x * y) {  // C++11 style; since C++14 "auto" alone suffices
    return x * y;
}
```

`auto f(...) -> R` 是尾置返回类型的写法，返回类型写在参数列表之后，因而可以引用参数。

## 3.3. 类与对象

### 3.3.1. 类的定义

**定义 3.3.1（类）** **类**是用户定义的类型，它把描述对象状态的数据和操作这些数据的函数组合在一起。类中的数据称为**数据成员**（成员变量），类中的函数称为**成员函数**。用类定义的变量称为该类的对象或实例。

类 = 属性（数据）+ 服务（函数）。下面的栈（[4.3.4](/4.3.4)）把一个 `std::vector<int>` 作为内部存储，对外只提供栈的操作：

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

用"对象名`.`成员名"访问对象的成员，通过指针访问时用"指针`->`成员名"。成员函数必须在类内声明，定义可以写在类内，也可以写在类外；写在类外时要用 `类名::` 限定，说明它属于哪个类。成员函数参数列表后的 `const` 表示该函数不修改对象，是常量成员函数（[4.2.4](/4.2.4)）。

`struct` 和 `class` 都能定义类，唯一的区别是默认访问权限：`struct` 的成员默认是 `public` 的，`class` 默认是 `private` 的。习惯上，只是把几个数据打包在一起、没有需要维护的**不变式**的类型用 `struct`（如 `struct Point { double x, y; };`），有封装需求的用 `class`。

### 3.3.2. 接口与实现的分离

在多文件程序中（[4.2.2](/4.2.2)），类的定义（包括成员函数的声明）放在**头文件**中，成员函数的定义放在实现文件中，一般每个类一对文件：

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

使用者只需要读头文件中的 `public` 部分就知道这个类能做什么。不过 C++ 的头文件并没有完全隐藏实现：私有数据成员也写在头文件里，因为编译器需要知道对象的大小才能在使用者的代码中创建对象。修改私有成员仍会迫使所有包含该头文件的源文件重新编译；需要彻底隔离时可以使用 Pimpl 惯用法（头文件中只保留一个指向实现类的指针，[4.2.12](/4.2.12)）。

## 3.4. 访问控制

### 3.4.1. public 与 private

**定义 3.4.1（访问控制）** 类的成员按照可以在何处被访问分为几组，这一机制称为**访问控制**。C++ 有三种访问说明符：

- `public`：公有成员，任何代码都可以访问，它们构成类的接口；
- `private`：私有成员，只有该类的成员函数和友元（[4.2.4](/4.2.4)）可以访问，它们是类的实现；
- `protected`：受保护成员，除本类外，派生类也可以访问（[4.2.7](/4.2.7)）。

```cpp
Stack s;
s.push(1);           // OK: push is public
s.data_.clear();     // error: 'std::vector<int> Stack::data_' is private within this context
```

访问控制是按类而不是按对象检查的：一个成员函数可以访问同类的其他对象的私有成员。

```cpp
class Stack {
public:
    bool same_as(const Stack& other) const { return data_ == other.data_; }  // OK
    // ...
private:
    std::vector<int> data_;
};
```

访问控制在编译期检查，不产生任何运行时开销；它防止的是无意的误用，而不是恶意的破坏（用指针强行改写对象的内存仍然可以做到）。它与重载决议互不相干：编译器先做重载决议选出函数，再检查它能否访问。因此，一个私有的重载版本仍然会参与竞争，可能使类外的调用产生二义，或者被选中后因无权访问而报错。

### 3.4.2. 设计接口

把数据成员设为 `private`、通过成员函数访问，是封装的基本做法。但这并不意味着为每个数据成员都写一对 `get`/`set` 函数：那样做只是绕了一个弯把数据公开，类无法维护任何不变式。好的接口按使用者需要的操作来设计，而不是按内部数据来设计。比较：

| 按数据设计 | 按操作设计 |
|---|---|
| `set_balance(double)`、`get_balance()` | `deposit(double)`、`withdraw(double)`、`balance()` |
| 使用者自己检查余额是否足够 | 规则写在 `withdraw` 内部，只写一次 |
| 改用以分为单位的整数存储，所有调用者都要改 | 内部表示可以随意更换 |

一个实用的检验标准：如果类的每个数据成员都可以被任意赋值而不破坏任何规则，那么它可能根本不需要封装，用 `struct` 即可。

## 3.5. this 指针

成员函数与普通函数的重要区别在于：它总是作用在某个对象上。调用 `s.push(1)` 时，`push` 怎么知道要修改的是 `s` 的 `data_`？答案是每个非静态成员函数都有一个隐含的参数 `this`，它是指向调用该函数的对象的指针。`s.push(1)` 大致相当于 `Stack::push(&s, 1)`，函数体中的 `data_` 是 `this->data_` 的简写。在常量成员函数中，`this` 的类型是 `const Stack*`，因此不能通过它修改成员。

显式使用 `this` 的常见场合：参数名与成员名相同时区分二者；把当前对象作为参数传给其他函数；返回 `*this` 以支持链式调用。

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

Python 把这个隐含参数写了出来：方法的第一个参数（习惯命名为 `self`）就是调用它的对象，`a.f(x)` 等价于 `A.f(a, x)`。C++23 也允许显式写出这个参数，称为显式对象参数（"deducing this"）：`void f(this Stack& self)`，它主要用于简化模板代码。

## 3.6. 内联函数

函数调用有固定的开销：传递参数、跳转、建立**栈帧**、返回。对 `max`、`top()` 这样只有一行的函数，调用开销可能比函数体本身还大。内联是一种优化：编译器把函数体直接展开到调用处，省去调用，并为进一步优化创造机会。

**定义 3.6.1（内联函数）** 用 `inline` 声明、或在类定义内部定义的函数称为**内联函数**。内联函数可以在多个**编译单元**中各定义一次（各个定义必须相同），因此可以把定义写在头文件中。

```cpp
inline int max(int a, int b) { return a > b ? a : b; }

class Stack {
public:
    bool empty() const { return data_.empty(); }  // defined in the class: implicitly inline
    // ...
};
```

关于 `inline` 需要澄清一个常见误解。是否真正展开一次调用，完全由编译器决定：它会拒绝展开过大或递归的函数，也会主动展开没有标 `inline` 的小函数（尤其在 `-O2` 下）。现代 C++ 中 `inline` 关键字的实际作用是放宽**单一定义规则**（[4.2.2](/4.2.2)），允许定义出现在头文件中；而要让编译器能够展开一个函数，它的定义也恰恰需要在调用处可见。所以短小的、频繁调用的函数（如简单的访问函数）通常直接定义在类内，较大的函数在实现文件中定义。滥用内联会让每个调用处都复制一份函数体，使代码膨胀。

内联函数是带参数的**宏**的类型安全替代（[4.2.2](/4.2.2)）：

| | 宏 `#define MAX(a, b) ((a) > (b) ? (a) : (b))` | 内联函数 `inline int max(int a, int b)` |
|---|---|---|
| 处理阶段 | 预处理，文本替换 | 编译，是真正的函数 |
| 类型检查 | 无 | 有 |
| 参数求值 | `MAX(a++, b)` 中 `a++` 可能求值两次 | 每个实参恰好求值一次 |
| 作用域与访问控制 | 无，不能作为类的成员 | 遵守作用域，可以是成员函数，能访问私有成员 |
| 调试 | 调试器看不到宏 | 未优化时与普通函数一样可以单步调试 |

需要对多种类型通用时，用函数模板（[4.2.9](/4.2.9)）代替 `MAX` 宏；标准库已经提供了 `std::max`。

## 3.7. Python 对照：类与封装

### 3.7.1. 类的定义与命名约定

Python 的 `class` 语句也定义一个新类型，但实例的数据属性不需要事先声明，在 `__init__` 中赋值即创建（`__init__` 的作用见 [4.2.4](/4.2.4)）。Python 没有访问说明符，封装依靠命名约定：

| 写法 | 含义 |
|---|---|
| `name` | 公开属性 |
| `_name` | 约定为内部使用；外部代码可以访问，但不应依赖它 |
| `__name` | 名称改写：在类 `A` 中被改写为 `_A__name`，主要用于避免与子类的属性重名，并非真正的私有 |
| `__name__` | 语言定义的特殊名字（如 `__init__`、`__len__`，[4.2.5](/4.2.5)），不要自己发明 |

Python 社区的态度是"我们都是成年人"：约定已经足够表明意图，语言不阻止使用者有意绕过它。

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

Java 风格的 `get_x()`/`set_x()` 在 Python 中不常见。惯用做法是先直接公开属性；以后需要在读写时计算或检查，再用 `@property` 把它改成方法，而使用者的代码 `obj.x`、`obj.x = v` 无须改动。C++ 没有这种机制，因此在 C++ 中一开始就要通过成员函数访问数据。

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

### 3.7.3. 类属性与实例属性

在 `class` 语句体中直接赋值的名字是类属性，由类和它的所有实例共享，相当于 C++ 的静态数据成员（[4.2.4](/4.2.4)）；通过 `self.x = ...` 赋值的是实例属性，每个对象各有一份。读取 `obj.x` 时先查实例，再查类；但通过实例赋值总是创建或修改实例属性，于是会遮蔽同名的类属性：

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

只是存放数据的简单类可以用标准库的 `dataclasses.dataclass` 自动生成 `__init__`、`__repr__` 和 `__eq__`，相当于 C++ 中的 `struct`：

```python
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


p = Point(1.0, 2.0)
print(p, p == Point(1.0, 2.0))  # Point(x=1.0, y=2.0) True
```

## 小结

- 函数重载让同一名字表示参数不同的一组函数，由重载决议按精确匹配、提升、转换的次序选择；返回类型不参与区分。默认实参只能位于末尾，只在声明中给出一次。空指针用 `nullptr`。
- `auto` 在编译期推导类型，去掉引用与顶层 `const`；需要引用时写 `auto&`、`const auto&`。C++20 起参数也可以写 `auto`。
- 类 = 数据成员 + 成员函数；`public` 成员构成接口，`private` 成员是实现，访问控制按类检查、在编译期执行。接口应按操作而不是按数据设计。
- 非静态成员函数通过隐含的 `this` 指针作用于对象；Python 把它显式写成 `self`。
- `inline` 的实际作用是允许在头文件中定义函数，是否展开由编译器决定；内联函数和模板取代了类函数宏。
- Python 用命名约定代替访问控制，用 `@property` 在不改变接口的前提下加入检查与计算。
