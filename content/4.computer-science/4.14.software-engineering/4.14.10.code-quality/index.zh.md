---
title: 代码质量
description: 写出别人能读懂、能修改、能信任的代码：防御性编程及其权衡；代码布局与编码规范，以及格式化工具；命名约定与糟糕的命名；自文档化代码；解释为什么的注释；代码坏味道、圈复杂度与 ABC 度量，代码检查工具与类型检查器的真实输出；重构，即一系列保持行为不变的步骤，并附有在测试保护下的完整示例；设计坏味道、设计模式与 SOLID 原则；以及由 AI 智能体编写代码时的代码质量。
source_hash: cad6f871bc48
---

程序被阅读的次数远多于被编写的次数：评审者要读，扩展它的同事要读，几年后修复它的维护者要读，作者本人几个月后对它也如同陌生人。代码质量，就是使这种阅读既省力又安全的代码属性。本章属于本课程中"好代码"这条线（[4.14.1](/4.14.1)）：先讲**防御性编程**，它使代码在假设被违反时也不致失败（10.1）；然后转向代码的呈现，即布局（10.2）、命名（10.3）、结构（10.4）与注释（10.5）。10.6 节说明如何通过坏味道、度量和静态分析工具发现糟糕的代码；10.7 说明如何通过重构安全地改进代码；10.8 把讨论从函数提升到类，那里的代码坏味道变成了设计坏味道，补救办法是**设计模式**与 SOLID 原则（[4.2.13](/4.2.13)）。使重构变得安全的测试是接下来两章的内容（[4.14.11](/4.14.11)、[4.14.12](/4.14.12)）。示例用 Python 编写，运行环境为 Python 3.14、ruff 0.17、radon 6.0、mypy 2.4 与 pytest 9.1；其中的 C 片段只用于说明布局。

## 10.1. 防御性编程

### 10.1.1. 不作任何假设

墨菲定律说："凡是可能出错的事，终将出错。"它的原始表述更精确：如果做一件事有不止一种方式，而其中一种会导致灾难，那么总会有人采用那种方式。对代码来说就是：如果你的代码可能被误用，它就会被误用。输入会为空、过长、格式错误或带有恶意；函数会以错误的顺序被调用；文件会缺失；网络会超时；为某个场景写的代码会被挪到另一个场景中复用。

**防御性编程**（[4.1.5](/4.1.5)）要求把每一段代码都写成：在这类事情发生时仍能保持合理的行为。它的第一条规则是*不作任何假设*：未写明的假设是故障的恒常来源，而且随着代码的增长与易手而成倍增加。一个经典的例子是：某函数在输入超过 1000 个字符时崩溃，写它的程序员认为不会有人输入这么长的内容；攻击者就会，结果是缓冲区溢出。

Ariane 5 的失败（例 1.1.1）表明未写明的假设如何叠加起来。几个在各自环境中都合理的决定恰好碰到了一起：

- 在 Ariane 4 的惯性参考软件中，把 64 位浮点数（水平偏差，与水平速度有关）转换为 16 位有符号整数的操作没有加保护，以降低处理器负载；分析表明，在 Ariane 4 的轨道上该值不可能溢出。
- 这套软件原封不动地用到了 Ariane 5 上，而 Ariane 5 的轨道在飞行初期产生的水平速度要大得多。支撑"可以不加保护"的那个假设，只记录在 Ariane 4 的分析中，没有以任何人会对照新轨道重新检查的形式留存下来。
- 包含该转换的对准函数只在起飞前有用，却在起飞后继续运行了约 40 秒，这是从 Ariane 4 继承来的需求，目的是在倒计时暂停之后能够快速重启。

溢出引发的异常使两台惯性单元都关闭了。这些决定每一个都建立在一个对 Ariane 4 成立、对 Ariane 5 不成立的假设之上；只要对转换的范围做一次检查，或者重新审视这些假设，就能避免这次损失。

### 10.1.2. 处理错误输入

程序对错误输入可以有多种响应方式，从最差到最好依次是：

| 响应 | 名称 | 例子 |
|---|---|---|
| 处理它并产生错误的结果 | 垃圾进，垃圾出 | 负的数量产生负的发票 |
| 接受它但什么也不做 | 垃圾进，什么也不出 | 表单悄悄丢弃了订单 |
| 以清楚的消息拒绝它 | 垃圾进，错误消息出 | "数量必须是正整数" |
| 使错误输入不可能出现 | 不允许垃圾进入 | 最小值为 1 的数字字段，无法存放非法值的类型 |

防御性编程以最后两行为目标。实用的规则是：检查来自外部的所有数据（文件、网络请求、用户、环境变量）的值；检查函数所有输入参数的值，至少在模块边界处检查；并有意识地决定如何处理错误输入。决定取决于错在谁：

- 来自程序外部的错误输入是预料之中的事件。它作为错误报告给调用者，通常是抛出带有准确消息的异常，或返回错误值，程序继续运行。
- 违反内部假设是程序中的缺陷。它用**断言**（[4.1.5](/4.1.5)）来检查，使程序在缺陷显现的那一点停下，而不是任由被破坏的状态扩散。断言不是校验输入的手段：Python 带 `-O` 运行时会删除 `assert` 语句。

```python
from dataclasses import dataclass

MAX_QUANTITY = 1000


@dataclass(frozen=True)
class OrderLine:
    sku: str
    quantity: int

    def __post_init__(self) -> None:
        # Validate at construction, so that no invalid OrderLine can exist.
        if not self.sku:
            raise ValueError("sku must not be empty")
        if not 1 <= self.quantity <= MAX_QUANTITY:
            raise ValueError(f"quantity must be in 1..{MAX_QUANTITY}, got {self.quantity}")


def parse_line(text: str) -> OrderLine:
    """Parse 'SKU,QUANTITY' from an uploaded file."""
    sku, sep, qty = text.partition(",")
    if not sep or not qty.strip().isdigit():
        raise ValueError(f"malformed order line: {text!r}")
    return OrderLine(sku.strip(), int(qty))
```

这个类在它的**构造函数**中校验自身，因此每个接收 `OrderLine` 的函数都可以信赖它的**不变式**而无需再次检查；这就是用类型实现的"不允许垃圾进入"策略。在边界处检查、在内部信任，是安全与重复之间通行的折中。

### 10.1.3. 代价与收益

| 反对 | 支持 |
|---|---|
| 检查要耗费一些运行时间 | 检查能省下数小时的**调试**，因为失败在它开始的地方就被报告了 |
| 每项检查都是要编写、测试和阅读的额外代码 | 稍慢一点但能工作的代码，远胜于大多数时候能工作、偶尔却惨败的代码 |
| 过多的检查会掩盖主逻辑 | 检查把原本不会写下来的假设记录成文档 |

代价这一论据很少起决定作用：一次范围检查只花几纳秒，生产环境中的一次崩溃要花几小时甚至更多。可读性的论据是真实的，办法是像上面那样把检查放在模块边界和构造函数里，而不是在每个函数中重复。

## 10.2. 布局与呈现

### 10.2.1. 代码是写给人看的

源代码有三类读者。编译器或解释器只需要语法正确。作者在写的时候理解逻辑，所以只为自己写的代码会在日后维护时让作者本人困惑。第三类读者最重要，却最少被考虑：其他程序员，即需要阅读、修改和扩展代码的同事和未来的维护者，包括未来的自己。要为他们的方便而写。

呈现对质量有实际影响，因为程序员从布局中读出代码的含义。好的呈现揭示代码的结构；坏的呈现误导读者，还会隐藏缺陷。在 C 中，下面两行的缩进暗示两者都受 `if` 控制，实际上只有第一行受控：

```c
if (user_is_admin)
    grant_access();
    log_access();       // runs for everyone, despite the indentation
```

同一类错误导致了 2014 年苹果的"goto fail"漏洞：一行重复的 `goto fail;`，缩进得像是属于某个 `if`，跳过了 TLS 证书验证的最后一步。Python 把缩进作为语法的一部分，避开了这个特定的陷阱；GCC、Clang 等编译器会对此给出警告（`-Wmisleading-indentation`）。

### 10.2.2. 布局风格

好的布局是*一致的*（整个项目采用一种风格：缩进、花括号、空格、行宽）、*符合惯例的*（采用业界通行的主要风格之一，而不是私人发明）和*简洁的*（易于学习和遵循）。C 系语言的经典花括号风格只是花括号的位置不同：

```c
int kr_style(void) {              /* K&R, also used by Java and most C++ guides */
    int a = 0, b = 0;
    while (a != 10) {
        b++;
        a++;
    }
    return b;
}

int allman_style(void)            /* Allman: braces on their own lines */
{
    int a = 0, b = 0;
    while (a != 10)
    {
        b++;
        a++;
    }
    return b;
}

int gnu_style (void)              /* GNU: braces indented by half a level */
{
  int a = 0, b = 0;
  while (a != 10)
    {
      b++;
      a++;
    }
  return b;
}
```

还有别的风格（Whitesmiths 把花括号与循环体一起缩进）。没有哪一种在客观上最好；重要的是项目选定一种。布局规则不止涉及花括号：控制结构的缩进、单条语句的形式（每行一条语句，运算符两侧加空格）、函数与类的布局（它们之间的空行、成员的顺序）以及注释的布局。

### 10.2.3. 编码规范与格式化工具

编码规范（coding standard）是项目中关于布局、命名与语言特性使用的一套成文规则。一些著名的规范，各有侧重：

| 规范 | 侧重 |
|---|---|
| Indian Hill C Style and Coding Standards（AT&T 贝尔实验室） | 可读性与团队协作 |
| GNU Coding Standards | 可移植性与自由软件的惯例 |
| MISRA C 与 MISRA C++（汽车工业软件可靠性协会） | 嵌入式、安全关键系统的安全性与可靠性；1998 年版有 127 条规则，现行版本（MISRA C:2023、MISRA C++:2023）有一百多条准则，由专用工具检查 |
| SEI CERT C、C++ 与 Java 编码规范 | 安全：防止漏洞的规则 |
| PEP 8（Python）、Google 风格指南（C++、Java、Python、TypeScript 等）、C++ Core Guidelines | 一门语言的社区惯例 |

选定一种好的风格并坚持下去。如今，规范中的布局部分最好由代码格式化工具（formatter）来强制执行，它是一种把代码自动改写成标准风格的工具：Python 用 `ruff format` 或 Black，C 与 C++ 用 clang-format，JavaScript 与 TypeScript 用 Prettier，还有 `gofmt` 与 `rustfmt`，它们的输出就是各自语言的事实标准。格式化工具终结了关于风格的争论，使**代码评审**中不再有风格方面的意见，并使差异保持很小，因为没有人会去重新排版别人的行。下面对一个写得马虎的函数运行 `ruff format`：

```python
import os, sys
import json
def load_orders(path,default=[]):
    try:
        f=open(path)
        data=json.load(f)
    except:
        return default
    result = [ ]
    for o in data :
        if o['status']=='paid' or o['status']=='shipped' : result.append( o )
    if result == None: return default
    return result
```

```text
$ ruff format --diff messy.py
--- messy.py
+++ messy.py
@@ -1,13 +1,17 @@
 import os, sys
 import json
-def load_orders(path,default=[]):
+
+
+def load_orders(path, default=[]):
     try:
-        f=open(path)
-        data=json.load(f)
+        f = open(path)
+        data = json.load(f)
     except:
         return default
-    result = [ ]
-    for o in data :
-        if o['status']=='paid' or o['status']=='shipped' : result.append( o )
-    if result == None: return default
+    result = []
+    for o in data:
+        if o["status"] == "paid" or o["status"] == "shipped":
+            result.append(o)
+    if result == None:
+        return default
     return result

1 file would be reformatted
```

格式化工具只改变布局；这个函数中严重得多的问题（裸 `except`、可变的默认参数、从不关闭的文件）要由 10.6.3 中的代码检查工具来发现。

优秀的程序员知道布局如何影响可读性，并努力写出最清晰的代码；即使团队风格与个人偏好相抵触，他们也采用团队风格。糟糕的程序员则深信自己的看法才是唯一正确的，没有一以贯之的风格，还用自己的风格践踏别人的代码。

## 10.3. 命名

### 10.3.1. 名字说明什么

人们从名字中读出事物的含义。好的名字描述事物的身份（它是什么）和行为（它的角色、关系与交互），并使其易于辨认：为一个概念命名，会把模糊的想法变成设计中定义明确的一部分。程序员要为变量、常量、函数、类型（类、枚举、结构体、类型别名）、模块与包、**命名空间**、宏、子系统和源文件命名。

好的名字应当：

- *有描述性*：`user_age`、`calculate_order_total`，而不是 `x` 或 `do_it`；
- *技术上正确*：在语言中合法，不含空格，所含字符（下划线、Unicode、大小写）为语言和工具所可靠处理；
- *符合惯用法*：遵循该语言的命名约定；
- *得体*：长度足以表意（清晰优先于简短），语气严肃；`foo`、`bar` 和玩笑不属于生产代码。

### 10.3.2. 按种类的约定

- 变量是名词或名词短语：`order_form`、`count`；布尔变量读起来像谓词：`is_valid`、`has_children`。
- 函数是动词或动词短语：`count_apples()`、`send_invoice()`。函数的名字从调用者的角度、按它做什么来取，隐藏它怎么做：`find_customer`，而不是 `loop_over_customer_table`。
- 类型是名词：`Invoice`、`Window`。接口常常以某种能力命名：`Serializable`、`Comparable`。避免多余的词（`InvoiceClass`、`InvoiceData`、`InvoiceObject` 所说的没有一点是 `Invoice` 没说的）。
- 命名空间与包把名字分组以避免冲突；它们的名字应当反映其内容的逻辑关系。例如 Java 的包名像颠倒的互联网域名那样层层嵌套（`org.apache.commons.lang3`）。

大小写约定用来区分名字的种类，各语言之间不尽相同：

| 种类 | Python（PEP 8） | Java | C# | C++（常见） | JavaScript / TypeScript |
|---|---|---|---|---|---|
| 局部变量、参数 | `snake_case` | `camelCase` | `camelCase` | `snake_case` 或 `camelCase` | `camelCase` |
| 函数、方法 | `snake_case` | `camelCase` | `PascalCase` | `snake_case` 或 `camelCase` | `camelCase` |
| 类、类型 | `PascalCase` | `PascalCase` | `PascalCase` | `PascalCase` | `PascalCase` |
| 常量 | `UPPER_CASE` | `UPPER_CASE` | `PascalCase` | `kPascalCase`（Google）或 `UPPER_CASE` | `UPPER_CASE` 或 `camelCase` |
| 包、模块 | `lowercase` | `lowercase` | `PascalCase` | `snake_case` | `kebab-case` 文件名 |

在同一套约定之内，大小写也可以携带含义：在 Python 中，`Window` 是类型，`window` 是它的实例；在 C# 中，局部变量 `count` 与公有属性 `Count`。

### 10.3.3. 糟糕的名字

| 缺陷 | 例子 | 更好的名字 |
|---|---|---|
| 晦涩：随意的缩写，小作用域之外的单个字母 | `nmbr_aps`、`t2`、`proc_dt` | `apple_count`、`retry_timeout`、`processing_date` |
| 冗长 | `the_number_of_apples_before_i_started_eating` | `initial_apple_count` |
| 不准确或有误导性 | 存放字典的 `customer_list`；还会改变大小的 `get_size()` | `customers_by_id`；拆成两个函数 |
| 含糊或笼统 | `data`、`value`、`info`、`manager`、`temp` | 说明该值代表什么的名字 |
| 只有大小写或一个字符的差别 | 同一作用域中的 `user` 与 `User`；`item1`、`iteml` | 含义不同的名字 |
| 遮蔽外层名字 | Python 中的局部变量 `list` 或 `id` | `items`、`user_id` |

说的与代码所做的相反的名字，比毫无意义的名字更糟：

```c
void checkForContinue(bool weShouldContinue)
{
    if (weShouldContinue) abort();
}
```

这个函数什么也不检查，并且恰恰在被告知继续时中止。优秀的程序员尊重名字：他们为自己创建的每样东西想好名字，在长度与清晰度和上下文之间取得平衡，并使名字在整个项目中保持一致。糟糕的程序员写出只写一次的代码，无视语言的惯用法，并且因为不考虑自己写的这一块如何融入整体，而对事物不一致地命名。

## 10.4. 自文档化代码

对付难读的代码，传统的办法是文档：关于代码的长篇文档和代码中的长篇注释。独立的文档写起来和读起来都很贵，第一次改动就会与代码脱节，而且难以找到，其中的重要信息很容易被漏掉。唯一完整而正确地描述代码的文档就是代码本身。自文档化代码（self-documenting code）是指其名称、类型和结构无需额外说明就能表明意图的代码：写代码是为了让人容易地读，编译器自会应付。

比较同一个函数的两种实现：

```c
int fval(int i) {
    int ret = 2;
    for (int n1 = 1, n2 = 1, i2 = i - 3; i2 >= 0; --i2) {
        n1 = n2; n2 = ret; ret = n2 + n1;
    }
    return (i < 2) ? 1 : ret;
}
```

```c
int fibonacci(int position) {
    if (position < 2) {
        return 1;
    }
    int previous_but_one = 1;
    int previous = 1;
    int answer = 2;
    for (int n = 2; n < position; ++n) {
        previous_but_one = previous;
        previous = answer;
        answer = previous + previous_but_one;
    }
    return answer;
}
```

两者计算的都是从 $0$ 开始编号的 Fibonacci 数 $1, 1, 2, 3, 5, \dots$。第一个很短，但读者必须模拟执行才能发现它做什么；第二个则不言自明。即使最小、最优雅的函数，日后也需要维护，而维护的代价就是理解它们的代价。

自文档化代码的技巧：

- 让正常路径一目了然。`if`–`else` 链的排列要一致，例如总是正常情形在前、错误情形在后，或者总是错误在前，作为提前返回的卫语句（guard clause）。
- 避免深层嵌套。第二个 `fibonacci` 在位置较小时提前返回；只有单一出口的版本就得把整个循环嵌套在 `if (position >= 2)` 里面。结构化程序设计曾坚持单入口、单出口；如今通常的平衡是接受若干提前退出，换取扁平的代码。
- 不要为优化而牺牲清晰。除非已经证明某段代码是达到可接受性能的瓶颈，否则不要优化（**性能分析**见 [4.4.7](/4.4.7)）；保留清晰的版本作为参照和测试预言。
- 分解成原子函数：一个函数只做一件事，短小，没有出人意料的**副作用**。
- 让重要的代码突出，并利用语言的特性（类、数据类、模块）把相关信息组织在一起，而不是依靠位置邻近。
- 选择有意义的名字（10.3）和有描述性的类型：`OrderLine` 或枚举比元组或字符串说明得更多，而且类型检查器可以对其做验证。
- 给常量命名。魔数（magic number）是代码中没有解释的字面量，例如 `if total >= 199`；具名常量 `FREE_SHIPPING_THRESHOLD = 199` 说明了含义，而且改动时只需改一处。

优秀的程序员写出清晰、自文档化的代码和必不可少的最少文档，心里想着将要维护它的程序员。糟糕的程序员要么完全不写文档，要么任其腐烂，认为难写的东西就该难懂，并且为难以理解的面条代码（spaghetti code）而自豪：控制流如此纠缠，以致无法跟踪。

## 10.5. 注释

注释应当写得足够多，但不要更多。注释写坏比写好容易，而坏注释可能比没有注释危害更大，因为读者会相信它。重要的是注释的质量，而不是数量。下面的 Java 片段中可以分辨出三种注释：

```java
// sum from 1 to num                         <- wrong: the loop adds 1, not i,
sum = 0;                                     //    and stops before num
for (int i = 1; i < num; i++) {
    sum = sum + 1;
}

// set product to "base"                     <- repeats the code
product = base;
// loop from 2 to "num-1"
for (int i = 2; i < num; i++) {
    // multiply "base" by "product"
    product = product * base;
}

// compute the square root of num using the Newton-Raphson approximation
r = num / 2;                                 // <- explains the intent
while (Math.abs(r - (num / r)) > TOLERANCE) {
    r = 0.5 * (r + (num / r));
}
```

好注释的规则：

- 解释为什么，而不是怎么做。代码说明怎么做；注释说明为什么这样做、它是干什么的，或者不这样做会出什么问题。
- 不要描述代码。重复代码的注释使阅读量翻倍，而且两者之一一旦改动，它就错了。
- 记录出人意料之处：变通办法、不显然的性能技巧、来自外部的约束。
- 说真话，并使注释有价值、清楚。

两条站得住脚的注释：

```java
// Use a right shift to divide by two: replacing the division
// cut the loop time by 75% (profiled on the production data set).
elementList[element] = elementList[element] >> 1;

/* Work around an error in writeData() that appears only when the third
   parameter equals 500. '500' has been replaced with a named constant. */
if (blockSize == WRITEDATA_BROKEN_SIZE) {
    blockSize = WRITEDATA_WORKAROUND_SIZE;
}
writeData(file, data, blockSize);
```

注释常常说明代码本身应该改进。依次改进代码与注释：

| 步骤 | 代码 | 评价 |
|---|---|---|
| 1 | `// if account flag is zero` `if (accountFlag == 0)` | 注释重复了代码 |
| 2 | `// if establishing a new account` `if (accountFlag == 0)` | 更好的注释：说明了意图 |
| 3 | `if (accountType == AccountType.NEW_ACCOUNT)` | 更好的代码：意图在代码中，注释没有必要 |
| 4 | `// Establish a new account` `if (accountType == AccountType.NEW_ACCOUNT) { … }` | 概括整个代码块的注释 |

进一步的指导：

- 选择低维护成本的风格。右边带边框的星号框，以及注释中按列对齐的变量表，每次编辑后都必须重新对齐，很快就会败坏；朴素的块注释则不会。
- 文件头注释说明文件的目的与内容，并在需要时附上法律声明。它不应列出文件中的每个函数、类和全局变量（这样的列表立刻就过时了），也不应列出版本与修改历史，这些由**版本控制系统**记录（[4.14.3](/4.14.3)）。
- 接口文档是一种特殊的注释：Python 的 docstring、Javadoc、Doxygen。它为不读函数体的调用者记录函数的契约（做什么、参数、返回值、错误、**前置条件**），并由工具提取成参考文档。

优秀的程序员写少量真正好的、解释为什么的注释，把精力集中在写好代码上，而不是堆砌大量注释。糟糕的程序员分不清好注释与坏注释，解释怎么做，写出只有自己看得懂的注释，用大量注释来支撑糟糕的代码，并用冗余信息填满文件。

## 10.6. 发现糟糕的代码

### 10.6.1. 代码坏味道

**定义 10.6.1（代码坏味道）** **代码坏味道**是代码表面上的一种特征，通常预示着设计中更深层的问题：它不是缺陷，因为代码能工作，而是代码将难以理解或修改的迹象。这个术语出自 Kent Beck，经 Martin Fowler 的著作《重构》（*Refactoring*，1999 年；第 2 版 2018 年）而流行，该书为每种坏味道配上了消除它的重构手法。

Fowler 的目录命名了二十多种坏味道；下面是最常见的，用第 2 版的名称（括号中为第 1 版的名称）：

| 坏味道 | 症状 |
|---|---|
| 神秘命名（Mysterious Name） | 名字没有说明事物做什么（10.3） |
| 重复代码（Duplicated Code） | 同样的结构出现在多处；修复必须在每处重复 |
| 过长函数（Long Function / Long Method） | 函数太长，无法一眼看懂 |
| 过大的类（Large Class） | 类的字段和方法太多，承担了多项工作 |
| 过长参数列表（Long Parameter List） | 参数很多，难以调用和测试 |
| 数据泥团（Data Clumps） | 同一组值在许多函数之间一起传递 |
| 基本类型偏执（Primitive Obsession） | 在该用小类型（金额、日期区间、电话号码）的地方用了字符串和数字 |
| 重复的 switch（Repeated Switches / Switch Statements） | 同一个针对类型码的 `switch` 或 `if` 链出现在多处 |
| 发散式变化（Divergent Change） | 一个模块因许多互不相关的原因而被修改 |
| 霰弹式修改（Shotgun Surgery） | 一次改动需要在许多模块中做小的修改 |
| 依恋情结（Feature Envy） | 一个函数使用另一个类的数据多于自己的 |
| 过长的消息链（Message Chains） | `a.get_b().get_c().get_d()`：调用者依赖整条导航路径 |
| 中间人（Middle Man） | 只把工作委托给另一个类的类 |
| 内幕交易（Insider Trading / Inappropriate Intimacy） | 彼此了解对方内部细节的类 |
| 夸夸其谈的通用性（Speculative Generality） | 为永远不会出现的情形预留的钩子与抽象 |
| 临时字段（Temporary Field） | 只在某些情形下才被赋值的字段 |
| 冗赘的元素（Lazy Element / Lazy Class） | 做得太少、不足以证明自己存在价值的类或函数 |
| 纯数据类（Data Class） | 只有字段和访问器、行为都在别处的类 |
| 被拒绝的遗赠（Refused Bequest） | 不想要所继承内容的子类 |
| 注释（Comments） | 把注释当作遮盖不清晰代码的除臭剂（10.5） |

发散式变化与霰弹式修改是糟糕的**模块化**的两个侧面：前者是**内聚**弱，后者是**耦合**强（定义 5.5.2）。过长参数列表这一坏味道值得细看，因为它太常见了。参数很多的函数难以被测试覆盖，因为组合数增长很快，而且在测试其调用者时也难以用测试替身替换。布尔参数是一个警告信号：如果函数的行为取决于它的值，它多半应当拆成两个函数。而如果同样的一组实参在许多函数之间成团传递，它们就构成一个数据泥团，应当变成一个独立的类（重构手法"引入参数对象"，Introduce Parameter Object）。

### 10.6.2. 复杂度度量

坏味道由人来判断；度量由工具来计算。衡量函数复杂度的常用度量有两种。

**定义 10.6.2（圈复杂度）** 程序的**圈复杂度**由 Thomas McCabe 于 1976 年提出，是穿过其控制流图的线性无关路径的条数。对于有 $E$ 条边、$N$ 个结点、$P$ 个连通分量（每个函数一个）的控制流图 $G$，
$$
V(G) = E - N + 2P.
$$

对于控制流结构化的单个函数（$P = 1$），三种计算方式是一致的：

- $V(G) = E - N + 2$；
- $V(G)$ = 判定数 $+ 1$，其中每个 `if`、`elif`、循环（`for`、`while`）、`case` 和 `except` 计为一个判定；
- $V(G)$ = 把图画在平面上时它将平面分成的区域数，包括外部区域。

顺序语句序列的 $V = 1$；`if`–`then`–`else`、`while` 循环与 repeat–until 循环的 $V$ 都是 $2$。数 $V(G)$ 也是路径基的大小，所有路径都可以由它组合得到，因此也是基本路径测试（[4.14.11](/4.14.11)）所需的**测试用例**数。

下面的函数计算运费：

```python
def shipping_cost(order):
    cost = 0.0
    if order.weight <= 1:
        cost = 5.0
    elif order.weight <= 5:
        cost = 8.0
    else:
        cost = 8.0 + (order.weight - 5) * 1.5
    if order.express:
        cost *= 2
    if order.country != "CN":
        if order.country in ("JP", "KR"):
            cost += 20
        else:
            cost += 45
    for item in order.items:
        if item.fragile:
            cost += 3
    if order.total >= 199 and not order.express:
        cost = 0.0
    return cost
```

它包含八个判定（`if`、`elif`、`if`、`if`、嵌套的 `if`、`for`、`if`、`if`），因此 $V = 9$。两个工具的报告如下：

```text
$ ruff check --select C901 --config 'lint.mccabe.max-complexity = 5' shipping.py
shipping.py:1:5: C901 `shipping_cost` is too complex (9 > 5)
Found 1 error.
$ radon cc -s shipping.py
shipping.py
    F 1:0 shipping_cost - B (10)
```

Ruff 实现的是 McCabe 的计数；radon 还把最后一个条件中的布尔运算符 `and` 也算作一个判定，因为 `order.total >= 199 and not order.express` 隐藏了两个条件（这种变体有时称为扩展圈复杂度）。Radon 的字母等级 A 表示 1–5，B 表示 6–10。

**定义 10.6.3（ABC 度量）** **ABC 度量**由 Jerry Fitzpatrick 于 1997 年提出，用三个计数来衡量函数的规模：$A$，赋值的次数（`=`、`+=`、`-=`、`*=`、`++` 以及类似的存储值的运算符）；$B$，分支的次数，这里指控制转移到其他代码，主要是函数和方法调用；$C$，条件的数目（`<`、`==`、`!=` 之类的比较，关键字 `else`、`case`、`default`，以及条件表达式的 `?`）。ABC 分数是向量 $(A, B, C)$ 的长度：
$$
|ABC| = \sqrt{A^2 + B^2 + C^2}.
$$

常用的阈值是：每个函数的圈复杂度不超过 10，这是 NIST 关于结构化测试的报告（SP 500-235，1996 年，在有正当理由时允许到 15）所推荐的上限；以及每个方法的 ABC 分数约为 20，这是 Ruby 社区的经验法则，Flog 与 RuboCop 之类的工具会计算它。对度量要持保留态度。与测试覆盖率一样，度量更擅长指出哪里需要改进，而不是证明代码很好：复杂度为 3 的函数仍然可能难以阅读。最有用的目标是*热点*，即多项度量同时报警的地方，尤其是当版本历史表明它们还经常被修改时。

### 10.6.3. 静态分析工具

**定义 10.6.4（静态分析）** **静态分析**是不执行程序而对其进行检查，以发现缺陷、违反编码规则的情形及其他质量问题。对源代码进行轻量级静态分析、查找可能的错误和违反编码规范之处的工具，称为**代码检查工具**（linter），得名于检查 C 程序的 Unix 程序 `lint`（Stephen Johnson，1978 年）。

代码检查工具能发现格式化工具不管的那些问题。对 10.2.3 的函数运行：

```text
$ ruff check --select E,F,B,SIM messy.py --output-format concise
messy.py:1:1: E401 [*] Multiple imports on one line
messy.py:1:8: F401 [*] `os` imported but unused
messy.py:1:12: F401 [*] `sys` imported but unused
messy.py:3:30: B006 Do not use mutable data structures for argument defaults
messy.py:5:11: SIM115 Use a context manager for opening files
messy.py:7:5: E722 Do not use bare `except`
messy.py:11:58: E701 Multiple statements on one line (colon)
messy.py:12:18: E711 Comparison to `None` should be `cond is None`
messy.py:12:22: E701 Multiple statements on one line (colon)
Found 9 errors.
[*] 3 fixable with `--fix` (2 unsafe fixes available with `--fix --unsafe-fixes`).
```

其中有几项是真正的缺陷：可变的**默认实参** `[]` 在各次调用之间是共享的，因此向返回的默认值追加内容的调用者，会为所有人改变它（[4.4.1](/4.4.1)）；裸 `except` 还会捕获 `KeyboardInterrupt`，并隐藏名字拼写错误之类的编程错误；而且文件从未被关闭。规则代码的字母指明了来源：`E` 与 `F` 来自 pycodestyle 和 Pyflakes，`B` 来自 flake8-bugbear，`SIM` 来自 flake8-simplify，都已在 ruff 中重新实现。规则在项目配置中选定，这样每位开发者和 **CI** 流水线应用的都是同一套：

```toml
# pyproject.toml
[tool.ruff]
line-length = 100

[tool.ruff.lint]
select = ["E", "F", "B", "SIM", "UP", "I", "C901"]   # I: import sorting
mccabe.max-complexity = 10
```

**类型检查器**是针对**类型标注**（[4.4.1](/4.4.1)）的静态分析器。它能找出否则要等到执行某条罕见路径时才会出现的错误：

```python
def average(values: list[float]) -> float:
    return sum(values) / len(values)


def report(scores: dict[str, list[float]]) -> str:
    best = max(scores, key=lambda name: average(scores[name]))
    return "best: " + best + " with " + average(scores[best])
```

```text
$ mypy typed.py
typed.py:7: error: Unsupported operand types for + ("str" and "float")  [operator]
Found 1 error in 1 file (checked 1 source file)
```

各语言的主要静态分析工具：

| 语言 | 格式化工具 | 代码检查工具 | 类型检查器或更深入的分析 |
|---|---|---|---|
| Python | ruff format、Black | ruff、Pylint | mypy、Pyright |
| JavaScript / TypeScript | Prettier | ESLint、Biome | TypeScript 编译器（`tsc`） |
| C / C++ | clang-format | clang-tidy、cppcheck | 编译器警告、运行时的 sanitizer、Coverity |
| Java | google-java-format | Checkstyle、PMD | SpotBugs、Error Prone |
| 多语言 | | | SonarQube、CodeQL、Semgrep |

静态分析持续运行时最有效：在编辑器中随输入运行，在每次提交之前的 pre-commit 钩子中运行，并在 CI 流水线中作为每个**拉取请求**的质量门禁（[4.14.3](/4.14.3)）。SonarQube 之类的持续检查服务跟踪代码库随时间的健康状况：重复代码、违反编码规范、复杂度、注释、可能的缺陷与安全漏洞。当团队在已有代码库上引入代码检查工具时，通常先对新代码启用规则，或把现有的违规记录为基线，使警告数只减不增。

## 10.7. 重构

### 10.7.1. 定义

**定义 10.7.1（重构）** **重构**是一种有纪律的技术，用于重组现有的代码体，在不改变其外部行为的前提下改变其内部结构。它的核心是一系列小的、保持行为不变的变换，其中每一个变换本身也称为一个重构；每一步之后，系统都保持完全可用。

重构改进代码的非功能性质量，主要是简单性、灵活性与可理解性，有时也包括性能。有两个条件使它安全。步骤要小，使错误能立刻发现且易于撤销；并且有自动化测试在每一步之后运行，因为"不改变外部行为"是一个必须检验而不能假定的论断。当一段遗留代码没有测试时，第一步是在修改之前先编写特征测试（characterization test），即记录代码当前行为的测试。重构不是单独的项目阶段，而是日常工作的一部分：在测试驱动开发（[4.14.12](/4.14.12)）中，它是每个循环的第三步；一条常见的规则是，重构你即将修改的代码，使修改变得容易。

Fowler 的目录给每个重构手法起了名字，说明动机，并给出机械的步骤。两对小的互逆手法说明了这个想法。内联函数（Inline Function）在函数体与名字一样清楚时，用函数体取代调用；提炼函数（Extract Function）则相反：

```java
// before: the helper adds nothing to the body
int getRating() { return moreThanFiveLateDeliveries() ? 2 : 1; }
boolean moreThanFiveLateDeliveries() { return numberOfLateDeliveries > 5; }

// after Inline Function
int getRating() { return (numberOfLateDeliveries > 5) ? 2 : 1; }
```

内联变量（Inline Variable）去掉只是给一个本已清楚的表达式起名字的临时变量：`double basePrice = anOrder.basePrice(); return basePrice > 100;` 变成 `return anOrder.basePrice() > 100;`。

10.6.1 的坏味道与重构手法的对应关系：

| 坏味道 | 重构手法 |
|---|---|
| 过大的类 | 提炼类（Extract Class）、提炼子类（Extract Subclass）、提炼超类（Extract Superclass）、搬移函数（Move Function）到新模块 |
| 过长函数 | 提炼函数、分解条件表达式（Decompose Conditional）、以查询取代临时变量（Replace Temp with Query）、以管道取代循环（Replace Loop with Pipeline）、以命令取代函数（Replace Function with Command） |
| 过长参数列表、数据泥团 | 引入参数对象、保持对象完整（Preserve Whole Object）、以查询取代参数（Replace Parameter with Query） |
| 霰弹式修改、内幕交易 | 搬移函数、搬移字段（Move Field）、函数组合成类（Combine Functions into Class）：把相关的东西收集到一处 |
| 注释 | 提炼函数（用一个取代注释的名字）、引入断言（Introduce Assertion） |
| 重复代码 | 提炼函数、提炼类、函数上移（Pull Up Method）、塑造模板函数（Form Template Method） |
| 重复的 switch | 以多态取代条件表达式（Replace Conditional with Polymorphism）、以子类取代类型码（Replace Type Code with Subclasses） |

其中大多数已由 IDE 自动化（重命名、提炼、内联、搬移），能在整个代码库中正确地执行。

### 10.7.2. 一个完整的例子

10.6.2 的函数 `shipping_cost` 的函数体很长，有魔数，还有一条规则（免运费）虽然写在最后，却覆盖了此前的一切。修改之前，我们先用一个覆盖每个判定的参数化测试固定它的行为：

```python
from dataclasses import dataclass, field

import pytest

from shipping import shipping_cost


@dataclass
class Item:
    fragile: bool = False


@dataclass
class Order:
    weight: float
    country: str = "CN"
    express: bool = False
    total: float = 50
    items: list = field(default_factory=list)


@pytest.mark.parametrize(
    ("order", "expected"),
    [
        (Order(weight=1), 5.0),
        (Order(weight=5), 8.0),
        (Order(weight=7), 11.0),
        (Order(weight=1, express=True), 10.0),
        (Order(weight=1, country="JP"), 25.0),
        (Order(weight=1, country="US"), 50.0),
        (Order(weight=1, items=[Item(fragile=True), Item()]), 8.0),
        (Order(weight=1, total=199), 0.0),
        (Order(weight=1, total=199, express=True), 10.0),
    ],
)
def test_shipping_cost(order, expected):
    assert shipping_cost(order) == pytest.approx(expected)
```

```text
$ pytest -q test_shipping.py
.........                                                                [100%]
9 passed in 0.01s
```

然后我们逐个应用下列重构，并在每一步之后运行测试：替换魔法字面量（Replace Magic Literal，具名常量）、对每条规则提炼函数、分解条件表达式、以管道取代循环（易碎品的循环变成一个 `sum`），最后是移动语句（Slide Statements），把免运费规则作为卫语句移到最前面，这是保持行为不变的，因为该规则覆盖了此前的所有结果：

```python
FREE_SHIPPING_THRESHOLD = 199
EXPRESS_FACTOR = 2
FRAGILE_SURCHARGE = 3
NEARBY_COUNTRIES = {"JP": 20, "KR": 20}
OTHER_COUNTRY_SURCHARGE = 45


def shipping_cost(order):
    if qualifies_for_free_shipping(order):
        return 0.0
    cost = base_cost(order.weight)
    if order.express:
        cost *= EXPRESS_FACTOR
    cost += international_surcharge(order.country)
    cost += handling_surcharge(order.items)
    return cost


def qualifies_for_free_shipping(order):
    return order.total >= FREE_SHIPPING_THRESHOLD and not order.express


def base_cost(weight):
    if weight <= 1:
        return 5.0
    if weight <= 5:
        return 8.0
    return 8.0 + (weight - 5) * 1.5


def international_surcharge(country):
    if country == "CN":
        return 0
    return NEARBY_COUNTRIES.get(country, OTHER_COUNTRY_SURCHARGE)


def handling_surcharge(items):
    return FRAGILE_SURCHARGE * sum(1 for item in items if item.fragile)
```

```text
$ pytest -q test_shipping.py
.........                                                                [100%]
9 passed in 0.01s
$ radon cc -s shipping.py
shipping.py
    F 8:0 shipping_cost - A (3)
    F 21:0 base_cost - A (3)
    F 35:0 handling_surcharge - A (3)
    F 17:0 qualifies_for_free_shipping - A (2)
    F 29:0 international_surcharge - A (2)
```

行为没有改变，同样的九个测试证实了这一点。总的复杂度大体相同，因为判定是**业务规则**本身固有的，但现在它分散在五个函数中，每个函数都可以单独阅读、命名、测试和修改；`shipping_cost` 本身读起来就像定价政策的摘要，而改动某个国家的附加费只涉及一张表。

## 10.8. 从代码坏味道到设计坏味道

### 10.8.1. 设计模式与反模式

10.6 与 10.7 的思想适用于函数或类的内部。在类之间的关系这一层，相应的概念是设计坏味道与**设计模式**。建筑师 Christopher Alexander 把模式描述为一个反复出现的问题，连同对它的一个经过检验的解法的核心；他的著作《建筑模式语言》（*A Pattern Language*，1977 年）收录了 253 个建筑与规划的模式，从城镇的分布到屋顶的细节，组织成一种模式语言（pattern language），其中较大的模式由较小的模式来完成。"四人组"（Gamma、Helm、Johnson 与 Vlissides，1994 年）的 23 个**设计模式**把这一思想带到面向对象软件中，分为三类（[4.2.13](/4.2.13)）：

| 创建型 | 结构型 | 行为型 |
|---|---|---|
| 工厂方法、抽象工厂、生成器、原型、单例 | 适配器、桥接、组合、装饰器、外观、享元、代理 | 责任链、命令、解释器、迭代器、中介者、备忘录、观察者、状态、策略、模板方法、访问者 |

模式描述的是相互通信的对象和类，它们在特定的上下文中解决一个一般性的设计问题；它刻画了一类相关问题的常见而成功的解法，并针对每个具体问题加以定制。模式既不是类或库（如列表或散列表），也不是完整的设计：它更接近设计某一部分的蓝图。模式复用的是设计而不是代码，它们的共同主题是把变化的部分与不变的部分分开：面向接口而非实现编程；优先使用**组合**而非**继承**；委托。

反模式（antipattern）则相反：一种常见的、看起来像解法、实际上弊大于利的结构，例如无所不知、无所不做的上帝类，或者显然应该遵循某种模式却没有遵循的代码。反模式常常是累积的技术债务（technical debt）的结果：团队现在选择权宜的方案，而不是更好但更耗时的方案，由此招致的未来返工成本。与金融债务一样，技术债务有时值得有意地承担，以赶上截止日期；之后它会产生利息，表现为更慢、风险更大的修改，直到通过重构偿还。

两个层次的比较如下：

| | 类内部的方法 | 类之间的关系 |
|---|---|---|
| 坏的迹象 | 代码坏味道 | 设计坏味道 |
| 目录 | 代码坏味道与重构 | 设计坏味道与设计模式 |
| 度量 | ABC 分数、圈复杂度 | 方法内聚缺乏度（LCOM）、对象间耦合 |
| 典型重构 | 提炼函数、在类内搬移代码 | 提炼类、在类之间搬移代码 |
| 准则 | SOFA：方法要短小（Short）、只做一件事（One thing）、参数要少（Few arguments）、停留在单一抽象层次（Abstraction） | SOLID 原则 |

### 10.8.2. SOLID 原则

SOLID 原则由 Robert C. Martin 在 2000 年前后整理，由 Michael Feathers 命名，目的是使面向对象设计中的修改代价最小。它们在 [4.2.13](/4.2.13) 中与设计模式一并介绍过；这里从维护的角度逐一审视：揭示违反的症状，以及修复它的重构手法或模式。

| 原则 | 表述 | 违反的症状 | 补救办法 |
|---|---|---|---|
| **单一职责原则** | 一个类有且只有一个引起它变化的原因 | 非常大的类；几组互不相关的方法；无法用 25 个词说明它的职责 | 提炼类 |
| **开闭原则** | 增加功能应当通过增加代码，而不是修改已有代码 | 针对对象类型或创建后从不改变的属性的 `switch` 或 `if` 链 | 以**多态**取代条件表达式；策略、模板方法、装饰器、抽象工厂 |
| **Liskov 替换原则** | 子类型的实例总可以替换其超类型的实例 | 被拒绝的遗赠：子类对所继承的操作没有有意义的实现方式 | 以组合与显式委托取代**继承** |
| **接口隔离原则** | 客户端不应依赖它们不使用的方法 | "胖"接口，其实现者把许多方法留空或抛出错误 | 把接口拆分成角色接口 |
| **依赖倒置原则** | 高层模块依赖抽象，而不依赖低层模块 | 不修改一个类，就无法为它的依赖添加变体，或单独测试它 | 在两者之间引入接口；注入依赖；适配器 |

具有多组行为的模型是违反单一职责的典型：一个 `User` 类同时是顾客、认证主体和社交网络的成员，就有三个变化的轴。可以用度量检测这样的类。在 LCOM4（Hitz 与 Montazeri，1995 年）中，类的方法是图的顶点，如果一个方法调用另一个，或两者使用同一个字段，则这两个方法之间连一条边；LCOM4 就是这个图的连通分量数。内聚的类有 LCOM4 $= 1$；值为 2 或更大，说明该类由几个方法"团"组成，它们可以成为单独的类（提炼类）。

**依赖倒置原则**通常通过依赖注入（dependency injection）实现：类通过构造函数或参数接收它所依赖的对象，而不是自己创建它们。仅这一项改变，就使类既可扩展又可测试：

```python
from datetime import datetime
from typing import Protocol


class Clock(Protocol):
    def now(self) -> datetime: ...


class Mailer(Protocol):
    def send(self, to: str, body: str) -> None: ...


class DailyReport:
    def __init__(self, clock: Clock, mailer: Mailer) -> None:
        self.clock = clock          # injected: a real clock in production,
        self.mailer = mailer        # a fixed clock and a fake mailer in tests

    def send_to(self, manager: str) -> None:
        today = self.clock.now().date()
        self.mailer.send(manager, f"Sales report for {today}")
```

`DailyReport` 只依赖这两个协议；[4.14.12](/4.14.12) 的测试会给它传入测试替身。有些课程沿用 Fox 与 Patterson 的《软件即服务工程》（*Engineering Software as a Service*），把 SOLID 的 I 读作"依赖注入"（injection of dependencies），把 D 读作"Demeter"；在标准表述中，这两者分别是依赖倒置原则和一条独立的原则，即**迪米特法则**。它说：只和你的朋友（对象自己的字段、它的参数和它创建的对象）说话，不和通过它们才能到达的陌生人说话。它的典型症状是 `order.customer.address.city.postal_code` 这样的消息链，它把调用者与整条导航路径耦合在一起，并且在测试中迫使人构造一串模拟对象（"模拟列车事故"）。补救办法是把行为委托给持有数据的对象（`order.shipping_postal_code()`），或者用访问者模式把遍历与计算分开，或者用观察者模式在相关事件发生时得到通知，而不是主动去取。

模式与原则是工具，不是目标。为尚未发生的变化引入抽象，会使代码更复杂（夸夸其谈的通用性）；通常的建议是写出能工作的最简单的代码，并在它所支持的变化真正到来时，向某个模式重构。

## 10.9. 由智能体编写代码时的代码质量

当**编程智能体**（[4.2.14](/4.2.14)）写出大部分代码时，代码的读者变了，但对可读代码的需求没有变：人仍然要评审每一处改动并为系统负责，而智能体本身也是读者，它通过名字、结构和注释来理解代码库。清晰的名字和小的函数对智能体与对人同样有帮助，而有误导性的名字则对两者都有误导。本章的三项做法变得更加重要。

- 让约定可执行。只存在于风格文档中的规则，人执行得不一致，智能体执行得不可靠；写进格式化工具、代码检查工具和**类型检查器**配置中的规则，每次都会被执行。运行 `ruff format --check`、`ruff check` 与类型检查器的 pre-commit 钩子和 CI 质量门禁，把编码规范变成智能体每次改动后都能运行、并能在任何人评审之前自行修复的检查。
- 留意智能体容易产生的坏味道。生成的代码常常重复已有的辅助函数而不是找到它，添加重复代码内容的防御性检查和注释，宽泛地捕获异常以使错误消失，并添加没有人要求的投机性选项。重复代码检测器、复杂度上限和禁止裸 `except` 的规则能抓住其中一部分；其余的要靠评审发现，评审应当读差异本身，而不是只读智能体的摘要。
- 在测试保护下，小步重构。智能体擅长跨多个文件的机械重构，但也会做出看似合理却改变了行为的修改。保障措施与 10.7 相同：先写特征测试，每次提交只做一个重构，每一步之后运行全部测试，并明确指示在重构时不得修改测试。

智能体所读的项目指令（10.2.3 的编码规范、命名约定、检查它们的命令）本身也是必须保持真实的文档；[4.14.14](/4.14.14) 讨论如何编写和维护它们。

## 小结

- 防御性编程不作任何假设：它在模块边界处校验外部数据与参数，以清楚的错误报告错误输入，只把断言用于内部假设，并尽可能使非法状态无法表示。
- 代码是写给人看的。布局应当一致、符合惯例且简洁；采用一种规范（PEP 8、Google 风格指南、安全关键 C 代码的 MISRA），并用格式化工具强制执行其布局部分。
- 名字要有描述性、正确、符合惯用法且得体；避免晦涩、冗长、有误导性和含糊的名字，并遵循语言的大小写约定。
- 自文档化代码使正常路径一目了然，避免深层嵌套，使用小函数、有描述性的类型和具名常量。注释解释为什么而不是怎么做，并记录出人意料之处。
- 代码坏味道预示设计问题；圈复杂度（$V = E - N + 2$ = 判定数 $+1$，至多约为 10）与 ABC 分数量化复杂度；代码检查工具与类型检查器不运行代码就能发现缺陷。
- 重构在不改变行为的前提下改变结构，以测试验证的小步进行；每种坏味道都有标准的重构手法。
- 在类的层次，设计坏味道用设计模式与 SOLID 原则来修复；依赖注入使类既可扩展又可测试，迪米特法则避免消息链。
