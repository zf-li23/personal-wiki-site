---
title: 模板与泛型编程
description: 泛型编程的动机；函数模板、类模板与实例化、模板的编译模型；非类型模板参数；全特化与偏特化、if constexpr；C++20 概念与约束；静态多态与动态多态的比较；Python 的类型标注与泛型语法。
---

第 8 章的**虚函数**让一段代码可以处理多种类型的**对象**，前提是这些类型都派生自同一个**基类**，并且在运行时付出间接调用的代价。很多时候我们需要的是另一种通用性：同一个算法（求最大值、排序、查找）、同一种数据结构（栈、动态数组、映射）适用于任何满足条件的类型，包括 `int`、`double` 这样根本没有基类的内置类型，而且要和手写的专用版本一样快。C++ 用模板实现这种通用性。本章讲函数模板与类模板、模板特化，以及 C++20 用来约束模板参数的概念，最后比较模板与虚函数这两种多态。第 10 章的标准库就是建立在模板之上的。

## 9.1. 泛型编程

求两个数中较大者的函数，对 `int`、`double`、`std::string` 各写一遍，函数体完全相同，只有类型不同。传统的解决办法都有缺陷：

- 预处理宏 `#define MAX(a, b) ((a) < (b) ? (b) : (a))`：没有类型检查，参数可能被求值两次（`MAX(i++, j)`），出错时难以调试。
- 用 `void*` 或公共基类表示"任意对象"（C 的 `qsort`、早期 Java 的容器）：丢失类型信息，需要强制转换，内置类型要先包装成对象，还有间接调用的开销。

**定义 9.1.1（泛型编程）** 把算法与数据结构写成与具体类型无关的形式，以类型为参数，使用时再代入具体类型，同时保持类型安全和与专用代码相当的效率，这种程序设计方法称为**泛型编程**（generic programming）。

泛型编程关心的是算法对类型的最低要求：求最大值只要求类型支持 `<`，排序还要求元素可以交换，查找只要求可以比较相等。把这些要求提炼出来、让算法只依赖它们，算法就能用于尽可能多的类型。

## 9.2. 函数模板

### 9.2.1. 定义与实例化

**定义 9.2.1（模板）** 以类型或常量为参数、用来生成函数或类的代码框架称为**模板**。用具体的模板实参代入模板参数、由编译器生成一个具体的函数或类，称为模板的**实例化**（instantiation）。

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

`typename T` 也可以写成 `class T`，含义相同。调用 `myMax(3, 7)` 时，编译器从实参类型推导出 `T = int`（模板实参推导），生成并编译函数 `int myMax(int, int)`；同一个程序中用到几种类型，就生成几个函数。推导要求各处推出的类型一致，`myMax(3, 2.5)` 推出相互矛盾的 `int` 与 `double`，编译失败；显式写出 `myMax<double>` 后实参按普通函数的规则转换。

C++20 允许把参数类型写成 `auto` 来简写函数模板：`auto twice(auto x) { return x + x; }` 等价于一个以 `x` 的类型为参数的模板。

### 9.2.2. 模板的编译模型

模板本身不是函数，只有被实例化时才生成代码。编译器检查模板分两个阶段：定义时检查与模板参数无关的部分（语法、不依赖 `T` 的名字）；实例化时代入实参，再检查依赖 `T` 的部分，例如 `a < b` 对该类型是否合法。由此有几个实际后果：

- 模板的定义通常写在头文件中。实例化发生在使用模板的翻译单元里，编译器此时必须看到模板的完整定义。如果把定义放在单独的 `.cpp` 文件中，其他文件只能看到声明，编译通过，链接时却找不到 `myMax<int>` 的定义（[4.2.2](/4.2.2)）。替代办法是在 `.cpp` 中为预先确定的类型写显式实例化 `template int myMax<int>(int, int);`，或者使用 C++20 模块。
- 错误信息出现在实例化处。用一个不支持 `<` 的类型调用 `myMax`，报错指向模板内部的 `a < b`，嵌套较深时信息冗长难读。§9.5 的概念就是为解决这一问题而引入的。
- 代码膨胀与编译时间。每种实参类型生成一份代码，可执行文件变大；大量模板放在头文件中，每个翻译单元都要重新解析与实例化，编译变慢。

### 9.2.3. 非类型模板参数

模板参数也可以是编译期常量，例如整数、枚举、指针，C++20 起还可以是浮点数和满足条件的类类型。标准库的 `std::array<T, N>` 就以元素个数 `N` 为参数，大小在编译时确定，元素直接存放在对象内部，不使用堆内存：

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

`std::array<int, 4>` 与 `std::array<int, 5>` 是两个不同的类型，不能互相赋值。

## 9.3. 类模板

### 9.3.1. 定义类模板

类模板以类型为参数生成类，是容器的标准写法。下面是一个栈，C++ 与 Python 3.12 的泛型语法对照：

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

`Stack` 是模板，`Stack<int>` 才是类型。在类模板内部，`Stack` 可以作为 `Stack<T>` 的简写；在类外定义成员函数时要重复模板头 `template <typename T>` 并写 `Stack<T>::`。类模板的成员函数只有被调用时才实例化，所以 `Stack<T>` 中即使某个成员函数要求 `T` 支持某种操作，只要不调用它，用不支持该操作的类型实例化 `Stack` 也没有问题。C++17 起，编译器还能从构造函数的实参推导类模板的实参（CTAD），例如 `std::vector v{1, 2, 3};` 推导出 `std::vector<int>`。

### 9.3.2. 成员函数模板

类（无论是否是模板）的成员函数本身也可以是模板。常见的用途是接受"任意一种"迭代器或可调用对象：

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

这里 `addAll` 对 `It` 的要求只是支持 `!=`、`++` 和 `*`，链表的迭代器和普通指针都满足。这正是第 10 章迭代器的思想。

## 9.4. 模板特化

### 9.4.1. 全特化

通用的模板对某些类型可能不正确或不够高效，这时可以为这些类型单独提供实现。

**定义 9.4.1（模板特化）** 为模板的某些特定模板实参单独给出的定义称为**模板特化**。为全部模板参数指定具体实参的称为全特化（explicit specialization），只限定部分参数或参数的形式的称为偏特化（partial specialization）。使用模板时，编译器选择与实参匹配的最特殊的版本。

全特化以 `template <>` 开头。对函数模板，全特化不参与重载决议、容易产生意外，通常直接写一个普通的重载函数代替：例如比较 C 字符串 `const char*` 时，通用的 `myMax` 比较的是指针地址，应当另写 `const char* myMax(const char*, const char*)` 用 `std::strcmp` 比较内容。对类模板，特化是常用的技术。标准库中的 `std::vector<bool>` 就是 `std::vector` 针对 `bool` 的特化（严格地说，分配器参数仍是模板参数，所以它是一个偏特化），它把每个元素压缩成一位存储（因此它的元素不是真正的 `bool` 对象，`operator[]` 返回的是代理对象，这一设计常被认为是失误）。

### 9.4.2. 偏特化

偏特化只能用于类模板（和变量模板）。下面的 `TypeName` 用全特化处理 `int`、`double`，用偏特化处理"任意类型的指针"和"任意类型的 `vector`"，递归地给出类型的名字：

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

这种"在编译时根据类型计算结果"的类模板称为类型特征（type trait）。标准库 `<type_traits>` 提供了大量现成的特征，如 `std::is_pointer_v<T>`、`std::is_integral_v<T>`、`std::remove_const_t<T>`，它们的实现方式就是特化。

### 9.4.3. 编译期分支

C++17 的 `if constexpr` 让函数模板在编译时按条件选择分支，未选中的分支不会被实例化。很多原来需要特化的场合，用它写起来更直接：

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

## 9.5. 概念

### 9.5.1. 约束模板参数

在 C++20 之前，模板对类型的要求只写在文档里，违反时报错出现在模板内部。C++20 引入概念，把要求写进模板的声明中。

**定义 9.5.1（概念）** C++20 中，**概念**（concept）是对模板实参的具名的编译期谓词：它在编译时对给定的类型（或常量）求值为 `true` 或 `false`，表示该类型是否满足一组语法要求。用概念约束模板参数后，不满足约束的实参在调用处就被拒绝，并且错误信息直接指出哪一条约束不成立。

标准库在 `<concepts>`、`<iterator>`、`<ranges>` 中定义了常用的概念，如 `std::integral`、`std::floating_point`、`std::totally_ordered`、`std::copyable`、`std::invocable<F, Args...>`、`std::ranges::range`。约束有几种等价的写法：

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

### 9.5.2. 定义概念

自定义概念用 `requires` 表达式列出类型应支持的操作，每一项只检查能否编译，不执行：

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

`std::signed_integral<T>` 在标准库中定义为 `std::integral<T> && std::is_signed_v<T>`，它蕴含 `std::integral<T>`，所以对 `int` 两个 `show` 都可行时，编译器选择约束更强的那个。用约束选择重载，取代了过去依靠 SFINAE 等技巧写出的晦涩代码。

概念与第 8 章 Python 的 Protocol 思路相同：按"具有哪些操作"描述类型，不要求类型继承自某个基类；区别在于概念在编译时检查，并且约束是模板实例化的前提。

## 9.6. 模板与多态

模板也是一种**多态**：同一份代码作用于不同类型，按类型生成不同的行为（第 8 章所说的参数多态）。因为调用目标在编译时确定，它又称静态多态；虚函数则是动态多态。下面用两种方式实现"打印任意形状的面积"：

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

| | 虚函数（动态多态） | 模板（静态多态） |
|---|---|---|
| 调用目标确定于 | 运行时 | 编译时 |
| 对类型的要求 | 继承自指定基类 | 支持所需操作（可用概念表达） |
| 内置类型、第三方类型 | 不能直接使用 | 可以 |
| 异构容器 | 可以（`std::vector<std::unique_ptr<Shape>>`） | 不能，每个实例化是不同的类型 |
| 运行开销 | 间接调用，难以内联 | 无，可内联 |
| 编译与代码体积 | 新增派生类不必重新编译调用者 | 定义放在头文件中；代码膨胀、编译慢 |

两者常常结合使用。标准库的 `std::function`（第 12 章）用模板接受任意可调用对象，内部用虚函数统一调用接口，这种技术称为类型擦除（type erasure）：对外只暴露一个固定的类型，又能装下任意满足要求的对象。

## 9.7. Python 对照

### 9.7.1. 动态类型就是泛型

Python 的函数本来就不限定参数类型：`def my_max(a, b): return b if a < b else a` 对一切支持 `<` 的对象都有效，这就是**鸭子类型**（第 8 章）。Python 不需要模板来获得通用性，它缺少的是在运行之前发现类型错误的能力。类型标注（type hints）提供这种能力：标注本身在运行时几乎不起作用，由 mypy、pyright 等静态类型检查器读取并检查。

### 9.7.2. 泛型函数与泛型类

Python 3.12 引入了与 C++ 模板相近的泛型语法（PEP 695）：类型参数写在函数名或类名后的方括号中；`[T: Bound]` 给出上界，相当于 C++ 的概念约束；`[T: (int, str)]` 把 `T` 限定为列出的几种类型之一；`type` 语句定义泛型类型别名。§9.3.1 的 `Stack[T]` 就是一个泛型类。

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

与 C++ 的根本区别在于：Python 的泛型只存在于类型检查阶段，运行时 `Stack[int]` 和 `Stack[str]` 是同一个类，不会生成不同的代码，也就没有特化；对某些类型的特殊处理在运行时用 `isinstance` 判断，或者用 `functools.singledispatch` 按第一个参数的类型分派到不同的函数。

## 小结

- 泛型编程以类型为参数编写算法与数据结构；C++ 用模板实现，编译器按实参实例化出具体代码。
- 模板定义一般放在头文件中；错误在实例化时检查。
- 特化为特定实参提供专门实现：函数模板优先用重载，类模板可全特化与偏特化；`if constexpr` 在编译时选择分支。
- C++20 概念把对类型的要求写进声明，提前、清楚地报告错误，并按约束强弱选择重载。
- 模板是静态多态，零运行开销但不能放进异构容器；虚函数是动态多态；二者可以经类型擦除结合。
- Python 天然是泛型的；3.12 的泛型语法与 Protocol 上界只供静态类型检查使用。
