---
title: 设计模式
description: 设计模式的概念与分类；以负载监视器为例的模板方法、策略、适配器与装饰器模式；开闭原则、单一职责原则与 SOLID 等设计原则；Python 中用一等函数、鸭子类型和装饰器语法实现的对应写法。
---

前面各章讲的是面向对象的机制：**封装**、**组合**与**继承**、**虚函数**与**多态**、**模板**、**函数对象**。机制本身并不保证程序结构良好：同样的需求，可以写成一改就到处牵连的代码，也可以写成增加功能时只需添加新类的代码。设计模式是开发者在长期实践中总结出来的、反复出现的设计问题的成熟解法，它展示了怎样组合这些机制来应对需求的变化。本章以一个负载监视器为贯穿的例子，依次讲模板方法、策略、适配器和装饰器四种模式，从中提炼出开闭原则、单一职责原则等设计原则，并说明在 Python 这样有一等函数和鸭子类型的语言中，许多模式可以写得更轻。软件设计的其他方面（需求、架构、测试与维护）见 [4.14 软件工程](/4.14)。

## 13.1. 设计模式

**定义 13.1.1（设计模式）** 针对软件设计中在特定情境下反复出现的问题，给出的经过实践检验、可以重复使用的解决方案的描述，称为**设计模式**（design pattern）。一个模式通常包括名称、要解决的问题、解决方案的结构（参与的类与对象及其协作方式）和使用后果（优点与代价）。

这一概念因 Gamma、Helm、Johnson、Vlissides 四人（常称 GoF，Gang of Four）1994 年的著作《Design Patterns: Elements of Reusable Object-Oriented Software》而广为人知，书中收录了 23 种模式，分为三类：

| 类别 | 关注 | 例子 |
|---|---|---|
| 创建型 | 怎样创建对象，把创建与使用分开 | 工厂方法、抽象工厂、建造者、单例 |
| 结构型 | 怎样把类和对象组合成更大的结构 | 适配器、装饰器、组合、代理、外观 |
| 行为型 | 对象之间怎样分配职责、相互协作 | 模板方法、策略、观察者、迭代器、命令 |

书中贯穿全书的两条原则是：针对接口编程，而不是针对实现编程（第 8 章）；优先使用组合，而不是继承（第 7 章）。下面会看到，这四种模式都是这两条原则的具体化。设计模式的价值还在于提供了共同的词汇：说"这里用策略模式"，同行就明白了整个结构。

## 13.2. 例：负载监视器

设想要写一个程序监视计算节点的负载：每隔一秒读取 CPU 负载、内存总量、已用内存和网络延迟，然后显示出来。困难在于读取这些信息的方法因环境而异：Linux 读 `/proc` 下的文件，Windows 调用系统 API，集群中还可能从 Ganglia 这样的监控系统获取。

最直接的写法是枚举所有环境，在每个函数里按环境分支：

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

这种写法的问题是：每增加一种环境，就要修改枚举和每一个函数中的 `switch`；同一种环境的代码散落在各个函数中，不同环境的代码又挤在同一个函数里，改一处容易碰坏别处。理想的情况是，增加一种环境时只需添加新代码，不必修改已经写好、测试过的代码。

**定义 13.2.1（开闭原则）** 软件实体（类、模块、函数）应当对扩展开放、对修改关闭：需求变化时，通过增加新的代码来扩展其行为，而不是修改已有的代码。这一设计原则称为**开闭原则**（open–closed principle）。

开闭原则的实现手段就是第 8 章的**抽象**与**多态**：把会变化的部分隐藏在稳定的接口之后，新的变化以新的实现类加入。

## 13.3. 模板方法模式

**定义 13.3.1（模板方法模式）** 在基类的一个方法中定义算法的骨架，把其中某些步骤声明为虚函数、交给派生类实现，使派生类可以在不改变算法结构的前提下重新定义这些步骤，这种设计模式称为**模板方法模式**（template method pattern）。定义骨架的那个方法称为模板方法。

（这里的"模板"指算法的框架，与第 9 章的 C++ **模板**无关。）监视器的流程"读取各项指标、然后显示"是固定的，变化的只是读取的方法，于是把流程写在基类中，把各个读取步骤交给派生类：

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

增加一种环境只需再写一个派生类，`Monitor` 和已有的派生类都不用修改，符合开闭原则。C++ 中把模板方法写成公有的非虚函数、把步骤写成私有的虚函数，称为非虚接口（non-virtual interface）惯用法，简称 NVI：派生类可以覆盖私有虚函数，但不能绕过骨架直接调用它们，基类因此能在骨架中统一地加入检查、日志等逻辑。

模板方法的局限在于：每个派生类必须一次性决定所有步骤的实现。如果负载有 $n$ 种读法、内存有 $k$ 种、网络延迟有 $m$ 种，而且可以任意搭配（例如在 Linux 上用 Ganglia 读负载、用 `/proc` 读内存），就需要多达 $n \cdot k \cdot m$ 个派生类，其中大量代码重复。

## 13.4. 策略模式

### 13.4.1. 用组合代替继承

**定义 13.4.1（策略模式）** 把一族可以相互替换的算法分别封装成独立的类，它们实现同一个接口；使用算法的对象（环境类）通过组合持有一个策略对象，并把相应的工作委托给它。这种设计模式称为**策略模式**（strategy pattern）。

把监视器的每一种变化分别抽象成一个策略接口，监视器由几个策略对象组合而成：

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

现在 $n$ 种负载读法、$k$ 种内存读法、$m$ 种延迟读法只需要 $n + k + m$ 个策略类，加上 3 个策略接口和 1 个监视器类，而不是 $n \cdot k \cdot m$ 个派生类；任意搭配在运行时完成，甚至可以在运行中更换。每个策略类只做一件事，可以单独测试和复用。

### 13.4.2. 单一职责原则

**定义 13.4.2（单一职责原则）** 一个类（或模块）应当只负责一项职责，即只有一个引起它变化的原因。这一设计原则称为**单一职责原则**（single-responsibility principle）。

模板方法版本的 `LinuxMonitor` 同时负责读负载、读内存、读延迟：其中任何一种读法的变化都要修改它。策略模式把每种职责分到一个策略类中，职责之间解耦，一种职责的变化不会影响其他职责。职责过多的类往往难以理解和测试，修改一处时也更可能牵动其他功能。

### 13.4.3. 模板方法与策略的比较

两种模式解决的是同一个问题：算法的多样性对代码结构的冲击。业务简单时二者几乎等效。

| | 模板方法 | 策略 |
|---|---|---|
| 机制 | 继承：派生类覆盖步骤 | 组合：环境类持有策略对象 |
| 变化的粒度 | 稳定流程中的若干步骤 | 整个算法 |
| 何时确定 | 编译时（选择哪个派生类） | 运行时，可以更换 |
| 多个变化维度 | 派生类数量按乘积增长 | 按和增长 |
| 适合 | 流程复杂而稳定、只有局部步骤变化 | 算法本身多变，需要自由搭配 |

在 C++ 中，只有一个操作的策略还可以用第 12 章的 `std::function<double()>` 表示，省去策略接口和策略类，直接传入 **lambda 表达式**；在 Python 中这是首选的写法，见上例中的 `load`。

## 13.5. 适配器模式

**定义 13.5.1（适配器模式）** 把一个类的接口转换成使用者期望的另一个接口，使原本因接口不兼容而不能一起工作的类可以一起工作，这种设计模式称为**适配器模式**（adapter pattern）。其中使用者期望的接口称为目标（target），需要被转换的已有类称为被适配者（adaptee）。

就像电源转接头：手机充电器只能插 USB 口，墙上只有 220 V 插座，转接头把一种接口转换成另一种。在监视器中，假设已经有一个现成的、不能修改的 Windows 监视器类（例如来自第三方库），它的功能满足需要，但接口与我们的不同：

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

适配器有两种实现：

- 对象适配器：适配器实现目标接口，并组合一个被适配者对象，把调用转发给它。它也能适配被适配者的派生类（持有指针时），是更常用的形式。
- 类适配器：适配器 public 继承目标接口、private 继承被适配者（[4.2.7](/4.2.7) 的"照此实现"），直接调用继承来的函数。private 继承保证外界只能看到目标接口。

适配器让已有的类无需修改就能复用（符合开闭原则），把使用者与第三方组件的接口隔开：将来更换组件，只需重写适配器。标准库中的 `std::stack`、`std::queue` 称为容器适配器（第 10 章），就是把 `deque` 的接口适配成栈和队列的接口。

在 Python 中，由于**鸭子类型**，适配器不必继承任何接口，只要提供使用者需要的方法即可；只是改个名字的简单适配，甚至可以直接把被适配者的绑定方法赋给新的属性名。

## 13.6. 装饰器模式

### 13.6.1. 为对象动态地增加功能

现在要把监视结果显示在窗口中，并且可以选择加上边框、水平滚动条、垂直滚动条，任意组合。用继承实现，每种组合都要一个派生类，$k$ 种功能有 $2^k$ 种组合；用策略模式，基类中要预先留好"边框策略""滚动条策略"的位置，增加一种新功能就要修改基类。

**定义 13.6.1（装饰器模式）** 定义一个与被装饰对象实现同一接口的装饰类，它持有一个被装饰对象，在把请求转发给它的前后加入额外的行为。由于装饰后的对象仍满足同一接口，它可以再被装饰，从而在运行时把多个功能逐层叠加到一个对象上。这种设计模式称为**装饰器模式**（decorator pattern）。

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

调用 `show` 时，请求沿着包装链从外向内传递：`Border` 调用 `HScroll`，`HScroll` 调用 `VScroll`，最后到达 `MonitorView`，每一层在结果上加上自己的功能。每个装饰器只知道它直接包裹的对象满足 `View` 接口，不需要了解整条链。有多少种功能就包裹多少层，功能的种类和次序都在运行时决定；增加新功能只需写一个新的装饰类。其他语言中的典型例子是 Java 的 I/O 流（缓冲流包裹文件流）；Python 的 `io.BufferedReader` 包裹原始文件对象也是同一结构。

### 13.6.2. Python 的装饰器语法

Python 的 `@decorator` 语法与装饰器模式同名、思想相通，但作用对象是函数（或类）而非对象：装饰器是一个以函数为参数、返回新函数的函数，新函数通常是包裹原函数的**闭包**（第 12 章），在调用前后加入日志、计时、缓存、权限检查等功能。`@d` 写在 `def f` 上方，等价于定义后执行 `f = d(f)`；多个装饰器从下往上逐层包裹。

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

## 13.7. 设计原则

设计模式是具体的方案，设计原则是隐藏在它们背后的一般准则。面向对象设计中最常提到的是 Robert C. Martin 归纳的五条原则，取首字母合称 SOLID：

- S：单一职责原则（定义 13.4.2）。
- O：开闭原则（定义 13.2.1）。
- L：Liskov 替换原则，见下面的定义 13.7.1。
- I：接口隔离原则（interface segregation principle）。使用者不应被迫依赖它用不到的方法：与其设计一个包罗万象的大接口，不如拆成几个小而专一的接口，一个类可以实现其中的几个（第 7 章的多重继承接口）。
- D：依赖倒置原则（dependency inversion principle）。高层模块不应依赖低层模块，二者都应依赖抽象：策略模式中的 `Monitor` 依赖 `LoadStrategy` 接口，而不是某个具体的读取方式，具体的策略对象由外部创建后传入（依赖注入）。

**定义 13.7.1（Liskov 替换原则）** 若类型 $S$ 是类型 $T$ 的子类型，则程序中任何使用 $T$ 类型对象的地方，都可以换成 $S$ 类型的对象而不改变程序的正确性。也就是说，派生类必须遵守基类接口的约定：不加强前置条件、不削弱后置条件、保持基类的不变量。这一设计原则称为**Liskov 替换原则**（Liskov substitution principle），由 Barbara Liskov 于 1987 年提出。

第 7 章"正方形不是矩形"的例子违反的就是这一原则：`Square` 无法遵守"设置宽度不改变高度"这一 `Rectangle` 的约定。Liskov 替换原则是判断能否使用 public 继承的准则：is-a 必须在行为上成立，而不只是在概念上成立。

此外常与 SOLID 并列的还有两条：合成复用原则（composite reuse principle），即优先使用组合而不是继承来复用代码，策略、适配器、装饰器模式都是例子；迪米特法则（law of Demeter），又称最少知识原则，即一个对象只与它的直接协作者交互，不通过一连串的 `a.b().c().d()` 深入其他对象的内部。

这些原则的共同目标是降低耦合、提高内聚：把可能变化的部分与稳定的部分分开，让变化局限在尽可能小的范围内。它们是权衡的准则而不是必须遵守的规定。为尚不存在的变化预先引入抽象，会使简单的程序变得复杂；常见的建议是先写出最简单的可行代码，等变化真正出现、而且不止一次出现时，再重构到合适的模式。

## 13.8. 模式与语言

GoF 的模式是针对 C++ 和 Smalltalk 这类语言总结的，其中不少是在弥补语言缺少的特性。在有一等函数、闭包和鸭子类型的语言中，许多模式变得很轻，甚至消失在日常写法里：

| 模式 | 典型的 C++ 写法 | Python 中的对应写法 |
|---|---|---|
| 策略 | 策略接口 + 策略类；或 `std::function`、lambda | 直接传入函数 |
| 模板方法 | 基类的非虚函数调用私有虚函数 | 同样用继承，或把步骤作为函数参数传入 |
| 命令 | 命令接口 + `execute` | 函数或 `functools.partial` |
| 观察者 | 观察者接口；回调列表 `std::vector<std::function<…>>`，用 `weak_ptr` 避免悬垂 | 回调函数列表、`weakref` |
| 迭代器 | 迭代器类（第 10 章） | 迭代器协议与生成器 |
| 适配器 | 实现目标接口的包装类 | 鸭子类型下的包装类，或直接赋值绑定方法 |
| 装饰器 | 实现同一接口的包装类 | 包装类；对函数用 `@decorator` |
| 单例 | 函数内的静态局部变量（称为 Meyers 单例） | 模块级对象（模块只导入一次） |
| 工厂 | 返回 `std::unique_ptr<Base>` 的函数 | 类本身就是可调用的工厂；以类为参数 |

模式背后的问题（怎样隔离变化、怎样让对象协作）在任何语言中都存在，变化的只是表达方式。学习设计模式的重点因此不是背诵类图，而是认出问题、理解每种方案的代价，并选择在当前语言中最简洁的表达。

## 小结

- 设计模式是反复出现的设计问题的成熟解法，分为创建型、结构型与行为型；GoF 的两条基本原则是针对接口编程、优先使用组合。
- 模板方法用继承固定流程、开放步骤；策略用组合封装可替换的算法，多个变化维度时类的数量按和而不是按积增长。
- 适配器转换接口，让不兼容的已有类无需修改即可复用；装饰器实现同一接口并包裹对象，在运行时逐层叠加功能。
- 开闭原则、单一职责原则、Liskov 替换原则、接口隔离原则与依赖倒置原则（SOLID）是这些模式背后的设计准则，应按需权衡，不为想象中的变化过度设计。
- Python 的一等函数、鸭子类型与 `@decorator` 语法让许多模式变得很轻：策略就是函数，适配器不必继承接口。
